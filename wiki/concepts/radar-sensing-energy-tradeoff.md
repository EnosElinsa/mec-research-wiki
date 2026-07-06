---
type: concept
title: "Radar-Sensing / Energy Tradeoff"
tags: [iscc, radar-sensing, energy-efficiency, uav]
related:
  - "[[zhou-2026-radar-energy-iscac]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[mmwave-radar-sensing]]"
  - "[[uav-trajectory-control]]"
  - "[[hierarchical-aerial-mec]]"
created: 2026-07-07
updated: 2026-07-07
---

# Radar-Sensing / Energy Tradeoff

The design tension between collecting more radar sensing data and spending less energy on sensing, offloading, computation, and propulsion. In [[zhou-2026-radar-energy-iscac]], UAVs sense ground users and offload part of the sensing data to a HAP MEC server; maximizing sensing-data volume without energy control would increase radar, communication, compute, and movement costs.

The tradeoff is an [[integrated-sensing-computation-communication]] variant because sensing data is not only measured; it must also be transmitted and processed under latency and energy constraints.
