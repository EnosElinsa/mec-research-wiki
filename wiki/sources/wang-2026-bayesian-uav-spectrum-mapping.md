---
type: source
modeling_card: required
title: "Bayesian Learning-Based Spectrum Mapping With UAV Path Dynamic Optimization Under 3-D Unknown Environments"
authors: ["Jie Wang", "Qiuming Zhu", "Yuanjin Zheng", "Zhipeng Lin", "Qihui Wu", "Kai-Kuang Ma", "Qianhao Gao", "Yiran Chen"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3694148"
venue: ""
tags: [source, spectrum-mapping, radio-map, sparse-bayesian-learning, uav-trajectory-control, information-gathering]
related:
  - "[[information-driven-uav-spectrum-mapping]]"
  - "[[temporal-spectrum-cartography]]"
  - "[[radio-map-assisted-channel-estimation]]"
  - "[[spectrum-sensing-channel-selection]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[blockage-aware-channel-model]]"
  - "[[qihui-wu]]"
  - "[[qiuming-zhu]]"
created: 2026-07-11
updated: 2026-07-16
---

# Bayesian Learning-Based Spectrum Mapping With UAV Path Dynamic Optimization Under 3-D Unknown Environments

## Citation

Wang, J., Zhu, Q., Zheng, Y., Lin, Z., Wu, Q., Ma, K.-K., Gao, Q., & Chen, Y. (2026). *Bayesian Learning-Based Spectrum Mapping With UAV Path Dynamic Optimization Under 3-D Unknown Environments*. DOI: 10.1109/TWC.2026.3694148. The local parse exposes the DOI line but not a reliable venue banner, so the venue field is left blank.

## TL;DR

Constructs 3-D radio environment maps from sparse UAV spectrum measurements in unknown environments. The framework couples an information-driven RRT* sampler (3DIG-RRT*) with sparse Bayesian dictionary learning plus Gaussian-process refinement (SBDL-GP), so the UAV samples informative regions while the recovery model adapts the channel dictionary to measured shadowing and path-loss behavior.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A spectrum-sensing UAV traverses an unknown three-dimensional region partitioned into RSS cubes. Sparse measurements update a close-in air-to-ground channel dictionary and a Gaussian-process shadowing model while an online planner selects collision-free samples within mission time and energy budgets.

**Problem & objective**: Equation (17) is an NP-hard informative path-planning problem that selects $\mathcal G_I=\arg\max_{\mathcal G\in\mathcal R}I(\mathcal G)$ to maximize mutual information and reconstruct the radio environment map from as few sampled cubes as possible.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Sampling path | $\mathcal G$ | discrete waypoint sequence | Candidate UAV path through the 3-D cube grid |
| Waypoint | $\mathbf w_g$ | continuous/discretized 3-D position | Control and measurement location on the path |
| Sparse emitter vector | $\boldsymbol\omega$ | continuous sparse vector | Latent emitter coefficients recovered from measurements |
| Channel dictionary | $\boldsymbol\Phi$ | continuous matrix | Propagation atoms refined from sampled data |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Path cost satisfies the mission budget, $C(\mathcal G)\le B$ |
| C2 | Waypoints and connecting segments remain in collision-free space |
| C3 | RRT* steering obeys UAV motion and sampling-distance limits |
| C4 | Receding-horizon replanning occurs after each $m_{\mathrm{up}}$ measurements |
| C5 | Sampled RSS values, sparse coefficients, and dictionary updates remain consistent with the recovery model |

**Algorithm**: Initialize the channel dictionary and REM uncertainty → grow 3DIG-RRT* using mutual-information utility → execute the first receding-horizon waypoints and collect RSS → estimate sparse emitters with SBL → refine dictionary atoms with K-SVD and shadowing with Gaussian processes → reconstruct the REM and replan.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied UAV-assisted three-dimensional spectrum mapping in unknown environments with sparse measurements. They formulated an NP-hard sampling-path problem that maximizes mutual information under path-cost, collision, and UAV-motion constraints. The proposed 3DIG-RRT* planner selects informative waypoints and periodically replans as new measurements arrive. SBDL-GP then combines sparse Bayesian learning, K-SVD dictionary refinement, and Gaussian-process shadowing estimation to reconstruct the radio environment map. Simulations and measurements report lower mapping error than the evaluated compressed-sensing and interpolation methods and higher sampling efficiency than the compared trajectory planners.

## Problem

Spectrum mapping normally assumes fixed sensors, vehicle-mounted sensors, known emitter information, or a pre-matched channel model. In unknown 3-D environments those assumptions break: the UAV must decide where to sense, and the reconstruction method must infer unsampled RSS values despite sparse samples, buildings, shadow fading, and unknown emitter/channel structure.

## System model

- The region of interest is discretized into 3-D cubes with RSS values to be recovered.
- A UAV carries spectrum monitoring, air-to-ground communication, and RTK modules; the current measured-system note says dynamic trajectory adjustment is not yet supported, so a predefined flight path is used for the measured dataset.
- The spectrum field is represented through a sparse emitter vector, a semi-deterministic path-loss dictionary, and shadow-fading components.
- The planner chooses UAV waypoints under obstacle, distance, and sampling-budget feasibility while maximizing information gain.

## Method

The proposed pipeline has two coupled blocks. First, 3DIG-RRT* searches feasible 3-D paths with a mutual-information utility from recent measurements and predicted uncertainty. Second, SBDL-GP estimates the sparse emitter signal with sparse Bayesian learning, refines dictionary atoms with K-SVD-style dictionary learning, and applies Gaussian process regression to shadow fading before reconstructing the REM.

## Key findings

- In the abstract and conclusions, SBDL-GP reduces MAE by more than 60% over compressed-sensing methods and by about 35% over data-driven interpolation.
- At 0.3% sampling, it reports up to 74% lower MAE than Lasso/OMP and 44% improvement over Kriging/KNN.
- 3DIG-RRT* improves sampling efficiency by up to 70%; the ROI-driven planner has 25-30% higher MAE than 3DIG-RRT* in the reported comparison.
- In the SNR test at 0.5% sampling, dropping SNR from 30 dB to 10 dB increases SBDL-GP MAE by 7.8%, while Kriging increases by 91%.
- Runtime remains seconds-scale in the reported table: at 0.5% sampling, SBDL-GP takes 1.748 s versus 0.954 s for SBL-GP, 0.287 s for Kriging, 4.08 s for Lasso, 0.0048 s for OMP, and 0.215 s for KNN.
- The measured ROI is 117 m by 97 m with four emitters transmitting at 0 dBm and 1 GHz.

## Limitations / parse caveats

The parse lacks a full publication header beyond the DOI line. Equations and tables contain OCR spacing artifacts, and several quantitative comparisons are figure-supported rather than table-supported. The page therefore records only values that appear in stable prose or parsed tables. The measured system verifies the mapping pipeline but uses a predefined flight path rather than the proposed dynamic online trajectory update.

## Relation to the corpus

This source is a spectrum-mapping and UAV-sensing entry rather than MEC offloading. It extends [[temporal-spectrum-cartography]] from low-altitude RF-map reconstruction into 3-D unknown-environment REM construction, complements [[radio-map-assisted-channel-estimation]] by treating the radio map itself as the reconstructed object, and adds [[information-driven-uav-spectrum-mapping]] as a reusable active-sampling pattern.

## Raw artifacts

- `raw/sources/Bayesian_Learning-Based_Spectrum_Mapping_With_UAV_Path_Dynamic_Optimization_Under_3-D_Unknown_Environments/Bayesian_Learning-Based_Spectrum_Mapping_With_UAV_Path_Dynamic_Optimization_Under_3-D_Unknown_Environments.md`
- Original PDF and extracted figures (`images/`) in the same folder.
