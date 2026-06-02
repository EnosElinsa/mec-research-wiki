---
type: synthesis
title: "Swarm-intelligence metaheuristics across the UAV-MEC corpus"
tags: [synthesis, metaheuristic, swarm-intelligence, multi-objective, classical-solver, optimization]
related:
  - "[[particle-swarm-optimization]]"
  - "[[whale-optimization-algorithm]]"
  - "[[binary-whale-optimization]]"
  - "[[salp-swarm-algorithm]]"
  - "[[multi-verse-optimizer]]"
  - "[[ant-lion-optimizer]]"
  - "[[gravitational-search-algorithm]]"
  - "[[ant-colony-optimization]]"
  - "[[self-adaptive-global-best-harmony-search]]"
  - "[[sun-2021-temcmop-uav-cb]]"
  - "[[liang-2024-hmecmop-uav-cb]]"
  - "[[zheng-2024-recmop-uav-cb]]"
  - "[[li-2024-emssa-uav-swarm-vaa]]"
  - "[[sun-2024-imssa-uav-secure-cb]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
  - "[[huang-2025-dual-aav-maritime-secure-cb]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
  - "[[gao-2024-sagin-perception-offloading]]"
  - "[[mao-2024-ntn-hierarchical-caching-cav]]"
  - "[[wang-2025-acbft-uav-consensus]]"
  - "[[zhang-2024-uav-task-offloading-ddpg]]"
  - "[[albakhrani-2025-moalf-uav-mec]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[cmop-evolutionary-uav-mec-lineage]]"
  - "[[drl-vs-evolutionary-vs-classical-solvers]]"
  - "[[mixed-integer-nonlinear-programming]]"
created: 2026-06-03
updated: 2026-06-03
---

# Swarm-intelligence metaheuristics across the UAV-MEC corpus

A recurring solver choice in the corpus is the **nature-inspired swarm metaheuristic** — a population of candidate solutions that move through the search space by an imitation rule (whales bubble-netting, salps chaining, antlions trapping, masses gravitating, ants laying pheromone) and, in the multi-objective case, emit a **Pareto set in one run** that a decision-maker picks from afterward. The corpus carries pages for nine distinct such algorithms, each anchored to the source(s) that use it; this page ties the family together: which algorithm appears where, the two distinct *roles* they play, the shared "improved-variant" toolkit nearly all of them carry, and the rationale the sources give for reaching for a swarm method over DRL or convex optimization.

