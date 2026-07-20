# Script: Stop Prompting Claude Code. Write Loops Instead.

**Target length:** 12-15 min
**Audience:** Creators & solopreneurs using Claude Code (concept-first, minimal code)
**Hero demo:** A real content-pipeline loop running the business
**Tone:** Practical, fast-paced, "I'm a creator not a developer and this changed everything"

> Note: no em dashes anywhere. Short sentences. This reads like you talking, not an essay.

---

## [0:00 - 0:45] Hook

*(Using Hook 1 - the borrowed-authority open. Full text in hooks.md.)*

The guy who built Claude Code just said something that flips everything you've been taught about AI.

He said: "I don't prompt Claude anymore. I write loops that prompt Claude. My job is to write loops."

[SHOW: the Boris Cherny quote on screen, big text, his name underneath]

That clip got 700,000 views in a day. Because it quietly made every prompt tip you've ever saved obsolete.

Here's the problem. Almost everyone, including me until recently, is still typing one prompt, getting one answer, and doing it again tomorrow. That's the slow way.

[NOTE: slow down here, look at camera]

In the next few minutes I'm going to show you the shift, from prompts to loops. And I'm going to show you a real loop that runs my entire content business while I sleep. No code required.

Let's get into it.

[SHOW: title card / channel intro - keep it under 2 seconds]

---

## [0:45 - 2:15] The mental shift: prompt vs loop

Okay so first, what actually changed. Because "write loops not prompts" sounds like a slogan until you get the difference.

A prompt is a vending machine.

[SHOW: simple graphic - coin in, snack out]

You put one in. You get one thing out. Then it's over. Tomorrow you walk back up and put another coin in.

A loop is an employee.

[SHOW: simple graphic - a cycle arrow with "check / act / repeat"]

You tell it what good looks like once. And it keeps working. It checks, it acts, it repeats, until the job is actually done. And then it does it again tomorrow without you.

That's the whole shift. You stop being the thing inside the loop. You stop being the person typing the prompt every single time. Instead you write the loop one time, and the loop does the prompting.

[NOTE: this is the core line of the video - land it]

The unit of work moved. It used to be the keystroke. Then it became the prompt. Now, for the people getting crazy results, it's the loop.

And here's why this matters for you specifically if you're a creator and not a developer. A prompt gets you one output. One caption. One script. A loop gets you a system. The captions, the scripts, the carousels, the research, queued up, on a schedule, without you babysitting it.

[SHOW: side by side - "1 prompt = 1 output" vs "1 loop = a system that runs"]

---

## [2:15 - 4:00] Why this is happening now (the proof)

Now you might be thinking, this sounds like developer stuff. It's not anymore. And here's why it's blowing up right now.

This came from Boris Cherny. He runs Claude Code at Anthropic. The team that builds the tool.

[SHOW: The New Stack headline "The Anthropic leader who built Claude Code says he ditched prompting, now he just writes loops"]

And it's not just talk. Anthropic's own engineers are shipping around eight times more code than before, with over 80% of it written by AI. The loop is how.

[SHOW: stat on screen - "8x more output, 80%+ AI-authored"]

But here's the part nobody's connecting for creators. The exact same thing that makes a developer ship 8x more code makes you ship 8x more content. It's the same machine. You're just pointing it at a different job.

[NOTE: this is the bridge - say it with conviction]

And the reason this is suddenly possible is that Claude Code shipped the tools to actually do it. Real commands. Let me show you the four that matter, and you only really need one to start.

---

## [4:00 - 6:30] The loop toolkit (the 4 commands, creator translation)

I'm going to translate these out of developer language. Four tools. Plain English.

**Number one. Slash loop.**

[SHOW: type `/loop` in Claude Code]

This is the one you start with. You give it an interval and a task. Like, every morning, do this thing. And it just fires on schedule. The task can be one of your own skills. So "every morning at 7, run my content research skill" is a complete loop.

[NOTE: this is the hero command - emphasize it]

It runs quietly in the background. It won't interrupt you. And it expires on its own so it can't run forever. Training wheels are built in.

**Number two. Slash goal.**

[SHOW: type `/goal` in Claude Code]

This one's different. Instead of "do it every morning," you give it a finish line. You say, keep going until this is true. And a second faster model grades the work after every pass. So it loops until the job actually meets your standard, then stops. That's the "employee that doesn't quit until it's done" command.

**Number three. Slash batch.**

[SHOW: type `/batch` in Claude Code]

This is for volume. One instruction, split across a bunch of agents at the same time. "Write me five short scripts from this research" and it fans them out in parallel instead of one at a time.

**Number four. Ultracode.**

[SHOW: type a prompt with the word `ultracode` in it]

This is the big one. You just put the word "ultracode" in your prompt and Claude Code writes its own little program to coordinate up to a thousand sub-agents at once. Migrations, audits, giant research sweeps. You will not need this on day one. But know it exists, because it's where this goes.

[SHOW: quick recap card - /loop = schedule, /goal = until done, /batch = volume, ultracode = scale]

