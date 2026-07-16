---
type: source
title: "A Robust Multi-Domain Adaptive Anti-Jamming Communication System for a UAV Swarm in Urban ITS Traffic Monitoring via Multi-Agent Deep Deterministic Policy Gradient"
authors: ["Mu Chen", "Yong Li", "Zaojian Dai", "Tao Zhang", "Yu Zhou", "Hui Wang"]
year: 2026
url: "https://doi.org/10.1109/TITS.2025.3584216"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
modeling_card: required
tags: [source, uav-swarm, anti-jamming, its, maddpg, ctde, channel-selection, power-control]
related:
  - "[[multi-domain-uav-anti-jamming]]"
  - "[[uav-enabled-its]]"
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[ma-pomdp]]"
  - "[[spectrum-sensing-channel-selection]]"
  - "[[anti-jamming-mec]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[yang-2026-embodied-antijamming-uav]]"
  - "[[embodied-anti-jamming-resource-allocation]]"
created: 2026-07-10
updated: 2026-07-16
---

# A Robust Multi-Domain Adaptive Anti-Jamming Communication System for a UAV Swarm in Urban ITS Traffic Monitoring via Multi-Agent Deep Deterministic Policy Gradient

## Citation

Chen, M., Li, Y., Dai, Z., Zhang, T., Zhou, Y., & Wang, H. (2026). *A Robust Multi-Domain Adaptive Anti-Jamming Communication System for a UAV Swarm in Urban ITS Traffic Monitoring via Multi-Agent Deep Deterministic Policy Gradient*. **IEEE Transactions on Intelligent Transportation Systems**, 27(2), 2777-2793. DOI: 10.1109/TITS.2025.3584216.

## TL;DR

Models urban ITS monitoring by a UAV swarm under co-channel interference and malicious jamming. The paper formulates joint channel selection and transmit-power control as a Dec-POMDP and trains a MADDPG controller with centralized critics and decentralized actors so each UAV can adapt from local channel/interference observations.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV swarm monitors urban traffic through U2U coordination links and U2G reporting to a ground station in the presence of co-channel interference and fixed, swept, or random jammers. Each UAV observes local channel gain and interference, selects a channel and transmit power, and follows Gaussian-Markov mobility.

**Problem & objective**: The anti-jamming problem minimizes expected long-term weighted transmission energy and frequency-hopping overhead, $\min_{L^t,P^t}\mathbb E\{\sum_{t=0}^{T-1}\sum_{n=1}^{N}[\beta E_n^t+(1-\beta)F_n^t]\}$, while every U2U payload is delivered within a slot.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Channel selection | $L_n^t$ | discrete channel index | Channel chosen by UAV $n$ at slot $t$ |
| Transmit power | $P_n^t$ | continuous, bounded | U2U or U2G transmit power of UAV $n$ |
| Joint action | $a_n^t=[L_n^t,P_n^t,\bar d_n^t]$ | mixed | Channel, power, and mobility decision exposed to the Dec-POMDP |
| Policy | $\mu_n$ | stochastic policy | Local observation to channel-power mapping |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each U2U link delivers its payload: $R_n^{t,l}t\ge K$ for every link and slot. |
| C2 | Transmit powers remain within the platform limits. |
| C3 | Frequency-hopping cost is incurred only when channels change: $F_n^t=g(L_n^t,L_n^{t-1})W$. |
| C4 | Agents act from local observations in decentralized execution, while centralized training may use joint observations and actions. |

**Algorithm**: Model local observations and mixed channel-power actions as a Dec-POMDP, train MADDPG with centralized critics and decentralized actors using replay and target networks, and shape rewards from U2G capacity, U2U success, transmission energy, and hopping penalties under fixed, swept, and random jamming.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] studied anti-jamming communication for an urban-ITS UAV swarm that must coordinate U2U data sharing while reporting through U2G links. They minimized weighted transmission energy and frequency-hopping overhead over channel-selection and transmit-power decisions subject to per-slot U2U payload delivery. A Dec-POMDP and MADDPG centralized-training decentralized-execution controller let local actors adapt to interference while centralized critics learn coordination. In the reported four-UAV experiments, MADDPG stabilized after about 500 episodes, reached roughly 45 Mbps U2G capacity, and outperformed MADQN, single-agent DDPG, PPO, and random baselines in U2U success, energy, and hopping cost.

