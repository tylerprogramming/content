# Script: 23 Claude Code Concepts Every Beginner Needs to Know

---

## [0:00 - 0:30] Hook

I watched every Claude Code tutorial on YouTube and they all have the same problem — they explain concepts but never actually show you. So in the next 15 minutes, I'm going to walk you through 23 Claude Code concepts, and for every single one, I'll open my terminal and demo it live. No slides. No theory. Just Claude Code running on screen. Let's go.

[SHOW: Quick montage of Claude Code running, text flying across terminal]

---

## [0:30 - 1:15] Concept 1: What is Claude Code

You know ChatGPT, Claude, Gemini — you type, they talk back. That's it. They can't touch your computer. Claude Code is different. It can create files, build websites, install packages, run commands — all from a conversation in plain English. You describe what you want, it builds it. Chatbots give advice. Claude Code takes action.

[SHOW: Split screen — ChatGPT on left giving a text response, Claude Code on right actually creating a file]
[NOTE: Keep this quick. The point lands fast.]

---

## [1:15 - 2:00] Concept 2: The Terminal

Claude Code runs in the terminal. That black screen with white text that looks intimidating. But here's the secret — when you're using Claude Code, you barely need to know any terminal commands. You type in plain English. Claude handles the rest. You just need three things: how to open it — type `claude`. How to close it — Control C twice. And how to clear it — `/clear`. That's it.

[SHOW: Open a terminal, type `claude`, show it launching. Then show Control+C to exit. Then reopen and type `/clear`.]

---

## [2:00 - 3:00] Concept 3: Prompting

A prompt is what you type to tell Claude Code what to do. Same as typing into ChatGPT. Plain English, no special syntax. But specificity matters. "Build me a website" gets you something generic. "Build me a one-page landing page for a consulting business with a green color scheme, a contact form, and three service cards" — that gets you something usable. Better prompts, better results. That's the whole game.

