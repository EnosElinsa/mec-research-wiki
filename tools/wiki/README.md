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
| `curation_status.py` | Reconcile `raw/sources/` vs curated pages; list uncurated folders; detect duplicate MinerU ingests (identical/near). Exit 1 if genuinely-new papers remain. | `--dupes`, `--near-ratio`, `--json` |
| `make_batches.py` | Split the genuinely-new papers (or an explicit list) into context-window-sized batches for a multi-invocation run. | `--size` (required), `--input`, `--json` |
| `corpus_counts.py` | Exact page counts per wiki type + `raw/sources` count + log.md size, for reconciling `overview.md`/`index.md`. | `--json` |
| `process_refs.py` | Find curation process-narration (batch/pass labels) leaked into any page except `log.md`. Exit 1 if any found. | `--json` |
| `index_audit.py` | Reconcile the wiki page inventory against `index.md`: report pages that exist on disk but are not catalogued, and pages catalogued under more than one *primary bullet* (true duplicate listings). A primary listing is the leading wikilink of a list item; a slug merely re-mentioned inside another bullet's prose (entity roster, finding/methodology citing its source, deliberate `>` cross-ref) is reported informationally, not as a duplicate. Exit 1 if any coverage gap or duplicate primary listing. | `--ignore`, `--json` |
| `frontmatter_audit.py` | Lint YAML frontmatter validity + tag/type consistency on every typed wiki page: required keys (`type`/`title`/`tags`/`created`/`updated`), `type` matches directory, `# H1` present, type-specific tags/keys (source→`source` tag + `authors`/`year`/`url`/`venue`; entity→`author` or `tool`; finding→`source`+`confidence`; synthesis→`synthesis` tag), and no self-reference in `related:`. A structural lint, not a fact-checker. Exit 1 if any page has a structural error. | `--type`, `--show-soft`, `--ignore`, `--json` |
| `mine_refs.py` | Mine the `# REFERENCES` of every `raw/sources/*/full.md` into deduplicated reference records; idempotently MERGE into `wiki/references/reference-database.json` (preserves enrichment + curated tags, refreshes `cited_by`/`cited_count`, re-derives venue tiers). Used by `mec-reference-scout`. | `--json`, `--merge DB.json` |
| `render_refdb.py` | Render the human-readable `wiki/references/reference-database.md` (summary + most-cited centrality table) from the JSON DB so the two never drift. | `--db`, `--out`, `--min` |
| `recommend_refs.py` | Rank not-yet-curated references as curate-next candidates (recency + venue tier + in-corpus citation frequency + scope), tag breadth/depth and ready-in-raw, and refresh the dated `wiki/references/recommendations.md`. | `--top`, `--db`, `--out`, `--json` |

`--json PATH` writes the machine-readable report; a relative PATH lands in
`.curation-out/` (the scratch dir) automatically.

## Typical flows

```sh
# Before a curation run: what is new, and how should it be batched?
python tools/wiki/curation_status.py --dupes --json status.json
python tools/wiki/make_batches.py --size 7 --json batches.json

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
# Reference-scout pass: mine refs -> merge DB -> render md -> recommend.
python tools/wiki/mine_refs.py --merge wiki/references/reference-database.json
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
