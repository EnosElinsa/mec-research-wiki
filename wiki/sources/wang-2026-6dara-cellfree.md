---
type: source
modeling_card: required
title: "Two-Timescale Optimization for Aerial Rotatable Antenna Array in Cell-Free Networks With Dynamic Users"
authors: ["Wen Wang", "Yongming Huang", "Wanli Ni", "Cheng Zhang", "Dongming Wang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3668103"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 13181-13198"
tags: [source, cell-free-mimo, aerial-access-point, rotatable-antenna-array, two-timescale-optimization, team-mmse, potential-game, mappo]
related:
  - "[[liu-2026-passive-6dma]]"
  - "[[passive-six-dimensional-movable-antenna]]"
  - "[[six-dimensional-aerial-rotatable-antenna-array]]"
  - "[[team-mmse-receive-combining]]"
  - "[[aerial-terrestrial-cell-free-massive-mimo]]"
  - "[[two-timescale-optimization]]"
  - "[[csi-estimation-error]]"
  - "[[potential-game]]"
  - "[[nash-equilibrium]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[beta-policy-drl]]"
  - "[[jains-fairness-index]]"
  - "[[hong-2026-beam-delay-alignment]]"
  - "[[fang-2026-cellfree-uav-predictive-beamforming]]"
  - "[[wideband-asynchronous-cell-free-massive-mimo]]"
  - "[[mobility-asynchrony-and-geometry-in-aerial-coverage]]"
  - "[[yongming-huang]]"
  - "[[dongming-wang]]"
created: 2026-07-14
updated: 2026-07-16
---

# Two-Timescale Optimization for Aerial Rotatable Antenna Array in Cell-Free Networks With Dynamic Users

## Citation

Wang, W., Huang, Y., Ni, W., Zhang, C., & Wang, D. (2026). *Two-Timescale Optimization for Aerial Rotatable Antenna Array in Cell-Free Networks With Dynamic Users*. **IEEE Transactions on Wireless Communications, 25**, 13181-13198. DOI: 10.1109/TWC.2026.3668103.

## TL;DR

Combines whole-UAV 3D movement with three-axis rigid-array rotation in user-centric cell-free uplink networks. Frame-level association and 6D geometry use a potential game plus Beta/attention MAPPO, while slot-level distributed combining uses team-MMSE.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Dynamic uplink users are jointly served by distributed aerial access points, each carrying a rigid antenna array whose UAV position and three-axis orientation can change once per frame. User clustering and six-dimensional array geometry operate at the large timescale, while distributed receive combining adapts to imperfect local CSI in each slot.

**Problem & objective**: Problem (19) is an uplink-sum-rate MINLP that maximizes $\max_{\Omega}\frac{1}{N}\sum_{n=1}^{N}R_{\mathrm{Slot}}[\tau,n]$ over clustering, UAV positions, array rotations, and receive combiners.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| User clustering | $\eta_{m,k}[\tau]$ | binary | Whether aerial array $m$ serves user $k$ in frame $\tau$ |
| UAV position | $\mathbf q_m[\tau]$ | continuous 3-D position | Large-timescale aerial access-point location |
| Array rotation | $\boldsymbol\phi_m[\tau]$ | continuous, $[0,2\pi)^3$ | Three-axis rigid-array orientation |
| Receive combiner | $\mathbf w_{m,k}[\tau,n]$ | complex continuous vector | Small-timescale local combiner for user $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 19b | Clustering is binary, $\eta_{m,k}[\tau]\in\{0,1\}$ |
| 19c | Each array serves at most $\eta_{\max}$ users |
| 19d | Every user is served by at least one aerial array |
| 19e | Served users remain in the array's forward radiation hemisphere |
| 19f, 3-5 | Rotation, position, speed, and collision-avoidance limits are satisfied |

**Algorithm**: Compute slot-level team-MMSE combiners from local instantaneous and statistical CSI → update user clustering with the M-CSAP exact-potential game → control UAV velocity and three rotation angles with attention-based Beta-policy MAPPO → feed frame-averaged rates back to the next large-timescale update.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied aerial rotatable antenna arrays in user-centric cell-free uplink networks with dynamic users. They formulated a two-timescale MINLP that maximizes average uplink sum rate by jointly optimizing user clustering, UAV positions, three-axis array rotations, and receive combiners. The small-timescale block uses team-MMSE combining based on local instantaneous and statistical CSI. At the large timescale, M-CSAP solves an exact-potential clustering game and AB-MAPPO controls three-dimensional UAV velocities and array rotations. Simulations report higher sum rate than the evaluated fixed-geometry, centralized-combining, clustering, and policy variants under the tested user-density and mobility settings.

## Method and guarantee scope

[[team-mmse-receive-combining]] is team-optimal only for fixed association/geometry under local instantaneous and cross-node statistical CSI. The local altruistic association game is proved an exact potential game, guaranteeing at least one pure Nash equilibrium but not social/global optimality. Concurrent spatial adaptive play is argued to inherit convergence; its greedy non-neighbor set is maximal rather than proved maximum.

AB-MAPPO controls 3D velocities and three rotation angles under CTDE. Its constraint handling, convergence, scalability, and generalization are empirical, not guaranteed.

## Findings

Simulation reports the full TMMSE/M-CSAP/AB-MAPPO stack as highest-rate among tested variants. Joint position/rotation helps most at low altitude and under denser/higher-mobility settings; modest parameter-shift tests retain 92.8%-100% of matched-training sum rate. These are model-specific simulation results.

## Limitations

No UAV/gimbal prototype, calibration study, actuation latency, fronthaul implementation, or payload/energy evaluation. Reward penalties do not guarantee collision or forward-hemisphere constraints. Team/game guarantees rely on fixed geometry, distributed information, symmetric neighborhoods, and local influence. Statistical CSI acquisition overhead is proposed but not evaluated.

## Relation to the corpus

This source adds physical orientation control to [[aerial-terrestrial-cell-free-massive-mimo]] through [[six-dimensional-aerial-rotatable-antenna-array]], while [[team-mmse-receive-combining]] handles the faster receive block. Its [[potential-game]] association and [[mappo]] geometry policy illustrate a two-timescale split between analytical distributed signal processing, game-based clustering, and learned aerial control.

## Raw artifacts

- Parse: `raw/sources/Two-Timescale_Optimization_for_Aerial_Rotatable_Antenna_Array_in_Cell-Free_Networks_With_Dynamic_Users/Two-Timescale_Optimization_for_Aerial_Rotatable_Antenna_Array_in_Cell-Free_Networks_With_Dynamic_Users.md`
- Original PDF and extracted figures are in the same folder.
