"""Exact page counts per wiki type + meta-doc health, for reconciling the
Snapshot in overview.md and the directory in index.md.

Replaces the counts.ps1 one-off with a cross-platform Python version (the
PowerShell variant remains available but this is the canonical one).

Usage:
  python tools/wiki/corpus_counts.py
  python tools/wiki/corpus_counts.py --json counts.json
"""

from __future__ import annotations

import argparse
import json
import os
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


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", metavar="PATH", help="write counts as JSON (relative paths land in .curation-out/)")
    args = ap.parse_args(argv)

    c = counts()
    raw = len(wikilib.raw_folders())
    width = max(len(k) for k in c)
    for k, v in c.items():
        print(f"{k.ljust(width)}  {v}")
    print(f"{'raw/sources'.ljust(width)}  {raw}")

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
