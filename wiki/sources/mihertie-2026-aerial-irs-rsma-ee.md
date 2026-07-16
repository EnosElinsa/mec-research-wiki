---
type: source
modeling_card: required
title: "Energy Efficiency Maximization for Aerial Intelligent Reflecting Surface-Assisted MISO Systems"
authors: ["Habtamu Demeke Mihertie", "Zhengqiang Wang", "Mohamed Amine Ouamri", "Elhadj Moustapha Diallo", "Xingwang Li"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3653184"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 1894-1908"
tags: [source, uav-mounted-ris, rate-splitting-multiple-access, miso, energy-efficiency, hardware-impairments, beamforming, successive-convex-approximation]
related:
  - "[[rate-splitting-multiple-access]]"
  - "[[uav-mounted-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
  - "[[li-2026-aerial-ris-trajectory-phase]]"
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
  - "[[ahmed-2026-noma-irs-vehicular]]"
  - "[[xingwang-li]]"
created: 2026-07-13
updated: 2026-07-16
---

# Energy Efficiency Maximization for Aerial Intelligent Reflecting Surface-Assisted MISO Systems

## Citation

Mihertie, H. D., Wang, Z., Ouamri, M. A., Diallo, E. M., & Li, X. (2026). *Energy Efficiency Maximization for Aerial Intelligent Reflecting Surface-Assisted MISO Systems*. **IEEE Transactions on Green Communications and Networking**, 10, 1894-1908. DOI: 10.1109/TGCN.2026.3653184.

## TL;DR

A BCD-SCA design jointly optimizes RSMA precoders/common rates, continuous UAV-mounted IRS phases, and one aerial-IRS placement point for communication-side energy efficiency under aggregate transmitter/receiver hardware distortion.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna BS serves multiple single-antenna ground users only through a passive IRS mounted on a UAV, with blocked direct links. One-layer RSMA sends one common stream and private streams over Rician BS-to-IRS and IRS-to-user channels, while transmitter and receiver hardware impairments produce signal-dependent Gaussian distortion.

**Problem & objective**: Problem (17)-(18), a non-convex communication-centric energy-efficiency maximization, solves $\max_{\mathbf P,\mathbf q,\mathbf r,\boldsymbol\varphi}\sum_k R_k^{\mathrm{tot}}/P_{\mathrm{tot}}$ over precoding, aerial placement, common-rate allocation, and IRS phases.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| RSMA precoders | $\mathbf P$ | complex continuous matrix | Common and private BS beamforming vectors |
| Aerial-IRS placement | $\mathbf q$ | continuous feasible position | UAV-mounted IRS hovering location |
| Common-rate allocation | $\mathbf r$ | continuous, $r_k\ge0$ | Common-stream rate assigned to each user |
| IRS phase vector | $\boldsymbol\varphi$ | complex unit-modulus entries | Passive phase applied by each IRS element |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 18a | Allocated common rates are decodable within the common-stream rate |
| 18b | $r_k+R_k^p\ge R_k^{\mathrm{th}}$ for every user |
| 18c | Each IRS coefficient satisfies $\lvert\varphi_m\rvert=1$ |
| 18d | Common-rate allocations satisfy $r_k\ge0$ |
| 18e | BS transmit power satisfies $\operatorname{tr}(\mathbf P^H\mathbf P)\le P_{\max}$ |

**Algorithm**: Initialize precoders, phases, and placement from channel structure → alternate precoder/common-rate, IRS-phase, and aerial-placement blocks → use SCA and quadratic transforms for fractional and rate terms → lift the IRS phase matrix and apply sequential rank-one relaxation → repeat the BCD loop to a stationary point.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Mihertie et al. [x] studied communication-centric energy-efficiency maximization for a UAV-mounted IRS-assisted multi-user MISO downlink with rate-splitting multiple access and practical hardware impairments. They formulated a non-convex problem that jointly optimizes RSMA precoders, common-rate allocation, IRS phase shifts, and the aerial-IRS placement point under minimum-rate, transmit-power, and unit-modulus constraints. Their alternating-optimization framework uses block coordinate descent, successive convex approximation, quadratic transformation, and sequential rank-one relaxation. The resulting sequence is designed to converge monotonically to a stationary point. Simulations report higher energy efficiency for the proposed RSMA design than the evaluated NOMA and SDMA baselines, including reported values of 2.20 for RSMA and 1.65 for NOMA in the stated two-user setting.

## Problem

A multi-antenna BS serves users only through a UAV-mounted passive surface because direct links are blocked. RSMA interference management, surface phases, deployment position, rate constraints, and residual RF distortion must be coordinated under a BS power cap.

## System model

- One MISO BS communicates with multiple single-antenna users through a UAV-mounted IRS; direct BS-user paths are blocked.
- BS-IRS and IRS-user links use Rician fading. One-layer RSMA sends one common stream plus private streams; each user decodes the common stream before its private stream.
- Aggregate transmitter and receiver impairments are modeled as signal-dependent Gaussian distortion.
- The optimized aerial variable is a deployment/hovering point rather than a time-indexed trajectory; simulation fixes height at 100 m.
- Energy efficiency divides sum rate by amplifier-scaled BS transmit power plus BS, user, and per-element IRS circuit power. Propulsion and battery energy are excluded.

## Method

The outer BCD loop alternates three SCA-based blocks. It optimizes precoders and common-rate allocation, lifts the IRS phase vector into a semidefinite matrix and applies sequential rank-one constraint relaxation, and updates aerial placement inside a local trust region. The paper claims monotonic improvement to a local/stationary solution, not a global optimum.

## Key findings

- The reported energy-efficiency sequence stabilizes within about ten outer iterations.
- From two to five users, the prose reports an RSMA increase of `21.8%`, compared with `10.1%` for NOMA and `1.8%` for SDMA.
- At two users, RSMA is reported at `2.20` versus `1.65` for NOMA, a `33.7%` advantage under that setup.
- At `45` BS antennas, the prose reports RSMA, NOMA, and SDMA values of `12.08`, `9.17`, and `9.29`, respectively; the paper's unit labels vary across figures.

## Limitations / parse caveats

The evaluation is simulation-only and assumes perfect cascaded CSI, continuous lossless phases, blocked direct links, fixed height, and two to five users. It optimizes one placement point and excludes propulsion/battery energy, so its metric is communication-centric. The parse alternates between 2-D and 3-D placement and between `SROCR` and `SROCA`; equations and units are damaged. Several prose values in the transmit-power, impairment, and IRS-size studies conflict materially with their extracted plots and are not promoted here. The Fig. 6 explanation invokes reflection loss and channel-estimation error even though the setup assumes ideal amplitude and perfect CSI.

## Relation to the corpus

This source makes [[rate-splitting-multiple-access]] the interference-management layer of a passive [[uav-mounted-ris]] downlink. It differs from [[pan-2025-uav-ris-energy-efficient-comm]], which includes UAV energy and discrete phases in a multi-objective multi-UAV design, and from the learned active-RIS/NOMA controller in [[morshed-2026-active-ris-uav-noma-mappo]].

## Raw artifacts

- Parse: `raw/sources/Energy_Efficiency_Maximization_for_Aerial_Intelligent_Reflecting_Surface-Assisted_MISO_Systems/Energy_Efficiency_Maximization_for_Aerial_Intelligent_Reflecting_Surface-Assisted_MISO_Systems.md`
- Origin PDF: `raw/sources/Energy_Efficiency_Maximization_for_Aerial_Intelligent_Reflecting_Surface-Assisted_MISO_Systems/Energy_Efficiency_Maximization_for_Aerial_Intelligent_Reflecting_Surface-Assisted_MISO_Systems.pdf`
- Figures: `raw/sources/Energy_Efficiency_Maximization_for_Aerial_Intelligent_Reflecting_Surface-Assisted_MISO_Systems/images/`
