#!/usr/bin/env python3
"""Cross-check entity-page author rosters against source-page author lists.

For every ``wiki/entities/*.md`` page (an author entity, i.e. tagged ``author``)
this reconciles the roster of sources the page *claims* the author contributed
to against the ground-truth ``authors:`` frontmatter of the ``wiki/sources/*``
pages, in BOTH directions:

  * CLAIMED-BUT-ABSENT: the entity page links a source whose author list does
    not contain a name matching the entity (a roster over-claim).
  * PRESENT-BUT-UNLISTED: a corpus source lists an author whose name matches the
    entity, but the entity page does not link that source (a possible omission).

Name matching is deliberately conservative and reported in graded strengths so
a human can judge namesakes (the tool NEVER decides identity):
  * strict   -> normalized full-name equality (case/punct/hyphen-insensitive).
  * respaced -> identical once interior spaces are removed ("Li Ping Qian" ==
                "Liping Qian"); a Chinese given-name spacing variant, treated as
                strong as strict for over-claim suppression but reported so it
                stays visible.
  * loose    -> same first AND last token but not strict/respaced (initials
                differ); flagged separately because shared Chinese surnames +
                given names make loose matches a frequent namesake signal.

This is an aid for the auditor, not an oracle: PRESENT-BUT-UNLISTED hits on
common names (e.g. "Wei Zhang", "Jie Xu", "Ying Chen") are very often distinct
people and must be confirmed against the parses before any edit. Do not
add/remove roster entries on a tool match alone.

Exit code is always 0 (advisory report); use ``--json`` for a machine report.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wikilib  # noqa: E402


def _norm_name(name: str) -> str:
    """Case/punct/hyphen-insensitive normal form: 'Victor C. M. Leung' and
    'Victor C.-M.Leung' both -> 'victor c m leung'."""
    n = name.lower().replace("–", "-").replace("—", "-")
    n = re.sub(r"[.\-]", " ", n)
    n = re.sub(r"[^a-z0-9 ]+", " ", n)
    return re.sub(r"\s+", " ", n).strip()


def _front_value(text: str, key: str) -> str | None:
    """Return the raw value of a single-line frontmatter ``key:`` (first hit)."""
    m = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", text)
    return m.group(1).strip() if m else None


def _parse_authors(text: str) -> list[str]:
    """Parse an ``authors:`` frontmatter value, handling BOTH YAML styles:
      * inline flow list:  authors: ["A", "B", "C"]  (quoted or bare)
      * block list:        authors:\\n  - A\\n  - B\\n
    Only the frontmatter block (between the first two ``---`` fences) is
    considered so prose ``- `` bullets later in the page are never slurped."""
    # Restrict to the YAML frontmatter block.
    fm = text
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            fm = text[3:end]
    m = re.search(r"(?m)^authors:[ \t]*(.*)$", fm)
    if not m:
        return []
    inline = m.group(1).strip()
    out: list[str] = []
    if inline:
        # Inline flow list (or a single bare value).
        inner = inline.lstrip("[").rstrip("]")
        for tok in inner.split(","):
            tok = tok.strip().strip('"').strip("'").strip()
            if tok:
                out.append(tok)
        return out
    # Block list: consume subsequent ``  - item`` lines.
    rest = fm[m.end():].splitlines()
    for line in rest:
        if re.match(r"^[ \t]*-\s+", line):
            tok = re.sub(r"^[ \t]*-\s+", "", line).strip().strip('"').strip("'").strip()
            if tok:
                out.append(tok)
        elif line.strip() == "":
            continue
        else:
            break  # next frontmatter key
    return out


def _title(text: str, fallback: str) -> str:
    t = _front_value(text, "title")
    if t:
        return t.strip().strip('"').strip("'")
    return fallback


def build_source_authors() -> dict[str, list[str]]:
    src_dir = os.path.join(wikilib.wiki_dir(), "sources")
    out: dict[str, list[str]] = {}
    for fn in os.listdir(src_dir):
        if not fn.endswith(".md"):
            continue
        slug = fn[:-3]
        out[slug] = _parse_authors(wikilib.read_text(os.path.join(src_dir, fn)))
    return out


def is_author_entity(text: str) -> bool:
    tags = _front_value(text, "tags") or ""
    return "author" in tags


def match_strength(entity_norm: str, author_norm: str) -> str | None:
    if entity_norm == author_norm:
        return "strict"
    # Respacing variant: identical once interior spaces are removed
    # ("li ping qian" == "liping qian"). A Chinese given-name spacing variant;
    # as strong as strict for over-claim suppression. Guard against trivially
    # collapsing two distinct single-token names.
    if entity_norm.replace(" ", "") == author_norm.replace(" ", "") and " " in (
        entity_norm + author_norm
    ):
        return "respaced"
    et, at = entity_norm.split(), author_norm.split()
    if len(et) >= 2 and len(at) >= 2 and et[0] == at[0] and et[-1] == at[-1]:
        return "loose"
    return None


def _roster_region(text: str) -> str:
    """The part of an entity page that constitutes its *roster claims*: the
    frontmatter ``related:`` + intro + bulleted source list, i.e. everything
    before the first ``## Contributions`` heading. The Contributions section is
    free-form editorial commentary that often contrast-mentions sources the
    author did NOT write ("anchored by different sources [[x]]"); counting those
    wikilinks as roster claims yields false claimed-but-absent over-claims.
    Falls back to the whole page when there is no such heading."""
    m = re.search(r"(?im)^##\s+contributions\b", text)
    return text[: m.start()] if m else text


def audit(entity_slugs: list[str] | None):
    src_authors = build_source_authors()
    # Pre-normalize source author lists.
    src_norm = {s: [(_norm_name(a), a) for a in authors] for s, authors in src_authors.items()}
    source_slugset = set(src_authors)

    ent_dir = os.path.join(wikilib.wiki_dir(), "entities")
    reports = []
    for fn in sorted(os.listdir(ent_dir)):
        if not fn.endswith(".md"):
            continue
        slug = fn[:-3]
        if entity_slugs is not None and slug not in entity_slugs:
            continue
        text = wikilib.read_text(os.path.join(ent_dir, fn))
        if not is_author_entity(text):
            continue  # tool entities (pytorch) have no author roster
        ename = _title(text, slug)
        enorm = _norm_name(ename)

        # Roster claims come from the roster region only (excludes the editorial
        # "## Contributions" commentary). The full-page link set still suppresses
        # present-but-unlisted hits, so a source mentioned only in Contributions
        # is neither a false over-claim nor a false omission.
        claimed = {t for t in wikilib.iter_wikilinks(_roster_region(text)) if t in source_slugset}
        linked_anywhere = {t for t in wikilib.iter_wikilinks(text) if t in source_slugset}

        claimed_but_absent = []
        for s in sorted(claimed):
            strengths = {match_strength(enorm, an) for an, _ in src_norm[s]}
            strengths.discard(None)
            if not strengths:
                claimed_but_absent.append(s)

        present_but_unlisted = []
        for s, authors in src_norm.items():
            if s in linked_anywhere:
                continue
            best = None
            for an, orig in authors:
                ms = match_strength(enorm, an)
                if ms == "strict":
                    best = ("strict", orig)
                    break
                if ms == "loose" and best is None:
                    best = ("loose", orig)
            if best:
                present_but_unlisted.append({"source": s, "strength": best[0], "author_as_written": best[1]})

        reports.append({
            "entity": slug,
            "name": ename,
            "claimed_count": len(claimed),
            "claimed_but_absent": claimed_but_absent,
            "present_but_unlisted": present_but_unlisted,
        })
    return reports


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", help="file of entity slugs (one per line) to limit the report")
    ap.add_argument("--json", dest="json_path", help="write machine report (relative -> .curation-out/)")
    args = ap.parse_args()

    entity_slugs = None
    if args.input:
        with open(args.input, encoding="utf-8") as f:
            entity_slugs = [ln.strip() for ln in f if ln.strip()]

    reports = audit(entity_slugs)

    n_absent = sum(len(r["claimed_but_absent"]) for r in reports)
    n_unlisted = sum(len(r["present_but_unlisted"]) for r in reports)
    print("=" * 70)
    print(f"ENTITY ROSTER AUDIT: {len(reports)} author entities checked")
    print(f"  claimed-but-absent (over-claims): {n_absent}")
    print(f"  present-but-unlisted (possible omissions / namesakes): {n_unlisted}")
    print("=" * 70)
    for r in reports:
        if not r["claimed_but_absent"] and not r["present_but_unlisted"]:
            continue
        print(f"\n[{r['entity']}] {r['name']}  (claims {r['claimed_count']} sources)")
        for s in r["claimed_but_absent"]:
            print(f"  CLAIMED-BUT-ABSENT: {s}")
        for u in r["present_but_unlisted"]:
            print(f"  unlisted ({u['strength']}): {u['source']}  [author as written: {u['author_as_written']}]")

    if args.json_path:
        path = args.json_path
        if not os.path.isabs(path):
            path = os.path.join(wikilib.scratch_dir(), path)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(reports, f, indent=2, ensure_ascii=False)
        print(f"\nreport -> {path}")


if __name__ == "__main__":
    main()
