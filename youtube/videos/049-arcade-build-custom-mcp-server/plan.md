# 049 — Build Your Own Custom MCP Server with Arcade

**Lane:** arcade.dev series (part 4: 045 connect → 046 agent → 048 make a server → **049 build custom** → 047 course).
**Status:** planning. Package not built yet. **Needs a fact-check pass on Arcade's custom-tool workflow before scripting (see below).**

## Thesis
Prebuilt tools cover a lot, but the thing you actually want to automate is usually custom. This video writes a real tool from scratch, deploys it as an MCP server with Arcade, and has Claude use it — with auth, hosting, and per-user OAuth handled for you. The payoff line: you just shipped a real MCP server, and other people could log into it.

## Working titles (pick at /yt-seo)
- Build Your Own Custom MCP Server with Arcade
- I Built a Custom MCP Server (and Claude Used It)
- Turn Any API Into an MCP Tool for Claude
- Build an MCP Server Other People Can Use

## Audience
Developers / builders — the "you could sell this" crowd. This is the monetization-adjacent one. Tyler's 8-years-engineer credibility is the wedge; keep it doable, not a lecture.

## How it differs from 048
- **048** assembles prebuilt tools, no code → hosted server URL.
- **049** writes + deploys a CUSTOM tool (code) → your own hosted MCP server. Progression: use → build.

## Rough outline (tighten at /yt-package, AFTER fact-check)
1. Hook, result first: Claude calling a tool I wrote ten minutes ago, running on my real account.
2. Why: prebuilt is great until your thing is custom (an internal API, a niche SaaS, your own product).
3. The pieces: a tool is a function + what auth it needs; Arcade turns that into a hosted MCP server.
4. Build one live: write a small tool that hits an API worth showing (keep it real, keep it safe / draft-mode if it writes).
5. Deploy it with Arcade (the deploy workflow) so it becomes a server with a URL.
6. Connect it to Claude Code and watch Claude call it.
7. The payoff: auth + hosting + per-user OAuth handled; this is shippable, others could log in.
8. CTA: point back to 048 (assemble) and 046 (agent); tease the course (047).

## FACT-CHECK FIRST (do not script until confirmed vs docs.arcade.dev)
- Arcade **Tool SDK**: current decorator/API for defining a tool (Python), project scaffold (`arcade new`?), local dev/worker.
- **Deploy**: exact command/flow (`arcade deploy`?), what it produces, how a custom toolkit is exposed as an MCP server / gateway URL.
- **Custom auth**: how you declare a tool needs OAuth, whether custom OAuth providers are supported, secrets handling.
- Pricing/tier required to deploy a custom tool (is deploy on the free tier?).
- Whether the demo should be Python only, and the minimum realistic build that still looks impressive in ~8-10 min.
- Confirm nothing here requires the viewer to expose secrets on camera; design the demo so no keys/tokens are ever shown.

## Disclosure
Confirm sponsor/partner status with Arcade before publishing; if sponsored, say so on camera + in the description.
