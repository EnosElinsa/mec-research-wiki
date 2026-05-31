---
type: source
title: "SG-MAPG: A Three-Layer Hierarchical Model for Service Fairness and Cost Optimization in UAV-Assisted MEC Systems"
authors: ["Zhihui Bi", "Fan Yang", "Zhenyu Li", "Guanqi Liu", "Zhufang Kuang"]
year: 2025
url: ""
venue: ""
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
updated: 2026-06-01
---

# SG-MAPG: A Three-Layer Hierarchical Model for Service Fairness and Cost Optimization in UAV-Assisted MEC Systems

## Citation

Bi, Z., Yang, F., Li, Z., Liu, G., & Kuang, Z. (2025). *SG-MAPG: A Three-Layer Hierarchical Model for Service Fairness and Cost Optimization in UAV-Assisted MEC Systems*.

## TL;DR

A three-tier UAV-MEC architecture — **Base Station (BS) ↔ UAV ↔ User Equipment (UE)** — modeled as a hierarchical [[stackelberg-game|Stackelberg]] game. Each tier is the leader for the tier below and the follower for the tier above. The **3L-MSADM** Markov-decision-process-meets-Stackelberg framework integrates MDPs, game theory, and auction-based task allocation; **SG-MAPG** is the multi-agent policy-gradient algorithm that approximates the Stackelberg equilibrium via policy convergence.

This is a hybridization of two patterns we've already seen: the **two-tier Stackelberg pricing** of [[wang-2025-uav-swarm-stackelberg]] and the **multi-tier hierarchical MEC** of [[peng-2025-drudm-cfg]] / [[hierarchical-aerial-mec]].

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
