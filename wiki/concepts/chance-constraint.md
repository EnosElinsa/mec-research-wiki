---
type: concept
title: "Chance Constraint"
tags: [optimization, robust, probability, qos]
related:
  - "[[distributionally-robust-optimization]]"
  - "[[conditional-value-at-risk]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# Chance Constraint

A constraint of the form $\Pr(g(x, \xi) \leq 0) \geq 1 - \epsilon$, where $\xi$ is a random parameter. Captures soft-QoS requirements like "latency must meet the deadline at least 95% of the time" — useful when occasional violations are tolerable but frequent ones aren't.

Chance constraints are typically non-convex even when $g$ is linear. Three workhorse approximations:

- **Bonferroni / scenario approximation** — replace by a finite collection of sampled deterministic constraints.
- **CVaR upper bound** — replace by [[conditional-value-at-risk|CVaR]]_$\epsilon$($g$) $\leq 0$, which is conservative but convex.
- **Distributionally robust** — replace by $\sup_{\mathbb{P} \in \mathcal{P}} \Pr_\mathbb{P}(g > 0) \leq \epsilon$. See [[distributionally-robust-optimization]].

Used in [[jia-2025-dro-uav-hap-mec]] for the latency requirement under uncertain CSI. The DRO + CVaR combination yields a tractable second-order cone program.
