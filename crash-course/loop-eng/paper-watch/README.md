# What's New on arXiv — a watch with a memory

**Loop Engineering, Concept 12 — the spine (memory between runs).**

Every day this shows you the newest research papers on a topic you care about —
but **only the ones you haven't seen yet.** How does it skip the ones it already
showed you? It writes them into a file, and reads that file first next time. That
file is the **spine** — the loop's memory.

Nothing to install, no key, no sign-up. Claude fetches the papers from arXiv itself.

## Run it

```bash
git clone https://github.com/panaversity/agentfactory-labs.git
cd agentfactory-labs/crash-course/loop-eng/paper-watch
claude
```

Say **yes** when Claude asks whether you trust this folder. Then ask:

```
show me what's new on arXiv about "LLM agents"
```

You'll see the latest papers, newest first:

```
  📄  FRESH ON ARXIV  ·  "LLM agents"
      first look — here are the latest papers
  ------------------------------------------------------------
   • Adaptive Adversaries: A Multi-Turn Benchmark for LLM Agent Security
     Devina Jain, David Hartmann +1 more   ·   2026-07-20   ·   cs.CR
     arxiv.org/abs/2607.18063
   • Memory-Augmented Planning for Long-Horizon LLM Agents
     Sara Kim, Alex Novak   ·   2026-07-20   ·   cs.AI
     arxiv.org/abs/2607.18044
```

**Watching your own field?** Swap `"LLM agents"` for anything you're studying:

```
"diffusion models"   ·   "reinforcement learning"   ·   "prompt injection"   ·   "retrieval augmented generation"
```

The watch follows one topic at a time — switch topics and it starts fresh on the new one.

## Now feel the spine — this is the whole lesson

**Ask again, right away:**

```
show me what's new on arXiv about "LLM agents"
```

This time it says **"nothing new since last run ✓"**. The loop *remembered* — it
wrote the papers it showed you into `progress.md` and read them back. See for
yourself:

```
cat progress.md
```

**Now delete the memory and ask one more time:**

```
rm progress.md
show me what's new on arXiv about "LLM agents"
```

Every paper comes back as "new." You just made the loop forget everything.
**No spine, no loop** — that one file is what turns separate runs into progress.

## How it fits the loop

This project is **the spine** (Concept 12) paired with **one heartbeat** — and
choosing the right heartbeat matters, so here is the whole story.

**Spine** → `progress.md`: read first, written last. It holds the papers you've
already seen. This is what makes each run show only what's *new*.

### Which heartbeat runs it? (and which NOT)

**Right now, running it by hand, _you_ are the heartbeat** — every time you ask,
you fire one run. That is the best way to *feel* the spine (run → run again →
delete → run). The spine works no matter who fires the beat: you, a timer, or a
schedule.

**To make it automatic, pair it with a scheduled Routine** — Concept 6, "runs
while you sleep." In Claude Code:

```
/schedule every weekday at 9am, run the paper-watch skill and show me what's new
```

arXiv updates about **once a day**, so a daily schedule is exactly the right rhythm.
This is the pairing the project is built for: **spine + scheduled Routine.**

**Not `/loop`, and not `/goal`** — and it's worth knowing why:

| Heartbeat | What it does | Right for paper-watch? |
|---|---|---|
| **Schedule / Routine** (`/schedule`) | runs once a day, even while you sleep | ✅ **yes** — arXiv changes once a day |
| `/loop` (in-session) | fires on a timer while your session is open (e.g. every minute) | ❌ too fast — you'd just get "nothing new" all day |
| `/goal` (run-until-done) | repeats until a condition is true, then **stops** | ❌ a watch never "finishes" — there's no stop line |

So: **by hand while you learn the spine, then a daily Routine to run it for real.**

**Compared to the [Sky Watch](../sky-watch/):** both are daily Routines — but Sky
Watch reprints *today's* asteroids every run (it needs **no** memory), while this
one shows only what's *new since last time* (it **can't work** without the spine).
Same heartbeat, opposite memory need. That contrast is exactly *when* you need a
spine.

> New to the terminal, or want the step-by-step version? See **[START-HERE.md](START-HERE.md)**.
