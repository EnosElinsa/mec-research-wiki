# Wiki maintenance toolkit

Reusable, version-controlled scripts shared by the MEC-wiki agents
(`mec-wiki-curator`, `mec-wiki-auditor`, `mec-wiki-synthesizer`,
`mec-reference-scout`). This directory is the **maintained home** for the logic
that used to be re-written as throwaway one-offs in `.curation-out/` every
session.

## The rule (why this directory exists)

- **Reusable logic lives here, tracked in git.** Anything you would otherwise
  paste into a new `.curation-out/check_thing_v3.py` belongs here instead, as a
  parameterized CLI that the next session can reuse and improve.
- **`.curation-out/` is gitignored scratch — state and reports only.** Batch
  plans, JSON reports, grounding dumps, decision notes: fine there, disposable.
  Reusable code: never there.
- **Ratchet, don't restart.** Each session, prefer extending an existing tool
  (add a flag, generalize a path) over writing a new variant. The toolkit should
  converge toward a stable, trusted set rather than sprawl.
- **Path-agnostic.** Everything imports `wikilib`, which discovers the repo root
  itself. Run the scripts from the repo root: `python tools/wiki/<script>.py`.

## Scripts

| Script | Purpose | Common flags |
|---|---|---|
| `wikilib.py` | Shared library: repo paths, md enumeration, Obsidian-faithful wikilink parsing, raw/sources reference parsing (`# REFERENCES` block extraction, IEEE entry parsing, title normalization, stable `surname-year-slug` keys, venue allow-list classifier, folder→curated-slug map). Imported by the others; not run directly. | — |
| `linkcheck.py` | Wikilink integrity (zero-dangling check), Obsidian resolution rules. Exit 1 if any dangling link. | `--orphans`, `--json` |
| `graph_audit.py` | Freeze an exact-created-date wiki cohort, audit its simple undirected induced graph, create/refresh an editorial coverage ledger, and compare later graph state without admitting new pages into the cohort. Exit 0 for every structurally valid snapshot/comparison (including regressions); exit 2 for malformed reports, ambiguous basenames, missing frozen members, or invalid arguments. | `snapshot --created --label --weak-degree --exclude --observed-ui-pages --observed-ui-cohesion --json --ledger`; `compare --baseline --json --ledger` |
| `curation_status.py` | Reconcile `raw/sources/` vs curated pages by raw-artifact path with normalized-title and conservative repeated-character OCR fallbacks for stale paths; list uncurated folders; detect duplicate MinerU ingests (identical/near) across both `full.md` and title-named parses. Exit 1 if genuinely-new papers remain. | `--dupes`, `--near-ratio`, `--json` |
| `make_batches.py` | Split the genuinely-new papers (or an explicit list) into context-window-sized batches for a multi-invocation run; optionally print only one numbered allowlist while preserving the complete JSON plan. | `--size` (required), `--input`, `--batch`, `--json` |
| `corpus_counts.py` | Exact page counts per wiki type + `raw/sources` count + log.md size, for reconciling `overview.md`/`index.md`; can refresh the three inventory counts in the overview Snapshot. | `--json`, `--update-overview` |
| `process_refs.py` | Find curation process-narration (batch/pass labels, "this pass", "this/same batch", dated-run references, "paper #N" ingest-order, forward-looking "future/subsequent/later sources should land here / be tagged" placement) leaked into any page except `log.md`. A paper's own "future work" section is evergreen domain content and is NOT flagged. Exit 1 if any found. | `--json` |
| `index_audit.py` | Reconcile the wiki page inventory against `index.md`: report pages that exist on disk but are not catalogued, and pages catalogued under more than one *primary bullet* (true duplicate listings). A primary listing is the leading wikilink of a list item; a slug merely re-mentioned inside another bullet's prose (entity roster, finding/methodology citing its source, deliberate `>` cross-ref) is reported informationally, not as a duplicate. Exit 1 if any coverage gap or duplicate primary listing. | `--ignore`, `--json` |
| `frontmatter_audit.py` | Lint YAML frontmatter validity + tag/type consistency on every typed wiki page: required keys (`type`/`title`/`tags`/`created`/`updated`), `type` matches directory, `# H1` present, type-specific tags/keys (source→`source` tag + `authors`/`year`/`url`/`venue`; entity→`author` or `tool`; finding→`source`+`confidence`; synthesis→`synthesis` tag), and no self-reference in `related:`. A structural lint, not a fact-checker. Exit 1 if any page has a structural error. | `--type`, `--show-soft`, `--ignore`, `--json` |
| `entity_roster_audit.py` | Cross-check author-entity rosters against source-page `authors:` lists, both directions: **claimed-but-absent** (entity links a source whose author list lacks a matching name — roster over-claim) and **present-but-unlisted** (a source lists a matching author the entity does not link — possible omission *or* namesake). Roster claims are read from the **roster region only** (frontmatter `related:` + intro + bulleted source list, i.e. everything before the first `## Contributions` heading), so editorial contrast-mentions in the Contributions commentary are not mis-counted as claims. Name matching is reported as `strict` (full-name), `respaced` (identical once interior spaces are removed, e.g. "Li Ping Qian" == "Liping Qian" — a Chinese given-name spacing variant), or `loose` (first+last token only); both YAML author styles (inline flow + block list) are handled. Advisory only (always exit 0) — it never decides identity; confirm namesakes against the parses before editing. | `--input`, `--json` |
| `mine_refs.py` | Mine the `# REFERENCES` of every `raw/sources/*/full.md` into deduplicated reference records; idempotently MERGE into `wiki/references/reference-database.json` (preserves enrichment + curated tags, refreshes `cited_by`/`cited_count`, re-derives venue tiers). Used by `mec-reference-scout`. | `--json`, `--merge DB.json` |
| `verify_refdb.py` | Integrity gate for the mined `reference-database.json`: scans every record's string fields for residual MinerU contamination markers (the `strip_ref_contamination` regression guard), checks all parsed years are in `[--min-year, --max-year]`, and lists future-year records (>= `--flag-year`) split into curated (expected in-press) vs uncurated (review for mis-parse). Exit 1 on any contamination marker or out-of-range year; year warnings alone do not fail. | `--db`, `--min-year`, `--max-year`, `--flag-year`, `--json` |
| `render_refdb.py` | Render the human-readable `wiki/references/reference-database.md` (summary + most-cited centrality table) from the JSON DB so the two never drift. | `--db`, `--out`, `--min` |
| `recommend_refs.py` | Rank not-yet-curated references as curate-next candidates (recency + venue tier + in-corpus citation frequency + scope), tag breadth/depth and ready-in-raw, and refresh the dated `wiki/references/recommendations.md`. | `--top`, `--db`, `--out`, `--json` |

