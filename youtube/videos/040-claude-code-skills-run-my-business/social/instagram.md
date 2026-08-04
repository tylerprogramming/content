# Instagram - 040: 17 Claude Code Skills That Actually Run My Business

Format: carousel, 4:5 (1080x1350), 6 slides. Tyler adds the CTA slide separately with Kie.ai.
Render through the carousel maker (see "How to render" at the bottom). Nothing has been generated yet.

---

## Carousel 1: "17 text files run my business"

**Framework:** `hormozi` (contrarian, proof-driven)

**Slide 1 (Cover)**
Headline: 17 text files run my business
Subtext: No code. Here is what is actually inside.

**Slide 2**
Headline: A skill is just a text file
Body: One folder, one file called SKILL.md. The top says when to use it. The rest is plain English instructions.

**Slide 3**
Headline: You write it once
Body: Nothing to install, nothing to compile. Write down the task once and it becomes a command you can run forever.

**Slide 4**
Headline: Some run while I sleep
Body: A few are on a schedule. They gather the comments and draft the email before I sit down.

**Slide 5**
Headline: Everything defaults to draft
Body: Nothing goes out without me reading it. You get the speed without handing over your judgment.

**Slide 6 (Summary)**
Headline: Did it twice? Make it a file.
Body: You stop being the person doing the task and start being the person reviewing the result.

---

### Caption

I run my content business out of one folder of text files.

Swipe to see all 6.

Not an app, not a script, not a dashboard. A Claude Code skill is a folder with one markdown file in it. The top of the file says when to use it, and the rest is just the instructions you would give someone you were training.

That is genuinely the whole thing. No install, no code to compile.

So here is what mine do. One researches what I should make next. One drafts the writing. One handles comments. One runs the admin side of my community. A few of them fire on a schedule while I am asleep.

They all default to draft mode though, so nothing gets posted without me reading it first. And they are not always right. I would say they get me about 80 percent of the way and I do the last bit.

If you are looking for a first AI workflow to build, do not overthink it. Pick the task you did twice this week. Write the instructions down in plain English. That is your first skill.

Save this for later when you build yours.

Send it to someone who keeps redoing the same task.

#claudecode #claudeai #ai #claudecodetips #aiautomation

---

## Carousel 2: "Build your first Claude Code skill"

**Framework:** `educational` (step-by-step)

**Slide 1 (Cover)**
Headline: Build your first skill in 2 minutes
Subtext: No code. This is the whole process.

**Slide 2**
Headline: 1. Pick the task you did twice
Body: Not the biggest task. The most repeated one. That is the one worth writing down.

**Slide 3**
Headline: 2. Make a folder and a file
Body: A folder inside your skills directory, with one file in it called SKILL.md.

**Slide 4**
Headline: 3. Say when to use it
Body: One or two lines at the top, in plain English. This is how Claude knows to reach for it.

**Slide 5**
Headline: 4. Write the instructions
Body: The same thing you would tell a person you were training. Steps, rules, what good looks like.

**Slide 6 (Summary)**
Headline: Save it. It is a command now.
Body: Then fix the one line that annoyed you next time. Mine got good by being used, not by being planned.

---

### Caption

Everyone asks how to start with Claude Code automation. This is the actual first step, and it takes about two minutes.

Swipe for all 5 steps.

A skill is a folder with one markdown file inside it. That is it. The top of the file tells Claude when to use it, and everything underneath is plain English instructions, the same way you would train a new assistant.

There is no app to install and no code to write. Which is the part most people do not believe until they see the file.

The mistake I see is picking something too ambitious for the first one. Do not build your whole workflow on day one. Pick the small thing you already did twice this week, write it down, and use it. Then fix the one line that annoyed you.

Every skill running my business now started as a rough text file I improved a little at a time.

I have been an engineer for years and none of this needed that. If you can describe a task clearly, you can build one.

Save this for when you sit down to write yours.

Send it to someone who has been meaning to try Claude Code.

#claudecode #claudeai #ai #claudecodetips #aiautomation

---

## How to render

Carousel maker must be running on port 3010.

```bash
curl -s -X POST http://localhost:3010/api/bulk-generate \
  -H 'Content-Type: application/json' \
  -d '{
    "items": [
      {"topic": "17 Claude Code text-file skills that run a real content business, no code", "frameworkId": "hormozi", "platform": "instagram"},
      {"topic": "Build your first Claude Code skill in 2 minutes, step by step, no code", "frameworkId": "educational", "platform": "instagram"}
    ]
  }'
```

Then open http://localhost:5175 to add backgrounds and export. Exports land in
`~/content/platform/carousels/<slug>/<slug>.pdf`, which is what Blotato posts.

Or use the batch button in the carousel maker header and paste the two topics.

---

## Checks

- Captions are 190 and 200 words
- Swipe CTA in the first three lines on both
- Keyword-rich: "Claude Code skill", "Claude Code automation", "AI workflow"
- Dual save plus share CTA on both
- Exactly 5 hashtags, at the very end
- No em dashes
