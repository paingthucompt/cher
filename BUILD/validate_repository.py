#!/usr/bin/env python3
from pathlib import Path
import re
import sys
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
MD_FILES = sorted(ROOT.rglob("*.md"))
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

errors = []
warnings = []

for path in MD_FILES:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if path.stat().st_size == 0:
        warnings.append(f"empty markdown file: {path.relative_to(ROOT)}")

    in_fence = False
    h1_count = 0
    for line in text.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and line.startswith("# ") and not line.startswith("## "):
            h1_count += 1
    if h1_count != 1 and path.stat().st_size > 0:
        warnings.append(f"H1 count {h1_count}: {path.relative_to(ROOT)}")

    for match in LINK_RE.finditer(text):
        href = match.group(1).strip()
        if href.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = href.split("#", 1)[0]
        if not clean:
            continue
        # Ignore explicit placeholder examples in rules/build docs.
        if "path/to/" in clean or "CHAR_001_AungAung" in clean:
            continue
        target = (path.parent / clean).resolve()
        try:
            target.relative_to(ROOT.resolve())
        except ValueError:
            warnings.append(f"external relative link: {path.relative_to(ROOT)} -> {href}")
            continue
        if not target.exists():
            line = text.count("\n", 0, match.start()) + 1
            errors.append(f"broken link: {path.relative_to(ROOT)}:{line} -> {href}")

chapter_numbers = defaultdict(list)
for path in (ROOT / "MASTER_BIBLE").rglob("CHAP_*.md"):
    match = re.search(r"CHAP_(\d+)", path.name)
    if match:
        chapter_numbers[int(match.group(1))].append(path.relative_to(ROOT))

for number, paths in sorted(chapter_numbers.items()):
    if len(paths) > 1:
        warnings.append(
            "duplicate CHAP number "
            + f"{number:02d}: "
            + ", ".join(str(path) for path in paths)
        )

required = [
    "README.md",
    "MASTER_INDEX.md",
    "VERSION.md",
    "CHANGELOG.md",
    "CANON_INDEX.md",
    "CHARACTER_INDEX.md",
    "ORGANIZATION_INDEX.md",
    "TIMELINE.md",
    "GLOSSARY.md",
]
for rel in required:
    path = ROOT / rel
    if not path.exists():
        errors.append(f"missing required file: {rel}")
    elif path.stat().st_size == 0:
        errors.append(f"required file is empty: {rel}")

print(f"Checked {len(MD_FILES)} Markdown files")
print(f"Errors: {len(errors)}")
for item in errors:
    print(f"ERROR: {item}")
print(f"Warnings: {len(warnings)}")
for item in warnings:
    print(f"WARN: {item}")

sys.exit(1 if errors else 0)
