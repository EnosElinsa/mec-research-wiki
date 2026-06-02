"""Rank not-yet-curated references as candidates to curate next.

Reads the merged reference-database.json, drops already-curated works and
clearly out-of-scope entries, then scores the rest on:

  * recency       2026 > 2024-25 > <=2023 (primary signal),
  * venue tier    Q1 > top-conf > conf > other,
  * centrality    cited_count within the corpus (depth signal),
  * MEC scope     keyword-inferred when the DB has no ``scope`` tag.

Each surviving candidate is tagged breadth vs depth and ready-in-raw vs
needs-fetching (matched against the uncurated raw/sources folders), and written
to a dated ``recommendations.md``. Nothing is fabricated — every row is a
reference string that appears in a parse.

Usage:
  python tools/wiki/recommend_refs.py                 # refresh recommendations.md
  python tools/wiki/recommend_refs.py --top 30 --json recs.json
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys

import wikilib

# --- scope inference (only used when the DB has no explicit scope tag) -------

_IN_SCOPE = re.compile(
    r"offload|edge comput|mec\b|resource alloc|trajectory|uav|aerial|hap\b|haps|"
    r"leo|satellite|sagin|vehicular|maritime|marine|usv|energy harvest|wireless power|"
    r"\bwpt\b|swipt|caching|migration|federated|isac|sensing|aigc|generative|"
    r"reinforcement learning|\bdrl\b|evolutionary|game|stackelberg|matching|"
    r"jamming|blockchain|noma|ris\b|computation|task schedul|6g|fog comput",
    re.I,
)
_OUT_SCOPE = re.compile(
    r"\bimage classif|object detect|semantic segment|natural language|"
    r"\bdataset\b|antenna design|circuit|\bsql\b",
    re.I,
)


def infer_scope(rec):
    s = rec.get("scope")
    if s in ("in", "out", "uncertain"):
        return s
    text = (rec.get("title") or "") + " " + (rec.get("venue") or "")
    if _OUT_SCOPE.search(text) and not _IN_SCOPE.search(text):
        return "out"
    if _IN_SCOPE.search(text):
        return "in"
    return "uncertain"


# --- track mapping -----------------------------------------------------------
# (regex on title, track label). First match wins; ordered most-specific first.
_TRACKS = [
    (r"maritime|marine|\busv\b|ocean|offshore|ship|vessel", "Maritime MEC"),
    (r"satellite|leo\b|sagin|space-air-ground|space/aerial|ntn\b|non-terrestrial", "SAGIN / satellite offloading & federation"),
    (r"vehicular|internet of vehicles|\bv2x\b|\bv2i\b|\brsu\b|roadside|\bvfc\b|autonomous driving|connected (?:and )?autonomous vehicle", "Vehicular MEC"),
    (r"isac|integrated sensing|sensing and communication|radar|doppler|\bcrb\b|\bcrlb\b", "ISAC / sensing / PLS"),
    (r"jamming|anti-jamming|physical layer security|\bpls\b|secrecy|eavesdrop", "Anti-jamming / security-DRL"),
    (r"blockchain|consensus|\bbft\b|trust|zero-trust", "Trust / security / federation"),
    (r"federated learning|\bfl\b|federation", "Trust / security / federation"),
    (r"aigc|generative|diffusion|\bgan\b|gpt|foundation model", "Generative-AI MEC"),
    (r"beamforming|virtual antenna|collaborative beamforming|\bvaa\b", "Collaborative beamforming (virtual antenna array)"),
    (r"caching|cache|service placement|service provision", "Caching / service placement"),
    (r"energy harvest|wireless power|\bwpt\b|swipt|wireless-powered|energy-harvest", "Energy efficiency & WPT"),
    (r"hierarchical aerial|hap[s]?-uav|uav-hap|high-altitude platform", "Hierarchical aerial MEC (UAV+HAP)"),
    (r"swarm", "UAV-swarm collaborative computing"),
    (r"post-disaster|disaster|emergency|search and rescue|rescue", "Post-disaster MEC"),
    (r"constrained multi-?objective|evolutionary|\bcmop\b|differential evolution|\bmoea\b|swarm optimization", "CMOP / evolutionary UAV-MEC"),
    (r"stackelberg|coalition|auction|bargain|potential game|game[- ]theoretic|matching", "Game-theoretic offloading"),
    (r"survey|tutorial|overview", "Foundational surveys / overviews"),
    (r"reinforcement learning|\bdrl\b|\bddpg\b|\bppo\b|actor-critic|\btd3\b|\bsac\b|\bmappo\b|maddpg|deep q|\bdqn\b|policy gradient|q-learning|learning-based|learning-assisted|attention-reinforced", "UAV-MEC + DRL"),
    (r"convex|lyapunov|\bsca\b|\bsdr\b|alternating optimization|stochastic optimization|trajectory|bit allocation|relay", "Classical/convex optimization UAV-MEC"),
    (r"offload|edge comput|\bmec\b|computation|resource alloc|data collection|task|uav|aerial|drone|wireless network|6g|d2d|cellular", "UAV-MEC + DRL"),
]


def candidate_track(rec):
    t = (rec.get("title") or "")
    for pat, label in _TRACKS:
        if re.search(pat, t, re.I):
            return label
    return "Generic offloading techniques"


# Track sizes (number of representative sources) parsed from overview.md so the
# breadth/depth call references the live wiki rather than a hardcoded snapshot.
def track_sizes():
    ov = os.path.join(wikilib.wiki_dir(), "overview.md")
    sizes = {}
    if not os.path.exists(ov):
        return sizes
    text = wikilib.read_text(ov)
    # Track rows look like: | Track name | [[a]], [[b]] | status |
    for line in text.splitlines():
        if line.count("|") >= 3 and "[[" in line:
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2:
                name = cells[0]
                n = len(re.findall(r"\[\[", cells[1]))
                if name and n:
                    sizes[name] = n
    return sizes


def _tier_rank(tier):
    return {"Q1": 3, "top-conf": 2, "conf": 1}.get(tier, 0)


def score(rec, sizes):
    """Composite score; recency dominates, then venue, then centrality.

    A breadth bonus is given only to genuine small wiki tracks (1-2 sources).
    The catch-all "Generic offloading techniques" bucket is NOT a real track, so
    it earns no breadth bonus and competes purely on recency/venue/centrality.
    """
    y = rec.get("year")
    rec_rank = 3 if (y or "").isdigit() and int(y) >= 2026 else (
        2 if (y or "").isdigit() and int(y) >= 2024 else 0)
    tier = _tier_rank(rec.get("venue_tier"))
    cc = rec.get("cited_count", 0)
    track = candidate_track(rec)
    size = sizes.get(track, 0)
    is_real_small = track != "Generic offloading techniques" and 1 <= size <= 2
    breadth_bonus = 1 if is_real_small else 0
    return rec_rank * 100 + tier * 15 + min(cc, 12) * 4 + breadth_bonus * 30


def first_author(authors):
    if not authors:
        return "n/a"
    parts = re.split(r",| and ", authors)
    a = parts[0].strip()
    if len(parts) > 1 or "et al" in authors.lower():
        a = re.sub(r"\bet al\.?", "", a).strip() + " et al."
    return a


_VENUE_HINT = re.compile(r"(IEEE\s+(?:Transactions|Trans\.|Journal|J\.|Internet|Communications|Network|Wireless)[^,\n.]*)", re.I)


def parse_uncurated_header(folder):
    """Best-effort title / first-author / year from an uncurated parse's head.

    Used only to surface a parsed-but-not-yet-curated paper as a 'ready now'
    candidate. Faithful to the parse; unknown fields stay None.
    """
    fp = os.path.join(wikilib.raw_sources_dir(), folder, "full.md")
    info = {"folder": folder, "title": None, "authors": None, "year": None, "venue": None}
    if not os.path.exists(fp):
        return info
    head = wikilib.read_text(fp)[:1500]
    m = re.search(r"(?m)^#\s+(.+)$", head)
    if m:
        info["title"] = m.group(1).strip()
    # first non-empty line after the title is usually the author block
    if m:
        after = head[m.end():].strip().splitlines()
        for ln in after:
            ln = ln.strip()
            if ln and "abstract" not in ln.lower():
                info["authors"] = re.sub(r"\s+", " ", ln).split("Abstract")[0].strip()
                break
    ys = re.findall(r"\b(20[12][0-9])\b", head)
    if ys:
        info["year"] = max(ys)
    return info


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--db", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--top", type=int, default=30, help="rows in the main ranked table")
    ap.add_argument("--json", metavar="PATH", help="also dump the ranked candidate structs")
    args = ap.parse_args(argv)

    refs_dir = os.path.join(wikilib.wiki_dir(), "references")
    db_path = args.db or os.path.join(refs_dir, "reference-database.json")
    out_path = args.out or os.path.join(refs_dir, "recommendations.md")
    db = json.load(open(db_path, encoding="utf-8"))
    recs = db["records"]

    # Already-curated set: by curated_as tag AND by separator-insensitive title
    # key of wiki pages. The separator-insensitive key (wikilib.title_match_key)
    # repairs PDF de-hyphenation artifacts in mined titles (e.g. "relayassisted"
    # vs the curated "Relay-Assisted") that a punctuation-only normalization
    # would miss, leaking already-curated papers into the recommendations.
    cur_keys = wikilib.curated_title_keys()

    slug_map = wikilib.folder_to_slug_map()
    uncurated_folders = set(wikilib.raw_folders()) - set(slug_map)

    sizes = track_sizes()

    cands = []
    for r in recs:
        if r.get("curated_as"):
            continue
        if not r.get("title"):
            continue
        if wikilib.title_match_key(r["title"]) in cur_keys:
            continue
        sc = infer_scope(r)
        if sc == "out":
            continue
        track = candidate_track(r)
        size = sizes.get(track, 0)
        is_real_small = track != "Generic offloading techniques" and 1 <= size <= 2
        kind = "breadth" if is_real_small else "depth"
        cands.append({
            "rec": r, "track": track, "scope": sc,
            "size": size, "kind": kind,
            "score": score(r, sizes),
        })

    cands.sort(key=lambda c: (-c["score"], -c["rec"]["cited_count"]))

    # Parsed-but-not-yet-curated papers: the strongest "ready to curate now"
    # picks, since their own parse already sits in raw/sources/.
    ready = []
    for folder in sorted(uncurated_folders):
        info = parse_uncurated_header(folder)
        # cross-corpus citation count of this paper, if others cite it
        cc = 0
        if info["title"]:
            nt = wikilib.normalize_title(info["title"])
            for r in recs:
                if r.get("title") and wikilib.normalize_title(r["title"]) == nt:
                    cc = max(cc, r["cited_count"])
        info["cited_count"] = cc
        info["track"] = candidate_track(info)
        info["size"] = sizes.get(info["track"], 0)
        ready.append(info)

    today = datetime.date.today().isoformat()
    n_curated = len(cur_keys)

    def venue_label(r):
        return r.get("venue_normalized") or r.get("venue") or "n/a"

    def why(c):
        r = c["rec"]
        if c["kind"] == "breadth":
            return f"_breadth_ — grows under-represented **{c['track']}** ({c['size']} src); cited {r['cited_count']}x in corpus"
        if c["track"] == "Generic offloading techniques":
            return f"_depth_ — cited by {r['cited_count']} corpus paper(s); general MEC offloading, no dedicated track yet"
        return f"_depth_ — cited by {r['cited_count']} corpus paper(s); deepens **{c['track']}**"

    lines = []
    lines.append("---")
    lines.append("type: recommendations")
    lines.append("title: Reference Scout Recommendations")
    lines.append("tags: [mec, references, recommendations]")
    lines.append("---")
    lines.append("")
    lines.append("# Reference Scout — Recommendations")
    lines.append("")
    lines.append(f"_Generated: {today}_ · Candidates mined from the reference lists of the {n_curated} curated papers, ranked against the current wiki state (`wiki/overview.md` tracks). Already-curated papers are excluded. Nothing here is fabricated — every row is a reference string that appears in a parse.")
    lines.append("")
    lines.append("**Scoring** combines recency (2026 > 2024-25 > <=2023), venue tier (Q1 journal > top conf > conf), in-corpus citation frequency (`cited_count` — a depth/centrality signal), and MEC scope. Each pick is tagged **breadth** (opens/grows an under-represented track) or **depth** (foundational, highly cited within the corpus).")
    lines.append("")

    ready = [r for r in ready if r["title"]]
    if ready:
        lines.append("## Ready to curate now (already parsed in `raw/sources/`)")
        lines.append("")
        lines.append("These papers' own MinerU parse already sits in `raw/sources/` but they are not yet curated — the strongest 'ready now' picks, no fetching needed.")
        lines.append("")
        lines.append("| Year | Title | Authors | cited_count | Candidate track | raw folder |")
        lines.append("|---|---|---|---|---|---|")
        for info in ready:
            lines.append(f"| {info.get('year') or 'n/a'} | {info['title']} | {first_author(info.get('authors'))} | {info['cited_count']} | {info['track']} | `{info['folder']}` |")
        lines.append("")

    # Main ranked table: prefer recent, but always surface the strongest depth picks.
    recent = [c for c in cands if (c["rec"].get("year") or "").isdigit() and int(c["rec"]["year"]) >= 2024]
    lines.append("## Top recommendations — recent & strong (need fetching/parsing)")
    lines.append("")
    lines.append("> `in raw/? = no` for every row: these are cited works whose own parse is not yet in `raw/sources/`, so each needs fetching + parsing before curation.")
    lines.append("")
    lines.append("| Year | Venue (abbrev) | Title | Authors | cited_count | Candidate track / why (breadth vs depth) | in raw/? |")
    lines.append("|---|---|---|---|---|---|---|")
    for c in recent[: args.top]:
        r = c["rec"]
        lines.append(f"| {r.get('year') or 'n/a'} | {venue_label(r)} | {r['title']} | {first_author(r.get('authors'))} | {r['cited_count']} | {why(c)} | no |")
    lines.append("")

    # Depth picks: most-cited uncurated works regardless of year.
    depth = sorted(cands, key=lambda c: -c["rec"]["cited_count"])[:20]
    lines.append("## Depth picks — most cited within the corpus (foundational)")
    lines.append("")
    lines.append("These references recur across many curated papers' bibliographies; curating them shores up the corpus's foundations. Older but high-`cited_count` works are surfaced here even when the recency-weighted table above skips them.")
    lines.append("")
    lines.append("| cited_count | Year | Venue | Title | Authors | track |")
    lines.append("|---|---|---|---|---|---|")
    for c in depth:
        r = c["rec"]
        lines.append(f"| {r['cited_count']} | {r.get('year') or 'n/a'} | {venue_label(r)} | {r['title']} | {first_author(r.get('authors'))} | {c['track']} |")
    lines.append("")

    # Rationale
    lines.append("## Rationale — tying picks to current wiki gaps")
    lines.append("")
    small = sorted({c["track"]: c["size"] for c in cands
                    if c["kind"] == "breadth"}.items(), key=lambda x: x[1])
    breadth_tracks = ", ".join(f"**{t}** ({n} src)" for t, n in small[:6]) or "none flagged"
    lines.append(f"- **Breadth.** Under-represented tracks in `wiki/overview.md` that candidates could grow: {breadth_tracks}.")
    big = sorted(sizes.items(), key=lambda x: -x[1])[:4]
    lines.append(f"- **Depth.** The largest tracks ({', '.join(f'{t} ({n})' for t, n in big)}) are deepened by the high-`cited_count` foundational works above.")
    lines.append(f"- **Readiness.** {len(ready)} candidate(s) already have a parse in `raw/sources/` and can be curated immediately; the rest need fetching + parsing first.")
    lines.append("")

    open(out_path, "w", encoding="utf-8").write("\n".join(lines))
    print(f"candidates: {len(cands)} | ready-in-raw: {len(ready)} | recent: {len(recent)} -> {out_path}")

    if args.json:
        out = args.json if os.path.isabs(args.json) else os.path.join(wikilib.scratch_dir(), args.json)
        json.dump([{k: (v if k != "rec" else v) for k, v in c.items()} for c in cands][:200],
                  open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"ranked structs -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
