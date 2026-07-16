---
type: source
title: "Game-Based Multi-UAV Dynamic Collaborative With Energy-Efficient Hierarchical Information Sharing for Mobile Crowdsensing"
authors: ["Xiaoliang Guang", "Yuhuai Peng", "Chenlu Wang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3621440"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, mobile-crowdsensing, dynamic-uav-clustering, hierarchical-information-sharing, cooperative-game, shapley-value, energy-balancing]
related:
  - "[[uav-assisted-mobile-crowd-sensing]]"
  - "[[dynamic-uav-clustering]]"
  - "[[hierarchical-uav-swarm]]"
  - "[[first-order-radio-energy-model]]"
  - "[[energy-balancing-uav]]"
  - "[[heterogeneous-uav-fleet]]"
created: 2026-07-13
updated: 2026-07-16
modeling_card: required
---

# Game-Based Multi-UAV Dynamic Collaborative With Energy-Efficient Hierarchical Information Sharing for Mobile Crowdsensing

## Citation

Guang, X., Peng, Y., & Wang, C. (2026). *Game-Based Multi-UAV Dynamic Collaborative With Energy-Efficient Hierarchical Information Sharing for Mobile Crowdsensing*. **IEEE Transactions on Mobile Computing**, 25(3), 3728-3743. DOI: 10.1109/TMC.2025.3621440.

## TL;DR

HISWTA dynamically clusters heterogeneous sensing UAVs, routes information among cluster heads, self-heals weak heads, and allocates sensing tasks by approximate Shapley value. The goal is to reduce relay/task energy imbalance so more UAVs remain available across successive mobile-crowdsensing cycles.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A heterogeneous UAV swarm repeatedly performs mobile crowdsensing while forming energy-aware clusters, sharing information through cluster heads, and allocating sensing work.

**Problem & objective**: Allocate sensing work and the information hierarchy to maximize completed task volume, $\max \sum_{k\in K}\sum_i T_{i,k}^{c}$, while limiting execution, communication, and connectivity costs.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Completed task volume | $T_{i,k}^{c}$ | nonnegative continuous | Work completed by UAV $i$ in cycle or task class $k$ |
| Allocated task volume | $T_{i,k}^{a}$ | nonnegative continuous | Work assigned to UAV $i$ before execution |
| Cluster partition | $\mathcal{C}$ | discrete partition | Membership of UAVs and selected cluster heads |
| Inter-head route | $\pi$ | permutation | Order for information sharing among cluster heads |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Completed work cannot exceed allocated work, $T_{i,k}^{c}\leq T_{i,k}^{a}$ |
| C2 | Task execution energy for each UAV stays within its residual budget |
| C3 | Intra-cluster and inter-head links satisfy communication-range and connectivity conditions |
| C4 | Cluster formation and route choices remain feasible for the available heterogeneous UAVs |

**Algorithm**: Estimate an energy-aware cluster count, select heads with multiplicative energy, distance, and connectivity criteria, solve inter-head sharing with greedy initialization plus Tabu Search and simulated-annealing amnesty, replace weak heads with fuzzy logic, and allocate tasks with Monte Carlo Shapley values.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Guang et al. [x] developed HISWTA for repeated mobile-crowdsensing missions performed by heterogeneous UAV swarms. Their formulation maximizes completed task volume under per-UAV execution and communication energy limits, while dynamic clustering, inter-head routing, and task allocation balance depletion across cycles. The method combines energy-aware cluster-head selection, improved tabu search for inter-cluster sharing, fuzzy head replacement, and Monte Carlo Shapley-value allocation. At critical task loads, simulations report task-completion-ratio improvements of 12%, 26%, and 10% for swarms of 5, 10, and 15 UAVs, with 100% completion and energy-consumption disparities of 0.89% and 0.64% in the reported 10- and 15-UAV ablations.

## Problem framing

