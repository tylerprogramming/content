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

## The exact on-camera command sequence (LIVE)

```bash
# You have your HeyGen short, e.g. ~/Downloads/heygen-short.mp4

# 1. Scaffold a hyperframes project from the short (auto-transcribes with Whisper)
cd ~/hyperframes-projects
npx hyperframes init heygen-short --video ~/Downloads/heygen-short.mp4 \
  --model small.en --non-interactive --skip-skills

# 2. Convert Whisper transcript -> flat words.json
python3 ~/.claude/hyperframes-presets/lib/extract_words.py ~/hyperframes-projects/heygen-short

# 3. Apply the TikTok-style caption preset (red pill, karaoke pop)
python3 ~/.claude/hyperframes-presets/red-sticker.py ~/hyperframes-projects/heygen-short

# 4. (great B-roll) preview it live in the studio - hot-reloads
cd ~/hyperframes-projects/heygen-short
npx hyperframes preview

# 5. Render the captioned vertical short
npx hyperframes render -o out/captioned.mp4 -q standard -f 30
```

### The money beat - 3 styles, same short, one filename swap

```bash
python3 ~/.claude/hyperframes-presets/red-sticker.py ~/hyperframes-projects/heygen-short   # TikTok red pill
python3 ~/.claude/hyperframes-presets/anton-pop.py   ~/hyperframes-projects/heygen-short   # YouTube bold yellow
python3 ~/.claude/hyperframes-presets/ali-abdaal.py  ~/hyperframes-projects/heygen-short   # calm cream
# re-render after each:  npx hyperframes render -o out/<style>.mp4 -q standard -f 30
```

### Optional: tighten dead air first (only if your short has pauses)

```bash
python3 ~/.claude/skills/hyperframes-edit/scripts/autoedit.py analyze \
  ~/Downloads/heygen-short.mp4 --project ~/hyperframes-projects/heygen-short-cut
# review cutlist.md, then:
python3 ~/.claude/skills/hyperframes-edit/scripts/autoedit.py render \
  ~/hyperframes-projects/heygen-short-cut --engine ffmpeg --xfade 0.12
# then run the caption-preset flow above on cleaned.mp4
```

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
