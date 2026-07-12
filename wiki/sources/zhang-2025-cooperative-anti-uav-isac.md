---
type: source
title: "Cooperative Beamforming Design for Anti-UAV ISAC Systems"
authors: ["Yue Zhang", "Hangguan Shan", "Yong Zhou", "Zhiguo Shi", "Li Sheng", "Yuanwei Liu"]
year: 2025
url: "https://doi.org/10.1109/TWC.2024.3519351"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, isac, anti-uav, cooperative-sensing, transceiver-beamforming, distributed-optimization, scnr]
related:
  - "[[cooperative-isac-transceiver-beamforming]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[networked-isac]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[second-order-cone-programming]]"
  - "[[wang-2026-stbc-cooperative-isac]]"
  - "[[tang-2025-cooperative-isac-lae]]"
  - "[[zhao-2025-networked-isac-uav-handover]]"
created: 2026-07-12
updated: 2026-07-12
---

# Cooperative Beamforming Design for Anti-UAV ISAC Systems

## Citation

Zhang, Y., Shan, H., Zhou, Y., Shi, Z., Sheng, L., & Liu, Y. (2025). *Cooperative Beamforming Design for Anti-UAV ISAC Systems*. **IEEE Transactions on Wireless Communications**, 24(3), 2249-2264. DOI: 10.1109/TWC.2024.3519351.

## TL;DR

Jointly designs transmit and receive beamformers for a multi-cell anti-UAV ISAC network. It maximizes UAV-sensing signal-to-clutter-plus-noise ratio (SCNR) under downlink SINR and per-BS power constraints, with a centralized AO/SCA/Dinkelbach solver and a primal-decomposition distributed solver that exchanges multipliers instead of global CSI.

## Problem

Small-UAV echoes compete with inter-cell interference, sensing/communication interference, clutter, residual self-interference, and downlink QoS requirements. Centralized multi-BS coordination can suppress these effects but requires heavy backhaul signaling and global CSI.

## System model

- `G` interconnected BSs jointly serve downlink users and sense one point-like UAV target.
- `Q` dual-functional BSs sense and communicate; the remaining BSs are communication-only.
- BS-1 receives monostatic and bistatic echoes from the cooperating sensing BSs.
- The objective maximizes sensing SCNR subject to minimum user SINR and per-BS transmit-power constraints.
- The channel model includes LoS sensing, clutter, residual self-interference, inter-cell interference, and AWGN.

## Method

Alternating optimization derives closed-form receive beamformers and iteratively updates transmit beamformers. Communication constraints become second-order-cone constraints; SCA lower-bounds the sensing numerator and Dinkelbach iteration handles the fractional objective. The distributed version introduces inter-cell-interference auxiliaries, applies primal decomposition, solves one convex secondary problem per BS, and updates shared variables with projected subgradients and exchanged Lagrange multipliers.

## Key findings

- The main setup uses four cells, two users per cell, 400 m adjacent-BS spacing, 30 m UAV height, 64 transmit and 64 receive antennas per BS, 28 GHz carrier frequency, 18 dBW BS power, and 500 Monte Carlo trials.
- Cooperative directional gain rises from 48.2 dB with one sensing BS to 52.7 dB with four sensing BSs.
- Centralized and distributed methods converge to the same modeled KKT solution; centralized convergence is faster, while the distributed method exchanges substantially fewer scalar values per subgradient iteration.
- For the reported `{G, K, Nt, Mr}` examples, centralized versus distributed-per-iteration signaling is 256 versus 8, 55,296 versus 96, and 2,752,512 versus 672 scalar values.
- Higher communication SINR requirements, more users/clutter, greater UAV height or distance, and larger cells reduce SCNR; more cooperating sensing BSs improve it.

## Limitations / parse caveats

The model assumes known UAV angles and sensing coefficients, LoS BS-UAV sensing links, local CSI, one point-like target, and a fixed simulated geometry. Distributed signaling is lower per subgradient iteration, not necessarily over the full run because it needs more iterations. The non-convex original problem is solved to a KKT point, not a proven global optimum. Most plotted SCNR values are figure-only and are not transcribed. The parse states DOI and publication dates; venue, volume, issue, and pages were verified against the DOI's Crossref record.

## Relation to the corpus

[[cooperative-isac-transceiver-beamforming]] adds interference- and clutter-aware physical-layer coordination to [[networked-isac]]. It differs from [[collaborative-beamforming]], whose current corpus meaning is a distributed virtual antenna array; here fixed cellular BSs coordinate ISAC transmit and receive beamformers. It complements the sensing fusion of [[tang-2025-cooperative-isac-lae]] and shared-resource echo separation of [[wang-2026-stbc-cooperative-isac]].

## Raw artifacts

- Parse: `raw/sources/Cooperative_Beamforming_Design_for_Anti-UAV_ISAC_Systems/Cooperative_Beamforming_Design_for_Anti-UAV_ISAC_Systems.md`
- Origin PDF: `raw/sources/Cooperative_Beamforming_Design_for_Anti-UAV_ISAC_Systems/Cooperative_Beamforming_Design_for_Anti-UAV_ISAC_Systems.pdf`
- Figures: `raw/sources/Cooperative_Beamforming_Design_for_Anti-UAV_ISAC_Systems/images/`