As a sensing swarm grows, inter-UAV traffic can drain relay nodes while uneven tasks exhaust heavily loaded aircraft. Static clustering and centralized allocation adapt poorly when tasks, links, positions, and available UAVs change. The paper therefore couples communication hierarchy with cooperative-game task allocation.

## System model

- Heterogeneous UAVs differ in energy, communication/sensing ranges, and computational power and move by Random WayPoint mobility.
- Cluster members send data to heads, which fuse/synchronize data and exchange information with other heads.
- Communication follows the [[first-order-radio-energy-model]] with `d^2`/`d^4` transmit regimes; task energy is linear in completed task volume.
- Re-clustering and head selection use residual energy, consumption ratio, position, connectivity, and communication quality after each task cycle.
- The modeled energy omits propulsion/hover terms even though later discussion invokes movement cost.

## Method

Theorem 1 gives a cluster-count expression under equal cluster sizes. A multiplicative energy/distance/connectivity priority chooses heads. Inter-head sharing is posed as a time-windowed Hamiltonian/TSP-like problem and addressed with greedy initialization, inverse/2-opt Tabu Search, a dynamic tabu length, and simulated-annealing-style amnesty. Fuzzy packet-loss/delay logic triggers head replacement.

Task allocation defines a cooperative-game value from threat and residual energy. Monte Carlo sampling estimates Shapley marginal contributions with variance/budget stopping; unavailable-UAV value is incrementally redistributed from the previous cycle. Current task volume is assigned proportionally to the resulting values.

## Key findings

- At task-critical thresholds, the paper reports maximum task-completion-ratio gains of `12%`, `26%`, and `10%` for 5, 10, and 15 UAVs.
- In the detailed 10-UAV ablation, HISWTA reports `100%` TCR, synergy 10, and `0.89%` energy-consumption difference versus lower synergy and larger disparity for two ablations.
- In the 15-UAV setting it reports `100%` TCR, synergy 15, and `0.64%` disparity.
- Robustness sweeps vary communication radius, LoS/NLoS fading, obstacle ratio, task density, and task dispersion, but most plotted margins are not stated numerically.

## Limitations / parse caveats

Validation is custom simulation only, with no named software, hardware, dataset, code, runtime, or deployment. The routing equation contains a self-loop/closure inconsistency, Algorithm 1 omits the named Tabu procedure, fuzzy inputs/output and ranges conflict, and the energy-priority denominator can become negative under ordinary depletion. Core/kernel/Shapley terminology and proofs are not fully reconciled; incremental Shapley reuse assumes stable value structure. ECR and `Delta ECR` definitions do not cleanly match later communication-energy explanations.

## Relation to the corpus

HISWTA extends [[dynamic-uav-clustering]] and [[hierarchical-uav-swarm]] from load/service hierarchy to sensing-information relays, and extends [[energy-balancing-uav]] from an objective to a cluster/routing/task-allocation pipeline. Its UAVs are the sensing participants themselves, broadening the human-participant emphasis of [[uav-assisted-mobile-crowd-sensing]].

## Raw artifacts

- Parse: `raw/sources/Game-Based_Multi-UAV_Dynamic_Collaborative_With_Energy-Efficient_Hierarchical_Information_Sharing_for_Mobile_Crowdsensing/Game-Based_Multi-UAV_Dynamic_Collaborative_With_Energy-Efficient_Hierarchical_Information_Sharing_for_Mobile_Crowdsensing.md`
- Origin PDF: `raw/sources/Game-Based_Multi-UAV_Dynamic_Collaborative_With_Energy-Efficient_Hierarchical_Information_Sharing_for_Mobile_Crowdsensing/Game-Based_Multi-UAV_Dynamic_Collaborative_With_Energy-Efficient_Hierarchical_Information_Sharing_for_Mobile_Crowdsensing.pdf`
- Figures: `raw/sources/Game-Based_Multi-UAV_Dynamic_Collaborative_With_Energy-Efficient_Hierarchical_Information_Sharing_for_Mobile_Crowdsensing/images/`
