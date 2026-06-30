# Script: I Built an AI Video Editor With Claude Code (And Edited This Video With It)

**Date:** 2026-06-19
**Target length:** 12-15 minutes (~2,000-2,300 words spoken). Aim short - this lane rewards tight and fast.
**Audience:** Creators and AI-curious builders who hate editing dead air and captions, and who want to see Claude Code build a real tool.
**Style:** Honest build-and-demo. Show the result first, reveal the build, run two live demos, be honest about limits, point to the open-source pieces.
**Honest-framing rule (non-negotiable):** Built ON open-source Hyperframes (Apache-2.0) plus ffmpeg plus Whisper. Tyler added the silence-cutting layer and the one-command caption flow with Claude Code. NEVER imply built from scratch.

> Filming note: the two DEMO sections are LIVE and must be captured as real screen recordings of the commands running. Everything marked [LIVE DEMO] is real, on camera, no fakes. See filming-guide.md.

---

## COLD OPEN (0:00 - 0:30) ~110 words

### [WORD FOR WORD - First 25 seconds]

[COLD OPEN - no talking. On screen: a raw talking-head clip plays for 2-3 seconds, full of awkward pauses and dead air. Hard cut to the SAME clip, tight, no dead air, with bold karaoke captions popping word by word. Let it play 4-5 seconds.]

[Tyler, to camera] That clip you just watched? The before was three minutes. The after was one minute and fifty seconds. I did not touch a timeline. I did not drag a single clip. I ran one command, and the dead air was gone. Then I ran one more, and the captions were on. And here is the part nobody else can say - I built the thing that did that. I built my own AI video editor with Claude Code. In the next ten minutes I am going to show you exactly how it works, edit a real clip with it live, and tell you honestly what is mine and what is just good open-source tools doing the heavy lifting. Let's get into it.

### [Resume natural delivery]

[NOTE: keep the cold open punchy. Do not explain the build yet. The reveal is enough. The "how" comes after the problem.]

---

## THE PROBLEM (0:30 - 2:00) ~270 words

Let me tell you why I built this, because if you make videos you already feel it.

There are two parts of editing that I genuinely hate. The first is cutting dead air. You film a talking-head clip, and between every sentence there is a pause. A little silence while you think. An um. A breath. And when you stack all those pauses up across a ten-minute video, it is minutes of dead time that makes the whole thing drag. So you sit in your editor, and you cut, and you cut, and you cut. It is the most tedious thing in the world and it takes forever.

The second is captions. Word-by-word captions are not optional anymore. They are how people watch. But adding them by hand, or even cleaning up auto-captions, is slow and fiddly.

Here is the thing. Both of those jobs are completely mechanical. There is no creativity in finding a silent gap. There is no artistry in syncing a word to the audio. A computer should do that. And the rest of editing - pacing the story, picking what matters, choosing b-roll, the music - that is the creative part, and AI is genuinely bad at it. I am not going to pretend otherwise.

So I did not try to build a tool that replaces my editing. I built a tool that does just the boring, mechanical parts. Cut the dead air. Drop on the captions. Two commands. And the best part is I did not build it from scratch, which is exactly what I want to show you next, because it means you could build the same thing.

---

## WHAT I DID - THE BUILD (2:00 - 4:00) ~300 words

Here is the honest version of what this tool is, because the honesty is the whole point.

I did not write a video editor from scratch. That would take months and I would do a worse job than tools that already exist. Instead, I stood on top of three open-source pieces and used Claude Code to wire them together.

[SHOW: a simple diagram or three logos - Hyperframes, ffmpeg, Whisper]

The first piece is Hyperframes. It is HeyGen's open-source video framework, Apache-2.0 licensed, which means it is free to build on. Hyperframes renders video from code. It is genuinely great at putting things like captions onto a video.

The second is ffmpeg. If you do anything with video on a command line, you know ffmpeg. It is the open-source swiss army knife of video. It can analyze audio and it can cut video.

