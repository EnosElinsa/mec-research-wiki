---
type: source
title: "Efficient and Secure Routing Protocol Based on Artificial Intelligence Algorithms With UAV-Assisted for Vehicular Ad Hoc Networks in Intelligent Transportation Systems"
authors: ["Hamideh Fatemidokht", "Marjan Kuchaki Rafsanjani", "Brij B. Gupta", "Ching-Hsien Hsu"]
year: 2021
url: "https://doi.org/10.1109/TITS.2020.3041746"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS), vol. 22, no. 7, pp. 4757-4769"
modeling_card: required
tags: [source, uav-assisted-vanet-routing, vanet, fanet, uav-enabled-its, ant-colony-optimization, trust-management, routing]
related:
  - "[[uav-assisted-vanet-routing]]"
  - "[[uav-enabled-its]]"
  - "[[ant-colony-optimization]]"
  - "[[stateless-geographic-fanet-routing]]"
  - "[[uav-mobile-relaying]]"
  - "[[uav-cluster-authentication]]"
  - "[[bujari-2018-stateless-fanet-routing]]"
  - "[[deng-2026-eret-fanet-routing]]"
  - "[[chen-2026-maddpg-uav-swarm-antijamming]]"
created: 2026-07-13
updated: 2026-07-16
---

# Efficient and Secure Routing Protocol Based on Artificial Intelligence Algorithms With UAV-Assisted for Vehicular Ad Hoc Networks in Intelligent Transportation Systems

## Citation

Fatemidokht, H., Kuchaki Rafsanjani, M., Gupta, B. B., & Hsu, C.-H. (2021). *Efficient and Secure Routing Protocol Based on Artificial Intelligence Algorithms With UAV-Assisted for Vehicular Ad Hoc Networks in Intelligent Transportation Systems*. **IEEE Transactions on Intelligent Transportation Systems**, 22(7), 4757-4769. DOI: 10.1109/TITS.2020.3041746. Final bibliographic fields were verified by exact-title Crossref match because the parse omits them.

## TL;DR

VRU combines vehicle/UAV road-segment routing with on-demand FANET routing. Its ground component uses UAV-collected density, connectivity, and behavioral-trust information to select urban road segments; its aerial fallback uses ant-colony route discovery when the vehicle network is disconnected.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Vehicles, UAVs, roadside units, and a trusted authority form an urban vehicular network with ground and aerial links. UAVs observe road-segment density and connectivity, aggregate direct and recommended trust, and provide a FANET fallback when vehicle-only forwarding becomes disconnected.

**Problem & objective**: Select a secure and stable route that increases packet delivery and malicious-node detection while reducing end-to-end delay and control overhead. The ground rule chooses the next feasible road segment by $\arg\max_j \mathrm{Trust}_j\gamma_jR_v/((1+\sigma_j)D_j)$, and the aerial fallback chooses the discovered route with maximal accumulated pheromone.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Cluster head | $v_i^{\mathrm{CH}}$ | discrete vehicle choice | Trusted vehicle representing a road-segment cluster |
| Next road segment | $j^*$ | discrete segment choice | Connected segment selected toward the destination |
| Routing mode | $m$ | binary choice | Ground VRU_vu forwarding or UAV VRU_u fallback |
| UAV next hop and route | $u_{h+1},\mathcal P$ | discrete path choices | ACO forwarding choices in the aerial network |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Candidate cluster heads and forwarding vehicles must pass the configurable trust threshold. |
| C2 | A ground segment is eligible only when its connectivity measure is positive: $\gamma_j>0$. |
| C3 | Direct ground forwarding requires the candidate distance to be within vehicle range $R_v$. |
| C4 | Segment scoring combines trust, connectivity, density dispersion, and distance to destination. |
| C5 | ACO next-hop selection uses unvisited feasible UAV neighbors and route-request lifetime limits. |
| C6 | Route selection favors the highest pheromone score, while stored alternatives support repair after a link break. |

**Algorithm**: Use Hello messages to estimate vehicle density, select cluster heads from trust, position, and speed, and update direct and indirect trust evidence and blacklists. Test road-segment connectivity and forward through the maximum-score segment; when no ground segment is connected, launch Request-Ant and Reply-Ant discovery, update UAV-link pheromones, choose the highest-scoring route, and reuse an alternate route during repair.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Fatemidokht et al. [x] proposed VRU, a UAV-assisted secure routing protocol for urban vehicular ad hoc networks. VRU chooses trusted cluster heads, scores connected road segments from trust, connectivity, density dispersion, and destination distance, and switches to ACO-based UAV routing when ground segments disconnect. The UAV route component selects paths by pheromone-weighted next-hop rules and reuses stored alternatives after link failure, while direct and indirect trust identify malicious vehicles. NS-2 simulations reported 16% higher packet delivery, 13% lower end-to-end delay, 40% lower overhead than AODV, and about 7% higher detection when UAV assistance was used.

