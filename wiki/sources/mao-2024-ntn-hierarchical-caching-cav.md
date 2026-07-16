---
type: source
title: "On a Hierarchical Content Caching and Asynchronous Updating Scheme for Non-Terrestrial Network-Assisted Connected Automated Vehicles"
authors: ["Bomin Mao", "Yangbo Liu", "Hongzhi Guo", "Yijie Xun", "Jiadai Wang", "Jiajia Liu", "Nei Kato"]
year: 2024
url: "https://doi.org/10.1109/JSAC.2024.3460063"
venue: "IEEE Journal on Selected Areas in Communications (IEEE JSAC)"
modeling_card: required
tags: [source, non-terrestrial-network, content-caching, connected-automated-vehicles, ant-colony-optimization, multi-agent-drl, leo-satellite]
related:
  - "[[non-terrestrial-network]]"
  - "[[service-caching-mec]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[ant-colony-optimization]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[zhao-2024-caching-service-placement-uav]]"
  - "[[zhao-2025-traj-offload-cache-migration]]"
created: 2026-05-29
updated: 2026-07-16
---

# On a Hierarchical Content Caching and Asynchronous Updating Scheme for Non-Terrestrial Network-Assisted Connected Automated Vehicles

## Citation

Mao, B., Liu, Y., Guo, H., Xun, Y., Wang, J., Liu, J., & Kato, N. (2024). *On a Hierarchical Content Caching and Asynchronous Updating Scheme for Non-Terrestrial Network-Assisted Connected Automated Vehicles*. **IEEE Journal on Selected Areas in Communications**. DOI: 10.1109/JSAC.2024.3460063.

## TL;DR

Content caching for **connected automated vehicles (CAVs)** served by **non-terrestrial networks (NTNs)** of LEO satellites and UAVs (for collaborative viewing, traffic sensing, metaverse entertainment in remote areas). Treating all LEO satellites as caching nodes causes content duplication and interference, so the authors use **Delay-Motivated Ant Colony Optimization (DM-ACO)** to select caching satellites with reduced propagation delay, then a **Multi-Agent DRL-based Hierarchical Caching and Asynchronous Updating (MADRL-HCAU)** strategy to manage LEO/UAV caching capacity with customized QoS.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A LEO-satellite and UAV caching hierarchy serves clustered connected automated vehicles with requested contents. LEO satellites are selected as caching nodes while other satellites relay content, and UAVs move between vehicle clusters under time-varying requests.

**Problem & objective**: The WMVC selection stage minimizes propagation cost $\min Z=\sum_{k=1}^{K}\sum_{k^{\prime}=1}^{K}w_{s_k,s_{k^{\prime}}}$ subject to graph connectivity, followed by hierarchical caching-delay minimization $\min Z^{\prime}=\sum_i\sum_q\sum_t D_{v_i,f_q}^{t}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Caching LEO set | $CS$ | binary vertex-selection set | LEO satellites chosen as caching nodes in the WMVC stage |
| UAV cache indicator | $C_{u_j,F}^{t}$ | binary | Whether UAV $u_j$ stores content vector $F$ at time $t$ |
| LEO cache indicator | $C_{s_k,F}^{t}$ | binary | Whether satellite $s_k$ stores content vector $F$ at time $t$ |
| Cache substitution action | $a_{u_j}^{t},a_{s_k}^{t}$ | discrete switch-out and switch-in pair | Content removed and content inserted at a UAV or LEO cache |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| WMVC connectivity | Selected caching vertices keep the topology connected: $\sum_{\bar{k}=1}^{\bar{K}}(cs_{\bar{k}})^{\circ}\geq 2S$ |
| C1, C2 | Cache indicators are binary for UAVs and LEO satellites: $C_{u_j,F}^{t},C_{s_k,F}^{t}\in\{0,1\}$ |
| C3 | UAV cache size is bounded: $\sum_q C_{u_j,f_q}^{t}S_{f_q}\leq\mathcal C_{u_j}$ |
| C4 | LEO cache size is bounded: $\sum_q C_{s_k,f_q}^{t}S_{f_q}\leq\mathcal C_{s_k}$ |
| C5 | Actual content transmission time does not exceed its delay threshold: $D_{v_i,f_q}^{t}\leq D_{f_q}$ |

**Algorithm**: Use DM-ACO to construct a low-delay WMVC caching-satellite set from pheromone and degree-based visibility. Then use Layer 1 multi-agent DQN for UAV cache decisions and Layer 2 centralized DQN for LEO cache decisions, with asynchronous switch-out and switch-in actions to smooth update traffic.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Mao et al. [x] studied hierarchical content caching for connected automated vehicles served by LEO satellites and UAVs in a non-terrestrial network. They minimized a weighted minimum-vertex-cover propagation cost for caching-satellite selection and then minimized aggregate content transmission delay under binary cache, capacity, and delay-threshold constraints. Their DM-ACO stage selects the caching LEO set, while a two-layer MADRL-HCAU policy makes UAV and LEO cache substitutions with asynchronous updates. Simulations reported packet-drop rates below 7.64 percent and delays below 4.13 seconds for asynchronous updates, with cache-hit ratios reaching 78.3 percent by vehicle requests and 81.1 percent by content count.

## Problem framing

NTNs give seamless coverage for CAVs, but heterogeneous caching hardware, varying communication environments, and frequent dynamics complicate caching policy. Two issues: (1) using every LEO as a cache wastes storage and degrades transmission via interference; (2) providing customized QoS via intra-/inter-layer cooperative caching is open.

## System model

- **Tiers.** LEO satellites + UAVs (NTN) caching for ground CAVs ([[non-terrestrial-network]], [[leo-satellite-edge-computing]]).
- **Caching-satellite selection** posed as a weighted minimum-vertex-cover (WMVC) problem minimizing system propagation delay.

## Method

- **DM-ACO:** delay-motivated ant colony optimization selects caching LEO satellites to reduce propagation delay ([[ant-colony-optimization]]).
- **MADRL-HCAU:** multi-agent DRL hierarchical caching + asynchronous updating manages LEO/UAV caching capacity, providing customized CAV services and dispensing peak traffic ([[centralized-training-decentralized-execution]]).

## Key findings

- Simulations show the scheme accelerates caching refresh and content downloading, reduces packet drop, and improves cache hit ratio (CHR) and average transmission delay versus popularity-aware and traditional LIFO caching (qualitative; specific curves in the paper).

## Limitations / future work

The authors note MADRL-HCAU's robust scalability to SAGINs (treating RSUs/BSs as fixed gravity-free UAVs) as a future direction.

## Relation to the corpus

A **caching over non-terrestrial networks** entry that complements the UAV caching/service-placement work [[zhao-2024-caching-service-placement-uav]] and the caching/migration study [[zhao-2025-traj-offload-cache-migration]], extending caching into the LEO/NTN + vehicular space. Introduces [[non-terrestrial-network]] and [[ant-colony-optimization]] to the corpus and reinforces [[service-caching-mec]].

## Raw artifacts

- `raw/sources/On_a_Hierarchical_Content_Caching_and_Asynchronous_Updating_Scheme_for_Non-Terrestrial_Network-Assisted_Connected_Automated_Vehicles/full.md`
- Original PDF and extracted figures in the same folder.
