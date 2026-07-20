# Filming Guide: Claude Code 30-Minute Course

## Overview

| Item | Detail |
|------|--------|
| Total length | ~30 minutes |
| Talking head | ~40% (12 min) |
| Screen recording | ~55% (16.5 min) |
| B-roll/transitions | ~5% (1.5 min) |
| Camera | Main camera, standard setup |
| Lighting | Standard key light setup |
| Energy | Confident, conversational. Like teaching a friend. NOT lecture mode. |

---

## Pre-Filming Checklist

### Screen Recording Prep
- [ ] Open VS Code with the CLAUDE.md file already loaded
- [ ] Open a clean terminal tab for Claude Code demos
- [ ] Have ~/.claude/skills/ directory ready to show (25 folders visible)
- [ ] Have a sample /yt output folder ready (don't generate live, use a pre-made one)
- [ ] Have Blotato open in a browser tab (for MCP demo)
- [ ] Have a git repo with some commit history ready
- [ ] Clear desktop of anything personal/distracting
- [ ] Set terminal font size to at least 16pt so viewers can read it
- [ ] Turn off notifications (Do Not Disturb)
- [ ] Close Slack, email, any notification sources

### Talking Head Prep
- [ ] Script the first 30 seconds and rehearse 3 times
- [ ] Print the CueCard section (end of script.md) for teleprompter
- [ ] Have water nearby
- [ ] Wear a solid-color shirt (no patterns, no logos)

---

## Shot-by-Shot Plan

### INTRO (0:00 - 1:30) | Talking Head + Quick Cuts

**Shot 1 (0:00 - 0:30): Word-for-word opening**
- Format: Talking head, direct to camera
- Energy: Start calm and honest ("I'm going to be honest"), then build energy through the "32 pieces of content" line
- Tip: Rehearse this 5 times. Nail the delivery. This is the hook.

**Shot 2 (0:30 - 1:00): Structure preview**
- Format: Talking head with quick screen flashes
- Have open on screen: Nothing yet, just you
- Cut to: Quick 1-second flashes of CLAUDE.md file, terminal, skill outputs (edit these in post)

**Shot 3 (1:00 - 1:30): Quick context**
- Format: Talking head with B-roll overlay
- B-roll needed: Tyler's YouTube channel page, recent thumbnails, content calendar (can be screenshots, 2-3 seconds each)

---

### CONCEPT 1: CLAUDE.md (1:30 - 4:30) | Screen-Heavy

**Shot 4 (1:30 - 1:50): Hook line**
- Format: Talking head
- Energy: Firm, authoritative. "If you only learn one thing, make it this."

**Shot 5 (1:50 - 3:00): Show the file**
- Format: Screen recording
- What to have open: VS Code with ~/.claude/CLAUDE.md
- Action: Scroll through slowly. Pause on the skills table, the workflow section, the preferences section.
- Narrate what each section does as you scroll

**Shot 6 (3:00 - 3:45): Live demo**
- Format: Screen recording
- What to have open: Clean terminal
- Action: Type "/yt claude code for creators" (use a pre-recorded version or a pre-made output so you don't wait 5 minutes live)
- Show the output directory with all the files appearing

**Shot 7 (3:45 - 4:30): Takeaway + transition**
- Format: Talking head
- Energy: Direct, instructional. "Here's what I want you to do."
- Deliver the re-engagement line looking right into camera

---

### CONCEPT 2: Context Window (4:30 - 7:30) | Mixed

**Shot 8 (4:30 - 5:00): Hook**
- Format: Talking head
- Energy: Slightly frustrated tone, like you've experienced the pain

**Shot 9 (5:00 - 6:15): Explanation + demo**
- Format: Screen recording
- What to have open: Claude Code terminal with a session in progress
- Action: Show the context usage indicator. If possible, show a fresh session (20%) vs a long session (80%). Demonstrate /clear and /compact.
- Tip: Pre-record two terminal sessions at different context levels

**Shot 10 (6:15 - 7:00): Desk analogy**
- Format: Talking head
- Energy: Casual, relatable. The desk analogy should feel natural.

**Shot 11 (7:00 - 7:30): Transition to permissions**
- Format: Talking head
- Energy: Build anticipation. The re-engagement line bridges to the next section.

---

### CONCEPT 3: Permissions (7:30 - 10:30) | Screen-Heavy

**Shot 12 (7:30 - 7:50): Hook**
- Format: Talking head

**Shot 13 (7:50 - 9:30): Demo**
- Format: Screen recording
- What to have open: Claude Code terminal
- Action: Show a permission prompt appearing. Click "yes" multiple times to show the friction. Then show the settings file where you configure permanent permissions.
- What to show: .claude/settings.json with the allow list

**Shot 14 (9:30 - 10:30): Takeaway + transition**
- Format: Talking head
- Energy: Encouraging. "Start strict, loosen over time."

---

### CONCEPT 4: Slash Commands (10:30 - 13:30) | Screen-Heavy

**Shot 15 (10:30 - 10:50): Hook**
- Format: Talking head

**Shot 16 (10:50 - 12:30): Demo montage**
- Format: Screen recording
- What to have open: Claude Code terminal
- Action sequence:
  1. Type "/" and show the autocomplete dropdown with all 25 skills
  2. Run /yt and show output (use pre-recorded)
  3. Run /thumbnail and show a generated thumbnail appearing
  4. Run /shorts and show the scripts being generated
- Tip: Pre-record each of these. Edit them into a fast montage with quick cuts.

**Shot 17 (12:30 - 13:30): Bridge to skills**
- Format: Talking head
- Energy: Building excitement. "Slash commands are the trigger. Skills are the engine."

---

### CONCEPT 5: Skills (13:30 - 16:30) | Screen-Heavy, Key Section

**Shot 18 (13:30 - 14:00): Hook**
- Format: Talking head
- Energy: This is the most important section. Show it.

**Shot 19 (14:00 - 15:15): Show skills directory + file**
- Format: Screen recording
- What to have open: VS Code file explorer showing ~/.claude/skills/ (all 25 folders)
- Action: Open the skills directory. Slowly scroll through the folder names so viewers can read them. Then open one skill's SKILL.md file (recommend /yt or /content). Scroll through it.
- Key moment: Pause on the SKILL.md and say "This is maybe 50 lines of markdown. No code."

**Shot 20 (15:15 - 15:45): Show the output**
- Format: Screen recording
- What to have open: A completed video package folder
- Action: Show the files that one /yt command created. Quickly open script.md, titles.md to show the quality.

**Shot 21 (15:45 - 16:30): Takeaway**
- Format: Talking head
- Energy: Empowering. "Pick one thing you do manually. Write it down. That's a skill."
- Deliver the halfway mark line with extra energy.

---

### CONCEPT 6: Hooks (16:30 - 19:30) | Mixed

**Shot 22 (16:30 - 17:00): Hook**
- Format: Talking head
- Clarify: "Not YouTube hooks, Claude Code hooks."

**Shot 23 (17:00 - 18:30): Explanation + demo**
- Format: Screen recording
- What to have open: Hook configuration file, then a demo of a hook running
- Action: Show a before/after. Generate a LinkedIn post with hashtags, then show the hook removing them automatically.

**Shot 24 (18:30 - 19:30): Takeaway + transition**
- Format: Talking head
- Energy: The MCP teaser should feel like "wait until you see this"

---

### CONCEPT 7: MCP Servers (19:30 - 22:30) | Screen-Heavy, Wow Factor

**Shot 25 (19:30 - 19:50): Hook**
- Format: Talking head

**Shot 26 (19:50 - 21:30): Blotato demo**
- Format: Screen recording (split screen if possible: terminal + Blotato browser)
- What to have open: Claude Code terminal on left, Blotato dashboard in browser on right
- Action: Run /content skill. Show Claude writing the post AND show it appearing in Blotato's queue. This is the "wow" moment.
- Tip: Pre-record this. The live timing might not sync perfectly.

**Shot 27 (21:30 - 22:00): Show config**
- Format: Screen recording
- What to have open: MCP config file in VS Code
- Action: Show the Blotato, Calendar, Slack entries. Keep it brief.

**Shot 28 (22:00 - 22:30): Takeaway + transition**
- Format: Talking head
- Energy: Forward momentum. We're building to the finish.

---

### CONCEPT 8: Sub-Agents (22:30 - 25:00) | Mixed

**Shot 29 (22:30 - 22:50): Hook**
- Format: Talking head

**Shot 30 (22:50 - 24:00): Demo**
- Format: Screen recording
- What to have open: Claude Code terminal running /shorts
- Action: Show the "Spawning sub-agent..." messages in the terminal. Show parallel work happening.
- Tip: This can be a pre-recorded session. The key visual is multiple agents working at once.

**Shot 31 (24:00 - 25:00): Explanation + transition**
- Format: Talking head
- Energy: Calm, knowledgeable. "You don't manage them manually."

---

### CONCEPT 9: Git (25:00 - 27:30) | Mixed

**Shot 32 (25:00 - 25:20): Hook**
- Format: Talking head
- Energy: Reassuring. "Even if you've never used git before."

**Shot 33 (25:20 - 26:45): Demo**
- Format: Screen recording
- What to have open: Terminal with git log showing Claude's commits
- Action: Run git log, show the commit history. Then demonstrate reverting one change. Keep the demo under 90 seconds.

**Shot 34 (26:45 - 27:30): Takeaway + transition**
- Format: Talking head
- Energy: Build to the finale. "Last one. This ties everything together."

---

### CONCEPT 10: Memory (27:30 - 29:30) | Mixed

**Shot 35 (27:30 - 27:50): Hook**
- Format: Talking head

**Shot 36 (27:50 - 28:45): Demo**
- Format: Screen recording
- What to have open: MEMORY.md file in VS Code
- Action: Show the file contents. Then demonstrate adding a new memory: tell Claude "remember that we use Blotato for all social scheduling" and show it writing to the file.

**Shot 37 (28:45 - 29:30): The "full system" moment**
- Format: Talking head
- Energy: Peak energy. This is the payoff. Connect all 10 concepts into one system.

---

### OUTRO + CTA (29:30 - 30:30) | Talking Head

**Shot 38 (29:30 - 30:30): CTA**
- Format: Talking head, direct to camera
- Energy: High, motivating, direct
- Key beats:
  1. Recap the 10 concepts (list them fast)
  2. Challenge: "Pick ONE thing you do manually"
  3. Comment prompt: "Tell me what you'd automate first"
  4. Skool mention: "Full system is in my community, link in description"
  5. End screen point: "If you want to see me build a skill from scratch, watch this"
- Do NOT trail off. Keep energy up through the very last word.

---

## Filming Order (Recommended)

Film screen recordings first, then talking head. This builds confidence.

### Session 1: Screen Recordings (~2 hours)

1. CLAUDE.md file walkthrough (Shot 5)
2. /yt command demo (Shot 6) - use pre-made output
3. Context window: /clear and /compact demos (Shot 9)
4. Permissions prompt demo (Shot 13)
5. Slash command montage: /, /yt, /thumbnail, /shorts (Shot 16)
6. Skills directory + SKILL.md walkthrough (Shot 19-20)
7. Hooks demo: LinkedIn formatting (Shot 23)
8. MCP: Blotato split-screen demo (Shot 26)
9. MCP config file (Shot 27)
10. Sub-agents: /shorts spawning (Shot 30)
11. Git log + revert demo (Shot 33)
12. MEMORY.md walkthrough + add memory (Shot 36)

### Session 2: Talking Head (~1.5 hours)

Film in script order. Use the CueCard from script.md on a teleprompter or monitor.

1. Intro (Shots 1-3) - DO THIS FIRST while energy is highest
2. Concept hooks and takeaways (Shots 4, 7, 8, 10-12, 14-15, 17-18, 21-22, 24-25, 28-29, 31-32, 34-35, 37)
3. Outro/CTA (Shot 38) - Film this 2-3 times. Pick the highest energy take.

---

## Energy Notes

| Section | Energy Level | Tone |
|---------|-------------|------|
| Intro (0:00-0:30) | Start calm, build to 8/10 | Honest, then excited |
| Concepts 1-3 | 6/10 | Teaching, clear, patient |
| Concepts 4-5 | 8/10 | Excited, this is the good stuff |
| Halfway mark | 9/10 | Peak energy moment |
| Concepts 6-8 | 7/10 | Confident, showing mastery |
| Concepts 9-10 | 7/10, building to 8/10 | Wrapping up, connecting the dots |
| CTA | 9/10 | Motivating, challenging, direct |

## Post-Production Notes

- Use jump cuts between talking head sections (no long pauses)
- Add lower-third text for each concept number: "Concept 1: CLAUDE.md"
- Add a progress bar or concept counter graphic in the corner
- Screen recordings should have a subtle zoom to whatever Tyler is pointing at
- B-roll for intro: channel page, thumbnails, content calendar (2-3 sec each)
- End screen: 15 seconds, point to "build a skill from scratch" video
