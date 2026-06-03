---
type: source
title: "Cooperative Ground-Satellite Scheduling and Power Allocation for Urban Air Mobility Networks"
authors: ["Hyung-Joo Moon", "Chan-Byoung Chae"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3460031"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags:
  - source
  - urban-air-mobility
  - non-terrestrial-network
  - space-air-ground-integrated-network
  - resource-allocation
  - mixed-integer-nonlinear-programming
  - alternating-optimization-sdr-sca
  - mobility-aware-offloading
related:
  - "[[urban-air-mobility]]"
  - "[[non-terrestrial-network]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[cellular-connected-uav]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[generalized-assignment-problem]]"
  - "[[graph-based-resource-management]]"
  - "[[mobility-aware-offloading]]"
  - "[[dai-2024-graph-rm-survey-optimization]]"
  - "[[wang-2024-satellite-terrestrial-computing]]"
created: 2026-06-03
updated: 2026-06-03
---

# Cooperative Ground-Satellite Scheduling and Power Allocation for Urban Air Mobility Networks

## Citation
Hyung-Joo Moon, Chan-Byoung Chae, "Cooperative Ground-Satellite Scheduling and Power Allocation for Urban Air Mobility Networks," *IEEE Journal on Selected Areas in Communications*, 2024. DOI: 10.1109/JSAC.2024.3460031. (Received 7 Mar 2024; revised 30 Jun 2024; accepted 5 Aug 2024; date of publication 13 Sep 2024; date of current version 18 Dec 2024 → year 2024. Corresponding author: Chan-Byoung Chae. Yonsei University, Seoul.)

## TL;DR
This paper designs **multi-user downlink scheduling and power allocation** for **urban air mobility (UAM)** aircraft served by a 6G non-terrestrial network that integrates multiple ground stations (GSs) and a single satellite. It maximizes the **GS-user sum rate** subject to link-association, power, elevation-angle, and minimum-QoS constraints. The approach first **offloads high-interference UAMs to the satellite** (on a separate band) to clean up interference among the remaining GS users, then converts the GS link-association integer problem into a **minimum-cost maximum-flow (MCMF)** graph problem, and finally solves the non-convex GS power allocation with **successive convex approximation (SCA)**. Because the GS-to-UAM channel is line-of-sight and scatterer-poor, scheduling is done by **short-horizon prediction** from UAM positions/velocities, avoiding instantaneous CSI and frequent handovers.

## Problem framing
UAM (passenger/cargo aircraft over cities) needs large **downlink** volumes for navigation, safety, command-and-control (C2), and multimedia — unlike conventional UAV models that focus on uplinking mission data or serving terrestrial users, and unlike a generic [[cellular-connected-uav]]. UAMs hold stable, planned flight paths and velocities, so the network should schedule by prediction rather than react to instantaneous channels. Serving wide airspace needs many GSs sharing one band, which creates inter-beam interference (IBI) and inter-GS interference (IGI) when a GS and two UAMs become geometrically aligned. The paper's idea: deploy a satellite on a separate band to absorb the worst-interfering UAMs, restoring orthogonality for GS users, and frame UAMs as the **edge users of a satellite-ground NTN** — a distinct system model for 6G NTN.

## System model
- **Topology (Fig. 1, SAGIN for UAM):** K GSs (each a P×Q rectangular hybrid-beamforming array, N ≪ PQ RF chains, so each GS serves ≤ N UAMs) and one LEO satellite providing an Earth-fixed spot beam; M UAMs total, split into M_GS GS-users and M_SAT = M − M_GS satellite-users; cell-free (any UAM may connect to any GS).
- **Channel:** GS-to-UAM is LoS-dominant (free-space path loss + Rician small-scale term); 3D maximum-ratio-transmission (MRT) beamforming steered from known UAM location/velocity. Satellite-to-UAM uses a separate band with TDMA/OFDMA (no co-channel interference among satellite users), FSPL + atmospheric loss, and a wide spot beam (no per-UAM beamforming).
- **Mobility:** UAMs follow linear trajectories over a short interval [0,T]; positions u_m(t) = u_m(0) + u̇_m·t with location and velocity known at the network controller, enabling prediction-based scheduling that holds links fixed over [0,T] to avoid handovers.
- **Problem (Sec. III):** maximize the GS-user **sum rate** over link association, transmit power, elevation angle, and minimum-QoS constraints — a **mixed-integer nonlinear program** (per the Index Terms).

## Method
- **Satellite user selection:** a greedy algorithm uses UAM locations/velocities to identify the UAMs that would cause the most severe GS interference and associates them with the satellite (different spectrum), improving GS-user SINR.
- **GS link association → MCMF:** the integer GS-user association is recast via a graph-theoretic approach as a **minimum-cost maximum-flow** problem; two variants are offered — an **analytical** method using polynomial approximations and a **numerical** method using integral approximation via time-sampled parameters — trading computational complexity against rate.
- **Power allocation via SCA:** with links fixed, instantaneous channel gains drive a **successive convex approximation** power-allocation algorithm that maximizes the sum rate under power limits and QoS requirements.

## Key findings
Grounded in the abstract and contributions (magnitudes are figure-derived, treated as indicative):
- The proposed scheduling + power allocation **outperforms several distance-based baselines** that associate users by proximity, even under strict QoS constraints.
- Reassigning high-interference UAMs to the satellite is reported to notably improve GS-user SINR, network capacity, and service continuity.
- The analytical-vs-numerical selection methods expose a complexity-vs-rate trade-off the operator can tune.

## Limitations / future work
- Results are simulation-based; no flight or testbed validation.
- The model assumes a single satellite and known UAM positions/velocities at the controller, with linear trajectories over the short scheduling horizon.
- Scheduled links are held fixed over [0,T] to avoid handovers, which trades adaptivity for stability.
- This is a **communication-layer** scheduling/power-allocation paper (downlink sum rate), not a computation-offloading design, despite the "offload to satellite" framing referring to traffic, not tasks.

## Relation to the corpus
This is a satellite-ground NTN downlink resource-allocation entry whose framing of **UAMs as the edge users of a SAGIN** is its distinctive contribution, captured in the new [[urban-air-mobility]] concept page. Its **MCMF graph reformulation** of link association is a concrete instance of the bipartite/flow techniques surveyed in [[dai-2024-graph-rm-survey-optimization]] ([[graph-based-resource-management]]), and its **SCA** power allocation is the same convex workhorse seen across the corpus. The satellite-offloads-interference idea and prediction-based, CSI-light scheduling distinguish it from task-offloading satellite work like [[wang-2024-satellite-terrestrial-computing]]; here "offloading" moves *users/traffic* to the satellite band, not computation. It contrasts with the [[cellular-connected-uav]] downlink-C2 literature by targeting path-stable transport aircraft rather than mission UAVs.

## Raw artifacts
- Parse: `raw/sources/Cooperative_Ground-Satellite_Scheduling_and_Power_Allocation_for_Urban_Air_Mobility_Networks/full.md`
- Origin PDF: `raw/sources/Cooperative_Ground-Satellite_Scheduling_and_Power_Allocation_for_Urban_Air_Mobility_Networks/234d2f6f-8b9a-47e8-a15d-ca691bd8d46f_origin.pdf`
- Figures: `raw/sources/Cooperative_Ground-Satellite_Scheduling_and_Power_Allocation_for_Urban_Air_Mobility_Networks/images/`
