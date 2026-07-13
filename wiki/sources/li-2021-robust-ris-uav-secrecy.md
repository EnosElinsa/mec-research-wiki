---
type: source
title: "Robust Secure UAV Communications With the Aid of Reconfigurable Intelligent Surfaces"
authors: ["Sixian Li", "Bin Duo", "Marco Di Renzo", "Meixia Tao", "Xiaojun Yuan"]
year: 2021
url: "https://doi.org/10.1109/TWC.2021.3073746"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 20, no. 10, pp. 6402-6417"
tags: [source, uav-communications, intelligent-reflecting-surface, physical-layer-security, robust-optimization, imperfect-csi, trajectory-control]
related:
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
updated: 2026-07-14
---

# Robust Secure UAV Communications With the Aid of Reconfigurable Intelligent Surfaces

## Citation

Li, S., Duo, B., Di Renzo, M., Tao, M., & Yuan, X. (2021). *Robust Secure UAV Communications With the Aid of Reconfigurable Intelligent Surfaces*. **IEEE Transactions on Wireless Communications, 20**(10), 6402-6417. DOI: 10.1109/TWC.2021.3073746.

## TL;DR

Jointly optimizes a UAV trajectory, uplink and downlink transmit powers, and separate RIS phase designs to maximize weighted worst-case bidirectional secrecy under norm-bounded eavesdropper-channel uncertainty.

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
