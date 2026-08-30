# DeepSeek Harness - Record Prep (re-verified 2026-08-30, day of record)

Everything needed to film clean. It's a dev preview, so some jank is expected - narrate it, that's the differentiator.

## Environment state (re-verified 2026-08-30 on this machine)
- OK node v26.5.0, npx 11.17.0 - `npx @deepseek-ai/dsh web` will run.
- OK `claude` resolves in a login shell to `~/.local/bin/claude` -> v2.1.251, authenticated. Required for the hero beat.
- **FIXED: `codex` is NOT installed.** Earlier note was wrong (it was a session shim, not a real binary). Either drop the "and Codex too" line or `npm i -g @openai/codex` before rolling. Do not promise Codex on camera unless you install it.
- OK Ollama running with **qwen3.8:27b-q8_0** (29 GB) + gemma4:e4b.
- **BLOCKER, STILL UNFIXED as of 2026-08-30 (re-checked after the OpenRouter setup):** Ollama is
  running from the desktop app with NO `OLLAMA_CONTEXT_LENGTH`. Verified `qwen3.8:27b-q8_0`
  supports 262,144 context but sets no `num_ctx`, so Ollama's 4096 server default applies. An
  agent loop dies at 4096. Default context is tiny and the agent loop will blow past it and thrash on camera. Before rolling: quit the Ollama app, then in a terminal run `OLLAMA_CONTEXT_LENGTH=64000 ollama serve` and leave it up.
- OK `~/.dsh` does NOT exist - first-run is genuinely fresh. If you rehearse, `mv ~/.dsh ~/.dsh.bak` before the real take.
- No pnpm - the from-source path won't work. Lead with `npx`, mention source only. Do not try it on camera.
- Port 3080 is free.

## Facts re-verified today (safe to say on camera)
- Repo is **`github.com/deepseek-ai/deepseek-harness`**, created **2026-08-13**, **204,419 stars**, pushed today. "Over two hundred thousand stars in about two weeks" is accurate.
- `@deepseek-ai/dsh` is at **0.1.1-rc.2, republished TODAY (2026-08-30)**. It is moving fast, so what you see may differ from any rehearsal. Say "release candidate" once and move on.
- Desktop wrapper B-roll: **do not use HaoyueQin/deepseek-harness-desktop (7 stars)**. Use **`dataelement/dsh-desktop` (3.3k stars)** or `dsh-tauri-desk/deepseek-harness-desktop` (1.4k). Still third party, still don't install it live.

## Plugins segment
**See `plugins-segment.md`** - the use -> disable -> install -> build -> orchestrate ladder, the real
plugin ids in your profile (86 of them), how `dsh plugin` works (it forwards to pnpm inside
`~/.dsh/profiles/web/`), and the third-party ecosystem list.

## Provider setup (OpenRouter + Ollama)
**See `provider-setup.md`** - exact click path and field values, pulled from the harness's own
llm-pi-ai README and the web app's UI test snapshots. Headlines: first-run key dialog has a
**"Configure later"** button (skip it, you never need a DeepSeek key); OpenRouter is a shipped
catalog provider so it is **"Add provider"** + one key; **Ollama is NOT in the catalog** so it is
the separate **"Add custom provider"** button + base URL + protocol + a model list. Also check the
UI language in the dry run - every UI snapshot in the repo is Chinese (Settings > General has a
Language row).

## Keys to have ready (paste, don't fumble)
- [ ] **DeepSeek API key** (platform.deepseek.com → API keys) OR
- [x] **DONE 2026-08-30.** OpenRouter is configured and `deepseek/deepseek-v4-flash` is the default
  model. Verified in `~/.dsh/settings.yaml`. The secret is NOT in settings.yaml - it is a `refs:`
  entry in `~/.dsh/.credentials.yaml`, which is exactly the "you can commit your harness config"
  line in the script. That line is now confirmed true, say it.
- [ ] Still worth 10 dollars of OpenRouter credit if you have not: free models cap at 50 req/day
  under that and an agent loop will stall.
- [ ] Apify not needed for this video.

## The ONE risky beat - subagent enable (READ THIS, the old version was incomplete)

I pulled the actual READMEs. Both paths work, but they are **not** the same tool and the script's VO currently describes B while naming A.

