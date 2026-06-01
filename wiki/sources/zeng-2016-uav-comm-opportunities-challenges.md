---
type: source
title: "Wireless Communications with Unmanned Aerial Vehicles: Opportunities and Challenges"
authors: ["Yong Zeng", "Rui Zhang", "Teng Joon Lim"]
year: 2016
url: "https://doi.org/10.1109/MCOM.2016.7470933"
venue: "IEEE Communications Magazine (IEEE COMMAG)"
tags: [source, uav-communications, air-to-ground-channel-model, uav-mobile-relaying, cellular-connected-uav, high-altitude-platform-station, survey]
related:
  - "[[uav-mobile-relaying]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[cellular-connected-uav]]"
  - "[[high-altitude-platform-station]]"
  - "[[zeng-2016-throughput-relaying]]"
  - "[[zeng-2017-energy-efficient-uav-trajectory]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[mozaffari-2019-uav-wireless-tutorial]]"
  - "[[zhan-2011-uav-relay-heading-optimization]]"
  - "[[yong-zeng]]"
created: 2026-06-02
updated: 2026-06-02
---

# Wireless Communications with Unmanned Aerial Vehicles: Opportunities and Challenges

## Citation

Zeng, Y., Zhang, R., & Lim, T. J. (2016). *Wireless Communications with Unmanned Aerial Vehicles: Opportunities and Challenges*. **IEEE Communications Magazine**, 54(5), 36–42. DOI: 10.1109/MCOM.2016.7470933.

## TL;DR

A magazine **overview** of UAV-aided wireless communications. It introduces the basic **networking architecture**, the main **air-to-ground channel characteristics** of low-altitude UAVs, the key **design considerations**, and the new **opportunities** that arise from exploiting UAV **mobility**. It frames three canonical use cases — **ubiquitous coverage**, **relaying**, and **information dissemination / data collection** — and lays out the principal design challenges (control-and-non-payload-communication links, dynamic/intermittent topology, size-weight-and-power constraints, and interference coordination).

## Problem framing

UAV-aided communication is positioned as a cost-effective way to provide connectivity to devices lacking infrastructure coverage (e.g. severe urban/mountainous shadowing, or disaster-damaged infrastructure). The article contrasts low-altitude platforms (LAPs, UAVs at up to several km) with high-altitude platforms (HAPs, stratospheric balloons): HAPs offer wider coverage and longer endurance for large areas, while low-altitude UAVs are **faster to deploy, more flexibly reconfigured, and enjoy short-range LoS links**, and their **maneuverability** can be jointly designed with adaptive communication for further gains (e.g. slowing down to sustain a good channel and transmit more data). UAVs are also split into **fixed-wing** (high speed/payload but must keep moving) vs **rotary-wing** (can hover, limited payload), with the choice driven by application.

## Key content

- **Three use cases.** (1) *UAV-aided ubiquitous coverage* — UAVs assist existing infrastructure for seamless coverage (e.g. rapid service recovery after infrastructure damage; BS offloading in crowded areas, a noted 5G scenario). (2) *UAV-aided relaying* — UAVs connect distant users/groups lacking a reliable direct link (e.g. frontline-to-command-center). (3) *UAV-aided information dissemination and data collection* — UAVs disseminate/collect delay-tolerant data to/from many distributed devices (e.g. precision-agriculture sensors).
- **Channel characteristics.** Low-altitude UAV links are dominated by short-range **LoS**, distinct from terrestrial fading and from long-distance HAP relaying; the article reviews the air-to-ground modeling considerations.
- **Design challenges.** (i) **CNPC links** (control and non-payload communications) with stringent latency/security for safety-critical functions (real-time control, collision/crash avoidance) → need better resource management + security. (ii) **Highly dynamic, sparsely/intermittently connected topologies** → need multi-UAV coordination / swarm operation and connectivity-aware protocols. (iii) **SWAP (size, weight, power) constraints** limiting communication/computation/endurance → need energy-aware deployment + replenishment. (iv) **Interference coordination** for UAV-enabled aerial BSs, harder than terrestrial cells due to mobility and lack of fixed backhaul/centralized control.

## Limitations / scope

This is a **magazine overview article**, not a quantitative study — it presents architecture, channel characteristics, design considerations, and open challenges rather than a specific optimization formulation, algorithm, or evaluation. No simulation results or theorems are claimed; the contribution is conceptual framing and a research agenda.

## Relation to the corpus

A widely-cited **foundational overview** of the corpus's UAV-communications track, from the NUS group of [[yong-zeng]], Rui Zhang, and Teng Joon Lim. It is the conceptual umbrella over their concrete formulations elsewhere in the corpus: the [[zeng-2016-throughput-relaying|mobile-relaying throughput]] and [[zeng-2017-energy-efficient-uav-trajectory|energy-efficient trajectory]] papers, and the later [[zeng-2019-uav-comm-tutorial-5g|5G UAV-comm tutorial]]. It complements the [[mozaffari-2019-uav-wireless-tutorial|IEEE COMST tutorial]] (aerial-base-station vs [[cellular-connected-uav|cellular-connected]] taxonomy) and provides the use-case framing (ubiquitous coverage / relaying / data collection) that recurs across the corpus's UAV-MEC, [[uav-mobile-relaying|relaying]], and [[uav-data-collection|data-collection]] sources. The relaying use case it sketches is realized concretely in [[zhan-2011-uav-relay-heading-optimization]].

## Raw artifacts

- `raw/sources/Wireless_communications_with_unmanned_aerial_vehicles_opportunities_and_challenges/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
