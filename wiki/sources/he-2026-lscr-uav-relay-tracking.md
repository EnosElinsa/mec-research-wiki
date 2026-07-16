---
type: source
title: "A Collaborative Relay Tracking Method Incorporating Larger-Scale Spatial Context for UAVs"
authors: ["Yongxiang He", "Zhao Zhang", "Jianjun Ma", "Peng Leng", "Hongwu Guo"]
year: 2026
url: "https://doi.org/10.1109/TITS.2026.3677037"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
modeling_card: required
tags: [source, uav-tracking, cooperative-perception, graph-neural-network, target-handover, intelligent-transportation]
related:
  - "[[target-graph-representation]]"
  - "[[graph-neural-network]]"
  - "[[cooperative-perception]]"
  - "[[uav-enabled-its]]"
  - "[[zhu-2026-hab-mappo-target-search]]"
  - "[[zhao-2025-networked-isac-uav-handover]]"
created: 2026-07-10
updated: 2026-07-16
---

# A Collaborative Relay Tracking Method Incorporating Larger-Scale Spatial Context for UAVs

## Citation

He, Y., Zhang, Z., Ma, J., Leng, P., & Guo, H. (2026). *A Collaborative Relay Tracking Method Incorporating Larger-Scale Spatial Context for UAVs*. **IEEE Transactions on Intelligent Transportation Systems**, 27(6), 6399-6410. DOI: 10.1109/TITS.2026.3677037.

## TL;DR

Converts multi-UAV target handover into graph similarity matching. LSCR builds Delaunay-triangulation target graphs around a tracked object, extracts target graph representation (TGR) features with a lightweight graph representation convolutional network, and uses a Twin-GRCN model to match targets across UAV viewpoints.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: One UAV hands a tracked ground target to a second UAV in a dense scene with an overlapping field of view. The first UAV sends pixel coordinates for the designated target and its neighbors, while the second UAV forms candidate graphs without requiring geodetic localization or image-crop transfer.

**Problem & objective**: Select the handover target with the highest cross-view same-source probability, $B^*=\arg\max_{B_j\in\mathcal C}P_j(A_0=B_j\mid O_1^{A_0},O_2^{B_j})$, among candidates that pass the handover threshold and overlap-time test.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Candidate set | $\mathcal C$ | discrete target set | UAV2 targets whose same-source probability exceeds the threshold |
| Handover target | $B^*$ | discrete target choice | Highest-probability candidate selected for relay tracking |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | A candidate enters $\mathcal C$ only if $P_j>\delta$, with $\delta=0.5$ in the paper. |
| C2 | Exactly one candidate with the largest admissible probability is selected. |
| C3 | Direct handover requires sufficient overlapping depth: $\Delta R>v t_h$. |
| C4 | Graph comparison uses time-aligned cross-view observations of the designated target and detected candidates. |

**Algorithm**: Construct a Delaunay graph around each target from pixel coordinates, encode node and edge spatial context with the lightweight GRCN, and score cross-view graph pairs with Twin-GRCN. Filter probabilities at $\delta$, choose the maximum-scoring candidate, and accept direct handover only when the overlap depth supports the required handover time.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

He et al. [x] converted dense-scene relay target handover between UAVs into graph similarity matching. LSCR forms Delaunay target graphs, encodes larger-scale spatial context with GRCN, and selects the highest Twin-GRCN probability above 0.5 when the overlap region supports the handover time. On 8448 graph pairs, LSCR achieved 92.1% accuracy, 0.063 KB information transfer, a 20 KB model, and 966 FPS on a CPU. Siam-ResNet50 reached 92.6% accuracy but required a 97.8 MB model and 2 to 5 KB transfer, while LSCR distinguished close or visually similar targets without geodetic localization.

## Problem

Relay tracking is difficult when two UAVs observe dense target clusters from different viewpoints. Position-based handover relies on accurate geodetic localization, while appearance-based Siamese CNNs require image transfer and struggle when targets look similar. The paper asks whether larger-scale spatial context around the target can support handover with less communication and computation.

## System model

- UAV1 tracks a designated target and sends the pixel coordinates of that target and nearby targets to UAV2.
- UAV2 detects candidate targets in its field of view and constructs a graph for each candidate.
- The method does not require target localization under a geodetic coordinate system or transmission of target image crops.
- The evaluation dataset contains 8448 graph pairs, 112242 nodes, and 190172 edges, with about 13 nodes and 23 edges per pair on average.

## Method

- Uses Delaunay triangulation to define target-neighbor topology that is more stable under viewpoint changes.
- Defines [[target-graph-representation]] features by combining node information and inter-node distance-derived edge weights.
- Introduces a Graph Representation Convolutional Network (GRCN) that aggregates node and edge information into a graph-level embedding.
- Uses a Twin-GRCN similarity model to estimate whether two target graphs from different UAV viewpoints represent the same source target.

## Key findings

- LSCR reports 92.1% handover accuracy, 0.063 KB information transmission, a 20 KB model size, and 0.0010 s times N CPU matching time.
- The standalone Twin-GRCN evaluation reports 92.1% accuracy, MSE 0.063, 966 FPS, and 20 KB model size.
- Siam-ResNet50 is slightly more accurate at 92.6% but requires 97.8 MB model size and 2-5 KB information transfer; Siam-MobileNet reports 84.9% accuracy and 20.23 MB model size.
- The method distinguishes close or same-appearance targets better than pure position or appearance matching in the parsed qualitative examples.

## Limitations / future work

The reported validation is dataset-based rather than a deployed multi-UAV field experiment. The conclusion frames visible/infrared heterogeneous camera relay tracking as a future extension.

## Relation to the corpus

This is a UAV sensing and cooperative perception source adjacent to MEC. It gives the corpus a lightweight [[graph-neural-network]] example where the graph represents target spatial context rather than wireless resources or task DAGs. It also complements [[zhu-2026-hab-mappo-target-search]] and [[zhao-2025-networked-isac-uav-handover]] as a handover/tracking mechanism with explicit bandwidth and model-size constraints.

## Raw artifacts

- `raw/sources/A_Collaborative_Relay_Tracking_Method_Incorporating_Larger-Scale_Spatial_Context_for_UAVs/A_Collaborative_Relay_Tracking_Method_Incorporating_Larger-Scale_Spatial_Context_for_UAVs.md`
- `raw/sources/A_Collaborative_Relay_Tracking_Method_Incorporating_Larger-Scale_Spatial_Context_for_UAVs/A_Collaborative_Relay_Tracking_Method_Incorporating_Larger-Scale_Spatial_Context_for_UAVs.pdf`
- Extracted figures in `raw/sources/A_Collaborative_Relay_Tracking_Method_Incorporating_Larger-Scale_Spatial_Context_for_UAVs/images/`
