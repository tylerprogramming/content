# TikTok cadence

Built from `research/tiktok/2026-07-25-competitor-cadence.md`. Instagram keeps
its own plan; this does not replace it.

## The shape

**One post a day, same slot, from source that already exists.**

Copied from `@nateherkai`: 17:01-17:03 for thirty consecutive days. Median only
1,208, but four posts cleared 34k and one hit 141,200. The slot costs nothing
and the upside is uncapped. `@chase_ai_` proves bursts also work at 135k
followers, so this is a starting shape, not a law.

Do not chase volume for its own sake. Every post has to be worth watching on
its own.

## The first 23 days: video 004

`004-claude-code-concepts` — "23 Claude Code Concepts Every Beginner Needs to
Know" — is already cut into 23 numbered sections **with exact time ranges** in
`script.md`:

```
 1. What is Claude Code    0:30-1:15   (45s)
 2. The Terminal           1:15-2:00   (45s)
 3. Prompting              2:00-3:00   (60s)
 …
23. Remote Control        19:45-20:45  (60s)
```

Median 45s, longest 75s, covering 20m15s of finished footage.

**That is 23 days of daily TikTok from one published video, with no filming.**

Each concept is a real clip cut from the longform, not a slide deck. It is the
same footage that already worked on YouTube, and clip length lands where three
of four accounts in the research perform best.

### Production

One batch, then post daily:

1. Pull the 23 ranges from `script.md`
2. Cut each from the source MP4
3. Reframe 16:9 → 9:16 (`tiktok_safe.py` handles stills; video needs the same
   treatment adding)
4. Queue one a day into the slot

### Ordering

Do not run 1-23 in order. Concepts 1-5 are the weakest hooks ("What is Claude
Code", "The Terminal"). Lead with the ones that stand alone:

- **Week 1:** 14 Checkpoints & /rewind · 11 Plan Mode · 22 Custom Agents ·
  20 Sub-agents · 18 Skills · 21 Hooks · 23 Remote Control
- **Week 2:** 12 Compact & /clear · 17 Slash Commands · 19 MCP Servers ·
  7 CLAUDE.md · 15 @ File References · 8 Memory · 16 Screenshots & Images
- **Week 3:** 4 Permissions · 6 Context Window · 5 Tool Use · 13 Session
  History · 10 /init · 9 Models · 3 Prompting · 2 The Terminal ·
  1 What is Claude Code

## Slideshows, as a second track

A TikTok slideshow is a **native photo post** — multiple images, TikTok adds
the music. It is not the same object as an MP4 of slides, and it is what
`@theromanknox` (20 of 30 posts) and `@chase_ai_` run. Chase's best post of the
month is a slideshow: 275,600 plays, 10,341 saves.

His slideshow median trails his video median, so they are not better on
average — they are capable of the biggest single result and cheap to make from
carousels that already exist.

Use them for the reframed carousel sets. Use clips for 004.

## Not settled

- **Whether Blotato can post a real slideshow.** Its API exposes
  `imageCoverIndex`, described as "TikTok: cover image index for carousel",
  which implies multi-image TikTok posts. The public docs do not confirm it.
  Test with `privacyLevel: SELF_ONLY` or `isDraft` before trusting it.
- **Music.** For slideshows, `autoAddMusic` lets TikTok attach a licensed
  track, so no file is needed. For clips, the source audio is the voiceover
  and no bed is required.
- **Video reframing.** `tiktok_safe.py` reframes stills only. Cutting 16:9
  longform to 9:16 needs the equivalent for video.

## Measure

Judge on saves and shares, not comments. The comment-gate mechanic is an
Instagram finding and was measured on accounts that mostly are not competing
here. Three weeks is the test; if nothing moves, stop.
