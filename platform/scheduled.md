# Scheduled posts

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
