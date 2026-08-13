---
title: Six channels, 180 videos - what they do that we do not
date: 2026-08-13
kind: analytics
status: final
data: data/2026-08-13-competitors-combined.csv
---

# Competitor teardown

Last 30 uploads each for IndyDevDan, David Ondrej, Nate Herk, Chase AI, Jack
Roberts and Sabrina Ramonov, pulled from the YouTube Data API. 180 videos, 89 of
them long-form with real view counts.

Every video is scored against **its own channel's median**, because raw views
just tell you who has more subscribers. 1.00x means "a normal video for that
channel."

---

## 1. The finding that reorders everything else

You asked to learn from Sabrina. Here is every channel measured the only
size-fair way — median long-form views as a percentage of subscriber count:

| Channel | Subs | Median long-form | % of subs |
|---|---:|---:|---:|
| **Chase AI** | 162,000 | 50,277 | **31.0%** |
| **IndyDevDan** | 144,000 | 32,491 | **22.6%** |
| Jack Roberts | 253,000 | 33,400 | 13.2% |
| David Ondrej | 411,000 | 42,300 | 10.3% |
| Nate Herk | 935,000 | 63,824 | 6.8% |
| Sabrina Ramonov | 353,000 | 5,970 | **1.7%** |
| **Tyler AI** | 23,600 | ~327 | **1.4%** |

**Sabrina is in the same hole you are.** 353,000 subscribers and a median
long-form video does under 6,000 views. Proportionally she is doing slightly
worse than you are. Copying her packaging copies a channel that is not currently
reaching its own audience.

The two channels actually working are **Chase AI at 31%** and **IndyDevDan at
22.6%** — and they are the two closest to you in size, at 162K and 144K. That is
lucky. Their tactics are more likely to transfer than a 935K channel's.

**Reprioritise: study Chase AI first, IndyDevDan second.** Nate Herk is worth
reading for title formulas, but he has 40x your subscribers and a lot of his
reach is brand.

---

## 2. Title patterns, measured

Median outlier of videos carrying each pattern vs videos without it, across all
89 long-form videos:

| Pattern | With | Without | n |
|---|---:|---:|---:|
| **Money in the title** | **1.89x** | 1.00x | 8 |
| **Borrowed authority** (ex-NASA, L8 principal, 10x dev) | **1.25x** | 1.00x | 10 |
| **Versus / "I tested X vs Y"** | **1.21x** | 1.00x | 4 |
| Starts with "I" | 1.21x | 1.00x | 10 |
| Starts with "How" | 1.18x | 1.00x | 5 |
| News framing ("just dropped/got/released") | 1.12x | 0.98x | 11 |
| Number in title | 1.02x | 0.92x | 47 |
| ALL-CAPS emphasis word | 1.01x | 1.00x | 36 |

Two of these need unpacking because the raw number is misleading.

### "Starts with I" is two different formats again

Same split we found on your own channel, confirmed at scale:

| | |
|---|---|
| 3.30x | I Tested GPT 5.6 Sol vs Fable 5. What You Need To Know. |
| 2.93x | I asked Claude Code to make me as much money as possible |
| 2.71x | I Built $1M Marketing Team with 1 AI Agent (7 Skills) |
| 2.08x | I Studied Stripe's AI Agents... Vibe Coding Is Already Dead |
| — | — |
| 0.39x | I Built The Same App on Every AI |
| 0.36x | I Deleted All My Claude Skills... And Claude Got Smarter |
| **0.27x** | **I Built an AI Agent That Works While I Sleep (No Code)** |

The winners attach "I" to an **external subject** (Stripe, GPT vs Fable) or a
**stake** ($1M, as much money as possible). The losers attach it to a personal
hobby project. That bottom entry is a Jack Roberts video on a 253K channel — it
is almost exactly a title you would write, and it did a quarter of his normal.
Treat "works while I sleep" as a dead angle, not an untried one.

### ALL-CAPS does nothing on its own

1.01x vs 1.00x across 36 videos. Everyone does it, so it is table stakes, not an
edge. Do not spend effort here.

### The money pattern, and your standing rule

Money titles are the strongest signal in the set at 1.89x — Nate Herk's top four
are almost all money, and Jack Roberts' best is *Beautiful $10,000 Websites*.

`CLAUDE.md` says **no money amounts in titles.** I am not overriding that. But
the evidence against it is now substantial and it is your call, so here it is
plainly. A middle path that respects the rule: money in the **thumbnail** and the
first line of the description, transformation language in the title. Chase AI's
5.10x video does exactly this — the title promises a capability, not a number.

---

## 3. The asset you are not using: borrowed authority

David Ondrej's top three videos, all the same format:

| | |
|---|---|
| 3.55x | Ex-NASA dev reveals his Agentic Engineering Workflow |
| 2.11x | L8 Principal's Agentic Engineering Setup (just copy him) |
| 1.82x | Agentic Engineering, explained by a 10x developer |

He is not the expert in these videos. He borrows someone's credential and shows
their setup. It is his single most reliable format.

**You do not have to borrow. You have the credential.** Eight years as a software
engineer at IBM and Chase, now an AI engineer at Pfizer. Nobody else in this
comparison set can say that, and you almost never say it either — it appears in
no title, no thumbnail, and no hook in the last thirty videos.

Titles that are true for you and unavailable to everyone above:

- *How a Pfizer AI Engineer Actually Builds Agents*
- *I Build AI Agents at a Fortune 500. Here Is the Setup I Use at Home.*
- *8 Years as a Software Engineer. Here Is What AI Actually Changed.*

