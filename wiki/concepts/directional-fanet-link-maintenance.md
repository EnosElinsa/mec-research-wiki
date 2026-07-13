---
type: concept
title: "Directional FANET Link Maintenance"
tags: [fanet, uav-communications, directional-antenna, link-maintenance, mmwave]
related:
  - "[[fan-2026-directional-neighbor-discovery]]"
  - "[[song-2026-albpd-directional-fanet]]"
  - "[[deng-2026-eret-fanet-routing]]"
  - "[[evolvable-route-expiration-time]]"
  - "[[stateless-geographic-fanet-routing]]"
  - "[[uav-mobile-relaying]]"
  - "[[wireless-backhaul]]"
  - "[[air-to-ground-channel-model]]"
  - "[[jitter-aware-uav-beamwidth-control]]"
created: 2026-07-10
updated: 2026-07-13
---

# Directional FANET Link Maintenance

Directional FANET link maintenance keeps UAV-to-UAV links alive when narrow beams and mobile UAVs make both range and angular alignment fragile. In [[song-2026-albpd-directional-fanet]], ALBP-D predicts distance-driven and angle-driven link breakage, then adjusts communication range and beamwidth before the link fails.

The concept complements [[stateless-geographic-fanet-routing]] and [[evolvable-route-expiration-time]]. Stateless routing decides where packets should go using local positions, eRET changes the route-reuse/content-discovery balance, and directional link maintenance tries to keep each directional hop usable long enough for routing and [[wireless-backhaul]] traffic to benefit from high-gain beams.

[[jitter-aware-uav-beamwidth-control]] is the single-link statistical counterpart: it selects a codebook beamwidth from accumulated platform-jitter outage/rate analysis rather than predicting a FANET neighbor-link break.
