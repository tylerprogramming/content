# Claude Code Tutorial #12 - Sub-agents: Delegate Tasks Like a Boss

## Full Script

---

### INTRO (0:00 - 1:15) ~1.25 min

You know what's wild? When you give Claude a complex task, it doesn't just try to do everything itself. It builds a team.

It spins up separate AI instances — each one focused on a specific piece of the problem. A researcher. A code reviewer. A security scanner. Working in parallel.

[SHOW: Terminal — Claude spawning a sub-agent, visible in the output]

These are called sub-agents. And in this video, I'm going to show you how they work, when Claude creates them automatically, and how to build your own custom specialists.

[NOTE: Title card — "Claude Code Tutorial #12 - Sub-agents"]

Let's get into it.

---

### SECTION 1: WHAT ARE SUB-AGENTS? (1:15 - 3:15) ~2 min

So what exactly is a sub-agent?

Think of it this way. When you're talking to Claude Code, you're talking to one AI instance. It has one context window — one "brain" that's tracking your entire conversation.

[SHOW: Simple diagram]
```
YOU  <--->  Claude (main agent)
            - sees your full conversation
            - knows your project context
            - has all your files loaded
```

That works great for simple tasks. But when things get complex — like "refactor this entire codebase" or "research this topic and then build a feature based on what you find" — one context window gets crowded. Fast.

[SHOW: Diagram expanding]
```
YOU  <--->  Claude (main agent)
               |
               |--- Sub-agent: Researcher
               |       (own context window)
               |       (focused on research only)
               |
               |--- Sub-agent: Code Writer
               |       (own context window)
               |       (focused on implementation)
               |
               |--- Sub-agent: Reviewer
                       (own context window)
                       (focused on code quality)
```

Sub-agents are separate Claude instances. Each one gets its own context window. Its own focus. Its own job.

The main agent delegates work. The sub-agents execute. Then they report back.

Why does this matter? Two reasons.

First — focus. A sub-agent that's only doing security review is going to catch more issues than a main agent that's juggling research, coding, and review all at once.

Second — context management. Your main conversation stays clean. All the detailed work happens in the sub-agent's context, and only the results come back to you.

---

### SECTION 2: WHEN CLAUDE AUTO-SPAWNS SUB-AGENTS (3:15 - 5:15) ~2 min

Here's the cool part. You don't always have to tell Claude to use sub-agents. It does it on its own.

Claude is smart about this. When it recognizes that a task has multiple distinct parts, it'll spin up sub-agents automatically.

[SHOW: Terminal — Claude Code prompt]

Let me show you. Watch what happens when I give Claude a complex task.

> I need you to do three things: First, research the best practices for React error boundaries in 2026. Second, look through my codebase and find everywhere I'm not handling errors properly. Third, fix each one following the best practices you found.

[SHOW: Claude processing, spawning sub-agents — the terminal should show "Using agent..." or similar indicators]

See that? Claude broke this into pieces. It's spawning a sub-agent to handle the research. Another one to scan the codebase. The results feed into the main agent, which then coordinates the fixes.

[NOTE: Point at the terminal output where sub-agent activity is visible. Circle or highlight if possible in post.]

I didn't tell it to use sub-agents. It decided on its own. That's the intelligence baked into Claude Code.

You'll notice sub-agents get spawned most often when:
- The task has clearly separate phases (research, then build, then test)
- The task involves searching across many files
- The task requires deep analysis that would eat up main context

[SHOW: Bullet list on screen]

---

### SECTION 3: CREATING CUSTOM SUB-AGENTS (5:15 - 8:45) ~3.5 min

Auto-spawning is great. But the real power is building your own.

Custom sub-agents live in a folder called `.claude/agents/` in your project.

[SHOW: Terminal]

```bash
mkdir -p .claude/agents
```

Each agent is a markdown file with YAML frontmatter. Let me build one right now.

We're going to create a security review agent. This is one I actually use. Every time I finish writing code, I run this agent and it audits everything for vulnerabilities.

[SHOW: Creating the file]

```bash
touch .claude/agents/security-reviewer.md
```

[SHOW: Opening in editor, typing the content]

```yaml
---
name: security-reviewer
description: Reviews code for security vulnerabilities, secrets exposure, and unsafe patterns
tools:
  - Read
  - Grep
  - Glob
  - Bash
---
```

Let me explain the frontmatter.

