---
type: source
title: "MADDPG-Based Joint Service Placement and Task Offloading in MEC Empowered Air-Ground Integrated Networks"
authors: ["Jianbo Du", "Ziwen Kong", "Aijing Sun", "Jiawen Kang", "Dusit Niyato", "Xiaoli Chu", "F. Richard Yu"]
year: 2023
url: "https://doi.org/10.1109/JIOT.2023.3326820"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
modeling_card: required
tags: [source, air-ground-integrated-network, service-placement, task-offloading, maddpg, multi-agent-drl, minlp]
related:
  - "[[air-ground-integrated-network]]"
  - "[[service-caching-mec]]"
  - "[[multi-agent-td3]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[task-offloading]]"
  - "[[zhao-2024-caching-service-placement-uav]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
created: 2026-05-29
updated: 2026-07-16
---

# MADDPG-Based Joint Service Placement and Task Offloading in MEC Empowered Air-Ground Integrated Networks

## Citation

Du, J., Kong, Z., Sun, A., Kang, J., Niyato, D., Chu, X., & Yu, F. R. (2023). *MADDPG-Based Joint Service Placement and Task Offloading in MEC Empowered Air-Ground Integrated Networks*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3326820.

## TL;DR

A comprehensive **air-ground integrated MEC** framework where UAV-carried edge servers serve IoT devices/UE. The goal is to minimize the long-term average weighted sum of task-completion delay and economic expenditure across all UEs, via service-instance pre-installation/removal, offloading decisions, access control, service-instance selection, and resource allocation. The MINLP is reformulated as an MDP and solved with **MADDPG**, with continuous outputs converted to discrete variables while preserving coupling constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A slotted air-ground integrated network contains IoT devices, user equipment, and multiple UAV-mounted MEC servers. UEs access UAVs over NOMA links, while each UAV has finite service-storage and computation capacity; the primary UAV performs centralized training and the UAVs execute their policies as distributed agents.

**Problem & objective**: The mixed-integer nonlinear program P1 jointly minimizes long-term average UE cost, $\min_{\boldsymbol{\Delta}(t),\boldsymbol{\rho}(t),\mathbf A(t),\mathbf P(t),\mathbf F(t)}\frac{1}{T_{\max}}\sum_{t=1}^{T_{\max}}\sum_i \mathrm{Cost}_i(t)$, where each cost combines task-completion delay and economic expenditure.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Service-instance adjustment | $\delta_{hj}(t)$ | integer | Number of instances of service $h$ installed on or removed from UAV $j$ |
| Task-offloading decision | $\rho_i(t)$ | binary, $\{0,1\}$ | Whether UE $i$ offloads its task |
| Access and instance selection | $a_{ij}(t),a_{ij}^{\mathrm{idle}}(t),a_{ij}^{\mathrm{new}}(t)$ | binary, $\{0,1\}$ | Selected UAV and whether an idle or newly installed instance serves UE $i$ |
| UE transmit power | $p_{ij}(t)$ | continuous, $0<p_{ij}(t)<p_i^{\max}$ | Uplink power used when UE $i$ accesses UAV $j$ |
| UAV computation allocation | $f_{ij}(t)$ | continuous, $0<f_{ij}(t)<f_j^{\max}$ | CPU resource assigned by UAV $j$ to UE $i$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C3 | Service-instance installation, removal, and inventory counts remain consistent across slots |
| C10 | UAV storage is bounded by $\sum_h n_{hj}(t)w_h\leq \Pi_j$ |
| C11-C12 | Each offloaded task selects one UAV and one feasible idle or newly installed service instance |
| C13-C14 | Transmit-power and computation allocations respect the UE and UAV capacity bounds |
| C15 | The resulting task-completion delay satisfies the UE delay requirement |

**Algorithm**: Reformulate P1 as an MDP whose UAV observations contain requests, resident instances, storage, and UE positions; let each MADDPG actor output placement, offloading, access, power, and computation controls; normalize continuous outputs and convert the coupled placement and selection components to feasible discrete decisions; train the actors with centralized critics, replay, target networks, and a reciprocal-cost reward with a penalty for infeasible actions; then execute the learned UAV policies distributively.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Du et al. [x] studied joint service placement and task offloading in a MEC-empowered air-ground integrated network with UAV-mounted edge servers. They formulated a mixed-integer nonlinear program that minimizes the long-term average weighted sum of task-completion delay and economic expenditure over service-instance adjustment, offloading, access, transmit-power, and computation-allocation decisions. They transformed the problem into a multi-agent MDP and used MADDPG with centralized training, distributed execution, and continuous-to-discrete action conversion that preserves coupled decisions. Simulation results reported fast convergence and lower system cost than the evaluated benchmark schemes.

## Problem framing

MEC-empowered AGINs deliver compute for applications like forest-fire monitoring and emergency rescue. The joint service-placement (which apps live on which UAV, under storage limits) + task-offloading problem has integer, binary, and continuous variables and is a tightly-coupled MINLP, hard for traditional optimization, and aims at long-term (not per-slot) cost.

## System model

- **Actors.** UAVs carrying edge servers + service instances; IoT devices and UE (collectively UEs).
- **Decisions.** Service-instance pre-installation/removal (storage-constrained), offloading decision, access control, service-instance selection, UE transmit power, UAV compute-resource assignment.
- **Objective.** Minimize long-term average weighted sum of completion delay + economic expenditure.

## Method

- Reformulate the MINLP as an MDP; solve with **MADDPG** ([[multi-agent-td3]] family / [[centralized-training-decentralized-execution]]).
- Normalize continuous variables and **convert MADDPG's continuous outputs into discrete variables** while preserving coupling constraints between variables.

## Key findings

- Simulations show fast convergence and superior cost minimization (weighted delay + expenditure) versus baselines (qualitative; specific reward curves in the paper).

## Limitations / future work

The conclusion does not enumerate explicit future work beyond the established framework.

## Relation to the corpus

A **service-placement + offloading** entry that complements the QoE-driven UAV caching/placement work [[zhao-2024-caching-service-placement-uav]] (matching+Gibbs) by instead using MADDPG, and joins the MADDPG/MATD3 multi-agent family ([[he-2023-fairness-3d-multiuav-maddpg]], [[zhao-2022-matd3-multiuav-ec-offloading]]). The continuous-to-discrete action conversion is a recurring hybrid-action workaround (cf. [[ma-2025-pdqn-vehicular-mec]]). Shares co-authors Jiawen Kang / Dusit Niyato with [[ye-2025-aigc-diffusion-contract]]. Reinforces [[air-ground-integrated-network]] and [[service-caching-mec]].

## Raw artifacts

- `raw/sources/MADDPG-Based_Joint_Service_Placement_and_Task_Offloading_in_MEC_Empowered_AirGround_Integrated_Networks/full.md`
- Original PDF and extracted figures in the same folder.