Related: IndyDevDan runs the same play pointed at his audience rather than at a
guest — *The Claude Code Feature Senior Engineers KEEP MISSING* at 1.81x. Naming
the professional identity of the viewer works as well as naming a guest's.

---

## 4. Thumbnails

Top three thumbnails from each channel, and yours side by side. Three measurable
gaps.

### Split-screen before/after — they use it, you never do

**Six of their eighteen top thumbnails are a split or a transformation:**
Chase's `SLOP → FIXED`, IndyDevDan's `LOOP ENG ❌ | SDLC ✅`, Nate's
`Fable 5 ← → Sol 5.6`, Sabrina's `WEEK 1 | WEEK 6` and `BEFORE | AFTER`.

**Zero of your last nine.** This is the biggest single gap and the easiest to fix.
Chase AI's best video of the last 30 — 5.10x, 256,518 views — is a plain
before/after of an ugly webpage next to a fixed one, **with no face at all.**
You make videos with an obvious before and after in them constantly and you have
never once put it in the frame.

### Text size and contrast

Theirs: two to four words, filling 30-50% of the frame width, heavy weight,
against dark saturated backgrounds with glow.

Yours: several are **small, thin type on white or cream**. *Claude Design |
Research Preview* is near-unreadable at feed size. *Is Opus 5 the Best?* is thin
grey type on a white field with a small logo, and that video did 0.9% CTR on
19,334 impressions — the worst impression-to-click ratio in your last 30.

Your own big-text thumbnails (`BEST AI MEETING ASSISTANT`, `17 SKILLS`, `STOP
CHATTING`, `I'LL SHOW YOU EVERYTHING`) are already in the right register. The
inconsistency is the problem — roughly half your grid is loud and half is a
product screenshot with a caption.

### Face

Theirs is either a **large expressive face** (Jack pointing, Ondrej deadpan) or
**no face and a huge outcome demo** (Chase's 5.10x). Yours is a consistent
medium-size neutral smile in almost every one. It is pleasant and it is invisible
in a feed. Pick a lane per thumbnail: big reaction, or no face and let the result
fill the frame.

---

## 5. Duration: it is a barbell

| Band | n | Median |
|---|---:|---:|
| Under 10 min | 7 | **1.56x** |
| 10-20 min | 24 | 1.00x |
| 20-35 min | 38 | 0.99x |
| **35-60 min** | 15 | **0.72x** |
| 60+ min | 5 | **2.11x** |

Short wins and very long wins. **35-60 minutes is the dead zone** — that is where
Chase's 51-minute course landed at 0.19x, and where your 47-minute Cowork course
landed too.

The 60+ band is small (n=5) but includes Nate Herk's *Claude Code for Non-Coders
(6 Hour Course)* at 2.34x and 149,415 views. That is the format you are about to
publish on Sunday, and this says the length is fine as long as it is positioned
as a complete course rather than a long video.

**Do not ship 40-minute videos.** Either tighten to under 20 or commit to a real
course.

---

## 6. The one comparison that will sting

Same topic. Different package.

| | |
|---|---|
| Chase AI | **Turn Claude Into A Design GENIUS In 3 Simple Steps** — 256,518 views |
| Tyler AI | **Claude Design is Incredible** — 521 views |

*Incredible* is your reaction. *Turn Claude Into A Design Genius In 3 Simple
Steps* is the viewer's outcome, plus a number, plus a promise that it is easy.
You were on the right topic. The package asked nobody to do anything.

Note also that "Claude Design" appears four separate times across Chase and Jack
in this window. It is a hot lane right now and you have already touched it.

---

## 7. What to do

**Confirmed, act on it:**

1. **Study Chase AI, not Sabrina.** 31% of subs per video, closest to your size.
   His formula: transformation promise + small number + "simple/easy", a hard
   before/after thumbnail, 15-23 minutes, shipped within days of the news.
2. **Add the before/after split to every thumbnail where one exists.** Six of
   eighteen winners use it, you use it zero times, and the single best video in
   the whole set is one.
3. **Stop shipping 35-60 minute videos.** Under 20, or a real course.
4. **Start using your own credential.** Pfizer AI engineer, ex-IBM, ex-Chase. It
   is the borrowed-authority format except you do not have to borrow it, and it
   is currently invisible across your entire catalog.
5. **Keep "I" only when it carries a stake or an external subject.** "I Tested X
   vs Y" is a repeatable 3.30x formula. "I automated my [thing]" is measured dead
   on channels 10x your size.

**Your call, flagged not decided:**

6. **Money in titles** is the strongest single pattern in the data (1.89x) and it
   is against your standing rule. Suggested compromise: keep it out of titles,
   put it in thumbnails and first lines.

**Do not conclude from this data:**

- *Course framing is a drag.* It shows 0.72x here on n=4, but this measures views
  against channels that are mostly news-driven. Your own course finding was about
  **impressions and subscribers**, a different metric, and it still stands.
- *New videos underperform.* The age table looks like it says that, but outlier
  is computed on lifetime views, so anything published this week is guaranteed to
  look low. That number is confounded and I am not using it.

---

## Data

```
data/2026-08-13-competitors-combined.csv   all 180 videos, all channels
data/2026-08-13-<channel>-last30.csv       one per channel
assets/competitor-pull.py                  regenerate: python3 competitor-pull.py @handle ...
```

Scores are recomputed from the CSV, so re-running the script updates the
numbers rather than leaving this file to drift.
