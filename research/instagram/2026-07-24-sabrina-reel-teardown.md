# sabrina_ramonov — 25 reels, transcribed and analysed

Source: Apify `apify/instagram-reel-scraper`, run `6o8gxDZa2FRpqB0wu`, dataset
`4BrQKXxfn4SKIp4eA`. 25 non-pinned reels with audio transcripts, 2026-07-14 to
2026-07-24 (11 days). 1,004,415 followers.

**Caveat:** one account, 25 posts, 11 days. These are correlations inside one
creator's feed, not proven mechanics. Where the numbers are noisy I say so.

## Headline numbers

| Metric | Value |
|---|---|
| Cadence | **2.3 reels/day** (25 in 11 days; 2-4 daily) |
| Median duration | **40.1s** (range 20.9 – 90.2) |
| Median plays | 18,748 (range 207 – 211,539) |
| Median transcript | **162 words at ~220 wpm** |
| Original audio | **24 of 25** |
| Hashtags | **exactly 5** on 24 of 25 |
| Spoken CTA | **23 of 25** |

## 1. The gate is worth ~3.6x reach and ~100x comments

| | n | median plays | median comments |
|---|---|---|---|
| Gated ("comment WORD") | 22 | **18,764** | **438** |
| Not gated | 3 | 5,242 | 4 |

The three ungated posts are the bottom of her feed. This is the clearest signal
in the dataset.

## 2. She says the CTA out loud — it is not just the caption

23 of 25 transcripts end with a spoken version of the gate. Verbatim closers:

> "Remember to hit follow and comment channels if you want me to DM you this full list."
> "Hit follow if you want me to send you all of these prompts, comment psychology and I'll DM you."
> "If you want me to send you my full list, hit follow and DM me secrets and I'll DM you."

Structure is always: **hit follow → comment WORD → I'll DM you.** Three
instructions, in that order, in the last four seconds.

## 3. Longer reels outperform shorter ones here

This is the opposite of the usual advice:

| Duration | n | median plays |
|---|---|---|
| 0-30s | 8 | 7,716 |
| 30-45s | 6 | 16,505 |
| 45-65s | 7 | **32,568** |
| 65s+ | 4 | 30,554 |

Her 45-65s reels get **4.2x** the plays of her sub-30s ones. Likely confounded:
the longer ones are numbered lists ("10 secret codes", "8 YouTube channels")
which are inherently more save-able. But nothing here supports keeping reels
under 30 seconds.

## 4. She reposts the same deliverable with a rewritten hook

Six gate words appear twice inside 11 days — same magnet, new opening line.
Outcomes swing violently in **both** directions:

| Gate | first upload | second upload | change |
|---|---|---|---|
| RUIN | 5,069 | 91,037 | **18.0x** |
| SECRET | 19,140 | 87,766 | **4.6x** |
| PHOTO | 14,770 | 28,786 | 1.9x |
| COMMANDS | 42,329 | 18,748 | 0.44x |
| BRAND | 60,472 | 16,173 | 0.27x |
| CHINA | 15,660 | 1,813 | 0.12x |

Three up, three down. **This is not a reliable rewrite technique — it is shots
on goal.** She treats a deliverable as reusable and keeps firing new hooks at it
until one catches. The RUIN pair is the tell:

- "ChatGPT knows your dark secrets." → 5,069
- "ChatGPT knows what's ruining your life." → 91,037

Same content. Same gate word. One sentence different, 18x the reach.

## 5. The hook is a first sentence, and it is one of two shapes

Every top performer opens with either a **numbered list** or a **capability
claim**. Ranked by plays:

| Plays | Opening line |
|---|---|
| 211,539 | "Here are eight YouTube channels that will teach you more skills than a $200,000 college degree." |
| 208,424 | "What happens when you ask AI the most brutal truths in psychology?" |
| 91,037 | "ChatGPT knows what's ruining your life." |
| 87,766 | "Five power words for chat GPT." |
| 60,472 | "How I'd start a one-person business and personal brand with AI in 30 days." |
| 42,329 | "10 secret codes for Claude code." |
| 32,568 | "10 ways ChatGPT erases you from the internet." |
| 28,786 | "AI can find every hidden photo you're in." |

Note what is absent: no "in this video", no greeting, no name, no context. The
first sentence *is* the value proposition. Nothing precedes it.

Also note the SECRET pair — the winner is the **plainer, shorter** one:
"Five power words for chat GPT" (87,766) beat "Five codes to unlock ChatGPT
psychology mode" (19,140).

## 6. Original audio, not trending sounds

24 of 25 use original audio. She is not riding trending music at all on reels.
(Distinct from carousels, where theromanknox and brodyautomates do attach music.)

## 7. Hashtags: exactly five, mostly the same five

`#ai` appears on 24 of 25 — effectively a fixed tag. Then #chatgpt (14),
#aitools (14), #chatgptprompts (12), #productivity (8), #technology (8).

She is not researching hashtags per post. She has a small rotating set.

## 8. Posting windows

Three clusters in UTC: **14:00-16:00**, **18:00-19:00**, **21:00-23:00**. That is
roughly 9am / 1pm / 5pm US Eastern. Consistent enough to be scheduled.

## What this means for us

1. **Say the CTA out loud.** We were planning caption-only gates. 23/25 of her
   reels speak it in the last four seconds. Cheapest change on the list.
2. **Stop targeting 25-30s.** Her 45-65s band does 4x her sub-30s band. Aim 45-60
   with a numbered structure.
3. **The first sentence is the whole hook.** No preamble, no "hey guys". Lead
   with the number or the capability.
4. **Deliverables are reusable.** One magnet supports many reels. Build the
   deliverable once, then keep writing new first sentences at it. Expect most to
   underperform — half of hers got worse.
5. **Five fixed hashtags.** Stop thinking about hashtags. Pick five, reuse.
6. **Original audio is fine for reels.** Music matters for carousels, not here.

Our advantage stands: her deliverables are prompt lists and PDFs. Ours can be
installable skills and working repos, which is a stronger reason to comment.
