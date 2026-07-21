#!/usr/bin/env python3
"""{{scriptname}}.py — a WATCHER with a SPINE (memory between runs).

Every run asks {{SOURCE_NAME}} for the newest {{THING}} on your topic, then shows
you ONLY the ones you have not seen before. How does it know which you've seen? It
reads a file first — progress.md, the spine — and writes to it last.

    python3 {{scriptname}}.py                     # newest {{THING}} on the default topic
    python3 {{scriptname}}.py --topic "..."       # pick your own topic
    python3 {{scriptname}}.py --json              # raw data instead of a card
    python3 {{scriptname}}.py --help              # all the options

HOW TO READ THIS FILE (to learn the spine):
    The whole lesson is 3 steps, at the bottom, in main():
        1. READ the spine   -> read_spine()
        2. do the work       -> fetch(), then keep only the new ones
        3. WRITE the spine   -> write_spine()
    read_spine() and write_spine() ARE the lesson — they're short, read those.
    fetch() just downloads from the internet; treat it as a black box.

TO ADAPT THIS TEMPLATE you fill in only TWO things, both marked "TODO" below:
    1. SOURCE_URL + the query params   (where to fetch from)
    2. _parse_response()               (turn the reply into a list of items)
Everything else — the spine, the retry, the honest failure, the card — works as-is.
"""

import argparse, json, os, sys, time
import urllib.parse, urllib.request
# import xml.etree.ElementTree as ET   # uncomment if your source returns XML

SPINE = "progress.md"          # the memory file — read first, written last
DEFAULT_TOPIC = "{{DEFAULT_QUERY}}"
STARTER_TOPICS = ["{{DEFAULT_QUERY}}", "...", "..."]   # TODO 3: a few known-good topics
                                                       # to suggest when a search finds nothing


# ══════════════════════════════════════════════════════════════════════════
#  ── SPINE ──  this is the lesson. Two short functions: read it, write it.
#  (Stateless project? Delete this whole block AND the READ/WRITE steps in main.)
# ══════════════════════════════════════════════════════════════════════════

def read_spine():
    """Read the memory: which items have we already shown? (empty on the first run)."""
    if not os.path.exists(SPINE):
        return None, {}                     # no file yet -> no memory -> everything is new
    topic = None
    seen = {}                               # {item_id: title}
    for line in open(SPINE):
        if line.startswith("topic:"):
            topic = line.split(":", 1)[1].strip()
        elif line.startswith("- "):
            parts = line[2:].split(None, 1)   # "- <id>  <title>"  ->  [id, title]
            seen[parts[0]] = parts[1].strip() if len(parts) > 1 else ""
    return topic, seen


def write_spine(topic, seen):
    """Write the memory: save every item we've shown, so the NEXT run remembers."""
    lines = [
        "# progress.md — the SPINE (this loop's memory)",
        "# The items below have already been shown to you. This script reads this",
        "# file first, so each run shows only what is NEW. Delete it and every item",
        '# looks new again — that is "no spine, no loop".',
        "",
        f"topic: {topic}",
        "",
    ]
    for item_id, title in list(seen.items())[-300:]:   # cap the list so it can't grow forever
        lines.append(f"- {item_id}  {title[:80]}")
    open(SPINE, "w").write("\n".join(lines) + "\n")


# ══════════════════════════════════════════════════════════════════════════
#  THE BORING PART  —  download from {{SOURCE_NAME}}.  Fill in the two TODOs;
#  all you need elsewhere is: fetch("robots") -> list of new items.
# ══════════════════════════════════════════════════════════════════════════

SOURCE_URL = "{{SOURCE_URL}}"      # TODO 1: the public endpoint — no key, no login


def fetch(topic, how_many=20):
    """Return the newest `how_many` items on `topic`, or exit saying it failed."""
    # TODO 1 (cont.): set the query params your source expects. Sort by NEWEST.
    query = urllib.parse.urlencode({
        "q": topic,
        "limit": how_many,
        # ... whatever your API needs ...
    })
    error = None
    for attempt in range(1, 4):                    # try 3 times, then give up honestly
        try:
            with urllib.request.urlopen(f"{SOURCE_URL}?{query}", timeout=25) as response:
                raw = response.read()
            return _parse_response(raw)
        except Exception as e:
            error = e
            time.sleep(2 * attempt)
    print(f"Could not reach {{SOURCE_NAME}} after 3 tries ({error}).")
    print("If you just ran this several times in a row, wait a minute, then retry.")
    print("This watch does not guess — a made-up 'here's what's new' is the one")
    print("answer a watch must never give.")
    sys.exit(1)


