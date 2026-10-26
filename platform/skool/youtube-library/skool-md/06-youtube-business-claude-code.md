## In this lesson
You'll run the nine skills I use for every video, in order: research what's working, transcribe a winning video, build the full package (titles, hooks, script), make thumbnails, fix the SEO, plan Shorts, write social posts, add chapters, and upload.
By the end you can take one idea from research to a scheduled upload, all inside Claude Code.

## Good to know
- Time: about an hour for your first video package, plus a one-time 10 minute Google setup if you want to upload from Claude Code.
- Cost: Claude Code needs a paid Claude plan. Thumbnails run on Kie.ai, paid but cheap per image. Three thumbnails cost me $0.27. Transcribing uses the OpenAI Whisper API, paid per minute of audio.
- Level: Beginner. You type commands and answer questions. The skills do the rest.
- Honest caveat: the skills plan, package and publish. You still film and edit the video yourself.

## What you need
- Claude Code (paid Claude plan): https://claude.com/claude-code
- My free skills (GitHub repo): https://github.com/tylerprogramming/claude-skills
- yt-dlp, free, the tool the research and transcribe skills use to read YouTube: https://github.com/yt-dlp/yt-dlp
- OpenAI API key for Whisper transcription, paid (sign-in page): https://platform.openai.com/api-keys
- Kie.ai account and API key for thumbnails, paid per image: https://kie.ai
- ffmpeg, free, for the chapters skill: https://ffmpeg.org
- Optional, for uploading: a Google Cloud project with the YouTube Data API v3: https://console.cloud.google.com

**1. Install the skills (0:29)**
Everything you need is in the Google Doc and the GitHub repo. In your terminal:

```
git clone https://github.com/tylerprogramming/claude-skills.git ~/projects/tyler-skills
cd ~/projects/tyler-skills && ./setup.sh
```

Then open Claude Code and paste:

> Look at ~/projects/tyler-skills and import the yt-search, yt-deep-research, transcribe, yt-package, yt-seo, yt-thumbnail, yt-shorts, social-copy, yt-chapters and yt-upload skills into my ~/.claude/skills, then tell me what setup each one needs.

A skill is just a text file that tells Claude how to do one job the same way every time. Some come with a Python file that does the heavy lifting.

**2. Research what's working (1:16)**
/yt-search claude code

It searches YouTube for the last 30 days, pulls 50 videos, ranks the top 15, splits long form from Shorts, and downloads their thumbnails. You get the top videos, title and thumbnail patterns, and video ideas, saved on your computer. It takes a few minutes. Want a longer window? Ask for 90 days instead.
/yt-deep-research does the search and transcribes the top videos for you in one go. Use it once you know the process.

**3. Transcribe a winning video (4:02)**
Pick the top video from your research. I typed:

```
/transcribe Nate's video
```

You don't need the slash. "Transcribe the number one video" works too, or paste a YouTube link. It saves the transcript and tells you why the video worked: the structure, the hook, the calls to action.

**4. Build the full video package (6:16)**
/yt-package <the transcript file it just saved>

It does its own web research, then asks you questions: your angle, which of your own work to demo, who it's for. Answer them. This step takes the longest. It creates a folder with titles, hooks, the script, the description, tags, an analysis, and reference thumbnails. The script is a guide, not something to read word for word.

**5. Make thumbnails with Kie.ai (10:58)**
/yt-thumbnail use this video's reference thumbnail to create three more

Nano Banana Pro is my favorite model on Kie.ai. The skill used a photo of my face as a reference. It made three concepts for $0.27. Treat them as ideas you can edit, not final art.

**6. Fix the title and description (13:12)**
/yt-seo on this video package

It checks title patterns from your research and the web, gives you a title scorecard with options to A/B test, and updates the titles, description and tags in your package.

**7. Plan Shorts and social posts (14:47)**
/yt-shorts get ideas from this video package

I got five Short ideas: two talking head, two screen recording, one mix. One Short can go to TikTok, YouTube Shorts, Instagram Reels, Facebook and Bluesky.
After you record, run /social-copy on the video. It writes posts for X, LinkedIn, Instagram, YouTube Community and Skool.

**8. Film, edit, then add real chapters (17:00)**
Filming and editing are the human part. When the final video is done:

```
/yt-chapters /path/to/final-video.mp4
```

It pulls the audio, transcribes your video, and puts real timestamps in your package description.

**9. Upload and schedule (18:50)**
/yt-upload uses the YouTube Data API v3 to upload and schedule. It needs a one-time setup first:
- In Google Cloud Console, create a project and enable the YouTube Data API v3.
- Set up the OAuth consent screen and add your own email as a test user.
- Create an OAuth client (Desktop app), download the JSON, and save it as credentials.json in your home folder.
- Run /yt-upload once. A browser opens, you approve, and token.json is created. After that it's one command.

## Files and links
- Free skills and newsletter: https://free.tylerai.dev/youtube/
- The skills repo: https://github.com/tylerprogramming/claude-skills
- The YouTube Workflow doc (the full flow and the upload setup): https://docs.google.com/document/d/1JgGYBcrfcDhXowmYt6CRRkZATggf695ZL9umDb1ffFE/edit
- Kie.ai: https://kie.ai
- Free community: https://www.skool.com/the-ai-agency

## If it breaks
- /thumbnail does nothing: I renamed it. Use /yt-thumbnail.
- Research or transcribing seems stuck: it takes a few minutes. Let it finish.
- The chapters in your package description are wrong: they're placeholders until you run /yt-chapters on the finished video.
- /yt-search fails: check yt-dlp is installed with: yt-dlp --version
- Thumbnails fail with a 401 error: your KIE_API_KEY is missing or wrong. It goes in ~/.claude/.env.
- /yt-upload won't connect: you skipped the one-time Google setup in step 9.

## Next
Build an AI agent in 5 steps with Claude Code
