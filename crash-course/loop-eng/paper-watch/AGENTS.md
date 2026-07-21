# Paper Watch

This project has one job: show the newest arXiv papers on the user's topic that
they have **not already seen**.

**Any question about new papers — what's new on arXiv, the latest research on a
topic, a paper feed — is answered by running this project's script, never from
memory:**

    python3 .claude/skills/paper-watch/scripts/paperwatch.py --topic "<their topic>"

(In Claude Code this runs automatically through the `paper-watch` skill; any other
agent should run the script directly.) The script owns the arXiv fetch, the topic,
and — most importantly — the **spine**: it reads `progress.md` first to learn what
was already shown, and writes it last.

The one thing to hold onto: this loop has a **memory**. `progress.md` is the spine.
Reading it first is what lets each run show only what is **new** instead of
repeating yesterday's list. Delete `progress.md` and the loop forgets everything —
every paper looks new again. **No spine, no loop.**

If the fetch fails, say so — never invent papers. A false "here's what's new" is
the one answer a watch must never give.
