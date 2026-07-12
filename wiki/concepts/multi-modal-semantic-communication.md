---
type: concept
title: "Multi-Modal Semantic Communication"
tags: [semantic, multimodal, vehicular, communication]
related:
  - "[[semantic-communication]]"
  - "[[vehicular-mec]]"
  - "[[anti-jamming-mec]]"
  - "[[liu-2025-multimodal-semantic-iov-jamming]]"
  - "[[niu-2026-falcon-semantic]]"
created: 2026-07-07
updated: 2026-07-13
---

# Multi-Modal Semantic Communication

Semantic communication where the useful meaning is distributed across multiple modalities, such as text traffic reports and image observations in IoV. [[liu-2025-multimodal-semantic-iov-jamming]] models UAV-assisted MEC in which UAVs receive text semantics from RSUs and image semantics from vehicles under a jammer; if one modality's link is degraded, the final semantic accuracy can suffer. This makes channel selection, UAV positioning, and user association more coupled than in single-modality [[semantic-communication]].

[[niu-2026-falcon-semantic]] moves inside the semantic codec. Its KANet/shared-prompt module aligns heterogeneous modality representations, token values combine self-attention, cross-modal relevance, and channel state, and a range-null diffusion receiver reconstructs distorted JSCC signals. Its evaluation covers visual, textual, and acoustic tasks, but remains workstation- and channel-simulation-based.
