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
updated: 2026-11-03
---

# GAI-Based Resource Management in RIS-Aided Next-Generation Network and Communication

## Citation

Wu, Z., Zhang, H., Li, L., Lu, Y., & Yang, J. (2025). *GAI-Based Resource Management in RIS-Aided Next-Generation Network and Communication*. **IEEE Transactions on Cognitive Communications and Networking**, 11(2). DOI: 10.1109/TCCN.2024.3519384. (Received 25 June 2024; accepted 8 December 2024; published 17 December 2024; current version 9 April 2025.)

## TL;DR

Proposes a **generative AI (GAI) + distributional RL (DBRL)** framework for resource management in RIS-aided 6G networks. A **channel distribution learning (CDL)** method handles BS-RIS-device cascade channel estimation across diverse devices/scenarios. GANs are used to model the action-value distribution in DBRL (replacing the standard scalar value function with a distributional form), enabling on-demand resource allocation that jointly maximizes **energy efficiency (EE) and QoS satisfaction rate (QoSSR)**. Paper claims to be the first GAI-based resource management work for RIS-aided next-generation networks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An $M$-antenna BS reaches single-antenna devices in $R$ communication service scenarios (scenario $r$ has $K_r$ devices) only through an $N$-element RIS, because a building blocks the direct path. Devices estimate the cascaded BS-RIS-device channel with a DNN, and the BS preallocates bandwidth and power across scenarios with different packet demands.

**Problem & objective**: Problem P0 in (16) maximizes the system utility $J=c_1\mathrm{EE}+\sum_rc_2^r\mathrm{QoSSR}^r$ in (15), a weighted sum of energy efficiency and per-scenario QoS satisfaction ratio.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Scenario bandwidth | $B^r$ | continuous, $\sum_rB^r=B$ | Bandwidth preallocated to scenario $r$ |
| Device power | $p_k^r$ | continuous, nonnegative | BS power for device $k$ in scenario $r$ |
| BS beamformer | $\mathbf w_k$ | complex unit vector | Precoder for device $k$ |
| RIS coefficient | $v_n=\beta_n(\varphi_n)e^{j\varphi_n}$ | discrete set $V$ | Phase-dependent-amplitude reflection of element $n$ |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| C1 | Channel estimate from the DNN: $\hat{\mathbf h}_k^r=f_\theta(\mathbf y_k^{r,p})$ |
| C2 | RIS reflection model: $v_n=\beta_n(\varphi_n)e^{j\varphi_n}$ |
| C3 | Discrete RIS coefficient set: $v_n\in V$ |
| C4 | Unit beamformer: $\lVert\mathbf w_k\rVert^2=1$ |
| C5 | Bandwidth: $\sum_rB^r=B$ |
| C6 | BS power: $\sum_{r,k}p_k^r\le P$ |
| C7 | Demand count of scenario $r$: $\sum_{k\in K_r}\lvert Q_k\rvert=d^r$ |
| C8 | Packet $q_k$ succeeds ($x_{q_k}=1$) only if $R_k^r\ge\bar R^r$ and $l_{q_k}\le\bar l^r$ |

**Algorithm**: Channel distribution learning (CDL) trains a DNN on pilot observations with LS-based labels to estimate cascaded channels. A GAN-based distributional RL agent (Wasserstein GAN with gradient penalty as the return-distribution model) then selects resource actions from the estimated state, clips the utility $J$ into a reward, and trains generator and discriminator from a replay buffer.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] studied generative-AI-based resource management in RIS-aided next-generation networks. They formulated a weighted energy-efficiency and QoS-satisfaction utility over scenario bandwidth, BS power, beamforming, and discrete RIS reflection coefficients under bandwidth, power, demand, and packet-success constraints. A channel distribution learning stage estimates cascaded BS-RIS-device channels for heterogeneous devices and service scenarios. Their distributional reinforcement-learning stage uses generative adversarial networks to model the return distribution rather than only its expectation. Simulations show lower channel-estimation RMSE than LS and MMSE estimation, especially at low SNR, and study utility, energy efficiency, and QoS satisfaction across bandwidth, threshold, packet-size, and batch-size settings; no other resource-allocation scheme is compared.

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

- `raw/sources/GAI-Based_Resource_Management_in_RIS-Aided_Next-Generation_Network_and_Communication/GAI-Based_Resource_Management_in_RIS-Aided_Next-Generation_Network_and_Communication.md`
- Original PDF and extracted figures (`images/`) in the same folder.
