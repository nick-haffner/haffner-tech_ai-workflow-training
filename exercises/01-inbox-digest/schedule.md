# Exercise 1 — Running it daily

The last requirement is that your digest runs **every morning** on its own.

## Build it manually first
Before scheduling, run the process by hand a few times until the output looks right
(updates written, summary matches the template, the count is correct). Scheduling a
process that isn't working yet just produces broken output on a timer.

## Then schedule it in Cowork
In Cowork, set the process to run on a **daily cadence** (e.g., 7:00 AM). Cowork's
scheduling runs your saved process automatically.

- Pick a time before you start your day.
- Have it produce the **summary artifact** and write the day's `summary-YYYY-MM-DD.md`.
- Keep it in **"ask before acting"** mode — for this exercise it only reads and writes
  files in this folder, so it shouldn't need to ask for anything risky.

## Notes
- Scheduled runs are subject to your plan's limits (Pro and Max allow a number of
  scheduled runs per day — one daily digest is well within that).
- For your real inbox later (not this exercise), the same shape works — you'd just point
  the process at a Gmail connector instead of the simulated file.
