---
type: query
title: Does j-PPO+EN-ConvNTM transfer from simulation to real-world UAV-MEC?
tags: [open-question, sim-to-real, uav]
related:
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[en-convntm-beats-baselines]]"
created: 2026-05-28
updated: 2026-05-28
---

# Does j-PPO+EN-ConvNTM transfer from simulation to real-world UAV-MEC?

## Why this is open

The authors explicitly flag this in their conclusion: all reported gains are from PyTorch simulation only. Real flight introduces:

- Wind, turbulence, and battery telemetry that don't match the constant-speed flight model.
- Channel fluctuations that violate the LoS-only OFDMA assumption.
- Hardware-induced action latency (the policy may decide to charge several time-steps before the UAV physically commits).
- Interference between concurrent uplinks not modeled by the paper.

## What evidence would help

- An outdoor multi-UAV testbed running the exact `j-PPO+EN-ConvNTM` policy.
- A semi-real evaluation where simulated devices feed a real UAV controller (HIL).
- A variance/perturbation study within simulation: inject Gaussian wind noise and measure $\Omega$ degradation.

## Why it matters for this wiki

If the framework is brittle under real-world noise, follow-up work probably needs domain randomization or a robust-RL formulation, not just architectural tweaks.
