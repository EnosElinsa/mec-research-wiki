---
type: source
title: "QoE Maximization for Laser-Powered Multi-UAV Communication Networks"
authors: ["Jianchao Chen", "Ming Jiang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3610026"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 2, pp. 2676-2690"
tags: [source, laser-power-transfer, multi-uav, qoe, matching, resource-reallocation, post-disaster-communication]
related:
  - "[[laser-power-transfer]]"
  - "[[gale-shapley-rematching]]"
  - "[[redundant-resource-reallocation]]"
  - "[[qoe-modeling-mec]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[device-association]]"
  - "[[wireless-backhaul]]"
created: 2026-07-14
updated: 2026-07-14
---

# QoE Maximization for Laser-Powered Multi-UAV Communication Networks

## Citation

Chen, J., & Jiang, M. (2026). *QoE Maximization for Laser-Powered Multi-UAV Communication Networks*. **IEEE Transactions on Mobile Computing, 25**(2), 2676-2690. DOI: 10.1109/TMC.2025.3610026.

## TL;DR

Places laser-charged UAV access points in a post-disaster downlink, rematches users and laser stations, then reclaims excess power and backhaul from already-qualified users to maximize how many meet rate- and delay-derived QoE thresholds.

## Problem and system model

A surviving macro base station and multiple UAV access points serve ground users, while distributed laser-power-transfer stations charge the UAVs. Ground users associate with either the BS or one UAV; each laser station associates with one UAV. BS and UAV access use orthogonal bands, but different UAVs interfere. UAV delivery uses BS-UAV backhaul followed by UAV-user access, while optical charging can continue in parallel.

QoE requires a user-specific minimum average data rate and a mean-opinion-score-derived delay threshold. The decisions are UAV placement, user and laser-station association, transmit power, and backhaul allocation. This is a communication network, not an edge-computing/offloading model.

## Method

The QWLMU procedure first maximizes sum average data rate by alternating placement and association. [[gale-shapley-rematching]] repairs locally poor conventional matches, while an L2-norm polynomial reformulation handles UAV placement. [[redundant-resource-reallocation]] then takes excess power and backhaul from users already meeting QoE and alternates block-SCA/quadratic-transform updates to qualify more users.

## Key findings

- In 10,000 random matching instances, rematching gives positive normalized weight gain over ordinary Gale-Shapley matching and converges after a few iterations.
- In the four-laser-station/four-UAV simulation, increasing laser transmit power from 600 to 2000 W eventually saturates average-data-rate gains.
- The placement-and-association stage outperforms ordinary matching and compared placement methods in system average data rate, especially at low-to-medium altitude or with more users; the text gives no exact margin.
- At the evaluated 60 m and 300 m altitudes, placement optimization increases the number of QoE-qualified users, and redundant-resource reallocation increases it further.
- QWLMU reports higher simulated energy efficiency than the compared LGD-UPS and MWEP methods, without a text-level exact percentage.

## Limitations

Evidence is simulation-only. The first stage converges to a stationary, not globally optimal, solution. Laser alignment is assumed manageable for slowly moving or hovering UAVs; weather, blockage, alignment error, eye safety, and a physical laser-power prototype are not evaluated. Channels and user layouts are synthetic, small-scale fading is assumed estimable, and multiple band/slot orthogonality assumptions simplify interference.

## Relation to the corpus

This source adds [[laser-power-transfer]] to UAV communication and separates threshold satisfaction from sum-throughput maximization. It is adjacent to laser-powered aerial MEC, but no computation tasks or CPUs are modeled here.

## Raw artifacts

- Parse: `raw/sources/QoE_Maximization_for_Laser-Powered_Multi-UAV_Communication_Networks/QoE_Maximization_for_Laser-Powered_Multi-UAV_Communication_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
