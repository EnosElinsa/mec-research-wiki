---
type: source
title: "Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection"
authors: ["Xingyu Li", "Wenzhe Zhang", "Linfeng Liu", "Ping Wang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3599384"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 1, pp. 1169-1183, Jan. 2026"
tags: [source, uav-swarm, forest-fire-detection, federated-learning, robustness, edge-intelligence]
related:
  - "[[two-tier-submodel-partition]]"
  - "[[uav-forest-fire-detection]]"
  - "[[federated-learning]]"
  - "[[split-federated-learning]]"
  - "[[task-redundancy-for-reliability]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[edge-intelligence]]"
created: 2026-07-07
updated: 2026-07-16
modeling_card: required
---

# Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection

## Citation

Li, X., Zhang, W., Liu, L., & Wang, P. (2026). *Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection*. **IEEE Transactions on Mobile Computing**, 25(1), 1169-1183. DOI: 10.1109/TMC.2025.3599384. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Proposes [[two-tier-submodel-partition|TSPF]] for robust UAV-swarm [[uav-forest-fire-detection|forest-fire detection]]. UAVs are graph-colored into spatially dispersed groups, back up data within each group, select group servers dynamically, and train partitioned submodels through two-tier federated aggregation so the swarm can keep training when some UAVs are destroyed.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A UAV swarm performs forest-fire detection and trains an online object-detection model. Graph coloring spreads UAVs across groups, group servers and a swarm server aggregate model updates, and intragroup wireless exchanges carry selected layers and backups. Multiple access uses scheduled point-to-server parameter exchanges; the paper does not specify a NOMA/OMA waveform, and the channel is represented through its communication-overhead model.

**Problem & objective**: A mixed discrete robustness and federated-learning design, represented as a multi-criterion objective $\max_X[A_{\mathrm{FFD}}(X),R_{\mathrm{robust}}(X),-C_{\mathrm{comm}}(X)]$, improving fire-detection accuracy and survivability while reducing model-upload overhead after UAV destruction.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Group color | $c_u$ | integer color label | Group assigned to UAV $u$ |
| Backup assignment | $b_{u,v}$ | binary | Whether surviving UAV $v$ stores UAV $u$'s local data |
| Group/swarm servers | $s_g,s_0$ | discrete selection | Servers for group $g$ and the whole swarm |
| Selected model layers | $\mathcal L_g$ | discrete subset | Submodel layers uploaded in lower-tier aggregation |
| Partition count | $\tau$ | positive integer | Number of disjoint submodels in the two-tier update |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Every UAV receives one graph-color group and groups satisfy the balanced/dispersed coloring rule |
| C2 | Backup assignments remain within intragroup storage and contact limits |
| C3 | Each group and the swarm select an available server using the DSS score |
| C4 | Selected submodel layers form disjoint partitions that can be concatenated into the global model |
| C5 | Model updates and recovery use only surviving UAVs and available communication links |

**Algorithm**: Balanced graph coloring → intragroup data backup → dynamic server selection → lower-tier selected-layer aggregation → upper-tier submodel concatenation and swarm aggregation → distribute the global model and repeat online updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied robust forest-fire detection with a UAV swarm that performs online federated model updates under possible UAV destruction. They designed the Two-tier Submodel Partition Framework, which combines balanced graph coloring, intragroup data backup, Dynamic Server Selection, and lower- and upper-tier aggregation of selected model layers. The framework partitions the global detector into submodels, aggregates selected layers within UAV groups, and concatenates the submodels at a swarm server to reduce parameter uploads. These mechanisms preserve local data and server availability when UAVs fail while maintaining online model updates. Experiments report improved fire-detection accuracy and robustness with lower communication overhead than the evaluated centralized, federated, and distributed baselines.

## Problem

Forest-fire detection needs fast edge inference in harsh, failure-prone environments. Centralized learning can be communication-heavy, while standard [[federated-learning|FL]] and distributed learning can lose data and accuracy when fire-damaged UAVs disappear. The paper asks how a UAV swarm can preserve detection accuracy, reduce communication delay, and remain trainable after node destruction.

## System model

The model uses a swarm of UAVs that collect fire-scene data and carry local model parameters, mission data, and backups for UAVs in the same group. A balanced graph-coloring step assigns UAVs to groups so same-group UAVs are spatially separated; each group has a group server, and the whole swarm has a swarm server. The simulations use a 100-UAV swarm split into 10 groups, with ResNet18 on the FLAME dataset and a reported Jetson Xavier NX feasibility discussion.

## Method

TSPF combines four pieces:

- balanced graph coloring for spatially dispersed group membership;
- intragroup data backup for robustness against destroyed UAVs;
- Dynamic Server Selection (DSS), which chooses group servers using state of charge and spatial-uniformity criteria;
- Two-Tier Federated Learning (TFL), where lower-tier group aggregation handles selected layers and the upper-tier swarm aggregation concatenates partitioned submodels.

## Key findings

- TSPF reports detection accuracy comparable to centralized learning and better than the distributed-learning, FL, and personalized-FL baselines in the parsed experiments.
- The communication-overhead table reports 5.59 MB of transmitted selected parameters for TSPF/PFL versus 11.18 MB full-model transmission for FL/HFL.
- TSPF reduces communication delay and training time relative to centralized and standard-FL baselines, which the paper frames as important for delay-sensitive fire detection.
- Intragroup backup preserves destroyed UAVs' data, while FL/distributed baselines lose the affected local datasets.
- The reported ablation selects group count chi = 10 and partition number tau = 2 as strong operating points; larger tau values increase fluctuations or degrade accuracy in the parsed figures.
- Robustness declines as fewer UAVs survive, but TSPF maintains model training under reduced surviving-node counts better than the baselines.

## Limitations / future work

The paper names three follow-up directions: a more specific backup mechanism, topology recovery and path planning when destroyed UAVs disrupt connectivity, and privacy-preserving erasure-coding-style backup.

## Relation to the corpus

This source adds robust [[uav-forest-fire-detection]] and [[two-tier-submodel-partition]] to the UAV-swarm line. It complements [[sun-2024-asap-uav-swarm]] and [[qu-ecoei-uav-swarm]], which focus on in-swarm inference, and [[wang-2026-scalable-multiuav-analytics]], which partitions video-analytics DAGs across UAVs. Its redundancy mechanism is data-preservation-oriented, distinct from [[task-redundancy-for-reliability]] where redundant task execution mitigates stochastic processor failures.

## Raw artifacts

- `raw/sources/Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection/Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection.md`
- Original PDF and extracted figures (`images/`) in the same folder.
