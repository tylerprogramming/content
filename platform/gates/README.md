# Comment gates

A gate is a keyword people comment to get something. The comment drives reach,
the DM delivers, and the link captures. One file per gate in this folder.

## The shape

Everything routes to the same place. Only the keyword and the links change.

```
comment "<KEYWORD>"
  → DM: the links, no conditions attached
    → free.tylerai.dev/<topic>/   (email = newsletter signup)
      → delivers the asset
        → invites to Skool
```

Two rules that fall out of that:

- **The keyword is specific, the destination is generic.** A gate word tied to
  the post someone just read is what makes them comment. A catch-all word
  converts worse on every post. But every gate can land in the same funnel and
  the same Skool library, and that compounding is the point.
- **The DM asks for nothing.** It hands over links. The email capture lives on
  the landing page, not in the DM, so the handover completes and the ask still
  happens. The comment has already been made by the time the DM sends, so a
  capture downstream costs completion rate, not reach.

## Why the links live here

The DM should answer the question the post raised, which means it needs the
actual repo, docs and video for *that* topic. Keeping them in one file per gate
means the DM copy is not retyped from memory each time, and a link that moves
gets fixed in one place.

**Verify links before a gate ships.** A dead link in a DM going out to hundreds
of people is expensive and invisible to you. Each gate file records when its
links were last checked.

## Adding a gate

Copy an existing file. It needs:

| Section | What it is |
|---|---|
| Keyword | The word people comment. One word, all caps, obvious from the post. |
| Promise | What the slides said they would get. Must match the CTA copy exactly. |
| Asset | Where the deliverable lives. |
| Links | Everything the DM hands over, verified. |
| DM copy | The message, ready to paste into the automation. |

Then add the keyword to the CTA slide of every post in the series, and make sure
the promise on the slide matches the promise here. A gate whose slides promise
five different things is a gate with one asset and five disappointments.

## Live gates

| Keyword | Series | Asset status |
|---|---|---|
| `EDITOR` | 5 Instagram carousels on HyperFrames + Claude Code | Manual replies for now, asset deferred until there is volume |
