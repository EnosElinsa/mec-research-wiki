---
type: source
title: "HAP-UAV-Assisted Hierarchical Aerial Computing Framework for Video Offloading: A Deep Reinforcement Learning Approach"
authors: ["Yifei Bao", "Jinghui Zhang", "Yi Cheng", "Dengyin Zhang", "Rongguo Fu"]
year: 2025
url: ""
venue: "Journal of Supercomputing / Cluster Computing (Springer; preprint, accepted Sep 2025)"
tags: [hap, uav, video-offloading, video-transcoding, ddpg, qoe, post-disaster, hierarchical-aerial-mec]
related:
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[ddpg]]"
  - "[[video-analytics-offloading]]"
  - "[[video-transcoding-tradeoff]]"
  - "[[qoe-modeling-mec]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
created: 2026-05-29
updated: 2026-05-29
---

# HAP-UAV-Assisted Hierarchical Aerial Computing Framework for Video Offloading: A Deep Reinforcement Learning Approach

## Citation

Bao, Y., Zhang, J., Cheng, Y., Zhang, D., & Fu, R. (2025). *HAP-UAV-Assisted Hierarchical Aerial Computing Framework for Video Offloading: A Deep Reinforcement Learning Approach*. (Accepted Sep 2025; published online Oct 2025.)

## TL;DR

A post-disaster scenario where ground camera equipments (CEs) feed video to nearby UAVs, and UAVs split each video chunk between local DNN inference and offloading to a HAPS for inference. Because the UAV → HAPS link is bandwidth-limited at tens of kilometers altitude, **video must be transcoded to a lower bitrate** before offloading — but lower bitrate degrades inference accuracy. The system jointly optimizes:

- offloading ratio η_u(i) ∈ [0,1] per UAV,
- transcoding indicator ε_u(i) ∈ {0,1} and ratio ε_u(i) ∈ [ε_min, 1),
- HAP computation resource allocation φ_u(i) per UAV.

The objective is a **QoE function** combining task delay (transmission + computation) with the average video bitrate after transcoding (proxy for inference accuracy). Solved as an MDP with **DDPG** for continuous control.

## Why this matters

This is the wiki's first **video-analytics workload** entry. Earlier offloading sources treat tasks as opaque (input-bytes, CPU-cycles, deadline). This paper introduces:

1. **Workload-aware compression.** The data being offloaded is *lossy-compressible*, and compression directly affects the downstream model's accuracy. None of [[liu-2026-jppo-en-convntm]], [[peng-2025-drudm-cfg]], [[zhu-2025-lycnn-drl-wpt-mec]] etc. have this knob.
2. **Three-way tradeoff.** Delay, video quality, and compute resources — not just delay vs energy. The QoE function explicitly bakes the bitrate-accuracy curve into the reward.
3. **Vanilla DDPG suffices.** Continuous offloading + transcoding ratios are pure continuous actions; DDPG fits cleanly. No need for the hybrid-action machinery of [[liu-2026-jppo-en-convntm|j-PPO]] or [[ma-2025-pdqn-vehicular-mec|P-DQN]].

## Method

- **State.** Per-round per-UAV: collected video volume D_u(i), UAV-HAP channel gain proxy, residual energy.
- **Action.** {η_u(i), ε_u(i), ε̄_u(i), φ_u(i)} per UAV.
- **Reward.** −(α·delay + β·(1 − transcoded_bitrate / original_bitrate)) — small Greek-letter weights tune the tradeoff.
- **Algorithm.** DDPG with target networks; OU-noise exploration.

## Findings

- Adaptive transcoding **dominates** fixed-rate transmission. Rather than transcoding everything to a fixed low bitrate, the policy raises bitrate when the channel is good and the offloaded fraction is small.
- DDPG converges faster than PPO baselines on this problem, attributed to the deterministic policy and replay buffer.
- The QoE-shaped reward avoids the "always offload" failure mode that pure-delay rewards trigger when compute on the HAP is cheap.

## Limitations

- Single HAP, fixed UAV trajectories — no joint trajectory + offloading optimization.
- The bitrate→accuracy curve is fitted offline; in real disaster scenes the curve shifts with content (e.g. low-light, smoke). No online adaptation.
- DNN inference cost ζ·(ε·η·D)^ξ is empirical; the exponent ξ may not generalize across model families.
- Simulation only; no field trial in actual disaster conditions.

## Cross-link with related sources

- **Video-analytics workload class:** new for the wiki. Distinct from the *cooperative perception* workload in [[xie-2026-uav-multisource-fusion]] (which fuses raw observations, not bitrate-controlled video).
- **Hierarchical UAV+HAP MEC:** alongside [[peng-2025-drudm-cfg]], [[nabi-2025-jour-hierarchical-aerial]], [[wang-2026-aerial-marine-msar]], [[jia-2025-dro-uav-hap-mec]].
- **Solver:** vanilla DDPG, comparison-relevant to [[ddpg-vs-jppo]].

## Raw artifacts

- `raw/sources/HAP-UAV-assisted hierarchical aerial computing framework for video offloading a deep reinforcement/full.md`
