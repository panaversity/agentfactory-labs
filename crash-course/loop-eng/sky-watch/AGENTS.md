# The Sky Watch

This project has one job: every day, before anything happens, say what asteroids
are coming toward Earth and whether any of them are worth worrying about.

**Any question about near-Earth asteroids — what is coming, what is closest, what
is dangerous — is answered by running this project's script, never from memory:**

    python3 .claude/skills/sky-watch/scripts/skywatch.py

(In Claude Code this runs automatically through the `sky-watch` skill; any other
agent should run the script directly.) The script owns the data source, the
seven-day look-ahead, and the danger rule.

The one thing to hold onto: a watch looks **forward**. Reporting a pass that has
already happened is useless. And if the fetch fails, say so — never invent an
"all clear," because a false one is the only answer a watch must never give.
