---
type: source
title: "Energy-Efficient Joint Localization and Communication via Air-Ground Collaboration in UAV-Assisted Emergency Systems"
authors: ["Zeyu Tian", "Lianming Xu", "Chen Xu", "Zheng Chang", "Li Wang", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3656750"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 11998-12015"
tags: [source, emergency-network, joint-localization-communication, aoa-localization, cooperative-beamforming, ddqn, energy-efficiency, uav-trajectory]
related:
  - "[[joint-localization-and-communication]]"
  - "[[post-disaster-mec]]"
  - "[[air-ground-integrated-network]]"
  - "[[ddqn]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[collaborative-beamforming]]"
  - "[[zhu-han]]"
  - "[[zheng-chang]]"
  - "[[zhao-2019-uav-emergency-disasters]]"
created: 2026-07-13
updated: 2026-07-13
---

# Energy-Efficient Joint Localization and Communication via Air-Ground Collaboration in UAV-Assisted Emergency Systems

## Citation

Tian, Z., Xu, L., Xu, C., Chang, Z., Wang, L., & Han, Z. (2026). *Energy-Efficient Joint Localization and Communication via Air-Ground Collaboration in UAV-Assisted Emergency Systems*. **IEEE Transactions on Wireless Communications**, 25, 11998-12015. DOI: 10.1109/TWC.2026.3656750.

## TL;DR

Pairs one collaborative UAV with one ground rescuer to localize a person from four AOA measurements and then steer two-node CoMP downlink beams toward that estimate. SYNCORE uses DDQN to adjust UAV position, movement time, and UAV/rescuer powers against a normalized communication-localization-energy objective.

## Problem

Disasters can remove terrestrial anchors and limit both aircraft count and energy. Communication-only optimization leaves poor localization geometry, while localization-only motion can waste energy and weaken data delivery. The paper asks whether one UAV and one rescuer can use localization feedback to improve communication and vice versa.

## System model

- One collaborative UAV (CU) and one ground rescuer (RC), each with a planar array, serve one person to be rescued (PR).
- Every slot carries communication and embeds a localization phase. The PR sends a distress signal; CU and RC estimate azimuth/elevation angles, update the PR position, and form cooperative downlink beams.
- The CU-PR and CU-RC links are treated as LoS-dominant; the ground PR-RC link is Rician. AOA errors are modeled as independent equal-variance Gaussian terms.
- Energy includes CU/RC radio transmission plus rotary-wing movement and hovering.

## Method

Shifted UPA subarrays and ESPRIT estimate four AOA components; least squares recovers PR coordinates. Geometry-derived steering vectors form the CU/RC beams. The DDQN-based SYNCORE state contains CU location, estimated PR location, and angles; discrete actions control horizontal/vertical movement, movement time, and transmit powers. The next localization and communication outcome supplies the energy-efficiency reward.

## Key findings

- A learning rate of `0.005` and batch size `64` yield empirical convergence near 500 episodes with stable reward around 230 in the reported hyperparameter study.
- Increasing localization error from `0.18 m` to `1 m` reduces received communication data by `54 Mbits`; increasing it from `1.7 m` to `3.1 m` reduces data by `431 Mbits`, showing nonlinear beamforming sensitivity.
- Walking-speed tests use `0.8` and `1.2 m/s`; a `3.3 m/s` running case lowers communication volume and raises positioning error.
- The paper's headline `43%` energy-efficiency improvement has no named baseline or operating point in the prose, so it is retained as a caveat rather than a comparative result here.

## Limitations / parse caveats

The evaluation is simulation-only and models one CU, one rescuer, and one user. It assumes a stable CU-RC LoS link, a detectable dominant component for ESPRIT, quasi-static slots, and idealized angle-error statistics. Strong wind, multi-user association, contention, and detailed sensing/computation energy are deferred or absent. The parse damages rate and reward equations, constraint labels, beamformer normalization, and algorithm text; its localization CDF sentence says `above 0.6 m` although the CDF orientation indicates `at or below`. No confidence intervals or run counts are reported.

## Relation to the corpus

This source adds [[joint-localization-and-communication]] to the emergency-network branch represented by [[zhao-2019-uav-emergency-disasters]]. It is adjacent to [[integrated-sensing-and-communication]], but uses a distress-signal AOA pipeline plus a communication beam rather than a shared radar/communication waveform.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient_Joint_Localization_and_Communication_via_Air-Ground_Collaboration_in_UAV-Assisted_Emergency_Systems/Energy-Efficient_Joint_Localization_and_Communication_via_Air-Ground_Collaboration_in_UAV-Assisted_Emergency_Systems.md`
- Origin PDF: `raw/sources/Energy-Efficient_Joint_Localization_and_Communication_via_Air-Ground_Collaboration_in_UAV-Assisted_Emergency_Systems/Energy-Efficient_Joint_Localization_and_Communication_via_Air-Ground_Collaboration_in_UAV-Assisted_Emergency_Systems.pdf`
- Figures: `raw/sources/Energy-Efficient_Joint_Localization_and_Communication_via_Air-Ground_Collaboration_in_UAV-Assisted_Emergency_Systems/images/`
