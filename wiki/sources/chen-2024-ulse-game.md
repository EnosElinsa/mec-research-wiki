---
type: source
title: "Multi-User Task Offloading in UAV-Assisted LEO Satellite Edge Computing: A Game-Theoretic Approach"
tags: [source, task-offloading, leo-satellite-edge-computing, game-theory, uav-mec, potential-game]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[task-offloading]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[leo-satellite-coverage-time]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[equilibrium-efficiency-metric]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
  - "[[bi-2025-sg-mapg]]"
  - "[[li-2025-stochastic-game-uav-swarm]]"
  - "[[huang-2023-mu-aec-task-energy]]"
created: 2026-05-29
updated: 2026-05-29
authors: [Ying Chen, Jie Zhao, Yuan Wu, Jiwei Huang, Xuemin Sherman Shen]
year: 2024
url: https://doi.org/10.1109/TMC.2024.3465591
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
---

# Multi-User Task Offloading in UAV-Assisted LEO Satellite Edge Computing: A Game-Theoretic Approach

## TL;DR
This paper studies multi-user [[task-offloading]] in a UAV-assisted LEO satellite edge computing (ULSE) network, where ground devices compete for scarce UAV/satellite channels and CPU to minimize their own delay-plus-energy cost. The cost-minimization problem is proven NP-hard, recast as a [[potential-game]] (the LUTO-Game) with a guaranteed [[nash-equilibrium]], and solved by a distributed algorithm (JULTO). In simulation, JULTO reaches equilibrium in a handful of iterations at cost near the centralized optimum, but with execution time orders of magnitude lower and consistently below greedy and random baselines.

## Problem
Compute-intensive, latency-sensitive applications on mobile user devices (MUDs) exceed their CPU/battery budgets, and ground-base-station [[mobile-edge-computing]] cannot cover harsh terrain or survive disasters. The authors place edge servers on both low-altitude UAVs and LEO satellites ([[leo-satellite-edge-computing]]) to deliver global coverage, forming a space-air system in the spirit of the [[space-air-ground-integrated-network]]. The challenge: MUDs are selfish and individually rational, so they compete for limited heterogeneous resources, and each MUD additionally faces a per-device [[leo-satellite-coverage-time]] window because the satellite is moving. The objective is to minimize the total delay-plus-energy cost over all MUDs subject to coverage-time, server-capacity, and individual-rationality constraints, in a solution space that grows exponentially with the number of MUDs, UAVs, and satellites.

## System model
- Tiers/actors: N MUDs, M1 UAVs (edge server + wireless power transfer), M2 LEO satellites (edge servers); no ground base stations.
- Task: each MUD has one task H_i = (B_i bits, C_i CPU cycles), C_i = B_i · 1000 cycles/bit. Decision o_i = (a_i, b_i, c_i) selects mode (local/UAV/LEO), server, and wireless channel.
- Communication: c^u UAV channels and c^L LEO channels; co-channel MUDs interfere (SINR), data rate via Shannon. UAV link uses a probabilistic LoS/NLoS path-loss model within a coverage radius R^uav; LEO link uses antenna gain, Rayleigh fading, and cloud/rain attenuation with free-space loss.
- Coverage time: geometric model from orbit height (784 km), earth radius (6371 km), elevation angle, and satellite speed yields max communication time T_i^L; LEO offloading must satisfy T_i^LEO ≤ T_i^L (adds a propagation delay term).
- Energy: local energy l^e·C_i; transmit energy p_i·t^tr; for UAV offloading the MUD harvests energy back via [[wireless-power-transfer]] / [[rf-energy-harvesting]] (e^eh = eta·p^uav·g), netted off the UAV cost.
- Cost: K_i = lambda^t·delay + lambda^e·energy, lambda^t + lambda^e = 1. Constraints: coverage time (C1), offload cost ≤ local cost (C2), UAV/LEO CPU capacity (C3/C4).
- Assumption: UAV mobility, flight, and hovering energy are ignored (single-snapshot decision).

## Method
- Objective is sum-cost minimization, proven NP-hard via reduction from the Multiple Knapsack problem.
- Reformulated as the LEO-UAV Task Offloading Game (LUTO-Game): selfish MUDs as players, offloading decisions as strategies, own cost as payoff; the target is a [[nash-equilibrium]] where each decision is a best response.
- A task offloading rule permits a switch only when a MUD's own cost reduction exceeds the harm to others, so every accepted move lowers total cost. With potential function Y = sum of costs, LUTO-Game is shown to be a [[potential-game]], yielding the finite improvement property and existence of at least one NE.
- JULTO algorithm: distributed and iterative ([[binary-vs-partial-offloading]] — whole-task offloading). All MUDs start local; each round, MUDs revert to local if offloading is worse or violates coverage, compute best alternatives in parallel, and those whose change reduces global cost compete, with one random winner updating per round until no MUD wants to move.
- Analysis: defines price of anarchy as an [[equilibrium-efficiency-metric]] (worst NE cost / centralized optimum) and derives an iteration-count upper bound and O(N(M1 c^u + M2 c^L)(...)) complexity.

## Key findings
- Converges in ~12 iterations (N=10, M1=3, M2=1, single channel each) to near-optimal total cost.
- Execution time far below the centralized optimum: at N=10, 512096.68 ms (centralized) vs 1.78 ms (JULTO); at N=8, 14560.04 ms vs 1.09 ms.
- Sub-linear iteration growth: N 10 → 100 raises iterations only 11 → 37; similar saturation versus UAV, satellite, and channel counts despite exponential solution-space growth.
- Lowest total cost, average delay, and average energy versus ICSOC, CCPM, and Random across task size, MUD compute capability, transmit power, and resource-count sweeps (e.g., 5.0 MB task: JULTO 890 vs ICSOC 940 vs CCPM 980 vs Random 1520).
- Delay cost dominates: total cost rises with the delay weight lambda^t (295 → 425 as lambda^t goes 0.1 → 0.9).

## Limitations
Simulation-only with no hardware or real traces. UAV mobility, flight, hovering energy, and satellite energy are excluded by assumption (the stated future-work direction). The per-round competition winner is chosen randomly, the efficiency guarantee is a worst-case price-of-anarchy bound rather than optimality, and offloading is whole-task to a single server/channel.

## Relation to the corpus
This is a game-theoretic counterpart to learning-based aerial/space offloading work. It contrasts with the Stackelberg formulation in [[wang-2025-uav-swarm-stackelberg]] and the stochastic/multi-agent games in [[bi-2025-sg-mapg]] and [[li-2025-stochastic-game-uav-swarm]] by using a [[potential-game]] with distributed best-response dynamics instead of a leader-follower or RL solver. It shares the multi-user MEC cost framing (and co-author Jiwei Huang) with [[huang-2023-mu-aec-task-energy]], and sits alongside other aerial/space MEC offloading studies such as [[jia-2025-dro-uav-hap-mec]], [[nabi-2025-jour-hierarchical-aerial]], and [[qin-2025-bcuav-masac]] within the [[multi-uav-assisted-mec]] and [[leo-satellite-edge-computing]] threads.

## Raw artifacts
- `raw/sources/Multi-User_Task_Offloading_in_UAV-Assisted_LEO_Satellite_Edge_Computing_A_Game-Theoretic_Approach/full.md`
