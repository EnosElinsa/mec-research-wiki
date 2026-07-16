---
type: source
title: "UAV Trajectory Planning for AoI-Minimal Data Collection in UAV-Aided IoT Networks by Transformer"
authors: ["Botao Zhu", "Ebrahim Bedeer", "Ha H. Nguyen", "Robert Barton", "Zhen Gao"]
year: 2023
url: "https://doi.org/10.1109/TWC.2022.3204438"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 22, no. 2, February 2023"
tags: [source, age-of-information, uav-data-collection, uav-trajectory-control, transformer, weighted-a-star, generalized-traveling-salesman-problem]
related:
  - "[[age-of-information]]"
  - "[[uav-data-collection]]"
  - "[[uav-trajectory-control]]"
  - "[[transformer-weighted-a-star-trajectory-planning]]"
  - "[[generalized-traveling-salesman-problem]]"
  - "[[hovering-disk-data-collection]]"
  - "[[samir-2020-time-constrained-data-collection]]"
  - "[[chang-2026-data-offloading-energy-constraints]]"
  - "[[constraint-regimes-in-uav-data-collection]]"
  - "[[transformer-encoder]]"
  - "[[air-to-ground-channel-model]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[zeng-2019-rotary-wing-energy-min]]"
  - "[[guo-2026-aot-uav-inspection-offloading]]"
  - "[[pytorch]]"
modeling_card: required
created: 2026-07-14
updated: 2026-07-16
---

# UAV Trajectory Planning for AoI-Minimal Data Collection in UAV-Aided IoT Networks by Transformer

## Citation

Zhu, B., Bedeer, E., Nguyen, H. H., Barton, R., & Gao, Z. (2023). *UAV Trajectory Planning for AoI-Minimal Data Collection in UAV-Aided IoT Networks by Transformer*. **IEEE Transactions on Wireless Communications**, 22(2), 1343-1358. DOI: 10.1109/TWC.2022.3204438. Published online 14 September 2022; current issue version 13 February 2023.

## TL;DR

Formulates fresh-data collection by one rotary-wing UAV as joint cluster-order and hovering-point selection. SNR-feasible hovering disks turn the continuous traveling-salesman problem with neighborhoods into a discretized [[generalized-traveling-salesman-problem|GTSP]]. A Transformer selects the cluster order, weighted A-star chooses one candidate hovering point per ordered cluster, and REINFORCE trains the ordering policy against a greedy rollout baseline. Sampling decoding gives the lowest total [[age-of-information|AoI]] among the evaluated methods, but the paper does not prove global optimality or an approximation ratio for the learned pipeline.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One rotary-wing UAV starts and ends above a BS, visits clustered IoT devices, and collects each cluster head's data at one hovering point; ordinary nodes use TDM and one cluster head transmits at a time over a probabilistic LoS/NLoS air-to-ground channel.

**Problem & objective**: Problems $\mathcal P_1$ and $\mathcal P_2$, an NP-hard TSPN converted to a GTSP, minimize $\bar A(\mathbf c,\boldsymbol\pi)$, the total AoI of all collected updates at mission completion.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Hovering points | $\mathbf c=\{\mathbf c_m\}$ | Continuous in $O_m$, then discrete in $G_m$ | One SNR-feasible collection point for each cluster |
| Visiting order | $\boldsymbol\pi$ | Permutation of $\{1,\ldots,M\}$ | Order in which the UAV visits the clusters |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Each hovering point satisfies the receive-SNR disk constraint $\mathbf c_m\in O_m$ |
| C2 | The discretized GTSP selects exactly one candidate, $\mathbf c_m\in G_m\subset O_m$ |
| C3 | The route visits each selected hovering point exactly once and returns to the BS |
| C4 | Collection, flight-time, and AoI relations follow (7), (9), (15), and (16) |

**Algorithm**: TWA-star, discretize each hovering disk, encode the UAV-IoT instance with a Transformer, decode a cluster permutation, select hovering points with weighted A-star, and train the ordering policy with REINFORCE and a greedy rollout baseline.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhu et al. [x] studied AoI-oriented data collection by a rotary-wing UAV in a cluster-based IoT network. They formulated a total-AoI minimization problem that jointly selects one SNR-feasible hovering point per cluster and the order in which those points are visited. Their TWA-star method discretizes each hovering disk, uses a Transformer to generate the cluster order, and applies weighted A-star to choose the hovering points. The Transformer is trained with REINFORCE using a deterministic greedy rollout as its baseline. Simulations show that sampling-decoded TWA-star attains the lowest total AoI among the evaluated decoders and comparison algorithms and generalizes from ten-cluster training instances to larger networks.

## Problem

A UAV must leave a ground BS, collect time-sensitive updates from clustered IoT devices through their cluster heads, and return to the BS. Hovering near a cluster head improves uplink rate and reduces forwarding time, while a point near the edge of its feasible disk may shorten the flight route. The objective jointly chooses one hovering point per cluster and the visiting order to minimize the sum AoI of all ordinary-node packets when the UAV returns. Propulsion energy is evaluated but is not the optimization objective or a displayed battery-budget constraint.

## System model

