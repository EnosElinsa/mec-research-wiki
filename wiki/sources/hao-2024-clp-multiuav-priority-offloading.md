---
type: source
title: "Joint Task Offloading, Resource Allocation, and Trajectory Design for Multi-UAV Cooperative Edge Computing With Task Priority"
tags: [source, multi-uav-mec, task-offloading, task-priority, trajectory-design, hybrid-action, drl, td3, binary-offloading]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[task-priority-in-mec]]"
  - "[[hybrid-action-decision-making]]"
  - "[[td3]]"
  - "[[hybrid-action-representation]]"
  - "[[priority-based-delay-utility]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[blockage-aware-channel-model]]"
  - "[[load-balancing-uav-mec]]"
  - "[[hao-2025-priority-aware-task-driven-co]]"
  - "[[ma-2025-pdqn-vehicular-mec]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
  - "[[qin-2025-bcuav-masac]]"
created: 2026-05-29
updated: 2026-07-16
authors: [Hao Hao, Changqiao Xu, Wei Zhang, Shujie Yang, Gabriel-Miro Muntean]
year: 2024
url: "https://doi.org/10.1109/TMC.2024.3350078"
venue: "IEEE Transactions on Mobile Computing (TMC), Vol. 23, No. 9"
modeling_card: required
---

# Joint Task Offloading, Resource Allocation, and Trajectory Design for Multi-UAV Cooperative Edge Computing With Task Priority

## Citation

Hao, H., Xu, C., Zhang, W., Yang, S., & Muntean, G.-M. (2024). *Joint Task Offloading, Resource Allocation, and Trajectory Design for Multi-UAV Cooperative Edge Computing With Task Priority*. **IEEE Transactions on Mobile Computing, 23**(9). DOI: 10.1109/TMC.2024.3350078.

## TL;DR
This paper studies [[task-offloading]] in a cooperative [[multi-uav-assisted-mec]] system where UAVs both relay and compute tasks for ground users, and where tasks carry a **priority** that shapes how delay is rewarded. It jointly optimizes UAV trajectories, **binary** offloading decisions, computation resource allocation, and transmit power to maximize a long-term-average "system gain" (priority-based delay utility minus energy). The problem becomes an MDP with a discrete-continuous hybrid action space, solved by **CLP**, a [[td3]]-based DRL algorithm that learns a [[hybrid-action-representation]] latent space; CLP beats three to four state-of-the-art baselines on delay, completion ratio, and system gain.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple antenna-equipped UAVs relay and compute indivisible priority-labeled UE tasks and may forward them to another UAV or an edge cloud. G2A and A2G links use probabilistic LoS/NLoS pathloss, A2A links use free-space loss, separate bandwidths support the three link types, and UAVs move in three dimensions while avoiding collisions.

**Problem & objective**: Problem (41) maximizes priority-aware delay utility minus energy over an infinite horizon, $\max_{\boldsymbol\gamma,\mathbf w,\mathbf p,\mathbf f}\lim_{T\to\infty}\frac1T\sum_{t=1}^{T}\sum_{m=1}^{M}F_m(t)$, where $F_m(t)=w_1U_m(t)-w_2E_m(t)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Binary processing target | $\gamma_m^n(t)$ | binary, $\{0,1\}$ | Whether UE $m$'s task is processed locally, by UAV $n$, or by the edge cloud |
| UAV position | $\mathbf w_n(t)$ | continuous 3-D position | Trajectory point of UAV $n$ |
| Transmit power | $\mathbf p(t)$ | continuous, bounded | UE and UAV communication powers |
| UAV computation allocation | $\mathbf f(t)$ | continuous, nonnegative and capacity-bounded | CPU resource assigned to UE tasks |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 41a-41b | UE and UAV transmit powers remain within their maximum values |
| 41c and Eq. (19) | Offloading is binary and exactly one local, UAV, or cloud target processes each task |
| 41d-41e | UAV positions remain in the service region and per-slot motion obeys the speed limit |
| Eqs. (1)-(4) | Altitude, horizontal and vertical movement, and pairwise collision-separation constraints hold |
| Eqs. (13), (22) | The serving UAV covers the UE and allocated UAV CPU does not exceed capacity |

