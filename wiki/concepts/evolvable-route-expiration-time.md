---
type: concept
title: "Evolvable Route Expiration Time"
tags: [fanet, routing, uav-swarm, adaptive-routing, content-centric-networking]
related:
  - "[[deng-2026-eret-fanet-routing]]"
  - "[[stateless-geographic-fanet-routing]]"
  - "[[directional-fanet-link-maintenance]]"
  - "[[wireless-backhaul]]"
  - "[[autonomous-uav-swarms]]"
created: 2026-07-10
updated: 2026-07-10
---

# Evolvable Route Expiration Time

Evolvable route expiration time is a FANET routing control knob where each UAV changes how long routing entries remain valid, so the network can slide between host-centric route reuse and content-centric broadcast discovery. A larger RET makes the node behave more like host-centric routing; a smaller RET pushes it toward content-centric behavior.

In [[deng-2026-eret-fanet-routing]], RET is updated from local passive observations of neighbor variation, request forwarding, and per-content request frequency. The idea complements [[stateless-geographic-fanet-routing]] and [[directional-fanet-link-maintenance]] by adding an adaptive routing-paradigm layer above next-hop geometry and directional-link upkeep.
