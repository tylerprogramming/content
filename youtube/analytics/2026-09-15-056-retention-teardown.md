# How the 056 intro was edited - handoff for another video agent

Retention on this video came back strong. This document is the method, written so another
agent can reproduce it without access to the original machine. It covers the pacing
targets, the animation inventory, the exact motion recipes, the AI-video prompts, and the
failure modes that produce a correct-looking file and a broken video.

**Source material:** two frame-synced 1920x1080 / 30fps recordings, `CAMERA` (presenter +
audio) and `SCREEN` (capture). Identical durations, so one cut plan drives both. Final
film 17:32; the intro treated here is the first 88 seconds.

**Toolchain:** ffmpeg for all compositing, GSAP + headless Chrome for motion graphics
rendered to transparent ProRes 4444 MOVs, Python for the cut plan and measurement.

---

## 1. The core principle

**Measure, do not eyeball.** Every visual claim in this edit was verified numerically
before being believed, and roughly a third of the "fixes" turned out to be measuring the
wrong thing. Specific measurements that each caught a real defect:

| question | measurement |
|---|---|
| Is the face on screen too much? | warm-pixel ratio per frame, threshold anchored on a known bare-face window |
| Is a zoom visible? | percent scale change per second; under ~8% over 0.3s it reads as nothing |
| Is it juddering? | frame-to-frame delta `d`, then `abs(diff(d))` as a ratio of `d`, excluding real cut points |
| Is a clip static? | mean frame delta; a "cutaway" at 0.8 is a still with a zoom on it |
| Did a graphic land on the word? | overlay start vs word timestamp from a transcript intersected with the cut plan |
| Is speech lost in a cut? | 50ms RMS runs above -40dB inside cut regions |

Contact sheets verify *what* rendered. Numbers verify *whether it works*. You need both.

---

## 2. Pacing targets

Derived from teardowns of two high-retention channels in the same niche. These are the
numbers to hit, measured on the delivered render:

| | target | 056 delivered |
|---|---|---|
| Face on screen, intro | ~35% | **28.4%** |
| Graphic/cutaway on screen | ~70%+ | **77.3%** |
| Longest bare talking head | under 7s | **4.0s** |
| Visual change cadence, first 30s | every ~2.4s | 3.0s mean |
| Cuts in first 50s | ~21 | 21 |
| First cut away from face | ~1.2s | 2.30s |

Before the creative pass this intro measured **55.9% face** with bare-face runs of **17.5s
and 18.0s**. Closing those two runs is the entire retention delta. It cost no re-recording
- it is all cutaways over audio that already existed.

**The structural insight:** it is not "talk, stop, play an animation." The narration runs
continuously and the *picture cuts underneath it*. The presenter is mid-sentence at every
cut. A graphic covers a line while it is being spoken, so no pause has to be engineered.

---

## 3. Animation inventory

Ten cutaway beats in 88 seconds. "Screen capture" means real recorded footage from the
session; "built" means HTML/GSAP rendered to transparent ProRes.

| At | Len | Beat | Type |
|---|---|---|---|
| 2.30 | 2.50s | Cold open: the product mid-build, the artifact it just produced visible | screen capture |
| 5.80 | 3.68s | Two product clips, rounded rect + 4px white border, one then dissolve to the other | screen capture |
| 10.30 | 5.40s | GitHub repo page, hold then punch to the star count | screen capture |
| 11.40 | 4.2s | Counter rolls to the real number, then struck through | built |
| 17.00 | 7.90s | "3 things first" roadmap cards, mosaic title reveal | built (registry block) |
| 27.35 | 5.6s | Full-frame question card, "WHAT EXACTLY IS A HARNESS?" | built |
| 36.95 | 9.2s | Diagram scene A: central node, in/out arrows, three struck capabilities | built |
| 48.84 | 4.5s | Editorial caption, dual-font size contrast | built |
| 53.14 | 17.4s | Diagram scene B: loop draws itself, five chips, ring closes, label lands | built |
| 71.04 | 6.3s | Three competitor cards on a dark bed | built |
| 79.40 | 6.5s | White card, black letters, three phrases arriving per-character | built (registry component) |

**Body treatment** (after 1:28): screen capture full-frame with the browser chrome cropped
off, webcam circle bottom-right, switching to bottom-**left** for one 9.5-minute stretch
where the app's settings modal and a reference site's sidebar both live on the right.

### Two structural choices worth copying

