---
type: source
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
updated: 2026-05-29
---

# Joint Content Caching, Service Placement, and Task Offloading in UAV-Enabled Mobile Edge Computing Networks

## Citation

Zhao, Y., Liu, C., Hu, X., He, J., Peng, M., Ng, D. W. K., & Quek, T. Q. S. (2024). *Joint Content Caching, Service Placement, and Task Offloading in UAV-Enabled Mobile Edge Computing Networks*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2024.3460049.

## TL;DR

Multiple UAVs with caching and computation serve heterogeneous content and service requests from user equipment (UEs). The authors define an **average QoE** metric — the weighted sum of the content cache-hit ratio and the service delay-shrinkage ratio — and maximize it over content-cache/service-placement decisions (at UAVs) and task-offloading decisions (at UEs). The NP-hard problem is decomposed into a caching/placement sub-problem (**Gibbs sampling**) and an offloading sub-problem (**matching game**), solved iteratively.

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

- `raw/sources/Joint_Content_Caching_Service_Placement_and_Task_Offloading_in_UAV-Enabled_Mobile_Edge_Computing_Networks/full.md`
- Original PDF and extracted figures in the same folder.
