---
type: concept
title: "Energy-Balanced Cooperative UAV Relaying"
tags: [uav-relay, cooperative-communication, energy-balancing, packet-scheduling, rate-adaptation]
related:
  - "[[li-2016-energy-balanced-uav-relaying]]"
  - "[[uav-mobile-relaying]]"
  - "[[energy-balancing-uav]]"
  - "[[uav-data-collection]]"
  - "[[zeng-2016-throughput-relaying]]"
created: 2026-07-13
updated: 2026-07-13
---

# Energy-Balanced Cooperative UAV Relaying

Energy-balanced cooperative UAV relaying assigns decoded packets, modulation levels, and derived transmit powers across several airborne relays to reduce the largest forwarding-energy expenditure. In [[li-2016-energy-balanced-uav-relaying]], the objective is min-max relay energy under packet-success and deadline constraints rather than minimum aggregate energy; its reported network lifetime is time until all UAV batteries are exhausted, not first-relay failure.

[[li-2016-energy-balanced-uav-relaying]] centralizes UAV reports of decoded packets and first-hop reception quality, while the base station measures second-hop SNRs. Its EPLA heuristic alternates transfers from the highest-energy to the lowest-energy relay with rate increases needed to satisfy a TDMA deadline, approaching a small-instance binary-integer scheduler at much lower runtime.

This is a scheduling-centered form of [[uav-mobile-relaying]]. It differs from [[zeng-2016-throughput-relaying]], where trajectory and source/relay powers are optimized under information causality. The cited EPLA results count forwarding transmit energy and therefore do not establish propulsion-aware fleet lifetime.
