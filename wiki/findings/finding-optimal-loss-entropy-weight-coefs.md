---
type: finding
title: Optimal hyperparameter sweet spot for j-PPO+EN-ConvNTM
source: "[[liu-2026-jppo-en-convntm]]"
confidence: medium
replicated: null
tags: [hyperparameters, drl]
related:
  - "[[j-ppo]]"
  - "[[j-ppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# Optimal hyperparameter sweet spot for j-PPO+EN-ConvNTM

From Table I of [[liu-2026-jppo-en-convntm]] (2 UAVs, 1 charging station, sweep one coefficient at a time, others held at default):

| Coefficient | Best value | Reported Ω at best |
|---|---|---|
| $c_1$ (VF loss weight) | 0.1 | 0.9849 |
| $c_2$ (entropy weight) | 0.01 | 0.9891 |
| $c_3$ (hybrid action weight) | 0.5 | 0.9827 |

## Interpretation

- **$c_1 = 0.1$** balances policy improvement against value-function fit. Larger values dominate the loss and degrade policy learning; smaller values let the value head drift.
- **$c_2 = 0.01$** is enough exploration for the action distribution without flattening it. At $c_2 = 0$ the policy collapses ($\Omega = 0.6178$); at $c_2 = 0.5$ it's too noisy ($\Omega = 0.7904$).
- **$c_3 = 0.5$** gives equal weight to the continuous-action and discrete-action probability ratios. Skewing toward either side sacrifices the other axis (e.g. $c_3 = 0.5 \to 0.9827$ vs $c_3 = 0.7 \to 0.6148$).

## Caveat

These were tuned at $U=2, Z=1$. The authors do not report whether the optimum shifts with fleet size or station density.
