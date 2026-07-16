---
type: source
title: "Mobile Edge Computing — A key technology towards 5G"
authors: ["Yun Chao Hu", "Milan Patel", "Dario Sabella", "Nurit Sprecher", "Valerie Young"]
year: 2015
url: ""
venue: "ETSI White Paper No. 11"
modeling_card: not_applicable
tags: [source, mobile-edge-computing, network-function-virtualization, network-slicing, standardization, foundational]
related:
  - "[[mobile-edge-computing]]"
  - "[[network-function-virtualization]]"
  - "[[network-slicing]]"
  - "[[small-cell-mec]]"
  - "[[vehicular-mec]]"
  - "[[video-analytics-offloading]]"
  - "[[mao-2017-mec-survey-communication]]"
  - "[[mach-2017-mec-survey-architecture]]"
  - "[[you-2017-meco-resource-allocation]]"
created: 2026-06-02
updated: 2026-07-16
---

# Mobile Edge Computing — A key technology towards 5G

## Citation

Hu, Y. C., Patel, M., Sabella, D., Sprecher, N., & Young, V. (2015). *Mobile Edge Computing — A key technology towards 5G*. **ETSI White Paper No. 11**, first edition, September 2015. ISBN 979-10-92620-08-5. European Telecommunications Standards Institute (ETSI). No DOI in parse.

## TL;DR

The foundational **ETSI white paper** that introduces **Mobile Edge Computing (MEC)** as a concept being standardized in the ETSI Industry Specification Group (ISG) of the same name. It frames MEC as providing an IT service environment and cloud-computing capabilities **at the edge of the mobile network, within the Radio Access Network (RAN)** in close proximity to subscribers, to reduce latency, improve network efficiency, and enrich the user experience. The paper lays out MEC's market drivers and business value, sketches a set of service scenarios (augmented reality, intelligent video acceleration, connected cars, IoT gateway), discusses deployment locations, and describes the ETSI ISG MEC standardization effort and its Proof-of-Concept (PoC) framework. It positions MEC as **complementary to NFV** — recognized by the 5G PPP, alongside NFV and SDN, as a key emerging technology for 5G.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Hu et al. [x] introduced Mobile Edge Computing as an IT service environment and cloud-computing capability deployed at the edge of the mobile network within the radio access network. The ETSI white paper describes proximity, low latency, high bandwidth, and real-time radio-network and location awareness as defining characteristics and positions MEC as complementary to network function virtualization. It discusses deployment at LTE macro base stations, radio network controllers, multi-RAT aggregation sites, and core-edge aggregation points, together with augmented reality, intelligent video acceleration, connected-car, and IoT-gateway service scenarios. The paper outlines the ETSI ISG standardization and Proof-of-Concept framework rather than proposing a mathematical optimization model or reporting a quantitative algorithm evaluation.

## Problem framing

Growth in mobile traffic, IoT congestion, and cost pressure push operators to move analysis and applications closer to the network edge. Application/content providers are challenged by the latency of reaching the cloud, while operators want to launch new revenue-generating services faster and serve verticals (automotive, industrial automation, e-health). The paper argues that a **standardized, open, multi-vendor** edge environment — characterized by proximity, low latency, high bandwidth, and real-time radio-network/context awareness — is needed so applications can be integrated seamlessly across operators' platforms. This is a positioning/standardization document rather than an optimization paper; it defines the concept and motivates the ecosystem.

## System model

This is a conceptual/architectural white paper rather than a mathematical-model paper, so there is no formal system model or objective function. The architectural picture it presents:

- **Where MEC lives.** A virtualized platform hosting MEC applications at the RAN edge, deployed at locations such as the LTE macro base station (eNodeB) site, the 3G Radio Network Controller (RNC) site, a multi-RAT cell aggregation site, or an aggregation point at the edge of the core network. Placement depends on scalability, physical constraints, latency targets, and which network information is to be exposed.
- **Relationship to NFV.** MEC reuses the NFV infrastructure and (as much as possible) NFV management and orchestration; the same platform can host both VNFs and MEC applications. MEC is complementary to NFV — NFV targets network functions, MEC enables applications at the edge.
- **Service scenarios** described qualitatively: Augmented Reality (localized object/data caches served from the MEC platform), Intelligent Video Acceleration (a RAN-analytics app feeds downlink-throughput estimates to assist TCP congestion control / adaptive coding), Connected Cars (roadside MEC apps propagate low-latency hazard warnings between vehicles), and IoT Gateway (low-latency aggregation/analytics for resource-constrained devices).

## Method

The white paper does not propose an algorithm. Its "method" is **standardization and ecosystem-building**: defining MEC and a standardized, open API surface (the GS MEC specifications, e.g. GS MEC 004 on service scenarios) so applications can be deployed across multi-vendor MEC platforms, and running the ETSI ISG MEC **Proof-of-Concept (PoC)** framework to demonstrate viability and build a diverse, open ecosystem.

## Key findings

- States the **defining characteristics of the MEC environment** — proximity, low latency, high bandwidth, and real-time radio-network and location/context awareness — and argues these translate into business value for operators, application/content providers, and OTT players.
- Identifies MEC, NFV, and SDN as the trio of key emerging technologies for 5G recognized by the 5G PPP; positions MEC as a key architectural enabler of the evolution to 5G. These are stated positions of the white paper, not measured results.

## Limitations / future work

As a 2015 positioning document, it predates the published GS MEC specifications it calls for and contains no quantitative evaluation. It calls for active participation in the ISG and the PoC framework. Note that ETSI's terminology later shifted from "Mobile Edge Computing" to "Multi-access Edge Computing" — a change postdating this edition and `not in parse`.

## Relation to the corpus

This is the corpus's **standardization anchor** for [[mobile-edge-computing]] itself: where most sources optimize within an MEC system, this paper defines the concept, its RAN-edge placement, and its relationship to [[network-function-virtualization]] and SDN/[[network-slicing]]. It provides the industrial/standards counterpart to the academic survey anchors [[mao-2017-mec-survey-communication]] (communication perspective) and [[mach-2017-mec-survey-architecture]] (architecture/offloading perspective), and predates the offloading-theory anchors such as [[you-2017-meco-resource-allocation]]. Its service scenarios foreshadow corpus tracks: the connected-cars scenario prefigures [[vehicular-mec]], the intelligent-video-acceleration scenario prefigures [[video-analytics-offloading]], and its femto/edge framing connects to [[small-cell-mec]].

> Author note: the "Hu" of this white paper (Yun Chao Hu, Huawei / ETSI MEC ISG) is distinct from the "Hu" of the UAV-MEC sources [[hu-2019-pdd-uav-mec-offloading]] and [[hu-2019-uav-relay-edge-computing]] — a namesake, not the same author.

## Raw artifacts

- `raw/sources/MEC_a_Key_Technology_Towards_5g/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
