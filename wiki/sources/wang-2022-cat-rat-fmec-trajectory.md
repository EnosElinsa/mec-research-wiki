---
type: source
title: "Deep Reinforcement Learning Based Dynamic Trajectory Control for UAV-Assisted Mobile Edge Computing"
authors: ["Liang Wang", "Kezhi Wang", "Cunhua Pan", "Wei Xu", "Nauman Aslam", "Arumugam Nallanathan"]
year: 2022
url: "https://doi.org/10.1109/TMC.2021.3059691"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, uav-mec, trajectory-control, user-association, deep-q-network, prioritized-experience-replay, convex-optimization]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[deep-q-network]]"
  - "[[prioritized-experience-replay]]"
  - "[[two-stage-decomposition]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[energy-latency-tradeoff]]"
  - "[[zhang-2024-uav-task-offloading-ddpg]]"
  - "[[liu-2022-miso-uav-mec-trajectory]]"
  - "[[cunhua-pan]]"
  - "[[nauman-aslam]]"
created: 2026-05-31
updated: 2026-07-16
---

# Deep Reinforcement Learning Based Dynamic Trajectory Control for UAV-Assisted Mobile Edge Computing

## Citation

Wang, L., Wang, K., Pan, C., Xu, W., Aslam, N., & Nallanathan, A. (2022). *Deep Reinforcement Learning Based Dynamic Trajectory Control for UAV-Assisted Mobile Edge Computing*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2021.3059691. (Date of publication 16 February 2021; date of current version 31 August 2022.)

## TL;DR

A flying-MEC (F-MEC) platform where UAVs carry computation resource and serve user-equipment (UE) task offloading. The goal is to **minimize the total energy consumption of all UEs** by jointly optimizing user association, resource allocation, and UAV trajectory. Two algorithms are proposed: **CAT** (Convex-optimizAtion-based Trajectory control), which uses **block coordinate descent (BCD)** to alternate between trajectory and association/resource subproblems; and **RAT** (deep-Reinforcement-leArning-based Trajectory control), which uses two deep Q-networks (actor + critic) with **Prioritized Experience Replay (PER)** plus a low-complexity matching algorithm for association/resource. RAT matches CAT's performance but, once trained, adapts to **any UAV take-off points** and produces solutions far faster than the iterative convex method.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: $N$ UEs and $M$ flying MEC UAVs operate over $T$ slots. A UE executes locally ($j=0$) or associates with one UAV, while each UAV controls horizontal heading and displacement.

**Problem & objective**: The energy-minimization formulation $P_1=\min_{U,A,F}\sum_{i=1}^{N}\sum_{j=0}^{M}\sum_{t=1}^{T}a_{ij}(t)E_{ij}(t)$ jointly selects trajectories, associations, and CPU allocations.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV movement | $U=\{\theta_j^h(t),d_j(t)\}$ | continuous, bounded | Horizontal heading and distance per slot |
| User association | $a_{ij}(t)$ | binary | UE $i$ uses local mode or UAV $j$ |
| CPU allocation | $f_{ij}^{C}(t),f_{ij}^{L}(t)$ | continuous, nonnegative | UAV and local execution frequencies |
| UAV coordinates | $G_j(t)=[X_j(t),Y_j(t)]$ | continuous, area bounded | Horizontal trajectory derived from $U$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C2 | $a_{ij}(t)\in\{0,1\}$ and $\sum_{j=0}^{M}a_{ij}(t)=1$ |
| C3 | UAV load: $\sum_i a_{ij}(t)\le V^{\max}$ |
| C4-C5 | $0\le\theta_j^h(t)\le2\pi$ and $0\le d_j(t)\le d^{\max}$ |
| C6-C7 | Area bounds $0\le X_j(t)\le X^{\max}$ and $0\le Y_j(t)\le Y^{\max}$ |
| C8-C9 | Coverage $a_{ij}(t)R_{ij}(t)\le R^{\max}$ and deadline $T_{ij}(t)\le T^{\max}$ |
| C10 | UAV CPU capacity: $\sum_i a_{ij}(t)f_{ij}^{C}(t)\le f^{\max}$ |

