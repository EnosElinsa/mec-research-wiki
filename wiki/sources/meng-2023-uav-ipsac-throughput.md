---
type: source
title: "Throughput Maximization for UAV-Enabled Integrated Periodic Sensing and Communication"
authors: ["Kaitao Meng", "Qingqing Wu", "Shaodan Ma", "Wen Chen", "Kunlun Wang", "Jun Li"]
year: 2023
url: "https://doi.org/10.1109/TWC.2022.3197623"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 22, no. 1, pp. 671-687"
tags: [source, uav, integrated-sensing-and-communication, periodic-sensing, beamforming, user-association, trajectory-optimization]
related:
  - "[[integrated-periodic-sensing-and-communication]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[uav-trajectory-control]]"
  - "[[device-association]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[meng-2026-uav-isac-corrections]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[kaitao-meng]]"
  - "[[qingqing-wu]]"
created: 2026-07-14
updated: 2026-07-14
---

# Throughput Maximization for UAV-Enabled Integrated Periodic Sensing and Communication

## Citation

Meng, K., Wu, Q., Ma, S., Chen, W., Wang, K., & Li, J. (2023). *Throughput Maximization for UAV-Enabled Integrated Periodic Sensing and Communication*. **IEEE Transactions on Wireless Communications, 22**(1), 671-687. DOI: 10.1109/TWC.2022.3197623.

## TL;DR

Introduces [[integrated-periodic-sensing-and-communication|IPSAC]], where a UAV communicates in every slot but schedules each target exactly once per sensing frame. A two-layer penalty/AO/SCA method jointly controls user association, target-sensing slots, beamforming, and trajectory to raise sum rate subject to sensing-frequency and beampattern constraints.

## Problem and system model

- One constant-altitude UAV with a uniform planar array serves single-antenna ground users through TDMA and senses known ground targets over a slotted mission.
- Each equal-length ISAC frame must sense every target exactly once, and at most one target and one user are selected per slot. The same information-bearing signal supports communication and sensing.
- The model assumes known user/target positions, LoS free-space channels, compensated Doppler, fixed endpoints, a maximum UAV displacement, per-slot transmit power, per-user frame-rate requirements, and target beampattern-gain thresholds.
- The mixed-integer non-convex objective is average sum achievable rate over beamformers, binary user/target schedules, and UAV trajectory.

## Method and guarantee scope

- For a fixed UAV position and selected user/target pair, the paper derives the globally optimal beamformer: maximum-ratio transmission when it already meets sensing, otherwise a user/target steering-vector combination.
- A sensing-slot rate lower bound removes finite-array correlation. It is asymptotically tight for large arrays and exact only under specified steering-vector separations.
- Auxiliary product variables and quadratic penalties handle binary user/target coupling. An inner alternating loop updates slack variables, schedules, and an SCA trajectory; an outer loop tightens the consistency penalty.
- Without endpoint constraints, the paper proves that an optimal one-frame pattern can repeat or reverse across adjacent frames. The endpoint-connected low-complexity construction remains a high-quality heuristic, not a global solution of the original problem.
- [[meng-2026-uav-isac-corrections]] removes a duplicated association factor and replaces an invalid Hessian argument with an auxiliary variable and Taylor bound. The correction states that the reported simulations already used the repaired formulation.

## Findings

- Higher sensing thresholds move the UAV toward targets and reduce communication rate; higher sensing frequency produces more turn-backs and further constrains the trajectory.
- At sensing slots, the optimized design tends to pair a target with a nearby communication user and directs the beam toward both.
- In the endpoint-free special case, achievable rate is nondecreasing with sensing-frame length, equivalently nonincreasing with sensing frequency under the paper's discrete feasibility assumptions.
- Large-array and low-complexity comparisons are mainly figure-derived. The parse drops the units or percent signs from two quoted gaps, so those values are not treated as exact results here.

## Limitations

The study is simulation-only and assumes perfect positions, deterministic sensing thresholds, LoS channels, equal frames, fixed altitude, compensated Doppler, and one user/target per slot. The symmetry result excludes endpoint constraints, and the full penalty/AO/SCA pipeline has no global-optimality guarantee. Multi-UAV sensing, imperfect Doppler compensation, clutter, and sensing-assisted communication gains are left open. Equation OCR is heavily damaged; method claims above follow the paper's prose and the published correction rather than symbol-level reconstruction.

## Relation to the corpus

This is the original method corrected by [[meng-2026-uav-isac-corrections]] and surveyed by [[meng-2024-uav-isac-overview]]. It complements event-triggered sensing in [[lyu-2026-situation-aware-uav-isac]] by optimizing periodic target-slot placement for throughput rather than switching sensing from an observed communication state.

## Raw artifacts

- Parse: `raw/sources/Throughput_Maximization_for_UAV-Enabled_Integrated_Periodic_Sensing_and_Communication/Throughput_Maximization_for_UAV-Enabled_Integrated_Periodic_Sensing_and_Communication.md`
- Original PDF and extracted figures are in the same folder.
