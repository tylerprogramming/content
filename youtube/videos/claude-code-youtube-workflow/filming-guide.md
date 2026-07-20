# Filming Guide: I Automated My Entire YouTube Workflow with Claude Code

---

## Pre-Recording Setup

### Environment Cleanup
- [ ] Close all unnecessary apps and browser tabs
- [ ] Clean up desktop — nothing distracting visible
- [ ] Set terminal font size large enough to read on camera (16-18pt)
- [ ] Use a clean terminal theme with good contrast (dark background, bright text)
- [ ] Clear terminal history so it looks fresh

### Files to Have Ready
- [ ] The `/yt-search` report already generated at `~/content/research/2026-02-24-claude-code.md` — this is your demo artifact
- [ ] A transcript already generated at `~/content/transcripts/` for the demo (run `/transcribe` on a top video from your search results)
- [ ] The video package for THIS video at `~/content/youtube/claude-code-youtube-workflow/` — this is the meta reveal
- [ ] Have VS Code or your editor open with `~/.claude/skills/` visible in the sidebar

### Test Runs
- [ ] Run `/yt-search test` once to make sure yt-dlp is working and no errors pop up
- [ ] Run `/transcribe` on a short video to confirm yt-dlp and Whisper are working
- [ ] Verify all output files exist and look clean

---

## Filming Steps

### Step 1: Record the Hook [0:00 - 0:30]

**What you do:** Talking head to camera. Terminal visible behind you or on a second screen.

**What you say:**
> "This video you're watching right now? I planned it using four commands in my terminal."

**On-screen:** Flash the terminal showing `/yt-search`, `/transcribe`, `/yt`, `/thumbnail` outputs. Pre-record these clips and cut them in during editing. 2 seconds each.

**Then:** Cut to the actual `script.md` file for THIS video briefly on screen. The viewer should see it but not have time to read it all.

---

### Step 2: Record the Problem Section [0:30 - 1:30]

**What you do:** Talking head. Optional: show a browser with 10+ tabs open to illustrate the "old way."

**What you say:** Describe the old research workflow — YouTube searching, TikTok scrolling, Google Docs outlining.

**On-screen:** If you want b-roll, quickly open a browser, search YouTube, click around, open a blank Google Doc. Capture 10-15 seconds of this chaos for the montage.

---

### Step 3: Demo /yt-search [1:30 - 4:00]

**What you do:** Screen recording of terminal.

**Exact commands to type:**
```bash
/yt-search claude code
```

**What happens next:** The skill runs `search_youtube.py`, fetches 50 results from YouTube, filters to 30 days, and outputs a report.

**While waiting (~60 seconds):** Talk about what it's doing.
> "It's hitting YouTube through yt-dlp, pulling the 50 most recent results, filtering to the last 30 days, and sorting by views."

**After it finishes:**
1. Open the report: show `~/content/research/2026-02-24-claude-code.md` in your editor
2. Scroll through the summary table slowly — let the viewer read the top 5-6 entries
3. Point out specific data: Nick Saraev at 266K, Lenny's Podcast at 215K
4. Call out the gap: "Nobody's showing Claude Code for content creation"

**Tip:** If yt-dlp takes too long, you can use the pre-generated report and just show the command being typed + the output file opening. Cut out the wait in editing.

---

### Step 4: Demo /transcribe + Analysis Conversation [4:00 - 7:30]

**What you do:** Screen recording of terminal.

**Part 1: Get the transcript**

**Exact commands to type:**
```bash
/transcribe https://youtube.com/watch?v=VIDEO_ID
```
(Use a real video URL from your /yt-search results — pick one of the top performers)

**What happens next:** The skill downloads the audio via yt-dlp, transcribes with Whisper, and saves to `~/content/transcripts/`.

**While waiting (~1-2 minutes):** Talk about why transcripts matter.
> "I can see what's getting views, but I want to know exactly what they're saying."

**After it finishes:**
1. Open the transcript at `~/content/transcripts/transcript_VIDEO_ID.txt`
2. Quick scroll through — show it's complete

**Part 2: Have the conversation (THIS IS THE PAYOFF)**

**What you do:** Start a conversation with Claude in the terminal. Paste the transcript and have a real discussion.

**Conversation flow to demo:**
1. Paste transcript and ask: "Break down the structure of this video. What sections does it have and how long is each?"
2. Claude responds with structural analysis
3. Follow up: "What hooks are they using? What's working?"
4. Claude responds with hook analysis
5. Then pivot to YOUR video: "I want to make a video about [your topic]. Based on this, what angles are they missing? How should I structure mine differently?"
6. Claude gives you concrete suggestions

**Key lines to say on camera:**
> "I don't just read the transcript — I have a conversation about it."
> "What are they NOT covering that I should?"
> "Now I'm not just copying what works — I'm improving on it."

**Tip:** Pre-run the transcription so it's ready. The conversation is the star — do this part live or semi-live. Let the viewer see real back-and-forth. This shows Claude Code isn't just running commands, it's a thinking partner.

---

### Step 5: Demo /yt — The Big One [7:30 - 11:00]

**What you do:** Screen recording of terminal + editor.

**Exact commands to type:**
```bash
/yt I Automated My Entire YouTube Workflow with Claude Code - A 10-15 min fast-paced practical tutorial showing how I use Claude Code custom skills to run my YouTube content creation pipeline from the terminal. Skills: /yt-search, /tiktok, /yt. Unique angle: nobody else is showing Claude Code for content creation. Target: YouTube creators, Claude Code users.
```

