---
type: concept
title: Cellular-Connected UAV
tags: [uav-communications, cellular-network, aerial-user, 5g]
related:
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[blockage-aware-channel-model]]"
created: 2026-05-31
updated: 2026-05-31
---

# Cellular-Connected UAV

One of the two complementary UAV-communications paradigms framed by the tutorial [[zeng-2019-uav-comm-tutorial-5g]]. In the **cellular-connected UAV** paradigm, UAVs are integrated into the network as **aerial users** served by existing terrestrial cellular infrastructure — the inverse of the **UAV-assisted communications** paradigm, where UAVs act as aerial base stations/relays serving ground users (the view taken by most [[multi-uav-assisted-mec]] sources).

## Why it is distinct

Serving UAVs as users introduces issues that ground users do not raise:

- **LoS-dominant air-ground channels** that, while improving signal strength, also cause strong aerial-terrestrial **interference** (a UAV "sees" many cells at once).
- **CNPC vs payload QoS asymmetry** — control-and-non-payload links need very high reliability and low latency at low data rate, while payload data is application-dependent and can be high rate.
- **3-D mobility** as a controllable degree of freedom, motivating [[uav-trajectory-control|trajectory design]] for connectivity rather than only coverage.

The tutorial uses this dichotomy to organize the UAV-communications design space; the concept anchors the "UAV as network user" thread distinct from the "UAV as edge server" thread that dominates the MEC corpus.
