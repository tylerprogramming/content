#!/usr/bin/env python3
"""Audit the-ai-agency classroom dump: every lesson, what it has, what it is missing,
and every tool/link it references. Input: aiagency-classroom-raw.json (from the box)."""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

RAW = Path(sys.argv[1])
OUT = Path(sys.argv[2])
d = json.loads(RAW.read_text())

TOOLS = {  # name: regexes (matched against title, desc, resource titles/links)
    "Claude Code": [r"claude code", r"claude\.com/claude-code"],
    "Claude (app/desktop)": [r"claude desktop", r"desktop app", r"claude\.ai"],
    "Claude Cowork": [r"cowork"],
    "Claude Routines": [r"routine"],
    "n8n": [r"\bn8n\b", r"chathub"],
    "OpenAI / ChatGPT": [r"openai", r"chatgpt", r"\bgpt\b"],
    "Gmail / Google": [r"gmail", r"google (sheets|drive|docs|cloud)", r"google oauth"],
    "Slack": [r"slack"],
    "MCP servers": [r"\bmcp\b"],
    "Apify": [r"apify"],
    "Kling (video)": [r"kling"],
    "Blotato": [r"blotato"],
    "Google Antigravity": [r"antigravity"],
    "Docker": [r"docker"],
    "VPS / Hostinger": [r"\bvps\b", r"hostinger", r"self-hosted"],
    "Supabase / database": [r"supabase", r"postgres", r"vector (db|store)", r"pinecone", r"qdrant"],
    "Telegram": [r"telegram"],
    "GitHub": [r"github"],
    "Node.js / npm": [r"\bnpm\b", r"node\.?js"],
    "Python": [r"python"],
    "ElevenLabs": [r"elevenlabs"],
    "Firecrawl": [r"firecrawl"],
    "YouTube API": [r"youtube (api|data)", r"yt api"],
    "Loom": [r"loom\.com"],
    "Ollama (local models)": [r"ollama"],
    "NASA API": [r"nasa"],
    "RSS": [r"\brss\b"],
    "Airtable": [r"airtable"],
    "Qdrant (vector DB)": [r"qdrant"],
    "Pinecone (vector DB)": [r"pinecone"],
    "Serper (search API)": [r"serper"],
    "Submagic": [r"submagic"],
    "Sora 2": [r"\bsora\b"],
    "Nano Banana (images)": [r"nano.?banana"],
    "Crawl4AI": [r"crawl4ai"],
    "Docling": [r"docling"],
    "Reddit": [r"reddit"],
    "CrewAI": [r"crewai", r"crew\b"],
    "Cloudflare": [r"cloudflare"],
    "Google Forms": [r"docs\.google\.com/forms", r"\bwebform\b"],
    "Google Sheets": [r"google sheets", r"spreadsheet", r"\.csv"],
    "Google Calendar": [r"calendar tool"],
}
# signup/setup pages: if a lesson links one of these hosts, the classroom gives members a way in
SETUP_HOSTS = {"n8n": ["n8n.io", "docs.n8n.io"], "Claude Code": ["docs.claude.com", "claude.com"], "MCP servers": ["modelcontextprotocol.io"],
               "Blotato": ["blotato.com"], "Firecrawl": ["firecrawl.dev"], "Serper (search API)": ["serper.dev"], "Qdrant (vector DB)": ["qdrant.tech"],
               "Submagic": ["submagic.co"], "Telegram": ["docs.n8n.io"], "Google Forms": ["docs.google.com"]}
# what a member needs before the lesson works, inferred from the lesson type (marked inferred in the report)
INFERRED = [(r"ai agent|rag|vector|chat|assistant|llm|analy[sz]", "LLM API key (OpenAI, Anthropic or similar)"),
            (r"gmail|google sheets|google docs|calendar|spreadsheet", "Google account + OAuth credential in n8n")]


