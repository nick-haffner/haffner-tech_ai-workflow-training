---
name: onboard
description: Run on the Haffner machine to deliver this plugin to a client. Auto-runs the Haffner-side prep (sync to remote, validate the plugin, confirm access + share link), then walks the client through each install step ONE AT A TIME, pausing for confirmation after every step. Invoke from inside the haffner-tech_ai-workflow-training repo.
---

# /onboard — Client plugin-install walkthrough

**Purpose.** Guide a client through installing the ai-workflow-training plugin — either
via Claude Code (terminal) or Claude Cowork (Claude Desktop). You run on the
**Haffner machine**: do the our-side steps automatically, then coach the client
step-by-step.

**Fixed coordinates (use these exactly):**
- owner/repo: `nick-haffner/haffner-tech_ai-workflow-training`
- marketplace name: `haffner-tech-ai-training`
- plugin name: `ai-workflow-training`

## Operating rules
- **Phase A runs automatically** — perform all Phase A actions in one pass, then report a short PASS/FAIL summary.
- **Phase B: ask which path before starting** — Claude Code or Cowork. Then follow the relevant steps.
- **One step per response.** After presenting a step, **stop** and ask the operator to confirm the client finished it ("Reply `done` to continue, or tell me what happened"). **Do not present the next step until the operator confirms.** If something breaks, help troubleshoot, then re-confirm before advancing.
- Track which step you're on across turns. If re-invoked mid-walkthrough, ask which step the client is on and resume there.

---

## Phase A — This machine (automatic)

Run these now, in order, then summarize.

**A1 · Confirm location.** Verify the working directory is this repo (look for `README.md` and `.claude-plugin/marketplace.json`). If not, stop and tell the operator to `cd` into the repo root.

**A2 · Sync to remote.** Run `git status`. If there are uncommitted changes or unpushed commits, surface them and offer to commit & push so the client clones the latest. Do not push silently if changes look unexpected — confirm with the operator first.

**A3 · Validate the plugin.** Check that each of these exists and parses correctly:
- `.claude-plugin/marketplace.json` — must define marketplace `haffner-tech-ai-training` and plugin `ai-workflow-training`
- `plugins/ai-workflow-training/.claude-plugin/plugin.json`
- `.claude/settings.json` — must contain `extraKnownMarketplaces.haffner-tech-ai-training` and `enabledPlugins["ai-workflow-training@haffner-tech-ai-training"]`

Report PASS, or list exactly what's missing. **If anything is missing, warn the operator and stop here unless they explicitly say to continue anyway.**

**A4 · Access + share link.** Confirm the repo is public or the client has access:
```
gh api repos/nick-haffner/haffner-tech_ai-workflow-training/collaborators -q '.[].login'
```
If the client isn't listed, add them:
```
gh api -X PUT repos/nick-haffner/haffner-tech_ai-workflow-training/collaborators/<their-username>
```
Output the exact clone command to send the client.

When Phase A is done, announce: **"Haffner-side prep complete."**
Ask the operator: **"Is the client using Cowork (Claude Desktop) or Claude Code (terminal)?"**
Then present Step 1 of the matching path below.

---

## Phase B — Cowork path (Claude Desktop)

**Step 1 · Get the repository files.**
```
git clone https://github.com/nick-haffner/haffner-tech_ai-workflow-training.git
```
No git? Download the ZIP from the GitHub page (green **Code** button → **Download ZIP**) and unzip.
→ Confirm the folder is on their computer.

**Step 2 · Open Cowork.**
Open **Claude Desktop** → switch to the **Cowork** tab.
→ Confirm Cowork is open.

**Step 3 · Add the marketplace.**
Go to the **Customize** tab → click **Add Marketplace** → paste:
```
https://github.com/nick-haffner/haffner-tech_ai-workflow-training
```
→ Confirm the marketplace was added.

**Step 4 · Install the plugin.**
Find **ai-workflow-training** in the marketplace list and install it.
→ Confirm install is complete.

**Step 5 · Verify.**
Type `/` in Cowork — the training commands should appear, including
`/ai-workflow-training:exercise-1` and `/ai-workflow-training:combine-projects`.
→ Confirm commands are visible.

---

## Phase B — Claude Code path (terminal)

**Step 1 · Clone the repo.**
```
git clone https://github.com/nick-haffner/haffner-tech_ai-workflow-training.git
```
(or `gh repo clone nick-haffner/haffner-tech_ai-workflow-training`)
→ Confirm the folder downloaded.

**Step 2 · Open it in Claude Code.**
```
cd haffner-tech_ai-workflow-training
claude
```
→ Confirm Claude Code opened in the folder.

**Step 3 · Trust the folder.**
Claude Code asks to trust this workspace → client selects **Yes**.
→ Confirm.

**Step 4 · Add the marketplace.**
Claude Code prompts to add the `haffner-tech-ai-training` marketplace → **Yes**.
→ Confirm.

**Step 5 · Enable the plugin.**
Claude Code prompts to enable `ai-workflow-training` → **Yes**.
→ Confirm.

**Step 6 · Verify.**
Type `/plugin` → open the **Installed** tab → `ai-workflow-training` should be listed.
Then type `/` to see the training commands.
→ Confirm install verified.

---

## Completion

Once the final step is confirmed (either path), summarize:
- The plugin is installed and the training commands are live.
- Point the client at `GETTING-STARTED.md` for orientation and `exercises/01-inbox-digest/BRIEF.md` to begin.
- Remind them: updates arrive via `git pull` inside the repo folder.
