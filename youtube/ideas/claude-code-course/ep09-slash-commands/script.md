# Episode 9 — Build Your Own Commands
## Claude Code Tutorial #9 - Build Your Own Commands

**Target length:** 12 minutes
**Audience:** Non-technical founders, beginners
**Tone:** Conversational, practical, fast-paced

---

### INTRO (0:00 - 1:30) ~1.5 min

What if you could type one command and Claude does an entire workflow for you? Not a single task. An entire workflow. Like deploying your app. Running all your tests and fixing what's broken. Generating a report on your codebase.

[SHOW: Quick montage — /deploy running, /test running, /report generating output]

That's what custom commands do. You write it once, save it in a folder, and from that point on — one slash command and it runs.

Today I'm showing you every built-in slash command in Claude Code, plus how to build your own from scratch. By the end of this video, you'll have a custom command running in your project.

[NOTE: Title card — "Claude Code Tutorial #9 - Build Your Own Commands"]

Free course. Links in the description. Let's build.

---

### BUILT-IN SLASH COMMANDS (1:30 - 4:00) ~2.5 min

First, let's look at what's already built in. If you type /help in Claude Code, you see everything.

[SHOW: In Claude Code, type:]

```
/help
```

[SHOW: The help output — list of all slash commands]

There's a lot here. Let me walk you through the ones that matter most.

[SHOW: Highlight each command as you mention it]

**/clear** — This wipes your current conversation. Fresh start. Use it when Claude is confused or going in circles. We covered this earlier in the course but it's worth repeating. Fresh context, fresh results.

[SHOW: Type /clear — show the conversation reset]

**/compact** — This compresses your conversation to save memory. Claude has a context window — basically how much it can remember at once. When your conversation gets long, /compact summarizes it so Claude can keep going without forgetting the important stuff.

[SHOW: Type /compact — show the conversation being compressed]

