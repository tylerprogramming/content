# Filming Guide — 10 Claude Code Concepts I Wish I Knew From the Start

## Pre-Recording Setup

- [ ] Open `~/.claude/CLAUDE.md` in your editor — have it ready to show
- [ ] Open `~/.claude/skills/` folder — have it open in VS Code/editor
- [ ] Open `~/.claude/settings.json` — have your allowlist visible
- [ ] Open a fresh Claude Code terminal session
- [ ] Close Slack, notifications, anything that could pop up
- [ ] Have a second terminal tab open for worktree demo
- [ ] Screen recording software running — crop to terminal + editor side by side
- [ ] Good lighting, teleprompter loaded with script

---

## Timing Cheat Sheet

| Section | Target Duration | Running Total |
|---------|----------------|---------------|
| Hook | 0:35 | 0:35 |
| Framing | 0:25 | 1:00 |
| #1 CLAUDE.md | 1:30 | 2:30 |
| #2 Context Window | 1:15 | 3:45 |
| #3 Permissions | 1:15 | 5:00 |
| #4 Slash Commands | 1:15 | 6:15 |
| #5 Skills | 1:30 | 7:45 |
| #6 Hooks | 1:00 | 8:45 |
| #7 MCP Servers | 1:00 | 9:45 |
| #8 Sub-agents | 1:00 | 10:45 |
| #9 Git + Worktrees | 1:00 | 11:45 |
| #10 Memory | 1:00 | 12:45 |
| CTA | 0:45 | 13:30 |

**Target: 13–14 minutes.**

---

## Step-by-Step Filming

### Step 1 — Hook (0:00–0:35)
**What you do:** On camera, talking head. No screen yet.

**What you say:**
> "I've been using Claude Code every single day for months. And if I'm being honest — the first few weeks I was doing it completely wrong..."

**[SHOW ON SCREEN]** Nothing yet. Cut to screen at end of hook when you say "Let me show you my real setup."

**Energy:** Direct, slightly confessional. Not overly excited. Sets up credibility.

---

### Step 2 — Concept 1: CLAUDE.md (1:00–2:30)

**What you do:**
1. Switch to editor with your CLAUDE.md open
2. Slowly scroll through it while narrating
3. Cut back to terminal
4. Type the demo prompt

**Exact demo prompt:**
```
Help me create a CLAUDE.md for my project. Ask me questions about my stack, workflow preferences, and coding conventions. Build the file as we go.
```

**What you say:**
> "Every session starts here. Claude reads this before anything else. This is mine — my rules, my workflow, my preferences. Wrote it once, benefits every session."

**What to show on screen:** Your actual CLAUDE.md. Let viewers read a few lines. The longer it is, the more impressive.

**Fill dead air while Claude responds:** "Notice how it's asking clarifying questions — that's exactly what you want. The more specific your CLAUDE.md, the less Claude has to guess."

---

### Step 3 — Concept 2: Context Window (2:30–3:45)

**What you do:**
1. Show the green context bar at bottom of terminal (may need fresh session to see it)
2. Type `/compact` with an argument

**Exact demo command:**
```
/compact keep the architecture decisions and API structure we discussed
```

**What you say:**
> "See that green bar? That's your context meter. When it fills up, Claude starts forgetting the earlier stuff. That's context rot. The fix is `/compact` — it summarizes and clears the noise."

**What to show:** Terminal with the green progress bar visible. After `/compact` — show the compressed summary Claude returns.

---

### Step 4 — Concept 3: Permissions (3:45–5:00)

**What you do:**
1. Open settings.json in editor — show your existing allowlist
2. Type the demo prompt in terminal

**Exact demo prompt:**
```
Add safe permissions to my settings.json: reading files, running tests, Git operations, and starting the dev server. Show me what you're adding before you save it.
```

**What to show:** settings.json with the allowlist. Then Claude showing the proposed additions before writing.

**What you say:**
> "Claude writes the config for you. You just review it. Now Claude pre-approves these safe actions — no interruptions. Everything risky still needs my approval."

---

### Step 5 — Concept 4: Slash Commands (5:00–6:15)

**What you do:**
1. Type `/help` in terminal — let it display the command list
2. Show your `.claude/commands/` folder briefly

**Exact demo command:**
```
/help
```

**What to show:** The full slash command menu. Then cut to your custom commands folder showing 2-3 real command files.

**What you say:**
> "Type slash-help to see everything. But the real power is here — your custom commands folder. Any repetitive task becomes a command. I have commands for my whole YouTube workflow."

