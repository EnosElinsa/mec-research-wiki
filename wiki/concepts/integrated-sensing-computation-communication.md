---
type: concept
title: "Integrated Sensing, Computation, and Communication (ISCC)"
tags: [isac, edge-computing, resource-allocation, federated-learning]
related:
  - "[[tang-2024-iscc-uav-feel]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[federated-learning]]"
  - "[[alternating-optimization-sdr-sca]]"
created: 2026-05-29
updated: 2026-05-29
---

# Integrated Sensing, Computation, and Communication (ISCC)

An extension of [[integrated-sensing-and-communication|ISAC]] that explicitly couples **computation** with sensing and communication, recognizing that on a resource-limited platform (e.g. a UAV) these three functions compete for the same bandwidth, energy, and time, and that platform placement affects all three.

In [[tang-2024-iscc-uav-feel]], ISCC resources (bandwidth, batch size, position) are jointly optimized with UAV deployment to minimize federated-edge-learning training time: the paper links sensing elevation angle to data-sample quality, bounds training loss via successful sensing probability, and solves the mixed-integer non-convex problem by alternating optimization (the BBPO scheme). ISCC ties the ISAC and [[federated-learning]] threads together.
