# Script - I Automated My Email With Claude Code

Target runtime: 12 to 15 minutes, tight. Format: talking head plus screen capture. Tyler's voice: practical, direct, honest. No em dashes. No fake money. Always distinguish what Claude Code does from what the Gmail and Resend APIs do.

PRIVACY REMINDER FOR THE EDIT: Blur every real sender name, address, subject line, and private body. Never let a token, .env, credentials.json, or token.json appear on screen. Use non-sensitive threads (newsletters, your own test sends, cleared sponsor logistics) for anything visible.

---

## 0:00 - 0:35 | COLD OPEN (word for word)

[On screen: real inbox, 99+ unread badge. Hard cut to the same inbox cleanly triaged with a label.]

"I don't really do my email anymore. Claude Code does.

This is my actual inbox, and I didn't sort any of this by hand. In the next few minutes I'm going to show you exactly how it works, and how you could build the same thing, or even sell it to a business.

And no, nothing here is faked. It's a real inbox, so I blurred anything private. Never put real tokens or private email on camera. Let's get into it."

[Quick title card or just cut straight to the next beat. No long intro.]

---

## 0:35 - 2:15 | THE PROBLEM

[Talking head, or over a fast scroll of the messy inbox.]

"So here's the honest problem. Email is the one thing that never stops. I run a YouTube channel, I've got a community, I do sponsor stuff, and I've got a normal life. And every single day the inbox fills back up. Newsletters I actually want, cold pitches I don't, a couple of real emails that genuinely need a reply, all mixed together.

The old way to deal with this is you sit down, you open Gmail, and you manually scan every subject line trying to figure out what matters. That is slow, it's boring, and it's the kind of task that quietly eats an hour out of your morning before you've done anything that actually moves your business forward.

I tried the AI email apps. There are a bunch of them, they're fifteen, twenty, thirty bucks a month, and they're fine. But two things bugged me. One, it's another subscription. Two, it's a black box. I don't control what it does, I can't change how it triages, and my email is sitting inside somebody else's tool.

So I did what I do with everything now. I built it myself in Claude Code. And I want to be really clear about what that means before I show you, because I don't want to oversell it."

---

## 2:15 - 3:30 | HOW IT ACTUALLY WORKS (draw the line)

[On screen: simple diagram. Claude Code in the middle, Gmail API on one side, Resend on the other.]

"Here's the honest breakdown of the pieces, because I see a lot of videos make this sound like magic and it's not.

Claude Code is the brain and the operator. It's the thing I talk to. It decides what to do, it reads, it summarizes, it drafts.

But Claude Code doesn't magically have access to my email. It talks to the Gmail API. That's Google's official way for an app to read and search your inbox, and you connect it with OAuth, which is the same secure login flow you've used a hundred times when an app asks to connect to your Google account. So the Gmail API is what actually reads and searches the inbox. Claude Code just drives it.

On the sending side, I use a service called Resend. Resend is what actually sends email out. So when I have Claude Code send a one-off email, or a batch, or a little welcome sequence, Claude Code is writing it and Resend is the thing that puts it in the outbox.

So the split is simple. Claude Code is the brain. Gmail's API is the eyes. Resend is the mouth. I wired all three together as skills, and I'll show you each one running for real. Nothing here is faked, and I still review everything important before it goes out. This triages and drafts. I approve."

---

## 3:30 - 6:30 | DEMO 1: INBOX TRIAGE (the money shot)

[Screen capture: Claude Code terminal on the left, Gmail on the right. Blur private content.]

"Alright, demo one, and this is the one I use every single day. Triage.

I've got a skill set up that connects Claude Code to my Gmail through the Gmail API. So I just talk to it. Watch.

[Type or speak the prompt on screen:]
'Go through my inbox from the last day. Group everything into what needs a reply, what's a newsletter I might want to read, and what's noise I can ignore. For anything that needs a reply, give me a one-line summary of what they want.'

[Let it run. Narrate as it works.]

And now Claude Code is calling the Gmail API in the background, pulling the recent threads, and reading them. This is the real thing, this is happening live.

[Results come back.]

And there it is. Look at this. It sorted the whole inbox. Up top, needs a reply, and it's three emails, not thirty. It's telling me this person wants to reschedule a call, this one is a sponsor asking for the invoice, this one is a viewer with a real question. Then it's got a bucket of newsletters it flagged as read-when-you-want. And then a whole pile it's calling noise, the cold pitches and the promos.

That is the entire point. I didn't read forty emails. I read one summary, and I instantly know the three things that actually need me today.

Now, one honest note. It's not perfect. Sometimes it'll put something in the wrong bucket, or flag a newsletter as important because the subject line was aggressive. So I skim its work, I don't blindly trust it. But even skimming, this turns what used to be an hour into about two minutes.

[Optional: show applying a Gmail label or star to the 'needs reply' group so the triage is visible in Gmail itself.]

And I can have it actually mark these in Gmail too, so the important ones get a label right in my inbox. So even if I open Gmail on my phone later, the triage is already done."

---

## 6:30 - 8:30 | DEMO 2: DRAFTING REPLIES

[Screen capture continues.]

"Okay, demo two. It found the emails that need a reply. Now let's have it write them.

[Prompt on screen:]
'For the three emails that need a reply, draft a response for each. Keep my tone, short and friendly, and don't send anything. Just draft them so I can review.'

[Let it run.]

And this is where the honesty really matters. I'm telling it to draft, not send. I always review before anything goes out, especially replies to real people.

[Drafts come back.]

Look at these. The reschedule one, it wrote a clean two-line reply offering two new times. The sponsor invoice one, it drafted a reply and even noted where the invoice would attach. The viewer question, it wrote a genuinely helpful answer in my voice.

