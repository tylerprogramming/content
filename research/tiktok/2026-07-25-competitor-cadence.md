# TikTok cadence — the IG competitor set

Source: Apify `clockworks/tiktok-scraper`, run `W30RcWdi7KjQupRgj`, profile
scrape, 30 latest non-pinned posts per account, 2026-07-25.

## Correction to the earlier note

An earlier pass concluded the slideshow detector was broken, after three
scrapes returned zero slideshows across 385 posts — including `#photomode`
and `#slideshow`.

**The detector works.** It fails on *search and hashtag* scrapes and works on
*profile* scrapes. theromanknox is 67% slideshows and they were flagged
correctly here. So the earlier "no data on TikTok carousels" stands only for
that method, and the finding below is real.

## The four accounts

| | On TikTok | Posts/day | Median plays | Slideshows |
|---|---|---|---|---|
| **sabrina_ramonov** | yes | **2.7** | 11,750 | 0 / 30 |
| **theromanknox** | yes | 0.8 | 1,294 | **20 / 30** |
| **brodyautomates** | technically | — | 0-3 | 0 / 9 |
| **chase.h.ai** | **no** | — | — | — |

**chase.h.ai does not exist as a handle** — but Chase does. He is
`@chase_ai_` on TikTok: 135,000 followers and **924 videos**. My first pass
searched the Instagram handle, got "profile does not exist", and wrongly
concluded he was absent. He is one of the most active accounts in the set.
See the second table below.

**brodyautomates is dead here.** Nine posts, none above 3 plays, despite 178k
followers on Instagram. Being large on one platform carries nothing.

## sabrina: 2.7 posts a day, on a clock

30 posts in 11 days. Not batched randomly — she posts into fixed slots:

```
14:xx   18:xx   22:xx   01:xx
```

Two to three a day, same times, every day. Median 11,750 plays, best 82,200.
This is the same near-daily discipline the Instagram teardown found, run at a
higher frequency.

Worth noting she posts **zero slideshows**. All 30 are video.

## theromanknox: the slideshow account

20 of 30 posts are slideshows, and they outperform his own video:

| | Median plays | Best |
|---|---|---|
| Slideshow | **1,294** | **102,200** (5,311 saves) |
| Video | 888 | 21,800 |

Both of his breakout posts are slideshows: 102,200 plays with 5,311 saves, and
65,700 with 4,427 saves. His save *rate* on those is around 5-7%, well above
the ~3% seen across the earlier video sample.

Read this carefully though. His median is ~1.3k plays, so this is a small
account and the medians are close enough to be noise. What is not noise is
that his two best posts are both slideshows, and both were saved heavily.

## What this suggests

- **Cadence is the lever, not format.** sabrina posts 3x more often than
  theromanknox and sees 9x his median, with no slideshows at all.
- **Slideshows are a saves play.** theromanknox's slideshow breakouts were
  saved at roughly double the rate of the video sample. That matches the
  Pinterest finding: single-frame reference formats get saved, not clicked.
- **Do not assume cross-platform presence.** Two of the four strongest
  Instagram accounts in this niche are absent or dormant on TikTok.

## Limits

One snapshot, 30 posts per account, no history. Play counts on very recent
posts are still climbing. theromanknox's sample spans 37 days while sabrina's
spans 11, so their medians are not measured over the same window.


---

# Round two: the right handles

Run `aK0t8e2c5sF2JHqPv`, 2026-07-25. Found by searching profiles rather than
guessing that Instagram handles carry over — which is what went wrong above.

| account | followers | posts/day | slideshows | median plays | best |
|---|---|---|---|---|---|
| **@chase_ai_** | 135,000 | 1.4 | 6 / 30 | **17,500** | **275,600** |
| **@nateherkai** | 21,400 | **1.0** | 0 / 30 | 1,208 | 141,200 |
| @nateherk | 17,800 | dormant | 0 / 13 | 1,558 | 8.2M (2020) |

## The three cadences, and what each is worth

**@nateherkai — once a day, 17:02, every day.** Not approximately: the
timestamps are 17:01, 17:02, 17:03 for thirty consecutive days. Median is only
1,208, but four posts cleared 34k and one hit 141,200. One slot, held.

**@chase_ai_ — bursts, not a drip.** 1.4/day on average, but he posts two or
three within the same few minutes (18:20 and 18:21, 22:13 and 22:19), then
skips days. Median 17,500 on 135k followers. This is the strongest account
here and it is *not* posting daily.

## Slideshows, second look

theromanknox is not the only one. chase runs them too, 6 of 30, and **his best
post of the month is a slideshow**: 275,600 plays with 10,341 saves.

But his slideshow *median* is 13,850 against 18,600 for video, so on typical
performance they are slightly behind. Both his biggest hits are outliers, one
slideshow and one video.

Honest read: slideshows are not better on average, but they are capable of the
biggest single results, and they are cheap to produce from work that already
exists.

## What this changes

**Frequency is not the lever on its own.** chase is the strongest account here
and posts in bursts, skipping days. nateherkai holds one slot a day. sabrina
runs 2.7 a day. All three work; they are not converging on a number.

**A held slot is the cheapest thing to copy.** nateherkai posts at 17:01-17:03
for thirty consecutive days. Median 1,208, but four posts cleared 34k and one
hit 141,200 — the slot costs nothing and the upside is uncapped.

**Correction to the earlier note here:** I wrote that cadence looked like the
lever, from sabrina's 2.7/day alone. With more accounts it does not hold as a
simple more-is-better rule.

## Excluded

`@n8nautomation21` was in an earlier draft as a cautionary case. Dropped at
Tyler's call — not a relevant comparison, and nothing here depends on it.
