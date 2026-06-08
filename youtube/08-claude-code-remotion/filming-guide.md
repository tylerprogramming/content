# Claude Code + Remotion - FILMING PLAYBOOK

> Step-by-step guide for what to ACTUALLY DO on screen while recording.
> Includes exact prompts, terminal commands, what to narrate, and pre-work.

---

## PRE-RECORDING SETUP (Do Before You Hit Record)

### 1. Verify Existing Remotion Project Works
- Open `~/my-video` and confirm all 7 compositions render correctly
- Run `npx remotion studio` and preview SevenPlatforms, TerminalType, BlotaMCP
- Make sure the component library (WordByWord, SlamText, etc.) all work

### 2. Prepare a "Clean Start" Folder
- Create a fresh empty directory for the from-scratch demo (e.g., `~/demo-video`)
- You'll build the new project here during filming
- Keep `~/my-video` open in a second window to show the finished component library

### 3. Terminal Setup
- Font size 18+ so viewers can read
- Dark theme
- Have two terminal tabs ready: one for Claude Code, one for Remotion Studio
- Clear terminal history

### 4. Remotion Studio
- Make sure `npx remotion studio` works in the existing project
- Have it running at localhost:3000 before you start recording
- Verify the composition dropdown shows all 7+ compositions

### 5. Pre-render the "Result" Videos
- Render 2-3 of your best compositions to MP4 before filming
- You'll show these in the "Show Result First" section
- `npx remotion render src/index.ts SevenPlatforms out/seven-platforms.mp4`
- `npx remotion render src/index.ts TerminalType out/terminal-type.mp4`

### 6. Screen Layout
- VS Code / editor on the left (60% width)
- Terminal on the right or bottom (40%)
- Remotion Studio in browser ready to cmd-tab to
- Picture-in-picture facecam in bottom-right corner

---

## FILMING: STEP BY STEP

---

### STEP 1: Record the Hook (0:00 - 1:00)

**What you do:**
1. Start with your face on camera (not screen share)
2. Deliver the contrarian hook confidently
3. Cut to a quick montage of animated shorts rendering in terminal

**What you say:**
> See script section [0:00 - 1:00]

**Key moments to nail:**
- "I haven't opened a video editor in months" - say this like it's no big deal
- Credibility stack - fast, factual, not bragging
- "Code-to-Content system" - emphasize this as the framework name
- Skool CTA should feel casual: "I share all of it inside my Skool community"

**Screen time:** 60 seconds, mostly face to camera

---

### STEP 2: Show the Result (1:00 - 2:00)

