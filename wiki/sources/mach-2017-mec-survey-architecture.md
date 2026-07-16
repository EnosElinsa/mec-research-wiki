---
type: source
title: "Mobile Edge Computing: A Survey on Architecture and Computation Offloading"
authors: ["Pavel Mach", "Zdenek Becvar"]
year: 2017
url: "https://doi.org/10.1109/COMST.2017.2682318"
venue: "IEEE Communications Surveys & Tutorials (IEEE COMST)"
modeling_card: not_applicable
tags: [source, survey, mobile-edge-computing, computation-offloading, mec-architecture, mobility-aware-offloading, foundational]
related:
  - "[[mobile-edge-computing]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[mobility-aware-offloading]]"
  - "[[small-cell-mec]]"
  - "[[virtual-machine-multiplexing]]"
  - "[[mao-2017-mec-survey-communication]]"
  - "[[wang-2025-lae-network-survey]]"
created: 2026-06-01
updated: 2026-07-16
---

# Mobile Edge Computing: A Survey on Architecture and Computation Offloading

## Citation

Mach, P., & Becvar, Z. (2017). *Mobile Edge Computing: A Survey on Architecture and Computation Offloading*. **IEEE Communications Surveys & Tutorials**. DOI: 10.1109/COMST.2017.2682318. (Manuscript received 28 October 2016; date of publication 15 March 2017; date of current version 21 August 2017 → year 2017.)

## TL;DR

A widely-cited **MEC survey organized around architecture and computation offloading**. It motivates MEC as the latency-cutting evolution of mobile cloud computing (MCC), contrasts MCC vs. edge computing, and reviews the precursor concepts (cloudlet, ad-hoc cloud, fog computing, C-RAN) and the integrated MEC architectures proposed in the literature (small cell cloud, mobile micro cloud, MobiScud, follow-me cloud, CONCERT) plus the **ETSI** MEC standardization effort. Its core organizes computation-offloading research into three problems: **(1) the offloading decision, (2) allocation of computing resources within the MEC, and (3) mobility management**.

This is the wiki's **architecture/offloading-centric MEC survey anchor**, complementary to the communication-perspective survey [[mao-2017-mec-survey-communication]].

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Mach and Becvar [x] surveyed mobile edge computing architectures and computation offloading for resource-constrained user equipment running delay-sensitive applications. They reviewed MEC use cases, mobile-network integration concepts, and ETSI standardization while contrasting distributed edge resources with centralized mobile cloud computing. Their computation-offloading taxonomy organized prior work into offloading decisions, allocation of MEC computing resources, and mobility management. The survey identified channel quality, application partitionability, computing capacity, backhaul quality, and user mobility as central design factors and called for hierarchical resource placement, dynamic resource management, predictive mobility support, and realistic trials.

## Problem framing

Mobile devices run increasingly demanding applications but are constrained by battery and CPU. MCC offloads to distant centralized clouds but adds high latency/jitter unsuitable for real-time apps. MEC moves compute/storage to the network edge (in network-topology proximity to UEs) to cut latency and energy while still extending battery life, and can also serve operators and third parties.

## Scope surveyed

- **Use cases and scenarios** (Section II): consumer-oriented (computation offloading, AR/VR, web-accelerated browser, gaming), operator/third-party (data aggregation, IoT gateway, ITS), and network-performance/QoE (radio-backhaul coordination, edge caching, RAN optimization). Cites a real MEC testbed showing AR latency cut up to ~88% and UE energy up to ~93% (the survey's quoted figure from its reference, not an original result).
- **MEC architecture & standardization** (Section III): small cell cloud (SCC), mobile micro cloud (MMC), MobiScud, follow-me cloud (FMC), CONCERT, and the ETSI ISG MEC framework, using SDN/[[network-function-virtualization|NFV]] and VM-based virtualization.
- **Computation offloading** (Sections IV–VII): offloading classification (full/partial), influencing factors, and the three research areas — **offloading decision**, **computing-resource allocation** (including VM migration), and **mobility management** for service continuity.
- **Lessons learned and open challenges** (Sections VIII–IX).

## Key findings

As a survey it reports no original quantitative results; its contribution is the architecture taxonomy and the three-way structuring of computation-offloading research, plus a comparison of MCC vs. edge computing (deployment, distance, latency, jitter, compute/storage).

## Limitations / future work

Survey, not original results — no benchmarks of its own. Published 2017, so like the other foundational surveys it predates the aerial/space/generative-AI MEC threads dominating the rest of the corpus; it is a terrestrial-MEC architecture baseline.

## Relation to the corpus

One of the two 2017 MEC survey anchors. Where [[mao-2017-mec-survey-communication]] takes the **communication** (joint radio-compute resource management) angle, this paper takes the **architecture + offloading-process** angle (decision / resource allocation / mobility management) and details the integrated-architecture concepts (SCC/MMC/FMC) underpinning [[small-cell-mec]] and [[virtual-machine-multiplexing]]. It grounds [[mobile-edge-computing]], [[task-offloading]], [[binary-vs-partial-offloading]], and [[mobility-aware-offloading]]; pair it with [[wang-2025-lae-network-survey]] for the modern aerial extension.

## Raw artifacts

- `raw/sources/Mobile_Edge_Computing_A_Survey_on_Architecture_and_Computation_Offloading/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
