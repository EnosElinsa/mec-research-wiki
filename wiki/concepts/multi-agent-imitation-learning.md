---
type: concept
title: "Multi-Agent Imitation Learning"
tags: [multi-agent-learning, imitation-learning, expert-demonstrations, opponent-modeling, adversarial-learning]
related:
  - "[[wang-2023-differentiated-uav-services]]"
  - "[[wang-2025-ctmig-task-migration-uav]]"
  - "[[generative-adversarial-network]]"
  - "[[stochastic-game]]"
  - "[[maddpg]]"
  - "[[centralized-training-decentralized-execution]]"
created: 2026-07-13
updated: 2026-07-13
---

# Multi-Agent Imitation Learning

Multi-agent imitation learning trains several interacting policies from expert trajectories rather than relying only on reward-driven exploration. Because one agent's action changes every other agent's environment, the learner may also model opponents or teammates and match joint action-state occupancy, not just copy isolated actions.

In [[wang-2023-differentiated-uav-services]], full-information oracle owners generate expert actions for a UAV service market. Each learning owner uses a discriminator, opponent-action model, policy, and value network to imitate equilibrium behavior from local observations without exchanging actual opponent policies during execution.

The family overlaps adversarial imitation through [[generative-adversarial-network|GAN-style]] occupancy matching, as used in [[wang-2025-ctmig-task-migration-uav]], but it is not synonymous with [[centralized-training-decentralized-execution]]. The differentiated-service design has no centralized critic for owner policies, yet it retains a globally informed network operator that observes system status, distributes demand information, and estimates preference density.
