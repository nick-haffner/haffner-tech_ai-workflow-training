# Connectors & access, by exercise

What Claude Cowork needs access to for each exercise. "Granting a folder" means
pointing Cowork at a folder on your computer so it can read/write the files there.

## Exercise 1 — Inbox digest (simulated, no real accounts)
- **Grant Cowork the folder** `exercises/01-inbox-digest/` (read-write).
- That's it — the inbox and CRM are **simulated files** in that folder. **Do not**
  connect your real email for this exercise.
- The walkthrough `/ai-workflow-training:setup-exercise-1` does this with you.

## Exercise 2 — Morning briefing (real sources)
You'll build this as a new project under `projects/`. You'll likely want:
- **Web search** — enabled in Cowork (for news headlines). Built in; no setup beyond
  having it on.
- **Email send** — a **Gmail connector**, or have Cowork draft into a file you send
  yourself. **Send the briefing to your own address while practicing**, never a real
  contact.
- **Grant Cowork your project folder** (read-write) so it can store the daily PDF.

### LinkedIn — read this before you start
There is **no supported, ToS-compliant connector** for automatically reading your
LinkedIn feed / "personal headlines." Don't try to automate LinkedIn scraping. Use one
of these instead:
- **Manual input (recommended):** keep a `personal-headlines.md` file in your project
  and paste a few items into it each morning; have the process read that file.
- **Scope it out:** build the briefing from news only for now.

## Exercises 3 & 4 — your projects
Grant Cowork the relevant project folder under `projects/`. Add connectors only as your
own design requires — and keep the "send to yourself while practicing" rule.

## The golden rule
While you're learning, run Cowork in **"ask before acting"** mode and keep any email
output pointed at **your own address**. Nothing irreversible should happen without your
explicit OK.
