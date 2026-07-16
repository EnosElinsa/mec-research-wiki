---
type: source
title: "Towards Federated Learning in UAV-Enabled Internet of Vehicles: A Multi-Dimensional Contract-Matching Approach"
authors: ["Wei Yang Bryan Lim", "Jianqiang Huang", "Zehui Xiong", "Jiawen Kang", "Dusit Niyato", "Xian-Sheng Hua", "Cyril Leung", "Chunyan Miao"]
year: 2021
url: "https://doi.org/10.1109/TITS.2021.3056341"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS), vol. 22, no. 8, pp. 5140-5154"
tags: [source, federated-learning, uav, internet-of-vehicles, contract-theory, matching, incentive-mechanism]
related:
  - "[[aerial-federated-aggregation-design-space]]"
  - "[[multidimensional-contract-matching]]"
  - "[[contract-theoretic-fl-incentives]]"
  - "[[federated-learning]]"
  - "[[contract-theory]]"
  - "[[gale-shapley-matching]]"
  - "[[matching-theory-for-resource-allocation]]"
  - "[[uav-assisted-mobile-crowd-sensing]]"
  - "[[wei-yang-bryan-lim]]"
  - "[[zehui-xiong]]"
  - "[[jiawen-kang]]"
  - "[[dusit-niyato]]"
created: 2026-07-14
updated: 2026-07-16
modeling_card: required
---

# Towards Federated Learning in UAV-Enabled Internet of Vehicles: A Multi-Dimensional Contract-Matching Approach

## Citation

Lim, W. Y. B., Huang, J., Xiong, Z., Kang, J., Niyato, D., Hua, X.-S., Leung, C., & Miao, C. (2021). *Towards Federated Learning in UAV-Enabled Internet of Vehicles: A Multi-Dimensional Contract-Matching Approach*. **IEEE Transactions on Intelligent Transportation Systems, 22**(8), 5140-5154. DOI: 10.1109/TITS.2021.3056341.

## TL;DR

Uses a multidimensional contract to screen independently owned sensing UAVs by heterogeneous coverage, travel, computation, and upload costs, then applies preference-based matching to assign one UAV to each IoV subregion for federated model training without sharing raw data.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A model owner divides an IoV sensing region into subregions and hires heterogeneous sensing UAVs to collect data for federated learning. Each UAV flies from its base to a subregion, senses and computes locally, then uploads a model update; access is one UAV per subregion with orthogonal point-to-point uploads over air-to-ground links.

**Problem & objective**: Multi-dimensional contract design and one-to-one matching, a discrete-continuous incentive optimization, maximizes the model owner's profit, $\max\sum_r[V_r(c_r)-\pi_r]$, subject to coverage, individual-rationality, incentive-compatibility, and stable-assignment constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Coverage allocation | $c_r$ | continuous, monotone | Sensing coverage promised to subregion $r$ |
| Contract reward | $\pi_r$ | continuous, nonnegative | Payment offered for a coverage type |
| UAV-subregion matching | $x_{u,r}$ | binary | UAV $u$ is assigned to subregion $r$ |
| Reported UAV type | $\hat\theta_u$ | discrete type | Sensing, travel, computation, and upload cost type reported by UAV $u$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every subregion is assigned at most one UAV, $\sum_u x_{u,r}\le1$ |
| C2 | Contract offers satisfy individual rationality for participating UAV types |
| C3 | Adjacent contract types satisfy incentive compatibility and monotone coverage |
| C4 | A matching is one-to-one and respects UAV availability and subregion preference lists |
| C5 | UAV utility includes sensing, travel, computation, and model-upload costs |

