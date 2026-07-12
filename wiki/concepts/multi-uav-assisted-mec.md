---
type: concept
title: Multi-UAV-Assisted Mobile Edge Computing
tags: [uav, mec, edge-computing, smart-city]
related:
  - "[[mobile-edge-computing]]"
  - "[[high-density-mobile-device-scenarios]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[uav-charging-scheduling]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[li-2025-dt-uav-swarm-resource-management]]"
  - "[[wang-2025-ppo-uav-positioning-offloading]]"
  - "[[gao-2026-fmad3qn-uav-gd-association]]"
  - "[[zhan-2026-gatd3qn-dependent-offloading]]"
  - "[[wang-2026-llm-qos-multiuav-resource]]"
  - "[[bui-2025-noma-near-far-offloading]]"
  - "[[song-2026-thz-multiuav-mec]]"
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
  - "[[wang-2026-scalable-multiuav-analytics]]"
  - "[[zhu-2026-hab-mappo-target-search]]"
  - "[[wang-2023-differentiated-uav-services]]"
  - "[[differentiated-uav-service-market]]"
created: 2026-05-28
updated: 2026-07-13
---

# Multi-UAV-Assisted Mobile Edge Computing

A class of [[mobile-edge-computing]] architectures where a fleet of UAVs acts as airborne edge servers for ground-level IoT devices. Compared to fixed edge nodes, UAVs offer:

- on-demand coverage (can be re-positioned where load spikes)
- LoS-dominant uplinks at modest altitude (improves channel gain)
- the ability to follow non-stationary user populations

The cost is non-trivial: trajectory planning, energy budget management, recharge scheduling, and coordinated coverage now all become joint optimization decisions. Most prior work — as surveyed in [[liu-2026-jppo-en-convntm]] (Section II) — assumes static or low-mobility users and stops short of [[high-density-mobile-device-scenarios]].

## Decision variables (per time slot)

| Variable | Type | Meaning |
|---|---|---|
| $Q_{u,n}$ | continuous (3-D position) | UAV $u$'s coordinates at time $n$ |
| $\lambda_{u,d,n}$ | continuous in $[0,1]$ | offload ratio from device $d$ to UAV $u$ |
| $\xi_{u,n}$ | discrete $\{0,1\}$ | charging indicator |

These mix [[hybrid-action-decision-making|continuous and discrete actions]], which is what motivates [[j-ppo]] over vanilla [[ppo]].

## Why high density matters

In sparse / low-mobility regimes, a static deployment plus a one-shot offloading rule already achieves near-optimal performance. In dense, mobile regimes:

- demand is bursty and shifts spatially within seconds
- battery becomes a binding constraint because longer flights are needed to follow users
- fairness across the device population is no longer guaranteed by uniform coverage — see [[spatial-equity-index]]

This is the regime that [[liu-2026-jppo-en-convntm]] specifically targets.

[[li-2025-dt-uav-swarm-resource-management]] approaches the multi-UAV setting from task-driven swarm formation: a digital twin admits UAVs into a search-and-rescue swarm only after virtual resource scheduling and delay-bound checks indicate the task requirements can be met.

Recent entries broaden the deployment/offloading axis. [[wang-2025-ppo-uav-positioning-offloading]] uses PPO to jointly position UAV MEC servers and split UE tasks between UAVs and a BS, while [[gao-2026-fmad3qn-uav-gd-association]] combines closed-form device association with federated dueling-DDQN 3D deployment under heterogeneous tasks and no-fly zones. [[zhan-2026-gatd3qn-dependent-offloading]] adds UAV placement plus dependent-task DAG offloading, [[wang-2026-llm-qos-multiuav-resource]] adds LLM-teacher/MAPPO-student resource allocation with inter-UAV task migration and fairness, [[bui-2025-noma-near-far-offloading]] adds near-/far-field NOMA offloading around UAV-mounted arrays, and [[song-2026-thz-multiuav-mec]] uses multiple UAVs as THz communication relays for queue-aware MEC service delay. [[zhao-2026-adaptive-wdc-wet-lae]] extends multi-UAV control to WDC/WET service balancing, [[wang-2026-scalable-multiuav-analytics]] splits video-analytics DAGs across UAVs, and [[zhu-2026-hab-mappo-target-search]] couples 3D search trajectories with image offloading and resource allocation.
