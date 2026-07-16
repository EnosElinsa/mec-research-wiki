---
type: source
title: "AoI-Aware Incentive Mechanism for UAV-Assisted Mobile Crowdsensing: A Contract-Theoretic Approach"
authors: ["Yuran Guo", "Ying Chen", "Hongtao Li", "Yuan Wu", "Jiwei Huang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3604073"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav-assisted-mobile-crowd-sensing, age-of-information, contract-theory, incentive-mechanism, mobile-crowdsensing]
related: ["[[aoi-aware-contract-incentives]]", "[[age-of-information]]", "[[contract-theory]]", "[[stackelberg-game]]", "[[reverse-auction-incentive]]", "[[gao-2023-uav-mcs-uma]]", "ying-chen", "[[yuan-wu]]"]
created: 2026-07-11
updated: 2026-07-16
modeling_card: required
---

# AoI-Aware Incentive Mechanism for UAV-Assisted Mobile Crowdsensing: A Contract-Theoretic Approach

## Citation

Guo, Y., Chen, Y., Li, H., Wu, Y., & Huang, J. (2026). *AoI-Aware Incentive Mechanism for UAV-Assisted Mobile Crowdsensing: A Contract-Theoretic Approach*. **IEEE Transactions on Mobile Computing**, 25(2), 1660-1677. DOI: 10.1109/TMC.2025.3604073.

## TL;DR

Designs a hierarchical [[aoi-aware-contract-incentives|AoI-aware contract incentive mechanism]] for UAV-assisted mobile crowdsensing. The platform monitors regional average AoI; when network congestion makes data stale, UAVs can act as temporary base stations while mobile users provide sensing updates. A one-dimensional contract incentivizes UAV service slots, and a multidimensional contract incentivizes users' data-update frequency under sensing and computation costs.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A mobile-crowdsensing platform recruits temporary UAV base stations and sensing users when regional age of information becomes too high.

**Problem & objective**: Choose service-slot and update-frequency contracts to maximize platform utility in the two layers, including $\max_{T_i,R_i}\sum_i q_i^{uav}[\kappa\log(T_i+1)-R_i]$ and $\max_{p_i,R_i}\sum_i q_i^{user}[\eta(cp_i-dp_i^2)-R_i]$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
| --- | --- | --- | --- |
| UAV service slots | $T_i$ | nonnegative integer or continuous slot count | Service duration selected for UAV type $i$ |
| UAV reward | $R_i$ | nonnegative continuous | Payment offered to UAV type $i$ |
| User update frequency | $p_i$ | nonnegative continuous, ordered by type | Sensing updates supplied by user type $i$ |
| User reward | $R_i$ | nonnegative continuous | Payment offered for the selected update frequency |

**Constraints**:

| ID | Meaning and key expression |
| --- | --- |
| C1 | Every UAV and user type satisfies individual rationality |
| C2 | Incentive compatibility makes truthful type selection optimal |
| C3 | Contract rewards and service or update choices obey monotonicity across ordered types |
| C4 | UAV deployment is triggered when regional AoI exceeds its threshold |

**Algorithm**: Reduce pairwise IR and IC constraints, derive closed-form rewards and service or update choices, and apply type clustering and smoothing when unconstrained items violate monotonicity.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Guo et al. [x] designed an AoI-aware hierarchical contract for mobile crowdsensing platforms that recruit temporary UAV base stations and sensing users under information asymmetry. The platform chooses UAV service-slot rewards and user update-frequency rewards to maximize expected utility subject to individual rationality, incentive compatibility, and monotonicity. The method reduces pairwise contract constraints, derives optimal rewards and frequencies, and applies clustering and smoothing when unconstrained items violate monotonicity. Numerical results confirm type self-selection and nonnegative participant utility, and the proposed mechanism yields higher reported platform utility and worker rewards than Stackelberg and reverse-auction baselines under incomplete information.

## Problem

Mobile crowdsensing platforms need fresh data but depend on self-interested mobile users and, in congested or poorly covered regions, UAV assistance. The platform does not know UAV service capabilities or users' sensing/computation costs. Without incentives, UAVs and users may not participate or may under-provide freshness. The paper uses AoI to connect sensing data quality to platform utility and contract theory to handle information asymmetry.

## System model

- The service area is divided into subregions.
- A platform assigns long-term sensing tasks and monitors regional average AoI.
- When a subregion's AoI exceeds a threshold, the platform deploys UAVs as temporary base stations/relays to reduce data transmission delay.
- Users collect and upload sensing data, with update frequency affecting AoI and platform benefit.
- The model has two incentive layers: platform-UAV and platform-user.

## Method

The first layer uses a one-dimensional contract based on UAV type and service time slots. The platform designs UAV rewards under individual rationality and incentive compatibility, with monotonicity handled through contract simplification and clustering/smoothing when needed. The second layer uses a multidimensional contract based on users' sensing and computation costs, reducing user types through marginal cost per update frequency and deriving optimal rewards/update frequencies under IR and IC constraints.

## Key findings

- Experiments use CVXPY on an Intel Core i7-8550U at 1.8 GHz with 15 GB memory.
- The first layer evaluates six UAV types and six subregions; the second layer evaluates 10 user types.
- The contract items satisfy self-selection behavior in the parsed figures: each UAV/user type obtains its best utility by selecting the item intended for that type, and selected-item utilities are non-negative.
- Higher UAV types provide longer service slots and receive higher rewards; lower-cost users update more frequently and obtain higher utility.
- Contract pricing is positioned between uniform and discriminatory pricing, and Fig. 13 reports higher worker rewards and platform utility than Stackelberg and reverse-auction baselines under incomplete information.
- Deploying UAVs as AoI approaches the threshold balances utility and cost; too-early deployment wastes resources, while too-late deployment harms freshness.

## Limitations / future work

The conclusion names future work on improving data freshness and UAV deployment, adding more UAV transmission factors, and differentiating contract types. The page avoids detailed formula transcription because the parse contains mojibake and malformed equations/tables.

## Relation to the corpus

This source extends uav-assisted-mobile-crowd-sensing beyond [[gao-2023-uav-mcs-uma]]'s coverage/calibration scheduling into incentive design. It also broadens [[contract-theory]] beyond edge AIGC service pricing and UAV-FL incentives into AoI-driven mobile crowdsensing. Its comparison with [[stackelberg-game]] and [[reverse-auction-incentive]] makes it useful for the game-theoretic-incentive branch even though the paper is not a compute-offloading optimizer.

## Raw artifacts

- `raw/sources/AoI-Aware_Incentive_Mechanism_for_UAV-Assisted_Mobile_Crowdsensing_A_Contract-Theoretic_Approach/AoI-Aware_Incentive_Mechanism_for_UAV-Assisted_Mobile_Crowdsensing_A_Contract-Theoretic_Approach.md`
- Original PDF and extracted figures (`images/`) in the same folder.
