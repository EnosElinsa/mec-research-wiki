---
type: concept
title: "Terminal-Edge Multiscale Digital Twin"
tags: [digital-twin, edge-computing, uav-delivery, graph-matching, multi-agent-reinforcement-learning]
related:
  - "[[zhou-2026-multiscale-dt-uav-delivery]]"
  - "[[digital-twin]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[graph-neural-network]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[multi-agent-q-learning]]"
  - "[[uav-delivery-pickup-dropoff]]"
created: 2026-07-13
updated: 2026-07-13
---

# Terminal-Edge Multiscale Digital Twin

A terminal-edge multiscale digital twin decomposes one complex physical-system twin by decision scale and execution location. An edge-run macro twin handles broad assignment and coordination, while terminal-run micro twins make local motion and resource decisions from finer observations.

[[zhou-2026-multiscale-dt-uav-delivery]] uses graph matching at the macro scale to associate parcel clusters with UAV groups. Competitive and cooperative [[multi-agent-q-learning]] at the micro scale then selects UAV-parcel associations, velocities, and paths under energy, latency, payload, and collision considerations. Decisions feed between scales so local execution can refine later macro coordination.

This differs from [[multi-digital-twin-network-optimization]], where separate twins provide different planning and validation environments for the same network design. Multiscale decomposition instead partitions strategic and operational decisions across edge and terminal computing tiers; its benefit depends on timely state exchange and sufficient edge/terminal compute capacity.
