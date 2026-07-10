---
type: source
title: "Active Search for Low-altitude UAV Sensing and Communication for Users at Unknown Locations"
authors: ["Yuanshuai Zheng", "Junting Chen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3689691"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, low-altitude-uav, sensing, communication, channel-estimation, trajectory-optimization, line-of-sight]
related:
  - "[[equipotential-surface-uav-search]]"
  - "[[drone-cell-3d-placement]]"
  - "[[air-to-ground-channel-model]]"
  - "[[blockage-aware-channel-model]]"
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[uav-trajectory-control]]"
  - "[[wireless-backhaul]]"
  - "[[integrated-sensing-and-communication]]"
created: 2026-07-10
updated: 2026-07-10
---

# Active Search for Low-altitude UAV Sensing and Communication for Users at Unknown Locations

## Citation

Zheng, Y., & Chen, J. (2026). *Active Search for Low-altitude UAV Sensing and Communication for Users at Unknown Locations*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3689691.

## TL;DR

Designs an online UAV search and placement method for low-altitude sensing/communication when ground-user locations, propagation models, and city geometry are unknown. The UAV reconstructs local LoS channel maps from measurements, follows an equipotential surface that balances BS-UAV backhaul and UAV-user service, and overlays LoS discovery with a spiral-style channel-measurement trajectory.

## Problem

Low-altitude UAV access-point placement is difficult when the UAV does not know where the users are or which urban links are LoS. A full 3-D exhaustive search is too long, while statistical-geometry or radio-map baselines can assume information that the online UAV does not have. The paper asks how a UAV can actively search for feasible service positions while preserving a backhaul link to the BS.

## System model

- A UAV serves a BS and $K$ ground users in dense urban blockage.
- Feasible UAV positions must satisfy a minimum altitude and LoS constraints to the BS and served users.
- The objective balances UAV-user service capacity and BS-UAV backhaul capacity.
- Channel measurements are noisy; the UAV estimates local channel gain and gradients from online LoS samples rather than from a prebuilt radio map.

## Method

The method searches on an equipotential surface where the optimized BS-UAV and UAV-user objectives are balanced. It estimates local channel gain and gradient through first-order local polynomial regression, derives measurement-pattern and MSE guidance, and uses circular/spiral measurement motion to collect samples. LoS discovery either descends along the equipotential surface while LoS holds or traces a constant-BS-link curve after an NLoS encounter. The parsed complexity statement is $O(KM + (K+N)^3)$ per step.

## Key findings

- Simulations use two Beijing 3-D maps: a sparse commercial map with BCR 18%, FAR 1.0, and $H_{\min}=29$ m, and a dense residential map with BCR 33%, FAR 1.86, and $H_{\min}=62$ m.
- Across 2000 random-user repetitions, the proposed scheme reaches more than 95% of exhaustive 3-D search capacity in the parsed edge/center/all cases.
- Table II reports proposed vs exhaustive-3D capacity of 2.79 vs 2.83 Gbps, 2.88 vs 2.92 Gbps, and 3.39 vs 3.44 Gbps on Map A; Map B reports 1.95 vs 2.03 Gbps, 1.95 vs 2.02 Gbps, and 2.31 vs 2.43 Gbps.
- The proposed trajectory length is 3.272 km on Map A and 3.051 km on Map B; the exhaustive 2-D and 3-D table entries are 1920 km and 42240 km.
- For edge users, the parsed CDF discussion reports weakest-link SNR gains above 14 dB over statistical geometry at CDF 0.8.

## Relation to the corpus

This paper extends [[drone-cell-3d-placement]] from offline placement into online active search under unknown user locations and unknown blockage. It is close to [[radio-map-assisted-channel-estimation]], but the useful distinction is that the map is constructed on the fly from UAV measurements instead of being generated ahead of time. The equipotential-surface search also links [[uav-trajectory-control]] to [[wireless-backhaul]], because the flight path has to maintain both user-service and BS-backhaul viability.

## Limitations / extraction notes

The evaluation is simulation-only. The method assumes LoS can be inferred from signal measurements, that LoS regions obey upward/colinear geometric properties, and that local LoS channels are well captured by the first-order local model. Benchmarks do not all use the same information set. The local parsed Markdown is silent on the final DOI/venue header; bibliographic metadata was verified against a title-matched IEEE Computer Society record.

## Raw artifacts

- Parse: `raw/sources/Active_Search_for_Low-altitude_UAV_Sensing_and_Communication_for_Users_at_Unknown_Locations/Active_Search_for_Low-altitude_UAV_Sensing_and_Communication_for_Users_at_Unknown_Locations.md`
- Origin PDF: `raw/sources/Active_Search_for_Low-altitude_UAV_Sensing_and_Communication_for_Users_at_Unknown_Locations/Active_Search_for_Low-altitude_UAV_Sensing_and_Communication_for_Users_at_Unknown_Locations.pdf`
- Figures: `raw/sources/Active_Search_for_Low-altitude_UAV_Sensing_and_Communication_for_Users_at_Unknown_Locations/images/`
