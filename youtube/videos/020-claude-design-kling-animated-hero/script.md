# Script — Claude Design + Kling 3 = Animated Landing Pages in Minutes

**Working title:** Claude Design + Kling 3 = Animated Landing Pages in Minutes
**Target runtime:** 13-16 minutes
**Angle:** Niche technique combining two tools. Animated hero sections are hard and expensive. AI makes them cheap and fast.

---

## [0:00 - 0:30] Hook — Proof Open

[SHOW: Full-screen finished landing page with cinematic animated hero playing — 4 full seconds]

Most landing pages look dead. Static hero image, static headline, nothing moves. This one was generated in 15 minutes with Claude Design and Kling 3 — and it moves like Apple's product pages.

[SHOW: Three X marks over After Effects, motion designer, invoice icons]

No After Effects. No motion designer. No $5,000 invoice.

[SHOW: Split — Claude Design canvas | Kling 3 generation playing]

I'll show you the exact workflow. Claude Design for the page. Kling 3 for the hero video. And the one trick that ties them together so the hero plays natively in the browser.

Let's go.

---

## [0:30 - 2:00] Section 1 — Why animated heroes matter (and why they're hard)

[SHOW: Scroll through Apple, Stripe, Linear product pages — all with subtle hero animations]

Apple, Stripe, Linear, Notion. Every premium brand landing page has a subtle animated hero. It's not decoration. It's the single biggest first-impression lever you have.

[SHOW: Static hero vs animated hero comparison]

Research has shown that animated hero sections can lift conversion by 15 to 30 percent on landing pages. That's not a small number. But animation has historically been expensive. Motion designer plus After Effects plus revisions equals three to five thousand dollars and two weeks.

[SHOW: Tyler on camera]

Today that math is broken. We can do it in 15 minutes for three bucks.

[NOTE: ~1:30 runtime. Sets stakes.]

---

## [2:00 - 4:00] Section 2 — The workflow overview

[SHOW: Flow chart — Claude Design → hero still exported → Kling 3 animates still → MP4 embed back in page → deploy]

Here's the full workflow before we dive in.

Step one. Build the static landing page in Claude Design. Normal flow.

Step two. Export the hero section as a still image.

Step three. Drop that still into Kling 3 as the start frame, prompt the animation.

Step four. Download the MP4. Drop it into the page as a video element with autoplay loop muted.

Step five. Deploy.

Four tools. Fifteen minutes. Let me show you.

