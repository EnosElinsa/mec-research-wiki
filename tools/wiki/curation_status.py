"""Reconcile raw/sources/ against the curated wiki and detect duplicate ingests.

It answers, in one place:
  * which raw-source folders are NOT yet curated (no wiki page references them);
  * which curated references point at no existing raw folder (renames/typos);
  * which raw folders match an existing source page by title even when a
    recorded raw-artifact path is stale;
  * which uncurated folders are likely DUPLICATE MinerU ingests of an already
    curated paper (byte-identical or near-identical parse Markdown), so they can be
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
import glob
import hashlib
import json
import os
import re
import sys

import wikilib


def _full_md(folder: str) -> str:
    folder_path = os.path.join(wikilib.raw_sources_dir(), folder)
    preferred = os.path.join(folder_path, "full.md")
    if os.path.exists(preferred):
        return preferred

    title_named = os.path.join(folder_path, f"{folder}.md")
    if os.path.exists(title_named):
        return title_named

    markdown = sorted(glob.glob(os.path.join(folder_path, "*.md")))
    return markdown[0] if len(markdown) == 1 else preferred


_RAW_TITLE = re.compile(r"(?m)^#\s+(.+?)\s*$")
_NEAR_TITLE_RATIO = 0.75


def _raw_title(folder: str) -> str:
    path = _full_md(folder)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8", errors="replace") as handle:
        header = handle.read(65536)
    match = _RAW_TITLE.search(header)
    return match.group(1).strip() if match else ""


def _repeated_character_ocr_variant(left: str, right: str) -> bool:
    """Return true when one title key drops one character from a doubled pair."""
    if abs(len(left) - len(right)) != 1:
        return False
    longer, shorter = (left, right) if len(left) > len(right) else (right, left)
    for index, char in enumerate(longer):
        if longer[:index] + longer[index + 1 :] != shorter:
            continue
        return (
            (index > 0 and longer[index - 1] == char)
            or (index + 1 < len(longer) and longer[index + 1] == char)
        )
    return False


def _title_matches(raw: list[str], referenced: set[str]) -> dict[str, str]:
    curated_titles = wikilib.curated_title_keys()
    matches = {}
    for folder in raw:
        if folder in referenced:
            continue
        key = wikilib.title_match_key(_raw_title(folder))
        if key and key in curated_titles:
            matches[folder] = curated_titles[key]
            continue
        ocr_matches = [
            slug
            for curated_key, slug in curated_titles.items()
            if _repeated_character_ocr_variant(key, curated_key)
        ]
        if key and len(ocr_matches) == 1:
            matches[folder] = ocr_matches[0]
    return matches


def _hash_len(folder: str):
    p = _full_md(folder)
    if not os.path.exists(p):
        return None, 0
    with open(p, "rb") as handle:
        data = handle.read()
    return hashlib.sha256(data).hexdigest(), len(data)


def _text_prefix(folder: str, limit: int = 4000) -> str:
    path = _full_md(folder)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8", errors="replace") as handle:
        return handle.read(limit)


def classify(include_title_matches=False):
    raw = wikilib.raw_folders()
    referenced = wikilib.referenced_raw_folders()
    title_matches = _title_matches(raw, referenced)
    raw_set = set(raw)
    uncurated = [d for d in raw if d not in referenced and d not in title_matches]
    curated = [d for d in raw if d in referenced or d in title_matches]
    orphan_refs = sorted(r for r in referenced if r not in raw_set)
    result = (raw, curated, uncurated, orphan_refs)
    return (*result, title_matches) if include_title_matches else result


def detect_duplicates(uncurated, curated, near_ratio=0.97):
    """For each uncurated folder, find a curated folder whose parse Markdown is
    identical (sha) or near-identical (difflib ratio >= near_ratio).

    Returns {uncurated_folder: {"match": curated_folder, "kind": "identical"|"near",
    "ratio": float}}.
    """
    cur_hashes = {}
    cur_text = {}
    cur_titles = {}
    for c in curated:
        h, _ = _hash_len(c)
        if h:
            cur_hashes[c] = h
            cur_text[c] = _text_prefix(c)
            cur_titles[c] = wikilib.title_match_key(_raw_title(c))
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
        tu = _text_prefix(u)
        u_title = wikilib.title_match_key(_raw_title(u))
        best, best_ratio = None, 0.0
        for c, tc in cur_text.items():
            c_title = cur_titles[c]
            if not u_title or not c_title:
                continue
            title_ratio = difflib.SequenceMatcher(None, u_title, c_title).ratio()
            if title_ratio < _NEAR_TITLE_RATIO:
                continue
            r = difflib.SequenceMatcher(None, tu, tc).ratio()
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

    raw, curated, uncurated, orphan_refs, title_matches = classify(
        include_title_matches=True
    )
    print(f"RAW FOLDERS: {len(raw)}")
    print(f"CURATED (path/title matched): {len(curated)}")
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

    if title_matches:
        print("=" * 70)
        print(f"TITLE-MATCHED CURATED FOLDERS: {len(title_matches)}")
        for folder, slug in sorted(title_matches.items()):
            print(f"  TITLE-MATCH: {folder} -> {slug}")

    if args.dupes:
        print("=" * 70)
        print(f"GENUINELY NEW (uncurated, non-duplicate): {len(genuinely_new)}")

    report = {
        "raw": raw,
        "curated": curated,
        "uncurated": uncurated,
        "orphan_refs": orphan_refs,
        "title_matches": title_matches,
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
