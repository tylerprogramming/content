# Script — 10 Claude Code Concepts I Wish I Knew From the Start

**Target length:** 12–15 minutes
**Format:** Talking head + live demos (real setup)
**Audience:** Founders/entrepreneurs, beginner–intermediate Claude Code users

---

## [0:00 – 0:35] Hook

[SHOW: Talking head, direct to camera]

I've been using Claude Code every single day for months.

And if I'm being honest — the first few weeks I was doing it completely wrong.

No CLAUDE.md. Vague prompts. Two-hour sessions wondering why Claude kept forgetting what I'd told it an hour ago.

These are the 10 concepts that actually fixed it.

And I'm not going to just explain them. I'm going to show you my real setup — the same Claude Code configuration I use to run my entire YouTube channel.

Let's go.

[NOTE: Keep this tight — under 35 seconds. Energy up.]

---

## [0:35 – 1:00] Quick Framing

[SHOW: Talking head]

Quick thing before we start. These aren't 10 random tips.

They're the 10 foundational concepts — the ones where understanding even one of them changes how everything else works.

And I picked 10 because Simon Scrapes did 27 and honestly, 10 is enough to start building like a pro.

[NOTE: Optional — cut this if it feels like filler. Jump straight into concept 1.]

---

## [1:00 – 2:30] Concept 1: CLAUDE.md

[SHOW: Terminal → open ~/CLAUDE.md in editor]

**The single most important file in Claude Code.**

Every time you open Claude Code, the first thing it does is read a file called CLAUDE.md.

Think of it as your instruction manual for Claude. Every session, before it does anything else, it reads this file.

