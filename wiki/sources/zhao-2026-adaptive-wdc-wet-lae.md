---
type: source
modeling_card: required
title: "Toward Adaptive IoT Service Balance in Low-Altitude Economy: Multi-UAV-Aided Bi-Objective Wireless Data Collection and Wireless Energy Transfer"
authors: ["Zeyu Zhao", "Yueling Che", "Sheng Luo", "Kaishun Wu", "Victor C. M. Leung"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3664903"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 7, pp. 10773-10787, Jul. 2026"
tags: [source, low-altitude-economy, wireless-data-collection, wireless-energy-transfer, age-of-information, multi-agent-drl, hierarchical-drl]
related:
  - "[[adaptive-wdc-wet-service-balancing]]"
  - "[[uav-data-collection]]"
  - "[[wireless-power-transfer]]"
  - "[[age-of-information]]"
  - "[[aoi-energy-tradeoff]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[ddpg]]"
  - "[[soft-actor-critic]]"
  - "[[deep-q-network]]"
created: 2026-07-07
updated: 2026-11-03
---

# Toward Adaptive IoT Service Balance in Low-Altitude Economy: Multi-UAV-Aided Bi-Objective Wireless Data Collection and Wireless Energy Transfer

## Citation

Zhao, Z., Che, Y., Luo, S., Wu, K., & Leung, V. C. M. (2026). *Toward Adaptive IoT Service Balance in Low-Altitude Economy: Multi-UAV-Aided Bi-Objective Wireless Data Collection and Wireless Energy Transfer*. **IEEE Transactions on Mobile Computing**, 25(7), 10773-10787. DOI: 10.1109/TMC.2026.3664903. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Balances multi-UAV [[uav-data-collection|wireless data collection]] for information devices against [[wireless-power-transfer|wireless energy transfer]] for energy devices in a low-altitude IoT network. The paper converts a bi-objective AoI/HoE problem into a single objective with a learned adaptive weight, then solves trajectory, WET, and WDC decisions with the MA2HDRL framework.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $U$ UAVs at fixed altitude $h_{fix}$ collect data from I-devices over $K$ sub-slots per slot (WDC, uplink) and transfer RF energy to E-devices (WET, downlink). Data freshness is the AoI $A_n[t]$ (6); E-devices harvest with a sensitivity threshold $P_{sen}$ and battery capacity (10), and their energy shortage is the hunger level of energy (HoE) $H_w[t]$ (11); UAV batteries drain with rotary-wing propulsion power (14).
**Problem & objective**: Bi-objective (P1) (15) minimizes $\{A_{total},H_{total}\}$ over trajectories $Q$, WDC decisions $D$, and WET decisions $Z$; it is transformed into (P2) (21), $\min_{Q,D,Z,\varsigma}\varsigma A_{total}+(1-\varsigma)H_{total}$, with the weight $\varsigma\in[0,1]$ optimized jointly.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $q_u[t]$ | continuous horizontal position | Location of UAV $u$ in slot $t$ |
| WET decision | $Z_u[t]$ | binary | UAV $u$ transfers energy in slot $t$ |
| WDC schedule | $D_{u,n}^t[k]$ | binary | I-device $n$ uploads to UAV $u$ in sub-slot $k$ |
| Objective weight | $\varsigma$ | continuous, $[0,1]$ | Adaptive AoI-versus-HoE preference (global reward preference $\zeta[e]$ in training) |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (3) | Per sub-slot, each I-device uploads to at most one UAV and each UAV serves at most one I-device |
| (6), (10), (11), (14) | AoI, E-device battery, HoE, and UAV battery dynamics |
| (16)–(17) | Binary WET and WDC decisions |
| (18) | Speed limit: $\lVert q_u[t]-q_u[t-1]\rVert\le V_u^{\max}\vartheta$ |
| (19) | Final UAV battery: $B_u^{end}\ge B_u^{\min}$ |
| (20) | Collision avoidance: $d_u^{u'}[t]\ge d_{\min}$ |
**Algorithm**: MA²HDRL: a central DDPG model (ARPA) sets the global reward preference each episode → on each UAV, a first-tier SAC agent chooses trajectory and WET actions per slot → a second-tier DQN agent chooses WDC schedules per sub-slot → rewards combine AoI, HoE, collision, and battery terms → all tiers update.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] studied adaptive service balancing between wireless data collection and wireless energy transfer in multi-UAV low-altitude IoT networks. They formulated a bi-objective AoI and hungry-level-of-energy problem over UAV trajectories, WET decisions, WDC schedules, and an adaptive scalarization weight under scheduling, harvesting, mobility, collision, and final-energy constraints. MA2HDRL uses a central DDPG agent to adjust reward preference. First-tier SAC agents choose trajectory and WET actions, while second-tier DQN agents schedule discrete data collection. Simulations show that any fixed preference trades AoI against HoE, while the self-adjusted preference keeps both low, and the ARPA preference is compared with an NPTS benchmark whose preference rises linearly over stages regardless of the network state.

## Problem

Low-altitude IoT networks can need both fresh data collection and RF energy replenishment, but the two services pull UAVs toward different devices and compete for limited flight, power, and scheduling resources. Fixed scalarization weights require manual tuning across environments, so the paper asks how a UAV fleet can adaptively balance [[age-of-information|AoI]] and hungry-level-of-energy (HoE) objectives.

## System model

The system has multiple UAVs serving I-devices that need WDC and E-devices that need WET over a task period of time slots. Each UAV flies at a fixed altitude, carries separate antennas for uplink WDC and downlink WET over non-overlapping bands, and must satisfy speed, collision, and final-energy constraints. Each slot is divided into subslots for WDC scheduling; each UAV can collect from at most one I-device per subslot, and each I-device can upload to at most one UAV. E-device harvesting follows a nonlinear RF energy-harvesting model with sensitivity and saturation, and HoE measures how urgently an E-device needs energy.

## Method

The paper formulates a BOOP that jointly optimizes UAV trajectories, WET decisions over slots, and WDC decisions over subslots. It then scalarizes AoI and HoE with a self-adaptive objective weight and solves the resulting SOOP using MA2HDRL:

- a central controller trains an Adaptive Reward Preference Adjustment model with [[ddpg]] to set global reward preference;
- each UAV agent uses [[soft-actor-critic|SAC]] in the first tier for continuous trajectory and WET decisions;
- each UAV agent uses [[deep-q-network|DQN]] in the second tier for discrete WDC subslot decisions.

## Key findings

- In the reported default setting with 3 UAVs, 5 I-devices, and 3 E-devices, MA2HDRL converges after about 6000 episodes and obtains an optimal objective weight of 0.7125 at episode 7125 in the parse.
- The adaptive reward preference changes more flexibly than a linear-increase benchmark and yields lower converged AoI and HoE with smaller fluctuations.
- Fixed reward preferences expose the WDC/WET conflict: increasing the WDC preference lowers AoI but raises HoE, while MA2HDRL keeps both low in the reported comparison.
- The HoE-aware policy brings all three E-device batteries to the sufficiency threshold in the example; without HoE, harvested energy becomes unbalanced and one E-device receives zero harvested energy.
- The example trajectory keeps the minimum inter-UAV distance at 5.8 m and leaves all three UAVs above the 20000 W s final-battery constraint.

## Limitations / future work

The conclusion says future work will investigate scalability in large-scale IoT deployments. The model also separates devices into WDC-only and WET-only classes and evaluates the method in simulation rather than hardware.

## Relation to the corpus

This source adds [[adaptive-wdc-wet-service-balancing]] to the LAE control vocabulary. It connects [[uav-data-collection]], [[wireless-power-transfer]], and [[age-of-information]] more tightly than single-service WDC/WET entries, and it is a multi-service counterpart to [[cai-2026-llm-drl-secure-lae-data]], where the corpus already tracks secure LAE data collection with AoI and energy constraints.

## Raw artifacts

- `raw/sources/Toward_Adaptive_IoT_Service_Balance_in_Low-Altitude_Economy_Multi-UAV-Aided_Bi-Objective_Wireless_Data_Collection_and_Wireless_Energy_Transfer/Toward_Adaptive_IoT_Service_Balance_in_Low-Altitude_Economy_Multi-UAV-Aided_Bi-Objective_Wireless_Data_Collection_and_Wireless_Energy_Transfer.md`
- Original PDF and extracted figures (`images/`) in the same folder.
