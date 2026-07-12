---
type: concept
title: "Secrecy Energy Efficiency"
tags: [security, energy-efficiency, secrecy-rate, physical-layer-security, fractional-programming]
related:
  - "[[physical-layer-security]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[li-2026-secrecy-ee-uav-ris-iov]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
  - "[[wang-2026-secure-reliable-uav-mec]]"
created: 2026-07-13
updated: 2026-07-13
---

# Secrecy Energy Efficiency

Secrecy energy efficiency measures confidential throughput per unit of consumed power or energy. Its numerator is commonly a secrecy rate - legitimate-link rate minus eavesdropper rate, clipped at zero - while its denominator depends on the system boundary. The metric prevents a [[physical-layer-security|physical-layer-security]] design from improving secrecy only by spending unbounded transmit or propulsion energy.

Because this is a ratio, [[fractional-programming-dinkelbach|Dinkelbach's method]] is a recurring solver component. The remaining coupling among powers, beamforming, phase shifts, scheduling, and trajectory is usually handled by alternating optimization or successive convex approximation.

The denominator must be read paper by paper. [[li-2026-secrecy-ee-uav-ris-iov]] divides secrecy rate by base-station, relay, and vehicle transmit power while excluding the solar-powered UAV's energy. [[wang-2026-secure-lae-uav-scheduling]] includes UAV propulsion through trajectory and velocity decisions. [[wang-2026-secure-reliable-uav-mec]] divides total securely and reliably transmitted offloading data by a weighted denominator comprising UAV computation, ground-user local computation, ground-user transmit, and UAV flight energy. These are related objectives, but their numerical values are not directly comparable without aligning those accounting boundaries.
