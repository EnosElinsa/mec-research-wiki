---
type: source
title: "DNN Task Partitioning and Migration Strategies in Multi-UAV-Assisted Mobile Edge Computing"
authors: ["Shuman Meng", "Bin Li", "Zhao Yi", "Lei Liu", "Zesong Fei"]
year: 2026
url: "https://doi.org/10.1109/JIOT.2026.3685675"
venue: "IEEE Internet of Things Journal, 13(13)"
modeling_card: required
tags: [source, dnn-partitioning, task-migration, multi-uav-mec, soft-actor-critic, prioritized-experience-replay, energy-minimization]
related:
  - "[[dnn-model-partition]]"
  - "[[task-migration]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[soft-actor-critic]]"
  - "[[prioritized-experience-replay]]"
  - "[[load-balancing-uav-mec]]"
created: 2026-11-02
updated: 2026-11-02
---

# DNN Task Partitioning and Migration Strategies in Multi-UAV-Assisted Mobile Edge Computing

## Citation

Meng, S., Li, B., Yi, Z., Liu, L., & Fei, Z. (2026). *DNN Task Partitioning and Migration Strategies in Multi-UAV-Assisted Mobile Edge Computing*. **IEEE Internet of Things Journal, 13**(13). DOI: 10.1109/JIOT.2026.3685675.

## TL;DR

Users split pretrained DNN inference between the device and UAV edge servers, and overloaded UAVs can migrate subtasks to other UAVs. The paper minimizes total weighted energy over user-UAV association, partition point, UAV trajectory, migration, and computing allocation, using SAC with prioritized experience replay and a convex-optimization subroutine for computing resources.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Users at fixed positions $\mathbf w_i$ each generate a DNN task $b_i$ whose model is preloaded on users and UAVs. UAVs fly at altitude $H_j(t)\in[H_{\min},H_{\max}]$ with kinematics $\mathbf q_j(t+1)=\mathbf q_j(t)+\mathbf v_j(t)\delta+\frac12\mathbf a_j(t)\delta^2$, keep a safe separation $d_{\mathrm{safe}}$, and have limited energy.

**Problem & objective**: P0, a MINLP: $\min_{\alpha,f,\mathbf q,\varphi,\beta}\sum_{t=1}^TE_{\mathrm{tot}}(t)$, the total weighted energy over all slots; reformulated as an MDP.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Association | $\alpha_{i,j}(t)$ | binary | User $i$ is associated with UAV $j$ |
| Partition point | $\varphi_i(t)$ | integer in $\{1,\dots,L_k+1\}$ | Layer at which user $i$'s DNN is split |
| Migration | $\beta_{i,jj'}(t)$ | binary | User $i$'s subtask migrates from UAV $j$ to UAV $j'$ |
| Computing | $f_{i,j}(t)$ | $[0,f_j^{\max}]$ | CPU frequency UAV $j$ gives user $i$ |
| Trajectory | $\mathbf q_j(t)$ | 3-D, via $\mathbf v_j$ and $\mathbf a_j$ | UAV position |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (1), (2a)-(2b) | Kinematics, $\lVert\mathbf q_j-\mathbf q_{j'}\rVert^2\ge d_{\mathrm{safe}}^2$, $\lVert\mathbf v_j\rVert\le v_{\max}$, $\lVert\mathbf a_j\rVert\le a_{\max}$. |
| (11), (23d) | Binary user-UAV association. |
| (16), (23e) | Binary migration decisions. |
| (23c) | Integer partition point. |
| (23f)-(23g) | Computing limits, $0\le f_{i,j}\le f_j^{\max}$ and $\sum_i\gamma_{i,j}f_{i,j}\le f_j^{\max}$ for tasks hosted after migration. |
| (23h) | Delay, $T_i(t)\le\delta$. |

**Algorithm**: SAC-PER learns association, partitioning, trajectory, and migration; a convex-optimization subroutine allocates computing resources inside each step to improve learning efficiency.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Meng et al. [x] proposed a multi-UAV-assisted mobile edge computing architecture for deep neural network inference tasks, in which DNN models are hierarchically partitioned and subtasks are distributed between local devices and aerial servers. Considering unbalanced network load and limited UAV energy, they introduced a task migration mechanism for resource coordination and load balancing among UAVs. The goal is to minimize total weighted energy consumption by jointly optimizing user-UAV association, DNN partitioning, UAV trajectory, task migration, and computing resource allocation. The problem is modeled as a Markov decision process and solved by a soft actor-critic algorithm with prioritized experience replay that integrates convex optimization as a subroutine for computing resource allocation. Simulation results show faster convergence and up to 14.6% lower total weighted energy consumption than baseline methods.

## Problem framing

Partitioning alone can overload some UAVs while others sit idle. Migration between UAVs balances load, but adds transfer energy and couples UAV decisions.

## System model

- Pretrained DNNs are preloaded on all devices and UAVs, so no model deployment is required.
- UAV motion includes acceleration.

## Method

SAC-PER with an embedded convex computing-allocation step.

## Key findings

- The method converges faster than baselines.
- Total weighted energy falls by up to 14.6% relative to baselines.

## Limitations / future work

Not stated beyond the simulated scenarios.

## Relation to the corpus

Combines [[dnn-model-partition]] with UAV-to-UAV [[task-migration]] in [[multi-uav-assisted-mec]], related to [[load-balancing-uav-mec]].

## Raw artifacts

- Parse: `raw/sources/DNN_Task_Partitioning_and_Migration_Strategies_in_Multi-UAV-Assisted_Mobile_Edge_Computing/DNN_Task_Partitioning_and_Migration_Strategies_in_Multi-UAV-Assisted_Mobile_Edge_Computing.md`
- Origin PDF and extracted figures are in the same folder.
