# 050 - Record Prep (do this before rolling, 2026-08-30)

Everything needed to film the social-research agent build clean. Checked 2026-08-29.

## State right now (verified)
- ✅ `claude` on PATH (`~/.local/bin/claude`).
- ✅ `yt_transcript.py` present: `~/.claude/skills/social-research/scripts/yt_transcript.py`.
- ✅ social-research SKILL.md exists (this is the ANSWER KEY - do not show it as pre-made).
- ⚠️ **Apify MCP is ALREADY connected** (hosted `mcp.apify.com`). So "watch me add Apify" is not a fresh add unless you handle it. See Step 2 options.
- ✅ **mattpocock-skills INSTALLED** (2026-08-29). The skill to use is **`grilling`** (there's also `grill-me`; `grilling` is the relentless plan/skill interrogation). Run `/reload-plugins` already done.

---

## Step 1 - grilling skill (DONE - installed 2026-08-29)
`mattpocock-skills` installed + reloaded. On camera you invoke **`grilling`** (say "grill this skill" / trigger it) to roast the social-research skill. Note the exact name is `grilling` - not `grill-me`. No install needed at record time.

## Step 2 - Apify MCP (pick ONE for the "connect the tool" beat)
Apify is already connected via hosted, so choose how you want the on-camera moment to look:

**Option A - cleanest teaching moment (recommended): remove, then re-add on camera.**
Off camera, remove it so the add is real:
```
claude mcp remove apify
```
On camera, re-add (hosted, uses your Apify login/token):
```
claude mcp add --transport http apify https://mcp.apify.com
```
Then `/mcp` to show it connected. Clean "here's the one command" beat.

**Option B - local server (also a real command, uses your token env):**
```
claude mcp add apify --env APIFY_TOKEN=<your_token> -- npx -y @apify/actors-mcp-server
```
Slightly more setup; good if you want to show it running locally.

**Option C - just show it's already there.** On camera run `/mcp`, point at Apify connected, say "one command adds this, here it is" and show the command as an overlay. Least friction, least dramatic.

> Recommend A. Have your Apify token handy either way. Don't fumble the command live - it's written here.

## Step 3 - Clean start for the live skill build (RIGHT BEFORE rolling, not now)
The video builds social-research FRESH on camera, so move the real one aside (do NOT delete - it's your working copy):
```
mv ~/.claude/skills/social-research ~/.claude/skills/social-research.bak
```
Restore it after filming:
```
rm -rf ~/.claude/skills/social-research && mv ~/.claude/skills/social-research.bak ~/.claude/skills/social-research
```
(If you'd rather keep a reference open while building, the answer key is in the .bak copy.)

## Step 4 - The rest of the pre-flight
- [ ] Claude Code open. Desktop app + claude.ai web tab open too (the "three doors" beat).
- [ ] Topic to research live: **"Claude Code AI agents"** (doubles as real research for you).
- [ ] `yt-dlp` on PATH + updated (`export PATH="/opt/homebrew/bin:$PATH"; yt-dlp --version`) - the skill's script uses it, Apify is the fallback.
- [ ] Clean, bumped terminal font, 16:9 window, webcam PIP ready.
- [ ] Screen recorder ready. Music stinger for the 0:29 hard cut.

---

## Copy-paste command block (in order)
```
# 1. grilling skill - DONE (installed 2026-08-29). On camera: invoke `grilling`

# 2. Apify - Option A (off camera remove, on camera re-add)
claude mcp remove apify
# ON CAMERA:
claude mcp add --transport http apify https://mcp.apify.com
/mcp

# 3. clean start (right before rolling)
mv ~/.claude/skills/social-research ~/.claude/skills/social-research.bak

# 4. the live build (on camera, inside Claude Code)
#   "Create a Claude Code skill called social-research. It takes a topic and
#    researches it across YouTube, Instagram, X, and TikTok using Apify, reads the
#    top YouTube videos' transcripts, finds what's working and the content gaps, and
#    gives me a brief with content ideas. Ground everything in real data, never invent numbers."
#   -> add tools (Apify MCP + the yt_transcript.py script)
#   -> `grilling` on the skill (roast it into shape)
#   -> /social-research Claude Code AI agents
#   -> schedule it (cron / routine)

# 5. AFTER filming - restore the real skill
rm -rf ~/.claude/skills/social-research && mv ~/.claude/skills/social-research.bak ~/.claude/skills/social-research
```

## Reminders
- The `/next-video`, competitor-watch, github-tests stuff is the HERMES video, not this one. 050 = the social-research build only.
- Build the YouTube path fully, then "same skill, point it at IG / X / TikTok" - don't build all four live (kills the 5-easy-steps promise).
- If a live run is slow, speed-ramp in the edit. Never sit on a spinner.
