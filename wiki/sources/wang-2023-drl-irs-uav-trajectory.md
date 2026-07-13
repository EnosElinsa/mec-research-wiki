---
type: source
title: "Joint Trajectory and Passive Beamforming Design for Intelligent Reflecting Surface-Aided UAV Communications: A Deep Reinforcement Learning Approach"
authors: ["Liang Wang", "Kezhi Wang", "Cunhua Pan", "Nauman Aslam"]
year: 2023
url: "https://doi.org/10.1109/TMC.2022.3200998"
venue: "IEEE Transactions on Mobile Computing (TMC)"
tags: [source, intelligent-reflecting-surface, uav-trajectory-control, dqn, ddpg, energy-efficiency]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-trajectory-control]]"
  - "[[deep-q-network]]"
  - "[[ddpg]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[kezhi-wang]]"
  - "[[cunhua-pan]]"
  - "[[nauman-aslam]]"
  - "[[wang-2021-maddpg-multiuav-trajectory]]"
created: 2026-07-13
updated: 2026-07-13
---

# Joint Trajectory and Passive Beamforming Design for Intelligent Reflecting Surface-Aided UAV Communications: A Deep Reinforcement Learning Approach

## Citation

Wang, L., Wang, K., Pan, C., & Aslam, N. (2023). Joint trajectory and passive beamforming design for intelligent reflecting surface-aided UAV communications: A deep reinforcement learning approach. *IEEE Transactions on Mobile Computing, 22*(11), 6543-6553. https://doi.org/10.1109/TMC.2022.3200998

## TL;DR

One rotary-wing UAV tracks a moving UE through one selected building-mounted IRS per slot. DQN or DDPG controls 3-D UAV displacement, while a nearest-IRS rule selects the surface and a closed-form phase-alignment rule sets its reflecting elements.

## Problem and system model

The direct UAV-UE path is excluded. IRS coordinates and UE motion are known, only the IRS nearest the UE is active, and other surfaces sleep. The objective sums each slot's achievable rate divided by UAV propulsion energy over the horizon; it is not one total-rate/total-energy ratio.

State includes UAV/UE/IRS coordinates, slot index, and remaining UAV energy. The displayed optimization has motion, area/altitude, and unit-modulus bounds but no explicit terminal battery-feasibility constraint.

## Method

[[deep-q-network|DQN]] chooses discrete signed axis moves or no movement; DDPG emits continuous 3-D displacement. Reward is per-slot rate/propulsion-energy minus an out-of-bounds penalty. Given geometry, analytical phase alignment coherently combines the selected IRS elements.

The DRL component controls trajectory only: IRS selection is deterministic and passive phases are solved analytically. Neither DQN nor DDPG has a convergence or global-optimality guarantee here.

## Key findings

- DDPG reports higher reward and energy efficiency than DQN, while DQN trains faster in the hardware-dependent comparison.
- Figure text reports DDPG energy efficiency increasing from roughly **52 to 70 bps/J** as reflecting-element count rises.
- Both learned trajectories outperform fixed-motion/fixed-phase and random-motion/random-phase baselines in the displayed simulation.

## Limitations

The model has one UAV and one predictably moving UE, fixed known IRSs, no direct link, ideal continuous phases, deterministic geometry, and perfect state information. It omits CSI uncertainty, phase quantization, switching/control energy, signaling overhead, multiple users, and collision/safety constraints. Evidence is simulation-only, and training-time comparisons are implementation-specific.

## Relation to the corpus

This early DRL/IRS source separates learned motion from deterministic IRS selection and phase alignment. It complements [[wang-2021-maddpg-multiuav-trajectory]] from the same author group and later joint aerial-RIS controllers that include more IRS variables in the learned action space.

## Raw artifacts

- Parse: `raw/sources/Joint_Trajectory_and_Passive_Beamforming_Design_for_Intelligent_Reflecting_Surface-Aided_UAV_Communications_A_Deep_Reinforcement_Learning_Approach/Joint_Trajectory_and_Passive_Beamforming_Design_for_Intelligent_Reflecting_Surface-Aided_UAV_Communications_A_Deep_Reinforcement_Learning_Approach.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
