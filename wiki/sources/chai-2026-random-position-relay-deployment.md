---
type: source
title: "Transmission Time Minimization-Based UAV Deployment and Resource Allocation With Random User Position Information"
authors: ["Rong Chai", "Huiling Wang", "Hong Chen", "Lin He", "Ruijin Sun", "Qianbin Chen"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3602956"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 921-932"
tags: [source, uav-relay, satellite, statistical-user-position, deep-q-network, device-association, physical-layer-security]
related:
  - "[[statistical-user-position-uav-deployment]]"
  - "[[deep-q-network]]"
  - "[[multi-agent-q-learning]]"
  - "[[device-association]]"
  - "[[uav-mobile-relaying]]"
  - "[[physical-layer-security]]"
  - "[[noma]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[rong-chai]]"
  - "[[qianbin-chen]]"
created: 2026-07-14
updated: 2026-07-14
---

# Transmission Time Minimization-Based UAV Deployment and Resource Allocation With Random User Position Information

## Citation

Chai, R., Wang, H., Chen, H., He, L., Sun, R., & Chen, Q. (2026). *Transmission Time Minimization-Based UAV Deployment and Resource Allocation With Random User Position Information*. **IEEE Transactions on Green Communications and Networking, 10**, 921-932. DOI: 10.1109/TGCN.2025.3602956.

## TL;DR

Models unknown ground-user positions with a truncated Gaussian density, trains independent DQN agents for relay-UAV grid placement and satellite-link power, and alternates that learned control with shortest-transmission-time association plus greedy load balancing.

## System and method

Ground users upload through fixed-altitude aerial relays to a satellite while a UAV eavesdropper threatens the first hop. OFDMA supports ground access and NOMA supports relay-satellite forwarding. The expected objective sums two-hop transmission time over the user-position density.

Each relay agent chooses a neighboring grid move or stay action and one discretized power level. All agents receive negative total transmission time. Given deployment and powers, users select the relay with shortest modeled time; a greedy repair shifts users from overloaded relays to their second choice.

## Findings and guarantee scope

The DQN/greedy embedded loop has no global/local optimality, monotonicity, feasibility, or convergence theorem for the joint problem. In simulation, the proposed association is more balanced than K-means and reports transmission-time gains over three baselines under selected bandwidth, power, and noise settings.

## Limitations

Simulation only; fixed-altitude grid deployment, static users, known density and demand, discretized power, direct satellite links, and simplified secrecy rates. The written association constraint permits unserved users, secrecy rate lacks a positive-part operator, and the online routine nevertheless assumes exact user coordinates. The greedy repair does not explicitly recheck every formal capacity constraint, and summing relay times is not justified as wall-clock completion time under parallel operation.

## Relation to the corpus

This source links [[statistical-user-position-uav-deployment]] to [[device-association]] in a satellite-aerial relay setting. Unlike deterministic deployment pages that optimize from known coordinates, it integrates the placement objective over a user density, yet its association and load-balancing routine still depends on realized positions; the page therefore keeps statistical planning and online assignment as distinct mechanisms.

## Raw artifacts

- Parse: `raw/sources/Transmission_Time_Minimization-Based_UAV_Deployment_and_Resource_Allocation_With_Random_User_Position_Information/Transmission_Time_Minimization-Based_UAV_Deployment_and_Resource_Allocation_With_Random_User_Position_Information.md`
- Original PDF and extracted figures are in the same folder.
