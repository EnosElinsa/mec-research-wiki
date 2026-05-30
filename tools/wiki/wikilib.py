"""Shared helpers for the MEC wiki maintenance toolkit.

This module is the common foundation for every script under ``tools/wiki/``.
It is path-agnostic (it discovers the repo root by walking up from this file),
so the tools work regardless of where the repo is checked out.

Design rules for this toolkit (see tools/wiki/README.md):
  * Reusable, parameterized logic lives here and in the sibling CLI scripts —
    NOT as one-off scripts in ``.curation-out/``.
  * ``.curation-out/`` is gitignored scratch: only transient state / report
    files belong there, never the reusable code.
  * Prefer extending these functions over copy-pasting a new variant.
"""

from __future__ import annotations

import os
import re
import glob

# --- repo layout -----------------------------------------------------------


def repo_root() -> str:
    """Return the repo root by walking up until we find ``wiki`` + ``raw``."""
    here = os.path.dirname(os.path.abspath(__file__))
    cur = here
    while True:
        if os.path.isdir(os.path.join(cur, "wiki")) and os.path.isdir(
            os.path.join(cur, "raw")
        ):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:  # reached filesystem root
            # Fall back to two levels up from tools/wiki/.
            return os.path.dirname(os.path.dirname(here))
        cur = parent


def wiki_dir() -> str:
    return os.path.join(repo_root(), "wiki")


def raw_sources_dir() -> str:
    return os.path.join(repo_root(), "raw", "sources")


def scratch_dir(ensure: bool = True) -> str:
    """The gitignored ``.curation-out/`` folder for transient state/reports."""
    d = os.path.join(repo_root(), ".curation-out")
    if ensure:
        os.makedirs(d, exist_ok=True)
    return d


# Wiki page type -> subdirectory under wiki/
PAGE_TYPES = [
    "sources",
    "concepts",
    "entities",
    "findings",
    "synthesis",
    "comparisons",
    "methodology",
    "queries",
    "thesis",
    "references",
]


# --- file enumeration ------------------------------------------------------


def md_files(root: str | None = None):
    """All .md files under ``root`` (default: whole repo), recursively.

    Skips the gitignored scratch dir so its drafts never pollute results.
    """
    root = root or repo_root()
    out = []
    for p in glob.glob(os.path.join(root, "**", "*.md"), recursive=True):
        if os.sep + ".curation-out" + os.sep in p:
            continue
        out.append(p)
    return out


def read_text(path: str) -> str:
    return open(path, encoding="utf-8", errors="replace").read()


def page_slugs(root: str | None = None) -> set[str]:
    """The set of resolvable wikilink targets: every .md basename in the repo
    (Obsidian resolves links by basename, including root files like purpose.md)."""
    return {os.path.splitext(os.path.basename(p))[0] for p in md_files(root)}


def raw_folders() -> list[str]:
    raw = raw_sources_dir()
    return sorted(d for d in os.listdir(raw) if os.path.isdir(os.path.join(raw, d)))


# --- wikilink parsing (Obsidian-faithful) ----------------------------------

_CODE_SPAN = re.compile(r"`[^`]*`")
_LINK = re.compile(r"\[\[([^\]]+)\]\]")


def iter_wikilinks(text: str):
    """Yield resolved link targets from ``text``, mirroring Obsidian:
    inline code spans are stripped, ``\\|`` table-escapes handled, and the
    alias / heading suffix removed so only the target basename remains."""
    stripped = _CODE_SPAN.sub("", text)
    for raw in _LINK.findall(stripped):
        raw = raw.replace("\\|", "|")
        target = raw.split("|")[0].split("#")[0].strip().rstrip("\\").strip()
        if target:
            yield target


# --- raw/sources reference parsing -----------------------------------------

_RAW_REF = re.compile(r"raw/sources/([^/`'\"\)\]]+)")


def referenced_raw_folders(root: str | None = None) -> set[str]:
    """Raw-source folder names referenced by any wiki page (via the
    ``raw/sources/<Folder>`` paths in Raw-artifacts blocks).

    Documentation/tooling files use ``raw/sources/<Folder>`` / ``<slug>`` as
    placeholders, and the toolkit's own files live under ``tools/``; both are
    skipped so they don't show up as phantom broken references.
    """
    refs: set[str] = set()
    for p in md_files(root):
        if os.sep + "tools" + os.sep in p:
            continue
        for m in _RAW_REF.findall(read_text(p)):
            tok = m.strip()
            # Skip obvious placeholders/prose, not real folder names.
            if not tok or tok.startswith("<") or "<" in tok or ">" in tok or "*" in tok:
                continue
            refs.add(tok)
    return refs
