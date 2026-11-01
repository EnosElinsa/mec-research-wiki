---
type: source
title: "A Two-Timescale Learning-Based Stochastic Game for Energy-Efficient UAV Trajectory Planning and Replacement in Hierarchical Aerial Computing"
authors: ["Jialiuyuan Li", "You Shi", "Chen Dai", "Yongjian Fan", "Changyan Yi", "Xiankun Ge", "Jiantao Shi"]
year: 2026
url: "https://doi.org/10.1109/TVT.2026.3664926"
venue: "IEEE Transactions on Vehicular Technology, 75(7)"
modeling_card: required
tags: [source, hierarchical-aerial-mec, uav-replacement, two-timescale-optimization, stochastic-game, multi-agent-drl, energy-efficiency, high-altitude-platform]
related:
  - "[[hierarchical-aerial-mec]]"
  - "[[two-timescale-optimization]]"
  - "[[stochastic-game]]"
  - "[[nash-equilibrium]]"
  - "[[battery-swapping-uav-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[gupta-not-in-parse-uav-replacement]]"
  - "[[shi-2023-two-timescale-migration-rerouting]]"
created: 2026-11-02
updated: 2026-11-02
---

# A Two-Timescale Learning-Based Stochastic Game for Energy-Efficient UAV Trajectory Planning and Replacement in Hierarchical Aerial Computing

## Citation

Li, J., Shi, Y., Dai, C., Fan, Y., Yi, C., Ge, X., & Shi, J. (2026). *A Two-Timescale Learning-Based Stochastic Game for Energy-Efficient UAV Trajectory Planning and Replacement in Hierarchical Aerial Computing*. **IEEE Transactions on Vehicular Technology, 75**(7). DOI: 10.1109/TVT.2026.3664926.

## TL;DR

UAVs and a HAP jointly serve mobile IoT devices, but UAV trajectory and replacement decisions can only change on a slow timescale while task delegation and bandwidth change every slot. The paper maximizes long-term energy efficiency with two coupled multi-agent stochastic games, proves a Nash equilibrium exists, and learns it with the UTRTD multi-agent actor-critic algorithm.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A hierarchical aerial computing system with $N$ mobile IoT devices, $M$ UAVs, and one HAP. Devices offload tasks of type $c$ with data size $D_c$, cycles per bit $\varepsilon_c$, and delay tolerance $\iota_c$ to UAVs or the HAP; UAVs may delegate tasks to the HAP. A low-energy UAV is replaced, and its devices are served by a substituting UAV or the HAP during replacement. Large-timescale frames contain small-timescale slots $\tau_t$.

**Problem & objective**: $[\mathcal P1]$: $\max\frac1T\sum_{t=1}^T\Omega(t)$, where $\Omega(t)$ is the data size of tasks fully processed within $\min\{\iota_c,T^{slot}\}$ divided by UAV trajectory, replacement, return, delegation, and computing energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Flight direction and speed | $\phi_m(t)$, $v^{traj}_m(t)$ | continuous | Large-timescale trajectory of UAV $m$ |
| Replacement indicator | $\epsilon_m(t)$ | binary | Whether UAV $m$ is replaced in frame $t$ |
| Replacement speed | $v^{repl}_m(t)$ | $(0,\epsilon_m(t)v^{\max}]$ | Speed of the replacing flight |
| Substitute selection | $\psi_m(t)$ | binary | Covered devices offload to a substituting UAV or to the HAP |
| Task delegation | $\delta_{m,n}(\tau_t)$ | binary | UAV $m$ forwards device $n$'s task to the HAP |
| Bandwidth | $B^U_m(\tau_t)$, $B^H_m(\tau_t)$ | continuous, nonnegative | Small-timescale UAV and HAP bandwidth |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (17a) | UAVs stay in the area, $x^U_m\in[X^{low},X^{up}]$, $y^U_m\in[Y^{low},Y^{up}]$. |
| (17b) | Minimum UAV separation, $d^{U2U}_{m,m'}(t)\ge d^{\min}$. |
| (17c)-(17d) | Direction, trajectory speed, and replacement speed ranges. |
| (17e) | Delegation only for tasks offloaded to that UAV, $\delta_{m,n}\in\{0,\varphi^{IU}_{m,n}\}$. |
| (17g) | HAP bandwidth budget, $\sum_m B^U_m(\tau_t)\le B^{Htotal}$. |
| (17i) | Residual energy covers the return flight, $E^{resi}_m\ge E^{retu}_m$. |

**Algorithm**: Reformulate $[\mathcal P1]$ as a large-timescale stochastic game for trajectory, replacement, and substitute selection and a small-timescale game for delegation and bandwidth, coupled through states and rewards. Prove NE existence, then train UTRTD, a multi-agent actor-critic method whose critics learn faster than actors, to reach the NE.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied hierarchical aerial computing in which UAVs and a high-altitude platform provide supplementary computational services to mobile IoT devices. They observed that task delegation must adapt on a small timescale while UAV trajectory planning and replacement operate on a large timescale because of the overhead of high-speed maneuvers. They proposed a two-timescale optimization framework that maximizes system energy efficiency and formulated the problem as two coupled multi-agent stochastic games capturing UAV-HAP interactions and system uncertainties. The existence of a Nash equilibrium is proved, and a reinforcement learning-based algorithm, UTRTD, is developed to jointly decide UAV trajectory planning, replacement, task delegation, and resource allocation. Simulation results show that UTRTD outperforms its counterparts, with about 5% improvement over the best baseline.

## Problem framing

UAVs respond faster than the distant HAP but have limited coverage, computation, and energy, so they need periodic replacement. Replacement interrupts coverage unless another UAV or the HAP takes over the affected devices, which links replacement planning to task delegation.

## System model

- IoT devices move, and task data sizes are uniformly distributed within type-specific bounds.
- A task counts toward $\Omega(t)$ only when fully processed within its delay tolerance and one slot, through local UAV computing, HAP offloading, or UAV-to-HAP delegation.
- UAV energy includes trajectory, replacement, and return propulsion plus delegation and computing energy.

## Method

Actor networks use layers (64, 64, 32, 32) and critics (256, 256, 128, 64). The paper analyzes UTRTD signaling overhead and computational complexity.

## Key findings

- UTRTD converges after about 200 training episodes with actor and critic learning rates 0.001 and 0.01.
- Slower learning rates converge more slowly and tend toward local optima.
- UTRTD reports about 5% higher energy efficiency than the best baseline.

## Limitations / future work

Each task is processed within one slot, so task flows across slots, task priority scheduling, and resource conflicts are simplified.

## Relation to the corpus

Extends [[hierarchical-aerial-mec]] with explicit UAV replacement, complementing the throughput-oriented replacement model in [[gupta-not-in-parse-uav-replacement]] and the station-based energy replenishment in [[battery-swapping-uav-mec]]. Its timescale split follows [[two-timescale-optimization]], as does the migration and rerouting design in [[shi-2023-two-timescale-migration-rerouting]].

## Raw artifacts

- Parse: `raw/sources/A_Two-Timescale_Learning-Based_Stochastic_Game_for_Energy-Efficient_UAV_Trajectory_Planning_and_Replacement_in_Hierarchical_Aerial_Computing/A_Two-Timescale_Learning-Based_Stochastic_Game_for_Energy-Efficient_UAV_Trajectory_Planning_and_Replacement_in_Hierarchical_Aerial_Computing.md`
- Origin PDF and extracted figures are in the same folder.
