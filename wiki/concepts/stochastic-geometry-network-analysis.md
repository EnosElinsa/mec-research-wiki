---
type: concept
title: "Stochastic Geometry Network Analysis"
tags: [stochastic-geometry, network-analysis, ppp, coverage-probability]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[jiang-2025-isac-lae-overview]]"
  - "[[deng-2026-uav-cpn-energy]]"
  - "[[yang-2026-clustered-leo-adaptive-selection]]"
  - "[[clustered-leo-adaptive-selection]]"
  - "[[uav-enabled-computing-power-network]]"
created: 2026-05-29
updated: 2026-07-10
---

# Stochastic Geometry Network Analysis

A mathematical framework that models network nodes (BSs, users, UAVs, sensing targets) as samples from a **point process** (typically homogeneous Poisson) and derives **closed-form** expressions for network-level performance metrics — coverage probability, outage probability, area spectral efficiency.

Strengths: gives **distribution-level guarantees** that simulations can't, scales analytically to huge networks, exposes how performance depends on node density and tier mix. Weakness: depends on the point-process assumption — real deployments are clustered or grid-like, not Poisson.

In the wiki, [[jiang-2025-isac-lae-overview]] uses stochastic geometry to derive the **area communication coverage probability** (ACCP) and **area radar detection coverage probability** (ARDCP) for an integrated air-ground ISAC network. The two probabilities are coupled — they share the same beamformer — so the analysis exposes the fundamental sensing-vs-communication tradeoff at the network level.

[[deng-2026-uav-cpn-energy]] applies the same analytical style to [[uav-enabled-computing-power-network|UAV-enabled Computing Power Networks]]: computing nodes are a PPP, and task-completion probability depends on whether at least one thinned node satisfies the communication and computation latency constraints under UAV energy limits.

[[yang-2026-clustered-leo-adaptive-selection]] applies spherical stochastic geometry to a clustered LEO access layer. It models intra-cluster satellites, interfering satellites, and terrestrial users with point processes, then derives conditional coverage behavior for direct versus UAV-assisted cooperative transmission.

A useful complement to per-task DRL/optimization papers: stochastic geometry tells you *whether the network can support the workload at all*, before per-task scheduling enters the picture.
