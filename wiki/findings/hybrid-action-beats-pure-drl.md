---
type: finding
title: Hybrid-action j-PPO outperforms continuous- or discrete-only DRL in UAV-MEC
source: "[[liu-2026-jppo-en-convntm]]"
confidence: medium
replicated: null
tags: [drl, comparison, action-space]
related:
  - "[[j-ppo]]"
  - "[[hybrid-action-decision-making]]"
  - "[[ddpg-vs-jppo]]"
created: 2026-05-28
updated: 2026-05-28
---

# Hybrid-action j-PPO outperforms continuous- or discrete-only DRL in UAV-MEC

In [[liu-2026-jppo-en-convntm]] Fig. 6, `j-PPO+EN-ConvNTM` is compared against four mainstream DRL algorithms on the [[equilibrium-efficiency-metric]]: **DDPG**, **A2C**, **TD3**, and **DQN**. Result ordering reported by the authors:

```
j-PPO+EN-ConvNTM  >  A2C  >  {DDPG, TD3, DQN}  (with severe degradation)
```

## Why DDPG / TD3 / DQN struggle

- DDPG and TD3 only emit continuous actions. They can plan UAV trajectories but the offloading-ratio + charging-indicator decisions have to be folded in indirectly (e.g. by thresholding a continuous output), which loses gradient signal on the discrete head.
- DQN only emits discrete actions. UAV trajectories collapse to a small set of discrete moves, hurting both $\psi$ and $\kappa$.
- A2C is the closest competitor because, like PPO, it natively supports either action type — but it lacks PPO's clipped trust region and so destabilizes more easily under [[high-density-mobile-device-scenarios]].

## Why this matters

This is the strongest argument in the paper for a **dedicated hybrid-action loss** rather than retro-fitting an existing DRL algorithm. See [[ddpg-vs-jppo]] for a direct comparison and [[hybrid-action-decision-making]] for the underlying design problem.