[SHOW: Tyler's actual CLAUDE.md — scroll through it slowly]

This is mine. I've got my preferences, my workflow, my rules for how I want things done.

The magic? I wrote it once. And now every Claude session starts with Claude already knowing how I work.

Without it — Claude is guessing. Every. Single. Time.

Day one task: create a CLAUDE.md. Ask Claude to help you write it. It'll ask you questions and build it for you.

[SHOW: Demo — type: "Help me create a CLAUDE.md for my project. Ask me questions about my preferences and workflow."]

---

## [2:30 – 3:45] Concept 2: Context Window (and Context Rot)

[SHOW: Talking head → diagram/animation of context filling up]

Claude Code has a memory limit. It's called the context window.

Everything in your session — every message, every file Claude reads, every response — lives in that window. When it fills up, Claude starts forgetting the stuff from earlier.

This is called context rot. And it explains why your sessions feel sharp for 20 minutes and then Claude starts going weird.

[SHOW: Green bar at bottom of Claude Code terminal]

See that green bar at the bottom? That's your context meter. Watch it.

Two ways to handle it before it becomes a problem:

[SHOW: Type /compact in terminal]

`/compact` — this summarizes the conversation and clears out the noise. You can even tell it what to keep: `/compact keep the API structure decisions`

[SHOW: New session starting]

Or just start a fresh session when you switch tasks. Don't try to do everything in one conversation.

[NOTE: This concept is the #1 thing people don't know and explains 80% of "Claude is getting worse" complaints.]

---

## [3:45 – 5:00] Concept 3: Permissions

[SHOW: settings.json file in editor]

Claude Code can create files, run commands, even delete things on your computer.

By default it asks permission before every action. That's safe — but it kills your flow when you're 45 minutes into a build.

The fix: pre-approve the safe stuff.

[SHOW: Tyler's settings.json with allowlist]

Here's my permissions setup. I've pre-approved reading files, running tests, Git operations, starting the dev server.

Everything else — installing packages, deleting files, touching the internet — Claude still asks me first.

[SHOW: Demo — type: "Add safe permissions to my settings.json: reading files, running tests, Git operations. Show me what you're adding before saving."]

Claude will write the config for you. You just review it.

Result: Claude works 3x faster, and you're still in control of anything risky.

---

## [5:00 – 6:15] Concept 4: Slash Commands

[SHOW: Type /help in Claude Code terminal]

These are your shortcuts. Type a forward slash and you get a menu of built-in commands.

The ones I use constantly:

`/clear` — wipe the conversation, fresh start
`/compact` — summarize and compress (we just covered this)
`/model` — switch between Haiku, Sonnet, Opus mid-session
`/cost` — see exactly what you've spent in tokens this session

[SHOW: /model command switching models]

But here's the part most people miss: **you can create your own slash commands.**

Any task you do repeatedly — put it in the `.claude/commands/` folder as a markdown file. Now it's a slash command.

[SHOW: Tyler's custom commands folder]

I have custom commands for my whole YouTube workflow. One command plans a video. Another runs my SEO analysis. It's saved me hours every week.

---

## [6:15 – 7:45] Concept 5: Skills

[SHOW: ~/.claude/skills/ folder structure]

Skills are the upgrade from slash commands.

A skill is a markdown file that teaches Claude how to do a specific task really well. When you invoke it, Claude reads the whole instruction set before it acts.

Think of it this way: a slash command says "do this." A skill says "here's exactly how to do this, step by step, with all my preferences and rules baked in."

[SHOW: Open one of Tyler's real skill files — e.g., /yt skill]

This is one of mine. It's the skill that plans my YouTube videos. It tells Claude to do web research, analyze the transcript structure, ask me specific questions, then generate a full script package.

[SHOW: Invoking the skill — /yt]

Without this skill, I'd be writing a 500-word prompt every time I want to plan a video. Now I just type `/yt` and it handles everything.

I have 20 of these skills. Each one encodes a specific workflow. Claude reads it, follows it exactly.

This is where Claude Code stops being a chatbot and starts being a system.

---

## [7:45 – 8:45] Concept 6: Hooks

[SHOW: settings.json hooks section]

Hooks are automation that runs without using any AI tokens.

They're scripts that trigger at specific moments — before Claude saves a file, after a tool call, when the session ends.

[SHOW: Example hook — linter running automatically after file edit]

Example: every time Claude edits a file, my linter runs automatically. I never have to ask. It just happens.

Or: a hook that logs every command Claude runs, so I can audit exactly what happened.

The key difference from skills: hooks don't use Claude's intelligence. They're deterministic. They always run. They never hallucinate.

Use hooks for the stuff you always want to happen — formatting, logging, validation. Let Claude handle the thinking. Hooks handle the guardrails.

---

## [8:45 – 9:45] Concept 7: MCP Servers

[SHOW: MCP configuration / connected tools]

By default, Claude Code works with files on your computer. That's it.

MCP — Model Context Protocol — is how you connect Claude to everything else.

[SHOW: List of Tyler's connected MCP servers]

I've got Claude connected to Telegram, Blotato for social media, Gmail, web search. So when Claude is planning content, it can actually look things up, pull data, and schedule posts — all from one conversation.

Setting it up is simpler than it sounds. You add a JSON config, restart Claude Code, and the new tools appear.

[SHOW: One MCP tool being invoked naturally in a Claude session]

No code. Just config.

Think of skills as teaching Claude *how* to do things. MCP is giving Claude *access* to things.

You need both.

---

## [9:45 – 10:45] Concept 8: Sub-agents

[SHOW: Claude Code terminal showing a sub-agent being spun up]

This one changes how you think about what's possible.

Sub-agents are separate Claude instances that your main Claude can spin up to handle specific tasks.

Each one gets its own context window — clean slate, no context rot from the main session.

[SHOW: Example — main Claude handing off a research task to sub-agent]

So instead of one Claude doing everything and slowly degrading, you have specialists.

Main Claude planning the strategy. Sub-agent doing the research. Another sub-agent writing the code.

And here's the thing — Claude decides to spin them up on its own when the task warrants it. You don't always have to ask.

When to use them intentionally: any task that's fully self-contained. "Go analyze this dataset and come back with findings." That's a sub-agent task.

---

## [10:45 – 11:45] Concept 9: Git + Worktrees

[SHOW: Git branch diagram → multiple terminal panes]

Always work in a Git branch when using Claude Code. This is non-negotiable.

Claude makes fast changes. Sometimes it goes down the wrong path. Git is your undo button for everything.

[SHOW: Claude Code creating a commit automatically]

Claude actually handles Git commits for you. After every significant change it'll commit with a message explaining what it did.

But the advanced version of this is worktrees.

[SHOW: Three terminal panes with three different Claude sessions]

Worktrees let you run multiple Claude instances on completely separate branches — same repo, no interference.

`claude --worktree feature-auth` — Claude works on auth in isolation.
`claude --worktree bugfix-login` — different Claude, different branch, same codebase.

When each finishes, you merge the branches. Total isolation, parallel development.

I use this to have Claude running multiple tasks simultaneously while I film.

---

## [11:45 – 12:45] Concept 10: Memory (Auto + Manual)

[SHOW: ~/.claude/memory/ folder]

Last one. And it's the one that makes Claude feel like it actually knows you.

Claude Code has two types of memory beyond CLAUDE.md.

[SHOW: Memory folder with individual memory files]

**Auto memory** — as you work, Claude notices your preferences and stores them. Language you use, tools you prefer, project conventions. It builds a profile of how you work.

**Manual memory** — you can tell Claude to remember specific things. "Remember I always want TypeScript. Remember my API structure uses REST not GraphQL."

[SHOW: Tyler's actual memory files]

Here's mine. I've got notes about my brand voice, my typical video structure, my publishing schedule. Things I'd otherwise have to re-explain in every new session.

The result: every Claude session starts with Claude already knowing you. Not guessing. Knowing.

That's the difference between a tool and a collaborator.

---

## [12:45 – 13:30] Wrap-up + CTA

[SHOW: Talking head]

That's the 10.

CLAUDE.md, context window, permissions, slash commands, skills, hooks, MCP servers, sub-agents, Git + worktrees, memory.

Learn these 10 and Claude Code stops being overwhelming. It becomes a system.

And if you want to see how all of these come together in a real workflow — I've got a full video on building a Claude Code skill from scratch. That's the one that takes everything we covered today and turns it into something you can actually use.

Link's in the description.

If this clicked for you, subscribe — I post new Claude Code tutorials every week.

[SHOW: Subscribe animation / end screen]

[NOTE: Keep CTA tight — 30–45 seconds max. Don't over-explain the next video.]
