---
description: Walk the learner through setting up Exercise 1 in Claude Cowork — viewing the simulated inbox/CRM and granting Cowork access to the exercise folder — one step at a time, pausing for confirmation at each step. Invoke when the learner is starting Exercise 1 or asks how to give Cowork the data.
disable-model-invocation: true
---

# Setup — Exercise 1 (Cowork folder access)

**Purpose.** Get the learner ready to build Exercise 1: see the simulated data, then
grant Claude Cowork access to the exercise folder so it can read the inbox and CRM and
write its output. Exercise 1 uses **simulated data only** — no real email account.

## Operating rules
- Present **exactly ONE step per response.** After each step, **stop** and ask the
  learner to confirm it's done ("Reply `done` to continue, or tell me what you're
  seeing"). **Do not advance until they confirm.** If something doesn't match, help
  troubleshoot, then re-confirm.
- Track which step you're on across turns. If re-invoked mid-way, ask which step
  they're on and resume.
- The exercise folder is `exercises/01-inbox-digest/` inside this repository.

## Step 1 — See the simulated inbox
Have the learner **double-click `exercises/01-inbox-digest/viewer/inbox.html`** (it opens
in their browser — no internet needed). They should see 12 messages, 6 of them marked
**unread**. Clicking a message expands it.
→ Confirm they can see the inbox.

## Step 2 — See the simulated CRM
Have them **double-click `exercises/01-inbox-digest/viewer/crm.html`**. They should see 6
contacts, each with a status, an open item, and your notes.
→ Confirm they can see the CRM.

## Step 3 — Open Cowork
Have them open **Claude Desktop** and switch to the **Cowork** tab.
→ Confirm Cowork is open.

## Step 4 — Grant Cowork the exercise folder
In Cowork, have them **give Cowork access to the folder** `exercises/01-inbox-digest/`
with **read-write** access (so it can read the simulated data and write its output into
`project-storage/`). In Cowork this is done by connecting/granting a folder; pick
**read-write** (not read-only — the process needs to write its updates and summary).
→ Confirm the folder is granted with read-write access.

## Step 5 — Verify Cowork can read the data
Have them ask Cowork, in plain language:
> "In `simulated-inbox/inbox.json`, how many emails are unread and who are they from?"
Cowork should answer **6 unread** — from Maria Alvarez, Tom Becker, Greg Olsen, Sandra
Kim, Dave Russo, and a cold sender (Alex Trent). If it can't see the file, the folder
grant didn't take — return to Step 4.
→ Confirm Cowork read the inbox correctly.

## Done
Once Step 5 checks out, tell them they're set up: open
`exercises/01-inbox-digest/BRIEF.md` and start designing the process. Remind them to keep
Cowork in **"ask before acting"** mode — this exercise only reads and writes files in
the folder, and never sends email.
