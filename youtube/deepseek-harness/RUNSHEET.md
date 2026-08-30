# RUNSHEET — DeepSeek Harness. Film from this page.

Verified against your machine 2026-08-30. Supersedes the ordering in `script.md`; the VO in
script.md is still good, the STRUCTURE below is the update.

## What changed, and why the video is now better

You discovered two things this afternoon that beat what was originally scripted:

1. **Your 25 existing Claude Code skills already work in dsh with zero porting.** dsh reads the
   same `.agents/skills` convention. Verified live: 26 skills in the catalog, `house-style` at
   #8, hyperframes/motion-graphics/talking-head-recut all there.
2. **You built a custom agent mode ("Tyler") that shows in the picker next to DeepSeek's four.**

And you earned a third thing the hard way: **you installed community plugins, hit a route
collision, and had to purge 479MB.** That is the honesty beat that separates this from the
222k-view hype pile. Do not hide it. Lead the plugin segment with it.

So the plugin segment flips: **not** "look how many plugins there are" but "I installed plugins,
it broke my install, here is the honest version." That is a better video and it is true.

---

## FIX BEFORE YOU ROLL (both still open, checked just now)

```
# 1. Ollama context. Quit the Ollama desktop app FIRST, then:
OLLAMA_CONTEXT_LENGTH=64000 ollama serve

# 2. dsh is not on PATH. You need it for `dsh web` and `dsh plugin`.
npm i -g @deepseek-ai/dsh && dsh --version
```
Then confirm state is clean: `bundles` = base + web-app, `cordis.patch.yml` = `[]`,
`dependencies` = none. All three verified clean right now, so do not install anything before
you roll.

**DECIDED 2026-08-30: keep the existing setup.** No `rm -rf ~/.dsh`. The Tyler preset and the
OpenRouter route stay. Beats 3 and 4 become **narration over what is already configured** rather
than a live wipe-and-redo.

What that changes on screen:
- The first-run "Configure later" dialog will NOT appear. Do not promise it. Instead say the line
  while showing Settings > Models: "on a fresh install it asks for a DeepSeek key, and there is a
  Configure later button. You never need one. Here is what mine looks like already."
- Beat 4 becomes a walkthrough of the existing OpenRouter route + **Open config file**, then the
  Ollama add done live (that one is genuinely new, so it still demos as a real setup).
- Still worth `cp -R ~/.dsh ~/.dsh.known-good` before you roll, purely as a restore point if the
  subagent patch in beat 8 breaks the boot.

---

## THE ORDER

| # | Beat | Target | Running |
|---|---|---:|---:|
| 1 | Hook | 0:25 | 0:25 |
| 2 | What a harness IS + everything is a plugin | 1:00 | 1:25 |
| 3 | Install | 1:00 | 2:25 |
| 4 | Models: OpenRouter + Ollama | 2:00 | 4:25 |
| 5 | Trajectory | 1:30 | 5:55 |
| 6 | **Your Claude Code skills already work** | 1:00 | 6:55 |
| 7 | **Your own mode (Tyler preset)** | 1:30 | 8:25 |
| 8 | **HERO: it runs Claude Code** | 1:30 | 9:55 |
| 9 | The honest plugin reality | 1:00 | 10:55 |
| 10 | Verdict | 1:00 | 11:55 |

---

### 1. Hook (0:30)
Use Hook 1 from `hooks.md` verbatim. Hard cut, no intro.
Say "**over** two hundred thousand stars" — it is 204,419.

### 2. What a harness IS, then everything is a plugin (1:00)
**Word-for-word VO in `harness-explainer.md`.** Model does nothing alone, text in text out. The
harness is the loop, the tools, the context strategy, permissions, the interface. "The model is
the engine, the harness is the rest of the car." You already use one: Claude Code, Codex, Cursor.
None of them open. This one does: 86 plugin rows, turn any of them off. "Alright, let's run it."
**Cut from here:** the Cordis paragraph, the "developer preview" caveat (moved to the first real
jank on screen), and the "in this video we'll cover" promise.

### 3. Install (1:00)
```
npx @deepseek-ai/dsh web        # UI at 127.0.0.1:3080
```
Desktop-app caveat: community wrappers, not official. B-roll `dataelement/dsh-desktop` (3.3k
stars), **not** the 7-star one in the old guide. Do not install it live.

### 4. Models (2:00) — full detail in `provider-setup.md`
The frame: a provider it ships is **one key**; a provider it never heard of is **three fields**.
- OpenRouter: Settings > Models > **Add provider** > `openrouter`. Already done on your machine,
  `deepseek/deepseek-v4-flash` is your default. Scroll the 39-provider list slowly.
- Ollama: **Add custom provider** (different button). Blank key, `http://127.0.0.1:11434/v1`,
  `openai-completions`, **Fetch available models**, `qwen3.8:27b-q8_0`, capacity **64000**.