- One rotary-wing UAV serves `M` clusters and starts and ends above the BS. Cluster `m` contains a cluster head and `N_m` ordinary nodes.
- Ordinary nodes generate updates on demand and transmit to their cluster head in equal-duration TDM slots. The cluster head forwards the collected data to the UAV; only one cluster head transmits to it at a time.
- The UAV flies at fixed altitude and horizontal speed along straight legs, hovering to collect data. Wake-up and sensing times and acceleration/deceleration are neglected.
- A probabilistic LoS/NLoS [[air-to-ground-channel-model]] defines average path loss. At fixed altitude, the receive-SNR threshold induces a horizontal feasible disk around each cluster head.
- A packet's AoI at mission completion includes the remaining collection and forwarding time in its cluster and all subsequent hovering and flight time through the UAV's return to the BS.

## Method

Each [[hovering-disk-data-collection|SNR-feasible disk]] is partitioned into `L_sub x L_sub` subregions and represented by candidate points, converting the continuous TSPN into a GTSP. The [[transformer-weighted-a-star-trajectory-planning|TWA-star]] pipeline then separates two decisions. A six-layer, eight-head [[transformer-encoder]] and autoregressive decoder produce a distribution over unvisited clusters and select a visiting order using greedy, sampling, or beam-search decoding. Given that order, weighted A-star searches a layered graph to select one candidate hovering point per cluster according to total AoI.

The Transformer is trained with REINFORCE using negative total AoI as reward. Sampled solutions are compared with a deterministic greedy rollout baseline, and the baseline is replaced only after a paired t-test indicates a significant improvement.

## Key findings

- Lemma 1 establishes that, under the fixed-height probabilistic LoS/NLoS average-channel model, points inside the derived disk meet the receive-SNR threshold and its boundary radius attains equality. This is a link-feasibility result, not an end-to-end optimality guarantee.
- The discretized problem is NP-hard. The stated complexities are `O((M+1)^2 d_em)` for the Transformer and approximately `O(M L_sub^2 log(M L_sub^2))` for min-heap weighted A-star.
- Training uses generated 10-cluster instances, embedding dimension 512, attention dimension 64, Adam learning rate `0.0001`, 200 epochs, 1000 steps per epoch, batch size 512, and `L_sub = 5`, giving 25 candidate points per disk. The implementation uses PyTorch 1.7 and Python 3.8 on one NVIDIA RTX 2080 Ti.
- Across the reported varying-cluster simulations, sampling-decoded TWA-star has the lowest total AoI among its greedy and beam variants, Ptr-A-star, a [[genetic-algorithm]], and simulated annealing.
- At `M = 45`, total AoI is 42,803 s for sampling, 43,971 s for beam, 46,118 s for greedy, 45,663 s for Ptr-A-star, 54,061 s for the genetic algorithm, and 59,537 s for simulated annealing. Sampling is best in this experiment; greedy does not outperform Ptr-A-star at this point.
- At `M = 20`, reported inference times are 2.3392 s for sampling, 2.4900 s for beam, 2.3037 s for greedy, 27.9023 s for Ptr-A-star, 163.41 s for the genetic algorithm, and 6.8623 s for simulated annealing. At `M = 45`, the corresponding times are 4.5112, 4.5190, 3.8995, 75.8817, 991.85, and 10.2019 s. Greedy is the fastest TWA-star decoder, while sampling gives lower AoI in the reported tests.

## Limitations / future work

The results are simulation-only. Candidate-point discretization has no stated error bound, and weighted A-star is not accompanied by admissibility, consistency, suboptimality, global-optimality, or convergence guarantees for the full pipeline. The policy is trained on 10-cluster instances and evaluated on instances from the same generated family; the varying-size experiment supports empirical generalization over cluster count, not robustness to distribution shift. The model assumes one UAV, one BS, fixed altitude and speed, straight fly-hover motion, pre-clustered devices, average channels, and no fast fading, inter-cluster-head interference, or packet errors beyond the SNR threshold. Multiple-UAV collection is left for future work.

## Relation to the corpus

This source combines [[age-of-information]], [[uav-data-collection]], and [[uav-trajectory-control]] through a distinct order-then-contact-point decomposition. It inherits the rotary-wing energy model and TSPN-style fly-hover perspective associated with [[zeng-2019-rotary-wing-energy-min]], but optimizes mission-completion AoI rather than energy. It complements [[guo-2026-aot-uav-inspection-offloading]], whose shared encoder and MLP heads jointly address inspection routing and offloading; Zhu et al. instead use a full autoregressive Transformer to order clusters and weighted A-star to select hovering points.

## Raw artifacts

- Parse: `raw/sources/UAV_Trajectory_Planning_for_AoI-Minimal_Data_Collection_in_UAV-Aided_IoT_Networks_by_Transformer/UAV_Trajectory_Planning_for_AoI-Minimal_Data_Collection_in_UAV-Aided_IoT_Networks_by_Transformer.md`
- Origin PDF: `raw/sources/UAV_Trajectory_Planning_for_AoI-Minimal_Data_Collection_in_UAV-Aided_IoT_Networks_by_Transformer/UAV_Trajectory_Planning_for_AoI-Minimal_Data_Collection_in_UAV-Aided_IoT_Networks_by_Transformer.pdf`
- Figures: `raw/sources/UAV_Trajectory_Planning_for_AoI-Minimal_Data_Collection_in_UAV-Aided_IoT_Networks_by_Transformer/images/`
