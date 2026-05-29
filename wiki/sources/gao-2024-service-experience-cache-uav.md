---
type: source
title: "Service Experience Oriented Cooperative Computing in Cache-Enabled UAVs Assisted MEC Networks"
tags: [source, uav-mec, service-caching, task-offloading, fairness, trajectory-optimization]
related:
  - "[[service-caching-mec]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[qoe-modeling-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[load-balancing-uav-mec]]"
  - "[[air-ground-integrated-network]]"
  - "[[wireless-backhaul]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[service-experience-ratio]]"
  - "[[jains-fairness-index]]"
  - "[[huang-2023-mu-aec-task-energy]]"
  - "[[hao-2025-priority-aware-task-driven-co]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
  - "[[zhang-2025-mcma-task-migration]]"
created: 2026-05-29
updated: 2026-05-29
authors: [Xingxia Gao, Linbo Zhai]
year: 2024
url: https://doi.org/10.1109/TMC.2024.3366944
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
---

# Service Experience Oriented Cooperative Computing in Cache-Enabled UAVs Assisted MEC Networks

## TL;DR
A multi-UAV plus macro-base-station (MBS) [[mobile-edge-computing]] system where cache-enabled UAVs cooperatively serve ground UEs, optimized not only for low aggregate latency but for per-UE fairness. The authors define a **service experience ratio** — [[jains-fairness-index|Jain's fairness index]] of per-UE delay divided by average service delay — and jointly optimize [[task-offloading]], [[service-caching-mec|service caching placement]], [[uav-trajectory-control|UAV trajectory]], and resource allocation to maximize it. The mixed-integer non-convex fractional problem is solved with [[fractional-programming-dinkelbach|Dinkelbach's method]] and a four-stage [[alternating-optimization-sdr-sca|alternating optimization]] algorithm, reporting a 19–34% higher service experience ratio than baselines.

## Problem
Terrestrial MEC servers can suffer poor NLoS channels or be destroyed/overloaded; UAV-assisted MEC restores coverage but adds tight communication/computing/storage (CCS) and energy limits. Crucially, optimizing only for *overall* low latency can leave some UEs with poor experience. The paper considers a cellular network with one MBS, U rotary-wing UAVs (aerial MEC servers/relays), and M UEs that can reach the MBS only through UAVs (see [[air-ground-integrated-network]]). The objective is to cut service delay **while guaranteeing fairness among UEs**, by jointly choosing where each task runs, which services each UAV caches, how UAVs fly, and how bandwidth/compute are allocated — under per-UAV energy budgets and per-task deadlines.

## System model
- **Actors/tiers:** static MBS (ground MEC, abundant CCS) ⇄ U rotary-wing UAVs (MEC + relay, SWAP-limited) ⇄ M ground UEs. UEs connect only via UAVs; UAV→MBS uses a [[wireless-backhaul]] link. UEs do no local computing.
- **Cooperation:** horizontal (UAV↔UAV) and vertical (UAV↔MBS); each atomic task is offloaded to exactly one of associated UAV / collaborative UAV / MBS, enabling [[load-balancing-uav-mec]].
- **Control:** SDN controller supplies global state (positions, speeds, inter-UAV CSI).
- **Mobility:** fixed altitude h, static within each of T slots; constraints on area bounds, max speed, minimum inter-UAV distance (collision avoidance), and closed-loop trajectory.
- **Channel:** OFDMA uplink; probabilistic LoS/NLoS path loss; rates for UE→UAV, UAV→MBS, and free-space UAV→UAV links.
- **Caching:** MBS holds all S services; each UAV caches a subset within storage K_u (per-service size c_s); binary cache variables.
- **Energy:** computing (∝ κ f³) + relaying transmit energy + rotary-wing propulsion power; bounded by E_th.
- **Offloading is binary/atomic** — see [[binary-vs-partial-offloading]].

## Method
- **Metric & objective:** maximize the [[service-experience-ratio]] = [[jains-fairness-index]] J(F̄) / average service delay; this couples [[qoe-modeling-mec|QoE]] (fairness) with latency.
- **Hardness:** mixed-integer non-convex program with fractional structure; proven NP-hard (offloading reduces to a TSP-like problem).
- **Transformation:** [[fractional-programming-dinkelbach|Dinkelbach's method]] turns the ratio objective into a parametric program; η updated until f(η*)=0.
- **Four-stage alternating algorithm:**
  1. **Task offloading** — satisfaction-based heuristic (Algorithm 1).
  2. **Service caching** — priority-based heuristic (Algorithm 2), caching highest-priority tasks' services until storage is full.
  3. **UAV trajectory** — SCA with first-order Taylor lower bounds + slack variable for propulsion energy, solved by CVX.
  4. **Bandwidth + computing allocation** — convex, solved by CVX.
- **Guarantees:** monotone-non-decreasing objective ⇒ convergence; overall complexity O(I_max·J_max·(U·M1 + U·S + 2U³ M³)) (polynomial).

## Key findings
- Service experience ratio **19–34% higher** than comparative works (abstract).
- Converges in ~4 iterations; U=4→U=6 improves the ratio by **78.6%**.
- Gains over baselines GCR / FRA / NCOA: ~54%/32%/23% vs computation capacity; ~62%/36%/17% vs coverage range; ~31%/16% (FRA/NCOA) vs storage; ~55%/15% (GCR/NCOA) vs bandwidth.
- Average service delay in [24.1, 40.4] s (mean 33.4 s), lower and less variable than baselines.
- **Near-optimal** vs branch-and-bound (BnB) while cutting complexity from O(2^{MU}+2^{US}) to ~O(MU+US); also beats greedy caching placement (CpG).
- Simulation setup: 20 UEs, 5 UAVs, 1 MBS, 10 services, 500×500 m area, h=100 m, T=100, Δt=0.5 s, v_max=30 m/s, W0=20 MHz, W1=10 MHz, F_u=20 GHz, K_u=3.

## Limitations
Simulation-only (no hardware/testbed). Assumes a centralized SDN controller with accurate global CSI. Single fixed UAV altitude (2D trajectory); no local computing at UEs; atomic/binary tasks only; task profiles assumed known per slot (no learning under uncertainty or mobility prediction). SCA gives only a local optimum / lower bound for the trajectory subproblem. Single static MBS; result-return delay/energy neglected.

## Relation to the corpus
This work sits at the intersection of [[service-caching-mec]], [[multi-uav-assisted-mec]], [[task-offloading]], and [[uav-trajectory-control]], unified by a fairness-aware [[qoe-modeling-mec]] objective. Methodologically it pairs [[fractional-programming-dinkelbach]] with [[alternating-optimization-sdr-sca]], a recurring optimization recipe in the corpus. Its cooperative offloading and [[load-balancing-uav-mec]] design parallels [[huang-2023-mu-aec-task-energy]] (multi-UAV cooperation) and the priority-aware scheme of [[hao-2025-priority-aware-task-driven-co]]; its joint trajectory/offloading flavor connects to [[wu-2026-terrain-aware-uav-mec]], while its dynamic caching complements the migration focus of [[zhang-2025-mcma-task-migration]] and the computational-task-caching of [[zhao-2025-traj-offload-cache-migration]]. New vocabulary it contributes: [[service-experience-ratio]] and [[jains-fairness-index]].

## Raw artifacts
- `raw/sources/Service_Experience_Oriented_Cooperative_Computing_in_Cache-Enabled_UAVs_Assisted_MEC_Networks/full.md`
