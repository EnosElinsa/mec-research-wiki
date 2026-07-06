---
type: concept
title: "Beta-Policy DRL"
tags: [drl, policy-gradient, bounded-action, exploration]
related:
  - "[[mappo]]"
  - "[[ppo]]"
  - "[[hybrid-action-representation]]"
  - "[[li-2024-robust-bmappo-multiuav-mec]]"
  - "[[zhu-2026-hab-mappo-target-search]]"
created: 2026-05-31
updated: 2026-07-07
---

# Beta-Policy DRL

In policy-gradient DRL the actor network's stochastic policy is usually a **Gaussian** distribution, whose support is unbounded. When actions have hard lower/upper limits (power, offloading ratio, position), Gaussian samples must be clipped, creating **boundary effects** and biased gradients. Replacing the Gaussian with a **Beta distribution** — which has bounded support on [0, 1] (rescaled to the action range) — removes the bias, matches double-bounded actions naturally, and tends to explore more uniformly early in training because the Beta density can place more mass near the boundaries.

## In this wiki

- [[li-2024-robust-bmappo-multiuav-mec]] uses a Beta-distribution actor output on top of [[mappo]] (b-MAPPO) for robust multi-UAV-MEC offloading, reporting higher reward and faster convergence than Gaussian Pure-MAPPO and MADDPG. It is a refinement of the [[ppo]]/[[mappo]] family relevant whenever continuous actions are bounded.
- [[zhu-2026-hab-mappo-target-search]] uses Beta-policy sampling for bounded continuous UAV search actions, avoiding the truncation bias that appears when Gaussian samples exceed action bounds.
