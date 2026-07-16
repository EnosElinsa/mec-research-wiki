---
type: source
title: "Robust Secure UAV Communications With the Aid of Reconfigurable Intelligent Surfaces"
authors: ["Sixian Li", "Bin Duo", "Marco Di Renzo", "Meixia Tao", "Xiaojun Yuan"]
year: 2021
url: "https://doi.org/10.1109/TWC.2021.3073746"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 20, no. 10, pp. 6402-6417"
modeling_card: required
tags: [source, uav-communications, intelligent-reflecting-surface, physical-layer-security, robust-optimization, imperfect-csi, trajectory-control]
related:
  - "[[xiaojun-yuan]]"
  - "[[robust-ris-assisted-uav-secrecy]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[physical-layer-security]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[marco-di-renzo]]"
  - "[[meixia-tao]]"
  - "[[feng-2026-aerial-ris-secure]]"
  - "[[xu-2021-secure-uav-mec-dual-uav]]"
created: 2026-07-14
updated: 2026-07-16
---

# Robust Secure UAV Communications With the Aid of Reconfigurable Intelligent Surfaces

## Citation

Li, S., Duo, B., Di Renzo, M., Tao, M., & Yuan, X. (2021). *Robust Secure UAV Communications With the Aid of Reconfigurable Intelligent Surfaces*. **IEEE Transactions on Wireless Communications, 20**(10), 6402-6417. DOI: 10.1109/TWC.2021.3073746.

## TL;DR

Jointly optimizes a UAV trajectory, uplink and downlink transmit powers, and separate RIS phase designs to maximize weighted worst-case bidirectional secrecy under norm-bounded eavesdropper-channel uncertainty.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude rotary-wing UAV and one ground user exchange confidential downlink and uplink data in separate portions of each flight slot. A building-mounted RIS creates controllable reflected paths, while a passive eavesdropper intercepts both directions and its cascaded channels lie in deterministic norm-bounded uncertainty sets.

**Problem & objective**: The robust joint design maximizes $R_{\mathrm{sec}}=\frac{1}{N}\sum_{n=1}^{N}\left[wR_{\mathrm{sec}}^{\mathrm{down}}[n]+(1-w)R_{\mathrm{sec}}^{\mathrm{up}}[n]\right]$, the weighted average worst-case bidirectional secrecy rate.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\mathbf Q$ | continuous horizontal sequence | UAV position over the flight horizon |
| Downlink RIS phases | $\Phi_d$ | continuous phases in $[0,2\pi)$ | Passive beamforming for UAV-to-user transmission |
| Uplink RIS phases | $\Phi_u$ | continuous phases in $[0,2\pi)$ | Passive beamforming for user-to-UAV transmission |
| UAV transmit power | $\mathbf p$ | continuous, average and peak bounded | Downlink power per slot |
| User transmit power | $\mathbf g$ | continuous, average and peak bounded | Uplink power per slot |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV displacement per slot is bounded and initial and final positions are fixed |
| C2 | UAV downlink power satisfies average and peak limits |
| C3 | Ground-user uplink power satisfies average and peak limits |
| C4 | Every uplink and downlink RIS element has a unit-modulus phase in $[0,2\pi)$ |
| C5 | Secrecy is evaluated against the worst channel error in each uncertainty set |

**Algorithm**: Alternating optimization separates closed-form transmit-power control, RIS passive beamforming, and UAV trajectory updates. The RIS block uses the S-procedure, SCA, and semidefinite relaxation with Gaussian randomization, while the trajectory block estimates the current small-scale UAV-RIS channel from the previous path and applies robust SCA until the secrecy objective converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied bidirectional physical-layer security between a UAV and a ground user assisted by a building-mounted RIS under imperfect eavesdropper CSI. They maximized weighted average worst-case uplink and downlink secrecy over trajectory, separate RIS phase matrices, and both legitimate transmit powers under mobility, phase, average-power, and peak-power constraints. Their alternating method combines closed-form power updates with the S-procedure, successive convex approximation, semidefinite relaxation, and robust trajectory refinement. It converged in about 10 iterations and achieved the highest worst-case secrecy rate among the tested benchmark designs as wiretap-channel uncertainty increased.

