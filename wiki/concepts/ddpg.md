---
type: concept
title: "Deep Deterministic Policy Gradient (DDPG)"
tags: [drl, actor-critic, continuous-action, off-policy, replay-buffer]
related:
  - "[[ppo]]"
  - "[[masac]]"
  - "[[ddqn]]"
  - "[[bao-2025-ddpg-video-offloading]]"
  - "[[ye-2026-deeplsc-lae-isac]]"
  - "[[cai-2026-llm-drl-secure-lae-data]]"
  - "[[ddpg-vs-jppo]]"
created: 2026-05-29
updated: 2026-07-07
---

# Deep Deterministic Policy Gradient (DDPG)

An off-policy actor-critic algorithm for continuous control. Combines:

- **Deterministic policy** $\mu_\theta(s)$ — outputs a single action vector instead of a distribution.
- **Q-critic** $Q_\phi(s, a)$ trained with TD-targets bootstrapped from a slow-moving target network.
- **Replay buffer** for sample efficiency.
- **Exploration noise** (typically Ornstein-Uhlenbeck or Gaussian) added to actions during training.

Strengths: sample efficient (off-policy + replay), simple to tune for narrow continuous problems. Weaknesses: known instability (Q-overestimation, sensitive to hyperparameters); often replaced by TD3 or [[masac|SAC]] for harder problems.

In the wiki, [[bao-2025-ddpg-video-offloading]] uses vanilla DDPG for joint offloading-ratio + transcoding-ratio + HAP-resource control — purely continuous, narrow scope, where DDPG fits well. [[ye-2026-deeplsc-lae-isac]] uses a DDPG backbone for continuous GBS beamforming and UAV-trajectory control, adding constrained noise exploration plus episode-level replay for LAE ISAC constraints. [[cai-2026-llm-drl-secure-lae-data]] uses DDPG as one baseline/backbone for LLM-enhanced secure data-collection control. Compare with the hybrid-action [[j-ppo]] in [[liu-2026-jppo-en-convntm]] (see [[ddpg-vs-jppo]]).
