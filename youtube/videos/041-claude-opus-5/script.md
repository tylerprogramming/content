# Script: Claude Opus 5 (is it really better?)

**Date:** 2026-07-24 (launch day)
**Target length:** 10-12 minutes.
**Audience:** People who use Claude Code every day to build and automate real work and want an honest answer on whether the new model is better and worth switching to.
**Style:** Honest hands-on test. Tyler has been using Opus 5 on his real work and nothing broke. The internet split into a hype camp ("cheaper Fable, save money") and a doubter camp ("hard to love, breaks your skills"), and neither matched his experience. So the video actually answers: is it better, and is it worth it. Two real head-to-head builds against Fable, cost shown honestly. NOT a benchmark recap.

> **Honest framing (non-negotiable):** This is about USING Claude on real work, not being an AI-news channel. No hype words (insane, crazy, game-changer, mind-blowing). No em dashes. Tyler hedges and admits limits. Nothing is staged to fail. The honesty is that it works.

> **Accuracy note (say a version of this on camera):** Opus 5 launched today. The model id looks like `claude-opus-5`, but verify the exact string in Anthropic's docs on camera before quoting it. Prices: Opus 5 is $5 in / $25 out per million tokens, Fable 5 is $10 / $50. Opus 5 is the same price as Opus 4.8, so it is a free upgrade for existing users.

> **Filming note:** The Design-to-code opener is pre-recorded. Both head-to-head builds are pre-run ahead of time with clean backup takes captured (models are non-deterministic). Everything marked [BUILD] plays a real screen recording. See filming-guide.md for exact prompts.

---

## [0:00 - 0:30] Cold Open (Hook 1)

[COLD OPEN - talking head, word for word from teleprompter.]

Claude Opus 5 is out, and the real question is whether it is as good as Fable for half the price. I have been using it on my actual work, and honestly, I think it mostly is a cheaper Fable. A few people said it breaks your skills. That did not happen for me. So instead of just telling you, I am going to build a few real things with it, put it side by side with Fable, show you what each one costs, and let you judge for yourself. Let's get into it.

[SHOW: quick 2-second flash of the two split-screen builds coming up, as a teaser. Do not explain them yet.]

---

## [0:30 - 1:30] What Launched and What It Costs

So let me catch you up fast, because I know a hundred people already posted the benchmarks today and I am not going to waste your time re-reading them.

