# {{EMOJI}} {{PROJECT_TITLE}} — Start Here (Beginner Guide)

This project checks **{{SOURCE_NAME}}** ({{SOURCE_BLURB}}) and shows you {{ONE_LINER}}
— but only the ones you haven't seen before. Run it whenever you like and you stay
current in a few seconds.

The magic is a **memory file**. This guide walks you through feeling it work. Do
every step; the important one is Step 4.

---

## What you need

- **A terminal** (the black window where you type commands).
- **Python 3** — check by typing `python3 --version`. A number means you're good.
- **Claude Code** — the tool you're reading this in.
- **No API key.** {{SOURCE_NAME}} is free and open. That's it.

---

## Step 1 — get it, and run it once

```bash
git clone https://github.com/panaversity/agentfactory-labs.git
cd agentfactory-labs/crash-course/loop-eng/{{project-slug}}
python3 .claude/skills/{{project-slug}}/scripts/{{scriptname}}.py
```

**What you should see:** a card of the newest {{THING}} on the default topic,
newest first.

---

## Step 2 — run the exact same command AGAIN

```bash
python3 .claude/skills/{{project-slug}}/scripts/{{scriptname}}.py
```

**What you should see:** `nothing new since last run ✓`. Nothing new appeared in
those few seconds — **and the watch remembered what it already showed you.**

---

## Step 3 — look at the memory

```bash
cat progress.md
```

**What you should see:** a list of the {{THING}} it has shown you. This file is the
**spine**. The script reads it first every run — that's how it knows what's new.

---

## Step 4 — the aha: erase the memory

```bash
rm progress.md
python3 .claude/skills/{{project-slug}}/scripts/{{scriptname}}.py
```

**What you should see:** every item is "new" again. You deleted the memory, so the
watch is a stranger who has never seen any of them. This is the whole lesson:
**no spine, no loop.** The file is what turned "runs" into "progress."

---

## Step 5 — pick your own topic

```bash
python3 .claude/skills/{{project-slug}}/scripts/{{scriptname}}.py --topic "<your topic>"
```

Try whatever you're following — the watch tracks it separately.

---

## Step 6 — make it a habit (the heartbeat)

{{SOURCE_NAME}} updates about once a day, so a **daily** run is perfect. Open Claude
Code here and say:

```
/schedule every weekday at 9am, run the {{project-slug}} skill and show me what's new
```

Now every morning it shows only the **new** {{THING}} — because the spine remembers
the ones from before. That is a real loop: a heartbeat that fires it, and a spine
that remembers between runs.

---

## If something looks off

| What you see | What it means | Fix |
|---|---|---|
| `Could not reach {{SOURCE_NAME}}` | you ran it too many times too fast, or the network hiccuped | wait a minute, then run again. It never invents data. |
| `nothing new` on the very first run | you have an old `progress.md` from before | `rm progress.md` and run again |
| a permission prompt every run | you're in Claude Code and skipped the trust dialog | restart `claude` here and say **yes** to trust |

> **Teachers:** many public APIs rate-limit rapid requests. If a whole class runs
> this at the same second on the same Wi-Fi, some may get `Could not reach…`. Easy
> fixes: give each student a **different `--topic`**, don't all hit Enter together,
> and leave a few seconds between the run / run-again / delete / run-again steps.
