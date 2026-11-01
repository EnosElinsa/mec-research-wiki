---
type: concept
title: "Wireless Networked Control System"
tags: [wireless-control, edge-computing, hrllc, control-stability, communication-computation-control]
related:
  - "[[finite-blocklength-urllc]]"
  - "[[mobile-edge-computing]]"
  - "[[li-2025-wireless-control-hrllc-scheduling]]"
  - "[[liu-not-in-parse-wireless-control-association]]"
created: 2026-11-02
updated: 2026-11-02
---

# Wireless Networked Control System

A control architecture in which plants, sensors, and actuators are linked to a remote controller over wireless links. In the edge form studied in this wiki, sensors upload plant states to a base station, an edge server computes control commands, and the base station sends them to actuators. The sampling period, the time to close every loop once, must be short enough to keep each plant stable, so communication time, edge computation, and short-packet reliability enter one design problem alongside a stability condition.

## In this wiki

- [[li-2025-wireless-control-hrllc-scheduling]] minimizes the period for several loops served by one BS under TDMA, choosing the loop order, powers, slot lengths, and CPU allocation; stability appears as a matrix inequality in the period.
- [[liu-not-in-parse-wireless-control-association]] spreads loops over multiple massive-MIMO BSs that take turns in TDMA and optimizes BS-sensor/actuator association together with powers and slot times.

Both use finite-blocklength error models from [[finite-blocklength-urllc]]. The concept differs from task offloading for latency or energy alone because the objective is tied to closed-loop stability.
