---
type: concept
title: "QCQP + SDR + Probabilistic Mapping"
tags: [optimization, semidefinite-relaxation, binary-decisions, scheduling]
related:
  - "[[alternating-optimization-sdr-sca]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[lyapunov-optimization]]"
  - "[[zhao-2025-traj-offload-cache-migration]]"
created: 2026-05-29
updated: 2026-05-29
---

# QCQP + SDR + Probabilistic Mapping

A three-step recipe for solving a coupled **binary** scheduling decision: (1) recast the binary subproblem as a non-convex **Quadratically Constrained Quadratic Program (QCQP)**; (2) relax it via **semidefinite relaxation (SDR)** into a tractable SDP solved with CVX/MOSEK; (3) recover a feasible binary decision from the (generally fractional) SDP solution through a **normalized probabilistic (randomized) mapping** — sampling/rounding guided by the relaxed values.

In the wiki, [[zhao-2025-traj-offload-cache-migration]] uses this as the per-slot scheduling solver for its mutually-exclusive compute/migrate/cache decision, inside a [[lyapunov-optimization]] + block-coordinate-descent loop. It is a more structured alternative to greedy heuristics for the binary half of an [[mixed-integer-nonlinear-programming|MINLP]], and a relative of the SDR techniques in [[alternating-optimization-sdr-sca]].
