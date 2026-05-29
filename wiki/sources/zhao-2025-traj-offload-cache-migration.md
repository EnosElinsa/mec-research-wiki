---
type: source
title: "Joint Optimization of Trajectory, Offloading, Caching, and Migration for UAV-Assisted MEC"
tags: [source, uav-mec, multi-uav-mec, task-offloading, task-migration, task-caching, trajectory-control, lyapunov-optimization, semidefinite-relaxation, throughput-maximization]
related:
  - "[[mobile-edge-computing]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[task-migration]]"
  - "[[service-caching-mec]]"
  - "[[computational-task-caching]]"
  - "[[uav-trajectory-control]]"
  - "[[lyapunov-optimization]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[qcqp-sdr-probabilistic-mapping]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[blockage-aware-channel-model]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[load-balancing-uav-mec]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[bao-2025-ddpg-video-offloading]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
created: 2026-05-29
updated: 2026-05-29
authors: [Mingxiong Zhao, Rongqian Zhang, Zhenli He, Keqin Li]
year: 2025
url: "https://doi.org/10.1109/TMC.2024.3486995"
venue: "IEEE Transactions on Mobile Computing (TMC); online 28 Oct 2024, current version 5 Feb 2025"
---

# Joint Optimization of Trajectory, Offloading, Caching, and Migration for UAV-Assisted MEC

## TL;DR
This paper studies a multi-UAV, multi-user, multi-slot [[multi-uav-assisted-mec]] system where each UAV can **compute**, **migrate** to another UAV, or **cache** a ground user's offloaded task — the last enabling [[computational-task-caching]], i.e. deferring a whole computational task to a later slot when capacity frees up. It maximizes long-term average **throughput** under a long-term scheduling-cost budget and cache-stability constraint, using [[lyapunov-optimization]] to break the dynamic problem into per-slot subproblems solved by Block Coordinate Descent ([[alternating-optimization-sdr-sca]]): a K-means-based deployment step ([[weighted-kmeans-uav-deployment]]), an offloading step, a binary scheduling step recast as a QCQP and solved by [[qcqp-sdr-probabilistic-mapping]], and a bandwidth step. Simulations report throughput up **10%-45%**, scheduling cost down **15%-30%**, and execution time down **8%-37%** versus conventional methods.

## Problem
UAV-assisted MEC extends [[mobile-edge-computing]] to areas without infrastructure, but UAVs have far less compute than fixed edge servers, limited coverage, and must track mobile users. Prior work studies [[uav-trajectory-control]], [[task-offloading]], [[task-migration]], and caching largely in isolation and misses their **synergy**. Crucially, existing UAV caching work focuses on content/data pre-caching ([[service-caching-mec]]) and neglects **computational task caching** — caching tasks during compute peaks and processing them once capacity frees up, which can cut service-denial and raise throughput. The paper jointly optimizes UAV trajectories together with task association, offloading, computation, migration, caching, and inter-UAV bandwidth, giving a dynamic, long-term, mixed-integer, non-convex problem with five interdependent binary decisions.

## System model
- **Actors**: U UAVs serving I mobile users in overlapping regions; no fixed edge server in the base model — UAVs compute, relay among themselves, or cache. Users upload via FDMA on a fixed 1 MHz each; inter-UAV migration shares a 20 MHz pool, supporting [[load-balancing-uav-mec]] across UAVs.
- **Time/tasks**: duration D split into τ slots (200 s / 200 slots); each user generates at most one task per slot (Bernoulli), described by input bits e_i(t) and CPU cycles w_i(t) (1-3 Mbits, 1-3 cycles/bit). A task must be offloaded to its associated UAV in its slot, then computed, migrated, or **cached for the next slot**.
- **Decisions**: association s, offloading z, computation a, migration m, caching o, and migration bandwidth split b.
- **Channel** ([[blockage-aware-channel-model]]): UAV-to-ground uses a probabilistic LoS/NLoS path-loss model (elevation-angle-dependent LoS probability; α=11.95, β=0.14, NLoS attenuation k=0.2, path-loss exponent 2.3, 60 dB at d0=1 m); UAV-to-UAV assumed LoS-only. UAV altitude 60 m, coverage radius 180 m; users move randomly at 0.5-1 m/s.
- **Cost/energy**: scheduling cost c = ϖ1·delay + ϖ2·energy (base 0.4/0.6, re-scaled per compute/migrate/cache); delay spans migration, computation, and caching; energy spans migration transmit energy, computation (η_c=10⁻¹²), and caching (η_o=10⁻¹⁵). UAV compute W_u=1 GHz.
- **Long-term constraints**: cache-space stability and an average scheduling-cost budget (=20 per UAV). Cache-write time assumed negligible.

