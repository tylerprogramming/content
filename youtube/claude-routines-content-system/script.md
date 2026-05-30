# Script: Claude Routines + Claude Code — The Real Automation Stack

**Target runtime:** 28-30 minutes
**Format:** Tutorial + live demos + business framing
**Angle:** Routines (cloud) and Claude Code (local) as a complete stack for creators/solopreneurs. Nobody else is teaching both sides.

---

## [0:00 - 1:00] HOOK

[SHOW: Cold open. Claude Routines dashboard on claude.ai. Tyler on camera, fast cuts.]

> "Everybody's saying Claude Routines killed n8n. They're wrong.
>
> That's not the story. The story is what happens when you pair Routines with Claude Code on your own machine. That's the stack that actually runs a business on autopilot.
>
> Quick context on why you should listen to me on this. I've built hundreds of AI agents and automations. For Fortune 500 companies. JPMorgan. Pfizer. For 150K plus YouTubers running their entire content pipeline. For top Skool communities with custom GPTs and knowledge bases. This isn't theory for me. This is what I do.
>
> So when Anthropic dropped Routines, I was in day one. Gmail, Slack, Apify, all hooked up, running while I sleep. I run 22 custom Claude Code skills that publish 30 plus pieces of content a week. That's the system.
>
> In this video I'm going to show you exactly what Routines are. I'll walk you through two real ones I run in my own business. Then I'll build a new one from scratch live. After that, I'm switching to Claude Code on my machine, running the same kind of work but hands-on. And I'll show you one command nobody's talking about, `/loop`, that changes everything.
>
> By the end, you'll know where Routines win. Where Claude Code wins. And how to use them together.
>
> Let's get into it."

[NOTE: Keep the hook under 60 seconds. Cuts should be fast. No long pauses. This needs to punch.]

---

## [1:00 - 3:00] POINT 1 — What Routines Actually Are

[SHOW: claude.ai/code/routines dashboard. Pan over existing routines.]

> "Okay, first thing. What is a Routine?
>
> A Routine is Claude Code, running in a cloud container on Anthropic's machines. Not yours. Laptop closed, you're asleep, it still runs.
>
> There are three ways to trigger one. A schedule, like every morning at 6 AM. A GitHub event, like whenever a pull request gets opened. Or an API call or webhook, meaning any other system can fire it.
>
> Routines hook into MCP connectors. Slack. Gmail. Apify. GitHub. Google Drive. Whatever you give it access to, it can use.
>
> So think of it like this. A skill in Claude Code tells Claude what steps to take. A Routine tells Claude what steps to take and when to do it, without you there.
>
> That's it. That's the whole feature. The rest is what you do with it."

[SHOW: Quick text overlay: "Routine = Claude Code + Schedule + Connectors (runs on cloud)"]

---

## [3:00 - 5:00] POINT 2 — The Business Case

[SHOW: Tyler at desk, camera on him. Cuts to Slack messages arriving in real-time.]

> "Here's why this matters. And I want to be real specific because most people skip right past this.
>
> A virtual assistant costs you between 15 and 30 dollars an hour. Call it 20. Five hours a day, five days a week, that's 500 bucks a week. 26 grand a year.
>
> A Routine run costs you pennies. Literally pennies per execution. Because you're only paying for tokens.
>
> Now I'm not saying fire your VA. I'm saying every recurring task you do, or that you pay someone else to do, is a candidate for a Routine.
>
> Morning inbox triage. 45 minutes a day. Over a year, that's 195 hours.
>
> Competitive research. Two hours a week. Hundred hours a year.
>
> Content pipeline busywork. Three hours a day. Gone.
>
> The move isn't to do more work. The move is to stop doing the work that doesn't need you. Direct it. Don't do it.
>
> Every hour a Routine runs for you is an hour you get back for the stuff only you can do. Recording videos. Talking to customers. Thinking.
>
> Okay. Let me show you what that actually looks like."

