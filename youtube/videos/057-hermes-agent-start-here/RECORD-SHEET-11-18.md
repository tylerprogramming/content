# 057 Record Sheet, sections 11 to 18 (10:30 to 30:00)

Film from this page. Left = say. Right = do. No em dashes, no hype words. Count on camera when you name a count.

Pre-roll for this half
- Title-check chat exists (tonight's session) and `~/.hermes/skills/title-check/SKILL.md` exists. Open both in tabs.
- Coder profile DELETED before §15 so New Agent is real: `rm -rf ~/.hermes/profiles/coder` (Slack env re-copy after).
- Coder SOUL text on a card next to you (below in §15).
- Routines pane open in Bots tab. Phone ready for the cron card.
- `ollama list` shows gemma4:e4b and qwen3.8. Model picker shows both.
- Researcher's chat open. Packager and Coder primed with Bot Chat.
- Second creator transcript queued for the parallel beat (Greg Isenberg).

---

## 11. Skills (10:30 to 14:00)

| Say | Do |
|---|---|
| You see, Hermes advertises itself as the agent that grows with you. What that means is it learns as you work with it, it develops skills over time. So what are skills? Think of a skill as an instruction manual for completing a task. If you've built a Claude Code skill, it's the same idea. A markdown file. | Camera |
| If you go to Capabilities and look at Skills, you can see the pre-built ones Hermes already has. Different categories. Apple Notes, Reminders, iMessage. Research, there's one for papers. GitHub, a whole set. There are a lot, check them out. But what makes Hermes famous is that as you work with it, it learns these skills by itself, and you can teach it new ones. | Capabilities → Skills tab. Scroll categories. |
| Here, for example, in this conversation, I asked Hermes to look at my last ten uploads and tell me which title pattern is winning. | Open the title-check session. Scroll the table. |
| So it pulled the numbers, and it told me something I had wrong. I thought "I Automated My Something" was my winning lane. It isn't. The winner is a named tool up front, second person, and a small number. Three point five percent click-through versus two point four. Then it gave me five titles for this exact video, scored one to ten. | Point at the CTR numbers, then the 5 titles |
| Here's where I want to draw your attention. I then said: | |
| | Scroll to: `Make this into a skill for checking my titles.` |
| And it made the skill. You can see the description, what it's supposed to do. And how Hermes should use it in the future: pull the last ten, find the pattern, score new titles against it. | Open `~/.hermes/skills/title-check/SKILL.md` |
| So now I have that skill, and I can do slash title-check. | New chat |
| | `/title-check Hermes Agent setup video for Claude Code users` |
| It says the user has invoked title-check. And it gives me scored titles, same format, without me explaining anything. | Let it run |
| One more thing for the Claude Code people. I've got a folder of skills I built there. I asked Hermes to port them, and it wrote itself a skill for porting skills. | Capabilities → Skills → point at `claude-to-hermes-skill-porting` |
| So don't rebuild anything. Bring it over. Now, one more major feature, which is cron jobs, or scheduled tasks. | Camera |

## 12. Cron (14:00 to 16:00)

| Say | Do |
|---|---|
| A cron job is a scheduled task that runs automatically at certain times without you triggering it. A lot of things in life are recurring. Every day you get up, you check the same things. On the computer it's the same. You want the same things done every day or every week. That's what cron jobs are for. | Camera |
| | Terminal: `hermes cron list` |
| One example: every weekday at eight, this one reads my product's ClickUp board and sends me a brief on Slack. What's due, what's stalled, what to pick up. Another one at nine every night tells me what to film next. And this one, my code review agent, checks my repos every morning and only pings me if something's red. That's the one you saw at the top of the video. | Point at each row and its `Last run: ok` |
| Let me make one. You can do it in the app. Bots tab, Routines, New. | Bots tab → Routines → New. Weekdays 8am. Deliver: Slack. |
| | Prompt: `Check tylerprogramming/skoolos and jarvis-public: commits in the last 24h, failed CI, open PRs. Review any commit over 30 lines with code-review. Lead with the one thing that matters. If everything's green say exactly: All green. Nothing needs you.` |
| A cron is three things. A schedule, a prompt, and where to deliver. Two things worth knowing. Every run is a fresh session, so the prompt has to stand on its own. And it checks the model key, the skill, and Slack before it ever fires. | Save |
| | Terminal: `coder cron run "coder: morning repo check"` |
| That's what lands on my phone. | Phone: card lands. Hold 3 seconds. |
| Now, one honest thing. Hermes is a process. It only runs while this machine is awake. That's why you don't run it on your laptop for this. Mac mini in the corner, a five dollar server, or turn on keep computer awake. | Settings → Advanced → Keep computer awake |
| Great. We've covered the major features. Now there's one more concept I've separated into its own section because it's so important. Memory. | Camera |

## 13. Memory deep dive (16:00 to 18:30)

| Say | Do |
|---|---|
| If you've used other agents, you've probably gotten frustrated at some point because of memory. It forgets things. It gets slow. This all has to do with memory management. Hermes has a good memory system, and for most people the default is fine. But there are two things you can do to get a lot more out of it. First, let me cover the default. | Camera |
| The memory system is two tiers. You've already seen the first one. It's three files. MEMORY dot MD, important information about the setup, where things live, what's in progress. USER dot MD, that's you. And SOUL dot MD, up here, that's the agent, so it knows who it is. | Finder: `~/.hermes/memories/` then up one level to `~/.hermes/SOUL.md` |
| Each of these is kept deliberately brief. Here's the part nobody explains: they're capped. About two thousand characters each. | Click the context meter in the status bar. Point at memory's share. |
| Because these load into every single session. Every message. So they have to stay small or you'd pay for your whole history every time you type. Tiny profile, always on. | |
| But what if you want something more specific? That's tier two. Hermes has a tool called session search that looks through every conversation you've ever had. Stored in a SQLite database. Twenty-two thousand messages in mine. It doesn't read them unless it needs to. Unlimited archive, on demand. That's the whole design. | Terminal: `ls -la ~/.hermes/state.db` |
| Let me show you this in action. Start a new session. | New chat |
| | `Based on everything you know about how I work, draft the outline for my next video. Don't ask me any questions first.` |
| You can see it searching past sessions. And it gives me an outline in my format, sections, timings, the kind of demos I do. One sentence, no context. It didn't ask me anything, because it didn't need to. | Point at the session_search tool call, then the outline |
| That's the difference between an agent that stores things and an agent that uses them. | |
| | `/journey` |
| And this is everything it's learned, over time. Every skill, every memory. You can scrub it. | Scrub the graph |
| So these two tiers are already pretty good. But if you want to push it up two notches, there are two things you can do, and neither one needs an account. | Camera |

## 14. Making memory better (18:30 to 20:00)

| Say | Do |
|---|---|
| First, it can learn on its own. After every turn, a second copy of the agent reads what just happened and decides if it learned something about you. It's already on. I just pointed it at a small local model so it's free. | Terminal |
| | `hermes config get auxiliary.background_review` |
| Runs on gemma, on this machine. Now open MEMORY dot MD again. | Open MEMORY.md. Point at a tool-pitfall line. |
| Neither of us typed that. It hit a problem, figured out the fix, and saved it. That's the growing-with-you part, and it's a config line. | |
| Second, and this is the one I'd actually turn on. Make it ask before it writes. | |
| | `hermes config set memory.write_approval true` |
| Now instead of writing straight to the file, it queues the change. | In chat: `/memory pending` |
| And you review it. Nothing goes into your agent's head without you seeing it first. Memory with a code review step. | Approve one |
| Now people ask why the memory file is so small when I've done so much with this thing. Look where the knowledge actually went. | |
| | `open ~/.hermes/skills/software-development/attend-skool-crm/` |
| Fourteen files. My VPS, my Skool setup, my dashboard rules, my Slack format. It wrote all of this. And it only loads when I'm working on that product. Memory is the pointer. Skills are the how. Tiny profile always on, and the big stuff only when it matters. | Count the files on camera |
| There's a ceiling above this, an external memory service, or an Obsidian vault. I'm not setting those up here. What you just saw is the default, needs no accounts, and it's enough. | Camera |

## 15. Profiles = bots (20:00 to 24:00)

| Say | Do |
|---|---|
| Now here's the fourth thing, and it's the one I didn't know about when I started. You can have more than one of these. And a bot is just a folder. | Camera |
| See this tab, Bots, next to Sessions. That's my roster. Let me make a new one. | Bots tab → New Agent |
| | Name `coder` · Title `Coder` · Description `Engineering bot: reviews PRs, watches CI, opens small PRs on my repos.` |
| Create. And it introduces itself. | Create |
| | `open ~/.hermes/profiles/coder/` |
| That's it. That's the bot. Its own SOUL, its own memory folder, its own skills, its own chat history. Nothing shared with the main one. Which means it can run a different model, have different tools, and know different things. | Finder, point at each folder |
| Give it a personality. Right-click, Edit Profile. | Right-click Coder → Edit Profile → SOUL |
| | Paste SOUL (card): `You are Coder, Tyler's engineering bot. You review PRs and commits on tylerprogramming repos, watch CI, and open small PRs when asked. Lead with the one finding that matters. File and line, quote the code. Never merge without Tyler's word. Short, direct, no hype.` |
| And teach it what it needs to know, same as we did with the first one. | Coder's chat |
| | `Remember: my repos are tylerprogramming/skoolos, that's Attend, and jarvis-public. gh is authenticated as me. Never merge without my word.` |
| | `Review the latest commit on tylerprogramming/skoolos. Fetch it with gh. File and line, quote the code. Don't post to GitHub.` |
| Real findings. It read the actual diff, checked the prices in the README against the code, and flagged a stale comment. That's a review I'd take. | Speed-ramp the wait, land on the findings |
| | `Make this into a skill called code-review.` |
| Same move as before. Now every time this bot reviews, it uses the same checklist. | |
| | Terminal: `hermes -p coder chat` |
| Everything in the app has a terminal twin. Dash p, the profile name. Same agent. | Type one line, exit |
| And remember this row from Settings? Now it does something. | Cmd+, → Applies to chips |
| Every setting is per bot. Coder can be on a cheap model. The research one can be on a big one. Pick the one you're editing here. | Click Coder chip, point at Model |
| So that's four. Hermes, my main one. Coder. And two more you'll meet at the end, one that does research and one that builds my video packages. Each is a folder. Each has a job. | Bots tab, 4 avatars |

## 16. Local + free (24:00 to 26:00)

| Say | Do |
|---|---|
| Okay, one more topic for your setup that lays the foundation for everything else. Open source AI. This is optional. If you're happy paying for a frontier model, that's totally fine. But for me, I'm not willing to spend that much. So I run local models, downloaded onto this Mac, completely private, and everything stays in this box. | Camera |
| And by the way, that's what I've been using this whole time. The memory review, the code review, all local. | |
| Easiest way is Ollama. Go to ollama dot com, download it. Then in the launch tab, Hermes is right there. | Browser: ollama.com |
| | Terminal: `ollama launch hermes` |
| Or the one gotcha, if you set it up by hand: agents need a big context window and Ollama doesn't report one. Set it yourself. | |
| | `OLLAMA_CONTEXT_LENGTH=64000 ollama serve` |
| Then pick it in the model picker. I've got two here. Gemma, small and fast. Qwen, bigger, and it can see images. | Composer picker → gemma4:e4b |
| Now always test that it actually uses tools, not just chats. | |
| | `List the files in ~/content/youtube/videos, read the newest STATE.md, and tell me what's next.` |
| Reads the folder, reads the file, answers. Tools working, offline. | Point at the two tool calls |
| Model on my machine. Memory on my machine. Nothing leaves. For anyone who cares about privacy, or cost, this is the setup. Alright. Congratulations for making it this far. Now let me show you what you can build once you've laid this foundation. | Camera |

## 17. The payoff (26:00 to 29:30)

| Say | Do |
|---|---|
| So for the last part, I'm going to show you what you can build once you've laid this foundation. This is my multi-agent setup. This is where I do research and build my video packages. Let's actually build something together so you can see how it works. | Camera |
| Here's the roster. Coder, you just met. Researcher, same six steps, I made it earlier. Packager, same again. And the way they work together is you just talk to one of them. | Bots tab → open Researcher's chat |
| Recently I've been prepping this exact video. Researcher already pulled the top twenty Hermes videos and broke down the best one, beat by beat. So let me say: | Scroll Researcher's history briefly |
| | `@packager build the package for video 057 from the research you have. When it's done, @coder opens a PR with it on tylerprogramming/content and posts the link to Slack.` |
| Click enter. Cool. Watch the strip up here. Researcher hands it to Packager. Packager's working. | Active-now strip: Packager chip lights. Speed-ramp. |
| It says it's on it, and it'll let me know when it's ready. And hey, look at that. | Packager reply: folder, title, hook |
| Now Packager hands to Coder. Coder's chip. It's opening the PR. | Coder chip lights |
| This is the git review pane. Last turn, that's only what the agent just touched. Eight new files in the package folder. Commit, push, PR. | Cmd+G in the content repo. Last turn filter. |
| | Browser: the PR on GitHub |
| And on my phone. | Phone: Slack, Coder's message with PR link |
| Three bots. One sentence from me. A real pull request I can review, and it told me where it is. So yeah, that is a full build using the Bots tab. | Hold on phone |
| One thing worth knowing. This handoff works from a bot's chat in the app. From Slack, one bot can't hand to another yet. So the way I think about it: the desktop is where you talk to a bot. Slack is where bots talk to you. | Camera |
| Since it's a multi-agent system, you can also come back and ask it to do other things at the same time. Like, hey Researcher, break down the second video on that list. And Coder, review my last commit. And they'll work in parallel. | Type both in their chats. Both chips light. |
| Once you get to this stage, Hermes also has a native board, kanban, where you can orchestrate all of them and coordinate the work. That's the next video. | |

## 18. Outro (29:30 to 30:00)

| Say | Do |
|---|---|
| So here's how I think about it as a software engineer. This is not Claude Code versus Hermes. I run both. Claude Code is the specialist. I open it when I'm writing serious code. Hermes is the staff that's already there. | Camera |
| If you set up just those four things. Memory. A skill it wrote itself. One cron on a machine that stays on. And a second bot with a job. You already have something most people never get to. | Four-things card |
| Everything I showed you is running on mine right now. That's not a demo I built for the video. That's the setup. | |
| If you want to see the multi-agent side go deeper, the board, bots on other machines, let me know in the comments. I'm happy to go there. And the setup notes and every command from this video are in the free community, link below. | |
| Tell me in the comments what you're going to build with yours. I read every one. See you in the next one. | End card |

---

Still unproven before §17 rolls (mine): Packager → Coder leg, Coder actually opening the PR. Do a dry run once.
