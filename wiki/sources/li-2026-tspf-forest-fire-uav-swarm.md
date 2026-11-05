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
updated: 2026-11-03
modeling_card: required
---

# Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection

## Citation

Li, X., Zhang, W., Liu, L., & Wang, P. (2026). *Two-Tier Submodel Partition Framework for Enhancing UAV Swarm Robustness in Forest Fire Detection*. **IEEE Transactions on Mobile Computing**, 25(1), 1169-1183. DOI: 10.1109/TMC.2025.3599384. The top-level local parse is silent on DOI; DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record.

## TL;DR

Proposes [[two-tier-submodel-partition|TSPF]] for robust UAV-swarm [[uav-forest-fire-detection|forest-fire detection]]. UAVs are graph-colored into spatially dispersed groups, back up data within each group, select group servers dynamically, and train partitioned submodels through two-tier federated aggregation so the swarm can keep training when some UAVs are destroyed.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A swarm $U=\{v_1,\dots,v_N\}$ of trusted UAVs performs forest-fire detection (FFD) and trains a detector online; $N_d$ UAVs may be destroyed during the mission. The swarm is split into $\chi$ groups by graph coloring, UAVs communicate directly (range about 400 m), each group server builds a group dataset (2) from the local datasets (1), and a swarm server updates the global model; the channel is represented only through the size of uploaded parameters.
**Problem & objective**: (3) states three objectives without a single solved program: maximize the accuracy ratio $Acc'/Acc$ under UAV destruction, maximize the restored data $\sum_k\lvert D_{res}(G_k,V_d(G_k))\rvert$, and minimize the communication overhead $OH(U,\chi)$.
**Decision variables**:
| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Group partition | $G_k$, $k=1,\dots,\chi$ | graph-coloring groups | UAV membership of each group |
| Group/swarm servers | $g_k$ and the swarm server | discrete, chosen by score $SC$ | Servers reselected every $t^*$ slots |
| Submodels | $S(1),\dots,S(\tau)$, $\tau\le\chi$ | disjoint layer subsets | Layers trained and uploaded by each group |
**Constraints**:
| ID | Meaning and key expression |
|---|---|
| (6) | Submodels partition the layers: $\bigcup_kS(k)=L$, $S(j)\cap S(k)=\emptyset$ for $j\ne k$ |
| (4) | Server selection score: $SC(v_i)=SOC(v_i)+1-UD(v_i)$ |
| Model rule | Intragroup backup: each local dataset (1) includes the other group members' model parameters and business data, so destroyed UAVs' data can be restored |
| Model rule | Lower-tier aggregation (7) averages submodel gradients within a group; upper-tier aggregation (8) concatenates the submodels, averaging groups that trained the same one when $\tau<\chi$ |
**Algorithm**: Balanced graph coloring → intragroup data backup → dynamic server selection (DSS) by (4) → lower-tier submodel aggregation (7) → upper-tier concatenation (8) → distribute the global model and repeat online updates.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Li et al. [x] studied robust forest-fire detection with a UAV swarm that performs online federated model updates under possible UAV destruction. They designed the Two-tier Submodel Partition Framework, which combines balanced graph coloring, intragroup data backup, Dynamic Server Selection, and lower- and upper-tier aggregation of selected model layers. The framework partitions the global detector into submodels, aggregates selected layers within UAV groups, and concatenates the submodels at a swarm server to reduce parameter uploads. These mechanisms preserve local data and server availability when UAVs fail while maintaining online model updates. Experiments report detection accuracy above distributed learning, FL, and PFL and comparable to centralized learning, which is impractical because of its overhead and single point of failure; TSPF and PFL upload less than FL, HFL, SFL, and HSFL.

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

- `raw/sources/Two-Tier_Submodel_Partition_Framework_for_Enhancing_UAV_Swarm_Robustness_in_Forest_Fire_Detection/Two-Tier_Submodel_Partition_Framework_for_Enhancing_UAV_Swarm_Robustness_in_Forest_Fire_Detection.md`
- Original PDF and extracted figures (`images/`) in the same folder.
