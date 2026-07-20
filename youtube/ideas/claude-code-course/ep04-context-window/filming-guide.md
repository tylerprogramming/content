# Filming Guide - Claude Code Tutorial #4 - Context Window Mastery

**Total Runtime Target:** 12 minutes
**Format:** Talking head + live terminal demo
**Prep Time:** ~15 min to set up demo conversations

---

## Pre-Filming Setup

1. **Terminal setup:**
   - Clean terminal, dark theme, large font (18-20pt)
   - Open Claude Code in a sample project directory (e.g., a simple Node.js or Python project)
   - Make sure the context bar is visible at the bottom

2. **Pre-build a long conversation:**
   - Before filming, have a session going with Claude Code that has high context usage (70%+)
   - Ask it to read several files, discuss architecture, go back and forth on decisions
   - Save this terminal state so you can show "context rot" live
   - Alternatively, prepare to fast-forward through building up context during filming

3. **Have two terminal windows/tabs ready:**
   - Tab 1: Fresh Claude Code session (for Sections 1-2)
   - Tab 2: Pre-loaded high-context session (for Sections 3-5)

---

## Recording Playbook

### Scene 1: Hook (0:00 - 0:30) -- Talking Head

**Setup:** Camera, no terminal visible
**Say:** Hook A script (see hooks.md)
**Cut to:** Terminal on "Let's get into it"

---

### Scene 2: What Is the Context Window (0:30 - 2:30) -- Terminal Demo

**Setup:** Tab 1 - Fresh Claude Code session
**What to do:**

1. Show the empty terminal
   - **Say:** "Okay. So the context window. What is it? Think of it like Claude's short-term memory..."

2. Type: `What is a REST API?`
   - Wait for response
   - **Say:** "So right now, my prompt is in the context window. Claude's response is too..."

3. Type: `Can you give me an example?`
   - Wait for response
   - **Say:** "Every message is water going into a bucket. And at some point, the bucket gets full."

---

### Scene 3: Reading the Context Bar (2:30 - 4:00) -- Terminal Demo

**Setup:** Same session, continue building context
**What to do:**

1. Point out (mouse cursor or annotation) the bottom bar
   - **Say:** "See this bar at the bottom? This is your context meter."

2. Send a few more messages to show the bar growing:
   - Type: `Explain how HTTP status codes work`
   - Type: `Now explain authentication in APIs`
   - Type: `What's the difference between REST and GraphQL?`
   - **Say:** "See it filling up? Every message adds to it."

3. **Say:** "When you see that bar getting past about 70 or 80 percent, start paying attention."

---

### Scene 4: Context Rot Demo (4:00 - 6:00) -- Terminal Demo

**Setup:** Switch to Tab 2 - Pre-loaded high-context session (70%+ context)
**What to do:**

1. Show the high context bar
   - **Say:** "I've been having a long conversation here. Look at the context bar. We're getting pretty full."

2. Ask Claude to reference something from early in the conversation:
   - Type something like: `Can you remind me of the database schema we decided on earlier?`
   - **Say:** "I'm going to ask it to reference something from the beginning of our conversation."

3. Wait for response -- it should be vague or miss details
   - **Say:** "See that? It kind of... forgot. That's context rot."

4. Quick cut to talking head:
   - **Say:** "This is totally normal. It's not Claude being bad. It's just how context windows work."

---

### Scene 5: /compact Demo (6:00 - 9:00) -- Terminal Demo

**Setup:** Same high-context session
**What to do:**

1. Type: `/compact`
   - Press Enter
   - **Say:** "Command number one. Slash compact. Watch what happens."

2. Wait for compaction to finish
   - **Say:** "Claude is compressing the conversation. Keeping the important stuff. Ditching the fluff."

3. Point out the context bar dropping
   - **Say:** "Look at that context bar. It just dropped way down."

4. Now show custom compact instructions:
   - Type: `/compact focus on the API changes we discussed`
   - Press Enter
   - **Say:** "You can tell compact what to focus on. This keeps the API details crisp while summarizing everything else."

5. Quick cut to talking head for the "real example" explanation

6. Back to terminal -- ask the same question from Scene 4:
   - Type the same database schema question
   - **Say:** "See? The output is better now. More focused. Because Claude's context is clean."

---

### Scene 6: /clear Demo (9:00 - 10:30) -- Terminal Demo

**Setup:** Same session
**What to do:**

1. Type: `/clear`
   - Press Enter
   - **Say:** "Slash clear. This just... wipes everything."

2. Show the reset context bar (zero)
   - **Say:** "Zero context. Claude remembers nothing."

3. Quick cut to talking head:
   - **Say:** "Compact is like cleaning your desk. Clear is like getting a brand new desk."

---

### Scene 7: Auto-Compaction (10:30 - 11:15) -- Terminal or Talking Head

**Setup:** Talking head or terminal screenshot
**What to do:**

1. **Say:** "Claude Code has auto-compaction built in. At about 85 to 95 percent full, it compacts automatically."
2. If you can trigger auto-compaction live, great. Otherwise just explain it.
3. **Say:** "Don't rely on it. Compact proactively."

---

### Scene 8: Recap & Next Episode (11:15 - 12:00) -- Talking Head

**Setup:** Camera, no terminal
**Say:** Recap script from script.md
**Reminder:** Tease Episode 5 (Permissions & Safety)

---

## Timing Cheat Sheet

| Section | Start | Duration | Type |
|---------|-------|----------|------|
| Hook | 0:00 | 30 sec | Talking head |
| What is context window | 0:30 | 2 min | Terminal |
| Reading the context bar | 2:30 | 1.5 min | Terminal |
| Context rot demo | 4:00 | 2 min | Terminal |
| /compact demo | 6:00 | 3 min | Terminal + talking head |
| /clear demo | 9:00 | 1.5 min | Terminal |
| Auto-compaction | 10:30 | 45 sec | Talking head |
| Recap + next ep | 11:15 | 45 sec | Talking head |

---

## B-Roll / Overlay Ideas

- Bucket filling with water (context filling up)
- Gas gauge analogy for the context bar
- Side-by-side: output quality at 30% context vs 90% context
- Simple text overlay showing the two commands: `/compact` and `/clear`

---

## Common Mistakes to Avoid During Filming

- Don't rush through the compaction -- let the viewer see the bar drop
- Make sure the pre-loaded session actually shows degraded output (test beforehand)
- Keep the terminal font large enough to read on mobile
- Don't use technical jargon without immediately explaining it
