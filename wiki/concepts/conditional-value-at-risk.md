---
type: concept
title: "Conditional Value-at-Risk (CVaR)"
tags: [optimization, risk-measure, robust, dro]
related:
  - "[[distributionally-robust-optimization]]"
  - "[[chance-constraint]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# Conditional Value-at-Risk (CVaR)

A coherent risk measure: the **expected loss in the worst $\alpha$-fraction** of outcomes. CVaR$_\alpha(X) = \mathbb{E}[X \mid X \geq \text{VaR}_\alpha(X)]$. Unlike VaR (a quantile), CVaR captures *how bad* the tail is, not just where it starts — and it's coherent (subadditive, monotone, etc.).

Why it matters in MEC: a [[chance-constraint]] like $\Pr(\text{latency} \leq T) \geq 1 - \alpha$ is generally non-convex, but its CVaR-relaxation $\text{CVaR}_\alpha(\text{latency} - T) \leq 0$ is convex (under mild conditions) and provides a **safe approximation** — solutions that satisfy the CVaR constraint also satisfy the chance constraint.

Combined with [[distributionally-robust-optimization|DRO]], CVaR provides a tractable reformulation route for moment-based ambiguity sets. [[jia-2025-dro-uav-hap-mec]] uses exactly this stack: moment-based DRO of a chance constraint → CVaR reformulation → MISOCP → primal decomposition.