`--json PATH` writes the machine-readable report; a relative PATH lands in
`.curation-out/` (the scratch dir) automatically.

## Frozen-cohort graph audits

`graph_audit.py snapshot` resolves only Markdown pages under `wiki/`, requires
unique page basenames, removes the administrative `index`, `log`, and
`overview` pages (plus any repeated `--exclude SLUG` values), and collapses
repeated, reciprocal, and self links into a simple undirected graph. The report
also ignores wikilink examples inside backtick or tilde fenced code blocks and
single- or multi-backtick inline code. A snapshot stores `report_type:
snapshot`, `generated_at_utc`, `label`, `graph_semantics`, parameters, and the
separate `external_observation`. Its cohort contains `selector`, sorted
`members`, directory-derived `member_types`, `member_count`,
`member_hash_algorithm: sha256-canonical-json`, and `member_hash`. Graph metrics
are `induced_edge_count`, `possible_edge_count`, `local_cohesion`,
`component_count`, `largest_component_size`, `isolate_count`,
`weak_member_count`, and `bridge_edge_count`; graph details contain internal and
external degrees, canonical induced/bridge edges, deterministic components,
isolates, and `weak_members` rows whose degree field is `internal_degree`.

Local cohesion is strictly the frozen cohort's induced density:
`induced_edge_count / (member_count * (member_count - 1) / 2)`. Optional LLM Wiki UI page and
cohesion readings are stored as `external_observation` with source `LLM Wiki
UI`; they are never inputs to this formula. A `report_type: comparison` report
validates the baseline, reuses its immutable member array, exclusions, and weak
threshold, and stores the current graph plus baseline metrics and a nested
`comparison` object containing metric/degree deltas and added/removed edges.
Pages created after the snapshot, including pages with the same `created` date,
remain outside induced metrics (a link to one can only affect a frozen member's
external degree).

Relative snapshot/comparison output and snapshot-ledger paths are written under
`.curation-out/`. For `compare`, relative `--baseline` and `--ledger` inputs are
resolved from the repository root; the refreshed ledger is written back to the
same path. Relative paths cannot escape those roots; absolute paths remain
explicitly allowed. All command paths must resolve to distinct files, and JSON
updates use an atomic sibling-file replacement. A coverage ledger
(`report_type: coverage-ledger`) stores `baseline_label`,
`baseline_member_hash`, and sorted `entries`. Each entry preserves its editorial
`theme`, `status`, `evidence_paths`, `candidate_relationships`, `accepted_links`,
and `deferral_reason` while refresh updates `post_batch_component` and
`post_batch_internal_degree`.

```sh
python tools/wiki/graph_audit.py snapshot --created 2026-07-14 --label "Research Log core" --weak-degree 1 --observed-ui-pages 323 --observed-ui-cohesion 0.03 --json research-log-2026-07-14-baseline.json --ledger research-log-2026-07-14-ledger.json
python tools/wiki/graph_audit.py compare --baseline .curation-out/research-log-2026-07-14-baseline.json --json research-log-2026-07-14-after.json --ledger .curation-out/research-log-2026-07-14-ledger.json
```

## Typical flows

```sh
# Before a curation run: what is new, and how should it be batched?
python tools/wiki/curation_status.py --dupes --json status.json
python tools/wiki/make_batches.py --size 7 --batch 1 --json batches.json

# After any edit: gate the commit on a clean graph + evergreen wording.
python tools/wiki/linkcheck.py
python tools/wiki/process_refs.py

# Audit-time consistency gates: index coverage + frontmatter/tag validity.
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py

# Reconcile the Snapshot before committing meta-doc edits.
python tools/wiki/corpus_counts.py
```

```sh
# Reference-scout pass: mine refs -> merge DB -> verify -> render md -> recommend.
python tools/wiki/mine_refs.py --merge wiki/references/reference-database.json
python tools/wiki/verify_refdb.py
python tools/wiki/render_refdb.py --min 2
python tools/wiki/recommend_refs.py --top 30
```

## Extending the toolkit

When a session needs something not covered here:

1. If an existing script is close, **add a flag** to it rather than forking.
2. If it is genuinely new, add a new `tools/wiki/<verb_noun>.py` that imports
   `wikilib`, takes arguments (no hardcoded paths, batch numbers, or counts),
   prints a human summary, and supports `--json`.
3. Update this table, and commit the tool **with** the work that motivated it.
4. Never leave the reusable logic behind in `.curation-out/`.
