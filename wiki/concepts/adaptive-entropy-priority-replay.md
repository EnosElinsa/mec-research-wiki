---
type: concept
title: Adaptive Entropy-Priority (AEP) Experience Replay
tags: [drl, replay-buffer, exploration]
related:
  - "[[peng-2025-drudm-cfg]]"
created: 2026-05-28
updated: 2026-05-28
---

# Adaptive Entropy-Priority (AEP) Experience Replay

A replay-buffer prioritization scheme introduced in [[peng-2025-drudm-cfg]] that combines two signals:

1. **TD-error magnitude** — classical prioritized experience replay (Schaul et al., 2016) — biases sampling toward transitions where the value estimate is most wrong.
2. **Policy entropy at the source state** — biases sampling toward states where the policy is currently undecided, accelerating exploration in regions of the state space where the agent has not yet committed.

Combining the two avoids two failure modes:

- TD-error-only prioritization can over-exploit a single high-error trajectory.
- Entropy-only prioritization treats all uncertain states equally, even those that don't carry useful learning signal.

## Why MA-DRL needs this

In multi-agent post-disaster scenarios, the joint state space is sparse and non-stationary (peer agents are still learning). Vanilla uniform replay wastes a lot of gradient capacity on irrelevant transitions; pure prioritized replay can fixate on adversarial pockets. AEP is the reported sweet spot.

## Caveats

- Two more hyperparameters (entropy weight, TD-error weight) on top of standard PER's $\alpha, \beta$.
- The entropy term is meaningful only for stochastic policies (SAC, MASAC, A3C, PPO). DDPG / MADDPG would need surrogate uncertainty estimates.
