# Knowledge Base: Cold Email Copy Bank

## Outbound Systems — Copy Module

This is the full copy bank. Use these verbatim when a student asks for copy. Do not paraphrase. Do not insert hyphens.

The core promise framework that every email should express somewhere:

> *I help [avatar] achieve [outcome] in [timeframe] by [USP]. If it doesn't work [risk reversal].*

Don't be too hard on risk reversal — some students don't need it. But avatar + outcome + timeframe + USP is non-negotiable.

Every email should also include **proof** — a case study, a number, a named result.

---

## Subject Line Vault

These are the proven subject lines. When a student asks about subject lines, recommend from this list.

- Quick question
- Question for {firstName}
- Quick question for {firstName}
- {outcome} for {firstName}
- Can you handle more work?
- Question about {company name}?
- This is a cold email
- RE: Question for {firstName}
- {firstName}?

### Notes on subject line choice
- Short and conversational outperforms clever.
- "This is a cold email" is counterintuitive but works because it's honest, pattern-interrupting, and disarming.
- "RE:" implies prior conversation and gets opens, but use sparingly.
- Subject lines like `{firstName}?` or `{outcome} for {firstName}` use enrichment fields — these need your sending tool to merge data correctly.

---

## Personalized First Lines

The first line of the email should reference something specific about the lead, pulled from enrichment data. Use these templates.

**Top recommendation: LinkedIn summary.** Pull their LinkedIn summary into Clay and have Clay write the first line from it. That's the highest-signal personalization source.

### First line templates

- *I notice you recently started hiring for {title}*
- *I noticed you recently took over as {title} and wanted to reach out.*
- *I just read your linkedin post about {summary of what their post was about}.*
- *I wanted to reach out because I noticed you guys are based out of {company location}.*
- *I was doing some research and it appears that people often compare you to {competitor}.*
- *Do you follow {competitor}? They come up when I search for you guys online.*
- *I was searching for the top {niche} in {location} and came across {companyName}'s website, really impressed by your ratings online.*
- *You came up on my suggested people on Linkedin and I noticed you work in the {niche} space, thought i'd reach out.*
- *I notice your based out of {location} I was speaking to a friend of mine in the area and they said {niche} companies are struggling with {problem you solve}. Is that the same for {company name}?*

### Ranking of first-line sources by signal strength

1. **LinkedIn summary** (highest signal — use Clay)
2. **Recent LinkedIn post** (very specific, shows real research)
3. **Recent job change / promotion** (timely, relevant)
4. **Location + competitor / problem** (geographic + peer proof)
5. **Company ratings / website** (lowest signal but fine for some niches)

---

## Email Body Copy — The 4 Templates

### Email 1 (The Full Pitch)

```
Hey {firstName}

I'm just reaching out because I was checking out {company name} and I noticed you {personalization}

I work specifically with {niche} to help them get to {outcome} in {timeframe} by {USP}

I've worked with companies in similar niches and have been able to {proof}

I'm not even sure if something like this would be of interest to you but thought I'd reach out.

Happy to send more information over to you or even show you some examples of companies we've helped.

Just drop me a reply to this email and I'll shoot that information over to you.

Thanks
{name}
```

**When to use:** Primary send. This is the workhorse email. Full promise + proof + low-friction ask.

### Email 2 (The Guarantee Pitch)

```
Hey {firstName}

{personalized first line}

Just reaching out because we help {niche} in {location} get an extra {offer} each month & if it doesn't work you don't pay.

We just helped {case study}, a business in {location} get {result}.

Can I send a quick video explaining how it works?

{signature}
```

**When to use:** When you have a guarantee / risk reversal. Leads with the guarantee, pairs it with a named case study, CTA is "can I send a video" (low-friction, points to the Evergreen VSL).

### Email 3 (The Short Promise)

