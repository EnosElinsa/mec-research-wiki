---
type: concept
title: "Federated Linear Bandit Learning"
tags: [federated-learning, contextual-bandit, linucb, online-learning, regret]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[qian-2026-federated-bandit-aircomp]]"
  - "[[federated-learning]]"
  - "[[over-the-air-computation]]"
  - "[[regret-minimization-learning]]"
created: 2026-07-13
updated: 2026-07-14
---

# Federated Linear Bandit Learning

Federated linear bandit learning lets distributed clients cooperate on an online contextual decision problem without pooling raw observations. Depending on the formulation, clients may share global structure while retaining heterogeneous local models or estimate a common parameter; upper-confidence-bound actions trade immediate reward against uncertainty, and performance is measured by cumulative regret.

In [[qian-2026-federated-bandit-aircomp]], clients assume one common fixed linear reward parameter and cache its Gram-matrix and reward-vector statistics. Local LinUCB caches synchronize only when a determinant-ratio information-gain trigger fires. The updates are aggregated through [[over-the-air-computation]], so channel noise perturbs the confidence statistics and appears explicitly in the regret guarantee. UAV trajectory, client powers, and receiver normalization are optimized to reduce that aggregation error.

The concept differs from gradient/model averaging in ordinary [[federated-learning]]: the shared object is an online bandit's sufficient statistics, and the central guarantee is regret rather than training loss or test accuracy.

[[aerial-federated-aggregation-design-space]] preserves that guarantee boundary when comparing event-triggered AirComp with gradient- and model-aggregation systems.
