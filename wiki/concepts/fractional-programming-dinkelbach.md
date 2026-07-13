---
type: concept
title: Fractional Programming and Dinkelbach Transform
tags: [optimization, fractional-programming, theory]
related:
  - "[[lyu-2026-situation-aware-uav-isac]]"
  - "[[guo-2026-irs-uav-isac-secrecy]]"
  - "[[xiao-2020-secrecy-energy-efficiency-relaying]]"
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
  - "[[fan-2026-hap-uav-iort-oee]]"
  - "[[overall-energy-efficiency]]"
  - "[[zhang-2026-dt-aircomp-cluster-formation]]"
  - "[[huroon-2026-bd-ris-rsma-uav]]"
  - "[[xie-2023-wireless-powered-short-packet-uav]]"
  - "[[secrecy-energy-efficiency]]"
  - "[[li-2026-secrecy-ee-uav-ris-iov]]"
  - "[[lu-2026-icsn-beamforming]]"
  - "[[crb-guided-angular-confidence-beamforming]]"
created: 2026-05-28
updated: 2026-07-14
---

# Fractional Programming and Dinkelbach Transform

[[lyu-2026-situation-aware-uav-isac]] applies a golden-section/Dinkelbach outer loop to Phase-I rate-per-power optimization and a Shen-Yu quadratic transform to Phase-II sum-of-ratios control. Rank penalties and SCA make the overall MINLP solution suboptimal despite a rank-one recovery result for one Phase-II subproblem.

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

[[lu-2026-icsn-beamforming]] uses the quadratic-transform branch of fractional programming rather than Dinkelbach iteration. Auxiliary variables decouple communication-rate ratios inside an alternating beamforming design whose angular confidence regions are updated from sensing CRBs.

[[zhang-2025-cooperative-anti-uav-isac]] uses Dinkelbach iteration on a sensing SCNR objective inside alternating [[cooperative-isac-transceiver-beamforming]], rather than on an energy-efficiency ratio.

[[fan-2026-hap-uav-iort-oee]] uses Dinkelbach as the outer loop for [[overall-energy-efficiency]], with an inner block-coordinate/SCA loop over HAP/UAV paths, HAP selection, UAV power, and IoRT bandwidth.

[[huroon-2026-bd-ris-rsma-uav]] uses the Shen-Yu quadratic transform variant for a BD-RIS/RSMA rate-per-power objective. [[xie-2023-wireless-powered-short-packet-uav]] uses Dinkelbach-style subtractive updates inside its blocklength and WPT-power subproblems.

[[li-2026-secrecy-ee-uav-ris-iov]] applies Dinkelbach to [[secrecy-energy-efficiency]] against an untrusted relay, then couples the power/amplification block to MM-based two-hop RIS phases and a warm-started DDPG trajectory policy.
