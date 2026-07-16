---
name: iss-position
description: Fetch and show the live position of the International Space Station by running this skill's bundled script, never from memory, an orbital estimate, or a different API. Use it whenever the user asks where the ISS is, wants to watch or track the space station, asks whether it is over land or sea, or runs a /loop that reports the ISS — including casual phrasings like "show me the location of the ISS", "where is it now", or "is it over the ocean yet". The station moves 7.7 km every second, so any position not fetched just now is already wrong.
allowed-tools: Bash, Read
---

# ISS position

The International Space Station travels at about 7.7 kilometres per second. A reading from ten
seconds ago is already 77 km out of date, and a position recalled from memory is simply fiction —
the station was never going to be where a language model guessed it would be. So there is only one
honest way to answer "where is the ISS?": ask the tracker, right now, every single time.

That is what this skill is for, and it is why the fetching lives in a script rather than in
instructions you have to follow carefully.

## Getting a position

Run the bundled script:

```bash
python3 .claude/skills/iss-position/scripts/iss.py
```

It fetches the live reading and prints a display card. The script owns the URL, the retries, and
the formatting, so none of that has to be remembered or re-derived — and every beat of a loop comes
out looking identical, which is what lets a reader see the numbers moving.

When you need the raw values to calculate with rather than to show — distance travelled, say — ask
for JSON instead:

```bash
python3 .claude/skills/iss-position/scripts/iss.py --json
```

## Showing the result

Print the card exactly as the script produced it. The spacing is deliberate: consecutive readings
line up column-wise, so a reader watching a loop can see the latitude marching down the screen.

Then add **one plain sentence** saying where that actually is on Earth — an ocean, a country, a
landmark someone would recognise. The script supplies coordinates; you supply the meaning. Someone
glancing up mid-conversation should learn "it's over the South Pacific, near New Zealand" without
having to decode `49.2° S 105.8° W` in their head.

**Example:**

```
  🛰  INTERNATIONAL SPACE STATION            live · 17:17:57 UTC
  ──────────────────────────────────────────────────────────
     Position    49.2° S      105.8° W
     Altitude    432 km
     Speed       27,557 km/h   (7.65 km/s)
     Sunlight    in sunlight
  ──────────────────────────────────────────────────────────

Deep in the southern Pacific, roughly halfway between New Zealand and Chile — nothing
below it but open water for thousands of kilometres.
```

## When the fetch fails

The script exits non-zero and prints why. Say the beat failed, in one line, and stop there.

Do not fill the gap. Not with a remembered position, not with an orbital estimate, not with a
different satellite API, not with "it was around here a minute ago". A plausible wrong position is
worse than an honest gap, because the reader has no way to tell it is wrong — and the entire value
of this skill is that every number on screen came from the tracker seconds earlier. Inside a loop a
failed beat costs almost nothing: the next one is a minute away, and it will probably succeed.

## Working out how far it has travelled

Compare against the **first** reading of the loop, not the previous one — "how far has it flown
since we started watching?" is the question people actually mean.

Longitude wraps at 180: 175 East to 175 West is 10 degrees of travel, not 350. If the gap between
two longitudes comes out bigger than 180, subtract it from 360.
