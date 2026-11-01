---
type: source
title: "Space-O-RAN: Enabling Intelligent, Open, and Interoperable Non-Terrestrial Networks in 6G"
authors: ["Eduardo Baena", "Paolo Testolina", "Michele Polese", "Dimitrios Koutsonikolas", "Josep Jornet", "Tommaso Melodia"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: not_applicable
tags: [source, open-radio-access-network, non-terrestrial-network, leo-satellite, ran-intelligent-controller, architecture]
related:
  - "[[open-radio-access-network]]"
  - "[[non-terrestrial-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[digital-twin]]"
created: 2026-11-02
updated: 2026-11-02
---

# Space-O-RAN: Enabling Intelligent, Open, and Interoperable Non-Terrestrial Networks in 6G

## Citation

Baena, E., Testolina, P., Polese, M., Koutsonikolas, D., Jornet, J., & Melodia, T. *Space-O-RAN: Enabling Intelligent, Open, and Interoperable Non-Terrestrial Networks in 6G*. Venue, year, and DOI are not in the parse.

## TL;DR

Space-O-RAN extends Open RAN to satellite constellations with hierarchical closed-loop control: dApps on satellites handle real-time scheduling and beam steering, cluster-level Space-RICs coordinate over inter-satellite links, and terrestrial SMO runs training and policy updates with digital twins. Starlink-topology simulations check the latency bounds behind this split.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Baena et al. [x] observed that most non-terrestrial networks remain isolated from terrestrial orchestration frameworks and rely on monolithic, static control architectures that limit adaptability and spectrum use. They introduced Space-O-RAN, a distributed control architecture that extends Open RAN principles into satellite constellations through hierarchical closed-loop control. Lightweight dApps run onboard satellites for real-time functions such as scheduling and beam steering, Space RAN Intelligent Controllers coordinate clusters over low-latency inter-satellite links, and strategic tasks including AI training and policy updates are handled by terrestrial service management and orchestration with digital twins and feeder links. A key enabler is the dynamic mapping of O-RAN interfaces to satellite links. Simulations using the Starlink topology validate the latency bounds that inform the architectural split and demonstrate feasibility and scalability.

## Scope and method

An architecture article supported by latency simulations on a Starlink topology; it defines no decision model.

## Key findings

- Control loops are placed by latency: onboard, cluster, and ground tiers.
- Inter-satellite links make cluster-level autonomous decisions feasible.
- Dynamic interface mapping adapts signaling to varying link conditions.

## Limitations / future work

The architecture is validated through simulation of latency bounds.

## Relation to the corpus

Extends [[open-radio-access-network]] to the [[non-terrestrial-network]] and [[leo-satellite-edge-computing]] setting, using [[digital-twin]] support at the ground tier.

## Raw artifacts

- Parse: `raw/sources/Space-O-RAN_Enabling_Intelligent_Open_and_Interoperable_Non-Terrestrial_Networks_in_6G/Space-O-RAN_Enabling_Intelligent_Open_and_Interoperable_Non-Terrestrial_Networks_in_6G.md`
- Extracted figures are in the same folder; no companion PDF is present.