def plain(desc):
    if not desc:
        return ""
    raw = desc[4:] if desc.startswith("[v2]") else desc
    try:
        nodes = json.loads(raw)
    except Exception:
        return desc
    out = []

    def walk(n):
        if isinstance(n, list):
            for x in n:
                walk(x)
            return
        if not isinstance(n, dict):
            return
        if n.get("type") == "text" and n.get("text"):
            out.append(n["text"])
        for m in n.get("marks") or []:
            href = (m.get("attrs") or {}).get("href")
            if href:
                out.append(f" <{href}> ")
        walk(n.get("content"))
        if n.get("type") in ("paragraph", "listItem", "heading"):
            out.append("\n")

    walk(nodes)
    return "".join(out).strip()


def resources(meta):
    r = meta.get("resources")
    if not r:
        return []
    if isinstance(r, str):
        try:
            r = json.loads(r)
        except Exception:
            return [{"title": r, "link": ""}]
    res = []
    for x in r if isinstance(r, list) else []:
        if isinstance(x, dict):
            res.append({"title": x.get("title") or x.get("file_name") or "", "link": x.get("link") or x.get("url") or ("file:" + (x.get("file_name") or x.get("fileName") or "")) })
    return res


def host(u):
    return re.sub(r"https?://(www\.)?", "", u or "").split("/")[0]


lessons = []


def visit(node_wrap, course_title, section, course_published):
    n = node_wrap["course"]
    meta = n.get("metadata") or {}
    kids = node_wrap.get("children") or []
    if n.get("unitType") == "set":
        sec_title = meta.get("title", "")
        if not kids:
            lessons.append(dict(course=course_title, section=sec_title, title="(empty section)", empty_section=True,
                                published=n.get("state") == 2 and course_published))
        for k in kids:
            visit(k, course_title, sec_title, course_published)
        return
    text = plain(meta.get("desc"))
    res = resources(meta)
    links = re.findall(r"https?://[^\s<>)\"]+", text) + [r["link"] for r in res if r["link"].startswith("http")]
    blob = " ".join([meta.get("title", ""), section or "", text] + [r["title"] + " " + r["link"] for r in res]).lower()
    tools = sorted(t for t, pats in TOOLS.items() if any(re.search(p, blob) for p in pats))
    vlink = meta.get("videoLink") or ""
    lessons.append(dict(
        course=course_title, section=section, title=meta.get("title", ""),
        published=n.get("state") == 2 and course_published, lesson_state=n.get("state"),
        video=host(vlink) if (vlink or meta.get("videoId")) else "", video_link=vlink or ("skool-hosted" if meta.get("videoId") else ""),
        video_min=round((meta.get("videoLenMs") or 0) / 60000, 1),
        text_chars=len(text), text=text[:400], resources=res, links=links, tools=tools,
    ))


courses = []
for x in d:
    c = x["course"]
    m = c["metadata"]
    pub = c.get("state") == 2
    courses.append(dict(title=m["title"], published=pub, privacy=m.get("privacy"), num=m.get("numModules"),
                        cover=bool(m.get("coverImage")), desc=plain(m.get("desc"))))
    for ch in x["children"]:
        visit(ch, m["title"], None, pub)

for L in lessons:
    if L.get("empty_section"):
        L["gaps"] = ["empty section"]
        continue
    g = []
    if not L["video"]:
        g.append("no video")
    if L["text_chars"] < 80:
        g.append("no written notes")
    if not L["resources"] and not L["links"]:
        g.append("no resources/links")
    L["gaps"] = g

json.dump(dict(courses=courses, lessons=lessons), open(OUT.with_suffix(".json"), "w"), indent=1, ensure_ascii=False)

# ---------- markdown report ----------
md = []
P = md.append
tot = [L for L in lessons if not L.get("empty_section")]
P("# The AI Agency classroom audit")
P("")
P(f"Source: live Skool classroom (read-only, via the box's Skool session). {len(courses)} courses, "
  f"{len(tot)} lessons, {sum(1 for L in lessons if L.get('empty_section'))} empty sections.")
