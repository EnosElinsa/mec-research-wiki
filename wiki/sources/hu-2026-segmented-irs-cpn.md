---
type: source
title: "Dynamically Segmented IRS-Assisted UAV Computing Power Networks: Towards System Delay and Energy Consumption Optimization"
authors: ["Hao Hu", "Yan Zhang", "Zhaolong Ning", "Chau Yuen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3678734"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-15"
modeling_card: required
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
updated: 2026-07-16
---

# Dynamically Segmented IRS-Assisted UAV Computing Power Networks: Towards System Delay and Energy Consumption Optimization

## Citation

Hu, H., Zhang, Y., Ning, Z., & Yuen, C. (2026). *Dynamically Segmented IRS-Assisted UAV Computing Power Networks: Towards System Delay and Energy Consumption Optimization*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3678734.

## TL;DR

Jointly controls UAV trajectories, user-UAV association, computing allocation, IRS row segmentation, and phase shifts for fully offloaded tasks. A MAPPO trajectory policy is followed by closed-form phase alignment, best-channel association, convex compute allocation, and SCA-based dynamic IRS segmentation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAV aerial computing servers serve users through one fixed elevated IRS in a slotted computing-power network. Each indivisible task is fully offloaded to one UAV, and IRS rows are dynamically partitioned among users. OFDMA divides bandwidth among users; the main channel model is LoS-dominant with direct and IRS-reflected paths, and an NLoS extension is evaluated.

**Problem & objective**: The paper formulates a mixed discrete-continuous, nonconvex multi-objective design that minimizes a weighted sum of total system delay and UAV computation energy, $\min w_1 D^{tot}+w_2 E^{comp}$, over trajectories, associations, computing power, IRS segmentation, and phase shifts.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\mathbf q_m[t]$ | continuous 2D position | Horizontal location of UAV $m$ in slot $t$ |
| User-UAV association | $a_{k,m}[t]$ | binary | Whether user $k$ offloads to UAV $m$ |
| Computing power | $f_{k,m}[t]$ | continuous, nonnegative | UAV CPU resource allocated to user $k$ |
| IRS row allocation | $b_k[t]$ | integer, nonnegative | Number of reflecting rows assigned to user $k$ |
| IRS phase shift | $\theta_{k,r}[t]$ | continuous phase | Phase applied by row $r$ for user $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each user associates with one UAV in each slot |
| C2 | Per-UAV computing allocations do not exceed available computing power |
| C3 | Every task meets its delay limit after transmission and execution |
| C4 | Integer IRS-row allocations are nonnegative and their sum does not exceed the IRS row budget |
| C5 | Reflecting coefficients satisfy the phase-shift and unit-modulus model |
| C6 | UAV motion, operating-region, and collision-separation requirements hold |

**Algorithm**: Learn UAV trajectories with shared-parameter MAPPO, align IRS phases in closed form, select best-channel user-UAV associations, alternately solve convex computing-power allocation and SCA-relaxed IRS segmentation, then round row counts and assign residual rows by marginal delay improvement.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hu et al. [x] studied a dynamically segmented IRS-assisted UAV computing power network for fully offloaded user tasks. They formulated a multi-objective problem that minimizes total system delay and UAV computation energy by jointly optimizing UAV trajectories, phase shifts, user association, computing-power allocation, and IRS-row segmentation. Their TCPA scheme applies shared-parameter MAPPO to UAV trajectory control, closed-form phase alignment and best-channel association to communication matching, and alternating convex and SCA updates to computing power and dynamic IRS segmentation. The continuous row allocation is rounded and remaining rows are assigned according to marginal channel-gain and delay improvement. Simulations report that dynamic segmentation reduces total delay across the evaluated user-load, IRS-size, UAV-count, and computing-demand settings while maintaining the modeled energy-delay tradeoff.

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
