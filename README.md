# MEC Research Wiki

A long-running research deep-dive on **mobile edge computing (MEC)** in all its variants — task offloading, resource allocation, trajectory and infrastructure design, decision-making algorithms (RL, DRL, multi-agent, game-theoretic, optimization-based), and adjacent topics (UAVs, LEO satellites, vehicular networks, low-altitude economy, federated learning, blockchain / zero-trust, wireless power, etc.).

This wiki has no fixed sub-scope. Anything inside the MEC umbrella is fair game; sources accumulate over time and the graph grows with them. The structure is generic enough that the same page-type vocabulary works whether the next paper is about UAV trajectories, LEO offloading, vehicular caching, or something else under the MEC tent.

Built and indexed with [LLM Wiki](https://github.com/llm-wiki). Wikilinks (`[[page-slug]]`) form the graph; YAML frontmatter typing is enforced by `schema.md`.

## Layout

```
purpose.md          Research question, hypothesis, scope, methodology
schema.md           Page-type / frontmatter / cross-link conventions
wiki/               Curated knowledge graph (markdown + wikilinks)
  overview.md       Project state at a glance
  index.md          Type-grouped page directory
  log.md            Reverse-chronological activity log
  entities/        Named things (people, models, tools, datasets)
  concepts/        Ideas, techniques, frameworks
  sources/         Papers, articles, talks (curated)
  methodology/     Research methods and protocols
  findings/        Individual empirical results
  thesis/          Working hypotheses and their evolution
  queries/         Open questions
  comparisons/     Side-by-side analyses
  synthesis/       Cross-cutting summaries
raw/sources/       Untouched primary documents (PDFs, parsed markdown, images)
                   — files here are queued for ingestion; see "Source pipeline" below
```

See `schema.md` for naming and frontmatter rules. See `purpose.md` for the higher-level research framing.

## Source pipeline

A source has three states:

1. **Raw** — present under `raw/sources/<slug>/` (parsed markdown, original PDF, extracted images), but not yet reviewed or linked into the graph.
2. **Curated** — has a corresponding `wiki/sources/<author-year-slug>.md` with frontmatter, a TL;DR, and outbound wikilinks to the entities / concepts / findings it introduces.
3. **Synthesized** — its findings have been cross-linked from at least one synthesis page or thesis page.

The `raw/sources/` directory grows over time. Curation is intentionally lazy: papers stay raw until something asks them to be linked into the graph. Singleton concept pages aren't created for a single mention — wait for the second source.

## Working with the wiki

The local LLM Wiki desktop app indexes `wiki/**/*.md` and `raw/sources/**` and serves a JSON API on `http://127.0.0.1:19828`. Wikilinks (`[[page-slug]]`) are graph edges; frontmatter `related:` lists are explicit cross-references.

To curate a raw source:

1. Confirm the parsed markdown lives at `raw/sources/<slug>/full.md`.
2. Skim it and decide whether it's in scope for `purpose.md`. If marginal, leave it raw and note why in `wiki/log.md`.
3. Write `wiki/sources/<author-year-slug>.md` following `schema.md`. TL;DR, problem framing, method, findings, limitations, plus outbound wikilinks to the entities / concepts / findings it introduces.
4. Add or extend `wiki/concepts/`, `wiki/entities/`, and `wiki/findings/` pages as needed.
5. Update `wiki/index.md` and `wiki/log.md`.
6. Trigger a rescan via the LLM Wiki API or the desktop UI so the local index picks up the new files.
