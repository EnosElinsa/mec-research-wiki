---
type: source
title: "Task-Driven Priority-Aware Computation Offloading Using Deep Reinforcement Learning"
authors: ["Hao Hao", "Changqiao Xu", "Wei Zhang", "Shujie Yang", "Gabriel-Miro Muntean"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3564356"
venue: "IEEE Transactions on Wireless Communications"
modeling_card: required
tags: [source, mec, computation-offloading, drl, priority, event-driven, dependence-aware, latent-space]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[event-driven-vs-slot-driven-offloading]]"
  - "[[task-priority-in-mec]]"
created: 2026-05-28
updated: 2026-07-16
---

# Task-Driven Priority-Aware Computation Offloading Using Deep Reinforcement Learning

## Citation

Hao, H., Xu, C., Zhang, W., Yang, S., & Muntean, G.-M. (2025). *Task-Driven Priority-Aware Computation Offloading Using Deep Reinforcement Learning*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3564356.

## TL;DR

Two clean ideas:

1. **Task-driven, not slot-driven.** The system advances time when a *task* arrives, not when a fixed slot expires. This eliminates the per-decision waiting delay (typically 10–100 ms aligned with the wireless coherence time) that slot-driven schedulers incur.
2. **Priority-aware utility.** A per-task priority utility function $u(\text{priority}, \text{delay}, \text{energy})$ captures that some tasks (control, navigation) are catastrophic to drop while others (video stream) merely degrade UX. The optimization objective ("system gain") combines delay, energy, *and* priority.

The DRL angle: the action space is **hybrid** (binary offload decision per task + continuous resource fraction per task) and the number of pending tasks varies. The paper handles this with a **dependence-aware latent space** that encodes task-task dependencies (e.g., DAG structure of microservices) into a fixed-size representation independent of task count, sidestepping the *output-neuron-count-grows-with-tasks* scalability problem common to vanilla DRL offloading agents.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple IoT devices generate high- and low-priority tasks in a cloud-edge-end system with several base-station edge servers and one remote cloud. Each indivisible task triggers a decision at its arrival time and is processed locally, at one edge server, or in the cloud; wireless transmission delay is modeled per destination, but no named multiple-access scheme or fading distribution is specified.

**Problem & objective**: Problem (22) maximizes long-term average priority-aware system gain, $\max_{i_k,p_{m_k}(k)}\lim_{K\to\infty}\frac1K\sum_{k=1}^{K}F(k)$, where $F(k)=w_1U(k)-w_2E(k)$ combines deadline-sensitive utility and device energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Processing destination | $i_k$ | integer, $i_k\in\{0,1,\ldots,N,N+1\}$ | Local device, one of $N$ edge servers, or cloud selected for task $k$ |
| Device transmit power | $p_{m_k}(k)$ | continuous, $0\leq p_{m_k}(k)\leq P_{m_k}^{\max}$ | Uplink power used by the task-generating device |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 22b | Each device transmit power remains between zero and its maximum |
| 22c | Exactly one admissible local, edge, or cloud destination is selected for task $k$ |
| Eqs. (6)-(7) | Local queue evolution, delay, and energy follow the device-computing model |
| Eqs. (12)-(13), (16)-(17) | Edge and cloud transmission, queueing, computation delay, and device-energy relations hold |

**Algorithm**: Trigger an MDP transition whenever a task arrives; build the state from task attributes, local and edge queue delays, link delays, and computing capacities; encode the discrete destination with a learned embedding and the continuous power with a conditional latent representation; pretrain and update the representation from replay; optimize the latent actor with TD3 twin critics and target networks; decode one destination-power action per task and deploy the scheduler independently at each device.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hao et al. [x] studied task-driven priority-aware computation offloading in a collaborative cloud-edge-end system. They formulated a long-term average system-gain problem over a discrete local, edge, or cloud destination and continuous device transmit power, with priority-sensitive delay utility and energy cost. Their TPO method triggers decisions at task arrivals, represents the hybrid action in a learned latent space, and trains the latent policy with TD3 using queue, task, link, and computing state. Simulation and Kubernetes-based testbed results reported the highest system gain, the lowest overall task and waiting delays, and the highest high-priority completion rate among the evaluated approaches.

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
