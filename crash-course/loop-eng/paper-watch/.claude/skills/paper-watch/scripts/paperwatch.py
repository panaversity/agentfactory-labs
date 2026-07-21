#!/usr/bin/env python3
"""paperwatch.py — a WATCHER with a SPINE (memory between runs).

Every run asks arXiv for the newest papers on your topic, then shows you ONLY the
ones you have not seen before. How does it know which you've seen? It reads a file
first — progress.md, the spine — and writes to it last. That file is the memory.

    python3 paperwatch.py                       # newest papers on the default topic
    python3 paperwatch.py --topic "diffusion"   # pick your own topic
    python3 paperwatch.py --json                # raw data instead of a card
    python3 paperwatch.py --help                # all the options

HOW TO READ THIS FILE (to learn the spine):
    The whole lesson is 3 steps, and you can see them at the bottom, in main():
        1. READ the spine   -> read_spine()
        2. do the work       -> fetch_papers(), then keep only the new ones
        3. WRITE the spine   -> write_spine()
    read_spine() and write_spine() ARE the lesson — they're short, read those.
    fetch_papers() just downloads papers from the internet (it uses XML, which is
    fiddly). You do NOT need to understand it to understand the spine. Treat it as
    a black box: "give it a topic, it returns a list of the newest papers."
"""

import argparse, json, os, re, sys, time
import urllib.parse, urllib.request
import xml.etree.ElementTree as ET

SPINE = "progress.md"          # the memory file — read first, written last
DEFAULT_TOPIC = "LLM agents"
STARTER_TOPICS = ["LLM agents", "diffusion models", "reinforcement learning",
                  "prompt injection", "retrieval augmented generation"]


# ══════════════════════════════════════════════════════════════════════════
#  THE SPINE  —  this is the lesson. Two short functions: read it, write it.
# ══════════════════════════════════════════════════════════════════════════

def read_spine():
    """Read the memory: which papers have we already shown? (empty on the first run)."""
    if not os.path.exists(SPINE):
        return None, {}                     # no file yet -> no memory -> everything is new
    topic = None
    seen = {}                               # {paper_id: title}
    for line in open(SPINE):
        if line.startswith("topic:"):
            topic = line.split(":", 1)[1].strip()
        elif line.startswith("- "):
            parts = line[2:].split(None, 1)   # "- <id>  <title>"  ->  [id, title]
            seen[parts[0]] = parts[1].strip() if len(parts) > 1 else ""
    return topic, seen


def write_spine(topic, seen):
    """Write the memory: save every paper we've shown, so the NEXT run remembers."""
    lines = [
        "# progress.md — the SPINE (this loop's memory)",
        "# The papers below have already been shown to you. paper-watch reads this",
        "# file first, so each run shows only what is NEW. Delete it and every paper",
        '# looks new again — that is "no spine, no loop".',
        "",
        f"topic: {topic}",
        "",
    ]
    for paper_id, title in list(seen.items())[-300:]:   # cap the list so it can't grow forever
        lines.append(f"- {paper_id}  {title[:80]}")
    open(SPINE, "w").write("\n".join(lines) + "\n")


# ══════════════════════════════════════════════════════════════════════════
#  THE BORING PART  —  download the papers from arXiv.  You can SKIP reading
#  this; all you need to know is: fetch_papers("robots") -> list of new papers.
# ══════════════════════════════════════════════════════════════════════════

ARXIV_URL = "https://export.arxiv.org/api/query"   # a public web address — no key, no login
ATOM = "{http://www.w3.org/2005/Atom}"             # an XML label arXiv uses; ignore it


def fetch_papers(topic, how_many=20):
    """Return the newest `how_many` papers on `topic`, or exit saying it failed."""
    query = urllib.parse.urlencode({
        "search_query": f'all:"{topic}"',
        "sortBy": "submittedDate", "sortOrder": "descending",
        "max_results": how_many,
    })
    error = None
    for attempt in range(1, 4):                    # try 3 times, then give up honestly
        try:
            with urllib.request.urlopen(f"{ARXIV_URL}?{query}", timeout=25) as response:
                feed = ET.fromstring(response.read())
            return [_read_one_paper(entry) for entry in feed.findall(f"{ATOM}entry")]
        except Exception as e:
            error = e
            time.sleep(2 * attempt)
    print(f"Could not reach arXiv after 3 tries ({error}).")
    print("arXiv limits rapid requests (about 1 every 3 seconds). If you just ran")
    print("this several times in a row, wait a minute, then try again.")
    print("The watch does not guess — a made-up 'here's what's new' is the one")
    print("answer a watch must never give.")
    sys.exit(1)


