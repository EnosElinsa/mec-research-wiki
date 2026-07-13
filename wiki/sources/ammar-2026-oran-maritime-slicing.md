---
type: source
title: "Maritime-Oriented Network Slicing in O-RAN Integrated Aerial-Terrestrial Networks"
authors: ["Sahar Ammar", "Wiem Abderrahim", "Basem Shihada"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3626785"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, open-ran, network-slicing, network-function-virtualization, maritime-networks, a2c, ppo]
related:
  - "[[open-radio-access-network]]"
  - "[[network-slicing]]"
  - "[[network-function-virtualization]]"
  - "[[advantage-actor-critic]]"
  - "[[ppo]]"
  - "[[hybrid-action-decision-making]]"
  - "[[maritime-mec]]"
  - "[[air-ground-integrated-network]]"
  - "[[uav-trajectory-control]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[basem-shihada]]"
created: 2026-07-13
updated: 2026-07-13
---

# Maritime-Oriented Network Slicing in O-RAN Integrated Aerial-Terrestrial Networks

## Citation

Ammar, S., Abderrahim, W., & Shihada, B. (2026). Maritime-oriented network slicing in O-RAN integrated aerial-terrestrial networks. *IEEE Transactions on Mobile Computing, 25*(4), 4806-4821. https://doi.org/10.1109/TMC.2025.3626785

The parse omits publication metadata; the exact-title Crossref record supplies the year, venue, DOI, volume, issue, and pages.

## TL;DR

An O-RAN maritime architecture jointly controls VNF scaling/migration, CPU and radio resources, and mobile-UAV trajectories for infotainment and emergency slices. Single-agent A2C and PPO operate on a discretized action space with energy-efficiency reward and QoS penalties.

## Problem and system model

The integrated network contains mobile UAVs, tethered UAVs, marine buoys, and ships. An infotainment slice requires high throughput; an emergency slice requires low delay and high reliability. Virtual network functions run on aerial and buoy nodes and may be scaled or migrated.

The mixed-integer problem maximizes average sum-of-ratios energy efficiency over time. Decisions cover VNF scaling/migration, CPU allocation, transmit power, and non-tethered UAV movement under mobility, compute, power, throughput, reliability, and delay constraints.

## Method

The MDP aggregates individuals at ship level and grids the maritime area. UAV movement becomes left/right/up/down/stay, while continuous CPU and power allocations are quantized to minimum/maximum levels. [[advantage-actor-critic|A2C]] and [[ppo|PPO]] train actor/critic networks against a weighted penalty reward. The paper invokes standard policy-gradient and stochastic-approximation assumptions for convergence to stationary/local policies and explicitly leaves global deep-policy optimality open.

## Key findings

- A2C converges after about 2,700 episodes versus up to 20,000 for PPO in the reported setup, with higher reward but more fluctuation.
- Trajectory optimization saves about 24% modeled power with five ships and 22% with 15 ships; under heavier emergency traffic, A2C adds about 4% saving over PPO.
- All three A2C deployment modes meet the reported emergency-delay requirement, while PPO migration does not.
- Migration is the only mode that meets the reported emergency-reliability requirement for both agents, trading against throughput and delay.
- A2C degrades less than PPO as the number of ships grows in the fixed-resource scalability experiment.

## Limitations

Evidence is simulation-only, without an O-RAN/RIC implementation or sea trial. Native mixed controls are coarsely discretized, and weighted penalties do not guarantee hard constraint satisfaction. Figure 3's reward magnitudes are missing from the parse. The analysis establishes local/stationary convergence assumptions rather than global optimality; satellite extension, multi-agent hybrid DRL, distributed learning, and broader scalability remain future work.

## Relation to the corpus

This source brings [[open-radio-access-network]] orchestration into the maritime track by combining [[network-slicing]], [[network-function-virtualization]], and UAV mobility. It complements the VNF control loop in [[pham-2026-vnf-control-loop]] and maritime resource virtualization in [[liu-2022-maritime-uav-mec-virtualization]].

## Raw artifacts

- Parse: `raw/sources/Maritime-Oriented_Network_Slicing_in_O-RAN_Integrated_Aerial-Terrestrial_Networks/Maritime-Oriented_Network_Slicing_in_O-RAN_Integrated_Aerial-Terrestrial_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
