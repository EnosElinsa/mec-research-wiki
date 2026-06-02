---
type: synthesis
title: "DRL vs evolutionary vs classical solvers across the MEC corpus"
tags: [synthesis, drl, evolutionary, classical, comparison, solver-family]
related:
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[two-stage-decomposition]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[distributionally-robust-optimization]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[stackelberg-game]]"
  - "[[lyapunov-optimization]]"
  - "[[binary-whale-optimization]]"
  - "[[multi-verse-optimizer]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
  - "[[cmop-evolutionary-uav-mec-lineage]]"
  - "[[safety-and-robustness-mechanisms-in-mec]]"
  - "[[lyapunov-guided-drl]]"
  - "[[hierarchical-aerial-mec-design-space]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[swarm-metaheuristics-in-uav-mec]]"
created: 2026-05-29
updated: 2026-06-03
---

# DRL vs evolutionary vs classical solvers across the MEC corpus

> **Scope note:** the family roster below is a **partial snapshot** of an earlier, smaller state of the corpus (26 sources), not a current census of the full corpus. The *qualitative* operating guidance still holds (and is reinforced by the [[sagin-satellite-offloading-landscape]], [[isac-sensing-in-aerial-mec]], and [[maritime-mec-architectures]] track syntheses), but the exact family counts here are not current. A full re-tally across the present corpus is future work.

Across the corpus, three solver families coexist in roughly comparable size, and the choice between them is a real design decision rather than a default. This page maps the families and gives operating guidance.

## Family roster (26-source partial snapshot)

| Family | Sources | Size |
|---|---|---|
| **DRL** (PPO/SAC/DQN/DDPG/MADDPG/MASAC etc.) | [[liu-2026-jppo-en-convntm]], [[peng-2025-drudm-cfg]], [[zhang-2025-ssac-mgi-heterogeneous-uav]], [[zhang-2025-mcma-task-migration]], [[zhu-2025-lycnn-drl-wpt-mec]], [[hao-2025-priority-aware-task-driven-co]], [[mao-2025-bcsa-frl]], [[qin-2025-bcuav-masac]], [[ma-2025-pdqn-vehicular-mec]], [[bao-2025-ddpg-video-offloading]], [[nabi-2025-jour-hierarchical-aerial]], [[hsu-2025-drl-hues-hap-noma]] | **12** |
| **Evolutionary / metaheuristic** | 6-paper [[cmop-evolutionary-uav-mec-lineage\|CMOP-evolutionary lineage]] (peng-2022, huang-2023, peng-2024, huang-2025, xie-2026, wu-2026) + [[liu-2025-haps-uav-maritime-iot]] (EMOMVO-CGD as whole-MOP solver) | **7 main**, plus BWOA stage in [[jia-2025-dro-uav-hap-mec]] (counted in Classical) |
| **Classical** (convex / Stackelberg / matching / AO+SDR+SCA / DRO+CVaR) | [[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]], [[wang-2026-aerial-marine-msar]], [[benaya-2025-aerial-isac-haps]], [[jia-2025-dro-uav-hap-mec]] | **5** |
| **Surveys / overviews** (no solver) | [[wang-2025-lae-network-survey]], [[jiang-2025-isac-lae-overview]] | 2 |

**Note on overlap.** Several sources fit multiple families. [[jia-2025-dro-uav-hap-mec]] is *primarily* classical (DRO + CVaR + primal decomposition + CVX) but uses BWOA (a metaheuristic) for the binary subproblem after decomposition. [[wang-2026-aerial-marine-msar]] uses matching (classical) + quasi-convex (classical) + PGD (classical) but in a multi-stage decomposition. The "family" label here means *primary* solver responsibility for the non-trivial sub-problem.

## Family characteristics

| Axis | DRL | Evolutionary | Classical |
|---|---|---|---|
| Output shape | Trained policy | Pareto front | Single solution (per scalarization) |
| Setup time | High (training) | Medium (per problem) | Low |
| Per-decision time | Sub-millisecond | Hours | Milliseconds–seconds |
| Optimality guarantees | None | Empirical Pareto-optimal | Local (convex sub) / global (special) |
| Handles non-stationarity | Yes (training) | Per-problem only | Per-problem only |
| Handles non-differentiable constraints | Poorly | Well | Depends |
| Handles multi-objective | Via reward shaping | Native | Via scalarization |
| Provable robustness | No | No | Yes (DRO/CVaR) |

