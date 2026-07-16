---
type: source
modeling_card: required
title: "GAI-Based Resource Management in RIS-Aided Next-Generation Network and Communication"
authors: ["Zijun Wu", "Haijun Zhang", "Linpei Li", "Yang Lu", "Jian Yang"]
year: 2025
url: "https://doi.org/10.1109/TCCN.2024.3519384"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
tags: [source, ris, resource-management, generative-ai, distributional-reinforcement-learning, channel-estimation, 6g, energy-efficiency]
related:
  - "[[haijun-zhang]]"
  - "[[active-ris]]"
  - "[[generative-diffusion-model]]"
  - "[[distributional-reinforcement-learning]]"
  - "[[graph-based-resource-management]]"
created: 2026-06-04
updated: 2026-07-16
---

# GAI-Based Resource Management in RIS-Aided Next-Generation Network and Communication

## Citation

Wu, Z., Zhang, H., Li, L., Lu, Y., & Yang, J. (2025). *GAI-Based Resource Management in RIS-Aided Next-Generation Network and Communication*. **IEEE Transactions on Cognitive Communications and Networking**, 11(2). DOI: 10.1109/TCCN.2024.3519384. (Received 25 June 2024; accepted 8 December 2024; published 17 December 2024; current version 9 April 2025.)

## TL;DR

Proposes a **generative AI (GAI) + distributional RL (DBRL)** framework for resource management in RIS-aided 6G networks. A **channel distribution learning (CDL)** method handles BS-RIS-device cascade channel estimation across diverse devices/scenarios. GANs are used to model the action-value distribution in DBRL (replacing the standard scalar value function with a distributional form), enabling on-demand resource allocation that jointly maximizes **energy efficiency (EE) and QoS satisfaction rate (QoSSR)**. Paper claims to be the first GAI-based resource management work for RIS-aided next-generation networks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna BS serves multiple service classes through one RIS when direct BS-device paths are blocked. Distributed channel-distribution learners estimate cascaded BS-RIS-device channels, and an online controller allocates radio resources for heterogeneous QoS demands.

**Problem & objective**: A stochastic RIS resource-management problem maximizes a joint utility, $\max \lambda\,\mathrm{EE}+(1-\lambda)\,\mathrm{QoSSR}$, over power, bandwidth, beamforming, and RIS phase shifts.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| BS transmit power | $p_k$ | continuous, bounded | Power allocated to device $k$ |
| Bandwidth share | $b_k$ | continuous, nonnegative | Spectrum allocated to a service request |
| BS beamformer | $\mathbf w_k$ | complex continuous vector | Precoder for device $k$ |
| RIS phase | $\theta_n$ | continuous, $[0,2\pi)$ | Phase shift of RIS element $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Total bandwidth allocation does not exceed available spectrum |
| C2 | BS power and beamforming satisfy the transmit-power budget |
| C3 | Every RIS element has unit amplitude and a feasible phase |
| C4 | Device rates and service outcomes determine QoS satisfaction |
| C5 | Resource decisions use the estimated cascaded channel state |

**Algorithm**: Estimate device-specific cascaded channels with distributed CDL networks → represent the action-value return distribution with a GAN-based distributional critic → sample power, bandwidth, beamforming, and phase actions → update the policy from energy-efficiency and QoS-satisfaction reward → repeat as users and service classes change.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] studied generative-AI-based resource management in RIS-aided next-generation networks. They formulated a joint energy-efficiency and QoS-satisfaction utility over BS power, bandwidth, beamforming, and RIS phase decisions under radio-resource and QoS constraints. A channel distribution learning stage estimates cascaded BS-RIS-device channels for heterogeneous devices and service scenarios. Their distributional reinforcement-learning stage uses generative adversarial networks to model the return distribution rather than only its expectation. Simulations report higher system utility and improved channel-estimation performance relative to the evaluated conventional estimation, scalar-value learning, and fixed-RIS baselines.

## Problem framing

6G RIS-aided networks face two intertwined challenges: (i) cascade channel estimation is expensive — with N RIS elements, pilot overhead scales as Q ≥ NM, prohibitive for massive RIS; (ii) resource allocation (bandwidth, phase shifts, BS transmit power, beamforming) across diverse service types must adapt in real-time to dynamic user demands. Existing AI approaches (DRL, graph-NN) treat resource management separately from channel estimation, and use scalar Q-functions that lose distributional information about returns. This paper integrates CDL for channel estimation with GAI-DBRL for resource allocation.

## System model

- **BS** with M antennas + **RIS** with N reflective elements + R communication service scenarios, each with K_r single-antenna devices.
- **Cascade channel:** BS→RIS (h₁ ∈ C^{N×M}) and RIS→device (h₂,k^r ∈ C^{N×1}). Direct path blocked by buildings.
- **CDL:** DNN-based estimator trained per device/scenario to estimate the cascade channel; distributed (each device estimates from local pilots), reducing pilot overhead significantly.
- **GAI-DBRL:** GANs replace the standard critic by approximating the full return distribution rather than just its expectation; this distributional form enhances the agent's ability to distinguish risk-sensitive resource allocations across diverse service types.
- **Objective:** maximize joint system utility = combination of EE and QoSSR, subject to bandwidth, phase-shift, power, and QoS constraints.

## Method

1. **CDL** phase: DNN-based cascade channel estimation fitted per device/scenario; reduces pilot overhead vs. LS baseline.
2. **DBRL** phase: GANs model the distributional action-value function; policy selects BS transmit power, RIS phase shifts, and beamforming coefficients per slot.
3. Validated by simulation and numerical analysis across multiple scenario configurations.

## Key findings

- The proposed algorithm **significantly improves system utility** (joint EE + QoSSR) compared to baselines (standard DRL without distributional GAI, fixed-phase RIS) in simulation (parse Abstract, Section IV).
- CDL-based channel estimation improves accuracy and reduces pilot overhead compared to classical LS estimation (parse Section III).
- DBRL-GAI combination enhances adaptability to changes in user count, channel conditions, and service-type diversity — continuous high-efficiency operation is demonstrated (parse Section III-B).

## Limitations / future work

Parse does not report explicit numerical gains (e.g., %-improvement over baselines) in readable tables — figures referenced but tables not extracted. Single-RIS, single-BS topology. Haijun Zhang is the corresponding author; this is the same Haijun Zhang affiliation as [[wang-2025-maddpg-lc-dynamic-trajectory]] — flag for entity-page author identity confirmation.

## Relation to the corpus

Connects [[distributional-reinforcement-learning]] with GAI (GAN) for RIS resource management — a combination not previously used in the corpus's RIS papers. Relates to the GAI-for-network-optimization survey [[khoramnejad-2025-gai-wireless-optimization-survey]] and the GDM tutorial [[du-2024-gdm-network-optimization-tutorial]], but focuses on GANs for distributional Q-function rather than diffusion models. The RIS + 6G framing complements [[wu-2025-iopo-irs-uav-thz-mec]] (IRS in THz MEC) and the IRS-beamforming corpus entries.

## Raw artifacts

- `raw/sources/GAI-Based_Resource_Management_in_RIS-Aided_Next-Generation_Network_and_Communication/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
