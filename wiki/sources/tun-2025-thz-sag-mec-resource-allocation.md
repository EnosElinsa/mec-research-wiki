---
type: source
title: "Joint UAV Deployment and Resource Allocation in THz-Assisted MEC-Enabled Integrated Space-Air-Ground Networks"
authors: ["Yan Kyaw Tun", "György Dán", "Yu Min Park", "Choong Seon Hong"]
year: 2025
url: "https://doi.org/10.1109/TMC.2024.3516655"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 24, no. 5, May 2025"
tags: [source, space-air-ground-integrated-network, terahertz-communication, task-offloading, resource-allocation, uav-deployment, matching-game, successive-convex-approximation, bsum]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[terahertz-communication]]"
  - "[[task-offloading]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[block-successive-upper-bound-minimization]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[two-stage-decomposition]]"
  - "[[zhou-2021-delay-sagin-task-scheduling]]"
created: 2026-07-07
updated: 2026-07-07
---

# Joint UAV Deployment and Resource Allocation in THz-Assisted MEC-Enabled Integrated Space-Air-Ground Networks

## Citation

Tun, Y. K., Dán, G., Park, Y. M., & Hong, C. S. (2025). *Joint UAV Deployment and Resource Allocation in THz-Assisted MEC-Enabled Integrated Space-Air-Ground Networks*. **IEEE Transactions on Mobile Computing**, 24(5), 3794-3808. DOI: 10.1109/TMC.2024.3516655.

## TL;DR

Formulates energy minimization for THz-assisted MEC-enabled [[space-air-ground-integrated-network|SAG]] networks. Ground devices offload over short-range THz access links to UAVs; UAVs can compute locally, collaborate with neighboring UAVs, or forward tasks over mmWave backhaul to LEO satellites. A BCD framework decomposes the non-convex mixed-integer problem into device offloading, THz sub-band/power control, UAV deployment, and UAV task-offloading subproblems solved with convex optimization, matching/CCP, SCA, and [[block-successive-upper-bound-minimization|BSUM]].

## Problem

Remote and disaster-area IoT devices may lack terrestrial base stations but still need low-latency computation. SAG networks can combine UAV and LEO resources, while [[terahertz-communication]] supplies high-rate device-to-UAV access. THz links are short-range and blockage/attenuation sensitive, so energy-efficient operation requires jointly choosing offloaded fractions, sub-band assignment, transmit power, UAV locations, and UAV-to-UAV/UAV-to-satellite task forwarding.

## System model

- The system has J wireless devices, K UAVs, and S LEO satellites.
- Devices have latency-sensitive tasks characterized by maximum tolerable delay, CPU cycles per bit, and data size.
- Device-to-UAV access uses THz OFDMA sub-bands with frequency reuse across UAVs, so inter-cell interference can occur.
- UAV-UAV and UAV-satellite backhaul uses 28 GHz mmWave links.
- UAVs may process tasks locally, transfer them to other UAVs, or offload to LEO satellites; satellite energy is ignored because satellites are assumed to have renewable energy sources.
- Device-to-UAV association is initially determined by distance using K-means clustering.

## Method

The paper minimizes total energy consumed by devices and UAVs under delay, THz resource, and transmit-power constraints. It decomposes the problem with BCD:

- device task-offloading decisions solved as a convex subproblem;
- THz sub-band assignment and power control solved by a one-to-one matching game and concave-convex procedure;
- UAV deployment solved by successive convex approximation;
- UAV task-offloading decisions solved with BSUM after relaxing binary forwarding variables.

## Key findings

- The proposed algorithm reports the lowest total device+UAV energy across network sizes compared with all-local computing and no-UAV-collaboration baselines.
- The energy gap versus baselines widens as the number of devices grows, indicating better scaling in the simulated network.
- UAV collaboration matters: sending excess tasks directly to LEO satellites consumes more energy than using neighboring UAVs when available.
- Variant studies show task-offloading fraction and THz sub-band assignment are the most influential decision variables for energy; all-offload, fixed-offload, and random-sub-band variants are much worse than the full optimization.
- The proposed method has a low optimality gap in the tested sub-band assignment comparison against exhaustive optimal search.
- For the simulated 600 m by 600 m area, four UAVs provide nearly the same energy benefit as six or eight UAVs before counting additional hovering energy and hardware cost.

## Limitations / future work

The evaluation is simulation-only and uses fixed device-UAV association from K-means before optimization. The paper assumes static UAV/satellite locations for the simulation and ignores satellite energy consumption. Future work targets mobility of devices, UAVs, and satellites over time, which would require time-slot-dependent channel gains, re-association, and dynamic offloading/resource decisions.

## Relation to the corpus

This is a bridge between the wiki's SAGIN task-offloading track and the THz/MEC channel-resource track. It complements [[zhou-2021-delay-sagin-task-scheduling]], where SAGIN offloading is learned through risk-sensitive RL, and [[wu-2025-iopo-irs-uav-thz-mec]], where THz UAV-MEC uses IRS phases and learned offloading. Here the novelty is the four-block classical optimization stack over THz access, UAV collaboration, and LEO fallback.

## Raw artifacts

- `raw/sources/Joint UAV Deployment and Resource Allocation in THz-Assisted MEC-Enabled Integrated Space-Air-Ground Networks/Joint UAV Deployment and Resource Allocation in THz-Assisted MEC-Enabled Integrated Space-Air-Ground Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
