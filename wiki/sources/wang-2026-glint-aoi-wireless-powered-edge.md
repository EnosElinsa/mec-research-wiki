---
type: source
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
created: 2026-07-12
updated: 2026-07-13
---

# Decentralized Learning-Driven AoI Optimization in UAV-Assisted Wireless Powered Edge Networks

## Citation

Wang, X., Li, J., Ning, Z., Yu, F. R., & Guo, S. (2026). *Decentralized Learning-Driven AoI Optimization in UAV-Assisted Wireless Powered Edge Networks*. **IEEE Transactions on Mobile Computing**, 1-18. DOI: 10.1109/TMC.2026.3688661.

## TL;DR

GLINT minimizes sensor AoI by splitting multi-UAV control into two sequential learned stages: UAV position/association first, then WPT-time and sensor-transmission scheduling. Local critics are combined by a monotonic mixer during centralized training, while each UAV executes two local actors and an association matcher.

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
