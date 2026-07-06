---
type: source
title: "Energy-Efficient UAV-Assisted Mobile Edge Computing With Secure and Reliable Data Transmission"
authors: ["Mingqian Wang", "Jianshan Zhou", "Daxin Tian", "Xuting Duan", "Kaige Qu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3629147"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-mec, physical-layer-security, secrecy-outage-probability, secure-computation-efficiency, energy-efficiency, uav-trajectory-control, chance-constraint]
related:
  - "[[physical-layer-security]]"
  - "[[secrecy-outage-probability]]"
  - "[[secure-computation-efficiency]]"
  - "[[fixed-wing-propulsion-energy-model]]"
  - "[[chance-constraint]]"
  - "[[uav-trajectory-control]]"
  - "[[task-offloading]]"
  - "[[xu-2021-secure-uav-mec-dual-uav]]"
  - "[[li-2024-irs-secure-wpmec]]"
  - "[[wang-2026-secure-lae-uav-scheduling]]"
created: 2026-07-07
updated: 2026-07-07
---

# Energy-Efficient UAV-Assisted Mobile Edge Computing With Secure and Reliable Data Transmission

## Citation

Wang, M., Zhou, J., Tian, D., Duan, X., & Qu, K. (2026). *Energy-Efficient UAV-Assisted Mobile Edge Computing With Secure and Reliable Data Transmission*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2025.3629147.

## TL;DR

Studies a single-UAV MEC cloudlet serving multiple ground users under both **passive eavesdropping** and **reliability** constraints. Each ground user has multiple transmit antennas and injects **artificial noise** in the null space of the legitimate UAV channel, while the UAV optimizes its trajectory and the users optimize local-computing, offloading, and power-allocation variables. The objective is **global secure energy efficiency**: secure offloaded bits divided by total local-computing, transmit, and UAV-flight energy. The paper derives a closed-form optimal information-vs-artificial-noise power split, converts the secrecy-outage chance constraint into a worst-case secure-rate expression, lower-bounds computation energy, and solves the coupled resource / trajectory problem with an augmented-Lagrangian iterative algorithm.

## Problem framing

UAV-mounted MEC can serve temporary or infrastructure-poor regions, but wireless offloading is exposed to eavesdroppers and unreliable air-ground links. Optimizing only energy efficiency can select high-rate trajectories and power splits that leak information or violate secrecy reliability. The paper therefore treats **security and reliability as first-class constraints** in a UAV-MEC energy-efficiency formulation rather than adding them after trajectory design.

## System model

- **Topology.** One fixed-wing UAV MEC server flies at fixed altitude $H$ over $M$ ground users. Each user is monitored by a passive eavesdropper.
- **Antennas and access.** Users have $A_T$ transmit antennas, eavesdroppers have $A_E$ receive antennas, and the UAV has one antenna. Users share spectrum by FDMA.
- **Channels.** UAV-user links are LoS air-ground channels; user-eavesdropper links follow NLoS fading. The eavesdropper is modeled conservatively with perfect CSI.
- **Security lever.** Each user splits transmit power between data and artificial noise. The artificial-noise component lies in the legitimate channel's null space, degrading the eavesdropper without hurting the UAV.
- **Energy model.** The objective includes user local-computation energy, offloading transmit energy, and UAV propulsion energy using a fixed-wing flight-energy model.
- **Constraint shape.** A secrecy-outage chance constraint bounds the probability that the target secure rate exceeds the instantaneous legitimate-minus-eavesdropper rate.

## Method

The paper first derives the optimal artificial-noise/data power ratio and a worst-case achievable secure transmission rate under the outage constraint. It then reformulates the fractional secure-energy-efficiency objective with an augmented-Lagrangian multiplier structure, lower-bounds the computation-energy terms by Jensen-style arguments, and alternates over data allocation, local CPU frequency, transmit power, and UAV trajectory. The resulting algorithm has polynomial per-iteration complexity and jointly handles the power split, secure offloading rate, and flight path.

## Key findings

- The algorithm converges in roughly 30 iterations in the reported simulation setting.
- Joint trajectory and resource optimization consistently improves **global secure energy efficiency** over no-trajectory-optimization, computation-energy-only, and transmit-energy-only baselines.
- The strongest gain is reported against the no-trajectory-optimization baseline; the paper reports up to about 13 Kbits/J higher global secure energy efficiency in the shown settings.
- Average secure energy efficiency and secure offloading rate improve most when the number of ground users is small enough for trajectory control and artificial-noise allocation to dominate contention effects.

## Limitations / future work

The threat model is passive eavesdropping with conservative eavesdropper CSI, and the evaluation is simulation-based. The authors point to active-eavesdropping countermeasures, reinforcement-learning-based adaptive power control, jamming-resilient modulation, secure downlink/backhaul design, multi-UAV coordination, dynamic channels, and time-varying computation demand as future directions.

## Relation to the corpus

This is a **secure UAV-MEC energy-efficiency** entry. It extends [[xu-2021-secure-uav-mec-dual-uav]] from secure computing capacity to secure energy efficiency and differs from [[li-2024-irs-secure-wpmec]] by using user-side artificial noise rather than IRS-assisted WPT. It also complements [[wang-2026-secure-lae-uav-scheduling]], which lets low-altitude UAVs switch between communication and jamming roles; here, the same PLS idea is embedded directly inside a UAV-MEC offloading and trajectory problem.

## Raw artifacts

- `raw/sources/Energy-Efficient UAV-Assisted Mobile Edge Computing With Secure and Reliable Data Transmission/Energy-Efficient UAV-Assisted Mobile Edge Computing With Secure and Reliable Data Transmission.md`
- Original PDF and extracted figures (`images/`) in the same folder.
