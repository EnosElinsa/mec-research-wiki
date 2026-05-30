"""Reconcile raw/sources/ against the curated wiki and detect duplicate ingests.

It answers, in one place:
  * which raw-source folders are NOT yet curated (no wiki page references them);
  * which curated references point at no existing raw folder (renames/typos);
  * which uncurated folders are likely DUPLICATE MinerU ingests of an already
    curated paper (byte-identical or near-identical full.md), so they can be
    skipped rather than re-curated.

Usage:
  python tools/wiki/curation_status.py                 # summary + uncurated list
  python tools/wiki/curation_status.py --dupes         # also run duplicate detection
  python tools/wiki/curation_status.py --json status.json
Exit code is 1 when genuinely-uncurated (non-duplicate) papers remain.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import os
import sys

import wikilib


def _full_md(folder: str) -> str:
    return os.path.join(wikilib.raw_sources_dir(), folder, "full.md")


def _hash_len(folder: str):
    p = _full_md(folder)
    if not os.path.exists(p):
        return None, 0
    data = open(p, "rb").read()
    return hashlib.sha256(data).hexdigest(), len(data)


def classify():
    raw = wikilib.raw_folders()
    referenced = wikilib.referenced_raw_folders()
    raw_set = set(raw)
    uncurated = [d for d in raw if d not in referenced]
    curated = [d for d in raw if d in referenced]
    orphan_refs = sorted(r for r in referenced if r not in raw_set)
    return raw, curated, uncurated, orphan_refs


def detect_duplicates(uncurated, curated, near_ratio=0.97):
    """For each uncurated folder, find a curated folder whose full.md is
    identical (sha) or near-identical (difflib ratio >= near_ratio).

    Returns {uncurated_folder: {"match": curated_folder, "kind": "identical"|"near",
    "ratio": float}}.
    """
    cur_hashes = {}
    cur_text = {}
    for c in curated:
        h, _ = _hash_len(c)
        if h:
            cur_hashes[c] = h
            cur_text[c] = wikilib.read_text(_full_md(c))
    dupes = {}
    for u in uncurated:
        hu, _ = _hash_len(u)
        if not hu:
            continue
        # exact match first
        exact = next((c for c, h in cur_hashes.items() if h == hu), None)
        if exact:
            dupes[u] = {"match": exact, "kind": "identical", "ratio": 1.0}
            continue
        # near match by content ratio (cheap title/abstract proxy: first 4k chars)
        tu = wikilib.read_text(_full_md(u))[:4000]
        best, best_ratio = None, 0.0
        for c, tc in cur_text.items():
            r = difflib.SequenceMatcher(None, tu, tc[:4000]).ratio()
            if r > best_ratio:
                best, best_ratio = c, r
        if best and best_ratio >= near_ratio:
            dupes[u] = {"match": best, "kind": "near", "ratio": round(best_ratio, 4)}
    return dupes


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dupes", action="store_true", help="run duplicate-ingest detection on uncurated folders")
    ap.add_argument("--near-ratio", type=float, default=0.97, help="similarity threshold for a near-duplicate (default 0.97)")
    ap.add_argument("--json", metavar="PATH", help="write a JSON report (relative paths land in .curation-out/)")
    args = ap.parse_args(argv)

    raw, curated, uncurated, orphan_refs = classify()
    print(f"RAW FOLDERS: {len(raw)}")
    print(f"CURATED (referenced): {len(curated)}")
    print(f"UNCURATED: {len(uncurated)}")

    dupes = {}
    genuinely_new = list(uncurated)
    if args.dupes and uncurated:
        dupes = detect_duplicates(uncurated, curated, args.near_ratio)
        genuinely_new = [u for u in uncurated if u not in dupes]

    print("=" * 70)
    for d in uncurated:
        tag = ""
        if d in dupes:
            m = dupes[d]
            tag = f"   [DUPLICATE: {m['kind']} of {m['match']} (ratio {m['ratio']})]"
        print(f"UNCURATED: {d}{tag}")

    if orphan_refs:
        print("=" * 70)
        print(f"REFERENCED NAMES WITH NO MATCHING RAW FOLDER: {len(orphan_refs)}")
        for r in orphan_refs:
            print(f"  NO-MATCH: {r}")

    if args.dupes:
        print("=" * 70)
        print(f"GENUINELY NEW (uncurated, non-duplicate): {len(genuinely_new)}")

    report = {
        "raw": raw,
        "curated": curated,
        "uncurated": uncurated,
        "orphan_refs": orphan_refs,
        "duplicates": dupes,
        "genuinely_new": genuinely_new,
    }
    if args.json:
        out = (
            args.json
            if os.path.isabs(args.json)
            else os.path.join(wikilib.scratch_dir(), args.json)
        )
        json.dump(report, open(out, "w", encoding="utf-8"), indent=2)
        print(f"\nreport -> {out}")

    return 1 if genuinely_new else 0


if __name__ == "__main__":
    sys.exit(main())
