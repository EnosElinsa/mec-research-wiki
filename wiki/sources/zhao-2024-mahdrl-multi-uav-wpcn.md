---
type: source
title: "On Designing Multi-UAV Aided Wireless Powered Dynamic Communication via Hierarchical Deep Reinforcement Learning"
authors: ["Ze Yu Zhao", "Yue Ling Che", "Sheng Luo", "Gege Luo", "Kaishun Wu", "Victor C. M. Leung"]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3439556"
venue: "IEEE Transactions on Mobile Computing, 23(12)"
modeling_card: required
tags: [source, wireless-powered-communication-network, multi-uav, hierarchical-reinforcement-learning, soft-actor-critic, dqn, nonlinear-energy-harvesting]
related:
  - "[[wireless-powered-communication-network]]"
  - "[[hierarchical-reinforcement-learning]]"
  - "[[soft-actor-critic]]"
  - "[[deep-q-network]]"
  - "[[harvest-transmit-store-scheduling]]"
  - "[[wireless-powered-uav-fair-service-control]]"
  - "[[victor-c-m-leung]]"
created: 2026-11-02
updated: 2026-11-03
---

# On Designing Multi-UAV Aided Wireless Powered Dynamic Communication via Hierarchical Deep Reinforcement Learning

## Citation

Zhao, Z. Y., Che, Y. L., Luo, S., Luo, G., Wu, K., & Leung, V. C. M. (2024). *On Designing Multi-UAV Aided Wireless Powered Dynamic Communication via Hierarchical Deep Reinforcement Learning*. **IEEE Transactions on Mobile Computing, 23**(12). DOI: 10.1109/TMC.2024.3439556.

## TL;DR

Multiple UAVs power and collect data from low-power wireless nodes (WNs) whose role changes over time: by a double-threshold rule, each WN is an energy-harvesting E-node or a transmitting I-node. MAHDRL maximizes total transmitted data with a two-tier policy: SAC sets each UAV's trajectory and binary wireless energy transmission (WET) per slot, and DQN sets binary wireless data collection (WDC) per sub-slot.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $U\ge2$ UAVs serve $W$ WNs over $T$ slots with LoS-probability air-to-ground channels. A WN switches to I-node when its battery exceeds $B_I$ and back to E-node below $B_E$. E-nodes harvest energy non-linearly from all UAVs that transmit energy; I-nodes upload data in sub-slots to limit co-channel interference. UAV energy covers movement, WET, and WDC.

**Problem & objective**: (P1), a mixed-integer problem: $\max_{\mathbf Q,\mathbf Z,\mathbf D}\sum_{t=1}^T\sum_{w=1}^W C_w[t]$, the total data transmitted by all WNs.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Trajectory | $\mathbf Q$ | continuous UAV positions | Flight path of each UAV over slots |
| WET decision | $Z_u[t]$ | binary | UAV $u$ transmits energy in slot $t$ |
| WDC decision | $D^t_{u,w}[k]$ | binary | UAV $u$ collects data from I-node $w$ in sub-slot $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (12) | Minimum data per WN, $\sum_t C_w[t]\ge C_{\min}$. |
| (13) | Speed limit, $V_u[t]\le V^{\max}_U$. |
| (14) | Final UAV battery, $B^{end}_u\ge B^{\min}_U$. |
| (15)-(16) | Binary WDC and WET decisions. |
| (17) | Safe separation, $d^{u'}_u[t]\ge d_{\min}$. |
| (9) | Double-threshold WN type update with thresholds $B_E$ and $B_I$. |

**Algorithm**: Tier 1 uses SAC, trained centrally and executed at each UAV, to output continuous trajectory and binary WET per slot. Tier 2 uses DQN, trained locally at each UAV, to choose binary WDC per sub-slot given the tier-1 trajectory. Both policies run distributively at test time.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] proposed a design for wireless powered communication networks in dynamic environments assisted by multiple UAVs. Under a double-threshold based node type updating rule, each wireless node repeatedly switches between an E-node for non-linear energy harvesting over time slots and an I-node for transmitting data over sub-slots. To maximize the total transmission data size over all slots, each UAV determines its trajectory and binary wireless energy transmission decisions over slots and its binary data collection decisions over sub-slots, subject to its on-board energy and the node type rule. They proposed a multi-agent hierarchical deep reinforcement learning framework in which a soft actor critic policy in tier 1 decides trajectory and energy transmission and a deep Q-learning policy in tier 2 decides data collection, both executed distributively at each UAV. Simulation results show higher total transmitted data than a DDPG-based tier-1 variant during training and than MAHDRL without HoE, phase division, TEAM, and random WDC schemes in testing, across network sizes.

## Problem framing

The classic harvest-then-transmit protocol fixes the order of harvesting and transmission. Here nodes change roles dynamically, and UAVs face a conflict: they should cluster to add harvested energy at E-nodes but spread out to reduce interference during data collection.

## System model

- 400 m by 400 m area with four UAVs at random start positions and ten WNs with random initial battery energy.
- Non-linear energy-harvesting model at E-nodes; fixed WDC power $P_I$ at UAVs.

## Method

The central trainer trains the SAC policy and copies parameters to each UAV, while each UAV trains its own DQN. Comparisons include a DDPG+DQN combination.

## Key findings

- MAHDRL outperforms benchmarks including DDPG+DQN in both training and test stages.
- A network example shows node types alternating and UAV trajectories adapting to WN energy states.
- Performance holds across network scales.

## Limitations / future work

Central trainer placement and computation affect performance. The authors suggest a UAV-enabled mobile central trainer and joint transmission and computation design.

## Relation to the corpus

Extends [[wireless-powered-communication-network]] with role-switching nodes and multi-UAV [[hierarchical-reinforcement-learning]], related to [[harvest-transmit-store-scheduling]] and [[wireless-powered-uav-fair-service-control]].

## Raw artifacts

- Parse: `raw/sources/On_Designing_Multi-UAV_Aided_Wireless_Powered_Dynamic_Communication_via_Hierarchical_Deep_Reinforcement_Learning/On_Designing_Multi-UAV_Aided_Wireless_Powered_Dynamic_Communication_via_Hierarchical_Deep_Reinforcement_Learning.md`
- Origin PDF and extracted figures are in the same folder.
