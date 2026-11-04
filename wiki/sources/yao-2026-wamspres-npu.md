---
type: source
title: "Workload-Aware Performance Model Based Soft Preemptive Real-Time Scheduling for Neural Processing Units"
authors: ["Yuan Yao", "Yujiao Hu", "Yi Dang", "Wei Tao", "Kai Hu", "Qiming Huang", "Zhe Peng", "Gang Yang", "Xingshe Zhou"]
year: 2026
url: "not in parse"
venue: "not in parse"
modeling_card: required
tags: [source, airborne-embedded-system, neural-processing-unit, real-time-scheduling, soft-preemption, kubernetes]
related:
  - "[[uav-trajectory-control]]"
  - "[[action-space-explosion-in-multi-uav-mec]]"
created: 2026-08-27
updated: 2026-11-03
---

# Workload-Aware Performance Model Based Soft Preemptive Real-Time Scheduling for Neural Processing Units

## Citation

Yao, Y., Hu, Y., Dang, Y., Tao, W., Hu, K., Huang, Q., Peng, Z., Yang, G., & Zhou, X. *Workload-Aware Performance Model Based Soft Preemptive Real-Time Scheduling for Neural Processing Units*. Venue and DOI are not in the parse.

## TL;DR

WAMSPRES adds Kubernetes resource management, workload-aware execution-time prediction, and soft preemption to an NPU in a fixed-wing UAV embedded system. Dynamic quota reductions let high-priority tasks meet deadlines despite NPU hardware lacking native preemptive scheduling.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Several periodic neural-network tasks with fixed priorities share one Huawei Atlas 200 NPU in a small fixed-wing UAV's airborne embedded system. The inherent NPU scheduler shares resources equally and cannot preempt, so a Kubernetes device plugin exposes fine-grained computing-power quotas, and each task's remaining execution time changes whenever the workload changes (task arrival or exit).

**Problem & objective**: This is a scheduling design with no formal optimization problem. Each task is $Task_i=\langle\tau_i^{\delta,L},\gamma_i^{\delta,L},F_{i,j},D_i,P_i\rangle$ in (4) (actual and predicted remaining execution time under quota $\delta$ and workload $L$, completion rate, implicit deadline, priority). The goal is to raise the schedulability ratio, the share of tasks that meet their deadlines.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Computing-power quota | $\delta_{i,j}$ | percentage of the NPU, total at most TOTAL | Quota given to $Task_i$ after the $j$-th workload change |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (6) | Minimum quota meeting the deadline: $\gamma_i^{\delta_{i,k},L_{i,k}}\le D_i-\sum_{j<k}\tau_i^{\delta_{i,j},L_{i,j}}$ |
| Model rule | Completion rate update (5): $F_{i,j}=\frac{\tau_i^{\delta_{i,j},L_{i,j}}}{\gamma_i^{\delta_{i,j},L_{i,j}}}(1-F_{i,j-1})+F_{i,j-1}$ |
| Algorithm rule | Allocated quotas are compared with the total quota TOTAL; inactive tasks get zero quota |

**Algorithm**: A lightweight BPNN predicts remaining execution time from completion rate, workload indicators, and quota. At each workload change, the greedy soft-preemptive scheduler (Algorithm 1) visits tasks in descending priority, finds each task's minimum quota satisfying (6), and reduces low-priority quotas when the total exceeds TOTAL.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yao et al. [x] developed WAMSPRES for soft preemptive real-time scheduling of concurrent NPU tasks in airborne embedded systems. A workload-aware performance model predicts remaining execution time from device load and task inputs, while a Kubernetes device-plugin framework exposes fine-grained NPU quotas. The scheduler dynamically reduces low-priority quotas when urgent tasks arrive, approximating preemption despite NPU hardware limitations. A Huawei Atlas 200 prototype and simulated and realistic task sets report MAPE below 5% and 8% and up to 48.7% more schedulable tasks than the inherent scheduler; in a 2-hour realistic run, the Ascend scheduler reached a 54.6% schedulability ratio while WAMSPRES had no failures. The workload indicators depend on vendor APIs and the prototype's fixed task set.

## Problem and system model

Airborne AI tasks such as detection and control share a resource-constrained NPU. Co-execution increases execution time, but the native NPU scheduler lacks priority and preemption controls, causing deadline misses for urgent tasks.

## Method

Kubernetes manages virtual NPU resources through a device plugin. A performance predictor estimates remaining runtime, and a greedy scheduler reallocates quotas at scheduling points according to priority and deadline.

## Key findings

- WAMSPRES reports average MAPE below 5% on simulated sets and below 8% on realistic sets.
- Scheduling success improves by up to 48.7% over the inherent Ascend scheduler.
- The realistic airborne task set reaches 100% scheduling success in the reported duration experiments.

## Limitations / future work

The lightweight predictor trades model complexity for overhead and may forget when task sets change. Workload indicators rely on Huawei-specific driver APIs; broader hardware and changing-task support are future work.

## Relation to the corpus

This source adds NPU resource scheduling to the airborne-computing side of the corpus and provides a systems-level complement to UAV trajectory and MEC offloading optimization.

## Raw artifacts

- Parse: `raw/sources/Workload-Aware_Performance_Model_Based_Soft_Preemptive_Real-Time_Scheduling_for_Neural_Processing_Units/Workload-Aware_Performance_Model_Based_Soft_Preemptive_Real-Time_Scheduling_for_Neural_Processing_Units.md`
- Origin PDF and figures are in the same folder.
