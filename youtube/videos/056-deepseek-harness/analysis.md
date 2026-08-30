# Analysis — DeepSeek Harness

## Source transcript analysis

### Reference: NeuralNine, "DeepSeek Harness: The End of Claude Code?" (222,377 views)
**Breakout confirmed:** NeuralNine's recent videos run 2.4k-10k views; his best recent agent videos hit 20k and 45k. This one at 222k is ~20-30x his channel norm and ~5x his next best. The topic is the engine, not the channel.

**Structure (13:31):**
| Time | Segment | Purpose |
|---|---|---|
| 0:00-0:58 | Hook: "everything is a plugin" + "everything is traceable" | Two-point promise, contrasts Anthropic hiding thinking |
| 0:58-2:36 | What it is: dev preview, Cordis, the paper (skips the math) | Framing |
| 2:36-3:35 | Install from source (git clone + pnpm) | Setup |
| 3:35-5:00 | Providers: DeepSeek key, OpenRouter, custom Ollama | Model connect |
| 5:00-7:06 | Run a Flask app + Trajectory view (the star) | Feature 1 |
| 7:06-9:00 | Plugin system: disable the sidebar via cordis.patch.yaml | Feature 2 |
| 9:00-11:15 | Creator mode: cat overlay + calculator plugin, live | Feature 3 |
| 11:15-12:45 | Providers again / Ollama GPT-OSS 120B, recap | Wrap |
| 12:45-end | CTA (services/tutoring) | Outro |

**What works:** the two-point hook is crisp; Trajectory demo is genuinely impressive and he lets it breathe; creator mode (cat + calculator) is a memorable "it built its own tool" moment; honest that it is a rough preview.

**Weaknesses / our opening:**
- **He never covers subagents.** No mention that Harness can call Claude Code / Codex. This is the single biggest gap and our hero beat.
- **He never covers the desktop app.** We add it (with the "it's third party" honesty).
- He installs **from source (pnpm)** which is dev-heavy. We lead with the simpler **`npx @deepseek-ai/dsh web`**.
- He is architecture-curious (spends time on the Cordis paper). We stay practical and add the "where it fits / honest verdict" framing he lacks.
- His CTA is a freelancing pitch; ours drives to the community + a sequel (orchestrating Claude Code on a real project).

**Audience:** his is developer-leaning and feature-tour. Ours is Claude Code users / builders, with an explicit "how it fits your existing stack" throughline - Tyler's lane and authority.

---

## Web research

### What it is (verified)
Open-source agent harness from DeepSeek, released **Aug 13, 2026**. The harness = the runtime around a model (tools, skills, sessions, planning, subagents, UI). ~201k stars / ~23k forks in ~2 weeks. MIT licensed. **Developer preview** - breaking changes expected.
- Repo: github.com/deepseek-ai/deepseek-harness. CLI: `dsh`.
- Install: `npx @deepseek-ai/dsh web` -> web UI at 127.0.0.1:3080. From source: `pnpm install && pnpm run build && pnpm dsh web`.

### Core idea: "everything is a plugin" (Cordis)
Built on the Cordis framework. Model, tools, skills, agent loop, session system, sandbox, and the UI are all swappable/toggleable plugins. Cordis paper = "A Programming Paradigm for Spatiotemporal Composability" (every action has an inverse; dynamic add/remove without side effects). Practical takeaway only - skip the math on camera.

### Standout features
- **Creator mode:** describe a plugin in chat -> it loads the Cordis plugin-dev skill, builds it, asks to confirm, installs it live in-session. The agent extends itself. Demos: cat overlay, calculator.
- **Trajectory view:** append-only log of everything the model saw (system prompt, user prompt, context, thinking, tool calls + payloads + results, timings). Inspect by source, replay, export the session as a .jsonl zip. LangFuse-style observability baked in. Opposite of Claude Code hiding thinking.
- **Subagent delegation (HERO):** ships subagent provider plugins that delegate to the Claude Code (and Codex) binary on your PATH, **disabled by default**. Enable the plugin -> it makes a tool call out to Claude Code, waits, folds the result back, keeps reasoning. Makes dsh an **orchestration layer above Claude Code**, not a replacement.
- **Model-agnostic:** default DeepSeek V3.1 (DeepSeek or OpenRouter key). Add providers in the models tab. **Local via Ollama** (custom provider -> fetch models) = free/unlimited. Note: cannot use a ChatGPT subscription login.
- Tools: read/search/edit files, Bash (Linux/macOS), PowerShell (Windows).

### How OpenRouter works (for the model-connect beat)
OpenRouter is a single API that aggregates hundreds of models from many providers (DeepSeek, Anthropic, OpenAI, Google, open models) behind **one account and one API key**. You add credit, pick a model, OpenRouter routes the request to that provider and takes a small margin. Benefit for Harness: paste one key, switch models from a dropdown, no separate account/key per provider. OpenAI-compatible, so it drops into Harness's "add provider" flow cleanly.

### Desktop app (caveat)
"DeepSeek Harness Desktop" is **NOT official**. Third-party Electron wrappers (GitHub: HaoyueQin, salathleizhang, fendouai) bundle the official `dsh web` UI into a native, tray-resident, zero-config app (no Node setup, one-click dsh updates). Convenient, but community-made - say so on camera.

### Honest rough edges (dev preview)
- Plugin enable/disable is still via a config file (`~/.dsh/profiles/web/cordis.patch.yaml`), not clicks yet.
- Generated plugins are rough (calculator buttons were unlabeled first try).
- Cannot connect a ChatGPT subscription (API keys or local only).
- Broader DeepSeek context: the models have had reliability/safety critiques and service strain; not harness-specific but fair to be measured.

### YouTube landscape (30 days, real views)
- NeuralNine 222k (setup + "end of Claude Code?"), Manolo Remiddi 78k (Qwen 27B local), Turing Post 70k, Nate Herk 68k (100 hours vs Claude Code), Jack Roberts 64k ("= Claude Code for $0"), Better Stack 64k, Caleb Curry 56k (crash course), Chase AI 41k, MG 41k ("Free Claude Code in 10 min"). Zero Shorts.
- Winning hooks: replacement ("end of Claude Code") + free/$0/any-model. Local Qwen-27B stack appears 3x.
- **Gaps:** no one leads on subagents; no one covers the desktop wrapper honestly; the honest engineer teardown is underdone (Nate's is the closest, 68k).

---

## Sources
- https://github.com/deepseek-ai/deepseek-harness
- https://deepseek.com/harness/en/
- https://www.mindstudio.ai/blog/deepseek-harness-coding-agent
- https://www.mindstudio.ai/blog/deepseek-harness-vs-claude-code-codex
- https://www.theregister.com/ai-and-ml/2026/08/14/deepseeks-innovative-harness-treats-everything-as-a-plug-in/
- https://github.com/shaokeyibb/dsh-plugin-product-subagents (subagent providers)
- https://www.datacamp.com/tutorial/deepseek-harness
- https://github.com/HaoyueQin/deepseek-harness-desktop (third-party desktop wrapper)
- Reference transcript: `~/content/transcripts/transcript_qg9EyGOZd9U.txt`
- YouTube search data: `~/content/research/2026-08-28-deepseek-harness.json` + `-thumbnails/`
