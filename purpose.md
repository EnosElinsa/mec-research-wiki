# Project Purpose: MEC Research Wiki

## Research Question

> How do mobile edge computing (MEC) systems formulate and solve their joint offloading, resource-allocation, and trajectory or deployment decisions; which of those formulations and solution methods carry over between UAV, HAP, satellite, vehicular, maritime, and terrestrial settings; and under which assumptions do the reported gains hold?

The wiki answers this at two levels. Each source page records one paper's model and results, grounded in its full text. Analytical pages (synthesis, comparison, methodology, finding, query, thesis) compare those records across papers.

## Hypothesis / Working Thesis

> Problem structure should be exploited, not learned. Across the corpus, designs that split a joint problem along its structure (discrete versus continuous decisions, long-term versus per-slot time scales) and enforce hard, long-term, or robustness constraints with an explicit mechanism are preferred over end-to-end DRL policies that learn every decision and constraint from reward.

Three thesis pages track this position, each with its evidence and the results that would refute it:

- [[decomposition-beats-end-to-end-drl-in-mec]]: confidence medium, status supported.
- [[explicit-constraints-beat-reward-shaping-in-mec-drl]]: confidence medium, status supported.
- [[hybrid-action-memory-augmented-drl-wins-uav-mec]]: confidence medium, status supported; scoped to one UAV-MEC framework.

Truly end-to-end DRL is rare in the corpus ([[end-to-end-drl-feasibility-large-scale-mec]]), so much of the support for the first thesis is design consensus rather than head-to-head comparison.

## Background

MEC research is large, recent, and split by deployment type. Most papers combine a small set of system-model components (air-to-ground channel, propulsion energy, computation, queue, and age-of-information models) with a small set of solver pipelines, for example [[ao-sdr-sca-convex-pipeline]], [[lyapunov-guided-drl]], [[ctde-multi-agent-drl-protocol]], and the [[cmop-evolutionary-uav-mec-lineage]]. Surveys usually organize this work by application, which hides the shared structure.

This wiki indexes papers by model and method instead. Its goal is that a new system model or problem formulation can start from grounded, comparable prior work: the Modeling Quick-Use Card gives each paper's decisions, objective, and constraints in a fixed layout, and the Related Work paragraph gives a citation-ready summary of what the paper did and reported.

## Sub-questions

1. Which system-model components recur, and under which assumptions? See concept pages such as [[air-to-ground-channel-model]] and [[rotary-wing-propulsion-energy-model]], and [[constraint-regimes-in-uav-data-collection]] for how constraint choices differ across papers.
2. When does decomposition or classical optimization outperform a learned policy, and when is online learning necessary? See [[drl-vs-evolutionary-vs-classical-solvers]] and [[decomposition-beats-end-to-end-drl-in-mec]].
3. How do papers enforce hard, long-term, and robustness constraints, and what does each mechanism guarantee? See [[safety-and-robustness-mechanisms-in-mec]] and [[query-when-does-dro-beat-drl-for-csi-uncertainty]].
4. How far does the reported evidence reach beyond simulation? See [[hardware-validation-and-sim-to-real-in-mec]] and [[query-real-world-validation-of-jppo-en-convntm]].
5. Which operational problems (energy replenishment, service continuity, hierarchical aerial cooperation, mobility) remain open enough to seed new research? See [[uav-energy-replenishment-and-service-continuity]], [[hierarchical-aerial-mec-design-space]], and the drafts in `ideas/`.

## Scope

**In scope:**

- MEC in any deployment: UAV-, HAP-, and satellite-assisted, vehicular, maritime, space-air-ground integrated, and terrestrial.
- Decisions: task offloading, computation and communication resource allocation, caching, service placement and migration, trajectory, deployment, and user association.
- Solution methods: convex and non-convex optimization, game theory, evolutionary and swarm metaheuristics, single- and multi-agent DRL, and LLM- or generative-AI-assisted optimization.
- Adjacent topics that MEC system models build on: UAV communications and channel models, ISAC, RIS, physical-layer security and covert communication, federated and split learning, energy harvesting and wireless power transfer, blockchain, and digital twins.

**Out of scope:**

- Papers without a full-text parse. Titles and abstracts alone are not curated.
- Non-paper media (talks, books, blog posts) until `schema.md` defines a contract for them.
- Work that no MEC system model draws on. The ingest keyword filter is `tools/mec_relevance.ps1`.

## Methodology

- **Sources.** Journal, magazine, and conference papers, mostly from IEEE venues. Each paper is parsed to Markdown with MinerU; the parse is the evidence of record, and the PDF resolves parse errors.
- **Curation.** One source page per paper, written to the paper-source contract in `schema.md`. Metadata, numbers, baselines, and guarantees come from the parse; the web is used only to verify metadata the parse omits.
- **Grounding.** Every card symbol and number and every Related Work sentence is checked against the parse, and the evidence lines are recorded in `wiki/.grounding/`.
- **Analysis.** A derived page is created only when the evidence supports it. Theses state confidence, status, and refutation criteria. Contradictions between sources go to a query page until a synthesis resolves them.
- **Verification.** Structural gates in `tools/wiki/` (links, frontmatter, index coverage, source schema, grounding manifest, evergreen wording) run before every commit.
- **Idea generation.** Research-idea drafts in `ideas/` are built from the wiki and the raw parses, and state the limits of their novelty checks.

## Success Criteria

- Every paper in `raw/sources/` has a source page with grounding evidence.
- Every recurring formulation and solver family has a synthesis, comparison, or methodology page that cites its sources.
- Every thesis has explicit refutation criteria and a current status.
- A system-model or problem-formulation section can be drafted from the cards and Related Work paragraphs without rereading the full papers.
- The structural gates pass on every commit.

## Current Status

> As of 2026-11-05: 699 papers curated and grounded (593 with a modeling card, 106 without), 665 concepts, 211 entities, and 57 analytical pages. No raw paper is waiting for curation.
>
> The reference database holds 21,510 unique references mined from 690 parses. The main open item is the analytical layer, which is thin relative to the source layer (15 findings for 699 sources).
