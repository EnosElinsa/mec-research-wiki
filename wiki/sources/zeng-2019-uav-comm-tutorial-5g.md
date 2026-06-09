---
type: source
title: "Accessing From the Sky: A Tutorial on UAV Communications for 5G and Beyond"
authors: ["Yong Zeng", "Qingqing Wu", "Rui Zhang"]
year: 2019
url: "https://doi.org/10.1109/JPROC.2019.2952892"
venue: "Proceedings of the IEEE"
tags: [source, survey, uav-communications, cellular-connected-uav, trajectory-optimization, channel-model, 5g]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[cellular-connected-uav]]"
  - "[[uav-trajectory-control]]"
  - "[[blockage-aware-channel-model]]"
  - "[[wang-2025-lae-network-survey]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[mao-2017-mec-survey-communication]]"
  - "[[yong-zeng]]"
created: 2026-05-31
updated: 2026-06-09
---

# Accessing From the Sky: A Tutorial on UAV Communications for 5G and Beyond

## Citation

Zeng, Y., Wu, Q., & Zhang, R. (2019). *Accessing From the Sky: A Tutorial on UAV Communications for 5G and Beyond*. **Proceedings of the IEEE**. DOI: 10.1109/JPROC.2019.2952892.

## TL;DR

A widely-cited **tutorial / survey** on UAV communications for 5G and beyond. It frames the field around two complementary research paradigms — **UAV-assisted wireless communications** (UAVs as aerial communication platforms, e.g. aerial base stations/relays) and **cellular-connected UAVs** (UAVs as aerial users served by the cellular network) — and surveys the distinctive challenges that arise from UAVs' high altitude and controllable 3-D mobility. A foundational overview entry that predates and contextualizes much of this wiki's UAV-MEC corpus.

## Problem framing

Compared with terrestrial communications, UAV links face new issues: LoS-dominant UAV-ground channels (and the strong aerial-terrestrial interference they induce), distinct QoS requirements for UAV control messages (CNPC) versus payload data, stringent size/weight/power (SWAP) constraints, and a new design degree of freedom from highly controllable 3-D mobility. The tutorial organizes how to integrate UAVs into 5G and future cellular networks around these issues.

## System model

Not a single optimization model — a tutorial spanning the design space. The parse tabulates, among other things:

- **3GPP UAV link requirements** — CNPC (command and control) at ~60–100 kb/s with $10^{-3}$ packet error rate and 50 ms latency on the downlink, versus payload "application data" up to 50 Mbps with terrestrial-like latency.
- **Per-application payload requirements** — e.g. drone delivery, filming, surveillance, search and rescue, precision agriculture (height coverage, latency, DL/UL data rates).
- **Wireless-technology comparison** — direct link, satellite, ad-hoc network, cellular — with advantages/disadvantages each.

Key cross-cutting design topics the tutorial covers include 3-D placement, air-ground interference, antenna models, channel models, energy efficiency, and trajectory optimization (the parse's keyword list).

## Method

Survey/tutorial methodology: it synthesizes the literature into the two-framework taxonomy (UAV-assisted comms vs cellular-connected UAVs), reviews enabling techniques and channel/antenna models, and points out promising future research directions rather than proposing a single algorithm.

## Key findings

- Establishes the **UAV-assisted vs cellular-connected** dichotomy that organizes much subsequent UAV-communications research.
- Identifies LoS-dominant channels, CNPC-vs-payload QoS asymmetry, SWAP limits, and 3-D mobility as the defining design tensions.
- Highlights trajectory optimization and 3-D placement as the key new degrees of freedom UAVs add over fixed infrastructure.

## Limitations / future work

As a tutorial, it points to future research directions throughout rather than reporting experimental limitations; the parse does not list a single consolidated limitations section.

## Relation to the corpus

A **foundational survey** anchor for the UAV side of the wiki, complementing the MEC-communication survey [[mao-2017-mec-survey-communication]] and the more recent low-altitude-economy ([[wang-2025-lae-network-survey]]) and UAV-ISAC ([[meng-2024-uav-isac-overview]]) overviews. Its trajectory-optimization and channel-model framing underlies the [[uav-trajectory-control]] and [[blockage-aware-channel-model]] concepts used throughout the UAV-MEC sources, and it introduces [[cellular-connected-uav]] as a paradigm distinct from the aerial-base-station view in [[multi-uav-assisted-mec]].

## Raw artifacts

- `raw/sources/Accessing_From_the_Sky_A_Tutorial_on_UAV_Communications_for_5G_and_Beyond/full.md`
- Original PDF and extracted figures in the same folder.