### Option A - official `@deepseek-ai/dsh-subagent-claude-code` (v0.0.1-rc.1)
Real, shipped by DeepSeek, best credibility line. **Installing it is NOT enough** - it registers a *dormant* provider. Two more things are required:

1. Install into the profile, then restart it:
```
dsh plugin --profile web add @deepseek-ai/dsh-subagent-claude-code
dsh --profile web
```
2. **Enable the delegation tool.** SIMPLER THAN I FIRST WROTE: `tool-subagent` **already ships in
   your web-app bundle**, just with `disabled: true` (so does `tool-subagent-fork`). And
   `ui-subagent` ships **enabled**, so there IS a subagent activity surface in the UI already -
   you are not blind during the hand-off after all. So the minimum patch is to flip it on in
   `~/.dsh/profiles/web/cordis.patch.yml`:

```yaml
- id: tool-subagent
  disabled: false
  config:
    provider: claude-code
    toolName: subagent_claude_code
    backgroundMode: one-shot
    permissionMode: acceptEdits
```

   The longer hand-authored form, if the flip-on does not take:
```yaml
- id: jobs
  name: '@deepseek-ai/dsh-jobs-local'
- id: tool-jobs
  name: '@deepseek-ai/dsh-tool-jobs'
- id: tool-subagent-claude
  name: '@deepseek-ai/dsh-tool-subagent'
  config:
    provider: claude-code
    toolName: subagent_claude_code
    backgroundMode: one-shot
    maxDepth: provider-managed
    permissionMode: acceptEdits
```
   (The full Agent Presets already ship this row with `disabled: true` - copying a preset and deleting that line is the faster on-camera move.)
3. **`permissionMode` defaults to `dontAsk`, which DENIES anything not already authorized.** Leave the default and your delegated task will come back having done nothing. Set `acceptEdits` (or `bypassPermissions`) or the hero beat dies on camera.

Two facts that change the SHOT:
- It does **not** read your PATH and does **not** call your host `claude` binary. It ships a pinned Agent SDK + CLI payload and uses your native `~/.claude` settings and login. So **cut the line "it delegates to the Claude Code binary on your PATH"** if you use Option A - it is wrong.
- It is **one-shot and opaque**: Claude Code's reasoning, tool activity and intermediate messages **never enter the parent session**. You get one tool call and one final answer. Do not sit there waiting for a live stream that is never coming.

### Option B - third-party `dsh-plugin-product-subagents` (v0.3.1) - better VISUAL
```
dsh plugin --profile web add dsh-plugin-product-subagents
```
Registers via `~/.dsh/profiles/web/cordis.patch.yml`:
```yaml
- id: product-subagents
  config:
    idleTimeoutMs: 600000
    providers:
      claude-code: { type: product, command: claude }
```
This one **does** shell out to the authenticated `claude` on your PATH (so the PATH line is true here), children are continuable, and it exposes `product_delegate`, `product_wait`, `product_agents` and **`subagent_progress` (status + internal trace)** - which is the only path that gives you something moving to point at.

### RECOMMENDATION
Install **A** on camera (it is the honest headline: DeepSeek officially ships a Claude Code subagent provider), and **prove the hand-off in the Trajectory tab** - the delegation tool call, its payload and the returned answer are all right there. That is the elegant move: you already taught Trajectory at 5:00, so the hero beat pays it off instead of needing a new visual. Then show the workspace diff (`git status` / the new files) as physical proof the child actually did the work.

If A fights you, fall back to **B** and use `subagent_progress`. Mention A exists either way.

> DRY RUN whichever one before the real take, then `rm -rf ~/.dsh` to get the fresh first-run back.

---

## THE RECORD (in order) - full shot list

**Hook (0:00-0:30)** - name the hype, kill it, land 3 payloads (open source / free local / runs Claude Code), promise the how-to. Hard cut, no intro.
> "Half of YouTube is telling you DeepSeek Harness is the end of Claude Code. It's not. But..."

**1. What it is (0:30-2:00)**
[SHOW] deepseek.com/harness + the repo star count. Teach "harness = the runtime around a model." Big idea: everything is a plugin (model, tools, skills, agent loop, UI). One line on Cordis, do NOT open the paper.

