# 050 - Script: How To Build AI Agents in 2026 (5 Steps, No Code)

Target runtime ~10-12 min. Voice: teaching a friend, short sentences, "so/and then," humble, admit the messy parts. No em dashes. No hype words. Tyler is a software engineer; credibility is delayed. Retention rule: never a graphic-free screen-share, webcam PIP always on, a synced visual within ~2s of every claim.

**Agent built live = the social-research agent** (topic in, researches across YouTube/IG/X/TikTok via Apify, reads top transcripts, hands back a brief with content ideas). Built live, NOT pre-made. Second-by-second cold open lives in `first-2-min-opening.md`; the build detail lives in `live-build-guide.md`. This script is the connective narration.

---

## COLD OPEN (0:00 - 0:30)

[SHOW: b-roll of a research brief scrolling itself, ranked videos + platform logos. NO face until 0:08.]

This morning, before I even sat down, an AI agent researched my whole niche for me. It pulled the top content across every platform, and told me exactly what to make next.

[SHOW: hard cut to face, slow push-in.]

I built it in five steps, and I'll build it with you right now.

[SHOW: "A real agent" flips green; cards 1-2-3 build.]

A real agent. It connects to the tools that pull that data, and it does the research for you every morning.

[SHOW: chips fly in - "Never coded" / "No framework".]

No engineer, no framework, no glue code. You describe what you want, and Claude builds it.

[SHOW: bare face - the credibility beat.]

I have been a software engineer for about eight years. IBM, then Chase, now Pfizer. And I am telling you, the way we build these in 2026 is nothing like it was even a year ago.

[SHOW: "In this video: 5 Steps" roadmap card. Step 3 glows; open-loop marker on the brief.]

Five steps. By step three it is pulling real videos. And that brief from the start, the one that was waiting for me, I will show you exactly how it made it, and how to run it every morning without me.

[NOTE: hard cut. Music stinger. No "welcome back," no subscribe yet. Building on screen by 0:30.]

---

## STEP 1 - GET IN (0:30 - 0:50)

[SHOW: title card "Step 1: Get in". Three doors fast - Claude Code / Desktop app / claude.ai web, a chip on each.]

Step one. Just get in. There are three doors, and honestly, start wherever you are comfortable. The desktop app, the website, or the terminal.

[SHOW: land in Claude Code, webcam PIP bottom-right.]

I am going to build in Claude Code, and here is the only reason why. This is the one where I can give it real tools and put it on a schedule. That is what makes it an agent instead of a chat window.

---

## STEP 2 - DEFINE IT (Claude scaffolds the skill) (0:50 - 2:40)

[SHOW: title card "Step 2: Describe it".]

Step two. And here is the part that is completely different in 2026. I am not going to write the agent. I am going to describe it, and Claude is going to build it.

[SHOW: type the request into Claude Code, kinetic caption of the line.]

So I just type what I want, in plain English:

> "Create a Claude Code skill called social-me. It takes a topic and researches it across YouTube, Instagram, X, and TikTok using Apify, reads the top YouTube videos' transcripts, finds what's working and the content gaps, and gives me a brief with content ideas. Ground everything in real data, never invent numbers."

[SHOW: Claude creates the folder + SKILL.md live. Open the file.]

And watch. It is creating a folder, and a file called SKILL.md. That file, right there, is the agent.

[SHOW: node cards build - "a text file (the instructions)" + "the tools it can use" + "it can carry its own code".]

Because here is what an agent actually is, and it is simpler than the word makes it sound. An agent is just a text file that says its job, plus the tools it is allowed to use. And it can carry its own code too. That is the whole thing.

[SHOW: split card - "Chatbot: talks" vs "Agent: does the work".]

A chatbot just talks back to you. An agent has a job, it can reach real tools, and it goes and does the work. That is the only real difference.

[NOTE: keep this tight - concept taught inline off the file it just wrote, not as a separate lecture.]

And I want to be honest up front. It will not be perfect on the first try. Mine never is. You get it most of the way, then you nudge it. Expect eighty percent, then you help it get the rest. That back and forth is the whole workflow.

---

## STEP 3 - ADD THE TOOLS (MCP + the skill's own code) (2:40 - 5:00)

[SHOW: title card "Step 3: Give it reach (MCP)". This is the star of the video.]

Step three. Right now the agent knows its job, but it cannot touch anything yet. So we give it reach. Two kinds.

[SHOW: simple diagram - the skill in the middle, arrows out to YouTube / Instagram / X / TikTok, labeled "MCP (Apify)".]

First, MCP. Model Context Protocol. Do not worry about the name. It is just a standard plug that lets the agent connect to real services. I am plugging in Apify, which is how it will actually reach YouTube, Instagram, X, and TikTok.

[SHOW: run the Apify `claude mcp add ...` command, then `/mcp` showing Apify connected.]

