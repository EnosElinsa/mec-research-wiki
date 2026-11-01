---
type: source
title: "Balancing Energy Efficiency and Communication Quality in UAV Cargo Delivery Systems"
authors: ["Haixia Peng", "Jiangling Cao", "Dingcheng Yang", "Chenxi Li", "Tom H. Luan", "Zhou Su"]
year: 2025
url: "https://doi.org/10.1109/JIOT.2025.3577677"
venue: "IEEE Internet of Things Journal, 12(16)"
modeling_card: required
tags: [source, cargo-uav, cellular-connected-uav, radio-map, trajectory-optimization, ant-colony-optimization, dueling-dqn, logistics]
related:
  - "[[cellular-connected-uav]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[handoff-aware-uav-trajectory-planning]]"
  - "[[ant-colony-optimization]]"
  - "[[dueling-dqn]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[cao-2026-radio-map-cargo-pickup]]"
  - "[[huang-2026-hgadrl-cargo-uav-pickup-delivery]]"
  - "[[haixia-peng]]"
  - "[[jiangling-cao]]"
  - "[[dingcheng-yang]]"
  - "[[zhou-su]]"
created: 2026-11-02
updated: 2026-11-02
---

# Balancing Energy Efficiency and Communication Quality in UAV Cargo Delivery Systems

## Citation

Peng, H., Cao, J., Yang, D., Li, C., Luan, T. H., & Su, Z. (2025). *Balancing Energy Efficiency and Communication Quality in UAV Cargo Delivery Systems*. **IEEE Internet of Things Journal, 12**(16). DOI: 10.1109/JIOT.2025.3577677.

## TL;DR

A cellular-connected cargo UAV delivers packages of different weights from a warehouse to ground users and must stay connected to terrestrial cells. The paper minimizes a weighted sum of propulsion energy and expected outage time, solving delivery order and speed with an improved ant colony optimization (IACO) and the radio-map-guided horizontal trajectory with D3QN.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One cellular-connected cargo UAV serves $K$ ground users in an $L\times L$ urban area with buildings and $G$ terrestrial cells. It departs a warehouse loaded with all packages, flies at maximum altitude $H_{\max}$, descends vertically at each user, and returns. A building-based radio map gives the outage probability at every location.

**Problem & objective**: P0, a mixed sequence and trajectory problem: $\min E(\{\Phi,\nu_d(t),\mathbf q(t)\})+\mu\rho(t)T_{\mathrm{out}}(\{\mathbf q(t),c(t)\})$, where $\mu$ weights communication quality and $\rho(t)$ is the horizontal flight power used as a compensation factor.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Delivery sequence | $\Phi$ | permutation of users | Order in which packages are delivered |
| Trajectory | $\mathbf q(t)$ | continuous position in the area | Horizontal UAV path at altitude |
| Velocity | $\mathbf v(t)$ | $0\le\lVert\mathbf v(t)\rVert\le V_{\max}$ | Flight speed and direction |
| Communication scheduling | $c(t)$ | cell index | Serving cell associated with the UAV |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (18a) | Kinematics, $\dot{\mathbf q}(t)=\mathbf v(t)$. |
| (18b) | Speed limit, $0\le\lVert\mathbf v(t)\rVert\le V_{\max}$. |
| (18c) | Start and end at the warehouse, $\mathbf q(0)=\mathbf q(T)=(x_0,y_0,0)$. |
| (18d) | Every user $\phi_k$ is visited at some time $t_{\phi_k}\in[0,T]$. |
| (18e)-(18f) | Trajectory stays in the area, $0\le x_u(t),y_u(t)\le L$. |
| Association | $c(t)$ selects one of the $G$ cells at every time. |

**Algorithm**: Hybrid DRL (HDRL). IACO solves the directed weighted TSP for delivery order and flight speed under payload-dependent energy; D3QN then plans the horizontal trajectory between consecutive users on the radio map to reduce outage time and energy.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Peng et al. [x] investigated the tradeoff between energy efficiency and communication quality in a cellular-connected cargo UAV delivery system. They formulated an optimization problem that minimizes the weighted sum of the UAV's energy consumption and expected outage time, accounting for both horizontal and vertical flight energy. With the aid of a radio map, they proposed a hybrid deep reinforcement learning algorithm in which an improved ant colony optimization algorithm determines the delivery sequence and flight speed and a dueling double deep Q network optimizes the flight trajectory. Numerical results show that the proposed algorithm reduces both energy consumption and outage time, with a performance improvement of approximately 6% to 50% over the comparison schemes. The results also show that a larger weight factor improves communication quality at the cost of higher energy consumption.

## Problem framing

Package weights decrease as deliveries complete, so delivery order changes propulsion energy. Cellular coverage at altitude is uneven because buildings block links, so the shortest path can incur long outages. The weight $\mu$ sets the balance between these two goals.

## System model

- Area of $2\times2$ km with 300 buildings per unit area, Rayleigh-distributed heights, 8 base stations and 24 cells in the simulations.
- Outage probability per position is derived from LoS/NLoS state and distance and stored as a radio map at $H_{\max}=100$ m.
- Horizontal and vertical flight power depend on speed and the current total weight $W(t)$.

## Method

IACO adds speed choice and communication scheduling to ant colony search over the delivery order. D3QN agents operate on the radio-map grid and learn trajectories between delivery points. The combination is called HDRL.

## Key findings

- For $K=8$, IACO reduces energy by about 32.78% relative to ACO.
- HDRL improves on sequence-only ACO and IACO schemes by about 6% to 63% depending on the comparison.
- HDRL improves on a reward-reshaped D3QN by about 23% to 33%, and on distance-based HDRL and fixed-speed HDRL by about 25% and 15%.
- Larger $\mu$ shortens outage time and increases energy consumption.

## Limitations / future work

The model uses one cargo UAV. The authors plan to study collaboration mechanisms among multiple cargo UAVs.

## Relation to the corpus

Shares the radio-map cargo-logistics line with [[cao-2026-radio-map-cargo-pickup]] and [[huang-2026-hgadrl-cargo-uav-pickup-delivery]], and adds explicit outage-time weighting to [[radio-map-aided-uav-path-planning]]. Handoff-oriented counterparts appear in [[handoff-aware-uav-trajectory-planning]].

## Raw artifacts

- Parse: `raw/sources/Balancing_Energy_Efficiency_and_Communication_Quality_in_UAV_Cargo_Delivery_Systems/Balancing_Energy_Efficiency_and_Communication_Quality_in_UAV_Cargo_Delivery_Systems.md`
- Origin PDF and extracted figures are in the same folder.
