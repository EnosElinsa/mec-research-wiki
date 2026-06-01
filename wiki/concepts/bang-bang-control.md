---
type: concept
title: "Bang-Bang Control"
tags: [control-theory, time-optimal-control, uav]
related:
  - "[[uav-trajectory-control]]"
  - "[[mozaffari-2019-drone-antenna-array]]"
created: 2026-06-02
updated: 2026-06-02
---

# Bang-Bang Control

A **time-optimal control** strategy in which the actuator input switches abruptly between its extreme limits ("full on / full off"), rather than varying continuously. For systems whose dynamics are linear in a bounded control input, Pontryagin's minimum principle shows the minimum-time control is of this bang-bang form: the optimal input always sits at a saturation boundary, switching at most a finite number of times.

In the wiki, [[mozaffari-2019-drone-antenna-array]] uses bang-bang control theory to derive a **closed-form minimum control time** for repositioning quadrotor drones in a drone-based antenna array — the time to move and stabilize the drones between serving locations, expressed as a function of the external forces (wind, gravity), drone weight, and destinations. There, the control time traded off against transmission time is what the bang-bang analysis bounds, connecting it to the broader [[uav-trajectory-control]] thread.
