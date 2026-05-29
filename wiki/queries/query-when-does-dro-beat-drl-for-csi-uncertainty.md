---
type: query
title: When does distributionally robust optimization beat DRL for CSI uncertainty in aerial MEC?
tags: [open-question, robustness, csi, dro, drl]
related:
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[distributionally-robust-optimization]]"
  - "[[conditional-value-at-risk]]"
  - "[[csi-estimation-error]]"
  - "[[wu-2026-terrain-aware-uav-mec]]"
  - "[[wang-2026-aerial-marine-msar]]"
  - "[[drl-vs-evolutionary-vs-classical-solvers]]"
created: 2026-05-30
updated: 2026-05-30
---

# When does DRO beat DRL for CSI uncertainty in aerial MEC?

The corpus now handles channel-state-information (CSI) uncertainty in three structurally different ways, but **never compares them head-to-head**. This query tracks the gap.

## The three approaches in the corpus

1. **Distributionally robust optimization (DRO).** [[jia-2025-dro-uav-hap-mec]] models CSI uncertainty as an ambiguity set and optimizes the worst-case expectation, using [[conditional-value-at-risk|CVaR]] + primal decomposition. Guarantees a robustness margin without assuming a known channel distribution.
2. **Learn the distribution implicitly (DRL).** Most of the DRL track ([[drl-vs-evolutionary-vs-classical-solvers]]) treats CSI variability as part of the environment the agent learns to handle — no explicit robustness guarantee, but adapts online.
3. **Side-step uncertainty via structure.** [[wang-2026-aerial-marine-msar]] exploits known maritime routes; [[wu-2026-terrain-aware-uav-mec]] uses a deterministic terrain-aware geometric channel. Neither models stochastic CSI error at all.

## The open question

Under what conditions does the DRO approach (worst-case guarantee, no online adaptation) outperform a DRL controller (online adaptation, no guarantee) — and vice versa? Candidate determinants:

- **Severity and structure of the uncertainty.** DRO should win when the ambiguity set is well-specified and the cost of a worst-case violation is high (safety-critical). DRL should win when the channel is non-stationary in ways DRO's static ambiguity set can't capture.
- **Online vs offline regime.** DRL needs a training budget and a representative environment; DRO needs only the ambiguity-set specification. In a cold-start deployment, DRO may be the only option.
- **Tolerance for conservatism.** DRO's worst-case objective is conservative; if the realized channel is usually benign, DRO leaves performance on the table that DRL captures.

## What would settle this

- A controlled study running [[jia-2025-dro-uav-hap-mec]]'s DRO formulation and a DRL controller on the **same** UAV-HAP MEC environment under matched CSI-error models, reporting both average performance and worst-case violation rate.
- A hybrid (DRO-regularized DRL) baseline to see whether the two are complementary rather than competing.

No curated source provides this comparison yet; promoting it here so the next robustness-themed source gets slotted against it.
