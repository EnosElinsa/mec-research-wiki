---
type: source
title: "Low-Altitude UAV Tracking via Sensing-Assisted Predictive Beamforming"
authors: ["Yifan Jiang", "Qingqing Wu", "Hongxun Hui", "Wen Chen", "Derrick Wing Kwan Ng"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3696638"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, predictive-beamforming, uav-tracking, outage-capacity, ekf, sca]
related:
  - "[[sensing-assisted-predictive-beamforming]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[control-assisted-uav-beam-tracking]]"
  - "[[historical-echo-predictive-beamforming]]"
  - "[[zhang-2026-control-assisted-beam-tracking]]"
  - "[[xu-2026-hecta-predictive-beamforming]]"
  - "[[qingqing-wu]]"
  - "[[derrick-wing-kwan-ng]]"
created: 2026-07-13
updated: 2026-07-13
---

# Low-Altitude UAV Tracking via Sensing-Assisted Predictive Beamforming

## Citation

Jiang, Y., Wu, Q., Hui, H., Chen, W., & Ng, D. W. K. (2026). Low-altitude UAV tracking via sensing-assisted predictive beamforming. *IEEE Transactions on Wireless Communications, 25*, 17975-17988. https://doi.org/10.1109/TWC.2026.3696638

The parse omits publication metadata; the exact-title Crossref record supplies the year, venue, DOI, volume, and pages.

## TL;DR

A monostatic ISAC base station predicts a cellular UAV's state, transmits a first beam, updates the state from echoes with an EKF, and transmits a second beam. Analytical outage approximations make sensing duration, target SNR, and controlled UAV position jointly searchable.

## Problem and system model

One terrestrial BS with transmit/receive ULAs communicates with and tracks one single-antenna UAV at fixed altitude. Horizontal position and velocity follow linear controlled dynamics with Gaussian process noise. Each slot allocates one fraction to a beam aimed at the predicted azimuth and the remainder to a beam aimed at the EKF-updated estimate.

The per-slot objective maximizes duration-weighted outage capacity by choosing predicted horizontal position, sensing fraction, and prediction/estimation target SNRs. Constraints cover movement, velocity, a flyable-zone boundary, sensing-duration bounds, outage tolerance, and feasible SNR targets.

## Method

The paper combines EKF prediction/update with a two-step Taylor approximation of array gain and trajectory error. This turns the implicit complementary outage region into an elliptical approximation and yields tractable outage expressions. One solver uses outage-capacity bisection with nested feasibility search and SCA; a lower-complexity AO solver alternates golden-section/bisection searches with an SCA trajectory update.

## Key findings

- Outage approximations closely track `10^4` Monte Carlo runs at predicted y-coordinates 7 m and 15 m, but degrade at 3 m, especially in the prediction stage.
- For 32- and 64-element arrays, the prose places minimum-outage predicted positions on the minimum-y boundary at x-coordinates about `+/-5.8 m`.
- The AO trajectory visually matches exhaustive search in the reported setup and tends toward the minimum-y line, but no numerical trajectory error is given.
- Under prediction-MSE-dominant uncertainty and outage threshold `10^-2`, the proposed design exceeds benchmarks by more than 0.2 bps/Hz; that advantage disappears in the prediction-MSE-nondominant case.

## Limitations

The analysis relies on small tracking errors and position-dependent outage approximations. Evidence is simulation-only for one fixed-altitude UAV, one monostatic ULA BS, LoS-dominant free-space propagation, and slot-invariant motion. Bisection convergence concerns the approximated problem, SCA is local, and the AO heuristic has no convergence guarantee. The main advantage is conditional on prediction-MSE-dominant uncertainty; multistatic ISAC is future work.

## Relation to the corpus

[[sensing-assisted-predictive-beamforming]] uses echoes and explicit EKF state correction. This differs from [[historical-echo-predictive-beamforming]], which learns beams directly from echo histories, and [[control-assisted-uav-beam-tracking]], which uses flight-controller telemetry.

## Raw artifacts

- Parse: `raw/sources/Low-Altitude_UAV_Tracking_via_Sensing-Assisted_Predictive_Beamforming/Low-Altitude_UAV_Tracking_via_Sensing-Assisted_Predictive_Beamforming.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
