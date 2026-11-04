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
updated: 2026-11-03
---

# Serv-HU: Service Hand-off for UAV-as-a-Service

## Citation

Roy, A., Tummala, V. M. R., & Yadam, V. *Serv-HU: Service Hand-off for UAV-as-a-Service*. Venue and year are not in the parse.

## TL;DR

Serv-HU lets a primary UAV service provider hand uncovered portions of a requested area to selected secondary providers, then computes a price that accounts for all participating providers. Lagrangian and KKT-based optimization lowers the charged price by 10.3% to 12.7% relative to random secondary-provider selection in simulation.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: In a UAV-as-a-Service platform, an end user requests service over an area that the primary service provider (PSP) cannot fully cover with its own UAVs. The PSP hands off the uncovered residual area to secondary service providers (SSPs), whose eligibility $e(SP_i)$, review score $\phi(SP_i)$, and coverage factor $\lambda^i$ define a selection factor $SF_i=e(SP_i)\phi(SP_i)\lambda^i$ in (12).

**Problem & objective**: A two-stage design. Stage 1, (13), chooses the area each SSP serves to maximize its selection factor, $\arg\max_{A^i}SF_i$. Stage 2, (40), chooses the price the PSP charges the end user, $\arg\max_{C_{in}^{PSP}}UF_{PSP}$, with utility $UF_{PSP}=R_E-\ln(\Gamma(R_E))$ in (39) and relative cash outflow $R_E=C_{out}^{PSP}/C_{in}^{PSP}$.

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| SSP service area | $A^i$ | continuous, at most $A_{res}^i$ | Residual area delegated to SSP $i$ |
| Charged price | $C_{in}^{PSP}$ | continuous, positive | Amount the end user pays the PSP |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (14a) | SSP area within the residual area: $A^i\le A_{res}^i$ |
| (14b) | Review score bound: $\phi(SP_i)\le100$ |
| (41) | Cash outflow does not exceed inflow: $R_E\le1$ |
| Algorithm rule | Selection repeats until the served area reaches the residual area (Corollary 1); a failed SSP is replaced by $\arg\max_ie(SP_i)\phi(SP_i)/C_{in}^i$ in (19) |

**Algorithm**: Solve each stage with a Lagrangian and KKT conditions: (15)–(18) give the optimal SSP area $A^{i*}=A_{res}^i\exp(-\mu_1C_{in}^i/(S_p^{\max}\phi(SP_i)e(SP_i)))$, and (42)–(43) give the optimal charged price; Algorithm 1 computes provider reviews.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Roy et al. [x] considered service handoff between providers in a UAV-as-a-Service platform when a primary provider cannot cover the entire requested region. Their two-stage formulation first selects eligible secondary providers using coverage, review, and cost information, then sets the price the primary provider charges the end user by maximizing a concave utility of its relative cash outflow. The selection and pricing conditions are obtained through Lagrangian analysis and Karush-Kuhn-Tucker conditions. Simulations report a 10.3% to 12.7% price reduction relative to random secondary-provider selection. The study addresses provider-level coverage and pricing rather than runtime container or computation-service migration.

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
