---
type: methodology
title: "The AO + SDR + SCA convex pipeline for non-convex aerial beamforming/resource problems"
tags: [methodology, optimization, convex, isac, beamforming]
related:
  - "[[alternating-optimization-sdr-sca]]"
  - "[[benaya-2025-aerial-isac-haps]]"
  - "[[yao-2025-secure-isac-dual-eavesdropping]]"
  - "[[tang-2024-iscc-uav-feel]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[liu-2022-miso-uav-mec-trajectory]]"
  - "[[isac-sensing-in-aerial-mec]]"
  - "[[qcqp-sdr-probabilistic-mapping]]"
created: 2026-05-30
updated: 2026-05-30
---

# The AO + SDR + SCA convex pipeline

A recurring solver protocol across the wiki's convex-optimization aerial sources — especially the ISAC/secure-beamforming ones. Where the [[drl-simulation-with-pomdp-formulation]] methodology page captures the DRL track's protocol, the [[lyapunov-guided-drl]] page the temporal-decoupling protocol, and the [[discrete-continuous-two-stage-decomposition]] page the mixed-integer split, this page captures the **classical convex track's** dominant template. It generalizes the per-source descriptions in [[benaya-2025-aerial-isac-haps]], [[yao-2025-secure-isac-dual-eavesdropping]], and [[tang-2024-iscc-uav-feel]] (and resembles the older SCA-based [[zhang-2019-uav-iot-comp-comm]] and [[liu-2022-miso-uav-mec-trajectory]]).

## The problem shape it fits

A joint design over **coupled continuous blocks** — typically transmit/receive beamforming matrices, UAV/HAPS trajectory or placement, power, and resource allocation — with a non-convex objective (secrecy rate, sensing SNR, energy) and non-convex constraints (rate, sensing beampattern, QoS). The variables are coupled (beamforming depends on position, position depends on power budget), so a single convex solve is impossible.

## The three-stage protocol

### 1. Alternating Optimization (AO) — break the coupling

Partition the variables into blocks (e.g. {beamforming}, {trajectory/placement}, {power/resource}). Fix all but one block and optimize that block; cycle through the blocks until the objective stops improving. AO turns one hard joint problem into a sequence of smaller subproblems, each (after stages 2–3) convex. Convergence is to a stationary point, not a global optimum — this is the standard caveat.

### 2. Semidefinite Relaxation (SDR) — handle the beamforming block

The beamforming subproblem is typically a quadratically-constrained quadratic program (QCQP) in the beamforming vector, which is non-convex. Lift to the matrix variable $\mathbf{W} = \mathbf{w}\mathbf{w}^H$, drop the rank-1 constraint, and solve the resulting semidefinite program. If the SDP solution isn't rank-1, recover a feasible beamformer via Gaussian randomization or the probabilistic mapping in [[qcqp-sdr-probabilistic-mapping]].

### 3. Successive Convex Approximation (SCA) — handle the remaining non-convex terms

For the trajectory/power blocks with non-convex constraints (e.g. rate differences, fractional SINR), replace the non-convex terms with a convex surrogate (first-order Taylor lower bound) around the current iterate, solve the convexified problem, update the iterate, and repeat. SCA monotonically improves the objective under standard surrogate conditions.

## Why these three compose well

- **AO** isolates blocks so each can use the right tool.
- **SDR** is the right tool for the quadratic beamforming block.
- **SCA** is the right tool for the smooth-but-non-convex trajectory/power blocks.

The combination is the de-facto standard for aerial ISAC/secure-beamforming because the problems always have this structure: a quadratic beamforming part (→ SDR) and a smooth non-convex geometry/power part (→ SCA), coupled (→ AO).

## Where it appears in the corpus

- [[benaya-2025-aerial-isac-haps]] — HAPS full-duplex ISAC + friendly jammer; "AO with SDR + SCA" verbatim.
- [[yao-2025-secure-isac-dual-eavesdropping]] — secure UAV-ISAC; AO + SCA + SDR with the [[qcqp-sdr-probabilistic-mapping]] recovery step.
- [[tang-2024-iscc-uav-feel]] — ISCC for federated edge learning; AO (the paper's BBPO) over deployment + resource blocks.
- Precursors without the ISAC sensing term: [[zhang-2019-uav-iot-comp-comm]] (Lagrangian duality + SCA) and [[liu-2022-miso-uav-mec-trajectory]] (three-stage AO with closed-form inner solutions).

## Limitations

- **Stationary-point, not global.** AO + SCA converge to a local stationary point; initialization matters.
- **SDR can fail to be tight.** When the relaxed SDP solution isn't rank-1, the recovered beamformer is suboptimal; the gap is rarely quantified.
- **No robustness to CSI error by default.** The pipeline assumes accurate CSI; the corpus's robust variants (e.g. [[jia-2025-dro-uav-hap-mec]]'s DRO) sit outside this template. See [[query-when-does-dro-beat-drl-for-csi-uncertainty]].
