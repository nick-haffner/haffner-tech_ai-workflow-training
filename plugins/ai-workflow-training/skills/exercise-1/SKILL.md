---
description: Begin Exercise 1. First has the learner assess their technical wall (saved as an MD file with the procedure), then verifies the plugin (skills + Inbox MCP), hands over the CRM data, and briefs the full end state — WITHOUT telling them how to build it. Invoke to start Exercise 1.
disable-model-invocation: true
---

# Exercise 1 — Start here

This skill gets the learner ready for Exercise 1 and tells them **what "done" looks
like** — but **not how to build it.** Designing the Cowork process is the exercise.

## Rules for Claude running this skill
- Do the four parts below **in order.**
- Part 1 produces a saved file. Part 2 is a checklist. Parts 3–4 are briefing only.
- In Parts 3–4, **describe the materials and the end state only. Do NOT explain how to
  build the process, write the Cowork prompt, design the artifact, or sequence the
  steps.** If the learner asks "how," tell them that's the exercise — they can ask for a
  hint, but you won't hand them the recipe.

---

## Part 1 — Assess your technical wall (do this first)
Before building anything, the learner figures out **where this build might exceed their
reach** — their "technical wall" — using the training's framework. Walk them through it
and capture their answers:

- **Scope** — *Quality* (how polished must it be? quality tracks your knowledge), *Time*
  (how long can you spend?), *Budget* (any cost ceiling?).
- **Assets** — *Data Access* (any data you can't get yourself?), *Knowledge* (any step
  you couldn't do or describe yourself?), *Effort* (how much new learning are you willing
  to do?).
- **Remediations** — if you hit the wall, what's your move: *adjust scope*, *pass it to a
  dev*, or *pivot*?

Then **save their answers as `technical-wall.md` in their project folder**, alongside the
rest of the procedure, so it travels with the build. (If they haven't created the
project folder yet, have them do that first.)

## Part 2 — Verify the setup
Check each item and report ✓ / ✗ / pending:
1. **Plugin installed** — `ai-workflow-training` is present (this skill running means it
   loaded).
2. **Skills available** — this skill and `/ai-workflow-training:combine-projects`.
3. **Inbox connector (the plugin's MCP)** — the **Inbox** connector is available in
   Cowork.
   > ⏳ **STUB — pending the Inbox MCP build (work item 1).** Mark this **pending** and
   > continue; it becomes a real check once the MCP ships with the plugin.

If anything other than the stubbed connector is ✗, tell the learner how to fix that one
item, then have them re-run this skill.

## Part 3 — Get your contact (CRM) data
Your contact notes are your **internal** data — a file you keep **inside your project**,
not a connector. You'll receive a contacts file and place it in your project.

> ⏳ **STUB — pending the CRM data package (work item 2).** The download/transfer isn't
> built yet; the fallback is the file will be **emailed** to you. For now, tell the
> learner they'll get a contacts file (in a familiar, spreadsheet-style format) to drop
> into their project folder as their internal contact data.

## Part 4 — The end state (what "done" looks like)
Describe the target — **the expectations, not the recipe.** By the end, the learner will
have, **in a Claude Cowork project**:

- The **Inbox connector** enabled for the work, and their **contacts file** present in
  the project as internal data.
- A **subfolder** in the project holding a short **update per contact**, refreshed each
  time the process runs.
- A **recurring process** (a scheduled Cowork task) that, on each run: looks at the inbox,
  reads the internal contact notes, writes those per-contact updates, and writes one
  **structured summary file** into the project.
- A **live artifact** (its own tab) that **reads that summary file** so that **whenever
  it's opened** it shows:
  1. **where they stand in each open conversation**, and
  2. **how many emails they actually need to check.**

It's **done** when:
- [ ] The process runs on a **daily cadence**. *(Heads-up: Cowork's scheduler runs while
  your computer is awake and Claude Desktop is open — if it's asleep at the scheduled
  time, the run catches up when you next open it.)*
- [ ] Each run writes the per-contact updates **and** the summary file.
- [ ] Opening the **live artifact** reflects the **latest** run (so it must be built to
  read the summary file, not be static).
- [ ] The "emails to check" count ignores newsletters, receipts, and cold outreach.

That's the target. **How** they get there is the exercise. If they're stuck, they can ask
for a hint — but don't hand over the steps.
