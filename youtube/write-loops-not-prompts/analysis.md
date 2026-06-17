# Analysis: Write Loops, Not Prompts

**Video slug:** `write-loops-not-prompts`
**Date planned:** 2026-06-13
**Format:** Long-form, 12-15 min, creators/solopreneurs audience
**Hero demo:** A real content-pipeline loop running the business

---

## Source Transcript Analysis

Primary reference: **"How Anthropic Engineers ACTUALLY Prompt Claude Code"** — Austin Marchese, 467K views, 10:45 (`transcript_qOvc9IUKEIc.txt`). This is the borrowed-authority listicle that beat Anthropic's own channel at its own topic.

Secondary references:
- **"How Claude Code Works"** — Claude (official), 359K, 2:50 (`transcript_6bs5b4FltCU.txt`) — the agentic-loop explainer.
- **"Explore → Plan → Code → Commit"** — Claude (official), 281K, 3:11 (`transcript_xJQuF02NAK8.txt`) — the workflow video.

### Structure breakdown (Austin, #1)

| Time | Segment | Purpose |
|------|---------|---------|
| 0:00-0:17 | Hook: "I listened to Anthropic's engineers... almost everyone is prompting Claude Code wrong" | Curiosity gap + borrowed authority + "you're doing it wrong" threat |
| 0:17-1:07 | Foundation: the mental shift (prompts → skills) | Reframe before tactics |
| 1:07-2:02 | Rule 1: prompt skills, not Claude (the 3-layer abstraction: models → agents/prompts → skills) | Teaching with a visual model |
| 2:02-4:30 | Rule 2: skills are more than prompts (description / instructions / tools layers) | Depth + insider clips |
| 4:30-6:25 | Rule 3: composable, not custom skills | His own content-engine story as proof |
| 6:25-8:25 | Patterns: save scripts inside skills; user-invocable / disable-model-invocation flags | Concrete power-user tactics |
| 8:25-9:36 | Rule 4: prompts get smarter every session (the compounding loop) | The payoff: compounding |
| 9:36-end | Recap of 4 rules + CTA to next video | Clean finite close |

### What works well (steal these)

- **Borrowed authority.** He never claims to be the expert — he studied what Anthropic engineers said and repackaged it. Viewer gets the insider secret with zero risk. The word "ACTUALLY" sells "you've been doing it wrong."
- **One mental model, not a feature list.** The whole video sells a single reframe: *stop thinking in prompts, start thinking in skills.* Everything hangs off that.
- **A visual abstraction ladder.** Layer 1 models → Layer 2 agents/prompts → Layer 3 skills ("the app layer"). The phone analogy ("Anthropic builds the phone, you build the apps") makes it sticky.
- **His own story as proof.** The "I built one giant /content skill and it became unmanageable, so I split it up" story is the most relatable beat — it's exactly Tyler's world.
- **Numbered, finite promise.** "4 rules" = clear finish line = retention.
- **Compounding payoff.** Ends on "Claude on day 30 is better than day 1" — the emotional reason to care.

### Weaknesses / gaps (our opportunities)

- **It stops at skills.** Austin's video is about *skills* as the unit. The newer, hotter abstraction — the one Boris Cherny went viral for in June — is the **loop**. Skills are the thing the loop *calls*. We go one layer up. That's our entire differentiation.
- **Zero on-screen "running" footage.** It's mostly talking-head + slides + clips. Nobody in the top results actually shows a loop *running their business unattended*. Tyler can.
- **Developer-coded.** Even Austin's "non-technical" framing still uses domain-checking dev examples. The creator/solopreneur translation is wide open.
- **No "while you sleep" emotional payoff shown, only told.** We can literally show a morning where the work is already done.

### Target audience of the source

Austin's video targets ambitious AI-curious people, framed as "you don't need to be technical." It assumes light familiarity with Claude Code. Our video narrows to **creators and solopreneurs** specifically and goes concept-first with minimal code.

---

## Web Research: Loop Engineering (June 2026)

### The viral moment we're riding

> "I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops." — **Boris Cherny, Head of Claude Code, Anthropic**

That clip hit ~700K views in roughly 24 hours and kicked off "loop engineering" as the new meta. This is *fresh* (June 2026) and not yet saturated on YouTube — only a handful of creators (Sean Kochel, Ray Amjad) have touched it, and none from the creator-business angle.

### What "loop engineering" actually means

- The unit of work moved: **keystroke → prompt → loop.** A prompt gets you one output; a loop gets you a compounding operation.
- A loop is a harness that: **figures out what work exists → hands a chunk to an agent → checks what came back → repeats.**
- The shift: stop being the thing *in* the loop. Write the loop once, then you're the person who *designs the system that prompts the agent*, not the person doing the prompting.
- Core safety principles of a good loop: anchor intent (docs/CLAUDE.md), give it something that can say no (tests, review gates, a taste gate), give it skills worth calling, and cap it so it halts (max iterations, no-progress detection, dollar/token budget).

### The actual Claude Code features that make this real