**The diagram is split by a deliberate presenter gap.** Scene A runs 36.95-46.13, then the
graphic clears completely for 7 seconds of camera, then scene B runs 53.14-70.49. Cutaway,
presenter, cutaway. A 30-second unbroken diagram would have been worse than two 9-second
ones with a face between them.

**The competitor beat is also split.** Cards land, clear to camera for the turn line, then
the differentiator arrives as its own separate card. Originally one continuous 14.5s block;
splitting it put a face back in the middle of the longest graphic stretch.

---

## 4. Motion recipes

### 4a. The zoom architecture - the single biggest fix

**The bug:** zooms were defined per camera clip, one linear ramp across each clip's length.
But most camera clips sit *underneath* a full-frame cutaway. Of 14 moves, **10 fired
entirely under a cutaway and were never seen**. The 4 that were visible ran at **0.9-2.2%
of scale per second**, against a threshold of roughly 27%/s for a move to register. The
viewer was watching the middle of a slow drift, never a move.

**The fix:** define zoom on the *film* timeline, not per clip.

1. Compute the windows where camera is **actually visible** = the timeline minus every
   cutaway's enable range. Here that was 21.9s of visible camera inside an 88s intro,
   across 9 windows.
2. Place at most **one move per window** longer than ~1.2s, pinned to a word. Windows under
   ~1s hold still; there is not enough time for a move to read.
3. **Hold flat between moves.** A value that is constant before and after is what makes a
   move read as a move rather than a drift.
4. Alternate direction. A repeated identical punch reads as a tic.

Result: every visible move measures **26-63%/s**.

**Ease with smoothstep, not linear.** Linear ramps start and stop abruptly at the
keyframes, which is the other half of what reads as mechanical. As an ffmpeg `zoompan`
expression, where `p` is normalised progress through the move:

```
p     = ((on - f0) / (f1 - f0))
eased = z0 + (z1 - z0) * (p*p*(3 - 2*p))
```

For a softer servo-style move, `power2.inOut`:

```
eased = if(lt(p, 0.5), 2*p*p, 1 - 2*(1-p)*(1-p))
```

**Overshoot is what makes a punch land.** `1.00 -> 1.15 -> settle 1.11` punches;
`1.00 -> 1.11` glides. Keep the overshoot short.

Generator, given keyframes in clip-local seconds, holding between them:

```python
def zexpr(keys, fps=30):
    kf = [(int(round(t*fps)), z) for t, z in keys]
    expr = f"{kf[0][1]}"
    for (f0, z0), (f1, z1) in zip(kf, kf[1:]):
        if f1 <= f0 or abs(z1-z0) < 1e-6:
            expr = f"if(lt(on,{f1}),{expr},{z1})"; continue
        p = f"((on-{f0})/{f1-f0})"
        eased = f"({p}*{p}*(3-2*{p}))"
        expr = f"if(lt(on,{f0}),{expr},if(lt(on,{f1}),{z0}+({z1}-{z0})*{eased},{z1}))"
    return expr
```

Upscale the source ~2x before `zoompan` for clean subpixel motion, and keep zoom under
about 1.3 on 1080p screen text or the upscale softens the glyphs.

### 4b. Cutaway clips: hold, move, hold

Same shape. Every cutaway originally used one linear ramp across its whole length, which
is a drift. One clip ramped *in* on its first shot and back *out* on its second, which
read as seasick.

Rebuilt so each holds, punches once (~14% over 0.34s), and holds. Measured: moving frames
went from *every* frame to 21/74 and 25/161.

**Aim the push-in at the thing that matters**, not at frame centre. Anchoring on a specific
point in 1920x1080 space, clamped so the crop never runs off the source:

```python
def xy(px, py, up=2):
    ex = f"max(0,min(iw-iw/zoom,{px*up}-(iw/zoom/2)))"
    ey = f"max(0,min(ih-ih/zoom,{py*up}-(ih/zoom/2)))"
    return ex, ey
```

If the subject sits flush to one edge of frame, pin the crop to that edge
(`x='iw-iw/zoom'`) instead of centring; a centred crop clips it at every zoom level.

### 4c. Screen-capture cutaways

- **Crop the browser chrome.** Find the boundary with a row-luma profile rather than
  guessing (here it was y=0..126), then frame the push-in so its top edge clears it. Leaving
  it in reads as a raw grab.
