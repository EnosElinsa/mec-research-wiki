---
type: concept
title: "Closed-Form IRS Phase Alignment"
tags: [intelligent-reflecting-surface, phase-shift, action-space-reduction, beamforming]
related:
  - "[[xie-2026-uav-irs-eppo]]"
  - "[[uav-mounted-ris]]"
  - "[[fixed-point-irs-passive-beamforming]]"
created: 2026-07-13
updated: 2026-07-13
---

# Closed-Form IRS Phase Alignment

An analytical phase rule that aligns per-element geometric path phases so reflected components add coherently at the intended receiver. When platform and user geometry are known, it can remove hundreds of IRS phases from a learned action and leave the policy to control only UAV motion.

In [[xie-2026-uav-irs-eppo]], the rule aligns the LoS components of a UAV-carried IRS channel. The source does not prove global optimality for its full Rician, fairness-weighted, trajectory-coupled objective, so the rule is best understood as structured action-space reduction rather than an exact solution of the original joint problem.
