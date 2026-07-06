---
type: source
title: "Joint Beamforming and Reflection Design for Secure RIS-ISAC Systems"
authors: ["Jinjin Chu", "Zhiping Lu", "Rang Liu", "Ming Li", "Qian Liu"]
year: 2024
url: "https://doi.org/10.1109/TVT.2023.3328192"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, integrated-sensing-and-communication, intelligent-reflecting-surface, physical-layer-security, alternating-optimization-sdr-sca, majorization-minimization, beamforming]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[physical-layer-security]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[majorization-minimization]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[zhang-2025-gan-td3-isac-active-ris]]"
  - "[[su-2024-sensing-aided-isac-pls]]"
  - "[[yao-2025-secure-isac-dual-eavesdropping]]"
created: 2026-06-01
updated: 2026-07-07
---

# Joint Beamforming and Reflection Design for Secure RIS-ISAC Systems

## Citation

Chu, J., Lu, Z., Liu, R., Li, M., & Liu, Q. (2024). *Joint Beamforming and Reflection Design for Secure RIS-ISAC Systems*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2023.3328192. (Correspondence. Manuscript received 18 February 2023; date of publication 27 October 2023; date of current version 14 March 2024 → year 2024.)

## TL;DR

A correspondence on a **secure RIS-aided ISAC** system: a base station with a uniform linear array performs MU-MISO secure communication to $K$ users **and** detects a malicious point target (a potential eavesdropper), with an $N$-element **RIS** deployed near the users to overcome severe channel degradation. A dedicated **sensing signal** is sent alongside the communication signal to boost detection while limiting information leakage. The design **maximizes the radar output SNR** subject to per-user communication SINR, an eavesdropping-SINR ceiling (secure-transmission constraint), the transmit-power budget, and the RIS unit-modulus reflection constraint. The non-convex problem is split by alternating optimization (BCD) and solved with **SDR + fractional programming + majorization-minimization**.

## Problem framing

ISAC's information-carrying dual-functional waveform is at high risk of interception when the sensed target is malicious. Prior PLS-for-ISAC approaches (radar signal as jamming, artificial noise, symbol-level precoding) give limited gain under severe channel fading, especially when users sit in high-pathloss areas. RIS can create a favorable propagation environment and provide extra design DoF, but its potential to improve **radar sensing** performance in *secure* ISAC under bad channels was under-explored.

## System model

- **BS.** $M$ tx/rx antennas (ULA), $M\ge K$; transmits joint radar-communication signal $\mathbf{x}=\mathbf{W}_c\mathbf{s}_c+\mathbf{W}_r\mathbf{s}_r$.
- **RIS.** $N$ passive elements (unit-modulus $|\phi_n|\le1$) near the $K$ single-antenna users; assumes perfect CSI.
- **Target/eavesdropper.** A distant point target that also acts as a single-antenna eavesdropper; RIS-path target echoes neglected (far target).
- **Metrics.** Radar output SNR (objective); per-user communication SINR; eavesdropping SINR capped by a threshold $\Gamma_{e,k}$ for secure transmission.

## Method

Alternating optimization decomposes the non-convex, multivariate-coupled problem into **three subproblems** solved iteratively (Algorithm 1):

1. **Transmit beamforming $\mathbf{W}$** — reformulated with an auxiliary variable and solved via **semi-definite relaxation (SDR)** (drop rank-one, recover by EVD / Gaussian randomization; radar beamformer via Cholesky).
2. **Radar receive filter $\mathbf{u}$** — a Rayleigh quotient with closed-form largest-eigenvector solution.
3. **RIS reflection $\boldsymbol{\phi}$** — a feasibility/lower-bound-maximization handled by **Dinkelbach's fractional-programming transform** + **majorization-minimization** (first-order Taylor surrogate) into a convex update.

## Key findings

- The proposed secure RIS-ISAC scheme offers a **~2 dB radar performance (output SNR) gain compared to the scheme without RIS** (abstract, verbatim).
- Simulation curves (radar SNR vs. transmit power $P$, for $M=8,10$) show the proposed "w/ RIS" design above random-RIS, w/o-RIS, and w/o-receive-filter baselines (figure values are indicative, not asserted as exact).

## Limitations / future work

Perfect CSI is assumed (the authors explicitly note real RIS CSI is hard to obtain with limited overhead) and the target/eavesdropper is a single distant point. As a correspondence, the captured parse does not enumerate explicit future work → `not in parse`.

## Relation to the corpus

A **physical-layer secure-ISAC + RIS** anchor (sensing/security, not MEC). It sits with the ISAC/sensing/PLS track: distinct from [[zhang-2025-gan-td3-isac-active-ris]] (GAN-TD3 with double *active* RIS), [[su-2024-sensing-aided-isac-pls]] (sensing-aided eavesdropper-direction estimation), and [[yao-2025-secure-isac-dual-eavesdropping]] (dual-eavesdropping secrecy). Its AO+SDR+FP+MM pipeline reinforces [[alternating-optimization-sdr-sca]] and introduces the [[majorization-minimization]] surrogate-optimization concept. (Sensing/PLS anchor, not a computation-offloading paper.)

## Raw artifacts

- `raw/sources/Joint_Beamforming_and_Reflection_Design_for_Secure_RIS-ISAC_Systems/Joint_Beamforming_and_Reflection_Design_for_Secure_RIS-ISAC_Systems.md`
- Original PDF and extracted figures (`images/`) in the same folder.
