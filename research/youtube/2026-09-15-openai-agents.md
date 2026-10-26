# Research: OpenAI Agents API (video 058)

**Date:** 2026-09-15 (launch + 5 days)
**For:** 058, Claude Code + Hermes audience
**Raw pulls:** `research/2026-09-15-agents-api.{md,json}`, `research/2026-09-15-openai-agents.{md,json}`, `research/2026-09-15-openai-agents-api.{md,json}`, `research/2026-09-15-codex-harness.{md,json}` (+ `-thumbnails/` folders)
**Transcripts:** `transcripts/transcript_2YHa1vhnmK0.txt` (OpenAI launch video), `transcript_JFWq93b4_Oo.txt` (Bart Slodyczka), `transcript_lHSn7InuflY.txt` (Mathify), `transcript_k_xeuLIwwfQ.txt` (Ben BK, French), `transcript_Wn-JBHohRYI.txt` (QuantBrasil, Portuguese)

---

## 0. Read this first: timing and term pollution

| Fact | Number | Consequence |
|---|---:|---|
| Launch date | 2026-09-10 | Today is day 5. `packaging-rules.md` says cover news inside 48 hours and short, or skip the term. We are past the window. |
| Biggest English creator video on the API | 16,207 (Bart Slodyczka, 12:40) | This is not a DeepSeek Harness wave (222k top video in 30 days). The term is small. |
| Biggest video for the query "OpenAI Agents" | 431,559 (Diamandis podcast) | About a different story: OpenAI agents hijacking a German wiki + Hugging Face. 7 of the top 15 for "OpenAI Agents" are that rogue-agent story, not the API. |
| OpenAI official launch video | 276,182 in 5 days, 2:18 | The demand that exists is going to OpenAI's own upload. |

Read on the field: the API is a developer story with a small, engineer-heavy audience. The rogue-agent news story owns the phrase "OpenAI Agents" this week. 058 should be titled on "Agents API" or "Codex harness", never bare "OpenAI Agents", and it should not be a straight launch recap (late, and OpenAI's own 2:18 already took it). The opening is the comparison/self-host angle in section 4.

---

## 1. What OpenAI shipped (verified against openai.com and developers.openai.com)

| Item | Detail | Source |
|---|---|---|
| Name | Agents API, public beta, all developers | openai.com/index/introducing-the-agents-api |
| Date | 2026-09-10, same morning as GPT-Live-1 and ChatGPT for Financial Services | community.openai.com/t/introducing-the-agents-api-and-hosted-sandboxes/1396481 (dated 09-10) |
| One-line pitch | "Build and run cloud agents with the Codex harness, fully managed by OpenAI." | openai.com launch post |
| What it is | The harness that runs Codex, exposed as an API. OpenAI manages sessions, orchestration, context compaction, recovery. You provide tools and pick the execution environment. | developers.openai.com/api/docs/guides/agents-api/overview |
| Four primitives | Agent (model, instructions, tools, MCP servers), Environment (sandbox), Session (durable running instance), Events and items | overview doc |
| Default model | `gpt-6-astra` in every doc example | quickstart doc |
| Harness features | Automatic context compaction, tool search (loads tool defs on demand), programmatic tool calling (agent filters/combines tool results in code), subagents (`multi_agent: {enabled, max_concurrent_subagents}`), steering mid-turn, resume after disconnect, skills via `capability_directories`, plugins | overview + launch post |
| Environments | 1) `openai_hosted` sandbox, 2) `self_hosted` (you run `codex exec-server` anywhere, incl. a laptop, outbound WebSocket only), 3) `none` (no sandbox), 4) nine partner sandboxes: Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop, Vercel | self-hosted doc |
| Self-host install | `npm install -g @openai/codex@alpha` then `codex exec-server --remote <url> --environment-id <id>`; needs a separate environment key with all other permissions set to None | self-hosted doc |
| SDK surface | `client.beta.agents.sessions.create(...)` in Python, JS, Go, Java, Ruby; cURL needs header `OpenAI-Beta: agents=v1`; endpoint `POST /v1/agents/sessions` | quickstart doc |
| API key scopes | `api.agents.read`, `api.agents.write`, `api.responses.write` | quickstart doc |
| Price | No fee for the API itself. Tokens at model rates, tools at standard rates, hosted sandbox at container rates: 1 GB $0.03, 4 GB $0.12, 16 GB $0.48, 64 GB $1.92 per 20-minute session, 5-minute minimum | developers.openai.com/api/docs/pricing |
| Limits | US-only data residency. No Zero Data Retention, even with a self-hosted sandbox. Hosted sandbox can be deleted after keep-alives stop for an hour. | overview doc, openai-hosted doc |
| Open source | Harness code is the public Codex repo, github.com/openai/codex. OpenAI runs it; you can read it. | launch post |
| Also that day | Data agent in ChatGPT Work (openai.com/index/put-data-to-work), GPT-Live-1 (secondary coverage, unverified by me) | openai.com |

