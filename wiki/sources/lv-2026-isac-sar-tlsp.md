---
type: source
title: "Joint Power and Trajectory Optimization for UAV-Enabled ISAC SAR Imaging"
authors: ["Xianglong Lv", "Rongke Liu", "Quanyu Meng", "Yunshuo Zang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3687228"
venue: "IEEE Transactions on Wireless Communications (TWC)"
tags: [source, integrated-sensing-and-communication, synthetic-aperture-radar, trajectory-optimization, bayesian-optimization]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[two-layer-successive-programming]]"
  - "[[bistatic-sar-resolution-fairness]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[uav-trajectory-control]]"
  - "[[rongke-liu]]"
  - "[[lyu-2023-isac-maneuver-beamforming]]"
created: 2026-07-13
updated: 2026-07-13
---

# Joint Power and Trajectory Optimization for UAV-Enabled ISAC SAR Imaging

## Citation

Lv, X., Liu, R., Meng, Q., & Zang, Y. (2026). Joint power and trajectory optimization for UAV-enabled ISAC SAR imaging. *IEEE Transactions on Wireless Communications, 25*, 16915-16930. https://doi.org/10.1109/TWC.2026.3687228

## TL;DR

A BS illuminates fixed ground areas with its communication downlink while a rotary-wing UAV receives bistatic SAR echoes and uploads processed sensing data. A two-layer SQP/Bayesian pipeline jointly controls communication-flight variables and constant-speed sensing legs to trade total energy against two-dimensional imaging resolution and cross-target fairness.

## Problem and system model

The mission alternates sensing and communication trajectory segments. Sensing legs use fixed altitude and constant horizontal velocity under a stop-and-go SAR model; communication legs control position, speed, uplink power, and duration. Each sensing payload must be uploaded before the next sensing task or mission end.

The model includes propulsion, sensing-data processing, and transmission energy; echo-SNR, resolution, rate-margin, data-upload, kinematic, and endpoint constraints; and adjustable mission duration. The [[bistatic-sar-resolution-fairness]] metric combines mean two-dimensional resolution with its cross-area standard deviation.

## Method

[[two-layer-successive-programming]] separates fixed-sensing-parameter communication optimization from the highly nonconvex sensing geometry. The inner layer uses segmentwise SQP with BFGS Hessians and trust regions. The outer layer uses constrained Gaussian-process Bayesian optimization with multi-start initialization, selected non-improving moves, and correlation-aware sampling.

The hybrid method is designed to escape local basins better than a wholly gradient-based solver, but the paper gives no global-optimality guarantee.

## Key findings

- Across tested sensing weights, the paper reports at least **27.41%** lower average mission objective than its best baseline among SCA, PSO, two-layer SQP, and a basic Bayesian variant.
- Twenty-run simulations report objective standard deviation below 3% across sensing weights and below 4% as the outer dimension grows from 12 to 60.
- The tested PSO implementation remains infeasible; TLSP reports the lowest energy across tested weights while preserving target-resolution fairness at low weights.

Convergence curves are padded with each run's final value after termination, so iteration-wise comparisons should be interpreted cautiously.

## Limitations

Evidence is simulation-only. The model assumes static targets, deterministic LoS communication, known geometry, one BS/UAV, constant-speed sensing legs, and simplified stop-and-go SAR. It omits waveform design, clutter/range-Doppler processing, acceleration energy, hard or irregular coverage, moving targets, and multi-platform handover/assignment.

## Relation to the corpus

This source extends [[integrated-sensing-and-communication]] from illumination/communication control into bistatic SAR mission design. Unlike [[lyu-2023-isac-maneuver-beamforming]], it models echo reception, imaging resolution, sensing-data processing, and upload coupling rather than transmit illumination alone.

## Raw artifacts

- Parse: `raw/sources/Joint_Power_and_Trajectory_Optimization_for_UAV-Enabled_ISAC_SAR_Imaging/Joint_Power_and_Trajectory_Optimization_for_UAV-Enabled_ISAC_SAR_Imaging.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