## Problem

Urban traffic monitoring needs UAV-to-UAV links for swarm coordination and data fusion plus UAV-to-ground links for reporting. Fixed, swept, and random jammers can force frequency hopping and high transmit power, while the UAVs only observe local channel/interference states. A robust controller therefore has to choose channels and powers without full global CSI.

## System model

- The network contains roadside/traffic targets, a UAV swarm, a ground station, and interference or jamming devices.
- The wireless model includes Rayleigh fast fading, path loss, co-channel interference, jammer interference, SINR, and Shannon-rate expressions.
- UAV mobility follows a Gaussian-Markov model.
- Each UAV chooses a channel and U2U transmit power while a fixed U2G reporting link contributes capacity to the reward.
- The objective minimizes long-term weighted transmission energy and frequency-hopping cost while preserving per-slot U2U payload delivery.

## Method

The controller uses MADDPG under centralized training and decentralized execution. Local actors choose channel/power actions from local observations. Centralized critics see joint observations/actions during training, using replay, target networks, Adam, ReLU networks, discounting, and exploration. The reward combines U2G capacity, U2U delivery success, and penalties for transmit energy and frequency hopping.

## Key findings

- The reported simulation uses 4 UAVs, 4 interference devices, 4 U2U links, 2 W U2G power, 0.2 W U2U power, 1 MB U2U packet per slot, 2.4 GHz carrier frequency, and 40 MHz bandwidth.
- Training uses 2000 episodes, 100 max steps per episode, replay size 50000, batch size 64, actor/critic learning rate 0.0001, and discount factor 0.99.
- MADDPG stabilizes after roughly 500 episodes in the parsed curves.
- Total U2G capacity stabilizes around 45 Mbps in the reported setting.
- Against MADQN, single-agent DDPG, single-agent PPO, and random baselines, MADDPG yields higher U2U success, lower transmit power, lower hopping cost, and stronger robustness under swept and random jamming.

## Relation to the corpus

This is adjacent to MEC anti-jamming rather than an offloading formulation: the decision surface is radio resilience for an ITS UAV swarm. It extends [[uav-enabled-its]] from trajectory/service control toward jammed U2U/U2G communications, and it gives [[maddpg]] another CTDE use case outside compute offloading. It complements [[shao-2024-drl-antijamming-mec]], where the protected objective is MEC service quality, and [[liu-2025-multimodal-semantic-iov-jamming]], where the protected content is multi-modal semantic IoV data.

## Limitations / extraction notes

The local Markdown parse is missing top-level DOI, venue, and year; the bibliographic fields above come from the local PDF metadata. The parse corrupts parts of Table I and several equations/algorithm blocks, so the source page avoids over-precise claims from those regions.

## Raw artifacts

- Parse: `raw/sources/A_Robust_Multi-Domain_Adaptive_Anti-Jamming_Communication_System_for_a_UAV_Swarm_in_Urban_ITS_Traffic_Monitoring_via_Multi-Agent_Deep_Deterministic_Policy_Gradient/A_Robust_Multi-Domain_Adaptive_Anti-Jamming_Communication_System_for_a_UAV_Swarm_in_Urban_ITS_Traffic_Monitoring_via_Multi-Agent_Deep_Deterministic_Policy_Gradient.md`
- Origin PDF: `raw/sources/A_Robust_Multi-Domain_Adaptive_Anti-Jamming_Communication_System_for_a_UAV_Swarm_in_Urban_ITS_Traffic_Monitoring_via_Multi-Agent_Deep_Deterministic_Policy_Gradient/A_Robust_Multi-Domain_Adaptive_Anti-Jamming_Communication_System_for_a_UAV_Swarm_in_Urban_ITS_Traffic_Monitoring_via_Multi-Agent_Deep_Deterministic_Policy_Gradient.pdf`
- Figures: `raw/sources/A_Robust_Multi-Domain_Adaptive_Anti-Jamming_Communication_System_for_a_UAV_Swarm_in_Urban_ITS_Traffic_Monitoring_via_Multi-Agent_Deep_Deterministic_Policy_Gradient/images/`
