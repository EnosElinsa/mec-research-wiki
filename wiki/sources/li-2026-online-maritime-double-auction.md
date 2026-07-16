---
type: source
title: "An Online Double Auction Mechanism for Dynamic Resource Allocation in Maritime Networks"
authors: ["Xianglong Li", "Kaiwei Mo", "Guang Fang", "Zongpeng Li"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3657174"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
modeling_card: required
tags: [source, maritime-network, double-auction, online-algorithm, resource-allocation, uav-communications, social-welfare]
related: ["[[maritime-mec]]", "[[online-maritime-double-auction]]", "[[li-2020-maritime-uav-satellite-coverage]]", "[[dai-2024-multiuav-marine-welfare]]", "[[zeng-2024-usv-fleet-collaborative-offloading]]"]
created: 2026-07-11
updated: 2026-07-16
---

# An Online Double Auction Mechanism for Dynamic Resource Allocation in Maritime Networks

## Citation

Li, X., Mo, K., Fang, G., & Li, Z. (2026). *An Online Double Auction Mechanism for Dynamic Resource Allocation in Maritime Networks*. **IEEE Transactions on Intelligent Transportation Systems**, 27(5), 5441-5453. DOI: 10.1109/TITS.2026.3657174. The parse lacks top-level publication metadata; venue, year, pages, and DOI were verified from a title-matched Crossref record.

## TL;DR

Designs an [[online-maritime-double-auction|online maritime double auction mechanism]] for dynamic Internet-access allocation in maritime networks. Ships bid for bandwidth, ISPs sell capacity through terrestrial antennas or UAVs, and the online mechanism chooses feasible allocations under bid deadlines, coverage, capacity, UAV mobility, and weather-linked link constraints. The paper maximizes social welfare with a compact ILP/dual formulation and an online primal-dual marginal-pricing algorithm.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Ships submit online bids for slotted Internet access, while multiple ISPs sell heterogeneous capacity through fixed terrestrial antennas and mobile UAVs. Feasibility depends on bid timing, bandwidth, device coverage and capacity, ship and UAV positions, UAV travel time and endurance, and weather-dependent device availability.

**Problem & objective**: The primal 0-1 ILP maximizes maritime social welfare $\sum_{n,i}b_{ni}x_{ni}-\sum_{n,i,m,j,t}s_{nim}(t)z_{nimj}(t)$ by accepting ship bids and scheduling ISP devices over time.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Bid acceptance | $x_{ni}$ | binary, $x_{ni}\in\{0,1\}$ | Whether ship $n$'s bid $i$ is accepted |
| Device allocation | $z_{nimj}(t)$ | binary, $z_{nimj}(t)\in\{0,1\}$ | Whether ISP $m$'s device $j$ serves the bid in slot $t$ |
| Feasible schedule | $\zeta_{ni}$ | discrete slot-device set | Selected continuous time slots and ISP devices for a bid |
| Marginal price | $p_m(t)$ | continuous nonnegative value | Dynamic bandwidth price for ISP $m$ in slot $t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 2a-2b | Allocated slots respect bid and device deadlines, and a UAV has enough travel time to reach the ship |
| 2c | Service occurs only within the device communication range: $g_{nmj}(t)z_{nimj}(t)\leq G_{mj}$ |
| 2d | Allocated bandwidth does not exceed device capacity $c_{mj}(t)$ |
| 2e-2f | Accepted bids receive the required number of slots and allocation indicators remain consistent with acceptance |
| 2g-2h | Each ship has at most one accepted bid and all acceptance and allocation variables are binary |

**Algorithm**: Reformulate the NP-hard primal ILP as a compact packing ILP, derive its dual LP, and interpret dual variables as marginal resource prices. For every arriving ship, $A_{\mathrm{online}}$ calls $A_{\mathrm{core}}$ to find a minimum-cost feasible schedule, select the bid with maximum nonnegative net utility, accept and allocate it when profitable, charge the buyer and reward the ISP, and update utilization and exponential marginal prices online.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied online Internet-access allocation in maritime networks where ships buy bandwidth from ISPs operating terrestrial antennas and UAVs. They formulated social-welfare maximization as a 0-1 ILP over bid acceptance and device scheduling under deadline, travel-time, coverage, capacity, duration, and binary-allocation constraints. Their OMDAM mechanism derives a compact packing formulation and dual prices, then uses the online algorithm $A_{\mathrm{online}}$ and its allocation routine $A_{\mathrm{core}}$ to accept bids, assign feasible schedules, and update marginal prices. Simulations reported up to 17% higher social welfare than prior methods and consistently stronger welfare and bandwidth utilization under the tested user, bid, ISP, and asking-price settings.

## Problem

Open-sea communication demand is dynamic: ships move, bids arrive over time, UAV-based ISP capacity is mobile and coverage-limited, and terrestrial antennas have wider but fixed service regions. Static terrestrial double-auction models do not capture maritime coverage radii, UAV availability, ship mobility, or weather-dependent capacity. The paper frames the allocation as social-welfare maximization and states NP-hardness by reduction from knapsack.

## System model

- Buyers are ships requesting Internet access over time slots, with bandwidth demand, bid value, arrival/deadline information, and route-dependent coverage.
- Sellers are ISPs that provide capacity through fixed antennas or UAVs. Antennas have larger coverage radius and higher capacity; UAV ISPs have smaller coverage radius and mobile availability.
- Feasibility combines bid deadlines, ISP/device capacity, communication coverage radius, UAV position/mobility, and weather-linked link state.
- The objective is total accepted ship value minus ISP service cost.

## Method

The Online Maritime Double Auction Mechanism (OMDAM) uses an `A_online` routine over arriving bids and an `A_core` allocation/pricing routine. The paper reformulates the 0-1 ILP into a compact exponential form, derives a dual LP, and uses marginal-pricing/primal-dual updates to decide whether a ship bid should be accepted. It proves individual rationality and weak budget balance for the proposed payment rule, while explicitly noting that stronger dominant-strategy incentive compatibility is not guaranteed.

## Key findings

- The simulation setting uses a 3000 km sailing range, 30 minute slots, bid lengths of 5-20 slots, bid unit prices in [10, 50], ask prices in [10, 30], three UAV ISPs with three UAVs each at capacity 1.0, two antenna ISPs with two antennas each at capacity 3.0, a 100 km UAV coverage radius, and a 500 km antenna coverage radius.
- OMDAM reports up to 17% social-welfare improvement over the compared schedulers and double-auction baseline in the parsed summary of results.
- The advantage is largest under moderate/heavy load, where random scheduling wastes scarce UAV capacity, Tiresias ignores auction surplus, and the TDCDA baseline lacks maritime mobility and coverage constraints.
- The stated complexity is `O(I*T*M*J)` for `A_core` and `O(N*I*T*M*J)` for `A_online`.

## Limitations / future work

The paper's implemented mechanism does not include explicit UAV trajectory optimization, RL-based UAV positioning, or demand prediction. Those are discussed as future extensions layered around the auction core. The mechanism prioritizes individual rationality, weak budget balance, and high allocative efficiency; stronger truthfulness remains a future refinement. The parse has heavy OCR/math corruption, so this page avoids detailed formula transcription.

## Relation to the corpus

This is a maritime communication/resource-allocation source rather than a compute-offloading MEC paper, but it belongs in the [[maritime-mec]] track because the same infrastructure questions recur in maritime edge systems. It complements [[dai-2024-multiuav-marine-welfare]], which uses a double auction for OBS selection in marine MEC, and [[zeng-2024-usv-fleet-collaborative-offloading]], which uses a reverse auction for UAV-to-USV-fleet offloading. It also sits beside [[li-2020-maritime-uav-satellite-coverage]] as a communication-layer maritime coverage/resource-allocation entry.

## Raw artifacts

- `raw/sources/An_Online_Double_Auction_Mechanism_for_Dynamic_Resource_Allocation_in_Maritime_Networks/An_Online_Double_Auction_Mechanism_for_Dynamic_Resource_Allocation_in_Maritime_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
