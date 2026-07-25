# Four-account reel teardown — 99 reels with transcripts

Source: Apify `apify/instagram-reel-scraper`, runs `6o8gxDZa2FRpqB0wu` and
`6d6lfDaHhkhomMi7B`. 99 non-pinned reels with audio transcripts.

## Two corrections to the earlier research

**1. brodyautomates does NOT post monthly.** The earlier profile-scraper note said
"~1 per 2-4 weeks" from 46 lifetime posts. The reel scraper shows **25 reels
across 25 active days** (Jun 10 – Jul 24). The profile endpoint's `latestPosts`
was padded with pinned old posts and gave a false cadence. He posts near-daily.

**2. "Longer reels win" was true for one account, not generally.** That came from
sabrina alone. Across all four the pattern inverts:

| account | 0-30s | 30-45s | 45-65s | 65s+ |
|---|---|---|---|---|
| theromanknox | **9,479** (9) | 4,358 (8) | 5,785 (5) | 4,551 (3) |
| brodyautomates | **32,601** (1) | 23,932 (12) | 19,777 (5) | 14,596 (7) |
| chase.h.ai | 40,000 (1) | **69,398** (3) | 29,420 (6) | 21,512 (14) |
| sabrina_ramonov | 7,716 (8) | 16,505 (6) | **32,568** (7) | 30,554 (4) |

Three of four do *better* short. Only sabrina does better long. **Do not treat
duration as a lever** — the honest read is that it is not the variable driving
outcomes in this data.

## The comparison

| | theromanknox | brodyautomates | chase.h.ai | sabrina_ramonov |
|---|---|---|---|---|
| Followers | 304k | 178k | 221k | 1.0M |
| Reels sampled | 25 | 25 | 24 | 25 |
| Gated caption | 15/25 | 18/25 | **23/24** | 22/25 |
| **Spoken** CTA | 11/25 | 19/25 | **0/24** | 22/25 |
| Median duration | 34.6s | 44.6s | **82.5s** | 40.1s |
| Median plays | **5,785** | 23,389 | 23,034 | 18,748 |
| Max plays | 385,828 | 185,668 | 214,392 | 211,539 |
| Original audio | 23/25 | 25/25 | 24/24 | 24/25 |
| Median hashtags | 4 | 2 | **0** | 5 |

## What actually holds across all four

**Original audio: 96 of 99 reels.** This is the only universal. Nobody is riding
trending sounds. Whatever reach mechanism people attribute to trending audio,
these four are not using it.

**The comment gate: 78 of 99.** Every account runs it, at 60-96% of posts.

## What does NOT hold — stop treating these as rules

- **Spoken CTA.** chase says it **zero** times in 24 reels and still gates 23/24
  in the caption, with a 23,034 median. sabrina says it 22/25 times. Both work.
  My earlier "say the CTA out loud" advice was drawn from sabrina only.
- **Hashtags.** chase uses **none** (median 0) and matches sabrina's median plays
  with five. There is no hashtag consensus here.
- **Duration.** See above.
- **Followers predict nothing.** theromanknox has the most followers (304k) and
  the *worst* median reel (5,785) — 4x below brody at half his following.

## The single most replicable finding: brody's one hook

brodyautomates runs **one hook formula, repeated**, and it is his entire top five:

| Plays | Opening line |
|---|---|
| 185,668 | "This is insane, someone just built a GitHub repo that can do what 11Labs and WhisperFlow…" |
| 179,857 | "Someone just built a GitHub repo that gives agents read and search access across 13 platforms…" |
| 159,815 | "Someone just built a GitHub repo that scripts content for you, edits for you, voiceovers…" |
| 126,052 | "Someone just built a GitHub that lets an AI agent manage all of your social media accounts…" |
| 55,401 | "Someone just built a GitHub repo that can edit videos with AI." |

Seven of his 25 reels open with that stem. Median 23,389 plays on an account with
**two** hashtags and no fixed posting schedule.

The formula: **"Someone just built a [thing] that [does the impossible-sounding
job]."** Third person. Present tense. No "I". The creator is the messenger, not
the subject — which is why it scales: he never runs out of other people's repos.

This is directly available to us. We build the repos.

## chase.h.ai is the outlier worth studying second

Median **82.5 seconds** — double everyone else — with 14 of 24 reels over 65s.
Zero hashtags. Zero spoken CTAs. One caption reused verbatim on 23 of 24 posts:

> Comment "agent" to get my Claude code guides

That is the entire caption. No hook, no body, no questions, no tags. And he holds
a 23,034 median with a 214,392 top.

His top hook is a curiosity-gap opener, not a list:
> "If you don't know what I'm looking at here, you are probably falling behind because this…" (214,392 plays, 118s)

## Revised guidance

1. **Gate every post.** The only thing all four agree on besides audio.
2. **Use original audio.** 96/99.
3. **Steal brody's hook stem.** "Someone just built X that does Y" — except we
   build the X, so ours becomes "I built X that does Y" or stays third-person for
   other people's tools.
4. **Ignore duration, hashtags, and spoken CTA as levers.** The data does not
   support any of them as consistent. Pick what fits the piece.
5. **Lists still work** — sabrina's numbered reels are her best — but they are one
   working shape, not the only one. chase's curiosity-gap and brody's
   "someone-just-built" both beat her median.
