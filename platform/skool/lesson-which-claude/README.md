# Which Claude do you use? - Skool lesson deck

Two versions of the same seven beats.

```
which-claude-template.pptx   built on ~/Downloads/Template.pptx (Kourse)
build_deck_template.py       what generated it

which-claude-electric.pptx   the earlier version, electric palette, 16:9
build_deck.py                what generated it
preview-template/            approximate renders of the template one
preview-electric/            approximate renders of the electric one
```

## The template version

26.67 x 15in, the template's own size. Built by keeping the template's sample
slides, swapping the text inside their existing runs, and deleting the rest -
so the type styles, picture bullets, backgrounds and logos are the template's,
untouched.

Layouts used: `1. COVER`, `4. TITLE` x2, `5. LIST` x3, `6. SUMMARY TITLE`.
Unused: `2. AGENDA`, `3. INTRO`, `7. ACTION ITEMS`.

### Rebranded

- **Wordmark.** Kourse's is gone; `tyler ai` sits bottom-left on every slide,
  set in Avenir Next Heavy - the nearest match on this machine to the geometric
  heavy lowercase theirs used. Both the white and black versions are swapped, at
  the master as well as the layouts, so it carries everywhere.
- **Their square mark is deleted** from the cover and summary, top right. There
  was no equivalent of yours to put there. Point at a logo file and it goes back
  in that exact spot.

### Two things fixed along the way

- **Text colour.** The template left every run's colour unset, so it fell
  through to the theme, where `tx1` is `FF0000`. Every slide now states its own:
  black on the light photo grounds, white on the black list slides.
- **The font is still not installed.** The template calls for `Helvetica Now
  Var` (Text Bold / Text Black / Text Medium / Micro), which is not on this
  machine, so PowerPoint substitutes - probably Helvetica. True of the template
  as downloaded. Install the family and it snaps into place.

## The electric version

Palette from `~/social-studio/themes/electric.json`: `#F7F8FA` ground,
`#0A0A0A` ink, `#2454F0` accent. Fonts are Arial Black / Helvetica Neue / Menlo,
all present on any Mac, so it opens the same anywhere.

Rebuild either: `~/social-studio/.venv/bin/python build_deck_template.py`