Are they perfect? Mostly. I'll tweak a word here and there. But going from a blank reply box to a solid draft I just edit and send, that's the difference. The hard part of email isn't clicking send, it's starting the reply. This does the starting for me.

And to be totally clear about the mechanics, it can drop these straight into Gmail as real drafts through the Gmail API, so they're sitting in my drafts folder waiting for me to hit send. I stay in control of the actual send. That's on purpose."

---

## 8:30 - 10:30 | DEMO 3: SENDING AND A SIMPLE DRIP

[Screen capture: switch to the /email skill, Resend.]

"Now let's flip to the other side, sending. This is the second skill, and it uses Resend to actually send email.

Two quick things I use it for.

First, one-off and batch sends. Say I want to email the people who signed up for my free pack this week with a quick note. I can just tell Claude Code who and what, it drafts it, I approve it, and Resend sends it.

[Prompt on screen, using a real permission-based list, for example newsletter opt-ins:]
'Draft a short email to my newsletter list letting them know the new video is live. Friendly, no hype, one link. Show me before you send.'

[Draft appears. Emphasize the approval step.]

See that? It drafted it and it's waiting. I read it, and only when I say go does it hand it to Resend to send. I never let it blast my list without me looking first. That's a rule.

Second thing, and this is the fun one, automated sequences. When someone joins my list, I don't want to manually welcome every person. So I've got a simple welcome drip. New person comes in, they get an email now, another one a couple days later, and so on. Contact sync keeps the list up to date, and there's a daily cron, which just means a little scheduled job that runs once a day to send whatever's queued.

[Show the drip setup at a high level, blur any real addresses.]

Quick honest guardrail here. This is for people who actually asked to hear from me. Newsletter opt-ins, community members. This is not a cold-email-strangers machine, and I'd tell you not to build it for that. Keep it clean and you keep your sender reputation, and honestly you keep your integrity."

---

## 10:30 - 11:45 | THE ROUTINE (the payoff)

[On screen: a Claude Routine config or a calendar-style schedule graphic.]

"Now here's the part that actually changed things for me, and it's the reason I barely think about email at all anymore.

Everything I just showed you, the triage, I don't even trigger it by hand. I set it up as a Claude Routine that runs on a schedule.

Quick clarification so I don't mislead you. A routine runs on Anthropic's servers on a schedule, so my laptop doesn't have to be open for it to run. It just fires on its own.

So every morning, before I'm even at my desk, the routine has already gone through my inbox with the Gmail API, sorted everything, and left me a clean summary of what needs me. I made a whole short about this called the email triage routine that saves me hours every week, and it's real. I open my laptop and the triage is already done.

That's the difference between a cool demo and something that actually saves you time. A demo you have to run. A routine just happens. I automated the automation."

---

## 11:45 - 12:45 | HONEST LIMITATIONS

[Talking head. This section builds trust and it's why the channel works.]

"Before I wrap, let me be straight with you about the limits, because I'm not going to pretend this is flawless.

One, it's not always right. It'll occasionally miscategorize an email or write a draft that misses the point. So you review. You don't hand it the keys and walk away.

Two, I keep a human in the loop on anything that sends. Triage runs on its own, fine. But replies and sends, I look first. Every time.

Three, privacy is real. You are connecting an AI to your actual inbox. So use good judgment. Don't put secrets in prompts, don't show your tokens or your inbox on camera like I've been careful not to here, and if you're doing this for a client, treat their data like it's radioactive.

And four, be honest about what each piece does. Claude Code is the brain. The Gmail API reads. Resend sends. If someone tells you an AI just magically runs your email with no APIs and no setup, they're selling you something.

None of that ruins it. It just means you build it like an adult. And when you do, it genuinely gives you your mornings back."

---

## 12:45 - 14:00 | THE OPPORTUNITY + CTA

[Talking head, energy up.]

"Okay, last thing, and this is the part I'd actually pay attention to if I were you.

I built this for me. But think about who else has this exact problem. Every small business owner is drowning in email. Every agency, every coach, every consultant. Inbox triage and outbound email is something companies already pay real money for, they hire assistants and agencies to do it. And you now know how to build the system that does it.

I'm not going to throw a fake number on the screen and tell you what you'll make, because I don't know and I'm not going to lie to you. What I'm telling you is this is a real, valuable skill, and the tools to build it are right here in this video.

If you want the actual setup, I put together a free pack with the skills and the starting points I use, plus my newsletter where I share this stuff every week. It's the first link in the description, free.tylerai.dev/youtube. Grab it, it's free.

And if you want to go deeper and build these with other people who are doing the same thing, I've got a community, that link's down there too.

If this was useful, subscribe, because I do exactly this, I take real work and I automate it with Claude Code, and I show you how. I've got a video right there on how I automated my entire YouTube workflow the same way, go watch that next. I'll see you in it."

[End card: subscribe + the YouTube-workflow video thumbnail. Pin the free.tylerai.dev/youtube link in the top comment.]

---

## FILMING NOTES
- Total spoken pace should land around 13 minutes. If it runs long, tighten the problem section (2:15) first.
- The three demos are the spine. If a live demo misbehaves on the day, re-run it, do not fake the output. Real is the whole brand.
- Keep the terminal font large and legible. Zoom in on results.
- Every time a demo runs, keep a hand off the mouse where possible so it reads as real automation.
- Say the privacy line at least twice: once in the cold open, once in limitations.
- Do not use the raw Skool URL on screen or as the primary CTA. Hero link is always free.tylerai.dev/youtube.
- No em dashes in any lower thirds or on-screen text.
