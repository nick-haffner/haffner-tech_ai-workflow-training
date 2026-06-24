# Exercise 1 — Daily Inbox Digest (Claude Cowork)

**Goal:** design a Cowork process that reads an inbox, pulls your notes on each
contact, writes a short update per open conversation, and gives you a daily summary —
running automatically every morning.

Everything you need is in this folder. You're learning **Cowork process design** — the
data, storage, and output format are already set up for you.

## What you have (simulated — no real accounts)
- `simulated-inbox/inbox.json` — a fake inbox of 12 messages.
- `simulated-crm/crm.json` — your notes on each contact.
- `viewer/inbox.html` and `viewer/crm.html` — double-click to **see** the data.
- `templates/conversation-summary.md` — the format your summary should follow.
- `project-storage/` — where your process writes its output.

## Start here
Run **`/ai-workflow-training:start-exercise-1`** — it verifies your setup, hands you your
contact data, and describes the end state you're building toward. (It won't tell you *how*
to build it — that's the exercise.)

## What to build (in Cowork)
Design a process that, each run:
1. **Reads the inbox** (`simulated-inbox/inbox.json`).
2. For each contact with activity, **reads your CRM notes** (`simulated-crm/crm.json`).
3. **Writes a brief update** (2–4 lines) per open conversation into
   `project-storage/updates/` — one file per contact.
4. **Outputs a summary** (as a Cowork artifact *and* saved to
   `project-storage/`) with two parts, using the template:
   - **(1) Where you are in open conversations** — each contact, their status, and the
     next action.
   - **(2) How many emails you should check** — the count that actually need you
     (skip newsletters, receipts, and cold outreach).
5. **Runs every morning** on a schedule (see `schedule.md`).

## Done when…
- [ ] Cowork can read the inbox + CRM from this folder.
- [ ] `project-storage/updates/` has one short update per open conversation.
- [ ] A summary artifact appears with the two sections, matching the template.
- [ ] The "emails to check" count excludes newsletter/receipt/cold messages.
- [ ] The process is scheduled to run daily.

## Guardrails
Read `GUARDRAILS.md` — it sets the storage paths, format, and naming so you don't have
to decide them. Keep Cowork in **"ask before acting"** mode; this exercise never sends
email.
