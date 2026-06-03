---
type: source
title: "Computation Offloading and Resource Allocation in LEO Satellite-Terrestrial Integrated Networks With System State Delay"
authors: ["Bo Xie", "Haixia Cui", "Ivan Wang-Hei Ho", "Yejun He", "Mohsen Guizani"]
year: 2025
url: "https://doi.org/10.1109/TMC.2024.3479243"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags:
  - source
  - satellite-terrestrial-integrated-network
  - leo-satellite-edge-computing
  - computation-offloading
  - deep-reinforcement-learning
  - double-dqn
  - state-delay
  - resource-allocation
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[deep-q-network]]"
  - "[[van-hasselt-2016-double-dqn]]"
  - "[[three-tier-cloud-edge-end]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
  - "[[zhou-2024-mco-satellite-edge-offloading]]"
  - "[[liu-2023-sagecn-online-offloading]]"
  - "[[wang-2024-satellite-terrestrial-computing]]"
created: 2026-06-03
updated: 2026-06-03
---

# Computation Offloading and Resource Allocation in LEO Satellite-Terrestrial Integrated Networks With System State Delay

## Citation
Bo Xie, Haixia Cui, Ivan Wang-Hei Ho, Yejun He, Mohsen Guizani, "Computation Offloading and Resource Allocation in LEO Satellite-Terrestrial Integrated Networks With System State Delay," *IEEE Transactions on Mobile Computing*, 2025. DOI: 10.1109/TMC.2024.3479243. (Received 18 Jun 2024; accepted 9 Oct 2024; date of publication 14 Oct 2024; date of current version 5 Feb 2025 → year 2025 per the date-of-current-version convention. Corresponding author: Haixia Cui. South China Normal University + Hong Kong Polytechnic University + Shenzhen University + MBZUAI.)

## TL;DR
For a LEO satellite-terrestrial integrated network (STIN) where users can offload tasks locally, to a terrestrial base station (BS), to a LEO satellite edge server, or to a cloud data center (CDC), this paper minimizes energy consumption under latency constraints while explicitly modeling **system state delays** — the fact that a DRL agent observes outdated states and acts with delay. It formulates offloading as a **stochastic delay MDP (SDMDP)**, reduces it to an equivalent standard MDP, and solves it with a **double deep Q-network (DDQN)** using an **augmented state space** that carries the delayed observations/actions. A separate **multi-level feedback queue (RAMLFQ)** handles per-server CPU resource allocation. The paper states it is the first to study STIN computation offloading with system state delays.

## Problem framing
STINs turn LEO satellites into new edge servers extending compute to remote regions and oceans, but the edge environment is distributed and dynamic and AI workloads are heavy for resource-constrained devices. DRL is increasingly used for STIN offloading, yet existing studies assume states and feedback are obtained **instantaneously**. In practice, network latency, computational bottlenecks, and task-execution time introduce delays in observation and decision execution, forcing the agent to decide on stale information. The paper targets this gap: realistic offloading under inevitable system state/action delays.

## System model
- **Topology (Fig. 1, LEO-STIN):** M LEO satellites, N terrestrial BSs, K mobile users, and a cloud data center; fixed time slots over a finite horizon.
- **Offloading decision** `X(t,k) ∈ {0, N, N+1, N+2}` — process locally, offload to BS, to LEO satellite (LEOS), or to CDC. Inter-satellite link transfer is treated as fast/negligible-delay, so the nearest satellite by position is chosen.
- **Communication:** terrestrial links use the **C-band** (LoS path-loss channel) and BS↔CDC ethernet; user↔LEOS and LEOS↔CDC use **Ka-band** wireless backhaul (path-loss channel with log-normal shadow fading).
- **Computing models:** local, BS-server, CDC (assumed effectively infinite CPU), and LEOS-edge, each with its own latency (transmission + execution) and energy (execution + transmission) expressions; a partial-offloading split is used and total energy weights execution vs transmission by a factor φ ∈ (0,1).
- **Optimization P0:** minimize total energy over the offloading vector X, BS/LEOS compute-allocation matrices, and bandwidth allocation, subject to per-server compute/bandwidth caps and latency constraints. P0 is a **mixed-integer nonlinear program (MINLP)** and NP-hard (discrete X plus continuous resource matrices).

## Method
- **SDMDP → MDP:** the offloading policy is modeled as a stochastic delay MDP `⟨S, A, P_A, R, O, AC, C, γ⟩` (with observation delay O and action delay AC), then transformed into a standard MDP whose **augmented state** `I_O = S × A^{O+AC}` carries the in-flight delayed actions, so a delay-free solver applies.
- **DDQN offloading agent:** a [[van-hasselt-2016-double-dqn|double DQN]] with online and target networks and an **augmented experience pool** storing delay-structured transitions `(s_{t-O}, …, a_t, done)`; double-Q decoupling curbs value overestimation.
- **RAMLFQ resource allocation:** a multi-level feedback queue deployed on each BS/LEOS server that dynamically adjusts per-task CPU using task priority and priority-queue weights, with a time-slice round-robin scheduling strategy, to improve real-time CPU efficiency.

## Key findings
Grounded in the abstract and contributions (specific magnitudes are figure/table-derived, treated as indicative):
- The learning-based offloading algorithm attains **lower total cost** and higher performance efficiency than the compared existing offloading methods.
- Explicitly handling system state delay via the augmented-state DDQN is presented as enabling effective decisions despite stale observations — the paper's central, first-of-its-kind claim for STINs.
- RAMLFQ is reported to enhance the CPU's task-scheduling efficiency relative to non-priority-aware allocation.

## Limitations / future work
- Results are simulation-based; no on-orbit or hardware validation.
- Inter-satellite link delay is assumed negligible, simplifying the multi-hop satellite case.
- CDC compute is assumed effectively infinite, which understates cloud-side contention.
- The augmented-state representation grows with the delay length, which can stress the value network for large delays (a scalability caveat the delay formulation implies).

## Relation to the corpus
This is a satellite-terrestrial offloading entry alongside [[zhou-2024-mco-satellite-edge-offloading]] (mobility-aware, ADMM-distributed), [[liu-2023-sagecn-online-offloading]] (Lyapunov + delayed online learning), and [[wang-2024-satellite-terrestrial-computing]]; its distinguishing contribution is treating **learning-time state/action delay** as a first-class modeling object rather than assuming instantaneous feedback. Architecturally it is a [[three-tier-cloud-edge-end|cloud/edge/end]] design with [[leo-satellite-edge-computing|LEO edge]] servers, and its augmented-state [[van-hasselt-2016-double-dqn|DDQN]] adds a delay-aware data point to the corpus's [[drl-backbones-across-uav-mec-sources|DRL-backbone]] landscape. The MINLP-then-DRL split (DDQN for discrete offloading, RAMLFQ for resource allocation) mirrors the decomposition pattern recurring across the corpus.

## Raw artifacts
- Parse: `raw/sources/Computation_Offloading_and_Resource_Allocation_in_LEO_Satellite-Terrestrial_Integrated_Networks_With_System_State_Delay/full.md`
- Origin PDF: `raw/sources/Computation_Offloading_and_Resource_Allocation_in_LEO_Satellite-Terrestrial_Integrated_Networks_With_System_State_Delay/b2091f09-92a4-45bf-84c9-c40761291c80_origin.pdf`
- Figures: `raw/sources/Computation_Offloading_and_Resource_Allocation_in_LEO_Satellite-Terrestrial_Integrated_Networks_With_System_State_Delay/images/`
