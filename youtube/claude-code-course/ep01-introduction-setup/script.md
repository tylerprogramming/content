# Episode 1 — Full Script
## Claude Code Tutorial #1 - Install & Build Your First App
**Target length:** 10 minutes

---

## HOOK (0:00 - 0:30) ~30 seconds

Most people use AI wrong. They open ChatGPT, type a question, copy the answer, paste it somewhere else. That's not building. That's Googling with extra steps.

Claude Code is different. You type what you want. It builds it. Real files, real code, a real app — right on your computer.

In the next 10 minutes, I'm going to install Claude Code from scratch. And then we're going to build a full landing page together. Live. No editing. Let's go.

[SHOW: Terminal open, blank screen]

---

## SECTION 1: What Is Claude Code? (0:30 - 2:00) ~90 seconds

So what is Claude Code, actually?

You've probably used ChatGPT before. Or maybe Claude in the browser. You type a question, you get an answer. That's a chatbot. It talks.

[SHOW: Split screen — ChatGPT on left, Claude Code terminal on right]

Claude Code is not a chatbot. It's an agent. It doesn't just talk — it acts.

It can create files. Edit files. Run commands. Build entire projects. All from one prompt.

[SHOW: Highlight the terminal side]

Think of it like this. ChatGPT is like texting a smart friend. Claude Code is like hiring a developer who sits inside your computer and does what you ask.

And here's the thing — you don't need to know how to code to use it. You just need to know how to describe what you want. In plain English.

[NOTE: Pause briefly here. Let that land.]

That's what this course is about. Over the next few episodes, I'm going to teach you how to use Claude Code to build real things. Even if you've never written a line of code.

Let's start by installing it.

---

## SECTION 2: Installing Claude Code (2:00 - 4:30) ~2.5 minutes

Alright, first things first. You need two things.

**Number one: Node.js.**

[SHOW: Browser — google "install node.js", go to nodejs.org]

Go to nodejs.org. Download the LTS version. That stands for Long Term Support. It just means the stable one. Install it like any other app.

[SHOW: Download and install — speed this up in post if needed]
[NOTE: Can cut most of the install process. Just show the download click and then the "done" screen.]

To check if it worked, open your terminal.

On Mac, that's the app called Terminal. On Windows, use Command Prompt or PowerShell.

[SHOW: Open Terminal app]

Type this:

[SHOW: Type `node --version`]

```
node --version
```

If you see a version number, you're good. Don't worry about what the number is. Just needs to show something.

[SHOW: Output like `v20.11.0`]

**Number two: Claude Code itself.**

One command. That's it.

[SHOW: Type `npm install -g @anthropic-ai/claude-code`]

```
npm install -g @anthropic-ai/claude-code
```

This downloads and installs Claude Code globally on your machine. Takes about 30 seconds.

[SHOW: Installation output scrolling by]
[NOTE: Speed up the install output in post.]

Now you need an API key. This is how Claude knows it's you.

Go to console.anthropic.com. Create an account if you don't have one. Go to API Keys. Create a new key. Copy it.

[SHOW: Browser — console.anthropic.com > API Keys > Create Key]

[NOTE: Blur the actual key in post-production.]

Quick note on pricing. Claude Code uses the API, which means you pay per use. Not a monthly subscription. For most beginners, you'll spend maybe two to five dollars in a whole month. It's cheap.

Now let's fire it up.

---

## SECTION 3: Your First Launch (4:30 - 5:30) ~1 minute

In your terminal, just type:

[SHOW: Type `claude`]

```
claude
```

That's it. One word. Hit enter.

[SHOW: Claude Code boots up — the welcome screen appears]

First time, it'll ask for your API key. Paste it in. You only do this once.

And now you're in. See that cursor? That's where you talk to Claude.

[SHOW: Highlight the input area]

This is your workspace now. Everything happens here. You type what you want. Claude does it.

Before we build something, let me show you three things you need to know.

---

## SECTION 4: The Terminal Is Not Scary (5:30 - 6:30) ~1 minute

I know the terminal looks intimidating. Black screen. Blinking cursor. Feels like you're about to hack the Pentagon.

