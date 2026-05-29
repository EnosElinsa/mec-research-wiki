---
type: source
title: "Hybrid OMA/NOMA Mode Selection and Resource Allocation in Space-Air-Ground Integrated Networks"
authors: ["Xun Wang", "Hongbin Chen", "Fangqing Tan"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3452477"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, space-air-ground-integrated-network, noma, mode-selection, resource-allocation, deep-q-network]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[noma]]"
  - "[[deep-q-network]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[hsu-2025-drl-hues-hap-noma]]"
  - "[[qin-2025-matd3-noma-queue-sagin]]"
  - "[[li-2025-twohop-airground-drl-offloading]]"
created: 2026-05-29
updated: 2026-05-29
---

# Hybrid OMA/NOMA Mode Selection and Resource Allocation in Space-Air-Ground Integrated Networks

## Citation

Wang, X., Chen, H., & Tan, F. (2024). *Hybrid OMA/NOMA Mode Selection and Resource Allocation in Space-Air-Ground Integrated Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3452477.

## TL;DR

Studies an uplink **SAGIN** where terminals are served with **hybrid OMA/NOMA** transmission. The authors build a utility function from network characteristics (link, movement, communication resources) and jointly optimize hybrid OMA/NOMA mode selection and power allocation to maximize system utility. The non-convex problem is decomposed into two sub-problems solved by **SCA + Lagrange dual** (power) and a **deep Q-network (DQN)** with a tailored reward (mode selection), combined by an alternating iterative algorithm.

## Problem framing

Ground networks can't cover sparsely-populated regions (mountains, oceans, suburbs). SAGIN's global coverage and heterogeneous resources help, but terminals connected to different network tiers benefit from flexibly choosing OMA vs. NOMA; the joint mode-selection + power-allocation problem is non-convex.

## System model

- **Network.** Uplink SAGIN with terminals served by different tiers; hybrid OMA/NOMA transmission.
- **Utility.** Defined from differences in communication link, movement, and communication resources.
- **Objective.** Maximize system utility via joint power allocation and OMA/NOMA mode selection.

## Method

- Decompose into two sub-problems:
  - **Power allocation:** successive convex approximation (SCA) + Lagrange dual method ([[alternating-optimization-sdr-sca]]).
  - **Hybrid OMA/NOMA mode selection:** **DQN**-based algorithm with a reward function designed to guarantee constraints ([[deep-q-network]]).
- Combine via an alternate iterative algorithm.

## Key findings

- The proposed algorithm flexibly selects the suitable transmission mode per connected-network characteristics and beats benchmark schemes in achievable sum rate, average achievable rate, and outage probability (qualitative; specific curves in the paper).

## Limitations / future work

Uplink only. Future work: extend hybrid OMA/NOMA to downlink and uplink SAGIN to enlarge system capacity.

## Relation to the corpus

A **NOMA + SAGIN** entry that complements the NOMA-enabled aerial works [[hsu-2025-drl-hues-hap-noma]] (HAP NOMA + energy harvesting) and [[qin-2025-matd3-noma-queue-sagin]] (NOMA queue-aware AAV trajectory). Its SCA+DQN decomposition is a classic "convex-for-continuous, RL-for-discrete" pattern also seen in [[li-2025-twohop-airground-drl-offloading]]. Reinforces [[noma]], [[deep-q-network]], and [[space-air-ground-integrated-network]].

## Raw artifacts

- `raw/sources/Hybrid_OMA_NOMA_Mode_Selection_and_Resource_Allocation_in_Space-Air-Ground_Integrated_Networks/full.md`
- Original PDF and extracted figures in the same folder.
