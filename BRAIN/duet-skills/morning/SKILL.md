---
name: morning
description: Tyler's morning content brief. Reads his content repo on GitHub and sends what is filming next, the latest channel numbers, and 3 video openings. Use when Tyler types /morning, asks for his morning brief, or a scheduled morning task runs.
---

# /morning

A short brief Tyler reads on his phone before he starts. Under 900 characters. Facts from the files, never from memory.

## Sources (all in the GitHub repo `tylerprogramming/content`, branch `main`)

Read these fresh every run. Do not use what you remember from a previous run.

1. `youtube/notes/status.md`
   - The lines at the very top that start with `> 2026-` are a dated log, newest first. Read the first 5.
   - The table under `## 🔥 FRESH / FILMING NOW` lists the videos in progress. Each row has a title, a folder, and a status starting with an emoji: 📦 packaged, 📝 script, 🎬 filmed, ✂️ edited, ✅ published.
2. The newest file in `youtube/analytics/daily/` (named `YYYY-MM-DD.json`). It has three keys, `day`, `week`, `month`. Each has:
   - `period` (`start`, `end`): the dates the numbers cover. YouTube data lags about 3 days, so `day` is usually 3 days back. Always say the date.
   - `analytics`: `views`, `estimatedMinutesWatched`, `averageViewDuration` (seconds), `subscribersGained`, `subscribersLost`.
   - `perVideo`: views and `avgViewPct` per video for that period, with `title` and `isShort`.
   - `recentVideos`: the latest uploads with total `views` and `publishedAt`.
   - `searchTerms`: what people searched to find the channel.
3. `youtube/ideas/video-ideas.md`: the ideas list.
4. Anything in `research/` modified in the last 7 days. Read titles and the first section only.

If a file is missing or GitHub can't be reached, say which one in the brief and keep going with the rest. Never fill a gap with a guess.

## What to send

Exactly this shape:

```
Morning brief, <weekday> <date>

Filming next: <title> (<status word>). <one line: what's left before it can be filmed, from its status cell>
Then: <next title> (<status>)

Numbers (<period date>): <views> views, <+subs>/<-subs> subs, avg view <m:ss>
Top video: <title> <views> views
<one line only if something moved: a video doing 2x its usual, a new search term in the top 5, a sub loss day>

3 openings:
1. <idea> - <the number or file that makes it worth doing now>
2. <idea> - <reason>
3. <idea> - <reason>

Reply with a number.
```

## Rules for the 3 openings

- Each one needs a reason from the files: a research file from this week, a search term, a video over-performing, a gap a breakdown named. No reason, no opening.
- Prefer what is already packaged (📦) or researched over a brand-new idea.
- Never suggest a video that is already 🎬 filmed, ✂️ edited, or ✅ published.
- The channel is about AI and Claude Code automation. YouTube is where Tyler shows it, not the topic. Do not suggest YouTube-growth or "how to grow a channel" videos.

## Voice

Tyler's voice: plain, direct, short sentences. No hype words (insane, crazy, game-changer, huge). No em dashes. Numbers as digits. If something looks wrong in the data, say it plainly ("analytics file is 4 days old").

## If he replies with a number

Take that opening and make a one-page brief in the Make tab: the idea, why now (with the numbers), who already made it (search YouTube, last 30 days, top 5 with views), the angle nobody took, and a working title. Then message him the link. Do not post, publish, or change any file in the repo.

## Never

- Change, commit, or push anything in the repo.
- Post anywhere except Tyler's own DM or this chat.
- Invent a view count, a date, or a status.
