# IG competitor cadence + format teardown — 2026-07-24

Source: Apify `instagram-profile-scraper`, run `DL1ypwXzRr40Fhdeb`, dataset
`yzQyAfhFaCjDJ4rWd`. Four handles requested; `sabrinaramonov` did not resolve
(wrong handle — needs the real one).

**Caveat on the numbers:** the scraper returns ~12 recent posts per profile and
pinned posts are included regardless of age. So the posts/day figure is only
trustworthy where the window is genuinely recent (chase, roman). For brody the
sample spans 270 days because old pinned bangers are in it — his real recent
cadence is lower than any average would suggest.

## The three accounts run three completely different strategies

| | chase.h.ai | theromanknox | brodyautomates |
|---|---|---|---|
| Followers | 221,133 | 304,430 | 177,873 |
| Total posts | **751** | 195 | **46** |
| Followers per post | 295 | 1,561 | **3,867** |
| Format mix (recent 12) | 11 reels / 1 carousel | **1 reel / 11 carousels** | 6 reels / 6 carousels |
| Recent cadence | **2-3 per day** | 1-2 per day | ~1 per 2-4 weeks |
| Verified | yes | yes | no |

### chase.h.ai — volume, reels, one caption

751 posts. Recent window shows posts on Jul 14, 15 (x2), 16 (x4), 17 (x2), 23
(x2), 24 — frequently **two or three within the same minute**, which means
batch-uploading a whole session at once.

Nearly every post is `productType: clips` (a reel). And the caption is *the same
line every time*:

> Comment "agent" to get my Claude code guides

Eleven of the twelve sampled posts use that exact caption or a one-word variant
("agency" for a different magnet). He is not writing captions at all. The caption
is a lead-gen mechanism, nothing else.

Engagement range: 101–1,605 likes, 16–927 comments. Best performer 1,605 likes /
927 comments (Jul 14) — a reel about a Claude skill.

### theromanknox — carousels, near-daily

Almost the inverse: 11 of 12 recent posts are Sidecar (carousel). Posted Jul 16,
17, 18, 19 (x2), 20, 21, 23 (x2), 24 — call it 1-2 a day.

His two pinned all-time performers are both carousels:
- 16,392 likes / 3,011 comments — "Save this. 9 YouTube courses worth watching"
- 15,278 likes

Note how far those outrun his current posts (45–136 likes). Either reach has
collapsed or the pinned ones were boosted by something unusual. His comment-gate
post ("Comment «KNOX» below") got 367 comments on 136 likes — the gate works even
when baseline reach is low.

### brodyautomates — the efficiency outlier

**177,873 followers on 46 posts.** That is 3,867 followers per post, 13x chase's
ratio. He posts roughly monthly and the production quality is the highest of the
three.

His numbers dwarf the others despite the volume:
- 19,728 likes / **35,961 comments** — "Comment 'Claude' if you want it for free"
- 20,808 likes — a reel
- 2,601 likes / 1,257 comments — a carousel

**35,961 comments on a single post** is the largest number in this dataset by an
order of magnitude, and it is a comment gate.

## What this actually says

1. **There is no single winning cadence.** 2-3/day (chase) and 1/month (brody)
   both work at ~200k followers. What they share is a comment gate on essentially
   every post.

2. **Volume is the weakest of the three strategies per unit of effort.** Chase
   needs 751 posts to reach where brody got in 46. If the choice is "post more"
   or "post better", the data favours better.

3. **The caption is not content.** Chase proves you can run the same nine words
   forever. Stop writing bespoke captions for reach; write them for the gate.

4. **Carousels are not losing to reels.** Roman is 90% carousels at 304k. Brody
   splits evenly. Only chase is reels-first, and he has the worst
   followers-per-post ratio of the three.

5. **The gate is the mechanic, not the format.** Every outlier post across all
   four accounts studied (incl. the swipe file) gates a deliverable behind a
   comment.

## Implication for us

We have the opposite problem to chase: high production value, near-zero volume,
and no gate at all. The cheapest change with the largest expected effect is
adding a comment gate to posts we are already making — not making more posts.

Second: we have a real deliverable to gate that none of these three have. They
gate PDFs and guides. We can gate **working repos and installable skills**, which
is a materially better trade for the person commenting.

---

# Addendum — sabrina_ramonov + the music question

## The music finding (API vs screenshots)

Apify's `musicInfo` field came back **empty for every carousel** across both
theromanknox and brodyautomates, and populated for exactly one post — a reel.

That reading is wrong. The screenshots in `platform/instagram/swipe/2026-07-24/`
show the audio attribution line in the Instagram UI on their **carousels**:

- theromanknox carousel: `♫ TVN · 1%`
- brodyautomates carousel: `♫ Giulio Cercato · New Horizons`

So both attach music to carousels. The scraper simply does not expose audio for
`Sidecar` posts — treat that field as unreliable for carousels, not as evidence
of absence. Screenshots win here.

**Unverified:** whether attaching audio actually changes carousel distribution.
That is a widely repeated claim and it may well be true, but nothing in this
dataset proves it. What the data does show is that the two most successful
carousel accounts in the sample both do it deliberately.

## sabrina_ramonov — 1,004,415 followers, 2,035 posts

Handle is `sabrina_ramonov` (not sabrina.romanov). Verified. Bio: "Teach 10M ppl
AI (for free) / Sold AI startup $10M+ / Forbes 30 Under 30".

**100% reels** in the sampled window. Zero carousels.

Cadence: **~3 per day at fixed times.** Jul 22, 23, and 24 each show three posts
at roughly 15:30, 18:45 and 22:30 UTC. That is a scheduled slot system, not
ad-hoc posting.

Every single caption follows one template:

```
Follow and comment "WORD" and I'll send you [deliverable] 👇

[hook line]

[body: list or short explanation]

[3 search-style questions]

#5 #hash #tags #here #only
```

Gate words observed: BLITZ, GOAL, FACTS, BRAND, ERASE, CHINA, COMMANDS,
INVISIBLE.

Engagement on the gate: 13,255 comments (BLITZ), 1,953 (BRAND), 1,574
(INVISIBLE), 855, 557, 527, 293, 241, 131.

**The three question lines are Instagram SEO.** She writes the literal queries
someone would search — "How do you fact check AI generated content?", "What is a
Claude skill and how do you install one?" — inside the caption. That is a
deliberate discovery play and none of the other three accounts do it.

Also note: her videos are **640x1136** — deliberately low resolution. Production
value is clearly not the constraint on reach.

## Consolidated: what all four share

| | gate on every post | fixed template | music on carousels |
|---|---|---|---|
| chase.h.ai | yes ("agent") | yes, one line | n/a (reels) |
| sabrina_ramonov | yes (8 words seen) | yes, 5-part | n/a (reels) |
| theromanknox | on some | no | **yes** |
| brodyautomates | yes ("SKILLS") | no | **yes** |

Two of four run a rigid caption template and post 2-3x/day. Two run bespoke
captions and post far less. Both approaches clear 175k+.