**What you do:**
1. Switch to screen share - open Remotion Studio
2. Play SevenPlatforms composition (it's visually impressive)
3. Play a second composition (BlotaMCP or TerminalType)
4. Open the components folder in VS Code
5. Quickly name each component

**What you say:**
> See script section [1:00 - 2:00]

**Key moments to nail:**
- Let each composition play for at least 3-4 seconds so viewers can appreciate it
- When showing the component library, hover over each file name as you say it
- "Claude Code built all of them" - let that land

**Screen time:** 60 seconds

---

### STEP 3: Setup from Scratch (2:00 - 5:00)

**What you do:**
1. Open terminal in the empty directory
2. Run `npx create-video@latest demo-video`
3. Wait for install (speed up in post)
4. `cd demo-video && ls`
5. Open Claude Code: `claude`
6. In second tab: `npx remotion studio`
7. Show Remotion Studio opening in browser
8. Click around the default composition briefly

**Prompts to type:**
- No Claude Code prompts yet, just terminal commands

**What you say:**
> See script section [2:00 - 5:00]

**Speed up in post:** The npm install. Show the command, cut to it being done.

**Screen time:** ~3 minutes (cut to ~2 in post)

---

### STEP 4: Explain the Concept (5:00 - 7:00)

**What you do:**
1. Could use a simple whiteboard/diagram or just talk to camera
2. Show the render command: `npx remotion render src/index.ts SevenPlatforms out/seven-platforms.mp4`
3. Let it render - show the progress bar
4. Open the rendered MP4

**Key diagram (draw or use a graphic):**
```
React Components -> Compositions -> npx remotion render -> MP4
     (build once)    (combine)      (one command)        (upload anywhere)
```

**What you say:**
> See script section [5:00 - 7:00]

**Key moments to nail:**
- "Remotion is React for video" - this one line should click for people
- The three reasons (programmatic, reusable, automatable) - hold up fingers
- The terminal render is the money shot of this section

**Screen time:** ~2 minutes

---

### STEP 5: Build the Hook Overlay (7:00 - 12:00)

**What you do:**
1. In Claude Code, type the HookOverlay prompt (from script)
2. Let Claude Code work - narrate what it's doing
3. Show it reading the existing SlamText component
4. Show the new HookOverlay.tsx file being created
5. Show Root.tsx being updated
6. Refresh Remotion Studio
7. Select HookOverlay composition
8. Play it

**The prompt to type:**
```
Create a new Remotion composition called "HookOverlay" for a 9:16 YouTube Short (1080x1920).

It should:
- Display a hook phrase word by word with a slam animation
- Each word should scale up from 0 to full size with a slight bounce
- Use white text with a subtle drop shadow on a transparent background
- Hold the full phrase for 2 seconds at the end
- Total duration: 5 seconds at 30fps (150 frames)
- The hook text should be configurable as a prop

Use the same animation style as my existing SlamText component.
```

**What to narrate while Claude builds:**
- "See, it's reading my existing SlamText component first"
- "It's not starting from scratch, it's building on what I already have"
- "Spring animation, word-by-word mapping, configurable text prop, nice"

**If it looks wrong in preview:**
- DON'T cut. Say "Okay, that's not quite right. Let me fix it." and iterate with Claude Code. This is great content.

**Screen time:** ~5 minutes

---

### STEP 6: Build the Full Short (12:00 - 16:00)

**What you do:**
1. Type the ShortDemo prompt (from script)
2. Let Claude Code compose the full 30-second short
3. Point out the imports from the component library
4. Explain Sequence components and frame offsets briefly
5. Preview in Remotion Studio
6. Let the full 30 seconds play uninterrupted

**The prompt to type:**
```
Create a new composition called "ShortDemo" that's a complete YouTube Short (1080x1920, 30fps, 30 seconds).

Scene structure:
1. (0-3s) Hook text - use the WordByWord component: "Stop paying for video editors."
2. (3-6s) Problem text - use SlamText: "CapCut. Premiere. $30/month."
3. (6-9s) Solution text - use GradientReveal: "Remotion + Claude Code = Free"
4. (9-15s) Feature list - use HighlightText to show 3 bullet points one at a time:
   - "Animated text overlays"
   - "Render from terminal"
   - "Reusable components"
5. (15-20s) CountUp showing "30 seconds to render"
6. (20-25s) StrikeReplace: cross out "$360/year" and replace with "Free"
7. (25-30s) CTA using SlamText: "Link in bio"

Use a dark gradient background (#0a0a0a to #1a1a2e).
Add smooth transitions between scenes.
```

**Key moments:**
- The import statement showing all 6 components - zoom in on this
- The full 30-second playback - let it run without talking over it
- After it plays: "Six different animation styles, same system"

**Screen time:** ~4 minutes

---

### STEP 7: Render + Version Swap (16:00 - 18:00)

**What you do:**
1. Switch to terminal
2. Run the render command
3. Open the MP4
4. Then ask Claude Code to swap the text
5. Render version 2
6. Show both side by side if possible

**Commands:**
```bash
npx remotion render src/index.ts ShortDemo out/short-demo.mp4
```

**Claude Code prompt for version swap:**
```
Render the ShortDemo composition but change the hook text to "Claude Code changed everything." and the CTA to "Subscribe for more." Output to out/short-v2.mp4.
```

**Key moments:**
- The render completing in ~30 seconds (time it so you can confirm the claim)
- Opening the MP4 and it looking clean
- The version swap taking 30 seconds total
- "Same animations. Same quality. Different text. 30 seconds."

**Screen time:** ~2 minutes

---

### STEP 8: Pipeline Integration (18:00 - 20:00)

**What you do:**
1. Show the skills directory or a diagram of the 22 skills
2. Explain the /shorts to Remotion to Blotato flow
3. Show one of the more complex existing compositions as a bonus

**What you say:**
> See script section [18:00 - 20:00]

**No prompts needed here** - this is explanation + showing existing work.

**Screen time:** ~2 minutes

---

### STEP 9: Recap + CTA (20:00 - 23:00)

**What you do:**
1. Face to camera for the recap
2. List the four next steps
3. Skool CTA
4. Close

**What you say:**
> See script sections [20:00 - 22:00] and [22:00 - 23:00]

**Screen time:** ~3 minutes

---

## TIMING CHEAT SHEET

| Section | Target Time | Running Total |
|---------|------------|---------------|
| Contrarian Hook | 1:00 | 1:00 |
| Show Result First | 1:00 | 2:00 |
| Setup | 3:00 | 5:00 |
| Framework / Concept | 2:00 | 7:00 |
| Build: Hook Overlay | 5:00 | 12:00 |
| Build: Full Short | 4:00 | 16:00 |
| Render + Version Swap | 2:00 | 18:00 |
| Pipeline + Bonus | 2:00 | 20:00 |
| Recap | 2:00 | 22:00 |
| Close + CTA | 1:00 | 23:00 |
| **TOTAL** | **~23:00** | |

---

## ON-CAMERA TIPS

### While Claude Code is Building
- Narrate what it's doing: "It's reading the existing component first..."
- Point at specific lines: "See how it's using the spring animation?"
- Talk about why this matters: "This is the reusability piece"
- Don't just sit in silence

### If Something Goes Wrong
- Keep filming. Say: "Okay, that doesn't look right. Watch how easy this is to fix."
- Type the fix in Claude Code. This is BETTER content than a perfect first try.
- Bugs that get fixed live build trust with the audience.

### Energy Markers
- HIGH: Hook, showing results, preview moments, render completion
- MEDIUM: Setup, explaining concepts, showing code
- LOW (calm/focused): While Claude Code is working, brief code walkthroughs

### B-Roll / Cutaway Moments to Capture
- [ ] Terminal rendering with progress bar (satisfying)
- [ ] Remotion Studio playing a composition (loop a couple times)
- [ ] The component library folder in VS Code
- [ ] Side-by-side of two versions with different text
- [ ] The pipeline diagram or skills directory
- [ ] Close-up of the finished MP4 playing in QuickLook

### Thumbnail Notes
- Clean white background (matches AntiGravity video style)
- Remotion logo + Claude Code logo side by side
- Bold text: "Free Video Editing." or "No More Premiere."
- Tyler's face with slightly surprised/confident expression
- Reference: AntiGravity beginner video thumbnail (2,378 views)