def _parse_response(raw):
    """TODO 2: turn the raw reply into a list of item dicts, newest first.

    Return a list shaped like:
        [{"id": "unique-stable-id",   # SAME item -> SAME id every run (the spine matches on this)
          "title": "...",
          "subtitle": "authors, or a short line",   # optional
          "date": "2026-07-16",                     # optional
          "link": "example.com/..."},               # optional
         ...]

    If your source returns JSON:
        data = json.loads(raw)
        return [{"id": str(x["id"]), "title": x["name"],
                 "subtitle": x.get("by", ""), "date": x.get("date", ""),
                 "link": x.get("url", "")} for x in data["items"]]

    If your source returns XML (like arXiv), uncomment the ET import at the top:
        feed = ET.fromstring(raw)
        ns = "{http://www.w3.org/2005/Atom}"
        return [{"id": e.findtext(ns + "id"), "title": e.findtext(ns + "title"), ...}
                for e in feed.findall(ns + "entry")]
    """
    raise NotImplementedError("Fill in _parse_response() for your data source.")


# ══════════════════════════════════════════════════════════════════════════
#  showing the result on screen
# ══════════════════════════════════════════════════════════════════════════

def show(topic, new_items, first_run):
    print()
    print(f'  {{EMOJI}}  NEW ON {{SOURCE_NAME}}  ·  "{topic}"')
    if first_run and not new_items:
        print(f'      nothing found for "{topic}"')
    elif first_run:
        print("      first look — here's the latest")
    elif new_items:
        print(f"      {len(new_items)} new since last run")
    else:
        print("      nothing new since last run  ✓")
    print("  " + "-" * 60)

    if not new_items:
        if first_run:                       # nothing came back at all — likely a mistyped topic
            print(f'   Nothing matched "{topic}" — check the spelling, or try one')
            print("   of these to start:")
            print("      " + "    ".join(f'"{t}"' for t in STARTER_TOPICS[:4]))
            print()
            return
        print("   You're all caught up.")     # returning visitor -> the spine is working
        print("   That is the spine working — it remembered what it already showed you.")
        print(f"   Try:  rm {SPINE}   and run again. Every item will look new.")
        print("         (no spine, no loop)")
        print()
        return

    for item in new_items:
        print(f"   • {item['title'][:72]}")
        if item.get("subtitle") or item.get("date"):
            print(f"     {item.get('subtitle', '')}   ·   {item.get('date', '')}")
        if item.get("link"):
            print(f"     {item['link']}")
    print("  " + "-" * 60)
    print(f"   saved these to {SPINE}, so the next run remembers them.")
    print()


# ══════════════════════════════════════════════════════════════════════════
#  the loop, one beat:   READ the spine  ->  do the work  ->  WRITE the spine
# ══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Show the newest {{THING}} on a topic that you haven't seen yet.")
    parser.add_argument("--topic", default=DEFAULT_TOPIC,
                        help='what to watch, e.g. --topic "..."')
    parser.add_argument("--json", action="store_true",
                        help="print raw data instead of the card")
    args = parser.parse_args()

    # 1. READ THE SPINE — what did earlier runs already show?
    saved_topic, seen = read_spine()
    first_run = saved_topic is None
    if saved_topic is not None and saved_topic != args.topic:
        seen, first_run = {}, True          # switched topic -> this one starts fresh

    # 2. DO THE WORK — get the latest, keep only the ones NOT in the memory
    items = fetch(args.topic)
    new_items = [it for it in items if it["id"] not in seen]

    if args.json:
        print(json.dumps({"topic": args.topic, "new": new_items}, indent=2))
        return

    show(args.topic, new_items, first_run)

    # 3. WRITE THE SPINE — add the new items to the memory, so next run continues.
    #    Skip it on a first run that found nothing: a mistyped topic leaves no memory,
    #    so re-running it keeps offering starter topics instead of "nothing new."
    if new_items or not first_run:
        for item in new_items:
            seen[item["id"]] = item["title"]
        write_spine(args.topic, seen)


if __name__ == "__main__":
    main()
