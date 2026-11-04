---
type: source
modeling_card: required
title: "Joint Content Caching, Service Placement, and Task Offloading in UAV-Enabled Mobile Edge Computing Networks"
authors: ["Youhan Zhao", "Chenxi Liu", "Xiaoling Hu", "Jianhua He", "Mugen Peng", "Derrick Wing Kwan Ng", "Tony Q. S. Quek"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3460049"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
tags: [source, uav-mec, content-caching, service-placement, task-offloading, qoe, matching-theory, gibbs-sampling]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[service-caching-mec]]"
  - "[[computational-task-caching]]"
  - "[[qoe-modeling-mec]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[task-offloading]]"
  - "[[gao-2024-service-experience-cache-uav]]"
  - "[[zhao-2025-traj-offload-cache-migration]]"
created: 2026-05-29
updated: 2026-11-03
---

# Joint Content Caching, Service Placement, and Task Offloading in UAV-Enabled Mobile Edge Computing Networks

## Citation

Zhao, Y., Liu, C., Hu, X., He, J., Peng, M., Ng, D. W. K., & Quek, T. Q. S. (2024). *Joint Content Caching, Service Placement, and Task Offloading in UAV-Enabled Mobile Edge Computing Networks*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2024.3460049.

## TL;DR

Multiple UAVs with caching and computation serve heterogeneous content and service requests from user equipment (UEs). The authors define an **average QoE** metric — the weighted sum of the content cache-hit ratio and the service delay-shrinkage ratio — and maximize it over content-cache/service-placement decisions (at UAVs) and task-offloading decisions (at UEs). The NP-hard problem is decomposed into a caching/placement sub-problem (**Gibbs sampling**) and an offloading sub-problem (**matching game**), solved iteratively.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple UAVs with finite storage, CPU cores and energy serve UEs that each issue either a content request or a service request. Cache hits avoid content delivery, while placed service programs let the tasks of a service request run on a UAV instead of locally.

**Problem & objective**: Problem P1 in (16) maximizes the average QoE $Q(X_{\mathcal F},X_{\mathcal K},Y)$ in (15), a weighted sum with weight $\alpha\in[0,1]$ of the content cache-hit ratio and the service-delay shrinkage ratio.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Content caching | $x_{u,f}$ | binary | Content $f$ stored at UAV $u$ |
| Service placement | $x_{u,k}$ | binary | Service program $k$ deployed at UAV $u$ |
| Task offloading | $y_{m,n,u}^k$ | binary | Task $n$ of UE $m$'s service request $k$ offloaded to UAV $u$ |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (16a), (16b) | Request type $q_m\in\{0,1\}$; each UE issues at most one content request or one service request |
| (16c) | UAV storage, $\sum_fx_{u,f}c_f+\sum_kx_{u,k}c_k\le\mathrm{St}_u$ |
| (16d) | Each task runs locally or on at most one UAV, $\sum_uy_{m,n,u}^k\le1$ |
| (16e) | UAV CPU cores, $\sum_{m,k,n}y_{m,n,u}^k\le\mathrm{Core}_u$ |
| (16f) | UAV computation energy, $E_u^{\mathrm{pr}}\le E_{\max}$ |

**Algorithm**: For fixed offloading, content caching and service placement are updated by Gibbs sampling over QoE changes. For fixed placement, UE tasks are matched to feasible UAVs through a matching game built from UE–UAV preferences. The two blocks alternate until the average QoE stabilizes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] studied joint content caching, service placement, and task offloading in UAV-enabled mobile edge computing networks. They defined average QoE as a weighted combination of content cache-hit ratio and service delay shrinkage and maximized it under UAV storage, CPU-core, energy, request-type, and offloading constraints. Gibbs sampling updates content and service placement for fixed offloading. A matching game associates UE tasks with feasible UAVs for fixed placement, and the two blocks iterate. Numerical results report about 30% higher average QoE than a non-cooperative scheme with similar cache-hit ratio, and better QoE than content-first, service-first, and greedy offloading schemes.

## Problem framing

A UAV-enabled MEC network must satisfy both content requests (cacheable data) and service requests (computation), under UAV caching/computation limits. A single metric — average QoE combining cache hit ratio and service delay shrinkage — captures how well the network serves UEs, and depends jointly on caching, placement, and offloading.

## System model

- **Actors.** Multiple UAVs (caching + computation) serving UEs with heterogeneous content + service requests.
- **Metric.** Average QoE = weighted sum of content cache-hit ratio and service delay-shrinkage ratio ([[qoe-modeling-mec]]).
- **Decisions.** UAV content-cache + service placement; UE task offloading — subject to caching/computation capability constraints.

## Method

- Decompose the NP-hard QoE-maximization into:
  - **Content cache + service placement:** Gibbs-sampling-based algorithm.
  - **Task offloading:** [[matching-theory-for-resource-allocation|matching game]]-based algorithm.
- Solve iteratively.

## Key findings

- Numerical results validate effectiveness and show significant average-QoE improvement over benchmarks, **especially when UAV caching/computation capabilities are constrained** (the paper's stated headline regime).

## Limitations / future work

Simulation-based; the parse's conclusion does not enumerate explicit future work.

## Relation to the corpus

Joins the **caching/service-placement** offloading thread with [[gao-2024-service-experience-cache-uav]] (service-experience-oriented cache-enabled UAV MEC) and [[zhao-2025-traj-offload-cache-migration]] (trajectory+offload+cache+migration). Its Gibbs-sampling + matching decomposition adds variety to the matching-theory family ([[jia-2022-hierarchical-aerial-matching]], [[nabi-2025-jour-hierarchical-aerial]]). Introduces/reinforces [[service-caching-mec]] and [[qoe-modeling-mec]].

## Raw artifacts

- `raw/sources/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks.md`
- Original PDF and extracted figures in the same folder.
