---
type: concept
title: "Ray Antenna Array"
tags: [antenna-array, isac, uniform-angular-resolution, mmwave]
related:
  - "[[jiang-2026-ray-antenna-array]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[extremely-large-scale-mimo]]"
  - "[[mmwave-radar-sensing]]"
  - "[[two-level-movable-antenna]]"
created: 2026-07-14
updated: 2026-07-14
---

# Ray Antenna Array

A ray antenna array (RAA) arranges many directly combined simple linear subarrays along different radial orientations. A switch-based ray-selection network connects only the strongest ray outputs to a small number of RF chains, avoiding per-element phase shifters while retaining directional spatial selectivity.

[[jiang-2026-ray-antenna-array]] proves direction-independent first-null angular resolution of `arcsin(2/M)` under full directional coverage and stated element-pattern assumptions. Its OFDM [[integrated-sensing-and-communication|ISAC]] receiver combines energy-based ray selection, an RAA-specific MUSIC spectrum, zero-forcing target separation, and delay-Doppler periodograms. The reported cost advantage is a component-price calculation, not a fabricated-array or complete-system measurement, and the paper leaves inter-ray blockage and full 3-D coverage unresolved.
