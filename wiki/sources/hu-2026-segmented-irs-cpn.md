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
updated: 2026-11-03
---

# Dynamically Segmented IRS-Assisted UAV Computing Power Networks: Towards System Delay and Energy Consumption Optimization

## Citation

Hu, H., Zhang, Y., Ning, Z., & Yuen, C. (2026). *Dynamically Segmented IRS-Assisted UAV Computing Power Networks: Towards System Delay and Energy Consumption Optimization*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3678734.

## TL;DR

Jointly controls UAV trajectories, user-UAV association, computing allocation, IRS row segmentation, and phase shifts for fully offloaded tasks. A MAPPO trajectory policy is followed by closed-form phase alignment, best-channel association, convex compute allocation, and SCA-based dynamic IRS segmentation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAV computing servers $k\in\mathcal K$ serve users $n\in\mathcal N$ through one fixed IRS in a slotted computing-power network. Each user's task is fully offloaded to one UAV, IRS rows are dynamically partitioned among users, and links combine direct and IRS-reflected paths.
**Problem & objective**: P0 (12) is a two-objective problem over total user delay and total UAV computation energy; P1 (13) scalarizes it as $\min_{\mathbf L,\beta,c,I,\phi}\omega_1\sum_t\sum_nD_n[t]+\omega_2\sum_t\sum_kE_k[t]$.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\mathbf L_k[t]$ | continuous position | Location of UAV $k$ in slot $t$ |
| User-UAV association | $\beta_{n,k}[t]$ | binary | User $n$ offloads to UAV $k$ |
| Computing power | $c_{n,k}[t]$ | continuous | UAV $k$ computing power allocated to user $n$ |
| IRS row allocation | $I_n[t]$ | integer | Reflecting-element rows assigned to user $n$ |
| IRS phase shift | $\phi$ | continuous, $[0,2\pi)$ | Phase of each reflecting element |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C1 | Fixed per-slot movement $\lVert\mathbf L_k[t+1]-\mathbf L_k[t]\rVert=\tau V$ |
| C2 | Safety distance $\lVert\mathbf L_k[t]-\mathbf L_j[t]\rVert\geq L_{\min}$ |
| C3-C4 | Binary association; each user is assigned to one UAV |
| C5 | Per-UAV computing power $\sum_nc_{n,k}[t]\leq C^{\max}$ |
| C6 | Task delay limit for each user |
| C7-C8 | Limits on the number of reflecting rows per user and in total (expressions garbled in the parse; check the published paper) |
| C9 | Phase shifts in $[0,2\pi)$ |
**Algorithm**: TCPA decomposes P1 into three subproblems. Closed-form phase alignment (Theorem 1) and best-channel matching set phases and associations; an SCA-based block alternates computing-power allocation and relaxed IRS-row allocation, then rounds rows down and gives remaining rows to users with the largest channel-gain increase; MAPPO with parameter sharing among homogeneous UAV agents learns the trajectories.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hu et al. [x] studied a dynamically segmented IRS-assisted UAV computing power network for fully offloaded user tasks. They formulated a multi-objective problem that minimizes total system delay and UAV computation energy by jointly optimizing UAV trajectories, phase shifts, user association, computing-power allocation, and IRS-row segmentation. Their TCPA scheme applies shared-parameter MAPPO to UAV trajectory control, closed-form phase alignment and best-channel association to communication matching, and alternating convex and SCA updates to computing power and dynamic IRS segmentation. The continuous row allocation is rounded down and the remaining rows go to the users with the largest channel-power-gain increase. Simulations report faster convergence and higher reward than MATD3-based, static-IRS, no-IRS, and delay-only baselines; the delay-only baseline reaches lower delay only by sharply raising UAV computation energy.

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
