---
type: source
title: "Methods to Assign UAVs for K-Coverage and Recharging in IoT Networks"
authors: ["Zilin Song", "Kwan-Wu Chin", "Changlin Yang", "Montserrat Ros"]
year: 2024
url: "https://doi.org/10.1109/TMC.2023.3259461"
venue: "IEEE Transactions on Mobile Computing, 23(4)"
modeling_card: required
tags: [source, k-coverage, uav-charging, solar-charging-platform, mixed-integer-linear-programming, model-predictive-control, monte-carlo-tree-search]
related:
  - "[[uav-charging-scheduling]]"
  - "[[mixed-integer-linear-programming]]"
  - "[[energy-harvesting-mec]]"
  - "[[energy-causality-constraint]]"
  - "[[persistent-emergency-uav-swarm-service]]"
created: 2026-11-02
updated: 2026-11-02
---

# Methods to Assign UAVs for K-Coverage and Recharging in IoT Networks

## Citation

Song, Z., Chin, K.-W., Yang, C., & Ros, M. (2024). *Methods to Assign UAVs for K-Coverage and Recharging in IoT Networks*. **IEEE Transactions on Mobile Computing, 23**(4). DOI: 10.1109/TMC.2023.3259461.

## TL;DR

UAVs must keep at least $K$ of a set of monitoring points covered in every slot while recharging at solar-powered platforms whose energy arrivals vary in space and time. The paper writes an MILP that maximizes consecutive K-coverage lifetime with non-causal energy knowledge, then proposes a GMM-forecast MPC and an MCTS heuristic that reach about 81.04% and 67.07% of the MILP optimum.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A set $\mathcal U$ of UAVs, a set $\mathcal M$ of monitoring points on a path $\Lambda$, and a set $\mathcal C$ of solar charging platforms with batteries over $T$ slots. In each slot a UAV is at one charging platform, at one monitoring point, or disconnected. Flying between locations, hovering, and charging change UAV and platform energy levels across slots.

**Problem & objective**: MILP (45): $\max_x\sum_{t=1}^T\xi_t$, the number of consecutive slots with K-coverage.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Charging assignment | $\alpha^t_{ij}$ | binary | UAV $u_i$ is on charging platform $c_j$ in slot $t$ |
| Monitoring assignment | $\beta^t_{ik}$ | binary | UAV $u_i$ is at monitoring point $p_k$ in slot $t$ |
| Activity | $\gamma^t_i$ | binary | UAV $u_i$ is active rather than disconnected |
| K-coverage flag | $\xi_t$ | binary | Slot $t$ has at least $K$ monitored points |
| Energy and transition variables | $r^t_j$, $v^t_i$, $\delta^t_j$, $\varepsilon^t_i$, $w^t_{ijk}$, $x^t_{ijk}$, $y^t_{ikk'}$, $z^t_{ijj'}$ | continuous or binary | Platform and UAV energy states and movements between locations |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (1) | A platform charges at most one UAV per slot, $\sum_i\alpha^t_{ij}\le1$. |
| (2) | At most one UAV hovers at each monitoring point, $\sum_i\beta^t_{ik}\le1$. |
| (4) | One location per UAV, $\sum_j\alpha^t_{ij}+\sum_k\beta^t_{ik}+(1-\gamma^t_i)=1$. |
| (42)-(43) | Link $\xi_t$ to coverage, $\sum\beta^t_{ik}-K\le(M_2-K)\xi_t$ and $\sum\beta^t_{ik}\ge K\xi_t$. |
| (44) | Consecutive coverage, $\xi_{t+1}\le\xi_t$. |
| Energy | UAV and platform energy evolve with flight, hovering, charging, and solar arrivals. |

**Algorithm**: MILP gives the offline optimum with non-causal solar arrivals. MPC forecasts arrivals with a Gaussian mixture model and re-solves the MILP over a receding horizon. MCTS uses Monte Carlo simulations to choose the current slot's assignment at lower computation time.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Song et al. [x] studied a coverage problem in Internet of Things networks that use UAVs supported by solar-powered charging platforms. The problem is to assign each UAV to either a charging station or a monitoring point over a planning horizon, subject to K-coverage, where K of a set of points must be monitored by a UAV in each time slot. They formulated a mixed integer linear program to maximize the K-coverage lifetime, noting that the energy levels of charging platforms and UAVs are coupled across time slots and that the program requires non-causal energy-arrival information. They then proposed a model predictive control approach and a Monte Carlo tree search based solution. Simulation results show that the two methods achieve approximately 81.04% and 67.07% of the optimal results computed by the mixed integer linear program.

## Problem framing

Charging platforms in rural or post-disaster areas may lack grid power and run on solar energy. Their varying energy arrivals mean that sending a UAV to the nearest platform can waste energy if that platform has little stored energy.

## System model

- Solar conversion efficiency of 20% at charging platforms.
- Coverage lifetime counts consecutive slots with K-coverage; once broken it does not resume.
- Benchmarks REAA and UIAA use simpler assignment rules.

## Method

MPC uses only predicted solar arrivals, so it can be myopic and suffer estimation error. MCTS trades solution quality for lower computation time compared with MPC.

## Key findings

- MPC averages 81.04% and MCTS 67.07% of the MILP coverage lifetime as UAVs increase from four to eight.
- With ten UAVs, REAA and UIAA reach 64.27% and 54.7% of MILP.
- With one charging platform, REAA and UIAA reach 57.34% and 38.22% of MILP; MCTS averages 94.78% of MPC.

## Limitations / future work

MILP needs non-causal energy arrivals, and the online methods depend on forecast quality.

## Relation to the corpus

Adds renewable-powered platforms to [[uav-charging-scheduling]], coupling UAV and platform energy states as in [[energy-harvesting-mec]] and [[energy-causality-constraint]].

## Raw artifacts

- Parse: `raw/sources/Methods_to_Assign_UAVs_for_K-Coverage_and_Recharging_in_IoT_Networks/Methods_to_Assign_UAVs_for_K-Coverage_and_Recharging_in_IoT_Networks.md`
- Origin PDF and extracted figures are in the same folder.
