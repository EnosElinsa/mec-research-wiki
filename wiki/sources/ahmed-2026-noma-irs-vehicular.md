---
type: source
title: "Efficient Resource Management for NOMA-Enabled UAV Communications in 6G IRS-Assisted Vehicular Networks"
authors: ["Manzoor Ahmed", "Wali Ullah Khan", "Fahd N. Al-Wesabi", "Shouki A. Ebad", "Haya Mesfer Alshahrani", "Ashit Kumar Dutta", "Basem M. ElHalawany", "Xingwang Li"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3549224"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS), vol. 27, no. 2, pp. 2706-2715"
tags: [source, noma, intelligent-reflecting-surface, uav-communications, vehicular-network, passive-beamforming, power-allocation]
related:
  - "[[fixed-point-irs-passive-beamforming]]"
  - "[[noma]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[wu-2019-irs-joint-beamforming]]"
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
  - "[[ning-2025-channel-aware-irs-uav]]"
  - "[[cui-2026-aris-v2x-icac]]"
created: 2026-07-13
updated: 2026-07-13
---

# Efficient Resource Management for NOMA-Enabled UAV Communications in 6G IRS-Assisted Vehicular Networks

## Citation

Ahmed, M., Khan, W. U., Al-Wesabi, F. N., Ebad, S. A., Alshahrani, H. M., Dutta, A. K., ElHalawany, B. M., & Li, X. (2026). *Efficient Resource Management for NOMA-Enabled UAV Communications in 6G IRS-Assisted Vehicular Networks*. **IEEE Transactions on Intelligent Transportation Systems**, 27(2), 2706-2715. DOI: 10.1109/TITS.2025.3549224.

## TL;DR

Maximizes downlink sum capacity for a single UAV serving vehicles through power-domain NOMA and a building-mounted passive IRS. Alternating optimization couples projected fixed-point IRS phase updates with convex UAV power allocation under SINR and unit-modulus constraints.

## Problem

Urban obstacles weaken direct UAV-to-vehicle links. The paper asks how a passive IRS can provide an additional reflected path while jointly setting NOMA power coefficients and IRS phases to maximize aggregate vehicle capacity.

## System model

- One UAV transmits superposed NOMA signals to multiple vehicles through direct and IRS-reflected paths. Vehicles apply successive interference cancellation.
- The UAV-IRS and IRS-vehicle channels use Rician fading; the direct UAV-vehicle channel uses Rayleigh fading. Channel state is assumed known at the UAV.
- The objective maximizes sum `log2(1 + SINR)` under per-vehicle SINR, total power-coefficient, UAV transmit-power, and continuous unit-modulus phase constraints.

## Method

First-order Taylor expansion linearizes the non-convex formulation around feasible SINR points. With power fixed, [[fixed-point-irs-passive-beamforming]] iteratively updates the phase vector, projects it back to the unit circle, and stops its inner phase loop on objective change. With phases fixed, CVX solves the convex UAV power-allocation block and updates SINR reference points until their change is small. The paper alternates the two blocks but does not print a separate outer-loop stopping criterion.

The method is a per-channel numerical optimizer rather than a trained policy. Its stated complexity scales linearly with IRS element count within each phase iteration and cubically with vehicle count in the interior-point power block.

## Key findings

- Monte Carlo evaluation uses 1000 trials, two vehicles, 128 IRS elements, a fixed `80 m` UAV altitude, 10-30 dBm UAV power, and at most 10 optimizer iterations.
- Sum capacity stabilizes after two or three alternating iterations across the tested powers and IRS sizes.
- At 30 dBm, the IRS-assisted design reaches about `42 bit/s/Hz` versus `34 bit/s/Hz` without IRS, a stated gain near `24%`; the stated gain at 10 dBm is about `26%`.
- At 30 dBm, increasing IRS elements from 20 to 150 raises capacity from about `37` to above `42 bit/s/Hz`. With 128 elements, raising UAV power from 10 to 30 dBm raises capacity from about `37` to above `42 bit/s/Hz`.

## Limitations / parse caveats

The communication-only model assumes one fixed-altitude UAV, perfect channel state, ideal SIC, continuous passive phases, and no UAV or vehicle mobility process. It does not model road geometry, blockage evolution, CSI/SIC error, discrete phase hardware, trajectory control, or real-time solver latency. The phase iteration is locally optimal, not globally guaranteed. The conclusion mentions fixed-power and random-IRS baselines that are not defined in the narrated experiment, and the parse confuses Monte Carlo trials with optimizer iterations and prints the minimum-SINR parameter in rate units. Technical equations contain substantial OCR damage; final metadata was verified by exact title.

## Relation to the corpus

This is a classical passive-IRS/NOMA optimizer rather than [[vehicular-mec]]: vehicles receive communication service, with no computation or offloading model. It extends the foundational active/passive design in [[wu-2019-irs-joint-beamforming]] and contrasts with the learned active-RIS UAV-NOMA controller [[morshed-2026-active-ris-uav-noma-mappo]].

## Raw artifacts

- Parse: `raw/sources/Efficient_Resource_Management_for_NOMA_Enabled_UAV_Communications_in_6G_IRS-Assisted_Vehicular_Networks/Efficient_Resource_Management_for_NOMA_Enabled_UAV_Communications_in_6G_IRS-Assisted_Vehicular_Networks.md`
- Origin PDF: `raw/sources/Efficient_Resource_Management_for_NOMA_Enabled_UAV_Communications_in_6G_IRS-Assisted_Vehicular_Networks/Efficient_Resource_Management_for_NOMA_Enabled_UAV_Communications_in_6G_IRS-Assisted_Vehicular_Networks.pdf`
- Figures: `raw/sources/Efficient_Resource_Management_for_NOMA_Enabled_UAV_Communications_in_6G_IRS-Assisted_Vehicular_Networks/images/`
