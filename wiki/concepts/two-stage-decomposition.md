---
type: concept
title: "Two-Stage Decomposition"
tags: [optimization, decomposition, hybrid-action, classical-solver]
related:
  - "[[matching-theory-for-resource-allocation]]"
  - "[[hybrid-action-decision-making]]"
  - "[[wang-2026-aerial-marine-msar]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
created: 2026-05-29
updated: 2026-05-29
---

# Two-Stage Decomposition

A common solver pattern for joint-offloading-plus-resource-allocation problems: peel the problem into a **discrete stage** (which user goes to which server, which task goes where) and a **continuous stage** (transmit power, CPU allocation, trajectory). Solve each with a method tailored to its structure:

- Discrete stage: matching theory, integer programming, metaheuristics.
- Continuous stage: convex optimization, gradient descent, or DRL.

The trade-off vs joint optimization is loss of optimality — the boundary between stages is fixed before the second stage runs, so the continuous stage cannot push back against the discrete decision. In practice the joint optimum is hard to compute and the two-stage approximation is good enough.

Examples in the wiki:

- [[wang-2026-aerial-marine-msar]] — Stage I many-to-one matching (server selection); Stage II quasi-convex + PGD + convex.
- [[nabi-2025-jour-hierarchical-aerial]] — Stage I Gale-Shapley matching (GU-UAV association); Stage II SAC + PER (continuous offloading + allocation).
- [[jia-2025-dro-uav-hap-mec]] — primal decomposition: BWOA for binary, CVX for continuous.

Compare with the **joint hybrid-action** approach of [[liu-2026-jppo-en-convntm|j-PPO]] and [[ma-2025-pdqn-vehicular-mec|P-DQN]], which solve both at once via a hybrid policy.
