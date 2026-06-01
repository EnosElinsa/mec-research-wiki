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
created: 2026-06-02
updated: 2026-06-02
---

# Digital Twin

A **digital twin (DT)** is a continuously-updated virtual replica of a physical object, process, or environment. Because the physical world changes over time, a DT must be repeatedly **synchronized** with fresh measurements collected by edge devices (sensors, cameras, UAVs), which makes DTs a heavy and recurring data-transmission workload for the wireless edge — the data volume needed to keep the twin accurate is exactly the cost a DT system tries to manage.

## Relevance to MEC

DT synchronization couples sensing, communication, and edge compute: raw observations are gathered at the edge, must be moved over constrained links, and are rendered/maintained as the virtual model. This motivates techniques that reduce or prioritize the transmitted data — e.g. [[semantic-communication]] (send meaning, not bits) and importance-aware resource allocation — and that decide *when* and *how accurately* to update the twin under latency/energy budgets.

## In this wiki

- [[du-2024-yolo-semcom-digital-twin]] builds a digital twin of an apple orchard from UAV imagery ([[uav-data-collection]]): a YOLOv7-based detector extracts only the semantic content of captured images, and transmission power is allocated by per-object importance, cutting communication cost while keeping critical content accurate.
- [[yang-2024-taco-human-digital-twin-edge]] addresses **human digital twin** deployment at the edge, trading off update accuracy against cost on a two-timescale schedule.
