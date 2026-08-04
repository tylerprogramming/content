# Skool Onboarding Sequence (new free member → cohort)

Built 2026-07-31 from the `/harut` session on converting community members. Companion to
`platform/skool/free-community-plan.md` (strategy) and `platform/skool/cohort-launch-playbook.md`
(the launch runbook). Sent with `/email` via Resend.

**Who gets it:** every new member of the free community (`the-ai-agency`), starting the moment
they're accepted.

**What it is doing:** the free community is the lead magnet, not the product. This sequence walks a
new member from "I joined a thing" to "I want help implementing it," which is the cohort. It gives
away the information generously and only ever charges for implementation and access.

---

## The sequence

| # | Send | Subject | Job |
|---|---|---|---|
| 01 | Day 0, immediately on accept | Here are the skills | Hand over what they joined for, immediately |
| 02 | Day 1 (+24h) | Run this one first | Get ONE skill actually running today |
| 03 | Day 3 | Come to the live one | Invite to the live workshop, the conversion event |
| 04 | Day 7 | The part people get stuck on | Case study + raise-your-hand for the cohort |
| 05 | Weekly, ongoing | (varies) | Keep the list warm, one idea + one nudge |

### Why 01 and 02 are shaped this way

Most people entering this sequence are coming from the 040 video, and that video's CTA says
*"free skills, prompts, and the full setup are in my community."* So they joined to get the skills.

The first draft of this sequence opened with "go answer the pinned post, then open Start Here," which
is a fine generic welcome and completely wrong here. It makes someone who came for a specific thing go
hunt for it. **Email 01 now hands it over in the first line**, and email 02 gets one of them actually
running instead of teaching automation in the abstract.

The pinned-post ask moved to email 01's middle, tied to something they've done ("post which one you
picked"), which is a better engagement prompt anyway than "introduce yourself."

Harut's benchmarks to hold this against: contact new members inside 5 minutes (the Skool auto-DM does
that, this sequence is the follow-through), and a free community converting at 14%+ is healthy.

---

## Wiring it up

1. **Skool auto-DM fires first**, within minutes, pointing them at the pinned poll. That is a separate
   thing from this sequence and it should already be on.
2. **Export new members** (Members > Export) or Zapier it, then drop them into this Resend sequence.
3. **Segment on the join questions.** The free-community plan already asks niche, audience size, main
   channels, 90-day goal, biggest blocker. Two branches worth running:
   - *new to automation* → email 02 leans on the first-skill build
   - *already using Claude* → email 02 leans on scheduling and the multi-skill chain
   Everything else stays the same for both.
4. **Skool posts-as-emails** (allowed every 72 hours) is a separate channel and gets roughly double the
   open rate of a normal list. Use it for the live workshop and the cohort open, not for this sequence.

## The one thing that has to get built first

`{{SKILLS_PACK_LINK}}` in email 01 has to point at something real: the 17 skills, packaged, with a short
page on where the skills directory is. **It does not exist yet.** Everything upstream is already
promising it:

| Where | What it promises |
|---|---|
| 040 description + end card | "Free skills, prompts, and the full setup are in my community" |
| IG carousel 1 (SKILLS) | "I'll send you the full setup" |
| IG carousel 2 (BUILD) | "I'll send you the starter template" |
| IG carousel 3 (AUTOPILOT) | "I'll send you the scheduled setup" |
| IG carousel 4 (REAL) | "I'll send you my actual skill list" |
| This sequence, email 01 | the skills |

That's six promises pointing at five different-sounding deliverables, and none of them are built. Worth
collapsing to **one asset** — the skills pack in the classroom — and having every CTA say the same thing
about it. The carousel captions can keep their different comment words (SKILLS, BUILD, AUTOPILOT, REAL)
since those just trigger the DM, but the DM should deliver the same link every time.

## Before you send

- `{{SKILLS_PACK_LINK}}` in email 01 needs the packaged skills to exist. See above. This is the blocker.
- `{{PAID_OFFER_LINK}}` in email 04 is a placeholder. It points at the cohort application, which only
  exists once the cohort launch is actually running. Until then, either hold 04 or swap the CTA to the
  waitlist.
- `{{WORKSHOP_LINK}}` and the date in email 03 need the real Skool calendar event.
- No dollar amounts anywhere in here, per the standing rule. Pricing language goes through `/harut`
  before it ships.
- The case study in email 04 is written as a placeholder shape. Put a real member's before/after in it
  or cut the paragraph. Do not invent one.

## Status

| Step | State |
|---|---|
| Copy drafted | ✅ 2026-07-31 |
| Reviewed by Tyler | ☐ |
| Links filled in | ☐ |
| Loaded into Resend | ☐ |
| Live | ☐ |
