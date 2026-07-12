---
type: concept
title: MA-POMDP (Multi-Agent Partially Observable MDP)
tags: [drl, multi-agent, theory]
related:
  - "[[pomdp]]"
  - "[[masac]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[chen-2026-maddpg-uav-swarm-antijamming]]"
  - "[[multi-domain-uav-anti-jamming]]"
  - "[[wu-not-in-parse-aoi-sampling-buffering-routing]]"
  - "[[zhou-2026-a2g-madrl-air-ground-vcs]]"
  - "[[le-2026-asynchronous-uav-data-collection]]"
  - "[[asynchronous-qmix]]"
  - "[[wang-2026-wutf-fair-communication]]"
  - "[[wireless-powered-uav-fair-service-control]]"
created: 2026-05-28
updated: 2026-07-12
---

# MA-POMDP (Multi-Agent Partially Observable MDP)

The natural multi-agent generalization of [[pomdp|POMDP]]: $N$ agents, each with its own observation $o_n^i$ and action $a_n^i$, share a global state $s_n$ that none of them sees fully. The global transition depends on the joint action $\mathbf a_n = (a_n^1, \ldots, a_n^N)$.

## Why this framing dominates UAV-MEC papers

- Each UAV sees its own neighborhood, not the full constellation state.
- Joint trajectory + offloading + resource decisions are coupled across UAVs.
- Centralized-training-decentralized-execution paradigms (used by MASAC, MADDPG, etc.) are designed for exactly this setting.

## Common solution patterns

- **Centralized critic, decentralized actors** — critic gets the global view at training time; deployment uses only local observations. Used by [[masac|MASAC]], MADDPG, MAPPO.
- **Communication-augmented agents** — agents exchange compressed observations or attention messages.
- **Mean-field MARL** — replaces the joint action distribution with a sufficient summary (the mean) of peer actions; useful when N is large.

## In this wiki

[[peng-2025-drudm-cfg]] explicitly casts post-disaster offloading as MA-POMDP; [[qin-2025-bcuav-masac]] does the same under the AGIN lens. [[chen-2026-maddpg-uav-swarm-antijamming]] uses the same framing for [[multi-domain-uav-anti-jamming]], where each UAV observes local channel/interference conditions while joint U2U/U2G reliability determines the reward. The single-agent [[pomdp]] page covers the simpler variant used by [[liu-2026-jppo-en-convntm]] (one centralized controller for all UAVs).

[[shi-2025-aoi-energy-replenishment-multiuav]] uses a Dec-POMDP for multi-UAV AoI-aware data collection and energy replenishment, with each UAV making local flight, association, and charging decisions from partial observations while a shared freshness/energy objective couples the team.

[[wu-not-in-parse-aoi-sampling-buffering-routing]] applies the same partial-observation logic inside a leader-follower UAV swarm, where each follower sees only local queue, neighbor, and freshness state. [[zhou-2026-a2g-madrl-air-ground-vcs]] adds a UAV/UGV/PoI crowdsensing version whose [[sequential-multi-agent-policy-generation]] layer makes the joint action order explicit.

[[le-2026-asynchronous-uav-data-collection]] adds a Dec-POSMDP extension: partial observation remains, but action durations vary and decision epochs are agent-specific. [[asynchronous-qmix]] handles the resulting event-driven value decomposition without collapsing it back to a synchronized Dec-POMDP.

[[wang-2026-wutf-fair-communication]] uses the synchronous MA-POMDP form for [[wireless-powered-uav-fair-service-control]]: each actor observes all users and charging towers but omits other UAV positions and batteries, while the training critic receives the global state.
