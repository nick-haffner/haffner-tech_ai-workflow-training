---
description: Begin Exercise 1. Verifies the plugin (skills + Inbox connector), hands the learner their CRM data, and briefs the full end-state they're aiming for — WITHOUT telling them how to build it. Invoke to start Exercise 1.
disable-model-invocation: true
---

# Exercise 1 — Start here

This skill gets the learner ready for Exercise 1 and tells them **what "done" looks
like** — but **not how to build it.** Designing the Cowork process is the exercise.

## Rules for Claude running this skill
- Do the three parts below **in order**.
- Part 1 is a **verification checklist** — check each item, report ✓ / ✗ / pending, and
  tell the learner exactly what to fix for any ✗ before continuing.
- In Parts 2–3, **describe the materials and the end state only. Do NOT explain how to
  build the process, write the Cowork prompt, design the artifact, or sequence steps.**
  If the learner asks "how," tell them that's the exercise — they can ask for a hint, but
  you won't hand them the recipe.

---

## Part 1 — Verify the setup
Check each item and report the result:

1. **Plugin installed** — `ai-workflow-training` is present (this skill running means it
   loaded; confirm it also appears in `/plugin` → Installed). → ✓ / ✗
2. **Skills available** — the plugin's skills are present: this one and
   `/ai-workflow-training:combine-projects`. → ✓ / ✗
3. **Inbox connector** — the **"Inbox"** connector is added in **Cowork**
   (Customize → Connectors — it should be listed and connected). Ask the learner to
   confirm it's there.
   > ⏳ **STUB — pending the Inbox MCP server (work item 1).** The connector URL and the
   > exact add-steps are not finalized yet. For now, mark this item **pending** and
   > continue; it will become a real check once the server is deployed.

Report the checklist. If anything other than the stubbed connector is ✗, tell the learner
how to fix that one item, then have them re-run this skill.

## Part 2 — Get your contact (CRM) data
Your contact notes are your **internal** data — a file you keep **inside your project**,
not a connector. You'll receive a contacts file and place it in your project.

> ⏳ **STUB — pending the CRM data package (work item 2).** The download/transfer link
> isn't built yet; the fallback is that the file will be **emailed** to you. For now, tell
> the learner they'll receive a contacts file (in a familiar, spreadsheet-style format)
> and should drop it into their project folder as their internal contact data.

## Part 3 — The end state (what "done" looks like)
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
- [ ] Opening the **live artifact** reflects the **latest** run (because it reads the
  summary file — so it must be built to read that file, not be static).
- [ ] The "emails to check" count ignores newsletters, receipts, and cold outreach.

That's the target. **How** they get there is the exercise. If they're stuck, they can ask
for a hint — but don't hand over the steps.
