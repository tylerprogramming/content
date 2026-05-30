# Script: Claude Code for Content Creators (Not Developers)

**Target runtime:** 25-30 minutes
**Structure:** AntiGravity format (contrarian hook, show result, setup, framework, live build, result + bonus, close)

---

## SECTION 1: CONTRARIAN HOOK (0:00 - 1:00)

[SHOW: Tyler talking to camera, confident energy]

Every Claude Code tutorial on YouTube right now is for developers. Every single one. And that's a huge missed opportunity.

Because I'm not using Claude Code to build apps. I'm using it to publish over 100 pieces of content every single week. YouTube scripts, LinkedIn posts, Instagram carousels, TikToks, all scheduled and published automatically.

[NOTE: Quick pace here, stack the platforms fast]

My name is Tyler Reed. I've built AI automations for Fortune 500 companies. I helped a YouTuber with 150K subscribers publish over 100 pieces of content a week, some going viral. And I built 6 custom GPTs for one of the biggest Skool communities out there.

I have 22 custom Claude Code skills that run my entire content pipeline. I call it the Content Engine.

By the end of this video, you'll have Claude Code set up with 5 content skills and a full week of social media content scheduled across every platform. No coding required.

And if you want the full system, all 22 skills, templates, and my CLAUDE.md file, that's all inside my Skool community. Link in the description.

---

## SECTION 2: SHOW RESULT FIRST (1:00 - 2:30)

[SHOW: Screen recording - content calendar or Blotato dashboard showing scheduled posts across platforms]

Okay but before we set anything up, let me show you what the end result looks like. Because I think this is going to blow your mind.

[SHOW: Scroll through scheduled posts - LinkedIn, Instagram, X, YouTube Community]

This is my content calendar for this week. 32 pieces of content. Two long-form YouTube videos. Five YouTube Shorts. Five TikToks. Five Instagram Reels. Four Instagram carousels. Seven LinkedIn posts. Two X posts. Two YouTube Community posts.

[NOTE: Pause and let the numbers land]

All of this was generated, formatted, and scheduled using Claude Code. From my terminal. In about 20 minutes total.

[SHOW: Quick flash of terminal running a skill]

And I'm going to show you exactly how to build this. Step by step. Right now.

---

## SECTION 3: SETUP (2:30 - 5:30)

[SHOW: Clean terminal, fresh start]

Okay let's get you set up. This is going to take about 5 minutes. If you already have Claude Code installed, skip ahead to the timestamp on screen.

[SHOW: Chapter timestamp overlay]

### Step 1: Install Claude Code

First you need Node.js. Go to nodejs.org, download the latest version, install it. Takes 2 minutes.

[SHOW: nodejs.org download page briefly]

Now open your terminal. On Mac that's Terminal or iTerm. On Windows, use PowerShell.

Type this:

[SHOW: Terminal typing]

```
npm install -g @anthropic-ai/claude-code
```

[NOTE: Show the install completing]

That's it. Claude Code is installed. One command.

### Step 2: Get Your API Key

Now you need an Anthropic API key. Go to console.anthropic.com. Create an account if you don't have one. Go to API Keys, create a new key, copy it.

[SHOW: Console walkthrough, blur the actual key]

### Step 3: First Launch

Now in your terminal, navigate to your home directory and type:

```
claude
```

[SHOW: Claude Code launching for the first time]

It's going to ask for your API key. Paste it in. And you're in.

[NOTE: Show the Claude Code interface, let it breathe for a second]

This is Claude Code. It looks like a terminal because it is a terminal. But don't let that scare you. You're going to type plain English. That's it.

### Step 4: The CLAUDE.md File

Okay here's where it gets interesting. This is the thing that separates Claude Code from ChatGPT.

[SHOW: Create CLAUDE.md file]

We're going to create a file called CLAUDE.md. Think of this as Claude's instruction manual. It reads this file every single time you start a conversation.

```
claude "Create a file called CLAUDE.md in my home directory"
```

[NOTE: Show Claude creating the file]

Now we're going to fill it with your content rules. Things like:

- What platforms you post on
- Your posting schedule
- Your brand voice and tone
- Your hashtag rules
- Where to save files

[SHOW: Type or paste a sample CLAUDE.md with content creator rules]

Here's what mine looks like. I'll put a template in the description so you can grab it.

The key sections are your custom skills, your posting schedule, and your preferences. This is what turns Claude Code from a generic AI into YOUR content assistant. It knows your rules. Every time.

---

## SECTION 4: THE CONTENT ENGINE FRAMEWORK (5:30 - 7:30)

