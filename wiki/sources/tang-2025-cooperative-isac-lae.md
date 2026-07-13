---
type: source
title: "Cooperative ISAC-Empowered Low-Altitude Economy"
authors: ["Jun Tang", "Yiming Yu", "Cunhua Pan", "Hong Ren", "Dongming Wang", "Jiangzhou Wang", "Xiaohu You"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3542399"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, integrated-sensing-and-communication, low-altitude-intelligent-network, wireless-perception, cooperative-sensing, tensor-decomposition, data-fusion]
related:
  - "[[integrated-sensing-and-communication]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[wireless-perception]]"
  - "[[jiang-2025-isac-lae-overview]]"
  - "[[meng-2024-uav-isac-overview]]"
  - "[[zhu-2024-sensing-comm-doppler-uav-swarm]]"
  - "[[su-2024-sensing-aided-isac-pls]]"
  - "[[zhu-2024-crb-active-ris-isac]]"
  - "[[cunhua-pan]]"
created: 2026-07-06
updated: 2026-07-13
---

# Cooperative ISAC-Empowered Low-Altitude Economy

## Citation

Tang, J., Yu, Y., Pan, C., Ren, H., Wang, D., Wang, J., & You, X. (2025). *Cooperative ISAC-Empowered Low-Altitude Economy*. **IEEE Transactions on Wireless Communications**, 24(5), 3837-3853. DOI: 10.1109/TWC.2025.3542399.

## TL;DR

Develops a cooperative ISAC sensing scheme for low-altitude UAV parameter estimation. Each base station first performs monostatic parameter estimation with a tensor-decomposition model; then multiple base stations fuse their estimates through false-removing MST association, Pareto-optimal position fusion, and residual-weighted velocity estimation. The scheme is also extended to a dual-polarized tensor model.

## Problem framing

Low-altitude economy systems need base stations to communicate with UAVs and also sense UAV positions and velocities for safety, intrusion detection, and collision prevention. A single monostatic base station can suffer from path loss, blockage, and incomplete velocity information because it only observes radial velocity. Cooperative ISAC uses multiple base stations to improve sensing coverage and recover richer 3D flight status, but multi-target multi-BS sensing requires parameter estimation, cross-BS data association, and position/velocity fusion.

## System model

- Multiple multi-antenna base stations sense multiple low-altitude UAVs.
- Each base station uses a MIMO-OFDM framework with partially connected hybrid beamforming.
- Base stations operate over non-overlapping frequency bands to avoid inter-BS sensing interference.
- The sensing channel assumes LoS paths between base stations and UAVs, and weak reflections from other scatterers.
- A cloud fusion stage combines per-BS range, AoA, radial-velocity, and channel-coefficient estimates.

## Method

- Formulates monostatic parameter estimation as a tensor decomposition problem.
- Uses the Vandermonde structure of factor matrices and spatial smoothing tensor decomposition to estimate UAV AoAs, ranges, radial velocities, and channel coefficients.
- Adds a reduced-dimensional AoA estimator based on a generalized Rayleigh quotient to reduce complexity.
- Uses a false-removing minimum-spanning-tree data-association method to match per-BS estimates belonging to the same UAV.
- Applies Pareto optimality for position estimation and residual weighting for true-velocity estimation.
- Extends the tensor model to a dual-polarized system through a fourth-order tensor formulation.

## Key findings

- The proposed tensor-decomposition estimator lowers AoA, range, radial-velocity, and position RMSE as transmit power increases, while the MUSIC/FFT benchmark encounters a performance bottleneck.
- The dual-polarized extension improves position estimation when array size is limited.
- The tensor-decomposition scheme has lower monostatic parameter-estimation CPU time than the MUSIC/FFT benchmark because the GRQ-based AoA estimator avoids a 2D search.
- Cooperative position and velocity estimation improve as the number of base stations increases.
- Pareto position fusion improves over mean fusion, and residual-weighted velocity estimation improves over plain WLS.
- In the degraded single-antenna scenario, the proposed fusion scheme gives better position estimation than the benchmark fusion scheme and comparable velocity estimation.

## Limitations / future work

The model assumes LoS sensing paths, non-overlapping base-station frequency bands, and simulation-based evaluation. The parse does not state a separate future-work section.

## Relation to the corpus

This is a physical-layer [[integrated-sensing-and-communication]] source for the [[low-altitude-intelligent-network]] track. It complements [[jiang-2025-isac-lae-overview]] and [[meng-2024-uav-isac-overview]] by providing a detailed cooperative multi-BS sensing algorithm rather than a survey-level architecture. It is adjacent to [[zhu-2024-sensing-comm-doppler-uav-swarm]] and [[su-2024-sensing-aided-isac-pls]] because all treat sensing accuracy as a first-class design object, though this paper focuses on cooperative parameter estimation and data fusion rather than MEC offloading or secrecy.

## Raw artifacts

- `raw/sources/Cooperative ISAC-Empowered Low-Altitude Economy/Cooperative ISAC-Empowered Low-Altitude Economy.md`
- Original PDF and extracted figures (`images/`) in the same folder.
