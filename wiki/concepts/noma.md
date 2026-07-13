---
type: concept
title: NOMA (Non-Orthogonal Multiple Access)
tags: [wireless, multiple-access, spectrum]
related:
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
  - "[[decentralized-active-ris-uav-noma-control]]"
  - "[[qin-2025-bcuav-masac]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[ji-2021-uav-mec-noma-oma-energy-min]]"
  - "[[hu-2026-latency-hybrid-uav-mec]]"
  - "[[chen-2026-qos-noma-multiuav]]"
  - "[[bui-2025-noma-near-far-offloading]]"
  - "[[hosseini-2026-aoi-covert-uav]]"
  - "[[zhou-2026-a2g-madrl-air-ground-vcs]]"
  - "[[ahmed-2026-noma-irs-vehicular]]"
  - "[[fixed-point-irs-passive-beamforming]]"
  - "[[wang-2026-noma-marine-data-computation]]"
  - "[[su-2026-three-tier-uav-capacity]]"
created: 2026-05-28
updated: 2026-07-13
---

# NOMA (Non-Orthogonal Multiple Access)

A multiple-access scheme where multiple users share the *same* time-frequency resource, separated in the **power domain**. Receivers use successive interference cancellation (SIC) to peel off users in order of channel quality.

## Why MEC papers use it

- In dense scenarios — many IoT devices per UAV cell — orthogonal multiple access (OFDMA) wastes spectrum on guard bands and rigid resource grids. NOMA squeezes more devices into a cluster at the cost of inter-user interference modeled by SINR.
- The **SINR formula** $\gamma_{j,k} = \frac{p_{j,k} g_{j,k}}{\sum_{i\ne j} p_{i,k} g_{i,k} + \sigma^2}$ becomes a non-convex term that pulls power allocation into the optimization variables — which is exactly what most UAV-MEC papers want to design.

## In this wiki

[[qin-2025-bcuav-masac]] uses NOMA across devices within each UAV's cluster (orthogonal between UAVs). The transmission power $p_{j,k}(t)$ becomes a per-slot decision variable jointly optimized with UAV trajectories under the resulting interference structure.

[[mohammadi-2026-star-ris-uav-mec-noma]] uses NOMA with SIC for simultaneous offloading through a UAV-mounted STAR-RIS toward UAV-MEC and BS-MEC execution. Its simulation reports NOMA lower total energy than OMA in that STAR-RIS architecture, contrasting with [[ji-2021-uav-mec-noma-oma-energy-min]], where OMA is lower-energy in a different UAV-MEC model.

[[hu-2026-latency-hybrid-uav-mec]] compares TDMA and NOMA in a wireless-powered hybrid UAV-GBS MEC system. In its latency-minimization experiments, NOMA completes the same task workload with fewer slots than the corresponding TDMA setting as user density grows.

[[chen-2026-qos-noma-multiuav]] uses NOMA in a multi-UAV cooperative MEC system where users with different task priorities simultaneously offload over shared subchannels. The SIC-based transmission model is coupled to QoS utility, UAV association, 3D trajectories, offloading ratios, and UAV compute allocation.

[[bui-2025-noma-near-far-offloading]] adds a near-field/far-field split: users inside the Rayleigh distance use spherical-wave channel modeling, while far-field users use plane-wave modeling. The offloading optimizer therefore couples NOMA SIC with near-field communications and UAV-MEC compute allocation.

[[hosseini-2026-aoi-covert-uav]] uses PD-NOMA outside the offloading track: the public user's signal supplies cover traffic for a covert user while the UAV minimizes [[age-of-information]] under an aerial eavesdropper's detection test.

[[zhou-2026-a2g-madrl-air-ground-vcs]] uses NOMA as the communication substrate for air-ground vehicular crowdsensing. Channel assignment becomes part of the [[sequential-multi-agent-policy-generation]] action because UAVs and UGVs share channels while collecting PoI data.

[[wang-2026-noma-marine-data-computation]] uses uplink NOMA for mandatory sensing-data collection before UAV-side computation. Its reported energy comparison favors NOMA over both FDMA and TDMA under the paper's fixed marine-sensor model, contrasting with corpus entries whose access and energy assumptions produce different orderings.

[[su-2026-three-tier-uav-capacity]] analyzes PPP-distributed device access to hovering UAVs under perfect, worst-case, and indicator-based imperfect SIC, then makes that access capacity one bottleneck in a three-tier emergency network.

## Caveats

[[morshed-2026-active-ris-uav-noma-mappo]] makes pair-level NOMA power coefficients the BS agent's action inside [[decentralized-active-ris-uav-noma-control]], while the UAV and active-RIS agents alter the propagation geometry and reflected path.

- NOMA's SIC ordering assumes accurate channel estimation; in mobile UAV scenarios this is a non-trivial assumption.
- SIC error propagation can dominate at high user counts.