**What happens next:**
1. Claude does web research (you'll see WebSearch calls in the terminal)
2. Claude asks you Q&A questions — answer them on camera
3. Claude generates all the files

**The Q&A answers to give on camera:**
- Angle: "I'm showing my actual workflow — the skills I use every day to plan videos"
- Demos: "/yt-search, /transcribe, /yt, and /thumbnail — the full pipeline"
- Audience: "Creators who use Claude Code, or want to"
- Anything to avoid: "Don't want it to be too technical — keep it practical"

**After it generates:**
1. Open `~/content/youtube/claude-code-youtube-workflow/` in your editor
2. Show the file list: titles.md, hooks.md, script.md, description.md, filming-guide.md, analysis.md
3. Open titles.md — scroll through the 5 options
4. Open hooks.md — read the first hook out loud or show it
5. Open script.md — scroll through section headers
6. Quick flash of description.md and filming-guide.md

**THE META REVEAL:**
- Put script.md side-by-side with yourself on camera
- Point to the line you're reading
- Say: "This is the script you're hearing right now. This video is the output."
- Pause for a beat. Let it land.

**Tip:** The /yt skill takes 3-5 minutes including web research. You can either speed it up in editing or pre-run it and show a sped-up version. The Q&A part is worth showing in real-time though — it demonstrates the interactive nature.

---

### Step 6: Demo /thumbnail [11:00 - 13:00]

**What you do:** Screen recording of terminal.

**Exact commands to type:**
```bash
/thumbnail I Automated My Entire YouTube Workflow with Claude Code
```

**What happens next:**
1. The skill asks you for settings (aspect ratio, resolution, count) — use defaults or pick 16:9, 2K, 3 variants
2. It crafts a thumbnail prompt based on your video concept
3. Shows you the prompt for approval
4. Generates thumbnails via the Kie.ai API (~30 seconds each)
5. Downloads them to `~/content/youtube/thumbnails/`

**While waiting (~30 seconds per image):** Talk about what it's doing.
> "It's using the Kie.ai Nano Banana Pro API to generate thumbnail options. Each one takes about 30 seconds."

**After it finishes:**
1. Open `~/content/youtube/thumbnails/` and show the generated images
2. Show them side by side — point out the different compositions
3. If you have time, show a remix: pick one thumbnail and run it again with a different prompt as a reference

**The second meta moment:**
> "The thumbnail you clicked on to get to this video? Made with this skill."

**Tip:** Pre-generate the thumbnails so you have them ready. Show the command running, cut out the wait, then show the results. The remix is the wow factor — show one image going in and a different version coming out.

---

### Step 7: The Pipeline Overview [13:00 - 14:00]

**What you do:** Talking head or screen recording with a simple graphic.

**On-screen option 1:** Create a simple text slide:
```
/yt-search  →  /transcribe  →  /yt  →  /thumbnail
  Research      Analyze       Package    Thumbnail
```

**On-screen option 2:** Show the four output folders side-by-side in your editor:
- `~/content/research/`
- `~/content/transcripts/`
- `~/content/youtube/claude-code-youtube-workflow/`
- `~/content/youtube/thumbnails/`

**What you say:** Recap the pipeline. Four commands. Research, analysis, finished plan, and a thumbnail. All from the terminal.

**Quick plug:** Mention the skills video. Flash the thumbnail briefly.

---

### Step 8: Why This Matters [14:00 - 15:30]

**What you do:** Talking head. Genuine, slightly slower pacing.

**On-screen:** Show `~/.claude/skills/` folder in your editor with all 11+ skill folders visible. The visual of accumulated skills drives the "compounds over time" point.

**What you say:** This is the "real talk" section. Not selling — explaining. Claude Code isn't just for coding. The system compounds.

---

### Step 9: CTA + End Screen [15:30 - 16:00]

**What you do:** Talking head, high energy.

**What you say:** Subscribe, check the skills video, links in description.

**On-screen:** End screen with subscribe button. Quick montage callback — terminal running /yt-search, /transcribe, /yt, /thumbnail — same clips from the hook.

---

## Timing Cheat Sheet

| Section | Target Duration | Running Total |
|---------|----------------|---------------|
| Hook | 0:30 | 0:30 |
| The Problem | 1:00 | 1:30 |
| /yt-search demo | 2:30 | 4:00 |
| /transcribe + conversation | 3:30 | 7:30 |
| /yt demo + meta reveal | 3:30 | 11:00 |
| /thumbnail demo | 2:00 | 13:00 |
| Pipeline overview | 1:00 | 14:00 |
| Why this matters | 1:30 | 15:30 |
| CTA | 0:30 | 16:00 |

**Total target: ~16 minutes**

---

## On-Camera Tips

- **Energy:** Start high (hook), settle into conversational (demos), peak again (meta reveal), genuine (why it matters), high (CTA)
- **Pacing:** The demos should feel fast but not rushed. Let the output sit on screen long enough for viewers to read key data points.
- **Errors:** If a skill fails or throws a warning during recording, keep it in. Fix it on camera. Authenticity > perfection.
- **Terminal font:** Make sure text is readable at YouTube's default resolution. Test by watching a 30-second clip on your phone before committing to a full recording session.
- **The meta reveal:** This is the moment of the video. Practice the delivery. Pause after "This video is the output." Don't immediately move on — give the viewer a second to process it.
- **Cut points:** Each skill demo has a natural wait time (yt-dlp searching, Apify polling, /yt researching). These are your edit points. Record the command, cut out the wait, show the result.
