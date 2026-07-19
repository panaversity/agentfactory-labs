# 🔭 Sky Watch — Start Here (Beginner Guide)

This project checks the sky for asteroids coming near Earth and tells you, in
plain English, whether anything is worth worrying about. Most days the answer is
**"all clear."** That's the point — a good watch is quiet on quiet days and loud
on the one day it matters.

This guide takes you from zero to a watch that emails you every morning. Follow
it top to bottom. Each step tells you **what to do** and **what you should see**.

---

## What you need first

- **A Mac or Linux terminal** (the black window where you type commands).
- **Python 3** — check by typing `python3 --version`. If you see a number, you're good.
- **Claude Code** — the tool you're reading this in.
- **A free NASA key** — 2 minutes to get (Step 2 below). Without it the project
  still works, but NASA limits how often you can ask.

> **New to the terminal?** A "command" is just a line of text you type and press
> Enter. Copy the grey boxes below exactly. Don't worry about understanding every
> word yet.

---

## Step 1 — Run it once by hand

First, download the project and go into its folder. Copy these lines and press
Enter after each:

```bash
git clone https://github.com/panaversity/agentfactory-labs.git
cd agentfactory-labs/crash-course/loop-eng/sky-watch
```

Now run the watch:

```bash
python3 .claude/skills/sky-watch/scripts/skywatch.py
```

**What you should see:** a box like this, with today's real asteroids.

```
  ☄  SKY WATCH — next 7 days, from 2026-07-19
  ──────────────────────────────────────────────────────────────
     ✓  Nothing flagged hazardous in the window.
     Closest pass:  2016 PC8  on 2026-07-19
        31,201,476 km  =  81.2× the Moon
     3 close approaches today.
  ──────────────────────────────────────────────────────────────
```

🎉 That's it working! You just fetched live data from NASA.

> **Got an error saying "429 Too Many Requests"?** That's normal — it means NASA's
> free shared key is busy. Do Step 2 to get your own, then try again.

---

## Step 2 — Get your own NASA key (2 minutes)

1. Open **[api.nasa.gov](https://api.nasa.gov)** in your browser.
2. Fill in your first name, last name, and email. Click **Signup**.
3. A long code appears on screen right away (also emailed to you). Copy it.

Now tell your terminal about it. Replace `PASTE_KEY_HERE` with your real code:

```bash
export NASA_API_KEY=PASTE_KEY_HERE
```

Run the watch again — no more "429":

```bash
python3 .claude/skills/sky-watch/scripts/skywatch.py
```

> **Tip:** `export` only lasts for that one terminal window. To set it forever,
> run this once: `echo "export NASA_API_KEY=PASTE_KEY_HERE" >> ~/.zshrc` then
> close and reopen the terminal.

---

## Step 3 — Ask Claude in plain English

The script gives you numbers. Claude turns them into a friendly sentence.

Start Claude Code inside this folder:

```bash
claude
```

The first time, Claude asks **"Do you trust this folder?"** — say **yes**. (This
lets it run the watch without asking permission every single time.)

Now just type a normal question:

```
what asteroids are coming this week?
```

**What you should see:** a short paragraph like *"All clear this week — the closest
asteroid stays 23× farther than the Moon..."* Claude ran the script for you and
explained the result. That's the whole idea: **you ask like a human, it fetches
like a machine, and it never makes up an answer.**

---

## Step 4 — Get it by email every morning

This is the exciting part: a watch that runs on its own while you sleep.

### 4a. Connect Gmail

Go to **[claude.ai/customize/connectors](https://claude.ai/customize/connectors)**
and connect **Gmail**. This gives Claude permission to write emails for you.

### 4b. Create the schedule

In Claude Code, type this one line — **replace `your-email@example.com` with
your own email address**:

```
/schedule every day at 7am, run the sky-watch skill for today and draft the forecast email to your-email@example.com
```

**What you should see:** Claude confirms it made a **Routine**. You can view it any
time at **[claude.ai/code/routines](https://claude.ai/code/routines)**. From now
on, every morning at 7am it checks the sky and writes you an email.

### 4c. Important — Gmail makes a *draft*, not a sent email

Here's the one thing that surprises everyone: **Gmail can only create a draft.**
So each morning the watch lands in your **Drafts** folder, and you tap **Send**
yourself. That's a safety limit, not a bug.

> **Want it to truly send by itself?** Connect **Slack** instead of Gmail. Slack
> delivers messages on its own, so the watch arrives with no button to press.

---

## Step 5 — Prove it before you trust it

Never trust a midnight schedule you've never seen run. Test it fast first:

```
/schedule in 2 minutes, run the sky-watch skill and draft the forecast email to your-email@example.com
```

Wait two minutes, then check your Gmail **Drafts**. If the email is there — 
it works! Leave the 7am schedule on and go to bed. Tomorrow the watch is waiting.

---

## One nuance NASA will trip you on

Some asteroids get a scary **"potentially hazardous"** label but still miss us by
**180× the Moon's distance** — completely safe. That label describes the rock's
*orbit* over many years, **not** today's pass. This watch always shows the label
**and** the real distance side by side, so a routine flyby never becomes a false
scare. Don't panic at the word "hazardous" — read the distance.

---

## Something not working? (Quick fixes)

| Problem | What it means | Fix |
| --- | --- | --- |
| `429 Too Many Requests` | NASA's shared key is busy | Do **Step 2** — get your own key |
| Claude asks permission every time | You skipped the "trust this folder" question | Quit, run `claude` again, say **yes** |
| The email is in Drafts, not sent | Gmail can only draft (normal!) | Tap Send yourself, or use Slack (**Step 4c**) |
| No routine shows at claude.ai | You haven't run `/schedule` yet | Do **Step 4b** — the routine only exists after that |
| "watch failed" message | The internet or NASA was down | That's correct behaviour — it refuses to guess. Try again |

---

## The big idea (why this project matters)

A watch is valuable because it **shows up on its own**. You don't remember to check;
it checks for you. And when it has nothing to report, it still says so — that quiet
"all clear" is proof it ran, not proof it failed.

You built a machine that watches the sky every morning so you don't have to. 🌌
