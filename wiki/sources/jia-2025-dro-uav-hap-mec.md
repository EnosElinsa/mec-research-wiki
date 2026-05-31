---
type: source
title: "Distributionally Robust Optimization for Aerial Multi-Access Edge Computing via Cooperation of UAVs and HAPs"
authors: ["Ziye Jia", "Can Cui", "Chao Dong", "Qihui Wu", "Zhuang Ling", "Dusit Niyato", "Zhu Han"]
year: 2025
url: "https://doi.org/10.1109/TMC.2025.3571023"
venue: "IEEE Transactions on Mobile Computing"
tags: [source, aerial-mec, hap, uav, distributionally-robust, cvar, primal-decomposition, bwoa, weighted-kmeans, csi-error]
related:
  - "[[hierarchical-aerial-mec]]"
  - "[[high-altitude-platform-station]]"
  - "[[distributionally-robust-optimization]]"
  - "[[conditional-value-at-risk]]"
  - "[[csi-estimation-error]]"
  - "[[chance-constraint]]"
  - "[[binary-whale-optimization]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[wang-2026-aerial-marine-msar]]"
created: 2026-05-29
updated: 2026-06-01
---

# Distributionally Robust Optimization for Aerial Multi-Access Edge Computing via Cooperation of UAVs and HAPs

## Citation

Jia, Z., Cui, C., Dong, C., Wu, Q., Ling, Z., Niyato, D., & Han, Z. (2025). *Distributionally Robust Optimization for Aerial Multi-Access Edge Computing via Cooperation of UAVs and HAPs*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3571023.

## TL;DR

A two-layer aerial MEC: N UAVs (flexible, low capacity) + 1 HAP (stable, large capacity) serve M ground users in remote areas. The novelty is that **the ground-to-UAV (G2U) channel state is uncertain** — only the mean and variance of CSI estimation errors are known, not their distribution. The authors:

1. Deploy UAVs via a **weighted K-means** algorithm (weights reflect task importance, not just user count).
2. Reformulate the chance constraint on per-task latency using **distributionally robust optimization (DRO)** with a moment-based uncertainty set.
3. Convert the DRO chance constraint to a **conditional value-at-risk (CVaR)** form, yielding a mixed-integer second-order cone program (MISOCP).
4. **Primal-decompose** the MISOCP into (a) a continuous resource-allocation subproblem solved by CVX and (b) a binary task-offloading subproblem solved by a custom **Binary Whale Optimization Algorithm (BWOA)**.

Goal: minimize total energy across UAVs + HAP, subject to the robust latency chance constraint.

## Why this matters

The wiki's first **distributionally robust** optimization paper. Previous MEC papers in the corpus either:

- Ignore CSI uncertainty (most),
- Assume Gaussian errors (a few),
- Use DRL to implicitly handle drift ([[liu-2026-jppo-en-convntm]], [[zhang-2025-mcma-task-migration]]).

DRO fits a different niche: when you have **historical statistics but not a distribution**, and you want **provable** robustness. Worth comparing with the **maritime CSI side-step** in [[wang-2026-aerial-marine-msar]] (use known shipping routes to look up CSI).

## Method highlights

- **Uncertainty set 𝒫.** All distributions ℙ with E_ℙ(Δ_m) = μ_m, D_ℙ(Δ_m) = σ_m². Calibrated from historical CSI residuals.
- **CVaR reformulation.** A standard trick: for moment-based 𝒫, the worst-case tail probability equals a deterministic SOCP constraint involving μ and σ.
- **BWOA.** Whale optimization algorithm adapted to binary search via S-shaped sigmoid mapping. Justified empirically vs greedy and pure GA.

## Findings

- Robust solutions cost ~10–20% more energy than nominal solutions but maintain latency feasibility under realistic CSI errors that break the nominal solutions.
- WKD beats vanilla K-means deployment when tasks have heterogeneous priorities — important for emergency / mission-critical scenarios.
- Primal decomposition + BWOA scales to ~50 UAVs / ~200 users on commodity hardware.

## Limitations

- Quasi-stationary assumption: UAVs hover after deployment. No trajectory optimization within a slot.
- HAP is treated as a single shared compute pool — no contention model.
- Moment-based DRO is conservative; Wasserstein-DRO would be tighter but harder. Out of scope here.

## Cross-link with related sources

- **Robustness family.** Currently the wiki's only DRO entry; pairs naturally with the perfect-CSI assumptions in [[hsu-2025-drl-hues-hap-noma]] and [[benaya-2025-aerial-isac-haps]] for a future "robustness across the corpus" synthesis.
- **Aerial-MEC architecture.** Two-layer UAV+HAP, same as [[peng-2025-drudm-cfg]], [[nabi-2025-jour-hierarchical-aerial]], [[bao-2025-ddpg-video-offloading]].
- **Solver lineage.** Convex (SOCP) + metaheuristic (BWOA) + decomposition — sits closer to [[wang-2026-aerial-marine-msar]] and [[liu-2025-haps-uav-maritime-iot]] than to the DRL papers.

## Raw artifacts

- `raw/sources/Distributionally Robust Optimization for Aerial Multi-Access Edge Computing via Cooperation of UAVs/full.md`
