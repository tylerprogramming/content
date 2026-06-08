# Filming Guide — Claude Design Video

Practical, step-by-step playbook for what to actually do on screen. Follow this and you can film without re-reading the script.

---

## Pre-recording setup

### Accounts and access
- [ ] Claude Pro / Max subscription active (required — Claude Design not on free)
- [ ] Claude Design access confirmed at https://claude.ai/design
- [ ] Claude Code installed and logged in
- [ ] **Vercel account** (free Hobby plan works — sign up at vercel.com with GitHub if you haven't)
- [ ] **Vercel MCP installed in Claude Code:** run `claude mcp add --transport http vercel https://mcp.vercel.com` and complete OAuth (film this step on camera at Section 7)
- [ ] Fresh Next.js + Tailwind starter repo on GitHub, wired to Vercel (push to `main` = deploy)
- [ ] Custom domain optional but nicer for the live URL reveal

### Before you hit record
- [ ] Close every browser tab except: claude.ai/design, VS Code, terminal, Vercel dashboard, a blank browser for the live URL
- [ ] Hide bookmarks bar
- [ ] Zoom browser to 125% for readability
- [ ] VS Code: set font size to 16, close extra panels, one terminal pane open
- [ ] macOS: hide dock, hide menu bar, set Do Not Disturb
- [ ] Camtasia preset: 1080p, screen + camera tracks
- [ ] Microphone check (30 sec voice test)
- [ ] Headshot image (tylerai.png) ready in ~/Downloads for the instructor photo moment

### Repo prep
Use a fresh Next.js + Tailwind starter (no pre-existing components). This matches the "screenshots as design inspiration" workflow — viewers don't need an existing codebase to replicate.

```bash
npx create-next-app@latest tyler-ai-workshop --typescript --tailwind --app
cd tyler-ai-workshop
git init && git add . && git commit -m "Initial starter"
gh repo create tyler-ai-workshop --public --source . --push
```

Then in Vercel, import this repo. Production branch = `main`. Done.

### Design reference screenshots (do this BEFORE filming)
- [ ] Spend 5-10 minutes on Google Images / Dribbble / Godly.website and save 4 screenshots of landing pages you'd want Tyler AI's design system to mirror. Premium dark-mode SaaS vibe.
- [ ] Save them to `~/content/youtube/claude-design/b-roll/design-refs/` so you have them accessible during filming.

---

## Step 1 — Film the hook (last, not first)

**Tip:** Record the hook AFTER the rest, so you know the actual final timing ("shipped in 23 minutes"). Drop the real number into the hook on the second take.

When you film it:
- B-roll you'll need: claude.ai/design canvas, Claude Code terminal running, final live URL in browser bar. Shoot each as a 5-second clean shot so you can cut them fast.
- On-camera: one take, confident, no hype voice.
- Target: 22-25 seconds.

---

## Step 2 — "What Claude Design actually is" (1:40)

[SHOW on screen]
1. Navigate to https://claude.ai/design — leave on the homepage
2. Keep Nate's + Chase's thumbnails pulled up in a hidden tab. When you say "the videos you've seen mostly stop at the prototype," quick-cut to them.

[SAY — narration while showing]

> Claude Design is Anthropic's new visual design tool. Launched April 17th. Powered by Opus 4.7.

[CLICK into the "Prototype" section briefly to show the canvas]

> You describe what you want. Claude generates a prototype you can edit in the canvas. And when you're ready, you hand it to Claude Code with one command.

---

## Step 3 — Set up the brand design system from screenshots (2:20)

[SHOW]
1. Pre-cut: quick montage of Google Images searches with "premium dark saas landing page", "editorial pricing section", etc. — saving 4 screenshots to the desktop
2. Scroll down on Claude Design homepage, click **Set up design system** (bottom-left)
3. Company name: **"Tyler AI"**
4. Blurb: **"AI workflows for content creators"**
5. Drag the 4 screenshots from Finder directly into the upload zone
6. Click **Continue to generation**
7. You'll see the "takes about 5-15 minutes" modal — click continue

[TIME-LAPSE or cut]
Skip the 15-minute wait. Cut straight to the result screen.

[SHOW on the result screen]
- Colors section — click through, approve the dark-mode palette it pulled from your reference screenshots
- Typography — approve the headline + body pairing it derived from the screenshots
- Buttons, cards, spacing — approve each
- Click **Save design system**

[SAY — over the approval clicks]

> Claude pulled this entire system from 4 screenshots I saved off Google Images. It derived the color palette. It picked up the typographic rhythm. It matched the card and button styles. Now every design I make in Claude Design will inherit this visual language.

### Exact typing:
```
Company: Tyler AI
Blurb: AI workflows for content creators
```

**Fill dead air while approvals save:** Most viewers don't have a production codebase ready to feed Claude Design. But everyone can save 4 screenshots. That's why this workflow matters — it removes the barrier to entry Chase and Nate both required.

---

## Step 4 — Build the landing page prototype (3:45)

[SHOW]
1. Back to Claude Design dashboard
2. Click **New Prototype**
3. Name it: **"First AI Agent Workshop"**
4. Choose **High fidelity** (not wireframe)

[PASTE this exact prompt]:
```
Landing page for a 3-day live workshop called "Your First AI Agent."
Dates: May 4 through May 6, 9 to 11 AM Central.
10 seat cap. Early bird pricing ends April 29.
Include: countdown timer, three-day agenda, instructor bio section, testimonials, sticky CTA bar.
Use my design system.
```

5. Hit send
6. Claude will ask clarifying questions. Answer:
   - **Workshop about:** "Building AI agents with Claude Code"
   - **Who's hosting:** "Tyler Reed"
   - **Students walk away with:** "Their first working AI agent"
   - **Agenda detail level:** "High level per day"
   - **Early bird discount:** "20% off"
   - **Instructor photo:** skip for now, I'll add later

7. Click **Continue to generation**

[SHOW]
- Left panel: task checklist appearing as Claude builds
- Right panel: design rendering live

[SAY — while it builds]

> Notice it asked me questions before generating anything. This is like plan mode in Claude Code. It surfaces the blind spots before committing.

Wait for completion. Scroll through the result on-screen.

**If generation takes >2 minutes, cut.** Viewers don't need to watch it churn.

---

## Step 5 — Iterate (2:45)

Four iteration methods. Demo all four.

### 5a. Tweaks panel
- Open **Tweaks** panel on the right
- Change **Early bird end date** from April 29 → April 27 (show it update on the page)
- Change **Accent color** from blue → orange (show every button flip)

### 5b. Direct edit
- Click **Edit** mode toggle
- Click the instructor bio section
- Change headline text inline
- Adjust padding slider

### 5c. Comments
- Click **Comment** mode
- Click testimonials section
- Type: **"Make these feel more founder-y, less corporate"**
- Don't send yet — drop a second comment on the CTA: **"Tighten the copy, too many words"**
- Click **Send to Claude** (sends both at once)

### 5d. Draw
- Click **Draw** mode
- Circle the CTA button with a freehand loop
- Write/draw "bigger" next to it with an arrow
- Send

Wait for Claude to apply the changes. Scroll through the updated page.

[SAY]

> Four ways to iterate without leaving the canvas. You never have to retype a full prompt. You just point at the thing.

---

## Step 6 — The Claude Code handoff (2:20)

[SHOW]
1. Click **Export** (top-right)
2. Show the options menu briefly (zip, PDF, PPTX, Canva, HTML, Claude Code)
3. Click **Hand off to Claude Code**

[SHOW — the generated command modal]

The command will look like:
```
Fetch this design file: https://claude.ai/.../design-bundle.zip
Read its readme and implement the relevant aspects of the design into the current project.
```

4. Click **Copy command**

[SHOW]
5. Switch to **VS Code**, open the repo you used for the brand setup
6. Open **Claude Code** in terminal inside VS Code
7. Paste the command
8. Hit enter

[ON-SCREEN — Claude Code executing]
- Fetching endpoint
- Downloading the zip
- Extracting files
- Reading the readme
- Writing new route files

[SAY — while it runs]

> Claude Code already knows my component patterns because the brand system was built from this same repo. It doesn't reinvent a button. It uses the Button component I already have.

**Fill dead air:** Compare to v0 — with v0 you get raw component code you have to wire into your design system manually. This bundle preserves context.

---

## Step 7 — Run the code locally (2:20)

[SHOW in terminal]
```bash
npm run dev
```

Wait for dev server to start. Browser should auto-open or:

[SHOW in browser]
```
http://localhost:3000/workshop
```

Scroll through the page:
- Countdown ticking
- Three-day agenda
- Testimonials
- Sticky CTA pinned

**Show one small friction moment (authenticity):**
- Instructor photo is the wrong one — Claude Code grabbed a placeholder
- Fix: drop tylerai.png into `/public/instructor.jpg`, update the image path in the workshop page component (show the line change live in VS Code)
- Reload localhost, show the correct photo

[SAY]

> One thing to call out. Claude Code used the wrong image on first pass. Quick fix — dropped the right file in, updated the path, 30 seconds. This kind of last-mile thing, you'll still do yourself.

---

## Step 8 — Deploy live with Vercel MCP (1:50)

[SHOW on camera — install the Vercel MCP fresh, even if it's already configured, so viewers see the setup]

```bash
claude mcp add --transport http vercel https://mcp.vercel.com
```

OAuth popup opens in browser → approve → return to VS Code. ~20 seconds total. Don't cut this — the ease of setup is a selling point.

[SHOW in Claude Code — one prompt]

```
Deploy this project to Vercel production.
When the build completes, give me the live URL.
```

[SHOW Claude Code invoking Vercel MCP tools — creating deployment, streaming build output]
- The MCP commits + pushes on your behalf, kicks the deploy, streams logs
- Build completes in 60-90 seconds
- Live URL returned in the chat

**Cut the wait** if it takes more than 90 seconds. Jump to the completed deploy.

[SHOW in browser]
- Open the live URL Claude Code returned
- Scroll through the live page
- Countdown, agenda, testimonials, CTA — all live on production

[SAY]

> That's a landing page that went from an English-language prompt in Claude Design to a live production URL via Vercel MCP in under 25 minutes. I never left Claude Code. No git commands, no dashboard. The whole workflow lived in two surfaces.

---

## Step 9 — Cost breakdown (2:15)

[SHOW]
1. Go back to Claude Design
2. Click your profile / settings / usage
3. Show the **weekly allowance** indicator

[SHOW screenshot overlay — PCWorld headline]
- "I tried Claude Design for half an hour. I'm already locked out for a week."

[SHOW — your own usage after today's build]
- Do the math on camera. Something like: "Design system: 35%. Prototype and iterations: 40%. Total: 75% of weekly allowance."

[SHOW simple table on screen — prepare this as a graphic]

| Plan | Price | Best for |
|---|---|---|
| Pro | $20/mo | 1-2 designs per week |
| Max | $100/mo | Full-time design workflow |
| v0 Pro | $20/mo | Cheaper per-component |
| Lovable | $30/mo | Full apps |
| Bolt | $25/mo | Full-stack prototypes |

[SAY]

> Not a dealbreaker. But know what you're buying. Nobody else is showing you this because the token cap is awkward for hype videos.

---

## Step 10 — Decision framework (2:15)

[SHOW decision graphic on screen — bullet list animated in]

Just narrate over the bullets. Don't read word-for-word.

- **Claude Design** — full design-to-production loop in your real brand system
- **v0** — individual React components, Vercel-native
- **Bolt** — throwaway MVP prototypes
- **Lovable** — full apps with auth/DB/deploy included
- **Claude Code alone** — when you know what you want, no visual step needed

[SAY — end with the thesis]

> The unique slot Claude Design owns is the design-to-code bridge inside your existing repo. For builders already in the Claude Code ecosystem, this is the visual layer that was missing.

---

## Step 11 — Outro (60-90 sec)

[SHOW]
- Talking head
- Quick B-roll cut of the deployed site

[SAY — word-for-word works here]

> Recap. Claude Design turns prompts into production-ready designs. Claude Code takes the handoff and ships them into a real repo. Full loop, prompt to live URL, 23 minutes today.
>
> There's a cost to watch. There are better tools for some jobs. But the end-to-end flow is genuinely new. For builders already in Claude Code, this is the visual layer that was missing.
>
> Exact prompts, design system setup, and the Claude Code handoff template are in my Skool community. Link below. Free.
>
> If this helped, hit subscribe. Questions about the workflow, drop a comment.

Skool link and channel subscribe animation.

---

## On-camera tips

- **Energy:** Confident, not hyped. The result sells itself. No "INSANE" voice.
- **Pacing:** Short sentences. Breathe between them. Cut any sentence longer than 2 lines.
- **When Claude is thinking:** Fill dead air with the "why this matters" layer — don't just stare at the loading screen. Pre-plan one filler talking point per generation moment.
- **Errors on camera:** Keep them if they're fixable in 30 seconds. The one image-fix moment in Step 7 is the kind of small friction that builds credibility.
- **Visual moments to capture well:** the first prototype generation completing (cut close to the reveal), the Claude Code terminal executing (zoom the terminal pane), the live URL loading (go full-screen when you show it).

---

## Timing cheat sheet

| Section | Target | Running |
|---|---|---|
| Hook | 0:30 | 0:30 |
| What it is | 1:40 | 2:10 |
| Design system | 2:20 | 4:30 |
| Prototype | 3:45 | 8:15 |
| Iterate | 2:45 | 11:00 |
| Handoff | 2:20 | 13:20 |
| Run locally | 2:20 | 15:40 |
| Deploy | 1:50 | 17:30 |
| Cost | 2:15 | 19:45 |
| Decision framework | 2:15 | 22:00 |
| Outro | 1:00 | 23:00 |

**Total target: 23 minutes.** Rolls up to the hook's "shipped in 23 minutes" promise.

---

## Files to have ready before filming

1. **Repo** — any existing Next.js or Vite + Tailwind project of yours, on a branch
2. **Domain** — Vercel deploy wired to that branch or main
3. **Instructor headshot** — `~/assets/identity/tylerai.png` or similar
4. **Decision framework graphic** — design this ahead in Figma or Keynote, 5-bullet clean slide
5. **Cost comparison table** — same, pre-built as a graphic
6. **PCWorld headline screenshot** — grab it, save to `~/content/youtube/claude-design/b-roll/pcworld-headline.png`
