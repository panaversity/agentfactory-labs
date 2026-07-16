# Watching the ISS

This project has one job: watch the International Space Station, live, while the session is open.

**Any question about where the ISS is — its position, what it is over, how far it has flown — is
answered by the `iss-position` skill, never from memory.** The skill owns the API, the display, and
the rules; it loads itself when the question comes up, so nothing about it needs repeating here.

The one thing worth stating up front, because it is the reason the skill exists: the station moves
7.7 kilometres every second. A position recalled rather than fetched is not a rough answer, it is a
wrong one. If the fetch fails, say so — never fill the gap with a guess.
