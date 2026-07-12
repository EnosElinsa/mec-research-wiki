---
type: concept
title: "Releasing-Collecting-Recycling UAV Framework"
tags: [uav-data-collection, heterogeneous-uav, carrier-uav, dubins-path, rendezvous]
related:
  - "[[fu-2026-dubins-uav-data-collection]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[heterogeneous-uav-fleet]]"
created: 2026-07-13
updated: 2026-07-13
---

# Releasing-Collecting-Recycling UAV Framework

A releasing-collecting-recycling UAV framework couples a fast carrier UAV with subordinate communication UAVs. The carrier transports and releases the subordinates near assigned terminal clusters, the subordinates collect data on separate routes, and synchronized rendezvous trajectories let the carrier recover them before returning to base.

[[fu-2026-dubins-uav-data-collection]] implements this architecture with altitude-aware clustering, obstacle-aware bundled ant-colony tours, and Dubins recovery timing. The carrier/subordinate fleet size is part of the planning problem because too few collectors lengthen data tours while too many increase release, recovery, and waiting overhead.

The framework is more specific than general [[uav-data-collection]]: it requires airborne release and recovery plus time-coupled carrier/subordinate paths. Its current evidence assumes centralized offline planning, known terrain and terminals, homogeneous collectors, and negligible physical recovery time.
