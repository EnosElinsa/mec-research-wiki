---
type: source
title: "On an Intelligent Hierarchical Routing Strategy for Ultra-Dense Free Space Optical Low Earth Orbit Satellite Networks"
authors: ["Bomin Mao", "Xueming Zhou", "Jiajia Liu", "Nei Kato"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3365880"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, leo-satellite-edge-computing, non-terrestrial-network, free-space-optical-isl, multi-objective-reinforcement-learning, routing, walker-star-constellation, qos]
related:
  - "[[leo-satellite-edge-computing]]"
  - "[[non-terrestrial-network]]"
  - "[[free-space-optical-isl]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[walker-star-constellation]]"
  - "[[dynamic-qos-constraints]]"
  - "[[lee-2024-dho-leo-handover]]"
  - "[[mao-2024-ntn-hierarchical-caching-cav]]"
  - "[[bomin-mao]]"
created: 2026-06-01
updated: 2026-06-01
---

# On an Intelligent Hierarchical Routing Strategy for Ultra-Dense Free Space Optical Low Earth Orbit Satellite Networks

## Citation

Mao, B., Zhou, X., Liu, J., & Kato, N. (2024). *On an Intelligent Hierarchical Routing Strategy for Ultra-Dense Free Space Optical Low Earth Orbit Satellite Networks*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2024.3365880. (Manuscript received 31 July 2023; accepted 21 December 2023; date of publication 19 February 2024; date of current version 9 May 2024 → year 2024.)

## TL;DR

A **routing** strategy for ultra-dense **LEO satellite constellations** with **free-space-optical (FSO) inter-satellite links**. It proposes a **dual-layer MEO/LEO architecture** with **regional division** (each MEO satellite acts as a controller computing paths for the LEO satellites covering its ground region, while LEO satellites only forward packets), which cuts the signaling/computation overhead that ultra-dense, highly-dynamic LEO networks otherwise incur. On top of that, a **multi-objective deep-reinforcement-learning routing strategy** with a per-service **utility function** meets the differentiated QoS needs (latency, packet-loss rate, throughput) of diverse terrestrial applications, and a **cooperative mechanism** based on the monotonicity of each service's reward function resolves conflicts between independent per-service routing decisions. The design is made **adaptive to the number of FSO links**, which depends on each satellite's Acquisition-Pointing-Tracking (APT) terminals and geometric visibility.

## Problem framing

LEO constellations (Starlink, OneWeb) are ultra-dense, large-scale, and highly dynamic (satellites at 200–3000 km moving fast), so traditional shortest-path routing (Dijkstra/OSPF) — designed for terrestrial or small satellite networks and updating *behind* traffic changes — cannot keep up and optimizes only a single QoS metric. Meanwhile FSO is attractive for high-bandwidth ISLs, but laser directionality and the limited APT terminals mean FSO ISLs cannot be set up as flexibly as RF, so routing must adapt to the dynamic available-link set. Future services need *multiple* QoS metrics satisfied concurrently with attention to their differing sensitivities — which trade-off-only multi-objective methods neglect.

## System model

- **Architecture.** A **Walker constellation** of LEO satellites (notation $W_T/W_P/W_F/W_h/W_i$) plus an MEO control layer; LEO satellites are divided into **regions** mapped to ground-user regions by latitude/longitude, with each MEO satellite (carrying a high-performance server) controlling its covered LEO region. A temporal graph slices the time-varying topology into stable intervals.
- **Links.** FSO ISLs: intra-orbit links are relatively stable; inter-orbit links change spatially/temporally. Free-space path loss + Shannon-capacity ISL model; the number of FSO ISLs per satellite is bounded by its APT terminals and geometric visibility.
- **QoS metrics.** Applications categorized as **latency-sensitive**, **high-reliability** (packet-loss-rate), or **throughput-sensitive**; an $M/M/1/m$ FIFO queue model yields queuing delay, plus propagation and forwarding delay, packet-loss rate, and throughput.
- **Objective.** Maximize a general per-service **utility function** capturing each service's sensitivity to the multiple QoS metrics, via multi-objective routing.

## Method

- **Dual-layer + region division.** MEO controllers gather local LEO state and compute paths regionally to accelerate routing convergence and avoid LEO-to-LEO signaling.
- **Multi-objective DRL routing.** A DRL model optimizes the defined utility function to accommodate each service's differing metric sensitivities ([[multi-objective-reinforcement-learning]]).
- **Cooperative mechanism.** Based on the **monotonicity of each service's reward function**, it avoids conflicts among the independent per-service routing decision processes.
- **APT-terminal analysis.** Evaluates how the number of APT terminals (hence FSO ISLs) affects performance.

## Key findings

- The proposal is **applicable to varying numbers of APT terminals** and **outperforms benchmark algorithms** across diversified QoS metrics (abstract/parse; specific magnitudes are in the simulation figures and are indicative).
- Region division accelerates routing convergence, and using MEO satellites as controllers removes LEO-to-LEO status-exchange signaling, reducing both traffic and LEO computation overhead.

## Limitations / future work

The work assumes MEO controllers with high-performance servers and stable per-time-slice topology. The conclusion summarizes future directions (parse references a future-directions section) but the captured parse does not enumerate specific quantitative targets → `not in parse`.

## Relation to the corpus

A **non-terrestrial-network / LEO satellite** entry from the NWPU cluster led by [[bomin-mao]] with [[jiajia-liu]] and [[nei-kato]] — the same group as [[mao-2024-ntn-hierarchical-caching-cav]]. Like [[lee-2024-dho-leo-handover]], it is a **networking** paper (routing rather than computation offloading), but its dual-layer satellite architecture and QoS-driven DRL relate to the SAGIN/satellite track and to [[leo-satellite-edge-computing]]. It grounds the new [[free-space-optical-isl]] concept (FSO ISLs noted in passing on the LEO-edge-computing page) and reinforces [[walker-star-constellation]], [[multi-objective-reinforcement-learning]], and [[dynamic-qos-constraints]].

## Raw artifacts

- `raw/sources/On_an_Intelligent_Hierarchical_Routing_Strategy_for_Ultra-Dense_Free_Space_Optical_Low_Earth_Orbit_Satellite_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
