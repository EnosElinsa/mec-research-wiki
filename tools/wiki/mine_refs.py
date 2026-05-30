"""Mine the ``# REFERENCES`` of every raw/sources parse into a deduplicated DB.

This is the maintained home of the reference-scout's mining logic (it used to be
a throwaway ``.curation-out/parse_refs.py``). It:

  * enumerates ``raw/sources/*/full.md`` (via wikilib),
  * extracts + parses each references block into structured records
    (wikilib.extract_references_block / split_ref_entries / parse_ref_entry),
  * deduplicates across the whole corpus by normalized-title (+ surname/year),
  * tracks ``cited_by`` (the curated slug, or the raw folder if uncurated) and
    ``cited_count``,
  * MERGES idempotently into an existing reference-database.json: existing
    records keep their enriched fields (venue_normalized, venue_tier, scope,
    doi, curated_as), only cited_by/cited_count and previously-empty fields are
    refreshed — present fields are never overwritten with a guess.

Correctness-first: a field absent from the parse stays ``null``; nothing is
fabricated. Web/standard citations with no venue simply carry ``null`` venue.

Usage:
  python tools/wiki/mine_refs.py --json mined.json          # scratch dump only
  python tools/wiki/mine_refs.py --merge wiki/references/reference-database.json
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys

import wikilib


def mine_all():
    """Parse every parse's references. Returns (per_folder, skipped)."""
    raw = wikilib.raw_sources_dir()
    folders = wikilib.raw_folders()
    per_folder = {}
    skipped = []
    for folder in folders:
        fp = os.path.join(raw, folder, "full.md")
        if not os.path.exists(fp):
            skipped.append((folder, "no full.md"))
            continue
        text = wikilib.read_text(fp)
        block = wikilib.extract_references_block(text)
        if not block:
            skipped.append((folder, "no references block"))
            continue
        entries = wikilib.split_ref_entries(block)
        if not entries:
            skipped.append((folder, "no entries parsed"))
            continue
        per_folder[folder] = [wikilib.parse_ref_entry(b) for _, b in entries]
    return per_folder, skipped


def dedup(per_folder, slug_map):
    """Collapse parsed entries into unique records keyed by normalized title.

    Entries with no parseable title fall back to a raw-string signature so they
    still dedupe but never collide with titled works.
    """
    records = {}
    total_strings = 0
    for folder, refs in per_folder.items():
        citer = slug_map.get(folder, folder)
        for r in refs:
            total_strings += 1
            norm = wikilib.normalize_title(r["title"])
            if norm:
                # Long titles are unique enough to dedup on title+year alone;
                # short/generic titles also key on first-author surname to avoid
                # collapsing genuinely different works.
                if len(norm.split()) >= 5:
                    dk = f"{norm}|{r['year'] or ''}"
                else:
                    dk = f"{norm}|{wikilib.author_surname(r['authors'])}|{r['year'] or ''}"
            else:
                dk = "RAW|" + wikilib.normalize_title(r["raw"])[:80]
            rec = records.get(dk)
            if rec is None:
                rec = {
                    "key": wikilib.ref_key(r["authors"], r["year"], r["title"]),
                    "authors": r["authors"],
                    "title": r["title"],
                    "venue": r["venue"],
                    "year": r["year"],
                    "vol": r["vol"],
                    "no": r["no"],
                    "pp": r["pp"],
                    "url": r["url"],
                    "doi": r["doi"],
                    "cited_by": [],
                    "_dedup_key": dk,
                }
                records[dk] = rec
            else:
                # Fill blanks from a cleaner parse; never overwrite a present field.
                for f in ("authors", "title", "venue", "year", "vol", "no", "pp", "url", "doi"):
                    if not rec.get(f) and r.get(f):
                        rec[f] = r[f]
            if citer not in rec["cited_by"]:
                rec["cited_by"].append(citer)
    for rec in records.values():
        rec["cited_by"] = sorted(rec["cited_by"])
        rec["cited_count"] = len(rec["cited_by"])
    return records, total_strings


