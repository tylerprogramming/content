# Cold Email Advisor — Setup Guide

A Custom GPT built from Miles' Outbound Systems cold email training inside Capitalist. Answers student questions about cold email foundations, Evergreen VSL creation, and copy writing — in Miles' voice, using his templates.

## What's in This Folder

| File | Purpose | Upload To |
|---|---|---|
| `system-prompt.md` | Personality, rules, behavioral guardrails | GPT Instructions field |
| `kb-foundations.md` | What cold email is, who it's for, system map, expectations | Knowledge (upload) |
| `kb-evergreen-vsl.md` | VSL rules, structure, CTA, review checklist | Knowledge (upload) |
| `kb-copy-bank.md` | Subject lines, first lines, email templates, follow-ups, rules | Knowledge (upload) |

> Voice and behavior rules are baked directly into `system-prompt.md` — no separate voice-profile file needed.

## Setup Steps (OpenAI Custom GPT)

1. Go to chat.openai.com → **Explore GPTs → Create**
2. In the **Configure** tab:
   - **Name:** Cold Email Advisor
   - **Description:** Your cold email coach inside the Outbound Systems training. Built from Miles' teachings. Answers questions about strategy, Evergreen VSLs, and copy — direct, data-driven, and template-first.
   - **Instructions:** Copy/paste the entire contents of `system-prompt.md`
3. Under **Knowledge**, upload all three KB files:
   - `kb-foundations.md`
   - `kb-evergreen-vsl.md`
   - `kb-copy-bank.md`
4. Under **Capabilities:**
   - **Disable Web Browsing**
   - Code Interpreter: not needed
5. **Save** and test with the sample questions below.

## Sample Test Questions

Use these to verify the GPT is answering in Miles' voice, using the templates, and following the behavioral rules.

### Fit & foundations
1. *"I sell a $197 ebook on dog training. Should I use cold email?"* → Should say no / poor fit (B2C + low ticket), explain why, and suggest paid ads or organic instead.
2. *"What's a B2 Wannabe?"* → Should define Miles' term specifically (not a generic answer).
3. *"How long until I can start sending?"* → Should say 2-3 weeks due to warmup period.
4. *"Is this better than paid ads?"* → Should reference the comparison table / lower cost, higher quality leads, limited volume.

### Campaign diagnostics (KPI rule)
5. *"My reply rate is low, should I change my copy?"* → Should ask how many emails sent, ask for booking rate / positive reply rate / reply rate numbers, and apply the 500-email rule.
6. *"I've sent 200 emails and only got 2 replies. What's wrong?"* → Should tell them to keep sending, don't change copy before 500.

### Subject lines
7. *"What's a good subject line?"* → Should recommend from the Subject Line Vault and paste several.

### First lines
8. *"How should I personalize the first line of my emails?"* → Should recommend **LinkedIn summary via Clay** first, then list the other first-line variants.

### Writing copy from scratch
9. *"Can you write me a cold email for my coaching offer?"* → Should refuse to write yet and ask the 7 pre-copy questions (niche, avatar, outcome, timeframe, guarantee, USP, proof).

### Copy critique
10. *"Here's my email: [paste]"* → Should check for (a) promise statement following framework, (b) proof, (c) hyphens. Call out anything missing and rewrite using a template from the bank.

### Evergreen VSL
11. *"How long should my Evergreen VSL be?"* → 2-3 minutes, under 3.
12. *"Should I make it look like the VSL is personalized for them?"* → No — call it out as pre-recorded. Quote Rule 3.
13. *"I don't have any client case studies yet. Can I still make a VSL?"* → Yes — use your own results as proof.
14. *"Walk me through the VSL structure."* → 5 steps: intro (face) → agenda → story → screen share + proof → low-friction CTA.

### Follow-ups
15. *"How do I follow up if they don't reply?"* → Paste the full follow-up sequence (FU1, on-video FU, bump, priority check, memes/gifs).

### Lead sourcing
16. *"Where do I get leads for my real estate coaching offer?"* → Should ask "where does your avatar live" **first**, not jump to a tool. Then once avatar is confirmed, recommend Apollo / Apify / Clay / manual based on fit.
17. *"Should I use LinkedIn Sales Navigator with Clay?"* → Should redirect away from Sales Nav and recommend Apollo / Apify / Clay / manual.
18. *"Which lead sourcing tool should I use?"* → Should refuse to answer until they've described where their avatar lives online.
19. *"What about ZoomInfo or Hunter?"* → Should say those aren't the tools Miles teaches, redirect to the approved stack.

### Out of scope
20. *"Which tool should I use to send emails?"* → Should say that's covered in a different video, give framework-level answer only.
21. *"Walk me click-by-click through setting up an Apollo filter."* → Should give the framework of what to filter on, but say the UI walkthrough is in another video.
22. *"How do I close the call after they book?"* → Should say sales call scripts are a different module.

## Knowledge Base Coverage Map

| Section / Topic | Source | Knowledge File |
|---|---|---|
| What cold email is, ICP, B2 Wannabe | Video 1 (intro) | `kb-foundations.md` |
| Who the system is for / not for | Video 1 | `kb-foundations.md` |
| 6-step system map | Video 1 | `kb-foundations.md` |
| Lead sourcing framework + approved stack (Apollo / Apify / Clay / manual) | Behavior rules + foundations | `kb-foundations.md` + `system-prompt.md` |
| "Where does your avatar live" discovery question | Behavior rules | `system-prompt.md` |
| Why no Sales Navigator, no ZoomInfo, etc. | Behavior rules | `system-prompt.md` + `kb-foundations.md` |
| Setup expectations, costs, timeline | Video 1 | `kb-foundations.md` |
| 500-email rule, KPI tracking | Behavior rules | `system-prompt.md` |
| 3 VSL rules | VSL Creation Guide | `kb-evergreen-vsl.md` |
| VSL 5-step structure | VSL Creation Guide | `kb-evergreen-vsl.md` |
| VSL CTA + delivery message | VSL Creation Guide | `kb-evergreen-vsl.md` |
| Example VSLs (2 Loom links) | VSL Creation Guide | `kb-evergreen-vsl.md` |
| Subject Line Vault | Copy Bank | `kb-copy-bank.md` |
| Personalized first line templates | Copy Bank | `kb-copy-bank.md` |
| Email body templates 1-4 | Copy Bank | `kb-copy-bank.md` |
| Follow-up sequence | Copy Bank | `kb-copy-bank.md` |
| Booking link message | Copy Bank | `kb-copy-bank.md` |
| VSL delivery message | Copy Bank | `kb-copy-bank.md` |
| Promise framework (avatar/outcome/timeframe/USP) | Behavior rules + Copy Bank | `system-prompt.md` + `kb-copy-bank.md` |
| No-hyphens rule | Behavior rules | `system-prompt.md` + `kb-copy-bank.md` |
| Pre-copy 7 questions | Behavior rules | `system-prompt.md` |

## Coverage Gaps (When More Videos Are Available)

The GPT is solid for foundations, VSL, copy, and the lead sourcing framework. Upload transcripts for these videos later to fill the gaps:

- Inbox setup & domain infrastructure
- Warmup specifics
- Deep Apollo / Apify / Clay tool walkthroughs (UI-level steps)
- AI enrichment prompts (beyond "use Clay on LinkedIn summaries")
- Deliverability tuning
- Sales call / closing scripts

When you get those transcripts, drop them in and say "add these to the GPT" — new KB files can be added without rebuilding the others.
