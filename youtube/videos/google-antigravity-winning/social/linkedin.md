# LinkedIn - Google is Winning With Antigravity

**Video:** https://www.youtube.com/watch?v=B5eDktBzXMg
**Best time:** Tue-Thu 10-11 AM ET.
**Cadence:** 3 angles, spaced 3-5 days apart. Do not post them back to back.

**CTA ladder:** one ask per post, escalating. Video, then pure value, then the community.

| # | Angle | CTA | Placement |
|---|---|---|---|
| 1 | The story (did not expect this from Google) | YouTube video | first comment |
| 2 | The tactic (the file you write before the prompt) | none (pure value, max reach) | n/a |
| 3 | The honest take (setup cost, wrong turns, limits) | Skool via funnel link | soft, end of post |

Note: the skills repo is NOT the CTA here. This video is about Google Antigravity, and Claude does not appear in it. Pointing at Tyler's Claude skills would contradict the post and would not pay off what it promised. Post 2 runs link-free instead, which also maximizes reach.

---

## POST 1 - The story

I did not think a Google tool would be the thing I recommended this month.

But I built a full agentic workflow in Google Antigravity, and it changed how I think about this kind of build.

Here is what the before looked like for me.

For years, if I wanted a system that pulled data, evaluated it, and dropped it somewhere useful, I had two options. Wire it up node by node in a no-code tool, or write the scripts myself.

Both work. Both take a day, and both break in ways you sit and debug.

So here is what I did instead.

I opened a folder in Antigravity and added one markdown file. That file has no code in it. It just describes how the project should be built. What the goal is, what runs in what order, and what to do when something errors.

Then I typed one line. Instantiate based on the agents markdown file.

The planning is the part that got me. Before it touched anything, it laid out the whole build. Which APIs it needed, which scripts it would write, how it would verify each piece. I could read its thinking the whole way through.

The goal I gave it was concrete. Pull videos from a list of YouTube channels, score them, and save a summary into a Google Sheet. It wrote every script for that.

Setup was not zero effort. I still had to enable the YouTube Data and Sheets APIs in Google Cloud, create a service account, and put the credentials in the project. That is usually where people quit, and it walked me through each step.

Then I ran it, and it broke on a Google Sheet permission partway through.

Instead of a wall of red text, it told me exactly what was wrong. The sheet had not been shared with the service account. I shared it, ran it again, and it finished.

Real videos pulled, scored, and summarized into a Sheet, and I did not write a line of the code.

I went in expecting to be unimpressed, and I came out the other side.

If you could hand a system one outcome and let it work out the steps, what would you have it do first?

> Link in first comment: https://www.youtube.com/watch?v=B5eDktBzXMg

---

## POST 2 - The tactic (no link)

I think most people are working on the wrong half of this.

Everyone is trying to write a better prompt. The bigger lever is the file you write before the prompt.

Here is what I mean.

When I had AI build me a working system last week, my actual request was one sentence long. What came back was a whole project. A plan, the scripts, the checks, all of it.

That sentence was not doing the work. A markdown file sitting in the folder was.

That file has three things in it, and none of them are code.

First, the goal. What this project is for, in plain English, the way I would explain it to somebody new.

Second, the order. What runs first, what depends on what, and where the outputs are supposed to go.

Third, what to do when something breaks. Diagnose it, tell me plainly what is wrong, do not just stop and wait.

That is the whole file. About a page of text.

The reason it works is not complicated. It is the same reason a good brief works with a person. Vague instructions plus a capable worker still gets you a guess.

And you write it once. Every request after that inherits it, so the next thing I ask for is already shaped the way I want it.

Most of the time when AI output disappoints me, I was not unclear about the task. I was silent about the standards.

If you already write things down for the people you work with, you are most of the way there.

What is the one rule about how your work gets done that you would put in that file first?

---

## POST 3 - The honest take (soft link)

Everyone wants an argument about which AI company is winning. I do not think that is a useful question.

So here is the honest version from actually using one of these things for a real build.

I made an agentic workflow in Google Antigravity. Goal in, working system out. It planned the build, wrote all the scripts, and I never touched the code.

That part genuinely impressed me, and I did not expect it to.

Now the limits, because there always are some.

Setup was not zero. Google Cloud, enable two APIs, create a service account, drop the credentials in the right place. If you have never done that, it is an hour and a couple of wrong turns.

It also made a choice I would not have made. It reached for an API key when there was a simpler library that would have skipped half of that setup. It did not think to ask me, and if I had not known better, I would have just followed along.

And it broke. A sheet had not been shared with the service account, so it stopped.

To its credit, it told me exactly what was wrong in plain language instead of dumping an error at me, and I fixed it in about a minute.

That is the realistic picture. Not magic, not useless. Something like a strong junior who plans well, explains itself, and occasionally takes a longer route than it needed to.

Which is completely fine, as long as you know that going in.

The part I would push back on is picking a team. These are tools. Not every tool fits every job, and that matters a lot more when you are building something for a client than when you are playing on your own time.

Use the one that fits the thing in front of you.

What have you tried recently that surprised you, in either direction?

I put the setup and the exact steps in my free community if you want them:

https://free.tylerai.dev/youtube/
