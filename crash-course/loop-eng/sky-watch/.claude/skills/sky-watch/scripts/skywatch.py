#!/usr/bin/env python3
"""skywatch.py — the deterministic fetch. Look AHEAD at asteroids passing Earth.

A watch warns you *before* the pass, not after. So this asks NASA for the next
seven days of close approaches — today included — and returns them sorted by
date, nearest-miss first within each day.

One run = one honest forecast. If NASA cannot be reached it exits non-zero and
says so, rather than inventing a sky. A made-up "all clear" is the one answer a
watch must never give.

Usage:
    python3 skywatch.py            # the watch card, next 7 days
    python3 skywatch.py --json     # raw rows, for computing
    python3 skywatch.py --days 3   # a shorter window

Set NASA_API_KEY for a personal key (free, instant, at api.nasa.gov). Without
it, NASA's shared DEMO_KEY is used — fine to start, but rate-limited, so a burst
of test runs may get throttled.
"""

import json
import os
import sys
import time
import urllib.request
from datetime import date, timedelta

API = "https://api.nasa.gov/neo/rest/v1/feed"
KEY = os.environ.get("NASA_API_KEY", "DEMO_KEY")
TIMEOUT = 25
TRIES = 3
MOON_KM = 384_400  # mean Earth–Moon distance, for the "x the Moon" framing


def fetch(days):
    """Return NASA's feed for [today, today+days], or exit non-zero with a reason."""
    start = date.today()
    end = start + timedelta(days=days - 1)
    url = f"{API}?start_date={start}&end_date={end}&api_key={KEY}"
    last = None
    for attempt in range(1, TRIES + 1):
        try:
            with urllib.request.urlopen(url, timeout=TIMEOUT) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001 — every failure reads the same to a watcher
            last = e
            if attempt < TRIES:
                time.sleep(2)
    print(f"Could not reach NASA's asteroid feed after {TRIES} tries ({last}).")
    print("Do not guess the sky — say the watch failed and try the next run.")
    sys.exit(1)


def rows(feed, days):
    """Flatten the feed into one sorted list of the passes that matter."""
    out = []
    for day_objs in feed.get("near_earth_objects", {}).values():
        for o in day_objs:
            ca = o["close_approach_data"][0]
            km = float(ca["miss_distance"]["kilometers"])
            dia = o["estimated_diameter"]["meters"]
            out.append(
                {
                    "date": ca["close_approach_date"],
                    "name": o["name"].strip("()"),
                    "miss_km": km,
                    "miss_moons": km / MOON_KM,
                    "speed_kmh": float(ca["relative_velocity"]["kilometers_per_hour"]),
                    "size_min_m": dia["estimated_diameter_min"],
                    "size_max_m": dia["estimated_diameter_max"],
                    "hazardous": o["is_potentially_hazardous_asteroid"],
                }
            )
    out.sort(key=lambda r: (r["date"], r["miss_km"]))
    return out


def card(rs, days):
    line = "─" * 62
    hazards = [r for r in rs if r["hazardous"]]
    closest = min(rs, key=lambda r: r["miss_km"]) if rs else None
    head = f"  ☄  SKY WATCH — next {days} days, from {date.today()}"

    body = ["", head, f"  {line}"]
    if not rs:
        body += ["     No catalogued close approaches in the window.", f"  {line}", ""]
        return "\n".join(body)

    if hazards:
        body.append(f"     ⚠  {len(hazards)} flagged POTENTIALLY HAZARDOUS by NASA:")
        for r in hazards:
            body.append(f"        {r['date']}  {r['name']}  —  {r['miss_moons']:.1f}× the Moon")
    else:
        body.append("     ✓  Nothing flagged hazardous in the window.")
    body.append("")
    body.append(f"     Closest pass:  {closest['name']}  on {closest['date']}")
    body.append(f"        {closest['miss_km']:,.0f} km  =  {closest['miss_moons']:.1f}× the Moon")
    body.append(
        f"        ~{closest['size_min_m']:.0f}–{closest['size_max_m']:.0f} m across, "
        f"{closest['speed_kmh']:,.0f} km/h"
    )
    body.append("")
    body.append(f"     {len(rs)} close approaches total in the next {days} days.")
    body += [f"  {line}", ""]
    return "\n".join(body)


def main():
    args = sys.argv[1:]
    days = 7
    if "--days" in args:
        try:
            days = max(1, min(7, int(args[args.index("--days") + 1])))
        except (ValueError, IndexError):
            print("--days needs a number from 1 to 7.")
            sys.exit(1)

    feed = fetch(days)
    if "error" in feed:
        print(f"NASA returned an error: {feed['error']}")
        print("If this is a rate limit, set NASA_API_KEY (free at api.nasa.gov).")
        sys.exit(1)

    rs = rows(feed, days)
    if "--json" in args:
        print(json.dumps(rs, indent=2))
    else:
        print(card(rs, days))


if __name__ == "__main__":
    main()
