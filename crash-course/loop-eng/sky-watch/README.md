# The Sky Watch — a loop that runs while you sleep

**Loop Engineering, Concept 6 — unattended schedules.**

Every morning before you wake, a machine that isn't yours checks the sky and
leaves you a note: which asteroids are coming toward Earth in the next week, and
whether any of them are worth worrying about.

You start it once. After that it runs on a clock, with your laptop shut, whether
or not anything is happening up there.

## How this differs from the other three

The [ISS project](../iss-loop/) runs on **your** laptop and dies when you close
the terminal. This one runs on a schedule, on someone else's machine, and keeps
going while you sleep. That is the whole concept, in one contrast:

|                      | You start it  | It stops when                        |
| -------------------- | ------------- | ------------------------------------ |
| In-session (`/loop`) | you type      | you close the terminal               |
| **Scheduled (this)** | **the clock** | **you cancel it — never on its own** |

And unlike the [Doorbell](../doorbell/), which reacts _after_ a pull request
happens, this looks **forward**: it is midnight, here is the sky for the days
ahead. An event is a reflex. A schedule is a forecast.

## See it work right now

No schedule needed to try it. The forecast is just a script:

```bash
python3 .claude/skills/sky-watch/scripts/skywatch.py
```

```
  ☄  SKY WATCH — next 7 days, from 2026-07-19
  ──────────────────────────────────────────────────────────────
     ✓  Nothing flagged hazardous in the window.

     Closest pass:  2019 NG2  on 2026-07-20
        8,918,882 km  =  23.2× the Moon
        ~40–90 m across, 49,775 km/h

     40 close approaches total in the next 7 days.
  ──────────────────────────────────────────────────────────────
```

Now make it a loop.

## Run it

### 1. Open it in Claude Code

```bash
git clone https://github.com/panaversity/agentfactory-labs.git
cd agentfactory-labs/crash-course/loop-eng/sky-watch
claude
```

Say **yes** when Claude asks whether you trust the folder — that switches on the
pre-granted permission so the watch never stops to ask. Then try it once by hand:

```
what asteroids are coming this week?
```

It runs the `sky-watch` skill, calls NASA, and writes you a forward-looking
watch — one plain paragraph, danger first or calm first. Prove it works before
you schedule it.

### 2. Turn it into a schedule

Now the heartbeat. In Claude Code:

```
/schedule every day at midnight, run the sky-watch skill and write me the forecast
```

That creates a **cloud Routine** — it runs on Anthropic's servers, so it fires
at midnight whether your laptop is open, asleep, or in a bag. Once a day is well
under the daily run cap.

### 3. Prove it fast, then trust it overnight

A schedule is slow to prove — you cannot watch midnight arrive. So do not trust
it overnight until you have watched it fire once, fast:

1. Fire a one-off now to rehearse: `/schedule in 2 minutes, run the sky-watch skill`.
   A one-off does not count against your daily cap. Watch it run.
2. When that looks right, leave the midnight schedule on and go to bed.
3. In the morning, the watch is waiting.

That ladder — **prove it hourly and watched before you trust it nightly and
unattended** — is the rule from Part 6 of the course, made physical.

## Getting it by email (so you wake up to it)

A watch you have to open a browser to read is only half a watch. The real thing
lands in your inbox before you are awake. A Routine does this through a
**connector** — not a script with an email password (that could never live in a
public repo), but a channel you attach to the Routine on the web. The credentials
stay in your Claude account; the repo stays clean.

The mechanism, in four steps:

1. **Connect a channel** at [`claude.ai/customize/connectors`](https://claude.ai/customize/connectors) — Gmail, or Slack.
2. **Open your Routine** at [`claude.ai/code/routines`](https://claude.ai/code/routines). (You can create a schedule with `/schedule` in the CLI, but connectors are attached on the web — the CLI cannot do it.)
3. **Attach the connector** to this Routine, and only this one. A connector is a permission: with no email connector attached, the Routine could not email you even if the prompt asked.
4. **Add one line to the prompt:** _"…then email me the forecast at you@example.com, subject 'Sky Watch'."_

Fire a one-off to test (`/schedule in 2 minutes, run the sky-watch skill and email me the result`) and check that it arrives.

> **One honest limit.** The built-in **Gmail** connector can _draft_ but not
> _send_ — so with Gmail, each morning's watch lands in your **Drafts** folder,
> not your inbox. That is still delivery, just one click short. For a message that
> truly arrives on its own, use **Slack** (it delivers), or an email connector
> that supports sending. Check what your chosen connector can actually do before
> you rely on it — a Routine can only use the tools its connector gives it.

## What "all clear" means, and why it is the point

Most mornings, the watch will say some version of "nothing dangerous, nearest
pass is 20× the Moon, all clear." **That is not the loop failing — that is the
loop working.** A night watch earns its keep by being quiet on the quiet days and
loud on the one day it matters. An event-driven loop would say nothing at all on
a calm day. A schedule reports anyway — that is what makes it a _watch_.

When something genuinely close does appear, the same loop leads with it:

> ⚠ Heads up: 2024 XY passes on the 22nd at 1.8× the Moon and is on NASA's
> hazardous list — the closest this month. It will miss, but worth watching.

## The one nuance NASA data will trip you on

Some asteroids carry a **"potentially hazardous"** flag and still miss by 180×
the Moon. That flag describes the object's _orbit_ (it can come within ~7.5
million km and is over ~140 m wide), not this particular pass. The watch always
shows the flag **and** the real distance, so you can see the difference. Do not
let a routine flagged pass become a false alarm.

## Rate limits

The script uses NASA's shared `DEMO_KEY` by default — fine to start, but rate-
limited, so a burst of test runs may get throttled. Grab a free personal key at
[api.nasa.gov](https://api.nasa.gov) (instant, just an email) and set it:

```bash
export NASA_API_KEY=your-key-here
```

## What it ships

| File                                           | Job                                                                   |
| ---------------------------------------------- | --------------------------------------------------------------------- |
| `.claude/skills/sky-watch/`                    | Owns the data, the 7-day look-ahead, and the danger rule              |
| `.claude/skills/sky-watch/scripts/skywatch.py` | Fetches NASA; exits non-zero rather than inventing a sky              |
| `.claude/settings.json`                        | Three narrow pre-granted rules: the skill, the script, `api.nasa.gov` |
| `CLAUDE.md`                                    | Points at the skill                                                   |
