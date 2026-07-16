---
type: source
title: "Energy-Efficient UAV-Assisted Mobile Edge Computing: Resource Allocation and Trajectory Optimization"
authors: ["Mushu Li", "Nan Cheng", "Jie Gao", "Yinlu Wang", "Lian Zhao", "Xuemin Shen"]
year: 2020
url: "https://doi.org/10.1109/TVT.2020.2968343"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
modeling_card: required
tags: [source, uav-mec, energy-efficiency, trajectory-optimization, resource-allocation, admm, dinkelbach, successive-convex-approximation]
related:
  - "[[uav-trajectory-control]]"
  - "[[alternating-direction-method-of-multipliers]]"
  - "[[task-offloading]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[nan-cheng]]"
  - "[[xuemin-shen]]"
created: 2026-06-04
updated: 2026-07-16
---

# Energy-Efficient UAV-Assisted Mobile Edge Computing: Resource Allocation and Trajectory Optimization

## Citation

Li, M., Cheng, N., Gao, J., Wang, Y., Zhao, L., & Shen, X. (2020). *Energy-Efficient UAV-Assisted Mobile Edge Computing: Resource Allocation and Trajectory Optimization*. **IEEE Transactions on Vehicular Technology**, 69(3). DOI: 10.1109/TVT.2020.2968343. (Received 14 August 2019; accepted 14 January 2020; published 21 January 2020; current version 12 March 2020.)

## TL;DR

Considers a **UAV-mounted cloudlet** serving IoT nodes in remote/unattended areas. Maximizes UAV **energy efficiency** (total offloaded compute data / UAV energy consumption) by jointly optimizing UAV trajectory, user transmit power, and computation load allocation. The non-convex fractional programming problem is solved via **Dinkelbach algorithm + SCA**, decomposed for scalable distributed solving via **ADMM**. A spatial distribution estimation technique (Gaussian kernel density estimation) is applied when exact user locations are unknown.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-wing UAV-mounted cloudlet flies over mobile IoT users during a finite computation cycle. Users partially offload divisible tasks through orthogonal or non-orthogonal uplinks, and the UAV buffers and executes received bits with dynamic CPU frequency while propulsion dominates its energy budget.

**Problem & objective**: The fractional program maximizes $\eta=\frac{\sum_{i,k}R_{i,k}(\boldsymbol\delta_k,\mathbf Q_k)}{\sum_{i,k}E_{i,k}^{C,U}(\mathbf W_k)+\sum_kE_k^F(\mathbf Q)}$, the ratio of total offloaded bits to UAV computing plus propulsion energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User power fraction | $\delta_{i,k}$ | continuous, $[0,1]$ | Fraction of user $i$'s maximum uplink power in slot $k$ |
| UAV workload allocation | $W_{i,k}$ | continuous, nonnegative | Bits from user $i$ processed by the UAV in slot $k$ |
| UAV trajectory | $\mathbf Q$ | continuous position sequence | Fixed-altitude horizontal path across the cycle |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each user offloads between its required minimum and total task size |
| C2 | The UAV processes only received bits and completes all offloaded bits by the cycle end |
| C3 | Per-slot cloudlet CPU frequency remains below $f_{\max}^U$ |
| C4 | Each user's communication and local-computing energy budgets are respected |
| C5 | UAV speed and acceleration remain below $v_{\max}$ and $a_{\max}$ |
| C6 | The UAV reaches the designated final position and velocity |

**Algorithm**: SCA forms inner convex approximations of channel-rate and propulsion terms, while Dinkelbach iterations solve the resulting fractional program. ADMM then separates user-side power and expected-trajectory updates from UAV-side trajectory and workload allocation, allowing users to solve in parallel; Gaussian kernel density estimation supplies proactive user locations when future mobility is unavailable.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] maximized computation bits per joule for a UAV-mounted cloudlet serving partially offloading IoT users. Their fractional program jointly selects user power fractions, UAV workload allocation, and trajectory under offloading, user-energy, cloudlet-CPU, speed, acceleration, and terminal-state constraints. The solution combines successive convex approximation, Dinkelbach updates, and an ADMM decomposition that lets users and the UAV keep local model information private. The optimized trajectory satisfied every tested minimum-offloading requirement where the circular benchmark could fail, and energy efficiency converged after about 30 SCA iterations in the three-user case.

## Problem framing

Traditional MEC infrastructure is too sparse for remote IoT deployments (forests, deserts, underwater monitoring). A UAV-mounted cloudlet provides on-demand MEC in these settings. Maximizing UAV energy efficiency — rather than just minimizing delay or energy — is the central objective, treating the ratio of compute-output to energy as a system-lifetime metric. Joint trajectory + computation-load + communication-resource optimization under this fractional objective was not previously studied for UAV-MEC at the time.

## System model

- **Single UAV-mounted cloudlet** flying over IoT nodes in area A; service period T seconds, K time slots.
- **Partial offloading:** each user offloads a fraction of their computation load to the UAV; the rest is processed locally.
- **Energy efficiency:** total computation bits processed by UAV / total UAV energy consumption (mechanical + compute); fractional objective.
- **Constraints:** user communication energy budget, UAV computation capability, UAV trajectory kinematics.
- **ADMM decomposition:** splits the problem across UAV and ground users; each entity updates its own variables without sharing raw data — privacy-preserving.
- **Gaussian KDE:** when user locations are ambiguous at cycle start, KDE estimates user spatial distribution from historical data to predict trajectory.

## Method

1. **Dinkelbach algorithm** converts the fractional energy-efficiency objective to a series of convex subtractive problems.
2. **SCA** handles residual non-convexity in the trajectory subproblem.
3. **ADMM** decomposes into UAV subproblem + per-user subproblems, solved cooperatively; convergence proof provided.
4. Gaussian KDE extension handles limited mobility knowledge.

## Key findings

- Proposed joint design achieves **superior energy efficiency** compared to benchmarks (fixed-trajectory + separate optimization; no-ADMM centralized) in numerical simulations (parse abstract + Section VII).
- Weighted-sum energy consumption decreases as task-completion time budget increases, revealing a **time–energy tradeoff** (parse Section VII result observation).
- ADMM decomposition scales to large user counts without centralized information aggregation.
- Gaussian KDE prediction maintains near-optimal energy efficiency even with limited user mobility knowledge (parse Section VI).

## Limitations / future work

Single UAV; LoS channel assumed throughout (not the probabilistic LoS/NLoS model). Parse does not give explicit numerical gains over benchmarks; only qualitative "significant improvement" noted in abstract.

## Relation to the corpus

Xuemin Shen ([[xuemin-shen]]) is a co-author. Uses [[alternating-direction-method-of-multipliers]] for distributed decomposition — shared with [[tang-2021-cecls-hybrid-cloud-edge]] and others. The UAV-mounted-cloudlet (aerial MEC server) model and energy-efficiency objective recur across the corpus; this paper provides an early formulation pairing Dinkelbach + SCA + ADMM for that setting. Closely related to [[zhan-2020-completion-time-energy-uav-mec]] which examines the energy vs completion-time Pareto front for a similar fixed-wing UAV-MEC scenario.

## Raw artifacts

- `raw/sources/Energy-Efficient_UAV-Assisted_Mobile_Edge_Computing_Resource_Allocation_and_Trajectory_Optimization/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
