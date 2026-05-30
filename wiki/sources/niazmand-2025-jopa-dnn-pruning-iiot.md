---
type: source
title: "Joint Task Offloading, DNN Pruning, and Computing Resource Allocation for Fault Detection With Dynamic Constraints in Industrial IoT"
authors: ["Vahidreza Niazmand", "Qiang Ye"]
year: 2025
url: "https://doi.org/10.1109/TCCN.2025.3529688"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
tags: [source, industrial-iot, task-offloading, dnn-pruning, resource-allocation, soft-actor-critic, dynamic-qos, markov-reward-process]
related:
  - "[[task-offloading]]"
  - "[[dnn-model-partition]]"
  - "[[soft-actor-critic]]"
  - "[[hybrid-action-decision-making]]"
  - "[[dynamic-qos-constraints]]"
  - "[[markov-reward-process]]"
  - "[[knowledge-distillation-for-drl]]"
  - "[[wang-2024-maritime-eh-jcora]]"
  - "[[zhang-2025-vnf-sgin-dql]]"
created: 2026-05-31
updated: 2026-05-31
---

# Joint Task Offloading, DNN Pruning, and Computing Resource Allocation for Fault Detection With Dynamic Constraints in Industrial IoT

## Citation

Niazmand, V., & Ye, Q. (2025). *Joint Task Offloading, DNN Pruning, and Computing Resource Allocation for Fault Detection With Dynamic Constraints in Industrial IoT*. **IEEE Transactions on Cognitive Communications and Networking**. DOI: 10.1109/TCCN.2025.3529688. (Date of publication 14 Jan 2025; date of current version 8 Oct 2025.)

## TL;DR

A joint **task offloading + DNN model pruning + edge computing-resource allocation (JOPA)** problem for a **fault-detection service on industrial washing machines** in a layered IIoT system. It maximizes **long-term network resource utilization** while guaranteeing **time-varying** per-task **delay and accuracy (QoS)** requirements. Formulated as a stochastic problem, transformed to a **Markov reward process (MRP)**, and solved with a refined **soft actor-critic (SAC)** DRL framework customized for **hybrid (mixed discrete + continuous) actions**.

## Problem framing

DNN inference for facility fault diagnosis is accurate but compute-heavy (many FLOPs), straining IIoT device onboard capacity; pure device-only or edge-only solutions both fail to meet low-delay needs under time-varying wireless channels. Fault-detection tasks have **criticality levels that vary over time**, so their accuracy/delay requirements are non-stationary. Deploying **pruned** DNNs on devices (small footprint, fast, lower accuracy) while keeping **full-weight** models on the edge lets the system trade accuracy for delay adaptively. The technical question: jointly decide offloading, local pruning, and resource allocation to maximize bandwidth + compute utilization while meeting dynamic QoS.

## System model

- **Two-layer architecture.** Layer 1: N industrial washing machines, each with a vibration sensor, partitioned into G groups, each group wired to an **IIoT gateway (IGW)** with processing capacity. Layer 2: one **LTE base station** (LTE-M uplink) connected to an **edge server**.
- **Pruned vs full models.** Each IGW hosts V pruned DNN instances (each with an average accuracy and pruning rate); the edge server holds the full-weight model.
- **Objective.** Maximize overall network resource utilization (local + wireless bandwidth + edge compute) over time, under per-time-slot **end-to-end delay** and **accuracy** constraints, with a penalty for **dropped tasks**.

## Method

- Formulate a stochastic optimization, then recast as a **[[markov-reward-process|Markov reward process]]** (state transitions independent of actions) to handle the large size + dynamic QoS.
- Design a **[[soft-actor-critic|SAC]]**-based DRL solution with experience replay; actor/critic/target networks are customized to accommodate **hybrid actions** (discrete offloading + pruned-model selection alongside continuous resource allocation), give robust state-action evaluation, and stabilize training.
- Stochastic-policy gradient gives more exploration and better adaptation to time-varying requirements than DDPG.

## Key findings

- The proposed scheme (JOPA) **consistently achieves the highest overall resource utilization** vs two benchmarks (a JOPA variant **JOPAV1** without flexible local-model selection, and **AGDM**), and the **lowest task-dropping rate** — kept below the 1% target even as load grows, where JOPAV1 exceeds the limit once N > 150 (read from Figs. 9–11; reported qualitatively).
- It best **balances utilization vs QoS**: slightly higher inference accuracy at the cost of some delay, and better adaptability to dynamic delay/accuracy requirements.
- A pruning-rate study finds a **moderate rate (p = 0.7)** balances accuracy and delay; p = 0.1 maximizes accuracy but raises delay/dropping, p = 0.9 cuts delay but hurts accuracy (Fig. 12).

## Limitations / future work

Simulation-based, specific to the washing-machine fault-detection service; the parse's conclusion section was not reached in the read range, so further-work items are `not in parse` here beyond what the contributions imply.

## Relation to the corpus

A rare **DNN-pruning-aware** MEC entry that pairs **DNN model compression** with offloading and resource allocation — adjacent to the model-partition theme of [[dnn-model-partition]] but optimizing pruning rate rather than split point. Methodologically it joins the **SAC + hybrid-action** family ([[soft-actor-critic]], [[hybrid-action-decision-making]]), and its **MRP** formulation and **dynamic time-varying QoS** are distinctive vocabulary. Shares author Qiang Ye (University of Calgary) with [[wang-2024-maritime-eh-jcora]] and [[zhang-2025-vnf-sgin-dql]] — the Qiang-Ye cross-cutting thread. Anchors the [[dynamic-qos-constraints]] and [[markov-reward-process]] concepts.

## Raw artifacts

- `raw/sources/Joint_Task_Offloading_DNN_Pruning_and_Computing_Resource_Allocation_for_Fault_Detection_With_Dynamic_Constraints_in_Industrial_IoT/full.md`
- Original PDF and extracted figures in the same folder.
