---
type: concept
title: "Partial-CSI Outage Patterns"
tags: [partial-csi, channel-outage, missing-data, channel-prediction]
related:
  - "[[wang-2026-spatiotemporal-leo-channel-prediction]]"
  - "[[spatiotemporal-attention-channel-prediction]]"
  - "[[masked-csi-reconstruction-pretraining]]"
  - "[[dft-beamspace-channel-compression]]"
created: 2026-07-14
updated: 2026-07-14
---

# Partial-CSI Outage Patterns

A taxonomy for incomplete channel histories that distinguishes contiguous outages, randomly missing observations, and equidistant undersampling. Continuous loss models a sustained feedback interruption, random loss scatters missing observations across the history, and equidistant loss represents deliberate periodic sampling at a lower rate.

[[wang-2026-spatiotemporal-leo-channel-prediction]] uses these patterns alone and in mixtures to train and test [[masked-csi-reconstruction-pretraining]] for a spatiotemporal channel predictor. In its reported experiments, each mask zeroes complete historical time snapshots even though parts of the mathematical description refer more broadly to channel entries.

These patterns are abstractions rather than a complete feedback-error model. They do not separately cover delayed reports, quantization, asynchronous antenna loss, biased estimates, burst corruption with nonzero values, or topology-dependent missingness, and performance under the synthetic masks does not guarantee robustness to those effects.
