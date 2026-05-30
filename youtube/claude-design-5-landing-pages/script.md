# Script — I Shipped 5 Landing Pages in One Afternoon with Claude Design

**Working title:** I Shipped 5 Landing Pages in One Afternoon with Claude Design
**Target runtime:** 18-22 minutes
**Angle:** Volume + speed proof. 5 different industries. Time-lapse editing essential.

---

## [0:00 - 0:30] Hook — Proof Montage

[SHOW: 5-panel grid of finished landing pages, each getting a checkmark as named]

In the last 4 hours I shipped 5 completely different landing pages to 5 different live URLs. A SaaS. An agency. A restaurant. A creator site. A local business.

[SHOW: 5 live URLs flashing on screen, each scrolling briefly]

No designer. No developer. No hand-off meetings. Just Claude Design, Claude Code, and about 8 bucks in API credits.

[SHOW: Tyler on camera]

I'll show you the full process, the 5 prompt templates I used, and the one workflow trick that made this even possible in an afternoon.

Let's go.

---

## [0:30 - 2:00] Section 1 — The workflow that made this possible

[SHOW: Flowchart — template prompt → Claude Design → handoff → Claude Code → Vercel]

Before I show you the builds, here's the workflow that made 5 in an afternoon possible.

Template prompts. I made one master prompt template for landing pages. Fill in five variables: industry, product name, tone, target audience, primary CTA. Same 200-word prompt each time.

[SHOW: The master prompt template on screen]

Second. Vercel MCP installed in Claude Code. One command: `claude mcp add --transport http vercel https://mcp.vercel.com`. Now every deploy is a single prompt. No dashboard. No git commands. Five deploys go fast.

Third. One Vercel project with routes for each page — `/argus`, `/northbound`, `/luna`, etc. Deploy all 5 to the same domain. No new repo per project.

Fourth. Skip the design system setup for each. Use one shared system across all 5 — saves 60 plus percent of your weekly Claude Design usage. Build the shared system from a handful of reference screenshots you save off Google Images.

[NOTE: ~1:30 runtime. The systems thinking upfront is the retention hook.]

---

## [2:00 - 5:00] Section 2 — Build 1: SaaS landing page

[SHOW: Timer overlay — 4:00:00]

Build one. SaaS landing page for a fake product called Argus — social media intelligence platform.

[SHOW: Master prompt filled in for Argus]

I run the master prompt with SaaS variables filled in. Argus. Professional-technical tone. Creators as target audience. CTA is start free trial.

[SHOW: Claude Design generating, time-lapse to finished page]

8 minutes in Claude Design. Three quick tweaks — accent color, pricing tier layout, hero illustration swap.

[SHOW: Export, hand-off command, Claude Code runs, localhost preview]

Hand off to Claude Code. Extract to `/argus` route. Push. Deploy.

[SHOW: Live URL]

Live at yoursite.com/argus. 12 minutes elapsed.

[NOTE: ~3:00 runtime. First build establishes the rhythm.]

---

## [5:00 - 7:30] Section 3 — Build 2: Agency site

[SHOW: Timer at 3:48:00 remaining]

Build 2. Agency site — "Northbound Digital," fictional AI automation agency.

[SHOW: Master prompt filled in for agency]

Master prompt. Industry: agency. Tone: premium-authoritative. Target: mid-market SaaS founders. CTA: book a discovery call.

[SHOW: Generation time-lapse]

Claude Design brings back a dark-mode agency layout with case studies, services, testimonials, team.

[SHOW: Tweaks panel — darken palette, widen hero]

Two tweaks. Done.

[SHOW: Handoff, deploy, live URL]

Live at yoursite.com/northbound. 11 minutes for this one.

[NOTE: ~2:30 runtime. Faster cadence on build 2 shows learning curve.]

---

## [7:30 - 10:00] Section 4 — Build 3: Restaurant site

[SHOW: Timer at 3:20:00 remaining]

Build 3. Restaurant — Luna, fictional Italian small-plates spot.

[SHOW: Master prompt for restaurant]

Industry: restaurant. Tone: warm-editorial. Target: date-night diners. CTA: reserve a table.

[SHOW: Generation — the output is visually distinct, warm palette, food photography placeholders]

Claude Design handles restaurant well. Warm palette, food photography grid, menu preview, reservation block, hours and map footer.

[SHOW: Nano Banana generating 4 food photos]