Context that matters for the angle:

| Prior OpenAI surface | Status | Source |
|---|---|---|
| Agents SDK (Python/TS, open source, you run the loop) | Still the "run it yourself" option; April 2026 update added harness + sandbox + Manifest | openai.com/index/the-next-evolution-of-the-agents-sdk |
| Assistants API | Retired 2026-08-26 | secondary (tech-insider.org), unverified against OpenAI changelog |
| AgentKit Agent Builder + Evals | Winding down 2026-11-30 | openai.com/index/introducing-agentkit (June 3 update note) |
| Workspace agents in ChatGPT | GA for Business/Enterprise/Edu, April 2026 | openai.com/index/introducing-workspace-agents-in-chatgpt |

Competitor runtime, for the comparison beat:

| Runtime | Launched | Price on top of tokens | Models | Where it runs |
|---|---|---|---|---|
| OpenAI Agents API | 2026-09-10 beta | $0; container rates if OpenAI-hosted | OpenAI only (gpt-6-astra default) | OpenAI cloud, 9 partners, or your own box via `codex exec-server` |
| Claude Managed Agents | 2026-04-08 beta | $0.08 per active session-hour (secondary sources; Anthropic docs fetch failed, verify before camera) | Claude only | Anthropic containers |
| Hermes Agent | open source | $0, any model incl. local Ollama | any | your Mac, 057 already shows this |

---

## 2. YouTube landscape (last 7 days, yt-dlp pulls on 2026-09-15)

Views and dates are real. Velocity = views / days since upload, rounded.

### Videos about the API

| Views | /day | Dur | Date | Channel | Title | Lang |
|------:|-----:|-----|------|---------|-------|------|
| 276,182 | 55,200 | 2:18 | 09-10 | OpenAI | Introducing the Agents API | EN |
| 24,561 | 12,300 | 36:38 | 09-13 | Rafael Quintanilha, QuantBrasil | How to Create Your Own Agent with OpenAI's New Agents API | PT |
| 16,207 | 5,400 | 12:40 | 09-12 | Bart Slodyczka | I Tested OpenAI's New Cloud Agents... What You Need To Know | EN |
| 12,779 | 4,300 | 16:34 | 09-12 | Ben BK | OpenAI just dropped a BOMB for AI agents | FR |
| 7,545 | 1,900 | 16:29 | 09-11 | Mathify | OpenAI Agents API Just Launched, It's a Much Bigger Deal Than It Looks | EN |
| 6,559 | 3,300 | 15:37 | 09-13 | 01Coder | OpenAI Agents API 公测版上手：托管沙箱、Artifacts 与 Skills | ZH |
| 4,128 | 4,100 | 6:18 | 09-14 | Income stream surfers | OpenAI Agents API + NEW Codex Harness = Cloud Coding Agents INSTANTLY | EN |
| 1,712 | 600 | 16:10 | 09-12 | Sura×Asura | Codex API化 OpenAI Agents API × GPT-Live-1 | JA |
| 1,170 | 1,200 | 3:39 | 09-14 | Box | OpenAI Agents API + Box Mount: A Multi-Agent Deal Desk Demo | EN |
| 813 | 200 | 12:41 | 09-11 | AI Bros Podcast | Memory & Subagents Explained, Harness Engineering Part 2 | EN |
| 598 | 150 | 7:01 | 09-11 | Chuck Goetschel | OpenAI's Agents API is here, so why pause ChatGPT Pro? | EN |
| 435 | 110 | 10:19 | 09-11 | Cayman AI Automation | OpenAI Now RENTS You The Codex Harness | EN |
| 347 | 120 | 13:10 | 09-12 | 荒野全栈AI | 实测 Codex API：我自己搭了一个 Coding Agent | ZH |
| 152 | 50 | 9:02 | 09-12 | One Layer Down | Building Persistent AI: A Deep Dive into OpenAI Agents API | EN |

English creator videos on the API with over 1,000 views: 4 (Bart, Mathify, Income stream surfers, Box). Shorts on the API in the window: 0.

### Videos polluting the "OpenAI Agents" query (not the API)

