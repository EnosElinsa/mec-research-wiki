---
type: concept
title: "Drone-Cell 3-D Placement"
tags: [aerial-base-station, drone-cell, deployment, air-to-ground, coverage]
related:
  - "[[air-to-ground-channel-model]]"
  - "[[al-hourani-2014-optimal-lap-altitude]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[mixed-integer-nonlinear-programming]]"
  - "[[cellular-connected-uav]]"
  - "[[bor-yaliniz-2016-3d-abs-placement]]"
  - "[[li-2026-uav-bs-semantic-mfmaddpg-kde]]"
created: 2026-06-01
updated: 2026-07-07
---

# Drone-Cell 3-D Placement

The deployment problem of choosing **where to put a low-altitude UAV-mounted aerial base station (ABS, "drone-cell")** in three dimensions — its **altitude** plus its **horizontal location and coverage-area size** — to maximize a coverage/revenue objective (typically the number of ground users served above a QoS threshold).

What makes it genuinely 3-D, rather than a terrestrial-BS siting problem, is the **air-to-ground channel**: the line-of-sight probability (and hence path loss) is a function of the **elevation angle** $\arctan(h/r)$, so raising the drone-cell improves LoS to distant users but increases free-space loss to nearby ones. Altitude and horizontal coverage are therefore coupled, and the optimal placement is **not** simply "hover directly above the densest cluster" — it depends on the environment (suburban / urban / dense-urban / high-rise) through the channel constants.

The canonical formulation in this wiki is [[bor-yaliniz-2016-3d-abs-placement]], which casts revenue-maximizing 3-D placement as a quadratically-constrained [[mixed-integer-nonlinear-programming|MINLP]], introduces an altitude-to-coverage-radius variable solvable by 1-D bisection, and solves the residual with an interior-point solver. The underlying urban LoS-probability channel comes from [[al-hourani-2014-optimal-lap-altitude]] (see [[air-to-ground-channel-model]]). The problem differs from clustering-based multi-UAV siting like [[weighted-kmeans-uav-deployment]] (which partitions users among several UAVs) and from [[cellular-connected-uav]] (UAV as a *user* of the cellular network, not a base station).

[[li-2026-uav-bs-semantic-mfmaddpg-kde]] adds the semantic-communication variant: UAV-BSs are still placed in 3-D, but the objective is BLEU-derived semantic fidelity under SINR and interference constraints rather than coverage count or bit throughput.
