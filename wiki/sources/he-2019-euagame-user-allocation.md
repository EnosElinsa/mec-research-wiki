---
type: source
title: "A Game-Theoretical Approach for User Allocation in Edge Computing Environment"
authors: ["Qiang He", "Guangming Cui", "Xuyun Zhang", "Feifei Chen", "Shuiguang Deng", "Hai Jin", "Yanhui Li", "Yun Yang"]
year: 2019
url: "https://doi.org/10.1109/TPDS.2019.2938944"
venue: "IEEE Transactions on Parallel and Distributed Systems (IEEE TPDS)"
tags: [source, edge-user-allocation, game-theory, potential-game, nash-equilibrium, edge-computing]
related:
  - "[[edge-user-allocation]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[mobile-edge-computing]]"
  - "[[chen-2024-ulse-game]]"
  - "[[sun-2023-bargain-match-vec]]"
created: 2026-05-29
updated: 2026-05-29
---

# A Game-Theoretical Approach for User Allocation in Edge Computing Environment

## Citation

He, Q., Cui, G., Zhang, X., Chen, F., Deng, S., Jin, H., Li, Y., & Yang, Y. (2019). *A Game-Theoretical Approach for User Allocation in Edge Computing Environment*. **IEEE Transactions on Parallel and Distributed Systems**. DOI: 10.1109/TPDS.2019.2938944.

## TL;DR

Frames the **edge user allocation (EUA)** problem from an app vendor's perspective: allocate the maximum number of app users to hired edge servers while minimizing overall system cost, subject to proximity (coverage) and multi-dimensional capacity constraints. The authors prove EUA is a variable-size vector bin-packing problem (NP-hard), then model it as **EUAGame**, a [[potential-game]] that provably admits a [[nash-equilibrium]], and propose a decentralized algorithm that converges to an NE.

This is one of the foundational, frequently-cited game-theoretic treatments of edge resource allocation and a useful anchor for the wiki's game-theory thread.

## Problem framing

App vendors hire compute capacity (CPU, memory, storage, bandwidth) on distributed edge servers under a pay-as-you-go model. An app user in the overlap of several servers' coverage can attach to any one that has spare capacity. Two objectives conflict: (1) maximize allocated users; (2) minimize system cost. Centralized optimal allocation is NP-hard, so a scalable distributed mechanism is needed.

## System model

- **Actors.** n app users with multi-dimensional capacity needs; m edge servers with available capacity vectors over dimension set D = {cpu, memory, storage, bandwidth, ...}.
- **Multi-tenancy benefit.** Server utilization rises with the number of co-located users following a log-based model (with diminishing returns), captured as a per-dimension multi-tenancy benefit.
- **Constraints.** Coverage (a user can only attach to a server covering it) and per-dimension capacity.
- **Cost.** Hiring cost minus multi-tenancy benefit, plus a penalty for unallocated users (who fall back to local/cloud execution).

## Method

- Models EUA as a constrained optimization problem and proves NP-hardness via reduction to the variable-size vector bin-packing problem.
- Recasts it as **EUAGame**, where each user is a self-interested player choosing a neighbor server to maximize its benefit; proves the game is a [[potential-game]] (hence finite improvement property + existence of a pure-strategy [[nash-equilibrium]]).
- Proposes a **decentralized algorithm** that reaches an NE as a self-enforcing allocation, analyzed both theoretically and experimentally.

## Key findings

- The EUA problem is solved effectively and efficiently in a distributed manner; experiments (per the paper) show the decentralized approach finds high-quality allocations at far lower cost than centralized optimization. Specific benchmark numbers are reported in the paper's evaluation section and are not reproduced here beyond the qualitative claim.

## Limitations / future work

Quasi-static setting — user locations and capacity needs are fixed during allocation. The authors flag mobility/trajectory effects, dynamic user arrivals/departures, and diverse capacity needs as future work.

## Relation to the corpus

A terrestrial-edge counterpart to the wiki's aerial/space [[potential-game]] offloading work. It shares the potential-game-with-distributed-best-response structure of [[chen-2024-ulse-game]] (LUTO-Game) and contrasts with the bargaining/matching hybrid of [[sun-2023-bargain-match-vec]]. Unlike most curated sources, it studies *user-to-server allocation* (placement) rather than task offloading per se, broadening the [[edge-user-allocation]] thread.

## Raw artifacts

- `raw/sources/A_Game-Theoretical_Approach_for_User_Allocation_in_Edge_Computing_Environment.pdf-6a127707-a8c8-4eb3-95db-bd84451c63bb/full.md`
- Original PDF and extracted figures in the same folder.
