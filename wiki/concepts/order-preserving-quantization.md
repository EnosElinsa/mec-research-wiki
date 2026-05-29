---
type: concept
title: "Order-Preserving Quantization (DROO-style)"
tags: [drl, offloading, action-generation, quantization]
related:
  - "[[binary-vs-partial-offloading]]"
  - "[[two-stage-decomposition]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
created: 2026-05-29
updated: 2026-05-29
---

# Order-Preserving Quantization (DROO-style)

A technique for generating discrete (binary) offloading decisions from a neural network's continuous output, originally from DROO (Huang et al. 2020). A DNN emits a relaxed probability vector/matrix; instead of naive rounding, an **order-preserving** rule generates a small set of `H` diverse binary candidates (ordering entries by distance to a threshold, then flipping in a structured way), evaluates each candidate's true objective, and keeps the best. This avoids enumerating the exponentially many binary decisions while preserving the relative ordering the network learned.

In the wiki, [[wu-2025-iopo-irs-uav-thz-mec]]'s **OPPO** unit extends this to the multi-UAV/multi-user setting (each candidate scored after WOA phase optimization). It shares the DROO lineage with [[zhu-2025-lycnn-drl-wpt-mec]], and is a reusable building block for learned [[binary-vs-partial-offloading|binary offloading]] within a [[two-stage-decomposition]].
