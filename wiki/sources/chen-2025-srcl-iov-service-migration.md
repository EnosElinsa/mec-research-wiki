---
type: source
title: "Mobility-Aware Seamless Service Migration and Resource Allocation in Multi-Edge IoV Systems"
authors: ["Zheyi Chen", "Sijin Huang", "Geyong Min", "Zhaolong Ning", "Jie Li", "Yan Zhang"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3540407"
venue: "IEEE Transactions on Mobile Computing, 24(7)"
modeling_card: required
tags: [source, vehicular-mec, service-migration, resource-allocation, actor-critic, convex-optimization]
related:
  - "[[service-migration]]"
  - "[[vehicular-mec]]"
  - "[[advantage-actor-critic]]"
  - "[[zhaolong-ning]]"
created: 2026-08-27
updated: 2026-08-27
---

# Mobility-Aware Seamless Service Migration and Resource Allocation in Multi-Edge IoV Systems

## Citation

Chen, Z., Huang, S., Min, G., Ning, Z., Li, J., & Zhang, Y. (2025). *Mobility-Aware Seamless Service Migration and Resource Allocation in Multi-Edge IoV Systems*. **IEEE Transactions on Mobile Computing, 24**(7). DOI: 10.1109/TMC.2025.3540407.

## TL;DR

SR-CL separates long-term vehicle service migration from per-server computation allocation. A delayed-update actor and one-step critic learn migrations without future trajectories, while convex analysis gives the resource allocation used to minimize migration, communication, and computation delay.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Moving intelligent vehicles offload tasks to service instances on MEC servers colocated with base stations. Hosting can change across slots, and each target server divides finite computation among its associated vehicles.

**Problem & objective**: Minimize long-term total QoS delay, $\min \sum_t\sum_u G_{u,t}$, where $G_{u,t}$ contains migration, wireless and backhaul communication, and computation delay.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Migration destination | $x_{u,t}$ | discrete MEC index | Server hosting vehicle $u$ in slot $t$ |
| Compute allocation | $e_{u,t}$ | continuous, $[0,1]$ | Share of target server CPU assigned to vehicle $u$ |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Host | Each vehicle selects one available MEC server in each slot. |
| Allocation | $0\leq e_{u,t}\leq1$. |
| Server capacity | Shares assigned at one server satisfy $\sum_u e_{u,t}\leq1$. |
| Delay | $G_{u,t}$ includes state transfer, access, backhaul, and task execution induced by the decisions. |

**Algorithm**: Decompose the mixed-integer nonlinear problem into migration and allocation subproblems. Train an asynchronous actor-critic with a delayed actor and one-step critic for migrations, then derive the optimal CPU shares of each selected server through convex optimization and KKT conditions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chen et al. [x] jointly considered service migration and computation allocation for mobile vehicles using multiple MEC servers. They minimized long-term migration, access, backhaul, and computation delay over discrete host choices and continuous CPU shares. SR-CL decouples this mixed-integer nonlinear problem, uses a delayed-update actor with a one-step critic for migrations, and computes server allocation through convex optimization. Real vehicle trajectories and a Simu5G testbed show faster, more stable convergence and lower delay than the reported migration and DRL baselines across several configurations. The current objective omits energy cost, and the authors leave distributed scaling and broader mobility datasets for future work.

## Problem and system model

Vehicles generate tasks over slotted mobility traces. Moving a service incurs state-transfer and backhaul delay; keeping it remote adds communication delay; and concentrating services at one edge server increases execution delay under finite CPU.

## Method

The paper proves the joint problem NP-hard, separates server selection from computation allocation, learns long-horizon migration using an asynchronous actor-critic, and solves the allocation subproblem analytically for each migration profile.

## Key findings

- SR-CL converges faster and more stably than the compared IDQN and DDPG approaches.
- It maintains lower delay across tested compute capacities, migration coefficients, network topologies, backhaul bandwidths, and vehicle counts.
- Simu5G experiments support the simulation trends for seamless service delivery.

## Limitations / future work

Energy is not part of the objective. The authors propose distributed control, additional city trajectories, and a larger testbed for future evaluation.

## Relation to the corpus

This source links [[service-migration]] and [[vehicular-mec]] with learned long-term host selection and closed-form resource allocation. It complements prediction-assisted UAV migration in [[feng-2026-prediction-service-migration]].

## Raw artifacts

- Parse: `raw/sources/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems/Mobility-Aware_Seamless_Service_Migration_and_Resource_Allocation_in_Multi-Edge_IoV_Systems.md`
- Origin PDF and extracted figures are in the same folder.
