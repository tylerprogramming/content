# Script: 32 Posts a Week, 7 Claude Code Skills. Here's How.

**Target length:** 30-35 minutes
**Format:** Proof open → Framing → 7 skills (3-4 min each, every one shows the actual prompt + result) → Workflow tie-together → Build your own → CTA
**Energy:** Practical, proof-heavy, fast cuts on demos, slow cuts on "why it matters"

**Reference pattern:** Tyler's AntiGravity beginner script — concrete prompts in code blocks, real demos with real numbers, `[SHOW:]` and `[NOTE:]` cues for the editor.

---

## [0:00 - 0:20] Hook (Proof First)

> This is 32 pieces of content going out this week across YouTube, LinkedIn, X, Instagram, TikTok, Pinterest, and Skool.

[SHOW: Blotato content calendar with 32 scheduled posts visible. Quick scroll through showing the variety of platforms. Color-coded by platform.]

> There's no team. No VA. Just me, a full-time job, and these 7 Claude Code skills.

[SHOW: Quick terminal capture — type `/` slowly, autocomplete cycles through 43 skill names, then highlight 7 specific ones with a subtle ring.]

> I'm going to show you all 7, the exact prompts I use, and the Monday morning workflow that connects them. Then I'll show you how to build your own.

[NOTE: Energy is HIGH here. Confident, fast. The Blotato calendar IS the proof — make sure it shows real scheduled posts before recording.]

---

## [0:20 - 1:45] Framing

[SHOW: Face to camera, second monitor visible in frame with VS Code + Claude Code terminal]

> Quick setup so you know what you're getting.

> I'm a full-time software engineer. I have a wife and kids. Content gets made between 4 and 5:30 PM on weekdays, and a few hours on weekends. That's it. That's the time budget.

> If you're not full-time on content, you have to be ruthless about leverage. Skills are how I get leverage out of Claude Code.

> A Claude Code skill is just a slash command I can type. Each one wraps a workflow I'd otherwise do manually — research, scripting, posting, community management.

> I've built 43 of them. Most are experiments. 7 are essential. Those 7 — and only those 7 — are what I run every week.

> Here's how they connect.

[SHOW: Animated diagram or whiteboard with 7 boxes labeled `/yt-search → /transcribe → /yt → /seo → /shorts → /content → /skool`, each connected with arrows.]

> Research, transcripts, video planning, SEO, shorts, social posts, community. End to end content pipeline.

> Let's start with the one that kicks off every Monday morning.

