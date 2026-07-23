# YouTube Description: I Built an AI Video Editor With Claude Code (And Edited This Video With It)

---

Everyone is making the same video right now - "AI replaced my video editor." So I did something different. I used Claude Code to build my own AI video editor, and then I edited a real clip with it on camera. I did not just use a tool. I built one, and in this video I show you exactly how it works, run it live, and tell you honestly what is mine and what is just good open-source tools doing the heavy lifting.

Here is the honest version up front, because that matters to me. I did not build a video editor from scratch. I stood on top of three open-source tools - Hyperframes (HeyGen's open-source framework), ffmpeg, and Whisper - and I used Claude Code to wire them into two commands that kill the two parts of editing I hate most. One command cuts the dead air. A real 3 minute clip became 1 minute 50, with 71 seconds of silence removed, in about 2 seconds. The other command drops on karaoke word-by-word captions in one shot, in three styles - bold, tiktok, and clean.

I am a software engineer by day at a Fortune 500 company, and outside of that I run a YouTube channel and a free community about AI tools. This is the kind of thing I actually build for myself, and the whole point of this video is that you could build it too - every piece is open-source and free.

One genuinely useful thing you will learn: if you ever want to find silence in audio, do NOT use Whisper transcription timestamps. Whisper stretches words across the pauses, so the silence disappears. Use ffmpeg's silencedetect instead - it measures actual audio energy and finds the real gaps. That one insight is the difference between cuts that work and cuts that are garbage.

What this video covers:
- Why cutting dead air and adding captions is the most tedious part of editing
- How I built two commands on open-source tools with Claude Code
- LIVE demo: cutting 71 seconds of dead air from a real clip in 2 seconds
- Why Whisper timestamps fail for silence detection and what to use instead
- LIVE demo: three karaoke caption styles in one command
- The full raw-clip-to-finished workflow, end to end
- The honest limitations - what AI editing can and cannot do
- The recipe to build your own with Claude Code

CHAPTERS
0:00 - The clip you just watched was AI-edited (cold open)
0:30 - Why dead air and captions are the worst part of editing
2:00 - What I actually built (and what is open-source)
4:00 - LIVE: cutting 71 seconds of dead air in 2 seconds
7:30 - LIVE: three karaoke caption styles in one command
10:30 - The full workflow, end to end
12:00 - The honest limitations
13:30 - Build your own + free community

(Run /chapters on the final cut to true these up to the edited timestamps.)

The tools I built on are all open-source and free - Hyperframes, ffmpeg, and Whisper. I dropped the exact Claude Code prompts I used and the command outlines in my free community so you can build your own:
https://www.skool.com/the-ai-agency

[CTA NOTE for Tyler: this description is written for option (c) - teach the approach, soft Skool CTA. If you decide to open-source the repo (option a), add the repo link here. If you make it a Skool lead magnet (option b), make the Skool line the primary CTA. See analysis.md for the full decision.]

---

## SEO-Optimized Version (2026-07-22 — post-edit, matches the final cut + real chapters)

> ⚠️ **This is the version to upload.** The description above was written pre-edit to the old "I built it" framing. This one matches the actual 14:40 cut (HyperFrames tutorial) and uses the honest workflow framing. Chapters below are trued to the final timestamps.

Here's how I edit my videos with AI now - captions, silence cuts, and animations - all by talking to Claude Code. Everything I use is open-source and free: HeyGen's HyperFrames plus Claude Code.

I'm not a video editor and I didn't build a tool. HyperFrames is HeyGen's free, open-source video framework, and it installs a set of Claude Code skills you drive with plain language. In this video I run the whole thing on real clips: add word-by-word captions from a catalog of styles (pill karaoke, matrix, kinetic slam, neon), cut the dead air out of a 3 minute clip so it drops to under 2 minutes, add transitions and B-roll, and animate a screenshot into an intro - all by asking Claude Code.

I'm honest about it too. This is not one-click magic. The slick final versions you see online took real back-and-forth to get right. But once your styles are dialed in, it's faster and cheaper than the caption apps and silence removers I've paid for.

CHAPTERS
0:00 - Edit Your Videos With AI
0:40 - Installing the HyperFrames Skills
2:00 - Adding Captions to a Clip
4:00 - Browsing the Style Catalog
5:10 - Why It Takes Real Conversation
5:44 - Beyond Captions: Animations & Data
7:33 - Cutting Out the Dead Air
9:00 - Adding Transitions & B-roll
10:05 - Compared to SubMagic
10:40 - Inside HyperFrames Studio
11:56 - Animating Screenshots
14:11 - Try It Yourself + Community

Try it yourself - HyperFrames is on HeyGen's GitHub, free to install. I teach the full setup and drop the exact prompts in my free community:
https://www.skool.com/the-ai-agency
