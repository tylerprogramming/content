# Episode 4: Examples & Exact Prompts

## Feature Prompt 1: Visitor Counter

```
Add a visitor counter to LinkLaunch. Display it at the bottom of the page as small muted text that says "X visits". Use localStorage to track the count — increment it by 1 every time the page loads. Style it to match the dark theme with the secondary text color.
```

---

## Feature Prompt 2: Slide-In Animations

```
Add slide-in animations to LinkLaunch. Each link button and section should slide in from the left when the page loads. Use CSS @keyframes — define a slideInLeft animation that goes from opacity 0 + translateX(-30px) to opacity 1 + translateX(0). Stagger each element by 100ms using animation-delay so they cascade in one after another. The animation should be 0.5s ease-out.
```

---

## Feature Prompt 3: Contact Form

```
Add a "Get In Touch" contact form section below the latest video section. Include fields for:
- Name (text input)
- Email (email input)
- Message (textarea, 4 rows)
- Submit button with the accent color

Style everything to match the dark theme — dark input backgrounds (#1a1a2e), subtle borders, white text. When the form is submitted, prevent the default behavior, save the submission to localStorage as an array of entries, show a success message, and clear the form. No backend needed.
```

---

## The /compact Command

After adding all three features above, the context window will be getting full. Run this:

```
/compact focus on LinkLaunch's file structure and CLAUDE.md rules
```

What this does:
- Summarizes the entire conversation into a short context block
- Frees up most of the context window for new prompts
- Keeps the key details you told it to focus on
- Claude still remembers your project — just not every word of the old conversation

---

## How to Know When to Compact

Watch for these signs:
- Claude starts forgetting rules from your CLAUDE.md
- Responses get slower or less accurate
- You've been going for 15+ prompts in one session
- Claude asks you about things you already told it

Rule of thumb: compact every 10-15 prompts, or whenever you're switching to a new area of the project.
