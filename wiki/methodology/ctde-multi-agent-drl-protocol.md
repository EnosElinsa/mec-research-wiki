---
type: methodology
title: "CTDE multi-agent DRL protocol for cooperative MEC control"
tags: [methodology, ctde, multi-agent, drl, actor-critic, mec]
related:
  - "[[centralized-training-decentralized-execution]]"
  - "[[ma-pomdp]]"
  - "[[mappo]]"
  - "[[masac]]"
  - "[[maddpg]]"
  - "[[ctde-actor-critic-backbones-in-mec]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
  - "[[discrete-continuous-two-stage-decomposition]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[kang-2023-mappo-hierarchical-aerial]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[zhang-2025-ssac-mgi-heterogeneous-uav]]"
created: 2026-06-07
updated: 2026-06-07
---

# CTDE multi-agent DRL protocol for cooperative MEC control

A recurring solver protocol across cooperative MEC sources: formulate the environment as a partially observable multi-agent control problem, train with a critic or value function that can see global state and joint actions, then deploy actors that run from local observations. Where [[ctde-actor-critic-backbones-in-mec]] compares the algorithm families, this page captures the engineering protocol: what gets centralized, what stays local, why the split fits MEC, and where the corpus shows its limits.

The pattern is strongest in the sources that state [[centralized-training-decentralized-execution|CTDE]] explicitly: [[zhang-2025-mcma-task-migration]] for vehicular task migration across edge servers, [[peng-2025-drudm-cfg]] for post-disaster HAS-UAV aerial MEC, and [[kang-2023-mappo-hierarchical-aerial]] for UAV-HAP hierarchical aerial computing. [[qin-2025-bcuav-masac]] uses the same multi-agent actor-critic seam inside a Lyapunov-decomposed blockchain UAV-MEC controller, but its parse does not label the training paradigm as CTDE; it is best read as a related MASAC instantiation, not as an explicit CTDE proof point.

## The problem shape it fits

CTDE fits a cooperative MEC problem when all three conditions hold:

- **Agents have local views.** A server sees its covered vehicles in [[zhang-2025-mcma-task-migration]]; a UAV sees local post-disaster coverage and offloading state in [[peng-2025-drudm-cfg]]; a UAV in [[kang-2023-mappo-hierarchical-aerial]] makes GD association, resource-allocation, and task-offloading decisions from local observations.
- **The reward is system-level.** The sources optimize global task latency, completed-task volume, task-completion rate, delay, queueing, or fairness; a purely independent learner would treat the other agents' policy updates as moving environment dynamics.
- **Execution must stay distributed.** The trained policy should run on the UAV or server without requiring a central controller to emit every action online.

This is the [[ma-pomdp]] pattern in operational form: partial observations at the agent edge, global coupling during learning, local execution at deployment.

## The protocol

### Step 1 - choose the agent boundary

The agent is the operational unit that can act locally:

| Source | Agent boundary | Local decisions |
|---|---|---|
| [[zhang-2025-mcma-task-migration]] | MEC server | vehicle-by-vehicle offloading/migration and resource allocation |
| [[peng-2025-drudm-cfg]] | UAV | post-disaster IMD service selection, trajectory, and resource decisions |
| [[kang-2023-mappo-hierarchical-aerial]] | UAV | GD association, spectrum/cache/compute allocation, and UAV-to-HAP offloading ratio |
| [[qin-2025-bcuav-masac]] | UAV and terminal agents | terminal power control and UAV trajectory inside a larger Lyapunov/CVX/DOA decomposition |

The boundary follows deployability. It is not "one neural network for the whole fleet"; it is one local actor per operational unit, with cooperation learned through a centralized training signal.

### Step 2 - centralize only the learning signal

During training, the critic/value side receives global information. [[zhang-2025-mcma-task-migration]] states that each server follows CTDE: additional global states guide cooperative training, while each server later uses local policies for its covered vehicles. [[peng-2025-drudm-cfg]] puts the global critic and shared replay buffer on the HAS; the HAS uses global state and joint action information to evaluate UAV behaviors and update the global critic networks. [[kang-2023-mappo-hierarchical-aerial]] uses a centralized action-value function over global state and all agents' actions.

The actor side remains local: [[zhang-2025-mcma-task-migration]]'s servers act from local observations, [[peng-2025-drudm-cfg]]'s UAV actor networks output local policies, and [[kang-2023-mappo-hierarchical-aerial]] removes the critic at execution so only the trained actor runs online.

### Step 3 - match the backbone to the action space

CTDE is the training pattern, not the algorithm. The backbone changes with the decision variables:

- [[zhang-2025-mcma-task-migration]] uses **MAPPO** for the discrete offloading/migration stage and **MADDPG** for continuous bandwidth and compute allocation; the first-stage offloading decision is concatenated into the second-stage observation.
- [[peng-2025-drudm-cfg]] uses **MASAC** with entropy regularization, DRUDM admission, CFG fairness reward, and adaptive entropy-priority replay.
- [[kang-2023-mappo-hierarchical-aerial]] uses **MAPPO** and adds state normalization plus action masking to avoid invalid actions and speed training.
- [[qin-2025-bcuav-masac]] uses **MASAC** for the non-convex per-slot power-and-trajectory subproblem after [[lyapunov-optimization]] decouples long-term queue/security constraints.

The reusable design rule is: centralize the value estimate when agents are coupled, but choose MAPPO, MADDPG, MASAC, MATD3, or value decomposition according to action-space and stability needs.

## Why the protocol composes well

- **It targets the exact non-stationarity of multi-agent MEC.** A local UAV or server policy changes while its peers change too; the global critic/value function stabilizes learning by seeing more of the joint state-action context than any actor can see at deployment.
- **It preserves online deployability.** The centralized critic is training infrastructure. [[kang-2023-mappo-hierarchical-aerial]] explicitly says the critic is not included during decentralized execution, leaving only actor forward propagation online.
- **It works with decomposition.** CTDE rarely carries the entire optimization alone. [[zhang-2025-mcma-task-migration]] layers CTDE over a discrete-then-continuous split; [[peng-2025-drudm-cfg]] adds DRUDM admission and CFG fairness; [[qin-2025-bcuav-masac]] embeds MASAC beside CVX and DOA after Lyapunov decoupling. This aligns with [[discrete-continuous-two-stage-decomposition]] and the broader [[decomposition-beats-end-to-end-drl-in-mec]] thesis.

## Limits and contrast cases

- **Centralized training can become the bottleneck.** [[peng-2025-drudm-cfg]] notes that more UAVs can increase centralized-training coordination complexity and training overhead, even though decentralized execution keeps each UAV's online decision complexity local.
- **CTDE is not mandatory for every multi-agent MEC source.** [[zhang-2025-ssac-mgi-heterogeneous-uav]] explicitly chooses decentralized training and decentralized execution (DTDE), arguing that this avoids the communication and computation overhead of transmitting and integrating all UAV observations. It is a useful contrast: CTDE buys a stronger cooperative learning signal, while DTDE buys lower training communication and a more scalable independence assumption.
- **The corpus has no dense-fleet attention critic.** Existing CTDE examples use global critics or value functions, but not attention-factorized, mean-field, or graph critics for very large agent counts. The scaling fix remains absent from the curated sources.

## See also

- [[ctde-actor-critic-backbones-in-mec]] - algorithm-family comparison across CTDE backbones.
- [[centralized-training-decentralized-execution]] - concept-level definition.
- [[ma-pomdp]] - the formal problem model CTDE usually solves.
- [[discrete-continuous-two-stage-decomposition]] - the decomposition protocol CTDE often sits inside.
