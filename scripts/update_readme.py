#!/usr/bin/env python3
"""
Regenerate README.md with a table of every solved problem.

Scans problems/*/notes.md for YAML frontmatter (number, title,
difficulty, tags, date, url) and writes a sorted markdown table
into README.md between two marker comments, leaving the rest of
the README untouched.

Usage:
    python scripts/update_readme.py

Tip: wire this into a git pre-commit hook or a GitHub Action so
the table never goes stale.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
README_PATH = ROOT / "README.md"

START_MARKER = "<!-- PROBLEMS_TABLE_START -->"
END_MARKER = "<!-- PROBLEMS_TABLE_END -->"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    data = {}
    for line in match.group(1).splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            value = [v.strip() for v in inner.split(",") if v.strip()]
        data[key] = value
    return data


def collect_problems():
    rows = []
    if not PROBLEMS_DIR.exists():
        return rows
    for folder in sorted(PROBLEMS_DIR.iterdir()):
        notes = folder / "notes.md"
        if not folder.is_dir() or not notes.exists():
            continue
        meta = parse_frontmatter(notes.read_text(encoding="utf-8"))
        if not meta.get("number"):
            continue
        rows.append({
            "number": int(meta.get("number", 0)),
            "title": meta.get("title", folder.name),
            "difficulty": meta.get("difficulty", "Unknown"),
            "tags": meta.get("tags", []),
            "date": meta.get("date", ""),
            "url": meta.get("url", ""),
        })
    rows.sort(key=lambda r: r["number"])
    return rows


def build_table(rows) -> str:
    if not rows:
        return "_No problems solved yet._\n"

    counts = {"Easy": 0, "Medium": 0, "Hard": 0, "Unknown": 0}
    for r in rows:
        counts[r["difficulty"]] = counts.get(r["difficulty"], 0) + 1

    lines = [
        f"**Total solved: {len(rows)}**  ",
        f"Easy: {counts['Easy']} · Medium: {counts['Medium']} · Hard: {counts['Hard']}",
        "",
        "| # | Title | Difficulty | Tags | Date |",
        "|---|-------|------------|------|------|",
    ]
    for r in rows:
        title_cell = f"[{r['title']}]({r['url']})" if r["url"] else r["title"]
        tags = ", ".join(r["tags"]) if isinstance(r["tags"], list) else r["tags"]
        lines.append(f"| {r['number']:04d} | {title_cell} | {r['difficulty']} | {tags} | {r['date']} |")
    return "\n".join(lines) + "\n"


def update_readme(rows):
    block = f"{START_MARKER}\n{build_table(rows)}{END_MARKER}"

    if README_PATH.exists():
        content = README_PATH.read_text(encoding="utf-8")
    else:
        content = "# LeetCode Solutions\n\n" + START_MARKER + "\n" + END_MARKER + "\n"

    if START_MARKER in content and END_MARKER in content:
        pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
        content = pattern.sub(block, content)
    else:
        content = content.rstrip() + "\n\n" + block + "\n"

    README_PATH.write_text(content, encoding="utf-8")
    print(f"Updated {README_PATH} with {len(rows)} problems.")


def main():
    update_readme(collect_problems())


if __name__ == "__main__":
    main()