## Method
- **Formulation**: maximize long-term average throughput (served-task count) subject to single-UAV offloading, mutually exclusive compute/migrate/cache, the long-term cost budget, and cache stability — mixed-integer, non-convex, dynamic.
- **Lyapunov framework** ([[lyapunov-optimization]]): a per-UAV virtual queue G_u(t) tracks scheduling-cost backlog alongside the cache queue; a drift-plus-penalty bound with factor V decouples the problem into per-slot decisions, trading throughput against queue backlog.
- **BCD per slot** ([[alternating-optimization-sdr-sca]]): iterate four subproblems — (1) UAV deployment + association, (2) offloading, (3) scheduling, (4) migration bandwidth — to convergence (Algorithm 7, the Proposed Algorithm).
- **TSOUD deployment** ([[weighted-kmeans-uav-deployment]]): enhances K-means with heuristic indicators from the previous slot's migration M(t-1) and caching O(t-1) so UAVs relocate toward computation hotspots, coupling [[uav-trajectory-control]] with task scheduling.
- **Scheduling solver** ([[qcqp-sdr-probabilistic-mapping]]): the coupled binary compute/migrate/cache decision is recast as a non-convex QCQP, relaxed by semidefinite relaxation (CVX/MOSEK), then mapped back to feasible binaries via a normalized probabilistic (randomized) mapping.
- **Bandwidth**: convex; solved by primal-dual with a high-SNR closed-form (Proposition 1).

## Key findings
- Versus **K-means++** and **Random** deployment: throughput **+10%-45%**, scheduling cost **−15%-30%** (Fig. 5); conclusion also reports execution time **−8%-37%** versus conventional algorithms.
- Steady state (Fig. 5): PA throughput ≈ 30/slot (K-means++ ≈ 27, Random ≈ 21); PA scheduling cost ≈ 17.5 (K-means++ ≈ 19.5-20, Random ≈ 24.5).
- Running time (Table I): at 1000 users PA = 3.72 s vs K-B&B 18.85 s, K-GA 9.34 s, TSOUD-B&B 18.54 s, TSOUD-GA 8.30 s; RSA (random scheduling) fastest (0.36 s) but low quality.
- Migration + caching beats compute-only (Fig. 7): sustained association ≈ 40, offloading ≈ 30, computing ≈ 13, migration ≈ 17, caching ≈ 13 — above the compute-only baseline of ≈ 22.
- Lyapunov factor V (Fig. 8): larger V lowers throughput and grows backlog; system stabilizes within [O(1/V), O(V)] after ~100 slots.
- Versus **DRL baselines** (DDPG offline; A2C, PPO online), the Lyapunov approach is more stable — RL suffers fixed action dimensions, limited multi-hop migration (only two hops; extra tasks discarded), poor constraint satisfaction, cache-queue instability, and convergence difficulty with five interdependent binaries.
- Setup: 3 UAVs, 100 users, 500 m × 500 m, 200 slots.

## Limitations
Simulation-only (MATLAB R2021a + CVX/YALMIP; PyCharm/PyTorch for the RL comparison); no hardware or field trial. The model does not address network disruptions/communication failures, UAV battery depletion or mechanical failure or leaving the network, or dense-urban high-rise blockage with mixed LoS/NLoS — all named as future work. Cache-write time is assumed negligible, the closed-form bandwidth result relies on a high-SNR assumption, migration is limited to a few hops, and there is no fixed cloud/edge-server tier in the base scenario.

## Relation to the corpus
This is a [[multi-uav-assisted-mec]] study that jointly couples [[uav-trajectory-control]], [[task-offloading]], [[task-migration]], and a novel [[computational-task-caching]] mechanism (distinct from [[service-caching-mec]] content pre-caching), solved through [[lyapunov-optimization]] plus a [[qcqp-sdr-probabilistic-mapping]] scheduling step and a [[weighted-kmeans-uav-deployment]]-style trajectory step. It pairs naturally with [[zhang-2025-mcma-task-migration]] on task migration and with the overlapping author group's UAV caching/offloading work [[bao-2025-ddpg-video-offloading]] (cf. ref [5] cooperative cache scheduling). It also relates to UAV-MEC trajectory and scheduling studies such as [[wu-2026-terrain-aware-uav-mec]] (realistic [[blockage-aware-channel-model]] and trajectory control), [[zhang-2025-ssac-mgi-heterogeneous-uav]] (multi-UAV trajectory + scheduling), and multi-UAV delay/energy offloading like [[huang-2023-mu-aec-task-energy]]. Unlike the DRL-heavy corpus, it argues an optimization-theoretic ([[lyapunov-optimization]]) approach is more stable than DDPG/A2C/PPO for this five-binary, long-term-constrained problem.

## Raw artifacts
- `raw/sources/Joint_Optimization_of_Trajectory_Offloading_Caching_and_Migration_for_UAV-Assisted_MEC/full.md`
