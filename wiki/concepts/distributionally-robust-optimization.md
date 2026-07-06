---
type: concept
title: "Distributionally Robust Optimization (DRO)"
tags: [optimization, robust, uncertainty, csi, chance-constraint]
related:
  - "[[chance-constraint]]"
  - "[[conditional-value-at-risk]]"
  - "[[csi-estimation-error]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[jia-2026-dro-lawn-trajectory]]"
created: 2026-05-29
updated: 2026-07-06
---

# Distributionally Robust Optimization (DRO)

An optimization paradigm for problems with uncertain parameters where you know **some** distributional information (e.g. mean, variance, support, or empirical samples) but **not** the exact distribution. DRO solves the worst-case problem over an **ambiguity set** $\mathcal{P}$ of plausible distributions:

$$\min_x \max_{\mathbb{P} \in \mathcal{P}} \mathbb{E}_\mathbb{P}[f(x, \xi)]$$

Two common ambiguity-set families:

- **Moment-based** — all distributions matching a given mean and variance (used in [[jia-2025-dro-uav-hap-mec]]).
- **Wasserstein-based** — all distributions within Wasserstein distance $\epsilon$ of an empirical distribution.
- **Metric-ball ambiguity sets** around a reference task-size distribution, such as L1, L-infinity, and Fortet-Mourier balls (used in [[jia-2026-dro-lawn-trajectory]]).

DRO trades higher expected cost (the worst case is generally pessimistic) for **distribution-free guarantees**. Useful when CSI errors don't follow a clean parametric model, when historical data is sparse, or when adversarial perturbations matter. The moment-based form is often reformulable into [[conditional-value-at-risk|CVaR]] constraints, which then become tractable SOCP / SDP problems.

Sits on the wiki's **classical-solver** axis, complementary to the DRL papers that handle uncertainty by training on noisy environments. In the corpus, DRO appears both for CSI-error robustness in UAV-HAP MEC ([[jia-2025-dro-uav-hap-mec]]) and task-size-distribution robustness with trajectory control in low-altitude wireless networks ([[jia-2026-dro-lawn-trajectory]]).
