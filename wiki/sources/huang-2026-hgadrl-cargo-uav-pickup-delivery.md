---
type: source
title: "Joint Optimization of Energy Efficiency and Stable Communication Quality for Cargo UAV-Enabled Multi-Package Pickup and Delivery"
authors: ["Guoguo Huang", "Jiangling Cao", "Liang Yang", "Shenghai Chen"]
year: 2026
url: "https://doi.org/10.1109/TCCN.2025.3623371"
venue: "IEEE Transactions on Cognitive Communications and Networking, 12"
modeling_card: required
tags: [source, cargo-uav, pickup-and-delivery, cellular-connected-uav, radio-map, genetic-algorithm, dueling-dqn, outage-constraint]
related:
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[cellular-connected-uav]]"
  - "[[genetic-algorithm]]"
  - "[[dueling-dqn]]"
  - "[[peng-2025-cargo-uav-energy-outage-tradeoff]]"
  - "[[deng-2024-radio-map-uav-pickup-delivery]]"
  - "[[chen-2026-cargo-uav-pickup-lae]]"
  - "[[jiangling-cao]]"
  - "[[connectivity-aware-cargo-uav-path-planning]]"
created: 2026-11-02
updated: 2026-11-03
---

# Joint Optimization of Energy Efficiency and Stable Communication Quality for Cargo UAV-Enabled Multi-Package Pickup and Delivery

## Citation

Huang, G., Cao, J., Yang, L., & Chen, S. (2026). *Joint Optimization of Energy Efficiency and Stable Communication Quality for Cargo UAV-Enabled Multi-Package Pickup and Delivery*. **IEEE Transactions on Cognitive Communications and Networking, 12**. DOI: 10.1109/TCCN.2025.3623371. Published online in October 2025.

## TL;DR

A cellular-connected cargo UAV leaves a warehouse with packages to deliver, collects other packages on the way, and returns. The paper minimizes total energy while keeping the outage probability at every traversed position below a threshold, using a two-phase HGADRL framework: a genetic algorithm sets the service order and a multistep dueling DDQN plans each flight stage on a coverage map.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One cargo UAV serves $I$ users requesting pickup or delivery in an $L\times L$ km area with buildings and GBSs. It flies at constant altitude $H$, ascending or descending only at service points, and connects to one GBS at a time; signals from other GBSs are interference, and the outage probability $P_{out}(\mathbf q(t))=\Pr(SIR(t)<\gamma_{th})$ forms a 2-D coverage map.

**Problem & objective**: P0: $\min_{\mathbf q(t),\Pi}E_{total}$, the total payload-dependent flight energy over the mission.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Trajectory | $\mathbf q(t)=(x(t),y(t),h(t))$ | continuous in the area | UAV position over the mission |
| Flying direction | $\vec{\mathbf v}$ | unit vector, $\lVert\vec{\mathbf v}\rVert=1$ | Direction of each step at speed $V_{max}$ |
| Service order | $\Pi$ | permutation of users | Order of pickup and delivery visits |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (11a)-(11b) | Start and end at the warehouse, $\mathbf q(0)=\mathbf q(T)=L_w$. |
| (11c)-(11d) | Position update (the parse leaves the update line untagged; check the published paper), $\mathbf q(t+1)=\mathbf q(t)+V_{max}\vec{\mathbf v}$ with unit direction. |
| (11e)-(11g) | Stay in the area, $0\le x,y\le L$ and $0\le h\le H$. |
| (11h) | Every user location $L^i_{user}$ is visited. |
| (11i) | Outage limit, $P_{out}(t)\le\gamma_d$ along the trajectory. |
| (11i), payload | The same tag also imposes the weight-update constraints (5)-(9) at each pickup or delivery. |

**Algorithm**: Phase 1 runs a genetic algorithm on the service sequence under the payload-dependent energy model. Phase 2 trains one dueling DDQN per flight stage (seven networks in the experiments) on the coverage map to minimize stage energy while avoiding positions above the outage threshold.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Huang et al. [x] considered a cellular-connected cargo UAV system for multi-package pickup and delivery, in which the UAV departs from a warehouse with packages, completes deliveries, collects packages, and returns. Their objective is to minimize the UAV's total energy consumption while keeping the probability that its trajectory is covered by ground base stations above specified thresholds. They introduced a two-phase hybrid genetic algorithm and deep reinforcement learning framework, in which a genetic algorithm determines the service order and deep reinforcement learning then optimizes the flight trajectory of each stage. Experiments compare the framework with the RRT-Energy, D3QN-Distance, and RRT-Distance benchmark schemes under four communication outage thresholds. The results report average energy savings of about 19.7% relative to an RRT-based scheme and about 33.2% relative to a distance-based D3QN, while maintaining a stable connection with the base stations.

## Problem framing

Earlier cargo-UAV work handled delivery only or weighted communication quality in the objective. This paper treats connectivity as a hard per-position outage constraint and mixes pickup and delivery so payload can both decrease and increase during the mission.

## System model

- 3 km by 3 km area with nine 25 m GBSs, $15^\circ$ downtilt, and an 8-element vertical ULA per GBS following 3GPP TR 38.901.
- ITU-R M.2412 urban buildings with area ratio 0.32, density 320, and Rayleigh heights.
- Energy depends on total weight, which changes at every pickup or delivery point.

## Method

The GA uses tuned population size, iterations, crossover, and mutation rates. Each dueling DDQN has five hidden layers (512-256-128-128-9) and is trained with Adam on the coverage-map environment.

## Key findings

- The energy-trained D3QN saved about 19.7% versus RRT-Energy and 33.2% versus D3QN-Distance on average across thresholds.
- Overall average savings exceeded 20% to 30% while respecting the outage thresholds.

## Limitations / future work

The authors note that assuming sufficient capacity and battery for all users and a flight altitude above all buildings is unrealistic. Future research could address three-dimensional flight spaces and capacity constraints.

## Relation to the corpus

Extends the weighted-outage model of [[peng-2025-cargo-uav-energy-outage-tradeoff]] to mixed pickup and delivery with a hard outage constraint, and complements [[deng-2024-radio-map-uav-pickup-delivery]] and [[chen-2026-cargo-uav-pickup-lae]] in [[uav-delivery-pickup-dropoff]].

## Raw artifacts

- Parse: `raw/sources/Joint_Optimization_of_Energy_Efficiency_and_Stable_Communication_Quality_for_Cargo_UAV-Enabled_Multi-Package_Pickup_and_Delivery/Joint_Optimization_of_Energy_Efficiency_and_Stable_Communication_Quality_for_Cargo_UAV-Enabled_Multi-Package_Pickup_and_Delivery.md`
- Origin PDF and extracted figures are in the same folder.
