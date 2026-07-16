---
type: source
title: "Efficient Resource Management for NOMA-Enabled UAV Communications in 6G IRS-Assisted Vehicular Networks"
authors: ["Manzoor Ahmed", "Wali Ullah Khan", "Fahd N. Al-Wesabi", "Shouki A. Ebad", "Haya Mesfer Alshahrani", "Ashit Kumar Dutta", "Basem M. ElHalawany", "Xingwang Li"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3549224"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS), vol. 27, no. 2, pp. 2706-2715"
modeling_card: required
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
  - "[[xingwang-li]]"
created: 2026-07-13
updated: 2026-07-16
---

# Efficient Resource Management for NOMA-Enabled UAV Communications in 6G IRS-Assisted Vehicular Networks

## Citation

Ahmed, M., Khan, W. U., Al-Wesabi, F. N., Ebad, S. A., Alshahrani, H. M., Dutta, A. K., ElHalawany, B. M., & Li, X. (2026). *Efficient Resource Management for NOMA-Enabled UAV Communications in 6G IRS-Assisted Vehicular Networks*. **IEEE Transactions on Intelligent Transportation Systems**, 27(2), 2706-2715. DOI: 10.1109/TITS.2025.3549224.

## TL;DR

Maximizes downlink sum capacity for a single UAV serving vehicles through power-domain NOMA and a building-mounted passive IRS. Alternating optimization couples projected fixed-point IRS phase updates with convex UAV power allocation under SINR and unit-modulus constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An urban downlink has one UAV serving $V$ ground vehicles with power-domain NOMA. A passive IRS with $K$ elements supplies a reflected path in addition to the direct UAV-to-vehicle path; UAV-to-IRS and IRS-to-vehicle channels are Rician, the direct path is Rayleigh, and vehicles use successive interference cancellation.

**Problem & objective**: The non-convex problem $P_1$ maximizes $C_{\mathrm{sum}}=\sum_{v=1}^{V}\log_2(1+\gamma_v)$ by jointly selecting UAV power $P$, NOMA coefficients $\alpha_v$, and IRS phases $\phi_k$ collected in $\Phi$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV transmit power | $P$ | continuous, $0\le P\le P_t$ | Total UAV transmit power |
| NOMA power coefficient | $\alpha_v$ | continuous, $0\le\alpha_v\le1$ | Power fraction assigned to vehicle $v$ |
| IRS phase | $\phi_k$ | complex unit modulus, $\lvert\phi_k\rvert=1$ | Passive phase of IRS element $k$ |
| IRS phase matrix | $\Phi$ | diagonal complex matrix | Passive beamforming matrix built from $\phi_k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every vehicle meets the SINR threshold: $\gamma_v\ge\gamma_{\min},\ \forall v$ |
| C2 | NOMA coefficients use at most the full power fraction: $\sum_{v=1}^{V}\alpha_v\le1$ |
| C3 | UAV power is bounded by the maximum: $0\le P\le P_t$ |
| C4 | Passive IRS elements preserve unit modulus: $\lvert\phi_k\rvert=1,\ \forall k$ |

**Algorithm**: Linearize capacity and SINR constraints with a first-order Taylor expansion around feasible $\gamma_{v,0}$; with power fixed, initialize a unit-modulus $\Phi$, update it by fixed-point iteration, take the gradient step, and project onto the unit circle until the capacity change is below $\epsilon$; with $\Phi$ fixed, solve the convex power-allocation subproblem with CVX, update $\gamma_{v,0}$, and alternate the two blocks until convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ahmed et al. [x] studied sum-capacity enhancement for downlink NOMA UAV communications serving ground vehicles in an urban IRS-assisted network. They formulated a joint optimization of the UAV power-allocation coefficients and passive IRS phase shifts that maximizes $C_{\mathrm{sum}}$ while enforcing minimum vehicle SINR. They first linearized the non-convex problem with a first-order Taylor expansion, then alternated fixed-point IRS beamforming with convex UAV power allocation. Monte Carlo results reported rapid convergence within two or three iterations and about 42 bit/s/Hz versus 34 bit/s/Hz for the direct-link benchmark at 30 dBm, with larger IRS element counts further increasing capacity.

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
