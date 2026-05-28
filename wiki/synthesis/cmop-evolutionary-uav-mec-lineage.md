---
type: synthesis
title: "The CMOP-evolutionary UAV-MEC lineage (Peng/Huang group, 2022-2026)"
tags: [synthesis, cmop, evolutionary-algorithm, uav, mec, lineage, classical-solver]
related:
  - "[[peng-2022-cmop-uav-path-planning]]"
  - "[[peng-2024-energy-time-uav-its]]"
  - "[[huang-2023-mu-aec-task-energy]]"
  - "[[huang-2025-cmop-dispersed-computing]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
  - "[[xie-2026-uav-multisource-fusion]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[cmoea-d-cdp]]"
  - "[[infeasible-individual-utilization]]"
  - "[[dual-population-evolutionary-algorithm]]"
  - "[[multi-tasking-evolutionary-algorithm]]"
  - "[[local-search-evolutionary]]"
  - "[[b-spline-trajectory]]"
  - "[[chaoda-peng]]"
  - "[[xumin-huang]]"
  - "[[yuan-wu]]"
  - "[[jiawen-kang]]"
created: 2026-05-29
updated: 2026-05-29
---

# The CMOP-evolutionary UAV-MEC lineage (Peng/Huang group, 2022-2026)

A four-year program by the Peng/Huang/Wu/Kang group across South China Agricultural University, Guangdong University of Technology, and the University of Macau. Six sources in the wiki, all sharing a common template and refining it for new MEC scenarios. This page maps the lineage so future readers can navigate it as a single thread rather than six independent papers.

## Roster

| Year | Source | First author | Sub-problem |
|---|---|---|---|
| 2022 | [[peng-2022-cmop-uav-path-planning]] | Chaoda Peng | UAV path planning + offloading (lineage seed) |
| 2023 | [[huang-2023-mu-aec-task-energy]] | Xumin Huang | Multi-UAV interdependent (DAG) task scheduling |
| 2024 | [[peng-2024-energy-time-uav-its]] | Chaoda Peng | UAV-ITS energy + completion-time-difference + service caching |
| 2025 | [[huang-2025-cmop-dispersed-computing]] | Xumin Huang | Dispersed computing with task-redundancy reliability |
| 2026 | [[xie-2026-uav-multisource-fusion]] | Qiqi Xie | Vehicular cooperative perception (dynamic CMOO) |
| 2026 | [[wu-2026-terrain-aware-uav-mec]] | Zexiong Wu | Urban UAV-MEC with terrain-aware DEM channel |

[[chaoda-peng]] and [[xumin-huang]] are the two recurring first/lead authors. [[yuan-wu]] is on all six papers. [[jiawen-kang]] is on four.

## The shared template

Every paper in the lineage instantiates the same five-step pattern:

1. **Identify a UAV/MEC sub-problem** with at least two genuinely conflicting objectives (energy vs safety, energy vs time, latency vs charge, etc.).
2. **Cast as a constrained multi-objective optimization problem (CMOP)** with mixed-integer + continuous decision variables.
3. **Build a [[constrained-multi-objective-evolutionary-algorithm|CMOEA]]** on top of the [[cmoea-d-cdp]] framework — decomposition for diversity, constrained-domination for feasibility.
4. **Contribute one methodological knob** that's reusable across the lineage (a constraint-handling technique, a population structure, a genetic operator, a local search, a multi-tasking scheme).
5. **Compare against the previous lineage entry plus 1-2 external baselines** (typically ToP, PPS, NSGA-II, NSGA-III).

The result: a connected research program where each paper *picks up* the previous paper's knobs and *adds* one of its own.

## The methodological knobs

This is the spine of the lineage. Each row is a distinct contribution that compounds with the prior ones.

| Source | New knob | What problem it solves |
|---|---|---|
| [[peng-2022-cmop-uav-path-planning]] | **[[infeasible-individual-utilization]]** + dynamic α schedule | Constraint-handling: most CMOEAs throw away infeasibles. The seed shows that retaining strong-objective-but-infeasible individuals seeds exploration near the Pareto knee, where the optimum lives. |
| [[huang-2023-mu-aec-task-energy]] | **[[local-search-evolutionary]]** + DAG-respecting genetic operator | Convergence speed: local moves that respect predecessor ordering converge dramatically faster than blind crossover on DAG-structured assignment problems. |
| [[peng-2024-energy-time-uav-its]] | **Repair-based constraint handling** + data-type-aware genetic operator | Feasibility: surgically convert infeasibles into feasibles instead of discarding. Mixed integer/binary/continuous variables get specialized operators per type. |
| [[huang-2025-cmop-dispersed-computing]] | **[[dual-population-evolutionary-algorithm|Dual-population]]** scheme | Exploration-exploitation: a feasibility-strict main population and a diversity-loose auxiliary population co-evolve. Beats single-population on Pareto-front spread. |
| [[xie-2026-uav-multisource-fusion]] | **Dynamic CMOO** for time-varying constraints | Non-stationarity: sets of requesting users + observable objects change per cycle, so the CMOP itself is moving. Population-level priors carry over between cycles. |
| [[wu-2026-terrain-aware-uav-mec]] | **[[multi-tasking-evolutionary-algorithm|Multi-tasking]] CMOEA** + task-adaptive operator selection | Knowledge transfer: solve multiple related instances (different terrains) jointly, with a bandit-style mechanism picking which genetic operator to use per individual based on track record. |

