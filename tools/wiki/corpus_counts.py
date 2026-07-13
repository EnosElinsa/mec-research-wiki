"""Exact page counts per wiki type + meta-doc health, for reconciling the
Snapshot in overview.md and the directory in index.md.

Usage:
  python tools/wiki/corpus_counts.py
  python tools/wiki/corpus_counts.py --json counts.json
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

import wikilib


def counts():
    root = wikilib.wiki_dir()
    out = {}
    for t in wikilib.PAGE_TYPES:
        d = os.path.join(root, t)
        if os.path.isdir(d):
            out[t] = len([f for f in os.listdir(d) if f.endswith(".md")])
        else:
            out[t] = 0
    return out


def update_overview(path, page_counts):
    """Refresh the three inventory counts in the overview Snapshot."""
    text = wikilib.read_text(path)
    entity_dir = os.path.join(wikilib.wiki_dir(), "entities")
    tool_pages = 0
    if os.path.isdir(entity_dir):
        for name in os.listdir(entity_dir):
            if not name.endswith(".md"):
                continue
            page = wikilib.read_text(os.path.join(entity_dir, name))
            if re.search(r"(?m)^tags:\s*\[[^\]]*\btool\b", page):
                tool_pages += 1
    author_pages = page_counts["entities"] - tool_pages

    replacements = (
        (r"(?m)^- \*\*Curated sources:\*\* \d+", f"- **Curated sources:** {page_counts['sources']}"),
        (r"(?m)^- \*\*Concepts:\*\* \d+", f"- **Concepts:** {page_counts['concepts']}"),
        (
            r"(?m)^- \*\*Entities:\*\* \d+ author pages \+ \d+ tool pages",
            f"- **Entities:** {author_pages} author pages + {tool_pages} tool pages",
        ),
        (
            r"\(\d+ entity pages total\)",
            f"({page_counts['entities']} entity pages total)",
        ),
    )
    for pattern, replacement in replacements:
        text, changed = re.subn(pattern, replacement, text, count=1)
        if changed != 1:
            raise ValueError(f"overview count marker not found exactly once: {pattern}")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", metavar="PATH", help="write counts as JSON (relative paths land in .curation-out/)")
    ap.add_argument(
        "--update-overview",
        action="store_true",
        help="refresh source/concept/entity counts in wiki/overview.md",
    )
    args = ap.parse_args(argv)

    c = counts()
    raw = len(wikilib.raw_folders())
    width = max(len(k) for k in c)
    for k, v in c.items():
        print(f"{k.ljust(width)}  {v}")
    print(f"{'raw/sources'.ljust(width)}  {raw}")

    if args.update_overview:
        overview = os.path.join(wikilib.wiki_dir(), "overview.md")
        update_overview(overview, c)
        print(f"\noverview counts -> {overview}")

    # entity pages minus the lone tool page (pytorch) is a common derived number
    log_path = os.path.join(wikilib.wiki_dir(), "log.md")
    if os.path.exists(log_path):
        lines = wikilib.read_text(log_path).splitlines()
        print(f"\nlog.md lines: {len(lines)}")

    if args.json:
        out = (
            args.json
            if os.path.isabs(args.json)
            else os.path.join(wikilib.scratch_dir(), args.json)
        )
        payload = dict(c)
        payload["raw_sources"] = raw
        json.dump(payload, open(out, "w", encoding="utf-8"), indent=2)
        print(f"\ncounts -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
