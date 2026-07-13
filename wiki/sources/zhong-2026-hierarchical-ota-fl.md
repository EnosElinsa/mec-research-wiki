---
type: source
title: "UAV-Enabled Over-the-Air Federated Learning: A Hierarchical Aggregation Approach"
authors: ["Xiangyu Zhong", "Chenxi Zhong", "Xiaojun Yuan", "Ying-Jun Angela Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3635287"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 8066-8082"
tags: [source, federated-learning, over-the-air-computation, hierarchical-aggregation, uav-trajectory, aggregation-mse]
related:
  - "[[federated-learning]]"
  - "[[over-the-air-computation]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[hierarchical-over-the-air-federated-learning]]"
  - "[[gradient-correlation-aware-aggregation-mse]]"
  - "[[huang-2026-aircomp-uav-swarms-afl]]"
  - "[[xiaojun-yuan]]"
  - "[[ying-jun-angela-zhang]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV-Enabled Over-the-Air Federated Learning: A Hierarchical Aggregation Approach

## Citation

Zhong, X., Zhong, C., Yuan, X., & Zhang, Y.-J. A. (2026). *UAV-Enabled Over-the-Air Federated Learning: A Hierarchical Aggregation Approach*. **IEEE Transactions on Wireless Communications, 25**, 8066-8082. DOI: 10.1109/TWC.2025.3635287.

## TL;DR

Uses a mobile UAV parameter server to collect partial over-the-air gradient aggregates at multiple trajectory positions, then aligns them into global updates. The design jointly optimizes trajectory, device selection, and aggregation coefficients against a gradient-correlation-aware MSE bound, while the aggregation-frequency parameter trades more model updates against accumulated wireless error.

## Problem framing

In conventional [[over-the-air-computation|AirComp]], a weak device channel can force all simultaneous transmitters to reduce effective amplitude, while excluding weak devices can bias [[federated-learning|federated learning]]. The paper groups aggregation over a UAV flight path: the UAV moves toward spatially separated devices, computes partial aggregates over several slots, and combines them hierarchically instead of requiring every device to participate in one simultaneous transmission.

## System model

- A fixed-altitude UAV parameter server follows a closed horizontal trajectory and broadcasts the current model before collecting synchronous local-gradient transmissions from selected devices.
- Each gradient is normalized using its mean and variance, complex-packed, phase-compensated, and transmitted with fixed power over a free-space LoS channel. Partial AirComp sums are scaled and later aligned into a global gradient estimate.
- A flying round contains multiple model-update segments. The integer aggregation frequency controls the number of global updates per flying round and the number of uplink slots contributing to each update.
- Gradient means, variances, and cross-device correlations enter the aggregation-error model. The optimization controls UAV positions, binary device selection, receiver coefficients, and equivalent channel variables.

## Method

The paper derives the hierarchical aggregation error and its MSE, then uses a learning-convergence bound to minimize the summed MSE over communication rounds. Alternating optimization updates receiver coefficients in closed form, trajectory/channel variables through SCA, and relaxed device-selection/sample-total variables through fractional programming and SCA. Relaxed selections are rounded to binary values for simulation.

This procedure places the source in the AO/SCA branch of [[alternating-optimization-sdr-sca]]; it does not use SDR. The communication mechanism is captured by [[hierarchical-over-the-air-federated-learning]], while [[gradient-correlation-aware-aggregation-mse]] records how selection bias, channel mismatch, receiver noise, and cross-device gradient correlation enter the objective.

## Guarantee scope

Under differentiability, Lipschitz-gradient, and normalized-gradient distribution assumptions, the paper bounds the asymptotic minimum expected squared global gradient by average aggregation MSE. This is a stationarity-oriented learning bound, not a guarantee of globally minimizing the FL loss. A second theorem decomposes the MSE into noise, selection/mean-bias, and correlation-weighted mismatch terms. The alternating solver is claimed to converge, but relaxations, local convex approximations, and binary rounding limit the result to a local/approximate solution rather than global optimality.

## Key findings

- Across the reported MNIST, Fashion-MNIST, and CIFAR-10 experiments, the jointly optimized UAV parameter server is qualitatively closer to the error-free baseline than the tested static-server, repeated-static-aggregation, and non-trajectory-optimized UAV baselines.
- In the illustrated 120 s trajectory, the UAV does not need to fly directly over every device because clustered devices aggregate simultaneously. This is scenario-specific.
- Under non-IID Fashion-MNIST and a fixed 12,000-slot communication budget, the prose reports the best tested performance at aggregation frequency 60; frequency 120 performs below both 60 and 20 despite using more computation than 20.
- For simulated synchronization outliers, reported accuracy changes from 74.88% with no outliers to 74.60% at 10% and 71.26% at 20%. This experiment replaces affected signals with random noise and is not a physical timing-offset model.
- For simulated CSI phase deviation, reported accuracy changes from 74.88% at 0% to 74.25% at 10% and 74.15% at 20%. All values are model- and experiment-specific.

## Limitations

The model assumes fixed altitude, free-space LoS links, slotwise invariant CSI, compensated Doppler, synchronous upload, error-free model broadcast, and error-free delivery of gradient statistics. Gradient correlation is held constant within each flying round, while relaxed selection variables require rounding. Propulsion energy, end-to-end wall-clock training time, synchronization overhead, blocked/non-LoS channels, and imperfect statistics links are outside the objective. The parse's aggregation-frequency table is malformed, so only ordering stated explicitly in the prose is retained.

## Relation to the corpus

This source extends [[federated-learning]] and [[over-the-air-computation]] with two-level aggregation along a controlled UAV path. Compared with [[huang-2026-aircomp-uav-swarms-afl]], it centers on partial gradient aggregation by one mobile parameter server and a tunable global-update frequency. Its theorem-backed [[gradient-correlation-aware-aggregation-mse]] provides the communication-learning bridge, while [[uav-trajectory-control]] supplies spatial grouping opportunities.

## Raw artifacts

- Parse: `raw/sources/UAV-Enabled_Over-the-Air_Federated_Learning_A_Hierarchical_Aggregation_Approach/UAV-Enabled_Over-the-Air_Federated_Learning_A_Hierarchical_Aggregation_Approach.md`
- Origin PDF: `raw/sources/UAV-Enabled_Over-the-Air_Federated_Learning_A_Hierarchical_Aggregation_Approach/UAV-Enabled_Over-the-Air_Federated_Learning_A_Hierarchical_Aggregation_Approach.pdf`
- Figures: `raw/sources/UAV-Enabled_Over-the-Air_Federated_Learning_A_Hierarchical_Aggregation_Approach/images/`
