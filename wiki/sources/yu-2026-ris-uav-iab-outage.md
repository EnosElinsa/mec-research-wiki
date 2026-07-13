---
type: source
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
updated: 2026-07-14
---

# Outage Minimization for RIS and UAV Collaboration-Enhanced IAB Networks

## Citation

Yu, Y., Yang, B., Hao, X., Qian, Y., Guo, L., & Li, Y. (2026). *Outage Minimization for RIS and UAV Collaboration-Enhanced IAB Networks*. **IEEE Transactions on Wireless Communications, 25**, 7350-7364. DOI: 10.1109/TWC.2025.3630746.

## TL;DR

Jointly places UAV IAB nodes vertically and configures a rooftop RIS so urban access links meet user-rate requirements without exceeding backhaul capacity, reducing blockage-, SNR-, and relay-accumulation outages.

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
