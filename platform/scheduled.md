# Scheduled posts

## Instagram week · 2026-07-27 to 08-01

One carousel a day at 16:00Z (noon ET). The EDITOR series in order, then the
ROUTINES set opens on Saturday. Account `tylerreedai` (Blotato id 12074).

| day | carousel | gate | status |
|---|---|---|---|
| Mon 07-27 | Five Commands · EDITOR 1/5 | EDITOR | **scheduled** `929fca28` (silent) |
| Tue 07-28 | Nine Workflows · EDITOR 2/5 | EDITOR | **scheduled** `2869468` (silent, slides corrected 07-26) |
| Wed 07-29 | The Check Gate · EDITOR 3/5 | EDITOR | **manual** — Tyler posts natively, with music |
| Thu 07-30 | The Limits · EDITOR 4/5 | EDITOR | **manual** — Tyler posts natively, with music |
| Fri 07-31 | My Mistakes · EDITOR 5/5 | EDITOR | undecided |
| Sat 08-01 | 5AM Routine · ROUTINES 1/4 | ROUTINES | undecided |

Mon and Tue go out through Blotato and will be silent. Wed and Thu are posted
by hand so they can carry music, which Blotato cannot attach to a carousel.
That split is deliberate: it also gives a rough read on whether music matters,
though two posts either side is not a real test.

**These will be silent.** Blotato has no music parameter for Instagram
carousels, only `audioName` for reels, and music cannot be added after
publishing. If music matters on these, they have to be posted natively from
the phone instead.

**Six straight days of asking for a comment.** Deliberate, since the five
EDITOR carousels are one series with one deliverable, but worth watching: if
engagement drops across the week, the gate is the first thing to vary.

### Uploading is the slow part

Blotato's `create_presigned_upload_url` takes one filename per call and has no
batch variant, so each carousel is 6-7 round trips before it can be scheduled.
With a `BLOTATO_API_KEY` in `~/.claude/.env` the same endpoint can be scripted
in a single pass instead.


## TikTok · 2026-07-27 18:00Z (2pm ET)

**Loop vs Schedule · ROUTINES 2/4** — the first TikTok slideshow test.

| | |
|---|---|
| Account | `@codewithtyler` (Blotato id 13354) |
| Submission | `fdf66421-f5d6-4d36-91e7-86682a4c7abf` |
| Status | scheduled |
| Media | 6 JPG, 1080x1920, uploaded to Blotato storage |
| Privacy | `PUBLIC_TO_EVERYONE` |
| Music | `autoAddMusic: true` — TikTok picks a licensed track |
| Cover | slide 1 (`imageCoverIndex: 0`) |
| Comments | enabled |
| Gate | none. Ungated on purpose, so a test post is not asking anything. |

### Choices worth knowing

**`isAiGenerated: true`.** Slide 1's background is an AI-generated photo of a
realistic person. TikTok requires that disclosure, and under-declaring it is
the kind of thing that costs an account rather than a post. The upside of
hiding it is nothing.

**`isBrandedContent` and `isYourBrand` both false.** This is organic
educational content with no product CTA. Setting either would trigger a
branded-content label that does not apply.

**18:00Z.** The researched accounts post between 17:00Z and 18:45Z
(`@nateherkai` at 17:02, sabrina at 18:43). This sits in that band. It is a
starting slot, not a finding.

### What this is actually testing

1. **Does Blotato produce a real TikTok slideshow** from multiple `mediaUrls`?
   Their docs list Photo Slideshow as a supported type but never document the
   multi-image call.
2. **Is 1080x1920 accepted?** The spec says "up to 1080px" without naming the
   dimension. Width is fine; the height is the open question.

If it fails, both answers are in the failure message. If it posts, judge it on
saves and shares, not comments.
