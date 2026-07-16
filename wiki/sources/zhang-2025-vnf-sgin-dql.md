---
type: source
modeling_card: required
title: "Learning-Assisted Dynamic VNF Selection and Chaining for 6G Satellite-Ground Integrated Networks"
authors: ["Jianxin Zhang", "Qiang Ye", "Kaige Qu", "Yanglong Sun", "Yuliang Tang", "Dongmei Zhao", "Tong Ye"]
year: 2025
url: "https://doi.org/10.1109/TVT.2024.3454438"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, satellite-ground-integrated-network, nfv, sdn, service-function-chaining, deep-q-network, vnf-migration, 6g]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[non-terrestrial-network]]"
  - "[[network-function-virtualization]]"
  - "[[service-function-chaining]]"
  - "[[deep-q-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[task-migration]]"
  - "[[chen-2024-thoas-traffic-aware-sagin]]"
  - "[[niazmand-2025-jopa-dnn-pruning-iiot]]"
  - "[[pham-2026-vnf-control-loop]]"
  - "[[routing-vnf-scaling-control-loop]]"
created: 2026-05-31
updated: 2026-07-16
---

# Learning-Assisted Dynamic VNF Selection and Chaining for 6G Satellite-Ground Integrated Networks

## Citation

Zhang, J., Ye, Q., Qu, K., Sun, Y., Tang, Y., Zhao, D., & Ye, T. (2025). *Learning-Assisted Dynamic VNF Selection and Chaining for 6G Satellite-Ground Integrated Networks*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3454438. (Date of publication 30 Sep 2024; date of current version 16 Jan 2025.)

## TL;DR

A **deep Q-learning (DQL)** framework for **dynamic VNF selection and chaining (DVSC)** in a **6G satellite-ground integrated network (SGIN)**. Built on SDN/NFV, it determines a set of **VNF selection and chaining policies (VSCPs)** to balance **network resource provisioning + VNF migration costs** against **service performance gain**, maximizing **long-term network profit**. Formulated as a **Markov decision process (MDP)** capturing SGIN heterogeneity and time-varying topology; a new **sharing ratio (SR)** measures compute-resource sharing across VSCP sets.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: An SDN/NFV-enabled satellite-ground integrated network maps ordered service-function chains across time-varying satellite and ground nodes and routes each virtual link over physical satellite-ground, inter-satellite, or terrestrial links.

