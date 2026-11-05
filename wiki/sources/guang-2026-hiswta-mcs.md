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
updated: 2026-11-03
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

**Problem & objective**: P1 (4) maximizes completed task volume, $\max\sum_{k\in K}\sum_{i=1}^{M_k}T_{i,k}^c$, under allocation and per-UAV energy limits; inter-head sharing is the routing problem P2 (14) minimizing $\sum_{i,j}d_{ij}x_{ij}$, and task allocation is the cooperative game P3 (24).

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Completed task volume | $T_{i,k}^{c}$ | nonnegative continuous | Work completed by UAV $i$ in cycle or task class $k$ |
| Allocated task volume | $T_{i,k}^{a}$ | nonnegative continuous | Work assigned to UAV $i$ before execution |
| Cluster partition | $\mathcal{C}$ | discrete partition | Membership of UAVs and selected cluster heads |
| Inter-head route | $x_{ij}$ | binary, $\{0,1\}$ | Order for information sharing among cluster heads |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| (4b) | Completed work cannot exceed allocated work: $T_{i,k}^c\le T_{i,k}^a$ |
| (4c) | Task-execution energy within residual energy: $0\le T_{i,k}^c E_c\le E_i$ |
| (4d) | Communication energy within residual energy: $0\le E_{com,i}\le E_i$ |
| (14b)–(14g) | Inter-head sharing route P2: each head entered and left once, time windows $t_i^{\min}\le t_i\le t_i^{\max}$, MTZ subtour elimination $u_i-u_j+nx_{ij}\le n-1$, $x_{ij}\in\{0,1\}$ |
| (24b)–(24d) | Task allocation game P3: weights $\eta+\mu=1$, cluster workload $\sum_iT_{i,k}^c\le T_k$, $E_{i,k}\ge0$ |

**Algorithm**: Estimate an energy-aware cluster count, select heads with multiplicative energy, distance, and connectivity criteria, solve inter-head sharing with greedy initialization plus Tabu Search and simulated-annealing amnesty, replace weak heads with fuzzy logic, and allocate tasks with Monte Carlo Shapley values.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Guang et al. [x] developed HISWTA for repeated mobile-crowdsensing missions performed by heterogeneous UAV swarms. Their formulation maximizes completed task volume under per-UAV execution and communication energy limits, while dynamic clustering, inter-head routing, and task allocation balance depletion across cycles. The method combines energy-aware cluster-head selection, improved tabu search for inter-cluster sharing, fuzzy head replacement, and Monte Carlo Shapley-value allocation. At critical task loads, simulations report task-completion-ratio improvements of 12%, 26%, and 10% for swarms of 5, 10, and 15 UAVs, and in ablations against two-by-two sharing (TBT+TA) and PSO allocation (HIS+PSOTA) the full method reaches 100% completion with energy-consumption-ratio differences of 0.89% and 0.64% for 10 and 15 UAVs.

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
