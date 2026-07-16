---
type: source
modeling_card: required
title: "Cost-Effective Parallel Cooperative Charging Scheduling for UAVs"
authors: ["Sixu Wu", "Yun Yang", "Haipeng Dai", "Linfeng Liu", "Fu Xiao", "Jia Xu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3664259"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav, wireless-charging, scheduling, approximation-algorithm, set-cover]
related:
  - "[[parallel-cooperative-uav-charging]]"
  - "[[uav-charging-scheduling]]"
  - "[[wireless-power-transfer]]"
  - "[[generalized-assignment-problem]]"
  - "[[trajectory-privacy]]"
created: 2026-07-12
updated: 2026-07-16
---

# Cost-Effective Parallel Cooperative Charging Scheduling for UAVs

## Citation

Wu, S., Yang, Y., Dai, H., Liu, L., Xiao, F., & Xu, J. (2026). *Cost-Effective Parallel Cooperative Charging Scheduling for UAVs*. **IEEE Transactions on Mobile Computing**, 25(7), 11101-11115. DOI: 10.1109/TMC.2026.3664259.

## TL;DR

Assigns UAVs to RF charging stations and parallel charging facilities while exploiting a shared station-time tariff. CSAU combines a uniform-parallel-machine approximation with greedy set covering, giving a `gamma(ln n + 1)` approximation and substantially lower simulated charging-system cost than the three tested heuristic baselines.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Several providers operate charging stations with unequal-power parallel RF facilities. Each UAV must detour from its initial position to a selected station and then reach its target, and all UAVs assigned to a station share a tariff determined by the slowest facility completion time.

**Problem & objective**: PCCSUP is an NP-hard assignment and parallel-machine scheduling problem that minimizes total station payment, $\min \sum_s C_s(T_s)$, over station, facility, group, and queue decisions.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Station assignment | $x_{i,s}$ | binary | Whether UAV $i$ charges at station $s$ |
| Facility assignment | $y_{i,s,j}$ | binary | Parallel facility $j$ used by UAV $i$ |
| Queue order | $\pi_{s,j}$ | discrete permutation | Charging order on facility $j$ at station $s$ |
| Station completion time | $T_s$ | continuous, nonnegative | Maximum completion time across station facilities |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every retained UAV is assigned to exactly one station and facility |
| C2 | A UAV has enough residual energy to reach its candidate station and target |
| C3 | Facility power and station capacity can replenish each assigned demand |
| C4 | Parallel queues induce $T_s$ as the station's maximum completion time |
| C5 | Station tariff follows its base-fare threshold and marginal time cost |

**Algorithm**: Preprocess feasible UAV-station candidates → for each station grow a candidate charging group by low replenishment energy → schedule the group with a $\gamma$-approximation for uniform parallel machines → compute average marginal group cost → choose extensions through greedy set cover → repeat until all retained UAVs are assigned.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] studied cost-effective parallel cooperative charging scheduling for UAVs across multiple providers and unequal-power facilities. They formulated an NP-hard problem that jointly assigns UAVs to stations and facilities and orders charging queues to minimize shared station-time payments. CSAU uses AMCAM to construct station groups, invokes a gamma-approximation for uniform parallel-machine scheduling, and selects groups through a greedy set-cover procedure. The method has a $\gamma(\ln n+1)$ approximation bound for the base problem. Simulations report lower total cost than the evaluated IAASA, ICSA, and IAASAU heuristics, and a small-instance comparison reports its gap to exhaustive optimum.

## Problem

Multiple charging providers operate stations with several unequal-power RF facilities. A UAV's replenishment requirement includes its charging demand and the movement energy needed to detour from its initial location through a station to its target. UAVs assigned to one station share a group charge determined by the time until the slowest parallel facility finishes, so station selection, grouping, and queue arrangement cannot be optimized independently.

## System model

- Binary variables assign each UAV to exactly one facility at one station; each facility receives an ordered queue.
- Group charging time is the maximum completion time across a station's parallel facilities.
- The tariff is a base fare up to a station-specific threshold and then grows linearly with additional operating time.
- PCCSUP minimizes total payment across stations. The problem is NP-hard through its single-station, zero-base-fare reduction to uniform parallel-machine scheduling.
- The feasibility preprocessing conservatively requires every UAV to have enough residual energy to reach every candidate station; UAVs failing that all-stations condition or the demand/capacity condition are removed.

## Method

The Charging Scheduling Algorithm for UAVs (CSAU) repeatedly evaluates candidate station/group extensions. For each station, AMCAM adds low-replenishment-energy UAVs, invokes a `gamma`-approximation for the Uniform Parallel Machines Scheduling Problem to arrange them over facilities, and returns the extension with minimum average marginal cost. A greedy set-cover outer loop chooses among those extensions. The paper derives a `gamma(ln n + 1)` approximation and `O(m n^2 Gamma)` runtime, where `Gamma` is the embedded machine-scheduling routine's complexity.

Section VI extends the framework to release times, minimum-size `K`-anonymous groups, and vehicle transport for UAVs unable to reach a station. The release-time version is heuristic, and the vehicle-assisted objective loses the base problem's approximation guarantee.

## Key findings

- For 10-60 UAVs, CSAU reduces average total cost by `58.17%` versus IAASA, `55.74%` versus ICSA, and `22.16%` versus IAASAU.
- Across the movement-energy sweep, reductions reach `59.81%`, `56.60%`, and `31.07%` against the same three baselines; this is the scope of the abstract's "up to 59.81%" result.
- In a 9-UAV exhaustive comparison, CSAU is `23.98%` above OPT, compared with `25.72%` for IAASAU and more than `72%` for the two weaker baselines. OPT takes `44.06 s` for that instance.

## Limitations / parse caveats

Stations, facility powers, prices, and UAV demands are fixed; within-station movement is ignored; travel time is initially treated as small relative to hours-long charging. Feasibility preprocessing excludes some UAVs rather than serving every input. The `K`-anonymity extension reduces privacy to group size, and the release-time/vehicle variants weaken optimality guarantees. Several table cells and algorithm superscripts are OCR-damaged, so this page uses only narrative-supported percentages. Publication metadata is absent from the parse and was verified through the exact-title Crossref record.

## Relation to the corpus

[[parallel-cooperative-uav-charging]] extends [[uav-charging-scheduling]] from deciding when or where an operating UAV recharges to jointly choosing provider, shared-cost group, and parallel facility queue. Its set-cover grouping resembles assignment optimization, but the group-level station tariff makes it richer than a standard [[generalized-assignment-problem]].

## Raw artifacts

- Parse: `raw/sources/Cost-Effective_Parallel_Cooperative_Charging_Scheduling_for_UAVs/Cost-Effective_Parallel_Cooperative_Charging_Scheduling_for_UAVs.md`
- Origin PDF: `raw/sources/Cost-Effective_Parallel_Cooperative_Charging_Scheduling_for_UAVs/Cost-Effective_Parallel_Cooperative_Charging_Scheduling_for_UAVs.pdf`
- Figures: `raw/sources/Cost-Effective_Parallel_Cooperative_Charging_Scheduling_for_UAVs/images/`
