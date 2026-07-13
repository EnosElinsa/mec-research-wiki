---
type: concept
title: "Spatial-Temporal Graph-Attention Traffic Clustering"
tags: [traffic-clustering, graph-attention, spatial-temporal, m2m, uav]
related:
  - "[[graph-neural-network]]"
  - "[[traffic-aware-asynchronous-uav-control]]"
  - "[[chen-2026-traffic-aware-asynchronous-control]]"
created: 2026-07-14
updated: 2026-07-14
---

# Spatial-Temporal Graph-Attention Traffic Clustering

A clustering method that groups devices using both physical proximity and directional traffic behavior. Each device's outgoing flows form an angular histogram, and graph attention aggregates spatial and traffic-neighbor information before clustering.

In [[chen-2026-traffic-aware-asynchronous-control]], the clusters reduce multi-UAV scheduling from individual devices to traffic-aware service regions. The clustering score combines directional distribution similarity, including KL-divergence terms, with spatial compactness.

The paper evaluates cluster shape qualitatively on packet-flow datasets with synthetic coordinates. It reports no ground-truth clustering metric such as NMI or ARI, so this concept describes the representation and grouping mechanism rather than a validated clustering-accuracy guarantee.