| Views | Dur | Date | Channel | Title |
|------:|-----|------|---------|-------|
| 431,559 | 2:22:43 | 09-09 | Peter H. Diamandis | OpenAI Agents Hijack a German Website, Jensen Declares AGI Arrived... |
| 71,383 | 10:03 | 09-08 | Universe of AI | OpenAI Has A Stronger Model Than GPT-6 Astra Already! |
| 20,153 | 12:57 | 09-10 | The BlackVeil Files | Hugging Face Was Hacked by OpenAI's Own AI |
| 14,280 | 12:43 | 09-12 | ML Visualized | OpenAI's Hugging Face Hack: The Story You Missed |
| 12,053 | 8:51 | 09-09 | Devsplainers | AI Agents Are Already Plotting Behind Our Backs |
| 9,513 | 26:13 | 09-15 | Rod Miller | OpenAI Agents Gone Rogue: 2,000 Malicious Packages Found |

### What the three English videos actually do (from transcripts)

| Creator | Views | Shape | Hook (first line, exact) | What they built / showed |
|---|---:|---|---|---|
| Bart Slodyczka | 16,207 | Business-automation demo | "OpenAI have just released their agents API, and this introduces new ways to use agents." | Speed-to-lead agent: intake form -> cloud agent researches customer, drafts proposal, books calendar. Uses the platform dashboard "Agents" tab, the "Build in Codex" button (a ChatGPT plugin that manages the agent), MCP for Gmail + Calendar, an HTTP node from the form into `sessions.create`. Notes the gap: continuing a session from an email reply needs your own DB of session ids. |
| Mathify | 7,545 | Animated explainer, no build | "OpenAI just released an API that looks surprisingly small in code, but architecturally is a much bigger deal." | Explains the harness: "Who remembers state? Who runs the code? Who retries a failure? Who stores the files? Who trims the context when it overflows?" Animates compaction ("each gold pulse is one compaction, the session line never breaks"). Closes: "The model was only the beginning." |
| Ben BK (FR) | 12,779 | Explainer | "Le 10 septembre 2026, Codex a sorti une nouvelle API." | Harness vs model framing: Codex = model + harness + tools + environment, "the model is just one brick of four." Where the API stops, why it is a strategic move. |
| QuantBrasil (PT) | 24,561 | 36-min build | Announces the API, promises pros/cons and a config walkthrough | Frames it as "distribute the agent you already built in Codex / Claude Code / OpenCode to your team." Asks "is the Agents API the best way to build your own harness?" |

Read on the field:

| Pattern | Count | Note |
|---|---:|---|
| "Harness, not model" is the shared thesis | 3 of 4 transcripts | Mathify, Ben BK, QuantBrasil all lead with it. It is the accepted framing, not a gap. |
| Comparison to Claude Managed Agents / Claude Code / Hermes | 0 of 14 | QuantBrasil mentions Claude Code and OpenCode as places you built your agent, in Portuguese. No English video compares runtimes. |
| Self-hosted `codex exec-server` on your own machine | 0 of 14 | Every English video uses OpenAI-hosted. The docs say the environment "can be a laptop." |
| Price / cost breakdown | 2 (Cayman 435, AI with Aayush 25, Hindi) | Both under 500 views. |
| "Build in Codex" plugin from the dashboard | 1 (Bart) | Undercovered, and it is the fastest path to a working agent on camera. |
| Business-automation demo (form -> agent -> email) | 1 (Bart, the English winner) | The business demo beat the two explainers. Showing a running agent wins over diagrams here. |
| Durations of the English winners | 12:40, 16:29, 6:18 | All inside the 10-35 band. Nothing in the dead zone except QuantBrasil (36:38, PT). |

### Thumbnails (looked at the actual jpgs)

| Video | Face | Text | Structure |
|---|---|---|---|
| OpenAI official (276k) | Yes, presenter at laptop with OpenAI logo | "Agents API" | Brand lifestyle shot, no promise |
| Bart (16k) | Yes, large, right third, pointing | "Codex Cloud Agents" | Fake dashboard with 3 cloud terminal agents on a triangle, cyan glow, dark |
| Mathify (7.5k) | No | "OpenAI Agents API JUST LAUNCHED" + 6 feature chips (Run code, Manage files, Use tools (MCP), Spawn subagents, Long-running sessions, In the cloud) | CODEX block -> arrow -> API chip, dark, green accent |
| Ben BK (12.8k) | Yes | French overlay | Dark, face right |

Pattern: dark background, cyan/green accent, "Codex" or "Agents API" in 2 to 3 words, and an arrow or block diagram. Bart's face-plus-diagram is the best-performing English composition. Nobody has done a split (Codex harness vs your Mac / Claude Code vs Codex harness), which is the shape `packaging-rules.md` says is missing from our own thumbnails too.

---

## 3. Gaps that fit Tyler

