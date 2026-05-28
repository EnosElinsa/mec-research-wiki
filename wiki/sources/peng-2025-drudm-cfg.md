---
type: source
title: "DRUDM-CFG: A Fairness-Aware Multi-Agent DRL Algorithm for AMEC-Assisted Task Offloading in Post-Disaster Scenarios"
authors: ["Xiting Peng", "Chuanqi Qin", "Xiaoyu Zhang", "Lexi Xu", "Xiaoling Zhang", "Li Jiang"]
year: 2025
url: ""
venue: ""
tags: [uav, mec, has, post-disaster, multi-agent, drl, fairness, theil, hierarchical]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[high-altitude-platform-station]]"
  - "[[post-disaster-mec]]"
  - "[[theil-fairness-index]]"
  - "[[adaptive-entropy-priority-replay]]"
  - "[[masac]]"
  - "[[ma-pomdp]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[qin-2025-bcuav-masac]]"
created: 2026-05-28
updated: 2026-05-28
---

# DRUDM-CFG: A Fairness-Aware Multi-Agent DRL Algorithm for AMEC-Assisted Task Offloading in Post-Disaster Scenarios

## Citation

Peng, X., Qin, C., Zhang, X., Xu, L., Zhang, X., & Jiang, L. (2025). *DRUDM-CFG: A Fairness-Aware Multi-Agent DRL Algorithm for AMEC-Assisted Task Offloading in Post-Disaster Scenarios*.

## TL;DR

A two-tier aerial MEC architecture for [[post-disaster-mec|post-disaster scenarios]]: low-altitude UAVs cover dense pockets of intelligent mobile devices (IMDs); a single **High-Altitude Airship (HAS)** sits above as an umbrella relay with much larger compute and energy. IMDs offload to UAVs; UAVs offload large/non-urgent jobs further up to the HAS via a priority queue.

The algorithm — **DRUDM-CFG** — has three pieces:

1. **DRUDM** (Distance–Resource–Urgency Decision Mechanism) — a weighted-sorting rule UAVs use to pick *which* IMDs to admit per slot, balancing geographic distance, free UAV CPU, and per-task urgency.
2. **CFG** (Coverage Fairness Guarantee) — a [[theil-fairness-index|Theil-coefficient]]-based fairness regularizer baked into the RL reward to prevent UAVs from camping over dense pockets and starving IMDs in sparse regions.
3. **MA-DRL training** with [[adaptive-entropy-priority-replay|adaptive entropy-priority experience replay]] (AEP) for faster convergence in the multi-agent post-disaster MA-POMDP.

Outperforms baselines on task completion rate and average delay; CFG specifically improves service for sparse-area IMDs.

## Problem framing

Post-disaster ground infrastructure is degraded; communications are unreliable; some areas have IMD clusters (refugee camps, rescue teams) and some are sparse (search teams in collapsed zones). Direct IMD→HAS offloading suffers from long, unstable links — hence the relay layer.

Decision variables per slot:

- **Hybrid TO:** which IMD-task each UAV admits, and which UAV-queued tasks are forwarded to the HAS.
- **Resource allocation:** per-UAV CPU split among admitted IMDs.
- **UAV trajectories:** continuous control to balance coverage of dense and sparse regions.

Cast as an **MA-POMDP** — each UAV is a partial-observation agent.

## Method (Section 4)

### DRUDM admission rule

For each candidate IMD, score = $w_d \cdot \text{distance} + w_r \cdot \text{free-CPU} + w_u \cdot \text{urgency}$, with weights tuned per scenario. UAVs sort their candidate pool and admit top-$k$ until capacity. Avoids the failure mode of pure distance-based admission ([27] in their related work) where critical-deadline IMDs get rejected because a closer non-urgent task arrived first.

### CFG fairness regularizer

The fairness term is the Theil coefficient $\bar{TL}(t)$ over per-region service counts. Lower Theil = more equal distribution. CFG enters the RL reward as $-\beta \bar{TL}(t)$, pulling UAV policies toward sparse regions even when they're individually less efficient targets. Plays a role similar to the [[spatial-equity-index|Jain-style fairness $f_n$]] in [[liu-2026-jppo-en-convntm]] but uses Theil instead — Theil decomposes nicely across population subgroups, which matters when sparse and dense regions need different treatment.

### Adaptive Entropy-Priority (AEP) replay

A custom prioritized replay variant that scores transitions by a combination of TD-error magnitude and policy entropy in the source state, biasing replay toward high-information samples. Reported to accelerate convergence and reduce variance in multi-UAV post-disaster training.

## Findings

- **Task completion rate** — DRUDM-CFG > MADDPG / SAC / random-admission baselines.
- **Average delay** — lowered by the urgency-weighted admission (DRUDM) and the UAV→HAS overflow path.
- **Sparse-region service** — explicitly improves under CFG; without CFG, UAVs concentrate on dense pockets.

(Specific percentage figures not pulled from the paper for this curation pass — see the simulation section of the raw markdown if needed.)

## Limitations / future work

- Single HAS — paper does not analyze multi-HAS coordination.
- Weights $(w_d, w_r, w_u)$ in DRUDM are scenario-tuned, not learned.
- Theil coefficient is sensitive to how "regions" are defined; coarse partitioning may mask intra-region inequity.

## Cross-link with related sources

- Shares **multi-UAV trajectory + DRL** thread with [[liu-2026-jppo-en-convntm]] and [[qin-2025-bcuav-masac]].
- Introduces a *non-Jain* fairness metric ([[theil-fairness-index|Theil]]) that future comparisons across this wiki should consider — see [[fairness-metrics-in-mec]] when that page exists.
- Adds the **hierarchical aerial MEC** motif ([[hierarchical-aerial-mec]]) which paper #8 (SG-MAPG) and the low-altitude-economy paper will probably extend.

## Raw artifacts

- `raw/sources/DRUDM-CFG_a_Fairness-Aware_Multi-Agent_DRL_Algorithm_for_AMEC-Assisted_Task_Offloading_in_Post-Disaster_Scenarios/full.md`
