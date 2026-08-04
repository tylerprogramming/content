# Script - 3 Claude Code Skills That Replaced My Entire Morning Routine

Target runtime: 14-16 minutes
Audience: anyone with a laptop. Assume no coding, no terminal experience.
Angle: three real skills shown running on real data, then build a fourth from scratch on camera.

**Standing rules for delivery:** short sentences. Breathe between them. Never say "simply" or "just" to a non-technical viewer. When something fails on camera, leave it in and narrate it.

---

## [0:00 - 0:35] Hook - cold open

[SHOW: Terminal, fullscreen, already open. No face. Cursor blinking.]

This is my actual morning.

[NOTE: Type it live. Don't paste. The typing is the proof.]

[SHOW: typing `/gmail unread from the last 24 hours`, then enter]

That's my real inbox. Not a demo account.

[SHOW: output beginning to stream in]

While that runs - I used to do this by hand. Open Gmail. Open Skool. Open YouTube Studio. Three tabs, about twenty minutes, every single morning. Before I'd done one thing that actually mattered.

Now it's three commands.

And by the end of this video, you'll have built one yourself. Without writing any code.

[SHOW: cut to face for the first time]

Let's go.

---

## [0:35 - 1:20] The confession + what a skill actually is

[SHOW: face, then cut to `ls ~/.claude/skills` output scrolling]

Quick confession. I've built fifty-one of these things.

[NOTE: verify the real number on film day. Say the true number.]

I use three of them before nine in the morning.

So let me kill the biggest misconception right now, because it stopped me for months.

[SHOW: open a SKILL.md file in the editor. Scroll slowly. Don't explain the syntax yet.]

A skill is not code. It's a text file.

That's it. That's the whole thing. You write, in plain English, how you want a job done. You save it in a folder. And from then on the AI knows how to do that job.

[NOTE: pause here. This is the unlock for the non-technical viewer. Let it sit.]

If you can write an email, you can write one of these.

---

## [1:20 - 2:00] The promise + roadmap

[SHOW: simple three-item list on screen, or just talk to camera]

Three skills. Here's what each one replaced.

One - my inbox. Twenty-something emails overnight, and I need to know which two matter.

Two - my community. Who joined, who's gone quiet, who's about to leave.

Three - my channel. What happened to my videos while I was asleep.

And then at the end, the part I actually want you to steal - I'm going to build a fourth skill, live, that runs all three of those with a single command.

[NOTE: this roadmap is what the reference video never gave. Four disconnected agents with no system. Say the word "system" out loud here.]

That's the system. Let's do the first one.

---

## [2:00 - 5:15] Skill 1: Email

[SHOW: back to terminal, the `/gmail` output from the cold open now fully landed]

Okay, this finished while I was talking.

[SHOW: scroll through the actual grouped output. Redact anything sensitive in post with a blur, not by using a fake inbox.]

[NOTE: this is the moment the video earns its trust. Real names, real subjects, blurred where needed. Do NOT swap in a demo account. The whole differentiation is here.]

Look at what it did. It didn't just list my email. It sorted it.

[SHOW: point at the categories on screen]

That's the part people miss. Anyone can ask an AI to read their inbox. The skill is the instructions for *what to do* with it - which buckets, what counts as urgent, what I want back.

[SHOW: cut to the gmail SKILL.md, highlight the description line]

Here's the file that makes that happen. That line right there is how Claude knows to reach for this skill when I say "check my inbox." I never have to remember a command name.

[NOTE: 15 seconds max on the file here. The full teardown comes at 10:00. Don't front-load it.]

Now the honest part.

[SHOW: whatever it actually got wrong - a miscategorized email, a newsletter marked urgent, anything]

It put that in the wrong bucket. That's a newsletter, not something I need to answer.

That happens. And the fix isn't to abandon the whole thing - it's one line in the text file.

[NOTE: if nothing fails on the take, do NOT fabricate one. Instead say: "It gets this wrong maybe one in five mornings, usually newsletters. When it does, I add a line to the file." Honesty is the asset. Don't stage a bug.]

One thing I want to be clear about, because I get asked. This reads my email. It does not send anything. I set it up that way on purpose, and if you're a little uneasy about pointing AI at your inbox - good. Stay uneasy for a while. Let it earn it.

[NOTE: this is borrowed from the reference video and it's the single best line in it. Worth keeping because it's genuinely true.]

Email, done. About forty seconds. Used to be eight minutes.

---

## [5:15 - 8:15] Skill 2: Community

[SHOW: terminal, type `/skool community health`]

Second one. This is my Skool community.

[SHOW: real output - member counts, at-risk members, pending requests]

[NOTE: real numbers on screen. Blur individual member names if you're not comfortable, but leave the counts. The counts are the proof.]

Here's what I actually care about in the morning. Not the total member count - that number doesn't change fast enough to check daily.

[SHOW: point at the at-risk / churned section]

This. Who's gone quiet. Because that's the one where showing up a day early actually changes the outcome.

[NOTE: this is a genuine insight, not filler. It's the thing a dashboard can't tell you and it's why a skill beats a dashboard.]

That used to be me clicking through the members tab, sorting by last active, trying to eyeball it. Call it six or seven minutes and I'd do it maybe twice a week, honestly.

Now it's every morning, and it takes as long as it takes me to read four lines.

[SHOW: the pending join requests section, if any]

And it surfaces these, which I used to miss for days at a time.

[NOTE: if there are zero pending requests on film day, say so plainly - "nothing pending today, which is its own useful answer." Do not re-shoot to get a fuller screen.]

---

## [8:15 - 10:30] Skill 3: Channel numbers

[SHOW: terminal, type `/yt-analytics`]

Third one. This is the one I was worst at doing consistently.

[SHOW: real analytics output - views, CTR, retention, top videos]

[NOTE: real channel data. This is the most exposing of the three and also the most credible. Leave the numbers in.]

Here's why the skill beats just opening YouTube Studio, and it's not the time.

It's that Studio shows me everything, and I don't need everything at seven in the morning. I need to know if something moved.

[SHOW: point at whatever actually moved - a CTR change, a video over-performing]

That. That's a decision I can make before breakfast. Everything else on the Studio dashboard is a decision for Sunday.

[NOTE: strong line. Slow down on "a decision for Sunday."]

And this is the one where I want to show you the honest number, because I think people oversell this stuff.

[SHOW: face]

This didn't make me a better YouTuber. It made me a *consistent* one. I check my numbers every day now instead of twice a week and panicking. That's the actual benefit. It's smaller than "automate your life" and it's real.

[NOTE: this is the anti-hype beat. It's what separates the video from the 241K one. Don't cut it for time.]

---

## [10:30 - 14:00] Build the fourth skill, live

[SHOW: face, then terminal]

Okay. Three skills, three commands, maybe two minutes total.

But I'm still typing three commands. Let's fix that. Live, right now, no code.

[SHOW: type `use skill-creator to build me a morning skill`]

This is Claude's own skill for building skills. It's going to interview me.

[NOTE: this is the segment the whole video is selling. Slow down. Let the interview actually play out. If it asks four questions, show all four.]

[SHOW: the interview questions landing one at a time, and your answers typed live]

Watch what it's asking. It's not asking me for code. It's asking me what the job is.

[SHOW: answer along the lines of: "Run my gmail check, my skool community health, and my youtube analytics, in that order, and give me one combined summary at the end with anything that needs a decision today."]

That's it. That's the whole specification. Plain English.

[SHOW: the generated SKILL.md appearing, then open it in the editor, fullscreen]

And here's what it made.

[NOTE: this is the SKILL.md moment. Fullscreen, readable font, scroll slowly. Spend 45-60 seconds here.]

Let me walk you through this, because once you can read one of these you can write one.

[SHOW: highlight the frontmatter block]

Top part. Name, and a description. The description is the important one - that's how Claude decides when to reach for this skill. Notice it lists the phrases I might say.

[SHOW: highlight the body]

Bottom part. The instructions. In English. That's what it does when it runs.

[NOTE: do not explain YAML. Do not say "frontmatter" without immediately saying "the top part." Non-technical audience.]

And here's the thing nobody tells you, which is the answer to "doesn't having fifty-one of these slow it down?"

It doesn't load all of them. It only reads the name and the description at startup - a couple of lines each. It only opens the full file when it actually needs it.

[NOTE: this is progressive disclosure. Explain it exactly this way. Do not use the term unless you immediately define it.]

So you can have a hundred of these and it costs you almost nothing.

Now let's run it.

[SHOW: type `/morning`]

[NOTE: DEAD AIR WARNING - this will take longer than the individual skills because it's running all three. Fill it with the arithmetic from hooks.md option C: twenty minutes a day, five days, an hour and forty a week, that's a video I didn't film.]

[SHOW: the combined output landing]

One command. All three. One summary at the bottom with the things that actually need me today.

[NOTE: if the combined skill misfires on the first run - and there's a real chance it does - LEAVE IT IN. Fix it on camera. That's the most valuable 90 seconds in the video and no competitor has it.]

---

## [14:00 - 15:00] Close + CTA

[SHOW: face]

So that's the morning. Three skills I already had, one I built in about three minutes while you watched.

Here's what I'd actually tell you to do, and it's not "go build fifty-one skills."

[NOTE: direct callback to the confession. Land it.]

Pick the one thing you check every single morning. Just one. The tab you open before you've decided to open it.

Build a skill for that. Use skill-creator, exactly like I did. Give it twenty minutes.

If it sticks for a week, build the second one.

That's how I got to three. Not by planning a system - by replacing one tab at a time.

[SHOW: face, direct to camera]

The fifty-one skills are the part of my setup that looks impressive. The three are the part that actually changed anything.

If you want the SKILL.md files from this video, they're linked below.

[NOTE: only say this if you're actually going to publish them. If not, cut the line.]

And if you want to see the rest of the system - the stuff that runs after nine - that's the next video.

See you there.

[NOTE: end clean. No long outro. The reference video's 2-minute philosophical close is the weakest part of it and this audience doesn't need one.]

---

## Cut-for-time priority

If it runs long, cut in this order:
1. The roadmap at 1:20 (compress to two sentences)
2. The pending-join-requests beat in Skill 2
3. The "why not just open Studio" explanation in Skill 3 (keep "a decision for Sunday")

**Never cut:** the failure moment in Skill 1, the honest-benefit beat at the end of Skill 3, the SKILL.md walkthrough, or the "one tab at a time" close. Those four are the video.
