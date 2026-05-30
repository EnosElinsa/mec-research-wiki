"""Split a list of papers (or the genuinely-new uncurated folders) into
context-window-sized batches for a multi-invocation curation/synthesis run.

Batch size is a parameter; the input defaults to the genuinely-new folders
reported by curation_status.py.

Usage:
  # derive the new-paper list itself, then split into batches of 7
  python tools/wiki/make_batches.py --size 7

  # split an explicit list file (one folder name per line)
  python tools/wiki/make_batches.py --size 6 --input my_papers.txt

  # write the plan for the orchestrator to consume
  python tools/wiki/make_batches.py --size 7 --json batches.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys

import wikilib
from curation_status import classify, detect_duplicates


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--size", type=int, required=True, help="papers per batch (choose from the context window budget)")
    ap.add_argument("--input", metavar="PATH", help="file with one folder/paper name per line; default = genuinely-new uncurated folders")
    ap.add_argument("--json", metavar="PATH", help="write the batch plan (relative paths land in .curation-out/)")
    args = ap.parse_args(argv)

    if args.input:
        items = [ln.strip() for ln in open(args.input, encoding="utf-8") if ln.strip()]
        skipped = []
    else:
        _, curated, uncurated, _ = classify()
        dupes = detect_duplicates(uncurated, curated)
        items = sorted(u for u in uncurated if u not in dupes)
        skipped = sorted(dupes.keys())

    batches = [items[i : i + args.size] for i in range(0, len(items), args.size)]
    plan = {
        "total": len(items),
        "batch_size": args.size,
        "num_batches": len(batches),
        "skipped_duplicates": skipped,
        "batches": {f"batch{i}": b for i, b in enumerate(batches, 1)},
    }

    print(f"TOTAL ITEMS: {len(items)} | BATCH SIZE: {args.size} | BATCHES: {len(batches)}")
    if skipped:
        print(f"SKIPPED DUPLICATES: {len(skipped)}")
    for i, b in enumerate(batches, 1):
        print(f"\n=== BATCH {i} ({len(b)}) ===")
        for d in b:
            print(f"  - {d}")

    if args.json:
        out = (
            args.json
            if os.path.isabs(args.json)
            else os.path.join(wikilib.scratch_dir(), args.json)
        )
        json.dump(plan, open(out, "w", encoding="utf-8"), indent=2)
        print(f"\nplan -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
