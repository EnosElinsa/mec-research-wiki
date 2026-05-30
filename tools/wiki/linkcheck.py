"""Obsidian-faithful wikilink integrity check across the whole wiki.

Resolution rules (match Obsidian):
  * links resolve by BASENAME, including root files (``[[purpose]]`` -> purpose.md is valid);
  * inline code spans and ``\\|`` table-escaped aliases are ignored;
  * a heading suffix (``#section``) is stripped before resolving.

Usage:
  python tools/wiki/linkcheck.py                 # report dangling links
  python tools/wiki/linkcheck.py --orphans       # also list orphan pages
  python tools/wiki/linkcheck.py --json out.json # write a machine-readable report
Exit code is 1 when dangling links exist (0 otherwise), so it can gate a commit.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

import wikilib


def find_dangling():
    slugs = wikilib.page_slugs()
    missing: dict[str, list[str]] = {}
    inbound: dict[str, int] = {s: 0 for s in slugs}
    outbound: dict[str, int] = {s: 0 for s in slugs}
    for p in wikilib.md_files():
        slug = os.path.splitext(os.path.basename(p))[0]
        for target in wikilib.iter_wikilinks(wikilib.read_text(p)):
            if target in slugs:
                outbound[slug] = outbound.get(slug, 0) + 1
                inbound[target] = inbound.get(target, 0) + 1
            else:
                rel = os.path.relpath(p, wikilib.repo_root())
                missing.setdefault(target, []).append(rel)
    orphans = sorted(
        s for s in slugs if inbound.get(s, 0) == 0 and outbound.get(s, 0) == 0
    )
    return missing, orphans


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--orphans", action="store_true", help="also list orphan pages")
    ap.add_argument("--json", metavar="PATH", help="write a JSON report to PATH")
    args = ap.parse_args(argv)

    missing, orphans = find_dangling()

    if not missing:
        print("NO DANGLING LINKS (Obsidian-faithful: root indexed, code spans ignored)")
    else:
        print(f"DANGLING TARGETS: {len(missing)}")
        for t, srcs in sorted(missing.items()):
            u = sorted(set(srcs))
            print(f"  [[{t}]]  <- {len(u)} page(s): {u[:6]}")

    if args.orphans:
        print(f"\nORPHAN PAGES (no links in/out): {len(orphans)}")
        for s in orphans:
            print(f"  {s}")

    if args.json:
        out = os.path.join(wikilib.scratch_dir(), args.json) if not os.path.isabs(
            args.json
        ) else args.json
        json.dump(
            {"dangling": {k: sorted(set(v)) for k, v in missing.items()}, "orphans": orphans},
            open(out, "w", encoding="utf-8"),
            indent=2,
        )
        print(f"\nreport -> {out}")

    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
