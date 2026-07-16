# The Doorbell — a loop that nobody starts

**Loop Engineering, Concept 7 — event-driven loops.**

Propose a change to your code, and about a minute later a review appears. Nobody typed a prompt.
Nobody was watching. Something _happened_, and that started the work.

That is the whole idea, and it is the opposite of the last project.

## Two kinds of loop

In the [ISS project](../iss-loop/), **you** start the loop. You type `/loop show me the location of the ISS every minute`, and it runs while you watch.

Here, **you start nothing.** The loop sits there doing nothing at all — for a day, a week, forever — until someone proposes a change to the code. Then it wakes up.

A schedule is an alarm clock: it rings whether or not anything happened.
An event is a doorbell: **nothing until someone presses it, then instantly.**

That has a real consequence. On a quiet day this loop runs zero times and costs zero. On a busy day
it runs nine times. It matches the work, because the work is what starts it.

## First: this one needs your own repo

The ISS project ran on your laptop, so you could just clone this folder and go.

This one cannot. A doorbell only rings on **your** repo, because GitHub only runs workflows that sit
at the top of a repository — never in a subfolder like this one. So the files here are a kit to copy
out, not a project to run in place.

That is also why this project needs a token and the ISS one did not. Read on.

## Build it — 5 steps

You need a **Claude Pro or Max plan**. No API key, no billing setup.

### 1. Make your own repo and copy this kit into it

```bash
gh repo create my-doorbell --public --clone
cd my-doorbell
cp -R /path/to/agentfactory-labs/crash-course/loop-eng/doorbell/. .
git add -A && git commit -m "add the doorbell" && git push
```

You now have `readings.py` (something to review) and `.github/workflows/doorbell.yml` (the doorbell
itself) — and crucially, that workflow now sits at the **top** of your repo, where GitHub will read it.

### 2. Look at what you just copied

```yaml
on:
  pull_request:
    types: [opened, synchronize]
```

That is the doorbell. Four lines in the file are doing the real work:

| Line                                        | Why it is there                                                                       |
| ------------------------------------------- | ------------------------------------------------------------------------------------- |
| `on: pull_request`                          | **The doorbell itself.** This is what listens.                                        |
| `types: [opened, synchronize]`              | Ring when a change is proposed (`opened`) **and** when it is updated (`synchronize`). |
| `track_progress: true`                      | **Do not remove this.** Without it the run succeeds and posts nothing. See gotchas.   |
| `github_token: ${{ secrets.GITHUB_TOKEN }}` | Lets it comment without installing any GitHub App. GitHub provides this token free.   |

### 3. Get your token

```bash
claude setup-token
```

Your browser opens. You approve. It hands back a **code** — paste that into the terminal.
**Then** it prints the **token** you actually want.

Two pastes, and this trips up everyone: a _code_ goes into the terminal, and the _token_ it gives
back goes into step 4.

**Why does this need a token when the ISS project did not?** Because the work has left your laptop.
The ISS loop ran on your machine, where you were already logged in. This one runs on a blank
computer GitHub rents for 60 seconds, which has never heard of you. It needs its own way to prove it
is allowed to talk to Claude. That is all the token is — and it is the same reason every unattended
loop needs credentials of its own.

### 4. Give the token to your repo

```bash
gh secret set CLAUDE_CODE_OAUTH_TOKEN --repo YOUR-NAME/my-doorbell
```

Paste at the prompt. Nothing appears as you paste — that is deliberate, it is a secret.

The name must be exactly `CLAUDE_CODE_OAUTH_TOKEN`, because that is what the workflow looks for.

### 5. Ring it

Propose a change with a bug in it. Easiest way, no git needed:

1. On GitHub, open `readings.py` in your repo and click the **pencil** (Edit).
2. Paste this in at the bottom — the bug is on purpose:

   ```python
   def average_altitude(readings):
       total = 0
       for i in range(len(readings) - 1):
           total += readings[i]
       return total / len(readings)
   ```

3. Choose **"Create a new branch for this commit and start a pull request"**.
4. Click **Propose changes**, then **Create pull request**.

Now stop touching it. Within a minute or two, a review you never asked for:

> **Off-by-one error in `average_altitude()`**
>
> `range(len(readings) - 1)` iterates indices `0` to `len(readings) - 2`, skipping the last element
> of `readings`. The sum is then divided by the full `len(readings)` … the average is systematically
> too low.

## What happens when the doorbell rings

There is no robot waiting inside your laptop. The real sequence:

1. You propose a change.
2. **GitHub notices** and reads `.github/workflows/doorbell.yml`.
3. GitHub **rents a fresh computer** — a blank Ubuntu machine in a data centre.
4. It downloads your code, runs Claude, posts the review.
5. The machine is **destroyed**. Everything on it is gone.

## Gotchas we hit, so you do not have to

**A green checkmark does not mean it worked.** Our first attempt ran, took 4 turns, reported
success, and posted **absolutely nothing** — a cheerful green tick and an empty PR. Without
`track_progress: true` the action reviews quietly and never publishes. If you see green and silence,
this is why.

**Committing to `main` does nothing.** There is no "push" doorbell — only "a change was proposed."
Commit straight to `main` and nothing fires: no run, no cost, silence. Push to a branch with an open
pull request and it rings every time.

**Each ring is a brand-new computer.** Two pushes to one PR are two machines that never met.

**It costs real money.** About **$0.11 of your Claude usage per review**. Not a separate bill — just
not free. A busy PR with ten pushes is ten reviews.

**The token expires eventually.** If the doorbell goes quiet for no reason, run `claude setup-token`
again and update the secret.

## Now push again — and read what it says

Change something on that same branch and commit. A second review appears, and it will know things
it has no business knowing. Here is a real one from our own testing:

> **Bug:** The PR is a no-op. Commit `e79b8e7` changed `lowest()`'s docstring in `readings.py`, and
> commit `f85e54d` reverted it back to the original text. The resulting file is byte-identical to
> `origin/main`'s `readings.py` (both `dc43314`), so despite the PR title there is no actual change
> to merge.

Stop and look at that, because it is stranger than it first appears.

The computer that wrote the first review **no longer exists**. It was destroyed. The machine that
wrote this one had never run before, has no memory of anything, and does not know it has a
predecessor. It has never seen your earlier commits happen.

Yet it knows `e79b8e7` changed a docstring, `f85e54d` undid it, and the two cancelled out — and it
was right. Our PR really was a no-op.

**It read all of it.** The commits are in the git history. The earlier reviews are in the pull
request thread. All of it written down, sitting in the repo, waiting. A total stranger walked in,
read the record, and reconstructed the whole story in 2 minutes.

Nothing was remembered. Everything was **written down**, and the next run read it.

The model forgot. **The repo did not.**

That is not a trick — that is the next part of the course, and it has a name: the **spine**.