- Payoff: **Open config file**. The secret is NOT in `settings.yaml`, it is a `refs:` entry in
  `.credentials.yaml`. "You can commit your harness config." Verified true, say it.

### 5. Trajectory (1:30)
Point at the `content` workspace, run a real task, open the **Trajectory** tab. Click into a
tool call: system prompt, context, thinking, payload, result, timings. "The opposite of Claude
Code hiding the thinking."

### 6. Your Claude Code skills already work (1:00) — NEW, do not cut this
This is the beat with the highest value for YOUR audience and nobody else has it.

[SHOW] `~/content/.agents/skills` in the terminal — 25 skills you wrote for Claude Code.
[SHOW] the live session listing **26 skills**, `house-style` at #8, hyperframes, motion-graphics,
talking-head-recut.

> "I did not port anything. dsh reads the same `.agents/skills` convention Claude Code does. Every
> skill I have already written works here, today, unchanged. That is what an open harness buys you
> that a sealed one cannot."

### 7. Your own mode (1:30)
The mode dropdown ships four: **Standard, PTC, Minimal, Creator.** (It is "PTC mode" in the UI,
not "Code mode" — say it right.)

[SHOW] the dropdown with **Tyler** sitting fifth, its description visible.
[SHOW] `~/.dsh/.agent-presets/tyler/` — `preset.yml` + `agent.cordis.yml`.

> "That is my agent. My house style in the persona, my toolset, my skills. It sits in the same
> picker as DeepSeek's own four modes because there is no difference between theirs and mine."

Honest note: authoring is **copy-only** — you copy a shipped preset's directory and edit on disk.
There is no create-from-scratch path. Say it, it is the kind of detail that reads as real use.

Merge Creator mode in here if you are long: Creator mode is the mode for *building* presets, so
show it as how you got here rather than as its own calculator-plugin demo.

### 8. HERO: it runs Claude Code (1:30) — see `record-prep.md`
`tool-subagent` already ships in your bundle with `disabled: true`. Flip it on in
`cordis.patch.yml`, set `permissionMode: acceptEdits` (default `dontAsk` DENIES and the demo
silently does nothing), install the provider, delegate, prove it in **Trajectory** + the files
on disk.

> "This is not Harness versus Claude Code. Harness becomes an orchestration layer above it."

### 9. The honest plugin reality (1:00) — REFRAMED
Do not demo installing a community plugin as a win. Tell the truth instead:

- **2,710 plugins across 23 categories.** Biggest: UI Enhancements 441, Tools 340, Development
  215. The one that matters: **Models & Providers (110)** — adapters that route dsh at
  subscriptions you already pay for.
- **It is three weeks old.** Every package checked was created Aug 13-22. One sidebar plugin
  shipped **19 versions in 17 days.** Land grab, not an ecosystem.
- **The popularity signals are gamed.** GitHub's `dsh-plugin` topic returns 12,747 repos and the
  top of the star ranking is reactive-resume, PicGo, NocoBase, MemOS — not dsh plugins at all.
  They tagged the topic for reach. Stars there are worthless for picking.
- **Nobody is reviewing these.** A plugin runs third-party code with your permissions, reads your
  files, uses your credentials. Tool approvals do not sandbox plugin code. There are **98 plugins
  in a Security & Permissions category, many of them malware scanners for other plugins.** An
  ecosystem that needs that many guards is telling you something.
- **And it broke my install.** Two plugin managers registered the same routes, dsh would not boot,
  and cleaning it took a 479MB store purge. Removed packages had also left state behind under
  unrelated names, including a third-party agent preset that kept loading.

> "So yes, everything is a plugin. That is the best thing about it and the most dangerous thing
> about it, and three weeks in, both are true at the same time."

This is your credibility segment. It is worth more than a calculator overlay.

### 10. Verdict (1:00)
Not replacing Claude Code today, it is a preview. But: see everything, any model including free
local, your existing skills work unchanged, your own modes, and it can drive Claude Code.
Recap card: **open source / any model + local / your skills already work / your own agent mode /
runs Claude Code.**
CTA: community for the config. Sequel ask — OpenDesign drives Harness drives Claude Code.

---

## If you run long, cut in this order
1. The Ollama beat (keep OpenRouter, mention local exists) — saves 60s
2. Creator mode as its own demo (fold into #7) — saves 60s
3. The desktop-wrapper caveat — saves 30s

**Never cut #6, #8, or #9.** Skills-already-work, the Claude Code hand-off, and the honest plugin
reality are the three things no competitor has.

## Do not say
- "Two hundred thousand stars" → say **over** two hundred thousand
- "Code mode" → it is **PTC mode**
- "Codex too" → codex is NOT installed on this machine
- "It calls the claude binary on your PATH" → true for the third-party subagent plugin, false for
  the official one (it uses the Agent SDK with your native Claude auth)
