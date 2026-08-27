---
type: source
title: "Time-Constrained Service Handoff for Mobile Edge Computing in 5G"
authors: ["Nafiseh Sharghivand", "Lena Mashayekhy", "Weibin Ma", "Schahram Dustdar"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: required
tags: [source, mobile-edge-computing, service-handoff, mechanism-design, path-planning, pricing]
related:
  - "[[service-migration]]"
  - "[[matching-theory-for-resource-allocation]]"
created: 2026-08-27
updated: 2026-08-27
---

# Time-Constrained Service Handoff for Mobile Edge Computing in 5G

## Citation

Sharghivand, N., Mashayekhy, L., Ma, W., & Dustdar, S. *Time-Constrained Service Handoff for Mobile Edge Computing in 5G*. Venue and year are not in the parse.

## TL;DR

OSHM assigns an online, congestion-aware path for transferring a VM or container between cloudlets as a user moves. A label-correction planner is paired with a payment function that discourages users from misreporting private parameters; the paper proves truthfulness and weak budget balance.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Mobile users move between 5G MEC cloudlets. A service handoff follows a path of base-station links with queueing and transmission contention.

**Problem & objective**: Choose a feasible handoff path $p$ to minimize system workload and handoff time under a user deadline $\theta_m$, while computing a truthful charge.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Handoff path | $p_m$ | discrete path | BS-link sequence used for user $m$'s service transfer |
| Path allocation | $x_{m,p}$ | binary | Whether path $p$ serves handoff $m$ |
| Payment | $\pi_m$ | nonnegative | Charge determined from reported and system values |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Deadline | Selected handoff duration does not exceed $\theta_m$. |
| Capacity | Link bandwidth and BS queue capacity bound concurrent transfers. |
| Path | Paths are feasible, adjacent, and cycle-free. |
| Incentive | Payment preserves truthfulness and weak budget balance. |

**Algorithm**: Run label-correction path planning with workload and time valuations, then compute the payment from the mechanism's critical-value formulation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Sharghivand et al. [x] proposed OSHM for online VM or container handoff between 5G MEC cloudlets. Their label-correction path planner accounts for transfer time, queueing, workload, and user deadlines, while a payment function discourages strategic misreporting. The authors establish system equilibrium, truthfulness, and weak budget balance for the mechanism. Experiments report at least 61% lower average workload, 33% lower handoff time, and 29% lower energy consumption than the compared schemes. The method plans handoff paths and payments rather than choosing application placement or migration internals.

## Problem and system model

Each user handoff traverses a BS graph with finite radio resources and M/M/C-style queues. Transfer time depends on service size, path capacity, queueing, and the time valuation reported by the user and edge manager.

## Method

OSHM searches feasible paths online with label correction and computes charges after selecting a path. The mechanism's proof covers truthful reporting and budget balance under its modeled valuations.

## Key findings

- OSHM keeps reported handoff durations within user deadlines in the evaluated cases.
- The proposed paths balance congestion and service duration across competing handoffs.
- Reported reductions are at least 61% workload, 33% handoff time, and 29% energy.

## Limitations / future work

Future work includes multi-service paths for dependent applications and trajectory prediction when user routes are unavailable.

## Relation to the corpus

This source adds an incentive-aware path-planning layer to [[service-migration]] and complements migration-handover optimization in multi-cell MEC.

## Raw artifacts

- Parse: `raw/sources/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G/Time-Constrained_Service_Handoff_for_Mobile_Edge_Computing_in_5G.md`
- Origin PDF and figures are in the same folder.
