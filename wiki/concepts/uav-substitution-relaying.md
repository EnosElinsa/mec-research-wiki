---
type: concept
title: "UAV Substitution Relaying"
tags: [uav, relaying, endurance, trajectory-optimization, power-control, cooperative-communication]
related:
  - "[[zhang-2022-uav-relay-substitution]]"
  - "[[uav-mobile-relaying]]"
  - "[[information-causality-constraint]]"
  - "[[uav-trajectory-control]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[liu-2026-usp-nfrp-emergency-communication]]"
  - "[[persistent-emergency-uav-swarm-service]]"
created: 2026-07-12
updated: 2026-07-12
---

# UAV Substitution Relaying

UAV substitution relaying extends a relay connection beyond one aircraft's flight duration by rotating multiple UAVs through service. A simple schedule lets one half-duplex relay receive and forward before the next takes over; an overlapped schedule lets one UAV forward while its successor receives, improving spectrum use but creating inter-relay interference.

[[zhang-2022-uav-relay-substitution]] calls these HUS and SEUS and jointly controls relay trajectories and source/relay powers. The concept extends [[uav-mobile-relaying]] from a single finite-horizon mobile relay to a persistent multi-UAV service schedule while retaining the trajectory-power and two-hop flow structure of [[zeng-2016-throughput-relaying]].

[[liu-2026-usp-nfrp-emergency-communication]] generalizes the replacement idea from one source-destination flow to [[persistent-emergency-uav-swarm-service]] over several access areas. Its UAVs rotate through access/fixed-relay/non-fixed-relay roles while tree links are reconfigured during movement.