def _read_one_paper(entry):
    """Pull the fields we care about out of one XML <entry>."""
    raw_id = entry.findtext(f"{ATOM}id", "")
    paper_id = re.sub(r"v\d+$", "", raw_id.rsplit("/", 1)[-1])   # ".../2607.18063v1" -> "2607.18063"
    authors = [a.findtext(f"{ATOM}name", "") for a in entry.findall(f"{ATOM}author")]
    category = entry.find(f"{ATOM}category")
    return {
        "id": paper_id,
        "title": " ".join(entry.findtext(f"{ATOM}title", "").split()),
        "authors": authors,
        "date": entry.findtext(f"{ATOM}published", "")[:10],
        "category": category.get("term") if category is not None else "",
        "link": f"arxiv.org/abs/{paper_id}",
    }


# ══════════════════════════════════════════════════════════════════════════
#  showing the result on screen
# ══════════════════════════════════════════════════════════════════════════

def show(topic, new_papers, first_run):
    print()
    print(f'  📄  FRESH ON ARXIV  ·  "{topic}"')
    if first_run and not new_papers:
        print(f'      no papers found for "{topic}"')
    elif first_run:
        print("      first look — here are the latest papers")
    elif new_papers:
        print(f"      {len(new_papers)} new since last run")
    else:
        print("      nothing new since last run  ✓")
    print("  " + "-" * 60)

    if not new_papers:
        if first_run:                       # brand-new topic, nothing came back at all
            print(f'   No papers matched "{topic}" — check the spelling, or try a')
            print("   popular topic to start:")
            print("      " + "    ".join(f'"{t}"' for t in STARTER_TOPICS[:4]))
            print()
            return
        print("   You're all caught up.")     # returning visitor -> the spine is working
        print("   That is the spine working — it remembered what it already showed you.")
        print(f"   Try:  rm {SPINE}   and run again. Every paper will look new.")
        print("         (no spine, no loop)")
        print()
        return

    for paper in new_papers:
        authors = ", ".join(paper["authors"][:2])
        if len(paper["authors"]) > 2:
            authors += f" +{len(paper['authors']) - 2} more"
        print(f"   • {paper['title'][:72]}")
        print(f"     {authors}   ·   {paper['date']}   ·   {paper['category']}")
        print(f"     {paper['link']}")
    print("  " + "-" * 60)
    print(f"   saved these to {SPINE}, so the next run remembers them.")
    print()


# ══════════════════════════════════════════════════════════════════════════
#  the loop, one beat:   READ the spine  ->  do the work  ->  WRITE the spine
# ══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="Show the newest arXiv papers on a topic that you haven't seen yet.")
    parser.add_argument("--topic", default=DEFAULT_TOPIC,
                        help='what to watch, e.g. --topic "diffusion models"')
    parser.add_argument("--json", action="store_true",
                        help="print raw data instead of the card")
    args = parser.parse_args()

    # 1. READ THE SPINE — what did earlier runs already show?
    saved_topic, seen = read_spine()
    first_run = saved_topic is None
    if saved_topic is not None and saved_topic != args.topic:
        seen, first_run = {}, True          # switched topic -> this one starts fresh

    # 2. DO THE WORK — get the latest papers, keep only the ones NOT in the memory
    papers = fetch_papers(args.topic)
    new_papers = [p for p in papers if p["id"] not in seen]

    if args.json:
        print(json.dumps({"topic": args.topic, "new": new_papers}, indent=2))
        return

    show(args.topic, new_papers, first_run)

    # 3. WRITE THE SPINE — add the new papers to the memory, so next run continues.
    #    Skip it on a first run that found nothing: a mistyped topic leaves no memory,
    #    so re-running it keeps offering starter topics instead of "nothing new."
    if new_papers or not first_run:
        for paper in new_papers:
            seen[paper["id"]] = paper["title"]
        write_spine(args.topic, seen)


if __name__ == "__main__":
    main()
