---
type: concept
title: "Mixed-Integer Non-Linear Programming (MINLP)"
tags: [optimization, formulation, np-hard]
related:
  - "[[two-stage-decomposition]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[qcqp-sdr-probabilistic-mapping]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
  - "[[lee-2026-uav-delivery-time-energy]]"
  - "[[huroon-2026-bd-ris-rsma-uav]]"
  - "[[samir-2022-aoi-altitude-scheduling]]"
created: 2026-05-29
updated: 2026-07-13
---

# Mixed-Integer Non-Linear Programming (MINLP)

The optimization problem class with **both** discrete (integer/binary) and continuous decision variables in a non-linear objective and/or constraints. It is the canonical formulation for joint MEC problems: binary offloading/association/caching decisions coupled with continuous resource (power, bandwidth, CPU frequency, trajectory, phase) variables. MINLPs are generally NP-hard, so the corpus solves them via decomposition rather than exactly.

Recurring solution patterns in the wiki: [[two-stage-decomposition]] (decide the binaries, then optimize the continuous block — e.g. [[wu-2025-iopo-irs-uav-thz-mec]]), [[alternating-optimization-sdr-sca|alternating optimization]] / block coordinate descent, [[qcqp-sdr-probabilistic-mapping|SDR + probabilistic mapping]], and DRL that learns the whole policy. See [[binary-vs-partial-offloading]] for the discrete-decision half.

[[lee-2026-uav-delivery-time-energy]] is a non-MEC logistics example of the same class: binary pickup/drop-off indicators are coupled to continuous 3-D trajectory, variable slot lengths, payload weight, and no-fly-zone constraints.

[[huroon-2026-bd-ris-rsma-uav]] couples discrete BD-RIS cluster assignment to continuous RSMA precoding, common rates, non-diagonal scattering matrices, and UAV trajectories, then separates them through generalized Benders decomposition.