```
Hey {firstName}

{personalized first line}

I can help you get {outcome} in {timeframe} or you don't pay.

Not sure if this is something that you'd even be interested in but happy to send more info.

Let me know

{signature}
```

**When to use:** When you want to test a shorter variant. Pure promise, pure guarantee, minimal fluff. Good for follow-up batches or testing against Email 1.

### Email 4 (The Case Study Open)

```
Hey {firstName}

{personalized first line}

I recently helped {case study} accomplish {outcome} in {timeframe} and I think we could do something similar for you.

I'm not even sure if getting {outcome} is a priority for you guys right now but happy to send over more info if you want.

Let me know

{signature}
```

**When to use:** When you have a strong, named case study. Leads with social proof. Good for niches where prospects are skeptical of claims but respect peer results.

---

## Follow-Up Sequence

Follow-ups are not optional. People's inboxes are crowded. Most conversions come from follow-up 2 or 3, not the first send.

### Follow-Up 1

```
Hey {firstName}

is this worth a quick chat? No pressure, just can't help but feel you'd be a great fit :)
```

### Follow-Up 1 (when they've received the VSL)

```
Hey {firstName}! Were you able to check out the quick video?

Worth a quick chat?
```

### Follow-Up 2 (the bump)

```
Just bumping this back up in case it got lost.
```

### Follow-Up 3 (the priority check)

```
Hey {firstName}, is {outcome} still a priority? Let me know your thoughts on the video.
```

### Later Follow-Ups

Memes. Gifs. More bumps. Keep it casual, keep it light, keep the thread alive.

---

## Booking Link Message

When a lead asks to book a call with you, send this as a **separate email** in reply:

```
Awesome. Feel free to book below.

{Booking link}

Looking forward to talking with you.
```

Short. No fluff. The booking link is the entire message's purpose.

---

## Evergreen VSL Message

The message you send along with the Evergreen VSL Loom to a positive-reply prospect:

```
Awesome. Here's a quick video breaking down some more info.

{Video link}

Let me know if it's worth a quick chat.
```

---

## Copy Writing Rules

1. **No hyphens.** Use commas or periods. Hyphens get flagged as AI-generated and hurt deliverability.
2. **Short sentences.** One thought per line when possible.
3. **Low pressure language.** "Not even sure if this would be of interest" > "You need this."
4. **Always include proof.** Case study, number, named client.
5. **Always include the promise** — avatar + outcome + timeframe + USP.
6. **Match the template structure.** Don't invent new structures. Miles already tested these.

---

## The Fields Your Enrichment Needs to Populate

For this copy bank to work, your enrichment stack needs to provide per-lead:

- `{firstName}`
- `{company name}` / `{companyName}`
- `{personalization}` or `{personalized first line}` — generated from LinkedIn summary or other signal
- `{title}` — if using the hiring/role-change variants
- `{competitor}` — if using competitor variants
- `{location}` / `{company location}` — if using location variants
- `{niche}` — your ICP category
- `{outcome}` — the result you deliver
- `{timeframe}` — how long it takes
- `{USP}` — what makes you different
- `{case study}` — a named client + their result
- `{signature}` — your email signature

Whatever fields your copy uses, your enrichment step must populate them before send.

---

## Common Copy Mistakes to Call Out

When reviewing student copy:

- **No promise statement** → "Go back to the copy bank. Your email has no clear promise. Follow the *I help [avatar] achieve [outcome] in [timeframe] by [USP]* framework."
- **No proof** → "There's no proof in this email. Add a case study or a number. Without proof, nobody replies."
- **Hyphens in the copy** → "Strip every hyphen. They hurt deliverability. Use commas or periods."
- **Too long** → "Cut it in half. The 4 templates are the length they are for a reason."
- **Pressure language** → "Soften the CTA. Match the *'not even sure if this would be of interest'* tone. Pressure kills replies on cold."
- **No personalized first line** → "Add a personalized first line. Start with LinkedIn summary via Clay."
