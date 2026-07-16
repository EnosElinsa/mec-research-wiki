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
  - "[[safety-and-robustness-mechanisms-in-mec]]"
  - "[[discrete-continuous-two-stage-decomposition]]"
  - "[[jia-2026-hierarchical-uav-swarms]]"
  - "[[hierarchical-uav-swarm]]"
created: 2026-05-29
updated: 2026-07-16
modeling_card: required
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

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ground users with indivisible tasks are assigned to quasi-stationary UAV MEC servers, with an HAP relaying tasks that exceed UAV capacity or latency feasibility under uncertain G2U CSI.

**Problem & objective**: Jointly choose UAV deployment, user association, HAP forwarding, and CPU allocations to minimize aerial-platform energy, $\min_{\mathbf v,\boldsymbol\delta,\boldsymbol\lambda,\mathbf f}\sum_nE_n^{\mathrm{total}}+E_h^{\mathrm{total}}$, subject to robust latency chance constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UAV deployment | $\mathbf v_n$ | continuous 2-D positions | Horizontal location of UAV $n$ |
| GU-UAV association | $\delta_m^n$ | binary | Connect ground user $m$ to UAV $n$ |
| HAP forwarding | $\lambda_m^n$ | binary | Relay task $m$ from UAV $n$ to the HAP |
| CPU allocation | $f_m$ | nonnegative continuous | Processing frequency assigned to task $m$ |
| Task-size distribution | $\mathbb P_m$ | probability distribution in ambiguity set | Uncertain G2U task or CSI state used by the robust constraint |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | The probability of each task meeting its latency target is at least $\alpha_m$ under the distributional ambiguity set |
| C2 | Forwarding requires association, $\lambda_m^n\leq\delta_m^n$, and each user connects to one UAV |
| C3 | UAV and HAP energy totals stay below their capacity budgets |
| C4 | UAV deployment remains inside the horizontal operating area |
| C5 | Association, forwarding, and CPU variables obey their binary or nonnegative domains and server capacities |

**Algorithm**: Deploy UAVs with weighted K-means, reformulate the chance constraint with a moment-based DRO and CVaR mechanism, solve continuous allocation by primal decomposition and CVX, and optimize binary forwarding with BWOA.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Jia et al. [x] developed a two-layer UAV and HAP MEC model that minimizes platform energy when G2U channel errors have known moments but unknown distributions. The optimization jointly selects weighted UAV deployment, binary GU association and HAP forwarding, and CPU allocation under distributionally robust latency, energy, coverage, and capacity constraints. Their pipeline uses weighted K-means, a CVaR reformulation of the chance constraint, primal decomposition with CVX for continuous resources, and Binary Whale Optimization for forwarding decisions. In simulations, BWOA remains close to exhaustive-search optimum with lower time complexity, while the weighted deployment serves more users and consumes less energy than random deployment and the CVaR design remains near the ideal-CSI results.

## Why this matters

The wiki's first **distributionally robust** optimization paper. Previous MEC papers in the corpus either:

- Ignore CSI uncertainty (most),
- Assume Gaussian errors (a few),
- Use DRL to implicitly handle drift ([[liu-2026-jppo-en-convntm]], [[zhang-2025-mcma-task-migration]]).

DRO fits a different niche: when you have **historical statistics but not a distribution**, and you want **provable** robustness. Worth comparing with the **maritime CSI side-step** in [[wang-2026-aerial-marine-msar]] (use known shipping routes to look up CSI).

## Method highlights

- **Uncertainty set 𝒫.** All distributions ℙ with E_ℙ(Δ_m) = μ_m, D_ℙ(Δ_m) = σ_m². Calibrated from historical CSI residuals.
- **CVaR reformulation.** A standard trick: for moment-based 𝒫, the worst-case tail probability equals a deterministic SOCP constraint involving μ and σ.
- **BWOA.** Whale optimization algorithm adapted to binary search via a penalty-augmented fitness and sigmoid-style position switching. Evaluated against the exhaustive-search optimum, a greedy offloading algorithm, and simulated annealing (SAA): near-optimal energy at much lower time complexity than greedy/SAA as the network scales (Fig. 4).

## Findings

- Under CSI estimation errors, the robust design consumes more energy than the ideal-CSI (perfect-CSI) case, because the MEC servers allocate extra computing resources to absorb the environmental disturbances (Fig. 7, qualitative; no fixed percentage is given in the parse → the specific margin is `not in parse`).
- The WKD deployment consumes less energy than a random-deploy-and-random-connect (R&R) baseline at the same number of served GUs, and accommodates more GUs while avoiding UAV over-/under-utilization (Fig. 6).
- Evaluated at small scales — 30 GUs / 6 UAVs in a 1 km × 1 km area for the WKD clustering (Fig. 3), and M (GUs) = 10 with N (UAVs) = 2–5 for the algorithm/scale studies (Figs. 4–5); HAP task capacity H = 10. Larger "50 UAVs / 200 users" / commodity-hardware claims are `not in parse`.

## Limitations

- Quasi-stationary assumption: UAVs hover after deployment. No trajectory optimization within a slot.
- HAP is treated as a single shared compute pool — no contention model.
- Moment-based DRO is conservative; Wasserstein-DRO would be tighter but harder. Out of scope here.

## Cross-link with related sources

- **Robustness family.** Currently the wiki's only DRO entry; mapped against the corpus's other safety/robustness mechanisms in [[safety-and-robustness-mechanisms-in-mec]], and pairs naturally with the perfect-CSI assumptions in [[hsu-2025-drl-hues-hap-noma]] and [[benaya-2025-aerial-isac-haps]].
- **Aerial-MEC architecture.** Two-layer UAV+HAP, same as [[peng-2025-drudm-cfg]], [[nabi-2025-jour-hierarchical-aerial]], [[bao-2025-ddpg-video-offloading]].
- **Solver lineage.** Convex (SOCP) + metaheuristic (BWOA) + decomposition — sits closer to [[wang-2026-aerial-marine-msar]] and [[liu-2025-haps-uav-maritime-iot]] than to the DRL papers.

## Raw artifacts

- `raw/sources/Distributionally Robust Optimization for Aerial Multi-Access Edge Computing via Cooperation of UAVs/full.md`
