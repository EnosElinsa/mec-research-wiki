---
type: source
title: "Serv-HU: Service Hand-off for UAV-as-a-Service"
authors: ["Arijit Roy", "Veera Manikantha Rayudu Tummala", "Vinay Yadam"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: required
tags: [source, uav-as-a-service, service-handoff, pricing, service-provider-selection, optimization]
related:
  - "[[differentiated-uav-service-market]]"
  - "[[service-migration]]"
  - "[[contract-theory]]"
created: 2026-08-27
updated: 2026-08-27
---

# Serv-HU: Service Hand-off for UAV-as-a-Service

## Citation

Roy, A., Tummala, V. M. R., & Yadam, V. *Serv-HU: Service Hand-off for UAV-as-a-Service*. Venue and year are not in the parse.

## TL;DR

Serv-HU lets a primary UAV service provider hand uncovered portions of a requested area to selected secondary providers, then computes a price that accounts for all participating providers. Lagrangian and KKT-based optimization lowers the charged price by 10.3% to 12.7% relative to random secondary-provider selection in simulation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An end user requests UAV service over an application area from a primary provider whose own fleet cannot cover the whole area. Eligible secondary service providers can supply UAV capacity for the uncovered region.

**Problem & objective**: Select secondary providers and determine the end-user charge to minimize service price, $\min P$, while covering the requested area and accounting for provider cost and eligibility.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Provider selection | $x_i$ | binary | Whether secondary provider $i$ participates |
| Assigned coverage | $a_i$ | nonnegative | Application area delegated to provider $i$ |
| Charged price | $P$ | nonnegative | Total price paid by the end user |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Coverage | Primary and selected secondary providers cover the full requested application area. |
| Eligibility | A selected provider must meet review, price, coverage, and service criteria. |
| Capacity | Assigned area does not exceed the UAV resources available from each provider. |
| Pricing | The charge includes the primary and secondary provider costs under the derived KKT conditions. |

**Algorithm**: First filter and optimize the selection of secondary providers for the uncovered area. Then solve the provider-aware pricing problem using a Lagrangian and Karush-Kuhn-Tucker conditions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Roy et al. [x] considered service handoff between providers in a UAV-as-a-Service platform when a primary provider cannot cover the entire requested region. Their two-stage formulation first selects eligible secondary providers using coverage, review, and cost information, then derives the price charged to the end user. The selection and pricing conditions are obtained through Lagrangian analysis and Karush-Kuhn-Tucker conditions. Simulations report a 10.3% to 12.7% price reduction relative to random secondary-provider selection. The study addresses provider-level coverage and pricing rather than runtime container or computation-service migration.

## Problem and system model

The platform distinguishes UAV owners, a primary service provider, secondary providers, and end users. The primary provider remains the user's interface but can delegate uncovered area when its available UAV resources are insufficient.

## Method

Serv-HU evaluates candidate providers by their service record, coverage, unit-area price, and eligibility. It optimizes which candidates serve the uncovered region and then derives the joint charge for the primary and secondary participation.

## Key findings

- Optimized provider selection reduces charged price by 10.3% to 12.7% over random selection in the reported simulations.
- Selection depends on coverage, reviews, eligibility, and per-area price rather than price alone.
- The mechanism provides full requested-area coverage through provider cooperation.

## Limitations / future work

The work is simulation-based. Future directions stated in the paper include multi-hop task handoff among heterogeneous UAVs and a broader pricing mechanism for all financial actors in the platform.

## Relation to the corpus

This source adds provider-level service continuity to UAV-as-a-Service. Its handoff is organizational and economic, whereas [[service-migration]] pages usually move application state or computing tasks between edge nodes.

## Raw artifacts

- Parse: `raw/sources/Serv-HU_Service_Hand-off_for_UAV-as-a-Service/Serv-HU_Service_Hand-off_for_UAV-as-a-Service.md`
- Origin PDF and extracted figures are in the same folder.
