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
    with open(path, encoding="utf-8", errors="replace") as handle:
        return handle.read()


def page_slugs(root: str | None = None) -> set[str]:
    """The set of resolvable wikilink targets: every .md basename in the repo
    (Obsidian resolves links by basename, including root files like purpose.md)."""
    return {os.path.splitext(os.path.basename(p))[0] for p in md_files(root)}


def wiki_page_index(root: str | None = None) -> dict[str, str]:
    """Index wiki Markdown pages by their Obsidian-resolvable basename.

    ``root`` is the wiki tree itself (default: :func:`wiki_dir`), rather than
    the whole repository.  Obsidian basename resolution is ambiguous when two
    pages share a name, so graph consumers fail closed instead of guessing.
    """
    wiki_root = os.path.abspath(root or wiki_dir())
    index: dict[str, str] = {}
    duplicates: set[str] = set()
    pattern = os.path.join(wiki_root, "**", "*.md")
    for path in sorted(glob.glob(pattern, recursive=True)):
        slug = os.path.splitext(os.path.basename(path))[0]
        if slug in index:
            duplicates.add(slug)
        else:
            index[slug] = os.path.abspath(path)
    if duplicates:
        names = ", ".join(sorted(duplicates))
        raise ValueError(f"duplicate wiki page basename(s): {names}")
    return index


def wikilink_basename(target: str) -> str:
    """Return the basename used for unique wiki-page link resolution."""
    normalized = target.strip().replace("\\", "/").rstrip("/")
    basename = normalized.rsplit("/", 1)[-1]
    if basename.lower().endswith(".md"):
        basename = basename[:-3]
    return basename


def wiki_undirected_edges(
    pages: dict[str, str] | None = None,
    *,
    excluded: set[str] | frozenset[str] | None = None,
) -> set[tuple[str, str]]:
    """Resolve wiki links as a simple undirected graph.

    Only targets in the unique wiki-page index are resolvable.  Excluded
    administrative pages, unresolved links, self-links, repeats, and reciprocal
    mentions do not create graph edges.
    """
    pages = pages if pages is not None else wiki_page_index()
    excluded_slugs = set(excluded or ())
    edges: set[tuple[str, str]] = set()
    for source, path in sorted(pages.items()):
        if source in excluded_slugs:
            continue
        for target in iter_wikilinks(read_text(path)):
            resolved = wikilink_basename(target)
            if (
                not resolved
                or resolved == source
                or resolved in excluded_slugs
                or resolved not in pages
            ):
                continue
            edge = tuple(sorted((source, resolved)))
            edges.add(edge)
    return edges


def raw_folders() -> list[str]:
    raw = raw_sources_dir()
    return sorted(d for d in os.listdir(raw) if os.path.isdir(os.path.join(raw, d)))


# --- wikilink parsing (Obsidian-faithful) ----------------------------------

_LINK = re.compile(r"\[\[([^\]]+)\]\]")
_FENCE_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})([^\r\n]*)$")


def _line_ending(line: str) -> str:
    if line.endswith("\r\n"):
        return "\r\n"
    if line.endswith("\n"):
        return "\n"
    if line.endswith("\r"):
        return "\r"
    return ""


def _strip_fenced_code(text: str) -> str:
    """Remove CommonMark-style backtick and tilde fenced code blocks."""
    rendered: list[str] = []
    fence_character: str | None = None
    fence_length = 0
    for line in text.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        if fence_character is None:
            opening = _FENCE_OPEN.match(content)
            if opening:
                marker, info = opening.groups()
                # CommonMark forbids backticks in a backtick fence's info text.
                if marker[0] != "`" or "`" not in info:
                    fence_character = marker[0]
                    fence_length = len(marker)
                    rendered.append(_line_ending(line))
                    continue
            rendered.append(line)
            continue

        closing = re.fullmatch(
            rf" {{0,3}}{re.escape(fence_character)}{{{fence_length},}}[ \t]*",
            content,
        )
        rendered.append(_line_ending(line))
        if closing:
            fence_character = None
            fence_length = 0
    return "".join(rendered)


def _strip_inline_code(text: str) -> str:
    """Remove Markdown code spans delimited by equal backtick runs."""
    rendered: list[str] = []
    cursor = 0
    while cursor < len(text):
        if text[cursor] != "`":
            rendered.append(text[cursor])
            cursor += 1
            continue
        delimiter_end = cursor
        while delimiter_end < len(text) and text[delimiter_end] == "`":
            delimiter_end += 1
        delimiter = text[cursor:delimiter_end]
        closing = -1
        search = delimiter_end
        while search < len(text):
            run_start = text.find("`", search)
            if run_start < 0:
                break
            run_end = run_start
            while run_end < len(text) and text[run_end] == "`":
                run_end += 1
            if run_end - run_start == len(delimiter):
                closing = run_start
                break
            search = run_end
        if closing < 0:
            rendered.append(delimiter)
            cursor = delimiter_end
            continue
        cursor = closing + len(delimiter)
    return "".join(rendered)


