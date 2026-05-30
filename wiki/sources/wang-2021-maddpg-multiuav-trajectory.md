---
type: source
title: "Multi-Agent Deep Reinforcement Learning-Based Trajectory Planning for Multi-UAV Assisted Mobile Edge Computing"
authors: ["Liang Wang", "Kezhi Wang", "Cunhua Pan", "Wei Xu", "Nauman Aslam", "Lajos Hanzo"]
year: 2021
url: "https://doi.org/10.1109/TCCN.2020.3027695"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
tags: [source, multi-uav-assisted-mec, multi-agent-drl, maddpg, trajectory-design, fairness-metrics, energy-latency-tradeoff, uav-trajectory-control]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[maddpg]]"
  - "[[uav-trajectory-control]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[jains-fairness-index]]"
  - "[[wang-2022-cat-rat-fmec-trajectory]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
created: 2026-05-31
updated: 2026-05-31
---

# Multi-Agent Deep Reinforcement Learning-Based Trajectory Planning for Multi-UAV Assisted Mobile Edge Computing

## Citation

Wang, L., Wang, K., Pan, C., Xu, W., Aslam, N., & Hanzo, L. (2021). *Multi-Agent Deep Reinforcement Learning-Based Trajectory Planning for Multi-UAV Assisted Mobile Edge Computing*. **IEEE Transactions on Cognitive Communications and Networking**. DOI: 10.1109/TCCN.2020.3027695. (Manuscript received April 18, 2020; date of publication September 29, 2020; date of current version March 8, 2021 → year 2021.)

## TL;DR

A multi-UAV-aided MEC framework where several UAVs with distinct trajectories fly over a target area to serve ground UEs. The paper **jointly optimizes geographical fairness among UEs, fairness of each UAV's UE-load, and overall UE energy consumption** — a mixed integer/continuous problem. A **multi-agent DRL** trajectory-control algorithm (one agent per UAV) using **MADDPG** manages each UAV's trajectory independently; given the trajectories, a **low-complexity approach** then sets UE offloading decisions. It reports advantages over traditional algorithms in UE-serving fairness, UE-load fairness, and energy consumption.

## Problem framing

UAVs as flexible aerial servers can establish LoS links and adapt position to dynamic environments. The objective explicitly combines two fairness notions — **geographical fairness** over served UEs and **UE-load fairness** across UAVs — with **UE energy minimization**, producing a high-dimensional mixed-variable problem unsuited to exhaustive/conventional methods. A decentralized, per-UAV agent design is motivated by the curse of dimensionality.

## System model

- **Actors.** Multiple UAVs (one DRL agent each) serving ground UEs.
- **Objective.** Jointly maximize geographical fairness of served UEs and UAV UE-load fairness while minimizing total UE energy consumption.
- **Variables.** Integer (e.g., associations/offloading) plus continuous (trajectory) variables.

## Method

- **MADDPG**-based trajectory-control algorithm: each UAV is controlled by a dedicated agent, trained under CTDE ([[centralized-training-decentralized-execution]]), building on the DQN→Double-DQN→DDPG lineage the parse reviews.
- **Low-complexity offloading step.** Given fixed UAV trajectories, a separate low-complexity approach optimizes UE offloading decisions (a trajectory-then-offloading decomposition).

## Key findings

- The proposed solution achieves "considerable performance over other traditional algorithms" on all three axes — UE-serving fairness, per-UAV UE-load fairness, and total UE energy (stated qualitatively in the parse; specific curves in the figures, not asserted here as exact).

## Limitations / future work

No explicit quantitative future-work targets are grounded in the captured parse → `not in parse`.

## Relation to the corpus

A **MADDPG multi-UAV trajectory** entry by the Northumbria/QMUL/Southeast group ([[kezhi-wang]] corresponding). It is the **same research group** as [[wang-2022-cat-rat-fmec-trajectory]] (CAT/RAT, single twin-DQN agent) but is a **distinct earlier paper** — different venue (TCCN vs TMC), different DOI, a *multi-agent* MADDPG design, and an explicit **dual-fairness + energy** objective rather than pure energy minimization. Its dual fairness formulation links it to the [[fairness-metrics-in-mec]] hub and [[jains-fairness-index]], and it sits with [[he-2023-fairness-3d-multiuav-maddpg]] and [[seid-2021-madrl-multiuav-iot-edge]] in the MADDPG multi-UAV family.

## Raw artifacts

- `raw/sources/Multi-Agent_Deep_Reinforcement_Learning-Based_Trajectory_Planning_for_Multi-UAV_Assisted_Mobile_Edge_Computing/full.md`
- Original PDF (`e5d7b673-bd11-43f2-8872-4ceddac8e9b5_origin.pdf`) and extracted figures (`images/`) in the same folder.