- **Pick the window by measuring, not by memory.** Scan the capture for spans where the
  *content* region changes every frame while the *chrome strip* does not - a chrome spike
  means a tab switch, not the app working. One cutaway that looked fine measured 0.825 mean
  frame delta, i.e. a still with a zoom on it.
- **Check the page has settled.** One clip started mid-scroll and its first second showed a
  file list rather than the header it was supposed to show.

### 4d. Rounded corners on video layers

Use a generated alpha mask, not a CSS radius, because these are video layers. One mask
clips the footage, one stroke overlays the border, so the corner is antialiased once and
identically across every clip:

```python
from PIL import Image, ImageDraw
W, H, R, B = 1400, 788, 30, 4
m = Image.new("L", (W, H), 0)
ImageDraw.Draw(m).rounded_rectangle([0, 0, W-1, H-1], radius=R, fill=255)
m.save("rr_mask.png")
f = Image.new("RGBA", (W, H), (0,0,0,0))
ImageDraw.Draw(f).rounded_rectangle([B/2, B/2, W-1-B/2, H-1-B/2],
                                    radius=R, outline=(255,255,255,255), width=B)
f.save("rr_border.png")
```

Then per clip: `crop -> scale -> alphamerge with the mask -> overlay the border`.

### 4e. Self-drawing rings and loops

Use `pathLength="1000"` on the SVG path and a `stroke-dasharray` of 1000. This normalises
the geometry so the dasharray never has to match a real perimeter. A hand-computed ellipse
perimeter here was 80 units short (3830 vs a true 3910), so 2% of the ring never drew and
the shape visibly failed to close.

Also: a bare `<ellipse>` or `<circle>` starts drawing at 3 o'clock. To draw from the top,
use an explicit path starting at 12 o'clock:

```
M 820,115 A820,385 0 1 1 820,885 A820,385 0 1 1 820,115
```

### 4f. Text on camera

- Black type needs a **solid** ground, not a scrim. Over a semi-transparent overlay the
  camera reads through and the letters lose their edges.
- A scrim under glass cards should composite to **~0.70 alpha**. A first attempt measured
  0.976 and erased the presenter entirely.
- Dual-font size contrast for editorial captions: a body face at 76px against an italic
  serif at 150px, all one colour.

---

## 5. Component adaptations

Three off-the-shelf motion components were used; everything else was hand-built HTML on the
same GSAP renderer. What matters is not the components themselves but *what had to change*
to make them land on a real edit.

### Roadmap cards - "3 things first"
- **Real mosaic, not blur.** A gaussian blur on the title reads as a fade-in. An SVG
  `feMorphology dilate` smears glyphs into blobs. A genuine mosaic is: draw the text to a
  canvas, downscale to `w/block`, scale back up with `imageSmoothingEnabled = false`. Block
  size tweens 34 -> 1 over 0.70s.
- **Fit one shared type size across all cards.** Per-card auto-fit made the shortest card
  visibly smaller than its neighbours.
- **Retimed 15.9s -> 7.90s.** Stock length held a static frame for four seconds after the
  presenter had moved on. A graphic that outlives its line is dead air.

### Per-character letter drop - the closing phrases
Per-character drop, `stagger: 0.030`, `ease: power3.out`.

The thing that made it work: **"open source [product name]" is one continuous noun phrase**
with only 0.68s between its word cues. Rendered as three separate phrases the letters
physically collided on screen. Restructured into two blocks where block one *builds* across
two lines and only then clears. The exit also changed from staggered to a single 0.16s move
- a staggered exit ran 0.47s and was still clearing when the next block arrived.

### Camera-servo law - for anchored push-ins
Worth lifting as a law rather than a component: `T = -(anchor - 50) * S`, pan clamped so the
scaled world always covers the viewport, eased `power2.inOut`, then **hold**. Ported to an
ffmpeg `zoompan` expression so it drives real screen capture instead of a mock UI.

---

## 6. Pinning every beat to a word

All 63 timeline events were verified against a word map, not placed by eye.

**Method:** transcribe the source audio, then map each word's source timestamp through the
cut plan to its position in the edited film. Keep both timelines on every word. Then for
each animation beat, assert its trigger time is within ~0.3s of the word it is supposed to
land on.

**Do not trust a stated timestamp.** Presenter-supplied marks in this edit ran **2-4
seconds long** consistently. When a stated time conflicted with a measured word time, the
word won - "bring them in as I say them" only works against measured times.

**Speech-to-text caveats that matter here:**
- It **hallucinates fluent sentences over silence**. One invented a whole sentence across a
  stretch measuring -70dB.