def iter_wikilinks(text: str):
    """Yield resolved link targets from ``text``, mirroring Obsidian:
    fenced code blocks and inline code spans are stripped, ``\\|`` table-escapes
    handled, and the alias / heading suffix removed so only the target basename
    remains."""
    stripped = _strip_inline_code(_strip_fenced_code(text))
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


# --- IEEE reference-string mining (shared by mec-reference-scout) -----------
#
# These helpers parse the ``# REFERENCES`` section of a raw/sources ``full.md``
# (MinerU markdown) into structured records. They are deliberately conservative:
# a field that is not clearly present is left as ``None`` rather than guessed,
# mirroring the correctness-first stance of the scout agent.

_REF_HEADING = re.compile(r"(?im)^#{1,3}\s*references\s*$")
# A reference entry starts at a line-leading ``[n]`` marker.
_REF_MARKER = re.compile(r"(?m)^[ \t]*\[(\d+)\]\s+")
# Springer/Elsevier fallback: a line-leading ``N. `` numbered marker.
_REF_MARKER_DOT = re.compile(r"(?m)^[ \t]*(\d+)\.\s+")
# Heading that, if it appears after the references heading, ends the block
# (appendix / author biographies that MinerU sometimes keeps inline).
_POST_REF_HEADING = re.compile(r"(?im)^#{1,6}\s+")

# Trailing junk MinerU appends to the FINAL reference entry when no heading
# separates the bibliography from what follows: inline figure markdown, the
# <details>/<summary> wrappers around image captions, and author-biography
# prose. None of these tokens ever occur inside a legitimate IEEE reference
# string, so truncating at the earliest one safely de-contaminates the entry
# without touching well-formed references (and is idempotent on clean input).
_REF_CONTAM = re.compile(
    r"!\[\]\("                                                       # inline image markdown
    r"|</?details>|</?summary>"                                      # MinerU caption wrappers
    r"|\s#{1,6}\s+\w"                                                # embedded heading (e.g. "# Biographies")
    r"|Bi\s?ogra\s?phi\s?es"                                         # OCR-split "Biographies"
    r"|\b(?:Student |Graduate Student |Senior |Life )?(?:Member|Fellow),\s*IEEE\b"  # IEEE bio designations
    r"|\breceived (?:the|his|her|a|an)\b[^.]*\bdegree\b",            # bio sentence opener
    re.I,
)


def strip_ref_contamination(s: str) -> str:
    """Cut a reference string at the first MinerU contamination marker.

    The last entry of a references block frequently absorbs trailing figure
    markdown and author biographies because no markdown heading separates them.
    Those markers never appear inside a real reference, so truncating at the
    earliest one removes the junk without altering well-formed entries.
    Idempotent: clean input is returned unchanged.
    """
    if not s:
        return s
    m = _REF_CONTAM.search(s)
    return s[: m.start()].strip() if m else s

_QUOTED_TITLE = re.compile(r"[“\"]([^“”\"]+?)[”\"]", re.S)
_VOL = re.compile(r"\bvol\.\s*([0-9]+)", re.I)
_NO = re.compile(r"\bno\.\s*([0-9]+)", re.I)
_PP = re.compile(r"\bpp\.\s*([0-9]+(?:\s*[–\-]\s*[0-9]+)?)", re.I)
_PG1 = re.compile(r"\bp\.\s*([0-9]+)", re.I)
_YEAR = re.compile(r"\b(19[5-9][0-9]|20[0-1][0-9]|202[0-6])\b")
_MONTH_YEAR = re.compile(
    r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|Quart|Quarter)\w*\.?,?\s*(19[5-9][0-9]|20[0-1][0-9]|202[0-6])\b",
    re.I,
)
_DOI = re.compile(r"\b(10\.\d{4,9}/[^\s,\"]+)", re.I)
_URL = re.compile(r"https?://[^\s)\]\"]+")


