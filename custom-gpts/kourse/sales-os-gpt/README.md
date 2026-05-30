# Sales OS Assistant — Setup Guide

## What's in This Folder

| File | Purpose | Upload To |
|------|---------|-----------|
| `system-prompt.md` | The GPT's instructions — defines Miles' personality, behavior, scope | Paste into **"Instructions"** field in GPT Builder |
| `kb-sales-fundamentals-appointments.md` | Sales mindset, conviction, the pain principle, inbound + outbound appointment systems | Upload as **Knowledge** file |
| `kb-payments-tracking-script.md` | Payments via Skool, tracking calls, recording, contracts, full sales script walk-through | Upload as **Knowledge** file |
| `kb-presenting-closing-objections-team.md` | Presenting, closing techniques, unique justification, objection handling (looping framework), upsells, building a sales team | Upload as **Knowledge** file |

> **Note:** Sales OS is taught by Miles (Head of Sales / CRO at Kourse) — not Max. Do NOT upload `voice-profile.md` — Miles' voice and credentials are baked into the system prompt directly.

## Setup Steps (OpenAI Custom GPT)

1. Go to [chat.openai.com](https://chat.openai.com) → Explore GPTs → Create
2. In the **Configure** tab:
   - **Name:** Sales OS Assistant
   - **Description:** Your personal sales coach for booking more calls, closing high-ticket offers, and building a sales system — based on Miles' Sales OS training inside Kourse
   - **Instructions:** Copy/paste the entire contents of `system-prompt.md`
3. Under **Knowledge**, upload all 3 knowledge files:
   - `kb-sales-fundamentals-appointments.md`
   - `kb-payments-tracking-script.md`
   - `kb-presenting-closing-objections-team.md`
4. Under **Capabilities**:
   - Disable Web Browsing (keeps answers grounded in course content only)
   - Code Interpreter: not needed
5. Save and test with sample questions

## Sample Test Questions

Use these to verify the GPT is working correctly:

- "I'm nervous about sounding salesy on calls. What do I do?" → Should explain the helping mindset, moral obligation to sell, the lottery ticket analogy
- "How do I set up my booking form to get better qualified leads?" → Should explain SSI framework (Situation, Seriousness, Investment), friction scale, qualifying questions at different levels
- "Walk me through the full sales script" → Should cover all 8 stages: Introduction → Setting the Frame → Pre-Discovery → Discovery → Statement of Confidence → Presentation → Pre-Close → Closing
- "How do I ask about their goals without sounding scripted?" → Should explain question wrapping, give the wrapped goal question word-for-word
- "Someone said they need to think about it. What do I do?" → Should give the looping framework (Loop 0 through Best Case/Worst Case) and the push-pull for "I need to think about it"
- "How do I handle the price objection?" → Should explain isolating the objection with money aside close, then pay-in-two, then "how much can you put down today?"
- "What is unique justification?" → Should explain the photocopier study, give the "I do 10 calls a day" script, reference the $230K Skool Games example
- "When should I hire a setter vs. a closer?" → Should give the 50-100 leads/day threshold for a setter, 5+ calls/day threshold for a closer, and the "hire from your community first" principle
- "How do I upsell right after the sale?" → Should explain the buying window, rollover payments, the monthly-to-annual Loom sequence
- "How do I take payment if Skool's about page has a bug?" → Should explain the classroom method: create a classroom, name it for the student, set one-time price, invite free, send URL
- "How do I set up outbound DMs in Skool?" → Should redirect to the auto DM system in the outbound section (not covered in Promo OS — this is Sales OS)
- "How do I run a weekly workshop?" → Should redirect: that's covered in Promo OS, not Sales OS

## Knowledge Base Coverage Map

| Video | Topic | Knowledge File |
|-------|-------|----------------|
| Video 1 | Welcome to Sales OS — Miles' background, what's covered | kb-sales-fundamentals-appointments.md |
| Video 2 | Sales fundamentals — conviction, helping by selling, pain principle | kb-sales-fundamentals-appointments.md |
| Video 3 | Inbound appointment system — booking form, VSL, reminders, triage, pull-forward | kb-sales-fundamentals-appointments.md |
| Video 4 | Outbound setting — auto DM, cold calling, Scoot CRM, inbound opt-in setting | kb-sales-fundamentals-appointments.md |
| Video 5 | Payments + tracking — Skool methods, payment plans, BNPL, GHL pipeline, Fathom, contracts | kb-payments-tracking-script.md |
| Video 6 | Sales script — why use one, 8-stage framework, question wrapping, full walk-through | kb-payments-tracking-script.md |
| Video 7 | Presenting — pitch deck setup, how to present, check-ins, linking to discovery | kb-presenting-closing-objections-team.md |
| Video 8 | Closing — priming the close, stacking conditions, unique justification, the why-now offer | kb-presenting-closing-objections-team.md |
| Video 9 | Objection handling — looping framework, money aside close, deposit strategy, spouse objection | kb-presenting-closing-objections-team.md |
| Video 10 | Upsells — buying window, rollover payments, monthly-to-annual upsell, moral obligation | kb-presenting-closing-objections-team.md |
| Video 11 | Building a sales team — when to hire, volume thresholds, who to hire, handing off the system | kb-presenting-closing-objections-team.md |
