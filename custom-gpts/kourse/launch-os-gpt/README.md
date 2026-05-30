# Launch OS Assistant — Setup Guide

## What's in This Folder

| File | Purpose | Upload To |
|------|---------|-----------|
| `system-prompt.md` | The GPT's instructions — defines personality, behavior, scope | Paste into **"Instructions"** field in GPT Builder |
| `voice-profile.md` | Detailed tone/personality reference for Max's voice | Upload as **Knowledge** file |
| `kb-skool-setup.md` | Skool platform setup, 3 C's, about page, VSL, community design | Upload as **Knowledge** file |
| `kb-business-model.md` | The core business model, annual vs monthly pricing, lead magnet strategy | Upload as **Knowledge** file |
| `kb-tech-stack.md` | GoHighLevel, domain/email setup, Mailgun, Zapier/SAP integration, VSL funnel | Upload as **Knowledge** file |
| `kb-sales-funnel.md` | Sales page copywriting, calendar setup, the 3 core automations | Upload as **Knowledge** file |
| `kb-niche-course.md` | Niche selection (Ikigai/Apple strategy), course design, product-market fit | Upload as **Knowledge** file |

## Setup Steps (OpenAI Custom GPT)

1. Go to [chat.openai.com](https://chat.openai.com) → Explore GPTs → Create
2. In the **Configure** tab:
   - **Name:** Launch OS Assistant (or whatever the client prefers)
   - **Description:** Your personal guide for setting up the Launch OS tech stack and business systems
   - **Instructions:** Copy/paste the entire contents of `system-prompt.md`
3. Under **Knowledge**, upload all 6 knowledge files:
   - `voice-profile.md`
   - `kb-skool-setup.md`
   - `kb-business-model.md`
   - `kb-tech-stack.md`
   - `kb-sales-funnel.md`
   - `kb-niche-course.md`
4. Under **Capabilities**:
   - Disable Web Browsing (keeps answers grounded in course content only)
   - Code Interpreter: not needed
5. Save and test with sample questions

## Sample Test Questions

Use these to verify the GPT is working correctly:

- "Should I do annual or monthly pricing?" → Should strongly recommend annual, explain the cash flow and retention benefits
- "How do I set up my email deliverability?" → Should explain SPF, DKIM, DMARC, and Mailgun step by step
- "What's the difference between my free and paid Skool community?" → Should explain the funnel logic and lead magnet strategy
- "How do I set up the Zapier integration with GoHighLevel?" → Should walk through the SAP integration step by step
- "I don't know what niche to pick" → Should walk through the Ikigai framework and Apple strategy
- "How do I write a sales page?" → Should give the full sales page structure with sections and copywriting tips
- "What automations do I need?" → Should describe all 3 core automations (welcome sequence, VSL sequence, appointment confirmations)
- "How do I run Facebook ads?" → Should redirect to Traffic OS module

## Knowledge Base Coverage Map

| Video | Topic | Knowledge File |
|-------|-------|---------------|
| Video 1 | Welcome & Skool school setup | kb-skool-setup.md |
| Video 2 | The business model & pricing | kb-business-model.md |
| Video 3 | 3 C's, about page, VSL, community design | kb-skool-setup.md |
| Video 4 | GoHighLevel setup & Kourse snapshot | kb-tech-stack.md |
| Video 5 | Domain, email setup, deliverability, Mailgun | kb-tech-stack.md |
| Video 6 | Zapier/SAP integration, VSL funnel, website | kb-tech-stack.md |
| Video 7 | Sales page structure & copywriting | kb-sales-funnel.md |
| Video 8 | Calendar & booking setup | kb-sales-funnel.md |
| Video 9 | The 3 automations (welcome, VSL, appointments) | kb-sales-funnel.md |
| Video 10 | Testing, validation, product-market fit | kb-niche-course.md |
| Video 11 | Niche selection & course design | kb-niche-course.md |

## Framework for Future Modules

This same structure works for any new Kourse module:

1. **Reuse `voice-profile.md`** — same creator, same voice across all modules
2. **Build knowledge base files** from new transcripts (one file per topic cluster)
3. **Update system prompt** — add new topics to "Topics You Can Help With" section
4. **Keep each KB file focused** — one topic area per file for clean GPT retrieval

For very large modules:
- Split KB files by sub-topic (e.g., `kb-ghl-setup.md`, `kb-ghl-automations.md`)
- Keep each file under ~50KB for optimal GPT context retrieval
- The system prompt stays mostly the same — just update the scope section
