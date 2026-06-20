# AI Workflow Training — context & guardrails

This file loads when the **ai-workflow-training** plugin is active. It gives Claude
the shared rules for the training so the exercises stay safe and predictable.

## What this is

A hands-on training that teaches the learner to **design automated processes in
Claude Cowork**. The learner works through four exercises. The repository ships the
scaffolding (simulated data, viewers, briefs, templates) so the learner's only new
skill is **Cowork process design** — not repo/project architecture.

## Terminology

- A **project** is a self-contained folder where one automation is built. The
  learner creates their projects under `projects/`. (We say *project*, never *repo*,
  when talking about the learner's builds.)
- **Project storage** is the folder an automation reads/writes (its data + outputs).

## How Cowork fits

Cowork's agent loop and file access run locally, so Cowork can read and write files
in a **folder the learner grants it**. For these exercises the learner grants Cowork
access to the relevant exercise/project folder (read-write), then designs the process
against the files there. No real email account is required for Exercise 1 — it uses a
**simulated inbox and CRM** stored in this repo.

## Guardrails (always apply during the training)

1. **Ask before acting on anything irreversible** — sending email, deleting files,
   posting publicly. Prefer "ask before acting" mode while the learner is building.
2. **Never send practice emails to real people.** Use the learner's own address or a
   clearly-labeled test address. Real client/contact sends are out of scope here.
3. **Exercise 1 uses simulated data only** (`exercises/01-inbox-digest/`). Do not
   connect or read a real inbox for Exercise 1.
4. **Keep the learner in Cowork.** If something needs repo/project architecture for
   Exercises 1–2, it should already be scaffolded — point the learner at the existing
   files rather than having them design structure.
5. **Write outputs to the exercise's `project-storage/`** (Exercise 1) or the
   learner's project folder (Exercises 2–4), using the provided templates.

## Skills in this plugin

- `/ai-workflow-training:setup-exercise-1` — walk the learner through granting Cowork
  access to the Exercise 1 folder and confirming it can see the simulated data.
- `/ai-workflow-training:combine-projects` — teach what it means to combine two
  automations into a single project (used before Exercise 3).
