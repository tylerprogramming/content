# Filming Guide — DeepSeek Harness

The do-this / click-that version. It's a developer preview, so things WILL be a little rough on camera - that's on-brand, narrate it honestly. Target ~11-13 min.

## Pre-recording setup
- [ ] **Node installed** (for `npx`). Confirm `node -v`.
- [ ] **Ollama installed + a tool-capable model pulled** (e.g. `ollama pull qwen3`) for the free/local beat. Start it: `OLLAMA_CONTEXT_LENGTH=64000 ollama serve` (agents need >=64k context).
- [ ] **A DeepSeek API key OR an OpenRouter key** with a little credit, ready to paste for the cloud demo. (OpenRouter is the cleaner on-camera story - one key, many models.)
- [ ] **Claude Code installed and on your PATH** - REQUIRED for the hero subagent beat. Confirm `which claude`.
- [ ] (Optional) **Codex CLI** installed too, if you want to show the second subagent provider.
- [ ] A clean **workspace folder** to point Harness at (throwaway, so the Flask build is clean).
- [ ] Browser tabs pre-opened: github.com/deepseek-ai/deepseek-harness, deepseek.com/harness, openrouter.ai, one desktop-wrapper repo (HaoyueQin/deepseek-harness-desktop).
- [ ] Decide: show the third-party desktop app or just mention it. (Recommend: mention + 5s B-roll, don't install live.)

## Timing cheat sheet
| Section | Target | Running |
|---|---:|---:|
| Hook | 0:30 | 0:30 |
| What it is | 1:30 | 2:00 |
| Install + desktop caveat | 1:30 | 3:30 |
| Connect a model (OpenRouter / local) | 1:30 | 5:00 |
| Feature 1: Trajectory | 1:45 | 6:45 |
| Feature 2: Creator mode | 1:45 | 8:30 |
| HERO: Claude Code as subagent | 2:00 | 10:30 |
| Where it fits + verdict | 1:30 | 12:00 |

---

## Step 1 — Hook (to 0:30)
Name the hype, kill it honestly, land the 3 payloads (open source / free local / runs Claude Code), promise the how-to. Hard cut, no intro.
> "Half of YouTube is telling you DeepSeek Harness is the end of Claude Code. It's not. But it is the most interesting thing to happen to coding agents this year..."

## Step 2 — What it is (to 2:00)
[SHOW] deepseek.com/harness. Teach "harness = the runtime around a model." Then the one big idea: everything is a plugin (list: model, tools, skills, agent loop, UI).
> "Claude Code is a sealed box. This is the opposite."
Keep Cordis to one line. Do NOT open the paper on camera.

## Step 3 — Install + desktop caveat (to 3:30)
[SHOW] terminal:
```
npx @deepseek-ai/dsh web
```
Opens the UI at `127.0.0.1:3080`. (From source is `pnpm install && pnpm run build && pnpm dsh web` - mention as the alternative, don't do it live.)
Then the honest desktop note:
> "You'll see a DeepSeek Harness desktop app. Heads up - it's not official, it's a community wrapper around this same web UI. Convenient, just know it's third party."
[SHOW] 5s B-roll of a wrapper repo. Don't install it live.

## Step 4 — Connect a model (to 5:00)
**Full click-by-click with exact field values lives in `provider-setup.md`. Read that, not this.**
Short version:
1. First-run dialog asks for a DeepSeek key -> click **"Configure later"**. You never need one.
2. **Settings > Models > "Add provider"** -> pick **`openrouter`** from the 39-provider dropdown -> paste key -> Save. Scroll that dropdown slowly on camera, the length is the point.
3. **Settings > Models > "Add custom provider"** (different button!) -> blank key, name `Ollama`, base URL `http://127.0.0.1:11434/v1`, protocol `openai-completions` -> **"Fetch available models"** -> keep `qwen3.8:27b-q8_0` -> set its capacity to **64000** -> Save.
4. Switch the composer model dropdown cloud -> local. No restart needed, config is re-read per request.
5. Click **"Open config file"** and show the YAML both forms just wrote. That is the "everything is a plugin" payoff.
[NOTE] honest beat: no ChatGPT/Claude subscription login. API keys, provider OAuth, or local.
[NOTE] pre-roll blocker: quit the Ollama app, run `OLLAMA_CONTEXT_LENGTH=64000 ollama serve`.
[NOTE] check the UI language in the dry run. Repo UI snapshots are all Chinese; switch it in Settings > General if needed.

## Step 5 — Feature 1: Trajectory (to 6:45)
[SHOW] point it at your workspace, run:
```
Create a simple Flask to-do app.
```
Let it finish, then open the **Trajectory** tab.
[SHOW] the graphical step timeline; click into a tool call - show system prompt, context, thinking, the bash call, the exact payload, the result, timings.
> "This is every single thing the agent did. The opposite of Claude Code hiding the thinking. As an engineer, this is the feature I didn't know I wanted."
[SHOW] export session as a zip (the session.jsonl) to prove it's all there.

## Step 6 — Feature 2: Creator mode (to 8:30)
[SHOW] switch agent preset to **Creator mode**. Type:
```
Add a plugin for a calculator overlay in the bottom right. A simple GUI calculator.
```
[SHOW] it loads the Cordis plugin-dev skill, builds the plugin, asks to confirm. Approve it. The calculator appears in the corner.
> "That's a working tool I never coded. I just described it. Is it polished? No, this is a preview. But the agent just extended itself."
[NOTE] if it's rough (unlabeled buttons like NeuralNine's), KEEP it and say so. Rough-but-real is the tone.
[SHOW] optional: also do the sidebar-disable via `~/.dsh/profiles/web/cordis.patch.yaml` (`- id: ui-sidebar` / `disabled: true`) to show "even the UI is a plugin" - only if pacing allows.

## Step 7 — HERO: Claude Code as a subagent (to 10:30)
This is the beat nobody else has. Slow down here.
[SHOW] diagram: dsh in the middle -> Claude Code -> result back.
> "DeepSeek Harness can call Claude Code as a subagent. So it orchestrates it instead of replacing it."
[SHOW] enable the subagent / Claude Code provider plugin (it's shipped but disabled by default). It delegates to the `claude` binary on your PATH.
> "If you have Claude Code installed, Harness can just call it."
[SHOW] in a session, ask it to delegate a task to Claude Code. Show the tool call hand off, Claude Code working, the result folding back into the Harness session, and it continuing on top.
> "This isn't Harness versus Claude Code. Harness becomes an orchestration layer above it. That's the combination I'd actually run."
[NOTE] Have the exact enable step confirmed BEFORE rolling - subagent providers are shipped disabled; know precisely which plugin/config flips them on so you don't fumble. If it won't cooperate on camera, show the config + one clean delegation and speed-ramp.

## Step 8 — Where it fits + verdict (to 12:00)
Honest engineer close.
> "Is this replacing Claude Code today? No. It's a preview, it's rough in places. But if you want to see everything your agent does, run any model including free local ones, and compose tools instead of being locked in, this is the most exciting thing out right now. And it can drive Claude Code, so you don't even have to choose."
[SHOW] recap card: open source / any model + local / everything a plugin / builds its own tools / runs Claude Code.
CTA: community for the commands + subagent config; ask in comments if they want a real-project build orchestrating Claude Code with it (the sequel).

---

## On-camera tips
- It's a dev preview - if something is janky, narrate it. Honesty is the whole differentiator vs the hype videos.
- The two money shots: the Trajectory view (full transparency) and the subagent hand-off (Claude Code running inside Harness). Let both breathe, speed-ramp any waits.
- Don't imply you're not a developer - lean into the engineer read on transparency + orchestration.
- Cover it THIS week - the term is peaking now.

## Commands quick-reference
```
# install + run
npx @deepseek-ai/dsh web            # UI at 127.0.0.1:3080
# from source (alt)
git clone https://github.com/deepseek-ai/deepseek-harness && cd deepseek-harness
pnpm install && pnpm run build && pnpm dsh web

# local model (free)
ollama pull qwen3
OLLAMA_CONTEXT_LENGTH=64000 ollama serve
# in Harness: Settings > Models > Add provider > custom > http://127.0.0.1:11434/v1 (blank key) > fetch

# plugin toggle (config, dev-preview way)
# ~/.dsh/profiles/web/cordis.patch.yaml
#   - id: ui-sidebar
#     disabled: true

# subagent: ensure Claude Code is on PATH
which claude
# then enable the shipped-but-disabled Claude Code subagent provider plugin
```
