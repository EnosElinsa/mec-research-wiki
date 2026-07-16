---
type: source
title: "Trajectory Design and Resource Allocation for Multi-UAV Networks: Deep Reinforcement Learning Approaches"
authors: ["Zheng Chang", "Hengwei Deng", "Li You", "Geyong Min", "Sahil Garg", "Georges Kaddoum"]
year: 2022
url: "https://doi.org/10.1109/TNSE.2022.3171600"
venue: "IEEE Transactions on Network Science and Engineering (IEEE TNSE)"
modeling_card: required
tags: [source, multi-uav-assisted-mec, aerial-base-station, trajectory-design, resource-allocation, multi-agent-drl, user-association]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[multi-agent-td3]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[zhao-2022-matd3-multiuav-ec-offloading]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
  - "[[zheng-chang]]"
created: 2026-05-29
updated: 2026-07-16
---

# Trajectory Design and Resource Allocation for Multi-UAV Networks: Deep Reinforcement Learning Approaches

## Citation

Chang, Z., Deng, H., You, L., Min, G., Garg, S., & Kaddoum, G. (2022). *Trajectory Design and Resource Allocation for Multi-UAV Networks: Deep Reinforcement Learning Approaches*. **IEEE Transactions on Network Science and Engineering**. DOI: 10.1109/TNSE.2022.3171600.

## TL;DR

DRL-based trajectory design + resource allocation for a **multi-UAV communications** system where UAVs act as aerial base stations providing ubiquitous coverage. The objective is to maximize system utility over all served ground users (GUs) through a joint user-association, power-allocation, and trajectory-design problem. The authors propose a machine-learning strategic resource-allocation algorithm (combining RL + deep learning) and a **multi-agent DRL** scheme for distributed implementation without prior knowledge of network dynamics.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple fixed-altitude UAV base stations share one downlink spectrum and serve stationary ground users over slots $t\in\{1,\ldots,T\}$. Probabilistic LoS and NLoS air-to-ground loss and inter-UAV interference determine user rates, and each UAV must return to its base while respecting mobility and separation limits.

**Problem & objective**: Problem P1 is an NP-hard nonconvex combinatorial integer program that maximizes $\Upsilon_{sys}(\mathbf P,\boldsymbol\Psi,\mathbf B)=\log\left(\sum_{t=1}^{T}\sum_{u=1}^{U}R_u(t)\right)$ over power, trajectories, and associations.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User association | $\mathbf B=\{\beta_{m,u}(t)\}$ | binary, $\beta_{m,u}(t)\in\{0,1\}$ | Whether ground user $u$ is served by UAV $m$ in slot $t$ |
| Downlink power | $\mathbf P=\{p_{m,u}(t)\}$ | continuous, $0\leq p_{m,u}(t)\leq p_m^{\max}$; quantized for DRL | Power allocated by UAV $m$ to user $u$ |
| UAV trajectory | $\boldsymbol\Psi=\{\boldsymbol\psi_m(t)\}$ | continuous horizontal coordinates; quantized for DRL | Slot-by-slot horizontal position of UAV $m$ at fixed altitude $H$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 1 and C4 | Each UAV returns to its base, $\boldsymbol\psi_m(1)=\boldsymbol\psi_m(T)$ |
| 2 | Per-slot movement is bounded, $\|\boldsymbol\psi_m(t+1)-\boldsymbol\psi_m(t)\|\leq V_{\max}$ |
| 3 | UAV separation is safe, $\|\boldsymbol\psi_m(t)-\boldsymbol\psi_j(t)\|\geq S_{\min}$ |
| C1-C2 | Association is binary and each user has at most one UAV, $\sum_{m=1}^{M}\beta_{m,u}(t)\leq1$ |
| C3 | Transmit power is bounded, $0\leq p_{m,u}(t)\leq p_m^{\max}$ |
| C5 | Each served user meets its data-rate requirement, $R_u(t)\geq R_u^{\min}$ |

**Algorithm**: The centralized solution encodes rates and UAV battery levels as state and uses DQN with epsilon-greedy actions, experience replay, an online network, and a frozen target network to learn the joint association, power, and trajectory policy. The distributed extension uses centralized learning and decentralized execution, with each UAV maintaining a recurrent hidden state from its private observation and exchanging learned messages over a limited-bandwidth signaling channel.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chang et al. [x] studied joint trajectory design, user association, and downlink power allocation for multiple UAV base stations serving ground users over a finite horizon. They formulated an NP-hard mixed-integer utility-maximization problem with binary association, bounded transmit power, return-to-base, speed, inter-UAV separation, and minimum-user-rate constraints. Their centralized DQN uses system data rates and UAV battery levels as state, learns the joint action through replay and a target network, and is extended to a cooperative multi-agent scheme with centralized learning, decentralized execution, partial observations, and limited-bandwidth inter-UAV signaling. Simulations show that both DRL schemes outperform tabular Q-learning in throughput and utility, that centralized DRL gives the highest reported performance, and that multi-agent DRL remains close to it.

## Problem framing

Future mobile systems need ubiquitous connectivity over billions of devices; UAVs as flexible, low-cost aerial base stations help. The joint user-association + power-allocation + trajectory problem has a high-dimensional state space, motivating learning-based solutions, including a decentralized variant.

## System model

- **Actors.** Multiple UAVs as aerial base stations serving ground users.
- **Objective.** Maximize system utility over all served GUs.
- **Decisions.** User association, power allocation, trajectory design.

## Method

- A **machine-learning-based strategic resource-allocation algorithm** combining reinforcement learning and deep learning to design the optimal policy of all UAVs.
- A **multi-agent DRL** scheme for decentralized implementation without a-priori knowledge of network dynamics ([[multi-agent-td3]] family / [[centralized-training-decentralized-execution]]).

## Key findings

- Extensive simulations demonstrate advantages of the proposed schemes over baselines (qualitative; specific utility curves in the paper).

## Limitations / future work

Future work: improve multi-UAV system performance via energy-efficiency and delay optimization within the framework.

## Relation to the corpus

A **multi-UAV-as-base-station** trajectory/resource DRL entry — note this is a *communications* (coverage/utility) framing rather than compute offloading, distinguishing it from the offloading-centric [[zhao-2022-matd3-multiuav-ec-offloading]] and [[he-2023-fairness-3d-multiuav-maddpg]], with which it shares the multi-agent UAV-trajectory machinery. Reinforces [[multi-agent-td3]] and [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/Trajectory_Design_and_Resource_Allocation_for_Multi-UAV_Networks_Deep_Reinforcement_Learning_Approaches/full.md`
- Original PDF and extracted figures in the same folder.
