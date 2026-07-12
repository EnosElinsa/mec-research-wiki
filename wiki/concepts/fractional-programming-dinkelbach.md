---
type: concept
title: Fractional Programming and Dinkelbach Transform
tags: [optimization, fractional-programming, theory]
related:
  - "[[lyapunov-optimization]]"
  - "[[zhu-2025-lycnn-drl-wpt-mec]]"
  - "[[xiao-2025-star-ris-bidirectional-uav-mec]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
  - "[[qin-2023-ris-uav-mec-ee]]"
  - "[[zhao-2026-mappo-jscc-aec]]"
  - "[[cui-2026-aris-v2x-icac]]"
  - "[[effective-energy-efficiency]]"
  - "[[zhang-2026-air-ground-covert-jamming]]"
  - "[[zhang-2025-cooperative-anti-uav-isac]]"
  - "[[cooperative-isac-transceiver-beamforming]]"
created: 2026-05-28
updated: 2026-07-12
---

# Fractional Programming and Dinkelbach Transform

A family of techniques for optimizing ratios of two functions — common in EE-style objectives like

$$
\max \frac{\text{throughput}(x)}{\text{energy}(x)}
$$

The classical **Dinkelbach transform** converts a nonlinear-fractional program into a sequence of parametric problems:

$$
\max f(x) - q\, g(x), \quad \text{find $q^*$ such that the optimum is zero}
$$

A modern alternative — the **quadratic transform** (Shen & Yu 2018) — handles multi-ratio sums with stronger convergence and is now standard in wireless / SWIPT optimization.

## Why MEC papers use it

The EE objective in WPT-MEC, NOMA, and joint communication-computation problems is almost always a ratio. Direct gradient methods on the fractional form are brittle (non-convex, non-smooth at $g = 0$). Dinkelbach turns the inner problem into something tractable, which can then be combined with [[lyapunov-optimization]] for the long-term constraints.

## In this wiki

[[zhu-2025-lycnn-drl-wpt-mec]] applies fractional programming to LSEM's EE objective before applying Lyapunov to the long-term constraints. [[xiao-2025-star-ris-bidirectional-uav-mec]] uses Dinkelbach's algorithm to handle the completed-task-bits over energy objective in STAR-RIS-enabled UAV-MEC. [[wang-2026-secure-lae-uav-scheduling]] uses a Dinkelbach-driven trajectory/velocity subproblem for secrecy energy efficiency. The combination — fractional programming for the *objective* form, Lyapunov or SCA/AO for the *time and coupling constraints* — is a recurring template in long-term EE-MEC papers.

[[qin-2023-ris-uav-mec-ee]] uses Dinkelbach's method as the outer loop for RIS-assisted UAV-MEC energy efficiency. [[zhao-2026-mappo-jscc-aec]] uses Dinkelbach inside the U2H OMA power-control subproblem embedded in MAPPO-JSCC. [[cui-2026-aris-v2x-icac]] uses Dinkelbach to optimize an [[effective-energy-efficiency]] objective that combines V2X communication utility, computation utility, and energy cost.

[[zhang-2026-air-ground-covert-jamming]] applies Dinkelbach-style fractional programming on the communication-security side, embedding the ratio optimization inside a static RIS/jamming design that is later coupled to DDQN trajectory and user scheduling.

[[zhang-2025-cooperative-anti-uav-isac]] uses Dinkelbach iteration on a sensing SCNR objective inside alternating [[cooperative-isac-transceiver-beamforming]], rather than on an energy-efficiency ratio.
