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
    python3 skywatch.py --html     # a self-contained HTML card (for an email body)
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
    window = "today" if days == 1 else f"next {days} days"
    head = f"  ☄  SKY WATCH — {window}, {date.today()}"

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
    span = "today" if days == 1 else f"the next {days} days"
    body.append(f"     {len(rs)} close approaches {span}.")
    body += [f"  {line}", ""]
    return "\n".join(body)


def _esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def html_card(rs, days):
    """A self-contained HTML watch card — inline styles only, safe as an email body.

    Each pass is a *proximity* bar: the closer the asteroid, the fuller and hotter
    the bar, so the one worth caring about is the one that stands out. The scale is
    logarithmic (passes run from ~10x to ~200x the Moon, and a linear bar would
    flatten them all), and rows are sorted closest-first so the nearest pass leads.
    """
    import math

    today = date.today()
    win = "Today" if days == 1 else f"Next {days} days"
    hazards = [r for r in rs if r["hazardous"]]
    danger = bool(hazards)
    ordered = sorted(rs, key=lambda r: r["miss_km"])  # closest first

    # Proximity on a log scale: 1x the Moon => full bar, 300x => empty.
    LO, HI = 1.0, 300.0
    lo, hi = math.log10(LO), math.log10(HI)

    def band(r):
        m = r["miss_moons"]
        if r["hazardous"] and m < 20:
            return "#e0533d"  # flagged AND genuinely close — the real red
        if m < 10:
            return "#e0863d"  # very close
        if m < 40:
            return "#d5b53a"  # closeish
        return "#3a7bd5"      # comfortably far — the usual

    def bar(r):
        frac = (hi - math.log10(max(r["miss_moons"], LO))) / (hi - lo)  # 1=close, 0=far
        pct = max(3.0, min(100.0, frac * 100.0))
        return (
            '<div style="background:#11151c;border-radius:5px;height:22px;margin:4px 0;'
            'overflow:hidden;">'
            f'<div style="height:100%;width:{pct:.1f}%;background:{band(r)};'
            'opacity:.9;border-radius:5px;"></div></div>'
        )

    rows_html = []
    for r in ordered[: min(len(ordered), 12)]:
        flag = (
            ' <span style="color:#e0533d;font-weight:600;">⚠ hazardous</span>'
            if r["hazardous"]
            else ""
        )
        rows_html.append(
            '<tr><td style="padding:8px 10px 8px 0;vertical-align:top;white-space:nowrap;'
            f'color:#c7cede;font-size:13px;">{_esc(r["date"])}<br>'
            f'<span style="color:#8a94a6;">{_esc(r["name"])}</span>{flag}</td>'
            f'<td style="padding:8px 0;width:60%;">{bar(r)}'
            '<div style="color:#8a94a6;font-size:12px;margin-top:2px;">'
            f'{r["miss_moons"]:.1f}× the Moon · ~{r["size_min_m"]:.0f}–{r["size_max_m"]:.0f} m'
            "</div></td></tr>"
        )

    banner = (
        f'<div style="background:#3a1512;border:1px solid #e0533d;color:#ffb3a6;'
        f'padding:10px 14px;border-radius:8px;font-size:14px;">⚠ {len(hazards)} object'
        f'{"s" if len(hazards) != 1 else ""} on NASA\'s potentially-hazardous list this '
        "week. Check the distances below — the label is about their orbits, not this pass.</div>"
        if danger
        else '<div style="background:#0f2417;border:1px solid #2e7d52;color:#8fe0b0;'
        'padding:10px 14px;border-radius:8px;font-size:14px;">✓ All clear — nothing '
        "flagged hazardous in the window.</div>"
    )

    return f"""<!doctype html><html><body style="margin:0;background:#0a0d12;">
<div style="max-width:600px;margin:0 auto;padding:24px;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#e7ecf5;">
  <div style="font-size:20px;font-weight:700;letter-spacing:.5px;">☄ SKY WATCH</div>
  <div style="color:#8a94a6;font-size:13px;margin:2px 0 16px;">{win} · {today}</div>
  {banner}
  <div style="display:flex;justify-content:space-between;color:#8a94a6;font-size:11px;margin:14px 0 2px;">
    <span>◀ closer (a fuller, hotter bar)</span><span>farther ▶</span>
  </div>
  <table style="width:100%;border-collapse:collapse;">{"".join(rows_html)}</table>
  <div style="margin-top:14px;color:#8a94a6;font-size:12px;">
    Sorted closest first. Bar length is proximity, log-scaled. {len(rs)} close approaches {"today" if days==1 else f"in the next {days} days"}.
  </div>
</div></body></html>"""


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
    elif "--html" in args:
        print(html_card(rs, days))
    else:
        print(card(rs, days))


if __name__ == "__main__":
    main()
