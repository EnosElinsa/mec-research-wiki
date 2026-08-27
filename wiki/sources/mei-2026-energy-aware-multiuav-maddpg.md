---
type: source
title: "Energy-Aware Multi-UAV Collaboration for Data Collection and Trajectory Planning With MADDPG"
authors: ["Jing Mei", "Jinglei Xu", "Zhao Tong", "Keqin Li"]
year: 2026
url: "https://doi.org/10.1109/TNSM.2026.3721502"
venue: "IEEE Transactions on Network and Service Management, 23"
modeling_card: required
tags: [source, multi-uav, data-collection, trajectory-planning, energy-aware, maddpg]
related:
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[uav-trajectory-control]]"
  - "[[uav-data-collection]]"
created: 2026-08-27
updated: 2026-08-27
---

# Energy-Aware Multi-UAV Collaboration for Data Collection and Trajectory Planning With MADDPG

## Citation

Mei, J., Xu, J., Tong, Z., & Li, K. (2026). *Energy-Aware Multi-UAV Collaboration for Data Collection and Trajectory Planning With MADDPG*. **IEEE Transactions on Network and Service Management, 23**. DOI: 10.1109/TNSM.2026.3721502.

## TL;DR

This paper trains cooperating UAVs to collect ground-user data while respecting propulsion, communication, return-to-base, boundary, coverage, and collision constraints. A continuous-action MADDPG policy balances collected data with residual energy after successful return.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $K$ UAVs fly at fixed altitude over an $L\times L$ area and collect residual data from $M$ ground users in time slots. Each UAV has finite battery and must return to its base under a reserve threshold.

**Problem & objective**: Maximize collected data; when all user tasks are complete, additionally maximize residual energy through the paper's completion indicator, $\max D_{\mathrm{collected}}+\lambda\sum_k(E_k^{\mathrm{cons}}-\sum_tE_k(t))$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Heading | $\theta_k$ | continuous angle | Flight direction of UAV $k$ |
| Flight duration | $T_k^{\mathrm{fly}}$ | continuous | Duration of the action segment |
| UAV trajectory | $\mathbf u_k(t)$ | continuous position | Resulting UAV path |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Energy | Each UAV remains within its flight, hover, communication, and reserve energy budget. |
| Return | $\mathbf u_k(0)=\mathbf u_k(T)$ and reserve-to-base conditions are enforced. |
| Coverage | User data can be collected only while a UAV is within the modeled communication region. |
| Safety | UAVs remain inside the area and satisfy collision-separation constraints. |

**Algorithm**: Use centralized training with decentralized MADDPG actors, local observations of positions, residual energy, and residual user data, and a global critic with replay and target networks.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Mei et al. [x] formulated cooperative multi-UAV data collection as a continuous-action control problem with explicit propulsion, communication, reserve-energy, and collision constraints. Their objective combines collected user data with residual energy when all collection tasks complete. Centralized-training and decentralized-execution MADDPG actors choose each UAV's heading and flight duration from local observations. Simulations report higher completion and residual-energy performance than MATD3, MASAC, MAPPO, MAAC, and clustering baselines in the tested settings. The study assumes fixed altitude and leaves intermittent links, wind, asynchronous training, and heterogeneous UAVs for future work.

## Problem and system model

UAVs fly, hover, communicate with ground users, and return to base under a reserve threshold. Their motion and energy decisions are coupled because longer collection paths consume the reserve needed for safe return.

## Method

The paper defines a continuous MDP and trains MADDPG with decentralized actors and a centralized critic. Reward terms represent collected data, successful return energy, boundary violation, and collision penalties.

## Key findings

- Six-UAV scaling raises reported task-completion rate from 8.8% to 53.8% in the evaluated sweep.
- MADDPG obtains the highest reward and residual energy among the compared multi-agent methods.
- The reported default setting achieves about 0.95 service completion and 0.974 data collection.

## Limitations / future work

The model uses fixed altitude and idealized communication assumptions. Future work targets asynchronous training, learned topologies, intermittent links, wind, and heterogeneous vehicles.

## Relation to the corpus

This source connects [[maddpg]] and [[centralized-training-decentralized-execution]] to energy-aware multi-UAV data collection and trajectory control.

## Raw artifacts

- Parse: `raw/sources/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG/Energy-Aware_Multi-UAV_Collaboration_for_Data_Collection_and_Trajectory_Planning_With_MADDPG.md`
- Origin PDF and figures are in the same folder.
