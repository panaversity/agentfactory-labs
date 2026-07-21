# {{EMOJI}} {{PROJECT_TITLE}}

Shows you {{ONE_LINER}} — using **{{SOURCE_NAME}}** ({{SOURCE_BLURB}}). No API key,
no sign-up, no install. Teaches **Concept {{CONCEPT_NUMBER}} — {{CONCEPT_NAME}}**.

## Run it

```bash
python3 .claude/skills/{{project-slug}}/scripts/{{scriptname}}.py
```

Or, inside Claude Code, just ask in plain English and the skill runs it for you:

> what's new on {{SOURCE_NAME}} about "<your topic>"

<!-- ── SPINE section — delete this whole block if your project is stateless ── -->
## Feel the spine (30 seconds)

Run it, then run the **exact same command again**. The second time says *"nothing
new"* — the loop remembered. Now erase its memory and run once more:

```bash
rm progress.md
python3 .claude/skills/{{project-slug}}/scripts/{{scriptname}}.py
```

Everything comes back as "new." You just made the loop forget everything. That one
file, `progress.md`, is the **spine** — **no spine, no loop.**

## How it fits the loop

**Spine** → `progress.md`: read first, written last. It remembers what you've
already seen, so each run shows only what's **new**. *(Stateless project? Delete
this bullet and the "Feel the spine" section — see the note in `script.py`.)*

**Heartbeat** → keep the row that matches how often {{SOURCE_NAME}} changes:

| If {{SOURCE_NAME}} changes… | Use | Concept |
|---|---|---|
| once a day (or slower) | `/schedule every weekday at 9am, run the {{project-slug}} skill` | 6 — scheduled Routine |
| every few seconds, while you watch | `/loop` (in-session) | 4 — in-session |
| only when you want a result, then stop | `/goal` (run-until-done) | 5 — conditional |

Most watchers are the **daily schedule**: run it by hand while you learn the spine,
then schedule it when you want it automatic.

> New to the terminal? See **[START-HERE.md](START-HERE.md)** for the step-by-step.