def merge_into_db(records, db_path):
    """Idempotently reconcile freshly-mined records with an existing JSON DB.

    Because this run mines EVERY parse, the freshly-mined records are the
    authoritative truth for the faithful fields and the citation signal
    (cited_by / cited_count). The only thing worth carrying over from the old
    DB is *enrichment* that is not re-derivable from the parses:
    ``venue_normalized``, ``venue_tier``, ``scope``, ``curated_as`` and a
    cleaner ``doi``. We therefore emit exactly the fresh record set (no leftover
    old rows), which makes the merge fully idempotent — re-running converges to
    the same DB instead of accreting duplicates.
    """
    existing = {"records": []}
    if os.path.exists(db_path):
        existing = json.load(open(db_path, encoding="utf-8"))

    # Index old enrichment by several keys for robust matching.
    old_by_norm_year = {}
    old_by_norm = {}
    old_by_doi = {}
    for old in existing.get("records", []):
        nt = wikilib.normalize_title(old.get("title"))
        if nt:
            old_by_norm_year.setdefault((nt, old.get("year")), old)
            old_by_norm.setdefault(nt, old)
        if old.get("doi"):
            old_by_doi.setdefault(old["doi"], old)

    ENRICH = ("scope", "curated_as")
    used_keys = {}
    merged = []
    for rec in sorted(records.values(), key=lambda r: -r["cited_count"]):
        nt = wikilib.normalize_title(rec["title"])
        old = (
            old_by_norm_year.get((nt, rec.get("year")))
            or (old_by_doi.get(rec["doi"]) if rec.get("doi") else None)
            or old_by_norm.get(nt)
        )
        if old:
            for f in ENRICH:
                if old.get(f) is not None:
                    rec[f] = old[f]
            if not rec.get("doi") and old.get("doi"):
                rec["doi"] = old["doi"]
        # Always (re)derive venue tier/normalization from the allow-list so the
        # whole DB is tiered consistently; keep a curated normalization if the
        # classifier only knows the venue as "other".
        label, tier = wikilib.classify_venue(rec.get("venue"))
        if tier and tier != "other":
            rec["venue_normalized"] = label
            rec["venue_tier"] = tier
        elif not rec.get("venue_tier"):
            rec["venue_normalized"] = rec.get("venue_normalized") or label
            rec["venue_tier"] = tier
        rec.pop("_dedup_key", None)
        # Guarantee key uniqueness (truncated slugs can collide across works).
        base = rec["key"]
        if base in used_keys:
            used_keys[base] += 1
            rec["key"] = f"{base}-{used_keys[base]}"
        else:
            used_keys[base] = 1
        merged.append(rec)

    merged.sort(key=lambda r: (-r.get("cited_count", 0), -(int(r["year"]) if (r.get("year") or "").isdigit() else 0)))
    return existing, merged


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", metavar="PATH", help="write the freshly-mined records (relative → .curation-out/)")
    ap.add_argument("--merge", metavar="DB.json", help="idempotently merge into an existing reference-database.json (in place)")
    args = ap.parse_args(argv)

    slug_map = wikilib.folder_to_slug_map()
    per_folder, skipped = mine_all()
    records, total_strings = dedup(per_folder, slug_map)

    print(f"Parses with references: {len(per_folder)}")
    print(f"Skipped parses: {len(skipped)}")
    for f, why in skipped:
        print(f"  SKIP: {f}  ({why})")
    print(f"Reference strings parsed: {total_strings}")
    print(f"Unique references after dedup: {len(records)}")
    ge2 = sum(1 for r in records.values() if r["cited_count"] >= 2)
    ge3 = sum(1 for r in records.values() if r["cited_count"] >= 3)
    print(f"Cited by >=2 corpus papers: {ge2}")
    print(f"Cited by >=3 corpus papers: {ge3}")

    if args.json:
        out = args.json if os.path.isabs(args.json) else os.path.join(wikilib.scratch_dir(), args.json)
        json.dump(
            {"per_folder": per_folder, "skipped": skipped,
             "records": list(records.values()),
             "slug_map": slug_map, "total_strings": total_strings},
            open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"mined -> {out}")

    if args.merge:
        meta, merged = merge_into_db(records, args.merge)
        meta["records"] = merged
        meta["generated"] = datetime.date.today().isoformat()
        meta["parses_mined"] = len(per_folder)
        meta["distinct_papers"] = len(set(slug_map.get(f, f) for f in per_folder))
        meta["reference_strings"] = total_strings
        meta["unique_references"] = len(merged)
        json.dump(meta, open(args.merge, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"merged DB ({len(merged)} records) -> {args.merge}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
