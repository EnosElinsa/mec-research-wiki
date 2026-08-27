---
type: source
title: "Multi-Cell Mobile Edge Computing: Joint Service Migration and Resource Allocation"
authors: ["Zezu Liang", "Yuan Liu", "Tat-Ming Lok", "Kaibin Huang"]
year: 2021
url: "https://doi.org/10.1109/TWC.2021.3070974"
venue: "IEEE Transactions on Wireless Communications, 20(9)"
modeling_card: required
tags: [source, mobile-edge-computing, service-migration, handover, resource-allocation, matching-theory]
related:
  - "[[service-migration]]"
  - "[[task-offloading]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[mobile-edge-computing]]"
created: 2026-08-27
updated: 2026-08-27
---

# Multi-Cell Mobile Edge Computing: Joint Service Migration and Resource Allocation

## Citation

Liang, Z., Liu, Y., Lok, T.-M., & Huang, K. (2021). *Multi-Cell Mobile Edge Computing: Joint Service Migration and Resource Allocation*. **IEEE Transactions on Wireless Communications, 20**(9). DOI: 10.1109/TWC.2021.3070974.

## TL;DR

Joint migration-and-handover assigns each user's VM and radio link to a base-station MEC server while balancing offloading rate against migration cost. A relaxation, fractional-programming iteration, and matching-based integer recovery produces near-upper-bound performance and exposes a user-count threshold for hotspot load balancing.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple mobile users offload through a cellular MEC network. Each user has a dedicated VM whose server can change with radio handover, while cohosted VMs create I/O interference and servers have finite capacity.

**Problem & objective**: Maximize weighted offloading throughput minus migration cost, $\max_{\mathbf X}\sum_k\omega_k R_k(\mathbf X)-\lambda C_k(\mathbf X)$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Joint association | $x_{k,n}$ | binary | Whether user and VM $k$ use BS/server $n$ |
| Server load | $y_n$ | nonnegative integer | Number of VMs assigned to server $n$ |
| Radio allocation | $\beta_{k,n}$ | continuous | Radio resource assigned to user $k$ at BS $n$ |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Unique association | Each user and its VM select one BS/server. |
| Server capacity | $\sum_k x_{k,n}\leq M_n$ for server capacity $M_n$. |
| Integrality | $x_{k,n}\in\{0,1\}$. |
| Radio budget | Resource shares at a base station remain within its available radio budget. |
| Migration | Changing the previous VM host incurs the modeled backhaul migration cost. |

**Algorithm**: Relax binary association, solve the integer-relaxed sum-of-ratios problem iteratively, round aggregate server loads using derived properties, and recover individual assignments as a linear assignment problem solved by the Hungarian algorithm.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Liang et al. [x] coupled cellular handover with VM service migration and computation-radio resource management in multi-cell MEC. Their objective maximizes weighted offloading rate while penalizing migration cost and accounting for server capacity, virtualization, wireless access, and VM I/O interference. The proposed method relaxes binary association, solves the relaxed fractional problem iteratively, and uses matching-based integer recovery. Simulations place the result close to the relaxed upper bound and show a 34% utility gain over the radio-oriented baseline at 90 users in the reported setting. A hotspot extension reveals a user-count threshold beyond which helper-server capacity cannot preserve load balance.

## Problem and system model

Wireless reliability may favor a new base station while computation load and VM migration cost favor retaining the current host. I/O contention makes computation performance depend nonlinearly on how many VMs share each server.

## Method

The algorithm exploits the structure of the relaxed association problem, converts aggregate loads back to integers, and recovers per-user assignments through matching. A separate hotspot-mitigation formulation uses nearby idle servers to absorb overloaded-cell demand.

## Key findings

- The proposed policies perform close to the integer-relaxation upper bound over the reported settings.
- Communication dominates when user count is small, while computation and I/O interference dominate at larger load.
- Hotspot load balancing works only up to a capacity-dependent user threshold.

## Limitations / future work

The evaluation is simulation-based and uses the paper's VM I/O-interference and wireless models. Close-to-optimal performance refers to comparison with the relaxation bound, not a proof of global integer optimality.

## Relation to the corpus

This source is an analytical joint handover and [[service-migration]] anchor. It complements learning-based vehicular migration in [[chen-2025-srcl-iov-service-migration]] and two-timescale migration and task rerouting in [[shi-2023-two-timescale-migration-rerouting]].

## Raw artifacts

- Parse: `raw/sources/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation/Multi-Cell_Mobile_Edge_Computing_Joint_Service_Migration_and_Resource_Allocation.md`
- Origin PDF and extracted figures are in the same folder.
