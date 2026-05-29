---
type: concept
title: "Intra-Swarm Task Delegation"
tags: [uav-swarm, offloading, cooperation, scheduling]
related:
  - "[[task-offloading]]"
  - "[[task-migration]]"
  - "[[dynamic-uav-clustering]]"
  - "[[load-balancing-uav-mec]]"
  - "[[li-2025-stochastic-game-uav-swarm]]"
created: 2026-05-29
updated: 2026-05-29
---

# Intra-Swarm Task Delegation

Within a UAV swarm, a **follower → leader** (or peer) handoff of a task that the follower cannot process locally — e.g. because it lacks the required application/storage or compute. It is a within-swarm cooperation primitive distinct from generic [[task-offloading]] (device → server) and from [[task-migration]] (moving an in-progress/queued task between servers for load/mobility reasons).

In the wiki, [[li-2025-stochastic-game-uav-swarm]] models delegation as one of its five stochastic games (TDSG): a follower delegates to its leader when local processing is infeasible, coupled with [[dynamic-uav-clustering]] and application placement. It is a fine-grained contributor to [[load-balancing-uav-mec]] inside leader/follower swarms.
