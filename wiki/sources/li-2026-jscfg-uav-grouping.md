---
type: source
title: "Dynamic Grouping of Heterogeneous UAVs under Complex Sequential Tasks: A Joint Switch Coalition Formation Game Approach"
authors: ["Zhongkun Li", "Weiguo Xia", "Shaoqing Zhang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3708388"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
modeling_card: required
tags: [source, heterogeneous-uav, dynamic-grouping, coalition-formation-game, potential-game, topology-optimization, sequential-tasks]
related:
  - "[[joint-switch-coalition-formation-game]]"
  - "[[coalition-formation-game]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[autonomous-uav-swarms]]"
created: 2026-07-13
updated: 2026-07-16
---

# Dynamic Grouping of Heterogeneous UAVs under Complex Sequential Tasks: A Joint Switch Coalition Formation Game Approach

## Citation

Li, Z., Xia, W., & Zhang, S. (2026). *Dynamic Grouping of Heterogeneous UAVs under Complex Sequential Tasks: A Joint Switch Coalition Formation Game Approach*. **IEEE Transactions on Mobile Computing**, 1-15. DOI: 10.1109/TMC.2026.3708388.

## TL;DR

Forms communication groups for heterogeneous UAVs executing ordered mission subtasks. A joint-switch coalition game lets several UAVs move across multiple, potentially overlapping coalitions together so that type requirements remain feasible while total cohesion and predicted link-persistence utility improve.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A heterogeneous swarm of $N$ UAVs from $Z$ functional types follows preplanned paths while executing ordered mission subtasks. UAVs form communication groups, with overlapping membership permitted when a UAV type is scarce, and group utility combines cohesion, predicted link persistence, group size, and cross-group penalties.

**Problem & objective**: The combinatorial grouping problem in Eq. (13) selects joint switch commands to solve $\max_{\tau}GP(\boldsymbol\Theta)$, where $GP(\boldsymbol\Theta)=\sum_{k=1}^{N_1}GP(\Phi_k)$ is the total utility of coalition structure $\boldsymbol\Theta$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Coalition structure | $\boldsymbol\Theta=\{\Phi_1,\ldots,\Phi_{N_1}\}$ | discrete set partition or overlapping grouping | Communication groups formed by the swarm |
| Joint switch command | $\tau$ | discrete feasible switch operation | Coordinated movement of one or more UAV memberships among groups |
| UAV grouping decision | $\mathcal M$ | discrete decision vector | Group membership decision for each UAV player |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 13a | The grouping accounts for the full swarm: $\sum_{k=1}^{N_1}N_{\Phi_k}=N$ in the non-overlapping case |
| 13b | Every group meets each subtask-type requirement: $N_{\Phi_{k,z}}\geq n_z$ |
| Feasibility | Candidate joint switches preserve the basic task requirements of all affected groups |
| Trigger | Reconfiguration follows the utility-threshold or elapsed-time trigger before a new switch search begins |

**Algorithm**: Run BCSFA to classify each subtask layer as insufficient, balanced, or abundant and greedily construct a feasible basic coalition structure. Then run JSCFA layer by layer, enumerate feasible joint switches, discard operations that violate the joint-switch coalition-improvement order, execute the operation with maximum utility gain, and stop when the feasible switch set is empty, yielding a Nash-stable structure after finitely many switches.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied dynamic communication grouping for heterogeneous UAV swarms executing ordered subtasks with minimum requirements for each UAV type. They formulated a coalition-structure utility maximization problem whose joint switch decisions must allocate the swarm and preserve the per-group type requirements. Their BCSFA first constructs a feasible initial grouping by sequential greedy selection, after which JSCFA repeatedly executes the feasible joint switch with the largest utility gain until a Nash-stable structure is reached. Simulations under insufficient, balanced, and abundant UAV resources reported feasible group formation, finite convergence, and higher coalition utility after the joint-switch process.

## Problem

Search-lock-attack and similar missions require ordered subtasks and minimum numbers of different UAV types. Single-UAV coalition switches can violate those requirements, while static groups retain weak links as predetermined trajectories evolve. The paper optimizes communication topology without replanning the flight paths.

## System model

- `N` UAVs belong to `Z` functional types and follow preplanned, approximately same-altitude paths.
- A mission is decomposed into ordered subtasks. The illustrative requirement is one search UAV, two lock UAVs, and one attack UAV per group.
- The number of groups follows the number assigned to the initial subtask. Abundant, balanced, and insufficient-resource cases are distinguished; insufficient resources permit UAV membership in multiple groups.
- Same-subtask and adjacent-subtask UAVs communicate inside a group, while leaders exchange global information. TDMA is used within groups and FDMA across groups.

## Method

The [[joint-switch-coalition-formation-game]] allows coordinated sets of players to move across several coalitions when a single-player move cannot preserve type constraints. Its joint-switch common-improvement preference accounts for switching nodes, overlapping nodes, and other coalition members affected by the move.

A basic coalition-structure formation algorithm classifies each subtask layer by resource sufficiency and greedily builds a feasible initial coalition structure, potentially with overlapping coalitions when resources are insufficient. The joint-switch algorithm then evaluates feasible switch sets, applies the largest positive utility gain, and stops when no improving move remains. The authors characterize abundant-case single-node switching as an exact [[potential-game]] and argue finite improvement reaches a [[nash-equilibrium|Nash-stable]] structure in the other cases.

## Key findings

- Simulations use a `50 km x 50 km` area, three ordered subtasks, the type requirement `{1 U1, 2 U2, 1 U3}`, and UAV speeds from `80-100 km/h`.
- Illustrated insufficient, balanced, and abundant fleets are `{4,7,3}`, `{4,8,4}`, and `{4,10,4}` across the three types.
- In the fixed five-group comparison, `N=20` is the balanced point. The paper reports higher average total utility than the compared coalition algorithms when the fleet is below or above that point, but the parse contains no reliable exact utility margins.
- The balanced case requires more iterations than the insufficient and abundant examples; exact iteration counts are figure-only and are not promoted here.

## Limitations / parse caveats

Evidence is simulation-only. Flight paths are fixed, leader-broadcast communication overhead is treated as negligible, and passive topology switching is assumed to consume negligible energy. Future resource allocation and trajectory optimization are outside the model. The parse has a damaged central preference equation, inconsistent statements about whether all pairwise distances stay within range, and tension between a size-sum constraint and overlapping membership. One result paragraph says USVs where the paper otherwise studies UAVs. Publication metadata is absent and the journal header is a template placeholder; the 2026 TMC record was verified through the exact-title Crossref entry.

## Relation to the corpus

This paper extends [[coalition-formation-game]] from single-member merge/split behavior to coordinated switches that preserve heterogeneous mission requirements. Unlike [[sequential-task-offloading]], its sequential tasks are physical mission stages rather than dependent computation jobs. It gives [[heterogeneous-uav-fleet]] and [[autonomous-uav-swarms]] a topology-formation use case with predefined mobility.

## Raw artifacts

- Parse: `raw/sources/Dynamic_Grouping_of_Heterogeneous_UAVs_under_Complex_Sequential_Tasks_A_Joint_Switch_Coalition_Formation_Game_Approach/Dynamic_Grouping_of_Heterogeneous_UAVs_under_Complex_Sequential_Tasks_A_Joint_Switch_Coalition_Formation_Game_Approach.md`
- Origin PDF: `raw/sources/Dynamic_Grouping_of_Heterogeneous_UAVs_under_Complex_Sequential_Tasks_A_Joint_Switch_Coalition_Formation_Game_Approach/Dynamic_Grouping_of_Heterogeneous_UAVs_under_Complex_Sequential_Tasks_A_Joint_Switch_Coalition_Formation_Game_Approach.pdf`
- Figures: `raw/sources/Dynamic_Grouping_of_Heterogeneous_UAVs_under_Complex_Sequential_Tasks_A_Joint_Switch_Coalition_Formation_Game_Approach/images/`