It is one command to add it, and then I can see it is connected. Before this, connecting an agent to all these platforms meant writing a pile of code. Now somebody already built the connector. You just plug it in.

[SHOW: drop in the yt_transcript.py script.]

And the second kind of reach: the skill can carry its own code. I am dropping in a small script that pulls a YouTube transcript with yt-dlp. So the agent does not just call services, it can run its own tools too.

[SHOW: point at the fallback in the code.]

And here is a real-world touch. YouTube blocks yt-dlp a lot. So the skill has a fallback. When yt-dlp gets blocked, it falls back to Apify. That is the kind of thing that makes an agent actually hold up.

[SHOW: kinetic caption - "The skill is the recipe. MCP is the reach. The skill calls the tools."]

So here is the mental model for the whole thing. The skill is the recipe. MCP is the reach. And the skill calls the tools when it needs them.

---

## STEP 4 - REFINE IT (roast it with grill-me) (5:00 - 6:40)

[SHOW: title card "Step 4: Refine". Show the grill-me skill is installed.]

Step four. Now, instead of me sitting here trying to guess the perfect instructions, I am going to let another skill interrogate this one. This is grill-me, from Matt Pocock. Credit to him, it is great.

[SHOW: run grill-me on the social-research skill; questions start firing.]

I run it on my agent, and it starts firing hard questions. What is the exact output format. What happens when a platform returns nothing. When should this skill even trigger. What is the rule that stops it from making up numbers.

[SHOW: answer a few on camera, and the SKILL.md tightening as holes get filled.]

And as I answer, I tighten the file. It finds the holes I would have shipped, a missing output format, no grounding rule, unclear when to use it. This is the step that turns a rough draft into something you trust, and I did not have to be the expert. The skill did the interrogating.

[NOTE: speed-ramp the middle of the grilling in the edit. Keep 3-4 real questions, cut the rest.]

---

## STEP 5 - RUN IT, THEN SCHEDULE IT (6:40 - 8:40)

[SHOW: title card "Step 5: Run it, then hand it off".]

Step five. The payoff. Let's actually run it.

[SHOW: type `/social-research Claude Code AI agents`. Let it work - webcam PIP stays, push-in on the result.]

One command. Give it a topic. And now watch it go. It is hitting Apify for each platform. It is pulling the top YouTube videos and reading their transcripts, using that yt-dlp script, falling back to Apify when it needs to.

[NOTE: this is the money shot. Let the real output land. Do not sit on a spinner - speed-ramp the waits.]

And there it is. A real brief. What is actually working right now, the gaps nobody is covering, and a list of content ideas I could make next. That is real data, not made up, because we gave it that grounding rule.

[SHOW: guardrail beat - point at the YouTube section, then gesture to the other platforms.]

I built the YouTube path all the way through. And because it is one skill, I just point it at Instagram, or X, or TikTok, and it does the same thing there. Same recipe, more reach.

[SHOW: schedule it - a clock at 7am triggering the skill / a Claude routine.]

But it still only runs when I type it. So the last move, take even that off my plate. I put it on a schedule. Every morning, before I am up, it runs on its own and the brief is just waiting for me.

[NOTE: CLOSE THE OPEN LOOP. Callback to the cold open.]

And that, right there, is the thing I showed you at the very start. The brief that was ready before I sat down. Same agent, same five steps, it just ran on a schedule. Nobody typed anything. That is the difference between a chatbot and an agent. It runs without me.

---

## RECAP + WHAT TO BUILD FIRST (8:40 - 9:50)

[SHOW: all 5 steps as a clean stacked list, each ticks green.]

So that is the whole thing. Five steps. Get in. Describe it and let Claude build the skill. Give it reach with MCP and its own code. Refine it by letting grill-me roast it. Then run it, and schedule it.

And notice, we never touched a framework, we never wrote glue code. In 2026 you build an agent by describing the job and plugging in the tools. That is the shift.

[SHOW: kinetic caption - "Pick the boring thing you do every week."]

So here is what I would do. Do not build the everything-agent. Pick one boring thing you do every week. Research, a report you always pull, something repetitive. Build the small version, get it to eighty percent, then nudge it.

It takes about ten minutes to start. Just start.

---

## CTA + OUTRO (9:50 - end)

[NOTE: CTA folded into the momentum, then snap back. No dead-air "smash like."]

If you want the exact skill, the Apify setup, and the commands I used, I put them and a step-by-step walkthrough in the free community. Link is below. That is the fastest way to get your first one running today.

[SHOW: soft end card - the next video.]

And tell me in the comments what job you would hand off first. I read every one, and that is usually where my next video comes from.

That is it. Go build a small one. I will see you in the next one.

[NOTE: end card, no long outro. Hard-ish cut.]
