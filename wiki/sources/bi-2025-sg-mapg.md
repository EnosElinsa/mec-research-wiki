---
type: source
title: "SG-MAPG: A Three-Layer Hierarchical Model for Service Fairness and Cost Optimization in UAV-Assisted MEC Systems"
authors: ["Zhihui Bi", "Fan Yang", "Zhenyu Li", "Guanqi Liu", "Zhufang Kuang"]
year: 2025
url: ""
venue: ""
modeling_card: required
tags: [source, uav, mec, stackelberg, multi-agent, drl, fairness, hierarchical, auction]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[stackelberg-game]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
created: 2026-05-28
updated: 2026-07-16
---

# SG-MAPG: A Three-Layer Hierarchical Model for Service Fairness and Cost Optimization in UAV-Assisted MEC Systems

## Citation

Bi, Z., Yang, F., Li, Z., Liu, G., & Kuang, Z. (2025). *SG-MAPG: A Three-Layer Hierarchical Model for Service Fairness and Cost Optimization in UAV-Assisted MEC Systems*.

## TL;DR

A three-tier UAV-MEC architecture — **Base Station (BS) ↔ UAV ↔ User Equipment (UE)** — modeled as a hierarchical [[stackelberg-game|Stackelberg]] game. Each tier is the leader for the tier below and the follower for the tier above. The **3L-MSADM** Markov-decision-process-meets-Stackelberg framework integrates MDPs, game theory, and auction-based task allocation; **SG-MAPG** is the multi-agent policy-gradient algorithm that approximates the Stackelberg equilibrium via policy convergence.

This is a hybridization of two patterns we've already seen: the **two-tier Stackelberg pricing** of [[wang-2025-uav-swarm-stackelberg]] and the **multi-tier hierarchical MEC** of [[peng-2025-drudm-cfg]] / [[hierarchical-aerial-mec]].

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: In each time slot, $N$ UEs with no local execution capability send delay-sensitive tasks through $M$ fixed-altitude UAVs and $K$ MEC-equipped base stations. Tasks may be computed at a UAV, sent directly to a BS, or split so a UAV computes one fraction and relays the rest, while the hierarchy assigns BSs, UAVs, and UEs leader, sub-leader, and follower roles.

**Problem & objective**: Problem (46) maximizes service fairness per unit system cost, $\max_{W,Z}f_{ue}(t)/V_{\mathrm{true}}(t)$, where $V_{\mathrm{true}}(t)$ is the minimum weighted energy-and-delay cost selected across BS and UAV execution routes.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Task allocation ratio | $\nu_{m,k}(t)$ | Continuous, $[0,1]$ | Fraction of a UAV-handled task forwarded from UAV $m$ to BS $k$ |
| UAV flight angle | $\varphi_m(t)$ | Continuous, $[0,2\pi]$ | Horizontal movement direction of UAV $m$ |
| Price influence | $q$ | Continuous, $[0,1]$ | Coupling between BS computing prices and UAV prices |
| UE service selection | $A_n(t)$ | Binary, $\{0,1\}$ | Whether UE $n$ is served in slot $t$; the actor selects the corresponding $z_n(t)$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 46b | Task split, $0\leq\nu_{m,k}(t)\leq1$ |
| 46c | Flight direction, $0\leq\varphi_m(t)\leq2\pi$ |
| 46d | Price coupling, $0\leq q\leq1$ |
| 46e | Flight region, $0\leq x_m(t)\leq L$ and $0\leq y_m(t)\leq L$ |
| Reward feasibility | Collision, boundary, and UE-service violations incur $P_m^{\mathrm{col}}$, $P_m^{\mathrm{range}}$, and $P_m^{\mathrm{ue}}$ penalties in (52) |

**Algorithm**: The 3L-MSADM procedure computes BS prices, UAV computation and relay prices, the continuous split $\nu_{m,k}(t)$, and the lowest-cost execution route. SG-MAPG then learns $z_n(t)$, $\varphi_m(t)$, resource size, and $q$ under CTDE using one online actor, two target actors, three online critics, three target critics, replay sampling, conservative minimum target values, policy gradients, and soft target updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Bi et al. [x] studied fairness-aware task offloading and resource allocation in a three-tier MEC system comprising base stations, UAVs, and user equipment. Their model allows tasks to execute at UAVs, execute directly at base stations, or split between UAV processing and UAV-to-BS relaying through a continuous allocation ratio. They formulated a hierarchical Stackelberg problem that maximizes UE service fairness divided by a weighted energy-and-delay system cost over task splitting, UAV flight angles, cross-layer pricing, and UE selection. The 3L-MSADM procedure combines hierarchical pricing and route selection, while SG-MAPG approximates the coupled equilibrium under centralized training and decentralized execution with dual target actors and triple critics. Simulations reported 12.3% higher long-term fairness and 22.7% lower system cost than the random baseline in the two-UAV comparisons, with larger gains reported in additional three-UAV and mobile-UE settings.

## Problem framing

Three coupled decision layers:

| Layer | Role | Decisions |
|---|---|---|
| BS | Top leader | Pricing for UAV resources; coordination signals |
| UAV | Middle (leader to UE, follower to BS) | Trajectory; offload-acceptance; pricing for UE service |
| UE | Bottom follower | Task admission to UAV vs local execution |

Objectives jointly handled:

- Latency
- Energy (per UAV and per UE)
- Service fairness across UEs (especially in sparsely-covered regions)

## Method

- **Static-equilibrium-Stackelberg** would be too brittle for dynamic UAV-MEC. Instead, the paper trains **multi-agent policy gradient (MAPG)** agents whose convergence point approximates the Stackelberg equilibrium of the underlying game.
- This composes a *cooperative* element (multi-UAV coordination at the same tier) with a *competitive* element (across-tier pricing/offloading interactions).
- Auction-based task allocation handles the UE-to-UAV assignment side, similar in spirit to the matching layer in [[wang-2025-uav-swarm-stackelberg]].

## Findings

- Outperforms baselines on combined fairness × cost × latency metric.
- Adaptive pricing (vs static) significantly cuts the worst-case UE wait time in sparsely-covered regions.
- The Stackelberg–MARL hybrid converges to near-equilibrium without solving the game analytically — a useful pattern for high-dimensional dynamic problems.

## Limitations / future work

- Three layers but flat geometry — no HAPS or LEO tier.
- Auction is per-round; more sophisticated combinatorial auctions are deferred.
- The convergence-to-equilibrium claim is empirical, not analytically certified.

## Cross-link with related sources

- Generalizes [[wang-2025-uav-swarm-stackelberg]]'s two-tier Stackelberg to three tiers and adds the compute layer.
- Adjacent to [[peng-2025-drudm-cfg]] in the **hierarchical-aerial-MEC** thread, but uses Stackelberg for coordination instead of central admission rules.
- The **multi-agent-policy-gradient as Stackelberg solver** trick is interesting on its own — worth a synthesis page once a third paper uses it.

## Raw artifacts

- `raw/sources/SG-MAPG_A_Three-Layer_Hierarchical_Model_for_Service_Fairness_and_Cost_Optimization_in_UAV-Assisted_MEC_Systems/full.md`
