---
type: source
title: "Adaptive Selecting in Clustered LEO Systems: Direct or Cooperative Communication?"
authors: ["Shizhao Yang", "Yongxu Zhu", "Yao Shi", "Wei Feng", "Qinyu Zhang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3660891"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, leo-satellite, non-terrestrial-network, uav-relaying, stochastic-geometry, coverage-probability, cooperative-communication]
related:
  - "[[clustered-leo-adaptive-selection]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[uav-mobile-relaying]]"
  - "[[space-air-ground-integrated-network]]"
created: 2026-07-10
updated: 2026-07-10
---

# Adaptive Selecting in Clustered LEO Systems: Direct or Cooperative Communication?

## Citation

Yang, S., Zhu, Y., Shi, Y., Feng, W., & Zhang, Q. (2026). *Adaptive Selecting in Clustered LEO Systems: Direct or Cooperative Communication?* **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3660891.

## TL;DR

Analyzes a clustered LEO downlink where a UAV can assist one satellite cluster serving a random terrestrial user. The paper models intra-cluster satellites, inter-cluster interference, and users with spherical Poisson point processes, then lets the receiver adaptively select the stronger signal between direct satellite-user and UAV-assisted cooperative transmission.

## Problem

Clustered LEO systems can exploit satellite cooperation, but random out-of-cluster interference, UAV relay placement, and satellite channel fading make coverage analysis difficult. Prior clustered LEO analyses either simplify satellite geometry or use Nakagami-$m$ fading; this paper targets tractable stochastic-geometry analysis with shadowed-Rician satellite links and a low-complexity direct/cooperative selection rule.

## System model

- The downlink system has one satellite cluster, one typical UAV, and one random terrestrial user.
- Intra-cluster satellites can directly serve the user; inter-cluster satellites are interference.
- LEO satellites and users are deployed on visible spherical spaces as independent spherical Poisson point processes.
- The UAV hovers at fixed altitude above the terrestrial user cluster.
- Direct transmission uses satellite-user links; cooperative transmission uses satellite-UAV and UAV-user links with a decode-and-forward style relay path.

## Method

The analysis transforms three spherical visible regions into equivalent planar regions by scaling their densities. Under shadowed-Rician satellite fading, aggregated interference/noise terms at the UAV and user are approximated as Gamma random variables. The paper derives non-empty user probability, conditional user association, conditional Laplace transforms of accumulated signal power, and upper/lower bounds for conditional coverage probability. The adaptive selection mechanism compares direct and cooperative link quality and chooses the stronger available received signal.

## Key findings

- Simulation results indicate that moderate satellite cluster sizes and a UAV altitude around 200 m improve conditional coverage probability in the considered settings.
- The adaptive selection mechanism is generally comparable to or better than direct-only and cooperative-only transmission because it exploits spatial diversity.
- Larger satellite density can improve coverage, but the paper notes that large clusters also raise coordination complexity and may reduce practical feasibility.
- The comparison section reports more visible adaptive-selection gains at lower SINR thresholds; at larger UAV altitudes, the cooperative link can become outage-limited and performance approaches the direct link.

## Relation to the corpus

This is a communication-layer LEO/UAV analysis rather than a MEC offloading paper. It is useful beside [[leo-satellite-edge-computing]] because several satellite-edge sources assume LEO/UAV access or relay feasibility before optimizing tasks. It also extends [[stochastic-geometry-network-analysis]] from UAV-enabled computing-power networks into clustered LEO direct/cooperative coverage modeling.

## Limitations / extraction notes

The paper is analytical/simulation-based. It assumes perfect CSI for the main mechanism and leaves learning-based mode selection, interference mitigation, multiple-UAV coordination, and partial/imperfect CSI as future directions. The parse contains several OCR/math artifacts, so formula-level details should be checked against the PDF before reuse.

## Raw artifacts

- Parse: `raw/sources/Adaptive_Selecting_in_Clustered_LEO_Systems_Direct_or_Cooperative_Communication-/Adaptive_Selecting_in_Clustered_LEO_Systems_Direct_or_Cooperative_Communication-.md`
- Origin PDF: `raw/sources/Adaptive_Selecting_in_Clustered_LEO_Systems_Direct_or_Cooperative_Communication-/Adaptive_Selecting_in_Clustered_LEO_Systems_Direct_or_Cooperative_Communication-.pdf`
- Figures: `raw/sources/Adaptive_Selecting_in_Clustered_LEO_Systems_Direct_or_Cooperative_Communication-/images/`
