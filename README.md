# AI Workflow Training — Haffner Tech

A Claude Code **plugin** that sets you up to complete the Haffner Tech AI Workflow
Training homework exercises. Adding it drops the training's commands and scaffolding
straight into Claude Code, so you can learn by doing.

---

## Before you start

You'll need these (you already have them):

- A **Claude** account (Pro or Max)
- **Claude Code** installed on your computer
- A **GitHub** account with access to this repository

---

## Add it as a plugin (about 2 minutes)

This repository ships its own configuration, so Claude Code sets the plugin up
**for you** when you open it — there are no marketplace commands to memorize.

**1. Clone this repository to your computer**

```bash
gh repo clone nick-haffner/haffner-tech_ai-workflow-training
```

or, with plain git:

```bash
git clone https://github.com/nick-haffner/haffner-tech_ai-workflow-training.git
```

**2. Open the folder in Claude Code**

```bash
cd haffner-tech_ai-workflow-training
claude
```

**3. Approve the prompts**

Because this project carries its own settings, Claude Code will ask you to confirm
a few things the first time you open it. Approve each:

- **Trust this folder?** → **Yes**
- **Add the `haffner-training` marketplace** (from this repo)? → **Yes**
- **Enable the `ai-workflow-training` plugin?** → **Yes**

You only do this once.

**4. Confirm it installed**

Type `/plugin` and open the **Installed** tab — you should see
**ai-workflow-training** listed. Your training commands are now available; type `/`
to see them.

---

## Getting updates

When new exercises are released, pull the latest from inside the repo folder and
Claude Code picks up the changes:

```bash
git pull
```

---

## Optional: add it the "manual" way

If you'd rather add it the same way you'd add any plugin (handy if you ever set one
up for your company), you can skip the automatic prompts and do it by hand in
Claude Code:

```text
/plugin marketplace add nick-haffner/haffner-tech_ai-workflow-training
/plugin install ai-workflow-training@haffner-training
```

---

Questions? Reach out to **Haffner Technologies**.