## Problem and system model

A fixed-altitude rotary-wing UAV and one ground user exchange confidential data while a passive eavesdropper monitors both directions. A building-mounted [[intelligent-reflecting-surface]] assists the single-antenna links. Each flight slot is split by a fixed weight between UAV-to-user downlink and user-to-UAV uplink, with separate continuous RIS phase matrices.

Channels follow Rician fading. Legitimate CSI is assumed perfect, while the cascaded downlink and uplink eavesdropper channels lie in deterministic norm-bounded uncertainty sets. The UAV has fixed initial and final horizontal positions and a maximum per-slot displacement; UAV and user powers have average and peak limits. The objective is the time-average weighted worst-case secrecy rate across both directions.

## Method

[[robust-ris-assisted-uav-secrecy]] alternates among three blocks. The power block derives worst-case channel errors and closed-form slotwise powers, using bisection for average-power dual variables. The RIS block applies the S-Procedure to semi-infinite uncertainty constraints, lifts phase vectors, uses SDR and SCA for convex surrogates, and applies Gaussian randomization when the relaxed matrix is not rank one. The trajectory block freezes the previous iterate's UAV-RIS small-scale LoS component and worst-case wiretap realization, then solves first-order SCA bounds with CVX.

The heuristic-trajectory solution initializes the loop. The resulting [[alternating-optimization-sdr-sca]] procedure is an approximate stationary design; the paper does not claim global optimality.

## Key findings

- With equal uplink/downlink weight, normalized CSI-error variance 0.5, and average UAV and user powers of 20 dBm, the joint optimization converges in about 10 iterations. This is Fig. 2-derived context for the tested setup.
- In Fig. 5, the joint robust design has the highest average worst-case secrecy rate as flight time increases, ahead of robust design without passive beamforming, a preset heuristic trajectory, and a non-robust joint design. No exact percentage gain is available in the parse.
- All methods degrade as normalized eavesdropper-CSI error grows in Fig. 6, but the robust joint design remains highest. At error variance 0.5, the no-passive-beamforming and heuristic-trajectory curves are close; the paper attributes this qualitative figure behavior to large uncertainty making passive beamforming ineffective or counterproductive.
- Figs. 3-4 show joint and non-robust designs following arc-like paths toward a hover point between the user and RIS, while the no-passive-beamforming design moves closer to the user and away from the eavesdropper. Robust trajectories are more dispersed across channel realizations. These are figure-derived trajectory observations, not general geometric guarantees.
- Fig. 7 shows the slot weight changing the path: an uplink-dominant weight of 0.1 balances direct and reflected user-to-UAV gains, while a downlink-dominant weight of 0.9 also avoids the eavesdropper and favors relatively direct final-leg paths. The parse reports qualitative behavior rather than exact secrecy-rate gains.

## Limitations

The model contains one UAV, one user, one eavesdropper, one RIS, fixed altitude, single antennas, TDMA, continuous RIS phases, perfect legitimate CSI, bounded deterministic eavesdropper CSI error, and available centralized control links. It omits channel-estimation overhead, discrete phase quantization, RIS control latency, a moving eavesdropper, and multi-user interference.

The trajectory block reuses the previous iterate's small-scale LoS component and worst-case wiretap realization. SDR may require Gaussian randomization, and the alternating procedure has no global-optimality guarantee. Evidence is simulation-only with no hardware or flight validation. Multi-user extension requires scheduling under orthogonal access and additional interference cancellation under non-orthogonal access.

## Relation to the corpus

This paper is a model-based [[physical-layer-security]] counterpart to learned aerial-RIS control in [[feng-2026-aerial-ris-secure]]. It also complements [[xu-2021-secure-uav-mec-dual-uav]] by protecting bidirectional communication through RIS, trajectory, and power control rather than secure computation offloading with separate UAV roles.

## Raw artifacts

- Parse: `raw/sources/Robust_Secure_UAV_Communications_With_the_Aid_of_Reconfigurable_Intelligent_Surfaces/Robust_Secure_UAV_Communications_With_the_Aid_of_Reconfigurable_Intelligent_Surfaces.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
