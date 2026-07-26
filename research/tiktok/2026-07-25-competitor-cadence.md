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

**chase.h.ai does not exist on TikTok.** The scrape returned "This
profile/hashtag does not exist." He is the strongest of the four on Instagram
and is not on this platform at all.

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