Quick honesty note. Loop, goal, and batch are the everyday ones. Ultracode is the heavy machinery. If you remember one, remember slash loop.

---

## [6:30 - 7:30] The anatomy of a good loop (so it doesn't go rogue)

Before I show you mine, one thing. A loop is only as good as its guardrails. Because a loop that runs forever with no brakes is how you wake up to a mess.

[NOTE: this builds trust - shows you're responsible, not reckless]

Every good loop has four parts. Keep these in your head.

[SHOW: 4-part checklist building one line at a time]

One. It knows the intent. You wrote down what you actually want. For us that lives in skills and in your Claude dot M D file.

Two. It has something that can say no. A check. A test. A taste gate. Mine literally shows me the draft and waits for a thumbs up before anything goes out.

Three. It has skills worth calling. The loop is dumb on its own. The skills are where the real work lives.

Four. It can stop. A cap. Max runs, or a budget, or an expiry. So it always halts.

[SHOW: "intent / a way to say no / skills / a stop" as four icons]

Intent. A way to say no. Skills. A stop. If your loop has those four, you're safe to let it run.

---

## [7:30 - 11:00] DEMO: the loop that runs my content business

Alright. Theory's over. Let me show you a real one.

[SHOW: screen recording starts - Claude Code in the terminal]

This is my actual setup. I'm a content creator. I make videos about AI tools. And I have a stack of skills I built for every repetitive job in my week. Research, scripts, carousels, captions, all of it.

[SHOW: quick scroll through the skills list - don't dwell, just show the volume]

For the longest time I ran these one at a time. I'd sit down, type slash y t search, wait. Type the next one, wait. I was the thing in the loop.

So here's what I do now instead.

[SHOW: type the /loop command on screen]

```
/loop every morning at 7am, run my content research for this week's topics, then draft the short-form scripts from what you find, and show me the drafts before doing anything else
```

[NOTE: read the command out loud as you type it - let viewers follow]

Look at what just happened. I didn't write a prompt. I wrote a loop. One time.

Now every morning at 7, before I'm even awake, this fires. It runs my research skill. It pulls what's trending. It hands that to my script skill. And it drafts the week's short scripts.

[SHOW: cut to the loop having run - the drafted output sitting there]

And here's the guardrail I talked about. It does not post anything. It does not schedule anything. It stops and shows me. [SHOW: the drafts waiting for approval] I wake up, I read them with my coffee, thumbs up the good ones, and that's my content engine for the day. Done before breakfast.

[NOTE: this is the emotional payoff - sit in it for a beat]

Let me show you one more, because this is where it clicks.

[SHOW: type a /goal example]

```
/goal keep improving this video description until it has a hook in the first line, all chapters filled in, and the right keywords, then stop
```

This one doesn't run on a schedule. It runs until it's right. It writes a version, a second model grades it, it's not good enough, it tries again. It loops on its own until it hits the bar I set. Then it stops and hands it to me.

[SHOW: the goal loop iterating, then landing on a final version]

That's the shift in one screen. I'm not typing prompts. I set the intent and the finish line. The loop does the reps.

[NOTE: if a step is slow on camera, talk through "what it's doing right now" - see filming guide for dead-air fillers]

---

## [11:00 - 12:30] How to build YOUR first loop today

So how do you start. Don't overthink this. You do not need to be technical and you do not need a stack of skills like mine.

Here's the on-ramp.

[SHOW: 3-step card]

Step one. Pick the most boring repetitive thing you do every week. The thing you dread. For me it was content research. For you it might be drafting replies, or summarizing your week, or pulling trends.

Step two. Make Claude Code do it once, manually, until you like the result. That's it. Just get one good output the normal way.

Step three. Wrap that exact thing in a slash loop. "Every Monday, do this." That's your first loop. You just went from prompting to looping.

[NOTE: keep this dead simple - the whole point is it's not scary]

And then the magic part. Every time the loop does something you don't love, you fix it once, and you tell Claude to remember it. The loop gets smarter every single week. Day 30 is way better than day 1. That compounding is the entire game.

[SHOW: "fix it once -> it remembers -> compounds" arrow graphic]

You're not building a robot. You're training an employee. One note at a time.

---

## [12:30 - 13:30] Recap + CTA

So let's zoom out.

[SHOW: recap card - the 4 beats]

Prompts are a vending machine. Loops are an employee.

You stop being the thing in the loop. You write the loop once.

Start with slash loop. Add slash goal when you want a finish line. Give it guardrails so it can always stop.

And pick one boring task this week and wrap it in a loop. That's it. That's the whole shift.

[NOTE: direct to camera for the close]

I went from spending my mornings prompting, to waking up with the work already drafted. As a creator, that gave me my time back. And it's the single biggest change in how I use AI all year.

If you want to see the actual skills I loop together to run my whole content business, that's this video right here.

[SHOW: end screen - point to the "Claude Code for Content Creators" / "100 pieces of content" video]

I'll see you in that one. Go write your first loop.

[SHOW: subscribe prompt + end screen]
