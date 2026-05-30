# Script: I Automated My Entire YouTube Channel with Claude Code

**Target length:** 28-32 minutes
**Audience:** Content creators, business owners, YouTubers
**Format:** Results-first, organized by what Claude Code DOES (not technical concepts)
**Structure:** Modeled after Dan Martell (498K) - news hook, authority, promise, sections by business outcome

---

## COLD OPEN (0:00 - 0:20)

[SHOW: Rapid montage - your YouTube dashboard, scheduled posts in Blotato, carousel app, thumbnails generating, terminal running skills. Fast cuts, 1-2 seconds each. Music up.]

> Every single week, I publish 32 pieces of content across 7 platforms. Two YouTube videos. Five shorts. Five TikToks. Five Reels. Four Instagram carousels. Seven LinkedIn posts. And I do it in one day.

[SHOW: Cut to talking head]

> This is the system. And the whole thing runs on Claude Code.

---

## AUTHORITY + PROMISE (0:20 - 1:00)

> I'm not a developer. I'm a content creator who figured out that Claude Code isn't a coding tool. It's an automation tool. And once I understood that, everything changed.

> I have 25 custom skills. Text files that tell Claude exactly how to run my workflows. One command plans a video. Another generates thumbnails. Another writes and schedules a full week of social media posts. No VA. No team. Just me and Claude Code.

> In the next 30 minutes, I'm going to show you exactly how all of this works. Not a demo. My real setup. The same system I use every single week.

> And if you stick around to the end, I'll show you the full pipeline from zero to 32 pieces of content, step by step.

---

## 1-MINUTE CTA (1:00 - 1:10)

> Quick thing before we dive in. I put together my actual CLAUDE.md file and 5 starter skills you can download for free. If you want that, just DM me the word SKILLS on Instagram and I'll send it right over. Alright, let's get into it.

[NOTE: Keep this under 10 seconds. Fast, casual, no hard sell. Dan Martell does this at the same timestamp.]

---

## SECTION 1: THE SETUP (1:10 - 4:30)

### The Bridge

> So where does this all start? It starts with one file. And if you get this file right, everything else works. If you skip it, Claude is guessing every single time.

### The Content

[SHOW: Screen recording - open your CLAUDE.md file in VS Code]

> This is called CLAUDE.md. Think of it as your instruction manual for Claude. Every time you open Claude Code, the first thing it does is read this file. My preferences, my workflow, my rules, everything Claude needs to know about how I work.

[SHOW: Scroll through YOUR actual CLAUDE.md slowly]

> Look at this. I've got all 25 of my skills listed with what triggers each one. Below that, my YouTube workflow. The weekly content pipeline, what gets published where, how the files are organized. And at the bottom, my preferences. Things like "never use em dashes" and "LinkedIn posts have no hashtags."

> This file is why when I type "plan a video," Claude doesn't give me a generic outline. It gives me a full package with titles, hooks, a script, a filming guide, and a YouTube description. Because it already knows my format.

