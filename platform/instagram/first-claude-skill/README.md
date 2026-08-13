# first-claude-skill

Instagram carousel: "Build your first skill in 2 minutes", from video 040.

```
slides.json            the deck. Rich layout, electric theme.
out/                   current render - six PNGs and the PDF
assets/
  build-hero.py        regenerates the hero card
  hero-skillmd.png     the SKILL.md window used on slide 1
caption.md             the post caption
archive/
  v1-plain.json        the data that produced what actually published
  v1-plain/            those slides, cream theme, plain layout
```

## Which version is live

`archive/v1-plain/` is what went out - cream ground, terracotta accent, plain
headline-and-bullets layout, and it prints `@tylerai_dev` rather than the
account it posts to (`tylerreedai`). Left exactly as published rather than
quietly corrected, because that is the record.

`out/` is the rebuild: electric theme, rich layout, correct handle. Not
scheduled anywhere.

## Rebuilding

```bash
python3 assets/build-hero.py      # only if the hero needs changing
THEME=electric python3 ~/.claude/skills/instagram-writer/instagram_writer.py slides.json out
```

Slide 6 is still the plain CTA layout. The two reference accounts close a
carousel differently - one with a full-bleed keyword slide, one with a recap -
so it was left rather than guessed at.

Format: `~/.claude/skills/instagram-writer/SLIDES.md`.
Styles and the evidence behind them: `~/content/BRAIN/instagram/carousel-styles.md`.
