# Getting started

Welcome to the **Haffner Tech AI Workflow Training**. This guide orients you once the
plugin is installed (see `README.md` for install).

## The idea

You'll learn to **design automated processes in Claude Cowork** by doing four
exercises. Everything you need for the early exercises is already here — your job is
the Cowork process design, not setting up folders or formats.

## Key terms

- **Project** — a self-contained folder where you build one automation. You'll create
  your projects under `projects/` (Exercises 2–4). Exercise 1 is pre-built for you.
- **Project storage** — the folder an automation reads from and writes to.
- **Grant** — giving Cowork access to a folder so it can read/write the files there.

## How Cowork uses this folder

Cowork can work with files in a folder you **grant** it. For each exercise you'll
grant Cowork the relevant folder (read-write), then describe the process you want and
let Cowork build and run it against those files.

## The exercises

| # | Folder | What you build | Scaffolding |
|---|--------|----------------|-------------|
| 1 | `exercises/01-inbox-digest/` | A daily digest from a **simulated** inbox + CRM | Heavy — data, viewers, templates provided |
| 2 | `exercises/02-morning-briefing/` | A morning briefing (news + LinkedIn), as a **new project** you create under `projects/` | Light — you design the project |
| 3 | `exercises/03-integration/` | Combine 1 & 2 into one project + two short reports | You integrate; a teaching skill walks you through the concept first |
| 4 | `exercises/04-your-automation/` | Your own automation, start to finish | Minimal — it's yours |

Open each exercise's `BRIEF.md` to begin.

## Helpful commands (after install)

- `/ai-workflow-training:setup-exercise-1` — get Exercise 1 set up in Cowork (grant the
  folder, see the simulated data) with a step-by-step walkthrough.
- `/ai-workflow-training:combine-projects` — a short lesson on combining two automations
  into one project; run it before Exercise 3.

## Getting updates

New exercises and fixes arrive via:

```bash
git pull
```
