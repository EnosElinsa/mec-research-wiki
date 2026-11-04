---
type: source
modeling_card: required
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
updated: 2026-11-03
---

# BARGAIN-MATCH: A Game Theoretical Approach for Resource Allocation and Task Offloading in Vehicular Edge Computing Networks

## Citation

Sun, Z., Sun, G., Liu, Y., Wang, J., & Cao, D. (2023). *BARGAIN-MATCH: A Game Theoretical Approach for Resource Allocation and Task Offloading in Vehicular Edge Computing Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3239339.

## TL;DR

A hierarchical, game-theoretic scheme for joint resource allocation and task offloading in **vehicular edge computing (VEC)**. It coordinates the heterogeneity of tasks and servers across vehicle, edge, and cloud layers and formulates a joint resource-allocation-and-task-offloading problem (**JRATOP**) to maximize system utility. Since JRATOP is NP-hard, the authors propose **BARGAIN-MATCH**: a bargaining-based incentive approach for intra-server resource allocation plus a matching-based horizontal–vertical collaboration approach for inter-server offloading. The scheme is proven stable, weak Pareto optimal, and of polynomial complexity.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A three-tier vehicular edge network contains vehicles, VEC servers, and a cloud, with both horizontal peer collaboration and vertical cross-layer offloading. Vehicles move between server coverage areas, so offloading must finish within sojourn times, and servers sell computation resources at a price.

**Problem & objective**: JRATOP, problem P (23), is NP-hard and maximizes social welfare over the horizon, $\max_{S_t,S_c}\sum_tSW(t)$, where $SW(t)$ (22) adds vehicle utilities $U_i^a(t)$ and server utilities $U_j^i(t)$; $S_t$ is the offloading strategy and $S_c$ the resource allocation and pricing strategy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading strategy | $s_i^a(t)\in S_t$ | binary | Vehicle $i$ executes locally ($a=0$), at an edge server, or at the cloud |
| Computation allocation | $f_{j,i}(t)$ in $S_c$ | continuous, bounded by $f_j^{\max}$ | CPU frequency that server $j$ gives vehicle $i$ |
| Resource price | $c_{j,i}(t)$ in $S_c$ | continuous, nonnegative | Unit price server $j$ charges vehicle $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C2 | Offloading indicators are binary and each vehicle selects at most one destination |
| C3 | Task-generation indicator $p_i^{\mathrm{gen}}(t)\in\{0,1\}$ |
| C4 | Completion time is within $T_i^{\max}(t)$ |
| C5-C6 | Transmission and server-handover times fit within the vehicle's sojourn time in the current and arrival coverage |
| C7 | Vehicle speed lies in $[v^{\min},v^{\max}]$ |
| C8-C9 | Server CPU capacity $f_j^{\max}$ and core count $N_j^{\mathrm{core}}$ are not exceeded |
| C10-C11 | Vehicle local energy and server energy stay within their limits |
| C12 | A vehicle's payment stays within its budget $C_i^{\max}$ |

**Algorithm**: Solve intra-server trading with a bargaining game to obtain closed-form prices and CPU allocations → construct horizontal and vertical preference lists → run matching for inter-server offloading → iterate until a stable, weakly Pareto-optimal allocation is obtained.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Sun et al. [x] studied joint resource allocation and task offloading in a three-tier vehicular edge-computing network. They formulated JRATOP to maximize social welfare, the sum of vehicle and server utilities, over intra-server resource amounts and prices and inter-server horizontal and vertical offloading matches. BARGAIN-MATCH uses a bargaining game for intra-server trading and a matching-based collaboration procedure for inter-server offloading. The paper proves stability, weak Pareto optimality, and polynomial complexity of the resulting scheme. Simulations report higher system, vehicle, and server utilities and improved task-processing rate and delay than the conventional approaches, especially under heavy workloads.

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

- `raw/sources/BARGAIN-MATCH_A_Game_Theoretical_Approach_for_Resource_Allocation_and_Task_Offloading_in_Vehicular_Edge_Computing_Networks/BARGAIN-MATCH_A_Game_Theoretical_Approach_for_Resource_Allocation_and_Task_Offloading_in_Vehicular_Edge_Computing_Networks.md`
- Original PDF and extracted figures in the same folder.
