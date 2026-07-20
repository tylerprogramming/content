# Claude Code Course — Full Outline

**Format:** 13-episode YouTube playlist
**Target length:** 10-15 min per episode
**Style:** Fast-paced, practical tutorials with live demos
**Audience:** Non-technical founders and beginners

---

## Episode 1: Introduction & Setup (10 min)
**What you cover:**
- What is Claude Code vs ChatGPT/Gemini (chatbots talk, Claude Code takes action)
- Installing Claude Code (npm, API key setup)
- The terminal — it's not scary (open, close, clear)
- Your first prompt — build something simple live
- Quick tour of the interface (context bar, approval prompts)

**Demo:** Install Claude Code from scratch. Type your first prompt. Build a simple landing page in under 2 minutes.

**Hook:** "By the end of this video, you'll have Claude Code installed and your first project built — even if you've never opened a terminal before."

---

## Episode 2: Prompting Like a Pro (12 min)
**What you cover:**
- Why specificity matters (vague vs specific prompts side by side)
- The anatomy of a great prompt (context + task + constraints + format)
- Common prompting mistakes beginners make
- Iterating on results — how to give feedback
- When to start a new conversation vs keep going

**Demo:** Build the same project twice — once with a vague prompt, once with a detailed prompt. Show the difference. Then iterate on the result with follow-up prompts.

**Hook:** "The difference between Claude Code giving you garbage and giving you exactly what you want comes down to one skill."

---

## Episode 3: CLAUDE.md — The Most Important File (12 min)
**What you cover:**
- What CLAUDE.md is and why it matters
- Using /init to auto-generate one
- What to put in it (and what NOT to put)
- Global vs project-level CLAUDE.md files
- @imports for larger projects
- Iterating on your CLAUDE.md over time ("every mistake becomes a rule")

**Demo:** Start a project without CLAUDE.md — show Claude guessing wrong. Then create one with /init, customize it, and show Claude following the rules perfectly.

**Hook:** "There's one file that 90% of Claude Code users are ignoring — and it's the reason their results suck."

---

