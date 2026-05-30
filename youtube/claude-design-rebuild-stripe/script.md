# Script — I Rebuilt Stripe's Homepage in Claude Design in 20 Minutes

**Working title:** I Rebuilt Stripe's Homepage in Claude Design in 20 Minutes
**Target runtime:** 14-17 minutes
**Angle:** Famous homepage recreation. Proof-of-concept format. Single long demo + analysis.

---

## [0:00 - 0:30] Hook — Proof Open

[SHOW: Split-screen — Stripe.com live, Claude Design canvas rendering the rebuild]

Stripe's homepage is one of the best-designed sites on the internet. I just rebuilt it in Claude Design in 20 minutes with one prompt and three iterations.

[SHOW: Three X marks animate over "No layers, No Figma, No design system"]

No layers. No design system imports. No Figma. Just Claude Design and a screenshot.

[SHOW: Final rebuilt page scrolling]

I'll show you the full process, the exact prompts, and the one iteration trick that got me 90 percent of the way there in five minutes.

Let's go.

---

## [0:30 - 2:00] Section 1 — Why Stripe's homepage is hard

[SHOW: Screen recording scrolling Stripe.com slowly]

Stripe's homepage is not just clean. It has a specific set of design challenges that most AI tools get wrong.

[SHOW: Annotated callouts on Stripe homepage]

The gradient animation behind the hero. The typographic hierarchy that handles five tiers of information without feeling cluttered. The 3D globe visualization. The card grid that collapses perfectly to mobile. The subtle color system that holds together across 30 plus sections.

If Claude Design can handle Stripe, it can handle almost anything you'll actually build.

[NOTE: ~1:30 runtime. Sets stakes before the demo.]

---

## [2:00 - 3:30] Section 2 — Setup and the one screenshot trick

[SHOW: Take a screenshot of Stripe.com hero section. Drag it into Claude Design]

Here's the setup. I took one screenshot of Stripe's hero section. That's it.

[SHOW: Claude Design prompt box with the screenshot attached]

In Claude Design, new prototype, high fidelity, and I attach the screenshot.

Then the prompt. One paragraph.

[SHOW: Typed prompt on screen]

```
Rebuild this landing page in the same visual style.
Match the gradient hero, typographic hierarchy, and card-based feature sections.
Use the exact color palette from the screenshot.
Add sections for: products, pricing, testimonials, footer.
Before generating, ask me 5 clarifying questions.
```

The "ask me 5 clarifying questions" is the trick. This is borrowed from plan mode in Claude Code. Without it, Claude Design generates once and you hope. With it, you get a back-and-forth that saves iterations and tokens.

