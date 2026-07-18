#!/usr/bin/env python3
"""Fetch the live position of the International Space Station and print it.

One run = one honest reading. There is no cache and no fallback: if the API
cannot be reached, this exits non-zero and says so, rather than inventing a
position. A wrong number that looks right is worse than no number.

Usage:
    python3 iss.py            # the display card
    python3 iss.py --json     # raw values, for when you need to compute
"""

import json
import sys
import time
import urllib.request

API = "https://api.wheretheiss.at/v1/satellites/25544"  # 25544 = the ISS
TIMEOUT = 25  # generous: the TLS handshake alone can take >10s on a slow link
TRIES = 3


def fetch():
    """Return the API's JSON, or exit non-zero with a plain-English reason."""
    last = None
    for attempt in range(1, TRIES + 1):
        try:
            with urllib.request.urlopen(API, timeout=TIMEOUT) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001 - any failure is the same to a reader
            last = e
            if attempt < TRIES:
                time.sleep(1)
    print(f"Could not reach the ISS API after {TRIES} tries ({last}).")
    print("Check the connection. Do not guess a position — say this beat failed.")
    sys.exit(1)


def hemi(value, positive, negative):
    return f"{abs(value):.1f}° {positive if value >= 0 else negative}"


def normalize(d):
    """The reading's raw values, keyed the same way for the card and --json."""
    return {
        "latitude": d["latitude"],
        "longitude": d["longitude"],
        "altitude_km": d["altitude"],
        "velocity_kmh": d["velocity"],
        "visibility": d.get("visibility"),
        "timestamp": d["timestamp"],
    }


def card(n):
    """The display card. Fixed width so consecutive beats line up in a loop."""
    clock = time.strftime("%H:%M:%S UTC", time.gmtime(n["timestamp"]))
    lat = hemi(n["latitude"], "N", "S")
    lon = hemi(n["longitude"], "E", "W")
    kmh = f"{n['velocity_kmh']:,.0f} km/h"
    kms = f"{n['velocity_kmh'] / 3600:.2f} km/s"
    lit = "in sunlight" if n["visibility"] == "daylight" else (n["visibility"] if n["visibility"] is not None else "-")

    line = "─" * 58
    return "\n".join(
        [
            "",
            f"  🛰  INTERNATIONAL SPACE STATION            live · {clock}",
            f"  {line}",
            f"     Position    {lat:<12} {lon}",
            f"     Altitude    {n['altitude_km']:.0f} km",
            f"     Speed       {kmh}   ({kms})",
            f"     Sunlight    {lit}",
            f"  {line}",
            "",
        ]
    )


def main():
    n = normalize(fetch())
    if "--json" in sys.argv[1:]:
        print(json.dumps(n, indent=2))
    else:
        print(card(n))


if __name__ == "__main__":
    main()