These are tendencies, not laws — the corpus has counter-examples for most rows. But they explain the family choices the actual authors make.

## What each family is actually used for in the corpus

### DRL: per-slot recurring decisions

DRL dominates when the decision is **per-slot, recurring, and at deployment latency**. Twelve sources, all with similar shapes:

- Trajectory + power + offloading at every time slot (most multi-agent UAV-MEC papers).
- Per-task admission / migration / offloading decision at each task arrival ([[zhang-2025-mcma-task-migration]], [[ma-2025-pdqn-vehicular-mec]]).
- Per-slot transmit-vs-harvest scheduling ([[hsu-2025-drl-hues-hap-noma]]).
- Per-round aggregation in federated settings ([[mao-2025-bcsa-frl]]).

The unifying thread: **the same optimization problem is solved over and over** at deployment, and **fast inference matters more than provable optimality**. Train once, deploy at sub-ms latency.

### Evolutionary: mission-planning with Pareto fronts

Evolutionary dominates when the decision is **one-shot for a mission**, the objectives are **truly conflicting**, and the decision-maker wants to **see the whole front before committing**. Eight sources, all sharing this profile.

The Peng/Huang [[cmop-evolutionary-uav-mec-lineage|CMOP-evolutionary lineage]] is the largest cluster: six sources that all use [[constrained-multi-objective-evolutionary-algorithm|CMOEA]] on UAV-MEC sub-problems and refine one methodological knob per paper.

Two evolutionary entries use *metaheuristic* optimizers in distinct roles:

- [[liu-2025-haps-uav-maritime-iot]]'s **EMOMVO-CGD** (multi-verse + chaos + grey-wolf + discrete-update) solves the *whole* multi-objective problem — same role as a CMOEA, just a different population-based algorithm family.
- [[jia-2025-dro-uav-hap-mec]]'s **BWOA** is used only for the **binary subproblem** after primal decomposition (the continuous resource allocation stage uses CVX). So in this case the metaheuristic is a sub-block solver, not the whole pipeline.

### Classical: provable structure, decomposable problems

Classical methods dominate when the problem has **clean convex (or semi-convex) structure**, when **provable robustness** is required, or when an **incentive mechanism** is the answer instead of an optimization.

- Matching + convex + PGD: [[wang-2026-aerial-marine-msar]].
- AO + SDR + SCA: [[benaya-2025-aerial-isac-haps]].
- Stackelberg game equilibria: [[wang-2025-uav-swarm-stackelberg]], [[bi-2025-sg-mapg]].
- Distributionally robust + CVaR + primal decomposition: [[jia-2025-dro-uav-hap-mec]].

These are the wiki's only sources with **provable** properties (Stackelberg equilibrium existence, DRO chance-constraint satisfaction, etc.).

## Cross-family patterns

### Hybrid solvers are the norm, not the exception

The corpus is full of two-family compositions:

- **Lyapunov + DRL** ([[qin-2025-bcuav-masac]], [[zhu-2025-lycnn-drl-wpt-mec]]) — classical front-end converts long-term constraints into per-slot Lyapunov drift; DRL handles the per-slot non-convex residual.
- **Matching + DRL** ([[nabi-2025-jour-hierarchical-aerial]]) — Gale-Shapley for the discrete stage, SAC for the continuous stage.
- **DRO + metaheuristic** ([[jia-2025-dro-uav-hap-mec]]) — CVaR reformulation gives MISOCP, then BWOA handles the binary subproblem after primal decomposition.
- **CMOEA + classical channel model** ([[wu-2026-terrain-aware-uav-mec]]) — DEM-based geometric channel inside an evolutionary search.

Pure-family solvers exist (e.g. all six [[cmop-evolutionary-uav-mec-lineage|CMOP-evolutionary lineage]] entries) but the *strongest results* in the corpus tend to come from hybrid pipelines that pick the right tool per sub-block.

### [[two-stage-decomposition]] is the most portable scaffold

Discrete-then-continuous decomposition appears in every solver family:

- DRL family: [[ma-2025-pdqn-vehicular-mec]] (joint hybrid via P-DQN), [[liu-2026-jppo-en-convntm]] (joint hybrid via j-PPO), [[nabi-2025-jour-hierarchical-aerial]] (matching + SAC, *separate stages*).
- Evolutionary family: every CMOEA paper handles mixed-integer via per-type genetic operators; not exactly two-stage but conceptually similar.
- Classical family: [[wang-2026-aerial-marine-msar]] (matching + convex), [[jia-2025-dro-uav-hap-mec]] (BWOA + CVX).

