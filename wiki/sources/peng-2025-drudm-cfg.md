---
type: source
title: "DRUDM-CFG: A Fairness-Aware Multi-Agent DRL Algorithm for AMEC-Assisted Task Offloading in Post-Disaster Scenarios"
authors: ["Xiting Peng", "Chuanqi Qin", "Xiaoyu Zhang", "Lexi Xu", "Xiaoling Zhang", "Li Jiang"]
year: 2025
url: ""
venue: ""
tags: [source, uav, mec, has, post-disaster, multi-agent, drl, fairness, theil, hierarchical]
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
  - "[[ctde-multi-agent-drl-protocol]]"
created: 2026-05-28
updated: 2026-07-16
modeling_card: required
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

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A hierarchical AMEC network has IMDs at the ground layer, multiple UAV MEC nodes, and one high-altitude airship (HAS) with larger compute and energy resources. IMDs offload to one UAV, and queued UAV tasks can be partially forwarded to the HAS.

**Problem & objective**: Maximize weighted completed-task service while minimizing total task delay and the Theil coverage-fairness index, using the reward-aligned objective $\sum_{t,u,i}o_i(t)(\xi_1S_{TQ[u,i]}(t)-\xi_2T_i^{\mathrm{total}}(t))-\xi_3TL(t)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV admission set | $\widehat{IMD^u}$ | discrete subset | IMD tasks admitted by UAV $u$ |
| HAS bandwidth share | $sp_u^h(t)$ | continuous, $[0,1]$ | Fraction of HAS bandwidth assigned to UAV $u$ |
| Partial offloading rate | $\varphi(t)$ | continuous, $[0,1]$ | Fraction of each UAV queue forwarded to HAS |
| UAV flight control | $\vartheta_u(t),\theta_u(t)$ | continuous | Speed and direction of UAV $u$ |
| DRUDM weights | $w_u^{dist},w_u^{res},w_u^{urge}$ | positive, sum to one | Distance, resource, and urgency score weights |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Admission is bounded: $\lvert\widehat{IMD^u}\rvert\le\lvert IMD^u\rvert$ |
| C2 | HAS bandwidth shares: $\sum_u sp_u^h(t)\le1$ |
| C3 | UAV speed: $0\le\vartheta_u(t)\le\vartheta_u^{\max}$ |
| C4 | UAV endurance: $\sum_tE_u^{\mathrm{total}}(t)\le E_u^{\max}$ |
| C5 | Exclusive service: $\widehat{IMD^u}\cap\widehat{IMD^{u'}}=\varnothing$ for $u\ne u'$ |
| C6 | Queue forwarding rate: $0\le\varphi(t)\le1$ |
| C7 | UAV separation: $\|UAV_u^{pos}(t)-UAV_{u'}^{pos}(t)\|\ge d^{safe}$ |

**Algorithm**: Compute a distance-resource-urgency score and admit sorted IMDs with DRUDM, prioritize UAV queues with modified EDF and forward $\lfloor\varphi(t)K_u\rfloor$ tasks to the HAS, then train a CTDE MASAC policy with CFG Theil-fairness rewards and adaptive entropy-priority replay.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Peng et al. [x] propose a hierarchical HAS-UAV AMEC model for post-disaster task offloading with joint admission, resource allocation, trajectory control, and coverage fairness. DRUDM ranks candidate IMDs by distance, available UAV resources, and task urgency, while a priority queue forwards selected UAV tasks to the HAS. The optimization maximizes completed service while reducing delay and the Theil coverage index under bandwidth, energy, assignment, speed, and separation constraints, and is solved as a CTDE multi-agent POMDP with MASAC and adaptive entropy-priority replay. Simulations report the highest task completion rate, lower average delay, faster convergence, and more balanced service of sparse regions than the compared MASAC, MADDPG, random, and UAV-only baselines.

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

(Specific percentage figures are not transcribed here — see the simulation section of the raw markdown if needed.)

## Limitations / future work

- Single HAS — paper does not analyze multi-HAS coordination.
- Weights $(w_d, w_r, w_u)$ in DRUDM are scenario-tuned, not learned.
- Theil coefficient is sensitive to how "regions" are defined; coarse partitioning may mask intra-region inequity.

## Cross-link with related sources

- Shares **multi-UAV trajectory + DRL** thread with [[liu-2026-jppo-en-convntm]] and [[qin-2025-bcuav-masac]].
- Introduces a *non-Jain* fairness metric ([[theil-fairness-index|Theil]]) that future comparisons across this wiki should consider — see [[fairness-metrics-in-mec]].
- Adds the **hierarchical aerial MEC** motif ([[hierarchical-aerial-mec]]) which [[bi-2025-sg-mapg]] (SG-MAPG) and the low-altitude-economy survey [[wang-2025-lae-network-survey]] also extend.

## Raw artifacts

- Parse: `raw/sources/DRUDM-CFG_a_Fairness-Aware_Multi-Agent_DRL_Algorithm_for_AMEC-Assisted_Task_Offloading_in_Post-Disaster_Scenarios/full.md`
- Origin PDF: `raw/sources/DRUDM-CFG_a_Fairness-Aware_Multi-Agent_DRL_Algorithm_for_AMEC-Assisted_Task_Offloading_in_Post-Disaster_Scenarios/328a810b-17dd-4c5e-913a-2dbfe1e0ea85_origin.pdf`
- Figures: `raw/sources/DRUDM-CFG_a_Fairness-Aware_Multi-Agent_DRL_Algorithm_for_AMEC-Assisted_Task_Offloading_in_Post-Disaster_Scenarios/images/`
