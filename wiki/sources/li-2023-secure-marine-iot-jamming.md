---
type: source
title: "Secure Computation Offloading for Marine IoT: An Energy-Efficient Design via Cooperative Jamming"
authors: ["Mingqing Li", "Li Ping Qian", "Xinyu Dong", "Bin Lin", "Yuan Wu", "Xiaoniu Yang"]
year: 2023
url: "https://doi.org/10.1109/TVT.2022.3231295"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, maritime-mec, physical-layer-security, cooperative-jamming, noma, monotonic-optimization, energy-latency-tradeoff]
related:
  - "[[maritime-mec]]"
  - "[[physical-layer-security]]"
  - "[[cooperative-jamming]]"
  - "[[noma]]"
  - "[[monotonic-optimization]]"
  - "[[cross-entropy-method]]"
  - "[[two-stage-decomposition]]"
  - "[[high-altitude-platform-station]]"
  - "[[dai-2023-hybrid-marine-mmwl]]"
created: 2026-05-31
updated: 2026-05-31
---

# Secure Computation Offloading for Marine IoT: An Energy-Efficient Design via Cooperative Jamming

## Citation

Li, M., Qian, L. P., Dong, X., Lin, B., Wu, Y., & Yang, X. (2023). *Secure Computation Offloading for Marine IoT: An Energy-Efficient Design via Cooperative Jamming*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2022.3231295. (Manuscript received 1 Jul 2022; date of publication 22 Dec 2022; date of current version 18 May 2023 → year 2023.)

## TL;DR

A secure marine-IoT computation-offloading design where **unmanned surface vehicles (USVs)** offload compute-intensive tasks to an onshore base station via a **high-altitude platform (HAP)** aerial edge server, under eavesdropping attack. USVs are first scheduled to set up a high-quality NOMA uplink to the HAP, then reused to provide **cooperative jamming** (physical-layer security) while the HAP performs offloading. The work minimizes system-wise energy consumption by jointly optimizing USV positions, data-uploading duration, BS-offloaded workload, HAP transmit power, and per-USV jamming power, via a layered decomposition solved by a **Polyblock outer Approximation + bisection Search (PAS)** algorithm and a **Code-bAsed croSs-Entropy (CASE)** algorithm.

## Problem framing

In smart-ocean M-IoT, USVs collect compute-intensive, latency-sensitive data but suffer high transmission energy offloading to distant onshore MEC servers and high local-compute energy. A HAP acts as a nearby portable MEC unit. Because wireless is broadcast, the HAP link is vulnerable to eavesdropping, and there was little prior work on **NOMA-aided secure offloading with cooperative jamming** for M-IoT.

## System model

- **Three phases.** Phase I: USV scheduling (each USV moves from initial to destination position). Phase II: data uploading to HAP via **NOMA** (with SIC). Phase III: secure computation offloading — HAP processes part of the workload and forwards the rest to the onshore BS, while USVs jam the eavesdropper. See [[high-altitude-platform-station]], [[cooperative-jamming]].
- **Objective.** Minimize system-wise energy E_tot (USVs + HAP) under latency constraints, by jointly optimizing USV positions, uploading duration t, BS-offloaded workload S, HAP transmit power p_S, and each USV's jamming power p_{iE}.

## Method

- **Vertical decomposition** into a top problem (USV positions) and a bottom problem (the other variables) — a layered solve ([[two-stage-decomposition]]).
- **PAS-Algorithm:** alternately optimizes the bottom-problem variables using **monotonic optimization** (polyblock outer approximation) + bisection search. See [[monotonic-optimization]].
- **CASE-Algorithm:** searches the top-problem (USV positions) via the **cross-entropy** method, calling PAS for the bottom problem at each step, to get a suboptimal joint solution. See [[cross-entropy-method]].

## Key findings

- Versus a **fixed-jamming** scheme (p_{iE} = 0.28 W for all USVs), the joint optimization reduces total energy consumption by **27.32% on average** (stated verbatim).
- Numerical results validate accuracy/efficiency against an **enumeration** method (near-optimal benchmark) and a **random-selection** method, and show the advantage of flexible cooperative jamming for PLS (stated qualitatively).

## Limitations / future work

Simulation-based. Future work (stated): study more complex scenarios involving **seawater fluctuations** and their consequent influences (and, in the intro, underwater-channel effects).

## Relation to the corpus

A **maritime + physical-layer-security** entry that uniquely combines **NOMA offloading via a HAP** with **USV cooperative jamming**. It shares the maritime-MEC track with the same group's hybrid FDMA/NOMA scheme [[dai-2023-hybrid-marine-mmwl]] (co-authors Liping Qian, Bin Lin, Yuan Wu) and the NOMA-based marine emergency offloading [[lyu-2023-noma-marine-emergency-offloading]]. Its [[monotonic-optimization]]-based PAS solver links it to the MF-RIS work [[sun-2024-mfris-semantic-antijamming]] (both use monotonic optimization for a global solve), and its security framing connects to [[michailidis-2024-secure-ris-uav-mec-iot]]. Introduces the new [[cooperative-jamming]] and [[cross-entropy-method]] concepts; reinforces [[maritime-mec]], [[physical-layer-security]], and [[noma]].

## Raw artifacts

- `raw/sources/Secure_Computation_Offloading_for_Marine_IoT_An_Energy-Efficient_Design_via_Cooperative_Jamming/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
