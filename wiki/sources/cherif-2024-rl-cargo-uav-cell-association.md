---
type: source
title: "RL-Based Cargo-UAV Trajectory Planning and Cell Association for Minimum Handoffs, Disconnectivity, and Energy Consumption"
authors: ["Nesrine Cherif", "Wael Jaafar", "Halim Yanikomeroglu", "Abbas Yongacoglu"]
year: 2024
url: "https://doi.org/10.1109/TVT.2023.3340177"
venue: "IEEE Transactions on Vehicular Technology, 73(5)"
modeling_card: required
tags: [source, cargo-uav, cellular-connected-uav, handoff, cell-association, q-learning, trajectory-planning]
related:
  - "[[handoff-aware-uav-trajectory-planning]]"
  - "[[cellular-connected-uav]]"
  - "[[device-association]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[cherif-2021-disconnectivity-aware-cargo-uav]]"
  - "[[nesrine-cherif]]"
  - "[[wael-jaafar]]"
  - "[[halim-yanikomeroglu]]"
  - "[[connectivity-aware-cargo-uav-path-planning]]"
created: 2026-11-02
updated: 2026-11-03
---

# RL-Based Cargo-UAV Trajectory Planning and Cell Association for Minimum Handoffs, Disconnectivity, and Energy Consumption

## Citation

Cherif, N., Jaafar, W., Yanikomeroglu, H., & Yongacoglu, A. (2024). *RL-Based Cargo-UAV Trajectory Planning and Cell Association for Minimum Handoffs, Disconnectivity, and Energy Consumption*. **IEEE Transactions on Vehicular Technology, 73**(5). DOI: 10.1109/TVT.2023.3340177.

## TL;DR

This correspondence extends disconnectivity-aware cargo-UAV path planning by letting the UAV choose its serving cell as well as its path. A tabular Q-learning agent chooses a motion direction and one of the three strongest-RSRP cells at each step, minimizing a weighted sum of energy, distance flown with RSRP below threshold, and handoffs on a Leuven cellular layout.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A cargo-UAV delivers one package from warehouse $\mathbf q_w$ to drop-off $\mathbf q_d$ at fixed altitude $h$ and speed $v$. At each grid location it receives RSRP reports from all $M$ cells; a link is unreliable when RSRP is below $T_{\mathrm{th}}$.

**Problem & objective**: P1, joint trajectory planning and cell association: $\min_{\mathcal T,\mathcal C} w_{\mathrm{en}}\sum_i E(v,d_{i,i+1})+w_{\mathrm{sig}}\sum_i\mathcal D(d_{i,i+1})+w_{\mathrm{ho}}\sum_i\eta_{i,i+1}$ with $w_{\mathrm{en}}+w_{\mathrm{sig}}+w_{\mathrm{ho}}=1$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Trajectory | $\mathcal T=\{\mathbf q_1,\dots,\mathbf q_{\lvert\mathcal T\rvert}\}$ | grid locations at altitude $h$ | Cargo-UAV path |
| Cell association | $\mathcal C=\{c_1,\dots,c_{\lvert\mathcal T\rvert}\}$ | $c_i\in\{1,\dots,M\}$ | Serving cell at each location |
| Handoff indicator | $\eta_{i,i+1}$ | binary | 1 when the serving cell changes |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| P1.a | Battery budget, $\sum_i E(v,d_{i,i+1})\le E_A(v,h)$. |
| P1.b | Mission endpoints, $\mathbf q_1=\mathbf q_w$ and $\mathbf q_{\lvert\mathcal T\rvert}=\mathbf q_d$. |
| Disconnectivity | $\mathcal D(d_{i,i+1})=d_{i,i+1}$ when both endpoint RSRPs are below $T_{\mathrm{th}}$, so disconnected flight is penalized. |

**Algorithm**: Model the mission as an MDP with the UAV as agent. The state is $s=\{\mathbf q_s,c_s\}$ (location and serving cell), actions pair one of eight motion directions with a cell among the $N=3$ strongest RSRPs, and the reward $\mathcal W(s,a)=w_{\mathrm{en}}W_{\mathrm{mo}}+w_{\mathrm{sig}}W_{\mathrm{sig}}+w_{\mathrm{ho}}W_{\mathrm{ho}}$ penalizes motion, disconnectivity, and cell changes. Tabular Q-learning with decaying epsilon-greedy exploration learns the policy over $10^4$ episodes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Cherif et al. [x] proposed a joint trajectory planning and cell association approach for cargo-UAVs that use cellular networks for command and control. They formulated the cargo-UAV mission as a multi-objective problem that minimizes energy consumption, reduces handoff events, and guarantees cellular reliability along the trajectory under a battery constraint. Reinforcement learning, specifically Q-learning whose actions pair a motion direction with a candidate serving cell, is used to jointly optimize the trajectory and cell association. Simulations in a 3 km by 3 km area of Leuven with 64 cells compare the method with shortest-path and RSRP-aware path planning. The results show fewer handoffs and lower disconnectivity than the benchmarks at the expense of a slight increase in battery consumption.

## Problem framing

Existing cellular networks were designed for ground users, so aerial users see unreliable links and frequent handoffs. The earlier DP formulation fixed the serving BS by heatmap; this paper makes the cell choice part of the decision.

## System model

- 20 three-sector and 2 two-sector BSs in Leuven, Belgium, giving 64 cells over a 20 m grid.
- Speed 30 m/s, available battery energy 2500 kJ, RSRP threshold $-65$ dBm.
- Default weights $(w_{\mathrm{en}},w_{\mathrm{sig}},w_{\mathrm{ho}})=(2.5\%,90\%,7.5\%)$, with a second setting $(4\%,80\%,16\%)$.

## Method

Q-learning uses discount 0.9 and learning rate 0.01, with exploration decaying from 0.99 to 0.01. Training converges from about episode 3500. Because P1 maps to a capacitated vehicle routing problem, it is NP-hard, motivating the learning approach.

## Key findings

- The shortest-path benchmark consumes the least energy but has the most handoffs and the highest disconnectivity at every tested altitude.
- RSRP-aware planning lowers disconnectivity through detours but ignores handoffs.
- Both proposed weight settings reduce handoffs and disconnectivity relative to the benchmarks with a slight battery increase.

## Limitations / future work

The evaluation covers one UAV at fixed altitude and speed on a single measured map.

## Relation to the corpus

Builds directly on [[cherif-2021-disconnectivity-aware-cargo-uav]] and illustrates [[handoff-aware-uav-trajectory-planning]] with learned [[device-association]].

## Raw artifacts

- Parse: `raw/sources/RL-Based_Cargo-UAV_Trajectory_Planning_and_Cell_Association_for_Minimum_Handoffs_Disconnectivity_and_Energy_Consumption/RL-Based_Cargo-UAV_Trajectory_Planning_and_Cell_Association_for_Minimum_Handoffs_Disconnectivity_and_Energy_Consumption.md`
- Origin PDF and extracted figures are in the same folder.
