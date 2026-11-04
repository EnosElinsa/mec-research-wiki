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
updated: 2026-11-03
---

# Fault-Tolerant Aware Task Offloading Based on Reinforcement Learning in Mobile Edge Computing

## Citation

Long, S., Rao, C., Liu, H., Chen, Y., Li, Z., Shang, J., & Deng, Q. (2026). *Fault-Tolerant Aware Task Offloading Based on Reinforcement Learning in Mobile Edge Computing*. **IEEE Transactions on Mobile Computing, 25**(5). DOI: 10.1109/TMC.2025.3636100.

## TL;DR

FT-DSAC schedules DAG tasks with primary and backup replicas on heterogeneous MEC servers and relay paths. Action masking and fault-aware constraints are combined with discrete Soft Actor-Critic and centralized training to improve deadline success under server and relay failures.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Users submit DAG-structured applications to heterogeneous MEC subnets whose edge servers and relay devices can fail. Each task $n_i$ has a primary replica $n_i^P$ and a backup replica $n_i^B$ (primary-backup model); the backup runs only after the primary fails, and the actual finish time is $aft(n_i)=\min(ft(n_i^P),ft(n_i^B))$ in (16).

**Problem & objective**: Problem (19) maximizes the deadline-meeting ratio $\max_{x_i^{m,l}}\lvert N_{ddl}\rvert/N$, where $N_{ddl}=\{n_i\mid aft(n_i)\le sd(n_i)\}$ in (18); the paper also targets low long-term average delay, evaluated as WAET.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Replica placement | $x_{i,Y}^{m,l}$ | binary, $Y\in\{P,B\}$ | Whether replica $Y$ of task $n_i$ runs on edge server $l$ of subnet $sub_m$ |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (8) | Model rule: backup starts no earlier than primary, $st(n_i^B)\ge st(n_i^P)$ |
| C1 (9) | Primary waits for predecessor primaries: $st(n_i^P)\ge\max_k\{ft(n_k^P)+TD_{i,P}^{k,P}\}$ |
| C2 (10) | Primary waits for predecessor backups (rejected in favor of C3 because it adds delay) |
| C3 (11) | Primary does not wait for predecessor backups: $st(n_i^P)<\max_k\{ft(n_k^B)+TD_{i,P}^{k,B}\}$ |
| C4 (12) | Primary and backup in different subnets: $sub_i^B\ne sub_i^P$ |
| C5 (13) | Backup not in a predecessor primary's subnet: $sub_i^B\ne sub_k^P$ |
| C6 (14) | Backup waits for predecessor backups: $st(n_i^B)\ge\max_k\{ft(n_k^B)+TD_{i,B}^{k,B}\}$ |
| C7 (17) | Server assignment count rule for $x_{i,Y}^{m,l}$ as printed in the parse; check the published paper |

**Algorithm**: FT-DSAC models scheduling as a multi-agent MDP, masks actions that violate the fault-tolerance constraints, filters trajectories, and trains discrete Soft Actor-Critic agents with twin critics and a soft value target under centralized training with value decomposition and decentralized execution (CTDE).

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Long et al. [x] addressed fault-tolerant DAG task offloading in heterogeneous MEC networks. Each task receives primary and backup placements with subnet-separation and precedence constraints, and the objective targets deadline-aware task success while the reward favors earlier completion. FT-DSAC combines action masking and trajectory filtering with discrete Soft Actor-Critic under centralized training and decentralized execution. Experiments on synthetic and Montage, CyberShake, Epigenomics, and Inspiral workflows report 6% to 19% higher task-success reliability and 9% to 27% lower latency than FT-DSAC-Soft, FECW, TPTO, and O2O-DRL. Replica overhead and scaling to larger real business or language-model workflows remain open issues.

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
