---
type: concept
title: "Non-Overlapping Coverage-Gain Greedy Selection"
tags: [greedy-algorithm, set-cover, spatiotemporal-coverage, deployment, emergency-response]
related:
  - "[[xia-2026-ubt-emergency-response]]"
  - "[[uav-bus-taxi-emergency-response]]"
  - "[[generalized-assignment-problem]]"
created: 2026-07-13
updated: 2026-07-13
---

# Non-Overlapping Coverage-Gain Greedy Selection

Non-overlapping coverage-gain greedy selection repeatedly chooses the candidate that contributes the largest utility over currently uncovered space-time cells. After each choice, covered cells are removed from later marginal-gain calculations, limiting redundant routes or facilities under a selection budget.

[[xia-2026-ubt-emergency-response]] applies NOCG-Greedy to bus routes carrying UAVs. Each cell's utility already combines delay, hovering duration, and taxi cost; the paper states `O(Kmn)` time but gives no approximation guarantee for its continuous utility objective.
