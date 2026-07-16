# Watch the Space Station

**Loop Engineering, Concept 4 — in-session loops (repeat while you watch).**

A loop that fires on a timer while your session is open. Here it watches the real International
Space Station and tells you where it is, once a minute, without you asking again.

Nothing to install. Claude fetches the position itself.

## Run it

```bash
git clone https://github.com/panaversity/agentfactory-labs.git
cd agentfactory-labs/crash-course/loop-eng/iss-loop
claude
```

Say **yes** when Claude asks whether you trust this folder. Then type one sentence:

```
/loop show me the location of the ISS every minute
```

That is the last thing you type. A new position arrives every minute:

```
  🛰  INTERNATIONAL SPACE STATION            live · 17:17:57 UTC
  ──────────────────────────────────────────────────────────
     Position    49.2° S      105.8° W
     Altitude    432 km
     Speed       27,557 km/h   (7.65 km/s)
     Sunlight    in sunlight
  ──────────────────────────────────────────────────────────

Deep in the southern Pacific, roughly halfway between New Zealand and Chile.
```

Press **Esc** when you have seen enough.

> ⚠️ **Getting a permission prompt every minute?** You skipped the trust dialog. An untrusted folder
> ignores `.claude/settings.json` completely, even though the file is sitting right there. Quit, run
> `claude` here again, and say yes.

## More to try

```
/loop 1m show me where the ISS is and what country or ocean it is flying over
```

```
/loop 1m track the ISS and shout ARRIVED when it has travelled 20 degrees from where it started
```

The second one has a finish line. Expect 4 to 9 minutes: the ISS covers a steady ~4° of arc per
minute, but how much _longitude_ that buys depends on where it is.

## Why one sentence is enough

The folder carries the detail so your prompt does not have to:

| File                           | Job                                                             |
| ------------------------------ | --------------------------------------------------------------- |
| `.claude/settings.json`        | Three narrow rules, pre-granted, so the loop never stops to ask |
| `.claude/skills/iss-position/` | Owns the API, the display, and the never-guess rule             |
| `CLAUDE.md`                    | Points at the skill                                             |

## The one thing to notice

Close the terminal. The watching dies with it.

An in-session loop cannot outlive its session. It is a kitchen timer: it only rings while you are in
the kitchen. Claude Code says as much when it schedules the job — _"Session-only (not written to
disk, dies when Claude exits)."_

So how would you watch the ISS overnight, while you sleep? That question is the door to the next
heartbeat.
