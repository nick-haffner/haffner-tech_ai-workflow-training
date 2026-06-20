# Prerequisites — AI Workflow Training

> **Tentative** — this list was drafted during initial plugin setup and has not yet been
> fully validated against all exercises. A future `/ai-workflow-training:setup` skill will
> verify and install these automatically; update this file as gaps are found.

Everything a client needs installed before starting the training.

---

## Required for all clients

| Prerequisite | Why | How to get it |
|---|---|---|
| **Claude account** (Pro or Max) | Needed for Cowork and Claude Code | [claude.ai](https://claude.ai) |
| **Claude Desktop** | Cowork lives here; also the easiest way to get Claude Code | [claude.ai/download](https://claude.ai/download) |
| **Git** | Clone the repo and pull updates | [git-scm.com](https://git-scm.com/downloads) or via Claude Desktop |

**No Git?** You can download the repo as a ZIP from GitHub (green **Code** button →
**Download ZIP**). You'll need Git later to pull updates, so installing it is recommended.

---

## Required for Claude Code path only

| Prerequisite | Why | How to get it |
|---|---|---|
| **Claude Code** (`claude` in terminal) | The CLI that reads the project settings and auto-installs the plugin | Run `claude install latest` in a terminal, or use the Claude Desktop "Get Claude Code" button |

---

## Required for specific exercises

| Prerequisite | Exercise | Why | Notes |
|---|---|---|---|
| **Email account** (Gmail recommended) | Exercise 2 | Sends the morning briefing to you | Send to **your own address** during training — never a real contact |
| **Web search in Cowork** | Exercise 2 | Fetches news headlines | Toggle on in Cowork settings; no install needed |

---

## Required for Haffner side only (running `/onboard`)

| Prerequisite | Why | How to get it |
|---|---|---|
| **GitHub CLI (`gh`)** | Checks and manages collaborator access in Phase A | [cli.github.com](https://cli.github.com) |

---

## Not required (common misconceptions)

- **npm / Node.js** — not used in any exercise
- **Python** — the HTML viewers (`inbox.html`, `crm.html`) are pre-built; `_build_viewers.py` only needed if you modify the source data
- **LinkedIn account** — Exercise 2 uses a manual `personal-headlines.md` file instead of scraping
- **A real email inbox** — Exercise 1 uses simulated data only
