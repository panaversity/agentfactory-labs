---
name: paper-watch
description: Show the newest arXiv research papers on a topic that the user has NOT seen before, by running this skill's bundled script — never from memory. The script reads progress.md (the spine) first to learn what was already shown, fetches the latest papers from arXiv, prints only the genuinely new ones, and writes progress.md last. Use it whenever the user asks what is new on arXiv, wants new papers or fresh research on a topic, wants a paper feed, or runs a scheduled "what's new since yesterday" job. Only new-since-last-time counts — showing a paper twice defeats the point of a watch.
allowed-tools: Bash, Read
---

# Paper watch

A watch is only useful if it tells you what is **new**. Showing the same paper
again tomorrow is noise. So this skill remembers what it has already shown — in a
file, `progress.md`, the loop's **spine** — and each run reports only papers newer
than that.

The papers are not guessable. arXiv publishes new research every day, and only
arXiv knows today's list. So the papers always come from the bundled script, run
fresh, every time — never from memory.

## Getting today's new papers

Run the script. It reads `progress.md` first, fetches arXiv, prints only what is
new, then updates `progress.md`:

```bash
python3 .claude/skills/paper-watch/scripts/paperwatch.py
```

Pick a topic with `--topic`:

```bash
python3 .claude/skills/paper-watch/scripts/paperwatch.py --topic "diffusion models"
```

For the raw data to reason with (e.g. to write an email or a summary), ask for JSON:

```bash
python3 .claude/skills/paper-watch/scripts/paperwatch.py --json
```

## The spine is the whole point of this project

- The script **reads `progress.md` first** ("what have I already shown?") and
  **writes it last** ("remember what I showed this time"). That file is the memory
  that survives between runs.
- arXiv refreshes about **once a day**, so a **daily schedule** is the natural
  heartbeat: run it each morning and get only that day's new papers. A fast
  in-session loop would just see "nothing new" — the papers only change overnight.
- If the fetch fails, **say so** — never invent papers. A made-up "here's what's
  new" is the one answer a watch must never give.

## "Nothing new since last run" is correct, not broken

If you run it twice close together and the second time says *nothing new*, that is
the spine working: it remembered. To show a beginner **why** the spine matters,
delete it and run again — every paper comes back as new:

```bash
rm progress.md      # erase the memory... now every paper looks new again. No spine, no loop.
```
