---
type: source
title: "Efficient Management of Composite Heterogeneous Applications at the Network Edge"
authors: ["Madhura Adeppady", "Yenchia Yu", "Ali Asghar Rahmanian Kooshkaki", "Ahmed Ali-Eldin Hassan", "Carla Fabiana Chiasserini"]
year: 2026
url: "https://doi.org/10.1109/TNSM.2026.3709656"
venue: "IEEE Transactions on Network and Service Management (IEEE TNSM), 23, 6550-6568"
modeling_card: required
tags: [source, mobile-edge-computing, microservice-placement, service-migration, stateful-microservice, stateless-microservice, step]
related:
  - "[[mobile-edge-computing]]"
  - "[[service-migration]]"
  - "[[multi-microservice-application-placement]]"
  - "[[dynamic-space-time-graph-with-virtual-edges]]"
  - "[[calagna-2024-robust-stateful-migration]]"
  - "[[chen-2026-hc-mappo-vehicle-twin-migration]]"
created: 2026-08-27
updated: 2026-08-27
---

# Efficient Management of Composite Heterogeneous Applications at the Network Edge

## Citation

Adeppady, M., Yu, Y., Rahmanian Kooshkaki, A. A., Ali-Eldin Hassan, A., & Chiasserini, C. F. (2026). *Efficient Management of Composite Heterogeneous Applications at the Network Edge*. **IEEE Transactions on Network and Service Management, 23**, 6550-6568. DOI: 10.1109/TNSM.2026.3709656.

## TL;DR

The paper formulates Multi-microservice Application Placement (MAP) for edge applications composed of stateful and stateless microservices. STEP builds a Dynamic Network Topology Graph and a pruned, expanded decision graph to jointly place, share, migrate, select quality versions, and allocate resources while meeting application latency and downtime limits.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Mobile users request composite applications formed by chains of stateful and stateless microservices from an edge cluster attached to base stations. User handovers trigger reassessment of placement, migration or relocation, microservice sharing, quality-version selection, CPU allocation, and radio-block allocation.

**Problem & objective**: Minimize the weighted deployment-cost and quality objective, $\min_{y,z,\hat\tau,v}\;\beta C(y,z,\hat\tau,v)-(1-\beta)Q(z)$, where cost includes memory, CPU, and communication resources and $Q$ is average normalized application quality.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Microservice placement | $y_{s,i}^{n,q}$ | Binary | Instance $i$ of microservice $n$ at quality $q$ is deployed on server $s$ |
| User assignment | $z_{u,i}^{n,q}$ | Binary | User $u$ is served by that instance |
| CPU allocation | $\hat\tau_{n,q}^i$ | Continuous | CPU cycles/s allocated to the instance |
| Radio allocation | $v_{u,s}$ | Integer | Resource blocks allocated between user $u$ and server $s$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every application meets its end-to-end response-latency and migration-downtime limits. |
| C2 | Each microservice instance is placed on one server or a dummy server; shareable instances are reused subject to their semantics. |
| C3 | Stateful non-shareable instances preserve user continuity and are not simultaneously assigned to multiple users. |
| C4 | Entry microservices requested by the same user are co-located, and a user accesses only one instance of a given microservice. |
| C5 | Server memory and CPU plus base-station radio blocks do not exceed available capacities. |

**Algorithm**: Construct a multi-layer Dynamic Network Topology Graph, prune it to a local decision graph for affected applications, expand it to encode additive latency and downtime constraints, and use a minimum-cost Dijkstra path followed by convex CPU recalibration. STEP has polynomial decision complexity after the graph construction, while MAP is proven NP-hard.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Adeppady et al. [x] formulated composite edge-application placement as an NP-hard problem that jointly handles stateful and stateless microservices, user mobility, sharing, quality versions, and resource allocation. Their MAP objective trades deployment cost against normalized application quality while constraining response latency, migration downtime, server resources, and radio blocks. STEP constructs and prunes a Dynamic Network Topology Graph, embeds additive latency and downtime budgets in an expanded graph, and selects a minimum-cost path before convex CPU recalibration. Small-scale experiments place STEP within 7% of the optimal CPU cost, while Kubernetes experiments report up to 50% lower deployment cost, 50% higher application quality, and 15% fewer radio resources than the compared schemes. These gains are measured in the paper's emulation and testbed settings and do not imply universal superiority under other workloads or migration runtimes.

## Problem and system model

Applications are chains or DAG-like compositions of microservices. Stateful services carry user/session data and incur migration downtime; stateless services can be relocated and may be shared more broadly. Edge servers attach to base stations, users move between cells, and the orchestrator must preserve latency and downtime requirements while respecting memory, CPU, radio, and microservice-shareability constraints.

## Method

MAP represents placement, user assignment, CPU, and radio decisions, with quality versions allowing resource-quality adaptation. STEP responds to application arrival, termination, or handover by constructing a local DNTG, pruning infeasible or irrelevant vertices, expanding the graph for two additive constraints, selecting a minimum-cost path with Dijkstra, and recalibrating CPU allocation through a convex subproblem.

## Key findings

- MAP is reduced from multidimensional bin packing and proved NP-hard; STEP is a polynomial-time heuristic for the constructed decision graph.
- In the small-scale scenario, STEP is within 7% of optimal CPU cost and remains near-optimal as the graph-resolution parameter varies.
- In large-scale Kubernetes emulation, STEP reports up to 50% lower deployment cost, 50% higher application quality, and 15% lower radio-resource use while request success stays above 90%.
- STEP's quality-cost weight controls the expected trade-off: higher resource emphasis reduces deployment cost but lowers average application quality by up to 10% in the reported sweep.

## Limitations / future work

The migration and relocation times used in the emulation are configured from measured values but treated as fixed per microservice instance. The authors identify proactive migration based on predicted mobility as future work. Results remain tied to the eight-node Kubernetes testbed, selected applications, and modeled edge topology.

## Relation to the corpus

This source is the multi-microservice placement anchor for [[service-migration]] and [[mobile-edge-computing]]. It complements [[calagna-2024-robust-stateful-migration]], which models how a stateful container migrates, and [[chen-2026-hc-mappo-vehicle-twin-migration]], which learns vehicle-twin migration decisions rather than graph-search placement.

## Raw artifacts

- Parse: `raw/sources/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge/Efficient_Management_of_Composite_Heterogeneous_Applications_at_the_Network_Edge.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