**Algorithm**: CAT alternates a branch-and-bound association/resource subproblem with an SCA-based convex trajectory QCQP. RAT replaces the trajectory block with actor-critic DRL, prioritized replay, and a matching algorithm for association and resource allocation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] minimized UE energy in a flying MEC system by jointly choosing multi-UAV trajectories, user associations, and local or UAV CPU allocations. The mixed-integer formulation enforces one execution place per UE together with UAV load, movement, area, coverage, deadline, and computing-capacity constraints. Their CAT solver alternates a branch-and-bound scheduling block with an SCA trajectory block, whereas RAT uses actor-critic reinforcement learning, prioritized replay, and matching for faster dynamic decisions. The reported simulations showed that both methods outperform traditional trajectory controls, while the DRL design adapts to changing take-off locations after training.

## Problem framing

UEs have limited compute/battery; MEC helps, and **flying MEC (F-MEC)** carries compute on UAVs for more flexible service. Challenges: (1) minimize long-term energy of all UEs via proper user association (whether/which UAV to offload to); (2) allocate UAV onboard compute per offloaded UE; (3) control each UAV's real-time trajectory under dynamic conditions (e.g. UAVs taking off from different points). Traditional approaches (exhaustive search, quantized dynamic programming, discretized-trajectory convex methods) are high-complexity, sensitive to initial points, or lose control accuracy, and most consider only a single UAV.

## System model

- **Actors.** Multiple UAVs as flying MEC servers; UEs offloading tasks ([[multi-uav-assisted-mec]]).
- **Objective.** Minimize total energy consumption of all UEs ([[energy-latency-tradeoff]] — energy-focused).
- **Decisions.** User association (which UAV / whether to offload), UAV onboard compute allocation, UAV trajectory (flight direction + distance).

## Method

- **CAT (convex / optimization).** [[two-stage-decomposition|Block coordinate descent]] splits the problem into a trajectory subproblem and an association/resource subproblem, solved alternately to convergence.
- **RAT (DRL).** An actor [[deep-q-network|DQN]] decides UAV flight direction and distance; a critic DQN evaluates the actor's actions; the reward is the overall UE energy consumption. A minibatch is sampled with **Prioritized Experience Replay** ([[prioritized-experience-replay]]) to speed convergence. A **low-complexity matching algorithm** ([[matching-theory-for-resource-allocation]]) decides user association and resource allocation.
- **3-D extension.** Section 6 extends RAT to a 3-D scenario.

## Key findings

- RAT performs similarly to CAT in the abstract-level summary, and Section 7 reports RAT as the best-performing scheme across the simulated comparisons; both beat traditional baseline algorithms.
- Once trained, **RAT generalizes to arbitrary UAV take-off points** and returns trajectories with simple algebraic calculations instead of re-solving the optimization — useful for emergency scenarios (battlefields, earthquakes, large fires) where fast decisions matter.
- RAT with PER is **less sensitive to hyperparameters** (minibatch size, replay-buffer size) than reinforcement learning without PER.

## Limitations / future work

Simulation-based; the parse does not enumerate explicit limitations. The DRL actor-critic here is a **DQN-based** pair (discretized flight action) rather than a continuous-action policy-gradient method, which bounds trajectory granularity.

## Relation to the corpus

A foundational **convex-vs-DRL** UAV-MEC trajectory entry that explicitly pairs an optimization solver (CAT/BCD) with a DRL solver (RAT) on the same problem — the same "classical baseline + learned fast solver" contrast seen in [[yang-2022-stochastic-uav-mec-lyapunov]] (two-stage vs joint) and the decomposition + DDPG pipeline of [[zhang-2024-uav-task-offloading-ddpg]]. Its BCD trajectory + matching association resembles [[liu-2022-miso-uav-mec-trajectory]]'s alternating optimization, while RAT's generalize-to-any-takeoff-point argument anticipates the DRL "train once, deploy fast" motivation across the corpus's learned-trajectory works. Reinforces [[uav-trajectory-control]] and [[prioritized-experience-replay]] (the latter also central to [[shao-2024-drl-antijamming-mec]]).

## Raw artifacts

- `raw/sources/Deep_Reinforcement_Learning_Based_Dynamic_Trajectory_Control_for_UAV-Assisted_Mobile_Edge_Computing/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
