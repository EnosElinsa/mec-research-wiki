---
type: source
title: "Dynamically Segmented IRS-Assisted UAV Computing Power Networks: Towards System Delay and Energy Consumption Optimization"
authors: ["Hao Hu", "Yan Zhang", "Zhaolong Ning", "Chau Yuen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3678734"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-15"
tags: [source, computing-power-network, intelligent-reflecting-surface, multi-uav, mappo, energy-latency-tradeoff, task-offloading]
related:
  - "[[uav-enabled-computing-power-network]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[dynamic-irs-user-association]]"
  - "[[energy-latency-tradeoff]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[zhaolong-ning]]"
  - "[[deng-2026-uav-cpn-energy]]"
  - "[[ning-2025-channel-aware-irs-uav]]"
created: 2026-07-13
updated: 2026-07-13
---

# Dynamically Segmented IRS-Assisted UAV Computing Power Networks: Towards System Delay and Energy Consumption Optimization

## Citation

Hu, H., Zhang, Y., Ning, Z., & Yuen, C. (2026). *Dynamically Segmented IRS-Assisted UAV Computing Power Networks: Towards System Delay and Energy Consumption Optimization*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3678734.

## TL;DR

Jointly controls UAV trajectories, user-UAV association, computing allocation, IRS row segmentation, and phase shifts for fully offloaded tasks. A MAPPO trajectory policy is followed by closed-form phase alignment, best-channel association, convex compute allocation, and SCA-based dynamic IRS segmentation.

## Problem

UAV computing-power networks can extend compute coverage, but limited UAV compute and spectrum create a delay-energy tradeoff. A whole IRS or fixed element split cannot adapt to multiple users with heterogeneous tasks, so reflected elements and UAV compute must be allocated together as users and UAVs move.

## System model

- Multiple UAV aerial compute servers serve users through one fixed elevated IRS in a slotted area. Each indivisible task is fully offloaded and carries data size, required CPU cycles, and a delay limit.
- Every user selects one UAV per slot. UAV compute is capacity-constrained, while IRS rows are dynamically partitioned among users and phases align reflected paths.
- Direct and reflected channels are LoS-dominant; the base derivation drops the user-IRS NLoS component. OFDMA divides bandwidth equally among users.
- The weighted objective combines total task delay with UAV compute and constant per-slot flight energy under movement, collision, association, compute, delay, element-allocation, and phase constraints.

## Method

TCPA first aligns IRS phases and uses best-channel user-UAV association. Its matching block alternates convex compute allocation with SCA-relaxed IRS-row allocation, rounds the continuous row counts down, and assigns remaining rows by marginal channel-gain/delay improvement.

UAV motion is a Dec-POMDP solved by shared-parameter MAPPO under centralized training and local execution. At runtime, the policy moves UAVs; phase/alignment and association are recomputed; then IRS segmentation and compute allocation are solved for the new geometry.

## Key findings

- With mobile users increasing from 5 to 25, TCPA's total-delay advantage over fixed reflecting-element allocation grows from `2.84 s` to `8.52 s`; its advantage over no IRS grows from `4.12 s` to `39.21 s`.
- Increasing IRS size from `100 x 100` to `900 x 900` reduces total delay by `12.27%` for TCPA, `15.61%` for single-objective optimization, and `23.79%` for the tested TCPA-NLoS variant, with comparable computation energy.
- Above 10 users, TCPA may consume more compute energy than no-IRS and MATD3-Greedy, but it delivers the larger delay reduction targeted by the selected objective weights.
- Above 600 Megacycles per task, TCPA reports `12.49%` lower delay than no IRS with similar overall computation energy.
- The selected objective-weight ratio is `0.05`, prioritizing delay while retaining energy stability.

## Limitations / parse caveats

The work is synthetic simulation only and assumes full indivisible offloading, equal OFDMA bandwidth, a fixed IRS, continuous phases, known geometry, LoS-dominant channels, and constant flight power. Generalization to mobile users assumes a stationary motion distribution, and changing the UAV-agent count during training is reported to prevent convergence. The claimed global MAPPO convergence is therefore stronger than the fixed-agent evidence. The parameter table stops at 700 IRS rows/columns while results discuss `900 x 900`; several constraints and Algorithm 2 assignments are OCR-damaged. Final metadata was verified by exact title because the parse lacks a publication header.

## Relation to the corpus

This source extends [[uav-enabled-computing-power-network]] from stochastic-geometry availability analysis in [[deng-2026-uav-cpn-energy]] to online task allocation and multi-UAV motion. Its IRS rows implement the partitioned-user behavior already represented by [[dynamic-irs-user-association]], so no separate segmented-IRS synonym is needed. [[ning-2025-channel-aware-irs-uav]] is the communication-only neighbor; here the reflected channel is coupled directly to compute allocation and task delay.

## Raw artifacts

- Parse: `raw/sources/Dynamically_Segmented_IRS-Assisted_UAV_Computing_Power_Networks_Towards_System_Delay_and_Energy_Consumption_Optimization/Dynamically_Segmented_IRS-Assisted_UAV_Computing_Power_Networks_Towards_System_Delay_and_Energy_Consumption_Optimization.md`
- Origin PDF: `raw/sources/Dynamically_Segmented_IRS-Assisted_UAV_Computing_Power_Networks_Towards_System_Delay_and_Energy_Consumption_Optimization/Dynamically_Segmented_IRS-Assisted_UAV_Computing_Power_Networks_Towards_System_Delay_and_Energy_Consumption_Optimization.pdf`
- Figures: `raw/sources/Dynamically_Segmented_IRS-Assisted_UAV_Computing_Power_Networks_Towards_System_Delay_and_Energy_Consumption_Optimization/images/`