The third is Whisper. That is the open-source speech-to-text model. It turns audio into text, which is what you need for captions.

So those three tools do the heavy lifting. What did I actually add? Two things.

[SHOW: terminal, the repo]

I forked Hyperframes into my own repo and I used Claude Code to build two new commands on top of it. The first is a silence command, because Hyperframes deliberately took footage editing out, so cutting dead air was the gap I needed to fill. The second is a one-command caption flow that takes a clip, transcribes it, and renders captions in one shot.

That is it. That is the honest scope. Three open-source tools doing the work, Claude Code wiring them into two commands that kill the two parts of editing I hate. Now let me show you both of them running on a real clip. This is all live.

---

## DEMO 1 - SILENCE CUT (4:00 - 7:30) ~520 words

### [LIVE DEMO - real screen recording, real command, no fakes]

[SHOW: terminal open, a raw clip file visible. Say what the clip is first.]

Okay, here is a real clip. This is a three-minute talking-head clip I recorded, and like all my raw footage it is full of pauses. Let me play you five seconds of it so you hear the dead air.

[SHOW: play 5 seconds of the raw clip - the pauses should be obvious]

You hear that? Those gaps. That is what I have to cut out by hand normally. Watch what one command does.

[LIVE DEMO: type the command on camera]

```
hyperframes silence raw-clip.mp4
```

[SHOW: the command running. It finishes in about 2 seconds.]

Two seconds. That is not sped up. Let me show you the result.

[SHOW: play 5 seconds of the cut clip - tight, no gaps]

Three minutes went to one minute and fifty seconds. It cut seventy-one seconds of dead air. That is thirty-nine percent of the clip, gone, and it was all silence. Nothing I actually said got touched.

Now I want to show you how it does that, because there is a genuinely useful lesson in here, and it is the kind of thing that took me a few tries to get right with Claude Code.

[SHOW: open the code, or a simple explainer graphic]

My first instinct - and probably yours - was to use Whisper for this. Whisper transcribes the audio and it gives you a timestamp for every word. So I thought, easy, find the gaps between words, those are the silences, cut them.

That does not work. And here is why, because this is the useful part. Whisper's word timestamps are unreliable for finding silence. It stretches words across the pauses. So if you say "hello" and then pause for two seconds and say "world," Whisper will often timestamp the word "hello" as lasting that whole gap. The silence disappears inside the word. So when you look for gaps between words, there are none. The pauses are invisible. I tried it, the cuts were wrong, and it took me a minute to figure out why.

[SHOW: the silencedetect approach]

The thing that actually works is ffmpeg, specifically a filter called silencedetect. Instead of looking at words, it looks at actual audio energy. It measures how loud the audio is, moment to moment, and it flags the stretches where the volume drops below a threshold for long enough. That is real silence, measured directly from the sound, not guessed from a transcript. So the pipeline is - ffmpeg silencedetect finds the real silent gaps, and then ffmpeg cuts them out and stitches the clip back together. That is why it is accurate, and that is why it is fast.

So the lesson, if you take one technical thing from this video - if you ever want to find silence in audio, do not use transcription timestamps. Use audio energy. Use ffmpeg silencedetect. I learned that building this with Claude Code, and it is the difference between cuts that work and cuts that are garbage.

[NOTE: keep energy up coming out of the technical beat - it is the deepest part of the video, pull back up before Demo 2.]

---

## DEMO 2 - CAPTIONS (7:30 - 10:30) ~470 words

### [LIVE DEMO - real screen recording, real command, no fakes]

Okay, dead air is gone. Now the second job - captions. This is the second command, and it does everything in one shot.

[LIVE DEMO: type the command on camera]

```
hyperframes caption cut-clip.mp4 --style bold
```

