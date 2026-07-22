#!/usr/bin/env python3
"""
Scaffold a new LeetCode problem folder from templates/.

Usage:
    python scripts/new_problem.py 1 "Two Sum" --difficulty Easy --tags array,hash-table --func twoSum
    python scripts/new_problem.py 206 "Reverse Linked List" -d Easy -t linked-list -f reverseList

Creates:
    problems/0001-two-sum/
        solution.py
        test_solution.py
        notes.md
"""
import argparse
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBLEMS_DIR = ROOT / "problems"
TEMPLATES_DIR = ROOT / "templates"


def slugify(title: str) -> str:
    slug = title.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    return slug


def pad(number: int) -> str:
    return f"{number:04d}"


def render(text: str, **kwargs) -> str:
    for key, value in kwargs.items():
        text = text.replace(f"{{{{{key}}}}}", str(value))
    return text


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new LeetCode problem folder.")
    parser.add_argument("number", type=int, help="LeetCode problem number, e.g. 1")
    parser.add_argument("title", help="Problem title, e.g. 'Two Sum'")
    parser.add_argument("-d", "--difficulty", default="Unknown",
                         choices=["Easy", "Medium", "Hard", "Unknown"])
    parser.add_argument("-t", "--tags", default="",
                         help="Comma-separated tags, e.g. array,hash-table")
    parser.add_argument("-f", "--func", default="solve",
                         help="Name of the main solution method, e.g. twoSum")
    parser.add_argument("-u", "--url", default="",
                         help="Link to the problem on leetcode.com (auto-guessed if omitted)")
    parser.add_argument("--force", action="store_true",
                         help="Overwrite files if the folder already exists")
    args = parser.parse_args()

    slug = slugify(args.title)
    folder_name = f"{pad(args.number)}-{slug}"
    folder = PROBLEMS_DIR / folder_name

    if folder.exists() and not args.force:
        print(f"Folder already exists: {folder}")
        print("Use --force to overwrite files in it.")
        sys.exit(1)

    folder.mkdir(parents=True, exist_ok=True)

    tags_list = [t.strip() for t in args.tags.split(",") if t.strip()]
    tags_yaml = "[" + ", ".join(tags_list) + "]" if tags_list else "[]"

    context = {
        "number": args.number,
        "number_padded": pad(args.number),
        "title": args.title,
        "difficulty": args.difficulty,
        "tags": tags_yaml,
        "date": datetime.date.today().isoformat(),
        "func": args.func,
        "url": args.url or f"https://leetcode.com/problems/{slug}/",
    }

    files = {
        "solution.py": TEMPLATES_DIR / "solution.py",
        "test_solution.py": TEMPLATES_DIR / "test_solution.py",
        "notes.md": TEMPLATES_DIR / "notes.md",
    }

    for filename, template_path in files.items():
        template_text = template_path.read_text(encoding="utf-8")
        rendered = render(template_text, **context)
        (folder / filename).write_text(rendered, encoding="utf-8")

    print(f"Created {folder}")
    for filename in files:
        print(f"  - {filename}")


if __name__ == "__main__":
    main()
