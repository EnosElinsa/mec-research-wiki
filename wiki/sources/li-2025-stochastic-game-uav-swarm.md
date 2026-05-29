---
type: source
title: "A Reinforcement Learning-Based Stochastic Game for Energy-Efficient UAV Swarm-Assisted MEC With Dynamic Clustering and Scheduling"
tags:
  - source
  - uav-swarm
  - mobile-edge-computing
  - stochastic-game
  - reinforcement-learning
  - dynamic-uav-clustering
  - energy-efficiency
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[stochastic-game]]"
  - "[[dynamic-uav-clustering]]"
  - "[[nash-equilibrium]]"
  - "[[multi-agent-q-learning]]"
  - "[[intra-swarm-task-delegation]]"
  - "[[uav-charging-scheduling]]"
  - "[[service-caching-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[wireless-power-transfer]]"
  - "[[load-balancing-uav-mec]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
  - "[[zhang-2025-mcma-task-migration]]"
created: 2026-05-29
updated: 2026-05-29
authors:
  - Jialiuyuan Li
  - Changyan Yi
  - Jiayuan Chen
  - You Shi
  - Tong Zhang
  - Xiaolong Li
  - Ran Wang
  - Kun Zhu
year: 2025
url: "https://doi.org/10.1109/TGCN.2024.3424449"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
---

# A Reinforcement Learning-Based Stochastic Game for Energy-Efficient UAV Swarm-Assisted MEC With Dynamic Clustering and Scheduling

## TL;DR
A [[multi-uav-assisted-mec]] system organizes UAVs into swarms (one leader + several followers) acting as mobile edge servers for ground IoT devices, but lets follower UAVs **dynamically re-cluster** — switch leaders over time — as demand and application placement change. The authors maximize long-term energy efficiency (tasks processed per unit energy) by jointly deciding energy replenishment, application placement, leader trajectory, [[dynamic-uav-clustering]], and [[intra-swarm-task-delegation]]. They cast this as five interconnected multi-agent [[stochastic-game]]s, prove a [[nash-equilibrium]] exists, and solve it with **RLDC**, a decentralized [[multi-agent-q-learning]] algorithm using Q-value exchange. RLDC beats fixed-swarm and no-swarm baselines on energy efficiency across all swept parameters.

## Problem
UAV-swarm-assisted MEC is attractive for terrain-limited and emergency scenarios, but faces three coupled bottlenecks: with **fixed** clustering the computing workload across swarms becomes badly unbalanced as IoT demand shifts in space/time; battery-limited UAVs (especially leaders) must periodically return to a depot to recharge, interrupting service; and storage-limited UAVs cannot host every application type, forcing application-placement and within-swarm delegation choices. The paper asks how follower UAVs should dynamically choose which leader to follow, jointly with energy replenishment, application placement, leader trajectory planning, and task delegation, to maximize the **long-term energy efficiency** of all UAVs (total tasks processed / total energy consumed). The challenge is that autonomous UAVs both cooperate and compete (selfish leaders may delay charging or hoard popular apps; followers may crowd the busiest leader), and they have no knowledge of future task requests.

## System model
- **Actors/tiers:** edge **depot** (wired leader recharge + application update) → **M leader UAVs** (altitude 150 m) → **N follower UAVs** (altitude 120 m) → **K static ground IoT devices**. Each swarm is 1 leader + several followers (a [[hierarchical-aerial-mec]]-style structure).
- **Geography:** 1000 m × 1000 m region split into large grids (side `l`, bounds swarm motion) and small grids (side `q`, bounds follower motion); follower coverage radius `sqrt(2)q/2`.
- **Slot timing:** per slot a leader either returns to the depot or moves its swarm one large grid (forward/back/left/right) then hovers; during leader hover each follower selects a leader (clustering) and hovers over a small grid to process/delegate tasks.
- **Channels:** probabilistic LoS air-to-ground path loss (follower↔IoT) and free-space-style path loss (leader↔follower); shared band `B` per swarm causes intra-swarm interference; SINR-based rates `μ = B·log2(1+γ)`.
- **Energy:** compute energy `ξ·f²·D`; leaders charge followers via [[wireless-power-transfer]]; leaders recharge at depot ([[uav-charging-scheduling]]). Application placement at storage-limited UAVs is effectively [[service-caching-mec]].
- **Decisions:** depot-return `ε`, application placement `ωᴸ/ωᶠ`, association/clustering `δ`, delegation `φ`, leader move direction.
- **Assumptions:** result feedback ignored (small); IoT positions fixed; no future info; dedicated low-load control channel (CSMA/CA, >70 Mbps) carries Q-values with negligible delay.

