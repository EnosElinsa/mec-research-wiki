---
type: source
title: "Can Movable Antenna-Enabled Micro-Mobility Replace UAV-Enabled Macro-Mobility? A Physical Layer Security Perspective"
authors: ["Kaixuan Li", "Kan Yu", "Dingyou Ma", "Yujia Zhao", "Xiaowu Liu", "Qixun Zhang", "Zhiyong Feng"]
year: ""
url: ""
venue: ""
tags: [source, movable-antenna, physical-layer-security, beamforming, uav-trajectory-control, air-to-ground-communications]
related:
  - "[[micro-macro-mobility-security]]"
  - "[[movable-antenna]]"
  - "[[physical-layer-security]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[zhiyong-feng]]"
created: 2026-07-12
updated: 2026-07-12
---

# Can Movable Antenna-Enabled Micro-Mobility Replace UAV-Enabled Macro-Mobility? A Physical Layer Security Perspective

## Citation

Li, K., Yu, K., Ma, D., Zhao, Y., Liu, X., Zhang, Q., & Feng, Z. *Can Movable Antenna-Enabled Micro-Mobility Replace UAV-Enabled Macro-Mobility? A Physical Layer Security Perspective*. Venue / year / DOI: **not in parse**.

## TL;DR

Compares two physical-layer-security control scales for an air-to-ground link: wavelength-scale movement of UAV-mounted antenna elements while the aircraft hovers, and flight-scale movement of the whole UAV with fixed antenna positions. Joint beamforming and position optimization shows complementary regimes rather than a universal winner: movable-antenna micro-mobility is strongest at low transmit power, while UAV macro-mobility benefits more from higher power and larger arrays.

## Problem

UAV trajectory optimization can reshape legitimate and eavesdropping channels over a large region, but security-driven flight consumes propulsion energy and adds latency. Movable antennas offer much smaller and faster position changes, so the paper asks when local antenna reconfiguration can replace aircraft motion for average-secrecy-rate maximization.

## System model

- A UAV-mounted `M`-element uniform linear array sends confidential data to single-antenna Bob in the presence of single-antenna Eve over `N` slots.
- In the micro-mobility formulation, the UAV hovers while every antenna moves inside a bounded local region subject to spacing and per-slot displacement constraints.
- In the macro-mobility formulation, antenna positions are fixed while the UAV follows a horizontal trajectory under velocity and acceleration constraints.
- Both formulations maximize average secrecy rate by jointly optimizing position variables and transmit beamforming.

## Method

The micro-mobility solver alternates between projected-gradient-ascent position and beamforming updates, uses AdaGrad steps and feasibility projection, and adds simulated annealing to escape poor local optima. The macro-mobility solver alternates beamforming and trajectory blocks, convexifying the trajectory subproblem with successive convex approximation and first-order Taylor bounds before solving it with CVX.

## Key findings

- Simulations use UAV altitudes 50 and 100 m, `M = 2-8`, `N = 20-60`, carrier frequency 28 GHz, wavelength 0.0107 m, transmit power 0.1-10 W, maximum speed 15 m/s, maximum acceleration 3 m/s squared, minimum antenna spacing `lambda/2`, simulated-annealing initial temperature 1, and cooling factor 0.8.
- At `P = 1 W` and `H = 50 m`, the movable-antenna solver reports 4.1046 bit/s/Hz for `M = 4` after 3,207 iterations and 5.315 bit/s/Hz for `M = 5` after 2,595 iterations; all reported trials converge within 10,000 iterations.
- The macro-mobility solver performs about 6,000 effective optimization steps, from 100 outer iterations with 60 internal CVX optimizations, and stabilizes within the 100 outer iterations.
- In the evaluated curves, micro-mobility performs better at 0.1 W, while macro-mobility generally dominates from 1 W upward. Micro-mobility shows diminishing returns around four to five antennas under the tested movement constraints.
- Figure-supported and therefore indicative: for `P = 1 W`, `M = 2`, and movement within `[0, lambda]`, optimized antenna positioning gives 8.217 dB at Bob, -11.855 dB at Eve, and a 20.072 dB gap. The macro-mobility beam patterns are described as suppressing Eve-directed sidelobes by at least 15 dB and improving Bob's main-lobe gain by 8-12 dB at the illustrated slots.

## Limitations / parse caveats

The evidence is analytical optimization plus numerical simulation, not hardware or flight validation. The model assumes deterministic LoS channels and perfect Bob/Eve positions and CSI, excluding scattering and blockage. Both optimization procedures are suboptimal. Several equations and table cells are corrupted, including a repeated-altitude comparison and an unreadable reduced antenna movement range, so those values are not normalized here.

## Relation to the corpus

This source extends [[movable-antenna]] from channel modeling and capacity enhancement into [[physical-layer-security]]. Its [[micro-macro-mobility-security]] comparison complements the global geometry control in [[uav-trajectory-control]] and shows that local antenna motion and UAV flight can be selected by operating regime rather than treated as interchangeable mobility mechanisms.

## Raw artifacts

- Parse: `raw/sources/Can_Movable_Antenna-Enabled_Micro-Mobility_Replace_UAV-Enabled_Macro-Mobility_A_Physical_Layer_Security_Perspective/Can_Movable_Antenna-Enabled_Micro-Mobility_Replace_UAV-Enabled_Macro-Mobility_A_Physical_Layer_Security_Perspective.md`
- Origin PDF: `raw/sources/Can_Movable_Antenna-Enabled_Micro-Mobility_Replace_UAV-Enabled_Macro-Mobility_A_Physical_Layer_Security_Perspective/Can_Movable_Antenna-Enabled_Micro-Mobility_Replace_UAV-Enabled_Macro-Mobility_A_Physical_Layer_Security_Perspective.pdf`
- Figures: `raw/sources/Can_Movable_Antenna-Enabled_Micro-Mobility_Replace_UAV-Enabled_Macro-Mobility_A_Physical_Layer_Security_Perspective/images/`
