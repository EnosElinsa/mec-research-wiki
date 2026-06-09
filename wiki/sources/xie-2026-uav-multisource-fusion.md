---
type: source
title: "UAV-Enabled Multi-Source Data Fusion in Vehicular Networks: A Joint Optimization Approach for Reliability and Latency"
authors: ["Qiqi Xie", "Zexiong Wu", "Chaoda Peng", "Xumin Huang", "Yanglin Chen", "Yuan Wu"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3676831"
venue: "IEEE Transactions on Wireless Communications"
tags: [source, uav, vehicular, cooperative-perception, data-fusion, multi-objective, evolutionary-algorithm]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[vehicular-mec]]"
  - "[[cooperative-perception]]"
  - "[[dynamic-constrained-multi-objective-optimization]]"
  - "[[zhang-2025-mcma-task-migration]]"
created: 2026-05-28
updated: 2026-06-09
---

# UAV-Enabled Multi-Source Data Fusion in Vehicular Networks: A Joint Optimization Approach for Reliability and Latency

## Citation

Xie, Q., Wu, Z., Peng, C., Huang, X., Chen, Y., & Wu, Y. (2026). *UAV-Enabled Multi-Source Data Fusion in Vehicular Networks: A Joint Optimization Approach for Reliability and Latency*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3676831.

## TL;DR

Cooperative perception in vehicular networks fuses local observations from many vehicles to overcome single-vehicle occlusion. Existing systems put the fusion platform on either vehicles (V2V — limited by signal blockage) or roadside infrastructure (V2I — limited by fixed coverage). This paper proposes putting the fusion platform on a **UAV** — high-probability LoS, flexible coverage, mobile.

The UAV cyclically:

1. Adjusts position toward requesting vehicular users (VUs).
2. Collects each VU's local observation data on **non-connected objects (NCOs)** — i.e. things only that VU's sensors saw.
3. Fuses across VUs to produce a unified perception.
4. Broadcasts the fused result back.

The optimization problem: maximize **reliability** (perception accuracy / coverage of NCOs) while minimizing **latency**. Cast as a **dynamic constrained multi-objective optimization (DCMOO)** problem (constraints and objectives change as vehicles move). Solved with an **evolutionary algorithm** rather than DRL — because the dynamic constraint shifts faster than online RL can re-train, and the multi-objective Pareto frontier needs explicit population-level exploration.

## Why this is interesting

- **Different solver family.** The paper uses evolutionary dynamic constrained multi-objective optimization instead of a DRL controller.
- **Different MEC role for the UAV.** Most related UAV-MEC sources have UAVs computing offloaded *user tasks*. Here the UAV is a *perception fusion server* — semantically different but topologically similar (UAV as airborne edge).

## Findings

- UAV-fusion outperforms V2V (limited by occlusion) and V2I (limited by fixed coverage) on combined reliability/latency.
- The dynamic constraint formulation correctly handles the fact that the set of requesting VUs and observable NCOs changes per cycle.
- The evolutionary solver achieves competitive Pareto fronts within practical wall-clock budgets.

## Limitations / future work

- Single UAV — multi-UAV multi-area cooperative perception is the natural extension.
- Evolutionary algorithm must restart-warm on each cycle; learning a population-level prior across cycles is open.
- LoS assumption is realistic but doesn't model adversarial environments.

## Cross-link with related sources

- Same vehicular-MEC umbrella as [[zhang-2025-mcma-task-migration]] but with a *perception* (not compute) workload.
- Adds **cooperative perception** as a workload class to the wiki — distinct from the offloading / migration / inference workloads of other sources.
- Fits under [[low-altitude-intelligent-network]] / [[wang-2025-lae-network-survey]]'s integrated-sensing-communication-computing pillar.

## Raw artifacts

- Parse: `raw/sources/UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency/full.md`
- Origin PDF: `raw/sources/UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency/3f0640e8-069b-47ea-8844-e0100315d78c_origin.pdf`
- Figures: `raw/sources/UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency/images/`
