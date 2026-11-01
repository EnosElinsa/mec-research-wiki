---
type: source
title: "Disconnectivity-Aware Energy-Efficient Cargo-UAV Trajectory Planning with Minimum Handoffs"
authors: ["Nesrine Cherif", "Wael Jaafar", "Halim Yanikomeroglu", "Abbas Yongacoglu"]
year: 2021
url: "https://doi.org/10.1109/ICC42927.2021.9500982"
venue: "ICC 2021 - IEEE International Conference on Communications"
modeling_card: required
tags: [source, cargo-uav, cellular-connected-uav, handoff, trajectory-planning, dynamic-programming, energy-efficiency]
related:
  - "[[handoff-aware-uav-trajectory-planning]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[cherif-2024-rl-cargo-uav-cell-association]]"
  - "[[nesrine-cherif]]"
  - "[[wael-jaafar]]"
  - "[[halim-yanikomeroglu]]"
created: 2026-11-02
updated: 2026-11-02
---

# Disconnectivity-Aware Energy-Efficient Cargo-UAV Trajectory Planning with Minimum Handoffs

## Citation

Cherif, N., Jaafar, W., Yanikomeroglu, H., & Yongacoglu, A. (2021). *Disconnectivity-Aware Energy-Efficient Cargo-UAV Trajectory Planning with Minimum Handoffs*. **ICC 2021 - IEEE International Conference on Communications**. DOI: 10.1109/ICC42927.2021.9500982.

## TL;DR

A cargo-UAV flying beyond visual line of sight needs cellular command-and-control links served by down-tilted terrestrial base stations. The paper plans a grid trajectory that trades propulsion energy against the number of handoffs while capping the fraction of the mission spent in coverage holes, and solves it with dynamic programming.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One cargo-UAV flies at constant speed $v$ and altitude $h$ from a warehouse to a drop-off point over an area served by terrestrial BSs with 3-D antenna patterns. A connectivity heatmap assigns each grid cell a serving BS ID, with ID 0 marking a coverage hole.

**Problem & objective**: P1, a multi-objective trajectory problem: $\min_{\mathcal T} w_1\sum_{i=1}^{\lvert\mathcal T\rvert-1}E(v,d_{i,i+1})+w_2\sum_{i=1}^{\lvert\mathcal T\rvert-1}\eta_{i,i+1}$, weighting energy against handoff events.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Trajectory | $\mathcal T=\{\mathbf q_1,\dots,\mathbf q_{\lvert\mathcal T\rvert}\}$ | ordered grid locations at altitude $h$ | Cargo-UAV path from START to END |
| Handoff indicator | $\eta_{i,i+1}$ | binary | 1 when consecutive serving BS IDs differ and are not both 0 |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| P1.a | Battery budget, $\sum_i E(v,d_{i,i+1})\le E_A(v,h)$. |
| P1.b | Disconnectivity rate, $d_{\mathrm{disc}}/(\lvert\mathcal T\rvert-1)\le\alpha_{\max}$. |
| Motion | Each step moves to one of the neighboring grid cells. |

**Algorithm**: Build transition matrices for distance, disconnectivity, and handoff costs between grid cells from the heatmap, then run a dynamic-programming shortest-path search that returns the trajectory minimizing the weighted cost while respecting the battery and disconnectivity limits.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Cherif et al. [x] studied trajectory planning for cargo-UAV delivery missions that rely on cellular connectivity for command and control. They formulated a multi-objective problem that minimizes the UAV's energy consumption and handoff rate, constrained by the battery size and a tolerated disconnectivity rate. Because of the problem's complexity, they proposed a dynamic programming based solution over a cellular connectivity heatmap. Simulations show that a more stringent disconnectivity requirement increases both the handoff rate and the energy consumption because the trajectories become longer. The study also examines the impact of UAV altitude, disconnectivity tolerance, receiver sensitivity, and environment type, and derives guidelines for cargo-UAV operations.

## Problem framing

Terrestrial BSs are down-tilted, so a UAV is served by antenna sidelobes and meets coverage holes and frequent cell changes. Each handoff adds signaling overhead that can destabilize command and control. The disconnectivity rate is the ratio of time spent disconnected from all cells to total mission time.

## System model

- 10 BSs in a 3GPP UMa environment with maximum antenna gain 8 dBi, downtilt $-10^\circ$, and transmit power 43 dBm.
- Constant speed 30 m/s and available battery energy of 2500 kJ in the default setting.
- Rotary-wing propulsion power determines the per-step energy $E(v,d)$.

## Method

Algorithm 1 discretizes the heatmap into an $M\times N$ grid, computes the maximum flyable distance from the battery, initializes transition matrices, and applies dynamic programming to find the weighted minimum-cost path under the constraints.

## Key findings

- Lower tolerated disconnectivity forces detours around coverage holes and lengthens the path.
- When high disconnectivity is tolerable, flying at the lowest permissible altitude on the most direct path reduces energy.
- A more sensitive receiver makes the path less dependent on the disconnectivity limit but raises handoffs.
- Low-density environments such as RMa are favorable for energy-efficient operation, while dense UMi areas need a revised frequency strategy to reduce inter-cell interference.

## Limitations / future work

The model uses one UAV, constant speed and altitude, and a static connectivity heatmap.

## Relation to the corpus

The RL extension of this formulation, with explicit cell association, is [[cherif-2024-rl-cargo-uav-cell-association]]. Both papers anchor [[handoff-aware-uav-trajectory-planning]] within the [[cellular-connected-uav]] track.

## Raw artifacts

- Parse: `raw/sources/Disconnectivity-Aware_Energy-Efficient_Cargo-UAV_Trajectory_Planning_with_Minimum_Handoffs/Disconnectivity-Aware_Energy-Efficient_Cargo-UAV_Trajectory_Planning_with_Minimum_Handoffs.md`
- Origin PDF and extracted figures are in the same folder.
