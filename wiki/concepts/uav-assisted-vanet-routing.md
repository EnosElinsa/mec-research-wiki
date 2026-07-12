---
type: concept
title: "UAV-Assisted VANET Routing"
tags: [vanet, fanet, routing, uav-enabled-its, trust-management, fallback-routing]
related:
  - "[[fatemidokht-2021-vru-vanet-routing]]"
  - "[[uav-enabled-its]]"
  - "[[ant-colony-optimization]]"
  - "[[stateless-geographic-fanet-routing]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-cluster-authentication]]"
  - "[[bujari-2018-stateless-fanet-routing]]"
created: 2026-07-13
updated: 2026-07-13
---

# UAV-Assisted VANET Routing

UAV-assisted VANET routing uses aerial nodes as observers, relays, or an alternate forwarding plane when urban vehicle links are sparse or obstructed. UAVs can estimate road-segment density and connectivity from above, bridge disconnected vehicle clusters, or form a FANET route that bypasses an unusable ground segment.

[[fatemidokht-2021-vru-vanet-routing]] combines those roles in VRU. Its `VRU_vu` component selects vehicle road segments from trust, connectivity, density dispersion, and destination distance; `VRU_u` discovers an [[ant-colony-optimization|ACO]] route through UAVs when the ground path is unavailable. UAV/RSU/authority blacklist aggregation also makes route choice depend on behavioral trust.

This differs from [[stateless-geographic-fanet-routing]], which chooses aerial next hops directly from current geometry, and from [[uav-cluster-authentication]], which protects UAV-cluster membership and keys rather than rating vehicle forwarding behavior.
