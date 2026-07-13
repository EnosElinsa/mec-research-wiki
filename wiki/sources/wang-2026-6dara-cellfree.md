---
type: source
title: "Two-Timescale Optimization for Aerial Rotatable Antenna Array in Cell-Free Networks With Dynamic Users"
authors: ["Wen Wang", "Yongming Huang", "Wanli Ni", "Cheng Zhang", "Dongming Wang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3668103"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 13181-13198"
tags: [source, cell-free-mimo, aerial-access-point, rotatable-antenna-array, two-timescale-optimization, team-mmse, potential-game, mappo]
related:
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
  - "[[yongming-huang]]"
created: 2026-07-14
updated: 2026-07-14
---

# Two-Timescale Optimization for Aerial Rotatable Antenna Array in Cell-Free Networks With Dynamic Users

## Citation

Wang, W., Huang, Y., Ni, W., Zhang, C., & Wang, D. (2026). *Two-Timescale Optimization for Aerial Rotatable Antenna Array in Cell-Free Networks With Dynamic Users*. **IEEE Transactions on Wireless Communications, 25**, 13181-13198. DOI: 10.1109/TWC.2026.3668103.

## TL;DR

Combines whole-UAV 3D movement with three-axis rigid-array rotation in user-centric cell-free uplink networks. Frame-level association and 6D geometry use a potential game plus Beta/attention MAPPO, while slot-level distributed combining uses team-MMSE.

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