P("")
P("## Course summary")
P("")
P("| Course | Published | Lessons | With video | With notes | With resources | Empty sections |")
P("|---|---|---|---|---|---|---|")
for c in courses:
    ls = [L for L in lessons if L["course"] == c["title"] and not L.get("empty_section")]
    es = sum(1 for L in lessons if L["course"] == c["title"] and L.get("empty_section"))
    P(f"| {c['title']} | {'yes' if c['published'] else '**DRAFT**'}{' (paid)' if c['privacy'] else ''} | {len(ls)} | "
      f"{sum(1 for L in ls if L['video'])} | {sum(1 for L in ls if L['text_chars'] >= 80)} | "
      f"{sum(1 for L in ls if L['resources'] or L['links'])} | {es} |")
P("")
P("## Tools members need, by course")
P("")
for c in courses:
    ls = [L for L in lessons if L["course"] == c["title"] and not L.get("empty_section")]
    cnt = Counter(t for L in ls for t in L["tools"])
    P(f"- **{c['title']}**: " + (", ".join(f"{t} ({n})" for t, n in cnt.most_common()) or "none named in titles/notes"))
P("")
P("## Tools and accounts members need")
P("")
P("Named in lesson titles, notes or attached files. 'Signup link in classroom' = some lesson links the tool's site or docs.")
P("I can't see inside the videos, so a setup step may be covered on camera even when nothing is written down.")
P("")
P("| Tool | Lessons | Courses | Signup link in classroom |")
P("|---|---|---|---|")
by_tool = defaultdict(list)
for L in tot:
    for t in L["tools"]:
        by_tool[t].append(L)
alllinks = [u for L in tot for u in L["links"]]
for t, ls in sorted(by_tool.items(), key=lambda kv: -len(kv[1])):
    hosts = SETUP_HOSTS.get(t)
    has = any(any(h in u for h in hosts) for u in alllinks) if hosts else False
    cs = sorted({L["course"] for L in ls})
    P(f"| {t} | {len(ls)} | {', '.join(cs)} | {'yes' if has else '**no**'} |")
P("")
P("**Inferred prerequisites** (from what the lesson builds; nothing in the classroom says how to get them):")
P("")
for pat, need in INFERRED:
    ls = [L for L in tot if re.search(pat, (L["title"] + " " + (L["section"] or "")).lower()) and L["course"] in ("Full Automation Course", "AI Agents + Automations", "Build Your First AI Automation", "Monthly Live Builds")]
    if ls:
        P(f"- **{need}**: {len(ls)} lessons, e.g. " + "; ".join(f"{L['course']} > {L['title']}" for L in ls[:4]))
P("")
P("## Every lesson")
for c in courses:
    P("")
    P(f"### {c['title']}{'' if c['published'] else ' (DRAFT)'}")
    P("")
    P("| Section | Lesson | Video | Notes | Resources | Tools | Missing |")
    P("|---|---|---|---|---|---|---|")
    for L in [L for L in lessons if L["course"] == c["title"]]:
        if L.get("empty_section"):
            P(f"| {L['section']} | (empty) | | | | | **empty section** |")
            continue
        res = "; ".join((r["title"] or host(r["link"]))[:30] for r in L["resources"]) or ", ".join(sorted({host(u) for u in L["links"]}))
        v = f"{L['video']} {L['video_min']}m" if L["video"] and L["video_min"] else L["video"]
        P(f"| {L['section'] or ''} | {L['title']} | {v or '-'} | {L['text_chars'] or '-'} | {res or '-'} | {', '.join(L['tools']) or '-'} | {', '.join(L['gaps']) or 'ok'} |")
OUT.write_text("\n".join(md) + "\n")
print(OUT, len(tot), "lessons")
