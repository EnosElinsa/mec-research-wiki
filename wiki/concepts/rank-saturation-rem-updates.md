---
type: concept
title: "Rank-Saturation Radio-Map Updates"
tags: [radio-environment-map, radio-tomography, rank-estimation, adaptive-measurement, uav]
related:
  - "[[chakraborty-2026-skyscale-rti-deployment]]"
  - "[[radio-tomographic-attenuation-mapping]]"
  - "[[segment-coverage-uav-trajectory]]"
  - "[[uncertainty-triggered-radio-map-update]]"
created: 2026-07-14
updated: 2026-07-14
---

# Rank-Saturation Radio-Map Updates

Rank-saturation radio-map updating uses the marginal rank gain of a tomography projection matrix to judge whether new measurement paths add independent spatial information. Reconstruction is triggered while rank grows meaningfully and measurements can stop when additional rays become largely redundant, avoiding dependence on an unavailable online ground-truth map error.

[[chakraborty-2026-skyscale-rti-deployment]] considers QR, Lanczos estimation, and convex-hull area as progressively cheaper indicators. Saturation is geometry- and setup-specific: the hull measure is only a proxy, and static or sparse users may fail to create diverse rays even when the current [[radio-tomographic-attenuation-mapping|attenuation map]] remains inaccurate.
