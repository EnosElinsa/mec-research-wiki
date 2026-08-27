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
updated: 2026-08-27
---

# Workload-Aware Performance Model Based Soft Preemptive Real-Time Scheduling for Neural Processing Units

## Citation

Yao, Y., Hu, Y., Dang, Y., Tao, W., Hu, K., Huang, Q., Peng, Z., Yang, G., & Zhou, X. *Workload-Aware Performance Model Based Soft Preemptive Real-Time Scheduling for Neural Processing Units*. Venue and DOI are not in the parse.

## TL;DR

WAMSPRES adds Kubernetes resource management, workload-aware execution-time prediction, and soft preemption to an NPU in a fixed-wing UAV embedded system. Dynamic quota reductions let high-priority tasks meet deadlines despite NPU hardware lacking native preemptive scheduling.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple neural-network tasks share an NPU in an airborne embedded system. Tasks have priorities, deadlines, input sizes, and concurrent workload that changes their remaining execution time.

**Problem & objective**: Allocate dynamic NPU computing quotas to maximize deadline success, $\max \sum_i\mathbf 1\{C_i\leq d_i\}$, using predicted remaining execution time.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| NPU quota | $q_i$ | continuous share | Computing resource assigned to task $i$ |
| Task priority | $\rho_i$ | ordered value | Scheduling priority used at each decision point |
| Dispatch order | $\pi$ | discrete sequence | Order in which ready tasks receive NPU quota |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Capacity | Task quotas sum within the available NPU computing resource. |
| Deadline | High-priority tasks should complete before their relative deadlines. |
| Isolation | Tasks share NPU resources without violating container/device isolation. |
| Soft preemption | Quotas can be reduced at scheduling points; running kernels are not forcibly interrupted. |

**Algorithm**: Predict remaining task time from workload indicators and input parameters using a lightweight BPNN, then greedily reassign NPU quotas by priority and deadline through the Kubernetes-based scheduler.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yao et al. [x] developed WAMSPRES for soft preemptive real-time scheduling of concurrent NPU tasks in airborne embedded systems. A workload-aware performance model predicts remaining execution time from device load and task inputs, while a Kubernetes device-plugin framework exposes fine-grained NPU quotas. The scheduler dynamically reduces low-priority quotas when urgent tasks arrive, approximating preemption despite NPU hardware limitations. A Huawei Atlas 200 prototype and simulated and realistic task sets report MAPE below 5% and 8% and up to 48.7% higher scheduling success than the inherent scheduler. The workload indicators depend on vendor APIs and the prototype's fixed task set.

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
