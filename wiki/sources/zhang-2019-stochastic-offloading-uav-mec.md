---
type: source
title: "Stochastic Computation Offloading and Trajectory Scheduling for UAV-Assisted Mobile Edge Computing"
authors: ["Jiao Zhang", "Li Zhou", "Qi Tang", "Edith C.-H. Ngai", "Xiping Hu", "Haitao Zhao", "Jibo Wei"]
year: 2019
url: "https://doi.org/10.1109/JIOT.2018.2890133"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, stochastic-optimization, lyapunov-optimization, trajectory-scheduling, task-offloading, energy-latency-tradeoff]
related:
  - "[[mobile-edge-computing]]"
  - "[[lyapunov-optimization]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[yang-2022-stochastic-uav-mec-lyapunov]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
created: 2026-05-31
updated: 2026-07-16
modeling_card: required
---

# Stochastic Computation Offloading and Trajectory Scheduling for UAV-Assisted Mobile Edge Computing

## Citation

Zhang, J., Zhou, L., Tang, Q., Ngai, E. C.-H., Hu, X., Zhao, H., & Wei, J. (2019). *Stochastic Computation Offloading and Trajectory Scheduling for UAV-Assisted Mobile Edge Computing*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2018.2890133. (Manuscript received 22 Oct 2018; date of publication 28 Dec 2018; date of current version 8 May 2019.)

## TL;DR

A UAV-assisted MEC system with **stochastic computation tasks** (task streaming over a period, rather than fixed binary/partial tasks). The system minimizes the **average weighted energy consumption of the SMDs and the UAV**, subject to computation-offloading, resource-allocation, and UAV flying-trajectory-scheduling constraints. Because of non-convexity and time-coupling of variables, a **Lyapunov-based** approach analyzes the task queue and decomposes the energy-minimization into **three manageable subproblems**, solved iteratively by a combination of **ADMM + interior-point method + CVX**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One fixed-altitude UAV carrying an MEC server flies between prescribed endpoints and serves multiple smart mobile devices with stochastic task arrivals and local and edge queues. Devices offload over separate FDMA channels, and each air-to-ground channel follows free-space LoS path loss.

**Problem & objective**: Stochastic nonconvex problem (P) minimizes average weighted communication, computation, and flight energy, $\min_{\mathbf{X}(t)}T^{-1}\sum_{t=0}^{T-1}E_s(t)$, while maintaining stable local and UAV task queues.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Local CPU frequency | $f_{l,i}(t)$ | continuous, $[0,f_{i,\max}]$ | CPU-cycle frequency of device $i$ |
| UAV CPU allocation | $f_{c,i}(t)$ | continuous, nonnegative | MEC computation rate allocated to device $i$ |
| Offloaded task bits | $r_i(t)$ | continuous, nonnegative | Bits sent by device $i$ to the UAV in slot $t$ |
| UAV position | $\mathbf{p}_c(t)$ | continuous, planar position | UAV trajectory point used for channel and flight-energy control |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C2 | Local CPU frequency and offloaded bits obey device hardware and transmit-power bounds |
| C3 | Local execution plus offloading cannot exceed backlog, $f_{l,i}(t)\tau/\rho+r_i(t)\leq Q_i(t)$ |
| C4-C5 | Allocated MEC frequency does not exceed $F_c$, and executed edge tasks do not exceed $L_i(t)$ |
| C6 | UAV speed is bounded by $V_{\max}$ |
| C7-C8 | The online trajectory preserves previous positions and reaches the prescribed final point |
| C9 | Local and edge task queues remain stable |

**Algorithm**: Lyapunov drift-plus-penalty analysis removes long-term time coupling and yields one per-slot upper-bound problem; JSORT decomposes it into offloading and local-CPU control, UAV CPU allocation, and trajectory scheduling; ADMM, an interior-point method, and CVX solve the three blocks iteratively before queue states are updated.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied stochastic computation offloading, resource allocation, and trajectory scheduling in a UAV-assisted mobile edge computing system. They formulated a nonconvex stochastic problem that minimizes the average weighted energy consumption of smart mobile devices and the UAV under task-queue, computation, offloading, and mobility constraints. A Lyapunov-based approach transforms the long-term problem into a deterministic per-slot drift-plus-penalty problem and decomposes it into three subproblems. Their JSORT algorithm combines ADMM, an interior-point method, and a CVX-based trajectory update to solve the subproblems iteratively. Simulations report lower average weighted energy consumption than the MAES benchmark and more processed queue backlog than the MAEU benchmark, while illustrating the energy and queue-stability tradeoff controlled by $V$ and the weight factors.

## Problem framing

Smart mobile devices (SMDs) have limited compute and battery. UAV-assisted MEC offers coverage + extra computation where infrastructure is absent (disaster response, emergency relief, rural areas), with reliable LoS links and controllable mobility. The authors note that prior UAV-MEC works assume **binary or partial (deterministic) tasks**, leaving **stochastic** task streaming under-explored — and prior stochastic-task MEC work sits in ground cellular scenarios without MEC-server mobility management. This paper jointly addresses stochastic offloading, resource allocation, and UAV trajectory scheduling.

## System model

- **Actors.** A single UAV-mounted MEC server serving multiple SMDs with stochastically arriving computation tasks.
- **Objective.** Minimize the average weighted system (SMDs + UAV) energy consumption.
- **Queues.** Task queues per SMD; a **Lyapunov** drift analysis handles queue stability and decouples the long-term problem into per-slot subproblems ([[lyapunov-optimization]]).
- **Trade-off knobs.** The control parameter `V` and the weight factor `w_c` set the compromise between queue stability and system utility / energy.

## Method

- **Lyapunov-based decomposition** of the energy-minimization into three subproblems (offloading, resource allocation, trajectory scheduling).
- Iterative solver combining **ADMM**, the **interior-point method**, and the **CVX** convex solver.

## Key findings

- The energy-minimization scheme saves more energy than the **MAES** benchmark and processes more task-queue backlogs than the **MAEU** benchmark, across varied system parameters (the paper's named benchmarks; specific curves in the paper).
- Both `V` and the weight factors govern the **queue-stability vs system-utility compromise**: small `V` makes the system maximize task-execution rate; small `w_c` likewise favours execution rate and reduces queue backlogs (read from the parse's Fig. 8 discussion, reported qualitatively).

## Limitations / future work

The authors flag extending the work to **ad hoc networks with multiple UAVs**, and exploring **dynamic access control** and **interference management**.

## Relation to the corpus

An early **Lyapunov-based stochastic UAV-MEC** entry. It is distinct from the similarly-themed but later [[yang-2022-stochastic-uav-mec-lyapunov]] (Yang et al. 2022, IEEE TWC) — different authors, venue, year, and objective framing (Yang minimizes user energy with a two-stage-vs-joint comparison; this paper minimizes joint SMD+UAV energy via ADMM/interior-point/CVX). Sits alongside the other early optimization-based single-UAV MEC works [[zhang-2019-uav-iot-comp-comm]] and the WPT-MEC anchor [[zhou-2018-uav-wireless-powered-mec]]. Reinforces [[lyapunov-optimization]] and [[energy-latency-tradeoff]].

## Raw artifacts

- `raw/sources/Stochastic_Computation_Offloading_and_Trajectory_Scheduling_for_UAV-Assisted_Mobile_Edge_Computing/full.md`
- Original PDF and extracted figures in the same folder.