def extract_references_block(text: str) -> str | None:
    """Return the references section of a parse, or ``None`` if absent.

    Primary strategy: the ``# REFERENCES`` / ``## References`` heading, cut at
    the next markdown heading (drops trailing appendices/biographies).
    Fallback (some MinerU parses drop the heading): the final contiguous run of
    line-leading ``[n]`` entry markers near the end of the document.
    """
    m = _REF_HEADING.search(text)
    if m:
        rest = text[m.end():]
        nxt = _POST_REF_HEADING.search(rest)
        return rest[: nxt.start()] if nxt else rest
    # Fallback: locate the last ascending run of [n] markers.
    markers = [(mm.start(), int(mm.group(1))) for mm in _REF_MARKER.finditer(text)]
    if len(markers) < 5:
        return None
    start_idx = len(markers) - 1
    for i in range(len(markers) - 1, 0, -1):
        if markers[i][1] == markers[i - 1][1] + 1:
            start_idx = i - 1
        else:
            break
    # Require the run to actually start near [1]/[2] to avoid false positives.
    if markers[start_idx][1] > 3:
        return None
    return text[markers[start_idx][0]:]


def split_ref_entries(block: str):
    """Split a references block into ``(number, raw_string)`` entries.

    Multi-line entries are re-joined and inner whitespace collapsed. Falls back
    to ``N. `` numbering (Springer/Elsevier style) when no ``[n]`` markers exist.
    """
    parts = _REF_MARKER.split(block)
    # parts = [preamble, num1, body1, num2, body2, ...]
    out = []
    for i in range(1, len(parts) - 1, 2):
        num = int(parts[i])
        body = re.sub(r"\s+", " ", parts[i + 1]).strip()
        body = strip_ref_contamination(body)
        if body:
            out.append((num, body))
    if out:
        return out
    # Fallback: ``N. `` numbered list. Require an ascending run from a low start
    # to avoid splitting on stray sentence-leading numbers.
    marks = [(m.start(), m.end(), int(m.group(1))) for m in _REF_MARKER_DOT.finditer(block)]
    if len(marks) >= 5 and marks[0][2] <= 2:
        for j in range(len(marks)):
            s = marks[j][1]
            e = marks[j + 1][0] if j + 1 < len(marks) else len(block)
            body = re.sub(r"\s+", " ", block[s:e]).strip()
            body = strip_ref_contamination(body)
            if body:
                out.append((marks[j][2], body))
    return out


def parse_ref_entry(raw: str) -> dict:
    """Parse one IEEE-style reference string into fields. Missing → ``None``.

    Never guesses: authors/title/venue/vol/no/pp/year/doi/url are only filled
    when they are unambiguously present in the string.
    """
    # Defensive: de-contaminate even when called directly on a raw string
    # (split_ref_entries already strips, so this is idempotent in the pipeline).
    raw = strip_ref_contamination(raw)
    rec = {
        "authors": None, "title": None, "venue": None,
        "vol": None, "no": None, "pp": None, "year": None,
        "doi": None, "url": None, "raw": raw,
    }
    tm = _QUOTED_TITLE.search(raw)
    if tm:
        rec["title"] = tm.group(1).strip().strip(",.").strip()
        authors = raw[: tm.start()].strip().rstrip(",").strip()
        rec["authors"] = authors or None
        tail = raw[tm.end():].strip()
    else:
        tail = raw
    # venue: text up to the first vol./no./pp./in/2019 etc. signal.
    venue_zone = tail
    cut = re.search(r"(,?\s*(?:\bvol\.|\bno\.|\bpp\.|\bp\.|early access|\b(?:19|20)\d{2}\b|\[Online\]|doi:))", venue_zone, re.I)
    venue = venue_zone[: cut.start()] if cut else venue_zone
    venue = venue.strip().strip(",").strip()
    # Strip a leading "in " for conference proceedings but keep the proc name.
    if venue.lower().startswith("in "):
        venue = venue[3:].strip()
    rec["venue"] = venue or None
    v = _VOL.search(tail)
    if v:
        rec["vol"] = v.group(1)
    n = _NO.search(tail)
    if n:
        rec["no"] = n.group(1)
    p = _PP.search(tail)
    if p:
        rec["pp"] = re.sub(r"\s*", "", p.group(1))
    elif _PG1.search(tail):
        rec["pp"] = _PG1.search(tail).group(1)
    years = _YEAR.findall(raw)
    my = _MONTH_YEAR.search(raw)
    if my:
        rec["year"] = my.group(1)
    elif years:
        # Prefer a year that is NOT part of a page range (avoid pp. 2036–2045).
        pp_years = set()
        if rec.get("pp"):
            pp_years = set(re.findall(r"\b(\d{4})\b", rec["pp"]))
        clean = [y for y in years if y not in pp_years]
        rec["year"] = (clean or years)[-1]
    d = _DOI.search(raw)
    if d:
        rec["doi"] = d.group(1).rstrip(".")
    u = _URL.search(raw)
    if u:
        rec["url"] = u.group(0).rstrip(".")
    return rec


