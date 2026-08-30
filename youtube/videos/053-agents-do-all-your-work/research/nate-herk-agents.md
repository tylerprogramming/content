# Nate Herk (@NateHerk) — Agent/Automation Research Brief

For video **053 – "How To Use AI Agents To Do ALL Your Work"** (Tyler builds/showcases real Claude Code agents doing his real job).

Channel snapshot: ~944K subscribers. Former Goldman Sachs BI analyst, left corporate Nov 2024, runs an AI automation agency + founder of Uppit AI. His whole model is "no-code systems, download the template free in my Skool." Research pulled via Apify YouTube scraper (POPULAR sort) + 3 full auto-sub transcripts, Aug 2026.

---

## 1. Top agent/automation videos (by views)

| Views | Title | Date | Len | What it really is |
|---|---|---|---|---|
| **1.82M** | Build & Sell n8n AI Agents (8+ Hour Course, No Code) | 2025-05-23 | 8:26:38 | n8n course |
| **1.11M** | I Built the Ultimate Team of AI Agents in n8n With No Code (Free Template) | 2025-02-03 | 23:45 | n8n multi-workflow |
| **922K** | Build & Sell with Claude Code (10+ Hour Course) | 2026-03-12 | 10:00:05 | Claude Code course |
| **902K** | I Built a Marketing Team with 1 AI Agent and No Code (free n8n template) | 2025-04-26 | 33:55 | n8n multi-workflow |
| **672K** | Andrej Karpathy Just 10x'd Everyone's Claude Code | 2026-04-05 | 17:46 | Claude Code news/tips |
| **592K** | I Turned Claude Into a 24/7 Trader | 2026-04-17 | 33:15 | Claude Code routines |
| **543K** | Ollama + Claude Code = 99% CHEAPER | 2026-04-04 | 25:22 | Claude Code |
| **533K** | Building Beautiful Websites with Claude Code Is Too Easy | 2026-02-19 | 27:51 | Claude Code |
| **526K** | n8n Masterclass: Build AI Agents & Automate Workflows | 2024-10-20 | 1:31:43 | n8n course |
| **467K** | How I Sold These 4 AI Agents for $23,000 | 2025-08-31 | 14:18 | agency/business |

Notable: his single biggest short-form-feeling build video is the **n8n "Ultimate Team of AI Agents" (1.11M)**. His catalog **pivoted hard from n8n to Claude Code around Jan–Feb 2026** — every top video since is Claude Code. That pivot is the whole opportunity for Tyler: Nate is the biggest guy who moved from "automation dressed as agents" toward real Claude Code agents, and the trader video is his closest analog to 053.

Three analyzed in depth below: the two flagship n8n "agent" builds (to name the agent-vs-automation gap honestly) + the Claude trader (his most 053-like video).

---

## 2. Per-video breakdown

### A. "I Built the Ultimate Team of AI Agents in n8n" — 1.11M views
**What "agent" means here:** An **n8n workflow orchestrator**, not an autonomous agent. It's a "manager" LLM node whose only job is to route a Telegram message to one of 4 sub-workflows (email, calendar, contact, content-creator). Each sub-workflow is itself a tiny LLM node wired to hardcoded tool nodes (Gmail send, GCal create, Airtable). The "intelligence" is entirely: LLM picks which pre-built node to fire, and fills node parameters via n8n's `from AI` function. **It is a chatbot in front of a fixed toolbox.** Honest gap: nothing here decides its own goals, writes new capabilities, or does anything the builder didn't pre-wire.

**What he builds on screen, step by step:**
1. Demo first (~7 min): voice note to Telegram → "set up a team sync tonight 6pm with Nate + email him to confirm." Watches nodes light up green.
2. Then reverse-engineers it: Telegram trigger → voice/text switch → transcribe → "ultimate assistant" agent node.
3. Shows the manager's system prompt is SHORT ("your job is to send the query to the correct tool, never write emails yourself").
4. Adds each sub-workflow as a tool via "Call n8n Workflow as a Tool."
5. Walks the email sub-agent: shows how it must `get emails` first to grab a message ID before it can reply/label — the "logic" wow.
6. `from AI` function reveal — lets the model fill any node field (to, subject, body) from the query.

**Stack:** n8n (cloud, ~$27/mo), Telegram (in/out), OpenAI GPT-4o (manager + most agents), Claude 3.5 Sonnet (content writer only — "I like how it structures HTML"), Gmail, Google Calendar, Airtable (contacts), Tavily (web search).

**Hook/title pattern:** "I Built the **Ultimate Team of AI Agents**… **With No Code** (**Free Template**)." Formula = superlative + "team of agents" + "no code" + "free template" in the title itself.

**Demo structure:** Demo-first, build-second. Every claim is shown live (calendar invite pops up, sent email appears, thread reply lands). The **wow beat** = the agent chaining tools it wasn't explicitly told to (it emails Nate a follow-up "even though we didn't ask it to").

**CTA/lead magnet:** Join **free Skool community** → "YouTube Resources" → download the JSON workflows. Upsell: **paid Skool** (5 live calls/week, classroom, deep dives).