- It **drops words on a long-file pass**. Before concluding a reported repeat is not there,
  re-transcribe that window *alone*; if the isolated pass and the full pass disagree, trust
  the isolated one.
- Local `whisper.cpp` with a `large-v3-turbo` model transcribed 17.5 minutes in **26
  seconds** on Apple silicon. Faster and cheaper than an API round trip.

---

## 7. AI-generated video: three attempts, all rejected

Every generated clip for one beat was eventually thrown out and replaced with real screen
capture. Model: `bytedance/seedance-2`, 4s, 1080p.

**Attempt 1** - abstract glowing network mesh. Generic "AI" visual; said nothing about the
actual subject.

**Attempt 2:**

> Over-the-shoulder view of a dark monitor filling the frame, four terminal panes tiled
> side by side, each one streaming different lines of text at a different speed, cursors
> blinking out of sync. Cool blue and teal screen glow reflecting on a dark desk. Slow
> steady push in toward the centre of the screen. Cinematic, shallow depth of field, moody
> low-key lighting. No people, no hands, no faces, no logos, no readable words, no clocks,
> no hooded figures.

Rejected: a person's shoulder sits in frame until 1.16s and is still readable at the edge
after. Required both a late start and a 250px left crop to remove them.

**Attempt 3:**

> Macro shot gliding slowly across a dark curved monitor at a shallow angle, extremely
> shallow depth of field so only a narrow band of the screen is sharp and the rest falls
> into bokeh. Rows of small status indicators and progress bars fill and advance in
> sequence, tiny cyan and green dots lighting up one after another like tasks completing.
> Soft teal and deep blue glow, black room, no reflections of people. Slow lateral drift
> with a gentle push in. Cinematic, filmic grain, high contrast. No people, no hands, no
> faces, no logos, no readable words, no clocks.

Technically the best of the three - no person anywhere, full clip usable, on palette.
Still cut.

**The rule this produced:** the line was about *a specific thing existing*. Generated
b-roll can only gesture at a mood. Replaced with two real windows of the product working,
shown one at a time in a 1400x788 rounded rect with a 4px white border.

