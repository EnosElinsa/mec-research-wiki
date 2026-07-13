---
type: concept
title: "UAV Named Data Networking"
tags: [named-data-networking, uav-swarm, content-caching, information-centric-networking]
related:
  - "[[jin-2026-skyndn-incentivizer]]"
  - "[[autonomous-uav-swarms]]"
  - "[[gauss-markov-mobility-model]]"
  - "[[iterative-double-auction-incentive]]"
  - "[[double-auction]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV Named Data Networking

An information-centric networking architecture in which UAVs request content by name through Interest packets and any producer or cache holding that content may return a Data packet. Name-based retrieval and in-network caching can reduce dependence on a fixed endpoint, but mobility makes forwarding paths, cache availability, and the return route transient.

[[jin-2026-skyndn-incentivizer]] studies a mobile UAV swarm in which Data packets need not retrace the Interest path because that path may disappear. Its model forwards toward the nearest available next hop and uses an [[iterative-double-auction-incentive]] to compensate UAVs that spend energy and radio resources sharing cached content.

The source assumes homogeneous UAVs, orthogonal producer subchannels, average channel gains, a trusted central broker, and always-available nearest-hop forwarding. It does not model cache eviction, Pending Interest Table growth, content authentication, routing loops, interference, or broker disconnection, so its results do not establish a complete deployable NDN forwarding stack for arbitrary [[autonomous-uav-swarms|UAV swarms]].
