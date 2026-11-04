---
type: source
title: "Digital Twin-Based Task-Driven Resource Management in Intelligent UAV Swarms"
authors: ["Tianyang Li", "Supeng Leng", "Xiwen Liao", "Yan Zhang"]
year: 2025
url: "https://doi.org/10.1109/TITS.2025.3531120"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, digital-twin, uav-swarm, search-and-rescue, task-crowdsourcing, stochastic-network-calculus, multi-agent-drl, resource-management]
related:
  - "[[digital-twin]]"
  - "[[stochastic-network-calculus]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[communication-constrained-marl]]"
created: 2026-07-06
updated: 2026-11-03
modeling_card: required
---

# Digital Twin-Based Task-Driven Resource Management in Intelligent UAV Swarms

## Citation

Li, T., Leng, S., Liao, X., & Zhang, Y. (2025). *Digital Twin-Based Task-Driven Resource Management in Intelligent UAV Swarms*. **IEEE Transactions on Intelligent Transportation Systems**, 26(4), 5467-5480. DOI: 10.1109/TITS.2025.3531120.

## TL;DR

Builds a **digital-twin-based collaboration architecture** for UAV swarms in search-and-rescue scenarios. Task requirements drive swarm formation: a virtual traffic-flow scheduler uses stochastic network calculus to pre-assess end-to-end delay bounds, while a MADRL-based task-crowdsourcing policy adjusts which UAVs join the swarm. The goal is to satisfy sensing/service requirements without recruiting unnecessary UAVs or repeatedly reconfiguring physical routes.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A coordinator maintains a digital twin of each search-and-rescue UAV swarm and couples physical task crowdsourcing with virtual traffic-flow scheduling for sensing data.

**Problem & objective**: Integer program P (3) chooses virtual swarm membership and traffic-flow paths to minimize total membership change across crowdsourcing cycles, $\min_{\mathcal U_k^V(m),\delta_{i,j}^V(m)}\sum_{m\in T_k}\sum_{k\in\mathcal K}\lvert\mathcal U_k^V(m)-\mathcal U_k^V(m-1)\rvert$, so that fewer UAVs are committed and more stay idle for unexpected tasks while sensing and delay targets hold. The task requirement achievement ratio is an evaluation metric, not the formal objective.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Task membership request | $a_i$ | discrete in $\{0,1,\ldots,K\}$ | UAV $i$ stays idle or requests membership in task $k$ |
| Virtual flow handoff | $\delta^V_{i,j}$ | binary | Digital-twin traffic path used for pre-assessment |
| Virtual swarm membership | $\mathcal U_k^V$ | selected subset | UAVs admitted to task $k$ after resource and delay checks |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Sensing correctness reaches each task target, $P_k(T_k)\geq\overline P_k(T_k)$ |
| C2 | Every admitted virtual flow meets the task delay cap, $d^V_{i,j}\leq\tau_k$ for $\delta^V_{i,j}=1$ |
| C3 | Swarm size is capped, $\lvert\mathcal U_k^V\rvert\leq\overline N_U$ |
| C4 | One UAV serves at most one task, $\mathcal U_k^V\cap\mathcal U_{k'}^V=\varnothing$ for $k\neq k'$ |
| C5 | Admitted UAVs must be idle, $I_i=1$ |
| C6-C7 | Flow variables are binary and each member forwards to exactly one next hop, $\sum_j\delta^V_{i,j}=1$ |
| C8-C9 | Stability: arrival rates stay below the processing and link service rates on selected paths |

**Algorithm**: Use a distributed task-dynamic-crowdsourcing DQN with imitation-based reward shaping, then apply SNC-based traffic-flow allocation in the digital twin to pre-assign joining UAVs to resource-rich paths and pre-assess end-to-end delay before physical admission.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] proposed a digital-twin architecture for task-driven resource management in search-and-rescue UAV swarms. The framework jointly selects virtual swarm membership and intra-swarm flow paths to minimize membership changes across crowdsourcing cycles under sensing-correctness, end-to-end delay, swarm-size, single-task, idle-state, and traffic-stability constraints. A distributed MADRL crowdsourcing policy with imitation-based reward shaping proposes join actions, while an SNC traffic-flow allocator accepts only resource-feasible candidates. Simulations maintain more than 90% task requirement achievement with roughly four to six swarm members and reduce communication cost by over 80% versus the greedy scheme when enough UAVs are available, while UAV cost stays comparable to the other algorithms.

## Problem

UAV swarms can cover search-and-rescue tasks that a single UAV cannot, but task requirements, sensing performance, UAV mobility, communication routes, and computation resources interact. The paper targets resource management that is **task-driven** rather than merely connectivity-driven: admit UAVs and schedule traffic only when the virtual swarm can satisfy service and delay requirements.

## System model

- **Architecture.** The paper separates realistic task crowdsourcing from virtual traffic-flow scheduling, with four stages: task crowdsourcing, resource scheduling, pre-assessment, and feedback adjustment.
- **Digital twins.** UAV coordinators maintain DT models for physical and virtual swarm members, including routing, positions, sensor performance, transmit power, CPU frequency, channel gains, and statistical/theoretical end-to-end delay.
- **Traffic.** The virtual layer schedules sensing/service flows before physical route changes are committed.

## Method

The task-crowdsourcing component uses MADRL, with imitation learning used to improve learning efficiency. The traffic-flow allocation component uses [[stochastic-network-calculus]] to evaluate theoretical end-to-end delay bounds and to schedule intra-swarm service flows in the virtual layer before applying changes to the physical UAV network.

## Key findings

- The abstract reports that the proposed framework upholds a **90% achievement ratio** for task requirements while keeping UAV costs comparable.
- The results describe swarm sizes of roughly **4-6 members** when the task-requirement achievement ratio is above 90%.
- When enough UAVs are available, the conclusion reports communication-cost reductions of over 80% versus greedy selection and over 50% versus QMIX and IDQN, while maintaining the task-requirement satisfaction target.

## Limitations / future work

The authors note that larger UAV swarms make MADRL convergence more difficult, multi-hop relaying introduces more coupled variables, and stochastic-network-calculus delay estimates become less precise for time-varying multi-hop paths. Future work is framed around evaluation networks for faster adaptation/training and refined models for time-varying multi-hop UAV networks.

## Relation to the corpus

This paper complements the UAV-swarm MEC and collaborative-inference line by focusing on **task admission and traffic scheduling** rather than in-swarm DNN partitioning. It extends [[digital-twin]] from edge synchronization and ISCC control into a swarm-level resource-management role, and it supplies the corpus with a concrete [[stochastic-network-calculus]] example for probabilistic delay assessment in UAV-swarm traffic flows.

## Raw artifacts

- `raw/sources/Digital_Twin-Based_Task-Driven_Resource_Management_in_Intelligent_UAV_Swarms/Digital_Twin-Based_Task-Driven_Resource_Management_in_Intelligent_UAV_Swarms.md`
- Original PDF and extracted figures (`images/`) in the same folder.
