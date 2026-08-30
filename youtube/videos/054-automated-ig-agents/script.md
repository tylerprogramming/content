# Script - 054 - I Fully Automated My Instagram With AI Agents

Target length: 10 to 14 minutes. Uses Hook A. Short spoken sentences. No em dashes, no hype.
[SHOW: ...] = what is on screen. [NOTE: ...] = production/direction note.

---

## 0:00 - 0:40 COLD OPEN (Hook A, verbatim from hooks.md)

[SHOW: screen-record, an Instagram post going live, then a comment reply landing. No face.]
This post on my Instagram, the caption, the images, the reply under it, I did not write any of it.

[SHOW: Claude Code terminal running, then the Blotato calendar filling in.]
Three AI agents did. One makes the content. One schedules and publishes it. One reads the
comments and DMs and writes the replies.

[SHOW: FACE REVEAL, slow push-in.]
And I never opened the Instagram app to do it.

Now before you close this. Nothing here posts on its own. Every post and every reply waits for
me to say go. The agents do the work. I still pull the trigger.

[SHOW: chips fly in, "creator" / "small brand" / "never coded"]
It does not matter if you run a brand account or you have never touched a terminal. The setup is
a folder of text files.

I have been a software engineer for eight years, IBM, then Chase, now I do AI at Pfizer, and I
still would not hand my account to a bot I could not check. So I built one I can.

[SHOW: "In this video" roadmap card, 1-2-3.]
In this video I am going to build all three agents in front of you. The content one, the
publishing one, and the inbox one. And I will show you the one guardrail that keeps the whole
thing from getting my account banned.

[SHOW: HARD CUT to the build.]
Let's start with the content agent.

---

## 0:40 - 1:40 THE SETUP (why a folder, not a bot)

[SHOW: a plain folder in the editor, a few markdown files inside: voice.md, ideas.md, a skill file.]
So here is the thing. When people hear "I automated my Instagram," they picture some sketchy bot
farm. This is not that. This is Claude Code, and the whole account lives in a folder.

[NOTE: webcam PIP stays bottom-right for every screen-share from here on.]

[SHOW: open voice.md, scroll it.]
One file is my voice. How I write, what I sound like, words I never use. Another file is a
running list of topics. And then there is a skill, which is just a markdown file that tells the
agent the steps to follow.

That is really it. No dashboard, no drag-and-drop builder. If you can edit a text file, you can
change how any of these agents behave.

[SHOW: highlight the three folders/agents.]
And I split it into three agents on purpose. One job each. Make the content. Publish it. Handle
the replies. When one job is one agent, it is easy to see what it did, and easy to fix when it
gets something wrong. Because it will get things wrong, and I will show you that too.

---

## 1:40 - 4:00 AGENT 1 - THE CONTENT AGENT

[SHOW: terminal, typing a prompt to Claude Code, "make a carousel about X".]
Okay. Agent one. I give it a topic. That is the only thing I have to do.

[SHOW: Claude Code reading voice.md, then drafting the carousel outline live.]
Watch what it does. First it reads my voice file. Then it writes the carousel, slide by slide.
It is not writing like a marketing brochure, it is writing like me, because I gave it me to
read first.

[NOTE: kinetic captions on this next line, color the contrast.]
This is the part that matters. The agent is only as good as the voice file you feed it. Garbage
voice file, garbage posts. A real one, and it sounds like you.

[SHOW: image generation kicking off, a couple of generated images appear in the folder.]
Then it makes the images. I have an image model wired in, so the same run that wrote the caption
also generates the visuals for the carousel. They land right here as files in the folder.

[SHOW: the finished post, caption plus images, side by side.]
And now I have a finished post. Caption, images, the whole thing. It took about a minute.

[NOTE: honesty beat, say it plainly.]
But I do not post it yet. I read it first. Sometimes it nails it. Sometimes a line is off and I
just tell it "make slide three shorter" and it fixes it. That back and forth, that is the normal
way to work with these. Do not expect a hundred percent on the first try. Expect eighty, and
nudge it the rest of the way.

[SHOW: quick before/after of a caption edit.]
See, that took ten seconds. Now it is right.

---

## 4:00 - 6:30 AGENT 2 - THE PUBLISHING AGENT (Blotato)

[SHOW: the approved post, then the Blotato MCP connection in the terminal.]
Agent two publishes it. And this used to be the hard part.

[SHOW: brief graphic, "Meta Graph API" with a tangle of arrows, app review, auth.]
If you go straight to Instagram's own API, you are signing up for an app review that can take
weeks, a business account tied to a Facebook page, and a container upload flow that is genuinely
annoying to get right. I have done it. I do not recommend starting there.

[SHOW: Blotato logo, then one clean arrow from Claude Code to Instagram.]
So I use Blotato instead. It sits in the middle. Claude Code hands the finished post to Blotato
over something called MCP, which is just a way for the agent to call a tool directly.

[SHOW: the blotato_create_post call running, then the post appearing on the calendar.]
One call. I tell it when to post, it puts it on the calendar, and it confirms it is queued.

[NOTE: this is a real value beat, let it breathe.]
And here is the part I like. The schedule runs on Blotato's side. So I can close my laptop. The
agent does not have to sit there running for the post to go out at the time I picked. It is
queued, it is out of my hands, it goes.

