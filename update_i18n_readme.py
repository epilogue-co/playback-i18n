#!/usr/bin/env python3
"""Update README.md translation status table by parsing Qt Linguist .ts files."""

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

LANGUAGES = {
    "main_de.ts": ("🇩🇪", "German", "Human"),
    "main_el.ts": ("🇬🇷", "Greek", "Human"),
    "main_zh.ts": ("🇨🇳", "Simplified Chinese", "Human"),
    "main_fr.ts": ("🇫🇷", "French", "Human"),
    "main_es.ts": ("🇪🇸", "Spanish", "Human"),
    "main_it.ts": ("🇮🇹", "Italian", "AI"),
    "main_ja.ts": ("🇯🇵", "Japanese", "Human"),
    "main_ko.ts": ("🇰🇷", "Korean", "Human"),
    "main_nl.ts": ("🇳🇱", "Dutch", "AI"),
    "main_pt.ts": ("🇵🇹", "Portuguese", "AI"),
    "main_ro.ts": ("🇷🇴", "Romanian", "Human"),
}


def count_unfinished(ts_file):
    """Return (total, unfinished) translation counts from a .ts file."""
    tree = ET.parse(ts_file)
    total = 0
    unfinished = 0

    for translation in tree.findall(".//message/translation"):
        total += 1
        if translation.get("type") == "unfinished":
            unfinished += 1

    return total, unfinished


def generate_table():
    """Generate markdown table with current translation status."""
    base_dir = Path(__file__).parent
    rows = [
        "| Language               | Type          | Complete    | Missing Strings  |",
        "| ---------------------- | ------------- | --------    | ---------------  |",
    ]

    for filename, (flag, name, trans_type) in sorted(LANGUAGES.items(), key=lambda x: x[1][1]):
        ts_file = base_dir / filename
        if not ts_file.exists():
            print(f"Warning: {filename} not found", file=sys.stderr)
            continue

        try:
            total, unfinished = count_unfinished(ts_file)
            complete = "✅" if unfinished == 0 else "❌"
            rows.append(f"| {flag} {name:<21} | {trans_type:<13} | {complete:<11} | {unfinished:<16} |")
        except Exception as e:
            print(f"Error processing {filename}: {e}", file=sys.stderr)

    return "\n".join(rows)


def main():
    readme = Path(__file__).parent / "README.md"
    if not readme.exists():
        print("Error: README.md not found", file=sys.stderr)
        return 1

    content = readme.read_text()
    new_table = generate_table()

    pattern = r"(##\s+Translation\s+status\s*\n\s*\n)(.*?)(\n\s*\n##)"
    updated = re.sub(pattern, rf"\1{new_table}\3", content, flags=re.DOTALL)

    if updated == content:
        print("✓ README.md is already up to date")
        return 0

    readme.write_text(updated)
    print("✓ README.md updated successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
