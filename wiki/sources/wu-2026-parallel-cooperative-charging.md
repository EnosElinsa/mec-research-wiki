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
updated: 2026-11-03
---

# Cost-Effective Parallel Cooperative Charging Scheduling for UAVs

## Citation

Wu, S., Yang, Y., Dai, H., Liu, L., Xiao, F., & Xu, J. (2026). *Cost-Effective Parallel Cooperative Charging Scheduling for UAVs*. **IEEE Transactions on Mobile Computing**, 25(7), 11101-11115. DOI: 10.1109/TMC.2026.3664259.

## TL;DR

Assigns UAVs to RF charging stations and parallel charging facilities while exploiting a shared station-time tariff. CSAU combines a uniform-parallel-machine approximation with greedy set covering, giving a `gamma(ln n + 1)` approximation and substantially lower simulated charging-system cost than the three tested heuristic baselines.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Charging stations $M=\{s_1,\dots,s_m\}$, run by different providers, each have $q_j$ RF charging facilities with unequal powers $p_j^k$. Each UAV $o_i \in N$ with energy demand $E_i$ and residual energy $E_i^{re}$ detours to one station and then flies to its target $l_i$, so it must be replenished with $E_i(s_j)=E_i+b_i\big(d(o_i,s_j)+d(s_j,l_i)\big)$. The UAVs charged at a station form its charging group $G_j$, and charging starts when the last group member arrives.

**Problem & objective**: PCCSUP (6): $\min \sum_{s_j\in M} c(\phi_j)$, where the base-fare tariff is $c(\phi_j)=A_j$ if $T(\phi_j)\le T_j$ and $A_j+a_j\big(T(\phi_j)-T_j\big)$ otherwise, and $T(\phi_j)=\max_k T(\pi_j^k)$ with $T(\pi_j^k)=\sum_{o_i\in\pi_j^k}E_i(s_j)/p_j^k$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Facility assignment | $x_{ij}^k$ | binary | UAV $o_i$ is charged by facility $f_j^k$ of station $s_j$ |
| Charging arrangement | $\phi_j=\{\pi_j^1,\dots,\pi_j^{q_j}\}$ | partition of $G_j$ | Which group members each facility of $s_j$ charges |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (6-1) | Each UAV is assigned to exactly one charging facility, $\sum_{s_j}\sum_k x_{ij}^k = 1$. |
| (6-2) | $x_{ij}^k \in \{0,1\}$. |
| (7) | Residual energy reaches any station, $E_i^{re} \ge \max_{s_j} b_i d(o_i,s_j)$. |
| (10) | Demand fits the battery after the detour to the target, $E_i \le E_i^{MAX}-E_i^{re}-\max_{s_j} b_i d(s_j,l_i)$. |
| (5) | Tariff parameters satisfy $A_j \ge a_j T_j$. |

**Algorithm**: CSAU repeatedly calls AMCAM to build, for each station, the charging group and arrangement with approximately minimum average marginal cost, using a $\gamma$-approximation for uniform parallel-machine scheduling to arrange each group. It then picks groups in a greedy set-cover manner until every UAV is covered, which gives a $\gamma(\ln n + 1)$ approximation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wu et al. [x] studied cost-effective parallel cooperative charging scheduling for UAVs across multiple providers and unequal-power facilities. They formulated an NP-hard problem that jointly assigns UAVs to stations and charging facilities to minimize the total base-fare charging payment, which depends on each station's longest facility charging time. CSAU uses AMCAM to construct station groups, invokes a gamma-approximation for uniform parallel-machine scheduling, and selects groups through a greedy set-cover procedure. The method has a $\gamma(\ln n+1)$ approximation bound for the base problem. Simulations report lower total cost than the evaluated IAASA, ICSA, and IAASAU heuristics, and a small-instance comparison reports its gap to exhaustive optimum.

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