**2. Install + desktop caveat (2:00-3:30)**
```
npx @deepseek-ai/dsh web
```
Opens UI at `127.0.0.1:3080`. Then the honest note:
> "You'll see a DeepSeek Harness desktop app - heads up, it's not official, it's a community wrapper. Convenient, just know it's third party." (5s B-roll of a wrapper repo, don't install it.)

**3. Connect a model (3:30-5:00)**
[SHOW] Settings > Models > Add provider. Explain OpenRouter plainly (one key, hundreds of models, it routes + takes a cut). Paste key, pick a model. Then the FREE path:
[SHOW] add custom provider → Ollama (`http://127.0.0.1:11434/v1`, blank key) → fetch → pick **qwen3.8:27b**.
> "Now I'm running a coding agent completely locally. No key, no per-token cost."
Honest beat: can't use a ChatGPT subscription login.

**4. Trajectory (5:00-6:45)**
[SHOW] point at a workspace, run:
```
Create a simple Flask to-do app.
```
Open the **Trajectory** tab. Click into a tool call - system prompt, context, thinking, the bash call, payload, result, timings.
> "Every single thing the agent did. The opposite of Claude Code hiding the thinking."
Show export session as a zip.

**5. Creator mode (6:45-8:30)**
[SHOW] switch agent preset to **Creator mode**. Type:
```
Add a plugin for a calculator overlay in the bottom right. A simple GUI calculator.
```
It loads the Cordis plugin skill, builds it, asks to confirm. Approve. Calculator appears.
> "A working tool I never coded. I just described it." (If it's rough, KEEP it and say so.)

**6. HERO - Claude Code as subagent (8:30-10:30)** - slow down here
[SHOW] diagram: dsh → Claude Code → result back. Enable the plugin (see the risky-beat section above), then in a session delegate a task to Claude Code, show the hand-off and the result folding back in.
> "This isn't Harness versus Claude Code. Harness becomes an orchestration layer above it. That's the combination I'd actually run."

**7. Verdict (10:30-12:00)**
Honest close: not replacing Claude Code today (it's a preview, rough in spots), but if you want full transparency, any model incl free local, and composability - most exciting thing out. And it can drive Claude Code, so you don't have to choose.
Recap card: open source / any model + local / everything a plugin / builds its own tools / runs Claude Code.
CTA: community for commands + subagent config. Ask if they want a real-project build orchestrating Claude Code (the sequel).

---

## Copy-paste block
```
# fresh first-run check (before real take)
ls ~/.dsh || echo "fresh - good"        # if it exists: mv ~/.dsh ~/.dsh.bak

# install + run (on camera)
npx @deepseek-ai/dsh web                 # UI at 127.0.0.1:3080

# local model (free) - in the UI: Settings > Models > Add provider > custom
#   base URL http://127.0.0.1:11434/v1 , blank key, fetch, pick qwen3.8:27b
# (ollama already running with qwen3.8:27b + gemma4)

# Flask task (Trajectory demo)
Create a simple Flask to-do app.

# Creator mode task
Add a plugin for a calculator overlay in the bottom right. A simple GUI calculator.

# SUBAGENT (rehearse first) - option A official:
dsh plugin --profile web add @deepseek-ai/dsh-subagent-claude-code
# or option B third-party:
dsh plugin --profile web add dsh-plugin-product-subagents
#   then in session: product_delegate role=general task="..."  /  product_wait subagent_id=<id>
```

## Guardrails
- Dev preview = jank is fine, narrate it. That honesty is the whole edge vs the hype pile.
- Two money shots: Trajectory (full transparency) + the subagent hand-off (Claude Code running inside Harness). Let both breathe, speed-ramp waits.
- Cover it THIS week - the term is peaking.
- Don't imply you're not a developer - lean into the engineer read.

## Script deltas to say out loud (from today's verification)
- 8:30 beat: **delete** "It delegates to the Claude Code binary that is already on your PATH" if using Option A. Replace with: "It runs a real Claude Code session using your existing Claude login and settings, isolated from the harness."
- 8:30 beat: **delete** "show Claude Code working." You cannot see it. Replace with: tool call goes out, answer comes back, then open Trajectory and show the payload, then show the files it wrote.
- Say "over two hundred thousand stars", not "two hundred thousand" (it is 204k and climbing).
- Only promise Codex if you install it first.
