---
type: source
title: "Maritime-Oriented Network Slicing in O-RAN Integrated Aerial-Terrestrial Networks"
authors: ["Sahar Ammar", "Wiem Abderrahim", "Basem Shihada"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3626785"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
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
updated: 2026-07-16
---

# Maritime-Oriented Network Slicing in O-RAN Integrated Aerial-Terrestrial Networks

## Citation

Ammar, S., Abderrahim, W., & Shihada, B. (2026). Maritime-oriented network slicing in O-RAN integrated aerial-terrestrial networks. *IEEE Transactions on Mobile Computing, 25*(4), 4806-4821. https://doi.org/10.1109/TMC.2025.3626785

The parse omits publication metadata; the exact-title Crossref record supplies the year, venue, DOI, volume, issue, and pages.

## TL;DR

An O-RAN maritime architecture jointly controls VNF scaling/migration, CPU and radio resources, and mobile-UAV trajectories for infotainment and emergency slices. Single-agent A2C and PPO operate on a discretized action space with energy-efficiency reward and QoS penalties.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An O-RAN integrated maritime network contains non-tethered UAVs $N$, tethered UAVs $M$, and marine buoys $K$ serving infotainment and emergency slices $S$. VNFs of types $F$ can be scaled or migrated across nodes, while non-tethered UAV positions $X_n[t]$ move between decision slots.

**Problem & objective**: The mixed-integer nonlinear problem $P$ maximizes time-average network energy efficiency, $\max\frac{1}{T}\sum_{t\in T}\Phi_{\mathrm{EE}}[t]$, through joint RAN slicing, VNF scaling or migration, resource allocation, and UAV trajectory design.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| VNF scaling | $\eta_{f,s}^{\zeta}[t]$ | integer | Number of VNF instances of type $f$ added or removed at node $\zeta$ for slice $s$ |
| VNF migration | $\mu_{f,i,s}^{\zeta,\zeta'}[t]$ | binary, $\{0,1\}$ | Whether instance $i$ migrates from $\zeta$ to $\zeta'$ |
| CPU allocation | $c_{f,i,s}^{\zeta}[t]$ | continuous, nonnegative | CPU capacity assigned to a VNF instance |
| User transmit power | $p_{f,i,u_s}^{\zeta}[t]$ | continuous, nonnegative | Power serving user $u_s$ of slice $s$ |
| UAV position | $X_n[t]$ | continuous vector | Position of non-tethered UAV $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV movement is bounded: $\|X_n[t]-X_n[t-1]\|\le d_{\mathrm{UAV}}$ |
| C2 | Nodes maintain separation: $\|X_{\zeta}[t]-X_{\zeta'}[t]\|>d_{\mathrm{safe}}$ for $\zeta\ne\zeta'$ |
| C3-C6 | CPU and transmit allocations after scaling or migration do not exceed $C_{\zeta}^{\mathrm{total}}$ and $P_{\zeta}^{\mathrm{transmit}}$ |
| C7 | Allocated CPU meets each VNF slice requirement: total allocated capacity equals $C_{f,s}^{\mathrm{req}}$ |
| C8 | Slice throughput meets its target: $R_{f,i,s}^{\zeta}[t]\ge R_{\min}^{s}$ |
| C9 | Slice reliability meets its target: $W_{f,i,s}^{\zeta}[t]\ge W_{\min}^{s}$ |
| C10 | Slice delay stays below its target: $D_{f,i,s}^{\zeta}[t]+D_{\mathrm M,f,i}^{\zeta,\zeta'}[t]\le D_{\max}^{s}$ |

**Algorithm**: Discretize UAV movement and CPU or power actions, model the problem as an MDP, train actor and critic networks with A2C or PPO using a weighted energy-efficiency and QoS-penalty reward, and deploy the learned policy to choose scaling, migration, resource, and trajectory actions at each slot.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ammar et al. [x] studied O-RAN integrated aerial-terrestrial maritime networks with non-tethered UAVs, tethered UAVs, marine buoys, and infotainment and emergency slices. They formulated a mixed-integer nonlinear problem that maximizes time-average network energy efficiency through VNF scaling or migration, resource slicing, and non-tethered UAV trajectory control subject to mobility, resource, throughput, reliability, and delay constraints. They solved the sequential decision problem with A2C and PPO using quantized hybrid actions and QoS-penalty rewards. In the reported simulations, A2C converged in about 2700 episodes versus up to 20000 for PPO, and trajectory control saved around 24% power for five ships and 22% for fifteen ships.

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
