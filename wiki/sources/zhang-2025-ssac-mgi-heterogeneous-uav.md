---
type: source
title: "Safe and Energy-Efficient Trajectory Planning for Heterogeneous Multi-UAV Enabled Mobile Edge Computing"
authors: ["Xiuling Zhang", "Riheng Jia", "Quanjun Yin", "Zhonglong Zheng", "Minglu Li"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3632884"
venue: "IEEE Transactions on Mobile Computing"
tags: [uav, mec, heterogeneous, safe-rl, trajectory, sac, collision-avoidance, multi-agent]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[masac]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[safe-reinforcement-learning]]"
  - "[[collision-avoidance-mgi]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[peng-2025-drudm-cfg]]"
created: 2026-05-28
updated: 2026-05-31
---

# Safe and Energy-Efficient Trajectory Planning for Heterogeneous Multi-UAV Enabled MEC

## Citation

Zhang, X., Jia, R., Yin, Q., Zheng, Z., & Li, M. (2025). *Safe and Energy-Efficient Trajectory Planning for Heterogeneous Multi-UAV Enabled Mobile Edge Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3632884.

## TL;DR

Existing UAV-MEC schedulers assume **homogeneous** UAVs and uniform UE distributions — wrong for real deployments. This paper allows each UAV to carry a *subset* of service types with different resource budgets per type. The result: a UAV can only serve jobs whose service type it actually hosts, which forces UAVs to fly farther to find compatible jobs and inflates flight-energy.

Solution: **SSAC-MGI** — a multi-agent safe RL algorithm with two cooperating modules:

1. **SSAC (Shared Soft Actor-Critic)** — UAVs share a backbone for the *common* features (positions, time) but have heterogeneous heads for service-type-specific features. Lets the multi-agent system learn jointly without forcing identical capability assumptions.
2. **MGI (Markov Game of Intervention)** — a two-agent collision-avoidance subgame: when two UAVs are on a near-collision trajectory, one acts as "intervention agent" and the other as "non-intervention agent". The intervention agent's policy is constrained to deflect its own trajectory while the other's stays nominal. This avoids the symmetric-deflection failure mode where both UAVs swerve the same direction and still collide.

## Problem framing

Variables:

- UAV trajectories (continuous).
- Per-UAV per-slot job admission (which UE jobs to serve).
- Resource allocation per service type per UAV.

Objectives (multiplexed via reward):

- Minimize job miss rate (jobs that don't complete by deadline).
- Minimize average UAV energy consumption.
- Minimize average UE energy consumption.
- Maintain flight safety (no UAV-UAV collisions).

## Method specifics

- **Heterogeneous service representation.** Each UAV state includes a one-hot of its service-type set + per-type resource budget. SSAC's shared encoder ignores the type vector; per-head decoders condition on it.
- **Constraint shaping.** Safety constraint is *not* in the reward — it's enforced by the MGI sub-game whose Nash equilibrium guarantees collision avoidance even when the cooperative reward favors close approach.

## Findings

- Outperforms vanilla MASAC and MADDPG baselines on combined metric (miss rate × energy × safety).
- Asymmetric deflection from MGI eliminates the back-and-forth oscillation seen in symmetric collision-avoidance heuristics.
- Heterogeneous-aware shared encoder converges faster than per-UAV-isolated training because the shared backbone amortizes common features.

## Limitations / future work

- Service-type set per UAV is fixed at deployment; live re-provisioning isn't modeled.
- 2-D trajectory (fixed altitude); 3-D collision geometry is acknowledged but deferred.
- MGI is a 2-agent collision sub-game; multi-UAV simultaneous near-misses need extension.

## Cross-link with related sources

- Same UAV-trajectory + multi-agent DRL family as [[liu-2026-jppo-en-convntm]] and [[peng-2025-drudm-cfg]]. The novel ingredient is **heterogeneity** + **safety as an explicit Markov-game constraint**.
- Composes with [[hierarchical-aerial-mec]] — heterogeneous UAVs at the lower tier can specialize, with HAPS as the catch-all.

## Raw artifacts

- `raw/sources/Safe_and_Energy-Efficient_Trajectory_Planning_for_Heterogeneous_Multi-UAV_Enabled_Mobile_Edge_Computing/full.md`
