# Exercise 2 — Morning Briefing (you design the project)

**Goal:** every morning, gather the top news headlines and your LinkedIn "personal
headlines," produce a PDF briefing, store it, and email it to yourself — on a daily
schedule.

**New this time: you design the project.** In Exercise 1 the structure was built for
you. Here, *you* create the project. This is your first taste of project design — and
it's deliberately light.

## Set up your project
1. Create a new folder under `projects/`, e.g. `projects/morning-briefing/`.
2. Decide what goes in it — at minimum a place to **store the daily PDF**, and a small
   **config** (your email address, your news topics). Keep it simple; look at
   `exercises/01-inbox-digest/` if you want a reference for the shape of a project.
3. **Grant Cowork** your new project folder (read-write).
4. Turn on **web search** in Cowork. For email, send to **your own address** while
   practicing — never a real contact.

## About LinkedIn — read first
There's no supported, ToS-compliant way to auto-read your LinkedIn feed. Use the
fallback: keep a `personal-headlines.md` in your project and paste a few items into it
each morning, and have the process read that file. (Or build it news-only for now.)
See `shared/connectors.md`.

## What to build (in Cowork)
A process that each morning:
1. Searches the web for the top headlines on **your topics**.
2. Reads your `personal-headlines.md`.
3. Renders a **PDF** briefing (news + personal headlines).
4. Saves the PDF to your project's storage.
5. Emails it **to you**.
6. Runs on a **daily schedule**.

## Done when…
- [ ] You created a project folder under `projects/` and granted Cowork access.
- [ ] The process produces a PDF combining news + your personal headlines.
- [ ] The PDF is saved to your project storage and emailed to **your own address**.
- [ ] It's scheduled to run each morning.
