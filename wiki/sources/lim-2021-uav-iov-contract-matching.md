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
updated: 2026-07-14
---

# Towards Federated Learning in UAV-Enabled Internet of Vehicles: A Multi-Dimensional Contract-Matching Approach

## Citation

Lim, W. Y. B., Huang, J., Xiong, Z., Kang, J., Niyato, D., Hua, X.-S., Leung, C., & Miao, C. (2021). *Towards Federated Learning in UAV-Enabled Internet of Vehicles: A Multi-Dimensional Contract-Matching Approach*. **IEEE Transactions on Intelligent Transportation Systems, 22**(8), 5140-5154. DOI: 10.1109/TITS.2021.3056341.

## TL;DR

Uses a multidimensional contract to screen independently owned sensing UAVs by heterogeneous coverage, travel, computation, and upload costs, then applies preference-based matching to assign one UAV to each IoV subregion for federated model training without sharing raw data.

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
