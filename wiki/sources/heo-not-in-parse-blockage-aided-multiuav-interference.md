---
type: source
title: "Building Blockage-Aided Interference Coordination for Multi-UAV-Enabled Wireless Networks"
authors: ["Kanghyun Heo", "Gitae Park", "Kisong Lee"]
year: ""
url: ""
venue: ""
tags: [source, uav-communications, blockage, interference-coordination, trajectory-optimization, convex-optimization]
related:
  - "[[building-blockage-aided-interference-coordination]]"
  - "[[blockage-aware-channel-model]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[block-successive-upper-bound-minimization]]"
  - "[[multi-uav-assisted-mec]]"
created: 2026-07-11
updated: 2026-07-11
---

# Building Blockage-Aided Interference Coordination for Multi-UAV-Enabled Wireless Networks

## Citation

Heo, K., Park, G., & Lee, K. *Building Blockage-Aided Interference Coordination for Multi-UAV-Enabled Wireless Networks*. Venue / year / DOI: **not in parse**.

## TL;DR

Uses buildings as a resource rather than only a channel impairment. Multi-UAV trajectories, scheduling, LoS/NLoS channel states, and transmit powers are jointly optimized so desired signal links stay LoS while interfering links are intentionally made NLoS through urban blockage.

## Problem

Dense urban UAV networks cannot rely on always-LoS assumptions. Buildings can hurt desired links, but they can also attenuate co-channel interference. The paper asks how to coordinate UAV motion and radio resources so buildings block interference without violating building boundaries or sacrificing service links.

## System model

- `M` rotary-wing UAVs serve `K` ground nodes over a flight period `T` split into `N` slots.
- UAVs share the same frequency band, so co-channel interference is present.
- Cuboid buildings determine LoS/NLoS status by geometric intersection between the UAV-GN line segment and building volumes.
- The objective maximizes the minimum average spectral efficiency among GNs by optimizing scheduling, UAV trajectories, and transmit powers.

## Method

The non-convex MINLP is decomposed into convex subproblems. The solver uses quadratic transform, successive convex approximation, penalty convex-concave procedure for binary scheduling behavior, separating-hyperplane-based building avoidance, approximated indicator functions for blockage states, and block coordinate descent over variable blocks.

## Key findings

- Default settings include `K = 6`, `M = 2`, `L = 2`, `T = 20 s`, `N = 40`, slot length 0.5 s, minimum altitude 30 m, maximum altitude 600 m, maximum 3-D speed 45 m/s, vertical speed half of that, peak transmit power 36 dBm, `beta_0 = -30 dB`, and NLoS attenuation `mu = -30 dB`.
- The default environment uses two buildings of size 100 m by 100 m by 80 m.
- The algorithm converges within 30 iterations in the reported convergence plot.
- In the default trajectory discussion, the proposed scheme keeps selected UAVs at offset positions so GN 1 and GN 4 retain NLoS interference links; GN 1 and GN 4 receive about 2.5 s of hover-like service while other GNs receive about 0.5-1 s.
- In the extended case with `M = 3`, `L = 3`, and `K = 9`, at `t = 18.5 s` UAV 1 has LoS interference channels but no transmit power, so no actual interference occurs.
- Performance trends show the proposed scheme outperforming baselines in most scenarios, with larger gains as minimum altitude and peak transmit power increase.

## Limitations / parse caveats

The parse lacks year, venue, and DOI. The opening introduction is missing its first characters, many symbols are corrupted, and Table II is flattened and partly misaligned. The source uses a simplified first-order rotary-wing kinematic model; the paper itself notes that full dynamics could reduce the agility assumed by the optimization.

## Relation to the corpus

This source extends [[blockage-aware-channel-model]] beyond "avoid blockage" into [[building-blockage-aided-interference-coordination]]. It is adjacent to [[uav-trajectory-control]] and multi-UAV communication resource allocation, but it is not an MEC offloading paper.

## Raw artifacts

- `raw/sources/Building_Blockage-Aided_Interference_Coordination_for_Multi-UAV-Enabled_Wireless_Networks/Building_Blockage-Aided_Interference_Coordination_for_Multi-UAV-Enabled_Wireless_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
