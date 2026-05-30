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
updated: 2026-05-31
---

# Stochastic Computation Offloading and Trajectory Scheduling for UAV-Assisted Mobile Edge Computing

## Citation

Zhang, J., Zhou, L., Tang, Q., Ngai, E. C.-H., Hu, X., Zhao, H., & Wei, J. (2019). *Stochastic Computation Offloading and Trajectory Scheduling for UAV-Assisted Mobile Edge Computing*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2018.2890133. (Manuscript received 22 Oct 2018; date of publication 28 Dec 2018; date of current version 8 May 2019.)

## TL;DR

A UAV-assisted MEC system with **stochastic computation tasks** (task streaming over a period, rather than fixed binary/partial tasks). The system minimizes the **average weighted energy consumption of the SMDs and the UAV**, subject to computation-offloading, resource-allocation, and UAV flying-trajectory-scheduling constraints. Because of non-convexity and time-coupling of variables, a **Lyapunov-based** approach analyzes the task queue and decomposes the energy-minimization into **three manageable subproblems**, solved iteratively by a combination of **ADMM + interior-point method + CVX**.

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
