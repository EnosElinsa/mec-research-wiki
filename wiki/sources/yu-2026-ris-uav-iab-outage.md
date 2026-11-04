---
type: source
modeling_card: required
title: "Outage Minimization for RIS and UAV Collaboration-Enhanced IAB Networks"
authors: ["Yao Yu", "Bowen Yang", "Xin Hao", "Yingkun Qian", "Lei Guo", "Yonghui Li"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3630746"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 7350-7364"
tags: [source, integrated-access-and-backhaul, ris, uav, outage-probability, resource-allocation]
related:
  - "[[integrated-access-and-backhaul]]"
  - "[[access-backhaul-rate-matching]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[wireless-backhaul]]"
  - "[[blockage-aware-channel-model]]"
  - "[[angle-dependent-rician-fading]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[yonghui-li]]"
created: 2026-07-14
updated: 2026-11-03
---

# Outage Minimization for RIS and UAV Collaboration-Enhanced IAB Networks

## Citation

Yu, Y., Yang, B., Hao, X., Qian, Y., Guo, L., & Li, Y. (2026). *Outage Minimization for RIS and UAV Collaboration-Enhanced IAB Networks*. **IEEE Transactions on Wireless Communications, 25**, 7350-7364. DOI: 10.1109/TWC.2025.3630746.

## TL;DR

Jointly places UAV IAB nodes vertically and configures a rooftop RIS so urban access links meet user-rate requirements without exceeding backhaul capacity, reducing blockage-, SNR-, and relay-accumulation outages.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna donor BS backhauls clustered single-antenna UAV IAB nodes through direct and rooftop-RIS paths, while each UAV serves one urban user cluster over elevation-dependent Rician access links. Horizontal positions and time/bandwidth shares are fixed.

**Problem & objective**: Problem (25), solved by the URO scheme, minimizes the average outage probability $\min_{\Theta,\mathcal T_m}1-P_{nout}$, where $P_{nout}$ in (24) is the average non-outage probability, over UAV deployment (heights) and RIS phases.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV height | $h_m$ | continuous, bounded | Vertical position of IAB UAV $m$ |
| RIS phase | $\theta_n$ | continuous, $[0,2\pi)$ | Phase of RIS element $n$ |
| SDR matrix | $\mathbf E_m$ | PSD, unit diagonal, rank one relaxed | Lifted RIS phase representation in (60) |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (25b) | UAV height range: $h_{\min}\le h_m\le h_{\max}$ |
| (25c) | RIS phase range: $0\le\theta_{n_r}\le2\pi$ |
| Model rule | Bandwidth allocation, timeslot assignment, user scheduling, and horizontal UAV positions are fixed; the RIS-UAV link is assumed unblocked ($x_{rm}=1$) |
| Model rule | Outage of user $n$ in cluster $m$ covers both access-rate and backhaul-rate failure, expressed with Marcum-Q terms $Q_1(a_{mn},b_{mn})-Q_1(a_{mn},c_{mn})$ in (24) |

**Algorithm**: Fix RIS phases and lower-bound the Marcum-Q non-outage expression → update UAV heights by SCA → fix heights and maximize summed backhaul rates through SDR → recover feasible phases by Gaussian randomization → alternate URO blocks → optionally evaluate random blockage and jitter by sample-average approximation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yu et al. [x] studied outage minimization in integrated access and backhaul networks enhanced jointly by UAVs and a rooftop RIS. They formulated average outage minimization over UAV heights and unit-modulus RIS phases under height-range and phase constraints, where outage captures both access-rate and backhaul-rate failures under building blockage. Successive convex approximation updates the UAV heights using a lower bound on the Marcum-Q non-outage expression. Semidefinite relaxation and Gaussian randomization update the RIS phases, and URO alternates the two blocks. Simulations compare URO with phase-alignment RIS beamforming (baseline 1), fixed UAV heights (baseline 2), and random RIS phases (baseline 3), reporting a 44.72% outage reduction over baseline 1 across backhaul distances.

## Problem and system model

A multi-antenna donor base station backhauls `M` single-antenna UAV IAB nodes, each serving a user cluster. The BS-UAV channel combines a direct path and a BS-RIS-UAV reflected path from a fixed RIS on the tallest building; UAV-user access follows elevation-dependent Rician fading.

Affinity propagation fixes each UAV's horizontal coordinates at its cluster head. TDMA access/backhaul fractions and equal backhaul-bandwidth shares are predetermined. A cluster is non-outage only when every user exceeds its required rate while its access rate remains below the corresponding backhaul rate, preventing data accumulation at the UAV.

## Method

The [[access-backhaul-rate-matching]] objective minimizes average outage over UAV heights and unit-modulus RIS phases. Successive convex approximation uses an exponential lower bound on the Marcum-Q non-outage expression to update heights. Semidefinite relaxation maximizes summed backhaul rates over RIS phases, followed by Gaussian randomization for a feasible vector. The URO procedure alternates these blocks; its bounded objective is monotonic. A sample-average-approximation extension models NLoS and UAV-jitter randomness.

## Key findings

- The simulations report convergence within 11 alternating iterations.
- Across the tested backhaul distances, URO reduces average outage probability by 44.72% relative to the phase-alignment baseline.
- The non-outage lower bound has 3.09% overall average error against Monte Carlo outage estimates in the reported test.
- Higher UAV altitude improves access LoS probability but can weaken backhaul; the RIS and altitude variables therefore address different sides of the [[integrated-access-and-backhaul|IAB]] bottleneck.

## Limitations

Evidence is simulation-only. Time allocation, bandwidth, and user scheduling are fixed rather than optimized. The main formulation assumes an available RIS-UAV LoS path; the blocked case uses a threshold height. The simulated `lambda/10` RIS spacing may create mutual coupling and hardware complexity, and the SDR/randomization procedure has no global-optimality guarantee.

## Relation to the corpus

This source extends [[wireless-backhaul]] into [[integrated-access-and-backhaul]] with an explicit anti-accumulation rate condition. The RIS strengthens obstructed donor-to-UAV backhaul, while UAV altitude improves access reliability; this division of roles is the consistent model across the abstract, system description, and conclusion.

The Lei Guo on this source is affiliated with Chongqing University of Posts and Telecommunications and is not linked to the different Northeastern University researcher represented by the existing `lei-guo` entity.

## Raw artifacts

- Parse: `raw/sources/Outage_Minimization_for_RIS_and_UAV_Collaboration-Enhanced_IAB_Networks/Outage_Minimization_for_RIS_and_UAV_Collaboration-Enhanced_IAB_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
