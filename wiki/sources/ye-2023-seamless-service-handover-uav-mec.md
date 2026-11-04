---
type: source
title: "Seamless Service Handover in UAV-based Mobile Edge Computing"
authors: ["Zilong Ye", "Philip N. Ji", "Ting Wang"]
year: 2023
url: "https://ieeexplore.ieee.org/document/10437843"
venue: "IEEE Global Communications Conference (GLOBECOM), pp. 1114-1119"
modeling_card: not_applicable
tags: [source, uav-replacement, service-continuity, service-handover, uav-mec, charging-station, dispatch-heuristic, event-driven-simulation]
related:
  - "[[battery-swapping-uav-mec]]"
  - "[[uav-charging-scheduling]]"
  - "[[service-migration]]"
  - "[[stateful-edge-microservice-migration]]"
  - "[[gupta-not-in-parse-uav-replacement]]"
  - "[[li-2026-two-timescale-uav-replacement-hap]]"
  - "[[frejo-martin-2025-uav-stateful-microservice-live-migration]]"
  - "[[uav-energy-replenishment-and-service-continuity]]"
created: 2026-11-03
updated: 2026-11-03
---

# Seamless Service Handover in UAV-based Mobile Edge Computing

## Citation

Ye, Z., Ji, P. N., & Wang, T. (2023). *Seamless Service Handover in UAV-based Mobile Edge Computing*. **IEEE Global Communications Conference (GLOBECOM)**, pp. 1114-1119. The parse gives no venue, year, or DOI; the venue, year, and pages follow the NEC Laboratories America publication record, which links IEEE Xplore document 10437843.

## TL;DR

Low-battery UAVs that carry edge servers must return to a station, which interrupts service unless a fully charged UAV takes over first. A centralized controller dispatches the replacement ahead of time so that users, data, computing models, and task states move before the old UAV leaves. A greedy dispatch rule picks the retrieval station, the launching station, and the launch time.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ye et al. [x] identified the limited battery life of UAVs as an operational challenge for UAV-based mobile edge computing, since low-battery UAVs force frequent service handovers to fully charged UAVs. They proposed a seamless service handover system in which a centralized controller monitors UAV batteries and UAV-station resources and dispatches a fully charged UAV ahead of time, so that users, their data, computing tasks, and task states are transferred before the low-battery UAV leaves. A UAV dispatch algorithm sorts low-battery requests by remaining battery, selects the closest reachable station with free charging spots for retrieval, selects a launching station with available fully charged UAVs, and computes the launch time. Evaluation with a time-series event-driven simulator over a 12-hour city scenario shows shorter service downtime, a longer average service time per UAV, and more well-served users per minute than operation without handover. The authors also report that handover uses more UAVs and causes more frequent response-time spikes because replacement UAVs launch early.

## Scope and method

The controller has a UAV battery monitor (periodic heartbeats plus a listening port for low-battery requests), a UAV station monitor (station location, available fully charged UAVs, and free charging spots), and a UAV dispatch module. The dispatch rule processes requests in ascending order of remaining battery. A station is a retrieval candidate when the low-battery UAV can reach it after the handover time, which covers transferring data, computing models, and computation states at the available bandwidth, and when it has a free charging spot; the closest candidate is chosen. The retrieval station also launches the replacement when it has a fully charged UAV; otherwise the closest station with one launches it. Launch time depends on the remaining battery and the distance to the launching station.

The paper states the objective qualitatively (minimum service downtime and maximum UAV service time) and gives no formal optimization model. The simulated city is 30 by 30 miles with 4 randomly placed stations, each holding 20 UAVs and 20 charging spots. Battery life is 115 to 125 minutes depending on load, flight speed is 50 mph, and 4 hotspots start with 10 users each and gain 5 users per minute with jobs of 9 to 12 minutes. Response time is 20 to 60 ms when a UAV serves the area and 460 to 800 ms when it does not, over a 720-minute run.

## Key findings

- Handover narrows the response-time spikes caused by low-battery UAVs because the replacement arrives before the old UAV departs and no service reboot is needed.
- Table I reports 28 UAVs used with handover versus 24 without, average service time per UAV of 102 versus 98.3, and 197.6 versus 180.5 well-served users per minute (response time below 60 ms).
- Early launches drain replacement batteries sooner, so spikes become more frequent even though each is shorter.

## Limitations / future work

The evaluation is simulation-only and the dispatch rule is a greedy heuristic without optimality analysis. State transfer enters only as a handover time in the reachability check. Data security during handover and weather-dependent energy consumption are excluded, and the authors leave mitigating the extra-UAV and spike-frequency trade-offs to future work.

## Relation to the corpus

This source treats UAV replacement as an MEC service-continuity problem, which complements the throughput-oriented replacement trajectories in [[gupta-not-in-parse-uav-replacement]] and the hierarchical replacement game in [[li-2026-two-timescale-uav-replacement-hap]]. Its station-side resource checks relate to [[battery-swapping-uav-mec]] and [[uav-charging-scheduling]]. The state handover it assumes is implemented as pre-copy live migration in [[frejo-martin-2025-uav-stateful-microservice-live-migration]] and discussed generally under [[stateful-edge-microservice-migration]] and [[service-migration]].

## Raw artifacts

- Parse: `raw/sources/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing/Seamless_Service_Handover_in_UAV-Based_Mobile_Edge_Computing.md`
- Origin PDF and extracted figures are in the same folder.