It is the metaheuristic counterpart to the [[drl-backbones-across-uav-mec-sources|DRL-backbone]] map and a sibling to the [[cmop-evolutionary-uav-mec-lineage|CMOP-evolutionary lineage]] (which is the corpus's *population-based evolutionary* thread — distinct machinery, overlapping motivation). It also expands the solver axis that [[collaborative-beamforming-in-aerial-mec]] tabulates for the beamforming subset and that [[drl-vs-evolutionary-vs-classical-solvers]] argues at the family level.

## Roster: which swarm algorithm appears where

| Algorithm | Concept page | Source(s) | Variant used | Role in the source |
|---|---|---|---|---|
| Particle swarm | [[particle-swarm-optimization]] | [[wang-2025-acbft-uav-consensus]]; [[zhang-2024-uav-task-offloading-ddpg]]; [[albakhrani-2025-moalf-uav-mec]] | chain-ordering PSO; improved PSO (IPSO); adaptive PSO (APSO) | Embedded sub-solver (block ordering / offloading decision / one ingredient of a multi-technique framework) |
| Whale optimization | [[whale-optimization-algorithm]] | [[wu-2025-iopo-irs-uav-thz-mec]] | WOA (continuous) | Stage-2 sub-solver for continuous IRS phase shifts (given a stage-1 offloading decision) |
| Binary whale | [[binary-whale-optimization]] | [[jia-2025-dro-uav-hap-mec]] | BWOA | Binary task-offloading sub-problem after primal decomposition of a MISOCP |
| Salp swarm | [[salp-swarm-algorithm]] | [[li-2024-emssa-uav-swarm-vaa]]; [[sun-2024-imssa-uav-secure-cb]] | EMSSA; IMSSA | Standalone multi-objective solver for collaborative-beamforming MOPs |
| Multi-verse | [[multi-verse-optimizer]] | [[liu-2025-haps-uav-maritime-iot]]; [[liang-2024-hmecmop-uav-cb]] | EMOMVO-CGD; IMOMVO | Standalone multi-objective solver (maritime association; CB hovering-vs-motion energy) |
| Ant lion | [[ant-lion-optimizer]] | [[sun-2021-temcmop-uav-cb]] | IMOALO | Standalone multi-objective solver for the time/VAA-time/energy CB MOP (the corpus's earliest CB entry) |
| Gravitational search | [[gravitational-search-algorithm]] | [[zheng-2024-recmop-uav-cb]] | IMOGSA | Standalone multi-objective solver for the reliability + propulsion-energy CB MOP |
| Ant colony | [[ant-colony-optimization]] | [[mao-2024-ntn-hierarchical-caching-cav]] | DM-ACO | Embedded sub-solver selecting which LEO satellites cache content (minimize propagation delay) |
| Harmony search | [[self-adaptive-global-best-harmony-search]] | [[gao-2024-sagin-perception-offloading]] | SGHS | Embedded sub-solver for the BS compute-resource-allocation sub-problem (P3) inside a DRL+Lyapunov pipeline |

A tenth, the **mayfly algorithm**, appears once: [[huang-2025-dual-aav-maritime-secure-cb]] uses an improved multi-objective mayfly (IMOMA) for its secure dual-AAV collaborative-beamforming MOP. It has no dedicated concept page (single-source vocabulary); the source page records it and conceptually groups it with the salp-swarm CB optimizers.

## Two distinct roles, not one

The roster splits cleanly into two usage modes, and the split matters more than the choice of metaphor:

**1. Standalone multi-objective Pareto solver.** [[sun-2021-temcmop-uav-cb]] (ALO), [[liang-2024-hmecmop-uav-cb]] + [[liu-2025-haps-uav-maritime-iot]] (MVO), [[li-2024-emssa-uav-swarm-vaa]] + [[sun-2024-imssa-uav-secure-cb]] (SSA), [[zheng-2024-recmop-uav-cb]] (GSA), and [[huang-2025-dual-aav-maritime-secure-cb]] (mayfly) each take the *whole* problem — proven NP-hard, mixed continuous/discrete, often large-scale — and return a non-dominated set across two or three genuinely conflicting objectives (rate/secrecy/time vs flight energy). This is almost entirely a **collaborative-beamforming** phenomenon: all but the maritime-association case form a [[collaborative-beamforming|virtual antenna array]] whose element positions are decision variables. See [[collaborative-beamforming-in-aerial-mec]] for the CB-specific objective table.

**2. Embedded single-objective sub-solver.** [[gao-2024-sagin-perception-offloading]] (SGHS for P3), [[jia-2025-dro-uav-hap-mec]] (BWOA for binary offloading), [[wu-2025-iopo-irs-uav-thz-mec]] (WOA for stage-2 phase shifts), [[mao-2024-ntn-hierarchical-caching-cav]] (DM-ACO for caching placement), and the PSO trio ([[wang-2025-acbft-uav-consensus]], [[zhang-2024-uav-task-offloading-ddpg]], [[albakhrani-2025-moalf-uav-mec]]) drop a swarm metaheuristic *inside* a larger decomposition — after a convex/Lyapunov/DRL layer has peeled off the part it can handle, the metaheuristic mops up the non-convex combinatorial remainder. Here the swarm method is a component, not the headline contributor.

The practical reading: a standalone swarm solver signals "the authors wanted the whole Pareto front and had no real-time constraint"; an embedded one signals "a sub-problem resisted convex relaxation and didn't justify a second learner."

## The shared "improved-variant" toolkit

Almost none of the sources use a textbook swarm algorithm. Every standalone solver is an *improved/enhanced multi-objective* variant ("I-/E-MO-" prefix), and the improvements recur across metaphors — the family shares a toolkit even where the metaphor differs:

- **Chaotic / opposition-based-learning initialization** to raise initial-population quality: chaos-OBL in [[sun-2021-temcmop-uav-cb]] (IMOALO) and [[huang-2025-dual-aav-maritime-secure-cb]] (IMOMA); quasi-opposition-based learning in [[zheng-2024-recmop-uav-cb]] (IMOGSA); circle-map (chaotic) initialization in [[sun-2024-imssa-uav-secure-cb]] (IMSSA); chaos for exploration in [[liu-2025-haps-uav-maritime-iot]] (EMOMVO-CGD).
- **A discrete / hybrid solution-update operator** so the algorithm can handle the mixed continuous + discrete solution space (positions/weights are continuous; BS-serving order or task-to-node association is discrete) that conventional variants struggle with: hybrid update in IMOALO and IMOMA; discrete update strategy in IMOGSA and IMSSA; discrete-update for binary association in EMOMVO-CGD.
- **Archive refinement borrowed from evolutionary computation**: an NSGA-II-style crossover/mutation archive optimizer in [[zheng-2024-recmop-uav-cb]] (IMOGSA); a hypercube-pruned non-dominated archive is the MSSA baseline mechanism the [[salp-swarm-algorithm]] variants build on; a BBO-inspired migration + adaptive-mutation operator in IMSSA.

The convergence story they report is qualitative or figure-level: IGD/hypervolume curves and "outperforms swarm baselines" (e.g. [[huang-2025-dual-aav-maritime-secure-cb]] reports IGD stabilizing after ~200 iterations and beating MODA/MALO/MOMVO/MOMA). Treat exact margins as indicative.

## Why a swarm method here (the sources' own rationale)

The clearest statement is in [[zheng-2024-recmop-uav-cb]], which picks GSA explicitly against the two alternatives the corpus otherwise leans on: unlike **DRL** it needs no costly model training (the UAVs themselves run the solver), and unlike **convex optimization** it does not transform or distort the original solution space. The [[multi-verse-optimizer]] and [[binary-whale-optimization]] pages give the same verdict from the embedded-sub-solver side: reach for a swarm metaheuristic "when convex relaxation isn't available and DRL would be overkill" — cheap, gradient-free, no training, no convergence guarantee, but reasonable empirical performance on the corpus's UAV-MEC instances, and a one-run Pareto set when the objectives genuinely conflict.

This places the family precisely between the corpus's other two solver camps:

- **vs convex/AO pipelines** ([[ao-sdr-sca-convex-pipeline]], [[lyapunov-guided-drl]]): swarm methods accept non-differentiable, non-convex objectives directly (turning angles, sidelobe levels, mixed integers) instead of relaxing or majorizing them — at the price of optimality guarantees.
- **vs DRL** ([[drl-backbones-across-uav-mec-sources]]): swarm methods run offline per mission plan with no training phase, but cannot do per-slot inference; the embedded cases ([[gao-2024-sagin-perception-offloading]], [[wu-2025-iopo-irs-uav-thz-mec]]) pair a swarm sub-solver with a learner precisely to get both.

## Where the "consensus" is really one research line

The standalone multi-objective Pareto-solver cluster is heavily concentrated: [[sun-2021-temcmop-uav-cb]], [[li-2024-emssa-uav-swarm-vaa]], [[sun-2024-imssa-uav-secure-cb]], [[liang-2024-hmecmop-uav-cb]], and [[zheng-2024-recmop-uav-cb]] all come from the [[geng-sun]]-group collaborative-beamforming line (with [[huang-2025-dual-aav-maritime-secure-cb]] and [[liu-2025-haps-uav-maritime-iot]] adjacent in the maritime CB space). So the apparent multi-algorithm "consensus" that swarm metaheuristics suit aerial multi-objective MOPs is, in large part, **one lab cycling through metaheuristic metaphors** (ALO → MVO → GSA → SSA → mayfly) on structurally similar CB problems, each time adding the same family of chaos-init + discrete-update improvements. The embedded sub-solver uses (PSO, ACO, SGHS, BWOA, WOA) are more authorially diverse and more independent evidence that the *embedded* role is broadly useful.

## Gaps

- **No swarm solver carries a per-slot deployment claim.** Every standalone use is a mission-plan-tier offline optimizer; none is evaluated as a real-time controller. The closest the corpus comes to "swarm + reactivity" is the embedded pairing with a learner.
- **No head-to-head swarm-vs-DRL on the same problem.** As with the evolutionary lineage, the swarm sources benchmark against *other swarm/evolutionary* baselines (MODA, MOPSO, NSGA-II, conventional MOALO/MOMVO/MOMA), not against a DRL controller on the identical instance — so the "DRL would be overkill" claim is argued from problem shape, not measured. See [[drl-vs-evolutionary-vs-classical-solvers]].
- **Metaphor proliferation, shared substance.** Nine-plus distinct nature metaphors deliver the *same* mixed-variable Pareto search with the *same* chaos-init + discrete-update improvements. Whether the choice of metaphor matters beyond the improvement operators is untested in the corpus.
- **No hardware validation of a swarm solver** beyond the Raspberry Pi implementation that accompanies [[sun-2024-imssa-uav-secure-cb]]'s CB demonstration; the rest are simulation-only.

## See also

- [[collaborative-beamforming-in-aerial-mec]] — the CB track map; its solver column overlaps the standalone-Pareto subset here.
- [[cmop-evolutionary-uav-mec-lineage]] — the corpus's evolutionary (CMOEA/differential-evolution) thread; population-based like the swarm family but a distinct machinery and a different author network.
- [[drl-vs-evolutionary-vs-classical-solvers]] — the family-level "which solver when" synthesis this page feeds.
- [[mixed-integer-nonlinear-programming]] — the problem class nearly every swarm use targets.