**Algorithm**: Form an MDP from task tuples and UAV positions; encode each discrete processing target with a learned embedding and encode the coupled continuous controls with a conditional variational autoencoder; pretrain the hybrid representation with reconstruction, divergence, and state-residual losses; let a TD3 actor produce latent actions, decode them to feasible hybrid controls, and train twin critics, target networks, and the representation from replay; execute the actor and decoder after convergence.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hao et al. [x] studied priority-aware binary task offloading in a cooperative multi-UAV edge-computing system. They formulated a long-term mixed-integer problem that maximizes priority-based delay utility minus communication, computation, and flight energy over offloading, three-dimensional trajectories, transmit powers, and computation allocations. Their CLP algorithm learns a coupled discrete-continuous latent action representation with an embedding table and conditional variational autoencoder, then optimizes the latent policy with TD3. Simulations reported faster stable convergence at a learning rate of $10^{-3}$, the highest system gain among the evaluated methods, and approximately 100 percent completion for high-priority tasks with at least three UAVs.

## Problem
Terrestrial MEC struggles when users are dense or infrastructure is sparse, so UAVs are used to extend the edge — but their onboard energy and compute are limited, so offloading decisions matter a lot. The paper focuses on two aspects that prior multi-UAV work mostly ignores:
- **Task priority** ([[task-priority-in-mec]]): high-priority tasks (e.g. navigation, road sensing) have strict deadlines whose violation is costly, while low-priority tasks (e.g. entertainment) only affect user experience. Equal scheduling risks missing critical deadlines, but preemptive scheduling starves low-priority tasks.
- **Binary (indivisible) offloading** ([[binary-vs-partial-offloading]]): a complement to the more common partial offloading, applicable to indivisible tasks but turning the problem into a coupled discrete-continuous optimization.

The objective is the long-term average **system gain**, a weighted sum of a priority-based delay utility and (negative) energy consumption, jointly over [[uav-trajectory-control]], offloading, compute allocation, and power. The resulting problem is non-convex, dynamic, and needs future information — a natural fit for DRL.

## System model
- **Tiers / actors** ([[three-tier-cloud-edge-end]]): N UAVs, M ground UEs, one fixed edge cloud server (EC). A task has N+2 compute targets — local UE, any of the N UAVs, or the EC — so a UAV can offload to *another* UAV, realizing cooperation and [[load-balancing-uav-mec]].
- **Tasks**: time-slotted (~hundreds of ms); each task = (workload in CPU cycles, data size, allowed delay threshold, priority). Tasks are indivisible and processed at one location per slot.
- **Communication**: G2A (UE→UAV), A2A (UAV→UAV, full-duplex relay), A2G (UAV→EC) with separate bandwidths (20/40/10 MHz). G2A and A2G use a probabilistic LoS/NLoS path-loss model ([[blockage-aware-channel-model]]); A2A uses free-space path loss. Relaying does G2A and A2A in parallel (transmission delay = max of the two). Cross-interference and result-download cost are neglected.
- **Mobility & collisions**: 3D UAV positions with horizontal/vertical speed caps (49 m / 12 m per slot), height 50-100 m, and a pairwise minimum separation D_min = 50 m for collision avoidance.
- **Energy**: rotary-wing flight power proportional to v²; cubic-frequency compute energy with effective switched capacitance κ = 10⁻²⁸; EC energy excluded.
- **Priority utility** ([[priority-based-delay-utility]]): high-priority — log(1 + slack) if on time, fixed penalty if late; low-priority — fixed reward if on time, exponential decay if late (prevents starvation). This connects to [[qoe-modeling-mec]] via the long-tail latency-vs-experience intuition.

## Method
- **Formulation**: a mixed-integer long-term-average maximization transformed into an MDP with a **discrete-continuous hybrid action space** ([[hybrid-action-decision-making]]).
  - *State*: UE task properties + UAV 3D positions (positions act as a channel-quality proxy to keep state dimension O(N)).
  - *Action*: discrete offloading index per UE + continuous UAV moves, transmit power, and UAV compute allocation.
  - *Reward*: sum of per-UE system gains, with a large penalty (−1000) for constraint violations.
