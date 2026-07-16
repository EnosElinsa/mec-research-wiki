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
updated: 2026-07-16
---

# Toward Adaptive IoT Service Balance in Low-Altitude Economy: Multi-UAV-Aided Bi-Objective Wireless Data Collection and Wireless Energy Transfer

## Citation

Zhao, Z., Che, Y., Luo, S., Wu, K., & Leung, V. C. M. (2026). *Toward Adaptive IoT Service Balance in Low-Altitude Economy: Multi-UAV-Aided Bi-Objective Wireless Data Collection and Wireless Energy Transfer*. **IEEE Transactions on Mobile Computing**, 25(7), 10773-10787. DOI: 10.1109/TMC.2026.3664903. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Balances multi-UAV [[uav-data-collection|wireless data collection]] for information devices against [[wireless-power-transfer|wireless energy transfer]] for energy devices in a low-altitude IoT network. The paper converts a bi-objective AoI/HoE problem into a single objective with a learned adaptive weight, then solves trajectory, WET, and WDC decisions with the MA2HDRL framework.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple fixed-altitude UAVs collect fresh data from information devices and transfer RF energy to energy devices over separate bands. Nonlinear harvesting, slot/subslot scheduling, UAV battery, mobility, and collision constraints couple AoI and hungry level of energy.

**Problem & objective**: A bi-objective control problem minimizes network AoI and HoE, $\min(A_{\mathrm{avg}},H_{\mathrm{avg}})$, then uses a learned preference $\lambda(t)$ for the scalar objective $\lambda A+(1-\lambda)H$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\mathbf q_m(t)$ | continuous position | Service path of UAV $m$ |
| WET decision | $e_{m,j}(t)$ | binary/continuous | UAV energy transfer to E-device $j$ |
| WDC schedule | $x_{m,i}(t,s)$ | binary | I-device $i$ served in subslot $s$ |
| Reward preference | $\lambda(t)$ | continuous, $[0,1]$ | Adaptive AoI-versus-HoE weight |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each UAV collects from at most one I-device per subslot |
| C2 | Each I-device uploads to at most one UAV per subslot |
| C3 | Harvested energy follows sensitivity and saturation limits |
| C4 | UAV speed and pairwise separation remain feasible |
| C5 | Every UAV retains at least the required final battery energy |

**Algorithm**: Let the central DDPG preference agent choose the current AoI-HoE weight → let first-tier SAC agents choose continuous trajectories and WET actions → let second-tier DQN agents choose discrete WDC schedules → compute AoI, HoE, collision, and battery rewards → update all three policy tiers.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] studied adaptive service balancing between wireless data collection and wireless energy transfer in multi-UAV low-altitude IoT networks. They formulated a bi-objective AoI and hungry-level-of-energy problem over UAV trajectories, WET decisions, WDC schedules, and an adaptive scalarization weight under scheduling, harvesting, mobility, collision, and final-energy constraints. MA2HDRL uses a central DDPG agent to adjust reward preference. First-tier SAC agents choose trajectory and WET actions, while second-tier DQN agents schedule discrete data collection. Simulations report lower AoI and HoE and more balanced harvested energy than the evaluated fixed-preference and ablation policies.

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

- `raw/sources/Toward Adaptive IoT Service Balance in Low-Altitude Economy Multi-UAV-Aided Bi-Objective Wireless Data Collection and Wireless Energy Transfer/Toward Adaptive IoT Service Balance in Low-Altitude Economy Multi-UAV-Aided Bi-Objective Wireless Data Collection and Wireless Energy Transfer.md`
- Original PDF and extracted figures (`images/`) in the same folder.
