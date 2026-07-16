---
type: source
title: "DNN Partitioning, Task Offloading, and Resource Allocation in Dynamic Vehicular Networks: A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach"
authors: ["Zhang Liu", "Hongyang Du", "Junzhe Lin", "Zhibin Gao", "Lianfen Huang", "Seyyedali Hosseinalipour", "Dusit Niyato"]
year: 2025
url: "https://doi.org/10.1109/TMC.2024.3486728"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, vehicular-mec, dnn-model-partition, task-offloading, lyapunov-optimization, diffusion-model, multi-agent-drl, resource-allocation]
related:
  - "[[vehicular-mec]]"
  - "[[dusit-niyato]]"
  - "[[dnn-model-partition]]"
  - "[[lyapunov-optimization]]"
  - "[[maddpg]]"
  - "[[task-offloading]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[bai-2024-delay-aware-cooperative-edge-cloud]]"
created: 2026-06-04
updated: 2026-07-16
modeling_card: required
---

# DNN Partitioning, Task Offloading, and Resource Allocation in Dynamic Vehicular Networks: A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach

## Citation

Liu, Z., Du, H., Lin, J., Gao, Z., Huang, L., Hosseinalipour, S., & Niyato, D. (2025). *DNN Partitioning, Task Offloading, and Resource Allocation in Dynamic Vehicular Networks: A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2024.3486728. (Received 23 May 2024; accepted 23 October 2024; published 28 October 2024; current version 5 February 2025.)

## TL;DR

In vehicular edge computing (VEC), vehicles run DNN inference tasks (e.g., autonomous driving) and must decide how to partition each DNN across layers, where to offload the remaining layers (RSU or nearby service vehicles via V2I/V2V), and how to allocate RSU compute resources — all in a dynamic, mobile environment. The paper formulates this as a long-term MINLP under system-stability constraints, applies **Lyapunov optimization** to decompose it into per-slot subproblems, and introduces **MAD2RL** (Multi-Agent Diffusion-based Deep Reinforcement Learning) — claimed as the first integration of a diffusion model into a multi-agent RL framework — to solve partitioning and offloading decisions. Convex optimization provides a closed-form resource-allocation subroutine. Simulations on OpenStreetMap / SUMO traces with real DNN models demonstrate superior performance over benchmarks.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Client vehicles run DNN inference tasks and offload layer prefixes to one RSU or nearby service vehicles over OFDMA V2I/V2V links. Queues at client vehicles, the RSU, and service vehicles evolve under mobile channels and long-term stability requirements.

**Problem & objective**: Long-term VEC task-partitioning and offloading MINLP, minimized through Lyapunov drift-plus-penalty, with objective $\min\mathbb E[\text{DNN completion time}]$ subject to queue stability and per-slot resource feasibility.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| DNN split layer | $\phi_i(t)$ | integer, $1\ldots L$ | First layer executed at the selected edge node |
| Offload destination | $\xi_{i,j}(t)$ | binary | Client vehicle $i$ selects RSU or service vehicle $j$ |
| RSU CPU allocation | $F_k^{\mathrm{rsu}}(t)$ | continuous, nonnegative | RSU frequency assigned to DNN model type $k$ |
| Task admission/service | $a_i(t)$ | discrete | Number of DNN jobs admitted to the per-slot service process |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each client chooses one valid split and at most one edge destination |
| C2 | RSU CPU allocation stays within the RSU capacity |
| C3 | V2I/V2V transmission rates and queues remain feasible in each slot |
| C4 | Long-term queue drift is bounded, ensuring system stability |
| C5 | Offloaded and local layer workloads respect per-task processing order and deadlines |

**Algorithm**: Apply Lyapunov drift-plus-penalty → solve per-slot partition/offload actions with MAD2RL's diffusion actor → use closed-form KKT/CVX allocation for RSU resources → update queues and repeat across mobile traces.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liu et al. [x] studied DNN partitioning, task offloading, and resource allocation in dynamic vehicular edge computing with an RSU and service vehicles. They formulated a long-term mixed-integer nonlinear problem that minimizes DNN task completion time while maintaining queue stability. Lyapunov optimization converts the long-horizon problem into per-slot decisions, and MAD2RL uses a diffusion-based multi-agent policy to choose layer partitions and offloading destinations. Given those discrete decisions, a convex KKT subroutine allocates RSU computing resources in closed form. Simulations with OpenStreetMap and SUMO mobility and real DNN models report lower completion time and faster convergence than the evaluated DRL baselines.

