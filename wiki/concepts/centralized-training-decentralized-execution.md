---
type: concept
title: Centralized Training, Decentralized Execution (CTDE)
tags: [drl, multi-agent, training-paradigm]
related:
  - "[[ma-pomdp]]"
  - "[[masac]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[peng-2025-drudm-cfg]]"
created: 2026-05-28
updated: 2026-05-28
---

# Centralized Training, Decentralized Execution (CTDE)

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

CTDE shows up explicitly in [[zhang-2025-mcma-task-migration]] (server-as-agent for vehicular MEC), [[peng-2025-drudm-cfg]] (UAV-as-agent for post-disaster MEC), and [[qin-2025-bcuav-masac]] (UAV-and-terminal-as-agent for blockchain-MEC). Across these, the *backbone* differs (MADDPG / MASAC / MAPPO) but the CTDE pattern is shared.

## Limitation

Centralized critic input dimension grows with agent count. Beyond ~20 agents you typically need attention-based aggregation, value decomposition, or mean-field approximation to keep the critic tractable.