[NOTE: Don't go deep on context windows. Just say "memory" and move on.]

**/model** — Switch which Claude model you're using. Maybe you want a faster model for simple tasks, or the most powerful one for complex stuff.

[SHOW: Type /model — show the model options]

**/init** — Creates a CLAUDE.md file in your project. That's the instruction file that tells Claude about your project. We covered this in episode 4.

[SHOW: Briefly show /init — don't dwell on it since it was covered before]

**/rewind** — We just covered this in episode 8. Go back to any checkpoint. Your undo button.

**/permissions** — Manage what Claude is allowed to do. Can it create files? Run commands? This is your safety control.

[SHOW: Type /permissions — show the permissions list]

Those are the big ones. There are others, but these are the ones you'll use every day.

---

### WHAT ARE CUSTOM COMMANDS? (4:00 - 5:00) ~1 min

Now for the fun part. Custom commands.

[SHOW: Terminal with Claude Code]

A custom command is a set of instructions you write in a markdown file. You put that file in a special folder. And then you can run it as a slash command in Claude Code.

It's like creating a recipe. You write down the steps once. Then anytime you need that recipe, you just type the name and Claude follows the steps.

Why would you want this? Because you probably do the same workflows over and over.

[SHOW: Text on screen — examples:]

- Deploy your app? Same steps every time.
- Run tests and fix failures? Same workflow.
- Generate a weekly report? Same format.

Instead of typing the same instructions every session, you save them once and run them with a slash.

---

### THE .claude/commands FOLDER (5:00 - 6:00) ~1 min

Here's where custom commands live.

[SHOW: Terminal — file explorer or ls command]

In your project, there's a `.claude` folder. Inside that, you create a folder called `commands`.

```
your-project/
  .claude/
    commands/
      deploy.md
      test.md
      report.md
```

[SHOW: Create the folder structure]

Each markdown file in that commands folder becomes a slash command. The filename is the command name.

So `deploy.md` becomes `/deploy`. `test.md` becomes `/test`. `report.md` becomes `/report`.

[SHOW: Point to each file and its corresponding command name]

That's it. That's the entire system. Markdown file in a folder. Filename becomes the command.

[NOTE: Emphasize how simple this is. No config files, no setup, just a markdown file.]

---

### DEMO: CREATING A CUSTOM COMMAND (6:00 - 9:30) ~3.5 min

Let me build one from scratch. Let's create a /deploy command.

[SHOW: Terminal in the project directory]

First, I need the folder. Let me create it.

[SHOW: In Claude Code, type:]

```
Create the .claude/commands/ folder for me
```

[SHOW: Claude creates the directory]

Now I need to create the command file. I'll ask Claude to help me write it.

[SHOW: Type:]

```
Create a custom slash command at .claude/commands/deploy.md that does the following:
1. Run the test suite
2. If tests pass, build the project
3. Show me a summary of what would be deployed
4. Ask me to confirm before deploying
```

[SHOW: Claude creates the deploy.md file]

Let me show you what it wrote.

[SHOW: Open .claude/commands/deploy.md — show the contents]

See? It's just markdown. Plain English instructions. Nothing complicated. It tells Claude what to do step by step.

The format is simple. You write instructions like you'd explain to a person. Claude reads them and follows them.

Now let me run it. I type:

[SHOW: In Claude Code, type:]

```
/deploy
```

[SHOW: Claude starts executing the deploy command — running tests, building, showing summary]

Look at that. It's running through every step. Tests first. Then the build. Now it's showing me a summary. And it's asking me to confirm.

[SHOW: The confirmation prompt from Claude]

I'll say yes.

[SHOW: Type "yes" or "go ahead" — Claude completes the deployment]

One command. Entire workflow. And I can run this every single time I want to deploy. /deploy. Done.

[NOTE: If the project doesn't have a real deployment setup, fake it. Have the command run through the steps and show what it would do. The audience cares about the concept, not the actual deployment.]

Let me make another one real quick. A /report command.

[SHOW: Type:]

```
Create a custom command at .claude/commands/report.md that analyzes the current project and generates a brief report: how many files, what languages are used, any TODO comments in the code, and a summary of recent git commits.
```

[SHOW: Claude creates report.md]

Now I run it.

[SHOW: Type:]

```
/report
```

[SHOW: Claude analyzes the project and outputs a report — file counts, languages, TODOs, recent commits]

Instant project report. Every time.

---

### PRACTICAL EXAMPLES (9:30 - 10:30) ~1 min

Let me give you a few more ideas for custom commands.

[SHOW: List on screen]

**/test** — Run all tests, show failures, suggest fixes. Great for catching bugs.

**/review** — Look at all uncommitted changes and review them like a code reviewer. Find potential issues.

**/document** — Generate or update documentation for the codebase. Keep your docs fresh.

**/standup** — Summarize what changed since yesterday. Perfect for daily standups.

**/optimize** — Analyze the codebase for performance issues and suggest improvements.

[SHOW: Terminal]

The pattern is always the same. Think about a workflow you do repeatedly. Write the steps in a markdown file. Save it in `.claude/commands/`. Run it with a slash.

[NOTE: Don't demo all of these. Just show the list and move on. The audience gets the idea from the deploy and report demos.]

---

### TIPS FOR GOOD COMMANDS (10:30 - 11:00) ~0.5 min

A couple tips for writing good commands.

Be specific. Don't say "test the app." Say "run npm test, show any failures, and suggest a fix for each one." The more specific your instructions, the better the result.

[SHOW: Side-by-side — vague command vs specific command]

Break it into steps. Numbered steps work great. Claude follows them in order.

Include what to do when things go wrong. "If the tests fail, stop and show me the errors." That way your command handles edge cases.

---

### RECAP & NEXT EPISODE (11:00 - 12:00) ~1 min

Let's wrap up.

[SHOW: Bullet points appearing one at a time]

- Built-in commands: /help, /clear, /compact, /model, /init, /rewind, /permissions.
- Custom commands live in `.claude/commands/`.
- Each markdown file becomes a slash command.
- Write instructions in plain English. Claude follows them.
- Great for any workflow you do more than once.

[SHOW: Terminal with the /deploy command running one more time]

We've covered a ton of ground in this course so far. You know how to set up Claude Code, work with files, use git, configure your project, plan before you build, manage sessions, and now create custom commands.

Next episode, we're getting into some more advanced territory. Stay tuned.

If this course has been helpful, hit subscribe. I'll see you in the next one.

[NOTE: End card with subscribe button, playlist link]
