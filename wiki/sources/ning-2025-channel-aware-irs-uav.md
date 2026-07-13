---
type: source
title: "Channel-Aware User Association and Trajectory Design for Multi-IRS Assisted Multi-UAV Communications"
authors: ["Zhaolong Ning", "Hao Hu", "Xiaojie Wang", "Yan Zhang"]
year: 2025
url: ""
venue: ""
tags: [source, intelligent-reflecting-surface, multi-uav, mappo, noma, uav-trajectory-control, blockage]
related:
  - "[[dynamic-irs-user-association]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[mappo]]"
  - "[[noma]]"
  - "[[uav-trajectory-control]]"
  - "[[blockage-aware-channel-model]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[ning-2023-madrl-uav-trajectory-differentiated-services]]"
  - "[[zhaolong-ning]]"
  - "[[xiaojie-wang]]"
  - "[[hu-2026-segmented-irs-cpn]]"
created: 2026-07-12
updated: 2026-07-13
---

# Channel-Aware User Association and Trajectory Design for Multi-IRS Assisted Multi-UAV Communications

## Citation

Ning, Z., Hu, H., Wang, X., & Zhang, Y. (2025). *Channel-Aware User Association and Trajectory Design for Multi-IRS Assisted Multi-UAV Communications*. DOI / venue: **not in parse**. The parse reports publication on 9 December 2025.

## TL;DR

Studies a multi-IRS, multi-UAV NOMA downlink where urban obstacles switch direct UAV-user links between LoS and blocked states. The MGBA scheme combines phase-aligned IRS control, geometric LoS judgment, MAPPO for UAV trajectories and dynamic IRS-user association, and SCA for transmit-power allocation to maximize average system sum rate.

## Problem

Many IRS-assisted UAV designs assume one propagation state, restrict each IRS to one user, or optimize association separately from UAV motion. Here, IRS partitioning, user association, channel state, phase shifts, trajectories, and powers are coupled, while a centralized discrete action space grows rapidly with the UAV count.

## System model

- A slotted 3-D network contains `K` UAVs, `I` building-mounted IRSs, and `N` ground users.
- Each IRS can be partitioned among multiple users, and the association changes with UAV positions.
- A geometric obstacle test selects direct LoS availability; IRS-reflected paths provide virtual-LoS support for blocked users.
- Each UAV serves two users through NOMA with SIC ordering.
- The objective maximizes time-average system sum rate subject to IRS capacity and association, motion, minimum-rate, collision-distance, power, and SIC constraints.

## Method

MGBA derives phase-alignment rules for the IRS-assisted composite channel, performs real-time geometric LoS judgment, and formulates the control problem as a Dec-POMDP. Homogeneous MAPPO agents share actor parameters under centralized training and local execution; each UAV jointly selects a cardinal movement and IRS-user association. Given those decisions, SCA and first-order Taylor bounds produce a convex transmit-power subproblem solved with CVX.

## Key findings

- Simulations use a `500 m x 500 m` Manhattan-style area, two IRSs, UAV speeds up to 20 m/s, transmit powers 15-35 dBm, IRS dimensions from `50 x 50` to `250 x 250`, two to five UAVs, noise -80 dBm, IRS amplitude loss 0.9, and batch size 800.
- With two UAVs and four users, MGBA converges at 230 episodes; RUS, RPS, QMIX, and MGBA-T converge at 180, 220, 250, and 180 episodes. MADDPG and MATD3 do not converge after their continuous actions are discretized in this environment.
- Increasing IRS dimensions from `50 x 50` to `250 x 250` improves average sum rate by 6.52 bit/s/Hz. At `250 x 250`, MGBA exceeds RPS, RUS, QMIX, and MGBA-T by 29.33%, 22.70%, 25.72%, and 17.94%.
- Raising power from 15 to 35 dBm improves average sum rate by 4.91 bit/s/Hz. At 35 dBm, MGBA exceeds RPS, RUS, and QMIX by 44.06%, 27.29%, and 45.35%.
- Moving from three to four UAVs reduces energy efficiency by 2.91% while improving sum rate by 29.49%; moving from four to five reduces energy efficiency by 16.01% for a 5.05% sum-rate gain. The paper selects four UAVs as the tested balance point.
- Increasing IRS count from two to three improves energy efficiency by 34.99%. In the two-UAV/two-IRS comparison, adding an IRS yields 9.95% more energy-efficiency improvement than adding a UAV.

## Limitations / parse caveats

The evidence is simulation plus analytical derivation, not field validation. The model assumes perfect CSI and UAV positions, uses fixed UAV speed and four cardinal movement choices, and omits the NLoS scattering component from the final composite-channel calculation. The parse contains inconsistent learning-rate statements (`0.0004` in the table versus `5 x 10^-4` in prose) and an unassignable fourth percentage in one three-UAV comparison; this page does not resolve those inconsistencies.

## Relation to the corpus

This source extends [[intelligent-reflecting-surface]] through [[dynamic-irs-user-association]]: one IRS can be partitioned across users while association changes with UAV motion and blockage. It adds a MAPPO/CTDE communication-control case adjacent to [[ning-2023-madrl-uav-trajectory-differentiated-services]], but it optimizes communication sum rate rather than MEC service cost.

## Raw artifacts

- Parse: `raw/sources/Channel-Aware_User_Association_and_Trajectory_Design_for_Multi-IRS_Assisted_Multi-UAV_Communications/Channel-Aware_User_Association_and_Trajectory_Design_for_Multi-IRS_Assisted_Multi-UAV_Communications.md`
- Origin PDF: `raw/sources/Channel-Aware_User_Association_and_Trajectory_Design_for_Multi-IRS_Assisted_Multi-UAV_Communications/Channel-Aware_User_Association_and_Trajectory_Design_for_Multi-IRS_Assisted_Multi-UAV_Communications.pdf`
- Figures: `raw/sources/Channel-Aware_User_Association_and_Trajectory_Design_for_Multi-IRS_Assisted_Multi-UAV_Communications/images/`
