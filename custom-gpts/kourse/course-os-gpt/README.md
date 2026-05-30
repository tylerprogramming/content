# Course OS Custom GPT — Setup Guide

## What's in This Folder

| File | Purpose | Upload To |
|------|---------|-----------|
| `system-prompt.md` | The GPT's instructions — defines personality, behavior, boundaries | Paste into **"Instructions"** field in GPT Builder |
| `voice-profile.md` | Detailed tone/personality reference for the GPT | Upload as **Knowledge** file |
| `knowledge-base.md` | All course content organized by topic | Upload as **Knowledge** file |

## Setup Steps (OpenAI Custom GPT)

1. Go to [chat.openai.com](https://chat.openai.com) → Explore GPTs → Create
2. In the **Configure** tab:
   - **Name:** Course OS Assistant (or whatever the client prefers)
   - **Description:** Your personal guide for the Course OS module
   - **Instructions:** Copy/paste the entire contents of `system-prompt.md`
3. Under **Knowledge**, upload:
   - `voice-profile.md`
   - `knowledge-base.md`
4. Under **Capabilities**, enable:
   - Code Interpreter (optional — not really needed)
   - Disable Web Browsing (keeps answers grounded in course content only)
5. Save and test with sample questions

## Sample Test Questions

Use these to verify the GPT is working correctly:

- "Should I have a free and paid community?" → Should strongly recommend both, explain why
- "What gear do I need to record my course?" → Should emphasize mic > camera, keep it simple
- "How do I structure my slides?" → Should reference the 5 David JP Phillips principles
- "I'm scared to be on camera" → Should be encouraging, reference "if you can talk to a friend, you can record a course"
- "How do I run Facebook ads?" → Should say this is covered in the Traffic module, not Course OS

## Framework for Future Transcripts

This same 3-file structure works for any new course module:

1. **Extract voice profile** (only needed once per creator — reuse `voice-profile.md`)
2. **Build knowledge base** from the new transcript (add new topics or create a separate file)
3. **Update system prompt** if new topics need to be added to the scope

For larger documents:
- Split the knowledge base into multiple files by module (e.g., `kb-traffic-os.md`, `kb-sales-os.md`)
- Keep each file focused on one module's content
- The system prompt stays mostly the same — just update the "Topics You Can Help With" section
