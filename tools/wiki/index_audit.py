#!/usr/bin/env python3
"""Reconcile the wiki page inventory against ``wiki/index.md`` coverage.

The auditor must verify that ``index.md`` references every curated page exactly
once and that no index bullet points at a non-existent page. ``linkcheck.py``
already catches globally-dangling links; this tool answers the index-specific
questions:

  * Which pages exist on disk but are NOT linked from ``index.md``? (coverage
    gaps the index should list.)
  * Which slugs does ``index.md`` link to MORE THAN ONCE? (duplicate listings —
    excluding deliberate ``>`` cross-reference notes is left to human review,
    but the raw duplicate count is reported.)

Pages that are intentionally not catalogued in the index (the meta docs
themselves, the repo-root ``purpose``/``README``, parser scaffolding like
``schema``/``full``, and the raw MinerU orphan dumps) are excluded by default
via ``--ignore`` defaults; override with ``--ignore`` as needed.

Run from the repo root:  ``python tools/wiki/index_audit.py``
Exit code is non-zero if any coverage gap or duplicate listing is found.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter

import wikilib


# Pages that legitimately never appear as index bullets.
DEFAULT_IGNORE = {
    "index",
    "overview",
    "log",
    "purpose",
    "readme",
    "schema",
    "full",
}


def _type_of(path: str) -> str:
    """Infer the wiki page type from its parent directory name."""
    parent = os.path.basename(os.path.dirname(path))
    return parent if parent in wikilib.PAGE_TYPES else "other"


def collect_pages(ignore: set[str]) -> dict[str, set[str]]:
    """Map page-type -> set of slugs for every catalogue-able wiki page."""
    by_type: dict[str, set[str]] = {}
    wiki = wikilib.wiki_dir()
    for p in wikilib.md_files(wiki):
        slug = os.path.splitext(os.path.basename(p))[0]
        if slug.lower() in ignore:
            continue
        # Skip raw MinerU orphan dumps that sometimes land under wiki/.
        if slug.startswith("MinerU_markdown_"):
            continue
        by_type.setdefault(_type_of(p), set()).add(slug)
    return by_type


def index_links() -> list[str]:
    """All wikilink targets in ``index.md`` (in document order, with repeats)."""
    idx = os.path.join(wikilib.wiki_dir(), "index.md")
    return list(wikilib.iter_wikilinks(wikilib.read_text(idx)))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--ignore",
        nargs="*",
        default=None,
        help="page slugs (lowercase) to treat as never-indexed; "
        "defaults to the meta docs + parser scaffolding.",
    )
    ap.add_argument("--json", dest="json_path", default=None,
                    help="write a machine-readable report to PATH "
                    "(relative paths land in .curation-out/).")
    args = ap.parse_args(argv)

    ignore = set(args.ignore) if args.ignore is not None else set(DEFAULT_IGNORE)

    by_type = collect_pages(ignore)
    all_pages = {s for slugs in by_type.values() for s in slugs}
    links = index_links()
    linked = set(links)
    counts = Counter(links)

    # Coverage gaps: a page exists but no index bullet links to it.
    missing: dict[str, list[str]] = {}
    for t, slugs in sorted(by_type.items()):
        gap = sorted(s for s in slugs if s not in linked)
        if gap:
            missing[t] = gap

    # Duplicate index listings (a slug linked more than once).
    duplicated = {s: c for s, c in counts.items() if c > 1 and s in all_pages}

    total_missing = sum(len(v) for v in missing.values())

    print("=" * 70)
    print(f"INDEX COVERAGE: {len(all_pages)} catalogue-able pages, "
          f"{len(linked)} distinct slugs linked from index.md")
    print("=" * 70)
    if missing:
        print(f"PAGES NOT INDEXED: {total_missing}")
        for t, gap in missing.items():
            print(f"  [{t}] {len(gap)}")
            for s in gap:
                print(f"      {s}")
    else:
        print("PAGES NOT INDEXED: 0  (every page is catalogued)")

    if duplicated:
        print(f"\nSLUGS LINKED >1x IN INDEX: {len(duplicated)} "
              "(may include deliberate '>' cross-refs — review)")
        for s, c in sorted(duplicated.items(), key=lambda kv: -kv[1]):
            print(f"  {c}x  {s}")
    else:
        print("\nSLUGS LINKED >1x IN INDEX: 0")

    if args.json_path:
        out = args.json_path
        if not os.path.isabs(out):
            out = os.path.join(wikilib.scratch_dir(), out)
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(
                {
                    "catalogueable_pages": len(all_pages),
                    "distinct_linked": len(linked),
                    "missing": missing,
                    "duplicated": duplicated,
                },
                fh,
                indent=2,
            )
        print(f"\nReport written to {out}")

    return 1 if (missing or duplicated) else 0


if __name__ == "__main__":
    sys.exit(main())
