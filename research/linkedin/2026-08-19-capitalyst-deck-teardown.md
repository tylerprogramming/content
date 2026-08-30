# Capitalyst LinkedIn Decks - Teardown vs Tyler's Actual Numbers

**Source:** two decks by Miles and Patrice (Capitalyst LLC), part of a Skool-business organic course.
`LinkedIn Presentation - miles and patrice.pdf` (62 slides) and `Part 2` (18 slides).
**Analyzed:** 2026-08-19, against the account data pulled the same day (see `BRAIN/linkedin/brain.md`).

**Verdict:** the content half of these decks is good and, more usefully, it **independently confirms four rules
I had already derived from Tyler's own analytics from a completely different direction.** One apparent conflict
turns out to be a refinement that makes our rule better. The outreach half is for a different business model and
should be skipped.

---

## 1. What the decks confirm (already in the brain, now double-sourced)

| Brain rule | Deck says |
|---|---|
| #4 Always ship an image | "You should incorporate an image of you, or a diagram/infographic into **every** post." (P2 s11). Lists working creative formats: professional-atmosphere photos, static notepad/list images, **screenshots**, repurposed YouTube thumbnails, carousels. (P2 s16-17) |
| #5 Emoji step markers / numbered steps | "Number Them. People really appreciate lists on LinkedIn." "Lists thrive in professional settings. They're easy to organize, take notes on." (P1 s46-47) |
| #8 Use your standing, it is an unused asset | "You can spend up to 10% of the post just talking about what you've done." "**LinkedIn actually promotes your accomplishments for you.** It's a professional platform, and people are literally looking for ways to measure your status." (P1 s48-49) |
| #10 Long is fine when it is a build | 80% of posts should be **long-form, over 300 words**; 20% short. (P1 s14) |

Plus a direct explanation of the three worst posts on the account (40, 53, 55 impressions):

> "Posts that go deep... are much more valuable than a vague, 200 word post about general sales.
> Posts with depth and actionable insights outperform numerous shallow and generic posts." (P1 s20)

That is precisely the failure mode of "I used to be the person moving files around for Claude."

---

## 2. The decks' hook framework predicts our measured winners

The decks name three hook lanes (P1 s39). Mapping them onto the last 15 posts:

| Deck lane | Tyler's posts | Result |
|---|---|---|
| **Big Mistake or Threat** | "I never learned the video editor." / "I stopped editing my own videos." | 213, **366** |
| **Contrast or Controversy** | "Most people use Claude Code like a fancier chatbot." / "Most people think the hard part is X. It really isn't." | **551**, 197 |
| **Big Accomplishment** | *never used* | untested |

Two independent frameworks landing on the same answer is worth more than either alone. It also exposes the gap:
**the accomplishment lane is the one the platform actively boosts and the one Tyler has never run.** He has the
material and never uses it: AI engineer at Pfizer, 8 years at IBM and JPMorgan Chase, 30k+ people taught, a
content operation that runs out of one folder of text files.

---

## 3. The one real conflict, and why the resolution is better than either side

**Deck (P2 s6, s11):** "❌ A CTA to click a link, this takes people off the platform and hurts your post
performance." "Remove links from posts. Put the links in your bio, and in DM messages."

**Our data:** the 31,875-impression post has an inline `lnkd.in` video link in the body. The smolagents post
links YouTube directly. These are the two best posts on the account.

**Resolution: the link is not the problem. Making the click the *ask* is the problem.**

Look at what the winners actually ask for:
- Tyler's 31k post: link sits mid-body, and the closing ask is "👇 Let me know what you've created!" A **comment** CTA.
- The deck's own example (Max Perzon, P2 s8): no link at all, ask is "comment 'Skool' below and I'll send you my free course." A **comment** CTA.

Both keep the *ask* on-platform. The link is just reference material for people who want it. So the refined rule is:

> **Link in the body is fine. Never make clicking it the call to action.** Close on a comment or DM ask, every time.

This supersedes brain rule #7 as originally written, which said only "put the link in the body" and left the
CTA question open. Updated in the brain.

---

## 4. The biggest gap these decks expose: the engagement flywheel

Part 2 is largely about a mechanism the account currently runs at zero.