[SHOW: Simple diagram or whiteboard - "The Content Engine"]

Okay before we start building, let me explain how this system works. Because it's not just random prompts. It's a pipeline.

I call it the Content Engine. And it has 5 stages.

[SHOW: List appearing one by one]

**Stage 1: Research.** You tell Claude Code to search YouTube for what's already working in your niche. What topics get views. What angles perform. This is the /yt-search skill.

**Stage 2: Script.** Based on that research, Claude writes your video script. With hooks, structure, timestamps, everything. This is the /yt skill.

**Stage 3: Repurpose.** One video becomes 15 pieces of content. LinkedIn posts, tweets, Instagram carousels, YouTube Shorts scripts, all from the same source. This is the /content skill.

**Stage 4: Schedule.** Claude connects to Blotato, which is a scheduling tool, and pushes every post to the right platform on the right day. Automatically.

**Stage 5: Repeat.** Next week you do it again. But faster, because your skills get smarter.

[NOTE: Keep this section tight - concept only, no demos yet]

Five stages. Research, script, repurpose, schedule, repeat. That's the Content Engine. Now let's build it.

---

## SECTION 5: LIVE BUILD (7:30 - 21:00)

### Part A: YouTube Research with /yt-search (7:30 - 10:00)

[SHOW: Terminal ready]

Okay let's start with research. I'm going to show you how to find out what's working on YouTube before you make a video.

In Claude Code, I'm going to type:

```
/yt-search claude code tutorial
```

[SHOW: Skill running, scraping YouTube results]

[NOTE: Narrate while it runs - "So what this is doing is searching YouTube for recent videos matching these keywords, pulling view counts, engagement rates, and sorting by performance"]

Look at this. It found 11 videos in the last 30 days. Tech With Tim, 509K views. AI Foundations, 308K. Nate Herk, 303K.

[SHOW: Scroll through the results table]

But here's the thing I want you to notice. Every single one of these is developer-focused. Building apps, writing code, SaaS products. None of them are talking to content creators.

That's a gap. And that's exactly the kind of insight this research gives you.

[SHOW: The saved research file]

This gets saved as a markdown file in your yt-research folder. Date-stamped, searchable, always there when you need it.

Now let me search something else.

```
/yt-search social media ai automation content creator
```

[SHOW: Results coming in]

Look, HubSpot got 80K views with "32 social media posts in 10 minutes." Sandy Lee got 34K with "Automate 90% of social media with Claude Code." The demand is there. People want this.

This is how you find what to make before you make it. Research first. Always.

### Part B: Generating Content with /content (10:00 - 14:00)

[SHOW: Terminal ready]

Now let's generate actual content. Say I just published a YouTube video and I need social media posts for it.

I'm going to run:

```
/content claude-code-for-creators
```

[SHOW: Skill running]

[NOTE: Narrate - "This is reading my video script, pulling key quotes and insights, and generating platform-specific posts"]

Watch what it creates.

[SHOW: LinkedIn post appearing]

Here's the LinkedIn post. Notice it's not just a summary of the video. It's written for LinkedIn. No hashtags, no markdown, no bold text. Because that's what performs on LinkedIn. And Claude knows that because it's in my CLAUDE.md file.

[SHOW: X/Twitter post appearing]

Here's the X post. 230 characters or less. Punchy. No hashtags. Platform-native.

[SHOW: Instagram caption appearing]

Instagram caption. Exactly 5 hashtags. The same 5 every time because those are my brand hashtags.

[SHOW: YouTube Community post appearing]

YouTube Community post. Conversational, asks a question to drive comments.

[NOTE: Let each post sit on screen for 2-3 seconds so people can read them]

Four platforms. Four posts. All formatted correctly for each platform. Took about 30 seconds.

And here's the thing, if I don't like one, I just tell Claude. "Make the LinkedIn post more personal" or "add a story to the X post." It iterates in seconds.

### Part C: Building a LinkedIn Carousel (14:00 - 17:00)

[SHOW: Terminal ready]

Okay this one is fun. LinkedIn carousels are huge right now for engagement. But they take forever to make manually. Canva templates, writing each slide, exporting.

With Claude Code and Blotato, I can generate a full carousel from my video content.

```
/content claude-code-for-creators
```

[SHOW: The carousel content being generated - slide by slide]

Look at this. It's generating slides. Slide 1, the hook. Slide 2 through 5, the key points. Slide 6, the CTA.

[NOTE: Important - always 6 slides max. Slide 7 CTA is unreliable in Blotato]

Six slides. That's the sweet spot. We keep it to 6 because the 7th slide in Blotato can be unreliable, so I use a custom CTA image from Kie.ai as the final slide instead.

