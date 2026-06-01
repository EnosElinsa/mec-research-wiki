---
type: source
title: "Completion Time and Energy Optimization in the UAV-Enabled Mobile-Edge Computing System"
authors: ["Cheng Zhan", "Han Hu", "Xiufeng Sui", "Zhi Liu", "Dusit Niyato"]
year: 2020
url: "https://doi.org/10.1109/JIOT.2020.2993260"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-trajectory-control, computation-offloading, energy-latency-tradeoff, fixed-wing-propulsion-energy-model, alternating-optimization-sdr-sca, information-causality-constraint]
related:
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[information-causality-constraint]]"
  - "[[energy-latency-tradeoff]]"
  - "[[jeong-2018-uav-cloudlet-bit-allocation]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[hu-2019-pdd-uav-mec-offloading]]"
  - "[[zeng-2017-energy-efficient-uav-trajectory]]"
  - "[[dusit-niyato]]"
created: 2026-06-02
updated: 2026-06-02
---

# Completion Time and Energy Optimization in the UAV-Enabled Mobile-Edge Computing System

## Citation

Zhan, C., Hu, H., Sui, X., Liu, Z., & Niyato, D. (2020). *Completion Time and Energy Optimization in the UAV-Enabled Mobile-Edge Computing System*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2020.2993260. (Manuscript received 5 December 2019; revised 11 March / 15 April 2020; accepted 29 April 2020; date of publication 8 May 2020; date of current version 12 August 2020 → year 2020.)

## TL;DR

A **classical/convex** treatment of a single **fixed-wing** UAV acting as a flying MEC server for ground IoT devices, jointly designing **computation offloading + resource allocation + UAV trajectory + completion time** to minimize, separately, the UAV's **energy consumption** and its **completion time**. The two objectives are shown to be genuinely different (energy minimization wants low-power flying speeds; completion-time minimization wants maximum speed), and the paper characterizes the **Pareto-optimal tradeoff** between them. Both nonconvex problems are made tractable by the **path-discretization** technique and solved with an **alternating-optimization** algorithm whose two blocks are each handled by **successive convex approximation (SCA)**, converging to KKT solutions.

## Problem framing

Static edge servers have limited coverage and are costly to densely deploy, so a flying UAV-MEC server brings computation to remote/low-power IoT devices with favorable LoS links. For a UAV the **propulsion energy** dominates and depends on flight speed/acceleration, so it cannot be ignored as in terrestrial nodes. Prior UAV-MEC work mostly maximized computation/energy efficiency under a **predetermined** completion time, overlooking that completion time is itself a fundamental design variable for time-sensitive applications. There is a tension: faster flight cuts completion time but changes propulsion power, so the energy-minimizing and time-minimizing designs differ. The paper is, by its own statement, among the first to jointly tackle UAV completion-time and energy minimization for a UAV-enabled MEC system.

## System model

- **Topology.** K ground IoT devices at fixed, a-priori-known horizontal locations; one fixed-wing UAV (computing-capable edge server) flying at fixed altitude H between predetermined initial/final positions $\mathbf{q}_I, \mathbf{q}_F$; no other ground MEC servers (or they use different bands). The design extends to multiple UAVs each serving a device subset.
- **Computation.** Tasks are bitwise-independent and arbitrarily partitionable, so each device's $I_k$ input bits split between **local computing** and **partial offloading** to the UAV; both device and UAV use **dynamic voltage and frequency scaling (DVFS)** with per-node max CPU frequency.
- **Communication.** LoS channel with power gain $\beta_0 d_k^{-\alpha}$; **TDMA** offloading (one device offloads at a time, $\sum_k x_k(t)\le 1$); fixed per-device transmit power; result-download time neglected (output bits small). **Information-causality** constraints require offloaded bits to be received before the UAV can compute them.
- **UAV dynamics.** Trajectory $\mathbf{q}(t)$ with velocity/acceleration bounded by $V_{\min}\le\|\dot{\mathbf{q}}\|\le V_{\max}$, $\|\ddot{\mathbf{q}}\|\le a_{\max}$ (fixed-wing minimum-speed-to-stay-aloft); the **fixed-wing propulsion-energy model** (speed + acceleration) is adopted.
- **Objectives.** Two separate problems — minimize UAV energy (no preset completion time) and minimize completion time (under device energy budgets) — followed by the Pareto frontier balancing the two.

## Method

- **Path discretization.** The continuous trajectory is discretized along the path to convert each nonconvex continuous-time problem into a discretized, more tractable equivalent.
- **Alternating optimization + SCA.** Variables are decoupled into two blocks — (i) computation offloading + resource allocation, (ii) UAV trajectory + completion time — and alternately optimized; each block's nonconvex subproblem is handled by SCA, iterating to convergence (analyzed) at a KKT point.
- **Completion-time problem.** Reformulated with the same path-discretization model and solved by a structurally similar AO algorithm.
- **Pareto tradeoff.** A weighted formulation traces the Pareto-optimal solutions balancing UAV energy vs completion time.

## Key findings

- The proposed designs **outperform baseline schemes** on both UAV energy and completion time, and achieve performance **close to a lower bound** (the paper's stated simulation results; specific margins are figure-derived, so treat exact values as indicative).
- There is a clear **tradeoff between completion time and energy consumption** of the UAV: minimizing energy favors flying at less power-consuming speeds while minimizing completion time favors maximum speed, so the two optimal solutions differ in general.

## Limitations / future work

Single-UAV, single-processor, fixed-altitude, LoS-only TDMA model; downlink of results ignored; device locations assumed known. The authors explicitly defer collaboration with ground-based MEC servers and multiple multi-processor UAVs in urban areas to future work. Simulation-only.

## Relation to the corpus

A **classical/convex UAV-MEC** entry in the AO + SCA tradition (see [[alternating-optimization-sdr-sca]]) that pairs the **fixed-wing propulsion-energy model** of [[zeng-2017-energy-efficient-uav-trajectory]] with partial computation offloading. It sits close to the early UAV-cloudlet **bit-allocation + trajectory** work [[jeong-2018-uav-cloudlet-bit-allocation]] and the joint computation-communication design of [[zhang-2019-uav-iot-comp-comm]], and shares the **information-causality** constraint and min-delay framing with [[hu-2019-pdd-uav-mec-offloading]]. Its explicit energy-vs-completion-time Pareto study contributes to the corpus's [[energy-latency-tradeoff]] thread. Co-authored by [[dusit-niyato]].

## Raw artifacts

- `raw/sources/Completion_Time_and_Energy_Optimization_in_the_UAV-Enabled_Mobile-Edge_Computing_System/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
