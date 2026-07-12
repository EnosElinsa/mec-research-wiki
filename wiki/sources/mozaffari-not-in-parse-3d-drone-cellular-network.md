---
type: source
title: "Beyond 5G With UAVs: Foundations of a 3D Wireless Cellular Network"
authors: ["Mohammad Mozaffari", "Ali Taleb Zadeh Kasgari", "Walid Saad", "Mehdi Bennis", "Merouane Debbah"]
year: ""
url: ""
venue: ""
tags: [source, uav-communications, drone-cell, cellular-connected-uav, frequency-reuse, optimal-transport, wireless-backhaul]
related:
  - "[[drone-cell-3d-placement]]"
  - "[[cellular-connected-uav]]"
  - "[[three-dimensional-frequency-reuse]]"
  - "[[optimal-transport-theory]]"
  - "[[wireless-backhaul]]"
  - "[[non-terrestrial-network]]"
  - "[[mohammad-mozaffari]]"
  - "[[walid-saad]]"
created: 2026-07-11
updated: 2026-07-11
---

# Beyond 5G With UAVs: Foundations of a 3D Wireless Cellular Network

## Citation

Mozaffari, M., Kasgari, A. T. Z., Saad, W., Bennis, M., & Debbah, M. *Beyond 5G With UAVs: Foundations of a 3D Wireless Cellular Network*. Venue / year / DOI: **not in parse**.

## TL;DR

Introduces a fully aerial 3-D cellular network where low-altitude drone-BSs serve cellular-connected drone-UEs and HAP drones provide FSO backhaul. The paper combines truncated-octahedron deployment and frequency reuse with kernel-density estimation of drone-UE distributions and optimal-transport-based cell association to reduce total latency.

## Problem

Standard UAV cellular models are usually 2-D or treat UAVs as either aerial base stations or aerial users, not both in a volumetric network. This paper asks how to cover a 3-D service volume with drone-BSs and then associate mobile drone-UEs to cells while accounting for transmission, backhaul, and computation latency rather than SINR alone.

## System model

- The architecture contains `L` drone-UEs, `N` LAP drone-BSs, and HAP drones.
- Drone-BSs provide downlink access with omni-directional antennas; HAP drones supply LoS FSO backhaul.
- The 3-D service region is tessellated by truncated octahedra, placing drone-BSs at cell centers and deriving feasible integer frequency reuse factors.
- A kernel density estimator with cross-validation estimates the 3-D spatial distribution `f(x,y,z)` of drone-UEs over a deployment period.

## Method

The network-planning stage fills the desired volume with truncated-octahedron cells, then derives drone-BS positions and frequency-reuse geometry. The association stage formulates latency-minimal 3-D cell partitions using optimal transport theory. The objective is to minimize average total latency under disjoint/full-cover partitions, where total latency includes access transmission, HAP backhaul, and drone-BS computation delay.

## Key findings

- The abstract and contribution text report up to about 46% average-latency reduction relative to SINR-based association.
- In the plotted comparison, the proposed association gives 43.9% average total-latency reduction versus SINR association.
- The simulation table uses carrier frequency 2 GHz, drone-BS transmit power 0.5 W, noise spectral density -170 dBm/Hz, `L = 200`, per-drone-BS bandwidth 10 MHz, path-loss exponent 2, path-loss constant `1.42 x 10^-4`, packet size 10 kb, reuse factor 1, and backhaul rate `(100+n) Mb/s`.
- To satisfy a 70 ms maximum total-latency target, the proposed association needs 57% less transmission bandwidth than the SINR baseline.
- The iterative optimal-transport association algorithm converges within 6 iterations in the parsed figure discussion.

## Limitations / parse caveats

The local parse lacks a publication metadata header and DOI. Some math symbols and the cubic-space size are corrupted, so this page avoids depending on missing volume dimensions. The paper is a communication/network-planning foundation, not MEC offloading, although its latency model includes computation delay at drone-BSs.

## Relation to the corpus

This source extends the [[drone-cell-3d-placement]] and [[cellular-connected-uav]] foundations by combining UAV-as-base-station and UAV-as-user roles in the same 3-D network. It also gives [[three-dimensional-frequency-reuse]] another truncated-octahedron use case and adds an [[optimal-transport-theory]] example for 3-D aerial cell association.

## Raw artifacts

- `raw/sources/Beyond_5G_With_UAVs_Foundations_of_a_3D_Wireless_Cellular_Network/Beyond_5G_With_UAVs_Foundations_of_a_3D_Wireless_Cellular_Network.md`
- Original PDF and extracted figures (`images/`) in the same folder.
