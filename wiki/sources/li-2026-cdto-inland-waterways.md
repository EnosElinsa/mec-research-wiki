---
type: source
title: "Distributed Game-Based Joint Task Offloading Over UAV-Assisted Inland Waterways Edge Networks"
authors: ["Baiyi Li", "Jian Zhao", "Nan Li", "Xinghan Wang", "Tingting Yang"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3683451"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
modeling_card: required
tags: [source, inland-waterways, maritime-mec, uav-assisted-mec, device-to-device-communication, potential-game, graph-neural-network, multi-agent-rl, task-offloading]
related:
  - "[[maritime-mec]]"
  - "[[device-to-device-communication]]"
  - "[[potential-game]]"
  - "[[graph-neural-network]]"
  - "[[task-offloading]]"
  - "[[vehicular-mec]]"
created: 2026-07-06
updated: 2026-07-16
---

# Distributed Game-Based Joint Task Offloading Over UAV-Assisted Inland Waterways Edge Networks

## Citation

Li, B., Zhao, J., Li, N., Wang, X., & Yang, T. (2026). *Distributed Game-Based Joint Task Offloading Over UAV-Assisted Inland Waterways Edge Networks*. **IEEE Transactions on Intelligent Transportation Systems**, 27(6), 6970-6983. DOI: 10.1109/TITS.2026.3683451.

## TL;DR

Introduces **cluster-based distributed task offloading (CDTO)** for UAV-assisted inland-waterway edge networks. Autonomous surface vessels or USVs with heavy tasks form clusters with nearby assisting vessels; UAVs serve as cluster heads and adjust positions to cover the selected D2D offloading links. The task-offloading decision is modeled as an exact potential game and solved with a multi-agent graph reinforcement-learning design that uses D2D topology as graph structure.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Computationally intensive USVs split safety-critical perception tasks across nearby assisting USVs through time-varying D2D links. One UAV cluster head per intensive client relays global tasks to and from a terrestrial base station and moves to the projected cluster barycenter inside the admissible inland-waterway flight region.

**Problem & objective**: CDTO minimizes $T=\sum_{l=1}^{L}T_l$, the sum of end-to-end decision latency across all USV clusters, by coordinating clustering, sequential task splitting, and TBS-to-UAV bandwidth allocation.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| AC-cluster association | $s_{l,h}$ | binary | Whether assisting client $h$ joins cluster $l$ |
| Task split selection | $k_{l,m}$ | binary | Whether layer $m$ terminates a subtask assigned within cluster $l$ |
| Cluster strategy | $\mathbf s_l$ | discrete path strategy | Ordered D2D offloading links selected for cluster $l$ |
| TBS bandwidth share | $B_l$ | continuous, positive | Downlink or uplink bandwidth allocated to UAV cluster head $l$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each assisting USV joins at most one cluster: $\sum_ls_{l,h}\leq1$ |
| C2 | The task begins at its computationally intensive client and each selected cluster member holds at most one sequential subtask |
| C3 | TBS bandwidth is fully allocated: $\sum_lB_l=B$ |
| C4 | Selected D2D links must form a connected offloading chain under the current topology and rates |
| C5 | UAV cluster-head positions remain inside the admissible flight region after barycenter projection |
| C6 | Uplink bandwidth respects the total budget, per-cluster bounds, and UAV transmission-energy limit |

**Algorithm**: CDTO uses a task-relevant GNN to encode dynamic D2D topology and a shared multi-agent policy inside an exact potential game to select cluster links. Given those links, a greedy heuristic assigns task layers in proportion to USV computing capacity, closed-form convex updates allocate downlink bandwidth, and a one-dimensional search allocates uplink bandwidth.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] proposed cluster-based distributed task offloading for safety-critical perception in UAV-assisted inland-waterway edge networks. Their formulation minimizes aggregate decision latency over D2D cluster associations, sequential task splits, and TBS bandwidth under exclusivity, connectivity, computation, communication, and energy limits. CDTO combines a task-relevant graph neural network and exact-potential-game multi-agent learning with greedy task allocation and convex bandwidth updates. Simulations reported convergence after about 50 iterations, up to 28.6% lower safety-critical decision latency, and the only tested global mechanism that stayed within the prescribed latency threshold as the number of intensive clients increased.

## Problem

Autonomous inland-waterway transportation needs fast perception and decision making, but safety-critical tasks can exceed a single vessel's onboard compute budget. Centralized task offloading is fragile under link failures and mobility, while local-only or UAV-only baselines cannot always keep latency within the required threshold. The paper targets a distributed mechanism that can recompute offloading links quickly as vessels move or links fail.

## System model

- **Clients.** Computationally intensive clients (CCs) request offloading support, and assisting clients (ACs) provide spare computation over D2D links.
- **UAV support.** UAVs act as cluster heads, with the number of UAV cluster heads matching the number of CC-centered clusters in the modeled setting.
- **Network.** USVs move along predefined inland-waterway lanes. Nearby vessels can form D2D links, and UAV cluster-head locations are adjusted after offloading links are selected.

## Method

CDTO combines an exact-potential-game formulation with multi-agent graph reinforcement learning. The topology-aware reinforcement learner uses a task-relevant graph neural network centered on D2D links, so the shared policy can generate offloading-link decisions from the USV topology. After offloading links are determined, UAV cluster heads move to cover the selected communication links; task allocation and bandwidth allocation are then handled with heuristic and convex-optimization subroutines.

## Key findings

- The abstract reports safety-critical decision-latency reductions up to **28.6%** compared with traditional offloading.
- The learning process converges after about **50 iterations** in the reported varying-CC experiments.
- CDTO is reported as the only compared global mechanism that keeps safety-critical perception tasks within the latency threshold as the number of CCs increases.
- Under transient D2D link failures, the paper reports millisecond-level recomputation for intra-cluster D2D links and better response than a traditional exact-potential-game linear-programming baseline.
- Deadline satisfaction decreases as CC count rises, from roughly 97% to roughly 81% when CCs increase from 2 to 6, and improves as AC count increases.

## Limitations / future work

The paper reports increasing latency as the number of CCs grows. Future work includes using digital twins for QoS management in high-density CC regions, optimizing UAV energy and trajectory tracking, and improving trustworthy D2D computation offloading.

## Relation to the corpus

This is a bridge between [[maritime-mec]] and ITS-oriented [[vehicular-mec]]: the mobile nodes are inland-waterway vessels rather than road vehicles, while the solver stack uses familiar MEC building blocks - [[device-to-device-communication]], [[potential-game]], [[graph-neural-network]], and distributed task offloading. It also extends the maritime track beyond sea/ship coverage and SAR scenarios into inland waterway autonomy.

## Raw artifacts

- `raw/sources/Distributed_Game-Based_Joint_Task_Offloading_Over_UAV-Assisted_Inland_Waterways_Edge_Networks/Distributed_Game-Based_Joint_Task_Offloading_Over_UAV-Assisted_Inland_Waterways_Edge_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
