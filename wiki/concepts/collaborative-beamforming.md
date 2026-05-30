---
type: concept
title: Collaborative Beamforming (Virtual Antenna Array)
tags: [beamforming, antenna-array, aerial-communications, satellite, physical-layer]
related:
  - "[[sun-2025-emoppo-vlh-aerial-cb]]"
  - "[[li-2024-emodrl-ground-space-cb]]"
  - "[[zhang-2024-gdmtd3-aerial-secure-cb]]"
  - "[[sun-2024-imssa-uav-secure-cb]]"
  - "[[li-2024-emssa-uav-swarm-vaa]]"
  - "[[physical-layer-security]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[collaborative-beamforming-in-aerial-mec]]"
created: 2026-05-31
updated: 2026-06-01
---

# Collaborative Beamforming (Virtual Antenna Array)

A technique where multiple distributed transmitters (AAVs/UAVs, or ground terminals) synchronize and adjust their carrier phases / excitation-current weights to act as a single **virtual antenna array**, forming a high-gain mainlobe directed at a remote receiver. Because the received power scales with the square of the number of array elements, collaborative beamforming (CB) extends communication distance and improves interference resistance without modifying existing devices.

## Two flavors in this wiki

| Flavor | Array elements | Receiver | Source |
|---|---|---|---|
| Aerial CB (UVAA) | A swarm of AAVs | Terrestrial mobile user | [[sun-2025-emoppo-vlh-aerial-cb]] |
| Distributed CB (DCB) | Energy-limited ground terminals | LEO satellite (uplink) | [[li-2024-emodrl-ground-space-cb]] |
| Dual CB (GVAA + AVAA) | IoT sensors **and** UAVs simultaneously | Remote base stations | [[li-2024-emssa-uav-swarm-vaa]] |
| Secure CB (diffusion-DRL) | UAV swarm | Remote base station, vs eavesdroppers | [[zhang-2024-gdmtd3-aerial-secure-cb]] |
| Secure CB (swarm-intelligence) | UVAA of UAVs | Cluster of base stations, vs imperfect/unknown eavesdroppers | [[sun-2024-imssa-uav-secure-cb]] |

A cross-source map of how these five sources differ in target, objectives, and solver lives in [[collaborative-beamforming-in-aerial-mec]].

## Design tension

The beam pattern depends on the array elements' positions and excitation weights. For aerial CB, the AAVs' stochastic 3-D positions disrupt the pattern, and improving it requires flying — which costs energy. This makes CB a natural **multi-objective** problem (rate or secrecy vs flight energy), which is why the corpus's CB sources reach for [[multi-objective-reinforcement-learning]] and evolutionary policy-set methods. CB is also a lever for [[physical-layer-security]] (directing energy at the legitimate receiver, away from eavesdroppers).
