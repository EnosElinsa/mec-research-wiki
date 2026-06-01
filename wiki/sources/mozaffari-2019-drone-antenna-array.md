---
type: source
title: "Communications and Control for Wireless Drone-Based Antenna Array"
authors: ["Mohammad Mozaffari", "Walid Saad", "Mehdi Bennis", "Mérouane Debbah"]
year: 2019
url: "https://doi.org/10.1109/TCOMM.2018.2871453"
venue: "IEEE Transactions on Communications (IEEE TCOMM)"
tags: [source, uav-communications, collaborative-beamforming, bang-bang-control, uav-trajectory-control, virginia-tech]
related:
  - "[[collaborative-beamforming]]"
  - "[[bang-bang-control]]"
  - "[[uav-trajectory-control]]"
  - "[[drone-cell-3d-placement]]"
  - "[[mozaffari-2019-uav-wireless-tutorial]]"
  - "[[mozaffari-2017-uav-iot-energy-efficient]]"
  - "[[mohammad-mozaffari]]"
  - "[[walid-saad]]"
created: 2026-06-02
updated: 2026-06-02
---

# Communications and Control for Wireless Drone-Based Antenna Array

## Citation

Mozaffari, M., Saad, W., Bennis, M., & Debbah, M. (2019). *Communications and Control for Wireless Drone-Based Antenna Array*. **IEEE Transactions on Communications**, vol. 67. DOI: 10.1109/TCOMM.2018.2871453. (Manuscript received 2 April 2018; revised 5 August 2018; accepted 8 September 2018; date of publication 20 September 2018; date of current version 15 January 2019 → year 2019. Volume web-confirmed.)

## TL;DR

A framework for using **multiple single-antenna quadrotor drones as one aerial antenna array** that beam-steers by **physically repositioning the drones** (rather than electronic phase steering) to serve ground users in minimum **service time**. Service time has two parts: **transmission time** (inversely tied to the beamforming-gain-dependent SNR) and **control time** (moving/stabilizing the drones between serving locations). The paper minimizes transmission time by (i) optimizing inter-drone spacing to maximize array directivity — solved via **perturbation theory** as a sequence of perturbed convex problems — and (ii) placing the drones optimally per user; it minimizes control time using **bang-bang control theory**, deriving a closed-form minimum control time as a function of external forces (wind, gravity), drone weight, and destinations. This is a **UAV-communications / aerial-beamforming** entry, not an MEC offloading paper.

## Problem framing

During high-demand events, drones as flying access points can supplement limited cellular capacity/coverage. A drone-based antenna array can deliver high beamforming gain, but two gaps in prior work motivate the paper: existing UAV-antenna-array designs rely on heuristic/evolutionary directivity maximization and ignore **service-time** analysis, and the **time-optimal control** of quadrotor drones (especially under external forces) is largely unaddressed for this setting. Crucially, the array steers by moving drones, so communication performance and flight control are coupled — repositioning costs control time that trades off against the transmission time it enables.

## System model

- **Array.** L single-antenna ground users; M single-antenna quadrotor drones forming a **linear** antenna array, symmetrically excited about the array origin, with a minimum separation $D_{\min}$ for collision avoidance (linear case as a guideline for 2D/3D arrays).
- **Operation.** A **"fly-then-hover-and-transmit"** protocol: drones transmit only while stationary (the array must be stable for reliable beamforming) and reposition between users. Beam steering is achieved by adjusting drone positions, not element phases — the array gain is maximized by optimizing **drone spacing** given fixed element phases.
- **Service time.** Total service time = transmission time (∝ 1/downlink rate, a function of array beamforming gain / SNR) + control time (move + stabilize).
- **Control.** Quadrotor dynamics under external forces (wind, gravity) and drone weight; the goal is the minimum-time repositioning between optimal serving locations.

## Method

- **Drone-spacing optimization (directivity).** Maximize array directivity over inter-drone spacing using **perturbation theory**, solving successive perturbed convex optimization problems.
- **Per-user placement.** Given the optimal spacing, set the drones' locations according to each ground user's position to minimize that user's transmission time.
- **Minimum control time (bang-bang).** Optimally adjust rotor speeds; via **bang-bang control theory**, derive a closed-form expression for the minimum control time as a function of external forces, drone weight, and destinations.

## Key findings

- The drone antenna array significantly reduces service time and improves spectral/energy efficiency versus a **fixed uniform aerial antenna array** with the same number of drones, with a **32% improvement in spectral efficiency** (abstract/intro, parse).
- There is an inherent **tradeoff between control time and transmission time** as the number of drones in the array varies — more drones raise array gain (lower transmission time) but change the control burden.

## Limitations / future work

Analytical/simulation study of a **linear** array under a fly-then-hover-and-transmit protocol; the authors position the linear results as a guideline toward more complex 2D/3D array configurations. Other explicit future-work targets are `not in parse`.

## Relation to the corpus

A foundational **aerial-array beamforming** entry from the **Virginia Tech (Wireless@VT)** UAV-communications cluster, authored by [[mohammad-mozaffari]] and [[walid-saad]] alongside the same Mozaffari-Saad-Bennis-Debbah roster as their other works ([[mozaffari-2019-uav-wireless-tutorial]], [[mozaffari-2017-uav-iot-energy-efficient]]). Its drone-repositioning array is an early, physically-actuated form of the [[collaborative-beamforming|collaborative beamforming / virtual antenna array]] idea that the corpus's later aerial-CB sources develop with DRL/evolutionary solvers, and it contributes the [[bang-bang-control]] minimum-time control concept to the [[uav-trajectory-control]] thread.

## Raw artifacts

- `raw/sources/Communications_and_Control_for_Wireless_Drone-Based_Antenna_Array/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