## Problem

Fast topology changes and urban obstacles make VANET routes short-lived, while open ad hoc participation exposes forwarding to malicious vehicles. The paper asks how UAVs can help maintain delivery, choose stable road segments, and aggregate trust evidence without relying on one ground-only route.

## System model

- Vehicles, UAVs, roadside units, and a trusted authority communicate through V2V, V2I, V2U, and U2U links using IEEE 802.11p.
- GPS and digital maps are assumed for every vehicle and UAV. UAVs fly at a fixed low altitude, cover four road segments each, and have an assumed communication range near 1000 m.
- Urban road segments are divided into fixed clusters. UAVs select cluster heads from trust, speed, and distance-to-segment-center information.
- Direct interaction evidence and neighbor recommendations feed cluster, roadside-unit, and trusted-authority blacklists. The paper does not state the numerical trust threshold.

## Method

`VRU_vu` estimates vehicle density from Hello packets, tests road-segment connectivity, and scores candidate segments from trust, connectivity, density dispersion, and destination distance. If ground forwarding fails, `VRU_u` discovers UAV routes with Request-Ant and Reply-Ant messages, ranks routes by pheromone-like link geometry, and first tries stored alternatives after a break.

The two components can run in parallel. This makes [[uav-assisted-vanet-routing]] a hybrid vehicle/aerial fallback design rather than a purely [[stateless-geographic-fanet-routing|stateless FANET forwarding]] protocol.

## Key findings

- NS-2.35 simulations use a `4 x 4 km` urban grid, 25 intersections, 40 road segments, 100-3000 vehicles, 16-80 UAVs, and 20% malicious vehicles; each setting is run ten times.
- Against UVAR and AODV, Table III reports packet-delivery gains of `4%/16%`, end-to-end-delay reductions of `5%/13%`, hop-count reductions of `3%/22%`, and overhead reductions of `8%/40%`, respectively.
- The UAV-assisted diagnostic procedure improves malicious-vehicle detection by about `7%` relative to the same procedure without UAVs. This is not a comparison against every security baseline.
- The parsed Table IV reports `19%` and `-23%` changes against TFDD in two time windows and `2%` against AECFV; the negative late-window value is retained as an unresolved source/table ambiguity.

## Limitations / parse caveats

The study is simulation-only and explicitly limited to urban roads. It assumes GPS/maps, rechargeable long-life node batteries, fixed UAV altitude, and centralized UAV/RSU/authority trust aggregation. Malicious UAVs are outside the protection model. The claimed `O(log N)` and `O(m log m)` costs are not derived, the overhead prose and equation use different denominators, the trust threshold and attacker behavior are underspecified, and several formulas are OCR-damaged. The conclusion calls UAV energy saving future work even though the model initially removes energy as a concern.

## Relation to the corpus

This source extends the [[uav-enabled-its]] branch with road-level trust and connectivity control. It complements [[bujari-2018-stateless-fanet-routing]] and [[deng-2026-eret-fanet-routing]], which focus on aerial forwarding behavior, and differs from [[chen-2026-maddpg-uav-swarm-antijamming]], where security means radio anti-jamming rather than behavioral trust and blacklist aggregation.

## Raw artifacts

- Parse: `raw/sources/Efficient_and_Secure_Routing_Protocol_Based_on_Artificial_Intelligence_Algorithms_With_UAV-Assisted_for_Vehicular_Ad_Hoc_Networks_in_Intelligent_Transportation_Systems/Efficient_and_Secure_Routing_Protocol_Based_on_Artificial_Intelligence_Algorithms_With_UAV-Assisted_for_Vehicular_Ad_Hoc_Networks_in_Intelligent_Transportation_Systems.md`
- Origin PDF: `raw/sources/Efficient_and_Secure_Routing_Protocol_Based_on_Artificial_Intelligence_Algorithms_With_UAV-Assisted_for_Vehicular_Ad_Hoc_Networks_in_Intelligent_Transportation_Systems/Efficient_and_Secure_Routing_Protocol_Based_on_Artificial_Intelligence_Algorithms_With_UAV-Assisted_for_Vehicular_Ad_Hoc_Networks_in_Intelligent_Transportation_Systems.pdf`
- Figures: `raw/sources/Efficient_and_Secure_Routing_Protocol_Based_on_Artificial_Intelligence_Algorithms_With_UAV-Assisted_for_Vehicular_Ad_Hoc_Networks_in_Intelligent_Transportation_Systems/images/`
