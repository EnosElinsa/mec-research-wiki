---
type: source
title: "Adaptive Routing for Flying Ad Hoc Network using Evolvable Route Expiration Time"
authors: ["Liyou Deng", "Zhiyuan Wang", "Shan Zhang", "Xiaohan Qiu", "Mingsheng Tang", "Fusang Zhang", "Hongbin Luo"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3694704"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, fanet, uav-swarm, routing, content-centric-networking, host-centric-routing, adaptive-routing]
related:
  - "[[evolvable-route-expiration-time]]"
  - "[[stateless-geographic-fanet-routing]]"
  - "[[directional-fanet-link-maintenance]]"
  - "[[uav-mobile-relaying]]"
  - "[[wireless-backhaul]]"
  - "[[autonomous-uav-swarms]]"
  - "[[fatemidokht-2021-vru-vanet-routing]]"
  - "[[uav-assisted-vanet-routing]]"
created: 2026-07-10
updated: 2026-07-13
---

# Adaptive Routing for Flying Ad Hoc Network using Evolvable Route Expiration Time

## Citation

Deng, L., Wang, Z., Zhang, S., Qiu, X., Tang, M., Zhang, F., & Luo, H. (2026). *Adaptive Routing for Flying Ad Hoc Network using Evolvable Route Expiration Time*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3694704.

## TL;DR

Proposes eRET, an adaptive FANET routing framework that moves between host-centric and content-centric forwarding by evolving each UAV's route expiration time. The method uses local perception of topology dynamics, traffic load, and request pattern, then updates RET so nodes lean toward route reuse in stable/heavy-load conditions and toward content-centric discovery in highly mobile/light-load/high-sharing conditions.

## Problem

Host-centric FANET routing reuses established routes but breaks under fast topology change. Content-centric routing tolerates mobility through flooding and stateful forwarding but creates overhead and collisions under heavy traffic. Existing hybrid mechanisms such as HII and IHCR combine both paradigms but use static coupling or fixed RET, so they cannot adapt to time-varying UAV-swarm missions.

## System model

- The paper evaluates host-centric AODV, content-centric NDNF, LFBL, IHCR, and eRET in FANET packet-level simulations.
- FANET environment is represented through topology dynamics, traffic load, and request pattern.
- Table 2 uses an 800 m by 800 m playground, IEEE 802.11ac at 5 GHz, 64 nodes, Random Waypoint mobility, 0-120 m/s speeds, 1-12 transmission pairs, 24-1000 ms send intervals, content-sharing degree 1-24, 400 s simulation time, and 100 simulation runs.
- The search-and-rescue scenario has a high-speed search phase and a more stable rescue phase.

## Method

eRET makes route expiration time a node-level adaptive variable. Each UAV passively measures neighbor variation rate, request forwarding rate, and per-content request frequency as local indicators for topology dynamics, traffic load, and content-sharing pattern. Sliding-window estimation smooths those indicators; a multiplicative RET update increases RET under heavier load and decreases RET under stronger topology variation or content sharing. Each node then chooses unicast or broadcast Interest forwarding based on whether its local route entry is valid.

## Key findings

- Host-centric AODV adapts better in low-speed, heavy-load, low-content-sharing FANETs.
- Content-centric NDNF adapts better in high-speed, light-load, high-content-sharing FANETs.
- Fixed-RET hybrid IHCR can match AODV-like or NDNF-like behavior only when the fixed RET happens to fit the environment.
- In transition scenarios, eRET evolves toward content-centric routing as node speed rises, toward host-centric routing as traffic load rises, and toward content-centric routing as content-sharing degree rises.
- In the representative search-and-rescue scenario, eRET reduces total packet loss by up to 52.91% versus AODV and 65.24% versus NDNF.
- The paper reports that distributed RET evolution does not create evident flow starvation in the representative fairness table; PDR and throughput Jain fairness values are close to 1 for all compared mechanisms.

## Relation to the corpus

This is a FANET routing complement to [[stateless-geographic-fanet-routing]] and [[directional-fanet-link-maintenance]]. Stateless geographic routing asks how each packet chooses a next hop without route tables; directional link maintenance asks how to keep directional hops alive; eRET asks when a UAV swarm should behave more like host-centric AODV or more like content-centric NDNF. The concept is relevant to [[wireless-backhaul]] and [[autonomous-uav-swarms]] whenever swarm networking has to keep working across search, rescue, monitoring, and other phase-changing missions.

## Limitations / extraction notes

The evaluation is simulation-based. The paper notes open issues around node-density perception, location-centric routing, service-centric routing, abrupt-environment responsiveness, finer-grained traffic/QoS characterization, and joint tuning of perception interval, sliding-window size, and evolution step size. The local parsed Markdown is silent on DOI/venue in the header; bibliographic metadata was verified against a title-matched IEEE Computer Society record.

## Raw artifacts

- Parse: `raw/sources/Adaptive_Routing_for_Flying_Ad_Hoc_Network_using_Evolvable_Route_Expiration_Time/Adaptive_Routing_for_Flying_Ad_Hoc_Network_using_Evolvable_Route_Expiration_Time.md`
- Origin PDF: `raw/sources/Adaptive_Routing_for_Flying_Ad_Hoc_Network_using_Evolvable_Route_Expiration_Time/Adaptive_Routing_for_Flying_Ad_Hoc_Network_using_Evolvable_Route_Expiration_Time.pdf`
- Figures: `raw/sources/Adaptive_Routing_for_Flying_Ad_Hoc_Network_using_Evolvable_Route_Expiration_Time/images/`
