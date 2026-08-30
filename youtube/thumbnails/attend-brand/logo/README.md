# Attend — logo assets

Hand-built SVG (real vector, not AI-generated), exported to PNG via headless Chrome.

## Files

| File | Use |
|---|---|
| `favicon.svg` | Browser tab. Opaque cream rounded square so it reads on any tab colour. |
| `favicon-{16,32,48,180,192,512}.png` | Fallbacks + `apple-touch-icon` (180) + PWA manifest (192, 512). |
| `mark.svg` / `mark-{256,512,1024}.png` | Bell alone, transparent background. App icons, social avatars, watermarks. |
| `lockup.svg` / `lockup-{236,472}.png` | Bell + "Attend" wordmark, black text. Light backgrounds. |
| `lockup-dark.svg` / `lockup-dark-{236,472}.png` | Same, white text and lifted sky-blue dome. Dark backgrounds. |

## Palette

| Role | Hex |
|---|---|
| Dome (navy) | `#2A3B8F` |
| Base (vermilion) | `#CE3E2E` |
| Band (tan gold) | `#E0A860` |
| Plunger / dark-mode dome (sky) | `#5BAFE8` |
| Icon ground (cream) | `#FAF7F0` |
| Wordmark | `#0A0A0A` light · `#FFFFFF` dark |

## Web install

Drop the files in `/public` and add to `<head>`:

```html
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="/favicon-180.png">
<link rel="manifest" href="/site.webmanifest">
```

`site.webmanifest`:

```json
{
  "name": "Attend",
  "short_name": "Attend",
  "icons": [
    { "src": "/favicon-192.png", "sizes": "192x192", "type": "image/png" },
    { "src": "/favicon-512.png", "sizes": "512x512", "type": "image/png" }
  ],
  "theme_color": "#2A3B8F",
  "background_color": "#FAF7F0",
  "display": "standalone"
}
```

## Site header

Prefer inline SVG mark + real HTML text over the lockup image — sharper, selectable,
accessible, and it recolours for dark mode without a second asset.

```html
<a class="brand" href="/">
  <img src="/mark.svg" alt="" width="28" height="28">
  <span>Attend</span>
</a>
```

```css
.brand { display: inline-flex; align-items: center; gap: .5rem;
         font-weight: 700; font-size: 1.35rem; letter-spacing: -.02em;
         color: #0A0A0A; text-decoration: none; }
@media (prefers-color-scheme: dark) { .brand { color: #FFF; } }
```

Use `lockup*.png` only where you can't inject HTML — email signatures, slide decks,
third-party profile headers.

## Caveats

- **The wordmark is live text, not outlines.** It renders with Inter, falling back to the
  system sans. On a machine without Inter the letterforms shift slightly. For a locked
  master logo file, open `lockup.svg` in Figma and convert the text to outlines.
- Minimum mark size is ~16px. Below that the gold band merges into the base.
- Clear space: keep at least half the bell's width empty on all sides.
