# 14-Day Ship Challenge: Email Drip + Builder Roundup
Date: Apr 22, 2026

Draft copy for the automated emails that run alongside the challenge, plus the weekly Builder Roundup post template.

Send via `/email` (Resend) using the contact list synced from `sync_skool_members.py`.

---

## EMAIL 1: Day 0 (sent immediately on free signup)

**Subject:** Your 14 days start now (here's exactly what to do)

Hey {{first_name}},

Tyler here. Welcome to The AI Agency.

You just committed to something simple: in 14 days, you'll have one working AI automation deployed in your business. Not learned about. Actually running.

**Your ONLY task today:**

1. Open the Classroom tab
2. Start the "Start Here: Your AI Business Roadmap" course (15 minutes)
3. Then open "AI for Your Business: 5 Automations You Can Deploy Today"
4. Pick the ONE automation that either saves you the most time or makes you the most money right now

That's it. Do not try to do five. Pick ONE.

When you've picked, post in the Builds category:
- Who you are
- What business you run
- The ONE automation you're shipping in 14 days

I personally reply to the first 10 people who post. If you hit post today, you're likely in that 10.

You ship, you get the first month of Builder free. That's the deal.

Talk in 7 days.

Tyler

P.S. Next live Community Q&A is May 1, 1:00 PM ET. Bring your plan.

---

## EMAIL 2: Day 7 (mid-challenge checkpoint)

**Subject:** Day 7 check-in: are you on track or stuck?

{{first_name}},

Halfway through your 14-Day Ship Challenge. Two paths from here:

**If you're on track** (you picked an automation and you're mid-build):

- Post in the Builds category: one screenshot of where you're at + one thing you're stuck on
- I reply within 24 hours with a direct fix

**If you haven't started:**

Be honest with yourself. Is it:
- You couldn't pick an automation? (Reply to this email with your business type, I'll pick one for you)
- You got pulled into other work? (Protect 30 min on Saturday and you'll catch up easy)
- The install looked complicated? (Watch the Claude Code + Cowork course, Module 1, it removes the friction)

Most people who don't ship aren't stuck on the build. They're stuck on the pick. Just pick. The automation you start is always better than the one you're still researching.

You have 7 days left.

Tyler

P.S. Still need a reminder what's in this for you? Completion = first month of Builder free. The full skills library + weekly live sessions. Worth showing up.

---

## EMAIL 3: Day 14 (final push + instructions)

**Subject:** Today's the day. Here's how to cash in.

{{first_name}},

Day 14. If your automation is running, it's time to ship.

**What "shipped" means:**

1. Your automation is actually deployed (not just built, running on real inputs)
2. You recorded a 60-second Loom showing it working end to end
3. You posted in the Builds category with:
   - The Loom link
   - One metric (hours saved per week OR first dollar impact)
   - Tag @tyler

**Post that by midnight ET tonight** and you lock in:
- Your name in this week's Builder Roundup post (community-wide)
- Access to the Shipped Builders private channel
- **First month of Builder tier, free.** No credit card, no catch. I manually comp it.

To claim the Builder month: reply to your shipped post, or DM me. I'll comp you within 24 hours.

**If you're not quite ready:**

Post your progress in Builds anyway. Ask for help. The challenge isn't a pass/fail. Completers get the Builder month, but anyone posting progress gets my feedback.

This is the whole point of this community: you ship work that moves your business. Today is that day.

Let's go.

Tyler

---

## EMAIL 4: Day 16 (non-completer follow-up, optional)

**Subject:** You didn't ship. That's OK. Here's what I'd do next.

{{first_name}},

You joined 16 days ago and didn't post a completion. No judgment. That's honest of me to acknowledge.

Here's what I've seen from 600+ members: the ones who ship their first automation usually do it on their second 14-day run, not their first. The first one exposes what's actually blocking you. The second one works.

Three things you can do this week:

1. **Reset.** Pick a smaller automation. Instead of "automate all my content," pick "generate one social caption from a prompt." Ship that. Then go bigger.
2. **Ask.** Post in the Builds category: "I didn't ship. Here's where I got stuck." Community answers, I answer. Free.
3. **Go live.** Show up to the Community Q&A May 1. Come with your blocker. I'll debug it live with you.

The offer on the Builder month is still on the table if you ship within 14 days of TODAY. Reset clock, same deal.

You in?

Tyler

---

## WEEKLY BUILDER ROUNDUP (community post, posts every Monday)

**Title:** Builder Roundup - Week of {{date_range}}

**Body:**

This week's shipped builders:

**{{member_name_1}}** - {{automation}} - {{metric}}
Loom: {{loom_link}}

**{{member_name_2}}** - {{automation}} - {{metric}}
Loom: {{loom_link}}

**{{member_name_3}}** - {{automation}} - {{metric}}
Loom: {{loom_link}}

{{etc for all shippers this week, up to 10}}

---

Every one of these automations was built by a member in 14 days or less. Every one is running right now in their business.

**Starting your own 14-Day Ship Challenge this week?** Post your plan in the Builds category. First 10 builds get my personal reply.

**Already shipped but haven't posted?** Drop your Loom in Builds. You qualify for the first-month-free Builder offer for 14 days after your shipped date.

Let's build.

Tyler

---

## OPERATIONAL NOTES

**Drip trigger:** new free member joins -> Email 1 on Day 0, Email 2 on Day 7, Email 3 on Day 14, Email 4 on Day 16 (only if no completion post)

**How to detect completion:** check the Builds category for posts by the member that include a Loom link + mention completion. Can be manual for first month, then scripted later via `skool_engagement.py`.

**Builder Roundup:** pull shippers from last 7 days, post Monday mornings around 9 AM ET. Can be drafted via `/skool` once we have a query for "new posts in Builds category in last 7 days with Loom links."

**Comp flow for first month Builder free:**
1. Member posts completion in Builds
2. You reply, ask for their Builder signup or DM them a comp code
3. Skool admin UI has "Grant free month" option on membership page
4. Track comp'd members in a simple log so you know who's on comp'd month vs paid

**Capacity check:** if more than 25-30 people complete in a given month, the 45-min strategy audit becomes a bottleneck. Options if that hits: cap the strategy audit at 15 completers/mo + group audit for the rest, OR extend Builder onboarding lead time to 30 days.
