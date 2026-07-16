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
modeling_card: required
updated: 2026-07-16
---

# Low-Altitude UAV Tracking via Sensing-Assisted Predictive Beamforming

## Citation

Jiang, Y., Wu, Q., Hui, H., Chen, W., & Ng, D. W. K. (2026). Low-altitude UAV tracking via sensing-assisted predictive beamforming. *IEEE Transactions on Wireless Communications, 25*, 17975-17988. https://doi.org/10.1109/TWC.2026.3696638

The parse omits publication metadata; the exact-title Crossref record supplies the year, venue, DOI, volume, and pages.

## TL;DR

A monostatic ISAC base station predicts a cellular UAV's state, transmits a first beam, updates the state from echoes with an EKF, and transmits a second beam. Analytical outage approximations make sensing duration, target SNR, and controlled UAV position jointly searchable.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A terrestrial monostatic ISAC base station with transmit and receive ULAs tracks and communicates with one single-antenna UAV flying at fixed altitude under controlled linear motion, Gaussian process noise, and a LoS-dominant channel; each slot contains prediction-beam and EKF-updated-beam stages.

**Problem & objective**: Problem P1 maximizes per-slot outage capacity $C_n=w_n\log_2(1+\breve{\gamma}_n)+(1-w_n)\log_2(1+\hat{\gamma}_n)$ over the controlled predicted position, sensing duration, and target received SNRs.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Predicted horizontal position | $\breve{\mathbf q}_n$ | Continuous, $\mathbb R^2$ | Controls the next UAV position and beam direction |
| Sensing-duration ratio | $w_n$ | Continuous, $[w_{\min},w_{\max}]$ | Splits the slot between prediction and estimation stages |
| Target received SNRs | $(\breve{\gamma}_n,\hat{\gamma}_n)$ | Continuous, $(0,\gamma_{\max})$ | Set the outage capacities of the two stages |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | One-slot motion is speed limited: $\lVert\breve{\mathbf q}_n-\hat{\mathbf q}_{n-1}\rVert\leq v_{A,\max}\Delta T$ |
| C2 | The controlled position remains in the flyable region: $\breve y_n\geq y_{\min}$ |
| C3 | The sensing fraction satisfies $w_{\min}\leq w_n\leq w_{\max}$ |
| C4 | Both stage outage probabilities remain below $\varepsilon_{\mathrm{out}}$ |
| C5 | Target SNRs satisfy $0<\breve{\gamma}_n,\hat{\gamma}_n<\gamma_{\max}$ |

**Algorithm**: EKF prediction and echo-based update produce the state statistics; second-order Taylor expansions approximate both outage probabilities; a search solver combines outage-capacity bisection with SCA feasibility updates, while a lower-complexity alternative applies alternating one-dimensional searches and an SCA position update.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Jiang et al. [x] studied reliable tracking and communication for one cellular-connected UAV served by a monostatic ISAC base station. They jointly optimized the predicted horizontal position, sensing-duration ratio, and prediction and estimation SNR targets to maximize per-slot outage capacity under mobility, flyable-region, outage, and variable-bound constraints. Their scheme combines EKF prediction and update with second-order outage approximations, then solves the approximated problem using bisection and SCA or a lower-complexity AO procedure. Simulations with $10^4$ Monte Carlo runs showed that the outage approximations closely matched samples at the reported 7 m and 15 m positions but were less accurate at 3 m. In the prediction-MSE-dominant case, the proposed trajectory design exceeded the reported benchmarks by more than 0.2 bps/Hz, while that advantage disappeared in the prediction-MSE-nondominant case.

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
