---
type: concept
title: "Digital Twin"
tags: [digital-twin, edge-computing, synchronization, metaverse]
related:
  - "[[semantic-communication]]"
  - "[[uav-data-collection]]"
  - "[[mobile-edge-computing]]"
  - "[[du-2024-yolo-semcom-digital-twin]]"
  - "[[yang-2024-taco-human-digital-twin-edge]]"
  - "[[li-2023-adaptive-digital-twin-uav-iscc]]"
  - "[[he-2026-dt-sagimec-lae]]"
  - "[[li-2025-dt-uav-swarm-resource-management]]"
  - "[[vehicle-twin-migration]]"
  - "[[chen-2026-hc-mappo-vehicle-twin-migration]]"
  - "[[multi-digital-twin-network-optimization]]"
  - "[[belgiovine-not-in-parse-multidt-abs-deployment]]"
  - "[[zhao-2026-dt-ddqn-bisd-deployment]]"
  - "[[zhang-2026-dt-aircomp-cluster-formation]]"
  - "[[zhou-2026-multiscale-dt-uav-delivery]]"
created: 2026-06-02
updated: 2026-07-13
---

# Digital Twin

A **digital twin (DT)** is a continuously-updated virtual replica of a physical object, process, or environment. Because the physical world changes over time, a DT must be repeatedly **synchronized** with fresh measurements collected by edge devices (sensors, cameras, UAVs), which makes DTs a heavy and recurring data-transmission workload for the wireless edge — the data volume needed to keep the twin accurate is exactly the cost a DT system tries to manage.

## Relevance to MEC

DT synchronization couples sensing, communication, and edge compute: raw observations are gathered at the edge, must be moved over constrained links, and are rendered/maintained as the virtual model. This motivates techniques that reduce or prioritize the transmitted data — e.g. [[semantic-communication]] (send meaning, not bits) and importance-aware resource allocation — and that decide *when* and *how accurately* to update the twin under latency/energy budgets.

## In this wiki

- [[chen-2026-hc-mappo-vehicle-twin-migration]] treats [[vehicle-twin-migration]] as a vehicular-metaverse service-continuity problem, combining RSU workload prediction with UAV-assisted edge support.

- [[du-2024-yolo-semcom-digital-twin]] builds a digital twin of an apple orchard from UAV imagery ([[uav-data-collection]]): a YOLOv7-based detector extracts only the semantic content of captured images, and transmission power is allocated by per-object importance, cutting communication cost while keeping critical content accurate.
- [[yang-2024-taco-human-digital-twin-edge]] addresses **human digital twin** deployment at the edge, trading off update accuracy against cost on a two-timescale schedule.
- [[li-2023-adaptive-digital-twin-uav-iscc]] uses a DT layer to support CTDE multi-agent control in UAV-assisted ISCC, explicitly modeling DT estimation deviation rather than assuming a perfect virtual replica.
- [[he-2026-dt-sagimec-lae]] uses a cloud-side DT layer to mirror ISDs, a UAV, and the LEO-satellite relay environment in a low-altitude SAGIMEC architecture.
- [[li-2025-dt-uav-swarm-resource-management]] uses DTs for UAV-swarm task crowdsourcing and virtual traffic-flow scheduling, with [[stochastic-network-calculus]] providing pre-assessed delay bounds.
- [[belgiovine-not-in-parse-multidt-abs-deployment]] uses [[multi-digital-twin-network-optimization]] for airborne base stations: one ray-tracing twin optimizes placement/orientation/power and another validates mobile-UE scenarios and feeds coverage drops back into recovery planning.
- [[zhou-2026-multiscale-dt-uav-delivery]] uses a [[terminal-edge-multiscale-digital-twin]] for parcel delivery: edge UAVs run macro assignment twins while terminal UAVs run micro path/energy/collision-control twins.
