# Script: I Built My Email Stack in Claude Code (Drip Campaigns + $0/Month)

**Target length:** 28-32 minutes
**Format:** Pricing-page hook → Pain → Architecture → 3 demos (one-off, drip, blast) → 4-step build → Trade-offs → CTA
**Energy:** Practical, contrarian, money-conscious, proof-heavy
**Reference pattern:** Tyler's AntiGravity script — concrete prompts in code blocks, real demos with real numbers, `[SHOW:]` and `[NOTE:]` cues for the editor.

> **Filming note:** If you never actually paid for ConvertKit, swap the cold open to Hook B (the SQL receipt) and use the alt title "I Built My Email Stack in Claude Code (Drip Campaigns + $0/Month)". The pricing-tab moment still works — just frame it as "this is what others pay" rather than "this is what I cancelled."

---

## [0:00 - 0:25] Hook (Receipts in 8 Seconds)

[SHOW: Browser tab on convertkit.com/pricing. The $50/mo Creator tier is highlighted. Cursor hovers, then closes the tab. Cut to terminal running `python3 ~/.claude/skills/email/email_campaign.py` — output shows "6 emails sent: 3 step 1, 2 step 2, 1 step 3" with real timestamps.]

> *(VO at 0:03)*
> Most creators in my space pay 50 to 200 dollars a month to send emails. I pay zero.

> *(at 0:09)*
> Here's the entire system. One Claude Code skill, one Resend API key, one SQLite database. Drip campaigns, bulk blasts, welcome sequences. Free.

> *(at 0:16)*
> I'll walk you through the architecture, three live demos, and exactly how to build your own.

