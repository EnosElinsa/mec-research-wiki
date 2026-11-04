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
updated: 2026-11-03
---

# MOSE: A Novel Orchestration Framework for Stateful Microservice Migration at the Edge

## Citation

Calagna, A., Yu, Y., Giaccone, P., & Chiasserini, C. F. (2025). *MOSE: A Novel Orchestration Framework for Stateful Microservice Migration at the Edge*. **IEEE Transactions on Network and Service Management, 22**(5). DOI: 10.1109/TNSM.2025.3579051.

## TL;DR

MOSE orchestrates stateful microservice migration for moving edge users while preserving application connections and meeting downtime and migration-time targets. It profiles bandwidth, state size, and dirty-page rate, then uses the PAM model to choose a migration mode, bandwidth, and Pre-copy iterations for AAV autopilot and other applications.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An autonomous aerial vehicle (AAV) or other mobile user reaches stateful microservices on the edge server co-located with its serving gNB, so the services must follow it when the gNB changes. MOSE orchestrates the migration with CRIU/Podman, the COAT overlay preserves the established connection, and edge agents profile the microservice and network.

**Problem & objective**: This is an orchestration design with no formal optimization problem. Given target KPIs (migration duration $T^{\mathrm{mig}}$ and downtime $T^{\mathrm{down}}$) and the vertical's objective, either minimizing resource usage (bandwidth and CPU) or minimizing downtime, MOSE picks and configures a migration strategy using PAM upper bounds.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Migration strategy | Cold / PreCopy / Iterative PreCopy | categorical | Technique chosen by the migration designer (no symbol in the paper) |
| Migration bandwidth | $L$ | continuous, at most the available bandwidth | Bandwidth the network controller allocates |
| PreCopy iterations | $I$ | nonnegative integer | Iterations for Iterative PreCopy |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| Model rule | Resource-usage objective: Cold Migration, with PAM giving the minimum bandwidth that meets the downtime target, checked against the available bandwidth |
| Model rule | Downtime objective: Iterative PreCopy, first checked against the migration-duration target, then given the largest iteration count that meets it |
| Model rule | PAM uses the maximum dirty-page rate, so the KPIs are upper bounds independent of the iteration index |

**Algorithm**: The migration task handler passes target KPIs and the objective; the profiling module collects metrics from source and destination agents; the migration designer runs the configuration algorithm (Fig. 5) and sends strategy, bandwidth, and iteration count to the agents over Zenoh, which run the COAT migration.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Calagna et al. [x] proposed MOSE, an orchestrator for stateful microservice migration at the network edge. MOSE combines CRIU/Podman migration, the COAT overlay for connection continuity, and PAM upper bounds that account for state size, dirty-page rate, processing, and network conditions. Edge agents profile the application and the orchestrator chooses Cold, Pre-copy, or Iterative Pre-copy together with bandwidth and iteration settings to meet downtime and duration targets. Testbed experiments with SockPerf and iPerf3 report up to 77% lower downtime than the state of the art, mainly because Zenoh signaling removes the SSH overhead of the transfer step. The measured gains depend on the tested edge stack and conservative model parameters.

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