[NOTE: This is the section that gets shared. Keep it concrete. Don't let it drift into "imagine if." Tie every minute to real dollars.]

---

## [5:00 - 8:30] POINT 3 — Routine #1: Morning Inbox Digest

[SHOW: Tyler's actual Routine config open on claude.ai. Blur any sensitive info but leave the structure visible.]

> "This is the first Routine I built. It runs at 5:10 AM every weekday. I'm still asleep.
>
> Here's the prompt. Really simple.
>
> Pull all unread emails from Gmail using the connector. For each one, check if we've had any previous conversation with that person. If we have, pull that context. Then draft a reply based on what you know about me and the thread. When you're done, send me a Slack message with a summary and the drafts.
>
> That's the whole prompt. It's an SOP. Step one, step two, step three, done.
>
> Now watch. I'm going to hit Run Now right now just to demo it."

[SHOW: Click "Run Now." Cut to the Routine executing. Show the tool calls firing: Gmail search, context lookup, draft generation.]

> "While that runs, I'll tell you why this works.
>
> The Gmail connector is OAuth. One time setup. Never touch it again. The Slack connector is the same deal.
>
> The prompt is tight because Routines run hands-off. You can't course correct mid-run. So you write it like an SOP, you don't hope the model figures it out.
>
> Let's see what it sent me."

[SHOW: Switch to Slack DMs. Open the message from the Routine. Show the structured output: email subject, sender, context, draft reply.]

> "Look at this. Here's the email. Here's who sent it. Here's the last time we talked. And here's the draft, already written in my voice.
>
> I wake up, I open Slack, I scan five of these in under two minutes, and I approve or edit. Done. 45 minutes saved. Every single morning."

[SHOW: Text overlay: "195 hours saved / year. VA equivalent: $3,900/year."]

---

## [8:30 - 12:00] POINT 4 — Routine #2: Apify Competitor Monitor

[SHOW: Second Routine config. This one uses the Apify connector.]

> "Second Routine. This one's for creators. Watch.
>
> Every morning at 7 AM, this fires. It uses Apify, which is a web scraping platform, to pull the top TikTok videos on a list of hashtags I care about. Claude Code AI. AI automation. Content automation. You get the idea.
>
> It grabs the top 20 from each hashtag. Filters for ones posted in the last 24 hours with more than 10 thousand views. Then it writes me a digest. Top angles I'm seeing. What formats are working. And five script ideas I could film today based on what's trending."

[SHOW: Run the Routine. Cut to the Apify tool call. Then cut to the Slack output.]

> "Here's what it sent me this morning. Five ideas, ranked by traction, with the angle and the hook already written.
>
> If I hired a social media manager to do this, minimum 800 a month. High end, 1,500. A content strategist? Double that.
>
> This Routine costs me about 40 cents per run. 12 bucks a month.
>
> And here's the thing. It runs while I'm working out. I finish my lift, I open Slack, I pick the one I want to film that afternoon. That's it."

[NOTE: Emphasize the dollar gap. 12 dollars a month vs 1,500 dollars a month. The number does the selling.]

---

## [12:00 - 16:30] POINT 5 — Build a Routine From Scratch (Live)

[SHOW: Back to claude.ai/code/routines. Click "New Routine" button.]

> "Okay now I'm going to build one live. Right now. You can follow along.
>
> We're going to build a Routine that fires every Monday morning and gives me five YouTube video ideas based on what's trending in AI that week.
>
> Step one. Name it. I'll call it Weekly Video Ideas.
>
> Step two. The prompt. I said this earlier but I'll say it again. Write this like an SOP. Steps. Not hopes."

[SHOW: Type the prompt into the box.]

> "Here's what I'm writing. Use the Apify connector. Search YouTube for videos uploaded in the last 7 days on these keywords. Claude Code. Claude routines. AI automation. Sort by views descending. Take the top 15. For each one, pull the title, the channel, views, and the first line of the description. Then write me five new video ideas based on patterns you see across the top performers. Format the output as a Slack message. Send it to the YouTube Ideas channel.
>
> Done. That's the prompt."

[SHOW: Scroll down the Routine config. Select repo, model, environment.]

> "Pick your repo. I'll pick this business one. Pick your model. I use Opus 4.6 with the million token context because these research tasks eat context fast.
>
> Environment. Default for me. You can add API keys and variables here if your Routine needs them.
>
> Now the trigger. I want this on a schedule. Monday at 6 AM."

[SHOW: Click through the schedule picker. Set to weekly, Monday, 6:00 AM.]

> "Connectors. I need Apify. I need Slack. Both are already authenticated from my earlier Routines, so I just add them here."

[SHOW: Add Apify connector. Add Slack connector.]

> "Hit save. Now the real test. Click Run Now."

[SHOW: Click Run Now. Show the execution in real time.]

> "This is going to take a couple of minutes because it's calling Apify to scrape YouTube. I'll fast forward.
>
> And here it is. Look at that. Five video ideas. Each one tied to a specific trending angle. Each one with a proposed title and hook.
>
> Total time to build this Routine? About four minutes. Total time it's going to save me every week? Probably three hours of research.
>
> That's the move."

[NOTE: If the live run fails or hangs, cut to a pre-recorded successful run. Don't show dead air.]

---

## [16:30 - 17:30] POINT 6 — Switch to Claude Code Local

[SHOW: Tyler on camera. Transition animation.]

> "Okay. Routines are incredible for scheduled, hands-off work. Anything predictable. Anything recurring. Anything you want happening without you.
>
> But there's a whole category of work Routines can't touch. Interactive work. Iterative work. Work where you need to steer in real time. Work that needs access to your local files, your local git, your local environment.
>
> That's Claude Code. On your machine.
>
> Let me show you what I mean."

---

## [17:30 - 20:30] POINT 7 — Claude Code Local: /yt-search + /thumbnail

[SHOW: Terminal open. Claude Code running.]

> "This is Claude Code. Running locally. In my terminal. Right now.
>
> I'm going to do two things real fast. First, I'm going to research this exact video. Then I'm going to generate a thumbnail for it. Both in Claude Code. Both in under a minute each.
>
> Watch."

[SHOW: Type `/yt-search claude routines` and hit enter.]

> "This is my yt-search skill. It hits YouTube, pulls the top videos on claude routines from the last 30 days, sorts by views, and dumps a report.
>
> Now. Here's the part you can't do in a Routine. I'm going to look at this and respond to what I see.
>
> Top result. Nick Saraev. 112 thousand views in a day. Okay. I want more context on him specifically."

[SHOW: Type a follow-up: "Now compare his channel's last 10 videos to see what performs best" or similar. Let Claude run.]

> "See that? That's the difference. I'm not writing a new prompt. I'm continuing a conversation. I'm steering. Claude remembers what I just asked and builds on it.
>
> A Routine can't do that. A Routine runs the prompt you wrote, start to finish, no input from you. That's a feature, not a bug. But when I'm actually thinking through something, I want to steer.
>
> Okay. Thumbnail now."

[SHOW: Run `/thumbnail` skill. Show the interactive prompts Claude asks.]

> "Same skill system. But this one uses Kie.ai's Nano Banana model to generate thumbnails. I'm going to describe what I want. Claude's going to ask follow-ups. Then it'll generate three variants.
>
> Quick note. You could do this in a Routine. Schedule a weekly thumbnail batch, fire it off, done. And for bulk, that's the play. But for one-off creative work where I'm iterating on the concept, local is faster. Because I can react."

[SHOW: Thumbnail generation completing. Show the three variants.]

> "Three variants. 30 seconds. Free if you don't count the API cost, which is pennies.
>
> A designer charges 50 to 100 bucks per thumbnail. Per video. I publish two videos a week. That's 400 to 800 a month I'm not spending.
>
> Both of these skills, yt-search and thumbnail, they live on my machine. They have access to my files. They can be steered in real time. That's what Claude Code does that Routines don't."

---

## [20:30 - 23:30] POINT 8 — The /loop Command (The Secret Weapon)

[SHOW: Terminal. Fresh Claude Code session.]

> "Alright, now the part nobody is covering.
>
> Claude Code has a command called `/loop`. What it does is let you run any task on a recurring schedule, locally, right on your machine.
>
> Routines do cloud schedules. `/loop` does local schedules. Different tools. Different jobs.
>
> Why does this matter? Because some things can't run in the cloud. They need your local files. Your local environment. Your local API keys. Your local git repo.
>
> Watch."

[SHOW: Run `/loop 30m /yt-search ai automation` or a similar useful loop.]

> "I just told Claude Code to run /yt-search every 30 minutes on this keyword. Watch the timing.
>
> Every 30 minutes it fires. It pulls fresh data. It updates me if anything new trended. It's like a Routine, but running on my machine, with full access to my local skill library and my files.
>
> The use case most people miss. I use /loop while I'm working to watch a long-running process. If I kick off a video rendering with Remotion, I can /loop to check progress every 60 seconds. Routines can't do that. They don't have access to my local render.
>
> Another one. I use /loop to poll an API during development. Or to monitor a deploy. Or to run a periodic check on local data.
>
> Routines are for the cloud. `/loop` is for your machine. Use both."

[NOTE: Keep this section tight. Don't let it sprawl. The point is simple: local recurring tasks need a local solution.]

---

## [23:30 - 26:30] POINT 9 — Pros, Cons, and When to Use Which

[SHOW: On-screen comparison table. Clean, simple design.]

> "Let me give you the decision framework. When Routines. When Claude Code local. When both.
>
> Routines win when:
>
> The task is predictable. Same steps every time.
>
> You want it running without you. Laptop closed, you're asleep.
>
> The trigger is a schedule, a webhook, or an API call.
>
> You're integrating with cloud services. Gmail. Slack. GitHub. Apify.
>
> Claude Code on your machine wins when:
>
> You need to iterate. Steer. Have a conversation.
>
> The task needs access to your local files, your local git, your local environment.
>
> You're doing creative work. Writing, designing, exploring.
>
> You're developing. Building. Debugging.
>
> And here's the big one. You use both.
>
> I use Routines to handle the recurring stuff while I'm asleep or while I'm filming. I use Claude Code locally when I'm actually sitting down to do creative work. The Routine handles the 80 percent that's predictable. Claude Code handles the 20 percent that needs me.
>
> That's the stack. Not Routines OR Claude Code. Routines AND Claude Code."

[SHOW: Final comparison table as a clean overlay.]

| | Routines | Claude Code Local |
|---|---|---|
| Runs on | Anthropic cloud | Your machine |
| Best trigger | Schedule / webhook / API | You / /loop |
| Iterate mid-task | No | Yes |
| Local file access | No | Yes |
| Laptop closed | Still runs | Doesn't run |
| Best for | Recurring, hands-off | Creative, interactive |

---

## [26:30 - 28:30] POINT 10 — Make the Switch

[SHOW: Tyler on camera. Energy back up.]

> "Alright. Here's my challenge to you.
>
> Pick one thing you do every day. One recurring task. Something that eats 30 minutes or more.
>
> Inbox triage. Competitor research. Social media digests. Whatever it is.
>
> Turn it into a Routine this week. Not next month. This week.
>
> Because here's what I've learned. The people who are winning with AI right now aren't the ones who know the most. They're the ones who actually ship. Who take one task and automate it. Then another. Then another.
>
> That's how you end up with a business that runs without you.
>
> If you want the full system I'm running, 22 Claude Code skills, all the Routines you just saw, the whole content pipeline that publishes 30 pieces of content a week, I break it all down inside my Skool community. Link's in the description.
>
> Leave me a comment. Tell me the first Routine you're going to build. I actually read them. I'll reply to the good ones."

---

## [28:30 - 29:30] OUTRO

[SHOW: End screen. Next video card.]

> "If you want to see me build a specific Routine, comment below and I'll build it live in the next video.
>
> If this was useful, hit subscribe. I'm putting out content like this every week.
>
> Thanks for watching. I'll catch you in the next one."

[END]

---

## Performance Notes

**Why this performs better than Nick and the rest:**

1. **Nick shows Routines.** Tyler shows Routines + Claude Code + /loop. Nobody else is teaching both sides as a stack.
2. **Nick is technical.** Tyler adds business framing (VA math, dollar gap). Broader audience hook.
3. **Nick shows 3 demos.** Tyler shows 2 Routines + live build + 2 Claude Code demos + /loop. More value per minute.
4. **Dan's structure** (numbered points, shock hook, authority, demo→value, action close) is a proven 100K+ view formula.
5. **Thumbnail + title** leverage Nick's proven hook direction but differentiate with "stack" angle.
6. **Dan-style action close** ("pick ONE task this week") drives engagement. Comments become the social proof.

**Editing notes:**
- Fast cuts in hook (under 60s)
- Keep every point tight, no drift
- Use on-screen text overlays for dollar numbers and dates
- Pre-record fallback runs in case live Routine demos hang
- Split screen for comparison points

**Retention hooks inside video:**
- 1:00 Curiosity gap: "/loop command nobody's talking about"
- 5:00 Specific number reveal: "195 hours saved a year"
- 12:00 Live build promise: "building one from scratch right now"
- 23:30 The /loop reveal: "the part nobody's covering"
- 26:30 Action close: "pick ONE task this week"