[SHOW: Terminal with blinking cursor]

Relax. You only need to know three things right now.

**One. Start Claude Code.** Type `claude` and hit enter. That's it.

[SHOW: Type `claude`, hit enter]

**Two. Stop Claude Code.** Press Escape, then type `/exit`. Or just close the window. Nothing will break. I promise.

[SHOW: Press Escape, type `/exit`]

**Three. Clear the conversation.** Type `/clear`. This starts a fresh conversation without closing Claude Code.

[SHOW: Type `/clear`]

That's it. Three things. Start. Stop. Clear. You're a terminal expert now.

[NOTE: Keep this light and funny. Smile.]

---

## SECTION 5: Your First Build — Live Demo (6:30 - 9:00) ~2.5 minutes

Alright. The moment of truth. Let's build something.

I'm going to create a new folder for our project first.

[SHOW: Type `mkdir beanbox && cd beanbox`]

```
mkdir beanbox && cd beanbox
```

Now I'll start Claude Code in this folder.

[SHOW: Type `claude`]

```
claude
```

And here's my prompt. I'm just going to describe what I want. Plain English.

[SHOW: Type the following prompt slowly enough to read]

```
Build me a landing page for a coffee subscription startup called BeanBox.
Include a hero section with a tagline, a "how it works" section with 3 steps,
a pricing section with 3 tiers, and a footer. Modern, clean design.
Use just HTML and CSS in a single file called index.html.
```

[NOTE: Let the audience read the prompt. Don't rush.]

And I hit enter.

[SHOW: Claude Code starts working — creating files, writing code]

Now watch. Claude is reading my prompt. It's thinking about what to build. And now it's writing the code.

See these approval prompts? Claude is asking permission to create files. I'll click "yes" — or you can hit "y" on your keyboard.

[SHOW: Approval prompts appearing, clicking yes]

It's creating index.html. Writing the HTML structure. Adding CSS styling. All from that one prompt.

[SHOW: Claude Code finishing up]

Done. Let's see what we got.

[SHOW: Open index.html in a browser]

[NOTE: This is the money shot. Make sure the page looks good. If it doesn't, do another take with a slightly different prompt.]

Look at that. A full landing page. Hero section. How it works. Pricing tiers. Footer. All from one prompt. Took about 90 seconds.

No code written by us. No templates. No Googling.

This is the power of Claude Code.

---

## SECTION 6: Quick Tour of the Interface (9:00 - 9:45) ~45 seconds

Before we wrap up, let me show you a few things about the interface you'll want to know.

[SHOW: Claude Code running]

First — this bar at the top. That's your context indicator. It shows how much of the conversation Claude is tracking. More on that in a future episode.

[SHOW: Point to/highlight the context bar]

Second — these approval prompts. Whenever Claude wants to create a file, edit a file, or run a command, it asks you first. You're always in control. Nothing happens without your permission.

[SHOW: Example approval prompt]

Third — you can just keep typing follow-up prompts. Want to change the color? Just say "make the hero section dark blue." Want to add a section? Say "add a testimonials section with 3 fake reviews." It just works.

[SHOW: Type a follow-up prompt like "Make the hero section background dark blue"]

---

## OUTRO (9:45 - 10:00) ~15 seconds

That's episode one. You installed Claude Code. You built your first project. And you learned the basics of the terminal.

Next episode, I'm going to show you how to write prompts that actually get good results. Because the quality of what Claude builds depends entirely on how you ask.

[SHOW: End screen with "Episode 2: Prompting Like a Pro" text overlay]

I'll see you there.

[NOTE: Add subscribe animation / end screen elements in post.]

---

## Total Runtime Estimate: ~10 minutes
| Section | Duration |
|---------|----------|
| Hook | 0:30 |
| What Is Claude Code? | 1:30 |
| Installing Claude Code | 2:30 |
| First Launch | 1:00 |
| Terminal Basics | 1:00 |
| Live Demo | 2:30 |
| Interface Tour | 0:45 |
| Outro | 0:15 |
| **Total** | **~10:00** |
