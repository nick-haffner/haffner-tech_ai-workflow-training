# Exercise 1 — Guardrails

These are pre-decided so you can focus on the **Cowork process**, not the setup.

## Data (don't change)
- **Read** the inbox from `simulated-inbox/inbox.json` and notes from
  `simulated-crm/crm.json`. These are simulated. **Do not connect a real email account
  for this exercise.**

## Where output goes
- **Per-contact updates:** `project-storage/updates/<contact-id>.md`
  (e.g., `project-storage/updates/c-maria.md`). 2–4 lines each.
- **Daily summary:** `project-storage/summary-YYYY-MM-DD.md`, *and* shown as a Cowork
  artifact.

## Format
- The summary must follow `templates/conversation-summary.md` (two sections:
  open conversations, then emails-to-check count).
- "Emails to check" = messages that need a human reply/decision. **Exclude** newsletters,
  receipts, and cold outreach (in the sample: the Marketing Brief, Figma receipt, and the
  "Partnership opportunity" cold email).

## Behavior
- Run Cowork in **"ask before acting"** mode while building.
- This exercise **never sends email** and **never deletes** anything — it only reads the
  simulated data and writes into `project-storage/`.

## If you want to reset
Delete the files inside `project-storage/updates/` and any `summary-*.md` and re-run.
The simulated inbox/CRM are read-only inputs — leave them as they are.
