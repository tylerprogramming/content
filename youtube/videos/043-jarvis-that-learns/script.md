# Script: I Built an AI Assistant That Learns From Its Own Mistakes

Target 14 to 16 minutes. Four demos, one idea. The idea is the feedback loop.
Everything else is supporting evidence.

---

## [0:00 - 0:30] Hook

> So this is a text file my assistant wrote about my own channel.

[SHOW: brain.md open, scroll slowly to a dated rule]

> It says showcase videos beat tutorials for me, confirmed on July 30th. I did
> not write that line. An agent did, after it looked at how the last video
> actually performed. And then it went back and updated a rule it had written
> the week before.

> That is the part everyone skips. There are a bunch of Claude Code assistants
> out there now, and I have looked at most of them. They all produce stuff.
> None of them ever check whether the stuff worked.

> So I built one that does. It is free, it is on GitHub, and I am going to show
> you the whole thing.

[NOTE: no logo sting, no "in this video". Straight into the HUD.]

---

## [0:30 - 2:00] What it is

[SHOW: the HUD, full screen, let it breathe for a beat]

> So this is it. It runs on my machine, on localhost. There is no cloud, no
> account, nothing hosted anywhere.

> On the left, my actual numbers. Subscribers, the latest video, how it is
> pacing. Underneath that, the top few things I should do today. Underneath
> that, channels I watch. And down there, everything my agents have written.

> Around the middle, those are the agents. Six of them, each on a schedule.

[SHOW: hover an agent so the tooltip appears]

> And that bar at the bottom is Claude Code. I can type or I can talk, and it
> reads all of this before it answers.

> I want to be upfront about one thing. A dashboard for Claude Code is not a
> new idea. There is a project called OpenPaw that does the scheduling side
> really well. What I have not seen anywhere is the loop, so that is what most
> of this video is about.

[NOTE: name OpenPaw genuinely. Conceding the obvious point early buys the rest.]

---

## [2:00 - 4:30] Demo 1: ask it something real

> Let me just ask it something.

[SHOW: type into the command bar: "how am I tracking this week?"]

[NOTE: let the tool chip appear on screen. Do not talk over the first two
seconds, let people see it decide to read a file.]

> So it went and read the actual file. It is not guessing, and it is not
> pulling from training data. It opened vitals.json, which is a file on my
> disk that got refreshed this morning.

[SHOW: the answer streaming in]

> And I can talk to it instead.

[SHOW: click the mic, say "what did radar find this morning?"]

> That transcription happened on my machine too. That is whisper.cpp, running
> locally. The audio does not go anywhere.

> Which honestly took me three tries to get working, and I will come back to
> that, because the way it failed is the interesting part.

[NOTE: plant the bug story here, pay it off at 11:00.]

---

## [4:30 - 7:00] Demo 2: the agents, and the one that matters

> So there are six agents. Let me show you what one actually is.

[SHOW: open agents/postmortem.md in an editor]

> It is a markdown file. That is the whole thing. There is a bit of config at
> the top saying when to run and what tools it is allowed to use, and then the
> rest is just instructions in plain English.

> If you want a new agent, you write a new file. There is no code.

[SHOW: scroll to the schedule line]

> This one runs at 8am every day. And it survives a reboot, which sounds like a
> small thing, but a lot of these setups only run while your laptop is open.
> This one goes into launchd on a Mac, or cron on Linux.

> Now here is the one that matters.

[SHOW: postmortem.md, the step about updating the playbook]

> Every video I put out, this thing looks at it twice. Once at 48 hours, once
> at a week. It compares it to my own recent videos, not to some benchmark. And
> then it does the part nobody else does.

[SHOW: brain.md side by side]

> It opens my playbook, and it either confirms a rule that is already in there,
> or it contradicts one, and it writes down the evidence and the date.

> So next week, when it goes to pick a topic, it reads this file first. The
> thing it learned last week is sitting right there.

> That is it. That is the whole trick. It is not fancy, it is one file that
> gets edited by the thing that learned something.

[NOTE: slow down here. This is the thesis. Do not rush it.]

---

## [7:00 - 9:30] Demo 3: run one live

