---
type: source
title: "Unmanned Aerial Vehicle With Underlaid Device-to-Device Communications: Performance and Tradeoffs"
authors: ["Mohammad Mozaffari", "Walid Saad", "Mehdi Bennis", "Mérouane Debbah"]
year: 2016
url: "https://doi.org/10.1109/TWC.2016.2531652"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, device-to-device-communication, stochastic-geometry-network-analysis, drone-cell-3d-placement, air-to-ground-channel-model, geometric-disk-cover, uav-communications]
related:
  - "[[device-to-device-communication]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[air-to-ground-channel-model]]"
  - "[[drone-cell-3d-placement]]"
  - "[[geometric-disk-cover]]"
  - "[[cellular-connected-uav]]"
  - "[[mozaffari-2017-uav-iot-energy-efficient]]"
  - "[[mozaffari-2019-uav-wireless-tutorial]]"
  - "[[bor-yaliniz-2016-3d-abs-placement]]"
  - "[[al-hourani-2014-optimal-lap-altitude]]"
  - "[[lyu-2017-spiral-mbs-placement]]"
  - "[[mohammad-mozaffari]]"
  - "[[walid-saad]]"
created: 2026-06-02
updated: 2026-06-08
---

# Unmanned Aerial Vehicle With Underlaid Device-to-Device Communications: Performance and Tradeoffs

## Citation

Mozaffari, M., Saad, W., Bennis, M., & Debbah, M. (2016). *Unmanned Aerial Vehicle With Underlaid Device-to-Device Communications: Performance and Tradeoffs*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2016.2531652. (Manuscript received 31 August 2015; accepted 2 February 2016; date of publication 18 February 2016; date of current version 7 June 2016. Volume/issue/pages `not in parse`.)

## TL;DR

Analyzes the **coexistence** of a UAV acting as a downlink flying base station and an **underlaid device-to-device (D2D)** network sharing the same spectrum. Using **stochastic geometry**, it derives a tractable framework for **coverage probability** and **system sum-rate**, for two cases: a **static UAV** and a **mobile UAV**. For the static case, it finds the optimal UAV **altitude** maximizing the downlink users' (DUs') coverage probability and the system sum-rate, showing the optimal altitude **decreases as D2D density increases**. For the mobile case, it uses the **disk covering problem** to compute the minimum number of **stop points** the UAV must visit to fully cover the area at minimum transmit power, derives the D2D users' overall **outage probability** under multiple retransmissions, and characterizes the **coverage-vs-delay tradeoff** (more stop points → better DU coverage but more delay and higher D2D outage).

## Problem framing

UAVs as flying base stations can boost capacity/coverage with LoS-dominant links, useful for hotspots, public-safety/disaster relief, and IoT data collection. In infrastructure-limited areas, D2D communications (underlaid, reusing licensed spectrum) also improve coverage/capacity. Deploying a UAV over a band shared with an underlaid D2D network therefore creates **interference-management** challenges that prior single-cell D2D / massive-MIMO-D2D coexistence work did not address for an *aerial* base station. The aerial setting brings three new wrinkles: the UAV–ground channel is **probabilistic LoS/NLoS** (not classical fading), the UAV **height is adjustable** (affecting channel + coverage), and UAV **mobility** adds a new dimension. The paper claims the first comprehensive fundamental analysis of UAV communication performance in the presence of underlaid D2D links.

## System model

- **Geometry.** A circular area of radius `R_c`; **downlink users (DUs)** uniformly placed with density `λ_du`; **D2D users** distributed as a homogeneous **Poisson point process** with density `λ_d` over an (assumed infinite) plane, each D2D receiver paired with a transmitter a fixed distance `d_0` away in an isotropic direction.
- **Channels.** UAV→ground uses a **probabilistic LoS/NLoS air-to-ground** model (path loss depends on altitude/elevation); BS/D2D→ground uses **Rayleigh** fading. A DU receives the desired UAV signal plus interference from all D2D transmitters; a D2D receiver gets its pair's signal plus interference from the UAV and other D2D transmitters (SINR expressions derived).
- **Static UAV.** Derive DU and D2D **coverage probabilities** and the **system sum-rate** as functions of UAV altitude and D2D density; find optimal altitude for DU coverage and for sum-rate.
- **Mobile UAV.** The UAV visits a set of stop points to serve DUs; via the **disk covering problem**, find the minimum number of stop points for full coverage at minimum transmit power; with `M` retransmissions, derive the D2D overall outage probability; define **delay** as the time to visit all stop points.

