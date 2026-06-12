# AI Prompting Lab: All 13 Concepts

Practice every concept, by doing. Thirteen hands-on exercises, one per concept. You type the prompts, read the answers, and write what you noticed.

- **Time:** ~2 hours (split it across sessions)
- **Exercises:** 13
- **Tools:** ChatGPT, Claude, or Gemini (all free tiers work)
- **Level:** Beginner friendly

Most exercises give you two examples: a **Daily** (everyday) version and a **Work** (simple-professional) version. Run at least one; try both if you have time. Copy any prompt directly.

Some exercises need a little setup (a file to upload, a second tool, or a specific feature). Those are marked with **Needs**. If you can't do one today, read it and move on.

> **The one rule behind all 13:** Get the right context in, keep the wrong context out.

---

## Jump to an Exercise

| # | Exercise | Part |
|---|----------|------|
| 1 | [Novice vs Power User](#1-novice-vs-power-user) | Part 1: How AI knows things |
| 2 | [Knows vs Guesses](#2-knows-vs-guesses) | Part 1 |
| 3 | [The 3 Retrieval Modes](#3-the-3-retrieval-modes) | Part 1 |
| 4 | [Context Is Everything](#4-context-is-everything) | Part 2: Talking to AI well |
| 5 | [Think Hard](#5-think-hard) | Part 2 |
| 6 | [Stop the Flattery](#6-stop-the-flattery) | Part 2 |
| 7 | [Brainstorm-Iterate Loop](#7-the-brainstorm-iterate-loop) | Part 2 |
| 8 | [Multimodal (Image/Audio)](#8-multimodal--image--audio) | Part 3: Beyond text |
| 9 | [Build a Small App](#9-build-a-small-app) | Part 3 |
| 10 | [Data Analysis](#10-data-analysis) | Part 3 |
| 11 | [Desktop Apps & Permissions](#11-desktop-apps--permissions) | Part 4: Working safely & choosing tools |
| 12 | [Which Model When](#12-which-model-when) | Part 4 |
| 13 | [Models Checking Models](#13-models-checking-models) | Part 4 |

---

## Part 1: How AI Knows Things

### 1. Novice vs. Power User

**6 min -- feel what context does**

**Goal:** Same question, two ways. The briefing changes everything.

#### Step A: The novice prompt (try one)

Type a bare, no-context question:

**Daily:**

```
Which phone should I buy?
```

**Work:**

```
How do I write a good email?
```

Read it -- generic. True for anyone, useful to no one.

#### Step B: The power-user prompt (same topic + context)

**Daily:**

```
Help me choose a phone. Context: my budget is about $300, I
mostly take photos of my kids and use WhatsApp, my current
phone's battery dies by 3pm, and I find big phones hard to
hold. Give me 3 options with a one-line reason for each, then
tell me which you'd pick and why.
```

**Work:**

```
Help me write an email. Context: I need to ask my manager
to move our Friday team meeting to Monday because I have a
doctor's appointment. We have a friendly working relationship.
Keep it short and polite. Give me the email, ready to send.
```

**Write it down:** What was DIFFERENT about the second answer? (2 senten
ces)according to prompt one it shows lot of unncessary information and it was global like not specific acc to my scenerio when i gave prompt 2 it showed exact information acc to my needs

> **Takeaway:** AI is like a smart new coworker. It only knows what you tell it.

---

### 2. Knows vs. Guesses

**5 min -- confident does not equal correct**

**Goal:** A confident tone is not the same as a correct answer.

#### Step A: Something AI knows well

**Daily:**

```
Why do onions make you cry when you cut them? Answer in 2 short
paragraphs.
```

**Work:**

```
What is the difference between a CV and a cover letter? Keep it short.
```

Common topics -- the answers should feel solid.

#### Step B: Something AI may NOT know

**Daily:**

```
What were the main news headlines in my city today? If you cannot
be sure, say so clearly instead of guessing.
```

**Work:**

```
What is the current minimum notice period an employer must give
before changing an employee's contract in my country? Be specific.
If you are not sure this is current, say so instead of guessing.
```

A legal/HR fact that changes over time and varies by country -- watch whether the AI gives a confident number anyway.

**Write it down:** Did the AI admit when it wasn't sure, or sound confident anyway?
yes it showed by using word assuming ,may be .i ask how u know it said by web searching.i also ask differnt question in which it clearly showed i won't guess type sentences

> **Takeaway:** Always ask "How would the AI even know this?" For recent, local, or private facts, make it search or admit uncertainty.

---

### 3. The 3 Retrieval Modes

**8 min -- steer pretrained / search / research**

**Goal:** See how your wording makes the AI answer from memory, search the web, or run deep research.

**Needs:** a tool with web search on (most have it by default)

#### Mode 1: Pretrained (from memory)

**Daily:**

```
Summarize the plot of Romeo and Juliet in 4 sentences.
```

No search needed -- this doesn't change week to week. Should be instant.

#### Mode 2: Web search (fresh info)

**Daily:**

```
What's the weather forecast for my city this weekend? Use a
current source and cite it.
```

**Work:**

```
What are the latest developments this month in [your field]?
Cite each claim, and mark anything you can't support as 'unverified'.
```

Notice if it shows it searched. "Today / this week / latest / my city" are the trigger words.

#### Mode 3: Deep research (a structured report)

**Work:**

```
Research [a topic you care about] thoroughly. Use reputable
sources only (government sites, peer-reviewed studies, official
reports -- not forums). Produce a structured report with:
(1) the 3 most important points, (2) a comparison table,
(3) 3 open questions. Cite sources.
```

Words like "research thoroughly," "report," "cite sources," "use these source types" steer toward the deepest mode.

**Write it down:** Which prompts made the AI actually search? How could you tell?
mode 2 made ai acrually search because i asked it about latest recent book .also when i use research thoroughly it went into deep research

> **Takeaway:** You don't click a mode -- your wording picks it. Name your sources and ask for citations to keep web answers honest.

---

## Part 2: Talking to AI Well

### 4. Context Is Everything

**6 min -- brief it like a colleague**

**Goal:** Load context up front instead of making the AI guess.

#### Use this shape for both

**Daily:**

```
I need help planning dinner for tonight.
Here is what you need to know:
- I have chicken, rice, onions, and yogurt in the kitchen
- I have only 30 minutes
- One person at the table doesn't eat spicy food
What I want back: 3 simple meal options, no commentary.
```

**Work:**

```
I need help writing a short update for my team.
Here is what you need to know:
- We finished the customer survey this week
- 2 tasks are still pending (the report and the slides)
- The reader is my team, who like quick bullet points
What I want back: a 4-line status update, friendly tone.
```

**The template (copy and fill in):**

```
I need help for my toddler.he doesnt drinks milk
Here is what you need to know:
- [fact 1 -- he is 2 years old never drinks milk
- [fact 2 -- i need some alternatives
- [fact 3 --also concerned about calcium and vitd
What I want back: [a list / an email / 3 options / a plan].
```

**Write it down:** Which single piece of context changed the answer the most?
the more i clarify my situation the more detailed and detailed result it gives. when i type list it gave me list of my requirement to read it easily

> **Takeaway:** Five lines of good context beats five paragraphs of clever wording. When the topic changes, start a new chat.

---

### 5. Think Hard

**6 min -- hand it a real, hard decision**

**Goal:** Invoke reasoning mode and ask for structured output, not a wall of prose.

#### A quick contrast

Ask a tricky question normally, then ask again with "think hard." Compare.

**Daily:**

```
I have $200 to improve my home office and I work from home full
time. Think hard before answering. Then give me:
1) the 3 upgrades with the biggest impact on comfort and focus,
2) which one you'd do first and why,
3) one thing I should NOT waste money on.
```

**Work:**

```
I'm choosing between two job offers. Offer A: higher pay, longer
commute, less interesting work. Offer B: lower pay, remote,
steeper learning curve. I value learning and time with family.
Think hard. Then tell me:
1) the 3 trade-offs that actually matter for me,
2) which you'd pick and why,
3) under what conditions your answer flips.
```

**Write it down:** Did "think hard" produce a deeper answer? What changed? 
yes when i type think hard it defined my answer in detail by comparing both and made me understad pros and cons of both to completely satisfy me

> **Takeaway:** Save thinking mode for multi-trade-off questions you'd want a human to take their time on -- not quick lookups.

---

### 6. Stop the Flattery

**6 min -- sycophancy**

**Goal:** See how the way you ask pushes AI to just agree with you.

#### Step A: The "bait" prompt (AI tends to agree)

**Daily:**

```
Don't you think mornings are obviously the best time to exercise?
```

**Work:**

```
Don't you agree that working from home is clearly better than the
office?
```

Notice: it probably agrees and lists reasons that match what you implied.

#### Step B: The neutral prompt (AI actually thinks)

**Daily:**

```
Compare exercising in the morning versus the evening. List the
strongest case for each, and what kind of person each option
suits best. Don't tell me which to pick.
```

**Work:**

```
Compare working from home versus working in the office. List the
strongest arguments for each. Don't tell me which is better.
```

**Write it down:** Did Step B give you a reason you hadn't thought of? Write one.
step A also non biased and .step B gave me some reason to follow its answer like in evening morning exercise comparison it gave me pros of morning like hormonal health ,psychology,first birds sounds 

> **Takeaway:** Verbs like find, prove, defend, confirm hand the AI your answer. Use compare, evaluate, list both sides instead.

*Note: newer models resist obvious flattery, so the bait may make the AI hedge rather than fully agree. The lesson still holds -- notice how much more balanced Step B is.*

---

### 7. The Brainstorm-Iterate Loop

**8 min -- the highest-leverage habit**

**Goal:** Never accept the first answer. The value is in the back-and-forth.

#### Round 1: Ask for OPTIONS, not one answer

**Daily:**

```
I want a small hobby that costs almost no money and that I can do
for 15 minutes at home. Give me 5 different ideas, one line each.
Don't explain any of them yet.
```

**Work:**

```
I need to write a short message asking a coworker to send me a
file they keep forgetting to send. I want to sound friendly, not
annoyed. Give me 5 different versions, one or two lines each.
Don't explain any of them yet.
```

#### Round 2: Give feedback, ask again

Read the 5. Then type (fill the blanks):

```
I don't like option ___ because ___________.
I like option ___ but I want it to be more __________.
Give me 5 NEW ideas based on this feedback.
```

#### Round 3: Expand the winner

**Daily:**

```
I'll go with [your favorite hobby]. Give me a simple step-by-step
plan to start it this week.
```

**Work:**

```
I'll go with version [number]. Now make it slightly warmer and
add a friendly closing line, but keep it under 3 sentences.
```

**Write it down:** Was the idea you ended with better than anything in Round 1? Why?
yes i asked repeatedly ,also feedback like i dont agree expand your vision and it came more structured and defined.

> **Takeaway:** Load context, ask for options, give feedback, repeat, expand. The value isn't the first answer; it's the loop.

---

## Part 3: Beyond Text

### 8. Multimodal -- Image & Audio

**7 min -- give the AI a photo to read**

**Goal:** Practice handing AI something that isn't text.

**Needs:** a photo on your device (a receipt, handwritten note, or whiteboard)

#### Image input: transcribe & summarize

Upload any photo of text, then paste this:

**Daily:**

```
Here's a photo of a handwritten note (or receipt). Transcribe
what it says. Keep the original wording. If a word is unclear,
mark it [unclear] and give your two best guesses.
```

**Work:**

```
Here's a photo of a whiteboard from a meeting. List the main
points as bullets, then list any action items you can spot.
Flag anything you couldn't read with confidence.
```

AI is great at the gist, weak on tiny detail -- always check totals and the bits it flagged.

#### Bonus: let the AI write an image prompt

```
Write me a detailed image-generation prompt for a cozy,
watercolor-style illustration of a cat reading a book by a
window, suitable for a greeting card. Then I'll paste it into
an image tool.
```

**Write it down:** What did the AI read correctly? What did it get wrong or flag?
it read it correct no wrongs /redflags.

> **Takeaway:** AI does the boring 90% (typing it out) so you focus on the careful 10% (checking what it flagged).

---

### 9. Build a Small App

**8 min -- one prompt, a working tool**

**Goal:** Use the Goal / Input / Output shape to build a real working artifact.

**Needs:** a tool with Artifacts (Claude) or Canvas (ChatGPT / Gemini)

#### The three-slot recipe

**Daily:**

```
Build me a tip calculator.
Goal: split a bill and add a tip.
Input: I type the total, the tip %, and the number of people.
Output: show the tip amount, the grand total, and each person's
share. Make it clean and easy to use. Show me the working version.
```

**Work:**

```
Build me a simple countdown timer for focused work.
Goal: 25-minute work sessions with 5-minute breaks.
Input: I press start.
Output: a large timer counting down, a clear sound when each
session ends, and a clean layout. Show me the working version.
```

#### Then iterate on it (it edits the existing app in place):

```
Make the buttons bigger and change the color theme to calm blue.
Add a reset button.
```

**Write it down:** Did it work first try? What did you change in the iterate step?yes it worked i changed its buttons and it got changed anyway.

> **Takeaway:** The skill isn't coding -- it's writing a clear brief (Goal / Input / Output) and iterating. Small one-screen tools work great.

---

### 10. Data Analysis

**10 min -- expose the silent failure mode**

**Goal:** Learn to make the AI actually run code -- and verify that it did.

#### Round 1: The trap (don't mention code)

In a fresh chat, paste this exactly:

```
Here are 18 numbers: 47, 52, 89, 91, 23, 67, 78, 12, 95, 44,
88, 71, 33, 56, 99, 18, 64, 82. What is the median, the average,
and which numbers are outliers? Be specific.
```

Did it show a code block that ran? Or just a paragraph with numbers? Note your answer.
it showed paragraphs with numbers
#### Round 2: The fix (force the code)

```
Now run that calculation again -- but this time write and run
code to do it, and show me the code you ran.
```

Correct answers: median 65.5, average ~61.6, no clear outliers (roughly even spread). If Round 1 was off, you just saw the silent failure mode.

#### Bonus (Work): if you have a spreadsheet

**Needs:** any CSV (a budget, grades, a tracker export)

```
Here's a CSV. Before analyzing anything, tell me the exact row
count, the column names, and the date range. Then write and run
code to show me the 3 most interesting patterns, with a chart.
Show me the code you ran.
```

**Write it down:** Did Round 1 run code or guess? How could you tell the difference?
round 1 didnt showed code just paragraphs and answers.when i ask code it gave code 

> **Takeaway:** Always say "write and run code, show me the code." No code block = it probably guessed.

---

## Part 4: Working Safely & Choosing Tools

### 11. Desktop Apps & Permissions

**5 min -- mostly a read + plan exercise**

**Goal:** Understand the safe workflow before you ever let an app touch real files.

**Needs:** nothing to install -- this one is about judgment. (Optional: a desktop app like Cowork.)

#### Practice the "plan, don't act" habit in chat

You can rehearse the mindset in any chat tool. Paste this:

```
Imagine you are an AI assistant with permission to reorganize a
messy folder of 50 personal files (photos, PDFs, receipts).
Before doing anything, write me a step-by-step SAFE workflow you
would follow so that nothing is lost or wrongly renamed. Then
list 3 things I should NEVER let you do.
```

**The rule to memorize:** The safe order is always: 1) tell the task, 2) ask for a plan, 3) review & edit, 4) only then approve.

**Write it down:** What's one thing you'd NEVER grant an AI app on day one?
i won't allow to oerform bulk actions without review.
> **Takeaway:** Deleted files often skip the recycle bin; edits overwrite. Scope permissions tight; grow them with track record, not trust in the brand.

---

### 12. Which Model When

**8 min -- same prompt, two tools**

**Goal:** Feel how different models answer the same prompt differently.

**Needs:** two AI tools open (any two of ChatGPT / Claude / Gemini)

#### Run the SAME prompt in both

Pick one prompt. Paste it into Tool A, then Tool B. Read both answers.

**Daily:**

```
Plan a relaxing Saturday for someone who works hard all week and
lives in a city. Give me a simple hour-by-hour plan from 9am to
9pm, with cheap or free activities.
```

**Work:**

```
Write a 100-word LinkedIn post announcing that I finished a
course on AI prompting and what I learned. Friendly, not boastful.
```

**Write it down:** Which tool did better on THIS task -- and what was different? i asked chatgpt it gave me information with hour by hour recommendation also define pros which makes my mind to go exactly what it says.when i used claud for this it simply showed me what to do at this hour /where to go by this time.i will prefer chat gpt's answer.

> **Takeaway:** There's no single best AI -- it's "jagged." Keep two tabs open so you always have a tiebreaker. Re-test monthly; leaders rotate.

---

### 13. Models Checking Models

**10 min -- an objective quality signal**

**Goal:** Get honest feedback by making two different models grade the same draft.

**Needs:** two tools from different families (e.g. Claude + ChatGPT, not two of the same)

#### Step 1: Grade it in Tool A

Take any 150-250 word thing you wrote (an email, a paragraph from Exercise 7). Paste it, then:

```
Score this draft 1-10 on clarity, structure, evidence, and
what's missing -- one sentence of reasoning per score. Then tell
me the single change that would raise the lowest score the most.
```

#### Step 2: Same draft, same question, Tool B

Open a different-family tool. Paste the same draft and the same prompt.

#### Step 3: Compare

Put the two critiques side by side. Find any point only one of them caught -- that's the value of cross-checking.

**Write it down:** What did Tool B catch that Tool A missed (or vice versa)?
both gave accurate information but chatgpt stayed more clear.

> **Takeaway:** Different families have different blind spots. A point one misses, the other often catches. Save this for work where being wrong is expensive.

---

> **If you remember one thing from all 13:** Get the right context in, keep the wrong context out.

*A 13-exercise companion to "AI Prompting in 2026." Split it across sessions -- Part 1 & 2 first, Part 3 & 4 later. Exercises marked Needs require a little setup. No setup? Read it and come back when you can.*
