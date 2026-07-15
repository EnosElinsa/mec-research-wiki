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
  - "[[zhu-2024-sensing-comm-doppler-uav-swarm]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[physical-layer-security]]"
  - "[[ao-sdr-sca-convex-pipeline]]"
  - "[[gai-generator-vs-optimizer-in-isac]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
created: 2026-05-30
updated: 2026-07-14
---

# ISAC and sensing in aerial MEC

A bounded cross-section of seven curated sources folds **sensing** into the aerial communication/compute stack. It spans two surveys, two generative-AI channel/beamforming methods, two convex-optimization secure-ISAC designs, and one ISCC (integrated sensing-computation-communication) MEC design. This page maps how sensing enters those seven designs and what solver each uses; it is not an inventory of every later ISAC page in the corpus.

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

In [[tang-2024-iscc-uav-feel]], [[benaya-2025-aerial-isac-haps]], and [[yao-2025-secure-isac-dual-eavesdropping]], sensing performance (beampattern gain, sensing SNR, or sensing secrecy) is a term in the objective or a constraint alongside communication/compute. Within this seven-source roster, these three directly co-optimize sensing with communication or computation: the radar and the data link share the waveform/aperture, so the optimizer must trade them off.

- [[tang-2024-iscc-uav-feel]] adds **computation** to the mix (ISCC) — sensing feeds a federated-edge-learning workload, so the trade is three-way.
- [[benaya-2025-aerial-isac-haps]] and [[yao-2025-secure-isac-dual-eavesdropping]] add **security** — a friendly jammer / secrecy-rate term, solved with the same convex scaffold.

### 2. Sensing as the thing the channel model must capture (GenAI)

[[faisal-2025-cgan-ris-isac-channel]] and [[zhang-2025-gan-td3-isac-active-ris]] don't trade sensing against comm directly; they use **generative models** to handle the hard ISAC channel — a conditional GAN to estimate the RIS-assisted ISAC channel, and a GAN-enhanced TD3 to beamform with double active RIS. Sensing here is a property of the propagation environment the generative model learns. How those two generative methods relate to the GAI-as-decision sources elsewhere in the corpus is mapped in [[gai-generator-vs-optimizer-in-isac]].

## Function coupling: where computation does and doesn't enter

"Sensing + communication" is the common denominator, but only one method in the seven-source roster folds **computation/offloading** into the same optimization. The table groups the rostered method papers by which functions they actually couple and uses Zhu only as an adjacent comparator outside that roster:

| Functions coupled | What is jointly optimized | Sources |
|---|---|---|
| **Sensing + communication** (two-function) | Beampattern / sensing SNR / CRB vs rate or secrecy — no compute workload | **Rostered methods:** [[benaya-2025-aerial-isac-haps]] / [[yao-2025-secure-isac-dual-eavesdropping]] (secrecy + sensing), [[faisal-2025-cgan-ris-isac-channel]] / [[zhang-2025-gan-td3-isac-active-ris]] (channel/beamforming). **Adjacent comparator outside the seven-source roster:** [[zhu-2024-sensing-comm-doppler-uav-swarm]] (min-max CRLB under SNR-loss). |
| **Sensing + computation + communication** (tri-function, ISCC) | Sensing quality feeds a compute workload whose latency/accuracy is the objective | [[tang-2024-iscc-uav-feel]] only |

The seven-source roster supports the first and third takeaways below; the second uses Zhu only as an adjacent out-of-roster comparator:

- [[tang-2024-iscc-uav-feel]] is the **only tri-function source in this seven-source roster**. Its [[integrated-sensing-computation-communication|ISCC]] formulation links UAV deployment to sensing quality (elevation angle → data-sample quality), bounds federated-edge-learning training loss via successful-sensing probability, and minimizes total training time by jointly optimizing deployment plus bandwidth/batch-size/position (the BBPO alternating-optimization scheme). Sensing, computation, and communication compete for the same onboard resources, so the trade is genuinely three-way.
- **Outside the seven-source roster**, [[zhu-2024-sensing-comm-doppler-uav-swarm]] is the clearest adjacent **sensing + communication-only** comparator: it co-designs the Doppler-driven sensing-vs-communication trade-off (min-max CRLB under an SNR-loss constraint) for a UAV-swarm vehicular network, with **no MEC offloading** — sensing and a data link, nothing computed at the edge.
- The secure-ISAC ([[benaya-2025-aerial-isac-haps]], [[yao-2025-secure-isac-dual-eavesdropping]]) and generative ([[faisal-2025-cgan-ris-isac-channel]], [[zhang-2025-gan-td3-isac-active-ris]]) designs likewise optimize sensing and communication (often with a secrecy/security axis) but carry no compute/offloading objective.

Within the seven-source roster, the tri-function coupling gap is pronounced: sensing is fused with communication and, in the secure designs, security, while computation joins the sensing optimization only in Tang's source. This is the sensing-side counterpart to the [[collaborative-beamforming-in-aerial-mec|collaborative-beamforming]] observation that its reviewed CB sources carry no compute/offloading objective.

## Solver convergence: the AO + SDR + SCA pipeline

The two secure-ISAC sources ([[benaya-2025-aerial-isac-haps]], [[yao-2025-secure-isac-dual-eavesdropping]]) and the ISCC source ([[tang-2024-iscc-uav-feel]]) all reduce their non-convex joint beamforming/trajectory/resource problems to an **alternating-optimization loop with semidefinite relaxation and successive convex approximation** for the per-block subproblems. This recurring protocol is captured as a methodology page: [[ao-sdr-sca-convex-pipeline]].

## Observation-control boundary

This roster is organized by coupled functions and solvers. [[aerial-observation-control-covertness-surveillance-and-monitoring]] supplies a different reader path across covert activity detection, authorized suspicious-link interception, camera-based physical monitoring, and echo-based trajectory tracking. It keeps detection error, monitoring success probability, secrecy rate, service throughput, and tracking error separate even when systems share sensing waveforms, UAV motion, jamming, or reconfigurable surfaces.

## Gaps

- **No source in this seven-paper cross-section co-optimizes sensing with a DRL controller and a convex inner solver** — the secure/ISCC sources are convex-first and the generative sources are learning-first.
- **The two surveys frame far more than the five method papers cover** — e.g. cooperative multi-static sensing, sensing-assisted handover. The method sources are all single-platform or single-HAPS.
- **Within the roster, sensing-security is studied through physical-layer secrecy** ([[physical-layer-security]]); none of the seven sources addresses spoofed-sensing or adversarial-target attacks.
