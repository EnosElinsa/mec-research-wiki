# MEC Research Wiki

A curated, evidence-grounded knowledge base on **mobile edge computing (MEC)**. It covers task offloading, resource allocation, trajectory and deployment design, and the optimization and learning methods that solve them, across UAV, high-altitude platform (HAP), satellite, vehicular, maritime, and terrestrial networks. Adjacent work that MEC system models build on (UAV communications, channel models, ISAC, RIS, physical-layer security, federated learning) is included.

Every paper page is written from the paper's full-text parse. A paper with a reusable decision model carries a **Modeling Quick-Use Card** (scenario, objective, decision variables, constraints, algorithm), and every paper carries a citation-ready **Related Work paragraph**. Every card symbol and number and every Related Work sentence is checked against the parse, and the supporting line ranges are recorded in [`wiki/.grounding/`](wiki/.grounding/).

## Corpus at a glance

Counts as of 2026-11-05. `python tools/wiki/corpus_counts.py` prints the live numbers.

| Layer | Pages | Content |
|---|---:|---|
| Sources | 699 | One page per paper: 593 with a modeling card, 106 without (surveys, foundational algorithms, measurement and protocol papers) |
| Concepts | 665 | Techniques, system-model components, metrics, and architectures |
| Entities | 211 | 209 recurring authors and 2 tools |
| Analytical pages | 57 | 20 synthesis, 8 comparison, 15 finding, 6 methodology, 5 query, and 3 thesis pages |
| References | 2 | Citation database (21,510 unique references mined from 690 parses) plus curate-next recommendations |
| Raw papers | 699 folders | Markdown parse, extracted figures, and PDF (Git LFS) for each paper |

All 699 source pages are grounded. 647 come from IEEE journals, magazines, and conferences, and 501 were published in 2024-2026; the earliest is from 2010.

## Where to start

- [`wiki/overview.md`](wiki/overview.md): corpus snapshot and the research tracks that have emerged.
- [`wiki/index.md`](wiki/index.md): every page, grouped by type and topic.
- Cross-paper analysis, for example the [DRL vs evolutionary vs classical solvers](wiki/synthesis/drl-vs-evolutionary-vs-classical-solvers.md) synthesis, the [game-theoretic offloading formulations](wiki/comparisons/game-theoretic-offloading-formulations.md) comparison, [UAV energy replenishment and service continuity](wiki/synthesis/uav-energy-replenishment-and-service-continuity.md), and the [SAGIN and satellite offloading landscape](wiki/synthesis/sagin-satellite-offloading-landscape.md).
- Working theses with supporting evidence and refutation criteria: [decomposition beats end-to-end DRL](wiki/thesis/decomposition-beats-end-to-end-drl-in-mec.md) and [explicit constraints beat reward shaping](wiki/thesis/explicit-constraints-beat-reward-shaping-in-mec-drl.md).
- A typical source page: [Zeng et al. 2019, energy minimization for rotary-wing UAV communication](wiki/sources/zeng-2019-rotary-wing-energy-min.md).
- [`purpose.md`](purpose.md): the research question, scope, and current status.

## Reading the wiki

Pages link to each other with `[[page-slug]]` wikilinks, which GitHub displays as plain text. To follow links and view the graph, use one of:

