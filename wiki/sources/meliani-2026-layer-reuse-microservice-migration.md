---
type: source
title: "Layer-Reuse Aware Optimization for Efficient Microservice Migration in UAV Edge Systems"
authors: ["Abd Elghani Meliani", "Miloud Bagaa", "Adlen Ksentini"]
year: 2026
url: "https://doi.org/10.1109/ICC59461.2026.11588261"
venue: "IEEE International Conference on Communications (ICC)"
modeling_card: required
tags: [source, uav-edge, microservices, service-migration, container-layered-storage, sla, optimization]
related:
  - "[[container-layered-storage-migration]]"
  - "[[service-migration]]"
  - "[[stateful-edge-microservice-migration]]"
  - "[[multi-microservice-application-placement]]"
created: 2026-08-27
updated: 2026-08-27
---

# Layer-Reuse Aware Optimization for Efficient Microservice Migration in UAV Edge Systems

## Citation

Meliani, A. E., Bagaa, M., & Ksentini, A. (2026). *Layer-Reuse Aware Optimization for Efficient Microservice Migration in UAV Edge Systems*. **IEEE International Conference on Communications (ICC)**. DOI: 10.1109/ICC59461.2026.11588261.

## TL;DR

This paper optimizes UAV-edge microservice placement and migration while accounting for Docker image-layer reuse, registry selection, routing, migration count, and end-to-end latency SLAs. A Gurobi mixed-integer model provides an optimal baseline for later heuristic or learning-based methods.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV application is represented as communicating microservices deployed on geographically distributed edge servers. Servers cache image layers and may host registries; mobility can require a migratable service to move while non-migratable components remain on the UAV.

**Problem & objective**: Minimize the weighted provisioning-time violations, migration flags, and latency-SLA violations used by the paper, $\min\alpha T_v+\beta\varphi_v+\gamma z_{u,v}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Service placement | $y_{u,i}$ | binary | Host microservice $u$ on server $i$ |
| Registry choice | $\chi_{i,r}^{u}$ | binary | Registry $r$ supplies missing layers to server $i$ |
| Path selection | $X_{i,j}^{u,v}$ | binary | Link $(i,j)$ belongs to the route between services |
| Migration flag | $\varphi_{i,u}$ | binary | At least one layer is missing at destination $i$ |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Hosting | Each migratable microservice is assigned to an eligible edge server. |
| Layer reuse | Cached layers reduce missing-layer transfer and provisioning time. |
| Path | Selected routes obey link capacity and flow continuity. |
| SLA | End-to-end delay and provisioning time remain within application bounds. |
| Non-migratable | UAV-local components remain fixed. |

**Algorithm**: Solve the weighted mixed-integer formulation with Gurobi over placement, registry, path, and migration variables; use the optimum as a benchmark for scalable methods.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Meliani et al. [x] formulated layer-aware microservice migration for UAV-assisted edge applications. Their mixed-integer model jointly selects service placements, registries, routes, and migrations while penalizing provisioning-time and end-to-end latency SLA violations. Docker's shared immutable layers reduce the transfer required when the destination already caches part of an image. Gurobi experiments show that more registries and cached layers reduce provisioning violations, reaching zero in the fully preloaded case, while larger infrastructures increase migration decisions. The optimization is intended as an exact baseline; execution-time energy objectives and scalable heuristics are left for future work.

## Problem and system model

Microservices form an application graph with link capacities, tolerated inter-service delays, image layers, and provisioning bounds. Geographically distributed edge servers store subsets of layers and may fetch missing layers from selected registries.

## Method

The model computes effective transmission, propagation, queueing, and processing delay, then jointly optimizes placement, path, registry, and migration variables under capacity and SLA constraints.

## Key findings

- Increasing registry count removes provisioning violations when registry coverage is sufficient.
- Cached layers steadily reduce provisioning violations, reaching zero when all tested images are preloaded.

## Limitations / future work

The current objective omits execution-time and energy terms. The authors propose heuristic and learning-based approaches for larger dynamic deployments.

## Relation to the corpus

This source is a direct layer-reuse counterpart to [[container-layered-storage-migration]] and connects Docker image caching to [[service-migration]] in UAV edge systems.

## Raw artifacts

- Parse: `raw/sources/Layer-Reuse_Aware_Optimization_for_Efficient_Microservice_Migration_in_UAV_Edge_Systems/Layer-Reuse_Aware_Optimization_for_Efficient_Microservice_Migration_in_UAV_Edge_Systems.md`
- Origin PDF and figures are in the same folder.