---

### B. "I Built a Marketing Team with 1 AI Agent" — 902K views
**What "agent" means here:** Same architecture — **one n8n router LLM + 6 sub-workflow "tools"** (create image, edit image, search image DB, blog post, LinkedIn post, video). Again: not autonomous; it's a Telegram chatbot that picks one of six pre-built pipelines. He's more honest here — openly shows a video-tool that **times out and errors** on the agent level, and shows the workaround.

**What he builds:**
1. Demo: Telegram → "make a cat-food flash-sale flyer" → image; "make it more realistic" → edit; "blog post about sleep & productivity" → post+graphic; "video of a beaver building a house" → 20s rendered video.
2. Breaks down each sub-workflow. Image = GPT-image-1 HTTP call → base64 → convert-to-file → send Telegram + upload Drive + log to Google Sheet.
3. Video pipeline (most complex): image-prompt agent splits topic into 4 scenes → Flux (PiAPI) 4 images → Runway 4 img2vid clips → ElevenLabs 4 sound FX → Creatomate renders → Telegram.
4. **Spends a full segment on real pricing** (image ~$0.20, Runway ~$0.25/5s, Creatomate credits, ElevenLabs $5/mo, n8n $27/mo, GPT-4.1/4.1-mini token costs).

**Stack:** n8n, Telegram, OpenAI GPT-4.1/4.1-mini (via OpenRouter), GPT-image-1, Flux via PiAPI, Runway, ElevenLabs, Creatomate, Google Drive + Sheets (as the "image database"), Tavily.

**Hook/title pattern:** "I Built a **Marketing Team** with **1 AI Agent** and **No Code** (free n8n template)." Note the "**team** with **1** agent" tension — a curiosity hook.

**Wow beat:** The end-to-end faceless video generated from one voice note. Also the honesty beat (shows the error, shows exact dollar costs) which builds trust.

**CTA:** Free Skool → 7 JSON workflows + Google Sheet template + Creatomate template + a setup guide. Paid Skool upsell (1,100+ members).

---

### C. "I Turned Claude Into a 24/7 Trader" — 592K views  ← CLOSEST TO 053
**What "agent" means here:** This one is **an actual autonomous agent**, and Nate says so. Claude Code + **Routines** (scheduled cron triggers) wake a **stateless** agent on a schedule; it reads memory files, researches, decides, places real trades via Alpaca, journals lessons back to files, notifies him. No n8n. He explicitly contrasts it with automation: *"rather than just using a standard automation… with routines we get the full autonomy of Claude Code going through that whole agentic loop of figuring things out"* — and argues a rigid automation would kill the variability you want in trading.

**What he builds, step by step:**
1. Frames the unlock: Opus 4.7 (agentic financial-analysis benchmark) + Claude Code Routines = a 24/7 agent.
2. **Mental model segment (this is the gold):** each routine wakes "essentially stateless… doesn't know anything." Discipline/memory come from **files + context**. Every run: read files → do job → write lessons back for the next run. Plus a "context budget" talk (treat tokens like money, ~200K/run, "context rot").
3. Migrates his existing Open Claude "Bull" bot: asks the old bot to dump its strategy/signals/learnings → gets a zip of 7 files → drops them into a fresh Claude Code project → tells Claude to reorganize into a memory/ folder + CLAUDE.md.
4. Sets guardrails (max 5%/position, daily loss cap, no options, paper-trade first).
5. Has Claude write 5 routine **prompts** (pre-market, open, midday, close, Friday weekly review), each = read files → research (Perplexity) → trade (Alpaca) → update files → notify ClickUp.
6. Deploys as **remote routines** (run in the cloud w/ computer off) which requires a **GitHub repo** — explains local vs remote, env-var secrets (not .env), and "allow unrestricted branch pushes" so the agent can commit its own memory back.
7. Runs one live, hits a real bug (env var name mismatch), fixes it on screen, shows the weekly review land in ClickUp — the agent even **grades itself a C**.

**Stack:** Claude Code + Claude Desktop app (Routines), Opus 4.7, Alpaca (brokerage API, paper + real), Perplexity API (research), ClickUp (notifications), GitHub (repo for remote routines), VS Code. Uses the "Superpowers" brainstorming skill.

**Hook/title pattern:** "I **Turned Claude Into** a 24/7 Trader." Formula = "I turned [tool] into [surprising autonomous role]." (Cf. "…Into the Ultimate Second Brain.") Strong because it implies the tool now does a *job by itself, around the clock*.

**Wow beat:** Two of them — (1) the agent runs while your computer is OFF (remote/cloud routines), and (2) it self-improves by writing memory files + grading itself. Emotional core: "it beat the S&P by 8%."

**CTA:** Free Skool → a **13-page PDF** on the infrastructure/folder-structure/routine setup. "Drop this into Claude Code and brainstorm with it."

---

## 3. What Nate does that works (transferable moves)

