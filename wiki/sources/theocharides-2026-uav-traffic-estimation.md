---
type: source
title: "Real-Time Urban Traffic State Estimation via UAV-Based Sensing: A Gaussian Process and Moving Horizon Estimation Approach"
authors: ["Kyriacos Theocharides", "Yiolanda Englezou", "Charalambos Menelaou", "Stelios Timotheou"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3648943"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS), vol. 27, no. 4, pp. 4715-4730, 2026"
tags: [source, urban-traffic-state-estimation, uav-sensing, gaussian-process, moving-horizon-estimation, macroscopic-fundamental-diagram, successive-convexification, traffic-density]
related:
  - "[[gaussian-process-moving-horizon-traffic-estimation]]"
  - "[[charalambos-menelaou]]"
  - "[[stelios-timotheou]]"
  - "[[uav-enabled-its]]"
  - "[[uav-data-collection]]"
  - "[[vitale-2026-density-aware-4d-trajectory]]"
created: 2026-07-14
updated: 2026-07-14
---

# Real-Time Urban Traffic State Estimation via UAV-Based Sensing: A Gaussian Process and Moving Horizon Estimation Approach

## Citation

Theocharides, K., Englezou, Y., Menelaou, C., & Timotheou, S. (2026). *Real-Time Urban Traffic State Estimation via UAV-Based Sensing: A Gaussian Process and Moving Horizon Estimation Approach*. **IEEE Transactions on Intelligent Transportation Systems**, 27(4), 4715-4730. DOI: 10.1109/TITS.2025.3648943.

## TL;DR

Combines per-region Gaussian Processes with constrained moving-horizon estimation to infer regional road-traffic density and intended-destination density from sparse, noisy UAV observations. GP predictive means fill unobserved space-time points and their variances weight those virtual measurements; successive convexification then turns the nonconvex traffic-estimation problem into a sequence of convex quadratic programs.

## Problem

UAV traffic monitoring can observe several road-network regions without fixed roadside infrastructure, but each UAV measures only while hovering over its assigned region. Transitions and battery replacement create temporal gaps, and having fewer UAVs than regions creates spatial gaps. The estimator must recover aggregate regional density and destination-specific density despite these sparse noisy measurements and the nonconvex dynamics of a macroscopic fundamental diagram.

## System model

The road network is partitioned into homogeneous regions governed by a triangular macroscopic fundamental diagram. Vehicle conservation tracks regional and intended-destination densities, and actual inter-region flow is limited by intended flow and density-dependent boundary capacity. The model assumes known traffic parameters, maximum boundary capacities, a time-varying origin-destination matrix, and Gaussian process and measurement noise.

Each UAV follows a manually predetermined, non-overlapping cycle of assigned regions, hovers to collect video, and transmits live video to a ground control centre. The centre derives noisy density and transfer-flow measurements. UAVs provide no observations while moving or landing for battery replacement. The main simulation uses seven regions, one to seven UAVs, 10-second steps, and 20 Monte Carlo runs.

## Method

[[gaussian-process-moving-horizon-traffic-estimation]] fits a separate squared-exponential GP to each region's observed density time series. Predictive means provide virtual observations at missing time points, and predictive variances enter the MHE covariance matrix so uncertain interpolations receive corresponding weights.

The finite-window MHE minimizes covariance-weighted process and measurement residuals subject to traffic dynamics and physical bounds. Its first iteration relaxes the triangular MFD and boundary-capacity minimum relations into a convex quadratic program. Later iterations tighten density neighborhoods around the previous solution, construct lower MFD chords, and use McCormick inequalities for bilinear terms. The evaluation separates the effects of GP virtual measurements and boundary-capacity constraints and compares a no-capacity variant with direct nonlinear optimization by IPOPT.

## Key findings

- The hybrid GP+MHE estimator has the lowest plotted regional-density error among the tested successive-convexification variants for every UAV count except seven, where MHE without virtual measurements is slightly better. Destination-density results follow the same general pattern.
- GP virtual measurements provide the largest benefit with one to three UAVs. In the reported plots, GP-only and GP+MHE regional-density RMSE differ by less than 1 veh/km, while MHE remains necessary for intended-destination states that are not directly observed.
- Removing inter-boundary capacity constraints worsens both density estimates when more than four UAVs are used. This is the authors' interpretation of plotted results, not a tabulated universal threshold.
- The text reports 3 seconds per instance for the successive-convexification variants and 445 seconds for GP+IPOPT, roughly two orders of magnitude faster. Hardware, implementation language, and solver-version details are absent, and the nonlinear comparator omits the capacity constraints.
- At four UAVs, the author-reported figure values for destination-density RMSE are 3.3, 3.5, and 4.1 veh/km as process noise increases. Other figure summaries indicate about 0.1 veh/km maximum sensitivity to the tested traffic-parameter perturbations and up to 2.2 veh/km change for battery-swap durations from 0 to 3 minutes; these values are scenario-specific and figure-derived.

## Limitations

Evaluation uses macroscopic simulation with synthetic noisy measurements rather than an end-to-end airborne video, communication, and estimation deployment. UAV routes are predetermined, and the default comparison sets landing time to zero. The sensing model assumes each monitored region's boundary flows are observable; occlusion, camera calibration, weather, packet loss, and video-processing errors are not modeled separately. Traffic parameters and the origin-destination matrix are assumed known, GP hyperparameters are manually calibrated, and the runtime comparison lacks hardware details. Many accuracy conclusions are figure-based, and OCR damage affects equations in the parse.

## Relation to the corpus

This source extends [[uav-enabled-its]] and [[uav-data-collection]] from aerial observation into model-based regional traffic-state estimation. It shares authors [[charalambos-menelaou]] and [[stelios-timotheou]] with [[vitale-2026-density-aware-4d-trajectory]], but that source plans density-aware UAV trajectories rather than estimating road-traffic states.

## Raw artifacts

- Parse: `raw/sources/Real-Time_Urban_Traffic_State_Estimation_via_UAV-Based_Sensing_A_Gaussian_Process_and_Moving_Horizon_Estimation_Approach/Real-Time_Urban_Traffic_State_Estimation_via_UAV-Based_Sensing_A_Gaussian_Process_and_Moving_Horizon_Estimation_Approach.md`
- Origin PDF: `raw/sources/Real-Time_Urban_Traffic_State_Estimation_via_UAV-Based_Sensing_A_Gaussian_Process_and_Moving_Horizon_Estimation_Approach/Real-Time_Urban_Traffic_State_Estimation_via_UAV-Based_Sensing_A_Gaussian_Process_and_Moving_Horizon_Estimation_Approach.pdf`
- Figures: `raw/sources/Real-Time_Urban_Traffic_State_Estimation_via_UAV-Based_Sensing_A_Gaussian_Process_and_Moving_Horizon_Estimation_Approach/images/`
