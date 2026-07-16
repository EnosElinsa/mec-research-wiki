---
type: source
title: "Joint Task Offloading, DNN Pruning, and Computing Resource Allocation for Fault Detection With Dynamic Constraints in Industrial IoT"
authors: ["Vahidreza Niazmand", "Qiang Ye"]
year: 2025
url: "https://doi.org/10.1109/TCCN.2025.3529688"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
modeling_card: required
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
updated: 2026-07-16
---

# Joint Task Offloading, DNN Pruning, and Computing Resource Allocation for Fault Detection With Dynamic Constraints in Industrial IoT

## Citation

Niazmand, V., & Ye, Q. (2025). *Joint Task Offloading, DNN Pruning, and Computing Resource Allocation for Fault Detection With Dynamic Constraints in Industrial IoT*. **IEEE Transactions on Cognitive Communications and Networking**. DOI: 10.1109/TCCN.2025.3529688. (Date of publication 14 Jan 2025; date of current version 8 Oct 2025.)

## TL;DR

A joint **task offloading + DNN model pruning + edge computing-resource allocation (JOPA)** problem for a **fault-detection service on industrial washing machines** in a layered IIoT system. It maximizes **long-term network resource utilization** while guaranteeing **time-varying** per-task **delay and accuracy (QoS)** requirements. Formulated as a stochastic problem, transformed to a **Markov reward process (MRP)**, and solved with a refined **soft actor-critic (SAC)** DRL framework customized for **hybrid (mixed discrete + continuous) actions**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Vibration sensors on $N$ industrial washing machines feed $G$ industrial gateways, which either run one of $V$ pruned fault-detection DNNs locally or offload a task over LTE-M to an edge server holding the full model. Channel gain and task criticality vary by slot, and criticality determines each task's delay and accuracy requirements.

**Problem & objective**: The stochastic JOPA problem selects task offloading, local pruned-model instances, and edge CPU shares to maximize $\mathbb E[\eta^{-1}\sum_{t=1}^{\eta}u^t]$, the long-term aggregate utilization of local computing, bandwidth, and edge computing resources, subject to per-slot QoS constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Task offloading | $o_{m,g}^t$ | binary, $\{0,1\}$ | Whether task $m$ at gateway $g$ is offloaded |
| Pruned-model selection | $v_g^t$ | categorical, $\{0,\ldots,V-1\}$ | Local DNN instance selected at gateway $g$ |
| Edge CPU share | $c_g^t$ | continuous, $[0,1]$ | Fraction of edge computing capacity assigned to gateway $g$ |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| 17a | End-to-end delay obeys the criticality-dependent upper bound $D_{m,g}^t\le T^{\max}-k_{m,g}^t(T^{\max}-T^{\min})$ |
| 17b | A locally processed task meets its criticality-dependent minimum inference accuracy |
| 17c-17e | No edge share is assigned to a gateway with no offloaded task, and $\sum_g c_g^t=1$ with $0\le c_g^t\le1$ |
| 17f | Edge processing delay does not exceed task transmission time: $E_{m,g}^t\le\Omega_{m,g}^t$ |
| Dropping | A task violating delay, accuracy, or edge-service constraints is dropped and incurs reward penalty $J$ |

**Algorithm**: Represent channel gains and task criticalities as an action-independent Markov reward process. Use a customized SAC actor that maps continuous samples to binary offloading, categorical model selection, and softmax-normalized CPU shares; train it with two critics, slowly updated target networks, entropy regularization, and experience replay using a utilization reward penalized by the dropped-task ratio.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Niazmand and Ye [x] studied joint task offloading, DNN pruning, and computing-resource allocation for dynamic industrial fault detection. They formulated a stochastic optimization that maximizes long-term local, radio, and edge resource utilization while enforcing criticality-dependent per-task delay and inference-accuracy requirements. The problem was represented as a Markov reward process and solved with a customized soft actor-critic whose hybrid action maps jointly select offloading, local pruned models, and continuous edge CPU shares. Simulations showed that flexible pruned-model selection improved resource utilization and reduced task dropping relative to the two benchmarks while adapting to changing network load and QoS requirements.

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

Simulation-based, specific to the washing-machine fault-detection service. The conclusion explicitly points future work toward dynamic radio bandwidth resource allocation and machine-learning-based joint radio scheduling, task offloading, and computing resource allocation under varying network conditions and QoS demands.

## Relation to the corpus

A rare **DNN-pruning-aware** MEC entry that pairs **DNN model compression** with offloading and resource allocation — adjacent to the model-partition theme of [[dnn-model-partition]] but optimizing pruning rate rather than split point. Methodologically it joins the **SAC + hybrid-action** family ([[soft-actor-critic]], [[hybrid-action-decision-making]]), and its **MRP** formulation and **dynamic time-varying QoS** are distinctive vocabulary. Shares author Qiang Ye (University of Calgary) with [[wang-2024-maritime-eh-jcora]] and [[zhang-2025-vnf-sgin-dql]] — the Qiang-Ye cross-cutting thread. Anchors the [[dynamic-qos-constraints]] and [[markov-reward-process]] concepts.

## Raw artifacts

- `raw/sources/Joint_Task_Offloading_DNN_Pruning_and_Computing_Resource_Allocation_for_Fault_Detection_With_Dynamic_Constraints_in_Industrial_IoT/full.md`
- Original PDF and extracted figures in the same folder.
