---
type: concept
title: "Age of Information (AoI)"
tags: [metrics, freshness, data-collection, iot]
related:
  - "[[aoi-energy-tradeoff]]"
  - "[[qoe-modeling-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[song-2024-mol-aoi-energy]]"
created: 2026-05-29
updated: 2026-05-29
---

# Age of Information (AoI)

A **data-freshness** metric: the time elapsed since the generation of the most recently received/collected update from a source. Distinct from latency or throughput — AoI penalizes *stale* information even if individual packets arrive quickly, which matters for monitoring, control, and autonomous-driving applications where decisions depend on the freshest sensor data.

In a UAV data-collection setting, a device's AoI resets when the UAV collects its task and grows otherwise (up to a tolerable maximum beyond which data is invalid). In the wiki, [[song-2024-mol-aoi-energy]] makes total AoI a first-class objective, trading it against UAV energy in the [[aoi-energy-tradeoff]]. It is the corpus's freshness-oriented complement to delay-based [[qoe-modeling-mec]], and it tightly couples to [[uav-trajectory-control]] (the flight path determines who gets collected when).
