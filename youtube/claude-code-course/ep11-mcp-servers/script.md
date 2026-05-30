# Claude Code Tutorial #11 - MCP Servers: Connect Claude to ANY Tool

## Full Script

---

### INTRO (0:00 - 1:15) ~1.25 min

What if you could say "create a GitHub issue for this bug" — and Claude just does it? No browser. No clicking. No copy-pasting. Just done.

[SHOW: Terminal — Claude Code creating a GitHub issue in real time]

That's MCP. Model Context Protocol. It's how you connect Claude Code to your actual tools — GitHub, Notion, Slack, databases, whatever you use.

In the next thirteen minutes, I'm going to set up a GitHub MCP server from scratch. And show you Claude interacting with real repos, real issues, real pull requests.

[NOTE: Title card — "Claude Code Tutorial #11 - MCP Servers"]

Let's go.

---

### SECTION 1: WHAT IS MCP? (1:15 - 3:00) ~1.75 min

MCP stands for Model Context Protocol. That sounds technical. It's not.

Here's the simple version. MCP is a standard way for Claude to talk to other software.

[SHOW: Simple diagram on screen]
```
Claude Code  <--->  MCP Server  <--->  Your Tool
                    (bridge)          (GitHub, Notion, etc.)
```

Think of it like a translator. Claude speaks Claude. GitHub speaks GitHub. The MCP server sits in the middle and translates between them.

Without MCP, Claude is limited to what's in your terminal. Your files. Your code. That's it.

With MCP, Claude can reach out and interact with the tools you actually use every day.

[SHOW: List appearing on screen one by one]
- GitHub — repos, issues, PRs, code search
- Notion — pages, databases, notes
- Slack — messages, channels
- Figma — designs, components
- Databases — Postgres, SQLite, MongoDB
- And dozens more

The best part? Setting up an MCP server is shockingly easy. Let me show you.

---

### SECTION 2: SETTING UP GITHUB MCP (3:00 - 6:00) ~3 min

We're going to set up the GitHub MCP server. I'm picking GitHub because most of you have GitHub accounts, and the results are immediately visible.

[SHOW: Terminal, clean screen]

Before we start, you need a GitHub personal access token. Let me show you how to get one.

[SHOW: Browser — GitHub Settings]

Go to GitHub. Click your profile picture. Settings. Then scroll down to Developer Settings. Personal Access Tokens. Fine-grained tokens.

[SHOW: GitHub token creation page]

Click "Generate new token." Give it a name — something like "Claude Code MCP."

For permissions, you want:
- Repository access: All repositories (or select specific ones)
- Permissions: Issues (read/write), Pull Requests (read/write), Contents (read)

[SHOW: Selecting permissions, clicking Generate]

Copy that token. You'll need it in a second.

[NOTE: Emphasize — "Don't share this token. Don't put it in a video. Treat it like a password."]

Now, back in the terminal. Here's the magic command.

[SHOW: Terminal — typing the command]

```bash
claude mcp add github -e GITHUB_TOKEN=ghp_your_token_here -- npx -y @modelcontextprotocol/server-github
```

Let me break this down.

`claude mcp add` — this tells Claude Code you're adding an MCP server.

`github` — that's the name we're giving this server. You can call it whatever you want.

`-e GITHUB_TOKEN` — this passes your token as an environment variable. The server needs this to authenticate with GitHub.

`npx -y @modelcontextprotocol/server-github` — this is the actual server package. npx downloads and runs it automatically.

[SHOW: Command executing, success message]

That's it. One command. The GitHub MCP server is now connected to Claude Code.

Let's verify it's working.

```bash
claude mcp list
```

[SHOW: Output showing the github server listed with its tools]

There it is. You can see all the tools the GitHub server provides — create_issue, list_repos, get_pull_request, search_code, and more.

---

### SECTION 3: DEMO — GITHUB THROUGH CLAUDE (6:00 - 10:00) ~4 min

Now the fun part. Let's actually use it.

[SHOW: Opening Claude Code]

```bash
claude
```

