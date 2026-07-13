---
type: concept
title: "Mutual Policy Divergence-Driven Exploration"
tags: [multi-agent-reinforcement-learning, exploration, policy-divergence, heterogeneous-agents]
related:
  - "[[zhao-2026-uav-carrier-vcs]]"
  - "[[heterogeneous-agent-rl]]"
  - "[[ppo]]"
  - "[[attentive-memory-integrated-information-exchange]]"
created: 2026-07-14
updated: 2026-07-14
---

# Mutual Policy Divergence-Driven Exploration

An intrinsic MARL objective that combines divergence between different agents' current policies with divergence between one agent's current and previous policies. The first term encourages heterogeneous roles; the second discourages premature behavioral collapse.

[[zhao-2026-uav-carrier-vcs]] estimates conditional Cauchy-Schwarz policy divergence nonparametrically from representation-action trajectories and adds it to clipped PPO training. The balance coefficient is environment-dependent, and the paper supports the method through simulation and ablation rather than a convergence or optimality theorem.
