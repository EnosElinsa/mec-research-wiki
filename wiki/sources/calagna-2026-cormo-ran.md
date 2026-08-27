---
type: source
title: "CORMO-RAN: Energy Efficiency at the Near-RT RIC via Lossless Migration of O-RAN xApps"
authors: ["Antonio Calagna", "Stefano Maxenti", "Leonardo Bonati", "Salvatore D’Oro", "Tommaso Melodia", "Carla Fabiana Chiasserini"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3715058"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, open-ran, near-rt-ric, xapp, stateful-migration, energy-efficiency, mixed-integer-optimization]
related:
  - "[[open-radio-access-network]]"
  - "[[network-function-virtualization]]"
  - "[[stateful-edge-microservice-migration]]"
  - "[[service-migration]]"
  - "[[calagna-2024-robust-stateful-migration]]"
  - "[[carla-fabiana-chiasserini]]"
created: 2026-08-27
updated: 2026-08-27
---

# CORMO-RAN: Energy Efficiency at the Near-RT RIC via Lossless Migration of O-RAN xApps

## Citation

Calagna, A., Maxenti, S., Bonati, L., D’Oro, S., Melodia, T., & Chiasserini, C. F. (2026). *CORMO-RAN: Energy Efficiency at the Near-RT RIC via Lossless Migration of O-RAN xApps*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3715058.

## TL;DR

CORMO-RAN jointly activates near-RT RIC compute nodes and migrates stateful O-RAN xApps during low-traffic periods. It compares stateful migration with an O-RAN Shared Data Layer, preserves xApp state, and solves a server-activation and xApp-migration MIQP to reduce cluster energy while meeting downtime and control-loop timing constraints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A near-RT RIC cluster hosts heterogeneous stateful xApps on resource-constrained servers. A non-RT RIC rApp periodically or event-wise consolidates xApps, migrates them from servers that can be switched off, and keeps their control service available through stateful migration or a shared data layer.

**Problem & objective**: Minimize cluster energy, $\min_{\mathbf{x},\boldsymbol\mu}\sum_{s\in\mathcal S}E_s$, including server execution, migration, and shared-data-layer maintenance energy.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Server activation | $\mu_s$ | Binary | 1 when server $s$ remains active |
| xApp reallocation | $x_{k,s,s'}$ | Nonnegative integer | Number of class-$k$ xApps moved from $s$ to $s'$; $s=s'$ means retained |
| Migration strategy | $\tau$ | Categorical, SDL/SM-MR/SM-MD | Stateful migration or shared-data-layer mode |
| Initial switchability | $\alpha_s$ | Binary parameter | Whether server $s$ may be turned off |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | All currently deployed xApps are reallocated exactly once: $\sum_{s'}x_{k,s,s'}=n^0_{k,s}$. |
| C2 | xApps are instantiated only on active servers and no xApps remain on the virtual source server. |
| C3 | CPU, memory, and disk usage satisfy $R_{\chi_s}\le R_{\chi_s}^{\max}\mu_s$ for each resource $\chi$. |
| C4 | Only switchable servers can be shut down: $\mu_s\ge1-\alpha_s$. |
| C5 | Migration downtime and SDL maintenance remain within $T_{D_s}^{\max}$ and the near-RT deadline $T_{DF}^{\max}$. |

**Algorithm**: Build migration-energy terms from experimental state-size, dirty-page, and timing measurements, then solve the server activation and lossless migration MIQP with branch-and-bound/Gurobi; compare SDL, downtime-minimizing SM-MD, and resource-minimizing SM-MR.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Calagna et al. [x] studied lossless migration of stateful O-RAN xApps as a joint server-activation and migration problem for the near-RT RIC. They minimized cluster energy by choosing active servers, xApp reallocations, and either shared-data-layer or stateful-migration operation under resource, downtime, and control-loop deadline constraints. The paper experimentally compared Shared Data Layer, resource-minimizing stateful migration, and downtime-minimizing stateful migration for diverse xApp classes on a Red Hat OpenShift private-5G testbed. The resulting MIQP identifies feasible allocations and achieves up to 64% energy reduction against an always-active OpenShift baseline in low-load configurations. The evaluation is experimental and optimization-based, not a proof of a universally optimal migration policy outside the modeled cluster.

## Problem and system model

O-RAN xApps can be numerous and stateful, while low-traffic periods leave compute nodes underused. Turning off nodes saves energy, but xApp state, migration downtime, shared-data consistency, and near-RT control deadlines must be preserved. The system uses a non-RT RIC rApp to coordinate a near-RT RIC cluster, with xApps grouped by class and hosted on identical resource-constrained servers in the evaluated testbed.

## Method

The paper compares stateful migration (cold SM-MR or iterative-precopy SM-MD) with an O-RAN Shared Data Layer that externalizes xApp state to a strongly consistent etcd backend. CORMO-RAN measures migration and maintenance costs, formulates the Server Activation and Lossless stateful xApp migration problem, and solves its mixed-integer quadratic formulation with branch-and-bound. The experimental prototype uses Red Hat OpenShift, commercial radio units, and real xApps.

## Key findings

- Shared Data Layer gives zero migration downtime in the tested setup but adds backend maintenance and consistency overhead.
- Stateful migration can use less energy than SDL when node shutdown is feasible; SM-MR and SM-MD trade resource usage against downtime.
- The MIQP is solved optimally within one second for about 120 xApps in the reported configuration; larger cases hit the 300-second early-stop limit with a reported gap up to 10% for 200 xApps under SM-MD.
- CORMO-RAN reaches up to 64% energy reduction versus the always-active, OpenShift-default scheduling baseline in low-load settings.

## Limitations / future work

The evaluation uses a four-node cluster, modeled xApp classes, and a private-5G testbed; heterogeneous cluster extensions are discussed but not experimentally validated. Large deployments may require approximation because the MIQP runtime reaches the early-stop limit. The paper does not claim a global guarantee beyond the solved instance and modeled energy terms.

## Relation to the corpus

This source specializes [[open-radio-access-network]] with near-RT RIC xApp lifecycle control and connects [[service-migration]] to energy-aware server activation. It extends [[calagna-2024-robust-stateful-migration]] from connection-preserving container migration to O-RAN-specific orchestration and Shared Data Layer consistency.

## Raw artifacts

- Parse: `raw/sources/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps/CORMO-RAN_Energy_Efficiency_at_the_Near-RT_RIC_via_Lossless_Migration_of_O-RAN_xApps.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