Let's start simple.

[SHOW: Typing prompt]

> List my GitHub repositories

[SHOW: Claude fetching repos via MCP, displaying a list]

Look at that. Claude just called the GitHub API through MCP and pulled back my actual repos. Names, descriptions, stars, last updated. All real data.

[NOTE: Point at specific repos — "There's my Claude Code course repo, there's my personal site..."]

Let's try something more useful.

[SHOW: Typing prompt]

> Create a new issue in my claude-code-course repo titled "Add downloadable skill templates" with the description "Create a zip file of starter skill templates that viewers can download from the video description"

[SHOW: Claude creating the issue via MCP]

[SHOW: Browser — refreshing the GitHub repo issues page to confirm the issue exists]

It's real. There it is on GitHub. Created from my terminal through Claude. No browser, no clicking around.

Let's go further.

[SHOW: Typing prompt]

> Check the open pull requests on my personal site repo and summarize what each one does

[SHOW: Claude fetching PRs, summarizing each one with clear descriptions]

This is incredible for code review. Claude reads the PR diff, understands the changes, and gives you a summary. In seconds.

One more.

[SHOW: Typing prompt]

> Search my repos for any file that mentions "API_KEY" — I want to make sure I haven't accidentally committed any secrets

[SHOW: Claude searching across repos via MCP]

Security scan across all your repos from one sentence. That's the power of MCP.

---

### SECTION 4: OTHER POPULAR MCP SERVERS (10:00 - 11:30) ~1.5 min

GitHub is just the beginning. Let me quickly run through some other popular MCP servers.

[SHOW: List on screen, adding each one as you mention it]

**Notion MCP** — Read and write Notion pages and databases. Great if you use Notion for project management. Claude can update your docs, search your notes, create new pages.

**Slack MCP** — Send messages, read channels, search conversations. Imagine telling Claude "summarize what the team discussed in the engineering channel today."

**Postgres / SQLite MCP** — Connect Claude directly to your database. Ask questions in plain English, get SQL queries and results back. "How many users signed up last week?" — Claude writes the query, runs it, gives you the answer.

**Figma MCP** — Access your designs. Claude can read component properties, understand your design system, even help generate code that matches your designs.

**File System MCP** — Give Claude access to specific folders outside your project. Useful for cross-project work.

[SHOW: Browser — MCP server registry]

You can find all of these and more at the official MCP server registry. I'll link it in the description.

The setup process is the same for all of them. `claude mcp add`, give it a name, pass any required tokens, and point it at the server package.

---

### SECTION 5: WHERE TO FIND MCP SERVERS (11:30 - 12:15) ~45 sec

Quick practical note. Where do you actually find MCP servers?

[SHOW: Browser tabs]

First — the official registry. This is curated by Anthropic. Quality servers, well-documented.

Second — GitHub. Search for "MCP server" plus whatever tool you want. There are community-built servers for almost everything.

Third — npm. Many MCP servers are published as npm packages. That's why we use `npx` to run them — it handles the download automatically.

[SHOW: npm search for "modelcontextprotocol"]

Pro tip — when evaluating a community MCP server, check the GitHub stars, recent commits, and issues. You want servers that are actively maintained.

---

### SECTION 6: MANAGING MCP SERVERS (12:15 - 12:45) ~30 sec

A few quick management commands.

[SHOW: Terminal]

```bash
# List all your MCP servers
claude mcp list

# Remove a server
claude mcp remove github

# Check server status
claude mcp list --json
```

You can also configure MCP servers in your settings file at `~/.claude/settings.json`. But the CLI commands are easier for most people.

---

### OUTRO (12:45 - 13:00) ~15 sec

MCP servers turn Claude Code from a local tool into a connected platform. Your GitHub, your databases, your team tools — all accessible through natural conversation.

Next episode — sub-agents. That's where Claude starts delegating work to specialized AI instances. It's wild. Subscribe so you don't miss it.

[SHOW: End screen with subscribe button and next episode preview]

[NOTE: End screen — 20 seconds]