1. **Demo before build, every time.** First 5–8 min is pure "watch it work" on a real, relatable task. He earns the right to teach before he teaches.
2. **Show the receipts live.** He cuts to the actual Gmail thread, the actual calendar invite, the actual ClickUp message, the actual portfolio chart. Nothing is asserted; everything is shown.
3. **Short prompts as a selling point.** He repeatedly says "notice this system prompt is NOT long" — makes it feel achievable and steal-able.
4. **A single mental model per video.** Trader video = "stateless agent, files are its memory & discipline." One sticky idea the viewer leaves with.
5. **Honesty as a trust device.** He shows errors (video times out, env-var bug), gives exact dollar costs, and says "not financial advice, this is an experiment." Vulnerability reads as credibility.
6. **Relatable analogies.** "Teaching a kid to ride a bike," "treat tokens like money," "GitHub is like a shared Google Drive."
7. **One free artifact = the CTA engine.** Every video funnels to a free Skool download (JSON template / PDF). The whole video is a lead magnet delivery vehicle.
8. **Title formulas that promise autonomy.** "I turned X into Y that does Z 24/7" and "Ultimate team of agents… no code… free template."

---

## 4. What to STEAL for 053 (5 concrete moves)

1. **Open cold on the receipt, not the concept.** Nate-style: first 30–45s = the finished thing working on Tyler's REAL account (a real Gmail draft, a real Skool DM triage, a real ClickUp task moved, a real commit). No preamble (matches Tyler's "short intros" rule). Then "here's how I built it."

2. **Give the video ONE sticky mental model.** Steal the trader video's best idea and make it Tyler's spine: **"The agent is just a text file + a schedule."** A CLAUDE.md / skill / memory file IS the agent. Show the actual file on screen and say "this is the whole brain." This is more honest and more memorable than Nate's n8n node-spaghetti.

3. **Demo-first, build-second structure.** 3–4 quick "watch it do my actual job" demos up front (email triage, content packaging, analytics pull, Skool reply), THEN one deeper build-along. Cut to the real result after every claim (the sent email, the updated status.md, the ClickUp task).

4. **Put the free artifact in the title/description and deliver it.** Nate's engine is "free template in my Skool." Tyler's version: give away the actual CLAUDE.md / skill / prompt files (or the folder structure) as the lead magnet driving to `the-ai-agency` Skool. Make the download match what's on screen exactly.

5. **Do the honesty beat on purpose.** Show one thing that breaks and fix it live (Nate's env-var bug moment landed). Show real costs/limits. State plainly where the agent still needs a human. This is Tyler's credibility multiplier, not a weakness.

---

## 5. Where Tyler can BEAT Nate

1. **Real accounts, real stakes.** Nate demos on "Nate Herkelman," "Michael Scott," cat-food flyers, and *paper* trading. Tyler runs agents on his **actual** Gmail, Skool (870 free / paid SkoolOS), ClickUp pipeline, YouTube, Supabase, Resend — real money, real members, real consequences. That is inherently more compelling and impossible to fake.

2. **Software-engineer credibility Nate doesn't have.** Nate is an ex-BI analyst who leans "no code." Tyler is 8 yrs SWE (IBM, Chase) now AI engineer at Pfizer. He can explain WHY the agentic loop works, read the code, and speak to real engineering — a lane Nate literally can't occupy. (Never frame Tyler as "not a developer.")

3. **Kill the agent-vs-automation bait-and-switch.** Nate's two biggest "agent" videos are n8n automations wearing an agent costume. Tyler should **name that gap on screen**: "Most 'AI agent' videos are just n8n workflows — pre-wired tools a chatbot picks from. A real agent decides its own steps. Here's the difference." That honest reframing is a differentiated hook and positions Tyler as the truth-teller.

4. **"It's just a text file" beats "23 nodes."** Nate's builds require n8n + 6 sub-workflows + Creatomate + PiAPI + Runway + a Google Sheet "database" wired together — visually impressive but intimidating and brittle. Tyler can show the agent is a **plain-English markdown file + a schedule** — radically simpler, more honest, and more empowering. The whole "brain" fits on one screen.

5. **Show it doing knowledge work, not toy tasks.** Nate's agents make flyers, beaver videos, and paper trades. Tyler's do the unglamorous real job: triage Skool DMs (respecting the "read the DM before ranking" nuance), package a video, reconcile status.md, draft emails in his voice. "Agents doing MY actual work" > "agents making a cat picture."

6. **Honest limits + no hype-y money claims.** Nate leans on "$23,000," "$6K/mo," "beat the S&P." Tyler's standing rules forbid money-in-titles and require honesty — lean into it: "here's what it does well, here's where it still needs me." In a niche full of income-claim thumbnails, the credible builder wins the trust game and the repeat viewer.

---

### One-line positioning for 053
Nate = the biggest name selling "no-code agents" that are often dressed-up automations, demoed on fake accounts. Tyler's wedge = a real software engineer running **actually-autonomous Claude Code agents on his real business**, showing the agent is just a text file plus a schedule, honest about the limits. Same demo-first / one-mental-model / free-artifact structure Nate proved at 1M+ views — but with stakes and credibility Nate can't match.
