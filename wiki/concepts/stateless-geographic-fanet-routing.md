---
type: concept
title: "Stateless Geographic FANET Routing"
tags: [routing, fanet, uav-communications, geographic-routing]
related:
  - "[[bujari-2018-stateless-fanet-routing]]"
  - "[[deng-2026-eret-fanet-routing]]"
  - "[[evolvable-route-expiration-time]]"
  - "[[song-2026-albpd-directional-fanet]]"
  - "[[directional-fanet-link-maintenance]]"
  - "[[uav-mobile-relaying]]"
  - "[[wireless-backhaul]]"
  - "[[wu-not-in-parse-aoi-sampling-buffering-routing]]"
  - "[[fatemidokht-2021-vru-vanet-routing]]"
  - "[[uav-assisted-vanet-routing]]"
created: 2026-07-10
updated: 2026-07-13
---

# Stateless Geographic FANET Routing

Stateless geographic FANET routing forwards each packet using current node and destination positions rather than a maintained end-to-end route. That design avoids routing-table churn in fast-changing flying ad hoc networks, but 3-D geometry creates local minima and makes 2-D planarization/face-routing assumptions unreliable.

[[bujari-2018-stateless-fanet-routing]] compares deterministic progress, randomized progress, face/projection, hybrid, and restricted-flooding variants under a common simulation setup. Its main design lesson is a tradeoff: progress methods are scalable and short-path but can fail at local minima; face methods deliver more packets but can create long paths; hybrid methods often provide the most balanced delivery/path-dilation/scalability profile.

[[song-2026-albpd-directional-fanet]] adds the lower-layer directional-link view. Even if forwarding is stateless, each hop can still fail when UAV motion breaks range or beam alignment, so [[directional-fanet-link-maintenance]] predicts those breakages and adjusts beamwidth/range before routing has to recover from a broken link.

[[deng-2026-eret-fanet-routing]] adds a different adaptive-routing axis. Its [[evolvable-route-expiration-time]] mechanism does not choose geographic next hops; it changes how long route entries remain valid so the same FANET can behave more like host-centric routing in stable/heavy-load conditions and more like content-centric routing in fast-changing/high-sharing conditions.

[[wu-not-in-parse-aoi-sampling-buffering-routing]] connects FANET routing to freshness control. Its follower UAVs choose sampling, packet-buffer decisions, and next-hop forwarding jointly, so a geographically plausible route is only useful when it keeps the packet age low at the leader UAV.

[[fatemidokht-2021-vru-vanet-routing]] provides a stateful contrast: its UAV fallback discovers and stores end-to-end paths with ACO, while a separate vehicle/UAV component scores urban road segments from density, connectivity, and trust.
