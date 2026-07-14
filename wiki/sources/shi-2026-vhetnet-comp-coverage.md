---
type: source
title: "Vertical Heterogeneous Networks Beyond 5G: CoMP Coverage Enhancement and Optimization"
authors: ["Tian Shi", "Wenkun Wen", "Peiran Wu", "Minghua Xia"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3644244"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 9391-9405"
tags: [source, coordinated-multipoint, vertical-heterogeneous-network, aerial-user, stochastic-geometry, uav-deployment, coverage-probability]
related:
  - "[[coordinated-multipoint-transmission]]"
  - "[[same-tier-three-site-comp]]"
  - "[[two-regime-aerial-user-association]]"
  - "[[poisson-delaunay-comp-clustering]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[air-to-ground-channel-model]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[air-ground-integrated-network]]"
  - "[[jin-2026-jitter-aware-uav-comp]]"
  - "[[ren-2026-distributed-uav-los]]"
  - "[[hong-2026-beam-delay-alignment]]"
  - "[[fang-2026-cellfree-uav-predictive-beamforming]]"
  - "[[chai-2026-random-position-relay-deployment]]"
  - "[[bor-yaliniz-2016-3d-abs-placement]]"
  - "[[mobility-asynchrony-and-geometry-in-aerial-coverage]]"
created: 2026-07-14
updated: 2026-07-14
---

# Vertical Heterogeneous Networks Beyond 5G: CoMP Coverage Enhancement and Optimization

## Citation

Shi, T., Wen, W., Wu, P., & Xia, M. (2026). *Vertical Heterogeneous Networks Beyond 5G: CoMP Coverage Enhancement and Optimization*. **IEEE Transactions on Wireless Communications, 25**, 9391-9405. DOI: 10.1109/TWC.2025.3644244.

> **Publication chronology.** The article was published online on 22 December 2025 and appears in the 12 January 2026 current/final volume. The wiki therefore uses 2026 as the article year, while the DOI and online-publication record carry 2025.

## TL;DR

Analyzes aerial-user downlink coverage in a vertical heterogeneous network of UAV-mounted aerial base stations (ABSs) and terrestrial base stations (TBSs). The paper combines same-tier three-site CoMP, BPP/PPP stochastic geometry, altitude-dependent tier association, and a coverage-deficit-weighted K-means procedure for horizontal ABS placement.

## Problem framing

Sparse aerial users can cross altitude-dependent coverage gaps because terrestrial blockage, aerial-site proximity, and aggregate interference change differently with height. The paper asks how a two-tier [[air-ground-integrated-network|air-ground network]] can use [[coordinated-multipoint-transmission|CoMP]] to characterize and improve aerial-user coverage, and how ABSs can be repositioned when coverage-deficient sample locations are known.

The analytical goal is a tractable coverage probability that combines serving-tier association, three-site desired power, and interference from both tiers. The deployment goal is narrower: choose horizontal ABS centers that favor locations with terrestrial SIR deficits under a fading- and path-loss-aware surrogate objective.

## System model

- The network contains $N$ ABSs at common altitude $H$, uniformly distributed in a disk of radius $r_C$ as a finite binomial point process, and TBSs modeled by an independent homogeneous Poisson point process.
- A typical aerial user lies between the terrestrial and aerial layers. ABS-to-user links are assumed LoS; TBS-to-user links may be LoS or NLoS according to an elevation-dependent [[air-to-ground-channel-model]]. Both link types use Nakagami-$m$ fading.
- All sites transmit with equal power, thermal noise is neglected, and coverage is defined by an SIR threshold. Noncooperating ABSs and TBSs both contribute interference.
- Each serving cluster contains exactly three sites. **Mixed-tier ABS-TBS serving triads are excluded from the analytical model:** service is provided by either three ABSs or three TBSs. One simulation reports mixed triads below 10% and about 5% on average in its evaluated setup, but that scenario-specific observation does not establish that mixed-tier service is negligible generally.
- Association compares long-term aggregate received power from the three-ABS and three-TBS candidates. Overall coverage is the association-weighted sum of their conditional coverage probabilities.

## Method

1. Derive marginal and joint distance distributions for the general $n$th-nearest ABSs under the finite BPP and TBSs under the PPP.
2. Use [[poisson-delaunay-comp-clustering]] separately within each tier to define tractable three-site clusters instead of exhaustively ranking all candidate triads.
3. Apply moment matching to the aggregate fading-amplitude and large-scale-signal terms, then derive association probabilities, conditional serving-distance laws, interference Laplace transforms, and conditional and overall coverage expressions.
4. Characterize [[two-regime-aerial-user-association]] as altitude changes the balance between terrestrial LoS improvement and proximity to the aerial layer.
5. For intentional placement, weight each sample by its TBS coverage deficit and alternate between kernel-based cluster assignment and weighted-centroid updates. This extends [[weighted-kmeans-uav-deployment]] with SIR-deficit and Nakagami/path-loss weighting.
6. Compare the analytical results with Monte Carlo simulations and compare random placement, classical weighted K-means, and the proposed deployment rule.

## Key findings

- The nearest-site distance expressions and coverage curves closely follow the corresponding Monte Carlo results in the plotted configurations.
- The Gamma laws used for aggregate received-amplitude and large-scale-signal terms are **moment-matched approximations, not exact distributional equalities**. The tractable coverage result inherits these approximations together with the BPP/PPP, same-tier-cluster, fading, LoS, equal-power, and interference-limited assumptions.
- Association is U-shaped with altitude in the evaluated suburban and high-rise settings: improving terrestrial LoS first shifts users toward TBSs, while proximity to the ABS altitude later shifts them back toward ABSs. The reported regime boundary near 110 m is parameter- and scenario-dependent.
- **Proposition 2 assumes** that ABS association is continuous and strictly U-shaped with a unique minimum. Its zero-, one-, or two-root classification for equal ABS/TBS association is conditional on that shape; it does not prove that every deployment has a U-shaped association curve.
- Coverage decreases with the SIR threshold and can be non-monotone in the number of ABSs: additional ABSs initially improve desired signal strength, but eventually add enough interference to reduce coverage. The best ABS count depends on altitude and propagation parameters.
- In a scenario with SIR threshold $-4$ dB and path-loss exponent 3, the paper reports coverage of about 0.9 for CoMP versus about 0.1 for single-site transmission. The Delaunay-based scheme also tracks the plotted strongest-three heuristic without requiring the same exhaustive search, although no measured runtime comparison is provided.
- In the Fig. 12 deployment configuration, coverage is 61.99% for TBS-only service, 72.93% with random ABS placement, 79.85% with classical weighted K-means, and 81.42% with the proposed method. These percentages are configuration-specific; the proposed method improves on classical weighted K-means by 1.57 percentage points in that case.

## Limitations

- The work is analytical and simulation-based, with no field deployment or measured aerial-channel validation.
- Same-tier [[same-tier-three-site-comp]] assumes coherent synchronization and suitable backhaul. Cross-tier coherent transmission is not analyzed despite the broader two-tier framing.
- The finite uniform-disk ABS process and homogeneous PPP TBS process simplify real planned deployments. ABS links are always LoS, terrestrial LoS follows a simplified probability law, transmit powers are equal, and thermal noise is omitted.
- The analysis treats static aerial-user snapshots and fixed ABS altitude. It does not optimize mobility, trajectories, propulsion energy, handover dynamics, backhaul capacity, or terrestrial-user service.
- The placement method requires known sample locations and terrestrial SIR deficits, and optimizes horizontal centers rather than joint three-dimensional placement. Its alternating updates are stated to improve the surrogate objective, but **the deployment method has no global-optimality guarantee**.

## Relation to the corpus

This source extends [[stochastic-geometry-network-analysis]] from single-site aerial association to same-tier three-site CoMP in a two-tier VHetNet. [[ren-2026-distributed-uav-los]] instead emphasizes a practical 3GPP LoS model and repulsive terrestrial-site geometry, while [[jin-2026-jitter-aware-uav-comp]] studies CSI aging and prediction in multi-UAV CoMP rather than spatial association and coverage.

For deployment, the paper adds a physical-layer coverage-deficit variant of [[weighted-kmeans-uav-deployment]]. It differs from [[bor-yaliniz-2016-3d-abs-placement]], which jointly selects altitude and coverage geometry for a single aerial base station rather than placing multiple fixed-altitude ABSs around CoMP coverage holes.

## Raw artifacts

- Markdown parse: `raw/sources/Vertical_Heterogeneous_Networks_Beyond_5G_CoMP_Coverage_Enhancement_and_Optimization/Vertical_Heterogeneous_Networks_Beyond_5G_CoMP_Coverage_Enhancement_and_Optimization.md`
- Origin PDF: `raw/sources/Vertical_Heterogeneous_Networks_Beyond_5G_CoMP_Coverage_Enhancement_and_Optimization/Vertical_Heterogeneous_Networks_Beyond_5G_CoMP_Coverage_Enhancement_and_Optimization.pdf`
- Extracted figures: `raw/sources/Vertical_Heterogeneous_Networks_Beyond_5G_CoMP_Coverage_Enhancement_and_Optimization/images/`
