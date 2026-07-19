---
name: sky-watch
description: Write a forward-looking asteroid watch — which near-Earth objects pass in the next few days, which is closest, and whether NASA has flagged any as dangerous — by running this skill's bundled script, never from memory. Use it whenever the user asks what asteroids are coming, wants a sky watch or asteroid forecast, asks whether anything is going to hit or come close to Earth, or runs a scheduled job that reports on near-Earth objects. A watch warns before the pass, so always look ahead, never report a pass that has already happened.
allowed-tools: Bash, Read
---

# Sky watch

A watch earns its name by warning you _before_ something happens, not after. So
this skill always looks **ahead** — the next several days of asteroid close
approaches — and never reports a pass that is already in the past. "Yesterday an
asteroid nearly hit us" is a fact with no use in it.

The numbers are not guessable. Asteroid orbits are known, so NASA can say where
the rocks will be — but only NASA can. So the position always comes from the
bundled script, run fresh, every time.

## Getting the forecast

Run the script:

```bash
python3 .claude/skills/sky-watch/scripts/skywatch.py
```

It fetches the next seven days of close approaches and prints a watch card:
what is coming, the single closest pass, and — first, if any — the objects NASA
has flagged as potentially hazardous. The script owns the API, the date window,
and the danger check, so none of that has to be remembered.

For the raw numbers to reason with, ask for JSON:

```bash
python3 .claude/skills/sky-watch/scripts/skywatch.py --json
```

## Writing the watch

Turn the card into **one short, forward-looking paragraph** a person can read
over coffee and know whether to care. The shape:

1. **Lead with danger, or with calm.** If anything is flagged hazardous _and_
   actually close, say so first and plainly. If nothing is a real threat — the
   usual case — open by saying so. Do not bury "all clear" under a list.
2. **Name the closest pass, in Moons.** "23× the Moon's distance" means
   something; "8,918,882 km" does not. The script gives you both — use the Moon.
3. **Say when.** A watch is about the future, so dates matter: "on the 20th",
   "later this week".

**Example — a calm week:**

> Sky watch for the week ahead: nothing to worry about. Forty asteroids pass in
> the next seven days, and the closest, 2019 NG2 on the 20th, stays 23 times
> farther than the Moon. Two are on NASA's "potentially hazardous" list, but both
> pass beyond 170× the Moon — that label is about their orbits, not this trip.
> All clear.

**Example — the rare loud morning:**

> ⚠ Heads up: 2024 XY passes on the 22nd at just 1.8× the Moon's distance and is
> on NASA's hazardous list — the closest approach this month by far. It will miss,
> but it is worth watching. The rest of the week is quiet.

## One nuance to get right

"Potentially hazardous" is a **classification of the object's orbit** (it can
come within ~7.5 million km and is over ~140 m wide), not a claim that _this_
pass is dangerous. An object can carry the flag and still miss by 180× the Moon,
as most do. Always report the flag **and** the actual distance, so the reader
sees the difference. Never turn a routine flagged pass into a scare.

## When the fetch fails

The script exits non-zero and says so. Say the watch could not run this time, in
one line, and stop. Do not fill the sky with a remembered or guessed forecast —
a false "all clear" is the one thing a watch must never say. The next scheduled
run will try again.