> Let me actually run one instead of talking about it.

[SHOW: click RADAR on the agent ring]

> So radar watches ten channels. And the thing it is doing is not looking for
> videos with a lot of views, because a big channel always has a lot of views.
> It compares every video to what that channel normally does.

[NOTE: while it runs, fill with the explanation below. Sweep takes about three
minutes, so cut this down in the edit.]

> So if a channel usually does three thousand views a day and one video is
> doing forty thousand, that is the topic carrying it, not the audience. That
> is worth knowing about. A big channel doing big numbers is not.

[SHOW: the report appearing in the documents panel]

> And there it is. It wrote a report, and it named a topic two different
> channels broke out on in the same week, which is a much stronger signal than
> one channel doing well.

[SHOW: open the report, scroll]

> That file has a proper title, a date, and the numbers it based it on. All the
> agents write to the same convention, so this folder stays readable when there
> are a hundred of these in it.

---

## [9:30 - 11:00] Demo 4: voice, free and local

> Okay, the voice.

[SHOW: terminal, jarvis voice install]

> There are two ways to run this. If you have Docker it uses Docker. If you do
> not, and most people do not, it installs it natively instead.

> That was the whole reason I built the second path. Every guide for this says
> install Docker first, and that is where people stop.

[SHOW: jarvis voice start, then trigger a spoken reply]

> And that is Kokoro. It is free, it runs on this machine, and there is no API
> key anywhere.

> I do have an ElevenLabs key, and honestly ElevenLabs sounds better. But the
> point is you do not need one. It falls back through a chain, so it uses the
> best thing you have got and never breaks if you have got nothing.

[NOTE: be honest that ElevenLabs is better. It costs nothing to admit and it is
the kind of thing people notice if you skip it.]

---

## [11:00 - 13:00] The part where it did not work

> So I said I would come back to the microphone.

> When I first wired up local Whisper, it said it was working. The status
> screen said ready. And every single time I talked to it, it quietly used the
> browser instead, which sends your audio to Google.

[SHOW: the doctor output saying "yes"]

> There were three bugs stacked on top of each other. The config had a tilde in
> the path, and because we run the program directly instead of through a shell,
> nothing expanded it, so it was looking for a folder literally called tilde.

> Then the status check was only looking for the program, not the model file.
> So it said ready when it absolutely was not.

> And then the temp files were named with a timestamp, so when two of them got
> made in the same millisecond they had the same name, and ffmpeg was being
> asked to read and write the same file.

> The reason I am showing you this is that none of it threw an error. It just
> quietly did the wrong thing and told me it was fine.

> So if you build one of these, test the thing end to end. Do not trust a
> status light you wrote yourself.

[NOTE: this section is the trust builder. It is also the most "him" part of the
video. Do not cut it for time, cut the radar wait instead.]

---

## [13:00 - 14:30] How to get it

> So it is on GitHub, it is public domain, and there is nothing to buy. Clone
> it, run setup, and it asks you a handful of questions.

[SHOW: npm run setup, quickly]

> You need Claude Code for the best version of this. But if you do not have a
> subscription, it also runs on any OpenAI-compatible endpoint, including
> Ollama on your own machine, so it works with nothing paid at all.

> Link is in the description.

> Now, setting the whole thing up with your own channels and your own agents,
> that takes a bit longer than I can fit here. So I did a full walkthrough of
> that inside my community, link is also down there. But the code itself is
> free either way, and you do not need me to run it.

[NOTE: say this plainly, one time, then move on. No pitch tone.]

---

## [14:30 - 15:30] Close

> So the whole point of all this is the loop.

> Every one of these assistants can produce things for you. That part is kind
> of solved now. What almost none of them do is look at what happened
> afterwards and change how they work because of it.

> And it turns out that is not a hard thing to build. It is one agent, and one
> text file it is allowed to edit.

> So if you already have some automation running, whatever it is, pick the one
> thing you would want it to get better at, and give it somewhere to write down
> what it learned. Start there.

> Tell me in the comments what you would have yours learn first. I read all of
> them.

[NOTE: soft close, real question, no hard CTA.]
