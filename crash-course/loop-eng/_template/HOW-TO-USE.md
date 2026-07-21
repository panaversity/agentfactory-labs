# 🧩 Loop-Eng Project Template

Copy this folder to start a **new loop-engineering project** in the same house
style as `paper-watch`, `sky-watch`, and the others. You get a working skeleton —
a skill, a bundled script with a spine, the beginner docs, and the Claude Code
permissions, all wired together. You just fill in the blanks.

## The house rules (what every loop-eng project follows)

1. **One concept per project.** Teach exactly one thing (a heartbeat, or the
   spine). Name it in the README and link the course lesson.
2. **A live, free data source — no key, no sign-up.** It must run the second a
   student clones it. If a source needs an API key, pick a different source.
3. **Zero setup.** `git clone`, then `python3 …` or open Claude Code. Python
   **standard library only** — no `pip install`, no `npm`.
4. **The script owns the data. Claude never invents it.** If the fetch fails, the
   script says so and exits — a made-up answer is the one thing it must never give.
5. **Beginner-first docs.** Every step says *what to type* and *what you should
   see*. `START-HERE.md` walks a first-timer through it.
6. **If it has a spine, the spine is the lesson.** Read the memory first, write it
   last, and make *deleting* the memory the "aha" — no spine, no loop.

## The files you get

| File | What it is |
|---|---|
| `AGENTS.md` | The project's one job + that the script owns the answer — **read by every agent** (Codex, Cursor, Claude Code…) |
| `CLAUDE.md` | One line — `@AGENTS.md` — so Claude Code (which reads only `CLAUDE.md`) picks up `AGENTS.md` too |
| `README.md` | The short "what it does / run it / how it fits the loop" page |
| `START-HERE.md` | The step-by-step beginner walkthrough |
| `.claude/settings.json` | Permissions: run the skill + script without a prompt every time |
| `.claude/skills/SKILL-NAME/SKILL.md` | When to trigger + how to run the script |
| `.claude/skills/SKILL-NAME/scripts/script.py` | The bundled, deterministic script (ships **with** a spine) |

> **Cross-agent note:** `AGENTS.md` + `script.py` work for *any* coding agent — the
> script is plain Python and every agent reads `AGENTS.md`. The `.claude/` folder
> (skill + permissions) is just how *Claude Code* auto-runs it; other agents run the
> script directly, following `AGENTS.md`.

## How to use it — two ways

### The easy way (let Claude fill it in)
1. Copy the folder and rename it:
   `cp -r _template my-project && cd my-project`
2. Open Claude Code in it and say, for example:
   > Fill in this template for a project that watches **new GitHub releases** of a
   > repo from the **GitHub API**. It teaches Concept 12, the spine.
3. Claude replaces every placeholder, writes the fetch + parse, and tests it.

### The manual way (find-and-replace)
Rename the `SKILL-NAME` folder and `script.py`, then replace every `{{PLACEHOLDER}}`
below across all the files:

| Placeholder | Meaning | Example |
|---|---|---|
| `{{PROJECT_TITLE}}` | human name | `Paper Watch` |
| `{{project-slug}}` | folder + skill name (kebab-case) | `paper-watch` |
| `{{scriptname}}` | the `.py` file's name | `paperwatch` |
| `{{EMOJI}}` | one emoji for the project | `📄` |
| `{{SOURCE_NAME}}` | the data source | `arXiv` |
| `{{SOURCE_BLURB}}` | one line describing it | `a free, open library of research papers` |
| `{{SOURCE_URL}}` | the API endpoint | `https://export.arxiv.org/api/query` |
| `{{SOURCE_DOMAIN}}` | just the domain (for permissions) | `export.arxiv.org` |
| `{{CONCEPT_NUMBER}}` | which lesson | `12` |
| `{{CONCEPT_NAME}}` | its title | `The spine (memory between runs)` |
| `{{THING}}` | what you watch, plural | `papers` |
| `{{ONE_LINER}}` | a **noun phrase**: what one run shows (no leading verb) | `the newest papers on your topic you haven't seen yet` |
| `{{DEFAULT_QUERY}}` | the built-in default topic | `LLM agents` |

Then open `script.py` and fill in the **three TODOs** — `SOURCE_URL` (+ the query
params), `_parse_response()` (turn the reply into a list of items), and
`STARTER_TOPICS` (a few known-good topics it suggests when a search finds nothing).
Everything else — the spine, the retry, the honest failure, the card, argparse —
already works.

## Stateless project? (no memory needed)
If your project just reprints "what's true right now" every run (like `sky-watch`
listing today's asteroids), it doesn't need a spine. In `script.py`, delete the
block marked `── SPINE ──` and the READ/WRITE steps in `main()`; keep the fetch, the
card, and the honest-failure. In `README.md` and `AGENTS.md`, delete the spine
paragraphs (each is marked). That's the whole difference.

## Before you ship — the checklist
- [ ] Runs on a clean clone with `python3 …`, no install.
- [ ] `--help` works; a bad flag gives a friendly message, not a traceback.
- [ ] The fetch failing prints an honest error and exits (never invents data).
- [ ] `.claude/settings.json` names the real skill + real script path.
- [ ] `SKILL.md` `name:` matches the folder; `allowed-tools:` are **exact tool
      names** (`Bash, Read`) — **never** `Bash(...)` globs; those hard-fail.
- [ ] Every `START-HERE.md` step says what to type AND what you should see.
- [ ] If it has a spine: deleting the memory file mid-demo makes the "aha" land.
- [ ] Add a row to `../README.md` for the new concept + project.
