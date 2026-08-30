# 051 - Scrape ANYTHING using this AI Agent (2026 REMAKE) - Plan

## The original (source we are beating)
- Title: "Scrape ANYTHING using this AI Agent, here's how"
- Channel: Tyler's own (@TylerReedAI)
- Views: 25,665 | Published: 2025-03 | Length: 12:10
- Status: strong evergreen performer, one of the better-retaining builds on the channel.

### What worked (keep this)
- The promise is universal: "scrape ANYTHING" reads as a skeleton key, not a niche tool. Anyone who has ever copy-pasted a list off a website into a spreadsheet self-selects in.
- It was a real end-to-end build, not a tool review. Viewer watched a thing get made.
- Concrete payoff: data went from a live website into a usable file.

### What is dated (why it needs a remake)
- The 2025 build leaned on a more brittle, hands-on setup: custom code and CSS selectors / an older agent framework that broke the moment a site changed its layout, plus manual handling of JavaScript-heavy pages and anti-bot blocks.
- In 2026 none of that is necessary. The agent handles it. The whole "here's how you find the right selector" middle section is now obsolete and, honestly, was the boring part.
- The tools moved: Claude Code + MCP + skills did not exist in this form in early 2025.

## What is different for 2026
- The agent is **Claude Code**, driven in plain English. No selectors, no parser code to babysit.
- The scraping engine is **Firecrawl** (via its MCP server / Claude Code skill). It auto-detects when a page needs a real browser, renders JavaScript, rotates proxies, handles anti-bot, and returns clean markdown or structured JSON already stripped of ads/nav/footers. One install: `npx -y firecrawl-mcp`, then `/firecrawl:setup` with an API key. Free tier is 500 credits, no card.
- Structured extract: you hand Firecrawl a tiny JSON schema ("title" string, "company" string, "salary" number, "url" string) and it fills it in across a whole list page. No parsing.
- The "turn it into something useful" step is the new hero: Claude Code doesn't just dump rows, it writes them to a spreadsheet AND then reasons over them (ranks, filters, writes a short brief). That is the 2026 upgrade the 2025 video could not do.
- Delayed-credibility spine: the payoff (a spreadsheet filling itself) lands before Tyler's face, before any resume.

## The exact agent we build on screen
**Job:** point the agent at any list-shaped web page you check by hand, and get back a spreadsheet plus a short ranked brief, without writing a scraper.

- **Target site (on-screen demo):** a public remote-jobs board (We Work Remotely / RemoteOK-style listing of remote engineering + AI roles). Chosen because it is list-shaped, JavaScript-rendered, universally relatable, and safe/evergreen. Backup/secondary framing: a competitor's product + price list (same pattern, price tracking).
- **What we extract (JSON schema):** `title`, `company`, `location`, `salary_range`, `tags`, `apply_url` for every listing on the page. Firecrawl's `extract` fills the schema across all rows.
- **Where the data goes:** Claude Code writes the JSON to a **CSV / Google Sheet** (rows visibly filling in = the b-roll payoff). Then the useful part: Claude reads its own sheet and produces a **ranked shortlist of the top 10 matches + a one-paragraph brief** ("here are the 10 worth applying to and why"). That is the "makes it useful" beat.
- **Stretch beat (optional, teased as open loop):** wrap the whole thing as a reusable Claude Code skill / slash command so tomorrow it is one line, and it can run on a schedule.

### Tool ladder shown (so it stays accurate + shows range)
- **Firecrawl MCP** = the default. Clean text/JSON from any arbitrary URL, handles JS + anti-bot automatically.
- **Apify MCP** = level up when you need platform-specific structured data (LinkedIn, Google Maps, Amazon) via its Actor library.
- **Playwright MCP** = level up when you need to actually operate the browser (log in, fill a form, click through a flow) rather than just read it.
- Framing: start with Firecrawl, reach for the other two only when the page fights back. Keeps beginners un-intimidated.

## Target audience
- Anyone who repeatedly copy-pastes data off websites into spreadsheets: job hunters, people doing competitor/price research, anyone building a lead or research list, VAs, ops people, indie builders.
- Skill level: beginner-to-intermediate. Comfortable installing one thing and typing into Claude Code. Not required to be a developer.
- Transfer test (per voice guide): the takeaway is "any list you check by hand can become a self-updating spreadsheet," which applies to someone who has never made a video and never will. Jobs board is the setting, not the topic.

## Angle vs the original
- 2025 = "here is how to build a scraper." 2026 = "here is how to stop building scrapers." The agent + Firecrawl removes the brittle middle (selectors, JS, anti-bot) that was half the old video.
- New emphasis on the second half: not just getting the data, but Claude turning the data into a decision (ranked brief). Data -> answer, not data -> file.
- Delayed credibility. Open on the spreadsheet materializing, face at ~0:08, and the IBM / Chase / Pfizer software-engineering background only lands around 0:35 as the reason to trust the shortcuts, never as a flex and never as "you don't need to be a developer."
- Humble, doable framing throughout: one install, one schema, plain English. "Pick one page you check every week and point it at that."

## Target: 10k+ views. Evergreen slot; strong to re-pin and update annually.
