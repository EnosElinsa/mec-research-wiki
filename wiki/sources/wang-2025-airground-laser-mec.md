---
type: source
modeling_card: required
title: "Air–Ground Coordinated MEC: Joint Task, Time Allocation and Trajectory Design"
authors: ["Liuneng Wang", "Yanjun Li", "Yuzhe Chen", "Tingting Li", "Zheng Yin"]
year: 2025
url: "https://doi.org/10.1109/TVT.2024.3486036"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags:
  - source
  - uav-mec
  - air-ground-integrated-network
  - wireless-power-transfer
  - laser-charging
  - trajectory-optimization
  - ddpg
  - two-stage-decomposition
related:
  - "[[air-ground-integrated-network]]"
  - "[[wireless-power-transfer]]"
  - "[[uav-trajectory-control]]"
  - "[[ddpg]]"
  - "[[two-stage-decomposition]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[uav-mobile-relaying]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[decomposition-beats-end-to-end-drl-in-mec]]"
created: 2026-06-03
updated: 2026-07-16
---

# Air–Ground Coordinated MEC: Joint Task, Time Allocation and Trajectory Design

## Citation
Liuneng Wang, Yanjun Li, Yuzhe Chen, Tingting Li, Zheng Yin, "Air–Ground Coordinated MEC: Joint Task, Time Allocation and Trajectory Design," *IEEE Transactions on Vehicular Technology*, 2025. DOI: 10.1109/TVT.2024.3486036. (Received 14 May 2024; accepted 17 Oct 2024; date of publication 24 Oct 2024; date of current version 5 Mar 2025 → year 2025 per the date-of-current-version convention. Corresponding author: Yanjun Li. Zhejiang University of Technology + Houston Methodist Academic Institute / Weill Cornell Medicine.)

## TL;DR
An air-ground coordinated MEC system pairs a **laser-powered rotary-wing UAV** with a grid-powered ground access point (AP): the AP both charges the UAV via a laser beam and serves as a high-performance compute server, while the UAV acts simultaneously as an MEC server (computing UE tasks itself) and as a relay (forwarding UE tasks to the AP). The goal is to minimize the UAV's **long-term average energy consumption** by jointly optimizing trajectory, the UAV-vs-AP task-allocation ratio, and the energy-harvesting time. The non-convex problem is decomposed into an LP subproblem (task + EH-time allocation, solved with PuLP) and a trajectory subproblem (solved with [[ddpg|DDPG]]), and the resulting **LP-DDPG** algorithm reports the lowest UAV energy consumption against benchmarks while converging reliably.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A laser-powered rotary-wing UAV and a grid-powered AP jointly serve UEs; the UAV computes some tasks locally, relays other tasks to the AP, and harvests energy from the AP within each slot.

**Problem & objective**: The long-term problem minimizes average UAV energy, $\min_{\mathbf U,\boldsymbol\beta,\mathbf Q}\lim_{T\to\infty}T^{-1}\sum_tE_u(t)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\omega(t)$ or $(X(t),Y(t))$ | continuous, region and speed bounded | UAV position and movement |
| UAV task fraction | $\beta_n^u(t)$ | continuous, $[0,1]$ | Fraction computed at the UAV |
| AP task fraction | $\beta_n^{AP}(t)$ | continuous, $[0,1]$ | Fraction relayed to and computed at the AP |
| Harvesting time ratio | $q(t)$ | continuous, $[0,1]$ | Slot share used for laser energy harvesting |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | UAV motion is bounded: $0\leq\theta(t)\leq2\pi$, $0\leq d(t)\leq d_{max}$, and the position stays in the service region. |
| C2 | Task fractions partition each UE task: $\beta_n^u(t)+\beta_n^{AP}(t)=1$. |
| C3 | Harvesting time is bounded: $0\leq q(t)\leq1$. |
| C4 | Every task meets its deadline: $T_n(t)\leq T_{max}$. |
| C5 | Harvested energy covers consumption: $E_u(t)\leq E_u^{EH}(t)$. |

**Algorithm**: Alternate a linear-programming allocation and harvesting-time step solved with PuLP with a DDPG trajectory step, holding the other block fixed to form the LP-DDPG procedure.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] study laser-powered air-ground MEC in which a UAV is both an edge server and a relay for a grid-powered AP. The long-term energy model jointly selects the UAV trajectory, UAV versus AP task fractions, and laser-harvesting time under movement, task partition, deadline, and energy-causality constraints. Their LP-DDPG decomposition solves allocation and harvesting with linear programming and updates the trajectory with DDPG. Simulations report reliable convergence and the lowest modeled UAV energy among the compared allocation and trajectory baselines.

