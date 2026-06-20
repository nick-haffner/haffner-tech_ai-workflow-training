---
description: A short interactive lesson teaching what it means to combine two automations into a single project — using a worked example, with a comprehension question at each step and a comprehension check at the end, before the learner does it for their own automations. Invoke before Exercise 3.
disable-model-invocation: true
---

# Lesson — Combining two automations into one project

**Purpose.** Before Exercise 3, teach the learner what it actually means to bring two
separate automations together into a **single project**, using a worked example. Then
they'll apply it to their Exercise 1 + Exercise 2 builds.

> Terminology: a **project** is one self-contained folder that holds an automation —
> its process, its storage, and its config. (We always say *project* here.)

## How to run this lesson
- Teach **one step at a time — one step per response.**
- **Every step ends with a comprehension question.** Ask it, then **stop and wait for
  the learner's answer.** Do not move on until they answer.
- React to their answer briefly: confirm what's right, gently correct what's off, then
  proceed to the next step.
- After the five steps, run the **final comprehension check** (also wait for an answer),
  then direct them to do it for real.
- If the learner clearly already gets it, you may move faster — but still pause for each
  answer.

## The worked example (use this throughout)
Two small, comparable automations the learner does **not** have to build — they're just
to think with:

- **Project A — "Weekly receipt organizer":** reads a folder of receipt images, pulls
  out each amount, appends them to an expenses spreadsheet, and emails a weekly expense
  summary every Friday.
- **Project B — "Weekly mileage logger":** reads a file of trips, calculates the mileage
  reimbursement, appends it to a spreadsheet, and emails a weekly mileage summary every
  Friday.

---

## Step 1 — What "two separate projects" looks like
Lay it out: each project is its own folder, with its **own** schedule (Friday), its
**own** email step, its **own** storage/spreadsheet, and its **own** summary. They run
side by side and never talk to each other.

**Comprehension question:** *Looking at Project A and Project B, name two things that are
duplicated across them.* → wait for answer.

## Step 2 — Spotting the shared resources
Walk through what's the same in both: the **schedule** (both Friday), the **email
delivery** (both email you a summary), the **storage** (both append to a spreadsheet),
and the **shape of the output** (a weekly summary). These are the candidates for sharing.

**Comprehension question:** *Of the schedule, the email step, and the spreadsheet — which
could be shared if you combined them, and why would sharing help?* → wait for answer.

## Step 3 — What "combining" actually means
Combining = **one project folder** with **one schedule**, **one email step**, and **one
storage**, producing **one summary** that has both a receipts section and a mileage
section. The two *reading* steps stay (you still read receipts AND read trips) — but
everything around them is shared.

**Comprehension question:** *After combining, how many scheduled runs happen on Friday
instead of two? And what happens to the two separate summary emails?* → wait for answer.

## Step 4 — Capabilities that emerge
New things that only exist once combined: **one email** instead of two; a **single
weekly finance view** (receipts + mileage together); the ability to **cross-reference**
(e.g., a trip and its fuel receipt on the same day); and **one place to maintain**
instead of two.

**Comprehension question:** *Name one capability that only exists once the two are
combined — something neither separate project could do.* → wait for answer.

## Step 5 — The new work it creates
Combining isn't free. New work: **reconciling two different data shapes** (receipts vs
trips) into one summary; **designing the combined layout**; deciding what happens if
**one half fails** (no receipts that week, but trips exist); and a **bigger, more
complex single process** to maintain.

**Comprehension question:** *Name one new piece of work that combining created that
neither project had on its own.* → wait for answer.

---

## Final comprehension check
Give them this fresh scenario and **wait for their answer**, then give feedback:

> You have two daily automations: (1) a **"new leads" digest** built from a web form,
> and (2) a **"support tickets" digest** built from email. Suppose you combine them into
> one project. Name:
> 1. one **shared resource** you'd reuse,
> 2. one **capability that emerges** from combining them, and
> 3. one **new cost** the combination creates.

Confirm their three answers (shared resource, emergent capability, new cost) make sense.
If any is off, correct it briefly.

## Now do it for real
Direct them to Exercise 3: combine **your Exercise 1 (inbox digest)** and **Exercise 2
(morning briefing)** into a single project at `projects/combined-assistant/`, sharing
resources where it makes sense — then fill in `exercises/03-integration/reports/benefits.md`
and `drawbacks.md`. They've just done the thinking on the example; now apply it.
