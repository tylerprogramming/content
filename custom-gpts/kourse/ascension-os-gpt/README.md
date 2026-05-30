# Ascension OS Assistant — Setup Guide

## What's in This Folder

| File | Purpose | Upload To |
|------|---------|-----------|
| `system-prompt.md` | The GPT's instructions — defines personality, behavior, scope, and CTA rules | Paste into **"Instructions"** field in GPT Builder |
| `voice-profile.md` | Detailed tone/personality reference for Max's voice | Upload as **Knowledge** file (reuse from course-os-gpt) |
| `kb-mindset-mastery.md` | Self mastery, discipline, mindset frameworks, performance tracking | Upload as **Knowledge** file |
| `kb-team-hiring.md` | Team building, hiring strategy, roles, contracts, compensation | Upload as **Knowledge** file |
| `kb-masterminds.md` | How to sell masterminds, Kourse Mastermind overview, backend upsell strategy | Upload as **Knowledge** file |

## Setup Steps (OpenAI Custom GPT)

1. Go to [chat.openai.com](https://chat.openai.com) → Explore GPTs → Create
2. In the **Configure** tab:
   - **Name:** Ascension OS Assistant
   - **Description:** Your personal guide for the Ascension OS module — mindset, team, and mastermind scaling
   - **Instructions:** Copy/paste the entire contents of `system-prompt.md`
3. Under **Knowledge**, upload all 4 knowledge files:
   - `voice-profile.md`
   - `kb-mindset-mastery.md`
   - `kb-team-hiring.md`
   - `kb-masterminds.md`
4. Under **Capabilities**:
   - Disable Web Browsing (keeps answers grounded in course content only)
   - Code Interpreter: not needed
5. Save and test with sample questions

## Sample Test Questions

Use these to verify the GPT is working correctly:

- "How do I build more discipline?" → Should give actionable steps from the Discipline video + reference performance tracker + CTA to Kourse.com/mastermind
- "What is the Myers Briggs test and why should I do it?" → Should explain the test, the free 16Personalities site, and the ChatGPT prompt to generate the report
- "When should I hire my first team member?" → Should explain "hire where it hurts," explain the community manager as first hire, and direct to Kourse.com/mastermind
- "How do I sell a mastermind?" → Should walk through the product line (free → paid → mastermind), backend upsell strategy, then CTA to Kourse.com/mastermind
- "What is the Kourse Mastermind?" → Should describe what's taught, who it's for, and book a call CTA at Kourse.com/mastermind
- "How do I get more traffic?" → Should redirect to Traffic OS module
- "I'm feeling unmotivated" → Should reference the 90/10 mindset formula, discipline over motivation, and encourage with a CTA

## Knowledge Base Coverage Map

| Video | Topic | Knowledge File |
|-------|-------|----------------|
| Video 1 | Module welcome + performance tracking + annual planner | kb-mindset-mastery.md |
| Video 2 | Self mastery — know thyself, Myers Briggs, new character, book list, meditation, habits | kb-mindset-mastery.md |
| Video 3 | Discipline — self-discipline, sacrifice, willpower, systems + tools | kb-mindset-mastery.md |
| Video 4 | Team — who/when/why/how to hire, roles, compensation | kb-team-hiring.md |
| Video 5 | How to sell masterminds — backend upsell, product line, why it works | kb-masterminds.md |
| Video 6 | What is Kourse Mastermind — offer overview, who it's for, CTA | kb-masterminds.md |

## Framework for Future Modules

This same structure works for any new Kourse module:

1. **Reuse `voice-profile.md`** — same creator, same voice across all modules
2. **Build knowledge base files** from new transcripts (one file per topic cluster)
3. **Update system prompt** — add new topics to "Topics You Can Help With" section
4. **Keep each KB file focused** — one topic area per file for clean GPT retrieval
