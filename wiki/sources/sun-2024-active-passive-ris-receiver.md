---
type: source
title: "Active-Passive Cascaded RIS-Aided Receiver Design for Jamming Nulling and Signal Enhancing"
authors: ["Yifu Sun", "Yonggang Zhu", "Kang An", "Zhi Lin", "Cheng Li", "Derrick Wing Kwan Ng", "Jiangzhou Wang"]
year: 2024
url: "https://doi.org/10.1109/TWC.2023.3325813"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, reconfigurable-intelligent-surface, anti-jamming, receiver-architecture, robust-beamforming, csi-uncertainty, physical-layer-security]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[active-ris]]"
  - "[[anti-jamming-mec]]"
  - "[[physical-layer-security]]"
  - "[[csi-estimation-error]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[sun-2024-mfris-semantic-antijamming]]"
created: 2026-05-31
updated: 2026-05-31
---

# Active-Passive Cascaded RIS-Aided Receiver Design for Jamming Nulling and Signal Enhancing

## Citation

Sun, Y., Zhu, Y., An, K., Lin, Z., Li, C., Ng, D. W. K., & Wang, J. (2024). *Active-Passive Cascaded RIS-Aided Receiver Design for Jamming Nulling and Signal Enhancing*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2023.3325813.

## TL;DR

Proposes an **active-passive cascaded [[intelligent-reflecting-surface|RIS]]-aided receiver architecture** so that a large-scale antenna array can be deployed cheaply at the user side for anti-jamming communications. A passive RIS layer (N_P units) is cascaded with an [[active-ris|active RIS]] layer (N_A units), stacked in front of the receive antennas. Under imperfect (angular) jammer CSI, the paper formulates a **worst-case achievable-rate maximization** problem and solves the non-convex/NP-hard design with a low-complexity framework yielding semi-closed-form solutions. The authors state this is the first work to exploit an active-passive cascaded RIS at the user side for receiver design.

## Problem framing

Massive-MIMO anti-jamming works well but deploying hundreds of antennas at a user is impractical (hardware cost, power). A passive-RIS reflector suffers severe path loss; an active-RIS reflector amplifies the signal but injects dynamic noise and consumes large power at the user. The paper seeks a cost- and energy-efficient receiver that combines both, while remaining robust to **imperfect angular CSI** of the jammers ([[csi-estimation-error]]) and avoiding the high complexity and FPGA-unfriendliness of CVX/SDR-based robust solvers.

## System model

- **Actors.** A base station (transmit precoder, general power constraints), the user equipped with the cascaded RIS receiver, and M jammers (the simulations use M = 2) with imperfect angular CSI.
- **Architecture.** Passive RIS (N_P units, phase-only) cascaded with active RIS (N_A units, phase + amplitude) vertically stacked before the Rx antennas; a digital decoder follows.
- **Performance analysis.** Derives a power-scaling law: the proposed architecture's receive power and asymptotic SINR scale as N_A^2·N_P^2 and N_A·N_P respectively, versus (N_P + N_A)^2 and (N_P + N_A) for a single-layer active RIS — giving additional, separately-controllable degrees of freedom.

## Method

A low-complexity optimization framework that decomposes the joint design:

- **BS precoder.** Lagrange dual + Pareto optimization theory transform the general power constraints into a tractable form yielding an optimal semi-closed-form precoder.
- **Passive RIS coefficients.** A discretization method converts the jammers' imperfect CSI into a robust form; a new anti-jamming criterion yields two **jamming-nulling feasibility conditions** and a unified unit-modulus zero-forcing (UM-ZF) scheme with a semi-closed-form solution.
- **Active RIS coefficients.** Three efficient algorithms based on alternating majorization-minimization (AMM) and conventional/modified cyclic coordinate descent (C/M-CCD) trade complexity against performance; all are proven to converge to a limited KKT point.

## Key findings

- The cascaded architecture accurately nulls toward the jammers while aligning the mainlobe with the target even under angular uncertainty; received SINR at the BS direction is ~0 dB versus ~−10 dB for the single-layer and fully-digital architectures, while all architectures sit near −50 dB toward the jammer (verbatim from the simulation discussion).
- Power-scattering ratio (PSR): the proposed cascaded architecture concentrates power on the Rx antennas with a PSR of **32.8%**, which the paper reports as 2.78 times lower than the single-layer active RIS architecture's PSR of **75.9%** (verbatim).
- Numerical simulations show superior performance at lower complexity than the fully-digital receiver and the SDR method.

## Limitations / future work

Simulation-only; the parse does not enumerate explicit future work. *Not an MEC paper* — it is curated as a physical-layer **anti-jamming / RIS receiver** anchor. An earlier version appeared at IEEE ICC 2023 (Rome). DOI date of publication 25 Oct 2023 / date of current version 12 Jun 2024 → year 2024.

## Relation to the corpus

A physical-layer **anti-jamming + RIS** anchor that complements the MEC-side anti-jamming and RIS work. It shares the **worst-case / imperfect-CSI robust optimization** stance of [[sun-2024-mfris-semantic-antijamming]] (multi-functional RIS semantic anti-jamming) and the broader [[anti-jamming-mec]] thread, and adds a receiver-side architecture to the corpus's [[intelligent-reflecting-surface]] / [[active-ris]] coverage. Reinforces [[csi-estimation-error]], [[physical-layer-security]], and the [[alternating-optimization-sdr-sca]] solver family it explicitly contrasts against.

## Raw artifacts

- `raw/sources/Active-Passive_Cascaded_RIS-Aided_Receiver_Design_for_Jamming_Nulling_and_Signal_Enhancing/full.md`
- Original PDF and extracted figures in the same folder.
