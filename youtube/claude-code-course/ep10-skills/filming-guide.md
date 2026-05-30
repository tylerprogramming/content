# Filming Guide — Claude Code Tutorial #10: Skills

## Pre-Recording Checklist

- [ ] Clean desktop — hide personal files, close unrelated apps
- [ ] Terminal font size: 16pt+ (legible on mobile)
- [ ] Claude Code installed and updated (`claude --version`)
- [ ] Existing skills backed up (in case of demo issues)
- [ ] Have a YouTube URL ready for the /transcribe demo
- [ ] Test the /thumbnail skill once to confirm API key works
- [ ] Screen recording: 1920x1080, 30fps minimum
- [ ] Webcam positioned (top-right or bottom-right overlay)
- [ ] Second monitor OFF or hidden from capture

---

## Recording Playbook

### Segment 1: INTRO (Target: 1:30)

**What to say:** Deliver Hook Option 1 word-for-word (see hooks.md)

**What to show:**
1. Terminal with Claude Code open — just the prompt visible
2. Quick cuts: show each custom skill output (thumbnail, transcript, fitness grid) — 1-2 seconds each

**Exact flow:**
1. Open terminal, Claude Code running
2. Say hook line 1 while Claude prompt is visible
3. Cut to thumbnail output image (1 sec)
4. Cut to transcript text file (1 sec)
5. Cut to fitness grid (1 sec)
6. Back to face cam for "Let's get into it"

---

### Segment 2: WHAT ARE SKILLS (Target: 2 min)

**What to say:** Follow script Section 1

**What to show:**
1. Briefly show typing `/plan` in terminal as callback to earlier episode
2. Display the comparison table (prepare as a graphic or type it live)

**Exact commands:**
```bash
# Just show this from a previous session or type it
/plan
```

3. Show auto-invocation example:
```
# In Claude Code, type:
post this tweet: Just shipped a new Claude Code tutorial
```
Wait for Claude to auto-invoke the post skill.

**Timing note:** Keep the comparison table on screen for at least 5 seconds so viewers can read it.

---

### Segment 3: SKILLS FOLDER AND FORMAT (Target: 2 min)

**What to say:** Follow script Section 2

**What to show:**
1. Run `ls ~/.claude/skills/` to show existing files
2. Open one skill file to show the YAML frontmatter + body

**Exact commands:**
```bash
ls ~/.claude/skills/
cat ~/.claude/skills/post.md  # or whichever skill looks cleanest
```

**Key moments to emphasize:**
- Point out the YAML frontmatter (pause cursor on each field)
- Highlight `disable-model-invocation` and explain the true vs false distinction
- Scroll through the instruction body slowly

---

### Segment 4: BUILD A SKILL LIVE (Target: 5 min)

**What to say:** Follow script Section 3

**This is the core demo. Type everything live. Do NOT paste.**

**Exact commands in order:**

```bash
# Step 1: Create the skills folder (if needed)
mkdir -p ~/.claude/skills

# Step 2: Create the file
touch ~/.claude/skills/social-post-writer.md

# Step 3: Open in editor (use whatever editor you prefer)
code ~/.claude/skills/social-post-writer.md
# OR: nano ~/.claude/skills/social-post-writer.md
```

**Step 4: Type the YAML frontmatter (see script for exact content)**

Type at a natural pace. Narrate as you type: "Name is social-post-writer. Description tells Claude what this does..."

**Step 5: Type the instruction body (see script for exact content)**

You can speed this up slightly. Hit the key points verbally:
- "I'm giving it platform-specific guidelines"
- "Character limits for each platform"
- "Rules to keep the output sounding human"

**Step 6: Save and test**

```bash
# Open Claude Code
claude

# Test the skill with a natural prompt
> Write me a social media post about how I use Claude Code skills to automate my YouTube workflow
```

**What to expect:** Claude should auto-invoke the skill, generate 3 options per platform, include character counts.

**If something goes wrong:** Have the completed skill file ready to paste as backup. Don't let the demo stall.

---

### Segment 5: REAL SKILLS IN ACTION (Target: 3 min)

**What to say:** Follow script Section 4

**Exact commands:**

```bash
# Show all skills
ls ~/.claude/skills/

# Demo 1: Thumbnail generator
# In Claude Code:
> Create a YouTube thumbnail for a video about Claude Code skills

# Demo 2: Transcribe
# In Claude Code (have a YouTube URL ready):
> Transcribe this video: https://www.youtube.com/watch?v=XXXXX
```

**Key moments:**
- When the thumbnail generates, let it sit on screen for 3-4 seconds
- When the transcript saves, scroll through briefly to show it's real text
- Show genuine reaction — "That just happened from one sentence"

**Backup plan:** If the API is slow, have pre-generated outputs ready to show. Say "I ran this earlier and here's what it produced" rather than waiting on screen.

---

### Segment 6: COMMUNITY SKILLS AND TIPS (Target: 1 min)

**What to say:** Follow script Section 5

**What to show:**
1. Browser tab with GitHub repos or community skill examples
2. Copy a skill file into ~/.claude/skills/ to demonstrate

```bash
# Show copying a community skill
cp ~/Downloads/community-skill.md ~/.claude/skills/
```

**Deliver three pro tips with brief pauses between each.**

---

### Segment 7: OUTRO (Target: 30 sec)

**What to say:** Follow script Outro

**What to show:** End screen with subscribe button, next episode card

---

## Timing Cheat Sheet

| Segment | Target Duration | Running Total |
|---------|----------------|---------------|
| Intro | 1:30 | 1:30 |
| What Are Skills | 2:00 | 3:30 |
| Folder and Format | 2:00 | 5:30 |
| Build Skill Live | 5:00 | 10:30 |
| Real Skills Demo | 3:00 | 13:30 |
| Community + Tips | 1:00 | 14:30 |
| Outro | 0:30 | 15:00 |

**Total: ~15 minutes**

---

## Post-Recording Notes

- Review the live build segment — if any typos happened, note timestamps for potential jump cuts
- Verify all terminal text is readable at 1080p on a phone screen
- Capture a clean screenshot of the finished skill file for the thumbnail
- Export the social-post-writer.md file to include as a free download in the description
