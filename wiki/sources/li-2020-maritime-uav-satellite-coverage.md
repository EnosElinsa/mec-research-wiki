---
type: source
title: "Maritime Coverage Enhancement Using UAVs Coordinated With Hybrid Satellite-Terrestrial Networks"
authors: ["Xiangling Li", "Wei Feng", "Yunfei Chen", "Cheng-Xiang Wang", "Ning Ge"]
year: 2020
url: "https://doi.org/10.1109/TCOMM.2020.2966715"
venue: "IEEE Transactions on Communications (IEEE TCOM)"
tags: [source, maritime-mec, uav-trajectory-control, air-to-ground-channel-model, overlay-underlay-spectrum-access, wireless-backhaul, alternating-optimization-sdr-sca, csi-estimation-error]
related:
  - "[[maritime-mec]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[overlay-underlay-spectrum-access]]"
  - "[[wireless-backhaul]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[csi-estimation-error]]"
  - "[[non-terrestrial-network]]"
  - "[[wu-2024-satellite-maritime-spectrum-sharing]]"
  - "[[liu-2025-haps-uav-maritime-iot]]"
  - "[[wang-2024-twotier-satellite-marine]]"
  - "[[zeng-2017-energy-efficient-uav-trajectory]]"
  - "[[mozaffari-2019-uav-wireless-tutorial]]"
created: 2026-06-02
updated: 2026-06-02
---

# Maritime Coverage Enhancement Using UAVs Coordinated With Hybrid Satellite-Terrestrial Networks

## Citation

Li, X., Feng, W., Chen, Y., Wang, C.-X., & Ge, N. (2020). *Maritime Coverage Enhancement Using UAVs Coordinated With Hybrid Satellite-Terrestrial Networks*. **IEEE Transactions on Communications**. DOI: 10.1109/TCOMM.2020.2966715. (Manuscript received 4 April 2019; revised 6 September and 26 November 2019; accepted 5 January 2020; date of publication 15 January 2020; date of current version 16 April 2020 → year 2020. Presented in part at IEEE WOCC 2019.)

## TL;DR

Deploys **fixed-wing UAVs** as on-demand aerial base stations to enhance broadband coverage in a **hybrid satellite-UAV-terrestrial maritime communication network**, where UAVs share spectrum with satellites and use terrestrial base stations (TBSs) or satellites for wireless backhaul. The UAV's **whole trajectory and in-flight transmit power** are jointly optimized to **maximize the minimum ergodic achievable rate** of a mobile ship-user over the service interval, subject to UAV kinematics, tolerable interference to satellite-served users, backhaul, and total communication-energy constraints. The defining twist: only **location-dependent large-scale CSI** is assumed available (small-scale CSI cannot be obtained before takeoff), with ship positions obtained from the maritime Automatic Identification System (AIS); the UAV cannot land at sea, so its trajectory must be **pre-planned** before takeoff. The resulting non-convex problem is solved by **problem decomposition + successive convex optimization + bisection search**. This is a communication-layer (coverage/rate) paper, not an MEC computation-offloading paper.

## Problem framing

Maritime activity is driving demand for broadband at sea, but satellites (GEO/LEO) have rate-limited, long-delay links and TBSs along the coast have limited range; low-end ships without high-gain antennas struggle even inside satellite coverage. UAVs can fill this gap as agile aerial base stations with strong LoS, but the open question is how to **coordinate UAVs with existing satellites and terrestrial systems** — specifically spectrum sharing (and the interference it creates) and backhaul. Two practical constraints shape the formulation: (i) small-scale CSI is unavailable before takeoff and (ii) the UAV cannot replenish energy or land on the sea, so it must journey from coast to ocean and back along a trajectory **designed in advance** from large-scale CSI (path loss + Rician factor), which the authors argue is more practical than the perfect-CSI assumptions of prior trajectory-design work.

## System model

