---
type: concept
title: "Adaptive Intermediate Data Compression"
tags: [edge-ai, compression, communication, quantization]
related:
  - "[[collaborative-dl-inference]]"
  - "[[data-partition-parallel-inference]]"
  - "[[sun-2024-asap-uav-swarm]]"
created: 2026-05-29
updated: 2026-05-29
---

# Adaptive Intermediate Data Compression

Compressing the **intermediate feature maps** exchanged between nodes during distributed inference, to cut inter-node communication time on weak/variable links. The compression aggressiveness is chosen **adaptively** — e.g. by comparing the data-size-to-link-rate ratio against thresholds before each transmission — so it compresses harder when the link is the bottleneck and less when compute dominates.

In the wiki, [[sun-2024-asap-uav-swarm]] uses 8-bit quantization plus lossless gzip on intermediate features, with the quantization scale picked adaptively per transmission: it reduces intermediate data by 87.2%–92.7% with <0.15% accuracy loss (8-bit keeps ~32-bit accuracy; 4-bit degrades badly). It directly supports [[data-partition-parallel-inference]] and [[collaborative-dl-inference]] over bandwidth-limited UAV links.
