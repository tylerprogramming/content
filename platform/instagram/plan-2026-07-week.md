# IG plan — week of 2026-07-27

Built on `research/instagram/2026-07-24-competitor-cadence.md`. Cadence target:
**3 reels + 8 carousels per week.** Every post carries a comment gate.

## The gate is the whole point

Every outlier in the research gated a deliverable behind a comment. Copy the
mechanic, not the deliverable — theirs are PDFs, ours are working repos and
installable skills, which is a better trade for whoever comments.

Caption template, lifted from sabrina_ramonov (1M followers, ~3 posts/day, same
five-part structure every time):

```
Follow and comment "WORD" and I'll send you [deliverable] 👇

[one-line hook]

[body: the list, or the mechanism, in plain language]

[3 literal search questions — this is IG SEO]

#5 #hashtags #max #no #more
```

The three question lines matter. She writes the exact query someone would
search, inside the caption. None of the other three accounts do it.

**Carousels get music.** Both top carousel accounts attach audio (theromanknox
`♫ TVN`, brodyautomates `♫ Giulio Cercato`). Whether it changes distribution is
unproven, but it costs one tap.

## 8 carousels

Twelve listed so you can drop the four that don't fit. Slugs marked ✅ already
have `content.md` + `captions.md` written in `platform/carousels/` and only need
rebuilding in the Terminal theme.

| # | Carousel | Source | Gate |
|---|---|---|---|
| 1 | 5 Claude Code skills that replaced my content workflow | new, Skill Drop framework | `SKILLS` |
| 2 | 25 Claude Code skills, ranked by how often I actually use them | ✅ `25-claude-code-skills` | `RANKED` |
| 3 | I automated my video editing with Claude Code | video `026` (live 07-22) | `EDITOR` |
| 4 | One command that builds a whole carousel | ✅ `one-command-carousel` | `STUDIO` |
| 5 | My entire week of content, scheduled in one sitting | ✅ `schedule-full-week` | `WEEK` |
| 6 | Claude Routines: the setup I run every morning | ✅ `claude-routines` + video `024` | `ROUTINE` |
| 7 | The transcribe skill that reads any video into my repo | ✅ `transcribe-skill` | `TRANSCRIBE` |
| 8 | Seedance vs Kling: same prompt, both models | ✅ `seedance-vs-kling` | `COMPARE` |
| 9 | I run my entire YouTube channel with AI | video `027` (with editor) | `CHANNEL` |
| 10 | The thumbnail skill that tests 3 models at once | ✅ `thumbnail-skill` | `THUMB` |
| 11 | $500 ad for $0 | ✅ `500-dollar-ad-for-0` | `AD` |
| 12 | 32 pieces of content in one day | ✅ `32-pieces-one-day` | `THIRTYTWO` |

Nine of twelve are already written. The work this week is **rebuilding them in
the Terminal theme and adding the gate**, not writing new content.

## 3 reels to film this weekend

All three are screen recordings. No talking-head setup, no lighting, and each
one is a thing you already do.

### Reel 1 — "one command, whole carousel" (~25s)
Screen record Carousel Studio: type a topic, hit Generate, cut to seven finished
slides, hit Export. No narration needed; on-screen text only.
- Hook (first 2s, on screen): `one command. whole carousel.`
- Gate: `STUDIO`
- Reuse: YouTube Short, LinkedIn native video, FB Reel

### Reel 2 — "the skill I install on every new machine" (~30s)
Terminal only. `claude skill add` for your three most-used skills, showing the
install output. This matches the Terminal carousel theme exactly, so the reel and
the carousel look like the same product.
- Hook: `first 3 commands on a fresh laptop`
- Gate: `SKILLS`
- Reuse: Short, LinkedIn, X video

### Reel 3 — "I edited this video by typing" (~35s)
Use the `026` footage you already shipped. Split screen: your prompt on the left,
the edit happening on the right. This is the highest-ceiling of the three because
the payoff is visual and instant.
- Hook: `I did not touch a timeline`
- Gate: `EDITOR`
- Reuse: Short, LinkedIn, FB

## Cross-platform

| Platform | What changes |
|---|---|
| YouTube Shorts | Same vertical cut. Gate does not work — swap the CTA to "full video in description". |
| LinkedIn | Carousel as PDF, no hashtags, longer caption. Gate becomes "comment and I'll send it" — works well there. |
| Facebook | Reels cross-post from IG directly. Low effort, take it. |
| X | Carousel as image thread, slide 1 + punchy line, then numbered replies. |

## Scheduling

sabrina_ramonov posts at roughly 15:30, 18:45 and 22:30 UTC daily — fixed slots,
not ad-hoc. Pick three slots and keep them. With 11 posts across 7 days that is
1-2 a day, comfortably inside what one batch session can produce.

## Guides / funnel

Every gate above needs something to send. Ranked by effort:

1. **Already exists, zero work** — Carousel Studio repo link (gates 1, 4)
2. **One file** — a `.md` with the install commands for the skills you name
   (gates 2, 6, 7, 10)
3. **Real guide** — the "how I run a channel with AI" walkthrough (gate 9)

Start with 1 and 2. Nobody in the research is sending anything more elaborate
than a PDF, and a working repo already beats that.
