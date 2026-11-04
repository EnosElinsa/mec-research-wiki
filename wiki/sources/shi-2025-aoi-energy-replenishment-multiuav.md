---
type: source
modeling_card: required
title: "AoI-Aware Data Collection and Energy Replenishment for Multi-UAV-Enabled IoT Systems"
authors: ["Kaijin Shi", "Juan Liu", "Lingfu Xie", "Zheng Zhou", "Hua Chen", "Guinian Feng"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2025.3542611"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, age-of-information, uav-data-collection, wireless-power-transfer, uav-charging, marl, vdn, qmix, ctde]
related:
  - "[[age-of-information]]"
  - "[[aoi-energy-tradeoff]]"
  - "[[uav-data-collection]]"
  - "[[wireless-power-transfer]]"
  - "[[uav-charging-scheduling]]"
  - "[[value-decomposition-network]]"
  - "[[qmix]]"
  - "[[ma-pomdp]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[song-2024-mol-aoi-energy]]"
  - "[[zhao-2026-adaptive-wdc-wet-lae]]"
created: 2026-07-11
updated: 2026-11-03
---

# AoI-Aware Data Collection and Energy Replenishment for Multi-UAV-Enabled IoT Systems

## Citation

Shi, K., Liu, J., Xie, L., Zhou, Z., Chen, H., & Feng, G. (2025). *AoI-Aware Data Collection and Energy Replenishment for Multi-UAV-Enabled IoT Systems*. **IEEE Transactions on Green Communications and Networking**, 9(4), 1755-1768. DOI: 10.1109/TGCN.2025.3542611. The parse lacks top-level publication metadata; venue, year, pages, and DOI were verified from a title-matched Crossref record.

## TL;DR

Studies persistent fresh data collection in a multi-UAV IoT system where UAVs wirelessly charge sensor nodes, collect updates, offload data to a BS, and recharge themselves at fixed charging stations. The goal is to minimize average sensor-node AoI under UAV energy and service constraints. The problem is modeled as a Dec-POMDP and solved with [[value-decomposition-network|VDN]] and [[qmix|QMIX]] under multi-agent RL.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $U$ UAVs serve $N$ sensor nodes (SNs) at positions $S_n$ on a grid of candidate hovering positions $\mathcal W$, with charging stations (CSs) $\mathcal E$ at $L_e$ and a base station at $C$. In working mode a UAV associates with one SN, charges it by wireless power transfer, collects its fresh update, offloads the data to the base station, and flies to its next position. In recharging mode it lands on a CS and recharges.

**Problem & objective**: Problem (18) minimizes the weighted sum of average SN age of information and average UAV energy consumption, $\min_{X(t)} \frac{1}{NT}\sum_{t=1}^{T}\sum_{n=1}^{N} A_n(t) + \chi\frac{1}{UT}\sum_{t=1}^{T}\sum_{u=1}^{U} e_u(t)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $U_u(t)$ | element of $\mathcal W$ | Hovering position of UAV $u$ in slot $t$ |
| Association | $\varepsilon_{un}(t)$ | binary, $n \in \mathcal N \cup \mathcal E$ | UAV $u$ serves SN $n$ or flies to CS $n$ |
| Charging completion | $\iota_u(t)$ | binary | UAV $u$ finishes recharging and returns to working mode |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (18a) | No two UAVs occupy the same position, $U_{u_1}(t) \ne U_{u_2}(t)$. |
| (18b) | Positions lie in the candidate set, $U_u(t) \in \mathcal W$. |
| (18c) | In working mode a UAV serves at most one SN or heads to one CS, $\sum_{n\in\mathcal N\cup\mathcal E}\varepsilon_{un}(t) \le 1-\varsigma_u(t)$. |
| (18d) | Only a recharging UAV can complete charging, $\iota_u(t) \le \varsigma_u(t)$. |
| (18e) | $\varepsilon_{un}(t), \iota_u(t) \in \{0,1\}$. |
| (18f) | AoI evolution (7)-(8), UAV energy use (16), and residual-energy evolution (17). |

**Algorithm**: Reformulate Problem (18) as a Dec-POMDP in which each UAV observes local SN, UAV, and CS states and chooses flight direction, SN association, and recharging actions. Train VDN and QMIX with centralized training and decentralized execution.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Shi et al. [x] studied age-of-information-aware data collection and energy replenishment for a multi-UAV IoT system. UAVs wirelessly charge sensor nodes, collect and offload updates to a base station, and periodically recharge at fixed stations. They formulated the minimization of a weighted sum of average sensor-node AoI and UAV energy consumption over flight, association, and recharging decisions, and modeled it as a decentralized partially observable Markov decision process. VDN and QMIX learn cooperative value functions from local observations while centralized training aggregates the agents' information. Simulations report lower AoI for the learned policies than the evaluated traditional baselines, with QMIX handling complex scenarios better than VDN.

## Problem

Fresh IoT updates require frequent UAV visits, but both sensor nodes and UAVs are energy-limited. Sensor nodes depend on UAV wireless power transfer before uploading data, while UAVs must leave service to recharge at charging stations. The resulting AoI objective couples trajectory, node association, energy transfer, data collection, offloading, and recharging decisions across multiple UAV agents.

## System model

- The network contains `U` UAVs, `N` sensor nodes, `E` charging stations, and one base station.
- Each UAV alternates between working mode and recharging mode.
- In working mode, a UAV associates with a sensor node, transfers wireless energy, collects data, offloads collected data to the BS, and moves to a new position.
- In recharging mode, a UAV lands at a charging station, recharges, and later takes off to resume service.
- UAVs act under partial observations of local sensor-node, UAV, and charging-state information.

## Method

The paper formulates the problem as a Dec-POMDP and applies two cooperative MARL algorithms. VDN represents the joint action-value as a sum of local action-values. QMIX uses a monotonic mixing network so the centralized training objective can be optimized while each UAV executes decentralized actions from local observations. Each UAV chooses flight, sensor/charging-station association, and recharging behavior.

## Key findings

- The simulation area is `400 m x 400 m`, divided into 400 grids of 10 m, with 10 sensor nodes, two charging stations, one BS, 20 kJ UAV batteries, and a 4 kJ/s UAV charge rate.
- Charging-rate experiments sweep 2-10 kJ per slot.
- The learning setup uses GRU hidden size 128, an output MLP with 56 outputs, learning rate 0.0005, discount factor 0.99, minimum exploration probability 0.05, minibatch size 32, and target-network update interval 200.
- Both MARL methods outperform traditional baselines in the parsed discussion; QMIX is reported as stronger in complex scenarios, while VDN often has lower energy use.
- A greedy baseline's AoI rises from about 20 to about 80 as the number of sensor nodes grows in the parsed figure discussion.

## Limitations / future work

The implementation does not primarily model concurrent charging and data gathering; the parse notes that supporting that behavior would require action-space changes. Sensor-node deactivation can occur when UAV energy or charging-station access is insufficient. The parse has malformed formulas and table text, so numeric details are limited to stable simulation parameters and stated qualitative comparisons.

## Relation to the corpus

This source strengthens the wiki's [[age-of-information]] and [[aoi-energy-tradeoff]] branch outside MEC offloading. It is closest to [[song-2024-mol-aoi-energy]] in using AoI as the headline freshness objective, and closest to [[zhao-2026-adaptive-wdc-wet-lae]] in coupling wireless data collection with RF energy transfer. Methodologically, it adds a non-ensemble [[qmix|QMIX]] value-decomposition instance beside [[value-decomposition-network]] and [[ensemble-qmix]].

## Raw artifacts

- `raw/sources/AoI-Aware_Data_Collection_and_Energy_Replenishment_for_Multi-UAV-Enabled_IoT_Systems/AoI-Aware_Data_Collection_and_Energy_Replenishment_for_Multi-UAV-Enabled_IoT_Systems.md`
- Original PDF and extracted figures (`images/`) in the same folder.
