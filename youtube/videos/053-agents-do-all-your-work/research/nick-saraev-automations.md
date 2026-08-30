# Nick Saraev (@nicksaraev) — Automation / AI-Agent Content Research Brief

**For:** 053 "How To Use AI Agents To Do ALL Your Work" (Tyler's build/showcase of real Claude Code agents doing his real job)
**Compiled:** 2026-08-17
**Method:** Apify YouTube scraper (channel sorted POPULAR) + yt-dlp auto-sub transcripts of 3 videos.

Nick is an AI-automation-**agency** creator. He runs Leftclick (automation agency) and Maker School (a paid Skool "0-to-1" community). His whole channel is built around one thesis: **automation is a way to make money / build a service business**, not a way to do your own work. Keep that framing difference front of mind for 053 — it is the single biggest reason his content and Tyler's should feel different.

---

## 1. Top videos (ranked by actual view count)

| # | Title | Views | Published | Length |
|---|-------|-------|-----------|--------|
| 1 | CLAUDE CODE FULL COURSE 4 HOURS: Build & Sell (2026) | **2,287,840** | 2026-02-12 | 4:10:43 |
| 2 | N8N FULL COURSE 6 HOURS (Build & Sell AI Automations + Agents) | **1,230,645** | 2025-04-29 | 5:58:32 |
| 3 | AI Agents Full Course 2026: Master Agentic AI (2 Hours) | 601,270 | 2026-03-08 | 2:13:14 |
| 4 | What I'd Learn Instead of Automation in 2026 | 505,197 | 2025-09-03 | 14:39 |
| 5 | CLAUDE CODE ADVANCED FULL COURSE (3 HOURS) | 381,241 | 2026-03-28 | 3:18:23 |
| 6 | Watch me start & sell an AI service in 10 hours | 368,424 | 2025-04-23 | 1:31:42 |
| 7 | $2.4M of Prompt Engineering Hacks in 53 Mins (GPT, Claude) | 349,094 | 2025-03-05 | 53:31 |
| 8 | Claude Code + Nano Banana 2 + Kling = $15K Animated Sites | 331,337 | 2026-03-16 | 13:58 |

Also-rans just below: "AGENTIC WORKFLOWS: Build & Sell AI Automations" (299K), "VIBE CODING FULL COURSE" (299K), "5 BORING AI Automations To Sell For $1.5K+ Each" (276K), "Gemini 3.1 + Antigravity" (256K).

**Pattern to notice:** his two biggest hits by a mile are multi-hour "FULL COURSE... Build & Sell" marathons. The title formula that prints for him is `[TOOL] FULL COURSE [N HOURS]: Build & Sell`. His single most-viewed non-course video (505K) is a *contrarian* essay ("What I'd Learn Instead of Automation") — proof that a strong POV beats another tutorial.

---

## 2. Per-video breakdown (3 transcribed in full/sampled)

### A. "5 BORING AI Automations To Sell For $1.5K+ Each in 2025" (276K, 23 min)
- **What "automation" actually means here:** Be honest — these are **NOT agents**. Nick says it outright in the first 15 seconds: *"These are not flashy chatbots. They're not AI agents. What they are are unsexy but very simple straight-line automations."* Every build is a linear left-to-right Make.com / n8n workflow with an LLM node bolted in for one step.
- **What he builds (the 5 systems):**
  1. **Search-intent lead scraper** — Apify scrapes LinkedIn/Indeed job posts → Google Sheets dedupe → AnyMailFinder to get the CEO → Perplexity researches the person → GPT-4-mini writes a custom icebreaker → pushes into Instantly cold-email campaign.
  2. **Podcast repurposing engine** — Apify pulls a YouTube transcript → GPT extracts 10 points → splits into Instagram/LinkedIn/Facebook posts → DALL·E image → Google Sheet → scheduled node auto-publishes.
  3. **Invoice-chaser** (Make.com) — reads a Sheet/Stripe/QuickBooks for `overdue` → routes by days elapsed (7/14/21/28...) → sends escalating follow-up emails.
  4. **Cyclic blog-article generator** (Make.com) — OpenAI web search → builds outline from competitors' posts → writes section-by-section with per-section images → outputs a formatted Google Doc.
  5. **Email categorizer** (Make.com) — webhook on new Gmail → GPT labels into 4 buckets → moves/marks the message.
- **Stack:** Make.com + n8n + Apify (his favorite scraper, mentioned constantly) + OpenAI/GPT-4-mini + Perplexity + Instantly + Google Sheets as the universal "database."
- **Angle:** 100% money/agency. Repeated line: *"you could sell any of these systems for $1,500 a pop or more... I've seen people sell a couple for more than 10K."* Value is framed as **client ROI you can charge for** (e.g., "how much money is tied up in unpaid invoices"), never "save yourself time."
- **Hook:** *"Here are five boring AI automations that you could sell today for 1,500 bucks a pop or more."* Money number + "boring" (anti-hype) in the first sentence.
- **CTA / lead magnet:** Maker School ("templates and blueprints to literally every one of these systems... 2,000+ people... I increase the price every 100 members"). Scarcity + roadmap.

### B. "What I'd Learn Instead of Automation in 2026" (505K, 14 min) — his strongest non-course video
- **What it is:** A contrarian **essay**, no build. Argues that automation-*implementation* skill (knowing every Make module / n8n node / API) is depreciating because AI will soon build workflows from plain-English business requirements.
- **The framework he teaches:** "CLEAR" prompting — Clarity, Logic, Examples, Adaptation, Results — with a bad-prompt-vs-good-prompt lead-qualification example.
- **His three-layer thesis (worth stealing the structure):** (1) tool skill = "at the margins," getting invalidated; (2) new higher skill = **communicating business requirements to models**; (3) highest skill = **systems thinking / seeing the "shape" of a business** (marketing → sales → onboarding → delivery → reactivation).
- **Angle:** Still money/business, but zoomed out to career strategy. Opens with *"I made 400 grand last month building automation systems, and I'm going to tell you why learning automation in 2026 is probably one of the worst career moves you can make."* Contrarian + big money number + credibility stack (Alex Hormozi, Sam Ovens name-drops).
- **Hook pattern:** big income claim → contrarian reversal → "hear me out."
- **CTA:** Maker School (business behind AI) + Leftclick (done-for-you agency, "book a call").

### C. "Watch me start & sell an AI service in 10 hours" (368K, 91 min) — the definitive agency showcase
- **What it is:** A live, unedited-feel build of an **agency business**, not a product. He picks 3 niches, writes "I build X for Y" positioning statements, sets up lead-scraping + cold-email infrastructure, writes an "irresistible offer," and runs outreach until he gets his first interested reply on a call.
- **The "agent" content:** a small icebreaker-generation LLM step inside a cold-outreach flow — again, a workflow node, not an autonomous agent.
- **Angle:** Pure sell-a-service. *"Let's get up and running and make some freaking money."* The lesson is a business methodology: *"You don't build and then hope people will come. You start selling all the possible products you could... once you validate them, then you build the thing."*
- **CTA:** Maker School (0-to-1) + Make Money With Make.com (his premium community "capped at 500... $25,000/month and beyond").

---

## 3. Nick's angle vs. the "do all your work" angle

| | **Nick Saraev** | **Tyler / 053** |
|---|---|---|
| Core promise | *Make money* — sell automations to clients, build an agency | *Do MY actual job* — real Claude Code agents doing Tyler's real work |
| What "agent" means | Almost always a **Make.com/n8n linear workflow** with an LLM node; he explicitly says "not agents" | **Real Claude Code agents** — tool use, file access, running his real pipeline |
| Who benefits | The client (ROI you invoice) | Tyler himself (personal leverage / output) |
| Proof | "I scaled to $72K/month," "$400K last month," "sold for $10K" | "Here is my inbox / repo / channel actually getting worked on" |
| Emotional driver | Greed / opportunity / FOMO | Competence, relief, "look what one engineer can now do" |
| Credibility base | Agency revenue + Hormozi/Ovens proximity | 8 yrs SWE (IBM, Chase), AI engineer at Pfizer — builds the real thing |

**What this means for 053:** Nick owns the "make money with automations" lane completely and has millions of views doing it. Tyler should NOT compete there — he wins by owning the lane Nick deliberately vacated: **an actual engineer showing agents doing his genuine daily work, on camera, no invoice attached.** Nick's audience has to *imagine* the value ("you could sell this"); Tyler can *show* it ("this agent just triaged my email / cut my short / updated my tracker while I talked"). The honesty gap is the moat: Nick calls a Make.com flow an "agent" when it's convenient; Tyler using real Claude Code agents and *saying so plainly* is a differentiator, not a limitation.

---

## 4. What to STEAL for 053 (5 concrete moves)

1. **Lead the cold open with the payoff, stated flatly and specifically.** Nick's best hooks are one sentence with a concrete claim ("five boring automations you could sell for $1,500 a pop"). Tyler's version, honest and personal: *"I have 6 Claude Code agents that do most of my actual job. Here's every one of them, running live."* No preamble (matches Tyler's short-intro rule).

2. **The "boring beats flashy" reframe.** Nick's most durable idea is that unsexy straight-line systems make the money, not "scary-looking agents on YouTube." Tyler can invert it for authority: the agents that actually run his work are boring and reliable — triage email, cut a short, update a tracker — and that's exactly why they're real. Undercuts the hype crowd from a position of proof.

3. **Show the system end-to-end, node by node, in plain language.** Both his tutorials walk every step and explain *why each piece exists* ("this filter checks the website exists because we need it to proceed"). That narrated-reasoning style is why 4-hour videos hold. For 053: don't just show an agent finish — narrate what it's doing and why as it runs.

4. **Steal the 3-layer abstraction ladder as a segment.** From "What I'd Learn Instead": tool skill → communicating requirements to models → systems thinking. Tyler's honest engineer version: "You don't need to know every API — you need to describe your real work clearly enough that an agent can do it." That's literally the thesis of 053 and it's proven to pull 500K views.

5. **Concrete before/after with real artifacts.** Nick shows the actual email that got sent, the actual Google Doc that got generated. Tyler should show the actual PR, the actual published short, the actual inbox — real outputs from his real accounts, not mock data. This is where Tyler can out-credibility Nick.

---

## 5. What to AVOID (where Nick's style breaks Tyler's voice)

1. **The money-number hook.** "I made $400K last month" / "$2.4M of prompt hacks" is Nick's signature and it's off-brand for Tyler (voice rule: no money amounts in titles; he's an engineer, not a guru). Don't open 053 with an income claim.

2. **Calling workflows "agents" for clicks.** Nick blurs Make.com flows and "agents" freely. Tyler's whole edge is precision — if something is a script or a workflow, call it that. Never inflate a cron job into an "autonomous agent."

3. **The agency/"sell this for $1.5K" CTA.** Nick funnels everything into Maker School and "book a call." Tyler is not selling an agency playbook — the CTA should be his own community/content, framed around *doing your own work better*, not *starting a service business*.

4. **Scarcity/FOMO pressure ("price goes up every 100 members," "capped at 500").** That high-pressure Skool-marketing tone clashes with Tyler's calm, competent engineer voice. Skip it.

5. **Guru credibility-by-association (Hormozi/Ovens name-drops, "largest AI community by revenue").** Tyler's credibility is the opposite kind — he does the actual engineering job at a real company. Lean on *showing the work*, not on proximity to business influencers.

6. **6-hour marathon format.** It works for Nick's "sit down and learn to build a business" promise. 053 is a showcase — keep it tight and let the live agent runs be the spectacle. Don't pad to course length.