Generated video earns its place on **mood** lines ("while you sleep", "you don't need to be
an engineer"). On a line about a product, show the product.

**Always in the negative prompt:** no people, no hands, no faces, no logos, no readable
words, no clocks, no hooded figures. Clocks because diffusion renders nearly every one at
10:10. Hooded figures because an unqualified prompt on a previous video produced a
cybercrime read. Brand marks come from an icon library, never from a generative model -
asked for a specific logo, a diffusion model invents a plausible wrong one.

**Frame rate:** generated clips render at **24fps**. Dropped into a 30fps film they get
conformed by duplicating every fifth frame - measured 22 duplicates in 108 frames, the
worst judder in the intro. Rebuild the missing frames instead:

```
minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1
```

After: 0 duplicate frames. **Check `r_frame_rate` on every generated clip before wiring it
in.**

---

## 8. Audio pass

**Coughs cannot be found from the transcript** - speech-to-text runs straight through them.
Two acoustic signatures, and you need both because either alone gives false results:

1. **Spectral tilt.** More energy below 800Hz than above (speech carries more highs). A
   one-pole split at ~800Hz, then `10*log10(low_energy/high_energy)`. A cough measures
   +11 to +14dB.
2. **Voicing fraction.** Normalised autocorrelation peak in the 75-300Hz pitch band, frame
   by frame at 32ms window / 10ms hop. Voiced speech peaks strongly; a cough does not.

On one cough **tilt was useless** - a speech syllable in the same passage measured *higher*
tilt than the cough. Voicing decided it: **2% voiced frames against 14-41% for the speech
either side**. Run both tests.

Candidate criteria: 0.08-0.70s long, isolated by at least 0.18s of quiet on **both** sides.

**Speech-to-text hallucinates repetition loops.** A duplicate scan reported one phrase
repeated **ten times** across 30 seconds. It was not real: that span is 72% speech with 36
distinct runs, and its **envelope periodicity scored 0.13 - lower than ordinary speech
controls at 0.23 and 0.39**. Cutting on the transcript would have destroyed 25 seconds of
good material.

**Always test envelope periodicity before cutting a reported duplicate:** take a 20ms RMS
envelope, autocorrelate it, and look for a strong peak at the claimed repeat interval. If
the correlation is no better than a control passage, the repetition is a transcription
artifact.

Real duplicates do exist - one genuine stutter here repeated a five-word phrase three times
in 2.7 seconds. The rule when a take *is* repeated: **keep the last one.**

---

## 9. Failure modes

Every one of these produced a correct-looking file, a successful build, and a broken video.
None reported an error.

- **A GSAP tween scheduled past the composition's `data-duration` never runs.** A fade at
  14.66s in a 14.64s composition meant the graphic popped off instead of fading. Assert
  `EXIT + FADE < DUR`. The matching trap is the overlay's own `enable='between(t,AT,AT+N)'`
  in the compositing step - if N is shorter than the composition, the fade is cut off the
  same way even when the tween is correct.
- **Never slice CSS from `index(rule_start)` to `</style>`.** Removing one rule that way
  takes every rule after it. This silently deleted all the card styling from a composition;
  cards rendered as bare icons stacked in a corner. When a patch *deletes*, assert what must
  **remain**, not just what must go.
- **Shared CSS classes leak between scenes.** Resizing a `.node` class for one scene broke
  the concentric circles in another scene that used the same class.
- **A string patch that does not match fails silently.** A find/replace across four builder
  scripts missed one because its anchor differed by a single space. That script rendered to
  a scratch path and never moved the file into place; the stale graphic shipped into the
  next build. `assert new_text in source` after every patch.
- **A killed render leaves a lock file** that makes every later render of the same output
  path hang for minutes then exit 1 with nothing in stderr. Render to a scratch path and
  move the result into place.
- **`-ss <keyframe>` rounds down** and falls back to the previous keyframe. Ask for
  keyframe + 0.024 when splitting a rendered file, or you silently duplicate several
  seconds.
- **Contact sheets label frames in argument order; ffmpeg emits them in time order.** An
  unsorted timestamp list mislabels every tile. Sort before building the sheet.
- **Input-seeking a transparent ProRes with `-ss` can return empty frames.** Sample by
  frame number (`select='eq(n,N)'`) when verifying an alpha graphic, or you will conclude a
  working graphic is broken.

---

## 10. Render architecture

For an hour-length source, two approaches that work on short clips **fail**:

- One `trim` filter per clip in a single graph: every decoded frame passes through 2N
  filters. At N=360 this runs at **0.19x realtime**.
- One `select='between(t,a,b)+...'` expression: the parser dies with "Cannot allocate
  memory" past roughly 100 terms.

What works: **batches of ~30 clips, 3 concurrent ffmpeg passes**, each batch input-seeking
with `-ss` so it only decodes its own span. Intermediates are `.mov` with libx264 crf18
video and **PCM** audio, joined with the concat demuxer using `-c:v copy -c:a aac`. Video is
encoded exactly once, and keeping audio PCM until the final pass means hundreds of clip
boundaries add no AAC priming gaps.

Graphics are rendered to **transparent ProRes 4444** and overlaid inside the same batch
pass, never as a second encode of the finished film.

---

## 11. Order of operations

1. Profile the noise floor. **Never reuse the last video's threshold** - the right value
   swung 40dB between shoots here, and a wrong one silently ate 75 seconds of speech tails.
2. Silence pass, then prune slivers: drop keeps under 0.60s isolated by 3.0s of silence on
   both sides.
3. Transcribe; find retakes by reading for repeated beat structure and counting-in phrases
   ("start that over", "three, two, one"). Search the **source** transcript, not the recut
   one - the count often falls inside a gated region and comes back mangled.
4. Snap every cut boundary to the lowest-RMS 20ms frame within +/-0.45s.
5. Verify no speech was lost: 50ms RMS runs above -40dB inside cut regions. Target 0.0s.
6. Render the silence cut and review it before any creative work.
7. Creative pass: measure the face ratio and bare-face runs first, and let those numbers
   decide where cutaways go.
8. Re-measure after every change. Two of the worst defects in this edit were introduced by
   fixes to other defects.

---

## Summary: what actually moved the number

1. **Closing two bare-face runs of 17.5s and 18.0s.** Face ratio 55.9% -> 28.4%.
2. **Making zooms visible at all** - 10 of 14 were firing under cutaways and were never on
   screen.
3. **Hold-move-hold instead of continuous drift**, on both camera and cutaways.
4. **Real product footage instead of generated b-roll** on any line about a specific thing.
5. **Every beat pinned to a measured word timestamp**, never to a stated one.
6. **Re-measuring after every change**, because fixes introduce defects.
