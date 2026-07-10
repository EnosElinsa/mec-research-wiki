---
type: concept
title: Centralized Training, Decentralized Execution (CTDE)
tags: [drl, multi-agent, training-paradigm]
related:
  - "[[ma-pomdp]]"
  - "[[masac]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[ctde-actor-critic-backbones-in-mec]]"
  - "[[ctde-multi-agent-drl-protocol]]"
  - "[[chen-2026-maddpg-uav-swarm-antijamming]]"
  - "[[gao-2023-uav-mcs-uma]]"
  - "[[qmix]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[ensemble-qmix]]"
  - "[[zhang-2026-ensemble-marl-uav-target-search]]"
created: 2026-05-28
updated: 2026-07-11
---

# Centralized Training, Decentralized Execution (CTDE)

[[zhang-2026-ensemble-marl-uav-target-search]] adds the ensemble QMIX/value-decomposition form of CTDE to the curated corpus. Its [[ensemble-qmix]] controller trains centralized mixing networks but executes per-UAV majority-voted local actions. [[shi-2025-aoi-energy-replenishment-multiuav]] adds the direct [[qmix|QMIX]] and VDN comparison for rechargeable multi-UAV IoT data collection.

A canonical paradigm for cooperative multi-agent DRL:

- **Training time:** a centralized critic has access to all agents' observations and actions, plus any global state. It uses this view to compute stable value estimates.
- **Execution time:** each agent uses only its local observation through a decentralized actor. The centralized critic is discarded.

## Why this works

- Centralized critic eliminates the non-stationarity that plagues independent learners (each agent's policy is changing, so the environment looks non-stationary from any one agent's perspective).
- Decentralized execution stays deployable — no inter-agent communication required at inference.

## Standard backbones

- **MADDPG** — deterministic policies, replay buffer.
- **[[masac|MASAC]]** — stochastic policies + entropy bonus.
- **MAPPO** — on-policy clipped objective.
- **MATD3** — twin-Q critics, delayed updates.
- **Qmix / VDN** — value decomposition for fully cooperative discrete settings.
- **COMA** — counterfactual baseline for credit assignment.

## In this wiki

CTDE shows up explicitly in [[zhang-2025-mcma-task-migration]] (server-as-agent for vehicular MEC), [[peng-2025-drudm-cfg]] (UAV-as-agent for post-disaster MEC), and [[kang-2023-mappo-hierarchical-aerial]] (UAV-as-agent for hierarchical aerial MEC). It also appears in adjacent non-offloading control, including [[chen-2026-maddpg-uav-swarm-antijamming]] for jammed UAV-swarm communications and [[gao-2023-uav-mcs-uma]] for multi-UAV mobile-crowd-sensing coverage/calibration. Across these, the *backbone* differs (MAPPO / MADDPG / MASAC), but the training/execution split is shared. The engineering protocol is expanded in [[ctde-multi-agent-drl-protocol]].

## Limitation

Centralized critic input dimension grows with agent count. Beyond ~20 agents you typically need attention-based aggregation, value decomposition, or mean-field approximation to keep the critic tractable.