The images are placeholders by default. I drop 4 food photos I generated with Nano Banana into the public folder. Update the image references.

[SHOW: Handoff, deploy, live URL]

Live at yoursite.com/luna. 14 minutes — food photo generation added 3 minutes.

[NOTE: ~2:30 runtime. Shows the multi-tool workflow (Claude Design + Nano Banana) naturally.]

---

## [10:00 - 12:30] Section 5 — Build 4: Creator site

[SHOW: Timer at 2:45:00 remaining]

Build 4. Creator personal site — for a fictional YouTube educator named Sam Grant.

[SHOW: Master prompt for creator]

Industry: personal brand. Tone: approachable-expert. Target: ambitious self-learners. CTA: join newsletter + view latest video.

[SHOW: Generation — creator layout with featured content, about section, newsletter CTA]

Claude Design gives a creator layout. Featured video block, about section, newsletter capture, social links, latest videos grid.

[SHOW: Tweaks — personal headshot placeholder replaced with Nano Banana portrait]

I swap the headshot placeholder with a Nano Banana-generated portrait.

[SHOW: Handoff, deploy, live URL]

Live at yoursite.com/sam-grant. 10 minutes.

[NOTE: ~2:30 runtime.]

---

## [12:30 - 15:00] Section 6 — Build 5: Local business

[SHOW: Timer at 2:10:00 remaining]

Build 5. Local business — Harbor Dental, fictional dentist in a small coastal town.

[SHOW: Master prompt for local business]

Industry: local services. Tone: friendly-trustworthy. Target: local residents in their 30s and 40s. CTA: book appointment + phone number.

[SHOW: Generation — local business layout with clean palette, services, team, location map]

Local business layout. Services grid. Meet the team. Map and location. Phone number prominent. Easy to scan.

[SHOW: Deploy, live URL]

Live at yoursite.com/harbor-dental. 9 minutes — the template workflow has fully kicked in by now.

[NOTE: ~2:30 runtime.]

---

## [15:00 - 17:00] Section 7 — The 5 side-by-side + what you learn

[SHOW: 5-tab browser, cycle through all 5 live URLs]

All 5 live URLs. All 5 totally different industries and design languages.

[SHOW: Key observations list on screen]

Three lessons from this speed run.

One. Template prompts compound. Build one good master prompt, swap variables, you're 70 percent of the way there every time.

Two. Skip per-project design systems. Unless the brand is load-bearing, one shared system across your test projects saves 60 percent of usage.

Three. Nano Banana plus Claude Design is the real combo. Nano Banana for every photo placeholder. The restaurant and creator pages would look generic without it.

[NOTE: ~2:00 runtime. Synthesis is what separates volume videos from useful volume videos.]

---

## [17:00 - 19:00] Section 8 — Cost + time math

[SHOW: Breakdown graphic]

Total time. Just under 4 hours, including rest breaks and one re-generation.

Total cost. 65 percent of my weekly Claude Design Pro allowance. About 2 dollars in Nano Banana credits. About 4 dollars in Claude API for the Claude Code work. Call it 8 dollars total.

[SHOW: Agency comparison]

An agency would charge $2,000 to $3,000 per landing page. Five of them = $10,000 to $15,000. I did it for 8 bucks.

[NOTE: ~2:00 runtime. The economics payoff.]

---

## [19:00 - end] Outro

[SHOW: Tyler on camera]

Recap. Master prompt template. Shared design system. 5 industries in 4 hours. $8 total.

[SHOW: Skool community preview]

The master prompt template, the shared design system setup, and all 5 prompt variables are in my Skool community. Free. Link below.

[SHOW: Tyler on camera]

Drop in the comments what industries you want me to rebuild next. I'll do the top 5 in the next volume run.

Subscribe for more.

---

## Running total (target 18-22 min)

| Section | Target | Running |
|---|---|---|
| Hook | 0:30 | 0:30 |
| Workflow overview | 1:30 | 2:00 |
| Build 1: SaaS | 3:00 | 5:00 |
| Build 2: Agency | 2:30 | 7:30 |
| Build 3: Restaurant | 2:30 | 10:00 |
| Build 4: Creator | 2:30 | 12:30 |
| Build 5: Local business | 2:30 | 15:00 |
| 5 side-by-side + lessons | 2:00 | 17:00 |
| Cost + time | 2:00 | 19:00 |
| Outro | 1:00 | 20:00 |

**Target: 20 minutes**
