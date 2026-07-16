# In-Session Loop — Watch the Space Station

**Lesson:** Loop Engineering, Part 2 → Concept 4, _In-session loops (repeat while you watch)._

A loop that fires on a timer **while your session is open**. Here it watches the real International
Space Station fly around the Earth and tells you where it is, once a minute, without you asking
again.

There is no code to run and nothing to install — Claude fetches the position itself. What you
download is the _setup_, and it is what lets your prompts stay short:

- `.claude/settings.json` — one permission, pre-granted, so the loop never stops to ask.
- `CLAUDE.md` — which API to call, and how to report a position.

---

## Before you start

- **Claude Code**, and an internet connection. That is all.
- The API is free and needs no key: `https://api.wheretheiss.at/v1/satellites/25544` (25544 = the ISS).

---

## Run it

### 1. Open it in Claude Code

Download the project and unzip it. Then start Claude Code **from inside that folder**:

```sh
cd iss-loop      # the folder you just unzipped
claude
```

Claude Code reads its setup from whatever folder you start it in. That is the whole reason to `cd`
here first: this is where it picks up the pre-granted permission and the `CLAUDE.md`. Start it
somewhere else and your prompts have to carry all that detail themselves.

### 2. Say yes once, when it asks about the folder

Claude asks permission before fetching a URL. That is fine when you are typing, but **a loop cannot
stop to ask.** It fires while you are looking away, so a prompt on every beat would destroy the very
thing you are here to see.

So the answers already ship with the project, in `.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Skill(iss-position)",
      "Bash(python3 .claude/skills/iss-position/scripts/iss.py *)",
      "WebFetch(domain:api.wheretheiss.at)"
    ]
  }
}
```

Three narrow rules: use the ISS skill, run that one script, reach that one domain. Nothing else on
your machine, and nothing else on the internet.

The first time you open this folder, Claude asks once whether you **trust it** — the gate that stops
a downloaded project from quietly granting itself permissions. Say yes and the rule above goes live.
That is the only prompt you should see all demo.

> Run `/permissions` any time to see the rule sitting there.

> ⚠️ **If a permission prompt appears on every beat, you skipped the trust dialog.** An untrusted
> folder ignores `.claude/settings.json` completely — the file sits right there looking correct, and
> Claude Code quietly acts as if it were empty. Quit, run `claude` here again, and say yes. This is
> the one way this demo breaks.

### 3. Ask for what you want

Here is the good part. You do not write a specification. You say it the way you would say it to a
person:

```
/loop show me the location of the ISS every minute
```

Hit enter, and that is the last thing you type. Two things make a sentence that short work:

- `/loop` reads **"every minute"** as the heartbeat.
- `CLAUDE.md` in this folder already tells Claude which API to call and how to report it, so the
  prompt does not have to.

That is the habit worth stealing: **keep the detail in the project, keep the prompt human.**

### More starter prompts

That first one reports, and reports, forever, until you stop it. These two do a little more — still
one plain sentence each.

```
/loop 1m show me where the ISS is and what country or ocean it is flying over
```

Geography instead of numbers. Better in front of a room. (`1m` up front is just "every minute" said
explicitly. Use this form when you want the interval pinned rather than inferred.)

```
/loop 1m track the ISS and shout ARRIVED when it has travelled 20 degrees from where it started
```

Now it has a **finish line** — "watch this until it is done", the classic in-session job. Expect 4
to 9 minutes: the ISS covers a steady ~4° of arc per minute, but how much _longitude_ that buys
depends on where it is (about 2°/min near the equator, nearer 6°/min at its highest latitude).

### 4. Watch

Claude confirms the heartbeat once — _"Scheduled recurring job (Every minute)"_ — and then just
starts reporting. Talk to someone; it keeps going without you:

```
The ISS is at 17.3° South, 159.6° East — out over the South Pacific, roughly
northeast of New Caledonia and a long way from any land.

...a minute later...

The ISS is at 11.9° South, 155.4° East — still the South Pacific, now closer to
the Solomon Islands.
```

That is the whole show: a new position, once a minute, and you never touched the keyboard.

### 5. Stop it

Press **`Esc`** when you have seen enough — or when it shouts ARRIVED, if you gave it a finish line.
That is the whole life of an in-session loop: _fire, fire, fire, seen enough, stop._

> **Two things that will bite you.** Keep the terminal open — closing it stops `/loop`. And `1m` is
> the smallest honest step: the scheduler has one-minute granularity, so seconds round up.

---

## The one thing to notice

You do not have to take this from us. Look at what Claude Code itself says when it schedules the
job:

> Scheduled recurring job (Every minute). **Session-only (not written to disk, dies when Claude
> exits).** … Runs until you close this session · For durable cloud-based loops, use `/schedule`

That is the concept, printed by the tool. An in-session loop **cannot outlive its session** — it is
a kitchen timer, and it only rings while you are in the kitchen.

Run the tracking prompt and you see the other half of it. To say "travelled 20 degrees" at all, the
loop has to remember where it started, beat after beat — and it does, in the **session**, not on
disk. Nothing is ever written down. Close the terminal and the launch point goes with it.

So: how would you watch the ISS overnight, while you sleep? That question is the door to the next
heartbeat.
