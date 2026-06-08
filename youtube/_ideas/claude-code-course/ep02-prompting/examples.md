# Episode 2: Examples & Exact Prompts

## The VAGUE Prompt (bad example)

```
Add some social media stuff to my page.
```

Why this fails:
- "Social media stuff" could mean icons, links, feeds, share buttons, embeds, follower counts...
- No specifics on placement, style, or behavior
- Claude has to guess what you want

---

## The SPECIFIC Prompt (good example)

```
Add two new sections to LinkLaunch below the existing link buttons:

1. Social Stats Bar — a horizontal row showing follower/subscriber counts for each platform. Use these numbers:
   - YouTube: 12.4K subscribers
   - Twitter: 8.2K followers
   - GitHub: 340 repos
   - Instagram: 5.1K followers
   Display them in a single row with the platform name above the number. Use the same dark theme styling.

2. Latest Video Section — an embedded YouTube video section with:
   - A section title "Latest Video"
   - An embedded YouTube iframe (use this URL: https://www.youtube.com/embed/dQw4w9WgXcQ as a placeholder)
   - Video title text below: "Building a SaaS in 24 Hours with AI"
   - Keep it centered and responsive
```

---

## The FOLLOW-UP Iteration Prompt

```
Two fixes:

1. The social stats bar — on mobile, make it a 2x2 grid instead of a single row. Each stat should have equal width.

2. The YouTube embed — give the thumbnail rounded corners (12px border radius) and add a subtle box shadow that matches the dark theme.
```

---

## Key Takeaway

Specific prompts give you what you want on the first try. Vague prompts waste time going back and forth. Always include:
- **What** you want (the feature)
- **Where** it goes (placement on the page)
- **How** it should look (colors, sizes, layout)
- **Content** (actual text, numbers, URLs)
