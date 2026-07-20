# How to Set Up yt-upload (Get Your token.json)

This is the one-time setup that lets Claude Code upload and schedule videos to YOUR YouTube channel through the official YouTube Data API. It takes about 10 minutes, and you only do it once. After this, you upload with a single command.

This is the exact thing people get stuck on, so follow it top to bottom.

## What you're actually doing
YouTube won't let a script touch your channel unless YOU approve it once. So the flow is:
1. Turn on the YouTube API in a Google project.
2. Create an "OAuth client" - basically an ID card for your script.
3. Run the tool once - a browser opens, you click approve, and it saves a `token.json`.
4. From then on, the tool reuses that token. Done.

You need two files on your machine when you're finished:
- `~/credentials.json` - the OAuth client (the ID card). You download this from Google.
- `~/.claude/skills/yt-upload/token.json` - the approval token. This gets created automatically on first run.

---

## Step 1 - Open Google Cloud Console
Go to https://console.cloud.google.com and sign in with the Google account that owns your YouTube channel.

Create a project (or reuse one): top bar, project dropdown, "New Project," name it something like "youtube-tools," Create.

## Step 2 - Enable the YouTube Data API v3
- In the search bar type "YouTube Data API v3" and open it.
- Click Enable.
- (This is also where your daily quota lives. Default is 10,000 units/day. One upload costs 1,600, so that's ~6 uploads a day, plenty.)

## Step 3 - Set up the OAuth consent screen
- Left menu: APIs and Services, then OAuth consent screen.
- User type: External. Create.
- App name: anything (e.g. "yt-upload"). User support email: your email. Developer contact: your email. Save and continue.
- Scopes: you can skip adding them here, click Save and continue.
- Test users: click Add Users and add YOUR OWN Google email (the channel owner). Save. This matters - if you skip it you'll get a "not verified / access blocked" wall.
- Back to dashboard.

## Step 4 - Create the OAuth client (credentials.json)
- Left menu: APIs and Services, then Credentials.
- Click Create Credentials, then OAuth client ID.
- Application type: Desktop app. Name it, Create.
- A popup shows your client. Click Download JSON.
- Rename that file to `credentials.json` and move it to your home folder so it lives at `~/credentials.json`.

That's the "ID card" done. You never have to look at it again.

## Step 5 - First run (this creates token.json)
Run any yt-upload command once. The simplest is listing your uploads:

```bash
python3 ~/.claude/skills/yt-upload/yt.py list
```

What happens:
- A browser window opens.
- Google asks you to pick your account and approve two permissions: upload videos, and manage your videos.
- If it warns "Google hasn't verified this app," click Advanced, then "Go to yt-upload (unsafe)." This is safe - it's YOUR app talking to YOUR channel. The warning is just because you didn't pay Google to verify a personal tool.
- Approve. The browser says you can close the tab.
- The tool saves `~/.claude/skills/yt-upload/token.json` automatically.

You're done. Every future upload just works, no browser.

## Step 6 - Upload a video
```bash
python3 ~/.claude/skills/yt-upload/yt.py upload \
  --file "my-video.mp4" \
  --title "My Title" \
  --description-file description.txt \
  --tags-file tags.txt \
  --category 28 \
  --thumbnail thumb.jpg \
  --publish-at "2026-07-15T13:00:00-04:00"
```
- `--publish-at` schedules it as private-until-that-time (ISO 8601, `-04:00` = US Eastern during EDT).
- Leave `--publish-at` off to upload as private or public right now.
- `--category 28` is Science and Technology.

---

## Troubleshooting
- **"missing OAuth client" / can't find credentials:** `~/credentials.json` isn't there. Re-download from Step 4.
- **"access blocked / app not verified":** you didn't add yourself as a Test User in Step 3. Add your email, try again.
- **`invalid_grant: Token has been expired or revoked`:** delete `token.json` and re-run Step 5 to re-approve.
- **Quota exceeded:** you hit the daily 10,000 units. Wait 24 hours, or request a quota bump in the Cloud Console.
- **Custom thumbnail rejected:** your channel needs a verified phone number (one-time, in YouTube settings).

## The mental model to keep
- `credentials.json` = who the app is (you download it once).
- `token.json` = your approval (created once, refreshes itself).
- Delete `token.json` any time you want to re-approve from scratch. Nothing else breaks.
