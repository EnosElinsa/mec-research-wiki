# Research Log Sparse-Cluster Cohesion Design

**Date:** 2026-07-14
**Status:** Approved for implementation planning
**Repository:** `mec-research-wiki`

## Objective

Improve the internal semantic connectivity of the LLM Wiki knowledge area reported as **Sparse cluster: Research Log**. The original alert reported 295 pages with cohesion 0.03; the live UI later reported 323 pages with the same cohesion. The work must add evidence-grounded internal navigation and analytical pages without manufacturing generic links merely to raise a graph score.

Completion is a program-level outcome. A single synthesis page or one convenient theme batch is progress, not completion.

## Current evidence

The live repository state observed during design contained:

- 611 source pages, 656 concept pages, and 188 entity pages.
- 15 findings, 15 synthesis pages, 6 comparisons, 6 methodology pages, 5 queries, and 3 theses.
- 612 raw-source folders, all matched to curated source pages; genuinely uncurated count: zero.
- 1,507 catalogue-able pages with complete, unique index coverage.
- Zero dangling wikilinks, zero frontmatter errors, and zero leaked process-narration findings.

The public LLM Wiki graph endpoint is capped at 1,000 nodes and does not expose community IDs, membership, the clustering algorithm, or the cohesion formula. The historical 295-member roster and the live 323-member roster therefore cannot be exported or reconstructed exactly from the supported API.

A reproducible local core is available: the 286 typed wiki pages with `created: 2026-07-14`. A file-derived diagnostic found 341 unique undirected internal edges, 47 components, a largest component of 68 pages, and 87 members with internal degree zero or one. These values are provisional observations; the implementation must recompute and freeze them with the maintained graph-audit tool before any wiki edits.

The UI values 295/0.03 and 323/0.03 are retained as external observations. They are not numerically comparable to the file-derived density unless LLM Wiki later documents matching graph and denominator semantics.

## Design principles and invariants

1. Every analytical claim must trace to one or more current `raw/sources/<folder>/full.md` or title-named parses.
2. Existing source pages locate evidence but do not replace the parse.
3. Every proposed edge needs a semantic reason grounded in page content or parses.
4. Do not create all-to-all, same-topic-only, self, dangling, or administrative links.
5. Reuse existing slugs and tags; do not mint near-synonyms to improve density.
6. Derived pages are created only when the evidence earns their analytical shape.
7. Every wiki page except `wiki/log.md` remains evergreen. Run narration belongs only in the log and commit messages.
8. `wiki/index.md`, `wiki/log.md`, and `wiki/overview.md` are administrative hubs and are excluded from semantic cohort metrics.
9. One repository-owning coordinator performs all shared wiki, navigation, and Git writes. Subagents are read-only unless assigned a genuinely non-overlapping file scope.
10. The full core cohort must be accounted for; the first five themes do not redefine completion.

## Alternatives considered

### 1. Cohort audit plus thematic synthesis — selected

Freeze a reproducible cohort, measure its semantic graph, build an evidence ledger, and process coherent themes through derived pages plus reciprocal source/concept links. This produces both analytical value and measurable graph improvement.

### 2. Link-only sweep — rejected

Adding links directly between existing pages would move edge counts quickly, but it would encourage generic relationships and would not address the thin analytical layer.

### 3. Derived-pages-only expansion — rejected

Creating synthesis pages without reconciling backlinks would improve the wiki's prose but leave many source and concept pages structurally dependent on administrative hubs.

## Scope

### In scope

- A maintained, tested wiki-only graph snapshot/compare CLI.
- A fixed core cohort and machine-readable baseline.
- A coverage ledger for every core member.
- Evidence matrices for accepted themes.
- New or refreshed findings, synthesis, comparisons, methodologies, queries, or theses when supported.
- Justified reciprocal links on existing source, concept, entity, and analytical pages.
- Required `wiki/index.md`, durable `wiki/overview.md`, and one dated `wiki/log.md` update per batch.
- Independent evidence review, repository gates, scoped commits, pushes, and remote verification.

### Out of scope

- Curating genuinely new raw papers.
- Mining or rewriting `wiki/references/**`.
- Broad factual rewrites of source pages beyond a narrowly verified correction or connection.
- Treating raw parse pages as semantic graph members.
- Removing historical log entries to manipulate clustering.
- Claiming that local density reproduces LLM Wiki cohesion.
- Destructive Git operations or rewriting published history.

## Architecture

### 1. Wiki graph primitives

Extend `tools/wiki/wikilib.py` with focused helpers that enumerate unique wiki-page basenames and unique undirected simple edges from Obsidian-resolved wikilinks. The graph scope is `wiki/**/*.md`; repeated, reciprocal, and self-links do not inflate the metric.