[NOTE: ~2:00 runtime. Overview so viewers know what's coming.]

---

## [4:00 - 6:30] Section 3 — Build the landing page in Claude Design

[SHOW: Claude Design new prototype, prompt being typed]

I'm building a landing page for a hypothetical product — an AI workout coach app.

Prompt:

```
Landing page for an AI workout coach mobile app called Forge.
Dark theme, fitness-adjacent, premium feel similar to Apple Fitness+.
Hero section should feature a phone mockup with a workout UI.
Include sections: features (3 columns), testimonials, pricing, app store CTAs, footer.
Before generating, ask me 4 clarifying questions.
```

[SHOW: 4 clarifying questions appearing, answering each]

Fitness category, targeting serious lifters, dark color palette with one accent color (I pick red), and yes include a subtle gradient.

[SHOW: Generation happening, finished page scrolling]

Four minutes later I have the full static page. Hero, features, testimonials, pricing, footer.

[SHOW: Hero section close-up]

The hero has a phone mockup with a workout screen and a gradient background. Static. Now we need to make it move.

[NOTE: ~2:30 runtime.]

---

## [6:30 - 8:30] Section 4 — Export the hero still for Kling

[SHOW: Screenshot or export the hero section as PNG at 1920x1080 — whatever Claude Design supports]

In Claude Design, I export the hero section as a PNG. 1920 by 1080, or 2K if Kling accepts it.

[SHOW: Kling 3 interface, dragging the still in as start frame]

I open Kling 3. Image-to-video mode. Drop the PNG in as the start frame.

[SHOW: Typed Kling prompt on screen]

Prompt:

```
Subtle parallax motion. Gradient background shifts slowly from deep red to black.
Phone mockup gently floats up and down with slight rotation.
Particles of light drift across the background.
Cinematic, 10 seconds, 4K.
```

The trick is "subtle." Most beginners over-prompt animation and get distracting motion. You want hero animation to feel alive but not demand attention.

[NOTE: ~2:00 runtime. The subtle-prompt tip is the tactical nugget here.]

---

## [8:30 - 10:00] Section 5 — Kling generates the hero video

[SHOW: Kling 3 generation progress, then the finished 10-second video]

Kling generates. This takes about 2 minutes.

[SHOW: Finished hero animation playing full screen]

Here's what it came back with. Gradient shifts. Phone floats. Particles drift. Exactly what I prompted.

[SHOW: Cost panel]

Cost. About fifty cents for a 10-second 4K clip.

[NOTE: ~1:30 runtime.]

---

## [10:00 - 12:30] Section 6 — Embed the video back into the landing page

[SHOW: Claude Code terminal, open the project from Claude Design handoff]

Now the fun part. We hand the Claude Design project off to Claude Code and update the hero section to use our video.

[SHOW: Typed prompt in Claude Code]

```
Replace the hero section's static background gradient with a video element.
Use /assets/hero-animation.mp4 (I'll add the file).
Autoplay, muted, loop, playsinline.
Overlay the existing headline and CTA buttons on top with readable contrast.
```

[SHOW: Drop the Kling MP4 into /public/assets/]

I drop the MP4 into the public assets folder. Claude Code writes the component update.

[SHOW: Run npm run dev, localhost preview]

Localhost. The hero is now animated. Headline overlays cleanly. CTAs remain clickable.

[NOTE: ~2:30 runtime. The implementation payoff.]

---

## [12:30 - 13:45] Section 7 — Deploy via Vercel MCP + performance considerations

[SHOW: One prompt in Claude Code]

```
Deploy to Vercel production. Return the live URL.
```

[SHOW: Claude Code using Vercel MCP, build logs streaming, live URL returned]

I never left Claude Code. The Vercel MCP handles the commit, push, and deploy. One line to install if you haven't: `claude mcp add --transport http vercel https://mcp.vercel.com`.

[SHOW: The live animated hero playing on production]

15 minutes total. $3 in combined credits.

[SHOW: Performance tab — video file size, LCP metric]

Performance note. Hero videos are heavy. Target 2-5MB for the MP4. Kling exports bigger, so compress with ffmpeg first. I'll drop the ffmpeg one-liner in the description.

[NOTE: ~1:15 runtime. Honest tradeoff beat.]

---

## [13:45 - end] Outro

[SHOW: Split-screen before static / after animated]

Recap. Claude Design for the page. Kling 3 for the hero video. Claude Code for the embed. Deploy to Vercel.

[SHOW: Skool community preview]

The full prompts, the ffmpeg compression one-liner, and three more hero animation examples are in my Skool community. Link below.

[SHOW: Tyler on camera]

If you run this on a real product page, drop the link in the comments — I'll share the best ones in the next video.

Subscribe for more.

---

## Running total (target 13-16 min)

| Section | Target | Running |
|---|---|---|
| Hook | 0:30 | 0:30 |
| Why animated heroes | 1:30 | 2:00 |
| Workflow overview | 2:00 | 4:00 |
| Build page in Claude Design | 2:30 | 6:30 |
| Export still for Kling | 2:00 | 8:30 |
| Kling generates video | 1:30 | 10:00 |
| Embed video via Claude Code | 2:30 | 12:30 |
| Deploy + perf | 1:15 | 13:45 |
| Outro | 1:00 | 14:45 |

**Target: 14-15 minutes**
