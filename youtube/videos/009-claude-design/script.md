# Script — Claude Design Video

**Working title:** Claude Design + Claude Code: Prompt to Live URL in 23 Minutes
**Target runtime:** 20-24 minutes
**Angle:** Complete production workflow. Prototype in Claude Design, hand off to Claude Code, deploy live.

---

## [0:00 - 0:30] Hook — Proof Open

[SHOW: Fast cut — Claude Design canvas prompt → generated design → Claude Code terminal running → live URL with domain in browser bar]

I built this landing page in Claude Design, handed it off to Claude Code, and deployed it to a live URL in 23 minutes.

[SHOW: Three X marks animate over icons of Figma, a designer illustration, a code file]

No Figma. No designer. No frontend code.

This video shows the full workflow end to end. Every click. Every prompt. Every error.

[SHOW: Quick cut to Claude usage screen showing weekly limit warning]

Plus what it actually costs, because there's a catch nobody's talking about.

Let's go.

[NOTE: Keep energy confident, not hyped. Let the result sell itself. 25 seconds max on camera.]

---

## [0:30 - 2:10] Section 1 — What Claude Design actually is

[SHOW: Talking head + overlay graphics]

Claude Design is Anthropic's new visual design tool. It launched on April 17th. It's powered by Opus 4.7. And here's what it actually does.

[SHOW: Screen recording — claude.ai/design homepage]

You describe what you want in plain English. Claude generates a prototype you can edit in the canvas. You iterate with tweaks, comments, and even drawings. And when you're ready, you hand the whole thing off to Claude Code with one command.

That last part is the thing nobody's covering well.

[SHOW: Split-screen showing Chase AI and Nate Herk thumbnails]

The videos you've seen on Claude Design mostly stop at the prototype. They show you how to generate a landing page and they move on. What they skip is the full workflow — prompt, iterate, ship, deploy.

So that's what I'm doing today.

[SHOW: Back to talking head]

Quick context on access. Claude Design is not free. You need Pro, Max, Team, or Enterprise. Pro is 20 dollars a month. We'll come back to cost at the end — there's a wrinkle.

[NOTE: ~90 seconds. Setup done. Move into the build.]

---

## [2:10 - 4:30] Section 2 — Setting up the brand design system from screenshots

[SHOW: Claude Design homepage, bottom-left "Set up design system" button]

Before I build the landing page, I'm going to set up a design system. This is the most slept-on feature in Claude Design.

You can point it at a GitHub repo, drag in a local codebase, or — and this is what most people skip — just upload screenshots of designs you actually like. That's what I'm doing today.

[SHOW: Google Images results for "premium SaaS landing page dark mode"]

I spent five minutes on Google Images and saved four screenshots. A dark-mode SaaS hero I liked. A pricing section with a specific card style. A typographic layout that caught my eye. A testimonials layout that felt premium. Four images total.

[SHOW: Claude Design design system setup — drag in 4 screenshots, fill in company name + blurb]

Company name: Tyler AI. Blurb: "AI workflows for content creators." I drag in the four screenshots. I hit continue to generation.

[SHOW: Loading screen — 5-15 minute estimate]

It takes about 5 to 15 minutes depending on how much it has to process. You can leave the tab open.

[NOTE: Cut here. Time-lapse or jump-cut to when generation is done.]

[SHOW: Design system review page — colors, typography, spacing, buttons]

Here's what it came back with. It pulled the dark mode palette from my references. It picked up the typographic rhythm — bold display font for headlines, clean sans for body. Button styles, card patterns, spacing tokens — all derived from the four screenshots I fed it.

I click through and approve each category. Colors, approved. Typography, approved. Buttons, approved.

Now every design I make in Claude Design inherits this visual language. No codebase required. Just screenshots of what you want.