The pattern works because **discrete decisions tend to dominate the structure** (which user goes where) while **continuous decisions tend to be conditionally convex** (resource allocation given the matching). Solving them in sequence loses optimality vs joint solving but gains tractability and modularity.

### Robustness only lives in the classical family — for now

Of the 26 sources, only [[jia-2025-dro-uav-hap-mec]] has a formal robustness story (DRO + CVaR). The other 25 either assume perfect CSI or implicitly rely on DRL training to handle noise.

This is a real gap. A robust DRL controller (e.g. trained with adversarial perturbations or with explicit conservative-Q methods) would be welcome in the corpus. Until then, "robust to CSI uncertainty" maps almost 1-to-1 onto "uses DRO".

## When to pick each family — operating guide

### Pick DRL when

- You will solve **the same problem class repeatedly** at deployment.
- Per-decision latency must be **sub-millisecond**.
- The reward is **scalar or scalarizable** without losing too much.
- The action space is **manageable** (≤ a few thousand discrete options, or low-dim continuous).
- Channel / mobility statistics are **stationary enough** during the deployment to match training.

### Pick evolutionary (CMOEA) when

- You have **2–3 truly conflicting objectives** that resist scalarization.
- The constraints include **non-differentiable** terms (turning angle, terrain clearance, redundancy quorums).
- The decision-maker is **post-hoc** — they pick from the front after seeing it.
- The problem is **mission-planned**, not real-time. Evolutionary search runs offline.
- Decision space is **mixed-integer + continuous** with non-trivial integer structure.

### Pick metaheuristic (BWOA, MVO) when

- You've already factored a problem and need to handle a **binary subproblem** that's small enough for swarm search but too large for branch-and-bound.
- Convex relaxation is unavailable or too lossy.
- You want a fast, no-training-required search and don't need optimality guarantees.

### Pick classical (convex / matching / Stackelberg / AO) when

- The problem has **clean convex structure** in pieces, even if non-convex overall.
- **Provable properties** matter — equilibrium existence, robustness chance constraints, optimality bounds.
- The problem decomposes naturally into **alternating blocks**, each block convex or semi-convex.
- The objective is **single-objective with scalar tradeoff weights** (most classical-MEC work is single-objective).

### Pick hybrid when

- The problem **doesn't fit cleanly into one family** (which is most of the corpus).
- You can decompose into **per-block solver choices**: classical for convex blocks, DRL for non-convex per-slot blocks, evolutionary for the front, metaheuristic for binary residuals.
- A reference: [[qin-2025-bcuav-masac]]'s Lyapunov + MASAC + DOA composition is the wiki's most-cited example of doing this well.

### Problem features → recommended family (decision aid)

The guidance above, distilled to the **discriminating problem feature** and tagged by how strongly the corpus actually backs each boundary. **Empirically-supported** means a curated source demonstrates the choice on its own problem; **inferred** means the boundary follows from family characteristics and problem shape but **no curated source runs a head-to-head** to confirm it.

| If the problem is… | Lean toward | Evidence in this corpus |
|---|---|---|
| Re-solved every slot/task at deployment, scalarizable reward, sub-ms inference needed | **DRL** | Empirically-supported *within* the family — many DRL sources deploy per-slot policies; the [[j-ppo-vs-pdqn]] head-to-head settles the on-policy-hybrid vs off-policy-hybrid sub-choice |
| One-shot mission plan, 2-3 truly conflicting objectives, decision-maker picks from the front | **Evolutionary (CMOEA)** | Empirically-supported *within* the family — the [[cmop-evolutionary-uav-mec-lineage|CMOP lineage]] benchmarks CMOEA vs CMOEA baselines, never vs DRL |
| A small binary subproblem left after decomposition, no good convex relaxation | **Metaheuristic (BWOA/MVO)** | Empirically-supported as a *sub-block* role — [[jia-2025-dro-uav-hap-mec]] (BWOA after primal decomposition), [[liu-2025-haps-uav-maritime-iot]] (EMOMVO as whole-MOP solver) |
| Clean convex/semi-convex blocks, or a provable property (equilibrium, robustness bound) is required | **Classical** (AO+SDR+SCA / Stackelberg / matching / DRO) | Empirically-supported — the only sources with provable guarantees ([[wang-2025-uav-swarm-stackelberg]], [[jia-2025-dro-uav-hap-mec]], [[benaya-2025-aerial-isac-haps]]) |
| Long-term constraints over per-slot non-convex decisions | **Hybrid: Lyapunov (classical) + DRL** | Empirically-supported — mapped across 6 sources in [[lyapunov-guided-drl]] |
| Discrete assignment + conditionally-convex continuous allocation | **Hybrid: two-stage decomposition** | Empirically-supported as a pattern (matching+SAC in [[nabi-2025-jour-hierarchical-aerial]]; matching+convex in [[wang-2026-aerial-marine-msar]]) via [[two-stage-decomposition]]; the joint-vs-staged optimality cost is **inferred**, not measured |
| Robust to CSI/channel uncertainty | **Classical (DRO+CVaR)** today | Partly inferred — only [[jia-2025-dro-uav-hap-mec]] has a formal robustness story; whether DRO beats a robustly-trained DRL policy is **unsettled** ([[query-when-does-dro-beat-drl-for-csi-uncertainty]]) |
| **DRL vs evolutionary on the *same* UAV-MEC instance** | **Undetermined by the corpus** | **Inferred only** — no source runs both families on one instance; this is the single biggest evidentiary gap (see below) |

