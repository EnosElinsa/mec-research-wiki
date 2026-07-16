---
type: source
modeling_card: not_applicable
title: "FMCW-Enabled Integrated Sensing, Identification, and Backscatter Communication for Low-Altitude Economy"
authors: ["Shanxing Zeng", "Ying-Chang Liang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3650197"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, low-altitude-economy, integrated-sensing-and-communication, backscatter-communication, fmcw-radar, cramer-rao-bound, uav-identification]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[backscatter-communication]]"
  - "[[uav-backscatter-identification]]"
  - "[[mmwave-radar-sensing]]"
  - "[[cramer-rao-bound]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[jiang-2025-isac-lae-overview]]"
  - "[[tang-2025-cooperative-isac-lae]]"
created: 2026-07-07
updated: 2026-07-16
---

# FMCW-Enabled Integrated Sensing, Identification, and Backscatter Communication for Low-Altitude Economy

## Citation

Zeng, S., & Liang, Y.-C. (2026). *FMCW-Enabled Integrated Sensing, Identification, and Backscatter Communication for Low-Altitude Economy*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3650197.

## TL;DR

Proposes an **FMCW-enabled integrated sensing, identification, and backscatter communication (ISIBC)** framework for low-altitude economy networks. A ground base station transmits FMCW chirps to estimate each UAV's range and radial velocity, while a passive backscatter device attached to the UAV modulates identity / data symbols onto the reflected echo. The echo model includes both physical UAV surface reflection and BD antenna backscatter, plus synchronization errors. A zero-padded symbol design turns the received signal into a low-rank matrix, enabling an SVD-based two-stage estimator for range, velocity, and BD symbols, with CRLB analysis for the sensing parameters.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zeng and Liang [x] studied FMCW-enabled integrated sensing, identification, and backscatter communication for low-altitude UAV networks. A passive UAV-mounted backscatter device modulates identity and data symbols onto the FMCW echo while the ground station estimates range and radial velocity. Zero-padded symbols produce a low-rank received matrix, and a two-stage SVD estimator recovers sensing parameters and backscatter symbols before refining motion estimates. The paper also derives Fisher-information and Cramer-Rao bounds for range and velocity. Simulations report lower sensing error and bit error rate than the evaluated FFT/MRC and OMP-style estimators, but the paper does not formulate an application-level operational decision model.

## Problem framing

Cellular-connected UAV management needs both sensing and identity. Passive radar echoes reveal a target's motion but not which UAV produced the reflection; conventional communication packets identify the UAV but do not provide radar-grade range / velocity. The paper treats a low-power BD as an "electronic license plate" that can be read from the same FMCW sensing waveform used for localization.

## System model

- **Topology.** One ground base station senses and identifies multiple moving UAVs, each equipped with a backscatter device.
- **Signal.** The base station transmits FMCW chirps; received echoes contain physical surface reflection and BD-modulated antenna backscatter.
- **BD symbols.** BPSK backscatter symbols carry identity and other low-rate data. Zero padding mitigates inter-symbol interference.
- **Assumptions.** Self-interference is assumed removed; clutter is discussed qualitatively but not explicitly modeled in the estimator.
- **Tasks.** Estimate range, radial velocity, the number of UAVs, and BD symbols.

## Method

The paper derives a discrete beat-signal model with synchronization errors, then uses the zero-padded BD pattern to construct a low-rank matrix. For a single UAV, an SVD-based two-stage algorithm first estimates parameters and BD symbols, then removes the BD-symbol component to refine range and velocity. For multiple UAVs, an information-theoretic criterion estimates the number of targets before SVD-based decomposition separates their components. The analysis derives Fisher-information / CRLB expressions for range and velocity.

## Key findings

- In single-UAV simulations at 24 GHz with 500 MHz bandwidth, range RMSE falls below $10^{-2}$ m when SNR exceeds -5 dB, and velocity RMSE falls below $10^{-2}$ m/s when SNR exceeds 0 dB.
- Single-UAV BER reaches about $10^{-3}$ at -5 dB SNR.
- In multi-UAV simulations, range RMSE reaches about $10^{-3}$ m around 0 dB SNR and approaches the CRLB from about -5 dB onward.
- Multiple-UAV BER falls below $10^{-2}$ from roughly -6 dB SNR.
- The SVD-based design outperforms FFT/MRC and OMP-style baselines in the reported sensing and symbol-recovery curves.

## Limitations / future work

The estimator assumes self-interference cancellation and treats clutter qualitatively rather than as an explicit stochastic component. The evaluation is simulation-based; explicit future-work items are `not in parse`.

## Relation to the corpus

This is a **low-altitude sensing / identification** entry rather than a computation-offloading paper. It extends [[integrated-sensing-and-communication]] toward identity-aware UAV management by combining FMCW [[mmwave-radar-sensing]] with [[backscatter-communication]]. Compared with [[jiang-2025-isac-lae-overview]] and [[tang-2025-cooperative-isac-lae]], it focuses less on network architecture and more on the signal model that lets a ground base station both localize and identify low-altitude UAVs.

## Raw artifacts

- `raw/sources/FMCW-Enabled Integrated Sensing- Identification- and Backscatter Communication for Low-Altitude Economy/FMCW-Enabled Integrated Sensing- Identification- and Backscatter Communication for Low-Altitude Economy.md`
- Original PDF and extracted figures (`images/`) in the same folder.
