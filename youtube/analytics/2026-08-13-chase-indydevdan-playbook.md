---
title: The Chase AI and IndyDevDan formulas, decomposed and applied to the pipeline
date: 2026-08-13
kind: analytics
status: proposal
---

# Two formulas worth stealing

Chase AI does **31%** of his subscriber count per video, IndyDevDan **22.6%**.
Nobody else in the set is close, and they are the two nearest to us in size
(162K and 144K). They are not doing the same thing, though — the formulas are
almost opposites, and each fits a different slot in our pipeline.

---

## Chase AI — transformation and ease

Every title promises the viewer becomes capable, and that it is easy.

| Outlier | Title |
|---|---|
| **5.10x** | **Turn** Claude Into A Design **GENIUS** In **3 Simple Steps** |
| 1.58x | **The #1** Claude Code Design Skill **Just** Got a **HUGE** Upgrade |
| 1.56x | Opus 5 **Just** Dropped and Its Numbers Are Legit **INSANE** |
| 1.02x | **The #1** Trending Github Repo **Just SOLVED** Claude's Search Problem |
| 1.00x | **You're** Paying Anthropic 20x **MORE** Than **You** Need To |

**The parts:**

1. **A transformation verb.** `Turn X into Y`. Not "here is X", but "you end up
   with Y". This is the whole engine of the 5.10x.
2. **An ease qualifier.** `In 3 Simple Steps`. A small number — 3, not 12 — plus
   the word *Simple*. The number caps the effort, it does not measure the content.
3. **Exactly one caps word, late in the title.** GENIUS, HUGE, INSANE, SOLVED,
   MORE. Always at or near the end, so it lands as the payoff.
4. **`The #1` as a cheap authority prefix.** Used twice.
5. **Second-person accusation.** *You're Paying Anthropic 20x MORE Than You Need
   To.* The viewer is currently doing something wrong. That is a strong hook and
   we have never once used it.

**What he does NOT do:** he never describes the tool. There is no "Claude Design
Explained" on his channel.

---

## IndyDevDan — replacement and identity

Every title says something you rely on is finished, or names who you are.

| Outlier | Title |
|---|---|
| **7.49x** | The Pi Coding Agent: The **ONLY REAL** Claude Code **COMPETITOR** |
| 5.20x | My M5 Max, Gemma 4, MLX LOCAL Stack. **(This KILLS MODEL PROVIDERS)** |
| 3.43x | **FORGET** Loop Engineering. Agentic Engineering is about **THIS** |
| 2.08x | I Studied Stripe's AI Agents... Vibe Coding **Is Already Dead** |
| 1.81x | The Claude Code Feature **Senior Engineers** KEEP MISSING |

**The parts:**

1. **Replacement framing.** FORGET X. X is Already Dead. This KILLS Y. The ONLY
   REAL competitor. Every one of his top five kills something.
2. **Viewer identity, named.** `Senior Engineers`, `Engineers...`. The viewer is
   told this video is for their professional tier. Flattering and exclusionary at
   once, which is why it works.
3. **A parenthetical payoff.** `(This KILLS MODEL PROVIDERS)` — the title states
   the thing, the parenthesis states the consequence.
4. **A colon or a hard stop.** `Subject: The claim about it.` Two beats, not one
   long sentence.

**Which one fits us?** Chase's, mostly. His is accessible and it matches the
low/no-code direction. Dan's replacement framing needs standing to pull off —
but the Pfizer credential gives us exactly that standing, and it is unused.

---

## Thumbnails: the finding that surprised me

**Five of their six top thumbnails have no face at all.**

- IndyDevDan's top three: `PI AGENTS`, `M5 GEMMA4 MLX`, `LOOP ENG ❌ | SDLC ✅`.
  Zero faces. Hands on a keyboard, or nothing but type.
- Chase's best (5.10x, 256,518 views): `SLOP → FIXED`, two webpage panels. No face.

Our face is in **nine of nine**. It is a pleasant medium-size neutral smile in
every single one, which averages out to invisible.

**The spec both of them follow:**

| | |
|---|---|
| Word count | **2 to 4 words.** Never a sentence. |
| Size | Type fills **35-50% of the frame width**. Readable at 120px wide. |
| Colour | One accent (yellow, red, green) against dark. Semantic where possible — red ❌ for the old way, green ✅ for the new. |
| Structure | A **split** or an **arrow**: before → after, A vs B, old ❌ / new ✅. |
| Face | Either **absent**, or **large and reacting**. Never medium and pleasant. |

---

## Applied to what is in flight

Titles below are **proposals, not changes** — 045's title is Tyler's pick and
stays until he says otherwise.

### 045 — Arcade / connect apps (recorded)

Current: `Claude Code Can Finally Use ANY Tool (7 Minutes, No Code)`

Solid — it has the caps word and the time promise. What it lacks is Chase's
transformation: "ANY Tool" is abstract, and the viewer cannot picture the end
state. Options:

- **Turn Claude Code Into A Real Assistant In 7 Minutes (No Code)** — Chase's
  transformation grafted onto the parts we already have. Recommended.
- **Your Claude Code Can't Touch Your Apps. This Fixes That.** — Chase's
  second-person accusation, Dan's hard stop.

**Thumbnail:** split, no face. Left panel a terminal that can only talk, right
panel the same terminal reading Gmail and Calendar. Two words: **`TALKS` →
`DOES`**. That is the single clearest before/after in the whole pipeline and it
is currently not being used.

### 047 — MCP course (Sunday)

Current: `How To Give AI Agents Access To ALL Your Apps (Full MCP Course)`

**Leave it.** It already matches the grammar of our best-performing video and it
carries the search term. Chase-ifying it would cost the `MCP course` query.

**Thumbnail:** this is the one place to keep the face, because a course sells on
trust. Use Chase's `OPUS 5` composition rather than his `SLOP → FIXED` one: huge
type on the left two thirds, face in the right third. Words: **`ANY APP`** at
full height, with eight app logos below. Not a sentence, not a caption.

### Blotato (filming today, sponsored)

Nothing packaged yet, so this one starts clean and should be built on the formula
from the start:

- **Turn One Video Into 30 Posts In 3 Simple Steps** — the closest thing to a
  direct clone of the 5.10x. Transformation, small number, ease.
- **You're Posting To 9 Platforms By Hand. Stop.** — the accusation variant.

**Thumbnail:** split, no face. Left a mess of nine browser tabs, right one
dashboard. **`9 TABS` → `1`**.

### 10 Claude Code Skills You Can Steal (Every File Included)

Title is already right — a number, a possession verb, a giveaway parenthetical.

**Thumbnail:** we already have the correct register in the `17 SKILLS` thumbnail
from 040. Reuse that treatment, bigger: **`10 SKILLS`** at full height, the file
grid behind it, drop the face to a corner or cut it. Add **`FREE`** in the accent
colour if the repo is public at launch.

### 048 / 049 — MCP server builds

These are where Dan's replacement framing fits, and where the Pfizer credential
should make its first appearance:

- **FORGET Paid MCP Hosting. Do This Instead.**
- **How A Pfizer AI Engineer Builds MCP Servers**

---

## The four changes that matter most

1. **Put a before/after in the thumbnail.** Six of their eighteen do it, we do it
   zero times, and the best video in the set is one.
2. **Drop the face on at least half.** Five of their six top thumbnails have none.
3. **Use a transformation verb in the title.** `Turn X into Y`, not `X Explained`.
4. **Try the second-person accusation once.** *You're doing this the hard way.*
   Chase gets 50,000 views a time on it and we have never run it.