- **Obsidian.** Open the repository root as a vault. `.obsidian/` holds the shared settings (wikilinks, shortest-path link format).
- **LLM Wiki.** The [LLM Wiki](https://github.com/nashsu/llm_wiki) desktop app indexes `purpose.md`, `schema.md`, `wiki/**`, and `raw/sources/**`, and provides search, a graph view, and a local HTTP API on `127.0.0.1:19828`. Its index lives in the ignored `.llm-wiki/` folder. The app is optional; no maintenance step depends on it.
- **Plain files.** Every page is Markdown with YAML frontmatter, so `rg` or `grep` over `wiki/` works for search.

## Repository layout

```text
README.md            Project introduction (this file)
purpose.md           Research question, scope, methodology, and status
schema.md            Page types, frontmatter, naming, and the paper-source contract
CONTRIBUTING.md      Maintenance workflow, editing conventions, and commit rules
LICENSE-MIT          License for code and agent configuration
LICENSE-CC-BY-4.0    License for original wiki text and documentation
wiki/
  overview.md        Corpus snapshot and emerging tracks
  index.md           Catalogue of every page, grouped by type
  log.md             Reverse-chronological maintenance log
  sources/           One page per paper
  concepts/          Techniques, system-model components, metrics, architectures
  entities/          Recurring authors and tools
  findings/          Single-source results worth tracking separately
  synthesis/         Cross-paper maps of a track or design space
  comparisons/       Side-by-side analysis of comparable methods or formulations
  methodology/       Solution protocols shared by several papers
  queries/           Open questions raised by the corpus
  thesis/            Working positions with confidence, status, and refutation criteria
  references/        Mined citation database and curate-next recommendations
  .grounding/        Evidence sidecars: parse line ranges behind each card and Related Work paragraph
raw/sources/         One folder per paper: Markdown parse, figures, PDF (Git LFS)
ideas/               Research-idea drafts built on the wiki (Chinese) and the prompt that produces them
tools/               PowerShell ingest scripts: MinerU conversion, MEC relevance filter, folder naming
  wiki/              Python audit and maintenance toolkit (see tools/wiki/README.md)
.codex/agents/       Role definitions for the curator, auditor, synthesizer, and reference-scout agents
.agents/skills/      Agent skills; retrieve-ieee-papers fetches selected papers through authorized access
.obsidian/           Shared Obsidian vault settings
```

These local paths are ignored by Git: `.curation-out/` (scratch reports), `.llm-wiki/` (LLM Wiki index), `raw/tmp/` (staged downloads), and `docs/` (planning notes).

## How a paper enters the wiki

1. **Retrieve.** PDFs come from the maintainer's library or from the [`retrieve-ieee-papers`](.agents/skills/retrieve-ieee-papers/SKILL.md) skill, which downloads one selected paper through authorized institutional access, parses it with MinerU, and stages it under the ignored `raw/tmp/`. Batch imports use `tools/convert_with_mineru.ps1`, which applies the keyword filter in `tools/mec_relevance.ps1`.
2. **Raw.** The maintainer moves the paper folder into `raw/sources/<Folder>/`. The Markdown parse is the evidence of record; the PDF resolves parse errors such as garbled formulas.
3. **Curated.** A `wiki/sources/<author-year-slug>.md` page is written from the parse according to [`schema.md`](schema.md), then linked to concept and entity pages and added to `wiki/index.md` and `wiki/log.md`.
4. **Grounded.** Every card symbol and number and every Related Work sentence is checked against the parse, and the evidence lines are recorded in a `wiki/.grounding/` sidecar.
5. **Synthesized.** Finding, comparison, synthesis, methodology, query, and thesis pages cite the source when the evidence supports a cross-paper claim.

`python tools/wiki/curation_status.py --dupes` lists raw folders that have no source page and flags duplicate ingests.

## Quality gates

Run from the repository root before every commit. The scripts use only the Python standard library.

| Command | Checks | Passes when |
|---|---|---|
| `python tools/wiki/linkcheck.py` | Every wikilink resolves under Obsidian rules | No dangling links |
| `python tools/wiki/frontmatter_audit.py` | Required keys, type matches directory, type-specific tags | 0 errors |
| `python tools/wiki/index_audit.py` | Every page is catalogued exactly once in `wiki/index.md` | No gaps or duplicates |
| `python tools/wiki/process_refs.py` | No batch or run narration outside `wiki/log.md` | 0 hits |
| `python tools/wiki/source_schema_audit.py` | Source-page section order, card, and Related Work structure | 0 errors |
| `python tools/wiki/source_schema_manifest.py --evidence "wiki/.grounding/source-schema-evidence-*.json" --require-grounded` | Each source page maps to one parse and has grounding evidence | All pages grounded, 0 conflicts |
| `python tools/wiki/curation_status.py --dupes` | Raw folders without a source page | No new papers |
| `python -m unittest discover -s tools/wiki/tests` | Toolkit unit tests | All pass |

The structural audits cannot verify facts. Factual accuracy rests on the grounding review and its recorded evidence. [`tools/wiki/README.md`](tools/wiki/README.md) documents every script, flag, and exit code.

## Setup

```sh
git lfs install
git clone https://github.com/EnosElinsa/mec-research-wiki.git
```

The PDFs take about 1.7 GB. To clone only the text, set `GIT_LFS_SKIP_SMUDGE=1` before cloning (PowerShell: `$env:GIT_LFS_SKIP_SMUDGE = "1"`), then fetch individual PDFs later with `git lfs pull --include "<path>"`.

Requirements:

- Python 3 for `tools/wiki/` (standard library only; tested with Python 3.14).
- Windows PowerShell 5.1 or later, Node.js, the `mineru-open-api` CLI (`npm install -g mineru-open-api`), and a `MINERU_TOKEN` environment variable for `tools/convert_with_mineru.ps1`.
- Chrome, Node.js, a MinerU token, and institutional credentials for `retrieve-ieee-papers`; its [SKILL.md](.agents/skills/retrieve-ieee-papers/SKILL.md) covers the one-time encrypted secret setup.

## Agent roles

Maintenance is split across four agent roles defined in [`.codex/agents/`](.codex/agents/). Each role has a fixed write scope, and only one writer at a time owns `wiki/index.md`, `wiki/overview.md`, `wiki/log.md`, and Git.

| Agent | Writes | Hands off |
|---|---|---|
| `mec-wiki-curator` | New source pages plus the concept, entity, index, overview, and log updates they need | Synthesis, audits, and the reference database |
| `mec-wiki-auditor` | Verified corrections to existing pages: metadata, claims, links, counts, grounding | New papers to the curator, coverage gaps to the synthesizer |
| `mec-wiki-synthesizer` | Finding, synthesis, comparison, methodology, query, and thesis pages and their cross-links | New papers to the curator |
| `mec-reference-scout` | `wiki/references/` and the reference tools | Curation and analytical pages |

[`CONTRIBUTING.md`](CONTRIBUTING.md) summarizes the shared rules for both human and agent maintainers.

## Known limitations

- Most papers in the corpus report simulation results. [Hardware validation and the sim-to-real gap](wiki/synthesis/hardware-validation-and-sim-to-real-in-mec.md) lists the few with physical experiments.
- Nine foundational machine-learning papers (DQN, DDPG, PPO, TD3, and five others) have no numbered reference list that `tools/wiki/mine_refs.py` can split, so the reference database covers 690 of the 699 parses.

## Copyright and license

| Material | License |
|---|---|
| Code and agent configuration: `tools/`, `.agents/`, `.codex/` | [MIT](LICENSE-MIT) |
| Original wiki text and documentation: `wiki/`, `ideas/`, and the Markdown files in the repository root | [CC BY 4.0](LICENSE-CC-BY-4.0) |
| Papers under `raw/sources/` (PDFs, parsed text, figures) | Not licensed by this repository; see below |

The papers under `raw/sources/` are the work of their authors and publishers and remain under their original copyright and license terms. The same applies to equations, figures, and short quotations from those papers that appear in wiki pages. To request removal of a paper, open an issue.

To reuse wiki text under CC BY 4.0, credit "MEC Research Wiki (EnosElinsa)" and link to this repository.
