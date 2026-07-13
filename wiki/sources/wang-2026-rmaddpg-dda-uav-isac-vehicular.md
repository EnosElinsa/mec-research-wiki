---
type: source
title: "A Novel Integrated Sensing and Communication Scheme in UAVs-Enabled Vehicular Networks With MARL-Driven Adaptive Control"
authors: ["Ziyuan Wang", "Xiao-Ping Zhang", "Wenbo Ding", "Yuhan Dong", "Xinlei Chen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3591259"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-isac, vehicular-networks, marl, maddpg, random-network-distillation, multi-objective-optimization, crlb]
related:
  - "[[rmaddpg-dda-uav-isac-control]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-enabled-its]]"
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[cramer-rao-bound]]"
  - "[[li-2026-control-based-uav-isac]]"
  - "[[cui-2026-aris-v2x-icac]]"
  - "[[xinlei-chen]]"
  - "[[radar-mutual-information-rate]]"
created: 2026-07-10
updated: 2026-07-14
---

# A Novel Integrated Sensing and Communication Scheme in UAVs-Enabled Vehicular Networks With MARL-Driven Adaptive Control

## Citation

Wang, Z., Zhang, X.-P., Ding, W., Dong, Y., & Chen, X. (2026). *A Novel Integrated Sensing and Communication Scheme in UAVs-Enabled Vehicular Networks With MARL-Driven Adaptive Control*. **IEEE Transactions on Mobile Computing (IEEE TMC)**, 25(1), 132-147. DOI: 10.1109/TMC.2025.3591259.

## TL;DR

Designs RMADDPG-DDA, a MARL controller for UAV-enabled vehicular ISAC. Multiple UAVs jointly adapt channel allocation, motion, yaw, communication power, and ISAC transmit power to increase served vehicles and radar mutual information while respecting upload, QoS, energy, and collision constraints.

## Problem

The paper argues that many UAV-enabled ISAC designs are too static for vehicular networks: they treat sensing and communication separately, reuse hardware but not signals, rely on time division or stored uploads, or omit collision and energy constraints. Dynamic vehicle mobility turns the joint sensing/communication control into a distributed, stochastic, multi-objective problem.

## System model

- A cluster of UAVs serves moving vehicles in an urban crossroad scenario.
- Each UAV has a directional antenna for ISAC transmission/echo reception and an omnidirectional antenna for real-time upload to the base station.
- Vehicles move on two-way lanes; UAVs fly at fixed height with velocity and yaw control.
- The model includes propulsion, communication, and sensing energy; FDMA UAV-BS upload over communication bandwidth; non-overlapping ISAC bandwidth; LoS ISAC links; communication SNR; echo SNR; CRLB-derived sensing quality; radar mutual information; Jain-style sensing fairness; and effective mutual information.
- The optimization variables include channel allocation, motion, yaw, communication power, and ISAC transmit power.

## Method

The authors cast the non-convex stochastic control problem as MARL with weighted rewards for effective mutual information, served users, and energy saving. Penalties enforce communication-SNR, upload-capacity, and collision constraints.

RMADDPG-DDA augments MADDPG with:

- centralized training and decentralized execution;
- random-network-distillation novelty rewards for sparse-reward exploration;
- parameter sharing among UAV agents;
- dynamic data augmentation by permuting UAV and user identifiers.

The parsed baselines are MADDPG, DDPG, and MASAC.

## Key findings

- The simulation setup includes `M = 40` vehicles, `N = 4` UAVs initially, `T = 150 s`, `Delta t = 1 s`, a base station at `[140 m, 140 m]`, UAV height `80 m`, communication bandwidth `B_c = 5 MHz`, ISAC bandwidth `B_s = 0.1 MHz`, and a `3 GHz` carrier.
- Across 10 parallel tests, RMADDPG-DDA improves average served users by 34.01% over MADDPG, 44.37% over DDPG, and 16.71% over MASAC.
- It improves average effective mutual information by 68.26% over MADDPG, 96.74% over DDPG, and 114.66% over MASAC.
- The constraint tests cover communication SNR margin, upload-capacity margin, and minimum UAV distance; the parsed text states that the constraints are satisfied.
- Increasing the number of UAVs improves served users and effective mutual information but tightens space and communication constraints.
- Raising the energy weight reduces energy consumption with performance tradeoffs; the parse identifies a favorable local point near `omega_3 = 0.5`.

## Limitations / future work

The local parse is silent on DOI, venue, and year; the bibliographic metadata above is title-matched DOI metadata. The parse contains OCR and formula artifacts: the study-area `L_y` value is missing, and the safe-distance formula appears inconsistent with the textual "not less than" condition. The reported evidence is simulation-based; no real-world deployment or code availability is present in the parse. The explicit future-work direction is to address the single-antenna sensing limitation by combining MIMO with UAV networking.

## Relation to the corpus

This source strengthens the corpus's sensing-aware vehicular-control track. It is close to [[li-2026-control-based-uav-isac]], which also couples UAV motion with ISAC metrics, but Wang et al. focus on distributed MARL control in a moving-vehicle scenario. It also sits near [[cui-2026-aris-v2x-icac]] as a V2X/vehicular counterpart, with [[rmaddpg-dda-uav-isac-control]] capturing its particular MADDPG + exploration + augmentation pattern.

## Raw artifacts

- Parse: `raw/sources/A_Novel_Integrated_Sensing_and_Communication_Scheme_in_UAVs-Enabled_Vehicular_Networks_With_MARL-Driven_Adaptive_Control/A_Novel_Integrated_Sensing_and_Communication_Scheme_in_UAVs-Enabled_Vehicular_Networks_With_MARL-Driven_Adaptive_Control.md`
- Origin PDF: `raw/sources/A_Novel_Integrated_Sensing_and_Communication_Scheme_in_UAVs-Enabled_Vehicular_Networks_With_MARL-Driven_Adaptive_Control/A_Novel_Integrated_Sensing_and_Communication_Scheme_in_UAVs-Enabled_Vehicular_Networks_With_MARL-Driven_Adaptive_Control.pdf`
- Figures: `raw/sources/A_Novel_Integrated_Sensing_and_Communication_Scheme_in_UAVs-Enabled_Vehicular_Networks_With_MARL-Driven_Adaptive_Control/images/`
