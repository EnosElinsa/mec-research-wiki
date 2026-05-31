"""Scan every wiki page EXCEPT log.md for curation process-narration.

Process bookkeeping (batch numbers, run labels, "this/prior/next pass",
dated-run references) belongs only in wiki/log.md and git commit messages; all
other pages must read as evergreen reference material. This tool finds leaks so
the auditor can rewrite them.

Genuine domain uses of "batch" (ML mini-batch sizes, a paper's own
batch-processing method) are deliberately NOT flagged.

Usage:
  python tools/wiki/process_refs.py
  python tools/wiki/process_refs.py --json process_refs.json
Exit code is 1 when any offending reference is found (0 otherwise).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

import wikilib

OFFENDING = [
    re.compile(r"\bbatch[-\s]?\d+\s*/\s*\d+\b", re.I),          # batch 3/8, batch-3/8
    re.compile(r"\bbatch[-\s]\d+\b(?!\s*(?:size|,|\.|\d))", re.I),  # batch-3 / batch 5 (process)
    re.compile(r"\bmulti-batch\b", re.I),
    re.compile(r"\bthis batch\b", re.I),
    re.compile(r"\bwithin-batch\b", re.I),
    re.compile(r"\bsame batch\b", re.I),                         # "(in) this same batch"
    re.compile(r"\b(?:in|within|during|across) (?:this|that|the same) batch\b", re.I),
    re.compile(r"\bthis curation\b", re.I),
    re.compile(r"\bcuration pass\b", re.I),
    re.compile(r"\bsynthesis pass\b", re.I),
    re.compile(r"\bin this pass\b", re.I),
    re.compile(r"\bthe (?:next|previous|prior|last|earlier|first|second|third|2026)[\w\s-]*?pass\b", re.I),
    re.compile(r"\b(?:next|prior|previous|audit|follow-up) pass\b", re.I),
    re.compile(r"\bnewly (?:confirmed|added|curated|synthesized)\b", re.I),
    re.compile(r"\d{4}-\d{2}-\d{2}\s+batch\b", re.I),
    re.compile(r"\bthe \d{4}-\d{2}-\d{2} (?:batch|pass)\b", re.I),
    re.compile(r"\b(?:first|second|third) 2026-\d{2}-\d{2} batch\b", re.I),
    re.compile(r"\bfor this curation\b", re.I),
    re.compile(r"\b\d+-source snapshot\b", re.I),
    re.compile(r"\bpaper\s+#\d+\b", re.I),                       # "paper #8", "paper #10" (curation ingest order)
    # Forward-looking curation-workflow placement ("future X sources should land here",
    # "subsequent sources should be tagged ...") — an instruction to a later curation run.
    # The noun is restricted to curation vocabulary (sources/pages/entity-pages), so a
    # paper's own "future work" / "future research" (noun = work/research) is NOT flagged.
    re.compile(r"\b(?:should|will|would)\s+land here\b", re.I),
    re.compile(r"\b(?:future|subsequent|later|upcoming|forthcoming)\s+(?:[\w-]+\s+){0,3}(?:sources?|pages?|entity pages?)\s+(?:should|will|would|must|land|belong|be\s+tagged)\b", re.I),
]

# Legit ML / domain contexts we must NOT flag.
ML_OK = re.compile(r"batch[\s-]?(?:size|128|256|512|64|32|1024|of \d)", re.I)


def scan():
    results = {}
    for p in wikilib.md_files(wikilib.wiki_dir()):
        if os.path.basename(p) == "log.md":
            continue
        hits = []
        for i, ln in enumerate(wikilib.read_text(p).splitlines(), 1):
            for rx in OFFENDING:
                m = rx.search(ln)
                if not m:
                    continue
                seg = ln[max(0, m.start() - 15) : m.end() + 15]
                if ML_OK.search(seg):
                    continue
                hits.append((i, m.group(0), ln.strip()[:160]))
                break
        if hits:
            results[os.path.relpath(p, wikilib.wiki_dir())] = hits
    return results


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", metavar="PATH", help="write a JSON report (relative paths land in .curation-out/)")
    args = ap.parse_args(argv)

    results = scan()
    total = sum(len(v) for v in results.values())
    print(f"FILES AFFECTED: {len(results)}  | TOTAL HITS: {total}")
    print("=" * 80)
    for f, hits in sorted(results.items()):
        print(f"\n### {f}  ({len(hits)} hits)")
        for ln, tok, ctx in hits:
            print(f"  L{ln}: [{tok}]  {ctx}")

    if args.json:
        out = (
            args.json
            if os.path.isabs(args.json)
            else os.path.join(wikilib.scratch_dir(), args.json)
        )
        json.dump(
            {f: [h[0] for h in hits] for f, hits in results.items()},
            open(out, "w", encoding="utf-8"),
            indent=2,
        )
        print(f"\nreport -> {out}")
    return 1 if results else 0


if __name__ == "__main__":
    sys.exit(main())
