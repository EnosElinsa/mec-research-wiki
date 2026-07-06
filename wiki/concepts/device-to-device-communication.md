---
type: concept
title: "Device-to-Device (D2D) Communication"
tags: [cellular, spectrum-sharing, interference-management, stochastic-geometry, physical-layer]
related:
  - "[[mozaffari-2016-uav-underlaid-d2d]]"
  - "[[overlay-underlay-spectrum-access]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[air-to-ground-channel-model]]"
  - "[[li-2026-cdto-inland-waterways]]"
created: 2026-06-02
updated: 2026-07-06
---

# Device-to-Device (D2D) Communication

Direct communication between two nearby user devices without routing traffic through a base station. D2D improves coverage and capacity, offloads the infrastructure, and is valuable in hotspots or public-safety settings where devices can talk to each other with little infrastructure. D2D links are commonly deployed as **underlay** transmissions that reuse licensed spectrum already used by cellular (or, here, UAV) downlinks — which raises **interference-management** challenges between the underlaid D2D pairs and the primary network (see [[overlay-underlay-spectrum-access]]).

A D2D pair is typically modeled as a transmitter and a receiver separated by a fixed distance, with the set of interfering D2D transmitters distributed as a Poisson point process — making [[stochastic-geometry-network-analysis|stochastic geometry]] the natural analysis tool for coverage and rate.

## In this wiki

[[mozaffari-2016-uav-underlaid-d2d]] analyzes the coexistence of a UAV downlink base station with an **underlaid D2D** network sharing the same band. The UAV serves downlink users while the D2D pairs reuse the spectrum, so each suffers interference from the other; the paper derives coverage probability, sum-rate, and D2D outage via stochastic geometry, and shows the **optimal UAV altitude decreases as D2D density increases**. The aerial setting differs from classic terrestrial D2D coexistence because the UAV→ground channel is probabilistic-LoS ([[air-to-ground-channel-model]]) and the UAV's height and mobility are extra design dimensions.

[[li-2026-cdto-inland-waterways]] uses D2D links differently: nearby USVs share computation through D2D offloading links, while UAVs act as cluster heads that reposition to cover the selected links.
