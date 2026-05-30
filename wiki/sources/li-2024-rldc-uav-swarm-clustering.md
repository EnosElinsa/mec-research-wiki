---
type: source
title: "Energy-Efficient UAV Swarm Assisted MEC with Dynamic Clustering and Scheduling"
authors: ["Jialiuyuan Li", "Jiayuan Chen", "Changyan Yi", "Tong Zhang", "Kun Zhu", "Jun Cai"]
year: 2024
url: "https://doi.org/10.1109/WCNC57260.2024.10570678"
venue: "IEEE Wireless Communications and Networking Conference (WCNC) 2024"
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
  - "[[multi-agent-q-learning]]"
  - "[[intra-swarm-task-delegation]]"
  - "[[uav-charging-scheduling]]"
  - "[[service-caching-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[hierarchical-aerial-mec]]"
  - "[[load-balancing-uav-mec]]"
  - "[[li-2025-stochastic-game-uav-swarm]]"
  - "[[sun-2024-asap-uav-swarm]]"
  - "[[qu-ecoei-uav-swarm]]"
  - "[[wang-2025-uav-swarm-stackelberg]]"
created: 2026-05-31
updated: 2026-05-31
---

# Energy-Efficient UAV Swarm Assisted MEC with Dynamic Clustering and Scheduling

## Citation

Li, J., Chen, J., Yi, C., Zhang, T., Zhu, K., & Cai, J. (2024). *Energy-Efficient UAV Swarm Assisted MEC with Dynamic Clustering and Scheduling*. IEEE WCNC 2024, Dubai, UAE.

> Metadata note: this paper's **own parse** carries no `Digital Object Identifier`, venue, or year line. It is the **conference precursor** of the curated journal paper [[li-2025-stochastic-game-uav-swarm]] (IEEE TGCN), whose parse explicitly states "This article was presented in part at the IEEE WCNC 2024, Dubai, UAE [DOI: 10.1109/WCNC57260.2024.10570678]." Venue (WCNC 2024), year (2024), and the DOI above are grounded in that journal cross-reference plus a web-confirmed title match (arXiv:2402.18936). See the duplicate decision in the relation section.

## TL;DR
The conference seed of the [[li-2025-stochastic-game-uav-swarm|RLDC]] line of work. UAVs are organized into swarms (one leader + several follower UAVs) acting as mobile edge servers for ground IoT devices, and follower UAVs are allowed to **dynamically re-cluster** (switch leaders) as spatial positions and application placement change over time. The authors maximize long-term energy efficiency (tasks processed per unit energy) by jointly deciding energy replenishment, application placement, trajectory planning, [[dynamic-uav-clustering]], and [[intra-swarm-task-delegation]]. The problem is reformulated as **six** coupled multi-agent [[stochastic-game]]s and solved by **RLDC**, a [[multi-agent-q-learning]] (Q-learning) coordination algorithm. Simulations show RLDC beats fixed-swarm and no-swarm baselines on energy efficiency.

## Problem
UAV-swarm-assisted MEC is attractive for terrain-limited and emergency scenarios but faces three coupled bottlenecks (stated verbatim in the intro): with **fixed** clustering the computing workload across swarms becomes severely unbalanced as IoT demand shifts in space/time; battery-limited UAVs (especially leaders) must fly to a depot for energy replenishment, breaking long-term static formations; and storage-limited UAVs cannot host every application type, forcing application placement and within-swarm delegation. The paper asks how follower UAVs should dynamically choose which leader to follow, jointly with energy replenishment, application placement, leader/follower trajectory planning, and task delegation, to maximize **long-term energy efficiency** of all UAVs (total tasks processed / total energy consumed [P1]). Because UAVs are intelligent and autonomous, they both cooperate and compete, and they have no future task information.

## System model
- **Actors/tiers:** edge **depot** (wired leader recharge + application update) → **M leader UAVs** (altitude `H_L = 150 m`) → **N follower UAVs** (altitude `H_F = 120 m`) → **K ground IoT devices** (a [[hierarchical-aerial-mec]]-style structure).
- **Geography:** target region divided into large grids (side `l`, bounds swarm motion) and small grids (side `q`, bounds follower motion); follower downlink range `sqrt(2)q/2` covers one small grid; each small grid covered by ≤1 follower (collision avoidance).
- **Channels:** SINR-based uplink with a shared band `B` per swarm causing intra-swarm interference; rates `μ = B·log2(1+γ)`; probabilistic path loss for follower↔IoT and leader↔follower links.
- **Energy:** compute energy `ξ·f²·Task`; propulsion power model follows the rotary-wing reference [10] (= [[zeng-2019-rotary-wing-energy-min]] in this corpus); leaders also incur a depot-return energy term.
- **Decisions:** depot-return `ε`, application placement `ωᴸ/ωᶠ` ([[service-caching-mec]]), clustering/association `δ` ([[dynamic-uav-clustering]]), delegation `φ` ([[intra-swarm-task-delegation]]), leader/follower move direction; constraints (9)–(17) enforce single-leader-per-follower, ≥1 application per type, grid-center motion, collision avoidance, and intra-swarm containment.