## Problem framing
UEs in remote or emergency settings (maritime, mountainous, post-disaster) may be far from sparse, fixed ground base stations, suffering poor coverage; meanwhile UAVs make flexible airborne MEC servers but have limited compute and battery. An air-ground architecture lets the UAV switch between MEC-server and relay roles to extend service, and laser-charged WPT (which can deliver hundreds of watts through a narrow beam, with field-tested feasibility) co-locates the laser emitter with the ground server to sustain the UAV. Because harvested energy is **uncertain**, the system must use it efficiently. The paper notes that with the UAV's position fixed, the task-/time-allocation problem is strictly linear — the structural insight that motivates the decomposition.

## System model
- **Nodes:** one rotary-wing UAV with an MEC server + EH/communication circuits; a set of N single-antenna UEs that cannot compute locally; one grid-powered AP with a high-performance server and a laser transmitter.
- **Harvest-then-offload workflow per time slot:** (1) energy harvesting AP→UAV, (2) UE→UAV task transmission, (3) computation at the UAV, (4) UAV→AP task transmission (relay), (5) computation at the AP — all time-shared within a slot.
- **Time slots:** system time divided into T equal slots of length τ; the UAV's position is constant within a slot (trajectory discretized by slot), with a block-fading channel constant within a slot.
- **UAV movement:** 3-D Cartesian, constant altitude Z, per-slot horizontal flight angle θ(t) ∈ [0, 2π] and distance d(t) ∈ [0, d_max].
- **Tasks:** each UE n generates `L_n(t) = {D_n(t), C_n, T_max}` (data size, cycles-per-bit, max tolerated delay = slot length).
- **Objective:** minimize the UAV's long-term average energy consumption subject to UE task-completion-delay constraints.

## Method
A **two-step alternating optimization** decouples the coupled variables:
- **Subproblem 1 — computation-task and EH-time allocation:** with the UAV position fixed, this reduces to a **linear programming (LP)** problem, solved with the standard PuLP toolkit.
- **Subproblem 2 — real-time UAV trajectory scheduling:** a continuous-action, dynamic-environment control problem solved with **[[ddpg|deep deterministic policy gradient (DDPG)]]**.

Iterating the two subproblems yields the proposed **LP-DDPG** algorithm. A comparison table positions the work as the one design combining UAV-AP collaboration **and** WPT, with problem decomposition and a DRL trajectory solver, to minimize UAV energy.

## Key findings
Grounded in the abstract, contributions, and discussion (figure-derived numbers treated as indicative):
- **Convergence:** LP-DDPG's convergence is reported as guaranteed in the simulations.
- **Energy:** LP-DDPG exhibits the **lowest UAV energy consumption** among the benchmark algorithms across various scenarios.
- **Policy structure:** the paper identifies and discusses features of the optimal UAV-trajectory and task-allocation-ratio policies (e.g. how allocation shifts with channel/task conditions), offering design intuition rather than only a black-box policy.

## Limitations / future work
- The paper does not report a single headline percentage gain in the abstract; comparative energy advantages are shown across scenarios — treat them as relative, simulation-based results.
- Single-UAV, single-AP, single-antenna nodes; the related-work discussion notes multi-UAV / multi-antenna extensions exist elsewhere.
- Relies on laser-charging feasibility; harvested-energy uncertainty is modeled but real laser-link impairments (alignment, weather) are not a testbed result here.
- UEs are assumed unable to compute locally, simplifying the offloading decision.

## Relation to the corpus
This sits in the [[air-ground-integrated-network]] UAV-MEC line and is one of the corpus's [[wireless-power-transfer]] entries that powers the *UAV itself* (via laser), in contrast to [[zhou-2018-uav-wireless-powered-mec]] and [[zhu-2025-lycnn-drl-wpt-mec]] where the UAV/HAP wirelessly powers the *ground devices*. Its LP-then-DDPG structure is a clean instance of [[two-stage-decomposition]] — a convex/LP allocation stage feeding a learned trajectory stage — reinforcing [[decomposition-beats-end-to-end-drl-in-mec]] and adding a DDPG data point to [[drl-backbones-across-uav-mec-sources]]. The dual MEC-server/relay role connects it to [[uav-mobile-relaying]], and its full-offload model contrasts with the corpus's [[binary-vs-partial-offloading|partial-offloading]] designs.

## Raw artifacts
- Parse: `raw/sources/AirGround_Coordinated_MEC_Joint_Task_Time_Allocation_and_Trajectory_Design/full.md`
- Origin PDF: `raw/sources/AirGround_Coordinated_MEC_Joint_Task_Time_Allocation_and_Trajectory_Design/bb68f660-4524-4a34-927d-aab6cac62a85_origin.pdf`
- Figures: `raw/sources/AirGround_Coordinated_MEC_Joint_Task_Time_Allocation_and_Trajectory_Design/images/`
