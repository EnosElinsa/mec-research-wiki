---
type: concept
title: "Spatiotemporal-Attention Channel Prediction"
tags: [channel-prediction, transformer, spatiotemporal-attention, mimo]
related:
  - "[[wang-2026-spatiotemporal-leo-channel-prediction]]"
  - "[[transformer-encoder]]"
  - "[[masked-csi-reconstruction-pretraining]]"
  - "[[dft-beamspace-channel-compression]]"
  - "[[partial-csi-outage-patterns]]"
created: 2026-07-14
updated: 2026-07-14
---

# Spatiotemporal-Attention Channel Prediction

Transformer-based channel forecasting in which each antenna or subchannel coefficient at each time is represented as a token. Global attention learns long-range dependencies across the full antenna-time history, while local attention emphasizes nearby temporal and spatial structure before a causal decoder predicts future CSI.

[[wang-2026-spatiotemporal-leo-channel-prediction]] applies this design to direct satellite-user, satellite-RIS, and RIS-user MIMO subchannels in a moving LEO/UAV-RIS system. It combines the predictor with [[masked-csi-reconstruction-pretraining]] for incomplete histories and [[dft-beamspace-channel-compression]] to reduce the otherwise quadratic token cost.

The approach has no prediction-error, convergence, generalization, or outage-recovery guarantee. Its reported gains use simulator-generated channels from a specific orbital, mobility, weather, and 3GPP channel stack; measured satellite/UAV-RIS channels and cross-environment transfer are not evaluated.
