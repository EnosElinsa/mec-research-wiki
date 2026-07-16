---
type: source
title: "Hybrid OMA/NOMA Mode Selection and Resource Allocation in Space-Air-Ground Integrated Networks"
authors: ["Xun Wang", "Hongbin Chen", "Fangqing Tan"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3452477"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
modeling_card: required
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
updated: 2026-07-16
---

# Hybrid OMA/NOMA Mode Selection and Resource Allocation in Space-Air-Ground Integrated Networks

## Citation

Wang, X., Chen, H., & Tan, F. (2024). *Hybrid OMA/NOMA Mode Selection and Resource Allocation in Space-Air-Ground Integrated Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3452477.

## TL;DR

Studies an uplink **SAGIN** where terminals are served with **hybrid OMA/NOMA** transmission. The authors build a utility function from network characteristics (link, movement, communication resources) and jointly optimize hybrid OMA/NOMA mode selection and power allocation to maximize system utility. The non-convex problem is decomposed into two sub-problems solved by **SCA + Lagrange dual** (power) and a **deep Q-network (DQN)** with a tailored reward (mode selection), combined by an alternating iterative algorithm.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An uplink space-air-ground integrated network has LEO satellites, UAVs, and base stations serving terminals over orthogonal subchannels. Each subchannel can use OMA for one terminal or NOMA for two terminals, with link-specific rate and receiver-complexity utility.

**Problem & objective**: The non-convex formulation $P_0:\max_{\beta,P}\sum_lF_l(\beta,P)$ jointly selects mode and terminal powers to maximize system utility.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Mode selection | $\beta_{u,l,m}$ | binary | OMA or NOMA choice on AP $l$ subchannel $m$ |
| Terminal power | $P_{u,l,m}^{E,L}$ | continuous, $0\le P\le P_{\max}$ | Transmit power under mode $E$ and link $L$ |
| AP utility | $F_l(\beta,P)$ | derived continuous | Rate, complexity, and QoS utility at AP $l$ |
| Mode action | $a_l(t)$ | discrete | DQN action vector corresponding to $\beta$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Binary mode: $\beta_{u,l,m}\in\{0,1\}$ |
| C2 | At most two terminals per subchannel: $\sum_u\beta_{u,l,m}\le2$ |
| C3 | Each terminal uses at most one subchannel: $\sum_m\beta_{u,l,m}\le1$ |
| C4-C5 | Power bounds: $0\le P_{u,l,m}^{E,L}\le P_{\max}$ |
| C6 | NOMA SIC margin: desired received-power difference $\ge\Delta\Gamma$ |

**Algorithm**: With mode fixed, solve the power block by logarithmic SCA and Lagrange dual updates. With power fixed, a DQN observes channel coefficients and receives positive or negative mode-selection rewards; alternate the two blocks until the utility change is below the stopping threshold.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] optimized hybrid OMA and NOMA access for uplink terminals spanning satellite, UAV, and base-station layers of a SAGIN. Their utility combines achievable rate, NOMA receiver complexity, and terminal QoS, with binary mode, multiplexing, subchannel, power, and SIC-margin constraints. They solved continuous power allocation by SCA and Lagrange duality, then trained a DQN to select modes from channel states and alternated the two blocks. Simulations showed higher sum rate and average rate with lower outage probability than fixed OMA, fixed NOMA, and other hybrid baselines.

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
