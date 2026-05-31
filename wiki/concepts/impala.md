---
type: concept
title: "IMPALA (Importance-Weighted Actor-Learner Architecture)"
tags: [drl, off-policy, distributed, actor-critic]
related:
  - "[[ppo]]"
  - "[[deep-q-network]]"
  - "[[lee-2024-dho-leo-handover]]"
created: 2026-06-01
updated: 2026-06-01
---

# IMPALA (Importance-Weighted Actor-Learner Architecture)

A distributed, off-policy actor-critic DRL algorithm in which many parallel **actors** generate experience asynchronously while a central **learner** updates the policy, with **V-trace** off-policy correction (truncated importance sampling) to fix the policy lag between the behavior policy that produced the data and the target policy being improved. The asynchronous parallelism and importance-sampling correction give high sample efficiency and scalability for large state/action spaces.

In this wiki, [[lee-2024-dho-leo-handover]] trains its DHO LEO-satellite handover protocol with IMPALA, arguing V-trace stability across large state/action spaces makes it preferable to [[deep-q-network|DQN]], A3C, and [[ppo|PPO]] for the handover-decision task.
