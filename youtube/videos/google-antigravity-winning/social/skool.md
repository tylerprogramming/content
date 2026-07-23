# Skool - Google is Winning With Antigravity

**Video:** https://www.youtube.com/watch?v=B5eDktBzXMg
**Posted manually by Tyler** (Skool is not in Blotato).
**Cadence:** 3 posts, spaced 3-5 days apart. Goal on Skool is COMMENTS, not reach.

| # | Angle | CTA |
|---|---|---|
| 1 | The drop (video is up, what's in it) | video link |
| 2 | The tactic (try this today) | none, ends on a question |
| 3 | The discussion (real question) | no link, pure engagement |

---

## POST 1 - The drop

I did not expect to be impressed by a Google tool this week, but here we are.

I built a full agentic workflow in Google Antigravity, and I want to walk you through it because it is more doable than it sounds.

An agentic workflow is a simple idea. You describe the outcome you want, and the AI works out the steps, writes the code, and runs it. The goal I gave it was to pull videos from a list of YouTube channels, score them, and save a summary into a Google Sheet.

I opened a folder and added one markdown file. No code in it. It just says how the project should be structured, what runs in what order, and what to do when something errors. Then I typed one line, instantiate based on the agents markdown file, and let it plan.

The planning is what got me. It laid out the whole build before touching anything. Which APIs it needed, what scripts it would write, how it would verify each step. I could read the thinking the whole way through.

Setup was not zero. I had to enable the YouTube Data and Sheets APIs in Google Cloud, make a service account, and drop the credentials in the project. That is usually where people quit, and it walked me through it.

Then I ran it. It broke on a sheet permission, told me exactly what to fix, and finished after I shared the sheet. Real videos pulled, scored, and summarized, and I wrote none of the code.

I dropped the agent markdown file and the exact prompt in here so you can copy it. What would you have your first agentic workflow do?

https://www.youtube.com/watch?v=B5eDktBzXMg

---

## POST 2 - The tactic (try this today)

Here is the thing I took out of that build, and it applies no matter which tool you use.

Everybody is trying to write a better prompt. The bigger lever is the file you write before the prompt.

My actual request was one sentence. What came back was a whole project, plan and scripts and checks. That sentence was not doing the work. A markdown file sitting in the folder was.

There are three things in that file and none of them are code.

The goal, in plain English, the way I would explain the project to someone new. The order, what runs first, what depends on what, and where the outputs go. And what to do when something breaks, which for me is diagnose it and tell me plainly what is wrong instead of just stopping.

That is it. About a page of text.

It works for the same reason a good brief works with a person. Vague instructions plus a capable worker still gets you a guess. And you only write it once, so everything you ask for after that comes back already shaped the way you want.

Try this today. Pick one thing you ask AI for repeatedly, and write the page instead of the paragraph.

What is the first rule about how your work gets done that you would put in that file?

---

## POST 3 - The discussion (no link)

I want to ask you all something real, because I keep going back and forth on it myself.

Building that Antigravity workflow, there was a moment that stuck with me. It reached for an API key when a simpler library would have skipped half the setup. I happened to know that. If I had not, I would have just followed along and done the extra work for no reason.

It was still right. It just was not the best route.

So the thing I have been chewing on is how much you need to know to safely let one of these build for you. Enough to spot a longer path? Enough to catch a bad choice before you are three steps in?

Because the pitch is always that you do not need to know anything. In my experience knowing a little is what makes the whole thing work.

Here is my question.

Where have you let AI build something and only later realized it took the long way around? What did you have to know to catch it?

Drop it below. And if a few of you name the same kind of build, I will put one together properly and share the whole thing in here so you have a version that does not take the long route.
