# 📄 Paper Watch — Start Here (Beginner Guide)

This project checks **arXiv** (a free, open library of research papers) and tells
you which **new** papers came out on *your* topic — but only the ones you haven't
seen before. Run it each morning and you stay current in your field in 10 seconds.

The magic is a **memory file**. This guide walks you through feeling it work. Do
every step; the important one is Step 4.

---

## What you need

- **A terminal** (the black window where you type commands).
- **Python 3** — check by typing `python3 --version`. A number means you're good.
- **Claude Code** — the tool you're reading this in.
- **No API key.** arXiv is free and open. That's it.

---

## Step 1 — get it, and run it once

```bash
git clone https://github.com/panaversity/agentfactory-labs.git
cd agentfactory-labs/crash-course/loop-eng/paper-watch
python3 .claude/skills/paper-watch/scripts/paperwatch.py
```

**What you should see:** a card of the newest papers on "LLM agents," newest
first — each with its title, authors, date, and a link.

---

## Step 2 — run the exact same command AGAIN

```bash
python3 .claude/skills/paper-watch/scripts/paperwatch.py
```

**What you should see:** `nothing new since last run ✓`. No new paper came out in
those few seconds — **and the watch remembered what it already showed you.**

---

## Step 3 — look at the memory

```bash
cat progress.md
```

**What you should see:** a list of the papers it has shown you. This file is the
**spine**. The script reads it first every run — that's how it knows what's new.

---

## Step 4 — the aha: erase the memory

```bash
rm progress.md
python3 .claude/skills/paper-watch/scripts/paperwatch.py
```

**What you should see:** every paper is "new" again. You deleted the memory, so
the watch is a stranger who has never seen any of them. This is the whole lesson:
**no spine, no loop.** The file is what turned "runs" into "progress."

---

## Step 5 — pick your own topic

```bash
python3 .claude/skills/paper-watch/scripts/paperwatch.py --topic "diffusion models"
```

**Starter topics** if you're not sure where to begin:
`"LLM agents"` · `"diffusion models"` · `"reinforcement learning"` ·
`"prompt injection"` · `"retrieval augmented generation"` — or whatever you're
studying. (Type a topic with no papers and the watch tells you, then suggests these
— it never makes results up.)

---

## Step 6 — make it a daily habit (the heartbeat)

arXiv updates about once a day, so a **daily** run is perfect. Open Claude Code
here and say:

```
/schedule every weekday at 9am, run the paper-watch skill and show me what's new
```

Now every morning it shows only the **new** papers — because the spine remembers
all the ones from before. That is a real loop: a heartbeat that fires it, and a
spine that remembers between runs.

---

## If something looks off

| What you see | What it means | Fix |
|---|---|---|
| `Could not reach arXiv` | you ran it too many times too fast — arXiv limits rapid requests (about 1 every 3 seconds) | wait a minute, then run again. It never invents papers. |
| `nothing new` on the very first run | you have an old `progress.md` from before | `rm progress.md` and run again |
| a permission prompt every run | you're in Claude Code and skipped the trust dialog | restart `claude` here and say **yes** to trust |

> **Teachers, one thing to know:** arXiv allows about **1 request every 3 seconds
> per internet connection**. If a whole class runs this at the exact same second on
> the same Wi-Fi, some will get "Could not reach arXiv." Easy fixes: give each
> student a **different `--topic`**, don't all hit Enter together, and leave a few
> seconds between the "run it / run again / delete / run again" steps. Run at home
> or on a daily schedule and it never happens — that's the natural way to use it.
