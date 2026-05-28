---
type: concept
title: Generalized Advantage Estimation (GAE)
tags: [drl, policy-gradient]
related:
  - "[[ppo]]"
  - "[[j-ppo]]"
created: 2026-05-28
updated: 2026-05-28
---

# Generalized Advantage Estimation (GAE)

Schulman et al.'s estimator that smoothly trades bias against variance in advantage computation:

$$
A_n = \sum_{i=0}^{\infty} (\gamma \varsigma)^i \delta_{n+i}, \quad \delta_n = r(s_n) + \gamma V_{\theta_\text{old}}(\mathbf{h}_{n+1}) - V_{\theta_\text{old}}(\mathbf{h}_n)
$$

The hyperparameter $\varsigma$ controls the bias-variance trade-off. Used inside [[ppo]] and [[j-ppo]].