[SHOW: the same post, then it fans out to 8 other platform icons.]
Same call, by the way, can send it to nine platforms. So the carousel that agent one made can
hit Instagram, and TikTok, and LinkedIn, from one command. But we are staying on Instagram today.

[NOTE: keep the CTA folded in, then snap back.]
This is also the exact stack I use for real, so if you want the folder and the voice file I
start from, I keep those in my free Skool, link is below. Okay, back to it.

[SHOW: the calendar now has a week of posts on it.]
So now the content agent fills the folder, the publishing agent fills the calendar. That is half
the account already running. The other half is the part everybody skips.

---

## 6:30 - 9:30 AGENT 3 - THE INBOX AGENT (comments + DMs)

[SHOW: the Instagram inbox, comments and DMs stacking up.]
Agent three. This is the one that actually saves me the most time, because replying is the part
that never ends.

[SHOW: Claude Code reading the recent comments, then drafting replies in a list.]
So the inbox agent reads the recent comments and DMs, and it drafts a reply to each one. In my
voice, again, from the same voice file. It does not send them. It lines them up for me.

[SHOW: the approval list, Tyler approving three, editing one, skipping one.]
And this is where I stay in the loop hard. I go down the list. This one is good, send. This one
is good, send. This one it misread the tone, I fix it. This one is a troll, skip. Then it sends
the approved ones.

[NOTE: THE OPEN LOOP FROM THE HOOK CLOSES HERE. This is the guardrail.]
Now, the guardrail I promised you. This is the thing that breaks most of these setups, and it
bit me the first time.

[SHOW: graphic, "Instagram messaging rules" with three lines building in.]
Instagram does not let you just DM anyone you want from automation. Three rules. One, you can
only message someone who messaged you first. No cold outreach, ever. Two, you only have a
twenty-four hour window after they contact you, and after that the door closes. Three, there is
a cap, a couple hundred automated actions an hour, and if you blow past it, Instagram starts
flagging your account.

[SHOW: red-glow framing on a "flagged" example.]
I found this out the fun way. I had the agent replying to everything, fast, and Instagram did
not like the pace. So now the agent respects the window and paces itself. It only replies inside
that twenty-four hours, and it never cold-messages.

[NOTE: land the meaning, humble.]
And honestly, that guardrail is a good thing. It forces the whole system to stay human. The
agent can only answer people who reached out to me. It is helping me keep up, it is not out there
pretending to be me in strangers' DMs.

---

## 9:30 - 11:30 THE WHOLE THING RUNNING + THE HONEST LIMITS

[SHOW: all three agents in one view, a full loop, folder to calendar to inbox.]
So step back and look at the whole loop. Agent one makes the content. Agent two schedules and
publishes it. Agent three reads the replies and drafts the answers. And at three points, I say
go, on the post, on the schedule, on the replies.

[NOTE: repeat the honesty beat, it is the spine of the video.]
I want to be really clear about that, because the title says "fully automated" and I mean the
work, not the judgment. The making, the posting, the drafting, that is all off my plate. The
approving is not, and I did that on purpose. The day I let it post blind is the day it says
something dumb under my name.

[SHOW: quick montage of a couple of misses the agent made, captioned honestly.]
And it does miss. It wrote a caption last week that was just off. It misread a sarcastic comment
as a real question. That is normal. You are not building a thing that is perfect. You are
building a thing that gets you most of the way and asks you to check the last bit.

[SHOW: a rough "time" comparison, before/after, no exact numbers on screen as a claim.]
For me the whole point is this. The parts of Instagram that are just repetitive, make it, post
it, answer everyone, those are handled. The part that needs me, the judgment, I kept.

---

## 11:30 - 12:30 RECAP + CTA + OUTRO

[SHOW: three-card recap, one line each.]
So that is the build. Three agents. Content, out of a folder and a voice file. Publishing,
through Blotato with one call. Inbox, drafts you approve, inside Instagram's rules.

[SHOW: the folder one more time.]
And all of it is text files. No dashboard, no code you have to be scared of. If you can write
down how you want something done, you can build this.

[NOTE: soft CTA, Tyler's real voice, question not sell.]
If you want the starting folder, the voice file, and the skill, they are in my free Skool, link
in the description. Grab them and change them to sound like you.

[SHOW: face, direct.]
And tell me in the comments what part of your Instagram you would hand off first. The posting,
or the replying. I read every one. I will probably reply with the agent, and then approve it
myself.

[SHOW: end card.]
That is it. Go build one.

---

## Production notes (whole video)
- Face target: roughly 35% of the first two minutes, never bare and static longer than 5 to 7s.
- Webcam PIP on every screen-share so the face never fully disappears.
- New on-screen visual at least every ~5s; every ~1.5 to 2.5s in the first 30s.
- Every claim gets a synced visual within a second or two. Show the terminal, the calendar, the
  inbox live. Never describe what you could show.
- Open loop ("the one guardrail / ban") planted at 0:32, closed at ~8:00 with the messaging rules.
- Honesty beat (approval, human in the loop) stated at 0:11, reinforced ~4:40, landed ~9:45.
- Credibility (IBM/Chase/Pfizer) delayed to 0:24, framed as the reason for the guardrail.
- CTA folded into the Blotato section and again at the outro, then snap back. No dead-air asks.
