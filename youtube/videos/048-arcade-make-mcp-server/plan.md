# 048 — How to Make an MCP Server in 2026 (No Code)

**Lane:** arcade.dev series (part 3 of the arc: 045 connect → 046 agent → **048 make a server** → 049 build custom → 047 course).
**Status:** planning. Package not built yet (run /yt-package after the framing below is confirmed).

## Thesis
You do not code an MCP server in 2026. You assemble one. This video takes someone from "I keep hearing MCP" to "I have a working MCP server and Claude is using it," without writing a line of server code. It is the long-form version of Reel 4 (`045-arcade-connect-apps/reels.md`).

## Working titles (pick at /yt-seo)
- How to Make an MCP Server in 2026 (No Code)
- MCP Servers Explained: Give Claude Any Tool in 2026
- The 2026 Way to Give Claude Code Any Tool
- I Made an MCP Server Without Writing One

## Audience
Anyone who keeps seeing "MCP" and wants to actually make/use one. Beginner-friendly but credible (Tyler is an engineer, leans on the auth angle without gatekeeping).

## How it differs from 045
- **045** is a use-case showcase: "connect my real apps and run my morning from the terminal."
- **048** is the evergreen explainer + how-to: "what an MCP server is, and how you stand one up in 2026." Concept first, then the assemble-a-gateway workflow, then use it. Less about one workflow, more about the skill.

## Rough outline (tighten at /yt-package)
1. Hook, result first: add a whole toolset to Claude Code in one line, then Claude does something it could not a second ago.
2. What an MCP server actually is, one breath: a standard way to hand an agent tools. No mystique.
3. Old way vs new way: write the server + OAuth + host it + keep it alive  →  assemble a gateway and get a hosted URL.
4. Build it live: arcade.dev gateway, pick the tools you want, copy the hosted URL. That URL is the server.
5. Add it: `claude mcp add`, verify with `claude mcp list`, first-use OAuth consent (auth handled, no token in a file).
6. Use it: two or three real actions across the tools.
7. Where it goes: same URL works in Claude Cowork and in your own code; per-user auth means you can build it for other people.
8. CTA: that is assembling from prebuilt tools. Next video (049), write your OWN tool and deploy it as a server.

## Fact-checks before scripting (verify vs live arcade.dev / docs.arcade.dev the day of)
- Current gateway creation flow + exact wording.
- Tool count claim: keep it "thousands," do not quote a hard number unless re-checked.
- Pricing tiers (free to start, $ tier) — quote only what is current.
- `claude mcp add --transport http "<url>"` still the command; `claude mcp list` / `get`.
- Whether one Google auth covers multiple Google tools (show what actually happens).

## Disclosure
Confirm sponsor/partner status with Arcade before publishing; if sponsored, say so on camera + in the description.