- **`/loop`** — built-in skill that schedules recurring prompts. You give it an interval + a prompt (which can itself be a slash command/skill). It fires between turns at low priority, never interrupts mid-response. Session-scoped, ~3-day life, 7-day hard expiry as a safety net. Forgiving syntax (leading/trailing/omitted interval). Omit the interval and the model self-paces.
- **`/goal`** — added v2.1.139 (May 11, 2026). A native loop that runs across turns until a *verifiable condition you wrote* is true, with a separate fast model grading the work after every turn.
- **`/batch`** — built-in way to fan one natural-language instruction across multiple parallel agents.
- **Dynamic Workflows / "ultracode"** — announced June 2, 2026. Claude Code writes JavaScript orchestration scripts that coordinate up to 1,000 subagents in parallel without burning the context window (migrations, audits, multi-source sweeps). Trigger word was "workflow," changed to **"ultracode"** on June 3 because "workflow" triggered too easily in normal conversation.
- **Routines** — cloud automation layer (desktop app redesign, April 14). Plain-language: describe what you want, how often, which tools. Example pattern: a routine posts draft notes to Slack, thumbs-up = scheduled, thumbs-down = vetoed. Emoji as a taste gate.

### Why this matters for creators specifically

- Non-developers can now do most of this without writing code — Routines + skills + /loop are plain-language.
- The observed pattern: creators who adopted loops went from "one project a month" to "shipping daily" — a completely different output velocity.
- Anthropic's own engineers report shipping ~8x more code with 80%+ authored by AI by May 2026 — the loop is *how*.

### Competitive landscape on YouTube (from our yt-search)

- The "loops not prompts" narrative is days old on YouTube. Sean Kochel ("Write Loops, Not Prompts," 20K) and Ray Amjad ("How the Top 1% Run Claude Code," 13K, `/loop` thumbnail) are the only creators on it.
- Both are developer-framed. **No one has done the creator/solopreneur version** — loops running a content business. That's Tyler's unique, defensible angle (ties to video-ideas #5 and #6).
- The board is otherwise dominated by Anthropic's own explainers + beginner tutorials.

---

## Sources

- [Loop Engineering Guide 2026 — explainx.ai](https://explainx.ai/blog/loop-engineering-coding-agents-claude-code-guide-2026)
- [What Is Loop Engineering? — MindStudio](https://www.mindstudio.ai/blog/what-is-loop-engineering-ai-coding-agents)
- [The Anthropic leader who ditched prompting — The New Stack](https://thenewstack.io/loop-engineering/)
- [Claude Code Creators Explain Agent Loops — The Neuron](https://www.theneuron.ai/explainer-articles/claude-code-creators-boris-cherny-and-cat-wu-explain-how-to-use-agent-loops/)
- [Loop Engineering Playbook — Cobus Greyling (Medium)](https://cobusgreyling.medium.com/loop-engineering-playbook-4460e01e88d8)
- [I Don't Prompt Claude Anymore. I Write Loops — James Fahey (Medium)](https://medium.com/@fahey_james/i-dont-prompt-claude-anymore-i-write-loops-that-prompt-claude-57e48a4f28d7)
- [Stop Prompting Your Agent. Start Writing Loops — Oscar Gallego Ruiz (Medium)](https://medium.com/@garbarok/stop-prompting-your-agent-start-writing-loops-73608223f075)
- [Loop Engineering — Addy Osmani](https://addyosmani.com/blog/loop-engineering/)
- [Loop Engineering — Firecrawl](https://www.firecrawl.dev/blog/loop-engineering)
- [Loops, Not Prompts — Kingy AI](https://kingy.ai/ai/loops-not-prompts-how-advanced-ai-users-are-turning-codex-claude-code-and-llms-into-real-workflows/)
- [Autonomous Commands /goal /loop /batch — Rick Hightower (Towards AI)](https://medium.com/@richardhightower/claude-code-the-autonomous-commands-that-finish-work-while-you-sleep-goal-loop-batch-etc-7acb82bf46b1)
- [From Ralph Wiggum to /loop — paddo.dev](https://paddo.dev/blog/claude-code-loop-ralph-wiggum-evolution/)
- [How to Use Claude Code /loop — Verdent Guides](https://www.verdent.ai/guides/claude-code-loop-command)
- [Claude Code's /loop Command — Sangam Pandey](https://sangampandey.info/blog/claude-code-loop-command)
- [Introducing Dynamic Workflows in Claude Code — Claude.com](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code)
- [Claude Code Adds Dynamic Workflows — InfoQ](https://www.infoq.com/news/2026/06/dynamic-workflows-claude-code/)
- [Loopcraft: The Art of Stacking Loops — Latent Space](https://www.latent.space/p/ainews-loopcraft-the-art-of-stacking)
- [100 Creator Workflows: Claude Code Beyond a Developer Tool — MLearning.ai](https://mlearning.substack.com/p/100-creator-workflows-showing-claude-code-beyond-a-developer-tool-non-coding-tasks)