[NOTE: Energy HIGH. The pricing-page-to-terminal cut IS the proof. Don't talk over the terminal output — let it land for 1.5 seconds.]

---

## [0:25 - 2:30] The Pain Point

[CAMERA: Face to camera, slight pacing energy]

> Quick setup so you know what you're getting.

> I run a Skool community. I have a list of subscribers I email occasionally. I need to send three kinds of email.

> One — when somebody joins my community, they get a welcome sequence. Three emails, spaced over the first three days. That's a drip campaign.

> Two — when I publish a new video or have an announcement, I send a blast to my whole list. That's a bulk send.

> Three — sometimes I need to email one specific person. That's a one-off.

[SHOW: On-screen text overlay listing the 3 use cases as Tyler narrates each.]

> Most tools do all three fine. The problem is what they charge for it.

[SHOW: Quick montage — ConvertKit pricing ($50/mo at 1K contacts), Beehiiv pricing ($42/mo), ActiveCampaign ($93/mo). Side by side, prices circled.]

> $50 a month. $42. $93. All to send HTML through SMTP, which is a 40-year-old protocol.

> So I built it myself. In Claude Code. With Resend handling the actual email delivery. Total cost — Resend's free tier covers 100 emails a day. If you cross that, their paid tier is $20 a month for 50,000 sends. That's the entire cost.

> Here's how it's wired up.

---

## [2:30 - 6:30] The Architecture

[SHOW: Animated diagram or clean Excalidraw — three boxes labeled Resend / Claude Code / SQLite, with arrows showing data flow.]

> Three components.

### Component One: Resend (2:45 - 3:30)

> Resend is an API-first email service. You give them an API key, you give them an HTML payload and a recipient, they send the email and report back what happened.

[SHOW: Resend dashboard briefly — domains list with one verified, API keys panel. Blur the actual key.]

> Domain verified once. SPF, DKIM, all handled. Free tier 100/day, paid tier $20/mo for 50K sends. No SMTP headaches, no warm-up nightmare.

### Component Two: Claude Code Skill (3:30 - 4:45)

[SHOW: VS Code opening `~/.claude/skills/email/SKILL.md` — show the frontmatter and the routing logic in the body.]

> The skill lives at `~/.claude/skills/email/`. SKILL.md tells Claude what to do based on the request — send an email, blast a list, run a campaign, check status, list campaigns, sync contacts.

> Underneath the markdown there are three Python scripts:

[SHOW: File explorer in the skill folder]

```
~/.claude/skills/email/
├── SKILL.md
├── send_email.py          # one-offs and blasts
├── email_campaign.py      # drip automation runner
└── sync_contacts_resend.py  # push local contacts to Resend
```

> One file routes the request, three scripts do the work.

### Component Three: SQLite (4:45 - 6:30)

[SHOW: Open TablePlus pointed at `~/.claude/skills/skool/data/skool.db`. Show the schema sidebar listing tables.]

> The database lives at `~/.claude/skills/skool/data/skool.db`. I share it with my Skool skill on purpose. When new members sync into Skool, they're immediately available for email targeting.

> Three tables matter for email:

[SHOW: Click on each table in TablePlus, show the columns briefly]

```sql
-- email_campaigns: defines what a campaign is
CREATE TABLE email_campaigns (
  id INTEGER PRIMARY KEY,
  name TEXT,
  trigger_type TEXT,       -- 'auto' or 'manual'
  trigger_filter TEXT,     -- SQL WHERE clause for who gets it
  active INTEGER
);

-- email_campaign_steps: the individual emails in a campaign
CREATE TABLE email_campaign_steps (
  id INTEGER PRIMARY KEY,
  campaign_id INTEGER,
  step_number INTEGER,
  delay_hours INTEGER,
  subject_template TEXT,
  html_template TEXT
);

-- email_sends: every email I've ever sent
CREATE TABLE email_sends (
  id INTEGER PRIMARY KEY,
  campaign_id INTEGER,
  step_number INTEGER,
  member_id INTEGER,
  email TEXT,
  sent_at TIMESTAMP,
  resend_id TEXT,
  opened_at TIMESTAMP
);
```

> Campaigns, steps, sends. The third table is your audit log. Every email this system has ever sent is queryable. I can run one SQL query and tell you my open rate for any campaign over any time window.

[CAMERA: Face to camera]

> That's the stack. Three components. Resend for delivery, Claude Code for the interface, SQLite for state. Let me show you it actually working.

---

## [6:30 - 11:00] Demo 1 — One-Off Send

### The setup (6:30 - 7:00)

> Easiest case first. I want to email one person.

### The prompt + demo (7:00 - 9:30)

[SHOW: Terminal — type the request to Claude Code]

```
/email send john@example.com — let him know the new course module just dropped, casual tone
```

[SHOW: Claude Code interaction]

> Claude asks me what the subject should be. I type: "New module: Skill Templates"

[SHOW: Claude drafts the HTML in a preview window — clean simple template with a heading, paragraph, button, signature]

> It drafts the HTML. Shows it to me. I read it. If I like it, I approve.

[SHOW: Tyler types "looks good, send it"]

[SHOW: Skill runs the underlying command]

```bash
python3 ~/.claude/skills/email/send_email.py \
  --subject "New module: Skill Templates" \
  --html-file /tmp/email.html \
  --to john@example.com
```

[SHOW: Confirmation in terminal: "Email sent. Resend ID: re_8d4kp2qx_..."]

### Why this matters (9:30 - 11:00)

> Two things to notice.

> First — I never wrote the HTML. Claude drafted it from my one-line description.

> Second — I confirmed before sending. The skill is hard-coded to require my approval. There's no path where I accidentally blast something I didn't review.

[SHOW: Open SKILL.md, highlight the "Rules" section at the bottom: "Always show email content and get confirmation before sending. Never auto-send without user approval."]

> Same flow works for replying to a customer, sending a quick follow-up, anything one-shot. Drop the request, approve, sent.

> But the easy case isn't the reason I'd build this. The reason is the next demo.

---

## [11:00 - 19:30] Demo 2 — Drip Campaigns (The Real Reason)

### The setup (11:00 - 12:00)

[SHOW: Tyler at desk, face to camera]

> Real talk. The reason I'd build my own email tool isn't blasts. It's drip campaigns.

> Here's what I needed.

> Every time a new member joins my Skool community, they get three emails.
> One hour after they're approved — welcome message.
> 24 hours later — getting started guide.
> 72 hours after that — invitation to a self-hosted version of one of my tools.

> Most email tools charge you for this kind of automation. Mine runs locally.

### The campaign definition (12:00 - 14:30)

[SHOW: TablePlus — open `email_campaigns` table. Show the existing `new_member_welcome` row.]

> Here's my `new_member_welcome` campaign. Trigger type "auto." Trigger filter is a SQL WHERE clause targeting new members in the last 5 days.

```sql
-- the actual trigger filter in the campaign definition
WHERE approved_at > datetime('now', '-5 days')
  AND status = 'active'
```

[SHOW: TablePlus — open `email_campaign_steps` table. Show the 3 rows for the welcome campaign.]

> Inside the campaign, three steps:

| step | delay_hours | subject | template |
|---|---|---|---|
| 1 | 1 | Welcome to the community, {first_name} | templates/welcome.html |
| 2 | 24 | Getting started with skills | templates/getting_started.html |
| 3 | 72 | Want to self-host? | templates/self_hosting.html |

> Each step has a number, a delay in hours, a subject template with a `{first_name}` placeholder, and an HTML template file.

[SHOW: Open `~/.claude/skills/email/templates/welcome.html` in VS Code. Scroll through it briefly — show it's a clean, simple HTML email with inline styles.]

> The templates are simple. Hundred lines of HTML, inline styles for email client compatibility. I had Claude write the first one, then I copy-pasted the structure for the other two and edited the content.

### The runner (14:30 - 17:30)

[SHOW: Terminal — type the dry-run command]

```
/email campaign status
```

[SHOW: Claude routes this and runs the underlying command]

```bash
python3 ~/.claude/skills/email/email_campaign.py --dry-run
```

[SHOW: Output]

```
Campaign: new_member_welcome
  Step 1 (Welcome) — 3 contacts due
    - alice.tester@example.com (joined 2h ago)
    - bob.demo@example.com (joined 1.5h ago)
    - carol.preview@example.com (joined 1h ago)
  Step 2 (Getting Started) — 2 contacts due
    - dan.test@example.com (last email 26h ago)
    - eva.preview@example.com (last email 24h ago)
  Step 3 (Self-Hosting) — 1 contact due
    - frank.demo@example.com (last email 73h ago)
TOTAL: 6 emails would be sent
```

> Dry run first. 6 emails about to go out. Three new members getting step 1, two getting step 2, one getting step 3.

[SHOW: Run for real]

```
/email campaign
```

[SHOW: Terminal — same output but with "sent" confirmations and Resend IDs after each]

> Send for real. 6 emails out in about 4 seconds. Each one logged to the `email_sends` table with the Resend ID for later open tracking.

### Open tracking (17:30 - 19:30)

[SHOW: Terminal]

```
python3 ~/.claude/skills/email/sync_opens.py
```

> There's a separate script that pings Resend's API once a day, pulls open events for any send in the last week, writes the `opened_at` timestamp back to the sends table.

[SHOW: TablePlus — run a SQL query]

```sql
SELECT
  campaign_id,
  step_number,
  COUNT(*) AS sent,
  COUNT(opened_at) AS opened,
  ROUND(100.0 * COUNT(opened_at) / COUNT(*), 1) AS open_rate
FROM email_sends
WHERE sent_at > datetime('now', '-30 days')
GROUP BY campaign_id, step_number;
```

[SHOW: Query result with real open rates per step]

> One query. Full attribution. Open rate by campaign, by step, over any time window.

> ConvertKit charges $50 a month for a worse version of this with a fancier UI and no SQL access.

[NOTE: The SQL query result IS the verification. Make sure the data shown is real (or convincingly seeded) — if open_rate shows 0% for everything, the demo falls flat.]

---

## [19:30 - 23:30] Demo 3 — Bulk Blast

### The setup (19:30 - 20:00)

> Third use case. Bulk blast.

> I dropped a new video. I want to email my entire community list.

### The prompt + demo (20:00 - 22:30)

[SHOW: Terminal]

```
/email blast members — about the new video I just uploaded, "Build Your First Claude Code Skill in 15 Minutes" — punchy tone, link is youtube.com/watch?v=ABC123
```

[SHOW: Claude drafts the HTML — shows a preview]

> Claude drafts the email. Shows me the preview. I read it.

[SHOW: Claude asks: "Who do you want to target?" with options: all members, free only, premium only, custom filter]

> Asks me who to target. I'll pick "all members."

[SHOW: Claude responds: "247 contacts will receive this email. Confirm?"]

> 247 contacts. I confirm.

[SHOW: Terminal — batched sends running. Show 50 at a time with a brief pause between batches.]

```
Sending batch 1/5 (1-50) ... done
Sending batch 2/5 (51-100) ... done
Sending batch 3/5 (101-150) ... done
Sending batch 4/5 (151-200) ... done
Sending batch 5/5 (201-247) ... done
TOTAL: 247 emails sent in 58 seconds
```

> 247 emails sent in under a minute. Resend's batch size is 50, so the script loops with a brief pause to stay polite.

### Why this matters (22:30 - 23:30)

> Every send is logged in the `email_sends` table. Every recipient has a Resend ID I can look up later. Full open-rate analytics, same SQL queries from before.

> No SaaS dashboard. No subscription. No monthly invoice.

> Three use cases — one-off, drip, blast — all running from my terminal.

> Now I'll show you how to build your own.

---

## [23:30 - 28:00] Build Your Own — The 4-Step Setup

### Step 1: Get a Resend account (23:30 - 24:15)

[SHOW: Browser opens resend.com — signup page → domains page → add a domain]

> Sign up for Resend at resend.com. Add your sending domain. They walk you through the DNS records — SPF, DKIM, the verification record.

[SHOW: Quick view of the DNS records UI]

> About 10 minutes to set up if your DNS is in Cloudflare or a similar tool. Once verified, you get an API key.

[SHOW: API keys panel, generate a new key, blur the actual value]

> Copy the API key. We'll use it in step 3.

### Step 2: Create the skill folder + SKILL.md (24:15 - 25:30)

[SHOW: Terminal]

```bash
mkdir -p ~/.claude/skills/email
touch ~/.claude/skills/email/SKILL.md
```

> Create the folder. Create SKILL.md inside.

[SHOW: Open SKILL.md in VS Code, type the frontmatter live]

```yaml
---
name: email
description: Send emails via Resend - one-off emails, bulk blasts, or automated drip campaigns. Triggers on - send email, email campaign, drip campaign, blast email, email members, welcome emails.
argument-hint: [send/campaign/status/list] [options]
allowed-tools: Bash(python3:*), Read, Write, Edit, AskUserQuestion
user-invocable: true
---
```

> Five fields. Name matches the folder. Description is what Claude reads to decide when to fire this skill — make the triggers specific. Allowed tools is what the skill can use. User-invocable true makes it a slash command.

> Below the frontmatter is plain English describing what to do based on the user's request. I'll link my full SKILL.md in the description below — feel free to copy it.

### Step 3: The Python scripts (25:30 - 26:45)

[SHOW: Terminal]

```bash
cd ~/.claude/skills/email
touch send_email.py email_campaign.py sync_contacts_resend.py
```

> Three Python scripts. About 60-100 lines each. Don't write them yourself — describe what you want to Claude Code and let it write them.

[SHOW: Type into Claude Code]

```
read ~/.claude/skills/email/SKILL.md and write send_email.py — it should take --subject, --html-file, --to (single email) or --filter (free/premium/vip/all), call the Resend API using the RESEND_API_KEY env var, batch sends in groups of 50, and log every send to the email_sends table in ~/.claude/skills/skool/data/skool.db
```

> Claude reads my skill file, understands the contract, and writes the script. Same for the campaign runner and the contacts sync.

[SHOW: Files appearing, briefly highlight the imports + main function in send_email.py]

> Add `RESEND_API_KEY` to `~/.claude/.env`. The skill reads it from there.

### Step 4: The database (26:45 - 28:00)

[SHOW: Terminal]

```bash
sqlite3 ~/.claude/skills/skool/data/skool.db < ~/.claude/skills/email/schema.sql
```

> Three tables. Schema is in the SKILL.md I'm sharing — paste it into a `schema.sql` file and run it once.

[SHOW: TablePlus showing the new empty tables]

> Now you've got the foundation. Add your first campaign by inserting one row into `email_campaigns` and one row per step into `email_campaign_steps`. Sample insert in the skill file.

> Total build time if you're following along with Claude Code — maybe 90 minutes. Maybe 2 hours if you want to make the templates pretty.

---

## [28:00 - 30:00] The Honest Trade-Offs

[CAMERA: Face to camera, honest tone]

> Quick honesty check. This system has real downsides compared to a SaaS tool. I'm not going to pretend it doesn't.

> One — no GUI. If you don't like the terminal, this is a hard pass. ConvertKit's editor is genuinely nice.

> Two — no built-in analytics dashboard. You query SQLite. If you want pretty charts, you're building them or using a separate tool.

> Three — no template marketplace. You're writing HTML or letting Claude draft it. Most of mine are 100 lines, nothing fancy.

> Four — deliverability is on you. You have to warm up your sending domain. ConvertKit handles that for you. Resend makes it easy but doesn't do it automatically.

> If you're a creator running a community and you're paying $50 a month for email, this saves you 600 bucks a year and gives you full control. If you're a marketer running 10 different segmented campaigns with complex branching automations, this might not be enough.

> Be honest about which one you are.

---

## [30:00 - 31:30] CTA

[CAMERA: Direct to lens, energy up]

> Three things if this was useful.

> One — full code. SKILL.md, Python scripts, database schema, the welcome email templates I use. All in my free Skool community. Link below.

> Two — if you want to see the broader picture, my video "32 Posts a Week, 7 Claude Code Skills. Here's How." covers the full content pipeline this email skill plugs into. Link below.

> Three — subscribe. New Claude Code workflows Mondays and Thursdays.

> See you in the next one.

[SHOW: Quick callback montage — ConvertKit pricing tab closing → terminal running campaign → SQL query returning open rates → 247 emails sent confirmation. Fast cuts, 1.5 sec each.]

---

## Production Notes

### Critical Pre-Production

This video shows real email infrastructure. ANY of the following on screen = bad day:
- [ ] Real customer emails — blur in edit or use `example@example.com` substitutes
- [ ] Your Resend API key — never visible in terminal, env, or browser dev tools
- [ ] Your `.env` file — never open it on camera
- [ ] Skool member real names — use test data only
- [ ] Domain you don't want public

Do a full dry-run with a screen recorder before official take. Watch the recording. Fix anything sensitive before going live.

### Demo Prep (do these BEFORE filming)

1. **Create 3-5 test contacts** in SQLite with timestamps that put them at different campaign steps
2. **Pre-populate `email_sends`** with fake history so SQL queries look real on camera (include some `opened_at` values so the open-rate query returns interesting numbers)
3. **Send 1 real test email to yourself** with a beautiful HTML template — capture it as b-roll
4. **Have the ConvertKit pricing tab open** in a clean browser window
5. **Smoke test every command** in the 24 hours before recording

### B-roll Needed

- ConvertKit / Beehiiv / ActiveCampaign pricing pages (side by side or quick cuts)
- Architecture diagram (Excalidraw or Remotion)
- Real terminal recordings of every command in the script
- TablePlus or DB Browser views showing the 3 tables and the SQL query results
- Resend dashboard (blur API keys, blur send IDs)
- One screenshot of a beautiful rendered welcome email

### Energy Curve

| Segment | Energy | Notes |
|---|---|---|
| Hook | 10/10 | Pricing → receipt |
| Pain point | 7/10 | Empathy |
| Architecture | 6/10 | Teaching mode |
| Demo 1 (one-off) | 7/10 | Quick wins |
| Demo 2 (drip) | 8/10 | The "wow" moment, longest segment |
| Demo 3 (blast) | 7/10 | Practical, fast |
| Build your own | 8/10 | Empowering |
| Trade-offs | 6/10 | Honest, grounded |
| CTA | 10/10 | Get the click |

### Chapters (paste into description)

- 0:00 The $50/mo I don't pay
- 0:25 The 3 things I needed
- 2:30 The Architecture (Resend + Claude Code + SQLite)
- 6:30 Demo 1: One-off send
- 11:00 Demo 2: Drip campaigns (the real reason)
- 19:30 Demo 3: Bulk blast to my list
- 23:30 Build your own in 4 steps
- 28:00 The honest trade-offs
- 30:00 Grab the code (free)
