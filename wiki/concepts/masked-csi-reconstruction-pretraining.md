---
type: concept
title: "Masked CSI Reconstruction Pretraining"
tags: [channel-state-information, self-supervised-learning, masked-reconstruction, pretraining]
related:
  - "[[wang-2026-spatiotemporal-leo-channel-prediction]]"
  - "[[spatiotemporal-attention-channel-prediction]]"
  - "[[partial-csi-outage-patterns]]"
  - "[[transformer-encoder]]"
created: 2026-07-14
updated: 2026-07-14
---

# Masked CSI Reconstruction Pretraining

A self-supervised initialization strategy that removes selected CSI observations and trains an encoder to reconstruct only the masked values. The learned embedding and encoder parameters are then transferred to a future-channel predictor and fine-tuned with supervised prediction loss.

[[wang-2026-spatiotemporal-leo-channel-prediction]] samples continuous, random, or equidistant [[partial-csi-outage-patterns]] and zero-fills masked historical snapshots before reconstruction. Its experiments report the largest pretraining gains with smaller training sets and severe missing-history ratios, with narrower gains as the supervised dataset grows.

The source's equations and prose disagree on whether masks select individual channel entries or complete time snapshots; the reported experiments describe whole-time-step masking. No explicit mask token is supplied, and there is no guarantee for coefficient-level corruption, delayed or quantized CSI, nonzero noise bursts, or outage distributions outside the synthetic generator.
