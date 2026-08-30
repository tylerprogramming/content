# 050 - Remake map: the original 26k video, modernized

Source: "How to EASILY Build AI Agents (5 Steps)" - Tyler's own, 26,071 views, 2024-12, 10:49.
Transcript pulled 2026-08-19 (via Apify; yt-dlp was 403'd).

## What the original actually was (important)
It was the **coding / framework version**: AgentStack (a CrewAI-based CLI) + Firecrawl + AgentOps,
building a **web-scraper -> summarizer** crew. OpenAI GPT-4o, YAML prompts, `agentstack run`.

Original chapters:
- 00:00 Intro ("a 5-step process to create your own AI agents")
- 00:10 Step 1: Installation (`pip install agentstack`, `agentstack init`)
- 00:39 Step 2: Agents/Tasks (`agentstack generate agent/task`, pick GPT-4o)
- 03:23 Step 3: Tools (`agentstack tools add firecrawl`)
- 06:46 Step 4: Add Prompts (fill YAML + AgentOps observability)
- 08:35 Step 5: Run it! (`agentstack run` + AgentOps session replay)

**Takeaway:** the "coding version" Tyler was considering = a direct update of THIS. The audience-facing
modernization is the Claude version below. Decision: **lead with Claude (flagship); coding = separate
follow-up for developers, not a co-lead.**

## The modernized 5 steps (Claude version - the flagship)

Keep the original's spine and pacing. Swap the tooling. Add scheduling.

| Step | Original (2024) | Modernized (2026, Claude) |
|---|---|---|
| Intro | "5-step process to build AI agents" | Cold-open on the agent's real RESULT (the research brief it produced), face at ~0:08 |
| **1. Install / get in** | `pip install agentstack` + `init` | **Three doors:** Claude Code, the Desktop app (Cowork), or Claude.ai web - "start wherever you're comfortable." Then build the real agent in **Claude Code** (only place you get tools + scheduling). No framework install. |
| **2. Define the agent** | `agentstack generate agent/task`, pick GPT-4o | Write the instruction file (a **skill / SKILL.md**), plain English job description. No YAML, no model keys. "An agent is a text file + tools." |
| **3. Add tools** | `agentstack tools add firecrawl` | Flip on ONE **MCP server**: **Apify** (`claude mcp add`). It's what Tyler really uses for research, does YouTube + Instagram + TikTok with one connection, and keeps the "flip on a tool" beat clean. The skill then CALLS the Apify tool. |
| **4. Refine the instructions** | fill YAML prompts + AgentOps | **Pressure-test it with a skill.** Feature Matt Pocock's **`grill-me`** skill (credit him) - it interrogates your agent's intent (16-50 Qs) to catch gaps before you lock it in. Optional: ship a tiny "roast my agent" command of my own. |
| **5. Run it + schedule it** | `agentstack run` + replay | Run it in Claude Code, then **put it on a schedule** (cron / routine) so it runs itself. THIS is the modernization the original lacked - sets up "runs while you sleep." |

## The agent we build (modernize the web-scraper -> summarizer)
Original scraped a site + summarized it. New version = same mechanic, but a genuinely useful,
recurring **research agent**, and it demonstrates skill-code + MCP working together on screen.

**The research skill** (`SKILL.md` = the recipe) uses two kinds of tools:
- **Apify MCP** (flipped-on tool): searches/scrapes **YouTube, Instagram, X, TikTok** - one server, all four.
- **yt-dlp** (the skill's OWN bundled code): pulls a specific YouTube transcript. This is the
  "a skill can carry code" part - the visual proof that skill-code and MCP tools cooperate.
- Then **grill-me** roasts the skill to tighten it, and we **schedule** it to run every morning.

### Two rules to keep it EASY + safe
1. **Build ONE platform live (YouTube), then show it generalizes.** Do NOT build all 4 step-by-step
   or the "5 easy steps" promise breaks and it bloats to 30 min. Build YT fully, then "same skill,
   point it at Instagram / X / TikTok."
2. **yt-dlp is flaky (hit a YouTube 403 today).** Make **Apify the reliable path**; frame yt-dlp as
   the free/local option WITH an Apify fallback ("yt-dlp is free but YouTube blocks it sometimes,
   so the agent falls back to Apify"). Honest, and it never breaks on camera.

Builds a reusable "cast" of real agents (YT research, then IG research) to reference in later videos.

## MCP decision (which server to connect) - locked
- **050 uses Apify MCP.** Authentic (Tyler's real research tool), does YT + IG + TikTok with one
  server, cohesive with the recurring YT/IG-research examples. Top-5 MCP server (AgentRank 2026).
- **Cross-series logic:** 051 "Scrape ANY Website" uses **Firecrawl** (general web pages, clean
  markdown - what the ORIGINAL 050 used, so 051 keeps that continuity). Platform data = Apify,
  any website = Firecrawl. Each video features the right tool for its job.
- Keep 050 to ONE MCP so the "flip it on" teaching beat stays crisp.
- Setup on camera: get the Apify token -> `claude mcp add` the Apify server -> `/mcp` confirms it.

## Resources to feature (real, verified)
- Matt Pocock's skills (grill-me etc.): https://claude.com/plugins/mattpocock-skills - ~143k stars.
- Credit him on screen; it's generous and credible, and grill-me IS the "roast" beat.

## Still open
- Coding follow-up video: hold as a separate video for the dev audience, decide after 050 performs.
