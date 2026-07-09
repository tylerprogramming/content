# Script - "I Automated My YouTube Comments With Claude Code"

Target runtime: 10-14 minutes. Tyler's voice: practical, direct, honest. No em dashes anywhere. Hero CTA is https://free.tylerai.dev/youtube/. Skool is a soft secondary, mentioned once.

Structure follows the 3-layer spine: Showcase, System, Opportunity. The three live demos are the backbone: (1) pull unreplied comments, (2) review the auto-drafted replies, (3) post them via the API, dry-run first then live.

---

## 0:00 - Cold open (word for word)
[B-roll: scroll a real wall of unreplied comments across recent uploads. Desaturated, overwhelming. Then cut to one comment getting a real reply posted with a green check.]

"This is every comment on my channel I never replied to. For months I told myself I would get to them, and I never did. Watch this."

[Cut to terminal. Claude pulls the unreplied ones, drafts replies, Tyler approves, they post live. Fast montage, 3 seconds.]

"I did not hire anyone. I did not fake a single reply. I built one system with Claude Code that finds the comments I missed and helps me actually answer them. And by the end of this video you are going to know exactly how it works, because I am going to show you the whole thing running on my real channel."

[Title card / quick logo sting.]

---

## 0:35 - The problem (why this matters)
"Okay so here is the honest truth about running a channel. Replying to your comments matters. The algorithm watches engagement. Your community notices when you show up and answer them. It is one of the highest-leverage things you can do, and it is free.

And I was still terrible at it. Not because I do not care, but because the tracking is miserable. I have got comments coming in across a bunch of different videos. Some I already answered. Some I meant to answer three weeks ago. Some are questions I actually want to reply to, and some are just people being nice. And YouTube Studio does not make it easy to see, at a glance, here is everything you have not gotten back to yet.

So what happens is you open Studio, you feel overwhelmed, you reply to like two, and you close the tab. That was me for months.

Now, the wrong fix here is a bot. You have seen these. Somebody automates their comments and suddenly every video has fifty replies that just say Great video, love this, so helpful. That is fake engagement. It looks like a person phoning it in, because it is worse than a person phoning it in. It actively makes your channel feel hollow, and I did not want any part of that.

So I did not automate the caring. I automated the tracking. Let me show you the difference."

---

## 1:45 - The showcase (what I built, high level)
"Here is what I built. It is a Claude Code skill I call yt-replier, and it does three things.

One, it runs on its own in the background and finds every comment on my recent uploads that I have not replied to yet. It writes them into an inbox file so I have one clean list instead of digging through Studio.

Two, for comments that are clearly asking about my community or a resource, it drafts a reply for me. I read it, I edit it if I want, and only then does it go anywhere.

Three, when I approve, it posts the reply through the official YouTube Data API. Not a browser bot clicking around. The real, sanctioned API that YouTube gives developers.

And the whole thing is human-in-the-loop. Claude drafts, I approve, it posts. Nothing goes out that I have not read. I want to be really clear about that up front, because that is the entire point. The tedious part is automated. The human part stays human.

Let me actually show you, because talking about it is boring. Let me run it."

---

## 3:00 - Demo 1: Pull the unreplied comments
[Screen: VS Code with Claude Code open. Tyler types into the terminal.]

"So I am just going to talk to Claude Code like I always do. I will say, pull my unreplied YouTube comments.

[Claude runs the monitor script. Show the terminal working. Then show the inbox file opening with the real list of comments.]

And there it is. This is running a script that hits the YouTube Data API, pulls the comments on my recent videos, checks each one against a list of what I have already replied to, and writes the ones I have not gotten to into this inbox file.

Look at this. These are all real comments on my channel. This person asked a genuine question about a skill. This one is just saying thanks. This one is asking where the community is. I did not have to open Studio, I did not have to remember which video, it is all just here in one list.

And here is the part that keeps it clean. This actually runs on a schedule. I have got it set to run every hour, on the seven minute mark, as a cron job. So even when I am not thinking about it, once an hour it quietly checks for new comments and updates this inbox. When I sit down, the list is already waiting for me. I am not the one doing the tracking anymore. The machine does the tracking. I do the replying."

---

## 4:45 - Demo 2: Review the auto-drafted replies
"Now here is the second piece, and this is where people get nervous, so watch closely.

For some of these comments, the system also drafts a reply. Specifically, when a comment hits certain keywords, like somebody asking where do I learn this or where is your community, it will draft a reply that points them to the right place. Those drafts go into a separate queue.

[Screen: open the drafts queue file. Show 2-3 drafted replies next to their original comments.]

But here is the thing. These are drafts. That is the whole word. Nothing here is posted. It is sitting in a file waiting for me to look at it.

So let me actually read them. This person asked where they can learn to build these skills. The draft points them to my community with a real, specific answer, not a generic one. That is good, I will keep it.

This one, the draft is a little too salesy for my taste. So I am just going to tell Claude, make this warmer and answer their actual question first before mentioning the community.

[Claude rewrites it. Show the updated draft.]

Better. See, this is the part that matters. I am reading every single one. If a reply does not sound like me, or it does not actually help the person, it does not go out. I would rather reply to ten comments like a real human than a hundred like a bot. The automation is not there to replace me in the conversation. It is there so I am not spending my Saturday hunting through Studio trying to remember who I already talked to."

