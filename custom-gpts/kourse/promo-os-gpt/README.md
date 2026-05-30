# Promo OS Assistant — Setup Guide

## What's in This Folder

| File | Purpose | Upload To |
|------|---------|-----------|
| `system-prompt.md` | The GPT's instructions — defines personality, behavior, scope | Paste into **"Instructions"** field in GPT Builder |
| `voice-profile.md` | Detailed tone/personality reference for Max's voice | Upload as **Knowledge** file (reuse from course-os-gpt) |
| `kb-promo-strategies.md` | Promo checklist, all conversion tactics, school posts, DMs, calls, email, links, onboarding | Upload as **Knowledge** file |
| `kb-offer-pricing-presell.md` | Offer structure, pricing models, the $100M offer formula, launch & pre-sell strategy | Upload as **Knowledge** file |
| `kb-webinars-engagement-email.md` | Weekly workshops, Skool engagement secrets, video email sequence | Upload as **Knowledge** file |

## Setup Steps (OpenAI Custom GPT)

1. Go to [chat.openai.com](https://chat.openai.com) → Explore GPTs → Create
2. In the **Configure** tab:
   - **Name:** Promo OS Assistant
   - **Description:** Your personal guide for converting free Skool members into booked calls and paying customers
   - **Instructions:** Copy/paste the entire contents of `system-prompt.md`
3. Under **Knowledge**, upload all 4 knowledge files:
   - `voice-profile.md`
   - `kb-promo-strategies.md`
   - `kb-offer-pricing-presell.md`
   - `kb-webinars-engagement-email.md`
4. Under **Capabilities**:
   - Disable Web Browsing (keeps answers grounded in course content only)
   - Code Interpreter: not needed
5. Save and test with sample questions

## Sample Test Questions

Use these to verify the GPT is working correctly:

- "How often should I send Skool email blasts?" → Should say every 72 hours (Monday and Thursday), explain the auto-email feature
- "How do I run a weekly workshop?" → Should walk through the full structure: 2-3 min welcome, 30 min training (what not how), 5 min CTA to book call, 15-20 min Q&A on a community post
- "What should I price my course at?" → Should recommend $2,000–$3,500, explain split pay vs pay in full, the 2 out of 10 difficulty for high ticket
- "How do I pre-sell my course before it's built?" → Should explain the Hormozi-style pre-sell offer: scarcity, discount, bonus coaching calls, testimonial ask, launch timeline
- "What is the video email sequence?" → Should explain the landing page + locked video system, how it improves open rates and call bookings
- "How do I rank higher on Skool Discovery?" → Should cover check-in posts, accountability posts, active owner, polls, live streams, contests
- "Should I do a guarantee?" → Should explain the difference between conditional and unconditional, Max's current position on not doing them, and how to frame the risk of NOT buying
- "How do I run YouTube ads?" → Should redirect to Traffic OS module

## Knowledge Base Coverage Map

| Video | Topic | Knowledge File |
|-------|-------|----------------|
| Video 1 | Module welcome + promo goals overview | kb-promo-strategies.md |
| Video 2 | Free to paid conversions + full promo checklist | kb-promo-strategies.md |
| Video 3 | Offer & pricing — structure, models, value stack | kb-offer-pricing-presell.md |
| Video 4 | Launch & pre-sell — Hormozi-style pre-sell framework | kb-offer-pricing-presell.md |
| Video 5 | Weekly webinars/workshops — structure + school engagement hacks | kb-webinars-engagement-email.md |
| Video 6 | Skool engagement secrets — ranking in Discovery | kb-webinars-engagement-email.md |
| Video 7 | Video email sequence — strategy, landing pages, emails | kb-webinars-engagement-email.md |

## Framework for Future Modules

This same structure works for any new Kourse module:

1. **Reuse `voice-profile.md`** — same creator, same voice across all modules
2. **Build knowledge base files** from new transcripts (one file per topic cluster)
3. **Update system prompt** — add new topics to "Topics You Can Help With" section
4. **Keep each KB file focused** — one topic area per file for clean GPT retrieval
