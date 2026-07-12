---
type: source
title: "Cooperative HAP-UAV Optimization for IoRT Data Collection: A Green Transmission Strategy for Maximizing Energy Efficiency"
authors: ["Yanbo Fan", "Yuanguo Bi", "Xingyu Ji", "Dusit Niyato", "Enchao Zhang", "Liang Zhao", "Qiang He"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3664906"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, haps, uav, iort, data-collection, energy-efficiency, trajectory-optimization, fractional-programming]
related:
  - "[[overall-energy-efficiency]]"
  - "[[high-altitude-platform-station]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[uav-data-collection]]"
  - "[[information-causality-constraint]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
created: 2026-07-12
updated: 2026-07-12
---

# Cooperative HAP-UAV Optimization for IoRT Data Collection: A Green Transmission Strategy for Maximizing Energy Efficiency

## Citation

Fan, Y., Bi, Y., Ji, X., Niyato, D., Zhang, E., Zhao, L., & He, Q. (2026). *Cooperative HAP-UAV Optimization for IoRT Data Collection: A Green Transmission Strategy for Maximizing Energy Efficiency*. **IEEE Transactions on Mobile Computing**, 25(7), 10800-10817. DOI: 10.1109/TMC.2026.3664906.

## TL;DR

Defines overall energy efficiency (OEE) for two-hop IoRT-node-to-UAV-to-HAP collection as successfully relayed data divided by total UAV and HAP energy. The ECO strategy jointly optimizes UAV/HAP trajectories, UAV transmit power, per-slot HAP selection, and IoRT bandwidth through Dinkelbach iteration, block-coordinate updates, and SCA.

## Problem

Remote IoT nodes need wide-area collection without dense terrestrial infrastructure. UAVs shorten the access link and HAPs provide broad aggregation coverage, but mobility, propulsion energy, meteorological fading, and two-hop information causality couple transmission performance to the energy budget. Designs that fix HAP motion or optimize only rate or energy miss this system-level tradeoff.

## System model

- `K` rotary-wing UAVs collect data from `Q` IoRT nodes in geographically separated regions and relay it to one of `M` data-center-enabled HAPs.
- IoRT-UAV FDMA links include probabilistic LoS/NLoS propagation; UAV-HAP OFDM links include meteorological fading and range-estimation error.
- UAVs and HAPs move horizontally at fixed altitudes. Initial/final positions, speed, UAV separation, minimum-throughput, bandwidth, and power constraints apply.
- An information-causality constraint prevents each UAV from forwarding more cumulative data than it has collected.
- OEE uses the bottleneck two-hop uploaded data in the numerator and UAV transmit/propulsion plus HAP propulsion energy in the denominator.

## Method

The resulting fractional MINLP is path-discretized and transformed with Dinkelbach's method. An inner block-coordinate loop updates UAV power, IoRT bandwidth fractions, UAV trajectories, relaxed-and-recovered HAP selection, and HAP trajectories. Convex reformulations and first-order SCA handle the non-convex rate and propulsion terms. The nested procedure is monotone under its convexified subproblems, but it does not establish a global optimum for the original MINLP.

## Key findings

- The main simulation uses 10 IoRT nodes in a `10 km x 10 km` area, three UAV regions, two HAPs, a 50 s horizon, UAV/HAP altitudes of 0.3/8 km, and meteorological-fading coefficients 1.2, 3.6, and 6.3.
- ECO can select a farther HAP when its weather-impaired link is preferable, and it balances UAV proximity to IoRT nodes against UAV-HAP link quality and information causality.
- The proposed method ranks highest in uploaded data and OEE in the reported figure comparisons. Its higher UAV transmit energy is offset by lower HAP propulsion energy, leaving total energy comparable to the tested alternatives.
- A mobile-IoRT test uses nodes moving at 1 m/s and time-varying fading between 1.2 and 6.3; ECO again ranks highest in OEE.
- The parse does not transcribe exact OEE gains. A speed-description passage also conflicts with the UAV/HAP limits in Table III, so this page does not assign those approximate speeds to a specific tier.

## Limitations / parse caveats

Evaluation is simulation-only. The model fixes aerial altitudes, separates UAV regions/subchannels to remove inter-UAV interference, ignores HAP payload energy, and uses modeled rather than measured weather fading. Relaxed HAP selection and local convex approximations have no quantified integrality or global-optimality gap. Several equations and units are OCR-damaged. Publication metadata is absent from the parse and was verified through the exact-title Crossref record; technical claims come only from the parse.

## Relation to the corpus

[[overall-energy-efficiency]] extends the HAP-UAV architecture in [[high-altitude-platform-station]] and the sensing mission in [[uav-data-collection]] with a whole-chain data-per-energy objective. Unlike [[jia-2025-dro-uav-hap-mec]], this source optimizes communication for IoRT collection rather than uncertain compute offloading; unlike [[effective-energy-efficiency]], its numerator is relayed data rather than combined communication-computation utility.

## Raw artifacts

- Parse: `raw/sources/Cooperative_HAP-UAV_Optimization_for_IoRT_Data_Collection_A_Green_Transmission_Strategy_for_Maximizing_Energy_Efficiency/Cooperative_HAP-UAV_Optimization_for_IoRT_Data_Collection_A_Green_Transmission_Strategy_for_Maximizing_Energy_Efficiency.md`
- Origin PDF: `raw/sources/Cooperative_HAP-UAV_Optimization_for_IoRT_Data_Collection_A_Green_Transmission_Strategy_for_Maximizing_Energy_Efficiency/Cooperative_HAP-UAV_Optimization_for_IoRT_Data_Collection_A_Green_Transmission_Strategy_for_Maximizing_Energy_Efficiency.pdf`
- Figures: `raw/sources/Cooperative_HAP-UAV_Optimization_for_IoRT_Data_Collection_A_Green_Transmission_Strategy_for_Maximizing_Energy_Efficiency/images/`
