---
type: concept
title: "Graph Attention over a Flying Ad Hoc Network"
tags: [fanet, graph-attention, multi-uav, message-passing, partial-observability]
related:
  - "[[ye-2023-graph-uav-coverage]]"
  - "[[graph-neural-network]]"
  - "[[autonomous-uav-swarms]]"
  - "[[communication-constrained-marl]]"
  - "[[memory-augmented-multi-uav-navigation]]"
created: 2026-07-13
updated: 2026-07-13
---

# Graph Attention over a Flying Ad Hoc Network

Graph attention over a flying ad hoc network treats UAVs as nodes and current radio-neighbor relations as dynamic edges. Attention learns which neighbor embeddings matter for a local action, while stacking layers expands the information field beyond direct neighbors without requiring a direct long-range radio link.

[[ye-2023-graph-uav-coverage]] stacks two graph-attention layers over distance-defined FANET edges and combines them with GRU history. Each UAV communicates only with one-hop neighbors, but the second layer carries two-hop information. This models connectivity limits; it does not optimize bandwidth, latency, or message contention.