| Gap | Evidence | Why it is ours |
|---|---|---|
| Run the Codex harness on your own Mac | Self-hosted doc: `codex exec-server`, "can be a laptop", outbound-only. 0 of 14 videos do it. | Directly adjacent to 057 (Hermes on your Mac). Same viewer, same "your machine, your files" promise. |
| Three runtimes side by side: Agents API vs Claude Managed Agents vs Hermes | 0 of 14 compare. Claude Managed Agents has been out since April. | Tyler has standing on all three. "I Tested X vs Y" is the allowed "I" shape (3.30x). |
| The "you don't need it" take for the Claude Code / Hermes viewer | Everything the API sells (compaction, subagents, tool search, skills, MCP, resume) is what 057 already shows Hermes doing locally for $0. | Replacement framing (rule 6), second-person accusation (rule 5), and it converts 057 viewers. |
| Cost on camera | 2 videos, both under 500 views, neither in English with real numbers. Container rates are public: $0.03 to $1.92 per 20 min. | Numbers in the thumbnail, not the title. |
| Build in Codex plugin | Only Bart shows it. It is the fastest on-camera path. | Good for a short. |

What not to do:

| Avoid | Reason |
|---|---|
| A straight launch recap | Day 5, and OpenAI's own 2:18 has 276k. Late per packaging rules. |
| Title with bare "OpenAI Agents" | The phrase is owned by the rogue-agent news story this week (431k, 71k, 20k, 14k, 12k). |
| A 35+ minute build | Dead zone 0.72x. QuantBrasil's 36:38 is the outlier and it is Portuguese. |
| "Explained" | Rule 2. Mathify and One Layer Down already are the explainers and sit at 7.5k and 152. |

---

## 4. Title angles (rules-checked: second person or "I Tested", product noun, no money, no em dash, under 70)

| # | Title | Chars | Shape | Thumbnail |
|---|---|---:|---|---|
| 1 | Run OpenAI's Agents API on Your Own Mac in 10 Minutes | 52 | Second person + time box + product noun. Nobody has self-hosted on camera. | Split: OpenAI cloud sandbox (left, crossed) vs Mac terminal running `codex exec-server` (right). "YOUR MAC". |
| 2 | I Tested OpenAI's Agents API vs Claude Managed Agents vs Hermes | 62 | Allowed "I Tested X vs Y" (3.30x). The comparison nobody has done. | Three columns, one running agent each, price per hour under each ($0.08 / container rate / $0). |
| 3 | You Don't Need OpenAI's Agents API (Hermes Does This on Your Mac) | 64 | Second-person accusation + replacement. Converts the 057 audience. | Face large, "$0 vs $1.92" in the thumbnail, Hermes terminal behind. |

Recommendation: 1 or 3. Both are 10 to 15 minute cuts (under-10 band is 1.56x, so cut hard), both extend 057 instead of competing with the explainer pile, and both can film from one build: create a session with `environment.type: self_hosted`, run `codex exec-server` on the Mac, give it the same task 057 gives Hermes, show the cost line. Angle 2 is the fallback if Tyler wants a wider net; it needs a real Claude Managed Agents run, which adds a day.

Unverified before filming:
- I did not run the API. The 10-minute claim in title 1 needs a dry run of `npm install -g @openai/codex@alpha` + `codex exec-server` on the Mac Studio.
- Claude Managed Agents $0.08/session-hour is from secondary sources; confirm at docs.anthropic.com before it goes in a thumbnail.
- GPT-Live-1 and the Assistants API retirement date come from secondary coverage only.

Shorts (0 in window on the API term, wide open):
1. "OpenAI just made the Codex harness an API. Here is the one line that creates an agent." (the `sessions.create` call)
2. "The Agents API can run on your laptop. One command." (`codex exec-server`)
3. "It compacts its own context so the session never dies." (Mathify's beat, done in 40 seconds on a real run)
4. "Hermes already does this for $0." (cut from the 058 comparison)

---

## Sources
- https://openai.com/index/introducing-the-agents-api/
- https://developers.openai.com/api/docs/guides/agents-api/overview
- https://developers.openai.com/api/docs/guides/agents-api/quickstart
- https://developers.openai.com/api/docs/guides/agents-api/environments/self-hosted
- https://developers.openai.com/api/docs/guides/agents-api/environments/openai-hosted
- https://developers.openai.com/api/docs/pricing (Containers row)
- https://community.openai.com/t/introducing-the-agents-api-and-hosted-sandboxes/1396481
- https://openai.com/index/the-next-evolution-of-the-agents-sdk/
- https://openai.com/index/introducing-agentkit/ (June 3 wind-down note)
- https://platform.openai.com/docs/guides/agents (Agents SDK vs Responses API table)
- Secondary: marktechpost.com (09-10), infoworld.com, truefoundry.com (Claude Managed Agents pricing)
- YouTube data: yt-dlp pulls listed at top, 2026-09-15
