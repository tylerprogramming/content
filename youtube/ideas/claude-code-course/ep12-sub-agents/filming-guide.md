# Filming Guide — Claude Code Tutorial #12: Sub-agents

## Pre-Recording Checklist

- [ ] Have a project with real code open (your course repo or personal site)
- [ ] The project should have at least a few files with minor "issues" for the security agent to find (e.g., a console.log with a debug API key, a missing input validation)
- [ ] `.claude/agents/` folder should be EMPTY before recording (you're building from scratch)
- [ ] Terminal font size: 16pt+
- [ ] Screen recording: 1920x1080, 30fps
- [ ] Prepare the complex task prompt for the auto-spawn demo (copy to clipboard)
- [ ] Webcam positioned for face cam overlay

---

## Recording Playbook

### Segment 1: INTRO (Target: 1:15)

**What to say:** Deliver Hook Option 1 word-for-word

**What to show:**
1. Terminal with Claude spawning a sub-agent (can be pre-recorded B-roll)
2. Face cam for hook delivery

---

### Segment 2: WHAT ARE SUB-AGENTS (Target: 2 min)

**What to say:** Follow script Section 1

**What to show:**
1. Simple diagram (prepare as graphic or draw live)
2. Expanded diagram showing main agent + three sub-agents

**No terminal commands — pure explanation with visuals.**

**Tip:** Use a whiteboard app or Keynote animation for the diagrams. Keep them simple — boxes and arrows.

---

### Segment 3: AUTO-SPAWNING DEMO (Target: 2 min)

**What to say:** Follow script Section 2

**Exact commands:**

```bash
claude
```

**Type this prompt:**
```
I need you to do three things: First, research the best practices for React error boundaries in 2026. Second, look through my codebase and find everywhere I'm not handling errors properly. Third, fix each one following the best practices you found.
```

**What to watch for:** Claude should show agent activity in the output. Look for indicators like "Using agent..." or tool delegation patterns.

**If sub-agents don't spawn:** This depends on the complexity Claude perceives. If it tries to do everything inline, either:
- Use a more complex prompt with more distinct phases
- Or narrate: "Sometimes Claude handles it inline for simpler projects. On larger codebases, you'd see sub-agents spawn here."

---

### Segment 4: BUILD SECURITY REVIEWER (Target: 3:30)

**What to say:** Follow script Section 3

**Type everything live. Do NOT paste.**

**Exact commands in order:**

```bash
# Create the agents folder
mkdir -p .claude/agents

# Create the security reviewer file
touch .claude/agents/security-reviewer.md

# Open in editor
code .claude/agents/security-reviewer.md
```

**Type the YAML frontmatter and instructions from the script.**

Narrate as you type:
- "Name is security-reviewer"
- "I'm only giving it Read, Grep, Glob, and Bash — no Write access"
- "The instructions tell it exactly what to look for"

**Key teaching moments:**
- When typing the `tools` list, explicitly say "Notice I'm NOT giving it Write. This agent reads and reports only."
- When typing the output format, say "Structured output means I can scan results quickly"

---

### Segment 5: RUN THE AGENTS (Target: 2:15)

**Exact commands:**

```bash
# In Claude Code
> Run the security-reviewer agent on my src/ folder
```

**Let the output flow. Don't interrupt. Point at findings as they appear.**

Then create the research agent (can type faster for this one since viewers already understand the format):

```bash
code .claude/agents/research-agent.md
```

**Type the research agent content from script.**

```bash
# Test it
> Research the latest changes in React Server Components and summarize what I need to know
```

**Show the web searches happening in real time. React to the output.**

---

### Segment 6: TIPS (Target: 45 sec)

**What to say:** Follow script Section 5

**What to show:** Tips list as text overlay or bullet points. No terminal needed.

---

### Segment 7: OUTRO (Target: 15 sec)

**What to say:** Follow script Outro

**What to show:** End screen

---

## Timing Cheat Sheet

| Segment | Target Duration | Running Total |
|---------|----------------|---------------|
| Intro | 1:15 | 1:15 |
| What Are Sub-agents | 2:00 | 3:15 |
| Auto-Spawning Demo | 2:00 | 5:15 |
| Build Security Reviewer | 3:30 | 8:45 |
| Run the Agents | 2:15 | 11:00 |
| Tips | 0:45 | 11:45 |
| Outro | 0:15 | 12:00 |

**Total: ~12 minutes**

---

## Seeding the Demo (IMPORTANT)

For the security reviewer demo to be impressive, you need at least 2-3 findings. Before recording, add these to your demo project:

**File: src/config.js**
```javascript
// "Temporary" API key for testing
const API_KEY = "sk-1234567890abcdef";
```

**File: src/api/users.js**
```javascript
// Missing input sanitization
app.get('/user/:id', (req, res) => {
  const query = `SELECT * FROM users WHERE id = ${req.params.id}`;
});
```

**File: .env.example** (but also have a .env committed)

These give the security agent real findings to report, making the demo compelling.

---

## Post-Recording Notes

- Verify diagram animations are clear at 1080p on mobile
- Make sure the security report is legible — zoom in during post if needed
- Export the security-reviewer.md as a downloadable for the description
- Review the auto-spawn segment — if sub-agents didn't clearly appear, consider adding a text overlay explaining what's happening
