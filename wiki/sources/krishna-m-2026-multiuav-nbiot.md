---
type: source
title: "Performance Analysis of Multi-UAV-Aided NB-IoT Communication System"
authors: ["Siva Rama Krishna M.", "Naveen Mysore Balasubramanya"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3673845"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), pp. 1-16"
tags: [source, nb-iot, multi-uav, code-domain-noma, scheduling, latency, energy-efficiency]
related:
  - "[[narrowband-iot]]"
  - "[[code-domain-noma]]"
  - "[[longest-transmission-time-first-uav-grouping]]"
  - "[[non-terrestrial-network]]"
  - "[[air-to-ground-channel-model]]"
  - "[[makespan-minimization]]"
created: 2026-07-14
updated: 2026-07-14
---

# Performance Analysis of Multi-UAV-Aided NB-IoT Communication System

## Citation

Krishna M., S. R., & Balasubramanya, N. M. (2026). *Performance Analysis of Multi-UAV-Aided NB-IoT Communication System*. **IEEE Transactions on Mobile Computing**, 1-16. DOI: 10.1109/TMC.2026.3673845.

## TL;DR

Models stationary decode-and-forward UAVs as NB-IoT relays for ground-device clusters, then reduces end-to-end collection time and device energy by combining Zadoff-Chu code-domain NOMA with dynamic longest-transmission-time-first grouping.

## Problem and system model

Ground user equipment cannot reach the base station directly across the modeled 0.86 km2 cell. Stationary UAVs hover at 150 m, receive NB-IoT uplinks from assigned spots, and decode-and-forward the data to the base station. The 180 kHz link model includes NPRACH, NPUSCH, and NPDSCH procedures, TDL-D user-to-UAV channels, and TDL-D/EPA/ETU UAV-to-base-station channels.

Orthogonal access serves users sequentially with TDMA. The non-orthogonal design assigns simultaneous users different Zadoff-Chu spreading codes and applies successive interference cancellation with estimated channels; it is therefore [[code-domain-noma]], not the power-domain model represented by the wiki's general NOMA page.

## Method

Static grouping fixes the UAV pools. Dynamic [[longest-transmission-time-first-uav-grouping]] sorts offered loads in descending order and repeatedly assigns the next load to the currently lightest pool, adapting a longest-processing-time scheduling heuristic to multi-UAV collection. Physical-layer simulations include practical channel estimation and compare scheduled and grant-free random access.

## Key findings

- In the six-UAV example, dynamic grouping completes collection in 11 ms versus 15 ms for static grouping.
- OMA supports all three evaluated coverage requirements, while the NOMA design is limited to the small and medium coverage cases under the tested link budget.
- Dynamic NOMA gives the lowest latency and user-equipment energy across the discrete-uniform, Poisson, and beta load distributions.
- At 50 UAVs, reported grouping-processing time is below 0.125 microseconds for static grouping and 0.375 microseconds for dynamic grouping; these are implementation measurements, not airborne execution results.
- In the grant-free comparison, NOMA needs about 5 dB rather than 0 dB to reach 99% preamble-detection probability and about 3 dB additional SNR to reach BLER 0.1.

## Limitations

The UAVs are quasi-static; deployment, trajectory, and failure recovery remain future work. The main analysis assumes no NPRACH collision among active devices, although a separate collision calculation is provided. Imperfect cancellation limits a code group to two users. The grouping procedure is a heuristic and has no global-optimality proof. The paper uses inconsistent LTTF/LPTF naming, so this page describes the scheduling rule directly and avoids treating either label as a separate guarantee. Results are analytical and simulation-based, with no airborne deployment.

## Relation to the corpus

This source connects [[narrowband-iot]] access mechanics to multi-UAV relay scheduling. Its maximum-pool-completion objective is a specialized [[makespan-minimization]] problem, while its code separation makes it distinct from power-domain aerial NOMA resource-allocation papers.

## Raw artifacts

- Parse: `raw/sources/Performance_Analysis_of_Multi-UAV-Aided_NB-IoT_Communication_System/Performance_Analysis_of_Multi-UAV-Aided_NB-IoT_Communication_System.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
