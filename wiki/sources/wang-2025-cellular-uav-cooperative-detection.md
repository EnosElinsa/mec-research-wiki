---
type: source
title: "ISAC Enabled Cooperative Detection for Cellular-Connected UAV Network"
authors: ["Yi Wang", "Keke Zu", "Luping Xiang", "Qixun Zhang", "Zhiyong Feng", "Jie Hu", "Kun Yang"]
year: 2025
url: "https://doi.org/10.1109/TWC.2024.3509978"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, cellular-connected-uav, cooperative-detection, data-fusion, beamforming, trajectory-optimization]
related:
  - "[[ground-air-cooperative-isac-detection]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[cellular-connected-uav]]"
  - "[[multi-source-data-fusion]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[networked-isac]]"
  - "[[qixun-zhang]]"
  - "[[zhiyong-feng]]"
  - "[[kun-yang]]"
created: 2026-07-13
updated: 2026-07-13
---

# ISAC Enabled Cooperative Detection for Cellular-Connected UAV Network

## Citation

Wang, Y., Zu, K., Xiang, L., Zhang, Q., Feng, Z., Hu, J., & Yang, K. (2025). *ISAC Enabled Cooperative Detection for Cellular-Connected UAV Network*. **IEEE Transactions on Wireless Communications**, 24(2), 1541-1554. DOI: 10.1109/TWC.2024.3509978.

*Metadata note:* The local parse omits the article record; an exact-title Crossref DOI record supplies the 2025 TWC volume, issue, and pages above.

## TL;DR

Combines one terrestrial BS and one cellular-connected sensing UAV for aerial-target detection. Target-level measurements are associated and fused through an EKF, then the fused state feeds alternating beamforming and fixed-altitude trajectory optimization for communication under sensing-beampattern constraints.

## Problem framing

A terrestrial BS offers strong processing but limited sensing range; a connected UAV offers favorable air-ground visibility and mobile geometry but limited sensing capability. Cooperative sensing can extend coverage, but it requires target association, centralized fusion, reliable sensing-data transport, and a trajectory that preserves communication while illuminating targets.

## System model

- One BS and one rotary-wing cellular UAV monitor four surrounding UAVs while the connected UAV travels between fixed endpoints at `100 m` altitude.
- Both sensing nodes estimate delay, Doppler, and direction using 2-D DFT and MUSIC processing.
- A central server or cloud fuses target position and motion observations; the UAV shares data over 5G and the BS uses fiber or high-speed wireless backhaul.
- The optimization maximizes communication rate over transmit beams and the connected-UAV trajectory, subject to sensing beampattern, power, endpoint, and movement constraints.
- Sufficient flight energy is assumed, and wind/propulsion effects are omitted.

## Method

[[ground-air-cooperative-isac-detection]] first associates BS and UAV measurements by normalized position-plus-motion distance. An extended Kalman filter predicts and updates target state/covariance; unmatched observations are retained in the fused result set.

With the fused geometry fixed, beamforming is lifted into covariance matrices and relaxed to an SDP. Rate and sensing constraints are successively convexified. With beamforming fixed, SCA and a trust region update the trajectory; beam and trajectory blocks alternate until the rate objective converges.

## Key findings

- The body reports about `33%` lower range RMSE and `38%` lower velocity RMSE after fusion, without identifying a single baseline denominator.
- The abstract instead claims `67%` higher estimation accuracy, while the conclusion gives `38%`; these headline values are internally inconsistent and should not be combined.
- The proposed joint beamforming/trajectory design is reported to improve data rate by more than `31%`, but the text does not identify which HB, IRS-JTB, or JTB baseline is the denominator.
- Fusion is claimed to extend sensing beyond LoS, but no detection-range increase or blockage-specific metric is supplied.

## Limitations / parse caveats

Validation is simulation-only, with no hardware, Monte Carlo count, seed, runtime, fusion latency, or detection/false-alarm metric. The channel model shifts from Rician LoS/NLoS to LoS-only during optimization, target positions are both described as predetermined and estimated, and the displayed objective is per-slot despite a multi-slot trajectory.

The parse also contains sensing-threshold symbol conflicts, an incomplete EKF covariance, damaged lifted-power expressions, shifted table values, and an underspecified trust-region update. The overall non-convex loop supports a converged iterative solution, not a demonstrated global optimum.

## Relation to the corpus

This source is the asymmetric BS-UAV counterpart of multi-BS [[networked-isac]]. It shares MUSIC/EKF target-state fusion with [[zhao-2025-networked-isac-uav-handover]], but uses the fused state to control a connected UAV's communication beam and trajectory.

## Raw artifacts

- Parse: `raw/sources/ISAC_Enabled_Cooperative_Detection_for_Cellular-Connected_UAV_Network/ISAC_Enabled_Cooperative_Detection_for_Cellular-Connected_UAV_Network.md`
- Origin PDF: `raw/sources/ISAC_Enabled_Cooperative_Detection_for_Cellular-Connected_UAV_Network/ISAC_Enabled_Cooperative_Detection_for_Cellular-Connected_UAV_Network.pdf`
- Figures: `raw/sources/ISAC_Enabled_Cooperative_Detection_for_Cellular-Connected_UAV_Network/images/`
