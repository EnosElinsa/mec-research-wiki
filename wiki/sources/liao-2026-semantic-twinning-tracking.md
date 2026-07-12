---
type: source
title: "Goal-Oriented Semantic Twinning-Enabled Collaborative Target Tracking in Communication-Constrained Satellite-UAV Networks"
authors: ["Tianle Liao", "Shaohua Wu", "Yifei Qiu", "Xin Jin", "Qinyu Zhang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3700322"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, semantic-twinning, satellite-uav, collaborative-tracking, digital-twin, semantic-communication, age-of-information, incremental-learning]
related:
  - "[[goal-oriented-semantic-twinning]]"
  - "[[digital-twin]]"
  - "[[semantic-communication]]"
  - "[[age-of-information]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[edge-intelligence]]"
  - "[[maddpg]]"
  - "[[shaohua-wu]]"
  - "[[qinyu-zhang]]"
created: 2026-07-13
updated: 2026-07-13
---

# Goal-Oriented Semantic Twinning-Enabled Collaborative Target Tracking in Communication-Constrained Satellite-UAV Networks

## Citation

Liao, T., Wu, S., Qiu, Y., Jin, X., & Zhang, Q. (2026). *Goal-Oriented Semantic Twinning-Enabled Collaborative Target Tracking in Communication-Constrained Satellite-UAV Networks*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3700322.

## TL;DR

Builds a task-scoped satellite-edge twin for multi-cluster UAV tracking. Stale or missing state is reconstructed with temporal, kinematic, spatial, and causal models; satellite MADDPG policies schedule radio resources and tracking motion, while EWC plus mixed replay adapts to target-motion shifts.

## Problem framing

Full digital-twin synchronization is expensive and fragile over long, lossy satellite-UAV links. Global tracking also needs fresh communication, target fusion, safe cluster motion, and policy adaptation when the target changes behavior. The paper proposes to twin only task-critical state at task-appropriate granularity and infer the rest.

## System model

- Geographically separated UAV clusters track one target without direct inter-cluster links; each cluster leader relays traffic through a continuously covering LEO constellation.
- Satellite edge modules maintain a virtual network graph and tracking environment, fuse UAV observations, generate commands, and train/update policies.
- FDMA within each cluster still permits co-channel interference because there are fewer bands than UAVs.
- State includes motion, queues, processing/radio rates, power, energy, and sensing streams; propulsion energy is excluded.
- Satellite policies control discrete power/frequency choices and cluster acceleration/angular velocity; stale commands trigger a local backup policy.

## Method

[[goal-oriented-semantic-twinning|GOST]] rejects samples older than a threshold and reconstructs missing variables with ARIMA, Kalman/unscented-information filtering, GAT spatial interference inference, or DECI structural-causal inference. Its significance rule frequently samples variables used to infer other variables, while retaining sparse samples of reconstructed variables for validation.

MADDPG trains communication and tracking policies. When reward or target-motion distributions shift, EWC protects important parameters and a mixed replay buffer gradually changes the new-data share from 0.7 toward 0.3 before merging the adapted experience.

## Key findings

- The abstract reports `68%` lower AoI, `75%` lower positioning error, and `50%` lower target loss than a conventional DT under constrained channels. The parse does not provide the aggregation formulas needed to reproduce these headline percentages.
- Incremental learning is reported to use about `66%` of the samples required by online learning after target-motion changes.
- The paper reports MADDPG convergence in 300 episodes, but the corresponding figure axis is time rather than episodes.
- Its Jetson Nano nanosecond/microsecond latency values are analytical FLOP/peak-throughput estimates, not measured execution results.

## Limitations / parse caveats

Evaluation uses two six-UAV clusters in a custom simulation, with no code, trace, simulator, orbit model, run count, or field test. The AoI reward sign appears reversed, the Rician outage expression is incomplete, and discrete actions are not reconciled with deterministic policy gradients. Two-cluster reward logic, stage count, time axes, and CTDE terminology are internally inconsistent; the aggregation behind the headline target-loss percentage is underspecified and cannot be reproduced from the parse. Satellite handover, propulsion, and larger heterogeneous networks are not evaluated.

## Relation to the corpus

This source extends [[digital-twin]] synchronization from transmitting compressed observations to choosing twin scope, inferring omitted state, and preserving task reward under missing updates. It combines [[semantic-communication]], [[age-of-information]], satellite [[edge-intelligence]], and continual policy adaptation rather than classical task-offloading optimization.

## Raw artifacts

- Parse: `raw/sources/Goal-Oriented_Semantic_Twinning-Enabled_Collaborative_Target_Tracking_in_Communication-Constrained_Satellite-UAV_Networks/Goal-Oriented_Semantic_Twinning-Enabled_Collaborative_Target_Tracking_in_Communication-Constrained_Satellite-UAV_Networks.md`
- Origin PDF: `raw/sources/Goal-Oriented_Semantic_Twinning-Enabled_Collaborative_Target_Tracking_in_Communication-Constrained_Satellite-UAV_Networks/Goal-Oriented_Semantic_Twinning-Enabled_Collaborative_Target_Tracking_in_Communication-Constrained_Satellite-UAV_Networks.pdf`
- Figures: `raw/sources/Goal-Oriented_Semantic_Twinning-Enabled_Collaborative_Target_Tracking_in_Communication-Constrained_Satellite-UAV_Networks/images/`
