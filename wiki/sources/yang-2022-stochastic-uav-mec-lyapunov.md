---
type: source
modeling_card: required
title: "Online Trajectory and Resource Optimization for Stochastic UAV-Enabled MEC Systems"
authors: ["Zheyuan Yang", "Suzhi Bi", "Ying-Jun Angela Zhang"]
year: 2022
url: "https://doi.org/10.1109/TWC.2022.3142365"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, uav-mec, lyapunov-optimization, online-algorithm, trajectory-optimization, stochastic-optimization, user-mobility]
related:
  - "[[ying-jun-angela-zhang]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[lyapunov-optimization]]"
  - "[[uav-trajectory-control]]"
  - "[[two-stage-decomposition]]"
  - "[[energy-latency-tradeoff]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
created: 2026-05-29
updated: 2026-07-16
---

# Online Trajectory and Resource Optimization for Stochastic UAV-Enabled MEC Systems

## Citation

Yang, Z., Bi, S., & Zhang, Y.-J. A. (2022). *Online Trajectory and Resource Optimization for Stochastic UAV-Enabled MEC Systems*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2022.3142365.

## TL;DR

A UAV-enabled MEC platform serving multiple mobile ground users with **random movements and task arrivals**. The goal is to minimize the average weighted energy of all users subject to average UAV-energy and data-queue-stability constraints. Formulated as a multi-stage stochastic optimization and converted via **Lyapunov optimization** into per-slot deterministic problems; two reduced-complexity methods solve resource allocation and UAV movement either **sequentially (two-stage)** or **jointly (one-step)**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One rotary-wing UAV-mounted MEC server serves $K$ mobile ground UEs over TDMA at a fixed altitude. UE locations follow a Gauss-Markov mobility model and task arrivals are stochastic Bernoulli processes; the UAV starts at $\mathbf p_I$, ends at $\mathbf p_F$, and uses a probabilistic LoS channel model.

**Problem & objective**: The multi-stage stochastic problem $\mathcal P_1$ minimizes the long-term weighted UE energy, $\min_{\boldsymbol f[n],\boldsymbol\delta[n],\mathbf p_u[n]}\lim_{N\to\infty}\frac{1}{N}\sum_{n=1}^{N}\sum_{k=1}^{K}w_k\big(E_k^c[n]+E_k^o[n]\big)$, under UAV energy and queue-stability requirements.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UE CPU frequency | $f_k[n]$ | continuous, $0\le f_k[n]\le f_k^m$ | Local computing rate of UE $k$ |
| Offloading duration | $\delta_k[n]$ | continuous, $\delta_k[n]\ge0$ | TDMA airtime allocated to UE $k$ |
| UAV position | $\mathbf p_u[n]$ | continuous, 2-D trajectory | Horizontal UAV location in slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 12b | Average UAV propulsion energy is bounded by $E^u$ |
| 12c | Actual task queues are mean-rate stable, with finite long-term average backlog |
| 12d | UE CPU frequencies satisfy $0\le f_k[n]\le f_k^m$ |
| 12e | TDMA durations satisfy $t_0+\sum_k\delta_k[n]\le\Delta$ |
| 12f | Processed local plus offloaded bits do not exceed backlog plus arrivals |
| 12g-12i | UAV endpoints and per-slot speed and reachability limits are enforced |

**Algorithm**: Lyapunov optimization adds a virtual UAV-energy queue and minimizes a drift-plus-penalty upper bound per slot. A two-stage solver first allocates UE resources and then updates the UAV trajectory, while a joint solver optimizes both blocks together using successive convex approximation and convex subproblems.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yang et al. [x] studied online trajectory and resource control for a UAV-enabled MEC server serving mobile users with stochastic arrivals. They minimized long-term weighted UE energy while enforcing average UAV propulsion energy, queue stability, CPU, TDMA, and flight constraints. Lyapunov drift-plus-penalty converts the multi-stage stochastic program into per-slot deterministic decisions, and two proposed solvers optimize resource allocation and UAV movement either sequentially or jointly. The analysis reports queue stability and satisfaction of the UAV energy constraint with an $O(1/V)$ energy and $O(V)$ queue tradeoff. Simulations compare the two proposed solvers with geometric-center, equal-allocation, and DDQN baselines under changing user mobility and task arrivals.

## Problem framing

UAV-MEC must serve users out of terrestrial coverage despite random user mobility and stochastic task arrivals. The long-term objective (average user energy) under UAV-energy and queue-stability constraints needs an online algorithm that doesn't require future knowledge.

## System model

- **Actors.** One UAV-MEC platform; multiple mobile ground users with random movement + task arrivals.
- **Objective.** Minimize average weighted user energy subject to average UAV energy and data-queue stability.
- **Tool.** [[lyapunov-optimization]] converts the multi-stage stochastic problem into per-slot deterministic problems with fewer variables.

## Method

- Two reduced-complexity methods for the non-convex per-slot sub-problem:
  - **Two-stage:** sequentially solve user resource allocation, then UAV movement ([[two-stage-decomposition]]).
  - **Joint:** solve resource allocation and UAV movement together.
- Both satisfy the average UAV-energy and queue-stability constraints and trade off user energy vs. queue-backlog length (the O(1/V), O(V) Lyapunov trade-off).

## Key findings

- Both methods significantly outperform benchmarks (including a learning-based method) in reducing ground-user energy; the **joint method outperforms the two-stage method at the cost of higher computational complexity** (the paper's stated trade-off).

## Limitations / future work

The parse's conclusion does not enumerate explicit future work beyond the established framework.

## Relation to the corpus

A clean **Lyapunov-based online UAV-MEC** entry whose explicit two-stage-vs-joint comparison directly informs the wiki's [[two-stage-decomposition]] thread (cf. the discrete-then-continuous decompositions in [[wang-2026-aerial-marine-msar]], [[nabi-2025-jour-hierarchical-aerial]]). Shares the Lyapunov backbone with [[zhu-2025-lycnn-drl-wpt-mec]] and [[qin-2025-bcuav-masac]]; shares the UAV-EC offloading lineage with [[yu-2020-uav-ec-collaborative-offloading]]. Reinforces [[lyapunov-optimization]].

## Raw artifacts

- `raw/sources/Online_Trajectory_and_Resource_Optimization_for_Stochastic_UAV-Enabled_MEC_Systems/full.md`
- Original PDF and extracted figures in the same folder.
