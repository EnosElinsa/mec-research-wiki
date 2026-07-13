---
type: source
title: "Joint Optimization of UAV Deployment and Ground Users Clustering in Air-Ground Networks: A Hierarchical Coalition-Formation Game Approach"
authors: ["Haoran Du", "Runfeng Chen", "Tianyao Zhong", "Zhifeng Hou", "Yuli Zhang", "Dianxiong Liu", "Haichao Wang", "Yuhua Xu"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3610747"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, multi-uav, uav-deployment, coalition-formation, potential-game, device-to-device, user-clustering]
related:
  - "[[data-similarity-aware-coalition-formation]]"
  - "[[partial-space-adaptive-play]]"
  - "[[coalition-formation-game]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[device-to-device-communication]]"
  - "[[haichao-wang]]"
created: 2026-07-13
updated: 2026-07-14
---

# Joint Optimization of UAV Deployment and Ground Users Clustering in Air-Ground Networks: A Hierarchical Coalition-Formation Game Approach

## Citation

Du, H., Chen, R., Zhong, T., Hou, Z., Zhang, Y., Liu, D., Wang, H., & Xu, Y. (2026). *Joint Optimization of UAV Deployment and Ground Users Clustering in Air-Ground Networks: A Hierarchical Coalition-Formation Game Approach*. **IEEE Transactions on Green Communications and Networking**. DOI: 10.1109/TGCN.2025.3610747.

> **Metadata grounding note.** The parse omits final DOI, venue, and year. These fields were verified through the exact-title Crossref record; technical claims below remain parse-grounded.

## TL;DR

Nests ground-user coalition formation inside a discrete UAV-placement potential game. Covered users become coalition heads, cache shared requested data, and flood it over D2D links to uncovered users; partial-space adaptive play moves UAVs while a Pareto rule admits users whose data overlap and forwarding cost improve coalition utility.

## System model and objective

- Identical fixed-altitude UAV base stations and static users occupy a discretized 1 km square. UAV-ground links use probabilistic LoS/NLoS loss; D2D links use NLoS loss and Rayleigh fading.
- Orthogonal channel resources are assumed sufficient, so co-channel interference is ignored.
- A directly covered user may head a coalition, download the union of requested data, and disseminate it through multi-hop flooding. Download cost is shared according to overlapping item demand; forwarding cost depends on source, relay, and terminal roles.
- The objective maximizes summed user utility: successful data acquisition minus weighted download and forwarding overhead.

## Method

The inner [[data-similarity-aware-coalition-formation]] layer prioritizes uncovered users with few feasible heads. Users join coalitions by best response; a separate matching stage samples a free coalition and follows data-similarity preference lists before resource-constrained Pareto merge and exchange operations. Theorem 1 establishes existence of a stable partition through finite monotone improvements, but this is the paper's operation-specific stability rather than global coalition optimality, and a finite iteration cap can stop earlier.

The outer deployment layer treats total user utility as an exact potential and uses [[partial-space-adaptive-play]]: each iteration samples candidate UAV placements and selects by a softmax response. Its best-equilibrium claim is conditional on a sufficiently large learning factor and on each deployment producing a unique inner coalition result. The randomized inner algorithm can have multiple stable partitions, so that uniqueness assumption is not established. The paper explicitly acknowledges that the joint outcome need not be globally optimal.

## Key findings

- Simulations average **100 independent MATLAB experiments** with 3 UAVs, 20 users, 100 m altitude, 4.5 Mbit/s coverage threshold, and normalized shared-data/forwarding costs.
- Fig. 7 prints gains over traditional coalition formation of **0.1%, 0.7%, 1.9%, 6.7%, 9.6%, and 10.6%** for 12, 20, 28, 36, 44, and 52 users.
- Fig. 6 visually places the proposed utility near 11 early in training while the traditional coalition method approaches roughly 10.5 only near 3,000 iterations; these are plot-read estimates.
- The text around Fig. 10 reports that coalition benefits collapse as forwarding overhead rises; at 0.35, the proposed, sequential-coalition, and no-coalition methods coincide because coalitions shrink to one user.

## Limitations / interpretation

The study assumes static users, fixed UAV altitude, discrete placement, known positions and demand vectors, homogeneous radios, abundant orthogonal channels, and no interference. It omits UAV trajectories, propulsion/deployment energy, mobility, online demand uncertainty, and signaling overhead. Flooding is treated as reliable whenever pairwise rate exceeds a threshold, while its congestion and costs remain abstract normalized quantities.

The convergence plots do not measure Nash-deviation residuals, coalition-stability violations, or a global optimality gap. The outer proof assumes a unique inner outcome that the randomized coalition process does not guarantee. The parse also contains swapped rate indices, a displaced equation, an undefined “compliance is true” merge condition, a damaged softmax denominator, and inconsistent language between “best NE” and the acknowledged non-global joint result.

## Relation to the corpus

Unlike MEC-oriented [[coalition-formation-game]] sources, computation is absent here: the shared resource is requested content acquired by ground heads and forwarded over [[device-to-device-communication]]. The outer [[potential-game]] searches UAV placement while the inner coalition process determines the utility evaluated at each placement.

## Raw artifacts

- Parse: `raw/sources/Joint_Optimization_of_UAV_Deployment_and_Ground_Users_Clustering_in_Air-Ground_Networks_A_Hierarchical_Coalition-Formation_Game_Approach/Joint_Optimization_of_UAV_Deployment_and_Ground_Users_Clustering_in_Air-Ground_Networks_A_Hierarchical_Coalition-Formation_Game_Approach.md`
- Origin PDF and extracted figures (`images/`) in the same folder.
