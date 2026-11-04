---
type: source
modeling_card: required
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
  - "[[qiqi-xie]]"
created: 2026-05-28
updated: 2026-11-03
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

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A mobile UAV acts as an airborne cooperative-perception fusion server for moving vehicular users (VUs). In each time slot it responds to requesting VUs, collects their local observations of non-connected objects, fuses the data, and returns compressed fusion results over dynamic air-to-ground links.

**Problem & objective**: The dynamic constrained multi-objective problem (28) minimizes $\{-G_1(\mathbf x(n)),G_2(\mathbf x(n))\}$, maximizing average fusion reliability $G_1$ (26) and minimizing average VU waiting time $G_2$ (27), over the individual $\mathbf x(n)=(\mathbf q^{\mathrm u}(n),\boldsymbol\beta(n),\boldsymbol\alpha(n),\boldsymbol h(n),\boldsymbol B(n))$ (25).

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV position | $\mathbf q^{\mathrm u}(n)$ | continuous 3-D position | UAV location in slot $n$ |
| Request response | $\beta_m(n)$ | binary | UAV responds to VU $m$'s request |
| Data collection | $\alpha_m(n)$ | binary | VU $m$ uploads local observation data |
| Compression degree | $h_m(n)$ | continuous | Compression of the fusion result returned to VU $m$ |
| Bandwidth allocation | $B_m(n)$ | continuous, nonnegative | Uplink bandwidth assigned to VU $m$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1-C4 | UAV kinematics: speed at most $v^{\max}$, altitude within $[h^{\min},h^{\max}]$, and turning angle at most $\theta^{\max}$ |
| C5-C6 | The UAV responds only to requesting VUs and collects data from every VU it responds to |
| C7-C8 | Bandwidth goes only to uploading VUs, and total bandwidth is at most $B^{\max}$ |
| C9 | Each accepted request completes within one slot: $\beta_m(n)T_m^{\mathrm{wait}}(n)\le\delta$ |

**Algorithm**: Extend constrained NSGA-II into a dynamic constrained multi-objective evolutionary algorithm (DCMOEA) → when a new slot changes the environment, regenerate decision variables in their dependency order (request response, then data collection, then bandwidth) with the cascaded dependency generation strategy → evolve and retain feasible nondominated reliability-latency solutions.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xie et al. [x] studied UAV-enabled multi-source data fusion for cooperative perception in vehicular networks. A UAV collects local observations of non-connected objects from moving vehicles, fuses the observations, and broadcasts a unified perception result. They formulated a dynamic constrained multi-objective problem that maximizes perception reliability and minimizes latency as vehicle positions, requests, and observable objects change. A DCMOEA built on constrained NSGA-II uses a cascaded dependency generation strategy to rebuild feasible decisions when the environment changes. Simulations report better reliability-latency tradeoff solutions than four baseline dynamic multi-objective algorithms.

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

- Parse: `raw/sources/UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency/UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency.md`
- Origin PDF: `raw/sources/UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency/UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency.pdf`
- Figures: `raw/sources/UAV-Enabled_Multi-Source_Data_Fusion_in_Vehicular_Networks_A_Joint_Optimization_Approach_for_Reliability_and_Latency/images/`