[SHOW: Blotato carousel preview if possible]

Now I send this to Blotato and it creates the visual carousel automatically. Each slide, formatted, branded, ready to post.

### Part D: Scheduling with Blotato (17:00 - 19:30)

[SHOW: Terminal ready]

Okay this is the part that ties everything together. We've generated the content. Now we need to schedule it.

Claude Code connects to Blotato through something called an MCP server. You don't need to know what that means. Just know that it lets Claude talk directly to Blotato and schedule posts for you.

[SHOW: Blotato MCP in action]

Let me schedule this week's content.

[NOTE: Show the commands naturally, don't rush]

I tell Claude: "Schedule the LinkedIn post for Monday at 8am, the Instagram carousel for Monday at 12pm, the X post for Monday at 10am."

[SHOW: Posts appearing in Blotato schedule]

And look at that. Three posts scheduled. On the right platforms. At the right times.

Now multiply that across the whole week. Monday and Thursday are my long-form video days. So those get LinkedIn posts, Instagram carousels, X posts, and YouTube Community posts. Tuesday through Sunday, I've got shorts going out, standalone LinkedIn posts, all of it.

[SHOW: Full week calendar view]

32 pieces of content. All scheduled. From one terminal.

### Part E: The Full Week Content Calendar (19:30 - 21:00)

[SHOW: Calendar or spreadsheet view of the full week]

Let me show you what a full week looks like when this system is running.

Monday: Long-form YouTube video drops. LinkedIn post, Instagram carousel, X post, YouTube Community post all go out.

Tuesday: YouTube Short, TikTok, Instagram Reel, standalone LinkedIn post.

Wednesday: Same pattern. Short plus LinkedIn.

Thursday: Second long-form video. Full social media push again.

Friday through Sunday: Shorts, Reels, TikToks, standalone LinkedIn posts.

[SHOW: Point to specific days and content types]

That's 32 pieces of content. From 2 filming days. Because the content creation, the repurposing, the scheduling, that's all handled by Claude Code.

You film. Claude does the rest.

---

## SECTION 6: RESULT + BONUS (21:00 - 24:00)

[SHOW: Tyler back on camera]

So let's recap what we just built. You now have Claude Code installed, a CLAUDE.md file with your content rules, and 5 skills that can research topics, generate scripts, create platform-specific posts, build carousels, and schedule everything.

[NOTE: Tick these off on fingers or with on-screen checkmarks]

That's the Content Engine. And it works every single week.

### Bonus: The Skill That Saves Me the Most Time

[SHOW: Terminal]

Now here's a bonus. The skill I use the most isn't even one of the five we covered. It's /yt-search combined with /shorts.

Every week I run /yt-search on 2 or 3 topics in my niche. Claude analyzes what's getting views. Then I run /shorts and it generates 5 short-form scripts based on what's actually proven to work.

```
/shorts
```

[SHOW: Shorts being generated]

Five scripts. Each one under 60 seconds. With hooks written based on real data, not guesses.

[NOTE: Let a few scripts scroll by so people can see the format]

I film all five in one sitting. Maybe 30 minutes total. And those become my YouTube Shorts, TikToks, and Instagram Reels for the entire week.

That's 15 pieces of content from 30 minutes of filming. Because Claude did the research and the writing.

---

## SECTION 7: CLOSE + CTA (24:00 - 26:00)

[SHOW: Tyler on camera, genuine energy]

Look, I know what some of you are thinking. "This seems too technical for me." I get it. The terminal looks scary. But everything I showed you today was plain English. You type what you want. Claude does it.

You don't need to be a developer. You don't need to know how to code. You just need to know what content you want to create. Claude handles the rest.

If you want the full Content Engine, all 22 skills, my complete CLAUDE.md template, and access to a community of creators building with AI, join my Skool community. The link is in the description. It's free to join and we're in there every day helping people set this up.

[NOTE: Don't oversell - keep it casual]

If this video helped you, smash that like button. Subscribe if you want more content like this. I post two videos a week plus daily shorts, all about using AI tools to create more content in less time.

I'll see you in the next one.

[SHOW: End screen with subscribe button and next video]

---

## Script Notes

- **Total estimated runtime:** 26 minutes
- **Screen recording needed:** Terminal sessions, Blotato dashboard, content calendar view
- **B-roll needed:** Minimal - this is mostly screen + talking head
- **Key transition points:** Section 3 to 4 (setup to framework), Section 5A to 5B (research to content generation)
- **Energy notes:** High energy in hook, teaching energy in setup/framework, excited energy during live build, genuine energy in close
