---
type: source
modeling_card: required
title: "USV Fleet-Assisted Collaborative Computation Offloading for Smart Maritime Services: An Energy-Efficient Design"
authors: ["Hui Zeng", "Zhou Su", "Qichao Xu", "Ruidong Li", "Yuntao Wang", "Minghui Dai", "Tom H. Luan", "Xin Sun", "Donglan Liu"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3359310"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, maritime-mec, collaborative-offloading, reverse-auction, admm, energy-efficiency, usv-fleet, incentive-mechanism]
related:
  - "[[maritime-mec]]"
  - "[[task-offloading]]"
  - "[[reverse-auction-incentive]]"
  - "[[alternating-direction-method-of-multipliers]]"
  - "[[two-stage-decomposition]]"
  - "[[energy-latency-tradeoff]]"
  - "[[nash-equilibrium]]"
  - "[[zhou-su]]"
  - "[[dai-2024-multiuav-marine-welfare]]"
  - "[[dai-2023-hybrid-marine-mmwl]]"
  - "[[wang-2024-twotier-satellite-marine]]"
created: 2026-05-31
updated: 2026-07-16
---

# USV Fleet-Assisted Collaborative Computation Offloading for Smart Maritime Services: An Energy-Efficient Design

## Citation

Zeng, H., Su, Z., Xu, Q., Li, R., Wang, Y., Dai, M., Luan, T. H., Sun, X., & Liu, D. (2024). *USV Fleet-Assisted Collaborative Computation Offloading for Smart Maritime Services: An Energy-Efficient Design*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3359310. (Date of publication 27 February 2024; date of current version 17 October 2024. Corresponding author: Zhou Su. An earlier version appeared at IWCMC 2022, DOI 10.1109/IWCMC55113.2022.9825034.)

## TL;DR

AI-empowered UAVs doing marine monitoring generate computation-intensive tasks they cannot run locally. This paper offloads those tasks to **unmanned surface vehicle (USV) fleets** — clusters of USVs that pool computation resources. A **first-price sealed reverse auction with a reserve price** incentivizes USV fleets to participate (the reserve price = the UAV's valuation, guaranteeing the UAV's benefit), and the **symmetric equilibrium bidding strategy** is derived. Then, within the winning fleet, the leader splits the task into subtasks and an energy-minimization problem (subject to a delay constraint) is solved by **Block Coordinate Descent (BCD)** + an improved **Alternating Direction Method of Multipliers (ADMM)** with dynamic penalty coefficients.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Marine-monitoring UAVs auction computation tasks to mobile USV fleets whose leaders split accepted tasks across connected members. UAV-to-USV and intra-fleet links plus member compute capacity determine delay and transmission or execution energy.

**Problem & objective**: A two-stage mechanism first selects a fleet by reverse auction, then minimizes winning-fleet energy, $\min E_{\mathrm{tx}}+E_{\mathrm{comp}}$, under task-completion delay.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Fleet bid | $b_i$ | continuous, nonnegative | Price submitted by USV fleet $i$ |
| Winning fleet | $x_i$ | binary | Fleet selected below the reserve price |
| Subtask allocation | $d_j$ | continuous, nonnegative | Workload assigned to member USV $j$ |
| Compute allocation | $f_j$ | continuous, bounded | CPU capacity used by member $j$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | The lowest admissible bid below the reserve price wins |
| C2 | Subtasks sum to the original UAV workload |
| C3 | Member CPU allocations stay within available capacity |
| C4 | Communication plus execution finishes within the delay threshold |
| C5 | Intra-fleet forwarding follows available multi-hop connectivity |

**Algorithm**: Compute UAV reserve price and fleet valuations → derive or submit symmetric-equilibrium first-price reverse bids → choose the lowest valid fleet → alternate leader subtask allocation and member CPU allocation by BCD → solve each distributed block with dynamic-penalty ADMM → stop when fleet energy converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zeng et al. [x] studied energy-efficient collaborative computation offloading from marine-monitoring UAVs to unmanned surface vehicle fleets. A first-price sealed reverse auction with a UAV reserve price selects a participating fleet, and the paper derives a symmetric equilibrium bidding strategy. Inside the winning fleet, the leader allocates subtasks and members allocate computing capacity to minimize transmission and execution energy under a delay constraint. Block coordinate descent separates the two allocation blocks, and dynamic-penalty ADMM solves them distributively. Simulations report higher participation and lower fleet energy than the evaluated bidding and single-priority allocation baselines.

## Problem framing

UAVs hovering over maritime accident sites (ship collision, oil spill, search & rescue) produce heavy tasks (image recognition, video processing, path planning) but have limited battery and compute. USV fleets can supply abundant, shared computation, but three challenges block naive offloading: (1) UAVs cannot pick the optimal fleet because fleets withhold capability/connectivity info for privacy/security; (2) executing tasks costs fleets significant storage/compute, so without incentives they won't participate; (3) intra-fleet collaborative execution (local + transmission energy) consumes a lot of energy, limiting fleet endurance. The paper argues prior matching-game / cooperative-offloading work doesn't transfer to this maritime setting (no shared private info; fleet member-count/connectivity ignored).

## System model

- **Three components.** UAVs (task requesters), USV fleets (helpers; a leader splits tasks into subtasks for members), and **maritime cloud servers** (trusted; authenticate identities, store transaction records via satellite links).
- **Mobility.** 3-D Cartesian; cruise time split into equal slots. UAVs fly at fixed altitude $H_0$ with 2-D velocity; USV fleets move on the surface ($z=0$).
- **Communication.** UAV-to-USV (LoS, with inter-UAV interference, Shannon rate) and USV-to-USV (intra-fleet subtask forwarding). Path-loss-exponent models with a fixed antenna gain factor.
- **Valuations.** UAV valuation combines a **delay-threshold** term (more urgent → higher) and a **transmission-rate** term; USV-fleet valuation combines **storage space** (∝ task data size) and **computation resource** (member computation capacity weighted by hop connectivity).

## Method

- **Incentive — first-price sealed reverse auction with reserve price.** The lowest bidder below the reserve price wins and earns revenue. Theorem 1 derives the **symmetric equilibrium bidding strategy** $\beta(x_i) = E[\min(X^*_{-i}, \hat{S}) \mid X^*_{-i} > x_i]$, with existence (first-order condition on expected revenue) and uniqueness (proof by contradiction) established ([[nash-equilibrium]]).
- **Energy minimization.** Minimize the USV fleet's overall energy (transmission + local execution) for collaborative subtask execution under a delay constraint. The leader decides **subtask allocation**; members decide **computation-capacity allocation**. Because the two decisions are strongly coupled, the joint problem is decomposed by **BCD** into two subproblems (P2, P3), each solved by **ADMM** improved with dynamic penalty coefficients to cut complexity and ensure convergence ([[alternating-direction-method-of-multipliers]], [[two-stage-decomposition]]).
- **Complexity.** ADMM subproblems are $\mathcal{O}(QJT_q/\varepsilon^2)$; overall BCD+ADMM complexity $\mathcal{O}((1/\varepsilon_3) QJT_q (1/\varepsilon_1^2 + 1/\varepsilon_2^2))$.

## Key findings

Simulation: MATLAB; 10 UAVs and 20 USV fleets randomly deployed in a 40 km × 40 km area via Monte Carlo, fleet member count drawn from 5–25. Benchmarks: Random Bidding (RBS), Greedy Bidding (GBS) for the auction; Computation Capacity Priority (CCPS) and Hop Count Priority (HCPS) for the allocation.

- **Symmetric equilibrium bidding decreases as the number of USV fleets grows** (more competition → fleets lower bids to raise winning probability), approaching their valuation as the fleet count increases (Fig. 3).
- **Participation degree** of the proposed scheme improves on average by **28.27% over RBS and 25.74% over GBS** across different task data sizes (Fig. 5a), and by **27.84% over RBS and 21.14% over GBS** across different numbers of USV fleets (Fig. 5b) (verbatim percentages from the parse).
- The optimization scheme **converges** (overall energy stabilizes by ~1500 iterations, sharpest drop in the first ~800) (Fig. 6).
- Overall energy consumption rises with the number of tasks, and the proposed joint scheme yields **lower energy than CCPS and HCPS** (which optimize only one of subtask or capacity allocation); fleets with stronger connectivity (fewer hops) incur lower transmission energy (Fig. 7).

## Limitations / future work

Simulation-only (MATLAB). The authors defer joint allocation of caching, communication, and computation capacities for UAVs and USV fleets to future work. Numeric values beyond the stated participation-degree percentages are read from MinerU-parsed figures/tables and are indicative. The model assumes UAVs, USV fleets, and maritime cloud servers are all trusted.

## Relation to the corpus

A **maritime MEC** entry distinctive for combining a **reverse-auction incentive** with an **ADMM/BCD energy-minimization** core, and for the **USV-fleet-as-helper** architecture (UAVs offload *to* USV fleets, rather than USVs offloading). It sits beside the University-of-Macau marine multi-access line — [[dai-2024-multiuav-marine-welfare]] (which uses a double-auction for OBS selection) and [[dai-2023-hybrid-marine-mmwl]] — sharing co-authors **Minghui Dai** ([[minghui-dai]]) and [[zhou-su|Zhou Su]], and the two-tier marine game work [[wang-2024-twotier-satellite-marine]]. Reinforces [[maritime-mec]], [[task-offloading]], and the [[two-stage-decomposition]]/[[alternating-direction-method-of-multipliers]] solver thread.

## Raw artifacts

- `raw/sources/USV_Fleet-Assisted_Collaborative_Computation_Offloading_for_Smart_Maritime_Services_An_Energy-Efficient_Design/full.md`
- Original PDF (`3dff6c8e-38ab-46fe-9bc5-a9865789b6f2_origin.pdf`) and extracted figures (`images/`) in the same folder.
