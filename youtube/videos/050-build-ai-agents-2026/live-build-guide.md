# 050 - Live build guide (build the social-research agent ON CAMERA)

The video BUILDS the skill live - it is not pre-built. The "proper 2026 way": you describe the
agent to Claude and it scaffolds the skill, then Matt Pocock's `grill-me` (the ONE pre-built skill
you install) roasts it into shape. Mapped to the 5 steps.

Reference / answer key (your real working copy, do NOT show it as pre-made):
`~/.claude/skills/social-research/SKILL.md`. On camera, build it fresh. If you want a clean start,
`rm -rf ~/.claude/skills/social-research` first so nothing looks pre-baked.

## Pre-flight (have these ready, get exact commands BEFORE rolling)
- Claude Code open. (Also have the Desktop app + claude.ai web tab ready for the "three doors" beat.)
- **Apify token** + the exact `claude mcp add` command from Apify's MCP docs. GET THIS FIRST so you
  don't fumble the command on camera. (Do not guess it live.)
- **Matt Pocock's skills installed** (grill-me). Install before rolling with `/plugin install mattpocock-skills`
  (it's in Claude Code's official marketplace, nothing to add first; or `claude plugins install mattpocock-skills`
  from a shell). Then `/grill-me` is available. On camera just show it is there and use it.
- A topic to research live: "Claude Code AI agents" (doubles as real research for you).

## The live build

### Step 1 - Get in (three doors)
Show fast: Claude Code, the Desktop app, or claude.ai web - "start wherever you're comfortable."
Then land in Claude Code: "I'll build here, because this is the only one where I can give it real
tools and put it on a schedule."

### Step 2 - Define the agent (describe it, let Claude scaffold the skill)
Do NOT hand-write the SKILL.md. Type into Claude Code, roughly:
> "Create a Claude Code skill called social-research. It takes a topic and researches it across
> YouTube, Instagram, X, and TikTok using Apify, reads the top YouTube videos' transcripts, finds
> what's working and the content gaps, and gives me a brief with content ideas. Ground everything in
> real data, never invent numbers."
Watch it create the folder + SKILL.md. Open it. Teach the one idea: **"an agent is just a text file -
the instructions - plus the tools it can use, and it can carry its own code too."**

### Step 3 - Add the tools (MCP + the skill's own code)
- **Flip on the MCP tool:** run the Apify `claude mcp add ...` command (from pre-flight). Then `/mcp`
  to show Apify connected. "This is the reach - now the skill can touch YouTube, Instagram, X, TikTok."
- **Add the skill's own code:** drop in the `yt_transcript.py` script (yt-dlp). "A skill can run its
  own code too. This pulls a transcript with yt-dlp - and when YouTube blocks it, the skill falls
  back to Apify." (Show the fallback is real - yt-dlp 403s a lot.)
- Land the payoff line: **"The skill is the recipe, MCP is the reach. The skill calls the tools."**

### Step 4 - Refine (roast it with grill-me)
Run **grill-me** on the skill. It fires 16-50 hard questions about the agent's intent and gaps -
answer them, and tighten the SKILL.md as it exposes holes (missing output format, no grounding rule,
unclear when to use it). "Instead of guessing at the perfect prompt, I let a skill interrogate it."
Credit Matt Pocock on screen.

### Step 5 - Run it, then schedule it
- **Run live:** `/social-research Claude Code AI agents`. It calls Apify per platform, reads the top
  YouTube transcripts (yt-dlp -> Apify fallback), and prints the real brief. Let it run - the real
  output is the money shot.
- **Schedule it:** put the invocation on a cron / Claude routine so the brief lands every morning.
  "That's the difference between a chatbot and an agent - it runs without me."

## Keep it EASY (guardrails)
- Build the **YouTube** path fully, then "same skill, point it at Instagram / X / TikTok" - do NOT
  build all four step-by-step (kills the "5 easy steps" promise + bloats to 30 min).
- If the live run is slow, speed-ramp the waits in the edit, never sit on a spinner.
- The whole thing should feel like "I described it, connected one tool, roasted it, ran it." Easy.
