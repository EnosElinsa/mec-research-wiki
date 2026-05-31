#!/usr/bin/env python3
"""Audit YAML frontmatter validity and tag/type consistency across wiki pages.

The auditor repeatedly needs to confirm that every page carries valid, complete
frontmatter for its type, and that house tag conventions hold (e.g. a source
page must carry the ``source`` tag, a finding must carry ``source`` /
``confidence``). Doing that with one-off ``Get-ChildItem | ForEach`` /
``Select-String`` loops is exactly the recurring structured check the toolkit
exists to absorb, so it lives here as a parameterized, exit-coded CLI.

For each catalogue-able page under ``wiki/`` it checks:

  * frontmatter block is present and parseable (``---`` ... ``---``);
  * required-for-all keys exist: ``type``, ``title``, ``tags``, ``created``,
    ``updated``;
  * ``type`` matches the page's directory (e.g. a file in ``wiki/sources/`` has
    ``type: source``);
  * an ``# H1`` heading is present in the body;
  * type-specific keys/tags (see ``TYPE_RULES``): source pages carry the
    ``source`` tag and ``authors`` / ``year`` / ``url`` / ``venue`` keys;
    entity pages carry the ``author`` tag; findings carry ``source`` +
    ``confidence``; synthesis pages carry the ``synthesis`` tag.
  * ``related:`` contains no self-reference (a page linking to its own slug).

This is a *lint*, not a correctness oracle: it verifies that fields are present
and internally consistent, never that a DOI/venue/number is factually right
(that stays a human, parse-grounded judgement). Missing/empty values for the
optional source keys (``year``/``url``/``venue`` may legitimately be empty or
``not in parse``) are reported as INFO, not failures.

Run from the repo root:  ``python tools/wiki/frontmatter_audit.py``
Exit code is non-zero if any page has a structural frontmatter error.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

import wikilib


# Page-type -> rules. ``req_keys`` are frontmatter keys that must be present
# and non-empty; ``req_tags`` are tags that must appear in the ``tags`` list;
# ``soft_keys`` must be present but may be empty / "not in parse".
TYPE_RULES = {
    "source": {
        "req_tags": {"source"},
        "soft_keys": {"authors", "year", "url", "venue"},
    },
    "concept": {"req_tags": set(), "soft_keys": set()},
    "entity": {"req_tags_any": {"author", "tool"}, "soft_keys": set()},
    "finding": {"req_keys": {"source", "confidence"}, "req_tags": set(), "soft_keys": set()},
    "synthesis": {"req_tags": {"synthesis"}, "soft_keys": set()},
    "comparison": {"req_tags": set(), "soft_keys": set()},
    "methodology": {"req_tags": set(), "soft_keys": set()},
    "query": {"req_tags": set(), "soft_keys": set()},
    "thesis": {"req_tags": set(), "soft_keys": set()},
}

# Directory name (under wiki/) -> the singular ``type`` value its pages declare.
DIR_TO_TYPE = {
    "sources": "source",
    "concepts": "concept",
    "entities": "entity",
    "findings": "finding",
    "synthesis": "synthesis",
    "comparisons": "comparison",
    "methodology": "methodology",
    "queries": "query",
    "thesis": "thesis",
}

REQUIRED_FOR_ALL = ["type", "title", "tags", "created", "updated"]

# Meta docs / scaffolding that are not typed wiki pages.
DEFAULT_IGNORE = {"index", "overview", "log", "purpose", "readme", "schema", "full"}

_FM = re.compile(r"^\ufeff?---\s*\n(.*?)\n---\s*(?:\n|$)", re.S)
_H1 = re.compile(r"(?m)^#\s+\S")


def _front_matter(text: str) -> str | None:
    m = _FM.match(text)
    return m.group(1) if m else None


def _scalar(fm: str, key: str) -> str | None:
    """Value of a top-level ``key:`` scalar in the frontmatter, or None."""
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.*)$", fm)
    if not m:
        return None
    return m.group(1).strip()


def _has_key(fm: str, key: str) -> bool:
    return re.search(rf"(?m)^{re.escape(key)}:", fm) is not None


def _tags(fm: str) -> list[str]:
    """Parse ``tags:`` whether inline ``[a, b]`` or a YAML block list."""
    inline = re.search(r"(?m)^tags:\s*\[([^\]]*)\]\s*$", fm)
    if inline:
        return [t.strip().strip("'\"") for t in inline.group(1).split(",") if t.strip()]
    block = re.search(r"(?m)^tags:\s*\n((?:[ \t]*-[ \t]*.+\n?)+)", fm)
    if block:
        return [re.sub(r"^[ \t]*-[ \t]*", "", ln).strip().strip("'\"")
                for ln in block.group(1).splitlines() if ln.strip()]
    return []


def _value_empty(v: str | None) -> bool:
    if v is None:
        return True
    s = v.strip().strip("'\"").strip()
    return s in ("", "[]", "~", "null", "None")


def audit_page(path: str, ignore: set[str]) -> list[str]:
    """Return a list of structural errors for one page (empty == clean)."""
    slug = os.path.splitext(os.path.basename(path))[0]
    if slug.lower() in ignore or slug.startswith("MinerU_markdown_"):
        return []
    parent = os.path.basename(os.path.dirname(path))
    expected_type = DIR_TO_TYPE.get(parent)
    if expected_type is None:
        return []  # not a typed wiki page (e.g. references/, stray docs)

    text = wikilib.read_text(path)
    fm = _front_matter(text)
    if fm is None:
        return ["no parseable frontmatter block"]

    errors: list[str] = []

    for key in REQUIRED_FOR_ALL:
        if not _has_key(fm, key):
            errors.append(f"missing required key '{key}'")
        elif key != "tags" and _value_empty(_scalar(fm, key)):
            errors.append(f"empty required key '{key}'")

    declared = _scalar(fm, "type")
    if declared is not None:
        declared = declared.strip().strip("'\"")
        if declared != expected_type:
            errors.append(f"type '{declared}' != expected '{expected_type}' for wiki/{parent}/")

    if not _H1.search(text):
        errors.append("no '# H1' heading in body")

    rules = TYPE_RULES.get(expected_type, {})
    tags = set(_tags(fm))
    for t in rules.get("req_tags", set()):
        if t not in tags:
            errors.append(f"missing required tag '{t}'")
    any_tags = rules.get("req_tags_any", set())
    if any_tags and not (tags & any_tags):
        errors.append(f"missing one of required tags {sorted(any_tags)}")
    for k in rules.get("req_keys", set()):
        if not _has_key(fm, k) or _value_empty(_scalar(fm, k)):
            errors.append(f"missing required key '{k}'")

    # Self-reference in related: a page should not list its own slug.
    rel_block = re.search(r"(?m)^related:\s*\n((?:[ \t]*-[ \t]*.+\n?)+)", fm)
    rel_inline = re.search(r"(?m)^related:\s*\[([^\]]*)\]", fm)
    rel_text = (rel_block.group(1) if rel_block else "") + (rel_inline.group(1) if rel_inline else "")
    if slug in set(wikilib.iter_wikilinks(rel_text)) or re.search(rf"(?<![\w-]){re.escape(slug)}(?![\w-])", rel_text):
        errors.append("related: contains a self-reference")

    return errors


def soft_notes(path: str, ignore: set[str]) -> list[str]:
    """Non-failing INFO notes (e.g. source soft keys absent/empty)."""
    slug = os.path.splitext(os.path.basename(path))[0]
    if slug.lower() in ignore or slug.startswith("MinerU_markdown_"):
        return []
    parent = os.path.basename(os.path.dirname(path))
    expected_type = DIR_TO_TYPE.get(parent)
    if expected_type is None:
        return []
    fm = _front_matter(wikilib.read_text(path))
    if fm is None:
        return []
    notes = []
    for k in TYPE_RULES.get(expected_type, {}).get("soft_keys", set()):
        if not _has_key(fm, k):
            notes.append(f"soft key '{k}' absent")
        elif _value_empty(_scalar(fm, k)):
            notes.append(f"soft key '{k}' empty (ok if 'not in parse')")
    return notes


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--type", dest="only_type", default=None,
                    help="restrict to one page type (e.g. 'source', 'finding').")
    ap.add_argument("--show-soft", action="store_true",
                    help="also print non-failing INFO notes (empty source soft keys).")
    ap.add_argument("--ignore", nargs="*", default=None,
                    help="page slugs (lowercase) to skip; defaults to meta docs + scaffolding.")
    ap.add_argument("--json", dest="json_path", default=None,
                    help="write a machine-readable report to PATH "
                    "(relative paths land in .curation-out/).")
    args = ap.parse_args(argv)

    ignore = set(args.ignore) if args.ignore is not None else set(DEFAULT_IGNORE)
    only = args.only_type

    failures: dict[str, list[str]] = {}
    soft: dict[str, list[str]] = {}
    checked = 0
    for p in wikilib.md_files(wikilib.wiki_dir()):
        parent = os.path.basename(os.path.dirname(p))
        if parent not in DIR_TO_TYPE:
            continue
        if only and DIR_TO_TYPE[parent] != only:
            continue
        slug = os.path.splitext(os.path.basename(p))[0]
        if slug.lower() in ignore or slug.startswith("MinerU_markdown_"):
            continue
        checked += 1
        errs = audit_page(p, ignore)
        if errs:
            failures[slug] = errs
        if args.show_soft:
            ns = soft_notes(p, ignore)
            if ns:
                soft[slug] = ns

    print("=" * 70)
    print(f"FRONTMATTER AUDIT: {checked} pages checked"
          + (f" (type={only})" if only else ""))
    print("=" * 70)
    if failures:
        print(f"PAGES WITH ERRORS: {len(failures)}")
        for slug in sorted(failures):
            print(f"  {slug}")
            for e in failures[slug]:
                print(f"      - {e}")
    else:
        print("PAGES WITH ERRORS: 0  (all frontmatter valid)")

    if args.show_soft and soft:
        print(f"\nINFO (non-failing) — soft keys absent/empty on {len(soft)} pages:")
        for slug in sorted(soft):
            print(f"  {slug}: {'; '.join(soft[slug])}")

    if args.json_path:
        out = args.json_path
        if not os.path.isabs(out):
            out = os.path.join(wikilib.scratch_dir(), out)
        with open(out, "w", encoding="utf-8") as fh:
            json.dump({"checked": checked, "failures": failures, "soft": soft}, fh, indent=2)
        print(f"\nReport written to {out}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
