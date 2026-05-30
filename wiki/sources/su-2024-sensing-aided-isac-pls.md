---
type: source
title: "Sensing-Assisted Eavesdropper Estimation: An ISAC Breakthrough in Physical Layer Security"
authors: ["Nanchi Su", "Fan Liu", "Christos Masouros"]
year: 2024
url: "https://doi.org/10.1109/TWC.2023.3306029"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, physical-layer-security, cramer-rao-bound, secrecy-rate, artificial-noise, beamforming]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[physical-layer-security]]"
  - "[[cramer-rao-bound]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[yao-2025-secure-isac-dual-eavesdropping]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[wang-gai-isac-physical-layer]]"
created: 2026-05-31
updated: 2026-05-31
---

# Sensing-Assisted Eavesdropper Estimation: An ISAC Breakthrough in Physical Layer Security

## Citation

Su, N., Liu, F., & Masouros, C. (2024). *Sensing-Assisted Eavesdropper Estimation: An ISAC Breakthrough in Physical Layer Security*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3306029. (Manuscript received 15 Oct 2022; date of publication 23 Aug 2023; date of current version 11 Apr 2024.)

## TL;DR

A **sensing-aided physical-layer-security (PLS)** scheme for ISAC systems. A well-known limitation of PLS is needing information about potential eavesdroppers (Eves); the paper uses the **sensing** functionality of ISAC to estimate Eves' directions. The dual-functional base station first emits an **omnidirectional waveform** to detect Eves via the **combined Capon and approximate maximum likelihood (CAML)** technique, then formulates a **weighted optimization** that simultaneously maximizes the **secrecy rate** (aided by **artificial noise, AN**) and minimizes the **Cramér-Rao Bound (CRB)** of targets'/Eves' estimation. Because the secrecy-rate expression is a function of estimation accuracy, sensing and security improve each other across iterations until convergence.

## Problem framing

In mmWave ISAC, the shared spectrum + broadcast nature of transmission makes security hard: Rician channels couple the LoS communication channel to the sensing channel (breaking the i.i.d. legitimate-vs-eavesdrop-channel assumption of classical PLS), and confidential data embedded in radar probing signals is susceptible to interception by the very targets being illuminated. PLS conventionally needs Eve channel/location knowledge — which is exactly what sensing can supply.

## System model

- **Actors.** A dual-functional access point / base station (communication + radar), cooperative communication users (CUs, whose locations are known), and potential eavesdroppers (Eves) that are also sensing targets.
- **Stage 1 — detection.** Emit an omnidirectional waveform; receive echoes from CUs and Eves; remove known CU angles to obtain Eve angle estimates, with accuracy measured by the **CRB** ([[cramer-rao-bound]]).
- **Stage 2 — secure beamforming.** Formulate a weighted problem to minimize the CRB of targets/Eves and maximize the secrecy rate, subject to a wide-main-beam beampattern constraint (width set by estimation accuracy) and a transmit-power budget.
- **Robustness.** Eve-location uncertainty is handled by widening the sensing beampattern's main beam to cover the angular region where an Eve may appear, indicated by the previous iteration's CRB.

## Method

- **CAML** (combined Capon + approximate maximum likelihood) for Eve angle estimation.
- An **alternating optimization** algorithm that iteratively maximizes the determinant of the **Fisher Information Matrix (FIM)** and the secrecy rate with the aid of AN; the secrecy rate is updated as Eve-angle estimation accuracy improves ([[alternating-optimization-sdr-sca]] family).
- A **fractional programming (FP)** algorithm to solve the weighted optimization problem, verified for both single-Eve and multi-Eve detection ([[fractional-programming-dinkelbach]]).
- Analytical lower bound on CRB and upper bound on secrecy rate are derived.

## Key findings

- Numerical results show the secrecy rate is **enhanced as the CRB decreases**, in both single-Eve and multi-Eve scenarios — i.e. better sensing accuracy yields better security, the paper's central "mutual benefit" claim (specific curves in the paper).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work; the study is a (non-UAV) terrestrial ISAC base-station design, evaluated by simulation.

## Relation to the corpus

A **sensing-aided PLS** anchor for the wiki's ISAC/security thread, distinct from the UAV-mounted secure-ISAC work [[yao-2025-secure-isac-dual-eavesdropping]] (which optimizes a UAV trajectory + beamforming against a dual-functional eavesdropper). Here there is no UAV — the novelty is using radar sensing to *estimate the eavesdropper* and feeding that into PLS. Framed conceptually by the UAV-ISAC overview [[meng-2024-uav-isac-overview]] and the GAI-for-ISAC physical-layer survey [[wang-gai-isac-physical-layer]]. Introduces and reinforces [[cramer-rao-bound]] as the sensing figure of merit, alongside [[physical-layer-security]] and [[integrated-sensing-and-communication]].

## Raw artifacts

- `raw/sources/Sensing-Assisted_Eavesdropper_Estimation_An_ISAC_Breakthrough_in_Physical_Layer_Security/full.md`
- Original PDF and extracted figures in the same folder.