[NOTE: ~2:20 runtime. Screenshot-first approach is more universal than the repo-import flow Chase and Nate both showed — most viewers don't have a production repo handy.]

---

## [4:30 - 8:15] Section 3 — Prototyping the landing page

[SHOW: Claude Design dashboard, click "New prototype"]

Now the actual build. I'm making a landing page for a hypothetical product launch. High fidelity from the start.

I type: "Landing page for a 3-day live workshop called Your First AI Agent. May 4 through 6, nine to eleven AM central. Ten seat cap. Early bird pricing ends April 29. Include countdown, three-day agenda, instructor bio, testimonials, and a sticky CTA bar."

[SHOW: Claude starts asking clarifying questions]

Watch what happens. Before it generates anything, it asks me questions. What's the workshop about? Who's hosting? What should students walk away with? This is like plan mode in Claude Code.

[SHOW: Answer questions one by one]

I answer each. Workshop is on building AI agents with Claude Code. I'm hosting. Students walk away with their first agent shipped. Three-day agenda, high level per day. Hit continue.

[SHOW: Generation in progress panel with task checklist]

Generation takes about a minute. While it runs, notice the task checklist on the left. Claude is building components, applying the design system, wiring up the countdown. Transparency like this is rare in design tools.

[SHOW: Generated landing page — cover, countdown, agenda, testimonials, CTA]

Here's the output. Countdown is live and ticking. Three-day agenda laid out. Testimonials have real-looking copy. Sticky CTA bar pinned to the bottom. And the whole thing feels like it belongs to my brand because the design system is baked in.

But first drafts are never final. Let's iterate.

[NOTE: ~3:45 runtime. Move into iteration.]

---

## [8:15 - 11:00] Section 4 — Iterating with tweaks, comments, and drawings

[SHOW: Tweaks panel on right side]

Claude Design gives you four ways to iterate. The first is the tweaks panel. It pulls out the variables that make sense — in this case, early bird date, accent color, countdown on or off, sticky CTA on or off.

I change the early bird to April 27. The date updates everywhere on the page.

I change the accent from blue to orange. Every button, every highlight, every link updates. This is the design system doing its job.

[SHOW: Click "Edit" mode, select an element]

Second method — direct edit. I can click any element on the canvas. Select the instructor bio section. Change the headline text inline. Adjust the padding by dragging the slider.

[SHOW: Click "Comment" mode, drop a comment]

Third — comments. I click the testimonials section and drop a comment: "Make these feel more founder-y, less corporate." Claude queues it. I can drop five or ten comments, then batch-send them all.

[SHOW: Click "Draw" mode, sketch on the canvas]

Fourth — draw. You can literally sketch on the design. I'm circling the CTA button and drawing an arrow with the word "bigger" next to it. Send.

[SHOW: Claude responds with updated design]

All four of those are ways to iterate without leaving the canvas. You never have to type "change X to Y" as a full prompt again. You just point at the thing.

[NOTE: ~2:45 runtime. This is the "actually use it" section that Chase and Nate both rushed. Spend time here.]

---

## [11:00 - 13:20] Section 5 — The Claude Code handoff

[SHOW: Export button in top-right]

Now the part nobody else shows properly. I'm going to hand this off to Claude Code and actually run it.

I click export. Options are: download zip, PDF, PowerPoint, send to Canva, export HTML, or hand off to Claude Code.

[SHOW: Click "Hand off to Claude Code"]

I click "Hand off to Claude Code." Claude packages the design file, the chat history, a readme, and a pre-written prompt template into a bundle. It gives me a single command to paste into Claude Code.

[SHOW: Command copied]

The command looks like this: "Fetch this design file, read its readme, and implement the relevant aspects of the design into the current project."

That's it. One line.

[SHOW: Open VS Code, Claude Code terminal in a fresh Next.js + Tailwind starter project]

I open VS Code in a fresh Next.js starter project. Clean slate. I paste the command.

[SHOW: Claude Code executes — fetching endpoint, extracting zip, reading readme]

Claude Code fetches the endpoint. Extracts the zip. Reads the readme which tells it the component structure, the design tokens, and any context from our chat history.

Now watch this. Because the design system I built from the Google Images screenshots got baked into the export bundle, Claude Code has the color palette, typography, and component patterns in context. It writes the landing page with consistent design language — same buttons, same cards, same spacing tokens — matching what I approved in the design system review.

[NOTE: ~2:20 runtime. The handoff is the big differentiator. Let it breathe.]

---

## [13:20 - 15:40] Section 6 — Running the code locally

[SHOW: Claude Code finishes, suggests `npm run dev`]

Claude Code writes the page. It drops the new route under /workshop. It's using the existing Tailwind config, the existing Button component, my existing layout wrapper.

I run npm run dev.

[SHOW: Dev server starts, localhost opens]

Localhost comes up. Here's the homepage — that's my existing site. I navigate to /workshop.

[SHOW: Workshop landing page on localhost — same as the Claude Design output]

There it is. Same countdown. Same three-day agenda. Same testimonials. Same sticky CTA. Running in React, using my actual components, not a one-off HTML dump.

I scroll through. Everything works. The countdown ticks. The CTA is sticky. The design system is consistent.

[SHOW: Any issues? Show briefly if they exist, fix live]

One thing I want to call out. On my first run, Claude Code used the wrong image for the instructor photo. It picked one from elsewhere in the repo. Quick fix — I dropped the actual headshot into /public and updated the prop. Thirty seconds.

This is the kind of last-mile thing you'll still do yourself, even with Claude Design plus Claude Code.

[NOTE: ~2:20 runtime. Honesty beat — show the small friction. Builds credibility.]

---

## [15:40 - 17:30] Section 7 — Deploy live with the Vercel MCP

[SHOW: Claude Code terminal]

Now the deploy. And this is where most creators still switch tabs, open Vercel dashboard, wait for builds, grab URLs. I'm going to do all of it from inside Claude Code using the Vercel MCP.

[SHOW: Typed command in terminal]

```
claude mcp add --transport http vercel https://mcp.vercel.com
```

One line to install. It handles the OAuth flow — I approve in a browser popup, come back to VS Code, done.

[SHOW: Browser OAuth flow, return to VS Code]

Now the MCP is live. Claude Code can read and write to my Vercel account directly.

[SHOW: Typed prompt in Claude Code]

```
Deploy this project to Vercel. Use the production environment.
When it's done, give me the live URL.
```

[SHOW: Claude Code invoking Vercel MCP — creating deployment, streaming build logs]

Claude Code uses the Vercel MCP to commit, push, trigger a production deploy, and stream the build logs. No tab-switching. No CLI. No dashboard.

[SHOW: Live URL returned in Claude Code]

Two minutes later, the live URL comes back in the chat.

[SHOW: Live landing page on actual domain, scroll through]

That is a landing page that went from an English-language prompt in Claude Design to a live production URL via Vercel MCP in under 25 minutes. The whole workflow lived in two surfaces — Claude Design and Claude Code.

[NOTE: ~1:50 runtime. This is THE proof. The MCP flow is a noticeably tighter beat than manual git+dashboard. Lean into it.]

---

## [17:30 - 19:45] Section 8 — What this actually costs

[SHOW: Claude Design usage page showing weekly allowance]

OK, the part nobody else is telling you.

Claude Design has its own usage meter, separate from your regular Claude chat and separate from Claude Code. It resets weekly.

[SHOW: PCWorld headline screenshot — "I tried Claude Design for half an hour. I'm already locked out for a week."]

PCWorld tested it and hit the cap in 30 minutes. I've seen similar reports on Reddit and X. The Pro plan's weekly allowance is aggressive.

[SHOW: My actual usage after this build — breakdown screen]

Here's what today's build cost me. Design system setup: one session, hit about 35 percent of weekly. Landing page prototype with iterations: another 40 percent. So one complete workflow burned three quarters of my weekly Pro allowance.

If you plan to ship one major design per week, Pro works. If you iterate heavily or build multiple designs, you'll hit the cap fast. Max plan is five times Pro allowance, but it's 100 dollars a month.

[SHOW: Quick comparison table on screen]

Here's the honest math.
- Pro at 20 a month: great for 1-2 designs per week
- Max at 100 a month: realistic for a full-time design workflow
- Alternatives: v0 Pro is 20, Lovable is 30, Bolt is 25 — all cheaper per generation for simple components but none have native Claude Code handoff

Nobody else is showing you this because the token cap is awkward for hype videos. It's not a dealbreaker. But know what you're buying.

[NOTE: ~2:15 runtime. Honesty section — huge for trust.]

---

## [19:45 - 22:00] Section 9 — When to use Claude Design vs alternatives

[SHOW: Decision matrix graphic]

Fast decision framework.

[SHOW: One line per tool on screen]

Use **Claude Design** when you need the full design-to-production loop with your real brand system, and the person handing it off is also the person deploying it.

Use **v0** when you need individual React components fast, especially if you're already on Vercel.

Use **Bolt** when you need a full-stack MVP prototype that you'll throw away or rebuild.

Use **Lovable** when you need a complete app with auth, database, and deploy baked in, and you're not already in someone else's codebase.

Use **Claude Code alone** when you know exactly what you want and don't need the visual iteration step.

The unique slot Claude Design owns is the design-to-code bridge inside your existing repo. If you're building new features into a real product, Claude Design plus Claude Code is the closest thing to a solo-founder design-engineer workflow I've seen.

[NOTE: ~2:15 runtime. This is the decision-making gift to the viewer.]

---

## [22:00 - end] Outro

[SHOW: Talking head]

Quick recap. Claude Design turns prompts into production-ready designs. Claude Code takes the handoff and ships them into a real repo. The full loop, prompt to live URL, ran in 23 minutes today.

There's a cost to watch. There are better tools for some specific jobs. But the end-to-end flow is genuinely new, and for builders already in the Claude Code ecosystem, this is the visual layer that was missing.

[SHOW: Skool community preview]

I'm putting the exact prompts, the design system setup, and the Claude Code handoff template in my Skool community. Link in the description. It's free.

[SHOW: Tyler on camera]

If this helped, hit subscribe. If you have a specific question about the workflow, drop a comment — I read every one.

See you in the next video.

[NOTE: Keep outro tight — 60-90 seconds. Target total runtime 22-23 minutes.]

---

## Running total (target 20-24 min)

| Section | Target | Running |
|---|---|---|
| Hook | 0:30 | 0:30 |
| What Claude Design is | 1:40 | 2:10 |
| Design system setup | 2:20 | 4:30 |
| Prototyping | 3:45 | 8:15 |
| Iterating | 2:45 | 11:00 |
| CC handoff | 2:20 | 13:20 |
| Run locally | 2:20 | 15:40 |
| Push + deploy | 1:50 | 17:30 |
| Cost honesty | 2:15 | 19:45 |
| When to use what | 2:15 | 22:00 |
| Outro | 1:00 | 23:00 |

**Target total: 23 minutes** (matches "shipped in 23 minutes" framing in hook + title)
