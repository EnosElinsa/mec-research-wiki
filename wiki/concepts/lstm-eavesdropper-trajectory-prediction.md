---
type: concept
title: "LSTM Eavesdropper-Trajectory Prediction"
tags: [lstm, trajectory-prediction, physical-layer-security, partial-observability]
related:
  - "[[huang-2026-intelligent-jamming-maritime]]"
  - "[[pomdp]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[physical-layer-security]]"
  - "[[friendly-jamming-uav]]"
  - "[[uav-trajectory-monitoring]]"
  - "[[position-gated-velocity-nearest-neighbor-association]]"
  - "[[phase-rotated-dft-motion-parameter-estimation]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
created: 2026-07-14
updated: 2026-07-14
---

# LSTM Eavesdropper-Trajectory Prediction

LSTM eavesdropper-trajectory prediction estimates an unobserved current eavesdropper position from a sequence of past positions. A controller can then use the estimate as a compact belief-like state instead of carrying the complete trajectory history through every decision step.

[[huang-2026-intelligent-jamming-maritime]] uses this pattern in a [[pomdp|POMDP]] for legitimate and [[friendly-jamming-uav|jamming UAV]] trajectory/power control. When Eve is no longer observable, the predicted three-dimensional position replaces the history supplied to the policy.

Prediction does not remove partial observability or provide robustness by itself. The supporting simulation generates Eve with a memory-based [[gauss-markov-mobility-model]], while the observation-loss threshold, tested history length, and prediction errors are not reported in the supplied parse; generalization to abrupt, adversarial, or coordinated motion is therefore unestablished.

The ISAC [[uav-trajectory-monitoring]] pipeline provides a measured-track contrast. [[phase-rotated-dft-motion-parameter-estimation]] extracts current echo parameters and [[position-gated-velocity-nearest-neighbor-association]] assigns observations to trajectories; the LSTM instead imputes an unobserved controller input. [[aerial-observation-control-covertness-surveillance-and-monitoring]] treats them as complementary stages and transfers no accuracy claim.
