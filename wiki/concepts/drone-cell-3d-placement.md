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
  - "[[zheng-2026-active-search-low-altitude-uav]]"
  - "[[equipotential-surface-uav-search]]"
  - "[[aerial-active-ris-backhaul]]"
  - "[[chakareski-2019-uav-mmwave-hetnet-ee]]"
  - "[[lin-2025-energy-effective-ris-multiuav-coverage]]"
  - "[[mozaffari-not-in-parse-3d-drone-cellular-network]]"
  - "[[belgiovine-not-in-parse-multidt-abs-deployment]]"
  - "[[multi-digital-twin-network-optimization]]"
created: 2026-06-01
updated: 2026-07-11
---

# Drone-Cell 3-D Placement

The deployment problem of choosing **where to put a low-altitude UAV-mounted aerial base station (ABS, "drone-cell")** in three dimensions — its **altitude** plus its **horizontal location and coverage-area size** — to maximize a coverage/revenue objective (typically the number of ground users served above a QoS threshold).

What makes it genuinely 3-D, rather than a terrestrial-BS siting problem, is the **air-to-ground channel**: the line-of-sight probability (and hence path loss) is a function of the **elevation angle** $\arctan(h/r)$, so raising the drone-cell improves LoS to distant users but increases free-space loss to nearby ones. Altitude and horizontal coverage are therefore coupled, and the optimal placement is **not** simply "hover directly above the densest cluster" — it depends on the environment (suburban / urban / dense-urban / high-rise) through the channel constants.

The canonical formulation in this wiki is [[bor-yaliniz-2016-3d-abs-placement]], which casts revenue-maximizing 3-D placement as a quadratically-constrained [[mixed-integer-nonlinear-programming|MINLP]], introduces an altitude-to-coverage-radius variable solvable by 1-D bisection, and solves the residual with an interior-point solver. The underlying urban LoS-probability channel comes from [[al-hourani-2014-optimal-lap-altitude]] (see [[air-to-ground-channel-model]]). The problem differs from clustering-based multi-UAV siting like [[weighted-kmeans-uav-deployment]] (which partitions users among several UAVs) and from [[cellular-connected-uav]] (UAV as a *user* of the cellular network, not a base station).

[[li-2026-uav-bs-semantic-mfmaddpg-kde]] adds the semantic-communication variant: UAV-BSs are still placed in 3-D, but the objective is BLEU-derived semantic fidelity under SINR and interference constraints rather than coverage count or bit throughput.

[[zheng-2026-active-search-low-altitude-uav]] adds an online low-altitude variant where the UAV does not know user positions or the urban channel map in advance. Its [[equipotential-surface-uav-search]] method keeps the placement search tied to both access quality and BS backhaul, rather than solving an offline placement problem over known ground terminals.

[[aerial-active-ris-backhaul]] is adjacent but not identical: the optimized aerial platform is an active RIS support for UAV-BS backhaul rather than the access drone-cell itself, so placement interacts with amplification power, phase control, and 3-D coverage of aerial receivers.

[[chakareski-2019-uav-mmwave-hetnet-ee]] is an early energy-efficiency instance: the UAV tier coexists with a microwave macro BS and mmWave SBSs, and the UAV coverage radius/altitude is tied to maximum path loss before radio resources are allocated. [[lin-2025-energy-effective-ris-multiuav-coverage]] is a RIS-assisted communications-coverage variant, where [[k-dbscan-uav-deployment]] bounds each UAV's movement region before TDQN trajectory/service control.

[[mozaffari-not-in-parse-3d-drone-cellular-network]] moves from a single drone-cell to a fully 3-D cellular lattice: truncated-octahedron cells place LAP drone-BSs, HAP drones provide FSO backhaul, and [[optimal-transport-theory]] assigns drone-UEs by total latency. [[belgiovine-not-in-parse-multidt-abs-deployment]] adds the ray-tracing digital-twin variant, where [[multi-digital-twin-network-optimization]] validates airborne-base-station placements under mobile UEs before deployment.
