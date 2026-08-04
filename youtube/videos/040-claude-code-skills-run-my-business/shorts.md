# Shorts / Reels — 17 Skills (from 040)

**Source:** the 040 long-form, re-recorded 2026-07-31. Nine reels, all cuttable from that footage plus a few pickup shots.

**Rules for every one of these:**
- Lead with the demo. Command goes in, hard-cut to the finished result. No dead air, no "so today I'm going to show you."
- The talking is voiceover over the screen, not a talking head watching a spinner.
- Target 45-90s. The umbrella and the live-build can run to 2 min.
- Every skill named here is real and lives in `~/.claude/skills/`.
- End on the payoff line, not on a CTA. The CTA goes in the caption.

**Post order:** 1, 3, 5, 4, 2, 8, 6, 7, 9. Umbrella first, then alternate an idea reel with a demo reel so the feed does not read as one long tutorial.

---

## Reel 1 — "17 text files run my business" (umbrella, flagship)
**Pull from:** 0:00-0:35 hook + 0:35-1:30 montage
**Hook:** "This is the actual Claude Code that runs my content business. 17 skills, and none of it is code."
- **Show:** fast scroll of the skills list, then quick flashes of four outputs: a research report, a script file, a scheduled post, the Skool dashboard.
- Say: they find my ideas, write my videos, post everywhere, and answer my comments and email.
- **Payoff:** "They're just text files. If you can write instructions, you can build every one of these."
- **On-screen:** `17 skills. Zero code.`
- **Caption:** I run my whole content business out of one folder of text files. Here is what is in it.

## Reel 2 — "Everyone fakes these demos" (pattern interrupt)
**Pull from:** 0:00-0:35 hook + 0:35-1:30
**Hook:** "You've seen the videos where someone builds a fake business with Claude Code in one prompt. I'm not going to do that."
- **Show:** your real skills folder, then the actual outputs it has shipped. Real files, real dates.
- Say: nobody opens that pretend project again. This one has been running for months.
- **Payoff:** "Automate the work you already do. Not a business you made up for the video."
- **On-screen:** `Not a demo.`
- **Caption:** The test for whether someone's AI setup is real: can they open the actual file, and has it run more than once.

## Reel 3 — "What a skill actually is" (demystifier)
**Pull from:** 1:30-2:45
**Hook:** "Everyone's talking about Claude skills. Here's what one actually is."
- **Show:** open a real `SKILL.md` and scroll it slowly. Point at the description line up top, then the instructions below.
- Say: the top says when to use it. The rest is what you'd tell someone you were training.
- **Payoff:** "That's the whole thing. A text file that becomes a command."
- **On-screen:** `SKILL.md`
- **Caption:** No app, no install, nothing to compile. A skill is a folder with one markdown file in it.

## Reel 4 — "Build one in 2 minutes" (live build, the you-can-do-this reel)
**Pull from:** 11:30-13:30
**Hook:** "Let me build one right now so you can see how simple this is."
- **Show:** make the folder, make `SKILL.md`, type the one-line description, type the instructions, save. Then run it.
- Say it as you type, keep it genuinely short. Do not cut away from the typing.
- **Payoff:** "Two minutes. And every skill I showed you started exactly like that."
- **On-screen:** `2:00` counting, or `folder → SKILL.md → run`
- **Caption:** Do not plan the perfect one. Write the rough one, then fix the line that annoyed you.

## Reel 5 — `/yt-search` → "I don't guess what to make" (demo)
**Pull from:** 2:45-4:00
**Hook:** "I don't guess what to make anymore. I ask Claude what's already working."
- **Show:** run `/yt-search` on a topic, cut to the ranked results and the downloaded thumbnail grid.
- Say: it sorts by what's performing and flags what nobody has covered well.
- **Payoff:** point at a gap in the report. "That's my next video, and I didn't guess."
- **On-screen:** `/yt-search`
- **Caption:** Start from what already worked instead of a hunch. Same idea applies to any repeated research you do.

## Reel 6 — `/yt-package` → "It wrote this video" (demo, meta payoff)
**Pull from:** 4:00-5:30
**Hook:** "One command, and Claude writes the whole video."
- **Show:** run `/yt-package` on a transcript, hard-cut to the finished folder: `titles.md`, `hooks.md`, `script.md`, `filming-guide.md`.
- Say: titles, hooks, the full script, and a shot-by-shot filming guide.
- **Payoff:** open `script.md` and hold on it. "This is the script I'm reading off of right now."
- **On-screen:** `/yt-package`
- **Caption:** The meta part: the video this clip came from was planned by the skill in the clip.

## Reel 7 — `/social-copy` → "One video, every platform" (demo)
**Pull from:** 5:30-6:30
**Hook:** "I record one video and Claude writes the posts for every platform."
- **Show:** run `/social-copy`, cut to the `social/` folder filling with X, LinkedIn, Instagram, community, Skool.
- Say: same video, reshaped for each place it lives, in my voice, because I trained it on my own transcripts.
- **Payoff:** scroll the finished folder. "I didn't write one of these."
- **On-screen:** `/social-copy`
- **Caption:** The video is not the end of the work, it is the source for it.

## Reel 8 — "These run while I sleep" (cron proof, the trust reel)
**Pull from:** 6:30-9:30
**Hook:** "There are jobs running on my computer right now that I never touch."
- **Show:** `crontab -l` in the terminal, then the inbox file a monitor produced overnight, then the drafted replies queue.
- Say: it fires every hour, finds the comments I haven't replied to, and drafts the easy ones.
- **Payoff:** "Everything defaults to draft. It does the finding and the writing, I do the deciding."
- **On-screen:** `runs at :00, every hour`
- **Caption:** Automate the finding and the drafting. Keep the judgment.

## Reel 9 — `/email` → "The welcome emails send themselves" (demo)
**Pull from:** 8:30-9:30
**Hook:** "Someone joined my community an hour ago and I already emailed them. I wasn't there."
- **Show:** the drip sequence, then a real sent broadcast.
- Say: new person joins, the first email goes out, I'm not in the loop for it.
- **Payoff:** "The only part I still do is write it once."
- **On-screen:** `/email`
- **Caption:** Write the sequence one time. After that it is just running.

> **The 10th reel is parked.** It was `/skool`, which is not a real skill in `~/.claude/skills/`.
> Nothing else fit well enough, so we're shipping 9 for now. See the note at the bottom of
> `reel-scripts.md` — this still affects Part 3 of the long form and the count on the wall.

---

## Bonus reel (the closer, if you want an 11th)
**"Did it twice? That's a skill."**
**Pull from:** 13:30-end
**Hook:** "Here's the only rule I follow now."
- **Show:** flip through four skills that started as a repeated chore.
- **Payoff:** "Every time you do a task twice, that's a skill. You stop being the person doing the task and become the person reviewing the result."
- **Caption:** Pick the thing you did twice this week. That is your first one.

## More you can pull later
- `/yt-thumbnail` — "My thumbnails? Claude makes those too"
- `/transcribe` — "Pull any video's full transcript in seconds"
- `/yt-shorts` — "Turn my long video into short scripts" (meta: this reel about that skill)
- `/yt-seo` — "AI writes my title and description to get found"
- `/yt-upload` — "Claude uploads the finished video for me"
