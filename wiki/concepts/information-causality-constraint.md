---
type: concept
title: "Information-Causality Constraint"
tags: [relaying, buffering, optimization-constraint, uav-communications]
related:
  - "[[xiao-2020-secrecy-energy-efficiency-relaying]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[hu-2019-uav-relay-edge-computing]]"
  - "[[fan-2026-hap-uav-iort-oee]]"
  - "[[zhang-2022-uav-relay-substitution]]"
  - "[[uav-substitution-relaying]]"
created: 2026-06-01
updated: 2026-07-14
---

# Information-Causality Constraint

In a buffer-aided (decode-and-forward) relay, the constraint that the relay **can only forward data it has already received** from the source. Formally, at any time the cumulative bits transmitted relay→destination cannot exceed the cumulative bits received source→relay up to that point. It is the information-domain analogue of the **energy-causality** constraint in energy-harvesting systems (you cannot spend energy you have not yet harvested).

## Why it matters for mobile relays

For a [[uav-mobile-relaying|UAV mobile relay]] operating in FDD, data received from the source may be **buffered for a relatively long time** while the relay flies to a better forwarding position — so the constraint binds much more strongly than in conventional static relaying with near-instantaneous forwarding. It therefore directly shapes the optimal transmit-power allocation over time: in [[zeng-2016-throughput-relaying]] the throughput-optimal source/relay power follows a **"staircase" water-filling** structure (non-increasing source level, non-decreasing relay level) precisely because of this causality coupling.

## In this wiki

- [[zeng-2016-throughput-relaying]] — introduces the constraint for UAV mobile relaying and derives its staircase water-filling consequence.
- [[hu-2019-uav-relay-edge-computing]] — carries the information-causality constraint into a UAV relay + MEC-server offloading problem (forward only already-received task bits).
- [[fan-2026-hap-uav-iort-oee]] — applies cumulative causality to IoRT-UAV-HAP collection while jointly optimizing both aerial tiers and a data-per-energy ratio.
- [[zhang-2022-uav-relay-substitution]] — schedules each half-duplex relay's receive phase before its forward phase; its HUS/SEUS service rotation is a structured two-hop-flow counterpart to the general buffered-relay constraint.
