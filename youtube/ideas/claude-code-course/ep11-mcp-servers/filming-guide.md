# Filming Guide — Claude Code Tutorial #11: MCP Servers

## Pre-Recording Checklist

- [ ] GitHub personal access token generated and ready (DO NOT show it on camera)
- [ ] Token has correct permissions: Issues (R/W), Pull Requests (R/W), Contents (R)
- [ ] If you already have the GitHub MCP set up, REMOVE it first: `claude mcp remove github`
- [ ] Have at least 2-3 repos with open issues and/or PRs (for demo content)
- [ ] Prepare a repo name for the "create issue" demo (claude-code-course or similar)
- [ ] Terminal font size: 16pt+
- [ ] Screen recording: 1920x1080, 30fps
- [ ] Browser tab open to GitHub Settings > Developer Settings > PATs
- [ ] Browser tab open to the MCP registry (https://github.com/modelcontextprotocol/servers)
- [ ] Second browser tab ready to refresh GitHub issues page (to verify created issue)

---

## Recording Playbook

### Segment 1: INTRO (Target: 1:15)

**What to say:** Deliver Hook Option 1 word-for-word

**What to show:**
1. Terminal with Claude Code creating a GitHub issue in real time (pre-recorded or live)
2. Face cam for hook delivery

**Tip:** If you want to show the issue creation in the intro before the setup, pre-record it and use it as a B-roll insert.

---

### Segment 2: WHAT IS MCP (Target: 1:45)

**What to say:** Follow script Section 1

**What to show:**
1. Diagram (prepare as a simple graphic):
```
Claude Code  <--->  MCP Server  <--->  GitHub/Notion/Slack
```
2. List of tools MCP supports (use text overlay or bullet animation)

**No commands needed — this is explanation only.**

---

### Segment 3: SETTING UP GITHUB MCP (Target: 3 min)

**What to say:** Follow script Section 2

**Exact browser flow:**
1. GitHub.com > Profile > Settings > Developer Settings > Personal Access Tokens > Fine-grained tokens
2. Generate New Token
3. Name: "Claude Code MCP"
4. Repository access: All repositories
5. Permissions: Issues (R/W), Pull Requests (R/W), Contents (Read)
6. Generate > Copy token

**CRITICAL: Blur or cover the token on screen. Use a placeholder like `ghp_xxxxxxxxxxxx` if needed.**

**Exact terminal commands:**

```bash
# The magic command — type this live
claude mcp add github -e GITHUB_TOKEN=ghp_your_token_here -- npx -y @modelcontextprotocol/server-github
```

**Pause after each part to explain:**
- `claude mcp add` — "adding an MCP server"
- `github` — "naming it github"
- `-e GITHUB_TOKEN` — "passing our token securely"
- `npx -y @modelcontextprotocol/server-github` — "the server package"

```bash
# Verify it's connected
claude mcp list
```

---

### Segment 4: LIVE DEMO (Target: 4 min)

**This is the core segment. Show real data.**

**Exact commands in order:**

```bash
# Open Claude Code
claude
```

**Prompt 1 — List repos:**
```
List my GitHub repositories
```
*Wait for response. Point out specific repos by name.*

**Prompt 2 — Create issue:**
```
Create a new issue in my claude-code-course repo titled "Add downloadable skill templates" with the description "Create a zip file of starter skill templates that viewers can download from the video description"
```
*Wait for response. Then switch to browser and refresh the repo issues page to verify.*

**Prompt 3 — Check PRs:**
```
Check the open pull requests on my [repo-name] repo and summarize what each one does
```
*Wait for response. React to the summaries.*

**Prompt 4 — Security scan:**
```
Search my repos for any file that mentions "API_KEY" — I want to make sure I haven't accidentally committed any secrets
```
*Wait for response.*

**If MCP is slow:** Some responses take 5-10 seconds. Fill dead air with narration: "It's calling the GitHub API right now..." Don't cut away — the wait builds anticipation.

**If something fails:** Say "Let me try that again" and rephrase. MCP servers occasionally timeout. Have a backup prompt ready.

---

### Segment 5: OTHER MCP SERVERS (Target: 1:30)

**What to say:** Follow script Section 4

**What to show:**
1. Keep a list graphic building on screen as you mention each server
2. Switch to browser to show the MCP registry page briefly

**No terminal commands needed.**

---

### Segment 6: WHERE TO FIND SERVERS (Target: 45 sec)

**What to say:** Follow script Section 5

**What to show:**
1. Browser: MCP registry GitHub page
2. Browser: npm search for "modelcontextprotocol"
3. Briefly show a community server repo

---

### Segment 7: MANAGING SERVERS (Target: 30 sec)

**What to say:** Follow script Section 6

**Exact commands (show but don't necessarily run all):**

```bash
claude mcp list
claude mcp remove github    # just show, don't actually remove
claude mcp list --json
```

---

### Segment 8: OUTRO (Target: 15 sec)

**What to say:** Follow script Outro

**What to show:** End screen

---

## Timing Cheat Sheet

| Segment | Target Duration | Running Total |
|---------|----------------|---------------|
| Intro | 1:15 | 1:15 |
| What Is MCP | 1:45 | 3:00 |
| GitHub MCP Setup | 3:00 | 6:00 |
| Live Demo | 4:00 | 10:00 |
| Other Servers | 1:30 | 11:30 |
| Finding Servers | 0:45 | 12:15 |
| Managing Servers | 0:30 | 12:45 |
| Outro | 0:15 | 13:00 |

**Total: ~13 minutes**

---

## Post-Recording Notes

- Double-check that no tokens or secrets are visible in any frame
- Verify the GitHub issue was actually created (include the screenshot in a pinned comment)
- If the MCP list output is hard to read, consider adding a zoom-in in post
- Include the setup command in the video description for easy copy-paste
