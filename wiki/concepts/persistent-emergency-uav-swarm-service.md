---
type: concept
title: "Persistent Emergency Service with UAV Swarms"
tags: [uav-swarm, emergency-communication, persistent-service, relaying, path-planning]
related:
  - "[[liu-2026-usp-nfrp-emergency-communication]]"
  - "[[post-disaster-mec]]"
  - "[[autonomous-uav-swarms]]"
  - "[[uav-trajectory-control]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-substitution-relaying]]"
  - "[[ant-colony-optimization]]"
  - "[[fixed-wing-propulsion-energy-model]]"
created: 2026-07-12
updated: 2026-07-12
---

# Persistent Emergency Service with UAV Swarms

Persistent emergency UAV service keeps every disaster-area access point connected while battery-limited aircraft rotate through access and relay roles. The design problem is not only where relays should sit: it must decide replacement timing, closed replenishment routes, and how the backhaul topology changes while a relay is moving.

[[liu-2026-usp-nfrp-emergency-communication]] builds periodic station-to-station rotation paths. UAVs on each path depart at that path's fixed interval and take over successive tasks, so some relay positions can move rather than remain fixed. Dynamic tree logic repairs the aerial backhaul during those transitions, and max-min ant-system search chooses path sequences and fixed/non-fixed relay roles to reduce fleet size.

This extends [[uav-substitution-relaying]] from a source-destination relay schedule to a multi-hop access network with several target areas and an explicitly maintained tree. It also differs from generic [[uav-mobile-relaying]] because continuous service and return-to-charge rotation determine how many aircraft the mission needs.

The concept's evidence is currently simulation-scoped. Distance-threshold links establish connectivity without fading, interference, capacity, or traffic; recharge is instantaneous; and homogeneous fixed-wing UAVs fly at fixed altitude and speed. Those assumptions make topological continuity visible, but they do not establish emergency-network throughput or field reliability.