[NOTE: ~1:30 runtime. The screenshot+plan-mode trick is the video's first tactical nugget.]

---

## [3:30 - 5:00] Section 3 — The plan-mode Q&A

[SHOW: Claude Design's clarifying questions appearing]

Claude comes back with questions. What industry is the product in. What's the tone — corporate, technical, playful. Should the hero animation be subtle or bold. Do I want dark mode. What's the pricing structure.

[SHOW: Answering each in real time]

I answer: fintech, technical, subtle, light mode, three tiers.

[SHOW: Click continue, generation panel loading]

Five questions, thirty seconds of back and forth, and now Claude has enough context to get the first pass right instead of making me iterate five times.

[NOTE: ~1:30 runtime. The pro tip lands here.]

---

## [5:00 - 8:00] Section 4 — First generation + honest review

[SHOW: Generated page full screen, scrolling top to bottom]

Here's what Claude Design came back with.

[SHOW: Annotated callouts highlighting what's great and what's off]

What it nailed — typographic hierarchy, card grid, color palette from the screenshot, overall section rhythm. About 75 percent there.

What it got wrong — the gradient in the hero is too soft. The pricing table spacing is off. There's no 3D globe visualization — it substituted a flat world map. The testimonials section has a weird height.

[SHOW: Stripe's actual homepage for comparison]

Let's fix these with iteration.

[NOTE: ~3:00 runtime. Honest review beat is critical for trust.]

---

## [8:00 - 11:30] Section 5 — Three iterations to 90 percent

[SHOW: Tweaks panel]

Iteration 1. Tweaks panel. Increase gradient intensity. Tighten pricing table. Fix testimonial height.

[SHOW: Updates happening]

Iteration 2. Comment on the hero. "Make the gradient more vibrant and add animated depth, Stripe-style."

[SHOW: Claude applies comment]

Iteration 3. Draw mode. Circle the flat world map. Write "make this a 3D rotating globe." Send.

[SHOW: Claude replaces with a 3D globe]

Ten minutes total across the three iterations. I'm at about 90 percent of Stripe now.

[NOTE: ~3:30 runtime. Show the real iteration loop. This is what viewers came for.]

---

## [11:30 - 13:30] Section 6 — Side-by-side reveal + what it cost

[SHOW: Full split-screen — Stripe.com left, my rebuild right, both scrolling in sync]

Here's the comparison. Stripe on the left, my Claude Design rebuild on the right.

[SHOW: Scrolling through each matching section]

Hero — matches. Feature cards — matches. Pricing — matches. Testimonials — matches. Footer — matches.

The 3D globe is close but not identical. The gradient is 95 percent there. The typographic rhythm is indistinguishable.

[SHOW: Usage dashboard]

Cost. 18 percent of my weekly Pro allowance. That's about a dollar twenty five in API credits equivalent.

[NOTE: ~2:00 runtime. The reveal payoff.]

---

## [13:30 - 14:15] Section 7a — Deploy via Vercel MCP (optional beat)

[SHOW: One prompt in Claude Code]

```
Deploy this Stripe rebuild to Vercel production and send me the live URL.
```

[SHOW: Claude Code using Vercel MCP to deploy — live URL returned]

90 seconds later, the rebuild is live. I'm using the Vercel MCP so Claude Code handles deploy without tab switching. If you haven't set that up, it's one command: `claude mcp add --transport http vercel https://mcp.vercel.com`. Free on Vercel Hobby.

[NOTE: ~0:45 runtime. Optional but tightens the "recreation to live URL" loop.]

---

## [14:15 - 15:30] Section 8 — When this works and when it doesn't

[SHOW: Decision slide]

Recreation workflow works for — landing pages, marketing sites, pricing pages, feature showcases, docs sites. Anywhere the design language is standardized.

It breaks down on — product interfaces (Notion, Linear app UI), complex SaaS dashboards, brand identity that relies on custom illustration, sites with bespoke 3D or WebGL work.

[SHOW: Tyler on camera]

Use this for content sites. Not for app interfaces. Know the difference.

[NOTE: ~2:00 runtime. Decision framework protects the viewer.]

---

## [15:30 - end] Outro

[SHOW: Talking head]

Recap. One screenshot plus one prompt plus three iterations equals a 90 percent Stripe rebuild in 20 minutes. The "ask me 5 questions first" trick is the key unlock.

[SHOW: Skool community preview]

The exact prompt, the screenshot setup, and three more recreation examples are in my Skool community. Link below. Free.

[SHOW: Tyler on camera]

Drop in the comments what homepage you want me to rebuild next. I'll do the top-voted one on the channel.

Subscribe for more.

---

## Running total (target 14-17 min)

| Section | Target | Running |
|---|---|---|
| Hook | 0:30 | 0:30 |
| Why Stripe is hard | 1:30 | 2:00 |
| Setup + screenshot trick | 1:30 | 3:30 |
| Plan-mode Q&A | 1:30 | 5:00 |
| First gen + review | 3:00 | 8:00 |
| Three iterations | 3:30 | 11:30 |
| Side-by-side reveal | 2:00 | 13:30 |
| When it works | 2:00 | 15:30 |
| Outro | 1:00 | 16:30 |

**Target: 16-17 minutes**
