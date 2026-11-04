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
updated: 2026-11-03
---

# Time-Constrained Service Handoff for Mobile Edge Computing in 5G

## Citation

Sharghivand, N., Mashayekhy, L., Ma, W., & Dustdar, S. *Time-Constrained Service Handoff for Mobile Edge Computing in 5G*. Venue and year are not in the parse.

## TL;DR

OSHM assigns an online, congestion-aware path for transferring a VM or container between cloudlets as a user moves. A label-correction planner is paired with a payment function that discourages users from misreporting private parameters; the paper proves truthfulness and weak budget balance.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Mobile users move between 5G MEC cloudlets, and a user's VM or container is handed off from origin cloudlet $o$ to destination $d$ over a path of base-station (BS) links. Each new handoff adds queueing time at BSs used by existing handoffs and consumes part of each BS's remaining energy budget.

**Problem & objective**: SHIP$^3$ in (10), a constrained shortest-path problem, picks the handoff path $p$ that maximizes sequential social surplus $v_e+v_m$ (valuations of the edge manager for existing users and of user $m$). It is rewritten as the workload-and-time minimization (11)–(12) and as the link-based model SHIP$^3$-L (13).

**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Handoff path | $p\in\mathcal P$ | discrete path | BS-link sequence for user $m$'s handoff |
| Link selection | $x_l$ | binary | Link $l$ is on the path (SHIP$^3$-L) |
| Payment | $\pi_m$ | nonnegative | Charge set by the mechanism for truthfulness |

**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (10a) | Handoff time within the user's deadline: $\tau_m\le\theta_m$ |
| (10b) | BS energy budget: $e_j^{ml}\le\bar\epsilon_j$ on every node and link of the path |
| (13a)–(13c) | Flow conservation: one link leaves $o$, one enters $d$, balance at intermediate nodes |
| (13d) | Link-based deadline: $\sum x_l(\tau_m^l+\tau_{j^+}^q)\le\theta_m$ |
| (13e) | Link-based energy budget given energy already used by existing handoffs |
| (13f) | $x_l\in\{0,1\}$ |

**Algorithm**: OSHM runs label-correction path planning online on the workload-and-time objective under the deadline and energy constraints, then charges users with a payment function; the paper proves system equilibrium, truthfulness, and weak budget balance.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Sharghivand et al. [x] proposed OSHM for online VM or container handoff between 5G MEC cloudlets. Their label-correction path planner accounts for transfer time, queueing, workload, user deadlines, and base-station energy budgets, while a payment function discourages strategic misreporting. The authors establish system equilibrium, truthfulness, and weak budget balance for the mechanism. Experiments report at least 61% lower average workload, 33% lower handoff time, and 29% lower energy consumption than the compared schemes. The method plans handoff paths and payments rather than choosing application placement or migration internals.

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
