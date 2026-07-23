# Skool - I Edit My Videos by Talking to Claude Code

**Video:** https://www.youtube.com/watch?v=cdvi2ooarDc
**Posted manually by Tyler** (Skool is not in Blotato).
**Cadence:** 3 posts, spaced 3-5 days apart. Goal on Skool is COMMENTS, not reach.

| # | Angle | CTA |
|---|---|---|
| 1 | The drop (video is up, what's in it) | video link |
| 2 | The tactic (try this today) | HyperFrames repo |
| 3 | The discussion (real question) | no link, pure engagement |

---

## POST 1 - The drop

I finally fixed the part of making videos I hate the most.

Not the creative part. The two mechanical chores: cutting out all the dead air between sentences, and adding word-by-word captions. I used to do both by hand and it took forever.

Now I just talk to Claude Code. I drop a raw clip into HyperFrames (HeyGen's open-source video tool), ask it to cut the silences, and a 3 minute clip drops to under 2. Then I copy a caption style and ask it to add them. If I want a different look, I ask for another one.

I'm not a video editor and I didn't build a tool. Everything here is open-source and free, HyperFrames plus Whisper plus ffmpeg, all driven by Claude Code. It's not one-click magic, it took some back and forth to dial in, but now it's cheaper and faster than the caption apps I was paying for.

I dropped the exact prompts and setup in here. Who else wants to stop doing this by hand?

https://www.youtube.com/watch?v=cdvi2ooarDc

---

## POST 2 - The tactic (try this today)

Here's something worth knowing whether or not you ever touch video.

I wanted to cut the silent gaps out of a clip automatically. The obvious approach is to use the transcript, look at the timestamps between words, and cut the space in between.

That does not work. I found out the slow way.

Whisper stretches words across the pauses when it transcribes, so the silence disappears inside the word timings. You end up cutting in the wrong places and the audio sounds chopped.

What actually works is measuring the loudness of the audio directly and cutting the quiet parts. ffmpeg does it in one pass.

I didn't figure that out on my own, Claude Code did the right thing under the hood and I went and read why afterward. But it's the difference between cuts that sound clean and cuts that sound broken.

The bigger lesson for me: when you automate something, go look at HOW it solved it. That's where the actual learning is. Otherwise you just have a black box that works until it doesn't.

HyperFrames is free and open source on HeyGen's GitHub if you want to poke at it.

What's something you automated and then went back to understand properly?

---

## POST 3 - The discussion (no link)

Question for you all, because I think the answer says a lot.

I spent a long time not automating my editing because I assumed the setup would cost more time than it saved. Classic trap. I did the boring version by hand for months instead.

When I finally sat down with it, the part I actually hated took about an evening to hand off. Not a weekend. An evening.

The thing I got wrong was estimating the setup cost from the outside. It looked bigger than it was, so I never started.

So here's my question.

What's the thing you keep doing manually because you assume automating it would take too long?

Be specific if you can. Post the actual task, not the category. I'll tell you honestly whether I think it's an evening or a real project, and if a few of you name the same thing I'll build it and share it in here.