[SHOW: Quick demo - type a simple prompt and show how Claude's response is personalized because of the CLAUDE.md]

> Here's what I want you to do. Create a CLAUDE.md file. Put three things in it. What you do. How you like things structured. And your rules. Even 10 lines will completely change what Claude gives you.

> You can even ask Claude to help you write it. Just say "help me create a CLAUDE.md - ask me questions about my workflow." It'll interview you and build the file.

[NOTE: This section establishes that Claude Code is personalized to YOU. Not generic. This is the foundation everything else builds on.]

**TRANSITION:** "So Claude knows who you are now. But what can it actually do with that? Let me show you what my Monday morning looks like."

---

## SECTION 2: RESEARCH (4:30 - 9:00)

### The Bridge

> Real quick before I show you this. Everything I'm about to demo runs on something called skills. A skill is just a text file where you write down your process step by step. Claude reads it and follows the instructions every time. That's it. No code. Just a text file. Watch.

> Every video I make starts with research. I used to spend 2 hours on this. Opening YouTube, clicking through videos, copying titles into a spreadsheet, trying to spot patterns. Now it takes 30 seconds.

### The Content

[SHOW: Screen recording - Claude Code terminal]

> I type /yt-search and give it a topic.

[SHOW: Type "/yt-search claude code tutorial" and hit enter]

> That's a skill. A text file with instructions. Claude reads the file and follows the steps. It searches YouTube, pulls the top videos sorted by views, downloads their thumbnails, and saves a full research report. All automatically.

[SHOW: The research report appearing. Show the markdown with the table of videos, view counts, title patterns.]

> But watch what happens next.

[SHOW: Type "/transcribe [url]" with one of the top video URLs]

> I take the best performing videos and transcribe them. Now I can study exactly what they said, how they structured their hooks, what worked. This is competitive research that used to take an entire afternoon.

[SHOW: Transcript appearing in the scripts folder]

> And here's the part that ties it all together.

[SHOW: Type "/yt" to start planning the video]

> I type /yt. Claude reads the research report, reads the transcripts, does its own web research, and then asks me a few questions about my angle. After that, it generates everything. 10 title options with a scorecard. 5 hooks with the first 30 seconds scripted word for word. A full script with show markers and production notes. A filming guide. And a YouTube description.

[SHOW: The output folder with all the generated files. Open titles.md briefly, then script.md briefly.]

> One morning. Research, transcription, and a complete video package. That's three skills. /yt-search, /transcribe, /yt. And they're all just markdown files with instructions.

[NOTE: This is the "wow" section. Take your time showing the outputs. Let the viewer see the quality of what gets generated.]

**TRANSITION:** "So the video is planned. The script is written. But I still need visuals. Thumbnails, carousels, social graphics. And I haven't opened Canva in 6 months. Let me show you why."

---

## SECTION 3: CREATE VISUALS (9:00 - 14:00)

### The Bridge

> Most creators spend 30 to 45 minutes per thumbnail. Another hour on Instagram carousels. I replaced all of that with three commands.

### The Content

[SHOW: Screen recording - Claude Code terminal]

> First, thumbnails. I type /thumbnail and describe what I want.

[SHOW: Type "/thumbnail" with a description. Show Claude generating the prompt and sending it to Nano Banana Pro.]

> Claude writes the prompt and sends it to an AI image generator called Nano Banana Pro. I get multiple thumbnail options in under a minute.

[SHOW: Thumbnail variants appearing. Show 3-4 options.]

> No Photoshop. No Canva. No design skills. And these aren't generic AI images. Claude knows my brand because it read my CLAUDE.md. It knows what style works for my channel.

[SHOW: Side by side - AI generated thumbnail next to one of your real published thumbnails]

> Second, Instagram carousels.

[SHOW: Type "/instagram-writer" with a topic]

> One command. Claude generates all 6 slides of copy. Cover, pain point, solution, how it works, results, and CTA. Then it creates AI backgrounds using Nano Banana.

[SHOW: The carousel app opening with slides populated. Show the backgrounds being generated.]

> I built a custom carousel app for this. I load the slides, add the AI backgrounds, adjust the text, and export. The whole thing takes about 2 minutes.

[SHOW: Carousel app in action - scrolling through slides, exporting PNGs and PDF]

> And third, social media graphics. Product shots, Pinterest pins, ad creatives. All through the same image generation pipeline. Claude writes the prompt, the AI generates the image, everything gets saved and organized automatically.

[SHOW: Quick montage of different visual outputs - thumbnails, carousels, Pinterest pins]

> Now here's what makes this a system and not just a bunch of tools. Claude Code connects to these image generators through something called MCP servers. Think of it as a bridge. Claude talks to the API, the API generates the image, Claude saves it where it needs to go. I never leave the terminal.

[NOTE: Don't go deep on MCP here. Just name it, explain it in one sentence, and move on. The point is the RESULT, not the infrastructure.]

**TRANSITION:** "So I've got the video planned, the thumbnails done, the carousels built. But I still need social media posts for 7 platforms. And I need them to not all sound the same. That's where this gets really powerful."

---

## SECTION 4: WRITE ALL SOCIAL POSTS (14:00 - 18:30)

### The Bridge

> Every video I publish needs posts for LinkedIn, X, Instagram, YouTube Community, and Pinterest. Each platform has different rules. LinkedIn is educational, no hashtags. X is punchy, under 230 characters. Instagram needs exactly 5 hashtags. If I wrote all of these manually, that's half a day.

### The Content

[SHOW: Screen recording - Claude Code terminal]

> I type /content and point it at my video package.

[SHOW: Type "/content" and show Claude reading the script, generating posts]

> Claude reads my script, my description, my titles. Then it generates platform-native posts for every single platform. Not the same post copied 7 times. Each one is written for that specific platform.

[SHOW: Open the generated LinkedIn post. Then the X post. Then the Instagram caption. Show how they're different.]

> The LinkedIn post teaches something from the video in 4-5 sentences. No hashtags, no bold, no markdown. That's in my CLAUDE.md. Claude follows it every time.

> The X post is a standalone insight, under 230 characters. Not "check out my new video." An actual thought that makes sense on its own.

> The Instagram caption has a hook, value, and exactly 5 hashtags. Always the same 5. Because that's my rule and Claude knows it.

[SHOW: Side by side comparison of all the posts for one video]

> But here's the part that used to take me the longest. Scheduling.

[SHOW: Claude Code connecting to Blotato]

> Claude connects directly to my scheduling tool, Blotato. It uploads the images, writes the captions, and schedules everything for the week. LinkedIn goes out on the video release day. Instagram carousel that same day. Shorts content throughout the week. I confirm, and the entire week is done.

[SHOW: Blotato schedule view showing a full week of posts queued]

> That's one conversation in Claude Code. Research, visuals, posts, scheduling. The whole pipeline.

[NOTE: The Blotato scheduling demo is the money shot of this section. Make sure viewers see the full week populating. This is the "set it and forget it" moment Dan Martell talks about.]

**TRANSITION:** "Now you might be thinking, this sounds amazing but also complicated. How long does this actually take? Let me show you the full pipeline, start to finish."

---

## SECTION 5: THE FULL SYSTEM (18:30 - 23:00)

### The Bridge

> Let me walk you through what my actual content day looks like. From zero to a full week of content. Real time, real system.

### The Content

[SHOW: Talking head, then cut to screen recording for the walkthrough]

> Monday morning. I open Claude Code. First, I run /yt-search on two topics I want to cover this week. That gives me research on what's performing right now.

> Then I transcribe the top 2-3 reference videos with /transcribe. Now I have competitive intelligence.

> Then I run /yt on each topic. Claude reads the research, reads the transcripts, asks me my angle, and generates two full video packages. Scripts, titles, hooks, descriptions, filming guides. Both done.

> Then I run /shorts. Claude reads the research reports and generates 5 short-form scripts for the week. Each one has captions for YouTube Shorts, TikTok, Instagram Reels, and LinkedIn.

> Then /content for each video. LinkedIn posts, X posts, Instagram captions, YouTube Community posts. Platform-native, all different.

> Then /thumbnail for both videos. AI thumbnails in under a minute.

> Then /instagram-writer for 4 carousels. Build them in my carousel app with AI backgrounds.

> Then I tell Claude to schedule everything through Blotato. It uploads, sets the times, confirms.

[SHOW: The Blotato calendar view with the full week populated]

> That's the pipeline. /yt-search, /transcribe, /yt, /shorts, /content, /thumbnail, /instagram-writer, and Blotato. 8 skills. One morning. 32 pieces of content.

> The rest of the week? I film. I edit. The content system runs itself.

[SHOW: Quick recap graphic showing the pipeline - can be a simple list or flowchart]

> And here's the thing. Every one of these skills is just a markdown file. Plain English instructions. No code. I wrote each one in about 5 minutes. You tell Claude what to do step by step, and it follows those instructions every time you call it.

**TRANSITION:** "Now I want to show you something that makes this whole system even smarter over time."

---

## SECTION 6: MEMORY + THE SYSTEM THAT LEARNS (23:00 - 26:00)

### The Bridge

> Most AI tools forget everything between sessions. You start fresh every time. Claude Code doesn't. It remembers.

### The Content

[SHOW: Screen recording - open MEMORY.md]

> Claude Code has a memory system. It stores what it learns about you and your project in a file called MEMORY.md. Next time you start a session, it reads that file and already knows the context.

[SHOW: Your actual MEMORY.md with project details]

> My memory file knows that my video engine runs on port 3001. It knows my preferred file structure. It knows my posting schedule. I never have to re-explain any of this.

> And the skills themselves get better over time. When I notice something Claude gets wrong, like using em dashes when I've told it not to, I update the skill file. That fix is permanent. Claude never makes that mistake again.

> That's the difference between a tool and a system. A tool does what you tell it once. A system learns, improves, and compounds. Every week, my content pipeline gets a little bit faster, a little more accurate, and I do a little less manual work.

[SHOW: Side-by-side of an early skill file vs the current version, showing how it's evolved]

> Six months ago, I was writing every LinkedIn post manually. Now Claude generates 7 per week in my voice, schedules them automatically, and the quality is better than what I was writing by hand. That didn't happen overnight. It happened because the system learned.

**TRANSITION:** "So that's the entire system. But I know what you're thinking. How do I actually get started?"

---

## SECTION 7: YOUR FIRST 15 MINUTES (26:00 - 28:30)

### The Bridge

> If you're watching this and thinking "this is a lot," I get it. Here's exactly what I'd do if I was starting from scratch today.

### The Content

[SHOW: Talking head, direct to camera]

> Step 1. Install Claude Code. It's free to install. You need a Claude account, which is $20 a month. That's it.

[SHOW: Quick flash of the installation]

> Step 2. Create your CLAUDE.md file. Ask Claude to help you write it. "Help me create a CLAUDE.md. Ask me questions about my workflow." It'll interview you and build the file in 5 minutes.

> Step 3. Pick one thing you do every week that takes more than 30 minutes. Maybe it's writing social posts. Maybe it's planning content. Maybe it's doing research. Whatever it is, write down the steps in a markdown file. Put it in your skills folder. That's your first skill.

> Step 4. Use it. Call the skill. See what happens. If the output isn't right, tell Claude what to fix. Update the skill file. Run it again.

> That's it. That's how I started. One CLAUDE.md file and one skill. Six months later, I have 25 skills and a system that runs my entire content operation.

[NOTE: This section should feel achievable, not overwhelming. Keep the energy encouraging. "That's how I started" is the key line.]

---

## CTA + OUTRO (28:30 - 30:00)

> Here's my challenge to you. This week, build one skill. Just one. Whatever task eats the most time in your week, automate it with a markdown file and Claude Code.

> Drop a comment and tell me what you'd automate first. I read every single one.

> And if you want the full system, all 25 skills, my CLAUDE.md file, my MCP server configs, the whole content engine, that's all inside my Skool community. The link is in the description.

> If you want to see me build a specific skill from scratch, start to finish, that video is right here.

[SHOW: Point to end screen card]

> I'll see you in the next one.

[NOTE: Keep this tight. 60-90 seconds max. Don't ramble. End with energy and confidence.]

---

## CueCard

```
COLD OPEN
- 32 pieces, 7 platforms, one day
- "The whole thing runs on Claude Code"

AUTHORITY (0:20)
- Not a developer, content creator
- 25 custom skills, text files
- No VA, no team, just me + Claude Code
- Real setup, not a demo

1-MIN CTA
- "DM me SKILLS on Instagram for my CLAUDE.md + 5 starter skills"

SECTION 1: SETUP (1:10)
- CLAUDE.md = instruction manual
- Show MY file: skills, workflow, preferences
- Why Claude's output is personalized
- ACTION: Create yours, 3 things, or ask Claude to help

SECTION 2: RESEARCH (4:30)
- Quick skills explainer: "text file with your process, Claude follows it"
- /yt-search = 30 seconds, full report
- /transcribe = study competitor hooks
- /yt = complete video package (titles, hooks, script, filming guide)
- "Three skills. One morning."

SECTION 3: VISUALS (9:00)
- /thumbnail = Nano Banana, multiple options, under 1 min
- /instagram-writer = 6 slides + AI backgrounds
- Carousel app demo
- MCP = bridge to image generators (one sentence)

SECTION 4: SOCIAL POSTS (14:00)
- /content = platform-native for all 7
- Show LinkedIn vs X vs IG differences
- Blotato scheduling = full week in one conversation
- MONEY SHOT: Blotato calendar full

SECTION 5: FULL SYSTEM (18:30)
- Walk through real content day
- /yt-search -> /transcribe -> /yt -> /shorts -> /content -> /thumbnail -> /instagram-writer -> Blotato
- "8 skills. One morning. 32 pieces."

SECTION 6: MEMORY (23:00)
- MEMORY.md = it remembers across sessions
- Skills improve over time
- "The difference between a tool and a system"

SECTION 7: GET STARTED (26:00)
- Install (free + $20/mo)
- Create CLAUDE.md (ask Claude to help)
- Pick ONE task, write steps, make a skill
- "That's how I started"

CTA (28:30)
- Challenge: build one skill this week
- Comment what you'd automate
- Skool for full system
- Point to next video
```
