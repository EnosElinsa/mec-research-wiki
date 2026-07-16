# Wiki Schema — Research Deep-Dive

## Page Types

| Type | Directory | Purpose |
|------|-----------|---------|
| entity | wiki/entities/ | Named things (people, tools, organizations, datasets) |
| concept | wiki/concepts/ | Ideas, techniques, phenomena, frameworks |
| source | wiki/sources/ | Papers, articles, talks, books, blog posts |
| query | wiki/queries/ | Open questions under active investigation |
| comparison | wiki/comparisons/ | Side-by-side analysis of related entities |
| synthesis | wiki/synthesis/ | Cross-cutting summaries and conclusions |
| overview | wiki/ | High-level project summary (one per project) |
| thesis | wiki/thesis/ | Working hypothesis and its evolution over time |
| methodology | wiki/methodology/ | Research methods, protocols, and study designs |
| finding | wiki/findings/ | Individual empirical results or observations |

## Naming Conventions

- Files: `kebab-case.md`
- Entities: match official name where possible (e.g., `openai.md`, `gpt-4.md`)
- Concepts: descriptive noun phrases (e.g., `chain-of-thought.md`)
- Sources: `author-year-slug.md` (e.g., `wei-2022-cot.md`)
- Queries: question as slug (e.g., `does-scale-improve-reasoning.md`)
- Theses: hypothesis as slug (e.g., `scaling-improves-reasoning.md`)
- Methodologies: method name (e.g., `systematic-review.md`, `ablation-study.md`)
- Findings: descriptive slug (e.g., `larger-models-better-few-shot.md`)

## Frontmatter

All pages must include YAML frontmatter:

```yaml
---
type: entity | concept | source | query | comparison | synthesis | overview
title: Human-readable title
tags: []
related: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Source pages also include:
```yaml
authors: []
year: YYYY
url: ""
venue: ""
```

Paper-backed source pages also include exactly one of:

```yaml
modeling_card: required
```

```yaml
modeling_card: not_applicable
```

Thesis pages also include:
```yaml
confidence: low | medium | high
status: speculative | supported | refuted | settled
```

Finding pages also include:
```yaml
source: "[[source-slug]]"
confidence: low | medium | high
replicated: true | false | null
```

## Paper Source Contract

### Evidence authority

- A paper source is grounded in the Markdown parse under `raw/sources/<folder>/`, either `full.md` or a title-named `.md`. The companion PDF resolves parse omissions or corruption.
- The current workflow remains raw-parse driven. It does not introduce `.bib` lookup, BibTeX citekey filenames, or `source_id`, `source_type`, `base_confidence`, or `lifecycle` fields.
- Every Modeling Quick-Use Card symbol, expression, and numerical statement, and every sentence in the Related Work paragraph, must be traceable to the raw parse or companion PDF.

The current `wiki/sources/` corpus is paper-backed and follows this contract. If a future source is a talk, book, blog post, or other non-paper medium, revise the schema with an explicit discriminator before adding it rather than silently forcing the paper contract onto that page.

### Modeling-card applicability

Use `modeling_card: required` when the paper's central contribution contains an application-specific, reusable decision or control model with all of the following:

- explicit decision variables or actions;
- an objective, utility, cost, or reward;
- constraints, a feasible domain, or state/action limits.

Qualifying formulations include MINLP, convex, stochastic, or robust optimization, games, MDP/POMDP models, scheduling, and trajectory control when those elements are present.

Use `modeling_card: not_applicable` for surveys and tutorials, foundational algorithm papers, pure prediction, channel-estimation, measurement, or detection papers, and systems or protocols without a reusable decision model. A training loss or evaluation metric alone does not qualify. These exclusions take precedence over generic mathematical or RL background in a foundational-method paper.

For a borderline paper, inspect the raw parse or PDF before deciding. A title, tag, or `System model` heading is not evidence of applicability.

### Canonical early-section order

Paper source pages follow this order:

```text
Citation
TL;DR
[Modeling Quick-Use Card, only when modeling_card: required]
Related Work Paragraph
Problem framing
System model
Method
Key findings
Limitations / future work
Relation to the corpus
Raw artifacts
```

`TL;DR` is the positioning section. Do not add a separate one-line-positioning heading. Existing semantically equivalent detailed headings may remain during migration; valid prose does not need to be rewritten solely to rename a heading. The exact relative order of `Citation`, `TL;DR`, the optional card, and `Related Work Paragraph` is mandatory. A `not_applicable` page must not contain a Modeling Quick-Use Card.

### Modeling Quick-Use Card

Copy this English template only when `modeling_card: required`:

```markdown
## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: <network topology, nodes, application, assumptions, multiple-access scheme, and channel model>.

**Problem & objective**: <problem name or number, problem type, objective formula, and optimization metric>.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| <variable name> | $<symbol>$ | <binary, continuous, or integer range> | <meaning> |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | <constraint meaning and expression> |

**Algorithm**: <method family and step-by-step solution chain>.
```

Do not leave core fields or table cells blank, and do not use `N/A`, `TBD`, `...`, or a dash as a substitute for grounded content. The card is a concise reusable view, not a replacement for the detailed model and method sections. Its symbols and formulas must match those sections and the paper.

### Related Work Paragraph

Every paper-backed source page contains this section immediately after `TL;DR` and the optional card:

```markdown
## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Author et al. [x] studied <the paper's stated problem or scheme> in <the paper's scenario>. They formulated <the problem and objective> and proposed <the method and its key steps>. Simulation or experimental results show <the paper's reported findings>.
```

The prose must:

- be one English paragraph of 4-8 sentences;
- cover scenario, problem and objective, method steps, and the paper's principal reported results;
- preserve Abstract and Introduction terminology where possible;
- use `[x]` at the author citation;
- contain no internal wikilinks, CJK text, em dash, or `--`;
- state only what the paper did and reported, without wiki-authored comparison, evaluation, or gap claims.

Paper-reported comparisons are allowed when worded as reported results. The structural audit cannot establish factual grounding, so sentence-level evidence review remains mandatory.

## Index Format

`wiki/index.md` lists all pages grouped by type. Each entry:
```
- [[page-slug]] — one-line description
```

## Log Format

`wiki/log.md` records activity in reverse chronological order:
```
## YYYY-MM-DD

- Action taken / finding noted
```

## Cross-referencing Rules

- Use `[[page-slug]]` syntax to link between wiki pages
- Every entity and concept should appear in `wiki/index.md`
- Queries link to the sources and concepts they draw on
- Synthesis pages cite all contributing sources via `related:`
- Findings link back to their source via the `source:` frontmatter field
- Thesis pages reference supporting and refuting findings via `related:`
- Methodology pages are cited by the findings that used them

## Contradiction Handling

When sources contradict each other:
1. Note the contradiction in the relevant concept or entity page
2. Create or update a query page to track the open question
3. Link both sources from the query page
4. Resolve in a synthesis page once sufficient evidence exists

## Research-Specific Conventions

- Keep the thesis pages updated as evidence accumulates — they are living documents
- Every finding should assess replication status when known
- Methodology pages explain the *why* (rationale) not just the *how*
- Distinguish between direct evidence and inference in finding pages
