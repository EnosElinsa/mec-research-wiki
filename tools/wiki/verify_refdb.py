"""Verify the integrity of the mined reference database.

A correctness gate for the reference-scout pipeline: after ``mine_refs.py``
regenerates ``reference-database.json``, this confirms the parse output is
clean and self-consistent. It checks three things, all grounded in the parses
(it never invents or rewrites a field):

  1. Contamination — no record's string fields (title/venue/authors/raw) still
     contain a MinerU contamination marker (inline figure markdown,
     <details>/<summary> caption wrappers, embedded headings, author-biography
     prose). This is the regression guard for the ``strip_ref_contamination``
     fix: the final entry of a references block used to absorb this trailing
     junk and mis-stamp the year/venue.

  2. Plausible years — every parsed year is within ``[--min-year, --max-year]``.
     Anything past --max-year is almost always contamination bleed (a figure
     caption or biography date), so it fails the gate.

  3. Future-year provenance — every record at or after ``--flag-year`` is listed
     so a human can confirm it is a genuine in-press citation. Non-curated
     future-year records are surfaced as a warning (they are the rows most
     likely to be a mis-parse); curated ones (``curated_as`` set) are expected.

Exit 1 if any contamination marker is found or any year is out of range, so the
check can gate a commit. Year warnings alone do not fail the run.

Usage:
  python tools/wiki/verify_refdb.py
  python tools/wiki/verify_refdb.py --flag-year 2026 --json verify.json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections import Counter

import wikilib

# Fields that hold free text mined from a reference string.
_STR_FIELDS = ("title", "venue", "venue_normalized", "authors", "raw")


def scan_contamination(records):
    """Return [(key, field, value)] for any field still carrying a marker."""
    hits = []
    for r in records:
        for f in _STR_FIELDS:
            v = r.get(f)
            if isinstance(v, str) and v and wikilib.strip_ref_contamination(v) != v:
                hits.append((r.get("key"), f, v))
    return hits


def year_histogram(records):
    return Counter(r.get("year") for r in records)


def check_years(records, min_year, max_year):
    """Return [(key, year, title)] for records with an out-of-range year."""
    bad = []
    for r in records:
        y = r.get("year")
        if y and str(y).isdigit():
            yi = int(y)
            if yi < min_year or yi > max_year:
                bad.append((r.get("key"), y, r.get("title")))
    return bad


def future_records(records, flag_year):
    """Records at/after flag_year, split into curated vs not (for provenance)."""
    fut = [r for r in records if (r.get("year") or "").isdigit() and int(r["year"]) >= flag_year]
    curated = [r for r in fut if r.get("curated_as")]
    uncurated = [r for r in fut if not r.get("curated_as")]
    return curated, uncurated


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", default=None, help="path to reference-database.json")
    ap.add_argument("--min-year", type=int, default=1948, help="earliest plausible year")
    ap.add_argument("--max-year", type=int, default=2026, help="latest plausible year (past this = contamination bleed)")
    ap.add_argument("--flag-year", type=int, default=2026, help="list records at/after this year for provenance review")
    ap.add_argument("--json", metavar="PATH", help="write the machine-readable report (relative → .curation-out/)")
    args = ap.parse_args(argv)

    db_path = args.db or os.path.join(wikilib.wiki_dir(), "references", "reference-database.json")
    db = json.load(open(db_path, encoding="utf-8"))
    records = db.get("records", [])

    contam = scan_contamination(records)
    hist = year_histogram(records)
    bad_years = check_years(records, args.min_year, args.max_year)
    fut_curated, fut_uncurated = future_records(records, args.flag_year)

    print(f"DB: {db_path}")
    print(f"Records: {len(records)}  (generated {db.get('generated')}, {db.get('reference_strings')} strings from {db.get('parses_mined')} parses)")
    print("=" * 70)

    print("\nYEAR DISTRIBUTION (most recent first):")
    for y in sorted((k for k in hist if k), key=lambda v: str(v), reverse=True)[:14]:
        print(f"  {y}: {hist[y]}")
    print(f"  null/na: {hist.get(None, 0)}")

    print(f"\nCONTAMINATION MARKERS: {len(contam)}")
    for key, field, val in contam[:30]:
        snippet = val if len(val) <= 120 else val[:117] + "..."
        print(f"  [{field}] {key}: {snippet!r}")
    if len(contam) > 30:
        print(f"  ... ({len(contam) - 30} more)")

    print(f"\nOUT-OF-RANGE YEARS (<{args.min_year} or >{args.max_year}): {len(bad_years)}")
    for key, y, title in bad_years[:30]:
        print(f"  {y}  {key}  {title!r}")

    print(f"\nFUTURE-YEAR RECORDS (>= {args.flag_year}): {len(fut_curated) + len(fut_uncurated)}")
    print(f"  curated (expected in-press citations): {len(fut_curated)}")
    for r in fut_curated:
        print(f"    OK  {r['year']}  {r['key']}  -> curated_as={r['curated_as']}")
    print(f"  NOT curated (review — most likely mis-parse if unexpected): {len(fut_uncurated)}")
    for r in fut_uncurated:
        print(f"    ??  {r['year']}  {r['key']}  {r.get('title')!r}")

    ok = not contam and not bad_years
    print("\n" + "=" * 70)
    print("RESULT:", "CLEAN" if ok else "PROBLEMS FOUND")
    if fut_uncurated:
        print(f"NOTE: {len(fut_uncurated)} uncurated record(s) at/after {args.flag_year} — confirm these are genuine in-press citations, not contamination.")

    if args.json:
        out = args.json if os.path.isabs(args.json) else os.path.join(wikilib.scratch_dir(), args.json)
        json.dump({
            "db": db_path,
            "records": len(records),
            "year_histogram": {str(k): v for k, v in hist.items()},
            "contamination": [{"key": k, "field": f, "value": v} for k, f, v in contam],
            "out_of_range_years": [{"key": k, "year": y, "title": t} for k, y, t in bad_years],
            "future_curated": [{"key": r["key"], "year": r["year"], "curated_as": r.get("curated_as")} for r in fut_curated],
            "future_uncurated": [{"key": r["key"], "year": r["year"], "title": r.get("title")} for r in fut_uncurated],
            "clean": ok,
        }, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"report -> {out}")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
