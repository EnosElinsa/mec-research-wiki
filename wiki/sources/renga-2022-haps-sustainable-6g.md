---
type: source
title: "Can High Altitude Platform Stations Make 6G Sustainable?"
authors: ["Daniela Renga", "Michela Meo"]
year: 2022
url: "https://doi.org/10.1109/MCOM.002.2101048"
venue: "IEEE Communications Magazine, 60(9)"
modeling_card: not_applicable
tags: [source, high-altitude-platform-station, green-networking, ran-densification, traffic-offloading, renewable-energy, base-station-sleep]
related:
  - "[[high-altitude-platform-station]]"
  - "[[hap-solar-propulsion-energy-balance]]"
  - "[[non-terrestrial-network]]"
created: 2026-11-02
updated: 2026-11-02
---

# Can High Altitude Platform Stations Make 6G Sustainable?

## Citation

Renga, D., & Meo, M. (2022). *Can High Altitude Platform Stations Make 6G Sustainable?* **IEEE Communications Magazine, 60**(9). DOI: 10.1109/MCOM.002.2101048.

## TL;DR

A magazine case study on an urban RAN: a HAPS-mounted super macro base station takes traffic from terrestrial micro base stations so that lightly loaded ones can sleep. Combined with local photovoltaic supply, the offloading cuts grid energy demand of terrestrial nodes while keeping service quality.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Renga and Meo [x] examined whether high altitude platform stations can make 6G networks more sustainable, given that extensive RAN densification raises energy consumption. They considered HAPSs equipped with aerial base stations that provide additional, flexibly usable capacity so that terrestrial base stations can enter sleep modes. Using a portion of an urban RAN as a case study, they evaluated joint energy and resource allocation in which terrestrial traffic is offloaded to the HAPS-mounted base station and terrestrial clusters may use local renewable energy. The results show that offloading traffic to HAPS-mounted base stations reduces the grid energy demand of terrestrial nodes while maintaining adequate quality of service. When combined with local renewable supply, the reported grid energy saving exceeds 70 percent.

## Scope and method

The article simulates two months at one-hour granularity for clusters of six micro base stations and a macro base station, with photovoltaic sizes of 2 to 8 kWp and batteries of 2 to 8 kWh. HAPS cell capacity is varied from 25% to 150% of a 150 Mb/s per-cluster baseline. It evaluates offloading and sleep policies rather than defining a reusable decision model with an explicit objective and constraint set.

## Key findings

- HAPS offloading lowers the grid energy used to power terrestrial nodes, deactivates low-loaded micro base stations, and shifts traffic to macro base stations.
- Combined offloading and renewable supply achieves over 70% grid energy saving.
- Absolute savings are smaller in low-traffic areas than in high-traffic ones.

## Limitations / future work

The analysis covers one urban case and simplified HAPS capacity assumptions.

## Relation to the corpus

A network-level energy view of [[high-altitude-platform-station]] deployment that complements platform-side analyses in [[hap-solar-propulsion-energy-balance]].

## Raw artifacts

- Parse: `raw/sources/Can_High_Altitude_Platform_Stations_Make_6G_Sustainable/Can_High_Altitude_Platform_Stations_Make_6G_Sustainable.md`
- Origin PDF and extracted figures are in the same folder.