**Algorithm**: Reduce multidimensional IR/IC to worst-type IR and adjacent IC → recurse minimum rewards for a monotone coverage vector → repair non-monotone allocations by bunching/ironing → build preference lists → run Gale-Shapley matching → perform local federated updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lim et al. [x] studied federated learning data collection in a UAV-enabled Internet of Vehicles through multidimensional contract matching. They formulated a contract-theoretic mechanism that maximizes the model owner's profit while accounting for heterogeneous sensing, travel, computation, and model-upload costs of UAV service providers. Individual-rationality and incentive-compatibility conditions are reduced to a worst-type IR constraint and adjacent IC constraints, with bunching and ironing used when the coverage allocation is non-monotone. A preference-based one-to-one Gale-Shapley procedure then assigns UAVs to sensing subregions under the resulting contracts. Numerical examples report truthful type ordering, cost-dependent rewards, and stable assignments across heterogeneous UAV types and subregions.

## System model

- A model owner partitions an IoV sensing region into graph subregions and assigns one of more available UAV service providers to each subregion.
- A UAV flies from its base, covers part of a subregion, returns for local training, and uploads a fixed-size model update. Raw sensed data remains local.
- Private cost has four components: sensing/coverage propulsion, base-to-region travel, local computation, and model-update transmission.
- The model owner's value is a concave logarithmic surrogate of covered data, not measured FL accuracy.

## Method and guarantee scope

- Sensing and computation costs are collapsed into a marginal-coverage auxiliary type. Monotonicity, individual-rationality, and incentive-compatibility constraints reduce to a worst-type IR constraint and adjacent IC constraints.
- For a fixed monotone coverage vector, the reward recursion gives the minimum payments satisfying the reduced constraints; bunching and ironing repair non-monotone coverage allocations.
- Subregions prefer low marginal-cost UAVs, while UAVs rank contracts using utility and travel cost. A Gale-Shapley-style one-to-one procedure produces a stable assignment under those fixed preferences.
- Fixed travel/upload compensation can still make some UAV types' total utility negative. Therefore, the complete four-cost mechanism does not guarantee individual rationality for every type, and the paper does not jointly optimize FL learning, contracts, routes, and matching globally.

## Findings

- In the six-type example, coverage and reward decrease with marginal cost; the plotted utilities favor truthful type reporting.
- Model-owner profit is highest for the lowest-cost feasible UAV in the tested single-subregion case.
- In multi-subregion examples, distance changes UAV preferences and reward calibration breaks marginal-cost ties. Adding an extra low-cost UAV displaces a higher-cost participant and leaves the highest-cost UAV unmatched.
- Assignment invariance under selected sensing-area/data changes is scenario-specific because those changes preserve type ordering.

## Limitations

The work evaluates the mechanism rather than an FL task: it provides no dataset, model architecture, non-IID split, convergence curve, accuracy result, privacy attack, or wireless experiment. Rate, update size, propulsion, and return-to-base training are simplified, and direction-change energy is omitted. The four-dimensional private information is only partly represented by the one-dimensional sorting type. Several equations and an example table are OCR-damaged or internally inconsistent.

## Relation to the corpus

This extends [[contract-theoretic-fl-incentives]] with an explicit contract-plus-matching pipeline. Unlike [[zhao-2026-uav-fl-inspection-incentives]], it evaluates economic assignment behavior rather than federated training performance. [[zhou-2026-cpsfl-uav-foundation-models]] later represents a communication-centered UAV FL line co-authored by [[wei-yang-bryan-lim]].

[[aerial-federated-aggregation-design-space]] uses this source only as an adjacent ex-ante participation control: contracts and stable matching decide which UAV gathers data before training, without transferring those economic guarantees to aggregation or learning performance.

## Raw artifacts

- Parse: `raw/sources/Towards_Federated_Learning_in_UAV-Enabled_Internet_of_Vehicles_A_Multi-Dimensional_Contract-Matching_Approach/Towards_Federated_Learning_in_UAV-Enabled_Internet_of_Vehicles_A_Multi-Dimensional_Contract-Matching_Approach.md`
- Original PDF and extracted figures are in the same folder.
