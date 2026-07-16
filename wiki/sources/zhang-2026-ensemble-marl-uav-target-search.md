---
type: source
modeling_card: required
title: "An Ensemble MARL Approach for Heterogeneous UAV Swarm Target Search in 3D Space"
authors: ["Xuan Zhang", "Changxu Wei", "Ziyuan Wang", "Yixian Zhang", "Wenbo Ding", "Xiao-Ping Zhang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3656917"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 7, pp. 10076-10093, Jul. 2026"
tags: [source, uav-swarm, target-search, ensemble-marl, qmix, heterogeneous-uav, action-masking, ctde]
related:
  - "[[ensemble-qmix]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[value-decomposition-network]]"
  - "[[attention-based-uav-target-search]]"
  - "[[heterogeneous-uav-fleet]]"
  - "[[autonomous-uav-swarms]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-11
updated: 2026-07-16
---

# An Ensemble MARL Approach for Heterogeneous UAV Swarm Target Search in 3D Space

## Citation

Zhang, X., Wei, C., Wang, Z., Zhang, Y., Ding, W., & Zhang, X.-P. (2026). *An Ensemble MARL Approach for Heterogeneous UAV Swarm Target Search in 3D Space*. **IEEE Transactions on Mobile Computing**, 25(7), 10076-10093. DOI: 10.1109/TMC.2026.3656917. DOI/venue/year were verified against a title-matched Crossref/IEEE DOI record; technical claims are grounded in the local parse.

## TL;DR

Builds a heterogeneous UAV-swarm target-search controller in 3D space. Fixed-wing UAVs fly high and fast for broad coverage; multirotor UAVs fly lower for more precise detection. The method formulates target search as MARL with action masking for collision/no-fly-zone safety, then proposes [[ensemble-qmix|E-QMIX]], where multiple independently trained QMIX networks vote on each agent's action.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Fixed-wing and multirotor UAVs cooperatively search a discretized three-dimensional region containing unknown targets and no-fly zones. Fixed-wing UAVs provide fast high-altitude coverage, multirotor UAVs provide lower-altitude detection, and each agent acts from local observations under partial observability.

**Problem & objective**: The finite-horizon search problem is a mixed-integer, nonconvex Dec-POMDP that maximizes correctly found targets and penalizes mission duration, $\max_{\mathbf a^{\mathrm F},\mathbf a^{\mathrm M}} J=\lambda_1\kappa_1J_1-\lambda_2\kappa_2J_2$, or equivalently learns policies maximizing expected discounted shared reward.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Fixed-wing action | $a_t^i=(\Delta\phi_{\mathrm H}^i,\Delta z^i)$ | discrete | Heading and altitude changes of fixed-wing UAV $i$ |
| Multirotor action | $a_t^j=(\Delta x^j,\Delta y^j,\Delta z^j)$ | discrete | Grid movement or hovering action of multirotor UAV $j$ |
| Decentralized policy | $\pi^k$ | policy over admissible actions | Maps UAV $k$'s observation history to an action |
| Ensemble action | $\hat a_t^k$ | discrete, majority vote | Action executed after aggregating the E-QMIX members |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Fixed-wing heading, altitude, and horizontal-velocity changes obey the maneuver limits in Eq. (1) |
| C2 | Multirotor coordinate increments and altitude remain within the discrete motion limits in Eq. (2) |
| C3 | Every UAV remains at least $\rho_{\mathrm{safe}}^{\mathrm O}$ from each no-fly zone |
| C4-C5 | Same-type UAVs maintain separations $\rho_{\mathrm{safe}}^{\mathrm F}$ and $\rho_{\mathrm{safe}}^{\mathrm M}$ |
| C6 | The safety mask $m_t^k(a^k)=m_{1,t}^k m_{2,t}^k m_{3,t}^k$ removes collision, no-fly-zone, and boundary-violating actions |

**Algorithm**: Define the Dec-POMDP and shared search-time reward → mask unsafe actions → train separate CTDE E-QMIX ensembles for fixed-wing and multirotor agents with independent replay partitions → obtain one candidate action from each network → execute the majority-voted action during decentralized search.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied target search in a large-scale three-dimensional environment using a heterogeneous swarm of fixed-wing and multirotor UAVs. They formulated the cooperative search as a mixed-integer, nonconvex MARL problem that maximizes target discovery while minimizing search time under partial observability, no-fly-zone restrictions, and collision constraints. Their safety-aware action mask removes inadmissible moves, and their Ensemble QMIX framework trains multiple independent QMIX networks and aggregates their decentralized actions by majority voting. A mathematical analysis shows that majority voting increases an agent's probability of selecting the optimal action when the individual-network success probability exceeds one half. Simulations report that E-QMIX achieves the highest search efficiency and coverage rate among the evaluated single-network MARL and ensemble baselines.

## Problem

Homogeneous UAV swarms struggle to cover large 3D regions quickly while also detecting targets accurately. Fixed-wing UAVs offer speed and wide fields of view but lower precision; multirotor UAVs offer high-precision detection but slower, narrower coverage. The paper asks how to coordinate both types under partial observability, no-fly zones, collision constraints, unknown targets, and large joint action spaces.

## System model

The environment is a gridded 3D search region with targets and no-fly zones. Fixed-wing UAVs and multirotor UAVs operate in separate altitude bands, with altitude-dependent sensing radius, detection probability, and false-alarm probability. The target probability map is updated during search, and the objective jointly rewards finding more targets and reducing search time.

## Method

The base MARL setup uses [[centralized-training-decentralized-execution|CTDE]] and action masking to discard unsafe moves. The paper compares QMIX, VDN, MAPPO, MADQN, and random baselines, then introduces Ensemble MARL. E-QMIX trains multiple QMIX models independently and, during decentralized execution, each UAV chooses the majority-voted action across its model ensemble. Theoretical analysis shows that if each individual network selects the optimal action with probability above 0.5, majority voting increases the probability of selecting the optimal action for ensemble size at least 3.

## Key findings

- In the training setting with 50 by 50 cells, 4 fixed-wing UAVs, 16 multirotor UAVs, 30 targets, and 10 no-fly zones, QMIX reaches the highest and most stable episode reward among the single-network MARL methods; VDN is lower and higher-variance, MAPPO converges early but to a lower reward, and MADQN is the weakest learned baseline.
- In testing, E-QMIX finds targets fastest and reaches the highest coverage efficiency across the reported 4-FUAV/16-MUAV and 8-FUAV/32-MUAV settings.
- E-QMIX and E-VDN outperform their single-network backbones, supporting the majority-voting ensemble mechanism.
- The same model maintains search ability across different swarm sizes and target counts; increasing the UAV count reduces search time, and E-QMIX consistently completes the target search in the shortest time among benchmarks.
- Table III shows E-QMIX consistently improves episode reward over QMIX across total UAV counts 15, 20, 25, and 30 for tested ensemble sizes, but very large ensembles can degrade because the majority-voted action may mismatch each recurrent network's hidden-state trajectory.

## Limitations / future work

The simulation uses a simplified discretized 3D model rather than full real-world flight dynamics. Ensemble MARL increases computation overhead, and E-QMIX can suffer recurrent hidden-state inconsistency when the voted action differs from individual network outputs. Future work will extend to continuous settings, reduce ensemble overhead, validate in real scenarios, and explore uncertainty-aware or diversity-enhancing ensemble strategies.

## Relation to the corpus

This is an adjacent UAV-swarm search source, not an MEC offloading paper. It complements [[zhu-2026-hab-mappo-target-search]], which couples target search with image offloading and charging, by isolating the MARL coordination question for heterogeneous fixed-wing/multirotor search. Methodologically, it adds a QMIX/value-decomposition branch to the wiki's [[centralized-training-decentralized-execution]] vocabulary, addressing the prior gap noted in [[drl-backbones-across-uav-mec-sources]] where QMIX was not yet represented by a curated source.

## Raw artifacts

- `raw/sources/An_Ensemble_MARL_Approach_for_Heterogeneous_UAV_Swarm_Target_Search_in_3D_Space/An_Ensemble_MARL_Approach_for_Heterogeneous_UAV_Swarm_Target_Search_in_3D_Space.md`
- Original PDF and extracted figures (`images/`) in the same folder.