> "Comments, likes, sends, all are valuable on the other platforms. But on LinkedIn? **That's literally how you
> grow.** When someone comments on your post, it gets shared with their network. When you respond, LinkedIn
> pushes that post out to more people." (P1 s59)

> "LinkedIn's algorithm rewards **engagement over posting frequency**." (Neil Patel, cited P1 s62 / P2 s18)

Tyler's engagement numbers: **47 comments across 365 days. Zero comments on 13 of the last 15 posts.**

This is the mechanism behind the one outlier. The 31,875 post did not win on comments (it had 2). It won on
**12 reposts**, which is the same flywheel running through the share path instead of the comment path. The whole
rest of the year produced 3 reposts. Nothing is being fed into the flywheel at all.

Two specific plays from the decks that cost nothing and are not being run:

1. **Engage with 10 influencers who share your avatar** (not competitors), daily. "This can bring in multiple new
   followers a day just through comments." (P1 s58)
2. **Respond to every comment yourself, first, before outsourcing any of it.** "People want to speak to YOU."
   (P2 s18) Each response pushes the post further.

And the CTA design rule: **ask for a response, not an opinion-shaped nothing.** The deck's example is ending a
protein post with "What's your favorite high protein meal?" Concrete, answerable in four words, from the reader's
own life. Compare the account's current closers, which get zero.

---

## 5. Cadence (untested here, cheap to adopt)

- **3 to 5 posts per week**, 80% long-form (300+ words), 20% short. (P1 s14, s19)
- **Tuesday to Thursday** for maximum visibility; Monday to Friday generally. (P1 s15)
- **Before 9am**, or **4-5pm onwards** when people log back on. (P1 s15)
- "Only 1% of users post weekly, so your benefit is you fill that void." (P1 s16)

No data on this for Tyler's account. Worth adopting as a default because it is free, but log it as unconfirmed.

---

## 6. PAS, as a fallback for insight posts

Problem, Agitation, Solution (P2 s9), for when there is no build to point at:
- **Problem:** state the problem the reader is having.
- **Agitation:** what it costs them down the line.
- **Solution:** the actionable close.

This is worth adding to insight mode. Note it already describes the 197-impression arcade post almost exactly:
problem (connecting is not the hard part), agitation (your agent quietly dies after seven days and never tells
you), solution (arcade.dev holds the auth). That post was the best of the recent batch.

---

## 7. What to reject

**The entire outbound half of Part 1** (slides 22-29): Sales Navigator searches, connection requests at scale,
"always start with a video that has a question," then a Loom pitch. This is a coaching/agency lead-gen machine.
Capitalyst sells Skool-business consulting, so their deck optimizes for booked calls. Tyler's stated objective is
**authority first, Skool second**. Adopt none of this unless he decides to sell SkoolOS through outbound, which
is a separate decision from how the content is written.

**Money-amount hooks.** The deck's flagship example opens "I made $655,104 w/ a free course." This violates
Tyler's standing rule (no money amounts) and, more importantly, his positioning: he is a working engineer showing
what he built, not a guru showing what he earned. See `BRAIN/tyler-voice.md`.

**Controversy hooks.** The deck recommends them and then immediately warns you get "upset internet addicts
commenting on your posts" (P1 s40). Use the contrast lane, skip the controversy lane. Contrast is what already
produced the 551.

**"Repurpose your Skool posts onto LinkedIn"** (P1 s11). Fine, but it is a filler tactic. It produces insight
posts, which cap around 551 on this account. The build post caps at 31,875. Do not let repurposing displace the
build post.

---

## 8. What changes as a result

Applied to `BRAIN/linkedin/brain.md`:
- Rule #7 refined: link in body, but never a click CTA. Close on comment or DM.
- New rule: the engagement flywheel (respond first and personally, engage 10 avatar-adjacent accounts).
- New rule: the accomplishment hook lane, currently unused.
- New section: cadence defaults, marked unconfirmed.
- PAS added to the insight-post section.
- Hook lanes cross-referenced against measured results.

Applied to `/linkedin-writer`:
- Scorecard check 8 changed from a click-through assumption to a comment-CTA requirement.
- Insight mode gains the three hook lanes and PAS.
- Build mode gains the accomplishment line as an optional part 1 variant.
