---
type: source
title: "Joint Offloading, Trajectory and Deployment Optimization for Multi-UAV Cooperative Regional Search in SAGINs: A Hybrid DRL-GA Framework"
authors: ["Peng Zhao", "Hongbing Cheng", "Hangyu Zhang", "Zhiguo Wan"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3709181"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, sagin, search-and-rescue, task-offloading, uav-trajectory-control, soft-actor-critic, graph-neural-network, genetic-algorithm]
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[uav-trajectory-control]]"
  - "[[soft-actor-critic]]"
  - "[[graph-neural-network]]"
  - "[[genetic-algorithm]]"
  - "[[post-disaster-mec]]"
  - "[[gao-2024-sagin-perception-offloading]]"
  - "[[zhao-2025-probabilistic-semantic-sagin]]"
modeling_card: required
created: 2026-07-07
updated: 2026-07-16
---

# Joint Offloading, Trajectory and Deployment Optimization for Multi-UAV Cooperative Regional Search in SAGINs: A Hybrid DRL-GA Framework

## Citation

Zhao, P., Cheng, H., Zhang, H., & Wan, Z. (2026). *Joint Offloading, Trajectory and Deployment Optimization for Multi-UAV Cooperative Regional Search in SAGINs: A Hybrid DRL-GA Framework*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2026.3709181.

## TL;DR

Targets multi-UAV search and rescue in [[space-air-ground-integrated-network|SAGIN]] settings where wind, terrain, coverage, and heterogeneous offloading tiers interact. The paper decomposes the problem into online HCDRL control and low-frequency GA deployment search: an HCSAC policy uses CNN local perception plus GCN topology/offloading embeddings for trajectory and offloading, while a [[genetic-algorithm]] evaluates takeoff/recovery deployments through learned-policy rollouts. NOAA-derived GFS wind fields and uncertainty-aware terrain abstraction make the simulation less idealized than a static-grid UAV-MEC benchmark.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Multiple fixed-altitude UAVs search a gridded mountainous region and generate sensing tasks that can be processed locally or through BS, HAPS, LEO, edge, and cloud tiers in a SAGIN. Links use orthogonal subcarriers; channel coefficients combine antenna gain, free-space attenuation, atmospheric and rain loss, small-scale fading, and AWGN, while UAV motion is driven by terrain uncertainty and NOAA-derived wind fields.

**Problem & objective**: Coupled long-horizon MINLP with online offloading and trajectory control plus mission-level deployment search; the offloading model minimizes $\sum_{t=1}^{I} L(t)$, while the GA maximizes $w_c\bar C(\mathcal F)-w_e\bar E_{\mathrm{total}}(\mathcal F)-w_d\bar D_{\mathrm{lat}}(\mathcal F)$ to favor search coverage and penalize energy and latency.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Local processing indicator | $\alpha_u(t)$ | Binary, $\{0,1\}$ | Process UAV $u$'s task locally at time $t$ |
| Primary and secondary offloading indicators | $\beta_{u,i}(t),\gamma_{u,i,k}(t)$ | Binary, $\{0,1\}$ | Select a primary SAGIN server or a two-stage processing path |
| Trajectory action | $A_u^1(t)$ | Discrete direction in $\{0,\ldots,8\}$ | Move to an adjacent cell or issue the return action |
| Deployment chromosome | $\mathcal F$ | Discrete grid cells | Select every UAV's takeoff and recovery cells |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Exactly one execution mode is selected: $\alpha_u(t)+\sum_i\beta_{u,i}(t)+\sum_{i,k}e_{u,i}e_{i,k}\gamma_{u,i,k}(t)=1$ |
| C2 | Computation and channel allocations do not exceed the selected SAGIN nodes' available resources, as in (19a)-(19c) |
| C3 | Task latency satisfies $L_o^u(t)\le d_{c,u}(t)$ |
| C4 | Residual energy is protected by $E_u^{\mathrm{total}}(t)\le \mathrm{Battery}_u(t)-\xi\mathrm{Battery}_u$ |
| C5 | Trajectory actions remain inside the grid and respect terrain hazards and wind-adjusted motion feasibility |

**Algorithm**: Two-stage HCDRL plus GA, CNN local-map encoding and GCN SAGIN-topology encoding $\rightarrow$ parallel HCSAC policies for movement and offloading $\rightarrow$ policy rollouts for each deployment chromosome $\rightarrow$ GA selection, crossover, mutation, and elitism.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] studied joint task offloading, flight trajectory planning, and UAV deployment for multi-UAV search and rescue in SAGINs under terrain uncertainty and NOAA-derived wind fields. They formulated the mission as a multi-objective optimization that maximizes search coverage and minimizes task energy cost under resource, connectivity, latency, and battery constraints. They proposed a two-stage HCDRL and GA framework in which CNN and GCN encoders support HCSAC-based online trajectory and offloading decisions. The learned policy is then used as a rollout-based fitness evaluator for GA optimization of UAV takeoff and recovery positions. Simulations report mission-lifetime gains of up to 38%, search-coverage gains of 33% under strong wind, and a nearly 18% coverage lift from GA-optimized deployment.

