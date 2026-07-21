# Watching the ISS

This project has one job: watch the International Space Station, live, while the
session is open.

**Any question about where the ISS is — its position, what it is over, how far it
has flown — is answered by running this project's script, never from memory:**

    python3 .claude/skills/iss-position/scripts/iss.py

(In Claude Code this runs automatically through the `iss-position` skill; any other
agent should run the script directly.) The script owns the API, the display, and
the rules.

The one thing worth stating up front, because it is the reason the script exists:
the station moves 7.7 kilometres every second. A position recalled rather than
fetched is not a rough answer, it is a wrong one. If the fetch fails, say so —
never fill the gap with a guess.
