---
type: concept
title: "Prioritized Experience Replay (PER)"
tags: [drl, replay-buffer, off-policy, sample-efficiency]
related:
  - "[[ddqn]]"
  - "[[masac]]"
  - "[[adaptive-entropy-priority-replay]]"
  - "[[episodic-experience-replay]]"
  - "[[nabi-2025-jour-hierarchical-aerial]]"
created: 2026-05-29
updated: 2026-07-07
---

# Prioritized Experience Replay (PER)

An off-policy DRL technique that samples replay-buffer transitions **proportional to TD error** rather than uniformly. Transitions where the model's Q-prediction is far from the bootstrapped target carry more learning signal, so sampling them more often speeds up convergence.

Mechanics:

- Each stored transition $i$ keeps a priority $p_i = |\delta_i| + \epsilon$ where $\delta_i$ is the TD error.
- Sampling probability $P(i) \propto p_i^\alpha$.
- Importance-sampling weights $w_i = (1/(N \cdot P(i)))^\beta$ correct the bias.

Used in [[nabi-2025-jour-hierarchical-aerial]]'s ESAC algorithm to accelerate the SAC backbone. Related to but distinct from the **adaptive entropy + priority** scheme in [[adaptive-entropy-priority-replay]] used by [[peng-2025-drudm-cfg]], which combines PER with an entropy-aware exploration term. Also contrast [[episodic-experience-replay]], where the replay unit is a complete episode set rather than an individual transition, as in the LAE ISAC controllers [[ye-2026-deeplsc-lae-isac]] and [[ye-2026-meta-deepesc-lae-isac]].

PER is essentially free for off-policy methods (DDPG, SAC, DQN); not useful for on-policy methods like PPO that don't reuse old transitions.
