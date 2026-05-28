---
type: synthesis
title: A design recipe for DRL-controlled multi-UAV-MEC under high-density mobility
tags: [synthesis, design, uav, drl]
related:
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[high-density-mobile-device-scenarios]]"
  - "[[j-ppo-en-convntm]]"
  - "[[en-convntm]]"
  - "[[j-ppo]]"
  - "[[hybrid-action-memory-augmented-drl-wins-uav-mec]]"
  - "[[en-convntm-beats-baselines]]"
  - "[[hybrid-action-beats-pure-drl]]"
  - "[[uav-count-inverted-u-energy]]"
  - "[[charging-stations-improve-efficiency]]"
created: 2026-05-28
updated: 2026-05-28
---

# A design recipe for DRL-controlled multi-UAV-MEC under high-density mobility

A consolidated checklist distilled from [[liu-2026-jppo-en-convntm]] and the supporting findings.

## 1. Frame the problem as a POMDP, not an MDP

You don't see the future positions of moving devices, and a Markov state in the strict sense doesn't exist. Use a history-conditioned policy. See [[pomdp]].

## 2. Build a 3-channel grid observation

Channels for: (a) device occupancy + cumulative visits, (b) UAV energy + station markers, (c) per-cell visit history. This makes the observation a CNN-friendly tensor and lets external memory operate on spatial blocks.

## 3. Model action space as hybrid continuous + discrete

Trajectory increments are continuous; charging and offloading-ratio quantization are discrete. **Use [[j-ppo]]**, not vanilla PPO and not DDPG. Set the hybrid weight $c_3 \approx 0.5$.

## 4. Use an external-memory encoder

Pure recurrent networks fall behind on long horizons. Use [[en-convntm]] (STN front-end + 3-D NTM-style memory + attention enhancement). See [[j-ppo-baselines]].

## 5. Define a multi-objective reward, not single-axis

Use the [[equilibrium-efficiency-metric]] $\Omega = \psi f / \kappa$. Single-axis rewards (only data collection, only energy, only fairness) overfit and degrade the others.

## 6. Add safety penalties

Penalize inter-UAV proximity, obstacle proximity, and battery near-depletion. Without these, the policy will exploit the unconstrained reward.

## 7. Co-design fleet size and charging-station count

[[uav-count-inverted-u-energy]]: at fixed stations, UAV count has a finite optimum.
[[charging-stations-improve-efficiency]]: more stations always help. Don't pick fleet size in isolation.

## 8. Tune $c_1, c_2, c_3$ early

Best values reported: $c_1 \approx 0.1$, $c_2 \approx 0.01$, $c_3 \approx 0.5$. See [[finding-optimal-loss-entropy-weight-coefs]].

## 9. Break sequence correlation in PPO updates

When the encoder has internal state (NTM memory), divide the sample sequence into mini-batch segments of length $K$ and randomly select $M$ of them per update. This is the trick from Algorithm 1 step 12.

## 10. Validate on hardware before claiming deployment-ready

The framework is simulation-validated only — see [[query-real-world-validation-of-jppo-en-convntm]].