## Problem framing

Search-and-rescue UAV fleets must cover uncertain terrain while conserving energy and selecting where computation runs. Fixed deployment, idealized channels, and no-wind simulations can misrepresent mountainous SAR missions: poor initial geometry becomes expensive under wind, offloading nodes differ across BS/HAPS/LEO/cloud tiers, and monolithic DRL over deployment, trajectory, and offloading suffers from a large hybrid action-state space.

## System model

- A 10 km x 10 km search region is discretized into a 20 x 20 grid; the default fleet has four UAVs at 200 m altitude, with 20 m/s flight speed and `3.6e5 J` battery capacity.
- UAVs sense grid cells with onboard cameras and generate computation tasks while communicating with a SAGIN support stack that includes BS, HAPS, LEO, and cloud/central-edge resources.
- The wind state comes from offline NOAA GFS records, cropped and interpolated into local wind-u/wind-v maps; the authors state this is simulation input, not a real-time weather-data pipeline.
- The optimization couples deployment/recovery positions, per-step trajectory decisions, offloading-tier choices, task-completion latency, search coverage, and energy cost.

## Method

- **HCDRL / HCSAC.** Soft Actor-Critic is wrapped in hybrid convolutional state encoding: each UAV receives a local three-channel map for uncertainty and wind, while GCN embeddings capture SAGIN topology and offloading connectivity.
- **Policy-in-the-loop GA.** A chromosome represents candidate takeoff/recovery configurations. Each candidate is scored through HCDRL rollouts with normalized coverage, energy, and task-completion latency terms.
- **Module separation.** GA handles mission-level deployment at low frequency, while HCDRL handles online trajectory and offloading; this avoids forcing all decisions into one monolithic distributed DRL policy.
- **Interpretability.** Offloading heatmaps and UAV visit-frequency maps are used to inspect tier preference and emergent spatial partitioning.

## Key findings

- The full GA-HCSAC variant reports the best lifetime and coverage under low, moderate, and strong wind. Under strong wind, it reaches `38.47 +/- 1.19` minutes and `62.77 +/- 2.01%` coverage, versus `31.65 +/- 1.23` minutes and `53.20 +/- 1.97%` coverage without GA.
- Removing both offloading and GA gives the largest strong-wind drop: `27.85 +/- 0.99` minutes and `47.20 +/- 1.60%` coverage.
- The authors report that the full model extends mission lifetime by up to 38% and coverage by 33% under strong wind versus standard baselines; the GA deployment module alone contributes a nearly 18% strong-wind coverage lift.
- Standard DRL variants scale poorly in the preliminary no-wind comparison, while HCDRL remains trainable up to the tested six-UAV case.
- Training 1000 episodes takes 1.41 hours on the reported RTX 3060 / R7 5800H setup; forward inference latency is 8.96 ms per decision step at batch size 1.

## Limitations / future work

The validation is simulation-only. NOAA-derived wind fields improve environmental realism, but the paper does not test real UAV hardware, onboard processors, wireless-link instability, sensor delays, online environment updates, communication holes, or post-failure recovery. Scalability evidence covers one to six UAVs only. The GA module returns one weighted-sum deployment configuration rather than a Pareto front; the authors name NSGA-II-style Pareto variants, field validation, larger deployments, connectivity-aware offloading, and efficient GA replanning as future work.

## Relation to the corpus

This source strengthens the [[space-air-ground-integrated-network]] line from a SAR / deployment angle. Compared with [[gao-2024-sagin-perception-offloading]], it models wind-terrain search and deployment optimization rather than perception-aided queue-stable task hosting. It also connects to [[post-disaster-mec]] because the SAR setting shares weak-infrastructure and emergency-response assumptions, but its main architectural home is SAGIN. Methodologically, it adds a [[genetic-algorithm]] deployment layer on top of [[soft-actor-critic]], [[graph-neural-network]], and [[uav-trajectory-control]].

## Raw artifacts

- `raw/sources/Joint_Offloading_Trajectory_and_Deployment_Optimization_for_Multi-UAV_Cooperative_Regional_Search_in_SAGINs_A_Hybrid_DRL-GA_Framework/Joint_Offloading_Trajectory_and_Deployment_Optimization_for_Multi-UAV_Cooperative_Regional_Search_in_SAGINs_A_Hybrid_DRL-GA_Framework.md`
- Original PDF and extracted figures (`images/`) in the same folder.
