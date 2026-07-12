---
type: concept
title: "UAV Mobile Relaying"
tags: [uav-communications, relaying, trajectory-optimization, cooperative-communication]
related:
  - "[[uav-trajectory-control]]"
  - "[[information-causality-constraint]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[post-disaster-mec]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[hu-2019-uav-relay-edge-computing]]"
  - "[[zhao-2019-uav-emergency-disasters]]"
  - "[[song-2026-thz-multiuav-mec]]"
  - "[[huang-2026-aim-uav-relay-aor]]"
  - "[[bujari-2018-stateless-fanet-routing]]"
  - "[[zhang-not-in-parse-cellular-uav-to-x]]"
  - "[[uav-to-x-communication]]"
created: 2026-06-01
updated: 2026-07-12
---

# UAV Mobile Relaying

A relaying technique in which the relay node is **mounted on a high-mobility UAV**, so its position is a **design variable** rather than fixed. Unlike conventional **static relaying**, a mobile relay can fly toward the source to receive and toward the destination to forward, **proactively constructing favorable channels** instead of waiting for opportunistic fading. This adds a degree of freedom — **relay trajectory design** — that is jointly optimized with transmit-power allocation, typically over a finite time horizon.

## Key design ingredients

- **Information-causality constraint.** Under FDD with buffering, the relay can only forward data it has **already received**; this [[information-causality-constraint]] is more binding than in instantaneous static relaying and shapes the optimal power allocation (e.g. the "staircase" water-filling structure).
- **Trajectory–power coupling.** Power should follow the movement-induced channel, while the trajectory balances the source-relay and relay-destination links — usually solved by alternating optimization with [[alternating-optimization-sdr-sca|SCA]].

## In this wiki

- [[zeng-2016-throughput-relaying]] is the foundational anchor: it maximizes end-to-end throughput over relay trajectory + source/relay power and derives the staircase water-filling power structure.
- [[hu-2019-uav-relay-edge-computing]] carries the same information-causality + SCA machinery into **MEC**, letting one UAV be an edge server **and** a relay to an access point (a compute-offloading objective rather than throughput).
- [[zhao-2019-uav-emergency-disasters]] uses **multihop UAV relaying** (AF/DF, optimized hovering positions) as one pillar of a post-disaster emergency-network framework.
- [[song-2026-thz-multiuav-mec]] uses multiple UAVs as THz communication relays between IoT devices and MEC servers, with relay selection and UAV deployment optimized against MEC queueing delay.
- [[huang-2026-aim-uav-relay-aor]] adds antenna-pattern-aware relay-chain deployment: each relay state includes both 3-D position and heading, and AIM minimizes relay count while satisfying per-link RSS thresholds.
- [[bujari-2018-stateless-fanet-routing]] is the packet-routing complement: it compares stateless geographic forwarding protocols for FANETs where UAV nodes relay packets without maintaining end-to-end routes.
- [[zhang-not-in-parse-cellular-uav-to-x]] uses high-SNR UAVs as opportunistic relays for low-SNR sensing UAVs; the relay caches U2U data and uploads it over U2N, while speed rather than path geometry is optimized.