**Problem & objective**: The NP-hard dynamic VNF selection and chaining problem maximizes long-term network profit, $\max_{\mathbf x_t,\mathbf y_t}\sum_{t=1}^{T}\chi_t$, where profit balances service-performance gain against resource-provisioning and VNF-migration costs.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| VNF placement | $x_t^v(f_{i,l}^j)$ | binary, $\{0,1\}$ | Map VNF $j$ of flow $l$ to physical node $v$ |
| Virtual-link mapping | $y_t^{(v,u)}(f_{i,l}^j,f_{i',l}^{j+1})$ | binary, $\{0,1\}$ | Route a virtual link over physical link $(v,u)$ |
| VSCP-set action | $\mathbf w_m$ | discrete, $\mathbf w_m\in\mathcal W$ | Joint placement and routing policy selected for all flows in one interval |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | VNF processing load at node $v$ remains below $c_{f_i}^v$. |
| C2 | Aggregate flow rate on physical link $(v,u)$ remains below $B_t^{(v,u)}/\sigma$. |
| C3 | Each flow satisfies the end-to-end delay requirement: $D_{l,t}\leq D$. |
| C4 | Virtual-link routes obey source, destination, and intermediate-node flow conservation. |
| C5 | Placement and routing indicators are binary and satisfy service-request compatibility constraints. |

**Algorithm**: Cluster historical network loads, enumerate feasible per-flow chains by breadth-first search, greedily retain a high-profit VSCP set for each load cluster using the sharing ratio, and train a DQN with replay memory, target-network updates, and epsilon-greedy selection over the compressed action space.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] investigated dynamic VNF selection and chaining in an SDN/NFV-enabled satellite-ground integrated network with heterogeneous resources and time-varying topology. They formulated an MDP that selects VNF placements and virtual-link mappings to maximize long-term network profit, balancing service-performance gain against network resource provisioning and VNF migration costs under capacity, delay, service, and flow-conservation constraints. Their DDVSC method clusters historical load records, greedily constructs a compressed action space of VNF selection and chaining policy sets using a sharing ratio, and trains a deep Q-network to select a policy set from evolving network states. Simulations for an immersive online education service report 9.5%, 32.9%, and 8.9% higher accumulated network profit than the three evaluated algorithms and a 3.4% gap to the reported upper bound.

## Problem framing

6G aims for global seamless coverage, but terrestrial networks reach only ~6% of the earth's surface, so SGINs integrate satellites (global coverage, limited compute/bandwidth) with ground networks (rich compute, limited coverage). Supporting end-to-end services means mapping **service function chains (SFCs)** — ordered sequences of VNFs — across heterogeneous nodes. Two challenges: (1) re-mapping SFCs when traffic/topology change causes frequent costly **VNF migrations**; (2) satellite movement makes the topology time-varying, and prior time-varying-graph snapshot methods are storage- and complexity-heavy.

## System model

- **Architecture.** An **SDN/NFV-based SGIN** with a satellite network segment and a ground network segment; an NFV orchestrator (with SDN controller) places VNFs and routes flows. Satellites covering the ground segment are identified via the **virtual node (VN)** approach.
- **Decision.** A **VSCP set** = joint VNF selection + virtual-link mapping for multiple flows; the **sharing ratio (SR)** elaborates the level of compute-resource sharing.
- **Objective.** Maximize long-term network profit = service performance gain minus resource provisioning + VNF migration costs, under service/capacity/delay/flow-conservation constraints.

## Method

- Formulate DVSC as an **[[deep-q-network|MDP]]**; build the action space by (1) **clustering historical network-load records** (k-means-style) into load levels, then (2) **greedily searching** the optimal VSCP set per cluster (breadth-first over VSCPs, descending SR, keeping the highest estimated profit).
- Train a **deep Q-network (DQN)** with an evaluation + target network, replay buffer, and ε-greedy exploration to pick the VSCP set per network state — the **DDVSC** algorithm. VSCP sets are delivered to satellites covering the ground segment to remain feasible under satellite movement.

## Key findings

- The proposed DQL-based VNF selection and chaining algorithm **outperforms baseline algorithms and approaches the performance upper bound**, and balances resource provisioning + VNF migration costs against service-performance gain under dynamic network load (the paper's stated result; specific curves in Section VI).

## Limitations / future work

Simulation-based. Future work: investigate how earth-station deployment density and location affect the VNF selection and chaining problem.

## Relation to the corpus

A distinctive **NFV/SDN service-function-chaining** entry in the SGIN/satellite track — it optimizes **VNF placement + chaining + migration** rather than task offloading, complementing the slicing-based SAGIN scheme [[chen-2024-thoas-traffic-aware-sagin]] and connecting to [[leo-satellite-edge-computing]] and [[task-migration]]. Shares author Qiang Ye (University of Calgary) with [[niazmand-2025-jopa-dnn-pruning-iiot]] and [[wang-2024-maritime-eh-jcora]] (the Qiang-Ye cross-cutting thread). Anchors the [[network-function-virtualization]] and [[service-function-chaining]] concepts.

## Raw artifacts

- `raw/sources/Learning-Assisted_Dynamic_VNF_Selection_and_Chaining_for_6G_Satellite-Ground_Integrated_Networks/Learning-Assisted_Dynamic_VNF_Selection_and_Chaining_for_6G_Satellite-Ground_Integrated_Networks.md`
- Original PDF and extracted figures in the same folder.
