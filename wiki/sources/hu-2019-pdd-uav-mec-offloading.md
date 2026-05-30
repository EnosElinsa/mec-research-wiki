---
type: source
title: "Joint Offloading and Trajectory Design for UAV-Enabled Mobile Edge Computing Systems"
authors: ["Qiyu Hu", "Yunlong Cai", "Guanding Yu", "Zhijin Qin", "Minjian Zhao", "Geoffrey Ye Li"]
year: 2019
url: "https://doi.org/10.1109/JIOT.2018.2878876"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, uav-mec, computation-offloading, trajectory-design, user-scheduling, penalty-dual-decomposition, binary-vs-partial-offloading]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[penalty-dual-decomposition]]"
  - "[[yu-2020-uav-ec-collaborative-offloading]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[wu-2018-multiuav-minrate-trajectory]]"
created: 2026-05-31
updated: 2026-05-31
---

# Joint Offloading and Trajectory Design for UAV-Enabled Mobile Edge Computing Systems

## Citation

Hu, Q., Cai, Y., Yu, G., Qin, Z., Zhao, M., & Li, G. Y. (2019). *Joint Offloading and Trajectory Design for UAV-Enabled Mobile Edge Computing Systems*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2018.2878876. (Date of publication 31 Oct 2018; date of current version 8 May 2019.)

## TL;DR

A single-UAV MEC system where a moving UAV-carried cloudlet serves K ground users in an **orthogonal multiple access** manner. Each user **partially offloads** part of its task to the UAV and computes the rest locally. The paper minimizes the **sum over time slots of the maximum delay among users** by jointly optimizing the UAV trajectory, the per-user offloading ratio, and the binary user-scheduling variables, subject to discrete binary, energy-consumption, and trajectory constraints. The non-convex mixed-integer problem is recast with auxiliary/equality constraints and solved by a **penalty dual decomposition (PDD)** algorithm, plus a lower-complexity **simplified l0-norm** variant; an **average-delay** extension is also given.

## Problem framing

Conventional MEC fails where base stations are sparse or users surge in number. A mobile UAV with computing resources improves offloading link quality via high-altitude LoS, but the joint trajectory + offloading-ratio + user-scheduling problem is highly non-convex with discrete binary scheduling variables and tightly coupled constraints. UAV-enabled MEC was, at the time, under-investigated.

## System model

- **Actors.** One UAV-mounted cloudlet serving K ground users; the UAV flies above the users and provides compute over consecutive time slots via OMA.
- **Offloading.** Each user splits its task: a portion offloaded to the UAV, the remainder computed locally ([[binary-vs-partial-offloading]] — partial/splitting).
- **Objective.** Minimize the sum of the per-slot maximum delay among all users (a min-max delay objective), subject to binary user-scheduling constraints, energy constraints, and UAV trajectory constraints.

## Method

- Introduce **auxiliary variables + equality constraints** to convert the discrete binary constraints and the non-convex coupling into a tractable form.
- Apply the **[[penalty-dual-decomposition|PDD]]** framework: dualize and penalize the equality constraints as augmented-Lagrangian terms, then solve with a two-layer iteration — inner loop uses **CCCP** (concave-convex procedure) to update variables; outer loop updates AL multipliers and the penalty factor.
- A **simplified l0-norm** algorithm reduces complexity; the approach is also extended to a different objective minimizing the **average delay**.

## Key findings

- Simulations show the proposed PDD-based algorithm **significantly outperforms the benchmarks**, and that a moving UAV effectively improves users' computation performance (the paper's stated headline). Delay performance and convergence rate of the PDD algorithm are verified.

## Limitations / future work

Single UAV; the parse's conclusion focuses on validation rather than enumerating future directions.

## Relation to the corpus

An early (2018/2019) **single-UAV MEC offloading + trajectory** entry that predates and complements the SCA-based collaborative scheme of [[yu-2020-uav-ec-collaborative-offloading]] and the Lagrangian-dual+SCA single-UAV design of [[zhang-2019-uav-iot-comp-comm]]. Its **min-max delay** objective and **PDD** solver distinguish it from the energy-min and weighted-sum families; PDD is a new optimization vocabulary in this wiki. The author set (Cai/Yu/Qin/Zhao/G. Y. Li, Zhejiang University / QMUL / Georgia Tech) is distinct from the UAV-communication track's Wu/Zeng/Zhang group, whose multi-UAV min-rate paper [[wu-2018-multiuav-minrate-trajectory]] is curated in this same batch. Anchors the new [[penalty-dual-decomposition]] concept.

## Raw artifacts

- `raw/sources/Joint_Offloading_and_Trajectory_Design_for_UAV-Enabled_Mobile_Edge_Computing_Systems/full.md`
- Original PDF and extracted figures in the same folder.
