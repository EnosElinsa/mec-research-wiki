---
type: source
title: "A Survey on Mobile Edge Computing: The Communication Perspective"
authors: ["Yuyi Mao", "Changsheng You", "Jun Zhang", "Kaibin Huang", "Khaled B. Letaief"]
year: 2017
url: "https://doi.org/10.1109/COMST.2017.2745201"
venue: "IEEE Communications Surveys & Tutorials (IEEE COMST)"
tags: [source, survey, mobile-edge-computing, computation-offloading, resource-management, foundational]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[service-caching-mec]]"
  - "[[wang-2025-lae-network-survey]]"
  - "[[khoramnejad-2025-gai-wireless-optimization-survey]]"
  - "[[khaled-ben-letaief]]"
created: 2026-05-29
updated: 2026-07-13
---

# A Survey on Mobile Edge Computing: The Communication Perspective

## Citation

Mao, Y., You, C., Zhang, J., Huang, K., & Letaief, K. B. (2017). *A Survey on Mobile Edge Computing: The Communication Perspective*. **IEEE Communications Surveys & Tutorials**. DOI: 10.1109/COMST.2017.2745201.

## TL;DR

The canonical, widely-cited **survey of mobile edge computing from the communication perspective**, focused on the joint management of radio and computational resources. It frames MEC as the fusion of wireless communications and mobile computing, surveys computation-offloading techniques and MEC network architectures, and lays out research directions: MEC system deployment, cache-enabled MEC, mobility management, green MEC, and privacy-aware MEC. It also reviews standardization efforts (ETSI) and typical application scenarios.

This is the wiki's **definitional foundation paper** for MEC itself — most curated sources solve a narrow problem inside the landscape this survey maps.

## Problem framing

Cloud computing's long propagation distance makes it inadequate for latency-critical 5G/IoT applications. MEC pushes computing, network control, and storage to the network edge (base stations, access points) to enable computation-intensive, latency-critical apps on resource-limited mobile devices, promising large reductions in latency and mobile energy consumption.

## Scope surveyed

- **Computation offloading.** Models and trade-offs for offloading decisions, including the energy-latency tension and binary vs. partial offloading framings (see [[binary-vs-partial-offloading]], [[energy-latency-tradeoff]]).
- **Joint radio-and-computational resource management** — the survey's main thrust.
- **MEC architectures** and deployment options.
- **Cross-cutting issues:** cache-enabled MEC ([[service-caching-mec]]), mobility management, green MEC, privacy-aware MEC.
- **Standardization & applications:** ETSI's MEC definition, the relationship to fog computing, and representative use cases.

## Key findings

As a survey, it presents no original quantitative results. Its contribution is a structured taxonomy of MEC research from the communication angle and an enumeration of open directions.

## Limitations / future work

Survey, not original results — no benchmarks. Published in 2017, so it predates the aerial/space/generative-AI MEC threads that dominate the rest of this wiki; treat it as the conceptual baseline rather than state-of-the-art.

## Relation to the corpus

Provides the MEC vocabulary that every other source builds on, anchoring [[mobile-edge-computing]] and [[task-offloading]]. It is the terrestrial-MEC complement to the wiki's two newer survey anchors: [[wang-2025-lae-network-survey]] (low-altitude economy networks) and [[khoramnejad-2025-gai-wireless-optimization-survey]] (generative-AI for wireless optimization).

## Raw artifacts

- `raw/sources/A_Survey_on_Mobile_Edge_Computing_The_Communication_Perspective/full.md`
- Original PDF and extracted figures in the same folder.