- **Topology.** Mobile users are **ships** (following fixed shipping routes). TBSs serve coastal waters; maritime satellites cover beyond TBS range. UAVs are dispatched on demand: a high-rate request travels ship → nearest TBS → central processor, which sends an idle UAV to serve the user from $t_s$ to $t_e$, after which the UAV returns to the coast. Each UAV serves a single user; UAVs are sparsely distributed and use orthogonal resources to avoid mutual interference.
- **Spectrum & interference.** UAVs **share spectrum with satellites**; interference on UAV-served users from satellites is neglected (lower user antenna gain), but the UAV's leakage interference onto satellite-served users is constrained by an interference-temperature limit $I_0$.
- **Channel.** A composite channel with **both large-scale and small-scale fading**: log-distance path loss with a log-normal shadowing term plus **Rician** small-scale fading. The ergodic achievable rate is taken over the small-scale fading. Crucially, only the **large-scale CSI** (path loss, Rician factor $K$), which is location-dependent and obtainable from historical/pre-measured data, is assumed known; the random small-scale term is unknown before takeoff.
- **Backhaul & energy.** UAVs need wireless backhaul via TBSs (primary, near the coast) or satellites; the paper focuses on TBS-assisted backhaul but also studies satellite-assisted backhaul. UAV kinematics use velocity/acceleration/height bounds; a total allowable **communication energy** $E_0$ over travel time $T_0$ constrains transmit power.
- **Objective.** Maximize the **minimum ergodic achievable rate** of the UAV-served user over the whole travel time, over the UAV trajectory and in-flight transmit power.

## Method

The joint trajectory-and-power problem is **non-convex**. The authors **decompose** it and apply **successive convex optimization (SCA)** together with **bisection search** in an iterative algorithm: optimizing transmit power and trajectory in alternation, with the bisection handling the max-min rate target. Because only large-scale CSI is used, the ergodic-rate expressions are evaluated/approximated without instantaneous small-scale CSI, letting the whole trajectory be computed before the UAV is deployed.

## Key findings

- Joint optimization of UAV trajectory and transmit power using **only large-scale CSI** is reported to achieve a **significant performance gain** and to let the UAV "fit well" with the existing satellite and terrestrial systems. Specific numeric margins are figure-derived; treat exact values as indicative.
- Demonstrates that **pre-deployment** trajectory planning (required because the UAV cannot land at sea) is feasible from location-dependent large-scale CSI plus AIS-derived ship positions.

## Limitations / future work

The system model is deliberately simplified to focus on UAV-satellite spectrum sharing: each UAV serves one user, UAVs are sparsely distributed using orthogonal resources, inter-UAV interference and detailed user-association among UAVs are set aside (referenced to prior work), and the earth surface is treated as flat (valid only over short distances). The evaluation is simulation-based. Explicit future-work statements are `not in parse`.

## Relation to the corpus

A **communication-layer** maritime entry (coverage and rate, not computation offloading), distinctive for its **large-scale-CSI-only**, pre-planned fixed-wing trajectory design and its explicit three-way (satellite/UAV/terrestrial) spectrum-sharing and backhaul coordination. It sits beside the satellite-maritime VDES spectrum-sharing work [[wu-2024-satellite-maritime-spectrum-sharing]] as another spectrum-coordination entry on the maritime track, and complements the HAP-UAV maritime IoT communication design of [[liu-2025-haps-uav-maritime-iot]] and the two-tier satellite-marine offloading of [[wang-2024-twotier-satellite-marine]]. Its trajectory/SCA machinery connects to [[zeng-2017-energy-efficient-uav-trajectory]] (fixed-wing trajectory optimization) and the UAV-as-aerial-base-station framing of [[mozaffari-2019-uav-wireless-tutorial]]; the CSI-availability concern grounds [[csi-estimation-error]] and the satellite-UAV co-channel sharing grounds [[overlay-underlay-spectrum-access]] within the broader [[non-terrestrial-network]] context.

## Raw artifacts

- `raw/sources/Maritime_Coverage_Enhancement_Using_UAVs_Coordinated_With_Hybrid_Satellite-Terrestrial_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
