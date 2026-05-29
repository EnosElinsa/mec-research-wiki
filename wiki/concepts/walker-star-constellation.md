---
type: concept
title: "Walker-Star Constellation"
tags: [leo-satellite, constellation, simulation, coverage]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[leo-satellite-coverage-time]]"
  - "[[seamless-handover]]"
  - "[[han-2024-sagin-fl-handover]]"
created: 2026-05-29
updated: 2026-05-29
---

# Walker-Star Constellation

A standard LEO satellite constellation geometry in which orbital planes share a common inclination and are spaced to give near-polar, global coverage (the "star" pattern, vs the "delta" Walker pattern). It is parameterized by total satellite count, number of orbital planes, altitude, inclination, and minimum elevation angle, and is commonly instantiated with MATLAB's `walkerStar` + `accessIntervals` to compute per-region satellite coverage windows.

In the wiki, [[han-2024-sagin-fl-handover]] models its space tier as a Walker-Star constellation (80 satellites, 5 orbits, 800 km, 85° inclination, 15° min elevation) to derive realistic coverage times, which drive its satellite [[seamless-handover]] and offloading decisions. It is the constellation-modeling counterpart to the per-device geometric [[leo-satellite-coverage-time]] derivation used in [[chen-2024-ulse-game]].
