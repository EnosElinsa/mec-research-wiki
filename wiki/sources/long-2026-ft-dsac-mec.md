---
type: source
title: "Fault-Tolerant Aware Task Offloading Based on Reinforcement Learning in Mobile Edge Computing"
authors: ["Saiqin Long", "Chongxi Rao", "Haolin Liu", "Yunjie Chen", "Zhetao Li", "Jing Shang", "Qingyong Deng"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3636100"
venue: "IEEE Transactions on Mobile Computing, 25(5)"
modeling_card: required
tags: [source, mobile-edge-computing, task-offloading, fault-tolerance, dag-scheduling, soft-actor-critic]
related:
  - "[[task-offloading]]"
  - "[[soft-actor-critic]]"
  - "[[interdependent-tasks-dag]]"
  - "[[centralized-training-decentralized-execution]]"
created: 2026-08-27
updated: 2026-08-27
---

# Fault-Tolerant Aware Task Offloading Based on Reinforcement Learning in Mobile Edge Computing

## Citation

Long, S., Rao, C., Liu, H., Chen, Y., Li, Z., Shang, J., & Deng, Q. (2026). *Fault-Tolerant Aware Task Offloading Based on Reinforcement Learning in Mobile Edge Computing*. **IEEE Transactions on Mobile Computing, 25**(5). DOI: 10.1109/TMC.2025.3636100.

## TL;DR

FT-DSAC schedules DAG tasks with primary and backup replicas on heterogeneous MEC servers and relay paths. Action masking and fault-aware constraints are combined with discrete Soft Actor-Critic and centralized training to improve deadline success under server and relay failures.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Applications are DAG workflows whose tasks execute in heterogeneous MEC subnets. Each task has primary and backup placements on different subnets so execution can continue after a server or relay failure.

**Problem & objective**: Maximize deadline-aware task success, $\max |\mathcal N_{\mathrm{ddl}}|/N$; the reward gives deadline slack for on-time completion and penalties otherwise, while WAET is an evaluation metric.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Primary placement | $p_i$ | discrete server | Server executing task $i$ first |
| Backup placement | $b_i$ | discrete server | Fault-tolerant replica server |
| Task start/action | $a_t$ | masked discrete action | Offloading and scheduling action at decision step $t$ |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| DAG | Predecessor tasks complete before successors. |
| Replica separation | Primary and backup replicas use distinct subnets and obey predecessor-primary exclusion rules. |
| Resources | Server and relay capacities bound active task placements and transmissions. |
| Reliability | Failure-aware completion uses the earlier successful primary or backup execution. |
| Deadlines | Schedules are rewarded for deadline completion and penalized for weighted average execution time. |

**Algorithm**: Filter invalid actions using fault-aware masks and trajectory constraints, then train a discrete Soft Actor-Critic policy with centralized value estimation and the paper's DSAC/CQL updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Long et al. [x] addressed fault-tolerant DAG task offloading in heterogeneous MEC networks. Each task receives primary and backup placements with subnet-separation and precedence constraints, and the objective targets deadline-aware task success while the reward favors earlier completion. FT-DSAC combines action masking and trajectory filtering with discrete Soft Actor-Critic under centralized training. Experiments on synthetic and Montage, CyberShake, Epigenomics, and Inspiral workflows report 6% to 19% higher task-success reliability and 9% to 27% lower latency than the compared methods. Replica overhead and scaling to larger real business or language-model workflows remain open issues.

## Problem and system model

The system models task upload, queueing, computation, successor transfer, and execution reliability across heterogeneous edge servers and relays. Faults can make a primary or backup unavailable, so their placement and precedence must be coordinated.

## Method

FT-DSAC masks actions that violate DAG, replica-separation, resource, or fault rules. The policy learns deadline-aware task placement and scheduling while a centralized critic evaluates network-wide reliability and latency.

## Key findings

- FT-DSAC reports the highest task-success reliability across the evaluated failure-rate and network-density sweeps.
- Reported real-workflow task-success rates range from 0.92 to 0.96.
- The paper reports 6% to 19% reliability gains and 9% to 27% latency reductions over mainstream baselines.

## Limitations / future work

Primary-backup scheduling adds computational and storage overhead that may grow with workflow scale. The authors identify real business and LLM workflows and overhead reduction as future directions.

## Relation to the corpus

This source extends [[task-offloading]] with explicit replica-based fault tolerance and connects [[soft-actor-critic]] to DAG scheduling.

## Raw artifacts

- Parse: `raw/sources/Fault-Tolerant_Aware_Task_Offloading_Based_on_Reinforcement_Learning_in_Mobile_Edge_Computing/Fault-Tolerant_Aware_Task_Offloading_Based_on_Reinforcement_Learning_in_Mobile_Edge_Computing.md`
- Origin PDF and figures are in the same folder.
