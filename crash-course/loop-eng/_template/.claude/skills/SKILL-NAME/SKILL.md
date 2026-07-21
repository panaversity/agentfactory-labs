---
name: {{project-slug}}
description: Show the newest {{THING}} on a topic that the user has NOT seen before, by running this skill's bundled script — never from memory. The script reads progress.md (the spine) first to learn what was already shown, fetches the latest from {{SOURCE_NAME}}, prints only the genuinely new items, and writes progress.md last. Use it whenever the user asks what's new on {{SOURCE_NAME}}, wants fresh {{THING}} on a topic, wants a feed, or runs a scheduled "what's new since yesterday" job.
allowed-tools: Bash, Read
---

# {{PROJECT_TITLE}}

When the user asks about new {{THING}}, **run the bundled script**. Do NOT answer
from memory, and NEVER invent {{THING}} — the script owns the live data.

## Run it

```bash
python3 .claude/skills/{{project-slug}}/scripts/{{scriptname}}.py --topic "<their topic>"
```

Add `--json` if you want to reformat the results yourself (for example, group them
by theme before showing the user). Show the script's output. If it printed an
honest failure, relay that — do not fill the gap with guesses.

<!-- ── SPINE — delete this section if your project is stateless ── -->
## The spine (why this works)

The script keeps a memory file, `progress.md`. It **reads it first** to see what it
already showed, and **writes it last** with whatever was new. That's what makes each
run show only what's *new*. Never edit or delete `progress.md` yourself — the script
manages it. (If the user wants to "start fresh," they can delete it.)

## Heartbeat

{{SOURCE_NAME}} updates about once a day, so the natural way to run this is a
**daily schedule**. Offer to set it up:

```
/schedule every weekday at 9am, run the {{project-slug}} skill and show me what's new
```

<!-- If your source instead changes every few seconds, this is an in-session /loop
     project (Concept 4), not a schedule. See the heartbeat table in README.md. -->
