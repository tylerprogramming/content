# Episode 11: MCP Servers — Examples

## Project Context

We're connecting LinkLaunch to GitHub using MCP (Model Context Protocol). This lets Claude create repos, push code, manage issues, and more — all from the chat.

---

## 1. Initialize Git

First, set up git in the LinkLaunch project:

```
Initialize a git repo for LinkLaunch and make the first commit with all current files
```

---

## 2. Add the GitHub MCP Server

Run this command in your terminal (not inside Claude Code):

```bash
claude mcp add github -e GITHUB_TOKEN -- npx -y @modelcontextprotocol/server-github
```

### Prerequisites

- You need a GitHub Personal Access Token set as `GITHUB_TOKEN` in your environment
- To create one: GitHub > Settings > Developer Settings > Personal Access Tokens > Generate New Token
- Required scopes: `repo`, `read:org`

### Verify it's connected

After restarting Claude Code, you can verify the MCP server is active:

```
/mcp
```

You should see `github` listed as a connected server.

---

## 3. Create a GitHub Repository

```
Create a new GitHub repository called linklaunch and push my code to it
```

### What Claude does

- Uses the GitHub MCP to create the repo under your account
- Sets the remote origin
- Pushes all committed code to the new repo

---

## 4. Create an Issue

```
Create a GitHub issue titled 'Add analytics tracking' with a description about tracking link clicks and page views
```

### What Claude does

- Uses the GitHub MCP to create an issue on the `linklaunch` repo
- Sets the title and description
- Returns the issue number and URL

---

## 5. List Open Issues

```
Show me all open issues on the LinkLaunch repo
```

### What Claude does

- Queries the GitHub MCP for all open issues
- Displays them with issue numbers, titles, and labels

---

## MCP Setup Reference

### Add a server

```bash
claude mcp add <name> -e ENV_VAR -- <command>
```

### List connected servers

```bash
claude mcp list
```

### Remove a server

```bash
claude mcp remove <name>
```

---

## Key Takeaways

| Concept | Details |
|---------|---------|
| MCP | Model Context Protocol — lets Claude talk to external services |
| Setup | `claude mcp add` to register a server |
| GitHub MCP | Create repos, push code, manage issues, PRs, and more |
| Environment | Pass secrets via `-e` flag (e.g., `-e GITHUB_TOKEN`) |

> MCP servers extend Claude's reach beyond your local filesystem. GitHub is just one example — there are MCP servers for databases, APIs, Slack, and more.
