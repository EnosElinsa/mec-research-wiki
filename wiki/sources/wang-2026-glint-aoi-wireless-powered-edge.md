---
type: source
modeling_card: required
title: "Decentralized Learning-Driven AoI Optimization in UAV-Assisted Wireless Powered Edge Networks"
authors: ["Xiaojie Wang", "Jiameng Li", "Zhaolong Ning", "Fei Richard Yu", "Song Guo"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3688661"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, aoi, wireless-power-transfer, uav, data-collection, maddpg, value-factorization]
related:
  - "[[dual-network-sequential-aoi-control]]"
  - "[[age-of-information]]"
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[maddpg]]"
  - "[[device-association]]"
  - "[[zhaolong-ning]]"
  - "[[xiaojie-wang]]"
created: 2026-07-12
updated: 2026-07-16
---

# Decentralized Learning-Driven AoI Optimization in UAV-Assisted Wireless Powered Edge Networks

## Citation

Wang, X., Li, J., Ning, Z., Yu, F. R., & Guo, S. (2026). *Decentralized Learning-Driven AoI Optimization in UAV-Assisted Wireless Powered Edge Networks*. **IEEE Transactions on Mobile Computing**, 1-18. DOI: 10.1109/TMC.2026.3688661.

## TL;DR

GLINT minimizes sensor AoI by splitting multi-UAV control into two sequential learned stages: UAV position/association first, then WPT-time and sensor-transmission scheduling. Local critics are combined by a monotonic mixer during centralized training, while each UAV executes two local actors and an association matcher.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple rotary-wing UAVs charge fixed energy-constrained sensors by RF wireless power transfer, collect status updates by TDMA, and process them at the edge. OFDMA separates UAVs, while nonlinear harvesting, finite batteries, probabilistic LoS channels, and UAV flight energy couple mobility and freshness.

**Problem & objective**: A long-term NP-hard MINLP minimizes network-average age of information, $\min \limsup_{T\to\infty}\frac{1}{KT}\sum_{k,t}A_k(t)$, over UAV positions, association, charging time, and update scheduling.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $\mathbf q_m(t)$ | continuous 3-D position | Movement and service location of UAV $m$ |
| Sensor association | $x_{k,m}(t)$ | binary | Whether sensor $k$ is assigned to UAV $m$ |
| WPT duration | $\tau_m^{\mathrm W}(t)$ | discrete/continuous slot share | Charging time used by UAV $m$ |
| Update schedule | $s_{k,m}(t)$ | binary | Whether sensor $k$ transmits a fresh update to UAV $m$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each sensor associates with at most one covering UAV |
| C2 | Movement, WPT, and TDMA collection shares fit within the slot |
| C3 | A scheduled transmission has sufficient harvested battery energy |
| C4 | UAV altitude, movement, collision distance, endpoints, and return position remain feasible |
| C5 | UAV propulsion and RF-charging energy remain within the mission budget |

**Algorithm**: Let the first decentralized actor choose UAV positions → match sensors by path-loss preference → let the second actor choose WPT time and transmission schedules → mix local critic values monotonically during centralized training → use GRU state, Gumbel-Softmax actions, replay, and target updates → execute both actors locally.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied age-of-information minimization in a multi-UAV wireless powered edge network with nonlinear RF energy harvesting. They formulated a long-term mixed-integer problem over UAV positions, sensor association, wireless-power-transfer duration, and update scheduling under coverage, battery, time, mobility, collision, and UAV-energy constraints. GLINT decomposes the control into a position-and-association stage followed by a charging-and-transmission stage. During centralized training, a monotonic mixing network combines local critic values, while each UAV executes two local actors and an association matcher. Simulations report lower AoI and higher transmission efficiency than the evaluated centralized and decentralized learning baselines across the tested maps and network sizes.

## Problem

Rotary-wing UAVs act as RF chargers, data collectors, and edge servers for energy-constrained sensors. UAV movement, charging time, sensor association, and transmission scheduling jointly determine whether fresh packets can be powered and delivered. Directly learning the full mixed action space creates a large NP-hard MINLP and poor multi-agent convergence.

## System model

- Fixed sensors harvest RF energy from half-duplex UAVs and transmit updates over probabilistic LoS/NLoS air-ground links.
- Each slot is divided among 3D movement, WPT, and TDMA data collection; OFDMA separates different UAVs.
- Sensors use nonlinear sensitivity/saturation-limited harvesting and finite batteries. UAV energy includes flight, hover, and RF charging.
- A successful scheduled update resets sensor AoI to one; otherwise AoI increments.
- The long-term objective minimizes average AoI subject to coverage, association, time, battery, power, altitude, collision, return-position, and variable-domain constraints.

## Method

GLINT approximates the original problem with two interdependent Dec-POMDPs. Actor 1 chooses UAV positions; a path-loss preference matcher then assigns sensors. Actor 2 uses that result to select discretized WPT time and sensor transmissions. Each UAV has two sequential actors and a local critic. During CTDE training, a monotonic mixing network combines local values, full episodes support GRU temporal state, Gumbel-Softmax differentiates discrete choices, and target networks stabilize updates. P1 uses prior-slot WPT time and candidate-sensor indicators, so the decomposition is an approximation rather than an exact reformulation.

## Key findings

- With four UAVs, 20 sensors, and transmission time `0.2`, the two learned stages stabilize after about 300 episodes on both the Manhattan and Lake Louise maps; the UAV-scale study stabilizes after about 240 episodes.
- Across transmission-time values `0.1-0.3`, GLINT uses slightly more UAV energy than centralized MODDPG but achieves the best AoI and transmission efficiency among the compared methods; the reported balance occurs at `0.2`.
- From 20 to 120 sensors, GLINT stays closest to the theoretical AoI lower bound. At 120 sensors, most methods exhaust UAV energy after about 100 slots in the plotted discussion.
- AoI and per-UAV energy stabilize around 10 or more UAVs; transmission-efficiency improvement becomes negligible beyond about 14 UAVs in the tested setup.

## Limitations / parse caveats

The simulations assume perfect CSI, fixed sensors, half-duplex hardware, orthogonal inter-UAV bands, finite initial energy, and modeled channels/maps. Centralized training requires global information, but communication and stale-data effects are not evaluated. The association pseudocode referenced as Appendix F is absent from the parse, and no end-to-end optimality guarantee is established for the approximate decomposition. The parse states the TMC venue but omits year/DOI/final issue metadata; the exact-title Crossref record supplies the 2026 early-access record. Plot ordinates are not digitized.

## Relation to the corpus

[[dual-network-sequential-aoi-control]] deepens the rechargeable-sensor branch of [[age-of-information]] beyond one-stage value decomposition. It couples 3D [[uav-trajectory-control]] and [[device-association]] to nonlinear [[rf-energy-harvesting]] and a second-stage freshness scheduler.

## Raw artifacts

- Parse: `raw/sources/Decentralized_Learning-Driven_AoI_Optimization_in_UAV-Assisted_Wireless_Powered_Edge_Networks/Decentralized_Learning-Driven_AoI_Optimization_in_UAV-Assisted_Wireless_Powered_Edge_Networks.md`
- Origin PDF: `raw/sources/Decentralized_Learning-Driven_AoI_Optimization_in_UAV-Assisted_Wireless_Powered_Edge_Networks/Decentralized_Learning-Driven_AoI_Optimization_in_UAV-Assisted_Wireless_Powered_Edge_Networks.pdf`
- Figures: `raw/sources/Decentralized_Learning-Driven_AoI_Optimization_in_UAV-Assisted_Wireless_Powered_Edge_Networks/images/`
