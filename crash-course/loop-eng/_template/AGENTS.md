# {{PROJECT_TITLE}}

This project has one job: show {{ONE_LINER}}.

**Any question about new {{THING}} — the latest on a topic, a {{THING}} feed — is
answered by running this project's script, never from memory:**

    python3 .claude/skills/{{project-slug}}/scripts/{{scriptname}}.py --topic "<their topic>"

(In Claude Code this runs automatically through the `{{project-slug}}` skill; any
other agent should run the script directly.) The script owns the {{SOURCE_NAME}}
fetch and, most importantly, the **spine** (`progress.md`): it reads the memory
first to learn what was already shown, and writes it last.

<!-- ── SPINE paragraph — delete this if your project is stateless (no memory) ── -->
The one thing to hold onto: this loop has a **memory**. `progress.md` is the spine.
Reading it first is what lets each run show only what is **new** instead of
repeating the last list. Delete `progress.md` and the loop forgets everything —
every item looks new again. **No spine, no loop.**

If the fetch fails, say so — never invent {{THING}}. A false "here's what's new" is
the one answer this project must never give.
