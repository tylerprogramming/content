# Claude Code Tutorial #10 - Skills: Build Custom AI Workflows in Minutes

## Full Script

---

### INTRO (0:00 - 1:30) ~1.5 min

What if Claude could do your entire job — not just answer questions, but actually execute complex workflows perfectly every single time?

That's what Skills do. And in this video, I'm going to show you how to build one from scratch.

[SHOW: Terminal with Claude Code open, quick montage of skills being invoked]

Then I'll show you some of my personal custom skills. Like one that generates YouTube thumbnails. Another that transcribes entire videos. And one that tracks my fitness in a GitHub-style contribution grid.

[SHOW: Quick flash of each skill's output — thumbnail image, transcript file, fitness grid]

By the end of this video, you'll have your own custom skill running. Let's get into it.

[NOTE: Title card — "Claude Code Tutorial #10 - Skills"]

---

### SECTION 1: WHAT ARE SKILLS? (1:30 - 3:30) ~2 min

So what exactly is a skill?

Think of it this way. You know how we set up slash commands in an earlier episode? Those were like shortcuts. You type a command, Claude follows a template.

[SHOW: Quick reminder — typing /plan in terminal]

Skills are the next level up. A skill is a specialized instruction file that gives Claude deep domain knowledge about a specific task.

Here's the key difference. Commands are templates you invoke manually. Skills are expertise that Claude can tap into automatically.

[SHOW: Side-by-side comparison on screen]
```
COMMANDS                    SKILLS
- Manual invocation         - Auto or manual invocation
- Single prompt template    - Multi-file, deep knowledge
- Simple fill-in-blanks     - Domain expertise
- You trigger them          - Claude can trigger them
```

Let me give you a real example. I have a skill called "post." When I say "post this to Twitter," Claude doesn't need me to type slash-post. It recognizes what I'm asking, finds the right skill, and executes it.

[SHOW: Typing "post this tweet: Just shipped a new Claude Code tutorial" and Claude auto-invoking the post skill]

That's auto-invocation. Claude reads your request, matches it to a skill, and uses it. No slash command needed.

---

### SECTION 2: THE SKILLS FOLDER AND SKILL.MD FORMAT (3:30 - 5:30) ~2 min

Let's look at how skills actually work under the hood.

Skills live in a folder called `.claude/skills/` in your home directory.

[SHOW: Terminal]
```
ls ~/.claude/skills/
```

[SHOW: List of skill files appearing]

Each skill is a markdown file. Let me open one up so you can see the structure.

[SHOW: Opening a SKILL.md file in the editor]

Every skill file has two parts. First, YAML frontmatter at the top. This is the metadata — it tells Claude what the skill is and when to use it.

```yaml
---
name: social-media-post
description: Creates and publishes social media posts to connected platforms
triggers:
  - "post to"
  - "share on"
  - "tweet this"
disable-model-invocation: false
---
```

The `name` is how the skill identifies itself. The `description` tells Claude what it does. The `triggers` are phrases that help Claude know when to use this skill.

And this one is important — `disable-model-invocation`. When this is false, Claude can auto-invoke the skill. When it's true, the skill only runs when you explicitly call it with the Skill tool. You'd set it to true for anything destructive — like a skill that deploys code or deletes files.

Below the frontmatter is the actual instruction content. This is where you write everything Claude needs to know to execute the skill perfectly.

[SHOW: Scrolling through the instruction content of the skill file]

You can include step-by-step workflows. You can include examples. You can reference other tools. This is Claude's playbook.

---

### SECTION 3: BUILD A SKILL LIVE (5:30 - 10:30) ~5 min

Alright, let's build one together. We're going to create a social media post writer skill from scratch.

[SHOW: Terminal, clean screen]

First, let's make sure the skills folder exists.

```
mkdir -p ~/.claude/skills
```

[SHOW: Command executing]

Now let's create our skill file.

[SHOW: Opening a new file in the editor]

```
touch ~/.claude/skills/social-post-writer.md
```

Let me write the frontmatter first.

[SHOW: Typing in editor]

```yaml
---
name: social-post-writer
description: Writes engaging social media posts for Twitter, LinkedIn, and Threads based on a topic or content
triggers:
  - "write a post"
  - "social media post"
  - "draft a tweet"
disable-model-invocation: false
---
```

[NOTE: Type this out in real time — don't paste. Let viewers see the process.]

Now for the instructions. This is the fun part. Think of this as writing a brief for an expert copywriter.

[SHOW: Typing instructions]

```markdown
# Social Media Post Writer

## Role
You are an expert social media copywriter who creates platform-optimized posts.

## Workflow
1. Ask the user for the topic or content to write about
2. Ask which platform(s): Twitter, LinkedIn, or Threads
3. Generate 3 options for each platform
4. Each option should have a different angle (educational, personal story, hot take)

## Platform Guidelines

### Twitter (max 280 chars)
- Lead with a hook or bold statement
- Use line breaks for readability
- End with engagement driver (question or CTA)
- No hashtags unless specifically requested

### LinkedIn (max 3000 chars)
- Open with a pattern-interrupt first line
- Use short paragraphs (1-2 sentences each)
- Include a personal angle or lesson learned
- End with a question to drive comments

### Threads (max 500 chars)
- Conversational and authentic tone
- Can be slightly longer form than Twitter
- Works well with hot takes and opinions

## Output Format
For each option, provide:
- The post text (ready to copy-paste)
- Character count
- Why this angle works

## Rules
- Never use cringe phrases like "game-changer" or "let that sink in"
- Avoid generic motivational content
- Write like a real person, not a marketing bot
- Match the user's voice if they provide examples
```

[SHOW: Full file visible in editor]

That's it. Save the file. Skill is live.

[NOTE: Pause for emphasis here]

Now let's test it. Let me open Claude Code.

[SHOW: Terminal with Claude Code]

```
claude
```

I'll just ask naturally.

[SHOW: Typing prompt]

> Write me a social media post about how I use Claude Code skills to automate my YouTube workflow

[SHOW: Claude recognizing the skill, generating 3 options for each platform]

Look at that. Claude found the skill automatically. It's following our format — three options per platform, different angles, character counts, explanations.

[NOTE: React genuinely to the output. Point out specific lines that are good.]

And I didn't type any slash command. Claude just knew. That's the power of auto-invocation.

---

### SECTION 4: REAL SKILLS IN ACTION (10:30 - 13:30) ~3 min

Now let me show you something that'll blow your mind. These are skills I actually use every day.

[SHOW: Terminal]

```
ls ~/.claude/skills/
```

[SHOW: List of 12+ skill files]

I have twelve custom skills. Let me show you one of my favorites — the thumbnail generator.

[SHOW: Invoking the thumbnail skill]

> Create a YouTube thumbnail for a video about Claude Code skills

[SHOW: Claude invoking the skill, calling the Kie.ai API, generating a thumbnail]

[NOTE: Show the actual thumbnail output. Let it breathe on screen for 3-4 seconds.]

That just happened. Claude wrote the prompt, called the API, downloaded the image, and saved it to my thumbnails folder. One sentence from me.

Let me show you another one. My transcribe skill.

[SHOW: Invoking the transcribe skill with a YouTube URL]

> Transcribe this video: [paste a YouTube URL]

[SHOW: Claude downloading audio with yt-dlp, running Whisper, saving the transcript]

It downloads the audio. Runs it through Whisper for transcription. Saves the full text to my scripts folder. All from one command.

[NOTE: Scroll through the transcript briefly to show it's real, complete text]

This is what skills unlock. You're not just chatting with AI anymore. You're building a team of specialists that know exactly how to do their job.

---

### SECTION 5: COMMUNITY SKILLS AND TIPS (13:30 - 14:30) ~1 min

Quick note on community skills. You don't have to build everything from scratch.

[SHOW: Browser — searching for Claude Code community skills]

People are sharing skills online. You can find them on GitHub, in the Claude Code community, and in various repos.

To use someone else's skill, just drop their markdown file into your `.claude/skills/` folder. That's it.

[SHOW: Copying a skill file into the folder]

A few pro tips before we wrap up.

One — start simple. Your first skill doesn't need to be complex. Even a five-line instruction file is useful.

Two — iterate. Use the skill a few times. Notice what's missing. Add instructions. Skills get better the more you refine them.

Three — be specific. The more detailed your instructions, the more consistent the output. Vague skills give vague results.

---

### OUTRO (14:30 - 15:00) ~30 sec

Skills are where Claude Code goes from impressive to indispensable. You're not just using AI — you're training it to work exactly the way you work.

In the next episode, we're covering MCP servers — how to connect Claude Code to your actual tools. GitHub. Notion. Databases. That's where things get really powerful.

[SHOW: End screen with subscribe button and next episode preview]

If you found this useful, subscribe. Drop a comment with the first skill you're going to build. And I'll see you in the next one.

[NOTE: End screen — 20 seconds with subscribe animation and next video card]