## Method
- **Formulation:** long-term energy-efficiency maximization [P1] reformulated as five strongly interconnected multi-agent [[stochastic-game]]s — ERSG (energy replenishment), APSG (application planning), TPSG (trajectory planning), DCSG ([[dynamic-uav-clustering]]), TDSG ([[intra-swarm-task-delegation]]).
- **Per-agent MDPs:** each game defines state/action/reward/transition; rewards track system energy efficiency `E^effi` with `-10` penalties for constraint violations (battery depletion, collisions, infeasible clustering/processing). Leaders carry ER/AP/TP learners; followers carry DC/TD learners.
- **Solver — RLDC:** decentralized ε-greedy [[multi-agent-q-learning]]. Each slot, UAVs exchange historical Q-values over a dedicated channel (a central controller distributes them but makes no decisions), act, then update Q-values from own reward plus neighbors' Q-values. Settings: discount σ = 0.9, learning rates η = ν = 0.1, ε = 0.1.
- **Theory:** proves equivalence to a multi-period stage game ⇒ a [[nash-equilibrium]] exists (Lemma 1); proves per-game Q-values converge to optimal NE Q-values w.p. 1 via contraction mapping (Lemma 2, Theorem 1). Complexity: time `O(LOOP·T·N)`; space scales with exchanged Q-table sizes (state spaces exponential in M, N, C).

## Key findings
- RLDC > fixed-UAV-swarm > no-UAV-swarm on all-UAV energy efficiency across every swept parameter; the no-swarm case is worst because it cannot delegate unprocessable tasks.
- Energy efficiency rises monotonically with IoT device count — e.g. at 1900 devices ≈ 680 (RLDC) / 550 (fixed) / 470 (no swarm); at 500 devices ≈ 400 / 340 / 280 (values read from parsed figures, units unlabeled).
- Energy efficiency vs. time-slot length increases then saturates/declines (idle hovering); zero when move time exceeds the slot.
- Energy efficiency vs. velocity is unimodal, peaking ≈ 30 m/s; higher speeds waste propulsion energy.
- Small grid `q = 50 m` beats 25 m and 75 m; efficiency grows with leader storage capacity (q = 50 m: ≈ 240 → 400 as `Sᴸ` goes 1 → 10).
- Average task latency falls with higher follower TX power and higher leader compute capacity, and rises with larger `q`.
- Leader energy-consumption traces (Fig. 4) visibly fluctuate as followers switch leaders, demonstrating real dynamic clustering (e.g. two followers move from leader 3 → 1 at slot 22).

## Limitations
Simulation-only (no hardware); small scale (3 leaders / 9 followers / 500 devices in 1 km²); IoT positions assumed static; tabular Q-learning over discretized states with sizes exponential in M, N, C (scalability concern); fixed UAV altitudes; relies on a dedicated control channel with negligible Q-value exchange delay and a central Q-value distributor; collisions/constraints enforced only through reward penalties. Reported magnitudes are extracted from MinerU-parsed figure tables and should be read as trends.

## Relation to the corpus
This paper sits at the intersection of UAV-swarm MEC and game theory. It is the closest sibling to [[wang-2025-uav-swarm-stackelberg]], which also drives UAV-swarm decisions with a game-theoretic equilibrium (Stackelberg vs. this paper's [[stochastic-game]]/[[nash-equilibrium]]); both contrast with the [[chen-2024-ulse-game|potential-game]] formulation of multi-user LEO offloading. The depot→leader→follower structure echoes [[nabi-2025-jour-hierarchical-aerial]] ([[hierarchical-aerial-mec]]). Its decentralized [[multi-agent-q-learning]] coordination relates to the multi-agent RL approaches in [[qin-2025-bcuav-masac]] and [[zhang-2025-ssac-mgi-heterogeneous-uav]]. Its [[intra-swarm-task-delegation]] decision is a useful contrast to the [[task-migration]] formulation in [[zhang-2025-mcma-task-migration]]. Shared building blocks with the wider corpus include [[multi-uav-assisted-mec]], [[mobile-edge-computing]], [[task-offloading]], [[uav-trajectory-control]], [[uav-charging-scheduling]], [[wireless-power-transfer]], [[service-caching-mec]], and [[load-balancing-uav-mec]].

## Raw artifacts
- `raw/sources/A_Reinforcement_Learning-Based_Stochastic_Game_for_Energy-Efficient_UAV_Swarm-Assisted_MEC_With_Dynamic_Clustering_and_Scheduling/full.md`
