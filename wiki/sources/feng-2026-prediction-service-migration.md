---
type: source
title: "Prediction-Assisted Multi-UAV Online Service Migration and Trajectory Control for MEC-Empowered Vehicular Networks"
authors: ["Wei Feng", "Wenyang Gao", "Jianping Yao", "Longyu Zhou", "Chenggang Yan", "Tony Q. S. Quek"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3700894"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicular-mec, service-migration, trajectory-prediction, lyapunov-optimization, maddpg, uav-trajectory-control]
related:
  - "[[service-migration]]"
  - "[[task-migration]]"
  - "[[vehicular-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[maddpg]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-07
updated: 2026-07-07
---

# Prediction-Assisted Multi-UAV Online Service Migration and Trajectory Control for MEC-Empowered Vehicular Networks

## Citation

Feng, W., Gao, W., Yao, J., Zhou, L., Yan, C., & Quek, T. Q. S. (2026). *Prediction-Assisted Multi-UAV Online Service Migration and Trajectory Control for MEC-Empowered Vehicular Networks*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3700894. DOI/venue/year are parse-silent at the top level and verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Combines short-term vehicle-trajectory prediction, [[lyapunov-optimization]], and [[maddpg]] for online service migration in UAV-assisted vehicular MEC. A stacked LSTM predicts where vehicles will move, Lyapunov queues enforce a long-term migration-cost budget, and cooperative UAV agents jointly control service migration and UAV trajectories to reduce latency.

## Problem

In vehicular MEC, the UAV closest to a vehicle may change frequently. Migrating a service instance too often wastes bandwidth and causes migration delay, but not migrating can force tasks through multi-hop UAV backhaul to a distant serving UAV. The paper targets long-term average latency minimization subject to migration-cost constraints under mobile users and partial observability.

## System model

Multiple UAVs act as MEC servers over urban vehicular hotspots. Each ground user generates one task at the start of each slot. The local UAV provides the current access link, while the serving UAV holds the task service instance and performs computation. If those UAVs differ, task traffic is relayed over multi-hop UAV backhaul. Service migration transfers both task state and the MEC service instance to a more suitable UAV.

## Method

The framework first uses a stacked LSTM to predict short-term vehicle trajectories from historical movement, reducing avoidable cross-UAV migrations. It then constructs a Lyapunov virtual queue for migration cost and derives a per-slot control problem. The online decision process is cast as a cooperative Markov game, where UAV agents use MADDPG with centralized training and decentralized execution to choose trajectory and migration actions.

## Key findings

- The LSTM predictor reports average trajectory error around 2 m, which the paper treats as negligible relative to UAV communication coverage.
- The proposed method reaches the highest reward and lowest latency among compared baselines in the reported convergence curves; reward and latency stabilize around 220 iterations.
- Removing LSTM prediction slows convergence and yields lower reward and higher latency, supporting the paper's prediction-assisted migration argument.
- As task input size or user count grows, the proposed method is reported to keep higher reward and lower latency than DQN, Greedy, MAPPO, and no-LSTM variants.

## Limitations / future work

The conclusion states future work will extend the framework to heterogeneous multi-access edge computing with ground infrastructure, explore decentralized learning under partial observability, and integrate energy-aware constraints.

## Relation to the corpus

This source extends [[service-migration]] and [[task-migration]] from edge-server handoff into a multi-UAV vehicular setting where prediction reduces unnecessary migrations. It complements [[zhang-2025-mcma-task-migration]], which also uses trajectory prediction, and [[zhao-2025-traj-offload-cache-migration]], where [[lyapunov-optimization]] coordinates long-term migration/caching decisions.

## Raw artifacts

- `raw/sources/Prediction-Assisted Multi-UAV Online Service Migration and Trajectory Control for MEC-Empowered Vehicular Networks/Prediction-Assisted Multi-UAV Online Service Migration and Trajectory Control for MEC-Empowered Vehicular Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