_NORM_PUNCT = re.compile(r"[^a-z0-9 ]+")
_NORM_WS = re.compile(r"\s+")


def normalize_title(title: str | None) -> str:
    """Canonical form for dedup: lowercase, punctuation stripped, ws collapsed."""
    if not title:
        return ""
    t = title.lower().replace("–", "-").replace("—", "-")
    t = _NORM_PUNCT.sub(" ", t)
    return _NORM_WS.sub(" ", t).strip()


_TITLE_KEY_STRIP = re.compile(r"[^a-z0-9]+")


def title_match_key(title: str | None) -> str:
    """Separator-insensitive title key for matching mined refs to curated pages.

    Unlike :func:`normalize_title` (which collapses punctuation to *spaces*),
    this drops every non-alphanumeric character entirely, so word boundaries
    don't matter. This repairs PDF de-hyphenation artifacts where a hyphenated
    word wrapped across a line break and the parser dropped *both* the hyphen
    and the space: e.g. "Relay-Assisted" / "relay assisted" / "relayassisted"
    and "Multi-Agent" / "Multiagent" all collapse to the same key.

    Use this ONLY for curated-vs-mined title matching, never for the in-DB
    dedup (which must keep distinct titles distinct).
    """
    if not title:
        return ""
    return _TITLE_KEY_STRIP.sub("", title.lower())


def author_surname(authors: str | None) -> str:
    """Best-effort first-author surname (last token of the first author)."""
    if not authors:
        return ""
    first = re.split(r",| and |&", authors)[0].strip()
    first = re.sub(r"\bet al\.?", "", first, flags=re.I).strip()
    toks = first.split()
    if not toks:
        return ""
    surname = toks[-1]
    return _NORM_PUNCT.sub("", surname.lower())


def ref_key(authors: str | None, year: str | None, title: str | None) -> str:
    """Stable-ish key ``surname-year-titleslug`` for a new reference record."""
    surname = author_surname(authors) or "anon"
    yr = year or "na"
    norm = normalize_title(title)
    slug_words = []
    length = 0
    for w in norm.split():
        add = (1 if slug_words else 0) + len(w)
        if length + add > 45:
            break
        slug_words.append(w)
        length += add
    slug = "-".join(slug_words) or "untitled"
    return f"{surname}-{yr}-{slug}"


def folder_to_slug_map(root: str | None = None) -> dict:
    """Map each ``raw/sources/<Folder>`` name to its curated wiki slug.

    Built from the ``raw/sources/<Folder>/full.md`` path that each curated
    ``wiki/sources/<slug>.md`` page records in its Raw-artifacts block.
    """
    wiki_sources = os.path.join(wiki_dir(), "sources")
    mapping = {}
    if not os.path.isdir(wiki_sources):
        return mapping
    for p in glob.glob(os.path.join(wiki_sources, "*.md")):
        slug = os.path.splitext(os.path.basename(p))[0]
        for m in _RAW_REF.findall(read_text(p)):
            folder = m.split("/full.md")[0].split("/")[0].strip()
            if folder and "<" not in folder and ">" not in folder:
                mapping[folder] = slug
    return mapping


_FM_TITLE = re.compile(r"(?im)^title:\s*(.+?)\s*$")


def curated_title_keys(root: str | None = None) -> dict:
    """Map ``title_match_key`` -> curated slug for every ``wiki/sources`` page.

    Used to detect whether a mined reference is already curated. The key is
    separator-insensitive (see :func:`title_match_key`) so PDF de-hyphenation
    artifacts in mined titles ("relayassisted") still match the curated page
    ("Relay-Assisted"). On a key collision between two genuinely different
    curated titles the first slug wins; collisions are logged by the caller if
    needed (the stripped keys are long, so collisions are highly unlikely).
    """
    wiki_sources = os.path.join((root or wiki_dir()), "sources")
    keys = {}
    if not os.path.isdir(wiki_sources):
        return keys
    for p in glob.glob(os.path.join(wiki_sources, "*.md")):
        slug = os.path.splitext(os.path.basename(p))[0]
        m = _FM_TITLE.search(read_text(p))
        if not m:
            continue
        title = m.group(1).strip().strip('"').strip("'")
        key = title_match_key(title)
        if key:
            keys.setdefault(key, slug)
    return keys


