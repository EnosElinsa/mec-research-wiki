---
type: concept
title: "Full-Duplex NOMA UAV Relay"
tags: [uav-relay, full-duplex, noma, decode-and-forward, sic]
related:
  - "[[li-2026-full-duplex-noma-uav-relay]]"
  - "[[noma]]"
  - "[[uav-mobile-relaying]]"
  - "[[robust-uav-position-power-optimization]]"
created: 2026-07-14
updated: 2026-07-14
---

# Full-Duplex NOMA UAV Relay

A full-duplex NOMA UAV relay pipelines decode-and-forward service across slots: while the terrestrial base station broadcasts the next message, the UAV forwards the message decoded in the previous slot. A cell-edge user applies successive interference cancellation and combines its direct and relayed observations.

The protocol in [[li-2026-full-duplex-noma-uav-relay]] assumes perfect self-interference cancellation at the UAV and perfect SIC at the user. Its simulated spectral-efficiency advantage therefore describes an ideal full-duplex physical layer; residual cancellation errors, relay motion during a solve, and propulsion energy are outside the model.
