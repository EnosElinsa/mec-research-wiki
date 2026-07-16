---
type: source
modeling_card: not_applicable
title: "Performance Analysis of Distributed UAVs in Urban Environments Using a Practical Line-of-Sight Model"
authors: ["Yue Ren", "Huasen He", "Yunpeng Hou", "Xiaofeng Jiang", "Shuangwu Chen", "Jian Yang"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3635206"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 1478-1494"
tags: [source, cellular-uav, stochastic-geometry, los-probability, urban-channel, base-station-selection, mmwave]
related:
  - "[[3gpp-uav-los-probability-model]]"
  - "[[matern-hard-core-bs-deployment]]"
  - "[[cellular-connected-uav]]"
  - "[[air-to-ground-channel-model]]"
  - "[[blockage-aware-channel-model]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[device-association]]"
  - "[[mobility-asynchrony-and-geometry-in-aerial-coverage]]"
created: 2026-07-14
updated: 2026-07-16
---

# Performance Analysis of Distributed UAVs in Urban Environments Using a Practical Line-of-Sight Model

## Citation

Ren, Y., He, H., Hou, Y., Jiang, X., Chen, S., & Yang, J. (2026). *Performance Analysis of Distributed UAVs in Urban Environments Using a Practical Line-of-Sight Model*. **IEEE Transactions on Green Communications and Networking, 10**, 1478-1494. DOI: 10.1109/TGCN.2025.3635206.

## TL;DR

Derives outage and capacity behavior for aerial users served by spatially separated urban mmWave base stations, using a finite-region hard-core deployment and the distance- and height-dependent 3GPP UAV LoS model rather than a single elevation-angle sigmoid.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ren et al. [x] analyzed outage and capacity for aerial users served by distributed urban millimeter-wave base stations. They modeled finite-region Matérn hard-core base-station deployment, distance- and height-dependent 3GPP UAV line-of-sight probabilities, LoS/NLoS path loss, shadowing, and three-dimensional sectored antennas. The analysis derives serving-distance distributions, outage probabilities, and ergodic capacities for best-base-station, best-LoS/NLoS, nearest-base-station, and nearest-LoS/NLoS selection. Monte Carlo simulations compare the practical 3GPP line-of-sight model with ITU and Manhattan ray-tracing models. The reported results show lower outage for best-base-station selection and analytical-to-simulation capacity differences of at most 2% up to 25 dBm in the stated cases.

## Problem and system model

Ground base stations serve aerial users in urban macrocell and microcell environments at 28 GHz. Base-station locations follow a finite Matérn hard-core process, while links include LoS/NLoS path loss, log-normal shadowing, and three-dimensional sectored antennas. The [[3gpp-uav-los-probability-model]] changes piecewise with horizontal distance, altitude, and deployment type.

The paper compares best-BS, best-LoS/NLoS, nearest-BS, and nearest-LoS/NLoS selection. The analytical model derives serving-distance distributions, outage probabilities, and ergodic capacities; where best-BS capacity remains intractable, throughput is used instead.

## Method

[[matern-hard-core-bs-deployment]] represents the minimum separation between urban base stations more realistically than an independent Poisson process. The analysis combines hard-core retention, finite-area distance distributions, and LoS/NLoS conditioning. Monte Carlo simulations validate the resulting expressions and compare the 3GPP LoS curve with ITU modeling and Manhattan-layout ray tracing.

## Key findings

- The 3GPP LoS model follows the Manhattan ray-tracing reference more closely than the compared ITU model in the evaluated urban settings.
- Best-BS selection gives lower outage than nearest-BS selection; conditioning nearest selection on LoS can outperform unrestricted nearest-BS association.
- Throughput stabilizes once the candidate base-station region extends beyond roughly 1000 m, and transmit-power gains become small above about 25 dBm in the evaluated configuration.
- Analytical and simulated capacities differ by at most 2% up to 25 dBm and by less than 7% in the reported extreme cases.
- In the urban macrocell case, capacity generally decreases with altitude. In the urban microcell case at medium or high power, it peaks around 50-75 m, supporting selection of the lowest altitude that satisfies the outage requirement.

## Limitations

The derivation assumes independent LoS events and omits small-scale fading. Interference is excluded from the tractable analytical expressions but included in simulation, and the hard-core process requires spatial approximations. The study analyzes static altitude and association rather than temporal UAV mobility or trajectory optimization. A shadowing-direction statement in the parse conflicts with the surrounding equations, so no directional shadowing claim is carried into this page.

## Relation to the corpus

This source sharpens [[air-to-ground-channel-model]] and [[stochastic-geometry-network-analysis]] with a practical urban UAV LoS law and repulsive terrestrial deployment. Its selection rules are a physical-layer form of [[device-association]], not an MEC offloading policy.

## Raw artifacts

- Parse: `raw/sources/Performance_Analysis_of_Distributed_UAVs_in_Urban_Environments_Using_a_Practical_Line-of-Sight_Model/Performance_Analysis_of_Distributed_UAVs_in_Urban_Environments_Using_a_Practical_Line-of-Sight_Model.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
