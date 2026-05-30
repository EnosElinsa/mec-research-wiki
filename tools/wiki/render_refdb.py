"""Render the human-readable reference-database.md from reference-database.json.

Keeps the published markdown a faithful, regenerable view of the JSON DB so the
two never drift. Emits the frontmatter, a Summary block, and the "most-cited"
centrality table (cited_count >= a threshold), sorted by in-corpus citation
frequency. Faithful fields only — missing values render as ``n/a``.

Usage:
  python tools/wiki/render_refdb.py            # render next to the .json
  python tools/wiki/render_refdb.py --min 2    # centrality table threshold
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import sys

import wikilib


def _volnopp(r):
    bits = []
    if r.get("vol"):
        bits.append(f"vol. {r['vol']}")
    if r.get("no"):
        bits.append(f"no. {r['no']}")
    if r.get("pp"):
        bits.append(f"pp. {r['pp']}")
    return ", ".join(bits) if bits else "n/a"


def _venue(r):
    vn = r.get("venue_normalized")
    v = r.get("venue")
    if vn and v and vn != v and v not in vn:
        return f"{v} — {vn}"
    return vn or v or "n/a"


def _cell(s):
    return (s or "n/a").replace("|", "\\|").replace("\n", " ")


def _curated(r):
    return f"yes → {r['curated_as']}" if r.get("curated_as") else "no"


def render(db, min_cited):
    gen = db.get("generated") or datetime.date.today().isoformat()
    recs = db["records"]
    ge2 = sum(1 for r in recs if r["cited_count"] >= 2)
    ge3 = sum(1 for r in recs if r["cited_count"] >= 3)
    distinct = db.get("distinct_papers")
    out = []
    out.append("---")
    out.append("type: reference-database")
    out.append("title: Master Reference Database")
    out.append("tags: [mec, references, citation-mining]")
    out.append("---")
    out.append("")
    out.append("# Master Reference Database")
    out.append("")
    out.append(f"_Generated: {gen}_ · Mined from the `# REFERENCES` sections of all parsed papers in `raw/sources/`.")
    out.append("")
    out.append("Deduplicated by normalized title (+ author-surname/year). `cited_by` lists the curated wiki sources (or raw folders) whose reference list contains the work; `cited_count` is its citation frequency **within this corpus** (a centrality/depth signal). Fields are faithful to the parses — missing fields are `n/a`, never guessed.")
    out.append("")
    out.append("## Summary")
    out.append("")
    out.append(f"- **Parses mined:** {db.get('parses_mined')} `full.md` files → {distinct} distinct curated/raw papers.")
    out.append(f"- **Reference strings parsed:** {db.get('reference_strings')}.")
    out.append(f"- **Unique references after dedup:** {db.get('unique_references')}.")
    out.append(f"- **Cited by >= 2 corpus papers:** {ge2} (foundational / depth signal).")
    out.append(f"- **Cited by >= 3 corpus papers:** {ge3}.")
    out.append("")
    out.append(f"## Most-cited references (centrality ranking, cited_count >= {min_cited})")
    out.append("")
    out.append("Sorted by in-corpus citation frequency. These are the works the curated corpus leans on most.")
    out.append("")
    out.append("| cited_count | Year | Title | Authors | Venue | vol/no/pp | cited_by | curated? |")
    out.append("|---|---|---|---|---|---|---|---|")
    top = [r for r in recs if r["cited_count"] >= min_cited]
    top.sort(key=lambda r: (-r["cited_count"], -(int(r["year"]) if (r.get("year") or "").isdigit() else 0)))
    for r in top:
        out.append("| {cc} | {yr} | {title} | {auth} | {ven} | {vnp} | {cb} | {cur} |".format(
            cc=r["cited_count"],
            yr=_cell(r.get("year")),
            title=_cell(r.get("title")),
            auth=_cell(r.get("authors")),
            ven=_cell(_venue(r)),
            vnp=_cell(_volnopp(r)),
            cb=_cell(", ".join(r.get("cited_by", []))),
            cur=_cell(_curated(r)),
        ))
    out.append("")
    out.append(f"_Full record set (all {len(recs)} unique references, including singletons) lives in the companion `reference-database.json`._")
    out.append("")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", default=None, help="path to reference-database.json")
    ap.add_argument("--out", default=None, help="path to reference-database.md")
    ap.add_argument("--min", type=int, default=2, help="min cited_count for the centrality table (default 2)")
    args = ap.parse_args(argv)

    refs_dir = os.path.join(wikilib.wiki_dir(), "references")
    db_path = args.db or os.path.join(refs_dir, "reference-database.json")
    out_path = args.out or os.path.join(refs_dir, "reference-database.md")
    db = json.load(open(db_path, encoding="utf-8"))
    text = render(db, args.min)
    open(out_path, "w", encoding="utf-8").write(text)
    print(f"rendered {len([r for r in db['records'] if r['cited_count'] >= args.min])} most-cited rows -> {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
