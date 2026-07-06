---
type: source
title: "Energy Consumption Minimization in STAR-RIS-Assisted UAV-MEC Networks With NOMA"
authors: ["Hamed Mohammadi", "Mahrokh G. Shayesteh", "Hashem Kalbkhani", "Azadeh Khazali"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3694177"
venue: "IEEE Transactions on Green Communications and Networking"
tags: [source, uav-mec, star-ris, noma, task-offloading, energy-minimization, trajectory-optimization, successive-convex-approximation]
related:
  - "[[star-ris]]"
  - "[[uav-mounted-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[noma]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[ji-2021-uav-mec-noma-oma-energy-min]]"
  - "[[shi-2026-aoi-active-ris-noma-agmec]]"
created: 2026-07-07
updated: 2026-07-07
---

# Energy Consumption Minimization in STAR-RIS-Assisted UAV-MEC Networks With NOMA

## Citation

Mohammadi, H., Shayesteh, M. G., Kalbkhani, H., & Khazali, A. (2026). *Energy Consumption Minimization in STAR-RIS-Assisted UAV-MEC Networks With NOMA*. **IEEE Transactions on Green Communications and Networking**. DOI: 10.1109/TGCN.2026.3694177.

## TL;DR

Proposes a two-tier UAV-terrestrial MEC framework where a UAV carries both an MEC server and a [[star-ris|STAR-RIS]]. Users partially process tasks locally and offload the rest through the UAV-mounted STAR-RIS: transmitted components go to the UAV-MEC server and reflected components go to a terrestrial BS-MEC server. The weighted energy-minimization problem jointly optimizes task-bit allocation, user transmit power, STAR-RIS phase shifts, and UAV trajectory under [[noma|NOMA]], using SCA/MRT subproblem solutions inside a BCD iterative algorithm.

## Problem framing

UAV-MEC extends coverage but is constrained by battery and compute capacity. RIS improves propagation but conventional RIS only reflects; STAR-RIS can transmit and reflect, enabling users on different sides of the surface to access aerial and terrestrial MEC simultaneously. The paper targets the coupled energy cost across users, UAV, and BS under NOMA-based concurrent uplink offloading.

## System model

- Ground users, a terrestrial BS with MEC, and a UAV equipped with an MEC server and STAR-RIS.
- Users have fixed-size computation tasks over a mission time divided into slots.
- Each task may be split across local processing, UAV-MEC processing, and BS-MEC processing.
- The STAR-RIS operates in mode-switching protocol, with some elements transmitting to the UAV and some reflecting to the BS.
- NOMA with SIC is used for simultaneous user offloading; users are ranked by instantaneous channel gains for UAV and BS links.
- Direct user-to-BS links are assumed blocked, and the STAR-RIS provides the offloading paths.

## Method

The non-convex weighted energy minimization is decomposed into three subproblems:

- bit allocation and user transmit-power optimization;
- STAR-RIS transmission/reflection phase-shift design, using MRT-style closed-form phase expressions;
- UAV trajectory planning.

Each subproblem is handled with SCA or closed-form updates, then combined with a BCD outer loop. The parse states that the SCA inner layer is monotonic and the BCD outer loop converges to a stationary point, not a global optimum.

## Key findings

- The algorithm's total energy decreases and stabilizes after about 3-4 iterations in the reported simulation settings.
- Under the parse's baseline setting, NOMA gives 21.71 J total energy versus 23.87 J for OMA, a 9.95% reduction.
- As STAR-RIS element count increases, the proposed NOMA scheme's advantage over OMA grows; the parse reports a 6.19% energy reduction at 30 elements and 16.42% at 80 elements.
- Compared with a grid-search benchmark over a tractable range, the iterative method stays within about a 2-3% energy gap while avoiding the grid search's combinatorial cost.

## Limitations / future work

The solution is locally optimal. The model assumes centralized decision-making at the BS and needs user positions, task sizes, and CSI for the relevant STAR-RIS/UAV/BS links. It uses simulation rather than hardware validation; the parse discusses imperfect CSI as a comparative scheme but the primary optimization still relies on available channel information.

## Relation to the corpus

This page extends the RIS/NOMA energy-minimization thread from [[ji-2021-uav-mec-noma-oma-energy-min]] and [[shi-2026-aoi-active-ris-noma-agmec]] into UAV-mounted STAR-RIS. Its result contrasts with [[ji-2021-uav-mec-noma-oma-energy-min]]: here NOMA beats OMA under the STAR-RIS aerial-terrestrial offloading architecture, whereas Ji et al. report OMA lower-energy in their UAV-MEC setting.

## Raw artifacts

- Parse: `raw/sources/Energy Consumption Minimization in STAR-RIS-Assisted UAV-MEC Networks With NOMA/Energy Consumption Minimization in STAR-RIS-Assisted UAV-MEC Networks With NOMA.md`
- Origin PDF: `raw/sources/Energy Consumption Minimization in STAR-RIS-Assisted UAV-MEC Networks With NOMA/Energy Consumption Minimization in STAR-RIS-Assisted UAV-MEC Networks With NOMA.pdf`
- Figures: `raw/sources/Energy Consumption Minimization in STAR-RIS-Assisted UAV-MEC Networks With NOMA/images/`
