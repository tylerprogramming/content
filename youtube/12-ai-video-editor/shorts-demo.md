# Shorts Demo Segment - HeyGen short edited with Hyperframes

> Add-on segment for video #12. Tyler takes a HeyGen avatar short he created, edits it with
> Hyperframes (dynamic captions), and shows the result. Slots in after DEMO 2 (captions) or as
> its own beat near the full-workflow recap.
>
> **VERIFIED REAL (2026-06-30):** `~/hyperframes-projects` exists, Node 24, ffmpeg 7.1.1, all 3
> caption presets live at `~/.claude/hyperframes-presets/`. Every command below is real and runs.
> Tyler explicitly wants to show what you can ACTUALLY do - no fake commands.

---

## What's real vs the draft script's placeholder names

The main `script.md` demos use simplified command names (`hyperframes silence`, `hyperframes
caption --style bold`). Those are placeholders. The REAL working commands are:

- **Silence cut / auto-edit** = `autoedit.py` (the `/hyperframes-edit` skill). Portrait-safe.
- **Dynamic captions** = the caption-preset workflow (`/hyperframes-presets`): 3 presets -
  `red-sticker` (TikTok red pill), `anton-pop` (YouTube bold), `ali-abdaal` (calm cream).

Both are Tyler's own scripts built on open-source Hyperframes + ffmpeg + Whisper. Honest framing
holds: open-source does the heavy lifting, Tyler wired the silence layer + caption presets on top.

A HeyGen short is already tight (AI avatar, no dead air), so "editing it with Hyperframes" =
**burning on dynamic word-by-word captions**. That's the showable capability.

---

## How Tyler films it - TALK TO CLAUDE CODE (no raw Python on camera)

On camera Tyler is just talking to Claude Code in plain English. Claude Code invokes the
skill, which runs the real Hyperframes / ffmpeg / Whisper / preset scripts under the hood.
Still 100% honest - the real tools do the real work - it just matches how Tyler actually works.

### What Tyler TYPES into Claude Code (natural language)

1. **Add TikTok captions:**
   > "Take this HeyGen short at ~/Downloads/heygen-short.mp4 and add TikTok-style captions to it."

   Claude Code: scaffolds a hyperframes project, transcribes with Whisper, applies the
   `red-sticker` preset, renders the captioned vertical short. Tyler narrates while it runs.

2. **Show the other two styles (the money beat):**
   > "Now give me the bold YouTube version."   (anton-pop)
   > "And the calm cream tutorial version."     (ali-abdaal)

   Same short, three completely different caption looks, all from plain requests.

3. **(Optional) tighten dead air first, only if the short has pauses:**
   > "First cut any dead air out of this, then caption it."

   Claude Code runs the silence auto-edit, shows the cut list, then captions the cleaned clip.

### What Claude Code actually runs under the hood (for reference - NOT typed on camera)

```bash
# captions:
npx hyperframes init heygen-short --video ~/Downloads/heygen-short.mp4 --model small.en --non-interactive --skip-skills
python3 ~/.claude/hyperframes-presets/lib/extract_words.py ~/hyperframes-projects/heygen-short
python3 ~/.claude/hyperframes-presets/red-sticker.py ~/hyperframes-projects/heygen-short   # or anton-pop.py / ali-abdaal.py
npx hyperframes render -o out/captioned.mp4 -q standard -f 30
# optional silence cut:
python3 ~/.claude/skills/hyperframes-edit/scripts/autoedit.py analyze <video> --project <dir>
python3 ~/.claude/skills/hyperframes-edit/scripts/autoedit.py render <dir> --engine ffmpeg --xfade 0.12
```

These are real, verified commands - but Tyler does NOT type them. He asks Claude Code, and
this is what Claude Code executes. Show the Claude Code terminal doing the work as the b-roll.

---

## How to film the segment (~90-120s on screen)

1. **Show the raw HeyGen short** (5s) - clean avatar, no captions. "I made this in HeyGen. Now I
   want platform-ready captions on it without opening an editor."
2. **Run steps 1-3 live** - narrate: init transcribes it with Whisper, extract_words flattens the
   transcript, the preset renders the caption layer with Hyperframes. Real terminal, no cuts.
3. **`preview`** - show the karaoke captions popping word by word in the studio. This is the wow.
4. **The 3-style swap** - one command each, three completely different looks on the same short.
   "Pick your platform's vibe, re-render, done."
5. **Show the final `captioned.mp4`** playing. "HeyGen made the talking head, Hyperframes made it
   post-ready. Two AI tools, zero timeline."

**Honest line to land:** "Hyperframes is open-source and does the rendering. The caption presets
are scripts I built on top with Claude Code. That's the pattern this whole video is about."

**Corrections note:** `lib/corrections.json` auto-fixes Whisper mishears (cloud->Claude,
appify->Apify, claude.ai slash code->claude.ai/code) before captions render - so the on-screen
text is clean. Mention it if a correction visibly fires; otherwise it just works.
