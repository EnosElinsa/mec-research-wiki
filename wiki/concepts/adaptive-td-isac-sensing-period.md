---
type: concept
title: "Adaptive TD-ISAC Sensing Period"
tags: [isac, time-division, sensing-scheduling, resource-allocation, simulated-annealing]
related:
  - "[[wu-2026-sensing-error-uav-scheduling]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[sensing-error-aware-communication-rate]]"
  - "[[diffusion-augmented-madrl-replay]]"
created: 2026-07-14
updated: 2026-07-14
---

# Adaptive TD-ISAC Sensing Period

The optimization of the integer interval between sensing frames in time-division [[integrated-sensing-and-communication|ISAC]]. Short intervals refresh location estimates more often but consume slots that could carry data; long intervals preserve communication time while allowing mobility and sensing error to make beamforming and scheduling decisions stale.

[[wu-2026-sensing-error-uav-scheduling]] represents the interval by a positive integer `alpha`. For a fixed value, multi-agent learning optimizes UAV positions, user association, and bandwidth against a [[sensing-error-aware-communication-rate]]; simulated annealing then proposes neighboring period values, and the two subproblems are iterated.

This mechanism adapts a modeled scheduling timescale, not the sensing waveform itself. The source does not report the full retraining cost incurred while evaluating candidate periods, and its alternating learning-plus-annealing procedure has no global-optimality guarantee.
