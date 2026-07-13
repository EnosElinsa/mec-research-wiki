---
type: concept
title: "Penalty Dual Decomposition (PDD)"
tags: [optimization, non-convex, augmented-lagrangian, mixed-integer, classical-solver]
related:
  - "[[zhang-2026-irs-uav-covert-fbl]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[two-stage-decomposition]]"
  - "[[hu-2019-pdd-uav-mec-offloading]]"
  - "[[zhan-2026-gatd3qn-dependent-offloading]]"
  - "[[song-2026-thz-multiuav-mec]]"
created: 2026-05-31
updated: 2026-07-07
---

# Penalty Dual Decomposition (PDD)

A solver framework for non-convex problems with **coupling (equality) constraints**, useful when a problem mixes discrete binary variables with continuous ones. The recipe:

1. **Reformulate** discrete/coupling constraints as a set of **equality constraints** by introducing auxiliary variables.
2. **Dualize + penalize** those equalities into the objective as **augmented-Lagrangian (AL)** terms.
3. Solve with a **two-layer iteration**: the inner loop optimizes the AL problem (e.g. via a concave-convex procedure, CCCP), and the outer loop updates the AL multipliers and the penalty factor.

PDD converges to a KKT/stationary point of the original non-convex problem under mild conditions. It is a counterpart to the [[alternating-optimization-sdr-sca|AO+SDR+SCA]] pipeline — both attack non-convex coupled problems, but PDD specifically handles equality-constraint coupling and binary-to-equality conversion.

In the wiki, [[hu-2019-pdd-uav-mec-offloading]] uses PDD (inner CCCP, outer multiplier/penalty update) to jointly optimize UAV trajectory, per-user offloading ratio, and binary user scheduling for min-max-delay UAV-MEC, plus a lower-complexity l0-norm variant. [[zhan-2026-gatd3qn-dependent-offloading]] uses penalty dual decomposition inside its JSPO placement/association stage before graph-attention D3QN handles dependent-task offloading. [[song-2026-thz-multiuav-mec]] uses a PDD double loop for THz multi-UAV relay MEC, with relay selection, power control, UAV deployment, and user-resource association in the inner loop.
