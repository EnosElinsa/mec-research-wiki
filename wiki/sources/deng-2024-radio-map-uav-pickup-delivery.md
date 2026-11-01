---
type: source
title: "Energy Minimization for Radio Map-Based UAV Pickup and Delivery Logistics System"
authors: ["Zicong Deng", "Fahui Wu", "Yu Xu", "Dingcheng Yang", "Lin Xiao"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3430320"
venue: "IEEE Transactions on Vehicular Technology, 73(11)"
modeling_card: required
tags: [source, cargo-uav, pickup-and-delivery, radio-map, cellular-connected-uav, genetic-algorithm, energy-minimization]
related:
  - "[[uav-delivery-pickup-dropoff]]"
  - "[[radio-map-aided-uav-path-planning]]"
  - "[[cellular-connected-uav]]"
  - "[[genetic-algorithm]]"
  - "[[cao-2026-radio-map-cargo-pickup]]"
  - "[[huang-2026-hgadrl-cargo-uav-pickup-delivery]]"
  - "[[dingcheng-yang]]"
  - "[[yu-xu]]"
  - "[[lin-xiao]]"
created: 2026-11-02
updated: 2026-11-02
---

# Energy Minimization for Radio Map-Based UAV Pickup and Delivery Logistics System

## Citation

Deng, Z., Wu, F., Xu, Y., Yang, D., & Xiao, L. (2024). *Energy Minimization for Radio Map-Based UAV Pickup and Delivery Logistics System*. **IEEE Transactions on Vehicular Technology, 73**(11). DOI: 10.1109/TVT.2024.3430320.

## TL;DR

A cellular-connected cargo UAV serves multiple pickup-delivery pairs and must keep a reliable link to ground base stations. The paper builds a radio map, uses a Dijkstra variant to get communication-reliable shortest paths between all points, and solves the payload-aware energy-minimizing pickup and delivery problem (PDP) with a hybrid genetic algorithm (HGA).

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One cellular-connected UAV starts empty from a depot, flies at constant speed $v$, picks up goods at node $a_i$ and delivers them to paired node $b_i$ for $n$ pairs, and returns. A radio map of ground base stations gives the interruption probability along each path; flight power depends on carried mass.

**Problem & objective**: P0, a PDP with energy cost: $\min\sum_{i\in S}\sum_{j\in S,i\neq j}E_{ij}x_{ij}$, with $E_{ij}=P(w_{ij})l_{ij}/v$ where $l_{ij}$ is the shortest communication-reliable path length and $w_{ij}$ the carried mass.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Route arc | $x_{ij}$ | binary | 1 if the route flies from node $i$ to node $j$ |
| MTZ order | $u_i$ | integer | Position label used to eliminate subtours |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (9b)-(9c) | Every node is entered and left exactly once. |
| (9d) | MTZ subtour elimination, $u_i-u_j+(2n+1)x_{ij}\le2n$. |
| (9e) | Precedence, $T_{a_k}<T_{b_k}$ for every pickup-delivery pair. |
| (9f) | Payload limit, $w_n\le m_{\max}$. |

**Algorithm**: Decompose P0. A Dijkstra variant computes, for every node pair, the shortest path that trades flight distance against interruption time on the radio map, producing a distance matrix. HGA encodes pickup-delivery pairs as chromosomes and evaluates mass-dependent energy, using crossover and mutation to find an approximate minimum-energy visiting order.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Deng et al. [x] investigated path planning for multi-user pickup and delivery by a cargo UAV that must maintain a reliable connection with the ground base station. They minimized the UAV energy consumption by optimizing the access sequence, noting that energy depends on the pickup and delivery order and on the weight of the goods. A radio map of the target area is first constructed, and an improved Dijkstra's algorithm computes the shortest path between any two access points that satisfies reliable communication. A hybrid genetic algorithm then solves the minimum energy pickup and delivery problem on the resulting distance matrix. Simulation results show that the proposed minimum energy consumption PDP saves about 20% of energy compared with the traditional PDP that does not consider energy consumption.

## Problem framing

Prior UAV logistics work mainly studied TSP-style delivery from a warehouse. Pickup and delivery from distributed points adds precedence constraints and makes carried mass, and therefore power, vary along the route.

## System model

- 600 m by 600 m area with four ground base stations and 3GPP-style Rayleigh building heights capped at 45 m.
- Ten pickup-delivery pairs with goods weights from 10 N to 90 N and an empty departure.
- Constant-speed flight with acceleration ignored; energy per arc is power at the carried mass times flight time.

## Method

The Dijkstra variant adds interruption time to edge weights, accepting slightly longer distance for less interruption. HGA then searches pickup-delivery orders on the precomputed matrix.

## Key findings

- The energy-aware PDP consumed 522041 J versus 656475 J for a shortest-path PDP solved with OR-Tools, about 20% less.
- The energy-aware route prioritizes delivering heavier goods early to avoid carrying large masses over long distances.

## Limitations / future work

The study uses a single UAV. The authors plan to extend the problem to multiple UAVs and related variants.

## Relation to the corpus

A pickup-and-delivery counterpart to [[cao-2026-radio-map-cargo-pickup]] and [[huang-2026-hgadrl-cargo-uav-pickup-delivery]] in [[uav-delivery-pickup-dropoff]], using [[radio-map-aided-uav-path-planning]] to precompute feasible paths.

## Raw artifacts

- Parse: `raw/sources/Energy_Minimization_for_Radio_Map-Based_UAV_Pickup_and_Delivery_Logistics_System/Energy_Minimization_for_Radio_Map-Based_UAV_Pickup_and_Delivery_Logistics_System.md`
- Origin PDF and extracted figures are in the same folder.