`name` — how you'll reference this agent.
`description` — tells Claude when this agent is appropriate to use.
`tools` — which tools this agent is allowed to use. This is important. You can limit what a sub-agent can do. A security reviewer doesn't need Write access — it should only read and report.

[NOTE: Emphasize the tools restriction — this is a key safety concept]

Now for the instructions.

```markdown
# Security Reviewer Agent

## Your Role
You are a security-focused code reviewer. Your job is to find vulnerabilities, not fix them. Report only — never modify code.

## What to Check

### 1. Secrets and Credentials
- Hardcoded API keys, tokens, passwords
- .env files committed to version control
- Credentials in config files

### 2. Input Validation
- User inputs not being sanitized
- SQL injection vulnerabilities
- XSS vulnerabilities in frontend code

### 3. Authentication and Authorization
- Missing auth checks on routes/endpoints
- Insecure token storage
- Overly permissive CORS settings

### 4. Dependencies
- Known vulnerable packages (check package.json/requirements.txt)
- Outdated dependencies with security patches available

## Output Format
For each finding, provide:
1. **Severity:** Critical / High / Medium / Low
2. **File:** The exact file path
3. **Line:** The specific line number(s)
4. **Issue:** What's wrong
5. **Recommendation:** How to fix it

Sort findings by severity — Critical first.

If no issues are found, explicitly state "No security issues detected" with a brief summary of what was reviewed.
```

[SHOW: Full file visible in editor]

Save it. The agent is ready.

---

### SECTION 4: USING CUSTOM SUB-AGENTS (8:45 - 11:00) ~2.25 min

Let's run it. There are two ways to use a custom agent.

First — you can ask Claude to use it directly.

[SHOW: Claude Code prompt]

> Run the security-reviewer agent on my src/ folder

[SHOW: Claude spawning the security-reviewer sub-agent, scanning files, producing a report]

Look at this. The sub-agent is scanning through my files. It's checking for hardcoded secrets. Looking at input validation. Checking dependencies.

[NOTE: Let the output flow. Don't rush. Give viewers time to see the agent working.]

And here's the report. Sorted by severity. File paths. Line numbers. Specific recommendations.

[SHOW: The formatted security report output]

This is incredible. A full security audit from one sentence.

The second way — Claude might use your custom agent automatically. If you ask Claude to "make sure this code is secure," it might notice the security-reviewer agent in your .claude/agents/ folder and spin it up on its own.

Let me show you another practical example. Let's create a quick research agent.

[SHOW: Creating research-agent.md in .claude/agents/]

```yaml
---
name: research-agent
description: Researches topics using web search and documentation, returns structured summaries
tools:
  - WebSearch
  - WebFetch
  - Read
---
```

```markdown
# Research Agent

## Your Role
You are a research specialist. When given a topic, you search the web, find authoritative sources, and compile a structured summary.

## Process
1. Search for the topic using multiple queries
2. Read the top 3-5 relevant sources
3. Compile findings into a structured summary

## Output Format
- **Summary** (2-3 sentences)
- **Key Findings** (bullet points)
- **Sources** (linked)
- **Recommended Next Steps**
```

Now I can say:

> Research the latest changes in React Server Components and summarize what I need to know

[SHOW: Claude spawning the research agent, web searches happening, results coming back]

The research agent goes out, searches the web, reads multiple sources, and comes back with a clean summary. My main context stays clean. The research details live in the sub-agent's context.

---

### SECTION 5: TIPS AND BEST PRACTICES (11:00 - 11:45) ~45 sec

A few quick tips for working with sub-agents.

[SHOW: Tips list on screen]

**One — Limit their tools.** Don't give a research agent Write access. Don't give a reviewer agent Bash access. Least privilege.

**Two — Be specific in descriptions.** The description field is how Claude decides which agent to use. Vague descriptions mean Claude won't know when to reach for it.

**Three — Start with one.** Build one custom agent. Use it for a week. Refine it. Then build your second.

**Four — Check the output.** Sub-agents are powerful but not perfect. Always review what they produce, especially for security-sensitive work.

---

### OUTRO (11:45 - 12:00) ~15 sec

Sub-agents turn Claude Code from a single assistant into a whole team. Each specialist focused. Each one doing its best work.

Next episode is the finale — hooks and automation. We're going to wire everything together. Subscribe and I'll see you there.

[SHOW: End screen with subscribe button and next episode preview]

[NOTE: End screen — 20 seconds]
