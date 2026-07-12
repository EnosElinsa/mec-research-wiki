---
type: source
title: "Direction Modulation Design for UAV Assisted by IRS With Discrete Phase Shift"
authors: ["Maolin Li", "Wei Gao", "Qi Wu", "Feng Shu", "Cunhua Pan", "Di Wu"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3572113"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, directional-modulation, intelligent-reflecting-surface, physical-layer-security, discrete-phase-shift, uav-positioning, symbol-level-precoding]
related:
  - "[[directional-modulation]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[physical-layer-security]]"
  - "[[air-to-ground-channel-model]]"
  - "[[cross-entropy-method]]"
  - "[[near-field-communications]]"
created: 2026-07-13
updated: 2026-07-13
---

# Direction Modulation Design for UAV Assisted by IRS With Discrete Phase Shift

## Citation

Li, M., Gao, W., Wu, Q., Shu, F., Pan, C., & Wu, D. (2026). *Direction Modulation Design for UAV Assisted by IRS With Discrete Phase Shift*. **IEEE Transactions on Green Communications and Networking**, 10, 172-186. DOI: 10.1109/TGCN.2025.3572113.

## TL;DR

Uses a passive IRS to preserve intended symbol constellations at ground users while suppressing and phase-scrambling symbols at a multi-antenna eavesdropper. The solver combines robust symbol-level digital weights, a fixed-point UAV-position surrogate, and vector-trajectory rules for discrete IRS phases, including cross-entropy and block-coordinate variants.

## Problem

LoS-dominant UAV links expose intended symbols to nearby eavesdroppers, especially when an eavesdropper lies near a legitimate direction. Continuous IRS phases are difficult to implement, and symbol-level precoding, UAV position, and finite-alphabet phase shifts are tightly coupled. The paper therefore maximizes a lower-bounded legitimate rate while explicitly shaping the constellation at legitimate and unauthorized receivers.

## System model

- One fixed-altitude UAV with an `N`-element ULA serves multiple single-antenna users through direct and passive-IRS paths; one non-colluding ground eavesdropper has multiple antennas.
- Users and Eve lie near the IRS, while UAV-to-ground links are treated as far-field. IRS-to-ground propagation can fall in the [[near-field-communications|near field]].
- Channels combine LoS-dominant terms with weaker NLoS components and distance-dependent loss. The uncertain NLoS-plus-noise term is modeled as complex Gaussian with an upper-bounded variance.
- Symbol-level weights synthesize desired constellation regions at users and low-amplitude disturbed phases at Eve. IRS coefficients have unit amplitude and a finite phase alphabet.

## Method

[[directional-modulation]] first bounds the uncertain channel/noise term and converts the rate lower bound into received-symbol-amplitude maximization. A constructive-interference region and inverse-Gaussian-CDF margin replace strict noisy-symbol phase equality with a robust ideal-channel alignment condition.

For fixed IRS phases, the digital weights follow from a minimum-power equality system. A convex geometric upper-bound surrogate and fixed-point equations produce a feasible, explicitly suboptimal UAV position; an alternating penalty step then scales the symbol weights under the power budget. The vector-trajectory method chooses each discrete IRS phase by minimizing angular error to the desired symbol. CE-VT learns per-element phase probabilities from elite [[cross-entropy-method|cross-entropy]] samples, while BCD-VT enumerates one element's phase alphabet with the other elements fixed.

## Key findings

- Under the stated rank-one LoS assumptions, the paper bounds Eve's degrees of freedom by 2 and the legitimate multi-user side by `1+K_u`, interpreting the IRS as increasing legitimate DoF from `K_u` to `1+K_u`.
- The VT phase-quantization bound is proportional to `sum_m |tau_m| cos(2pi/2^(B_tilde+1))`; with at least one phase bit the stated gain is nonnegative and rises with phase precision.
- In simulation, CE-VT raises average signal power by about `6 dBm` over CE, BCD-VT by about `5.5 dBm` over BCD, and CE-VT with IRS by `31 dBm` over no IRS.
- At the reported `P_max=73.6 dBm` operating point, the three legitimate-user locations receive `-50 dBm` while Eve receives `-110 dBm`.
- CE-VT reaches about three times the no-IRS rate without channel uncertainty; under the uncertain-component setting its improvement is about twice CE and stabilizes near the `50 dBm` maximum-power setting.

## Limitations / parse caveats

The model has one non-colluding point eavesdropper, assumes `K_u<N<M`, passive unit-amplitude elements, a finite phase alphabet, fixed receiver/IRS positions, and LoS-dominant channels with independent Gaussian uncertainty. The position and phase algorithms are suboptimal iterative methods. Evidence is simulation-only. Several equations and constraint labels are OCR-damaged, and an IEEE download timestamp interrupts one sentence; the page retains only prose-backed derivations and clearly labeled numerical findings. The parse explicitly supplies the DOI but not final venue/year/pages; those fields were verified through the exact-title Crossref record.

## Relation to the corpus

This source adds symbol-level [[directional-modulation]] to the corpus's [[physical-layer-security]] and [[intelligent-reflecting-surface]] vocabulary. Unlike secrecy-rate or outage formulations, security is expressed through legitimate and eavesdropper constellation geometry under mixed direct/cascaded [[air-to-ground-channel-model|air-to-ground channels]] and implementable discrete phases.

## Raw artifacts

- Parse: `raw/sources/Direction_Modulation_Design_for_UAV_Assisted_by_IRS_With_Discrete_Phase_Shift/Direction_Modulation_Design_for_UAV_Assisted_by_IRS_With_Discrete_Phase_Shift.md`
- Origin PDF: `raw/sources/Direction_Modulation_Design_for_UAV_Assisted_by_IRS_With_Discrete_Phase_Shift/Direction_Modulation_Design_for_UAV_Assisted_by_IRS_With_Discrete_Phase_Shift.pdf`
- Figures: `raw/sources/Direction_Modulation_Design_for_UAV_Assisted_by_IRS_With_Discrete_Phase_Shift/images/`
