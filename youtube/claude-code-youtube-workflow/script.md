# Video Script: I Automated My Entire YouTube Workflow with Claude Code

---

## [0:00 - 0:30] Hook

> This video you're watching right now? I planned it using four commands in my terminal.
>
> I searched YouTube to find what's trending. I transcribed competitor videos to study their hooks and structure. I had Claude write the entire video package — titles, hooks, script, filming guide. And then it generated the thumbnail you clicked on to get here.
>
> I didn't open a browser. I didn't open Google Docs. I did it all from right here.
>
> Let me show you exactly how.

[SHOW: Quick flash of terminal with /yt-search running, then /transcribe output, then /yt generating files, then /thumbnail generating images — 2 seconds each. Then cut to THIS script.md file on screen.]

[NOTE: This is the big moment. The viewer realizes the video is self-referential. Deliver "right here" while pointing at or gesturing toward the terminal. High energy.]

---

## [0:30 - 1:30] The Problem

> So here's what content research used to look like for me.
>
> I'd open YouTube, search for whatever topic I was thinking about, click through a bunch of videos, take notes on what's working, what titles are getting views, what angles have been done.
>
> Then I'd find a video that's doing well and try to figure out what they're doing right. Watch the whole thing. Take notes. Maybe watch it again.
>
> Then I'd open a Google Doc and start outlining my video. Titles, hooks, script — all from scratch.
>
> And every single time I started a new video, I'd do the whole thing over again.
>
> That's easily 2 to 3 hours before I even start writing. And honestly? Half the time I'd skip the research and just wing it.
>
> So I built a system. Four Claude Code skills that handle the entire pipeline — including the thumbnail. Let me show you each one.

[SHOW: Quick montage of the "old way" — browser tabs, YouTube search, Google Docs. Then cut to clean terminal.]

