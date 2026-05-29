---
type: source
title: "Joint Computation and Communication Design for UAV-Assisted Mobile Edge Computing in IoT"
authors: ["Tiankui Zhang", "Yu Xu", "Jonathan Loo", "Dingcheng Yang", "Lin Xiao"]
year: 2019
url: "https://doi.org/10.1109/TII.2019.2948406"
venue: "IEEE Transactions on Industrial Informatics (IEEE TII)"
tags: [source, uav-mec, computation-offloading, trajectory-optimization, energy-minimization, sca, iot]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
  - "[[liu-2022-miso-uav-mec-trajectory]]"
created: 2026-05-29
updated: 2026-05-29
---

# Joint Computation and Communication Design for UAV-Assisted Mobile Edge Computing in IoT

## Citation

Zhang, T., Xu, Y., Loo, J., Yang, D., & Xiao, L. (2019). *Joint Computation and Communication Design for UAV-Assisted Mobile Edge Computing in IoT*. **IEEE Transactions on Industrial Informatics**. DOI: 10.1109/TII.2019.2948406.

## TL;DR

A single-UAV-with-MEC-server system serving IoT terminal devices (TDs) over a finite period. Each TD has three options per slot: compute locally, partially offload to the UAV, or offload to an access point **via UAV relaying**. The paper minimizes total energy (communication + computation + UAV flight) by jointly optimizing bit allocation, time-slot scheduling, power allocation, and UAV trajectory, solving the non-convex problem in two parts via **Lagrangian duality** and **successive convex approximation (SCA)**.

## Problem framing

Latency-critical IoT tasks exceed TD compute/battery budgets. A UAV-mounted MEC server (and the UAV as relay to an AP) extends compute coverage, but the joint bit/time/power/trajectory design is non-convex.

## System model

- **Actors.** One UAV (MEC server + relay), multiple IoT TDs, an access point.
- **Per-TD options.** Local compute; partial offload to UAV; offload to AP via UAV relay ([[binary-vs-partial-offloading]] — partial).
- **Objective.** Minimize sum of communication-related, computation-related, and UAV flight energy.

## Method

- Decompose into two sub-problems solved by **Lagrangian duality** and **SCA**, combined into an iterative algorithm guaranteed to converge within a dozen iterations ([[alternating-optimization-sdr-sca]]).

## Key findings

- Numerical results validate the algorithm and show its superiority over benchmark designs (qualitative; specific energy curves in the paper).

## Limitations / future work

Single-UAV; the parse does not enumerate explicit future work beyond the established design.

## Relation to the corpus

An early, **optimization-based single-UAV MEC** entry that anchors the classic "joint trajectory + offloading + resource" formulation later revisited with collaboration ([[yu-2020-uav-ec-collaborative-offloading]]), MISO beamforming ([[liu-2022-miso-uav-mec-trajectory]]), and DRL ([[zhang-2024-uav-task-offloading-ddpg]]). Reinforces [[alternating-optimization-sdr-sca]] and [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/Joint_Computation_and_Communication_Design_for_UAV-Assisted_Mobile_Edge_Computing_in_IoT/full.md`
- Original PDF and extracted figures in the same folder.
