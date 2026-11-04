---
type: source
modeling_card: required
title: "Energy-Efficient Offloading, Caching, and Resource Allocation for Blockchain-Assisted Low-Altitude Flying Networks: An Integrated Federated Learning and MAPPO Approach"
authors: ["Zhiran Wang", "Bintao Hu", "Miguel Lopez-Benitez", "Jianbo Du", "Xiaoli Chu", "F. Richard Yu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3709198"
venue: "IEEE Transactions on Mobile Computing"
tags: [source, low-altitude-network, uav-mec, blockchain, federated-learning, mappo, task-offloading, caching, energy-efficiency]
related:
  - "[[low-altitude-intelligent-network]]"
  - "[[edge-intelligence]]"
  - "[[task-offloading]]"
  - "[[service-caching-mec]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[federated-learning]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[energy-harvesting-mec]]"
  - "[[huang-2024-fed-idcco-iov-caching]]"
  - "[[wang-2024-blockchain-uav-mec-dpos]]"
  - "[[qin-2025-bcuav-masac]]"
created: 2026-07-07
updated: 2026-11-03
---

# Energy-Efficient Offloading, Caching, and Resource Allocation for Blockchain-Assisted Low-Altitude Flying Networks: An Integrated Federated Learning and MAPPO Approach

## Citation

Wang, Z., Hu, B., Lopez-Benitez, M., Du, J., Chu, X., & Yu, F. R. (2026). *Energy-Efficient Offloading, Caching, and Resource Allocation for Blockchain-Assisted Low-Altitude Flying Networks: An Integrated Federated Learning and MAPPO Approach*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3709198.

## TL;DR

Builds a four-layer low-altitude edge-intelligence architecture where UEs send delay-sensitive tasks to task UAVs, task UAVs aggregate work toward service UAVs, service UAVs train FL local models, and a BS aggregates the global model. The proposed FL-MAPPO-BOCRAOA algorithm jointly controls offloading, caching, radio/compute resources, and PV-aware throttling, while a blockchain layer supports trusted cooperation among service UAVs.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: UE tasks traverse a four-layer low-altitude network of UEs, task UAVs (TUAVs), service UAVs (SUAVs), and a BS. SUAVs cache content, execute tasks, train federated local models, record blockchain transactions, and harvest photovoltaic energy with SOC-aware throttling.
**Problem & objective**: Problem $\mathcal P$ (45) minimizes the long-term average utility cost of service delay and energy, $\min_{\{\mathbf a^{(1)},\mathbf a^{(2)},\mathbf a^{(3)},\mathbf p,\mathbf f,\mathbf w\}}\frac1T\sum_tUT(t)$.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Offloading and association | $\mathbf a^{(1)}=\{a_{u,n}(t)\}$, $a_{n,m}(t)$ | binary | UE-to-TUAV and TUAV-to-SUAV assignment |
| Resource-block allocation | $\mathbf a^{(2)}=\{a^k(t)\}$ | binary | RB $k$ use on A2G links |
| Caching strategy | $\mathbf a^{(3)}$ | binary | Content cached at SUAVs |
| Transmit power | $\mathbf p=\{p_u,p_{n,m},p_m\}$ | continuous | UE, TUAV, and SUAV powers |
| Computing resources | $\mathbf f=\{f_{u,n},f_{n,m},f_m^H\}$ | continuous | CPU at TUAVs and SUAVs, including $f_m^H$ |
| FL model | $\mathbf w(t)$ | continuous | Global model whose loss enters the cost |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (C1)-(C2) | Binary offloading, caching, and RB indicators |
| (C3) | Local-training and SOC weights $\eta_m(t),\xi_m(t)\in[0,1]$ |
| (C4)-(C5) | Each UE served by one TUAV, $\sum_na_{u,n}(t)=1$; each TUAV by one SUAV, $\sum_ma_{n,m}(t)=1$ |
| (C6) | Each RB allocated orthogonally to one A2G link |
| (C7)-(C9) | UE, SUAV, and TUAV power limits |
| (C10)-(C11) | TUAV and SUAV computing capacity, including $f_m^H$ at SUAVs |
| (C12) | Cached file size within SUAV memory $S_m^{\max}$ |
**Algorithm**: FL-MAPPO-BOCRAOA models the problem as a multi-agent MDP. CTDE MAPPO agents choose association, RB, power, computing-frequency, caching, and FL-training actions; SUAVs train local models that the BS aggregates, and a lightweight blockchain consensus records transactions to support trusted cooperation.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied energy-efficient task offloading, caching, and resource allocation in a blockchain-assisted low-altitude flying network. They modeled a four-layer UE, task-UAV, service-UAV, and base-station architecture with queueing, content caching, federated learning, blockchain overhead, and photovoltaic energy harvesting. The FL-MAPPO-BOCRAOA method jointly controls association and offloading, resource blocks, power, computing frequency, caching, and FL training through centralized training and decentralized execution. Service UAVs train federated local models and use blockchain records to support trusted cache and processing cooperation. Simulations report the highest final reward and lower average delay than A2C, A3C, MATRPO, and MADDQN as TUAVs and UEs increase, higher cache hit ratio with blockchain-assisted cooperation, and SOC-aware throttling under sunny and cloudy irradiance.

## Problem

Dense low-altitude UAV-MEC networks couple several bottlenecks at once: UE task delay, UAV computation capacity, SUAV cache limits, co-channel interference, queueing delay, energy sustainability, and trust among mobile edge servers. The paper formulates a long-term system utility cost that combines transmission, computation, queueing, fetching delay, and energy consumption across the UE/TUAV/SUAV/BS stack.

## System model

- UE layer: user equipment generates delay-sensitive computation tasks.
- TUAV layer: task UAVs receive UE tasks, process them, aggregate processed results, and request popular files from SUAV caches when an application needs them.
- SUAV layer: service UAVs have finite caches, process aggregated tasks, train FL local models, and act as blockchain nodes for trusted cooperation.
- BS layer: the base station receives local model parameters and aggregates the FL global model.
- Wireless access combines UE-TUAV and BS-SUAV resource allocation with NOMA-style TUAV-SUAV communication in the parse.
- SUAV energy includes remaining battery state, time-varying PV harvesting, and an SOC-aware throttle factor that constrains communication and computation loads.
- SUAV queueing uses a FIFO M/M/1 model, and cache requests follow a Zipf popularity model.

## Method

The paper casts joint offloading, caching, communication resource, and computation resource allocation as a multi-agent decision problem. The proposed FL-MAPPO-BOCRAOA method uses CTDE-style MAPPO: agents learn coordinated policies with a centralized training signal while acting locally at execution time. Federated learning updates are produced at SUAVs and aggregated at the BS; the blockchain model accounts for hash logging, transaction propagation, and lightweight consensus verification overhead.

## Key findings

- The proposed algorithm converges after about 475 episodes in the reported setup, faster than A2C, A3C, MADDQN, and MATRPO baselines.
- At 30 UEs, the parse reports 3.57 s average delay and $5.931 \times 10^3$ J energy for FL-MAPPO-BOCRAOA, below the reported A3C, MATRPO, A2C, and MADDQN values.
- PV-aware throttling keeps higher and more stable battery SOC than the unthrottled case, extends the time until SOC drops to 20% by about 40-70 episodes, and reduces peak communication/compute loads by 15-25% in the simulation.
- Under high M/M/1 load ($\rho \ge 0.7$), the proposed method reduces queue waiting time by 20-25% over MATRPO and over 30% over MADDQN.
- Blockchain support improves the cache hit ratio by an average of 6-9%, with a maximum 10.5% gain in the reported FL-MAPPO-BOCRAOA setting; the steady-state cache hit ratio reaches 0.93.

## Limitations / future work

The study is simulation-based and assumes a centralized BS global aggregator, available network state, and modeled blockchain overhead rather than a deployed blockchain stack. The paper's future work names large-scale multi-tier UAV-terrestrial cooperation and cross-layer communication-computation-consensus optimization.

## Relation to the corpus

This source links the [[task-offloading]] and [[service-caching-mec]] track to [[federated-learning]], [[mappo]], and blockchain trust. It is adjacent to [[huang-2024-fed-idcco-iov-caching]], which also couples FL with caching/offloading in a UAV-assisted vehicular setting, but Wang et al. add PV-aware throttling, M/M/1 queueing, and blockchain-supported cache cooperation. It also complements [[wang-2024-blockchain-uav-mec-dpos]] and [[qin-2025-bcuav-masac]] by moving blockchain from a resource-market or secure-control layer into a low-altitude FL/MAPPO offloading-and-caching loop.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient_Offloading_Caching_and_Resource_Allocation_for_Blockchain-Assisted_Low-Altitude_Flying_Networks_An_Integrated_Federated_Learning_and_MAPPO_Approach/Energy-Efficient_Offloading_Caching_and_Resource_Allocation_for_Blockchain-Assisted_Low-Altitude_Flying_Networks_An_Integrated_Federated_Learning_and_MAPPO_Approach.md`
- Origin PDF: `raw/sources/Energy-Efficient_Offloading_Caching_and_Resource_Allocation_for_Blockchain-Assisted_Low-Altitude_Flying_Networks_An_Integrated_Federated_Learning_and_MAPPO_Approach/Energy-Efficient_Offloading_Caching_and_Resource_Allocation_for_Blockchain-Assisted_Low-Altitude_Flying_Networks_An_Integrated_Federated_Learning_and_MAPPO_Approach.pdf`
- Figures: `raw/sources/Energy-Efficient_Offloading_Caching_and_Resource_Allocation_for_Blockchain-Assisted_Low-Altitude_Flying_Networks_An_Integrated_Federated_Learning_and_MAPPO_Approach/images/`