The helper must fail closed on duplicate wiki basenames because basename ambiguity would make Obsidian resolution and graph membership non-deterministic.

### 2. `graph_audit.py`

Add `tools/wiki/graph_audit.py` with two operations:

```powershell
python tools/wiki/graph_audit.py snapshot `
  --created 2026-07-14 `
  --label "Research Log core" `
  --weak-degree 1 `
  --observed-ui-pages 323 `
  --observed-ui-cohesion 0.03 `
  --json research-log-2026-07-14-baseline.json

python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-2026-07-14-after.json
```

`snapshot` stores the sorted effective member list and its SHA-256 hash, graph semantics, exclusions, internal and external degrees, induced edges, components, isolates, weak members, bridge edges, and the external UI observation. `compare` reuses the frozen membership and parameters, rejects missing members, and reports metric deltas plus added and removed edges.

The local cohesion definition is explicit:

```text
unique induced undirected edges / (n * (n - 1) / 2)
```

The CLI exits non-zero for malformed input, duplicate basenames, missing frozen members, or invalid snapshots. A valid comparison does not fail solely because a metric regresses; the regression is reported and blocks batch acceptance at the orchestration layer.

Add `tools/wiki/tests/test_graph_audit.py` and document the script, flags, metric semantics, and exit behavior in `tools/wiki/README.md`.

### 3. Coverage ledger

Maintain a gitignored ledger under `.curation-out/` for the duration of the program. Each core member records:

- slug, type, component, and baseline internal degree;
- proposed or completed theme;
- status: `pending`, `linked`, `derived`, or `deferred`;
- evidence paths and candidate semantic relationships;
- accepted links or the exact deferral reason;
- post-batch internal degree.

`linked` means the page gained at least one justified non-administrative relationship. `derived` means it is represented by an evidence-grounded analytical page and reciprocal navigation. `deferred` is allowed only when the ledger records why current evidence does not support another link. No member may remain `pending` at program completion.

The final dated log entry records status counts, baseline/final hashes, and metric deltas without publishing the transient ledger itself.

### 4. Evidence matrices

Before writing a theme, build a compact matrix mapping each proposed claim and edge to raw parse paths, evidence locations, incompatible assumptions, and caveats. Distinguish paper-reported facts from cross-source inference. Comparisons require a specific non-comparability analysis before any numeric juxtaposition.

### 5. Thematic batch unit

One batch covers one coherent theme, typically five to eight source papers and 15–25 total pages after concepts and analytical neighbors are included. Read-only workers may ground separate evidence questions. The coordinator selects the analytical form, writes all shared pages and backlinks, reconciles navigation, runs gates, and owns Git.

Each batch receives one scoped commit and push after verification. A batch that fails evidence review or graph acceptance is revised or deferred; it is not committed merely because drafts exist.

## Initial thematic roadmap

| Order | Theme | Intended analytical output | Planning estimate |
|---|---|---|---|
| 1 | Aerial coverage under mobility, asynchrony, and geometry | `wiki/synthesis/mobility-asynchrony-and-geometry-in-aerial-coverage.md` | 16–19 pages, 20–27 semantic edges |
| 2 | Constraint regimes in UAV data collection | `wiki/synthesis/constraint-regimes-in-uav-data-collection.md` | 17–21 pages, 22–30 edges |
| 3 | Aerial federated aggregation design space | `wiki/synthesis/aerial-federated-aggregation-design-space.md` | 18–21 pages, 23–31 edges |
| 4 | UAV trajectory safety guarantee ladder | Refresh `safety-and-robustness-mechanisms-in-mec`; add `wiki/comparisons/uav-trajectory-safety-guarantee-ladder.md` | 19–23 pages, 25–34 edges |
| 5 | Covertness, surveillance, and monitoring | `wiki/synthesis/aerial-observation-control-covertness-surveillance-and-monitoring.md` | 18–21 pages, 23–31 edges |

The first roadmap is expected to touch roughly 75–95 distinct pages and add 110–145 non-generic edges. These are planning estimates, not acceptance substitutes.

After every batch, the residual ledger is sorted by weak internal degree, component fragmentation, evidence groundedness, and analytical page-type imbalance. New themes are selected until the program-level acceptance criteria are satisfied and every core member is resolved.

## Batch data flow