## Problem framing

DNN-based vehicular tasks (autonomous driving, traffic-sign recognition) impose massive compute loads (e.g., ResNet152 requires ~22.6B FLOPs for a single 224×224 image). A single vehicle cannot handle this; VEC uses RSUs and neighboring service vehicles as edge nodes via V2I and V2V links. The challenge is threefold: (i) heterogeneous layer-wise compute cost and output-data size make the optimal DNN partition point non-obvious; (ii) vehicle mobility creates continuously varying channel conditions that demand real-time decisions; (iii) system stability (queue boundedness over time) must be guaranteed, not just per-slot performance. Existing heuristic and decomposition approaches are too slow for real-time use, and prior DRL approaches ignore stability.

## System model

- **Network.** Single RSU (V2I), multiple service vehicles (V2V), OFDMA (no intra-system interference assumed). Client vehicles (CVs) generate DNN tasks every time slot.
- **DNN partitioning.** Integer variable φ_i(t) selects the split layer: layers 1…φ-1 computed locally, layers φ…L offloaded to an edge node (RSU or SV).
- **Offloading.** Binary variable ξ_{i,j}(t) selects the destination edge node.
- **Resource allocation.** Continuous variable F_k^rsu(t) splits RSU CPU frequency across DNN model types.
- **Task queues.** Separate queues at each CV, the RSU (per DNN type), and each SV track backlog; Lyapunov function is the sum of squared queue lengths.
- **Objective.** Minimize expected total DNN task completion time subject to long-term queue stability.

## Method

1. **Lyapunov optimization** decomposes the long-horizon MINLP into per-slot deterministic problems via a drift-plus-penalty framework (drift bounds queue growth; penalty is the weighted sum of task delays).
2. **MAD2RL** solves the per-slot mixed-integer partitioning and offloading problem. Each CV is an agent. The diffusion model operates by iteratively denoising a Gaussian sample through M reverse steps, producing a probability distribution over joint (partition, offload) actions, from which the argmax action is drawn. This replaces the standard MLP actor, handling the high-dimensional, combinatorial action space more effectively.
3. **Convex subroutine.** Given partitioning and offloading decisions from MAD2RL, optimal RSU resource allocation is obtained in closed form via KKT conditions, significantly reducing the DRL's training burden.
4. **Validation.** Simulations use OpenStreetMap road topology and SUMO vehicle mobility with real DNN models (VGG16, ResNet18, etc.); results compared to several baselines.

## Key findings

- MAD2RL achieves **lower DNN task completion time** than benchmark DRL strategies (including MADDPG, MAD3PG) across different numbers of client vehicles and DNN model types (parse Sections VIII, abstract).
- The diffusion-model actor handles the combinatorial, high-dimensional action space better than standard MLP-based DRL in highly dynamic VEC environments (parse Sections VI, VIII).
- Lyapunov-guided system stability is maintained over time, a property absent in most prior VEC DRL works (parse Sections IV, V).
- The convex subroutine significantly improves MAD2RL convergence speed by eliminating resource-allocation from the DRL action space (parse Section VII-C).

## Limitations / future work

Assumes a single RSU coverage zone (multiple RSUs left as future extension). OFDMA inter-vehicle interference is neglected for tractability. The parse does not enumerate additional explicit limitations beyond these modeling assumptions.

## Relation to the corpus

Extends [[vehicular-mec]] with explicit [[dnn-model-partition]] and [[lyapunov-optimization]]-based stability guarantees, complementing [[bai-2024-delay-aware-cooperative-edge-cloud]] (which applies Lyapunov to multi-UAV edge-cloud cooperation). The [[diffusion-model-as-optimizer]] actor distinguishes this from other MARL-based VEC works in the corpus that use standard DDPG/SAC actors. The Lyapunov + DRL hybrid pattern recurs in several corpus sources; this paper applies it specifically to the layer-granularity DNN partitioning setting.

## Raw artifacts

- `raw/sources/DNN_Partitioning_Task_Offloading_and_Resource_Allocation_in_Dynamic_Vehicular_Networks_A_Lyapunov-Guided_Diffusion-Based_Reinforcement_Learning_Approach/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