---

### Step 6 — Concept 5: Skills (6:15–7:45)

**What you do:**
1. Show `~/.claude/skills/` folder — let them see all your skills
2. Open one skill file (recommend: `yt/SKILL.md` or a simpler one)
3. Type `/yt` or another skill command to show invocation

**What to show:** Skills folder with all your skill directories visible. Then open one SKILL.md and show the structure — front matter + instructions.

**What you say:**
> "This is one skill. It's the one that plans my YouTube videos. Every time I type slash-yt, Claude reads this entire file first, then follows every instruction in it."

**Slow scroll through the skill file.** Let viewers see the detail.

> "Without this, I'd type a 500-word prompt every time. With it — two characters. I have 20 of these."

---

### Step 7 — Concept 6: Hooks (7:45–8:45)

**What you do:**
1. Show the hooks section of settings.json
2. Talk through what each hook does — no need to demo live

**What to show:** settings.json hooks configuration. Highlight one specific hook (e.g., auto-formatter or logger).

**What you say:**
> "Hooks fire automatically. No AI tokens. No asking. Just runs. I have a hook that formats every file Claude edits. Every time, automatically. That's the difference between skills and hooks — skills use Claude's brain, hooks use deterministic rules."

---

### Step 8 — Concept 7: MCP Servers (8:45–9:45)

**What you do:**
1. Show your MCP configuration (mcpServers in settings or .mcp.json)
2. If possible — quickly invoke one MCP tool naturally (e.g., web search)

**What to show:** MCP server list in config. Then optionally a quick Claude session where an MCP tool gets called.

**What you say:**
> "I've got Claude connected to Telegram, Blotato, Gmail, web search. So when Claude plans a post, it can actually look things up and schedule it — all in one conversation. No separate tools."

---

### Step 9 — Concept 8: Sub-agents (9:45–10:45)

**What you do:**
1. Start a slightly complex task in Claude — one that triggers sub-agent use
2. Or describe how you use them intentionally

**Demo prompt:**
```
Research the top 5 Claude Code features that founders underutilize. Go deep — check docs, recent articles, community discussions. Come back with a structured report.
```

**What to show:** Claude spinning up a sub-agent (you'll see a separate agent starting). Highlight the "sub-agent" label in terminal output.

**What you say:**
> "See that? Claude just spun up a specialist to handle the research. Its own context window, clean slate. Main Claude stays focused while the sub-agent does the heavy lifting."

---

### Step 10 — Concept 9: Git + Worktrees (10:45–11:45)

**What you do:**
1. Show two terminal panes side by side
2. Launch two Claude worktrees

**Exact demo commands (two terminals):**
```bash
# Terminal 1
claude --worktree feature-new-skill

# Terminal 2
claude --worktree bugfix-output-format
```

**What to show:** Two terminals running separate Claude sessions. Both working simultaneously.

**What you say:**
> "Two Claudes. Different tasks. Same repo. No interference. When each one finishes, I merge the branches. Meanwhile I'm filming — Claude's still working."

---

### Step 11 — Concept 10: Memory (11:45–12:45)

**What you do:**
1. Show `~/.claude/projects/.../memory/` folder
2. Open one memory file (MEMORY.md or a specific memory file)

**What to show:** Your actual memory files. MEMORY.md index + one specific memory file showing the content.

**What you say:**
> "This is what Claude knows about me. My brand voice, my video structure, my workflow preferences. Not from this session — from months of working together. Every new session, Claude already knows this."

**Demo prompt:**
```
What do you remember about how I like to work?
```

---

### Step 12 — CTA (12:45–13:30)

**Back on camera, talking head.**

> "Those are the 10. Learn these and Claude Code stops feeling like a black box."
> "Next video — I'll show you how to build a Claude Code skill from scratch. We're building one live, for real. Link below."
> "Subscribe if you want more of this. I post Claude Code tutorials every week."

---

## On-Camera Tips

- **Each concept: aim for 60-90 seconds max.** If you're going long, cut the explanation and let the demo speak.
- **When Claude is processing:** don't wait in silence. Say "while Claude is thinking, notice that..." and point to something on screen.
- **If something breaks on camera:** keep rolling. Say "and this is where most people give up — let's debug it." That's actually great content.
- **Energy:** conversational and direct. Not hype. You've been using this for months — talk like someone sharing something genuinely useful, not selling a product.
- **Screen crop:** keep terminal and editor side by side. Don't full-screen the terminal — viewers want to see the file structure context.
