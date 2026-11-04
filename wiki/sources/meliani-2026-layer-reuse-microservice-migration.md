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
updated: 2026-11-03
---

# Layer-Reuse Aware Optimization for Efficient Microservice Migration in UAV Edge Systems

## Citation

Meliani, A. E., Bagaa, M., & Ksentini, A. (2026). *Layer-Reuse Aware Optimization for Efficient Microservice Migration in UAV Edge Systems*. **IEEE International Conference on Communications (ICC)**. DOI: 10.1109/ICC59461.2026.11588261.

## TL;DR

This paper optimizes UAV-edge microservice placement and migration while accounting for Docker image-layer reuse, registry selection, routing, migration count, and end-to-end latency SLAs. A Gurobi mixed-integer model provides an optimal baseline for later heuristic or learning-based methods.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV application is a graph of communicating microservices $M$ (edges $\mathcal E$) hosted on edge servers $V$ of an infrastructure graph. Container images share Docker layers; a server that lacks some layers of microservice $v$ ($\varphi_{i,v}=1$) pulls them from one registry in $R$, and $\mathcal V'_{v,i}$ records the previous placement.

**Problem & objective**: A weighted-sum MILP minimizes $\frac{1}{|M|}(\alpha\sum_v\mathcal T_v+\beta\sum_v\phi_v)+\frac{\gamma}{|\mathcal E|}\sum_{(u,v)}z_{u,v}$ with $\alpha+\beta+\gamma=1$: provisioning-time SLA violations, relocations, and end-to-end latency SLA violations.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Placement | $\mathcal V_{v,i}$ | binary | Microservice $v$ is hosted on edge $i$ |
| Routing | $\mathcal X_{i,j}^{u,v}$ | binary | Link $(i,j)$ carries traffic from $u$ to $v$ |
| Registry choice | $\chi_{i,r}^v$ | binary | Edge $i$ pulls missing layers of $v$ from registry $r$ |
| Relocation flag | $\phi_v$ | binary | $v$ changed its edge |
| SLA flags | $z_{u,v}$, $\mathcal T_v$ | binary | Latency SLA violated; provisioning time $\zeta_v$ exceeds $B_u$ |
| Delay intervals | $\mu_{i,j}^k$ | binary | Piecewise interval for linearizing the queueing delay |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (3) | Each microservice on exactly one edge: $\sum_i\mathcal V_{v,i}=1$ |
| (4)–(5) | Traffic leaves the edge hosting $u$ and enters the edge hosting $v$ |
| (6)–(7) | Loop-free, continuous paths (big-$\mathcal A$ linearization) |
| (10)–(13) | Link load $\Lambda_{i,j}$ within the piecewise breakpoints; one interval per used link; linearized end-to-end delay |
| (14) | $z_{u,v}=1$ when $D_{e2e}^{u,v}\ge W_{u,v}$ |
| (15)–(19) | Provisioning cost $\zeta_v=\sum_{i,r}\psi_{i,r}^v\chi_{i,r}^v$; a registry only if $v$ is hosted there and layers are missing, and at most one registry |
| (20) | $\mathcal T_v=1$ when $\zeta_v\ge B_u$ |
| (22)–(23) | $\phi_v$ marks a change from the previous placement $\mathcal V'_{v,i}$ |

**Algorithm**: Solve the MILP with Gurobi (60 s time limit), averaging 1000 repetitions over application graphs built from the 100 most-downloaded Docker Hub images; the paper treats the exact model as a baseline for future heuristics.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Meliani et al. [x] formulated layer-aware microservice migration for UAV-assisted edge applications. Their mixed-integer model jointly selects service placements, registries, routes, and migrations while penalizing provisioning-time and end-to-end latency SLA violations. Docker's shared immutable layers reduce the transfer required when the destination already caches part of an image. Gurobi experiments show that more registries and cached layers reduce provisioning violations, reaching zero in the fully preloaded case, while larger infrastructures increase migration decisions. The optimization is intended as an exact baseline; execution-time metrics, an energy objective, and comparisons with heuristic and learning-based strategies are left for future work.

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
