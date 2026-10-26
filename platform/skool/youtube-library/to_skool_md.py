#!/usr/bin/env python3
"""Lesson .txt (plain-text template) -> Skool-ready markdown for md_to_v2.

usage: python3 to_skool_md.py lessons/04-*.txt ...   (writes skool-md/<name>.md)
Drops line 1 (title = lesson title in Skool), the Video: line (video is the lesson's
video field) and CHECK: lines. Section names become ## headings, step lines become
bold, and the block after a step line ending in ':' becomes a code block (commands,
yaml) or a blockquote (prompts). Eyeball the output before pushing.
"""
import re, sys
from pathlib import Path

SECTIONS = {"IN THIS LESSON", "GOOD TO KNOW", "WHAT YOU NEED", "STEPS", "FILES AND LINKS", "IF IT BREAKS", "NEXT"}
STEP = re.compile(r"^\d+\.\s.+\(\d+:\d+(:\d+)?\)$")
CMD = re.compile(r"^(npx |npm |git |cd |uv |uvx |python3? |pip |curl |mkdir |cp |claude |ollama |arcade |hermes |brew |export |source |dsh |!|/[a-z][\w-]*( |$)|chmod |open |nano |\./|[A-Z_]+=)")
YAML = re.compile(r"^\s*(-\s+)?[A-Za-z_]+:(\s|$)")


def to_md(text: str) -> str:
    lines = [l for l in text.rstrip().splitlines()[1:] if not l.startswith(("Video: ", "CHECK:"))]
    out, sec, i = [], None, 0

    def emit(block):
        if any(CMD.match(b.strip()) or YAML.match(b) for b in block):
            out.extend(["```"] + block + ["```"])
        else:
            out.extend("> " + b.strip() for b in block)

    while i < len(lines):
        ln = lines[i]; s = ln.strip()
        if s in SECTIONS:
            sec = s
            if s != "STEPS":
                out += ["", "## " + s.capitalize()]
            i += 1; continue
        if sec == "STEPS" and STEP.match(s):
            out += ["", "**" + s + "**"]; i += 1; continue
        out.append(ln); i += 1
        if sec == "STEPS" and s.endswith(":"):
            j = i
            if j < len(lines) and not lines[j].strip():
                j += 1; block = []
                while j < len(lines) and lines[j].strip():
                    block.append(lines[j]); j += 1
                if block and not (block[0].strip().startswith("- ") and not YAML.match(block[0])):
                    out.append(""); emit(block); i = j
            else:
                block = []
                while j < len(lines) and lines[j].strip() and CMD.match(lines[j].strip()):
                    block.append(lines[j]); j += 1
                nxt = lines[j].strip() if j < len(lines) else ""
                if not block and nxt and not nxt.startswith("-") and not STEP.match(nxt) and nxt not in SECTIONS:
                    block = [lines[j]]; j += 1
                if block:
                    emit(block); i = j
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip() + "\n"


if __name__ == "__main__":
    outdir = Path(__file__).with_name("skool-md"); outdir.mkdir(exist_ok=True)
    for a in sys.argv[1:]:
        f = Path(a); md = to_md(f.read_text())
        assert "\u2014" not in md, f"em dash in {f.name}"
        (outdir / f.with_suffix(".md").name).write_text(md)
        print(f.name, len(md.split()), "words")
