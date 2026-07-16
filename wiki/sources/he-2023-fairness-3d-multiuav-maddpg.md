---
type: source
title: "Fairness-Based 3-D Multi-UAV Trajectory Optimization in Multi-UAV-Assisted MEC System"
authors: ["Yejun He", "Youhui Gan", "Haixia Cui", "Mohsen Guizani"]
year: 2023
url: "https://doi.org/10.1109/JIOT.2023.3241087"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
modeling_card: required
tags: [source, multi-uav-assisted-mec, maddpg, fairness, trajectory-optimization, task-offloading, energy-efficiency]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[multi-agent-td3]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[jains-fairness-index]]"
  - "[[energy-balancing-uav]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
  - "[[zhao-2022-matd3-multiuav-ec-offloading]]"
created: 2026-05-29
updated: 2026-07-16
---

# Fairness-Based 3-D Multi-UAV Trajectory Optimization in Multi-UAV-Assisted MEC System

## Citation

He, Y., Gan, Y., Cui, H., & Guizani, M. (2023). *Fairness-Based 3-D Multi-UAV Trajectory Optimization in Multi-UAV-Assisted MEC System*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3241087.

## TL;DR

A 3-D dynamic multi-UAV-assisted MEC system in which ground devices (GDs) with real-time mobility and task updates select a target UAV for offloading. The authors formulate communication, computation, and flight energy as objectives **based on fairness among UAVs**, analytically derive the optimal GD selectivity and offloading strategy per slot, then learn the multi-UAV 3-D trajectories with **MADDPG**. They minimize total system energy while ensuring inter-UAV fairness.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Mobile ground devices generate new tasks each slot and use TDMA uplinks to multiple UAVs carrying MEC servers. UAVs move in three dimensions through probabilistic LoS/NLoS air-to-ground channels, compute partially offloaded tasks, consume rotary-wing propulsion energy, and include an auxiliary UAV to improve load fairness.

**Problem & objective**: Problem (22) minimizes fairness-weighted communication, computation, and flight energy over a horizon, $\min_{\mathcal K',\Psi,\Theta}\sum_{t=1}^{T}E(t)$, where $E(t)$ divides aggregate energy by the Jain fairness index $I(t)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Ground-device selection sets | $\mathcal K'_m$ | discrete partition of ground devices | Devices assigned to UAV $m$ |
| Partial-offloading ratio | $\varphi_{k,m}(t)$ | continuous, $0\leq\varphi_{k,m}(t)\leq1$ | Portion of device $k$'s task processed by UAV $m$ |
| UAV speed | $\nu_m(t)$ | continuous, $\nu_{\min}\leq\nu_m(t)\leq\nu_{\max}$ | Flight speed of UAV $m$ |
| Flight direction | $\theta_\nu^m(t),\theta_\mu^m(t)$ | continuous angular controls | Horizontal and vertical deflection angles defining the 3-D trajectory |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Ground devices and UAVs remain within the prescribed three-dimensional region |
| C2-C3 | Offloading ratios lie in $[0,1]$ and UAV speeds remain within their effective range |
| C4 | Distinct UAVs cannot occupy the same position in a slot |
| C5 | Every ground device selects exactly one UAV, $\sum_m\lvert\mathcal K'_m\rvert=K$ |
| C6 | The Jain load-fairness index satisfies $0\leq I(t)\leq1$ |

**Algorithm**: For fixed positions and device assignments, derive the per-device offloading ratio by equating local and offloaded completion components; initialize each device at its nearest UAV and run unilateral energy-improving selection updates until the assignment reaches a Nash equilibrium; use those per-slot decisions inside an MDP; let each UAV actor choose normalized speed and horizontal and vertical angles; train the multi-UAV trajectory policy with centralized MADDPG critics, replay, target networks, and energy-based rewards.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

He et al. [x] studied fairness-aware three-dimensional multi-UAV trajectory and task offloading in a dynamic MEC system. They formulated horizon energy minimization over ground-device UAV selection, partial offloading, and UAV speed and direction under region, speed, collision, assignment, and fairness constraints. Their solution derives the per-slot offloading ratio analytically, obtains a Nash-stable device-to-UAV assignment through unilateral energy improvements, and trains the cooperative trajectories with MADDPG. Simulations reported that the proposed offloading strategy reached a UAV fairness index of about 0.95 after 25,000 training episodes and adapted UAV altitude to ground-device dispersion.

## Problem framing

GDs have limited compute/energy, and multiple UAVs must share the load fairly. The paper separates the decision into (a) which UAV a GD offloads to and how much (selectivity + offloading strategy, derived analytically) and (b) how UAVs move in 3-D over a horizon (learned).

## System model

- **Actors.** Multiple UAVs at 3-D positions; mobile GDs with task updates each slot.
- **Objectives.** Communication, computation, and flight energy, framed for fairness among UAVs.
- **Per-slot result.** Optimal GD selectivity and offloading strategy obtained by theoretical analysis/derivation (with extreme-value/differentiability arguments shown in the appendix).

## Method

- **Per slot t:** closed-form/derived offloading strategy and UAV selection for each GD.
- **Over horizon T:** model UAV trajectories as a sequence of joint location updates and solve with **MADDPG** (multi-agent DDPG) for the cooperative trajectory problem ([[multi-agent-td3]] family / [[centralized-training-decentralized-execution]]).

## Key findings

- Simulations show minimum total system energy (communication + computation + flight) **under the fairness premise**, and validate the rationality/effectiveness of the algorithm (qualitative; specific energy curves in the paper).

## Limitations / future work

Future work: multi-UAV communications across multiple cells and more novel trajectory designs.

## Relation to the corpus

Adds a **fairness-among-UAVs** angle to the multi-UAV trajectory + offloading track, complementing the energy-balancing fairness of [[huang-2023-mu-aec-task-energy]] and [[nabi-2025-jour-hierarchical-aerial]], and the safety-constrained heterogeneous-fleet trajectory work [[zhang-2025-ssac-mgi-heterogeneous-uav]]. Methodologically it shares the MADDPG/MATD3 cooperative-trajectory pattern with [[zhao-2022-matd3-multiuav-ec-offloading]] and [[chang-2022-marl-multiuav-trajectory]]. Reinforces [[energy-balancing-uav]] and [[jains-fairness-index]].

## Raw artifacts

- `raw/sources/Fairness-Based_3-D_Multi-UAV_Trajectory_Optimization_in_Multi-UAV-Assisted_MEC_System/full.md`
- Original PDF and extracted figures in the same folder.