- **CLP algorithm**: combines a latent [[hybrid-action-representation]] (after HyAR) with [[td3]].
  - A shared learnable **embedding table** maps the N+2 discrete offloading actions to continuous vectors.
  - A **conditional VAE** encodes the continuous parameters into a Gaussian latent variable conditioned on state and discrete embedding; decoding uses nearest-neighbor lookup (discrete) + VAE decoder (continuous).
  - A cascaded **dynamics-prediction** head predicts the state residual; the representation is trained with reconstruction + KL + weighted prediction loss.
  - TD3 (twin critics, delayed/​smoothed updates) learns the policy over the latent space; training alternates a warm-up representation pre-training stage with the main learning stage.
- **Why the latent space**: directly rounding a continuous actor's output (as plain [[ddpg]] would) collapses distinct values to the same discrete action and degrades performance; encoding the *whole coupled* hybrid action preserves discrete-continuous correlations.

## Key findings
- **System gain** (200 slots): CLP ≈ 78 > CMA ≈ 70 > CNL ≈ 64 > NCO ≈ 58 > OSU ≈ 54.
- **Ablation**: full hybrid representation (CLP ≈ 84/slot) > discrete-only representation (ORD ≈ 80) > plain rounding (NAR ≈ 63→75, most unstable).
- **Convergence**: learning rate 10⁻³ converges fastest (~600 episodes) and stably; 10⁻⁴ slow (~1500 episodes); 10⁻² fluctuates into local optima.
- **Priority trade-off**: high-priority tasks (CLP-H) hit ~100% completion and lowest delay (~130 ms at ≥3 UAVs); low-priority tasks (CLP-L) are deliberately sacrificed, worst with a single UAV, catching up as UAV count grows.
- **Weights**: raising w1/w2 from 1 to 5 (×10³) cuts delay 183→141 ms but raises energy 1.8→2.3 (×10⁴ J).
- **Scaling**: more UAVs lower delay and raise gain; more UEs raise delay and lower completion ratio/gain (which plateaus as tasks spill to the cloud).
- **Energy**: CLP beats the multi-UAV baselines CMA/CNL but uses more energy than single-UAV NCO/OSU (which trade energy for much worse delay and gain).
- **Baselines**: OSU (single-UAV [[ddpg]], delay-only), NCO (single-UAV multi-objective [[ppo]]), CNL (cooperative but greedy/myopic), CMA (cooperative multi-agent [[td3]], partial offloading).

## Limitations
Simulation-only (no hardware). UAV-UE cross-interference and result-download cost are neglected; tasks are indivisible with one task per UE per slot. The priority design intentionally sacrifices low-priority performance, which is severe under scarce compute (single UAV). EC is assumed to have unlimited power, and the flight-energy model is a simplified speed-squared form.

## Relation to the corpus
This is a [[multi-uav-assisted-mec]] work centered on [[task-offloading]], [[uav-trajectory-control]], and [[task-priority-in-mec]], distinctive for combining **binary** offloading ([[binary-vs-partial-offloading]]) with a learned [[hybrid-action-representation]] over [[td3]]. It is a natural companion to [[hao-2025-priority-aware-task-driven-co]] (same lead author, priority-aware offloading) and to [[ma-2025-pdqn-vehicular-mec]], which tackles a similar discrete-continuous [[hybrid-action-decision-making]] problem with task priority via parameterized DQN. It also relates to multi-UAV trajectory/collision and DRL offloading work such as [[zhang-2025-ssac-mgi-heterogeneous-uav]], [[qin-2025-bcuav-masac]], and [[wu-2026-terrain-aware-uav-mec]], and to multi-UAV delay/energy trade-off studies like [[huang-2023-mu-aec-task-energy]].

## Raw artifacts
- `raw/sources/Joint_Task_Offloading_Resource_Allocation_and_Trajectory_Design_for_Multi-UAV_Cooperative_Edge_Computing_With_Task_Priority/full.md`
