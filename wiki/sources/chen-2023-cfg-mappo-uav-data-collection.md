---
type: source
title: "Joint Optimization of Trajectory and User Association via Reinforcement Learning for UAV-Aided Data Collection in Wireless Networks"
authors: ["Gong Chen", "Xiangping Bryce Zhai", "Congduan Li"]
year: 2023
url: "https://doi.org/10.1109/TWC.2022.3216049"
venue: "IEEE Transactions on Wireless Communications, 22(5)"
modeling_card: required
tags: [source, uav-data-collection, user-association, coalition-formation-game, mappo, dec-pomdp, fairness, energy-efficiency]
related:
  - "[[uav-data-collection]]"
  - "[[coalition-formation-game]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[jains-fairness-index]]"
  - "[[device-association]]"
created: 2026-11-02
updated: 2026-11-02
---

# Joint Optimization of Trajectory and User Association via Reinforcement Learning for UAV-Aided Data Collection in Wireless Networks

## Citation

Chen, G., Zhai, X. B., & Li, C. (2023). *Joint Optimization of Trajectory and User Association via Reinforcement Learning for UAV-Aided Data Collection in Wireless Networks*. **IEEE Transactions on Wireless Communications, 22**(5). DOI: 10.1109/TWC.2022.3216049.

## TL;DR

Several UAVs collect data from heterogeneous ground users without a central controller. The paper maximizes fairness-weighted energy efficiency, solving discrete user association with a coalition formation game that reaches a Nash equilibrium and continuous trajectories with MAPPO under centralized training and decentralized execution.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $N$ UAVs fly over $M$ ground users (GUs) in region $\mathcal F$ over slots $\mathcal T$. Uplink SINR includes interference between UAVs. Fairness is measured by a fairness index $\hat f(t)$ and energy efficiency by $E(t)$.

**Problem & objective**: (P1): $\max_{\{a_{n,m}(t)\},\{\mathbf u_n(t)\}}\hat f(t)\cdot E(t)$, a nonconvex mixed-integer problem reformulated as a DEC-POMDP.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Association | $a_{n,m}(t)$ | binary | GU $m$ is associated with UAV $n$ |
| UAV position | $\mathbf u_n(t)$ | continuous in $\mathcal F$ | Trajectory of UAV $n$ |
| Speed and yaw | $v_n(t)$, $d_n(t)$, $\theta_n(t)$ | $v\in[0,v_{\max}]$, $d\in[0,1]$, $\theta\in[0,2\pi]$ | Movement controls per slot |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (16a)-(16c) | Binary association; each GU is associated with one UAV. |
| (16d)-(16f) | Speed, distance ratio, and yaw-angle ranges. |
| (16g) | Collision avoidance, $\lVert\mathbf u_n-\mathbf u_{n'}\rVert\ge d_{\min}$. |
| (16h) | UAVs stay within the data-collection region $\mathcal F$. |

**Algorithm**: Formulate association as a non-cooperative game and solve it with a coalition formation game algorithm (centralized or decentralized) that converges to NE. Train MAPPO under CTDE to control continuous trajectories and energy, combining both in EETD-CFG.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] investigated multiple UAVs that cooperatively fly over heterogeneous ground users and collect data without a central controller. Considering signal-to-interference-and-noise ratio and fairness among users, they jointly optimized UAV trajectories and ground-user associations to maximize total throughput and energy efficiency. The long-term problem is formulated as a decentralized partially observed Markov decision process and solved by combining a coalition formation game with multi-agent deep reinforcement learning. The discrete association problem is modeled as a non-cooperative game whose decentralized coalition formation algorithm converges to a Nash equilibrium, while a multi-agent reinforcement learning method optimizes trajectories and energy consumption with centralized training and decentralized execution. Simulation results show that the approach outperforms commonly used schemes in fair throughput and energy consumption, for example achieving a 12.5% higher average fairness index than MADDPG at a 120 m communication range.

## Problem framing

Discrete association and continuous trajectory decisions are coupled, and a single RL action space handles both poorly. Splitting them between a game and MAPPO keeps each part tractable.

## System model

- UAV-GU links suffer interference from other UAVs.
- Fairness is evaluated across GUs, and energy efficiency over the mission.

## Method

The coalition formation game handles association; MAPPO handles movement.

## Key findings

- With 2 UAVs, the fairness index reaches 0.8877, 5.6% above EETD-BR.
- Reported gains include 15.3% in fairness and 9.7% in energy efficiency, and 28.6% over MADDPG in one metric.
- At 120 m range, EETD-CFG beats MADDPG by 12.5% in fairness and EETD-Greedy by 8.7% in energy efficiency.

## Limitations / future work

The conclusion lists future extensions that are truncated in the parse.

## Relation to the corpus

Combines [[coalition-formation-game]] association with [[mappo]] under [[centralized-training-decentralized-execution]] for [[uav-data-collection]].

## Raw artifacts

- Parse: `raw/sources/Joint_Optimization_of_Trajectory_and_User_Association_via_Reinforcement_Learning_for_UAV-Aided_Data_Collection_in_Wireless_Networks/Joint_Optimization_of_Trajectory_and_User_Association_via_Reinforcement_Learning_for_UAV-Aided_Data_Collection_in_Wireless_Networks.md`
- Origin PDF and extracted figures are in the same folder.
