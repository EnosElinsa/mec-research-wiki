---
type: source
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
updated: 2026-06-03
---

# Air–Ground Coordinated MEC: Joint Task, Time Allocation and Trajectory Design

## Citation
Liuneng Wang, Yanjun Li, Yuzhe Chen, Tingting Li, Zheng Yin, "Air–Ground Coordinated MEC: Joint Task, Time Allocation and Trajectory Design," *IEEE Transactions on Vehicular Technology*, 2025. DOI: 10.1109/TVT.2024.3486036. (Received 14 May 2024; accepted 17 Oct 2024; date of publication 24 Oct 2024; date of current version 5 Mar 2025 → year 2025 per the date-of-current-version convention. Corresponding author: Yanjun Li. Zhejiang University of Technology + Houston Methodist Academic Institute / Weill Cornell Medicine.)

## TL;DR
An air-ground coordinated MEC system pairs a **laser-powered rotary-wing UAV** with a grid-powered ground access point (AP): the AP both charges the UAV via a laser beam and serves as a high-performance compute server, while the UAV acts simultaneously as an MEC server (computing UE tasks itself) and as a relay (forwarding UE tasks to the AP). The goal is to minimize the UAV's **long-term average energy consumption** by jointly optimizing trajectory, the UAV-vs-AP task-allocation ratio, and the energy-harvesting time. The non-convex problem is decomposed into an LP subproblem (task + EH-time allocation, solved with PuLP) and a trajectory subproblem (solved with [[ddpg|DDPG]]), and the resulting **LP-DDPG** algorithm reports the lowest UAV energy consumption against benchmarks while converging reliably.

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
