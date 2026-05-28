---
type: source
title: "Task-Driven Priority-Aware Computation Offloading Using Deep Reinforcement Learning"
authors: ["Hao Hao", "Changqiao Xu", "Wei Zhang", "Shujie Yang", "Gabriel-Miro Muntean"]
year: 2025
url: ""
venue: ""
tags: [mec, computation-offloading, drl, priority, event-driven, dependence-aware, latent-space]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[event-driven-vs-slot-driven-offloading]]"
  - "[[task-priority-in-mec]]"
created: 2026-05-28
updated: 2026-05-28
---

# Task-Driven Priority-Aware Computation Offloading Using Deep Reinforcement Learning

## Citation

Hao, H., Xu, C., Zhang, W., Yang, S., & Muntean, G.-M. (2025). *Task-Driven Priority-Aware Computation Offloading Using Deep Reinforcement Learning*.

## TL;DR

Two clean ideas:

1. **Task-driven, not slot-driven.** The system advances time when a *task* arrives, not when a fixed slot expires. This eliminates the per-decision waiting delay (typically 10–100 ms aligned with the wireless coherence time) that slot-driven schedulers incur.
2. **Priority-aware utility.** A per-task priority utility function $u(\text{priority}, \text{delay}, \text{energy})$ captures that some tasks (control, navigation) are catastrophic to drop while others (video stream) merely degrade UX. The optimization objective ("system gain") combines delay, energy, *and* priority.

The DRL angle: the action space is **hybrid** (binary offload decision per task + continuous resource fraction per task) and the number of pending tasks varies. The paper handles this with a **dependence-aware latent space** that encodes task-task dependencies (e.g., DAG structure of microservices) into a fixed-size representation independent of task count, sidestepping the *output-neuron-count-grows-with-tasks* scalability problem common to vanilla DRL offloading agents.

## Problem framing

- **System time evolution:** task-arrival-driven (event-based).
- **Decision per task:** offload or local; if offload, continuous resource fraction.
- **Objective:** maximize cumulative system gain
$$
G = \sum_i u_i(\text{priority}_i, T_i, E_i)
$$

## Method

- **MDP** formulation (single agent, single decision point per task arrival).
- **Hybrid action handling** via the dependence-aware latent space — projects the variable-size pending-task list into a fixed-dim representation. The DRL agent then outputs decisions in this latent space, which are decoded back into per-task actions.
- Likely uses an off-policy method (DDPG/SAC) on the continuous side and a Q-style head on the discrete side; specifics in the algorithm section.

## Findings

- Beats slot-driven baselines on average task delay (no decision waiting) and on critical-task completion rate (priority utility steers decisions away from missed deadlines on important tasks).
- Scales sub-linearly with task count thanks to the latent-space architecture, where vanilla DRL would scale linearly.

## Limitations / future work

- Single-server / centralized MDP — multi-server / multi-agent extension is open.
- Priority is treated as a static input; learned-priority models (where priority is inferred from task content) are deferred.
- Dependence structure is given; learning the dependence graph from observations is an open direction.

## Cross-link with related sources

- Same **priority / urgency** thread as [[peng-2025-drudm-cfg]]'s DRUDM (which combined urgency with distance and resource).
- Same **hybrid-action DRL** thread as [[liu-2026-jppo-en-convntm]]'s [[j-ppo]], but uses a different mechanism — latent space rather than dual-head probability ratio.

## Raw artifacts

- `raw/sources/Task-Driven_Priority-Aware_Computation_Offloading_Using_Deep_Reinforcement_Learning/full.md`
