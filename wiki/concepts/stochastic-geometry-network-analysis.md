---
type: concept
title: "Stochastic Geometry Network Analysis"
tags: [stochastic-geometry, network-analysis, ppp, coverage-probability]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[jiang-2025-isac-lae-overview]]"
created: 2026-05-29
updated: 2026-05-29
---

# Stochastic Geometry Network Analysis

A mathematical framework that models network nodes (BSs, users, UAVs, sensing targets) as samples from a **point process** (typically homogeneous Poisson) and derives **closed-form** expressions for network-level performance metrics — coverage probability, outage probability, area spectral efficiency.

Strengths: gives **distribution-level guarantees** that simulations can't, scales analytically to huge networks, exposes how performance depends on node density and tier mix. Weakness: depends on the point-process assumption — real deployments are clustered or grid-like, not Poisson.

In the wiki, [[jiang-2025-isac-lae-overview]] uses stochastic geometry to derive the **area communication coverage probability** (ACCP) and **area radar detection coverage probability** (ARDCP) for an integrated air-ground ISAC network. The two probabilities are coupled — they share the same beamformer — so the analysis exposes the fundamental sensing-vs-communication tradeoff at the network level.

A useful complement to per-task DRL/optimization papers: stochastic geometry tells you *whether the network can support the workload at all*, before per-task scheduling enters the picture.
