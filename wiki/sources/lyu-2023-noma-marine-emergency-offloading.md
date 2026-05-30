---
type: source
title: "Computing Offloading and Resource Allocation of NOMA-Based UAV Emergency Communication in Marine Internet of Things"
authors: ["Ting Lyu", "Haitao Xu", "Feifei Liu", "Meng Li", "Lixin Li", "Zhu Han"]
year: 2023
url: "https://doi.org/10.1109/JIOT.2023.3348164"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, maritime-mec, computation-offloading, noma, coalition-formation-game, resource-allocation, post-disaster-mec]
related:
  - "[[maritime-mec]]"
  - "[[noma]]"
  - "[[coalition-formation-game]]"
  - "[[task-offloading]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[energy-latency-tradeoff]]"
  - "[[post-disaster-mec]]"
  - "[[nash-equilibrium]]"
  - "[[you-2025-uncertain-maritime-hasac]]"
  - "[[wang-2024-twotier-satellite-marine]]"
created: 2026-05-31
updated: 2026-05-31
---

# Computing Offloading and Resource Allocation of NOMA-Based UAV Emergency Communication in Marine Internet of Things

## Citation

Lyu, T., Xu, H., Liu, F., Li, M., Li, L., & Han, Z. (2023). *Computing Offloading and Resource Allocation of NOMA-Based UAV Emergency Communication in Marine Internet of Things*. **IEEE Internet of Things Journal**. DOI: 10.1109/JIOT.2023.3348164. (Date of publication 29 December 2023; date of current version 25 April 2024.)

## TL;DR

A [[noma|NOMA]]-based UAV emergency-communication framework for marine IoT where marine terminal devices offload tasks to UAV edge nodes. The objective is to minimize each device's **computation overhead**, defined as a weighting of task completion time and device energy consumption. Jointly optimizing IoT-device transmission power, UAV computing-resource allocation, task offloading, and carrier (subcarrier channel) allocation yields an NP-hard [[mixed-integer-nonlinear-programming|MINLP]]. The authors decompose it into (1) a resource-allocation problem with fixed offloading (solved by quasi-convex + convex optimization after decoupling) and (2) a task-offloading problem solved by a low-complexity **coalition formation game** that reaches a **Nash-stable** solution — the *coalition game-based task offloading* (CGTO) algorithm.

## Problem framing

Marine emergency scenarios (maritime rescue, post-disaster) need real-time voice/video and computation but lack dependable ground base stations. UAVs serve as aerial base stations / relays to extend coverage, but have limited battery and computing power. The paper argues that prior UAV-emergency work ignores **channel (carrier) assignment**, which both lets a UAV serve more users and improves fault tolerance. The system is framed as a space-air-ground-ocean network: satellites detect a marine disaster and notify an emergency control center, which dispatches UAVs that then negotiate an offloading + resource-allocation strategy with the IoT devices.

## System model

- **Actors.** Satellites (situational monitoring), an emergency control center (dispatch), UAVs (aerial base stations / edge nodes), and marine IoT devices ([[maritime-mec]]).
- **Access.** [[noma]] lets devices reuse the same resource blocks, raising spectral efficiency and connectivity; carrier/subcarrier channel allocation is a decision variable.
- **Objective.** Minimize device computation overhead = weighted sum of task completion time + device energy consumption ([[energy-latency-tradeoff]]).
- **Decisions.** IoT-device transmission power, UAV computing-resource allocation, task offloading decision, carrier allocation.
- **Formulation.** NP-hard [[mixed-integer-nonlinear-programming|MINLP]].

## Method

- **Decomposition.** Split into (a) resource allocation with fixed offloading, and (b) task offloading given optimal resource allocation.
- **Resource allocation.** Decouple into two subproblems solved with **quasi-convex and convex optimization** methods.
- **Task offloading.** A **coalition formation game** ([[coalition-formation-game]]): terminal users cooperate to form coalitions and make distributed offloading decisions, yielding the **CGTO** algorithm with low complexity and guaranteed convergence to a **Nash-stable** solution.

## Key findings

- CGTO achieves the **lowest computation overhead** among the compared schemes — local computing (LC), only coalition game (OCG), heuristic orthogonal computing offloading (HOCO), independent offloading and joint resource allocation (IOJRA), and a DDPG scheme (grounded in the parse's Section V; specific curves in the figures).
- The advantage over the local-computing baseline **grows with task input size** — larger tasks benefit more from offloading (parse Fig. 7).
- The scheme also reduces computation overhead in an additional **ground disaster** scenario, indicating scalability (parse Section V / Fig. 9).

## Limitations / future work

The parse's conclusion emphasizes effectiveness and reasonable resource allocation but does not enumerate explicit limitations beyond the modeled assumptions; results are simulation-based.

## Relation to the corpus

A **game-theoretic** (coalition-formation) treatment of maritime/marine offloading that contrasts with the DRL-based [[you-2025-uncertain-maritime-hasac]] and the hybrid Stackelberg-bargaining [[wang-2024-twotier-satellite-marine]] approaches to maritime MEC. It is one of the corpus's clearest uses of [[coalition-formation-game]] for offloading (alongside the PLS coalition game in [[chen-2024-three-party-hierarchical-game-pls]]) and pairs [[noma]] with carrier allocation as in [[qin-2025-matd3-noma-queue-sagin]] / [[wang-2024-hybrid-oma-noma-sagin]]. Shares senior co-author Zhu Han with the NUAA aerial/maritime cluster ([[jia-2022-hierarchical-aerial-matching]], [[you-2025-uncertain-maritime-hasac]]). Reinforces [[maritime-mec]] and [[post-disaster-mec]].

## Raw artifacts

- `raw/sources/Computing_Offloading_and_Resource_Allocation_of_NOMA-Based_UAV_Emergency_Communication_in_Marine_Internet_of_Things/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