Here is what that one command does under the hood. It takes the clip I just cut, it runs Whisper on it to transcribe what I said, it groups the words into little caption chunks, and then it uses Hyperframes to render those captions onto the video, synced word by word - that karaoke effect where each word pops as you say it. One command, all of it.

[SHOW: the command running, then play the captioned result]

There it is. Bold captions, synced to my voice. And notice I used Whisper here, for transcription, which is exactly what Whisper is good at. That is the lesson from the last section in action - Whisper for words, ffmpeg for silence. Right tool for each job.

Now the fun part. I built three caption styles, because different platforms want different looks. Let me show you all three on the same clip.

[SHOW: switch styles, show each]

Style one is bold. [SHOW] That is the Oswald font, white text with a yellow highlight on the active word. This is my default for YouTube - big, readable, punchy.

```
hyperframes caption cut-clip.mp4 --style bold
```

Style two is tiktok. [SHOW] This is the look you have seen a thousand times on your for-you page - the word in a red pill that pops one at a time. Built for vertical, built for short-form.

```
hyperframes caption cut-clip.mp4 --style tiktok
```

Style three is clean. [SHOW] This one is a soft cream background, quieter, more grown-up. I use this for tutorial content where I do not want the captions screaming over the screen.

```
hyperframes caption cut-clip.mp4 --style clean
```

Same clip, three completely different looks, and switching between them is one word in the command. I am not editing each one by hand. I am picking a style and letting Hyperframes render it.

And again, to be clear, the rendering here is Hyperframes doing what Hyperframes is great at. What I added was wiring it into a single command so I do not have to think about the transcription step, the grouping step, and the rendering step separately. It is one command, clip in, captioned clip out.

---

## DEMO 3 - SHORTS (HeyGen short, captioned) (10:30 - 12:00) ~280 words

### [LIVE DEMO - real screen recording, real commands. See `shorts-demo.md` for exact commands.]

[SHOW: a vertical HeyGen short you made, no captions, ~5s]

One more, because this works on short-form too, and it is where most of you will use it. This is a short I made in HeyGen - an AI avatar, clean, but no captions. On a HeyGen short there is no dead air to cut, the avatar is already tight. So here the job is just the captions, and that is the part people pay caption apps for. Watch.

[LIVE DEMO: run the real preset flow - init transcribes with Whisper, extract_words, then the caption preset renders. Narrate each step.]

I point Hyperframes at the short, it transcribes what the avatar said with Whisper, and then I run one of my caption presets. Here is the fun part - I built three.

[SHOW: preview, captions popping word by word, then swap the 3 styles on the same short]

This first one is the TikTok look - red pill, the word pops as it is spoken. Same short, swap one filename, now it is the bold YouTube style, white and yellow. Swap again, the calm cream style for tutorials. Same short, three completely different caption looks, and I am not touching a timeline for any of it.

And to be honest about what is what - Hyperframes is the open-source engine doing the rendering. The caption presets are scripts I built on top with Claude Code. That is the exact pattern this whole video is about - take the open-source tools, wire them into commands that fit how you actually work.

[NOTE: this is the most relatable demo for the short-form crowd. Keep it fast. The 3-style swap is the wow beat - hit it hard.]

---

## THE FULL WORKFLOW (12:00 - 13:00) ~270 words

So let me put the whole thing together end to end, the way I actually use it, because that is where it gets satisfying.

[SHOW: the full sequence, sped up slightly, or as a clean recap]

I finish recording a talking-head clip. It is raw, it is full of pauses, it is three minutes long. Step one - I run the silence command.

```
hyperframes silence raw-clip.mp4
```

Two seconds later it is one minute fifty, no dead air. Step two - I run the caption command and pick my style.

```
hyperframes caption cut-clip.mp4 --style bold
```

A few seconds later the captions are on, synced word by word. And that is the whole thing. Two commands. The two parts of editing I hate most, the dead air and the captions, both done, in the time it takes to read this sentence.