[SHOW: Type a vague prompt, show mediocre result. Then type the specific prompt, show the better result. Side by side if possible.]
[NOTE: Have the specific prompt pre-written so you can paste it in. Don't waste time typing live.]

---

## [3:00 - 4:00] Concept 4: Permissions

Claude Code can make real changes to your computer — create files, run commands, even delete stuff. So by default, it asks permission before doing anything significant. You'll see these approval prompts constantly at first. That's good — it keeps you safe. But as you get comfortable, you can pre-approve safe actions like reading files, running your dev server, and running tests. Type `/permissions` and add them to your allow list. You keep control, Claude works faster.

[SHOW: Show an approval prompt appearing. Then show typing `/permissions` and adding a safe action. Show Claude working faster without stopping.]

---

## [4:00 - 5:00] Concept 5: Tool Use

What makes Claude Code powerful is it has built-in tools that let it interact with your computer. The main ones: Read — it can look at your files. Write — it can create new files. Bash — it can run terminal commands. You don't tell Claude which tool to use. You just describe what you want, and Claude picks the right tool automatically. You'll see it in the output — it'll say "Read file," "Write file," "Bash command" as it works.

[SHOW: Give Claude a task. Highlight in the output where it says "Read," "Write," "Bash" as it uses different tools.]

---

## [5:00 - 6:15] Concept 6: Context Window

This is the most important concept and the one most people get wrong. The context window is Claude's short-term memory. Every message you send, every file it reads, every response — it all piles up in the context window. And it has a limit. When it fills up, Claude starts losing track of what you told it earlier. Outputs get worse. It forgets instructions. This is called context rot. You can see how full your context is by the bar at the bottom of the terminal. Keep it clean. Start fresh sessions for new tasks. We'll cover how to manage it in a few concepts.

[SHOW: Point out the context usage bar at the bottom of the terminal. Show it growing as you chat. Then show what happens when it's nearly full — Claude gives a worse response.]
[NOTE: This is the most important concept. Give it a beat. Let it land.]

---

## [6:15 - 7:15] Concept 7: CLAUDE.md

This is probably the most important file you'll ever create. CLAUDE.md is a markdown file that lives in your project folder. You write your preferences, your rules, how you want things done. And Claude reads it first, every single time you start a session. It's your instruction manual. Things like "always use TypeScript," "use this brand voice," "never use em dashes." You write it once and Claude follows it forever. If you're not using a CLAUDE.md file, you're making Claude guess — and guessing leads to bad results.

[SHOW: Open a CLAUDE.md file in the editor. Show a few rules. Then start a Claude Code session and show it reading the file at the top. Give a task and show it following a rule from the file.]

---

## [7:15 - 8:00] Concept 8: Memory

CLAUDE.md is your manual instruction file. But Claude Code also has automatic memory. As you work, it learns your preferences and stores them across sessions. If you always use JavaScript, or prefer a certain style, Claude remembers that the next time you start a new session. You can also tell it explicitly — "remember that I always want tests written in Jest." And you can ask it what it remembers about you. It's all about getting more personalized over time.

[SHOW: Tell Claude "remember that I prefer using bun instead of npm." Then start a new session and ask it to install a package — show it using bun.]

---

## [8:00 - 8:45] Concept 9: Models

When people say "Claude Code," there's actually a family of AI models underneath. The three main ones: Haiku is the fastest and cheapest — great for simple tasks. Sonnet is the all-rounder — good at most things, reasonably priced. Opus is the most intelligent — handles complex problems but costs more. You can switch mid-conversation by typing `/model`. Match the model to the task. Sonnet for most things. Opus when it matters.

[SHOW: Type `/model` and show the model selector. Switch between models. Show the different models in action on the same task if time allows.]

---

## [8:45 - 9:30] Concept 10: /init

This one gets overlooked but it's the fastest way to start any project. When you open Claude Code in a new folder, type `/init`. Claude will scan your project, understand the structure, and generate a CLAUDE.md file for you automatically. It figures out what language you're using, what framework, what tools — and writes sensible defaults. You can edit it after, but it gives you a massive head start instead of writing your CLAUDE.md from scratch.

[SHOW: Create a new folder. Open Claude Code. Type `/init`. Show it generating the CLAUDE.md file. Open the file and show what it created.]

---

## [9:30 - 10:15] Concept 11: Plan Mode

Before Claude starts building, sometimes you want it to think first. Plan Mode lets Claude explore your codebase, read files, and answer questions — without making any changes. Hit Control+G to toggle it on. Now Claude is in read-only mode. It can look at everything, plan the approach, and tell you what it would do. When you're happy with the plan, hit Control+G again to switch back, and it'll execute. Think first, build second.

[SHOW: Hit Ctrl+G. Show "Plan Mode" indicator. Ask Claude to plan a feature. Show it reading files and proposing steps without editing anything. Then Ctrl+G back and let it build.]

---

## [10:15 - 11:00] Concept 12: Compact & /clear

Remember context rot? Here's how you fight it. Two commands. `/clear` wipes the entire conversation and gives you a fresh start. Use this when you're switching to a totally different task. `/compact` is smarter — it summarizes the key information from your conversation, clears the noise, and keeps going with a clean context. You can even tell it what to keep: `/compact focus on the API changes`. Claude also does this automatically when it detects the context getting full — around 85 to 95 percent.

[SHOW: Show a long conversation. Type `/compact focus on the database schema`. Show the context bar shrinking. Then show `/clear` for a full reset.]

---

## [11:00 - 11:45] Concept 13: Session History

Every Claude Code session is automatically saved. When you close your terminal and come back later, you don't have to start over. Type `claude --resume` and you'll see a list of all your previous sessions. Pick the one you want and jump right back in with full context. For even faster access, `claude --continue` drops you straight into your most recent session. You're rarely finishing a big project in one sitting — session history means you never lose progress.

[SHOW: Close Claude Code. Reopen terminal. Type `claude --resume`. Show the session list. Pick one and show it resuming with context.]

---

## [11:45 - 12:30] Concept 14: Checkpoints & /rewind

Claude works fast and sometimes it goes down the wrong path. That's fine because Claude Code automatically creates checkpoints — snapshots of your code before every edit. You don't need to enable this. It just happens. When something goes wrong, type `/rewind`. You'll see a list of every prompt from your session, and you can go back to any point. Pick the moment before things broke, and you're back. It's like an undo button for your entire project.

[SHOW: Make a few changes with Claude. Then type `/rewind`. Show the checkpoint list. Select one and show the code reverting.]

---

## [12:30 - 13:15] Concept 15: @ File References

Instead of telling Claude to "go find that config file," you can point it directly. Type @ and then the file path. Claude will read that file and use it as context for your request. So you can say "look at @src/config.ts and add a new database connection." Claude reads the file instantly without searching. You can reference multiple files too. It's faster and more precise than describing where things are.

[SHOW: Type a prompt with @src/config.ts or similar. Show Claude reading the file immediately and using it in context.]

---

## [13:15 - 14:00] Concept 16: Screenshots & Images

Sometimes it's easier to show Claude what's wrong than describe it. You can paste screenshots directly into Claude Code. Got a bug on your website? Screenshot it, paste it in. Claude sees the image, understands what's wrong, and fixes it. You can also paste in a design you like and ask Claude to build something similar. It won't be pixel-perfect, but it gets you 60 to 70 percent there on the first shot — way faster than describing every detail in text.

[SHOW: Take a screenshot of a webpage with a visible bug. Paste it into Claude Code. Show Claude identifying the issue and fixing it.]

---

## [14:00 - 14:45] Concept 17: Slash Commands

Throughout this video we've been using slash commands — `/clear`, `/compact`, `/model`, `/init`, `/rewind`. These are shortcuts for common actions. Type `/help` to see every slash command available. And here's the powerful part — you can create your own custom slash commands. Put a markdown file in `.claude/commands/` and it becomes a slash command you can run anytime. So if you have a workflow you repeat — like deploying, or generating reports — make it a slash command.

[SHOW: Type `/help` and show the full list. Then show a custom command file in .claude/commands/. Run it with /command-name.]

---

## [14:45 - 16:00] Concept 18: Skills

Skills take slash commands to the next level. A skill is a set of specialized instructions that teach Claude how to do a specific task really well. Instead of a simple shortcut, a skill can have detailed instructions, templates, best practices — everything Claude needs to be an expert at that one thing. They live in `.claude/skills/` and Claude can auto-detect when to use them based on what you ask. Let me show you one of mine.

[SHOW: Open .claude/skills/ and show one of your skills (like the /fitness or /thumbnail skill). Show the SKILL.md file. Then trigger it and show Claude following the specialized instructions to produce a high-quality result.]
[NOTE: This is the custom skill demo moment. Pick whichever skill is most visually interesting — /thumbnail is great because it produces something visible.]

---

## [16:00 - 17:00] Concept 19: MCP Servers

By default, Claude Code works with files on your computer. But your work lives across tons of tools — GitHub, Notion, Slack, databases. MCP stands for Model Context Protocol, and MCP servers connect Claude Code to those external tools. Once connected, Claude can pull data from them, push updates, and interact with your whole tech stack from one terminal window. It's what makes Claude Code more than just a coding tool — it becomes a control center for everything.

[SHOW: Show an MCP server already configured (like GitHub). Run a command that interacts with it — like "show me my open pull requests" or "create a new issue." Show Claude pulling real data from the external service.]

---

## [17:00 - 18:00] Concept 20: Sub-agents

As your tasks get more complex, one Claude session can get overwhelmed. That's where sub-agents come in. Claude can spin up separate instances — each with their own clean context window — to handle specific tasks. One sub-agent researches, another reviews code, another writes tests. They work independently and report back to the main session. The key benefit: your main context stays clean. The sub-agents do the heavy lifting in their own space and just send back the results.

[SHOW: Give Claude a complex task. Watch it decide to spin up a sub-agent. Show the sub-agent working in the background. Show the result coming back to the main session.]

---

## [18:00 - 19:00] Concept 21: Hooks

Hooks are custom scripts that run automatically at specific moments — like every time Claude saves a file, or every time it runs a command. The key difference from everything else: hooks don't use AI tokens. They're just regular scripts that fire on events. So you can auto-format your code every time Claude edits a file. Or log every command Claude runs. Or block Claude from touching certain folders. Set them up once and they run in the background forever, keeping everything clean without costing you anything.

[SHOW: Show a hook in .claude/settings.json or via /hooks. Demonstrate it firing — like auto-formatting a file after Claude edits it. Show the hook running in the background.]

---

## [19:00 - 19:45] Concept 22: Custom Agents

Sub-agents are great, but you can also build your own custom agents. Drop a markdown file in `.claude/agents/` and you've got a specialist. You define what model it uses, what tools it has access to, and what its job is. So you could make a "code reviewer" agent that only has read access and uses Sonnet to save money. Or a "security auditor" that scans for vulnerabilities. You run them by saying "use the code-reviewer agent" and they do their thing in their own context, then report back. It's like hiring a specialist for a specific job.

[SHOW: Show a custom agent file in .claude/agents/ — open the markdown, show the YAML frontmatter with model, tools, and instructions. Then trigger it: "use the code-reviewer agent to review this file." Show it working and returning results.]
[NOTE: Keep it brief — the sub-agents concept already introduced the idea. This is just "now you can build your own."]

---

## [19:45 - 20:45] Concept 23: Remote Control

Last one, and it might be my favorite. You know how when Claude is working on a big task, it hits permission prompts and just... waits? If you're not at your desk, the agent is blocked. Remote Control fixes that. Type `/rc` and you get a QR code. Scan it with the Claude app on your phone. Now your phone is a window into your terminal session. You can see what Claude's doing, approve changes, send messages — all from your couch, your car, wherever. Your code stays on your laptop. Your phone is just the remote control. It's the difference between babysitting the terminal and actually letting Claude be an agent.

[SHOW: Type `/rc` in terminal. Show the QR code. Scan with phone. Show the session on the phone. Approve a change from the phone. Show the terminal reflecting the activity.]
[NOTE: This is a great closer — visual, impressive, and leaves a strong final impression before the CTA.]

---

## [20:45 - 21:30] Recap & CTA

That's all 23 concepts. From the basics — what Claude Code is, how the terminal works, how to prompt — all the way up to skills, MCP servers, sub-agents, and hooks. If you're just getting started, focus on the first ten. Get comfortable with CLAUDE.md, Plan Mode, and managing your context window. Those three alone will transform how you use Claude Code. Bookmark this video and come back when you hit a concept you need a refresher on. If this was helpful, smash that like button and subscribe — I put out Claude Code content every week. See you in the next one.

[SHOW: Quick visual recap — flash each concept name on screen as you list them]
[NOTE: Energy up for the close. Keep it punchy.]