[SHOW: Anthropic's Opus 5 announcement page, scroll it briefly. The benchmark charts are here if you want a two-second glance.]

Anthropic put out Claude Opus 5 today. Two things actually matter for people like us who use this every day. First, the price. Opus 5 is five dollars per million tokens in, twenty-five out. Fable 5, their top model, is double that, ten and fifty. And here is the part that got everyone excited, Opus 5 is the same price as Opus 4.8, the model a lot of us were already on. So if you are already using Claude Code, this is kind of a free upgrade. You are not paying more, you are just getting the newer model.

[SHOW: OpenRouter's Opus 5 page with the clean pricing table, Opus 5 $5/$25 next to Fable $10/$50.]

[NOTE: on screen, put a small clean table: Opus 5 $5/$25, Fable 5 $10/$50, Opus 4.8 same as Opus 5.]

Second, they are positioning Opus 5 as the new default. Not the ceiling, the everyday driver. They say it is designed to be used every day, it approaches Fable's quality in a lot of categories at half the price, and it verifies its own work as it goes. It has a million token context, and there is an effort toggle you can set low, medium, high, and an extra-high above that. Hold onto that toggle, we will come back to it near the end, because it is how you control what this thing costs you.

[NOTE: verify the exact model id string on camera before showing any code. Say so out loud.]

---

## [1:30 - 2:30] The Honest Part: What the Doubters Said vs What I Saw

Now here is where I want to be straight with you, because there are two loud takes out there and I do not fully agree with either one.

One camp is running the benchmarks and saying Opus 5 is just a cheaper Fable, so cancel the expensive one and save your money.

[SHOW: brief receipt for the hype camp - the two videos on screen: "Opus 5 Just Dropped and Its Numbers Are Legit INSANE" (58.9K) and "Claude Opus 5 is Going to Save You Money" (20.1K). Title cards only, attributed.]

The other camp actually used it for a week and came back saying it is a hard model to love. That it stops early, that it argues with you, that it breaks your big skill files.

[SHOW: the receipt for the doubter camp - the "We Tested Claude Opus 5" video (17.7K), title/thumbnail on screen, with these real quote overlays pulled from it: "a hard model to love," "it stops, it argues with you," "it consistently stopped too early... it would say it was done, but it wasn't done," "breaks your existing workflows," "a poor man's Fable." Brief and attributed - this is the proof, not just my paraphrase.]

And when I read that, I will be honest, it made me a little nervous, because I had already switched my daily work over to it the day it came out.

So I paid attention. I ran the skills I use every day, the automations that quietly run my channel, the ones with big detailed instruction files that are supposed to be the ones that break.

[SHOW: Tyler's real folder of skills / automations, so the viewer sees these are real things he uses.]

And none of that happened for me. It did not stop early. It did not argue. My skills just ran, the same way they always have.

[SHOW: a real skill running clean on Opus 5, all the way to a finished result. Let the viewer see it complete.]

So I am not going to tell you the doubters are lying, they had their experience and I had mine. I am just telling you what actually happened on my machine, on my real work. It worked. So the more interesting question to me is not "does it break." It is "is it actually better, and do I still need to pay double for Fable." So let me go build some real things and find out.

---

## [2:30 - 3:30] Opener: Design to Working Code

[SHOW: pre-recorded screen recording, single Opus 5, effort medium.]

Let me start with something small, just to show you the feel of it.

I took a screenshot of a design, a plain picture of a landing page layout, and I dropped it into Claude on Opus 5 and asked it to build me the working front end. That is it. No detailed spec, just the image.

[SHOW: drop the design screenshot into the prompt so the viewer sees the input.]

And watch what comes back. It reads the layout, it writes the markup and the styling, and it gives me clean, working code.

[SHOW: the rendered result next to the original design screenshot, side by side. Let the match land.]

That is the thing that surprised me most in the first hour. It just works. Design in, working code out, no fighting it. That is a good sign for everything I am about to try next. Now let me make it earn it with a real build.

---

## [3:30 - 6:30] Head-to-Head #1: Build a Landing Page, Opus 5 vs Fable (the cost story)

[BUILD - same brief given to both models, split screen. See filming-guide.md for the exact brief. Pre-run with backup takes.]

Okay, first real head-to-head. I am going to give the exact same brief to Opus 5 and to Fable 5, at the same time, and build an actual landing page. Same words, same everything, only the model is different.

[SHOW: paste the brief so the viewer can read it. Then kick off both, split screen, Opus 5 on the left, Fable on the right.]

So both are going now. Let me talk you through what I am watching while they build.

[NOTE: dead air narration while both run. Talk through: what each one is scaffolding, the structure it chose, how fast each is moving, whether either is asking questions. Keep it honest and specific to what is on screen.]

Opus 5 is moving, it laid out the sections, it is styling as it goes. Fable is doing basically the same thing on its side, maybe a hair more thorough in the copy it is writing. Neither one is stuck. Neither one is arguing with me, which, again, is the thing I was told to expect and did not get.

[SHOW: both finished landing pages rendered, side by side.]

And here are the two results. Honestly? Look at them. If I hid the labels from you, I would have a hard time telling you which one came from the expensive model. They are both clean. They are both something I would actually ship. Maybe you have a slight preference for one, but this is close.

Now here is the part that matters, and this is the honest version of the "save you money" take.

[SHOW: the two token counts and costs side by side. Do the multiplication on screen.]

Let me show you what each one cost. Opus 5, at five in and twenty-five out per million tokens, this build came to [X]. Fable 5, at ten and fifty, the same build, same result, came to [X], right around double.

[NOTE: fill in the real token counts and dollar figures from the actual runs. Do the math on camera. Keep it honest, whatever it actually was.]

So for a job where I genuinely cannot tell the outputs apart, one of them costs about twice as much. If you are building landing pages, marketing sites, everyday front-end work, this is the whole argument right here. You may not need the expensive one for this. That part of the hype, it turns out, is real.

---

## [6:30 - 9:30] Head-to-Head #2: Build a Browser Game, Opus 5 vs Fable (the quality story)

[BUILD - same spec given to both models, split screen. The harder build. See filming-guide.md for the exact spec. Pre-run with backup takes.]

Okay but a landing page is not that hard. So let me make them actually work for it.

I saw a little vibe-coded browser game going around, one of those physics merge games, you drop things and matching ones combine and it all bounces around. That is a real test. There is physics, there is state, there is the question of whether the thing even runs and whether it feels good to play. Polish shows up here in a way it does not on a landing page.

So, same deal. Same spec to both models, side by side.

[SHOW: paste the game spec so the viewer can read it. Kick off both, split screen.]

[NOTE: dead air narration while both build. This one takes longer. Talk through: the physics approach each one takes, how each handles collisions and merging, whether either gets stuck, whether they self-check their work. This is the segment to slow down and actually watch.]

This one is more interesting to watch. Opus 5 is building out the physics loop, it is handling the merge logic. Fable is doing its thing on the other side. Both of them are actually reasoning about whether the game will run, which is that self-verification thing Anthropic talked about, and I did see it here on both.

[SHOW: both finished games, actually play each one on camera. Drop pieces, let them merge, let them bounce.]

Alright, moment of truth, let me play both.

[NOTE: play them honestly. Two honest outcomes, pick whichever is true on the day:]

[OUTCOME A - they tie:] And, okay. They both run. They both feel fine. I can drop pieces, they merge, the physics feel right on both. If this is what I got, then even on the hard build, Fable's premium is not buying me anything I can feel. Which is kind of remarkable.

[OUTCOME B - Fable is a bit cleaner:] And here is where I will be honest with you. They both run, but Fable's feels a little more polished. The physics are a touch smoother, this edge case here is handled better. It is not night and day, but I can feel it. So this is the one place where the expensive model still earns its price. If your work is the genuinely hard, needs-to-feel-perfect stuff, that top end is still worth something.

[NOTE: whichever outcome is real, show the cost side by side again. Fable ~2x. If they tied, the cost gap is the punchline. If Fable was cleaner, the cost gap is the honest tradeoff.]

Either way, look at what it cost to find that out.

[SHOW: token counts and cost for both, side by side again.]

So that is the quality question answered honestly. On the everyday stuff, Opus 5 is right there for half the money. On the hardest, feel-it-in-your-hands stuff, Fable might still have a small edge. That is the real picture, not the hype picture and not the doubter picture.

---

## [9:30 - 10:30] The Effort Toggle: How to Control Cost and Quality

Before I give you my verdict, one practical thing, because this is the lever nobody hands you a manual for.

[SHOW: the effort setting, low / medium / high / extra-high. Change it on camera so the viewer sees where it lives.]

Remember that effort toggle from earlier. This is how you actually get the most out of Opus 5. Think of it as a dial between speed and cost on one end and deeper reasoning on the other.

For most everyday work, the landing page, running a normal skill, medium is plenty and it keeps your cost down. When the job is genuinely harder, the game, a tricky build, something long, you turn it up and let it think more. And if you ever feel like it is over-thinking a simple job, you drop it down and it gets faster and cheaper.

[NOTE: on screen, one clean line: "Effort is your dial. Turn it down to save, turn it up for the hard stuff."]

So you are not stuck with one setting. The effort toggle is how you tune Opus 5 to the job in front of you, and it is a big part of why the cost can come out so much lower than Fable. Use it.

---

## [10:30 - 12:00] Honest Verdict + CTA

So let me actually answer the question from the title. Is Opus 5 really better, and is it worth switching?

[SHOW: a simple two-column "use Opus 5 when / use Fable when" on screen.]

Here is where I landed after building real things with it.

Opus 5 mostly is a cheaper Fable. And I mean that as a good thing. On everyday work, the landing page, the skills I run, most of what I do, I honestly cannot tell it apart from Fable, and it costs me about half as much.

It is also the same price as Opus 4.8, the model I was already using. So for me this was a free upgrade. I switched. If you are on Claude Code today, update it and switch too. There is basically no reason not to.

So for everyday building, you probably do not need to pay double for Fable anymore. That is the real shift. For most of what you actually do, the cheaper one is right there.

But I am not deleting Fable. For the absolute hardest jobs, the long-horizon stuff, the builds that run for a long time and need to feel perfect, Fable still has a slightly higher ceiling. So I keep it around for the heavy stuff and reach for Opus 5 for everything else.

And I want to be fair to both camps I mentioned at the start. The hype camp saying "just save your money," they are mostly right for everyday work. The doubter camp saying "it breaks your skills," that did not happen for me, but they used it their way and I used it mine, so I will just tell you my honest result. It worked. We will all know more in a couple of weeks as people learn it, and I will tell you if my take changes.

[NOTE: do not overclaim. The honesty is the value.]

So here is what I would actually do today. If you use Claude Code, update it, switch to Opus 5, and build the thing you were going to build anyway. Keep the effort on medium for normal work. See if it just works for you the way it did for me.

[SHOW: the two finished builds one more time, side by side.]

I put the exact brief and the game spec I used, plus my effort settings for different kinds of work, in my free community, so you can run the same head-to-head on your own machine without guessing. The link is in the description, it is free, come grab it, and come tell me how Opus 5 does on your builds, because I genuinely want to know if you are seeing what I am seeing.

And if this was useful, subscribe, because building real things with Claude instead of just reading the benchmarks is most of what I do here. I will see you in the next one.

[END]

---

## Timing Recap

| Section | Time | Format |
|---------|------|--------|
| Cold open (two-camp reframe) | 0:00-0:30 | Talking head + teaser flash |
| What launched and what it costs | 0:30-1:30 | Talking head + pricing tabs |
| The honest part (doubters vs what I saw) | 1:30-2:30 | Talking head + real skill running clean |
| Opener: design to working code | 2:30-3:30 | **Pre-recorded build** |
| Head-to-head #1: landing page + cost | 3:30-6:30 | **BUILD split screen** |
| Head-to-head #2: browser game + quality | 6:30-9:30 | **BUILD split screen** |
| The effort toggle | 9:30-10:30 | Talking head + toggle on screen |
| Honest verdict + CTA | 10:30-12:00 | Talking head + two-column graphic |

**Total: ~11-12:00.** The two head-to-head builds are the spine. #1 is the cost story, #2 is the quality story. Protect both. If you need to trim, tighten "what launched" and the verdict, never the builds. Nothing is staged to fail anywhere in this script.
