---
type: concept
title: "Radio-Tomographic Attenuation Mapping"
tags: [radio-tomography, radio-environment-map, uav, attenuation, inverse-problem]
related:
  - "[[chakraborty-2026-skyscale-rti-deployment]]"
  - "[[rank-saturation-rem-updates]]"
  - "[[segment-coverage-uav-trajectory]]"
  - "[[information-driven-uav-spectrum-mapping]]"
  - "[[radio-map-aided-uav-path-planning]]"
created: 2026-07-14
updated: 2026-07-14
---

# Radio-Tomographic Attenuation Mapping

Radio-tomographic attenuation mapping reconstructs a spatial field of propagation loss from many transmitter-receiver rays, then forward-projects that field to synthesize radio maps for new transmitter locations. It separates relatively persistent terrain attenuation from user-specific radio-environment maps, allowing measurements to be reused when users move or churn.

[[chakraborty-2026-skyscale-rti-deployment]] reduces the inverse problem by assigning one attenuation coefficient to each depth-derived terrain segment and applies regularized reconstruction to UE-UAV measurements. The approach assumes known UE locations and sufficiently stable, well-covered attenuation structure; segmentation errors, moving blockers, weather, interference, or poor initial rays can produce persistent map error.