A reader who needs *one* technique gets the corresponding paper. A reader who wants the *current* state-of-the-lineage gets [[wu-2026-terrain-aware-uav-mec]] — every prior knob is directly usable on top of it.

## What stays constant across the lineage

Three structural choices repeat in every paper:

- **[[b-spline-trajectory]]** for any UAV path. λ control points + spline interpolation makes the path differentiable and parameter-frugal.
- **CMOEA/D-CDP backbone**. Decomposition into N weight-vector subproblems + Constrained-Domination Principle for ranking.
- **Two genuinely conflicting objectives.** Single-objective scalarizations are explicitly rejected — the program's whole pitch is that the decision-maker should see the front.

The *application* changes — path planning → DAG → ITS → dispersed → fusion → urban — but the *machinery* stays close enough that techniques port across without re-engineering.

## Cross-referencing: what each new entry inherits

Reading the lineage as a graph rather than a list:

```
peng-2022 (seed: infeasibility-utilization)
   ├──→ huang-2023 (+ local search, DAG)
   ├──→ peng-2024 (+ repair CHT, data-type operator, service caching)
   │       └──→ huang-2025 (+ dual-population, parallel/serial, redundancy)
   ├──→ xie-2026 (+ dynamic CMOO, cooperative perception)
   └──→ wu-2026 (+ multi-tasking, terrain-aware channel)
```

`huang-2025` builds explicitly on `peng-2024`'s repair technique; `wu-2026` is a parallel branch that picks up the data-type operator and adds multi-tasking on top.

## Working theses

> **The CMOP-evolutionary lineage occupies a niche the wiki's DRL track does not fill: problems with truly conflicting objectives, brittle non-differentiable constraints (turning angle, terrain, redundancy threshold), and decision-makers who want to see the *whole* Pareto front rather than commit to a single scalar reward.**

Confidence: **high**. Six independent papers across four years, all reporting Pareto-front improvements over both DRL-style and prior-CMOEA baselines on UAV-MEC sub-problems, is strong evidence the niche is real.

> **The lineage's incremental contribution model — one new knob per paper — is itself a transferable research strategy.** Each knob is reusable, each comparison is anchored to the previous entry, and the cumulative methodological contribution is larger than any single paper would suggest.

Confidence: **medium**. The strategy works for this group; whether it generalizes is unclear. But it is a noteworthy contrast with one-shot DRL papers that propose a novel architecture and then move on.

## When to use a lineage technique vs DRL

Pick CMOEA-family when:

- You have **multiple conflicting objectives** without an obvious scalar combination.
- The constraints are **non-differentiable** (turning angle, mesh-distance terrain clearance, redundancy quorum).
- The decision-maker is **post-hoc** — they will pick from the front after seeing it, not commit a-priori to a single reward.
- The system is **mission-planned**, not real-time. Evolutionary search runs offline; per-decision DRL inference is sub-millisecond.

Pick DRL when:

- You need **per-slot decisions** at deployment time. Re-running an evolutionary search every slot is unaffordable.
- The environment is **non-stationary in ways DRL can adapt to during training** (channel drift, mobility, demand changes).
- The reward is **scalar and well-defined** (or at least scalarizable).

The lineage's [[xie-2026-uav-multisource-fusion]] and [[wu-2026-terrain-aware-uav-mec]] entries blur the line slightly — dynamic CMOO and multi-tasking add some online-adaptation flavor. But they are still mission-plan-tier solvers, not millisecond controllers.

## Limitations of the lineage as a whole

- **No hardware validation.** Every entry is simulation-only — same caveat as the rest of the wiki.
- **Computational cost is high.** All entries run 10⁴–10⁵ function evaluations. Real-time replanning is not in the scope.
- **No DRL ablation in the same paper.** The lineage compares against other evolutionary baselines (ToP, PPS, NSGA family) but doesn't run a fair head-to-head against a DRL controller on the same problem. This makes the "DRL-vs-evolutionary" question harder than it should be — see [[drl-vs-evolutionary-vs-classical-solvers]] for the cross-corpus take.
- **Group homogeneity.** All six papers come from the same network of authors. Independent replication on a different group's benchmark would strengthen the external validity claim.

## Open questions

1. **Does the methodological stack scale?** Six papers add six knobs. Are they all needed? A study that ablates each knob on the same benchmark (e.g. urban UAV-MEC with all six features turned on/off independently) would clarify which contributions carry the weight.
2. **Can the lineage absorb DRL?** A hybrid in which the evolutionary search proposes Pareto-frontier candidates and a DRL policy fine-tunes per-slot on each candidate would combine both worlds. None of the six papers takes this step.
3. **Where does the Stackelberg-game family in the wiki ([[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]]) connect?** Both are non-DRL, non-evolutionary solvers in the wiki. A three-way "evolutionary vs game-theoretic vs DRL" synthesis would clarify when each wins. Out of scope here.

## See also

- [[constrained-multi-objective-evolutionary-algorithm]] — concept page with method-level overview.
- [[drl-vs-evolutionary-vs-classical-solvers]] — cross-corpus solver-family synthesis (this lineage is the wiki's evolutionary representative).
- [[design-recipe-multi-uav-mec]] — DRL-track design recipe; sits on the opposite side of the spectrum.
