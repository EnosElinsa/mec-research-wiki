---
type: source
title: "Unpredictable Trajectory Optimization for UAV-Assisted Anti-Jamming Data Collection"
authors: ["Tiedan Hua", "Yang Chen", "Xi Chen", "Zhen-Hua Zhu"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3605584"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS), vol. 27, no. 1, pp. 448-459"
tags: [source, uav-data-collection, anti-jamming, trajectory-optimization, unpredictable-trajectory, stochastic-control, model-predictive-control, mobile-jammer]
related:
  - "[[unpredictable-uav-trajectory-control]]"
  - "[[navigation-stochastic-control-decomposition]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[anti-jamming-mec]]"
  - "[[yin-2026-uav-antijamming-nfsp]]"
  - "[[you-2019-rician-uav-data-harvesting]]"
  - "[[tang-2026-gat-antijamming]]"
created: 2026-07-14
updated: 2026-07-14
---

# Unpredictable Trajectory Optimization for UAV-Assisted Anti-Jamming Data Collection

## Citation

Hua, T., Chen, Y., Chen, X., & Zhu, Z.-H. (2026). *Unpredictable Trajectory Optimization for UAV-Assisted Anti-Jamming Data Collection*. **IEEE Transactions on Intelligent Transportation Systems, 27**(1), 448-459. DOI: 10.1109/TITS.2025.3605584.

The article was published online on 13 November 2025, had a current-version date of 26 December 2025, and was assigned to the final January 2026 issue.

## TL;DR

The unpredictable trajectory framework splits a UAV's heading-rate control into mission-directed navigation and stochastic components. Receding-horizon navigation maintains data-collection and endpoint progress, while a Gaussian stochastic term is shaped from current jammer geometry to increase trajectory-prediction difficulty and reduce a jammer-interference proxy. The paper states finite component bounds but does not explain how unbounded Gaussian samples are clipped or truncated to satisfy them.

## Problem

A deterministic collection route can be predicted by mobile jammers, allowing them to move toward future UAV positions and degrade the uplink. The paper seeks [[unpredictable-uav-trajectory-control]] that still collects a required payload and reaches a prescribed endpoint while making short-term motion harder to predict.

The operation is communication-level UAV data collection, not MEC computation offloading. “Anti-jamming” here denotes trajectory shaping against a modeled interference threat; it does not by itself establish secrecy, cryptographic protection, attack detection, or a general security guarantee.

## System model

- One fixed-speed, fixed-altitude Dubins UAV collects data from one ground IoT device over a LoS Rician link while one or more barrage jammers interfere across the full bandwidth.
- The UAV controls bounded heading angular velocity and must start and end at prescribed positions while collecting at least a required payload.
- UAV and jammers are assumed to observe each other's exact current coordinates and trajectory histories. Future jammer positions are unknown and frozen at their current coordinates across the navigation horizon.
- The evaluation considers six stationary jammers and six mobile jammers that deterministically pursue the UAV's current position.

## Method

The central [[navigation-stochastic-control-decomposition]] writes total heading control as a navigation term plus a stochastic term, with component bounds selected to respect the physical heading-rate limit.

At each slot, finite-set receding-horizon navigation enumerates discretized control sequences, balances remaining collection pressure against endpoint distance, and applies the first control from the best candidate sequence. The stochastic stage samples a Gaussian input with fixed variance and optimizes its mean to balance a two-step jammer-interference proxy against squared control effort. A modified, parallel gradient method initializes one thread per jammer and keeps the lowest reported objective. Random control is disabled near the endpoint to support arrival.

Exhaustive enumeration finds the best sequence only within the finite discretized navigation candidates at that slot. The gradient procedure does not establish a global optimum for the stochastic subproblem or for the complete mission. The paper's theorems support a single-jammer stationary relation, existence of a minimum on a bounded mean interval, and a far-distance approximation; they do not prove end-to-end security, stochastic mission feasibility for every realization, or global UTF optimality.

## Key findings

- MATLAB simulations use a `1 km x 1 km` area, a `100 m` UAV altitude, `10 m/s` speed, 200 slots, a `4 Mbit` collection requirement, five navigation candidates, and a three-step prediction horizon.
- Against SPOC, IBUR, and EMOPSO, UTF produces locally irregular paths while progressing toward the endpoint. The qualitative trajectory comparison is figure-based.
- For stationary jammers, UTF reports one-step Kalman prediction error `(max, avg, std) = (1.98, 0.40, 0.29)`; for mobile jammers it reports `(1.69, 0.37, 0.30)`. Table II does not state units.
- The reported averages and standard deviations are highest among the four methods, but UTF does not have the highest maximum error in every comparison. These prediction-error statistics are evidence within the tested simulator, not a lower bound against adaptive predictors.
- Increasing stochastic variance from `3` to `10` to `20` makes trajectories more irregular but worsens navigation, showing a mission-progress versus unpredictability tradeoff.
- Runtime grows sharply with candidate count and horizon: the reported examples range from `8.52 ms` at `(5,3)` to `33032.99 ms` at `(9,6)`, so real-time suitability depends on parameterization and hardware.

## Limitations / future work

Validation is simulation-only, with no flight test, measured channel trace, adaptive-jammer experiment, confidence interval, or significance test. The model assumes exact current jammer coordinates, fixed speed/altitude, sufficient mission time, equal constant jammer powers, and manually selected stochastic variance. Its Gaussian input has unbounded support even though finite control bounds are stated, with no visible clipping or truncation rule in the parse. Unpredictability is measured only by one-step Kalman prediction error, so the results do not demonstrate resistance to nonlinear, multi-step, learned, or UTF-aware predictors. Extending the method to formation-preserving multi-UAV operation is future work.

## Relation to the corpus

This source adds motion unpredictability to [[uav-data-collection]] and sits adjacent to the corpus's [[anti-jamming-mec]] work, but it does not optimize computation tasks or resources. [[yin-2026-uav-antijamming-nfsp]] instead treats hidden jammer state and recurrent opponent modeling, while [[tang-2026-gat-antijamming]] combines trajectory/deployment decisions with adversarial learning and beamforming. [[you-2019-rician-uav-data-harvesting]] shares Rician-channel collection and trajectory design without deliberate stochastic unpredictability.

## Raw artifacts

- Parse: `raw/sources/Unpredictable_Trajectory_Optimization_for_UAV-Assisted_Anti-Jamming_Data_Collection/Unpredictable_Trajectory_Optimization_for_UAV-Assisted_Anti-Jamming_Data_Collection.md`
- Origin PDF: `raw/sources/Unpredictable_Trajectory_Optimization_for_UAV-Assisted_Anti-Jamming_Data_Collection/Unpredictable_Trajectory_Optimization_for_UAV-Assisted_Anti-Jamming_Data_Collection.pdf`
- Figures: `raw/sources/Unpredictable_Trajectory_Optimization_for_UAV-Assisted_Anti-Jamming_Data_Collection/images/`
