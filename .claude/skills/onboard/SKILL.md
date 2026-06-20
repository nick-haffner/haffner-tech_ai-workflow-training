---
name: onboard
description: Run on the Haffner machine to deliver this plugin to a client (e.g., Brennan). Auto-runs the Haffner-side prep (sync to remote, validate the plugin, confirm access + share link), then walks the client through each install step ONE AT A TIME, pausing for confirmation after every step. Invoke from inside the haffner-tech_ai-workflow-training repo.
---

# /onboard — Client plugin-install walkthrough

**Purpose.** Guide a client through adding this repo as a Claude Code plugin via the
project-settings flow (Option 1: clone → open → approve prompts). You run on the
**Haffner machine**: do the our-side steps automatically, then coach the client
step-by-step.

**Fixed coordinates (use these exactly):**
- owner/repo: `nick-haffner/haffner-tech_ai-workflow-training`
- marketplace name: `haffner-training`
- plugin name: `ai-workflow-training`

## Operating rules
- **Phase A runs automatically** — perform all Phase A actions in one pass, then report a short PASS/FAIL summary.
- **Phase B is interactive and confirmation-gated** — present **exactly ONE step per response**. After presenting a step, **stop** and ask the operator to confirm the client finished it ("Reply `done` to continue, or tell me what happened"). **Do not present the next step until the operator confirms.** If something breaks, help troubleshoot, then re-confirm before advancing.
- Track which step you're on across turns. If re-invoked mid-walkthrough, ask which step the client is on and resume there.

## Phase A — This machine (automatic)
Run these now, in order, then summarize:

**A1 · Confirm location.** Verify the working directory is this repo (look for `README.md` and `.claude-plugin/marketplace.json`). If not, stop and tell the operator to run from the repo root.

**A2 · Sync to remote.** Run `git status`. If there are uncommitted changes or unpushed commits, surface them and offer to commit & push so the client clones the latest. Do not push silently if changes look unexpected — confirm with the operator first.

**A3 · Validate the plugin.** Check that each of these exists and parses:
- `.claude-plugin/marketplace.json` (defines the `haffner-training` marketplace + the `ai-workflow-training` plugin)
- `plugins/ai-workflow-training/.claude-plugin/plugin.json`
- `.claude/settings.json` with `extraKnownMarketplaces` (haffner-training) and `enabledPlugins` (`ai-workflow-training@haffner-training`: true)

Report PASS, or list exactly what's missing. **If anything is missing, warn that the client's install prompts won't fully fire until the plugin is built — and stop here unless the operator explicitly says to continue the walkthrough anyway.**

**A4 · Access + share link.** Confirm the client has read access:
`gh api repos/nick-haffner/haffner-tech_ai-workflow-training/collaborators -q '.[].login'`
If the client isn't listed, tell the operator to add them
(`gh api -X PUT repos/nick-haffner/haffner-tech_ai-workflow-training/collaborators/<their-username>`)
or make the repo public. Then output the exact clone command to send the client.

When Phase A is done, announce: **"Haffner-side prep complete — beginning the client walkthrough,"** and present **Phase B Step 1 only.**

## Phase B — Client machine (one step per response, confirm-gated)
For each step, give: what the client does, the exact command(s), and what they'll see on screen. Then pause for confirmation.

**Step 1 · Clone the repo.**
`gh repo clone nick-haffner/haffner-tech_ai-workflow-training`
(or `git clone https://github.com/nick-haffner/haffner-tech_ai-workflow-training.git`)
→ Confirm the folder downloaded.

**Step 2 · Open it in Claude Code.**
`cd haffner-tech_ai-workflow-training` then `claude`
→ Confirm Claude Code opened in the folder.

**Step 3 · Trust the folder.** Claude Code asks to trust this workspace → client selects **Yes**.
→ Confirm.

**Step 4 · Add the marketplace.** Claude Code prompts to add the `haffner-training` marketplace (from this repo) → **Yes**.
→ Confirm.

**Step 5 · Enable the plugin.** Claude Code prompts to enable `ai-workflow-training` → **Yes**.
→ Confirm.

**Step 6 · Verify.** Client types `/plugin`, opens the **Installed** tab — `ai-workflow-training` should be listed. Then types `/` to see the training commands.
→ Confirm install verified.

## Completion
Once Step 6 is confirmed, summarize: the plugin is installed, list the training commands now available, point the client at the first exercise, and remind them updates come via `git pull` inside the repo folder.