## Method
- **Formulation:** long-term energy-efficiency maximization [P1] reformulated as a series of strongly coupled multi-agent [[stochastic-game]]s — **six** games here: ERSG (energy replenishment), APSG (application planning), **LTSG** (leader trajectory planning), DCSG ([[dynamic-uav-clustering]]), **FTSG** (follower trajectory planning), and TDSG ([[intra-swarm-task-delegation]]). (The journal version [[li-2025-stochastic-game-uav-swarm]] later collapses leader+follower trajectory into a single TPSG, giving five games.)
- **Per-agent MDPs:** each game defines state/action/reward/transition; leader-ERSG uses a `-10` penalty when the "≥1 application per type" constraint is violated; reward signals track per-swarm tasks-per-energy and system `E^effi`.
- **Solver — RLDC:** decentralized ε-greedy [[multi-agent-q-learning]] with six per-role learners (leader: ER/AP/LT; follower: DC/FT/TD). Discount `σ ∈ [0,1]`; ε-greedy policy; standard Q-value update (Eq. 25).
- **Note:** unlike the journal version, this conference paper does **not** include the Nash-equilibrium existence proof or the convergence/complexity analysis (it states only that RLDC "obtains equilibriums").

## Key findings
- RLDC > fixed-UAV-swarm > no-UAV-swarm on all-UAV energy efficiency across every swept parameter; the no-swarm case is worst because it cannot delegate unprocessable tasks.
- Energy efficiency rises monotonically with IoT device count — e.g. ≈ 680 (RLDC) / 570 (fixed) / 480 (no swarm) at 1900 devices; ≈ 400 / 350 / 280 at 500 devices; zero at 100 devices (values read from the parsed Fig. 2 table, units unlabeled — read as trends).
- Energy efficiency vs. UAV velocity is unimodal, peaking ≈ 30 m/s in the parsed Fig. 3 table (≈ 420 RLDC); higher speeds waste propulsion energy.
- Small-grid size `q = 50 m` beats 25 m and 75 m; efficiency grows with leader storage capacity `Sᴸ` (q = 50 m: ≈ 240 → 400 as `Sᴸ` goes 1 → 10) — parsed Fig. 4 table.
- Simulation parameters (Table I): M = 3, N = 9, K = 500, C = 10, `Sᴸ = 6`, `Sᶠ = 4`, B = 10 MHz, slot 30 s, v = 20 m/s, target region **2500 m × 2500 m**.

## Limitations
Simulation-only (no hardware); small scale (3 leaders / 9 followers / 500 devices); IoT positions random/static; tabular Q-learning over discretized states (scalability concern); fixed UAV altitudes; collisions/constraints enforced only through reward penalties; no theoretical NE/convergence analysis (added later in the journal version). Reported magnitudes are extracted from MinerU-parsed figure tables and should be read as trends, not exact values.

## Relation to the corpus
**Relationship to the journal version:** this is **not** a duplicate of [[li-2025-stochastic-game-uav-swarm]] — it is its **conference precursor**. The journal paper (IEEE TGCN, 8 authors, five stochastic games, with an NE-existence proof and convergence/complexity analysis) explicitly states it "was presented in part at the IEEE WCNC 2024." This conference version has **6 authors** (Li, Chen, Yi, Zhang, Zhu, **Cai** — NUAA + **Concordia University**), **six** games (separate LTSG/FTSG), a larger **2500 m × 2500 m** region, and **no** NE/convergence proof. Genuinely distinct → curated and cross-linked rather than collapsed.

It sits in the UAV-swarm collaborative-computing track with [[sun-2024-asap-uav-swarm]] (in-swarm DL inference) and [[qu-ecoei-uav-swarm]] (elastic collaborative inference), and in the game-theoretic-offloading track. Shared building blocks: [[multi-uav-assisted-mec]], [[mobile-edge-computing]], [[task-offloading]], [[uav-trajectory-control]], [[uav-charging-scheduling]], [[service-caching-mec]], [[load-balancing-uav-mec]]. Its rotary-wing propulsion model is the [[zeng-2019-rotary-wing-energy-min]] model.

## Raw artifacts
- `raw/sources/Energy-Efficient_UAV_Swarm_Assisted_MEC_With_Dynamic_Clustering_and_Scheduling/full.md`
- Original PDF and extracted figures in the same folder.
