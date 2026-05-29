---
type: source
title: "Resource Allocation and Trajectory Design for MISO UAV-Assisted MEC Networks"
authors: ["Boyang Liu", "Yiyao Wan", "Fuhui Zhou", "Qihui Wu", "Rose Qingyang Hu"]
year: 2022
url: "https://doi.org/10.1109/TVT.2022.3140833"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, uav-mec, miso, beamforming, trajectory-design, energy-minimization, sca]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[qcqp-sdr-probabilistic-mapping]]"
  - "[[energy-latency-tradeoff]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
created: 2026-05-29
updated: 2026-05-29
---

# Resource Allocation and Trajectory Design for MISO UAV-Assisted MEC Networks

## Citation

Liu, B., Wan, Y., Zhou, F., Wu, Q., & Hu, R. Q. (2022). *Resource Allocation and Trajectory Design for MISO UAV-Assisted MEC Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2022.3140833.

## TL;DR

A **multiple-input single-output (MISO)** UAV-assisted MEC network that uses UAV beamforming to overcome poor channel quality from multipath/blockages. The paper minimizes system energy consumption by jointly optimizing the UAV's beamforming vectors, UAV CPU frequency, UAV trajectory, UE transmit power, and UE CPU frequency, via a **three-stage iterative algorithm** with closed-form expressions derived for the optimal UAV CPU frequency and UE transmit power.

## Problem framing

Traditional MEC suffers poor channel quality from multipath and blockages. Equipping the UAV with multiple antennas (MISO) and beamforming improves links, but the joint beamforming + frequency + trajectory + power design is non-convex.

## System model

- **Actors.** A MISO UAV (multiple antennas) serving single-antenna UEs.
- **Objective.** Minimize system energy consumption.
- **Variables.** UAV beamforming vectors, UAV CPU frequency, UAV trajectory, UE transmit power, UE CPU frequency, under task/trajectory/computation constraints.

## Method

- A **three-stage alternating algorithm**; closed-form expressions derived for optimal UAV CPU frequency and UE transmit power. The beamforming sub-problem uses semidefinite-relaxation-style convexification (rank-one constraint dropped, strong duality) ([[alternating-optimization-sdr-sca]], [[qcqp-sdr-probabilistic-mapping]]).

## Key findings

- The derived results show the UE offloading decision is determined by the UAV–UE CSI; simulations show superiority over benchmarks in energy consumption, especially for computation-intensive tasks, with guaranteed convergence (qualitative; specific curves in the paper).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work beyond the established design.

## Relation to the corpus

A **MISO/beamforming** twist on the optimization-based single-UAV MEC formulation shared with [[zhang-2019-uav-iot-comp-comm]] and [[yu-2020-uav-ec-collaborative-offloading]]; the explicit CSI-driven offloading-decision result connects to the CSI-uncertainty thread ([[jia-2025-dro-uav-hap-mec]], [[wu-2026-terrain-aware-uav-mec]]). Reinforces [[alternating-optimization-sdr-sca]] and [[uav-trajectory-control]]. Shares co-author Qihui Wu with several aerial sources.

## Raw artifacts

- `raw/sources/Resource_Allocation_and_Trajectory_Design_for_MISO_UAV-Assisted_MEC_Networks/full.md`
- Original PDF and extracted figures in the same folder.