The honest summary: the *within-family* and *sub-block-role* boundaries are empirically grounded, but the **headline DRL-vs-evolutionary boundary is inferred from problem shape, not measured**. Treat the cross-family rows as design heuristics, not validated rankings.

## What the corpus does NOT settle

### Head-to-head DRL-vs-evolutionary on the same problem

No source in the wiki runs both a DRL controller and a CMOEA on the same UAV-MEC instance. The closest is the Peng/Huang lineage, which compares CMOEA against prior CMOEA baselines but never against DRL. This is the single biggest gap in the cross-corpus story — without that comparison, the family choice is informed by problem shape but not by direct empirical evidence.

### When DRO is worth its conservatism

[[jia-2025-dro-uav-hap-mec]] reports that DRO/CVaR-reformulated solutions cost more energy than nominal solutions but maintain feasibility under realistic CSI errors. The paper's simulations validate the robustness benefit but don't pin down a precise overhead percentage that's representative across scenarios. Whether the energy tax is worthwhile depends on how often nominal solutions actually fail at deployment — a number the corpus doesn't have. A DRL-vs-DRO ablation under realistic CSI noise would clarify this dramatically.

### Evolutionary lineage scaling

Six papers from one group, all compounding. Whether the methodological stack scales — does the multi-tasking + dual-population + repair + infeasibility-utilization combination win when all four are stacked, or do they interfere? — is unstudied even within the lineage.

## Open questions

1. **A truly fair head-to-head benchmark.** A common UAV-MEC problem (multi-UAV, mixed integer, non-trivial constraints) on which all three solver families compete with matched compute budget would resolve a lot of the design uncertainty.
2. **Hybrid DRL + evolutionary.** A scheme where evolutionary search proposes Pareto-frontier candidates and a DRL policy fine-tunes each candidate at deployment time would be the natural composition. None of the 26 sources does this.
3. **Robust DRL.** Distributionally robust DRL (e.g. via conservative Q-learning, adversarial training, or risk-sensitive RL) is a live area outside the corpus. A curated source would let the robustness gap close without forcing classical-only solutions.
4. **Quantum-driven** (raised in [[wang-2025-lae-network-survey]]) — speculative future direction. No corpus entries yet, no useful guidance from the existing sources.

## See also

- [[drl-backbones-across-uav-mec-sources]] — DRL family deep dive (12 sources).
- [[cmop-evolutionary-uav-mec-lineage]] — evolutionary family deep dive (6 sources, single research group).
- [[swarm-metaheuristics-in-uav-mec]] — swarm-intelligence metaheuristic family deep dive (9+ algorithms; the "metaheuristic (BWOA/MVO)" row above maps onto its standalone-vs-embedded role split).
- [[hierarchical-aerial-mec-design-space]] — track-level synthesis where all three families overlap.
- [[two-stage-decomposition]] — the most portable cross-family scaffold.
- [[discrete-continuous-two-stage-decomposition]] — the discrete-then-continuous solver protocol that scaffold names.
- [[decomposition-beats-end-to-end-drl-in-mec]] — the thesis the hybrid/decomposition evidence supports.
- [[design-recipe-multi-uav-mec]] — DRL-track design recipe; the evolutionary equivalent would be a useful future page.