[SHOW: before clip vs after clip side by side one more time]

And remember, the clip you saw at the very start of this video? That was this exact workflow. Raw clip, silence command, caption command, done. I edited part of this video with the tool I built, and I am showing you the proof.

This is the part I want you to feel. I am not faster at editing because I got better at dragging clips. I am faster because I built a tool that does the boring parts for me, and I built it with Claude Code on top of tools that already existed. That is the move. That is the whole video.

---

## HONEST LIMITATIONS (12:00 - 13:30) ~280 words

Now I promised you the honest version, so here it is. Here is what this tool is not, and where it falls apart.

First, the obvious one. This does not replace a video editor. It does the two mechanical chores. It does not pace your story. It does not decide what is worth keeping. It does not add b-roll, it does not pick music, it does not know which take is your best take. All the actual creative judgment of editing is still yours. So if you came here for "AI made my whole video," that is not this. Anybody selling you that is overselling.

Second, it is built on open-source tools, and I want to keep saying that because it is true. Hyperframes does the rendering. ffmpeg does the detection and the cutting. Whisper does the transcription. I added the silence layer and the one-command flow. If those tools did not exist, I could not have done this in an afternoon. Give them the credit.

Third, render speed. The silence cut is genuinely fast, about two seconds. But the caption render goes through Hyperframes, and rendering video takes longer than just cutting it. It is not instant. On a longer clip it is a coffee-break, not a blink. That is the honest tradeoff for getting nice rendered captions instead of ugly burned-in ones.

And fourth, it is a CLI tool I built for me. It is rough around the edges. It is not a polished product with a nice interface. It is two commands in a terminal. That is fine for me because I live in a terminal, but I am not going to pretend it is a consumer app.

That is the honest picture. Now, what about you.

---

## CTA (13:30 - 14:30) ~230 words

> CTA DECISION - this section is written for option (c): teach the approach, point to the open-source pieces, soft Skool CTA. If Tyler picks (a) open-source the repo, swap the marked paragraph for "the repo is open, link in the description, go use it." If Tyler picks (b) Skool lead magnet, make the Skool line the hard CTA. See analysis.md for the full decision.

So here is the thing I actually want you to take away.

You do not need my repo. The tool I built is a private fork right now, and honestly, the value was never the repo. The value is the approach, and the approach is completely reproducible, because every piece I used is open-source and free.

[SHOW: the three tools on screen again]

If you want to build your own, here is the recipe. Start with Hyperframes for rendering. Use ffmpeg's silencedetect for finding and cutting dead air - not Whisper timestamps, remember why. Use Whisper for the caption transcription. And then sit down with Claude Code and have it wire those three together into commands that fit how you work. That is genuinely an afternoon project, and you will understand your own editing better for having built it.

[SOFT SKOOL CTA] I dropped the exact prompts I used with Claude Code and the command outlines in my free community - the link is in the description. It is free, come grab them, and come tell me what you build.

If this was useful, subscribe, because building little tools like this with Claude Code is most of what I do here. I will see you in the next one.

[END]

---

## Timing Recap

| Section | Time | Words | Live? |
|---------|------|-------|-------|
| Cold open (result first) | 0:00-0:30 | ~110 | result clip is real |
| The problem | 0:30-2:00 | ~270 | |
| What I did - the build | 2:00-4:00 | ~300 | |
| DEMO 1 - silence cut + Whisper-vs-silencedetect | 4:00-7:30 | ~520 | **LIVE** |
| DEMO 2 - captions, 3 styles | 7:30-10:30 | ~470 | **LIVE** |
| The full workflow | 10:30-12:00 | ~270 | |
| Honest limitations | 12:00-13:30 | ~280 | |
| CTA | 13:30-14:30 | ~230 | |

**Total: ~14:30, ~2,450 spoken words.** Trim the problem and limitations sections first if you need to land closer to 12 minutes. The two live demos are the spine - protect them.
