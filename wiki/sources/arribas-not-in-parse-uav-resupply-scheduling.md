---
type: source
title: "Optimizing UAV Resupply Scheduling for Heterogeneous and Persistent Aerial Service"
authors: ["Edgar Arribas", "Vicent Cholvi", "Vincenzo Mancuso"]
year: "not in parse"
url: "not in parse"
venue: "not in parse"
modeling_card: required
tags: [source, uav, energy-scheduling, persistent-service, fleet-sizing]
related:
  - "[[battery-swapping-uav-mec]]"
  - "[[continuous-omnidirectional-monitoring]]"
  - "[[wang-2026-robust-multiuav-jtcra]]"
created: 2026-08-27
updated: 2026-08-27
---

# Optimizing UAV Resupply Scheduling for Heterogeneous and Persistent Aerial Service

## Citation

Arribas, E., Cholvi, V., & Mancuso, V. *Optimizing UAV Resupply Scheduling for Heterogeneous and Persistent Aerial Service*. Venue and year are not in the parse.

## TL;DR

Studies how many homogeneous UAVs are needed to keep one vehicle continuously present at every service location while vehicles rotate through an energy-supply station. HORR is exact for equal flight distances, while the unequal-distance problem is NP-hard and PHERR provides a lightweight near-exact schedule.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fleet of identical UAVs persistently serves fixed aerial locations, one UAV per location, and each UAV must periodically leave service, fly to a common energy-supply station, resupply, and return or replace another UAV.

**Problem & objective**: Choose cyclic duty shifts and fleet size $N$ to minimize the number of UAVs, $\min N$, while maintaining uninterrupted coverage at every aerial location.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| Fleet size | $N$ | positive integer | Number of UAVs assigned to persistent service |
| Shift start | $s_i$ | continuous time | Start of a UAV service or replacement shift |
| Location group | $G_k$ | partition | Service locations grouped by similar supply-station distance |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| Coverage | Exactly one UAV continuously serves each required aerial location. |
| Energy | A servicing UAV leaves early enough to complete its return flight before exhausting energy. |
| Cycle | Each duty cycle includes outbound flight, service, return flight, and nonzero resupply time. |
| Homogeneous case | Equal station distances admit the feasible and exact HORR cyclic schedule. |
| Heterogeneous case | Unequal distances make fleet minimization NP-hard; PHERR partitions locations and applies HERR within groups. |

**Algorithm**: Apply HORR directly when all locations have equal flight distance. Otherwise, partition locations to reduce within-group distance heterogeneity, run the buffer-aware HERR rotation in each group, and combine the group schedules as PHERR.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Arribas et al. [x] formulated UAV energy resupply as a fleet-sizing problem for persistent service at fixed aerial locations. They proved that the homogeneous-distance case admits an exact cyclic schedule, called HORR, that uses the minimum possible number of UAVs. They also showed that unequal station distances make the general scheduling problem NP-hard. PHERR partitions locations into more homogeneous groups and applies a buffered rotating schedule within each group. Numerical analysis indicates that PHERR is near exact over the evaluated scenarios, but its guarantee is not the same as HORR's exact homogeneous-case result.

## Problem and system model

Every service location must remain occupied at all times. Flight to and from the energy station and the resupply operation are non-negligible, so spare vehicles and shift timing determine whether coverage can remain continuous.

## Method

The paper derives HORR for equal distances, proves its feasibility and optimal fleet size, establishes NP-hardness for heterogeneous distances, and develops HERR and its partitioned extension PHERR using analytical duty-cycle structure and a fleet-size lower bound.

## Key findings

- HORR is exact for the stated homogeneous-distance setting.
- The heterogeneous-distance problem is NP-hard.
- PHERR is reported to track the derived lower bound closely and outperform prior heuristics across the numerical cases.

## Limitations / future work

The model assumes homogeneous UAV capabilities, one persistently served UAV per fixed aerial location, and a common supply station. The paper does not optimize the application-specific service performed at each location.

## Relation to the corpus

This source supplies the fleet-rotation foundation behind [[battery-swapping-uav-mec]] and complements [[wang-2026-robust-multiuav-jtcra]], which learns communication-aware reconfiguration when energy-limited UAVs stop service.

## Raw artifacts

- Parse: `raw/sources/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service/Optimizing_UAV_Resupply_Scheduling_for_Heterogeneous_and_Persistent_Aerial_Service.md`
- Origin PDF and extracted figures are in the same folder.
