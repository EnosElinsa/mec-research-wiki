---
type: source
title: "BARGAIN-MATCH: A Game Theoretical Approach for Resource Allocation and Task Offloading in Vehicular Edge Computing Networks"
authors: ["Zemin Sun", "Geng Sun", "Yanheng Liu", "Jian Wang", "Dongpu Cao"]
year: 2023
url: "https://doi.org/10.1109/TMC.2023.3239339"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicular-mec, game-theory, bargaining-game, matching-theory, task-offloading, resource-allocation]
related:
  - "[[vehicular-mec]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[bargaining-game]]"
  - "[[task-offloading]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[chen-2024-ulse-game]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
  - "[[wang-2024-twotier-satellite-marine]]"
created: 2026-05-29
updated: 2026-05-29
---

# BARGAIN-MATCH: A Game Theoretical Approach for Resource Allocation and Task Offloading in Vehicular Edge Computing Networks

## Citation

Sun, Z., Sun, G., Liu, Y., Wang, J., & Cao, D. (2023). *BARGAIN-MATCH: A Game Theoretical Approach for Resource Allocation and Task Offloading in Vehicular Edge Computing Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3239339.

## TL;DR

A hierarchical, game-theoretic scheme for joint resource allocation and task offloading in **vehicular edge computing (VEC)**. It coordinates the heterogeneity of tasks and servers across vehicle, edge, and cloud layers and formulates a joint resource-allocation-and-task-offloading problem (**JRATOP**) to maximize system utility. Since JRATOP is NP-hard, the authors propose **BARGAIN-MATCH**: a bargaining-based incentive approach for intra-server resource allocation plus a matching-based horizontal–vertical collaboration approach for inter-server offloading. The scheme is proven stable, weak Pareto optimal, and of polynomial complexity.

## Problem framing

VEC applications (autonomous driving, navigation, AR) need heavy computation at low latency, but tasks differ in space/time/requirements and servers differ in capacity. The goal is to jointly optimize intra-VEC-server resource allocation (and pricing) and inter-VEC-server load-balanced offloading by stimulating horizontal (peer) and vertical (cross-layer) collaboration among vehicles, VEC servers, and a cloud server.

## System model

- **Hierarchy.** Vehicle layer → edge (VEC servers) layer → cloud layer, coordinated by a controller; horizontal collaboration within a layer and vertical collaboration across layers (a [[three-tier-cloud-edge-end]] structure).
- **Decisions.** Resource allocation, resource pricing, and task offloading, combined into the JRATOP utility-maximization problem.

## Method

- **Intra-server resource allocation:** a [[bargaining-game|bargaining]]-based trading model (incentive mechanism) that sets resource amounts/prices.
- **Inter-server task offloading:** a [[matching-theory-for-resource-allocation|matching]]-based horizontal–vertical collaboration approach.
- **Guarantees:** BARGAIN-MATCH is proven **stable, weak Pareto optimal, and polynomial-complexity**.

## Key findings

- Simulations show superior system utility, vehicle utility, and server utility versus conventional approaches, with notable improvement in task processing rate and delay — **especially when the system workload is heavy** (the paper's headline qualitative result).

## Limitations / future work

Simulation-based; the parse emphasizes the heavy-workload regime as where gains are largest. Mobility/trajectory and learning-based extensions are natural follow-ons (cf. the DRL approach in [[ma-2025-pdqn-vehicular-mec]]).

## Relation to the corpus

A **game-theoretic VEC** entry that complements the DRL-based vehicular work [[ma-2025-pdqn-vehicular-mec]] and the migration-based [[zhang-2025-mcma-task-migration]]. Its bargaining+matching hybrid parallels the Stackelberg+bargaining structure of [[wang-2024-twotier-satellite-marine]] and the matching machinery in [[jia-2022-hierarchical-aerial-matching]]; it sits alongside [[chen-2024-ulse-game]] in the broader game-theoretic offloading thread. Shares co-authors Zemin Sun / Geng Sun with [[sun-2024-mvtora-postdisaster-vfc]].

## Raw artifacts

- `raw/sources/BARGAIN-MATCH_A_Game_Theoretical_Approach_for_Resource_Allocation_and_Task_Offloading_in_Vehicular_Edge_Computing_Networks/full.md`
- Original PDF and extracted figures in the same folder.