# --- venue classification (allow-list from the mec-reference-scout brief) ----
#
# Maps a raw IEEE venue abbreviation (as it appears in reference strings) to a
# canonical "<full> — <abbrev>" label and a tier. Tiers:
#   "Q1"        Q1 journal / magazine / survey
#   "top-conf"  top networking/systems conference
#   "conf"      strong IEEE conference
#   "other"     recognized venue, not on the priority list
# Matching is substring-based on a normalized form so suffixes like the issue
# month (", Dec.") or "(GLOBECOM)" do not defeat it.

_VENUE_TABLE = [
    # (match-substrings, canonical label, tier)
    (("trans. mobile comput", "transactions on mobile comput"), "IEEE Trans. Mobile Comput. (TMC)", "Q1"),
    (("trans. wireless commun", "transactions on wireless commun"), "IEEE Trans. Wireless Commun. (TWC)", "Q1"),
    (("trans. veh. technol", "transactions on vehicular technol"), "IEEE Trans. Veh. Technol. (TVT)", "Q1"),
    (("trans. intell. transp", "intelligent transportation sys"), "IEEE Trans. Intell. Transp. Syst. (TITS)", "Q1"),
    (("j. sel. areas commun", "journal on selected areas in commun", "jsac"), "IEEE J. Sel. Areas Commun. (JSAC)", "Q1"),
    (("internet things j", "internet of things journal", "iot j"), "IEEE Internet Things J. (IoTJ)", "Q1"),
    (("trans. netw. sci. eng", "network science and eng"), "IEEE Trans. Netw. Sci. Eng. (TNSE)", "Q1"),
    (("trans. green commun", "green communications and netw"), "IEEE Trans. Green Commun. Netw. (TGCN)", "Q1"),
    (("trans. cogn. commun", "trans. cognit. commun", "cognitive communications and netw"), "IEEE Trans. Cogn. Commun. Netw. (TCCN)", "Q1"),
    (("trans. serv. comput", "transactions on services comput"), "IEEE Trans. Serv. Comput. (TSC)", "Q1"),
    (("trans. cloud comput", "transactions on cloud comput"), "IEEE Trans. Cloud Comput. (TCC)", "Q1"),
    (("trans. netw", "/acm trans. netw", "transactions on networking"), "IEEE/ACM Trans. Netw. (ToN)", "Q1"),
    (("inf. forensics security", "information forensics and security", "tifs"), "IEEE Trans. Inf. Forensics Security (TIFS)", "Q1"),
    (("trans. evol. comput", "evolutionary comput"), "IEEE Trans. Evol. Comput. (TEVC)", "Q1"),
    (("commun. surveys tuts", "commun. survey. tuts", "commun. surveys tut", "commun. survey. tut", "commun. surv. tut", "communications surveys", "communication surveys", "comst", "surv. tutor"), "IEEE Commun. Surveys Tuts. (COMST)", "Q1"),
    (("trans. commun",), "IEEE Trans. Commun. (TCOM)", "Q1"),
    (("commun. mag", "communications magazine"), "IEEE Commun. Mag.", "Q1"),
    (("ieee netw", "ieee network"), "IEEE Netw.", "Q1"),
    # top conferences (checked before the generic "Proc. IEEE" journal rule)
    (("infocom",), "IEEE INFOCOM", "top-conf"),
    (("mobicom",), "ACM MobiCom", "top-conf"),
    (("sigcomm",), "ACM SIGCOMM", "top-conf"),
    (("nsdi",), "USENIX NSDI", "top-conf"),
    (("mobihoc",), "ACM MobiHoc", "top-conf"),
    # strong IEEE conferences
    (("globecom", "global commun. conf", "glob. commun. conf"), "IEEE GLOBECOM", "conf"),
    (("int. conf. commun. (icc)", "ieee int. conf. commun", " icc)"), "IEEE ICC", "conf"),
    (("wcnc", "wireless commun. netw. conf"), "IEEE WCNC", "conf"),
    (("veh. technol. conf", "vtc"), "IEEE VTC", "conf"),
    # generic Proceedings of the IEEE (the journal) — only after conf rules
    (("proc. ieee", "proceedings of the ieee"), "Proc. IEEE", "Q1"),
]


def classify_venue(venue: str | None):
    """Return ``(canonical_label, tier)`` for a raw venue string.

    ``(None, None)`` if the string is empty; ``(venue, 'other')`` if it is a
    real venue not on the priority allow-list.
    """
    if not venue:
        return None, None
    low = " " + venue.lower().replace("&", " ").replace(".", ". ") + " "
    low = _NORM_WS.sub(" ", low)
    for subs, label, tier in _VENUE_TABLE:
        for s in subs:
            if s in low:
                return label, tier
    return venue, "other"
