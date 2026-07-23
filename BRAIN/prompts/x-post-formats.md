# X / Twitter Post Formats + Prompts

Reusable prompt templates for writing Tyler's X posts. Read `BRAIN/tyler-voice.md` FIRST, then pick a format below.

**Last updated:** 2026-07-23 (built from a live scrape of 40 top-performing "Claude Code" tweets via Apify)

---

## What actually performs in this niche (measured, not guessed)

Scraped 40 top tweets for "Claude Code" / "Claude Code automation". Findings:

| Tweet | Views | Bookmarks | Why it won |
|---|---|---|---|
| "I'm Boris and I created Claude Code... my setup might be surprisingly vanilla" | 8.2M | 103K | Plain, humble, zero hype |
| "I genuinely don't understand why everyone isn't using this yet" | 6.8M | 85K | Contrarian + `>` steps + "Bookmark this" |
| "Claude Code now has a screen reader mode." | 794K | 3.1K | Two plain factual sentences |
| "Don't waste 2 years learning to code... 82 minutes. Free:" + timestamps | 352K | 5.7K | Negative hook + chapter list |
| "Stop telling Claude, 'do this.'" (x3 repetition) | 384K | 2.9K | Repetition hook + "copy and paste" payoff |

## ⛔ Account constraint (verified 2026-07-23)

**@TylerReedAI does NOT have X Premium** (`isBlueVerified: false`, ~700 followers). Hard cap is 280 chars per tweet; we write to **230** as a safe buffer. Links always count as 23 chars no matter their length.

This matters: most of the huge tweets in the scrape below are 1,000+ characters, which is only possible on Premium (25,000 limit). **Those long-form shapes are NOT available to Tyler as single posts.** Anything longer than 230 must become a thread. Do not hand over a "post" that cannot physically be posted.

## Tyler's own proven shape (from his real tweets)

His actual recent tweets all land around 200 chars and use one shape:

> Plain or myth-busting opener. One line.
> *(blank line)*
> The concrete payoff in 2-3 sentences, or a short numbered list.

Real examples:
- "People think building a Claude Code skill needs an SDK or a framework. // It's a markdown file. Frontmatter on top, plain English below. Some are 50 lines, some generate their own Python. That's the whole thing."
- "I never start a video with a blank doc. Ever. // I point a skill at a transcript and 5 minutes later I have titles, hooks, a full script, and a filming guide. It writes the 80% draft. I make it mine."

Default to this shape. It is proven, it is his, and it fits the character limit.

**Rules that fall out of the data:**
1. Humble beats hype. The single biggest tweet in the niche has no hype at all.
2. "Free and open source" is the dominant winning angle. Tyler's skills repo is free and public - lead with that.
3. Chapter timestamps perform well and Tyler already has them on every video.
4. Use `>` for step lists. It is the native convention here.
5. Bookmarks are the real currency. "Bookmark this" is an explicit CTA in the top performers.
6. Specific numbers beat round ones. No hashtags. No emojis.
7. One idea per line, blank line between every idea.

---

## ⚠️ Voice guardrail (read before using any Blotato-style prompt)

Popular "viral X post" prompts (including the Blotato ones) ban the words **just, really, actually, maybe, could** and forbid adjectives/adverbs. **Do NOT apply that literally to Tyler.** His voice guide REQUIRES those hedges ("I just ask", "it's really just markdown files", "kind of"). Stripping them makes him sound like a generic AI-marketing account, which is the exact thing `tyler-voice.md` warns against.

**Take the STRUCTURE from those prompts. Keep Tyler's VOICE.**

Keep from the viral-prompt style: short lines, frequent line breaks, active voice, specific numbers, no hashtags, no emojis, no semicolons, no setup language ("in conclusion").
Ignore from it: the banned-word list, the no-adjectives rule, the forced controversy.

Also non-negotiable: **no em dashes**, and the positioning rule (this is about Claude automation, never YouTube-growth advice). See `tyler-voice.md`.

---

## FORMAT 1 - The standalone (under 280 chars)

The quotable. One idea, no link, nothing asked of the reader. This is the one that travels.

**Prompt:**
```
Write one standalone X post from the source below, under 280 characters.

Structure: open with a plain, slightly contrarian statement of fact. Then 3-5 short
sentences that pay it off. Fifth grade reading level. One idea per line with line breaks.

Voice: read BRAIN/tyler-voice.md. Warm, humble, hedged. Keep "just" and "kind of" if they
fit naturally. Never hype. Never position Tyler as a YouTube or growth expert - this is
about what the AI tool does.

No hashtags. No emojis. No em dashes. No link.
```

**Reference shape:** "I automated my entire YouTube workflow with Claude Code. It did not make my videos better. It removed the two hours of setup before I could start. The tool handles the boring parts. The judgment is still mine."

---

## FORMAT 2 - The step list (`>` bullets + bookmark CTA)

The bookmarkable one. Highest bookmark counts in the scrape used this shape.

**Prompt:**
```
Write an X post from the source below using the step-list shape.

Structure:
- Line 1: a plain statement of what this does. No hype.
- One line of context (what it replaced, or why it matters).
- "Here's the whole thing:" then 4-6 steps, each on its own line starting with "> "
- Each step is one short sentence.
- Close with how long it takes to set up, plainly.
- Final line: "Bookmark this" or the link.

Voice: BRAIN/tyler-voice.md. Humble, concrete, honest about limits.
Lead with "free and open source" if true - it is the strongest angle in this niche.

No hashtags. No emojis. No em dashes.
```

---

## FORMAT 3 - The simple explainer ("what it is")

Plain and factual. The "Claude Code now has a screen reader mode" shape. 794K views on two sentences.

**Prompt:**
```
Write a short X post that plainly explains what this thing is. Two to four sentences.

No hook tricks, no hype, no CTA. Just state what it is and what it does, the way you would
tell a friend. Assume the reader has never heard of it.

Voice: BRAIN/tyler-voice.md. Plain and warm.
No hashtags. No emojis. No em dashes.
```

---

## FORMAT 4 - The chapter list (video-specific)

Use when pointing at one of Tyler's videos. Native to the niche and he already has chapters.

**Prompt:**
```
Write an X post pointing at this video using the chapter-list shape.

Structure:
- Line 1: a plain or mildly contrarian hook about the topic.
- Line 2: what the video is, plus runtime and "Free:"
- 3-5 real chapter timestamps from the video, formatted "24:03 - Chapter name"
- One closing line with the takeaway.
- The link last.

Use REAL timestamps from the video's description. Never invent them.
Voice: BRAIN/tyler-voice.md. No hashtags, no emojis, no em dashes.
```

---

## FORMAT 5 - The mini thread (2-3 tweets)

For an idea too big for one tweet but not worth a full thread.

**Prompt:**
```
Write a 2-3 tweet X thread from the source below. Every tweet under 230 characters.

Tweet 1 states the idea plainly and creates a small open loop.
Tweet 2 pays it off with the concrete detail.
Optional tweet 3 is the honest limitation, or the link.

Voice: BRAIN/tyler-voice.md. No hashtags, no emojis, no em dashes.
```

---

## Per-video mix

For each video, aim for 4 X posts across formats, spaced ~2 days:

| # | Format | Link |
|---|---|---|
| 1 | Full thread or chapter list (Format 4) | yes |
| 2 | Step list with bookmark CTA (Format 2) | repo or none |
| 3 | Standalone quotable (Format 1) | none |
| 4 | Simple explainer (Format 3) or mini thread (Format 5) | yes |

Hard limit: every tweet under 230 characters (Tyler's account).
