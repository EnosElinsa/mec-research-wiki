---
type: synthesis
title: "ISAC and sensing in aerial MEC"
tags: [synthesis, isac, sensing, physical-layer-security, comparison]
related:
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[jiang-2025-isac-lae-overview]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[faisal-2025-cgan-ris-isac-channel]]"
  - "[[zhang-2025-gan-td3-isac-active-ris]]"
  - "[[tang-2024-iscc-uav-feel]]"
  - "[[yao-2025-secure-isac-dual-eavesdropping]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[physical-layer-security]]"
  - "[[ao-sdr-sca-convex-pipeline]]"
created: 2026-05-30
updated: 2026-05-30
---

# ISAC and sensing in aerial MEC

Seven curated sources fold **sensing** into the aerial communication/compute stack. They span two surveys, two generative-AI channel/beamforming methods, two convex-optimization secure-ISAC designs, and one ISCC (integrated sensing-computation-communication) MEC design. This page maps how "sensing" enters each design and what solver each uses.

## Roster

| Source | Venue / year | Type | Sensing's role | Core method |
|---|---|---|---|---|
| [[meng-2024-uav-isac-overview]] | IEEE Wireless Communications 2024 | Survey | Frames UAV-ISAC for 6G (motion control + S&C synergy) | — |
| [[jiang-2025-isac-lae-overview]] | IEEE Communications Magazine 2025 | Survey | ISAC for low-altitude economy (IAGN, MBCM channel) | Stochastic-geometry analysis |
| [[tang-2024-iscc-uav-feel]] | TWC 2024 | Method (ISCC) | Sensing + compute + comm jointly for federated edge learning | AO (BBPO) |
| [[benaya-2025-aerial-isac-haps]] | TGCN 2025 | Method (secure ISAC) | HAPS full-duplex ISAC + friendly-jamming UAV | [[ao-sdr-sca-convex-pipeline\|AO + SDR + SCA]] |
| [[yao-2025-secure-isac-dual-eavesdropping]] | LWC 2025 | Method (secure ISAC) | Secrecy + sensing security vs dual eavesdroppers | AO + SCA + SDR |
| [[faisal-2025-cgan-ris-isac-channel]] | TCOMM 2025 | Method (GenAI) | Channel estimation for RIS-assisted ISAC | Conditional GAN |
| [[zhang-2025-gan-td3-isac-active-ris]] | IoT-J 2025 | Method (GenAI) | Beamforming for ISAC with double active RIS | GAN-enhanced TD3 |

## Two ways sensing enters the design

### 1. Sensing as a co-optimized objective (ISAC / ISCC)

In [[tang-2024-iscc-uav-feel]], [[benaya-2025-aerial-isac-haps]], and [[yao-2025-secure-isac-dual-eavesdropping]], sensing performance (beampattern gain, sensing SNR, or sensing secrecy) is a term in the objective or a constraint alongside communication/compute. These three are the "true ISAC-MEC" sources: the radar and the data link share the waveform/aperture, so the optimizer must trade them off.

- [[tang-2024-iscc-uav-feel]] adds **computation** to the mix (ISCC) — sensing feeds a federated-edge-learning workload, so the trade is three-way.
- [[benaya-2025-aerial-isac-haps]] and [[yao-2025-secure-isac-dual-eavesdropping]] add **security** — a friendly jammer / secrecy-rate term, solved with the same convex scaffold.

### 2. Sensing as the thing the channel model must capture (GenAI)

[[faisal-2025-cgan-ris-isac-channel]] and [[zhang-2025-gan-td3-isac-active-ris]] don't trade sensing against comm directly; they use **generative models** to handle the hard ISAC channel — a conditional GAN to estimate the RIS-assisted ISAC channel, and a GAN-enhanced TD3 to beamform with double active RIS. Sensing here is a property of the propagation environment the generative model learns.

## Solver convergence: the AO + SDR + SCA pipeline

The two secure-ISAC sources ([[benaya-2025-aerial-isac-haps]], [[yao-2025-secure-isac-dual-eavesdropping]]) and the ISCC source ([[tang-2024-iscc-uav-feel]]) all reduce their non-convex joint beamforming/trajectory/resource problems to an **alternating-optimization loop with semidefinite relaxation and successive convex approximation** for the per-block subproblems. This recurring protocol is captured as a methodology page: [[ao-sdr-sca-convex-pipeline]].

## Gaps

- **No source co-optimizes sensing with a DRL controller AND a convex inner solver** — the ISAC sources are convex-first, the generative sources are learning-first, but none combines a Lyapunov/DRL outer loop (common in the rest of the corpus) with the ISAC convex inner block.
- **The two surveys frame far more than the five method papers cover** — e.g. cooperative multi-static sensing, sensing-assisted handover. The method sources are all single-platform or single-HAPS.
- **Sensing-security is only studied via physical-layer secrecy** ([[physical-layer-security]]); no source addresses spoofed-sensing or adversarial-target attacks.
