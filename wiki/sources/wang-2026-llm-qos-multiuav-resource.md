---
type: source
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
updated: 2026-07-14
---

# Large Language Model-based QoS-aware Resource Allocation for Multi-UAV Cooperative Edge Computing Networks

## Citation

Wang, Y., Tang, L., Wang, W., He, X., & Chen, Q. (2026). *Large Language Model-based QoS-aware Resource Allocation for Multi-UAV Cooperative Edge Computing Networks*. **IEEE Transactions on Mobile Computing**, early access, 1-18. DOI: 10.1109/TMC.2026.3683128.

## TL;DR

Introduces an LLM teacher-student framework for QoS-aware resource allocation in multi-UAV cooperative edge computing. The system jointly decides user access control, UAV trajectories, computation allocation, bandwidth allocation, and UAV-to-UAV task-migration ratios. A cloud-side LLM teacher uses a network knowledge graph, relation-aware GAT, LoRA fine-tuning, and Tree-of-Thoughts reasoning to generate expert policies; UAV-side MAPPO students learn distributed policies through policy distillation.

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
