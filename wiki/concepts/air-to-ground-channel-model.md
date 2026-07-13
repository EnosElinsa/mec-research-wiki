---
type: concept
title: "Air-to-Ground Channel Model"
tags: [channel-model, los-nlos, propagation, uav, coverage]
related:
  - "[[mahmoud-2021-uav-irs-iot-analysis]]"
  - "[[blockage-aware-channel-model]]"
  - "[[terrain-aware-channel-model]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[al-hourani-2014-optimal-lap-altitude]]"
  - "[[hu-2026-latency-hybrid-uav-mec]]"
  - "[[angle-dependent-rician-fading]]"
  - "[[you-2019-rician-uav-data-harvesting]]"
  - "[[bai-2026-multimodal-uav-vehicle-channel]]"
  - "[[hussain-2026-unet-uav-mmwave-pathloss]]"
  - "[[multi-modal-intelligent-channel-modeling]]"
  - "[[multi-scale-unet-pathloss-prediction]]"
  - "[[chen-2026-air-ground-covert]]"
  - "[[ambient-interference-aided-covertness]]"
  - "[[prabhath-not-in-parse-3d-space-spectrum-utilization]]"
  - "[[ebrahimi-not-in-parse-autonomous-uav-localization-rl]]"
  - "[[rss-based-uav-localization]]"
  - "[[wang-2026-bayesian-uav-spectrum-mapping]]"
  - "[[belgiovine-not-in-parse-multidt-abs-deployment]]"
  - "[[heo-not-in-parse-blockage-aided-multiuav-interference]]"
  - "[[building-blockage-aided-interference-coordination]]"
  - "[[zhang-2026-control-assisted-beam-tracking]]"
  - "[[control-assisted-uav-beam-tracking]]"
  - "[[li-2026-directional-modulation-irs-uav]]"
  - "[[zhang-2026-distributed-jscc-uav-video]]"
  - "[[wang-2026-multimodal-uav-coverage-backhaul]]"
  - "[[samir-2021-uav-cell-free-coverage]]"
  - "[[zhai-2026-uav-ma-secrecy]]"
  - "[[wan-2026-movable-antenna-multiuav-mimo]]"
  - "[[ren-2026-movable-antenna-uav-trajectory]]"
  - "[[cui-2020-marl-uav-resource-allocation]]"
  - "[[dong-2026-radio-map-d2d-relay]]"
  - "[[jin-2026-jitter-aware-uav-comp]]"
created: 2026-05-31
updated: 2026-07-13
---

# Air-to-Ground Channel Model

Recent corpus additions span three different uses: [[cui-2020-marl-uav-resource-allocation]] learns discrete allocation under probabilistic-LoS interference, [[dong-2026-radio-map-d2d-relay]] builds terrain-specific multi-frequency rate maps, and [[jin-2026-jitter-aware-uav-comp]] derives temporal channel correlation under attitude jitter.

Three movable-array sources use LoS/free-space A2G links while changing different spatial variables: [[zhai-2026-uav-ma-secrecy]] controls secrecy through trajectory and element motion, [[wan-2026-movable-antenna-multiuav-mimo]] controls multi-UAV uplink geometry, and [[ren-2026-movable-antenna-uav-trajectory]] carries array state through cellular path planning.

The **air-to-ground (ATG) channel model** describes propagation between an aerial platform (UAV / LAP / HAP) and ground receivers. The dominant formulation treats received signals as a probabilistic mixture of **LoS** and **NLoS** groups: the mean pathloss is the free-space pathloss plus a group-dependent **excessive pathloss**, weighted by the probability of each group. The **LoS probability** is commonly approximated as a sigmoid (S-curve) of the **elevation angle**, parameterized by the urban environment (built-up ratio, building density, building-height distribution).

## In this wiki

- [[al-hourani-2014-optimal-lap-altitude]] is the foundational origin of this sigmoid-LoS-vs-elevation-angle model: it derives the closed-form LoS probability from ITU P.1410 statistical parameters and uses it to compute the LAP altitude maximizing ground coverage. This statistical sub-family is the most common ATG model across the corpus's aerial sources (cf. [[blockage-aware-channel-model]]'s three sub-families — statistical, radio-map, and geometric — where the [[terrain-aware-channel-model]] is the geometric variant).
- [[hu-2026-latency-hybrid-uav-mec]] uses a probabilistic LoS/NLoS A2G channel inside a wireless-powered hybrid UAV-MEC latency problem, making UAV altitude part of both channel-quality and task-completion-latency control.
- [[you-2019-rician-uav-data-harvesting]] uses [[angle-dependent-rician-fading]] rather than a LoS/NLoS probability mixture, making altitude control balance path loss against elevation-angle-dependent effective fading power under an outage constraint.
- [[bai-2026-multimodal-uav-vehicle-channel]] and [[hussain-2026-unet-uav-mmwave-pathloss]] extend the channel-modeling side of the corpus: the former uses [[multi-modal-intelligent-channel-modeling]] with LiDAR-aided scatterer classes, while the latter uses [[multi-scale-unet-pathloss-prediction]] over geometry-derived LoS and building masks.
- [[chen-2026-air-ground-covert]] uses the probabilistic LoS/NLoS air-to-ground channel inside a covert-communication model, where Bob's connection probability and Willie's detection behavior also depend on PPP-modeled environmental interference.
- [[prabhath-not-in-parse-3d-space-spectrum-utilization]] is primarily UAV-to-UAV downlink analysis, but it provides a nearby 3-D aerial-channel benchmark across free-space, log-normal, and Nakagami-m propagation, with A2G/SAGIN extension identified as requiring adapted propagation assumptions.
- [[ebrahimi-not-in-parse-autonomous-uav-localization-rl]] uses the ATG channel as a localization model: RSSI is converted to distance under elevation-angle-dependent path loss and shadowing, then [[rss-based-uav-localization]] chooses waypoints that improve multilateration geometry.
- [[wang-2026-bayesian-uav-spectrum-mapping]] and [[belgiovine-not-in-parse-multidt-abs-deployment]] move toward environment-specific channel knowledge: the former learns a 3-D REM from sparse UAV samples, while the latter uses ray-tracing digital twins for airborne-base-station placement. [[heo-not-in-parse-blockage-aided-multiuav-interference]] adds the urban blockage case, where LoS/NLoS status is optimized for both desired and interfering links.
- [[zhang-2026-control-assisted-beam-tracking]] studies a LoS-dominant single-path mmWave link where propagation is not the main unknown; [[control-assisted-uav-beam-tracking]] instead predicts beam misalignment from UAV attitude, velocity, position, and waypoint-control state.
