---
type: concept
title: Equilibrium Efficiency Metric (Ω)
tags: [metric, evaluation, mec]
related:
  - "[[spatial-equity-index]]"
  - "[[energy-expenditure-coefficient]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-05-28
updated: 2026-05-28
---

# Equilibrium Efficiency Metric (Ω)

The aggregate scoring function used in [[liu-2026-jppo-en-convntm]] to compare UAV-MEC algorithms across multiple objectives at once. Two equivalent forms appear:

$$
\Omega_n = \frac{\psi_n \, f_n}{\kappa_n}  \quad\text{(multiplicative)}
$$

or

$$
\Omega_n = \beta_1 \psi_n + \beta_2 f_n - \beta_3 \kappa_n  \quad\text{(weighted sum)}
$$

where:

- $\psi_n$ is the **data collection coefficient** — fraction of total task volume successfully offloaded
- $f_n$ is the [[spatial-equity-index]] — Jain-style fairness over per-device visit counts
- $\kappa_n$ is the [[energy-expenditure-coefficient]] — energy spent vs energy available

Higher Ω is better (more data, more fairness, less energy). The paper uses the multiplicative form throughout the experiments.

## Why combined into one metric

UAV controllers easily over-fit to a single axis: maximize $\psi$ alone and the UAV camps over the dense cluster, hurting $f$; minimize $\kappa$ alone and the UAV barely flies, hurting $\psi$. Ω forces all three to move together.