[NOTE: Keep the "old way" description quick and relatable. Don't dwell. The viewer already knows the pain.]

---

## [1:30 - 4:00] Skill 1: /yt-search

> Skill number one. YouTube research.
>
> I type slash yt-search, and then whatever keywords I'm interested in. Let's use the exact search I ran for this video.

[SHOW: Terminal. Type `/yt-search claude code`]

> It hits YouTube through yt-dlp, pulls the 50 most recent videos, filters to the last 30 days, and sorts them by views. Top 15.

[SHOW: The script running. Watch the output stream in.]

> And here's what I get.

[SHOW: Open the generated report at `~/content/yt-research/2026-02-24-claude-code.md`. Show the summary table.]

> A clean markdown report. Every video — title, channel, views, likes, comments, duration, upload date, and a link.
>
> So right away I can see — Nick Saraev's 4-hour course has 266K views. The Lenny's Podcast episode with the head of Claude Code has 215K. NetworkChuck's "Claude Code on your phone" is at 204K.
>
> This tells me what formats are working. Long courses are crushing it. Podcast interviews are doing well. Short practical tutorials are in the mix.
>
> And more importantly — I can see what's NOT there. Nobody's showing Claude Code for content creation. It's all coding tutorials. That's a gap. That's my angle.
>
> All of that from one command. No browser. No spreadsheet.

[SHOW: Scroll through the report slowly. Let the viewer see the data. Highlight the gap — maybe circle or annotate "all coding tutorials" on screen.]

[NOTE: This is where you prove the value. Don't rush past the data. Let the viewer absorb the table. The "gap" insight is the payoff.]

---

## [4:00 - 7:30] Skill 2: /transcribe

> Okay, so now I know what's on YouTube. I can see what's getting views. But I want to go deeper — I want to know exactly what these top videos are saying. What hooks are they using? How are they structuring the content?
>
> Skill number two. Slash transcribe.

[SHOW: Terminal. Type `/transcribe https://youtube.com/watch?v=VIDEO_ID` with a real video URL from your /yt-search results]

> I give it a YouTube URL — usually one of the top performers from my search — and it does everything automatically.
>
> It downloads the audio using yt-dlp, runs it through Whisper for transcription, and saves the full transcript.

[SHOW: Script running — downloading audio, transcribing, saving.]

> And here's what I get.

[SHOW: Open the transcript at `~/content/scripts/transcript_VIDEO_ID.txt`. Show the full text.]

> A complete word-for-word transcript of the video. Now I can actually study what's working.
>
> But here's where it gets interesting. I don't just read the transcript — I have a conversation about it.

[SHOW: Terminal with Claude. Paste transcript and start a conversation.]

> I'll ask Claude to break down the structure. What sections does this video have? How long is each one? What's the flow?

[SHOW: Claude responding with a structural breakdown — intro, problem, solution, demo, CTA, etc.]

> Then I go deeper. What hooks are they using? What's working? What would I do differently?

[SHOW: Continue the conversation — "What hooks does this video use? What's missing that I could cover?"]

> And this is where I start planning my own angle. I'll say — here's what I want to teach. Here's my unique take. How should I structure this differently? What are they NOT covering that I should?

[SHOW: You typing something like "I want to make a video about X. Based on this transcript, what angles are they missing? How could I improve on this?"]

> Claude comes back with specific suggestions. Maybe they rushed the setup. Maybe they didn't show a real use case. Maybe there's a whole angle they never touched.

[SHOW: Claude's response with concrete suggestions.]

> Now I'm not just copying what works — I'm improving on it. I know the structure that performs, AND I know where the gaps are.
>
> This conversation takes maybe five minutes. And it completely changes how I approach the video.

[NOTE: This is the "aha" moment — transcribe isn't just about getting text, it's about having an intelligent conversation about content strategy. Show real back-and-forth. Let the viewer see the thinking process.]

> So now I've got the data from my YouTube search, I've studied the top performers, and I've mapped out how to do it better.
>
> Time to plan the video.


---

## [7:30 - 11:00] Skill 3: /yt (The Big One)

> Skill number three. This is the one that ties it all together.
>
> Slash yt. This skill takes a video concept and turns it into a complete video package.

[SHOW: Terminal. Type `/yt` followed by the video concept for THIS video.]

> I give it the topic, the angle, the target audience. And it goes to work.
>
> First, it does its own web research. It searches for the latest info on the topic, competitor landscape, community sentiment.

[SHOW: Watch the web searches happening in the terminal.]

> Then it asks me a few questions. What's my angle? What demos am I showing? Who's watching?

[SHOW: The Q&A happening in the terminal. Show yourself answering the questions.]

> And then it generates everything.

[SHOW: Open the video package folder. Show the file list: titles.md, hooks.md, script.md, description.md, filming-guide.md, analysis.md]

> Titles. Five options with explanations for why each one works.

[SHOW: Open titles.md. Scroll through.]

> Hooks. Three options — each one is a word-for-word script I can read on camera, with different techniques labeled.

[SHOW: Open hooks.md. Show the first hook.]

> A full script. Organized by sections with time estimates, screen recording notes, and production cues.

[SHOW: Open script.md. Scroll through the section headers. Pause on a [SHOW:] marker.]

> A YouTube description with chapters. A filming guide that tells me exactly what to click, what to type, and what to say at every step.

[SHOW: Quick flash of description.md and filming-guide.md.]

> This is the script you're hearing right now. This is the filming guide I followed to record this. This video is the output.

[SHOW: Side-by-side — the script.md file on one side, you on camera on the other. The viewer sees the line you're reading matches the file.]

[NOTE: THIS is the climax of the video. The meta reveal. Pause for a beat after "This video is the output." Let it land. The side-by-side is the money shot.]

> And the whole thing — from slash yt-search to a finished script — took me maybe 15 minutes. For a complete video package that would normally take me half a day.
>
> But we're not done yet. There's one more skill.

---

## [11:00 - 13:00] Skill 4: /thumbnail

> Every video needs a thumbnail. And if you're like me, you've spent way too long in Canva or Photoshop trying to get something that looks good.
>
> So I built a skill for that too. Slash thumbnail.

[SHOW: Terminal. Type `/thumbnail` followed by a concept for this video.]

> It uses the Kie.ai API to generate thumbnail options. I give it a concept — like "person at a terminal with code reflections on their face, dark room, cinematic lighting" — and it generates multiple variants.

[SHOW: The script running — creating task, polling, downloading.]

> And here's what I get back.

[SHOW: Open `~/content/youtube/thumbnails/` folder. Show the generated thumbnail images side by side.]

> Three different thumbnail concepts. Different compositions, different moods. All in about 30 seconds each.
>
> And if I like one of them but want to tweak it — say, change the color grading or add a split screen effect — I can remix it.

[SHOW: Run a remix — pass a generated thumbnail back as a reference image with a new prompt. Show the result.]

> It takes the image I already generated, uploads it, and uses it as a reference to create a new version. Same vibe, different direction.
>
> The thumbnail you clicked on to get to this video? Made with this skill.

[NOTE: Quick beat here. Let the meta moment land again — first the script, now the thumbnail. The viewer is seeing the full system come together.]

> And just like the other skills — it's one command. No Photoshop. No Canva. No stock photo sites.

---

## [13:00 - 14:00] The Full Pipeline

> So let me zoom out. Here's the full pipeline.
>
> Step one. Slash yt-search. Find out what's on YouTube. What's getting views. What's missing.
>
> Step two. Slash transcribe. Pull the transcripts from top performers. Study their hooks, structure, and delivery.
>
> Step three. Slash yt. Take everything I've learned and generate a complete video package — titles, hooks, script, filming guide.
>
> Step four. Slash thumbnail. Generate thumbnail options and remix until you've got something you're happy with.
>
> Four commands. Research, deep analysis, a finished plan, and a thumbnail. All from the terminal.

[SHOW: Simple graphic or text overlay showing the four steps as a pipeline: /yt-search → /transcribe → /yt → /thumbnail. Or show the four output folders side by side.]

> And here's the thing — these skills aren't magic. They're just markdown files with instructions. Any of you can build these.
>
> If you want to see how I actually built these skills from scratch, I have a whole video on that. Link is in the description.

[SHOW: Quick flash of the skills video thumbnail or title card.]

[NOTE: This is the bridge to your existing content. Quick plug, don't linger.]

---

## [14:00 - 15:30] Why This Matters

> I want to be real about something.
>
> Most of the Claude Code content out there right now is about coding. Building apps. Shipping features. And that's great — Claude Code is incredible for that.
>
> But the thing people are sleeping on is that Claude Code is a general-purpose automation tool. It can do anything you can describe in plain English.
>
> I'm a content creator. My workflow is research, planning, writing, and producing. And Claude Code handles all of it.
>
> If you're a creator and you're not using this — you're leaving hours on the table every single week.
>
> And the beautiful thing is, every skill I build makes the next video faster. The system compounds. I'm not starting from scratch anymore. I'm building on top of a workflow that gets better over time.

[SHOW: Quick view of the `~/.claude/skills/` folder showing all the skills accumulated. The visual of 10+ skill folders drives the point home.]

[NOTE: This is the "why should I care" section. Keep it genuine. You're not selling — you're explaining why this changed your process.]

---

## [15:30 - 16:00] CTA + Wrap

> So that's it. Four skills. One pipeline. Every video I make starts here.
>
> If you want to build your own skills, check out my skills video — I'll link it up here and in the description.
>
> And if you want to see the actual skill files I used in this video, I'll drop those in the description too.
>
> If this was useful, subscribe. I make stuff like this every week.
>
> Thanks for watching. I'll see you in the next one.

[SHOW: End screen with subscribe button and link to skills video. Quick montage callback — terminal running /yt-search, /transcribe, /yt, /thumbnail — same energy as the opening.]

[NOTE: Keep the CTA tight. 30 seconds max. End on energy.]