## Method

- **Stochastic-geometry derivation.** Coverage probabilities and average sum-rate are obtained analytically using PPP-based interference characterization (average D2D interference independent of user location under the infinite-PPP assumption).
- **Static-case optimization.** Altitude is optimized in closed/numerical form to maximize DU coverage and, separately, the combined DU+D2D system sum-rate.
- **Mobile-case coverage.** A three-step procedure: (1) at the optimal altitude compute the UAV's maximum coverage radius for the SINR threshold, (2) use the disk covering problem to find the minimum number of stop points + per-point coverage radius for the target area, (3) reduce UAV transmit power so its max coverage radius just meets the per-point requirement (minimum-power full coverage). Outage under retransmissions is derived per Theorem 3.

## Key findings

- An **optimal UAV altitude exists** that maximizes DU coverage probability and (separately) system sum-rate; the **optimal altitude decreases as D2D density increases**.
- A maximum system sum-rate is achievable by adjusting UAV altitude to the D2D density; for a fixed altitude, an **optimal number of D2D users** maximizing sum-rate also exists. Sum-rate rises as the D2D pair distance `d_0` shrinks (e.g. reducing `d_0` from 8 m to 5 m raises the optimal average D2D-user count by ~3×, per the parse).
- **Coverage-vs-delay tradeoff:** more stop points raise DU coverage but increase delay and D2D outage. Parse examples: raising DU coverage from 0.4 to 0.7 requires increasing stop points from 5 to 23; raising the average D2D-user count from 50 to 100 requires increasing stop points from 20 to 55. (Values are as stated in the parse for the given parameter settings.)

## Limitations / future work

The analysis is **analytical + simulation**, with a **single** UAV and a **downlink-only** scenario; D2D users are assumed to follow an infinite-area PPP (each user sees interference from infinitely many D2D transmitters), and a D2D receiver pairs with a transmitter at a **fixed** distance `d_0`. The mobile-UAV "delay" abstracts travel + per-stop transmission time. Explicit future-work statements are `not in parse`.

## Relation to the corpus

A foundational **stochastic-geometry** UAV-base-station entry from the Virginia Tech (Wireless@VT) thread of [[mohammad-mozaffari]] and [[walid-saad]], complementing their energy-efficient UAV-IoT 3D-placement work [[mozaffari-2017-uav-iot-energy-efficient]] and the [[mozaffari-2019-uav-wireless-tutorial|IEEE COMST tutorial]]. Its probabilistic-LoS [[air-to-ground-channel-model|air-to-ground channel]] and altitude-optimization theme connect to [[al-hourani-2014-optimal-lap-altitude]] and the [[drone-cell-3d-placement|drone-cell 3D placement]] of [[bor-yaliniz-2016-3d-abs-placement]]; its **disk covering** mobile-coverage formulation is the [[geometric-disk-cover]] problem also used by [[lyu-2017-spiral-mbs-placement]]. The distinguishing twist here is the **underlaid D2D coexistence** and the resulting [[device-to-device-communication|UAV–D2D]] interference tradeoffs, absent from the corpus's other aerial-base-station foundations.

## Raw artifacts

- Parse: `raw/sources/Unmanned_Aerial_Vehicle_With_Underlaid_Device-to-Device_Communications_Performance_and_Tradeoffs/full.md`
- Origin PDF: `raw/sources/Unmanned_Aerial_Vehicle_With_Underlaid_Device-to-Device_Communications_Performance_and_Tradeoffs/8090181e-977c-4e03-95bb-bdc99eb016ee_origin.pdf`
- Figures: `raw/sources/Unmanned_Aerial_Vehicle_With_Underlaid_Device-to-Device_Communications_Performance_and_Tradeoffs/images/`