[NOTE: Don't dwell here. Get to the demos. The diagram appears for 5 seconds, then we move.]

---

## [1:45 - 6:00] Skill 1 — `/yt-search`

### The setup (1:45 - 2:30)

[SHOW: Talking head, then cut to terminal]

> Skill one. `/yt-search`.

> Every Monday at 4 PM, I sit down to plan two long-form videos for the week. The first question I ask isn't "what should I make?" It's "what's actually working right now in my space?"

> If you don't answer that question first, you're guessing. And guessing is how channels die.

### The prompt + the demo (2:30 - 5:00)

[SHOW: Terminal — type the command in real time]

```
/yt-search claude code
```

> That's the whole command. I'll run it with the keyword "claude code." Under the hood it uses yt-dlp to pull recent videos, filters to the last 30 days, sorts by views, downloads the thumbnails into a folder, and saves a markdown report.

[SHOW: Terminal runs for ~60 seconds. Show the progress output. Speed-ramp if it takes longer.]

> About a minute. Let me open the report.

[SHOW: VS Code opening `~/content/yt-research/2026-05-17-claude-code.md` — scroll through the table of titles, views, durations.]

> 33 videos. Sorted by views. I can see in 30 seconds what title formulas are working, who's making them, what durations are hitting.

[SHOW: Open the thumbnails folder in Finder. Scroll through them.]

> And the thumbnails are downloaded. I can see what's working visually too — Alberta Tech's "Well... that explains it" with the face left, text right? That formula is doing 413,000 views.

### Why it matters (5:00 - 6:00)

> This is research that used to take me 2 hours a week — clicking around YouTube, copying titles into a doc, screenshotting thumbnails. Now it's 60 seconds.

> And this report is the input to every other skill in this pipeline. Garbage in, garbage out. Research is the moat.

> One skill, one command, the foundation of everything. That's number 1.

[NOTE: Make sure the search you run on camera returns real, current data. If you're filming on a different day, re-run it that morning so the views are fresh.]

---

## [6:00 - 10:30] Skill 2 — `/transcribe`

### The setup (6:00 - 6:30)

[SHOW: Face to camera, then terminal]

> Skill 2. `/transcribe`.

> Once I know what's working, I need to study the actual content. Watching a 30-minute competitor video to take notes is a waste of time when I can just read it.

### The prompt + the demo (6:30 - 9:00)

[SHOW: Pull the top result URL from the yt-search report — Alberta Tech's "Why devs are OBSESSED" — and run the transcribe command.]

```
/transcribe https://youtube.com/watch?v=LACyqdAfnaw
```

> Paste any YouTube URL. Skill downloads the audio with yt-dlp, runs it through OpenAI Whisper, saves the transcript to my scripts folder.

[SHOW: Progress bars for download + whisper. Speed-ramp.]

> Done in about 90 seconds for a 12-minute video.

[SHOW: Open `~/content/scripts/transcript_LACyqdAfnaw.txt` in VS Code.]

> Now I can read the entire video in 5 minutes. I can ask Claude — what was the hook, how did they structure it, what's the call to action — without watching anything.

[SHOW: Type into Claude Code chat:]

```
read ~/content/scripts/transcript_LACyqdAfnaw.txt and tell me the hook, the 3 main beats, and the CTA in bullet form
```

[SHOW: Claude's response appearing — bullet breakdown.]

> 30 seconds of reading. I have the structural takeaways. I can riff on them, beat them, or steal them. That's how I plan a video.

### Why it matters (9:00 - 10:30)

> Most creators are *watching* their competitors. I'm *reading* them. I can process 5 competitor videos in the same time it takes someone to watch one. That's not a flex — it's better leverage.

> One small thing — there's a corrections file in this skill that auto-fixes whisper mishears for my topic. "Cloud" gets corrected to "Claude." "Appify" to "Apify." "Claude.ai slash code" to "claude.ai/code." Set it once, it runs forever.

> Number 2.

---

## [10:30 - 16:00] Skill 3 — `/yt` (the heaviest lifter)

### The setup (10:30 - 11:15)

[SHOW: Talking head]

> Skill 3 is the one that does the most work. `/yt`.

> Most people, when they decide to make a YouTube video, sit down with a blank doc and start typing. I never start with a blank doc. I run `/yt` with a transcript as input, and 5 minutes later I have a complete video package.

### The prompt + the demo (11:15 - 14:30)

[SHOW: Terminal]

```
/yt ~/content/scripts/transcript_LACyqdAfnaw.txt
```

> Point the skill at the transcript I just pulled.

[SHOW: The skill responds — asks 1-2 clarifying questions. Tyler answers on camera.]

> See that? It just asked me what my angle is. My take. The unique slot I'm filling. Because if I skip this question, the script will sound like every other one out there.

[SHOW: Type the answer:]

```
Mine is the technical/creator angle — I'll show the actual commands and skills, not just talk about Claude Code at a high level.
```

[SHOW: Skill runs — show the package folder filling up at `~/content/youtube/<new-slug>/`]

> Watch the folder. `analysis.md`. `titles.md` with 10 scored options. `hooks.md` with 4 hooks to test. `script.md` — word for word, scene by scene. `description.md`. `filming-guide.md` with timestamps, b-roll notes, and energy cues for the editor.

[SHOW: Open each file briefly. Show the title scorecard. Show the script's chapter structure.]

> This used to be my entire weekend. Sit down Saturday morning, finish Sunday night, exhausted. Now it's 5 minutes.

### Why it matters (14:30 - 16:00)

> Here's the thing I want you to internalize. The skill isn't writing the video *for* me. It's writing the *80% draft* I edit and personalize. I still bring the stories, the contrarian takes, the actual recording. But I never start from zero. Ever.

> That's the difference between people who publish 1 video a month and people who publish 8.

> Number 3.

[NOTE: When the skill asks a question on camera, ALWAYS answer it on camera. Viewer needs to see the human-AI interaction loop. Don't pause and edit it out.]

---

## [16:00 - 19:00] Skill 4 — `/seo`

### The setup + demo (16:00 - 18:00)

> Skill 4 — `/seo`. Quick one but important.

[SHOW: Terminal]

```
/seo 7-skills-run-my-business
```

> Point it at any package folder. Skill does competitive research on the title and topic, optimizes the title for CTR, rewrites the description with proper keywords, generates a tag list.

[SHOW: Skill runs — display the before/after title comparison side by side.]

> Before — my draft title was "I Have 43 Claude Code Skills. These Are the 7 I Actually Use."
>
> After `/seo` recommended — "32 Posts a Week, 7 Claude Code Skills. Here's How."

[SHOW: The seo.md file opening — show the scored title options.]

> Stronger CTR pattern. Two verifiable numbers. Implied tutorial. Higher search match.

### Why it matters (18:00 - 19:00)

> The first hour of a video's life on YouTube decides the next 30 days of its life. The title and thumbnail decide if you get the first 1,000 views. This skill makes sure I don't burn that hour on a weak title.

> Number 4.

---

## [19:00 - 23:30] Skill 5 — `/shorts`

### The setup (19:00 - 19:45)

> Skill 5 is the one that makes me feel like I have a team — `/shorts`.

> Most creators batch shorts by filming them all on one day. That works, but the bottleneck isn't filming. It's scripting. Coming up with 5 different angles, 5 different hooks, 5 different scripts every week is what burns people out.

### The prompt + demo (19:45 - 22:30)

[SHOW: Terminal]

```
/shorts
```

> No arguments. It reads my latest yt-research reports, identifies the 5 highest-leverage angles, writes 5 short-form scripts.

[SHOW: Folder structure populating — `~/content/youtube/shorts/<NNN> - <Title>/script.md` and `captions.md` for each of 5 shorts.]

> 5 folders. Each one has a script optimized for 30-60 seconds with a hook in the first 1.5 seconds. Each one has captions for YouTube Shorts, TikTok, Instagram Reels, and LinkedIn — each platform formatted correctly.

[SHOW: Open one of the script.md files. Briefly highlight the hook + body + CTA structure.]

> Look at the format. Hook line in bold at the top. Body. CTA. Captions section below with per-platform versions — exactly 5 hashtags for Instagram, none for X, no markdown for LinkedIn.

[NOTE: Showcase the captions.md file too — that's where Tyler's tactical work lives. Skim each platform's caption to show platform-native differences.]

### Why it matters (22:30 - 23:30)

> Short-form distribution is non-negotiable in 2026. Algorithms reward consistency. But trying to think of 5 new angles every week is what kills creators.

> This skill outsources the angle generation so I can focus on the on-camera delivery. I record all 5 in one 45-minute session. They cover a full week.

> Number 5.

---

## [23:30 - 27:30] Skill 6 — `/content`

### The setup + demo (23:30 - 26:30)

> Skill 6 — `/content`. When a long-form video drops, I don't just post it on YouTube. I cut it into platform-native posts for X, LinkedIn, Instagram, YouTube Community, and Skool.

[SHOW: Terminal]

```
/content 7-skills-run-my-business
```

> Point at a video package. Skill reads everything and generates all the posts.

[SHOW: `~/content/youtube/7-skills-run-my-business/social/` folder appearing — x.md, linkedin.md, instagram.md, community.md, skool.md]

> 5 files. Each one platform-native.

[SHOW: Open each file briefly, narrate the differences]

> X post — 230 characters, no hashtags. LinkedIn — long-form story format, no markdown, no hashtags, no em dashes. Instagram — 6-slide carousel outline with exactly 5 hashtags. YouTube Community — short engagement post. Skool — community-specific discussion starter.

> Every single one is written for the surface it'll appear on. Not the same caption pasted 5 times.

### Why it matters (26:30 - 27:30)

> One video, 5 social posts, 20 minutes of cleanup, all scheduled via Blotato. Without this skill that's 90 minutes of manual platform-by-platform writing.

> Number 6.

---

## [27:30 - 30:30] Skill 7 — `/skool`

### The setup + demo (27:30 - 29:30)

> The 7th skill ties everything to the business. `/skool`.

> If you don't know, Skool is the community platform I run my AI agency community on. The skill automates everything I'd otherwise have to click through manually.

[SHOW: Terminal]

```
/skool post
```

> Writes a community post through the Skool API.

```
/skool sync members
```

> Pulls every member into the local SQLite database.

```
/skool engagement
```

> Ranks active members vs members who've gone quiet.

[SHOW: Each command running in sequence. Show the post appearing in the actual Skool browser tab. Show the SQLite query returning real member counts (anonymized if needed).]

> I run this every Sunday night. 15 minutes of work replaces what used to be 2 hours of clicking through the dashboard.

### Why it matters (29:30 - 30:30)

> Communities are the new content. Skool, Substack, Discord — every creator now has one attached to their channel. The bottleneck stops being content and starts being community management.

> If you automate that, you keep your weekend. Number 7.

---

## [30:30 - 33:00] The Workflow — How All 7 Connect

[SHOW: Same diagram from segment 2, but now each box lights up as Tyler narrates the order. Time-lapse style.]

> Monday at 4 PM. Here's exactly what happens.

> First — `/yt-search` on the two topics I want to cover next week. About 2 minutes total.

> Second — `/transcribe` on the top 2 reference videos. 5 minutes.

> Third — `/yt` twice, once per topic. 10 minutes including the clarifying questions.

> Fourth — `/seo` on both packages. 4 minutes.

> Fifth — `/shorts` once for the week. 3 minutes.

> Sixth — `/content` on both long-form packages. 4 minutes.

> Seventh — `/skool` to queue the weekly community posts. 3 minutes.

> Total — 31 minutes. The output is a full week of content across 7 platforms — 32 pieces.

[SHOW: Quick cuts of the actual output folders filling up — yt-research/ → scripts/ → youtube/<slug>/ → youtube/shorts/ → youtube/<slug>/social/]

> Tuesday and Wednesday I film. Editor takes over. By next Monday, the cycle repeats.

> 7 skills. One workflow. 32 posts.

[NOTE: This segment IS the proof. Spend 2-3 minutes here. Don't rush.]

---

## [33:00 - 35:00] How to Build Your Own + CTA

[SHOW: Open `~/.claude/skills/save-idea/SKILL.md` in VS Code — pick one of the smallest skills to demystify]

> Last thing. How do you build your own?

> A Claude Code skill is just a markdown file. That's it. Top of the file is YAML frontmatter — name, description, allowed tools, whether it's user-invocable. Below that is plain English instructions for what the skill should do.

> Drop the file at `~/.claude/skills/<name>/SKILL.md`. Restart Claude Code. Type `/<name>`. It runs.

[SHOW: Restart Claude Code, type `/save-idea`, show it firing.]

> If you can write a Google doc, you can build a skill. I have a full video walking through building your first one from scratch in 15 minutes — link in the description below.

[CAMERA: Direct to lens, energy up]

> If you want all 7 of these skills, plus the other 36, I dropped them in my Skool community — link below, free.

> If this was useful — subscribe. New videos Mondays and Thursdays. I'll see you in the next one.

[SHOW: Quick callback montage — Blotato calendar from the hook → 7 skill commands firing in sequence → folders filling up → calendar with all 32 posts scheduled. Fast cuts, 1.5 sec each. Mirror the energy of the open.]

---

## Production Notes

### B-roll Needed (capture before main shoot)

- **Hook montage:** Blotato content calendar with 32 real scheduled posts (must be authentic — pull from actual upcoming week)
- **Terminal montages:** all 7 skills firing in 5-second clips for the hook
- **Real folder views in Finder:** yt-research/, scripts/, youtube/<slug>/, youtube/shorts/, youtube/<slug>/social/
- **Real Skool dashboard** showing a post that was created via the skill
- **SQLite browser** with anonymized member data
- **Workflow diagram** (Excalidraw, Remotion animation, or whiteboard) — animate the boxes lighting up in order

### Sensitive Content Checklist (before recording)

- [ ] Don't show real customer emails in the Skool member sync demo — anonymize or use test data
- [ ] Verify `~/.claude/.env` is NEVER visible on screen
- [ ] Blotato calendar shows post titles, not full content — make sure none reveal unannounced launches
- [ ] Real YouTube URLs in the demos should be public videos (the Alberta Tech URL is — that's safe)
- [ ] Skool community count visible is OK to show, but don't show member names/emails

### Energy Curve

| Segment | Energy | Notes |
|---|---|---|
| Hook | 10/10 | Proof first |
| Framing | 7/10 | Setting stakes |
| Each skill setup | 7/10 | Lead with the problem |
| Each skill demo | 5/10 | Let the screen do the work |
| Each skill payoff | 8/10 | Sell the value |
| Workflow segment | 9/10 | The "aha" moment |
| Build your own | 8/10 | Empowering |
| CTA | 10/10 | Get the click |

### Common Mistakes to Avoid

1. **Don't read the script.** Use it as a map, riff the lines.
2. **Don't apologize on camera if a skill takes a moment.** Cut the pause in edit.
3. **Don't mention every skill in the cold open.** Save the payoff for each segment.
4. **Don't blur through demos.** The demos ARE the video. Let them breathe.
5. **Don't fake the Blotato calendar.** If you don't actually have 32 posts scheduled this week, use the real count and update the script. Tyler's whole brand is verifiability.

### Chapters (paste into YouTube description)

- 0:00 32 posts a week, no team
- 0:20 The setup (full-time job + family time)
- 1:45 Skill 1: /yt-search (research in 60 seconds)
- 6:00 Skill 2: /transcribe (read competitors instead of watching)
- 10:30 Skill 3: /yt (the heaviest lifter — full video package in 5 min)
- 16:00 Skill 4: /seo (title and tags)
- 19:00 Skill 5: /shorts (5 scripts in 3 min)
- 23:30 Skill 6: /content (cross-platform posts)
- 27:30 Skill 7: /skool (community automation)
- 30:30 The Full Workflow (31 minutes = 32 posts)
- 33:00 How to Build Your Own + CTA
