---
type: concept
title: "Random Linear Network Coding Multicast"
tags: [network-coding, multicast, reliability, packet-erasure, uav]
related:
  - "[[minimum-connection-time-trajectory]]"
  - "[[uav-trajectory-control]]"
  - "[[device-to-device-communication]]"
  - "[[zeng-2018-uav-multicasting-completion-time]]"
created: 2026-07-14
updated: 2026-07-14
---

# Random Linear Network Coding Multicast

A common-file broadcast pattern where the sender transmits random linear combinations of source packets. Any sufficiently large independent subset lets a receiver reconstruct the file, reducing dependence on packet identity and per-receiver retransmission feedback.

[[zeng-2018-uav-multicasting-completion-time]] uses RLNC so a moving UAV can serve many ground terminals over independently faded packet transmissions. The trajectory controls each terminal's packet-success probabilities and therefore the time required to reach a target recovery probability.

RLNC does not itself make trajectory design exact. The paper lower-bounds the resulting Poisson-binomial recovery probability and then applies a Gaussian approximation before route optimization.
