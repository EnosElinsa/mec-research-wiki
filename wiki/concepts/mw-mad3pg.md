---
type: concept
title: "Meta-Learning Weighted Multi-Agent Deep Deterministic Policy Gradient"
tags: [multi-agent-reinforcement-learning, meta-learning, maddpg, fairness, uav-enabled-its]
related:
  - "[[betalo-2026-meta-uav-scheduling]]"
  - "[[maddpg]]"
  - "[[meta-deep-reinforcement-learning]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[jains-fairness-index]]"
created: 2026-07-13
updated: 2026-07-13
---

# Meta-Learning Weighted Multi-Agent Deep Deterministic Policy Gradient

MW-MAD3PG is the fairness-aware meta-learning controller proposed in [[betalo-2026-meta-uav-scheduling]]. It combines deterministic multi-agent actor-critic updates with MAML-style task adaptation so UAV policies can adjust to different traffic densities, sensor distributions, energy limits, and channel conditions with a small number of gradient steps.

The method retains the local-actor/coordinated-critic structure of [[maddpg]], adds local and shared replay pathways, and injects [[jains-fairness-index|Jain-index]] deviation into rewards and meta-gradients. Its actions jointly cover movement, sensor selection, and communication resources.

The name should be treated as paper-specific. The parse alternates between MW-MAD3PG and MW-MADDPG, and its sharing descriptions go beyond a strict communication-free [[centralized-training-decentralized-execution|CTDE]] execution model. Reported gains are simulation results, not a general convergence or transfer guarantee.
