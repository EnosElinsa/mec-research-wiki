---
type: source
title: "MOSE: A Novel Orchestration Framework for Stateful Microservice Migration at the Edge"
authors: ["Antonio Calagna", "Yenchia Yu", "Paolo Giaccone", "Carla Fabiana Chiasserini"]
year: 2025
url: "https://doi.org/10.1109/TNSM.2025.3579051"
venue: "IEEE Transactions on Network and Service Management, 22(5)"
modeling_card: required
tags: [source, stateful-migration, edge-microservices, orchestration, container-migration, uav]
related:
  - "[[stateful-edge-microservice-migration]]"
  - "[[service-migration]]"
  - "[[calagna-2024-robust-stateful-migration]]"
  - "[[calagna-2026-cormo-ran]]"
  - "[[antonio-calagna]]"
  - "[[yenchia-yu]]"
  - "[[carla-fabiana-chiasserini]]"
created: 2026-08-27
updated: 2026-08-27
---

# MOSE: A Novel Orchestration Framework for Stateful Microservice Migration at the Edge

## Citation

Calagna, A., Yu, Y., Giaccone, P., & Chiasserini, C. F. (2025). *MOSE: A Novel Orchestration Framework for Stateful Microservice Migration at the Edge*. **IEEE Transactions on Network and Service Management, 22**(5). DOI: 10.1109/TNSM.2025.3579051.

## TL;DR

MOSE orchestrates stateful microservice migration for moving edge users while preserving application connections and meeting downtime and migration-time targets. It profiles bandwidth, state size, and dirty-page rate, then uses the PAM model to choose a migration mode, bandwidth, and Pre-copy iterations for AAV autopilot and other applications.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A moving aerial or mobile user accesses a stateful microservice through edge hosts. The service may migrate between hosts using Cold, Pre-copy, or Iterative Pre-copy while a COAT overlay preserves the user's connection.

**Problem & objective**: Select migration mode and parameters to meet target downtime and duration, $\min T^{\mathrm{down}}$ subject to $T^{\mathrm{mig}}\leq\theta^{\mathrm{mig}}$ and $T^{\mathrm{down}}\leq\theta^{\mathrm{down}}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Migration mode | $m$ | categorical | Cold, Pre-copy, or Iterative Pre-copy |
| Migration bandwidth | $L$ | positive continuous | Link bandwidth allocated to migration |
| Pre-copy iterations | $I$ | nonnegative integer | Number of iterative memory-transfer rounds |
| Service state size | $M$ | positive continuous | Runtime memory and state volume |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Duration KPI | $T^{\mathrm{mig}}\leq\theta^{\mathrm{mig}}$. |
| Downtime KPI | $T^{\mathrm{down}}\leq\theta^{\mathrm{down}}$. |
| Bandwidth | $L$ is bounded by available source-destination capacity. |
| Dirty state | PAM uses measured or conservative dirty-page rates to bound iterative transfer. |
| Connection | COAT overlay keeps the established connection reachable across relocation. |

**Algorithm**: Edge agents report migration conditions; the orchestrator evaluates PAM bounds, chooses migration mode, and configures bandwidth and iterations. COAT and CRIU/Podman execute the selected migration while preserving connectivity.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Calagna et al. [x] proposed MOSE, an orchestrator for stateful microservice migration at the network edge. MOSE combines CRIU/Podman migration, the COAT overlay for connection continuity, and PAM upper bounds that account for state size, dirty-page rate, processing, and network conditions. Edge agents profile the application and the orchestrator chooses Cold, Pre-copy, or Iterative Pre-copy together with bandwidth and iteration settings to meet downtime and duration targets. Testbed experiments report up to 77% lower downtime than the compared schemes and substantial reductions in transfer overhead for SockPerf and iPerf3 workloads. The measured gains depend on the tested edge stack and conservative model parameters.

## Problem and system model

The framework targets moving AAV or mobile users whose stateful services need to remain reachable while crossing edge-host boundaries. Agents expose bandwidth, service state, and dirty-page information; an orchestrator chooses a migration configuration against application QoE targets.

## Method

MOSE uses PAM's analytical migration and downtime estimates to compare migration modes and determine parameter settings. COAT provides an OvS-based overlay, while Zenoh agents communicate profiles and control commands across the edge infrastructure.

## Key findings

- MOSE-MD and MOSE-MR reduce SockPerf downtime to 975 ms and 1323 ms in the reported cases.
- For iPerf3, corresponding downtime values are 790 ms and 1043 ms, up to 77% below the compared state of the art.
- The orchestration workflow reduces the reported transfer step by about 99% while meeting target KPIs in the tested scenarios.

## Limitations / future work

The evaluations use four OpenStack VMs, two stateful workloads, and selected dirty-page and network conditions. Larger heterogeneous deployments and additional service types require further validation.

## Relation to the corpus

MOSE operationalizes the timing and connection models in [[calagna-2024-robust-stateful-migration]] and extends [[stateful-edge-microservice-migration]] with an edge orchestrator that chooses runtime migration modes.

## Raw artifacts

- Parse: `raw/sources/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge/MOSE_A_Novel_Orchestration_Framework_for_Stateful_Microservice_Migration_at_the_Edge.md`
- Origin PDF and extracted figures are in the same folder.