## Episode 4: Context Window Mastery (12 min)
**What you cover:**
- What the context window is (Claude's short-term memory)
- Why it matters more than anything else
- Reading the context bar
- Context rot — when and why outputs get worse
- /compact — smart summarization (with custom instructions)
- /clear — starting fresh
- When to use each one
- Auto-compaction (what happens behind the scenes)

**Demo:** Start a long conversation. Show the context bar filling up. Show outputs degrading. Then use /compact and show improvement. Then /clear for a fresh start.

**Hook:** "If you only learn one concept from this entire course, make it this one."

---

## Episode 5: Permissions & Safety (10 min)
**What you cover:**
- Why Claude asks for approval (it can change your computer)
- The approval prompt — what it looks like
- Pre-approving safe actions with /permissions
- settings.json — the allow list and deny list
- What to pre-approve (read files, run tests, dev server, git)
- What to keep gated (installs, deletes, API calls)
- Having Claude set up your permissions for you

**Demo:** Show the approval flow. Then set up permissions with /permissions. Show Claude working faster without stopping. Then show a deny list protecting sensitive files.

**Hook:** "Clicking approve every 10 seconds kills your flow. Here's how to fix it without compromising safety."

---

## Episode 6: Models & Memory (10 min)
**What you cover:**
- The three models: Haiku (fast/cheap), Sonnet (balanced), Opus (powerful)
- When to use each one
- Switching mid-conversation with /model
- Automatic memory — how Claude learns your preferences
- Manually telling Claude to remember things
- Reviewing what Claude remembers

**Demo:** Switch between models on the same task. Show the quality/speed difference. Then set a memory ("I prefer bun over npm"), start a new session, and show Claude remembering.

**Hook:** "You're probably using the wrong Claude model for the wrong task — and it's costing you."

---

## Episode 7: Plan Mode & Thinking (12 min)
**What you cover:**
- Plan Mode — Ctrl+G to toggle
- Read-only exploration before building
- The workflow: Explore > Plan > Implement > Commit
- Editing plans in your text editor (Ctrl+G again)
- When to use Plan Mode vs just building
- Extended thinking — Claude reasoning before acting (on by default)

**Demo:** Open a project. Toggle Plan Mode. Ask Claude to plan a feature — show it reading files and proposing steps without changing anything. Then switch to normal mode and let it build. Show the difference vs diving in blind.

**Hook:** "The biggest mistake Claude Code beginners make is letting Claude build before it thinks."

---

## Episode 8: Session Management & Checkpoints (12 min)
**What you cover:**
- Sessions are saved automatically
- --resume to pick a previous session
- --continue to jump back into the most recent
- /rename to name sessions
- Checkpoints — auto-snapshots before every edit
- /rewind — go back to any point
- Restoring code, conversation, or both

**Demo:** Work on something, close Claude Code. Reopen with --resume, show the session list. Resume one. Then make some changes, intentionally break something, and use /rewind to restore.

**Hook:** "Claude Code has a built-in time machine and most people don't even know it exists."

---

## Episode 9: Slash Commands & Custom Commands (12 min)
**What you cover:**
- Built-in slash commands overview (/help, /clear, /compact, /model, /init, /rewind, etc.)
- Creating custom slash commands
- The .claude/commands/ folder
- Writing a command file (markdown format)
- Running custom commands with /command-name
- Practical examples: deploy command, test command, report command

**Demo:** Show /help listing all commands. Then create a custom slash command from scratch — like a /deploy command that runs your deploy steps. Run it and show it working.

**Hook:** "If you're typing the same prompts over and over, you're doing Claude Code wrong."

---

## Episode 10: Skills — Teaching Claude to Be an Expert (15 min)
**What you cover:**
- What skills are (specialized instruction files)
- How they differ from slash commands (deeper, auto-invocable)
- The .claude/skills/ folder and SKILL.md format
- Auto-invocation vs manual-only
- Building your first skill from scratch
- Using community skills
- Real example: show one of your custom skills in action

**Demo:** Build a skill from scratch live — something like a "social media post writer" skill. Show the SKILL.md file, the instructions, then trigger it and show Claude following the specialized instructions. Then show one of your existing skills (/thumbnail or /fitness) for a "wow" moment.

**Hook:** "Skills turn Claude Code from a general assistant into a specialized expert — and building one takes less than 5 minutes."

---

## Episode 11: MCP Servers — Connecting Your Tools (13 min)
**What you cover:**
- What MCP is (Model Context Protocol)
- Why it matters (Claude can now interact with external tools)
- Setting up your first MCP server (GitHub)
- The setup command
- Interacting with GitHub through Claude Code
- Other popular MCP servers (Notion, Slack, databases, Figma)
- Where to find MCP servers

**Demo:** Set up the GitHub MCP server from scratch. Then ask Claude to list your repos, create an issue, check PRs. Show data flowing between Claude and GitHub in real time.

**Hook:** "What if Claude Code could control your GitHub, your database, and your Notion — all from one terminal?"

---

## Episode 12: Sub-agents — Delegating to Specialists (12 min)
**What you cover:**
- What sub-agents are (separate Claude instances with their own context)
- Why they matter (keeps main context clean)
- When Claude auto-spawns sub-agents
- Creating custom sub-agents in .claude/agents/
- YAML frontmatter for tools, model, and system prompt
- Practical examples: research agent, code review agent, security agent

**Demo:** Give Claude a complex task and watch it spawn sub-agents naturally. Then create a custom security-review agent from scratch, run it on your project, and show the results.

**Hook:** "What if you could clone Claude and have multiple versions working on different parts of your project at the same time?"

---

## Episode 13: Hooks & Automation (12 min)
**What you cover:**
- What hooks are (shell scripts triggered at lifecycle events)
- Key difference: hooks are deterministic (no AI tokens)
- Lifecycle events: before/after tool execution, on prompt, on response
- Setting up hooks with /hooks or settings.json
- Having Claude write hooks for you
- Practical examples: auto-lint, logging, blocking writes to protected folders
- Combining hooks with everything else you've learned

**Demo:** Set up a hook that auto-formats code after every edit. Show Claude editing a file and the hook firing automatically. Then set up a logging hook. Then a protection hook that blocks edits to a migrations folder.

**Hook:** "Hooks are the most underrated feature in Claude Code — they run automatically, they never fail, and they cost you nothing."

---

## Bonus Ideas (if you want to extend to 15)

### Episode 14: Building a Real Project Start to Finish
- Take everything from episodes 1-13
- Build a complete project live (SaaS landing page, API, or tool)
- Show the full workflow: /init, CLAUDE.md, Plan Mode, skills, sub-agents
- Real mistakes, real debugging, real iteration

### Episode 15: Advanced Tips & What's Next
- @ file references and rich input methods
- Screenshots/images for bug fixing
- Git integration and worktrees
- Background agents
- Agent teams (preview)
- Where Claude Code is heading

---

## Course-Level Strategy

### Playlist Structure
- Consistent naming: "Claude Code Tutorial #1 - Introduction & Setup"
- Consistent thumbnail template (your face + episode number + topic)
- Each video starts with a 10-second "what you'll learn" preview
- Each video ends with "next episode" teaser

### Cross-Promotion
- The 21 Concepts video acts as a gateway — link to the course in the description
- Each course video links to the full playlist
- Pin a comment with the playlist link on every video

### Publishing Schedule
- 2-3 videos per week to build momentum
- Release first 3-4 at once to establish the playlist
- Remaining videos on a schedule

### Thumbnail Template
- Consistent design across all episodes
- Episode number in corner
- Topic keyword prominent
- Your face on every thumbnail
- Same color scheme/style throughout (builds brand recognition)
