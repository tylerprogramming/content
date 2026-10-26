#!/usr/bin/env python3
"""Lesson .txt -> printable HTML guide (then PDF via the browser). One file per lesson.

usage: python3 make_guides.py   -> guides/<slug>-guide.html
"""
import html, re, sys
from pathlib import Path
import markdown

ROOT = Path(__file__).parent
OUT = ROOT / "guides"; OUT.mkdir(exist_ok=True)
import importlib.util
spec = importlib.util.spec_from_file_location("tsm", ROOT / "to_skool_md.py"); tsm = importlib.util.module_from_spec(spec); spec.loader.exec_module(tsm)

CSS = """
@page { size: Letter; margin: 0.7in 0.75in; }
body { font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif; color: #1a1a1a; font-size: 11.5pt; line-height: 1.5; }
.top { border-left: 10px solid #E62117; padding: 4px 0 4px 18px; margin-bottom: 18px; }
.eb { font-size: 9pt; font-weight: 700; letter-spacing: .18em; color: #E62117; }
h1 { font-size: 21pt; line-height: 1.15; margin: 4px 0 6px; }
.vid { font-size: 10pt; color: #555; }
.vid a { color: #E62117; }
h2 { font-size: 13pt; margin: 20px 0 6px; padding-bottom: 3px; border-bottom: 2px solid #eee; }
p { margin: 6px 0; }
ul { margin: 4px 0 8px; padding-left: 20px; }
li { margin: 2px 0; }
strong { color: #000; }
pre { background: #f4f4f5; border: 1px solid #e4e4e7; border-radius: 6px; padding: 9px 12px; font-size: 9.5pt;
      white-space: pre-wrap; word-break: break-all; page-break-inside: avoid; margin: 6px 0 10px; }
code { font-family: Menlo, Consolas, monospace; }
blockquote { margin: 6px 0 10px; padding: 8px 12px; border-left: 4px solid #FFE03D; background: #fffbea; font-style: italic; }
a { color: #1d4ed8; word-break: break-all; }
.foot { margin-top: 26px; font-size: 9pt; color: #777; border-top: 1px solid #eee; padding-top: 8px; }
"""

def build(txt: Path):
    raw = txt.read_text()
    lines = raw.splitlines()
    title = lines[0].strip()
    vid = next((l for l in lines[:4] if l.startswith("Video: ")), "")
    m = re.search(r"(https://\S+)\s*\((.*?)\)", vid)
    url, length = (m.group(1), m.group(2)) if m else ("", "")
    md = tsm.to_md(raw)
    # wrap stray command lines (not already fenced) as code, e.g. "python3 ..." after a non-colon line
    out_lines, fence = [], False
    for ln in md.splitlines():
        if ln.strip() == "```":
            fence = not fence; out_lines.append(ln); continue
        if not fence and tsm.CMD.match(ln.strip()) and not ln.startswith(("> ", "- ")):
            out_lines += ["```", ln.strip(), "```"]
        else:
            out_lines.append(ln)
    md = "\n".join(out_lines).replace("```\n```\n", "")
    # autolink bare URLs OUTSIDE fenced code only, and give step headings their own paragraph
    parts = re.split(r"(```.*?```)", md, flags=re.S)
    for k in range(0, len(parts), 2):
        parts[k] = re.sub(r"<(?!https?://)([^>\n]{1,40})>", r"&lt;\1&gt;", parts[k])       # keep <name> placeholders visible
        parts[k] = re.sub(r"(?m)^(?!- |\s*$)(.+)\n(- )", r"\1\n\n\2", parts[k])             # blank line before a list
        parts[k] = re.sub(r"(?m)^(- .*)\n(?!- |\s*$|\s+- )", r"\1\n\n", parts[k])            # blank line after a list
        parts[k] = re.sub(r"(?m)^(> .*)\n(?=> )", r"\1  \n", parts[k])                        # keep each quoted line on its own line
        parts[k] = re.sub(r"(?<![<\"'])\b(https?://[^\s)<>,]+[^\s)<>,.])", r"<\1>", parts[k])
        parts[k] = re.sub(r"(?m)^(\*\*\d+\..*\*\*)$", r"\1\n", parts[k])
        parts[k] = re.sub(r"(?m)^(> .*)\n(?!>|\n)", r"\1\n\n", parts[k])   # end a quote before the next line
    md = "".join(parts)
    body = markdown.markdown(md, extensions=["fenced_code"])
    doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>{html.escape(title)}</title><style>{CSS}</style></head><body>
<div class="top"><div class="eb">THE AI AGENCY · YOUTUBE LIBRARY</div><h1>{html.escape(title)}</h1>
<div class="vid">Video: <a href="{url}">{url}</a> ({html.escape(length)})</div></div>
{body}
<div class="foot">Tyler Reed · skool.com/the-ai-agency</div></body></html>"""
    out = OUT / (txt.stem.split("-", 1)[1] + "-guide.html")
    out.write_text(doc)
    return out

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def to_pdf(html_path: Path) -> Path:
    """Headless Chrome print (same output as the browser's Page.printToPDF: same pages, same links)."""
    import subprocess
    pdf = html_path.with_suffix(".pdf")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", html_path.resolve().as_uri()],
                   capture_output=True, timeout=120)
    if not pdf.exists() or pdf.stat().st_size < 10_000:
        raise SystemExit(f"PDF print failed for {html_path.name}")
    return pdf


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--pdf"]
    files = [Path(a) for a in args] or sorted((ROOT / "lessons").glob("*.txt"))
    for f in files:
        h = build(f)
        print(h)
        if "--pdf" in sys.argv:
            print(to_pdf(h))