1. Recheck Git status, raw/curated reconciliation, corpus counts, and the frozen cohort hash.
2. Select a coherent residual theme; do not alter frozen membership.
3. Ground every candidate claim and edge in current parses.
4. Reject unsupported or incompatible candidates before drafting.
5. Write the earned analytical pages and reciprocal links.
6. Update index, durable overview content when warranted, and one dated log entry.
7. Run independent evidence and link-rationale review.
8. Run repository and graph gates.
9. Commit and push the scoped theme; verify the remote SHA.
10. Update the ledger and select the next residual theme.

## Failure handling

- **Membership drift:** later-created pages cannot alter the frozen cohort. They may be linked as external neighbors, and a new baseline is created only after this program completes.
- **Capped or unavailable API:** continue from files and maintained tools. UI observations are optional accelerators until the final acceptance rescan.
- **Insufficient evidence:** defer the proposed page or edge with a precise ledger reason. Never substitute a generic same-topic link.
- **Incompatible studies:** write a synthesis map or explicit non-comparability section; do not rank incompatible gains.
- **Concurrent edits:** stop before overwriting any overlapping user change. Keep one writer for index, overview, log, cohort tooling, and Git state.
- **Worker rate limits or disconnects:** reduce concurrency or serialize. Worker failure never weakens the evidence gate.
- **Non-fast-forward push:** rebase once and retry once. Never force.
- **Ambiguous push or LFS timeout:** compare local HEAD, tracking ref, and `git ls-remote`; do not retry until remote state is known.

## Verification

### Per-batch gates

Run the current commands documented in `tools/wiki/README.md`. At minimum:

```powershell
python tools/wiki/curation_status.py --dupes
python tools/wiki/corpus_counts.py
python tools/wiki/linkcheck.py --orphans
python tools/wiki/process_refs.py
python tools/wiki/index_audit.py
python tools/wiki/frontmatter_audit.py
python tools/wiki/entity_roster_audit.py
python -m unittest discover -s tools/wiki/tests -p "test_*.py" -v
python tools/wiki/graph_audit.py compare `
  --baseline .curation-out/research-log-2026-07-14-baseline.json `
  --json research-log-2026-07-14-after.json
git diff --check
```

Also require:

- independent claim-to-parse and edge-rationale review;
- no unexplained removal of frozen-cohort edges;
- exact staged scope and a clean credential scan;
- every changed evergreen page free of run narration;
- commit SHA equal to the verified remote branch SHA after push.

### Program-level acceptance

All of the following are required:

1. Every frozen core member is `linked`, `derived`, or `deferred` with a concrete evidence reason; none are `pending`.
2. Relative to the recomputed baseline, unique internal semantic edges increase by at least 25%. If the observed 341-edge diagnostic is confirmed, the threshold is at least 427.
3. Component count falls by at least 25%. If the observed 47-component diagnostic is confirmed, the maximum is 35.
4. Degree-zero-or-one members fall by at least 50%. If the observed count of 87 is confirmed, the maximum is 43.
5. All repository gates pass on the final tree.
6. Every thematic commit is present on the tracking remote, and local HEAD equals the verified remote SHA.
7. After a final LLM Wiki rescan, the Research Log sparse-cluster insight is absent or its displayed cohesion is strictly greater than 0.03. If neither is true, the goal remains incomplete and another residual pass is selected.

The tool-generated baseline is authoritative for the numeric thresholds. If its fresh counts differ from the provisional diagnostics, apply the approved relative percentages rather than the provisional absolute numbers.

## Testing strategy for the graph tool

The graph-tool tests must cover:

1. wiki-only scope;
2. reciprocal, repeated, and self-link collapsing;
3. default administrative-hub exclusions;
4. frontmatter-date cohort selection;
5. density, components, isolates, weak members, and bridge edges;
6. frozen-membership reuse and exclusion of new nonmembers;
7. added/removed edge and degree deltas;
8. failure on missing frozen members;
9. failure on duplicate wiki basenames;
10. separation of UI observation metadata from local cohesion;
11. relative JSON output under `.curation-out/`.

## Git delivery

- The design specification is committed separately before implementation planning.
- Graph tooling and the frozen baseline use one verified foundation commit. The first theme begins only after that foundation is committed and pushed.
- Every later theme uses one coherent commit.
- Scratch reports and the coverage ledger remain gitignored.
- Each accepted theme is pushed after its gates pass, followed by local/tracking/remote SHA verification.
- No force-push, hard reset, branch deletion, or rewriting published history is permitted. The single non-fast-forward recovery rebase applies only to unpublished local commits.

## Implementation decomposition

The implementation plan will separate:

1. graph-audit foundation and frozen baseline;
2. each of the five initial themes;
3. residual-cohort selection and any additional evidence-earned themes;
4. final whole-program audit and UI rescan.

Each theme is independently reviewable and deployable, while the program-level acceptance criteria remain the definition of completion.
