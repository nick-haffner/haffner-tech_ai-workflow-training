# AI Workflow Training — Haffner Tech

A Claude plugin that loads the training's commands and guardrails into your AI environment,
so you can learn by doing.

---

## Before you start

You'll need:

- A **Claude** account (Pro or Max)
- **Claude Desktop** installed on your computer
- The **repository files** on your computer (clone or ZIP — see below)

See [`PREREQUISITES.md`](plugins/ai-workflow-training/PREREQUISITES.md) for a full list.

---

## Install — Claude Cowork

Cowork is a tab inside Claude Desktop. This is the primary path for the training.

**1. Get the repository files**

```bash
git clone https://github.com/nick-haffner/haffner-tech_ai-workflow-training.git
```

No git? Download the ZIP: green **Code** button on GitHub → **Download ZIP**, then unzip.

**2. Add the marketplace**

Open Claude Desktop → switch to the **Cowork** tab → open the **Customize** tab.

Click **Add Marketplace** and paste:

```
https://github.com/nick-haffner/haffner-tech_ai-workflow-training
```

**3. Install the plugin**

Find **ai-workflow-training** in the marketplace list and install it.

**4. Confirm**

Type `/` in Cowork — you should see the training commands.

---

## Install — Claude Code (terminal)

The repository carries its own settings so the plugin installs automatically when you
open the folder.

**1. Clone and open**

```bash
git clone https://github.com/nick-haffner/haffner-tech_ai-workflow-training.git
cd haffner-tech_ai-workflow-training
claude
```

**2. Approve the prompts**

Claude Code will ask you to confirm a few things the first time. Approve each:

- **Trust this folder?** → **Yes**
- **Add the `haffner-tech-ai-training` marketplace?** → **Yes**
- **Enable the `ai-workflow-training` plugin?** → **Yes**

You only do this once.

**3. Confirm**

Type `/plugin` → **Installed** tab — you should see **ai-workflow-training** listed.

---

## Getting updates

```bash
git pull
```

Run this inside the repo folder whenever new exercises or fixes are released.
Both Claude Code and Cowork pick up the changes automatically on next use.

---

## Optional: manual install (Claude Code)

If you prefer to skip the automatic prompts:

```
/plugin marketplace add nick-haffner/haffner-tech_ai-workflow-training
/plugin install ai-workflow-training@haffner-tech-ai-training
```

---

Questions? Reach out to **Haffner Tech**.
