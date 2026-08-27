---
type: source
title: "Design, Modeling, and Implementation of Robust Migration of Stateful Edge Microservices"
authors: ["Antonio Calagna", "Yenchia Yu", "Paolo Giaccone", "Carla Fabiana Chiasserini"]
year: 2024
url: "https://doi.org/10.1109/TNSM.2023.3331750"
venue: "IEEE Transactions on Network and Service Management (IEEE TNSM), 21(2), 1877-1893"
modeling_card: required
tags: [source, stateful-migration, edge-microservices, container-migration, connection-migration, migration-modeling, uav]
related:
  - "[[stateful-edge-microservice-migration]]"
  - "[[service-migration]]"
  - "[[container-layered-storage-migration]]"
  - "[[uav-trajectory-control]]"
  - "[[calagna-2026-cormo-ran]]"
  - "[[antonio-calagna]]"
  - "[[yenchia-yu]]"
created: 2026-08-27
updated: 2026-08-27
---

# Design, Modeling, and Implementation of Robust Migration of Stateful Edge Microservices

## Citation

Calagna, A., Yu, Y., Giaccone, P., & Chiasserini, C. F. (2024). *Design, Modeling, and Implementation of Robust Migration of Stateful Edge Microservices*. **IEEE Transactions on Network and Service Management, 21**(2), 1877-1893. DOI: 10.1109/TNSM.2023.3331750.

## TL;DR

COAT preserves an established transport connection while migrating a stateful container, and PAM models migration duration and downtime with processing, memory, network, and tool overheads. Podman/CRIU experiments with MQTT Broker and Memcached validate the model, which is then used to configure migration bandwidth and iterations for a UAV autopilot service.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A stateful edge microservice serves a mobile end user, potentially a UAV autopilot, through a TCP connection. Iterative PreCopy transfers memory and container state while the source runs; COAT adds an overlay network so the connection can continue after the destination restores the service.

**Problem & objective**: Configure migration parameters to satisfy KPI bounds, $T^{\mathrm{down}}_{\mathrm{coat}}\le\theta^{\mathrm{down}}$ and $T^{\mathrm{mig}}_{\mathrm{coat}}\le\theta^{\mathrm{mig}}$, while characterizing the migration duration and downtime.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Inter-server bandwidth | $L$ | Positive continuous | Allocated migration-link bandwidth |
| PreCopy iterations | $I$ | Nonnegative integer | Number of iterative dump rounds |
| Dirty-page rate | $\hat R$ | Scenario parameter | Worst-case memory dirtiness used for an upper bound |
| Microservice state size | $M$ | Positive continuous | Memory state volume transferred during migration |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | COAT downtime must satisfy the target bound, with bandwidth chosen using the paper's inequality (33). |
| C2 | Total COAT migration duration must satisfy $T^{\mathrm{mig}}_{\mathrm{coat}}\le\theta^{\mathrm{mig}}$. |
| C3 | Iteration count is selected as a nonnegative integer, bounded by the migration-duration expression (34). |
| C4 | The UAV safety requirement is $D_s(v)\le D_s^*$, where stopping distance includes reaction and braking distance. |
| C5 | The PAM upper bound uses $\hat R=R_{\max}$ for worst-case dirty-page behavior; it is not a global performance guarantee outside the measured tool/model parameters. |

**Algorithm**: Implement CRIU and Podman migration with COAT's OvS overlay network, measure processing and transfer components on MQTT Broker/Memcached, fit PAM's analytical upper bounds, and use the resulting inequalities to select bandwidth and iteration settings for the UAV autopilot case.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Calagna et al. [x] addressed stateful edge-microservice migration together with preservation of an established transport connection. Their COAT overlay network avoids client reconnection, while the PAM model accounts for CRIU and Podman processing, memory dirtiness, network transfer, and relocation overhead when estimating migration duration and downtime. Experiments with MQTT Broker and Memcached show that PAM predicts the measured KPIs much more accurately than the compared state-of-the-art model. The authors then use bandwidth and iteration inequalities to configure migration for a UAV autopilot while bounding stopping distance during downtime. The results are testbed measurements and model-conditional upper bounds, not a theorem that every container runtime or network satisfies the same timing.

## Problem and system model

Stateful migration must move CPU context, memory, sockets, and open files while keeping a mobile user's transport connection usable. The paper focuses on TCP and uses CRIU checkpoint/restore with Podman containers. Iterative PreCopy transfers dirty pages before a final Stop-and-Copy phase; COAT adds a source, destination, and mobile-device overlay network to preserve reachability when addresses or private networks change.

## Method

The PAM model decomposes migration into CRIU freezing, processing, memory, network, Podman, and COAT overlay components. It derives total duration and downtime expressions for traditional and COAT migration, then evaluates upper bounds at minimum and maximum dirty-page rates. A UAV autopilot example maps downtime to reaction distance and derives required migration bandwidth for a safety threshold.

## Key findings

- PAM's prediction error for total migration duration is reported as up to 99.7% smaller than the compared state-of-the-art model, with a 64.4% reduction reported for downtime prediction.
- Processing overhead can dominate transfer time at high bandwidth, so a network-only model underestimates migration KPIs.
- Larger state size and dirty-page rate tighten bandwidth and downtime requirements; for small state sizes, extra PreCopy iterations may provide little benefit.
- The UAV autopilot analysis shows required bandwidth increases with UAV speed and dirty-page rate when stopping-distance safety is enforced.

## Limitations / future work

The validation uses MQTT Broker and Memcached plus a modeled UAV autopilot; other runtimes, protocols, and wireless conditions are not demonstrated. PAM is an analytical model calibrated with the tested tools and parameters, so its bounds are conditional. The paper does not claim that COAT removes all migration downtime.

## Relation to the corpus

This source is the detailed stateful-migration anchor for [[service-migration]] and [[stateful-edge-microservice-migration]]. It provides the migration-KPI model reused by [[calagna-2026-cormo-ran]] and complements [[container-layered-storage-migration]], which reduces Docker file-system transfer volume rather than preserving TCP state.

## Raw artifacts

- Parse: `raw/sources/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices/Design_Modeling_and_Implementation_of_Robust_Migration_of_Stateful_Edge_Microservices.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