---

## 6:30 - The honesty beat (core of the video)
[Tyler to camera, no screen. Slow down here. This is the trust anchor.]

"I want to pause on this, because it is the most important thing in the video.

It would be really easy to take this system and make it evil. I could remove the approval step. I could tell it to reply to every single comment automatically with something generic. I could pump my numbers overnight. And a lot of people do exactly that.

Do not do that. It does not work, and it will hurt you. People can smell a fake reply from a mile away. The algorithm is getting better at spotting it too. And more than any of that, the entire reason to reply to your comments is to actually connect with the people watching. If you automate away the connection, you have automated away the only thing that was worth doing.

So the rule I gave myself, and the rule I would give you, is this. Automate the tracking. Never automate the talking. Claude finds the comments and drafts a starting point. You still show up as a human. That line, right there, is the difference between a tool that grows your channel and a tool that quietly kills it."

---

## 7:30 - Demo 3: Post via the API, dry-run then live
"Okay, I have read my replies, I have edited the ones I wanted to edit. Now I post them. And even here, there is a safety net.

By default, this thing runs in dry-run mode. That means when I run the reply script, it shows me exactly what it would post and where, but it does not actually send anything. Watch.

[Screen: run the reply script in default mode. Terminal prints each reply and the comment it is responding to, with a clear DRY RUN label. Nothing is posted.]

See that. DRY RUN at the top. It is telling me, here is the reply, here is the comment it goes on, here is the video. And it stopped. Nothing hit YouTube. This is my last chance to catch anything weird before it is public.

Everything looks good. So now, and only now, I add the post flag.

[Screen: run the same command with --post. Terminal shows the API call going out. Show the real API response come back. Then cut to the actual YouTube comment section and refresh to show the reply is live.]

And there it goes. That just posted through the YouTube Data API, using the comments insert endpoint. And if I hop over to the actual video, refresh, there is my reply, live, on the real comment.

One more thing it does behind the scenes. It writes down every comment it has replied to. So the next time it runs, it will never reply to the same comment twice. No double replies, no awkward duplicates. It just knows what is done."

---

## 9:15 - Limitations (keep it honest)
"Let me be straight about what this is not, because I do not want you building it thinking it is magic.

This is not a hands-off machine. If you set it up expecting to never look at your comments again, you built the wrong thing, and honestly you missed the point. It still needs me. I read the drafts. I approve the posts. That is by design.

It also only auto-drafts for a narrow set of comments, the ones hitting specific keywords where the answer is predictable. The genuine questions, the interesting conversations, the ones where somebody disagrees with me, those I still write myself from scratch. The system just makes sure I see them.

And there is setup involved. You need API access set up through Google, you need to authorize your own channel, and you need to be comfortable running a script. It is not a one-click thing. But it is very much a Claude-Code-can-walk-you-through-it thing, which is kind of the whole magic of this stuff now.

So it is a tracking and drafting assistant with a hard human gate. That is it. And that is exactly what I wanted."

---

## 10:15 - The opportunity
"Now here is the part I want you to sit with, especially if you are trying to build something with these skills.

I built this for one channel. Mine. But think about who else has this exact problem. Every creator you know is drowning in comments they never answer. Every small brand with a social presence is leaving DMs and comments on read. Community management is a real job that real companies pay real money for, and most of it is exactly this. Tracking what came in, drafting good responses, keeping engagement genuine, and never letting something go out that should not.

You could take this pattern, the monitor that finds what is unreplied, the drafting step, the human approval, the posting through an official API, and offer it as a service. Comment and community management for creators or brands, powered by a system like this, with you as the human in the loop making sure it stays real.

I am not going to throw a fake number on the screen and tell you this makes you rich. I do not know your situation. But I know the problem is everywhere, I know people pay to have it solved, and I know most people solving it right now are either doing it fully by hand or doing it with spam bots. There is a real gap in the middle for someone who does it well and does it honestly. That could be you."

---

## 11:30 - CTA and close
"If you want to actually build stuff like this, I put together a free pack of the Claude Code resources I use, plus a newsletter where I break down what I am building each week. It is the first link in the description, free.tylerai.dev slash youtube. Go grab it, it is free.

[Optional single soft Skool mention.] And if you want to build alongside other people doing this, I have got a community too, but honestly start with the free pack first.

Here is what I would do if I were you. Pick the one repetitive thing on your channel or in your business that you keep avoiding. For me it was comments. For you it might be something else. And instead of forcing yourself to do it, ask whether the tracking part, the boring part, could be handled by a system, while you keep the human part that actually matters.

That is the whole game. Automate the tedious. Keep the human.

I will see you in the next one. And yeah, I am actually going to reply to your comment on this one."

[End screen: free.tylerai.dev/youtube plus a related video.]

---

## Filming notes
- The three demos must be real screen recordings on Tyler's actual channel. The live API response and the refreshed comment section are the payoff moments. Do not fake them.
- Keep the honesty beat (7:30) as a straight-to-camera segment with no screen. It should feel like Tyler leveling with the viewer, slower than the rest.
- Blur or get comfortable showing real commenter usernames. Prefer showing genuine positive or question comments, nothing embarrassing to a viewer.
- Total spoken content is tight for 10-14 minutes. If running long, trim the problem section (0:35) first, it can lose 20 seconds.
