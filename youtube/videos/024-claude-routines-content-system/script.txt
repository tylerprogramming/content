# Script: Claude Routines + Claude Code - The Real Automation Stack

**Target runtime:** 28-30 minutes
**Format:** Tutorial + live demos + business framing
**Angle:** Routines (cloud) and Claude Code (local) as a complete stack for creators/solopreneurs. Nobody else is teaching both sides.

---

## [0:00 - 0:35] HOOK (proof-first - get to a real Routine in the first 15 seconds)

[SHOW: OPEN ON THE PAYOFF. A Slack message that a Routine posted overnight - the inbox digest or the competitor digest - landing on screen. Then quick cut to the Routine's config on claude.ai showing it ran while the laptop was closed.]

> "This ran at 5 AM while I was asleep. [SHOW the Slack output] My AI read my inbox, drafted every reply, and handed me a summary before I woke up. I didn't touch it. This is a Claude Routine, and it runs in the cloud, no laptop, no me.
>
> [Quick cut, on camera] Everybody's saying Routines killed n8n. Wrong. The real story is Routines plus Claude Code as one stack, and I've built this kind of automation for IBM, JPMorgan, Pfizer, and 150K YouTubers, so let me just show you.
>
> Two real Routines I run, then I build one live, then the Claude Code side and the one command nobody talks about, `/loop`. Let's go."

[NOTE: HARD RULE - a real Routine result is on screen in the first 10-15 seconds. Credibility is ONE fast sentence, not a paragraph. No "what is a routine" theory before the proof. This is where retention is won. Total hook ~30-35s, then straight into Point 1.]

---

## [1:00 - 3:00] POINT 1 - What Routines Actually Are

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

## [3:00 - 5:00] POINT 2 - The Business Case

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

## [5:00 - 8:30] POINT 3 - Routine #1: Morning Inbox Digest

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

## [8:30 - 12:00] POINT 4 - Routine #2: Apify Competitor Monitor

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

## [12:00 - 16:30] POINT 5 - Build a Routine From Scratch (Live), On the Web

[SHOW: Open the browser to claude.ai/code/routines. The web dashboard with the existing routines listed. Click "New Routine."]

> "Okay now I'm going to build one live, right now, on the web. You can follow along at claude.ai slash code slash routines.
>
> Quick note. There are three ways to make a Routine. Right here on the web, which is what I'll use because it's the easiest to see. The slash schedule command if you're in the terminal. Or New Remote Task in the desktop app. Same Routine either way, pick whatever you like. I'll do the web.
>
> And I'm not going to build a boring one. Everyone shows you an email summary. I'm going to build something nobody shows you. A Routine that reads my own database and gives me a business scorecard every Monday morning.
>
> Yeah. It queries my actual database. Watch."

[NOTE: This is the differentiator. No other Claude Routines video shows the database/Supabase angle. Lean into it.]

> "Step one. Name it. Weekly Business Scorecard.
>
> Step two. The prompt. Write it like an SOP. Steps, not hopes. The cloud session starts with zero context, so everything it needs has to be in the prompt."

[SHOW: Type the prompt into the box.]

> "Here's what I'm writing. Using my Supabase project, pull this week's business numbers and post a scorecard to Slack. One. Query the business_weekly table for the latest week and the week before. Two. Query youtube_daily for the last seven days. Total views, subscribers gained, and the best performing video. Three. Calculate the change versus last week for each number. Four. Post a clean scorecard to my Slack business channel with each metric, the week over week change, and one honest one-line takeaway. Be terse. No preamble.
>
> Done. That's the whole brain of it."

[SHOW: Scroll down the Routine config. Select repo, model, environment, on the web form.]

> "Now the rest of the form. Pick the repo it runs in. Pick your model. Default is fine. Environment, default for me. This is also where you'd add any keys or variables it needs.
>
> Now the trigger. I want this on a schedule. Weekly, Monday, 6 AM. I type my local time and it converts to the right zone for me automatically."

[SHOW: Click through the schedule picker. Set to weekly, Monday, 6:00 AM.]

> "Connectors. This one needs two. Supabase, so it can read my database. And Slack, so it can post the result. I tick both right here on the form."

[SHOW: Tick the Supabase connector and the Slack connector in the web UI.]

> "Hit save. It's live, it'll fire every Monday on the cloud. But let's not wait until Monday. Click Run Now."

[SHOW: Click Run Now. Show the execution in real time, the Supabase query firing, then the Slack post.]

> "It's connecting to my database, running the queries, doing the math, and writing the Slack message. I'll fast forward.
>
> And there it is, dropped right into Slack. My members, my views this week, up or down versus last week, and a one-line read on how the week actually went. My AI just did a Monday-morning business review by reading my own database. While I did nothing.
>
> Four minutes to build. Runs forever."

[NOTE on camera: this shows real revenue/member numbers. Blur or use rounded/demo figures for anything you don't want public. If the live run fails or hangs, cut to a pre-recorded successful run. Don't show dead air.]

> [Talking head, then cut to the terminal.]
> "Now I built that on the web so you could see every field. But I basically live in the terminal, so let me show you the fast way. Same Routine, one command."

[SHOW: Claude Code open in the terminal. Type the /schedule command.]

> "I type slash schedule, and I just tell it what I want in plain English. Every weekday at 8 AM, scan my Gmail for sponsorship and brand deal emails, and post a summary with the deadlines to my Slack deals channel."

[SHOW: Claude Code walks through it conversationally - confirms the time conversion to the schedule, checks the connectors are connected, shows the config, asks to confirm. Then creates it and returns a claude.ai link.]

> "And it walks me through it right here in the terminal. It confirms my 8 AM converts to the right schedule. It checks I've got Gmail and Slack connected. It shows me the whole config. I say yes, and it's live, the exact same cloud Routine I just built on the web, made from my terminal in about thirty seconds. It even hands me a link to manage it on the web.
>
> But here's one thing you have to understand, and it trips people up. Even though I built this from my terminal, it still runs in the cloud, and it can only use my cloud connectors. The ones connected to my Claude account. Not the MCP servers sitting on my laptop.
>
> Those are two different lists. Your Claude account connectors, that's what Routines use, you manage them at claude.ai slash customize slash connectors. And then your local Claude Code has its own MCP servers in its own config on your machine. They can overlap, but they're not the same thing, and a cloud Routine can never reach a local-only one. Remember that, because it decides what you can and can't automate in the cloud."

[NOTE: KEY ACCURACY POINT. /schedule creates a CLOUD routine using claude.ai account connectors (claude.ai/customize/connectors), NOT local MCP servers. Building from the terminal does not make it local. A cloud Routine cannot use a connector that only exists in your local Claude Code config.]

> [Talking head.]
> "And here's the thing. Once you see this pattern, you start seeing routines everywhere. So let me give you a few you can steal."

[SHOW: Clean list overlay, 4 routine ideas with their connectors.]

> "One. A sponsorship tracker. Gmail plus Slack. It scans your inbox for brand deals and drops the offers and deadlines in Slack so you never miss one.
>
> Two. A competitor upload alert. Apify plus Slack. It watches your competitors' channels and pings you the second they post, with a one-line take.
>
> Three. A morning meeting prep brief. Calendar plus Gmail plus Slack. Before your day starts, it pulls the relevant emails for every meeting on your calendar.
>
> Four. A content gap auditor. Google Drive plus Slack. It reads your scripts folder and tells you what you still need to make this week.
>
> Same recipe every time. A prompt, some connectors, a schedule. That's all a Routine is."

[NOTE: these 4 are real, buildable with Tyler's connected connectors (Gmail, Apify, Calendar, Drive, Supabase, Slack). Keep the list on screen as a saveable/screenshot moment.]

---

## [16:30 - 17:30] POINT 6 - Switch to Claude Code Local

[SHOW: Tyler on camera. Transition animation.]

> "Okay. Routines are incredible for scheduled, hands-off work. Anything predictable. Anything recurring. Anything you want happening without you.
>
> But there's a whole category of work Routines can't touch. Interactive work. Iterative work. Work where you need to steer in real time. Work that needs access to your local files, your local git, your local environment.
>
> That's Claude Code. On your machine.
>
> Let me show you what I mean."

---

## [17:30 - 20:30] POINT 7 - Claude Code Local: /yt-search + /thumbnail

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

## [20:30 - 23:30] POINT 8 - The /loop Command (The Secret Weapon)

[SHOW: Terminal. Fresh Claude Code session.]

> "Alright, now the part nobody is covering.
>
> Claude Code has a command called `/loop`. What it does is let you run any task on a recurring schedule, locally, right on your machine.
>
> And I need to clear up the thing that confuses everybody, because they're both slash commands in the terminal. `/schedule` and `/loop` are NOT the same thing. `/schedule`, the one I used earlier, creates a cloud Routine. Anthropic's servers, cloud connectors, laptop closed. `/loop` runs right here on my machine, in my terminal session, with my local files and my local skills. Same idea, recurring work, completely different place it runs.
>
> Why does the local one matter? Because some things can't run in the cloud. They need your local files. Your local environment. Your local API keys. Your local git repo.
>
> Watch."

[SHOW: two-box overlay for the contrast - `/schedule` → CLOUD Routine (Anthropic servers, cloud connectors, laptop closed) | `/loop` → LOCAL (your machine, your files + skills). Caption: "Both are terminal commands - that's why people mix them up."]

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

## [23:30 - 26:30] POINT 9 - Pros, Cons, and When to Use Which

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
| Connectors it can use | Cloud only (claude.ai connectors) | Your local MCP servers |
| Laptop closed | Still runs | Doesn't run |
| Best for | Recurring, hands-off | Creative, interactive |

> [Talking head, point at the connectors row.]
> "And that connectors row is the one people miss. A Routine can only touch the connectors on your Claude account. If a task needs a tool that only lives on your machine, or your local files, that's a Claude Code job, not a Routine. That one line tells you which side of the fence any task belongs on."

---

## [26:30 - 28:30] POINT 10 - Make the Switch

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
