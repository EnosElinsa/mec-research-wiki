---
type: source
modeling_card: required
title: "Large Language Model-based QoS-aware Resource Allocation for Multi-UAV Cooperative Edge Computing Networks"
authors: ["Yaqing Wang", "Lun Tang", "Weili Wang", "Xiaoqiang He", "Qianbin Chen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3683128"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), early access, 2026"
tags: [source, multi-uav-assisted-mec, llm, resource-allocation, knowledge-distillation, mappo, fairness]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[llm-assisted-resource-allocation]]"
  - "[[llm-assisted-mec-optimization-control-plane]]"
  - "[[knowledge-distillation-for-drl]]"
  - "[[mappo]]"
  - "[[graph-neural-network]]"
  - "[[graph-based-resource-management]]"
  - "[[task-migration]]"
  - "[[task-offloading]]"
  - "[[jains-fairness-index]]"
  - "[[fairness-metrics-in-mec]]"
  - "[[qianbin-chen]]"
created: 2026-07-07
updated: 2026-07-16
---

# Large Language Model-based QoS-aware Resource Allocation for Multi-UAV Cooperative Edge Computing Networks

## Citation

Wang, Y., Tang, L., Wang, W., He, X., & Chen, Q. (2026). *Large Language Model-based QoS-aware Resource Allocation for Multi-UAV Cooperative Edge Computing Networks*. **IEEE Transactions on Mobile Computing**, early access, 1-18. DOI: 10.1109/TMC.2026.3683128.

## TL;DR

Introduces an LLM teacher-student framework for QoS-aware resource allocation in multi-UAV cooperative edge computing. The system jointly decides user access control, UAV trajectories, computation allocation, bandwidth allocation, and UAV-to-UAV task-migration ratios. A cloud-side LLM teacher uses a network knowledge graph, relation-aware GAT, LoRA fine-tuning, and Tree-of-Thoughts reasoning to generate expert policies; UAV-side MAPPO students learn distributed policies through policy distillation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: User devices offload tasks to cooperative UAV edge servers connected by air-to-air migration links. A cloud teacher sees a network knowledge graph, while UAV-side students execute distributed policies over dynamic channels, task loads, computing capacity, and bandwidth.

**Problem & objective**: A long-term mixed discrete-continuous control problem minimizes weighted delay and unfairness, $\min \alpha D_{\mathrm{avg}}+(1-\alpha)(1-J_{\mathrm{fair}})$, over access, trajectory, compute, bandwidth, and task migration.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User access | $x_{u,m}(t)$ | binary | UAV initially serving device $u$ |
| UAV trajectory | $\mathbf q_m(t)$ | continuous position | Position of UAV edge server $m$ |
| Computing allocation | $f_{u,m}(t)$ | continuous, nonnegative | CPU resource assigned to task $u$ |
| Bandwidth allocation | $b_{u,m}(t)$ | continuous, nonnegative | Uplink or migration bandwidth share |
| Migration ratio | $\rho_{u,m,m'}(t)$ | continuous, $[0,1]$ | Task fraction moved between UAVs |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each device has one feasible access association and task fractions are conserved |
| C2 | Per-UAV CPU allocations do not exceed computing capacity |
| C3 | Bandwidth shares and transmit resources remain within link budgets |
| C4 | Migration ratios use available air-to-air links and preserve task workload |
| C5 | UAV trajectories satisfy mobility, region, and separation constraints |

**Algorithm**: Build the network knowledge graph → encode relations with a relation-aware GAT → generate expert allocations with a LoRA-tuned LLM and Tree-of-Thoughts reasoning → distill teacher policies to UAV-side MAPPO students with policy matching → execute decentralized actions and update from delay-fairness rewards.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied QoS-aware resource allocation in cooperative multi-UAV edge computing networks using a large-language-model teacher and distributed student policies. They formulated a weighted delay and fairness objective over user access, UAV trajectories, computing resources, bandwidth, and inter-UAV task-migration ratios. A network knowledge graph and relation-aware graph attention network provide structured state information to a LoRA-tuned teacher model. Tree-of-Thoughts reasoning generates expert policies, and policy distillation transfers them to MAPPO students for decentralized UAV execution. Simulations report faster convergence, lower delay, and higher Jain-style fairness than the evaluated learning baselines and ablated teacher components.

## Problem

Multi-UAV cooperative edge computing must keep delay low while preserving fairness across user devices. The decision space mixes access control, trajectory, bandwidth, compute, and inter-UAV task migration, so a centralized optimizer is expensive and a fully local DRL policy can miss network-wide structure. The paper formulates a weighted delay-fairness objective combining delay with Jain-style fairness.

## System model

- A cloud layer trains or updates a teacher model.
- UAVs act as cooperative edge servers with student policies.
- User devices upload tasks over ground-to-air links.
- UAVs can migrate task fractions over air-to-air links.
- The objective optimizes weighted delay-fairness by controlling access, trajectories, computation, bandwidth, and migration ratios.

## Method

The framework separates expensive global reasoning from UAV-side execution:

- A network knowledge graph stores relationships among UAVs, devices, tasks, and resources.
- A relation-aware GAT encodes graph structure for the teacher.
- A fine-tuned LLM with LoRA and Tree-of-Thoughts reasoning generates expert resource-allocation policies.
- UAV-side students use MAPPO for distributed decision-making.
- Policy distillation transfers teacher behavior to the student policies; the parse mentions JS-divergence-style policy matching.

## Key findings

- The proposed model converges faster and reaches higher reward than the compared baselines in the reported training curves.
- The paper reports lower delay and higher fairness as device count, UAV computing capacity, and bandwidth vary.
- The delay curves stabilize around 300-400 episodes in the reported experiments.
- The ablation table reports full-model delay 244, fairness 0.918, and weighted delay-fairness 0.448. Removing ToT, R-GAT, NKG, or distillation worsens the weighted delay-fairness score to 0.486, 0.522, 0.558, and 0.594, respectively; the distillation removal causes the largest drop in that table.

## Limitations / future work

The conclusion emphasizes faster convergence, lower steady-state latency, improved fairness, robustness, and scalability. Explicit limitations or future-work directions are not present in the parse -> `not in parse`.

## Relation to the corpus

This source extends [[llm-assisted-resource-allocation]] from LLM-backed runtime repair into teacher-student policy generation for [[multi-uav-assisted-mec]]. It connects LLM reasoning to [[knowledge-distillation-for-drl]], [[mappo]], [[graph-neural-network]], [[graph-based-resource-management]], [[task-migration]], and [[jains-fairness-index]]. It is one of the teacher-policy instances of [[llm-assisted-mec-optimization-control-plane]], and gives the fairness hub a multi-UAV LLM-policy example where delay and fairness are optimized jointly.

## Raw artifacts

- `raw/sources/Large Language Model-based QoS-aware Resource Allocation for Multi-UAV Cooperative Edge Computing Networks/Large Language Model-based QoS-aware Resource Allocation for Multi-UAV Cooperative Edge Computing Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
