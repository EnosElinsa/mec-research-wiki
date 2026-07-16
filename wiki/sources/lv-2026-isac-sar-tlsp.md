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
modeling_card: required
created: 2026-07-13
updated: 2026-07-16
---

# Joint Power and Trajectory Optimization for UAV-Enabled ISAC SAR Imaging

## Citation

Lv, X., Liu, R., Meng, Q., & Zang, Y. (2026). Joint power and trajectory optimization for UAV-enabled ISAC SAR imaging. *IEEE Transactions on Wireless Communications, 25*, 16915-16930. https://doi.org/10.1109/TWC.2026.3687228

## TL;DR

A BS illuminates fixed ground areas with its communication downlink while a rotary-wing UAV receives bistatic SAR echoes and uploads processed sensing data. A two-layer SQP/Bayesian pipeline jointly controls communication-flight variables and constant-speed sensing legs to trade total energy against two-dimensional imaging resolution and cross-target fairness.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A base station illuminates $M$ fixed sensing areas while a rotary-wing UAV alternates constant-speed bistatic-SAR sensing legs with communication legs that upload sensing data; propulsion, processing, and communication energy are modeled explicitly.

**Problem & objective**: Minimize the mission objective $f_{\mathrm{mission}}=(\rho_{\mathrm{sens}}Q_{\mathrm{sens}}+1)(\sum_mE_s^m+\sum_mE_c^m)$ over sensing and communication segment variables.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Sensing segment | $S_r$ | endpoints, altitude, nonnegative speed | Start/end points and speed of each sensing leg |
| Communication path | $\mathbf r_c^m[n]$ | continuous 3-D position | UAV position in communication slot $n$ of segment $m$ |
| Communication speed | $v_c^m[n]$ | continuous, $[0,v_{\max}]$ | UAV speed in communication slot |
| Uplink power | $P_{\mathrm{comm}}^m[n]$ | continuous, $[0,P_{\mathrm{comm}}^{\max}]$ | UAV communication power |
| Slot duration | $\Delta t_c^m$ | continuous, nonnegative | Duration of communication segment $m$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Motion obeys $\|\mathbf r_c^m[n+1]-\mathbf r_c^m[n]\|^2=(v_c^m[n]\Delta t_c^m)^2$ and segment endpoints are continuous. |
| C2 | Communication rate has a floor and uploads prior sensing data, $\mathcal R_c^m[n]\geq\mathcal R_0$ and $\sum_n(\mathcal R_c^m[n]-\mathcal R_0)\Delta t_c^m\geq\mathcal D_s^{m-1}$. |
| C3 | Sensing echoes meet the SNR threshold and altitude bound, while every resolution area satisfies $\mathcal A_{\mathrm{res}}^m\leq\mathcal A_0$. |
| C4 | Speeds, communication powers, and segment durations stay within their bounds, with $H^m\geq H_0$. |

**Algorithm**: Decompose the nonconvex mission into communication and sensing layers, solve communication variables with segmentwise SQP under fixed sensing parameters, optimize sensing geometry with constrained multi-start Bayesian optimization, and iterate the two-layer successive programming updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lv et al. [x] studied joint power and trajectory optimization for a base-station-assisted UAV ISAC SAR mission with adjustable duration and two-dimensional resolution fairness. They formulated a weighted mission-energy objective over sensing segment geometry, communication trajectories, speeds, powers, and durations subject to motion, echo-SNR, resolution, rate-margin, and data-upload constraints. Their two-layer successive programming method uses sequential quadratic programming for communication variables and a modified Bayesian optimizer with multi-start and correlation-aware sampling for the sensing geometry. Simulations report at least 27.41% improvement over the baselines while retaining the lowest energy consumption and resolution fairness across sensing weights.

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
