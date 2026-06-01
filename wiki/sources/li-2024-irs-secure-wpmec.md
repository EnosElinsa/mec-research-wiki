---
type: source
title: "Intelligent Reflecting Surface Assisted Secure Computation of Wireless Powered MEC System"
authors: ["Baogang Li", "Jia Liao", "Wenjing Wu", "Yonghui Li"]
year: 2024
url: "https://doi.org/10.1109/TMC.2023.3269791"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, mobile-edge-computing, wireless-power-transfer, intelligent-reflecting-surface, physical-layer-security, secure-computation-efficiency, alternating-optimization-sdr-sca, computation-offloading]
related:
  - "[[mobile-edge-computing]]"
  - "[[wireless-power-transfer]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[physical-layer-security]]"
  - "[[secure-computation-efficiency]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[rf-energy-harvesting]]"
  - "[[chen-2025-swipt-mec-sac]]"
  - "[[wu-2025-iopo-irs-uav-thz-mec]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[michailidis-2024-secure-ris-uav-mec-iot]]"
  - "[[mao-2025-irs-noma-fl-secrecy]]"
created: 2026-06-02
updated: 2026-06-02
---

# Intelligent Reflecting Surface Assisted Secure Computation of Wireless Powered MEC System

## Citation

Li, B., Liao, J., Wu, W., & Li, Y. (2024). *Intelligent Reflecting Surface Assisted Secure Computation of Wireless Powered MEC System*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3269791. (Manuscript received 23 December 2022; revised 13 March 2023; accepted 18 April 2023; date of publication 25 April 2023; date of current version 6 March 2024 → year 2024.)

## TL;DR

Deploys an **intelligent reflecting surface (IRS)** to improve the **secure computation** performance of a **wireless-powered MEC (WPT-MEC)** system in the presence of a **passive eavesdropper**. An access point (AP) integrated with an MEC server first charges multiple single-antenna users via downlink WPT (IRS boosts energy harvesting), then the users perform partial offloading and local computing with the harvested energy (IRS weakens the eavesdropper's channel during offloading). The paper **maximizes the users' total secure computation task bits** by jointly optimizing AP energy transmit beamforming, IRS phase shifts (in both WPT and offloading stages), users' transmit power, offloading time, and local computation frequency. The non-convex problem is solved by an iterative algorithm combining **Taylor expansion, semidefinite relaxation (SDR), Lagrange duality, and KKT conditions**, reporting >45% secure-bits improvement at the AP's maximum transmit power versus benchmarks.

## Problem framing

WPT-MEC sustains energy-constrained IoT devices by combining RF wireless power transfer with edge offloading, but the broadcast nature of offloading exposes device information to eavesdroppers, and weak/obstructed device-to-AP channels limit both energy harvesting and offloading. Prior work integrated only **subsets** of {MEC, WPT, IRS, PLS}: some studied IRS-assisted secure MEC but ignored WPT (energy sustainability problem), others studied IRS-assisted WPT-MEC but ignored security (information-leakage problem). This paper targets the gap — using IRS to simultaneously improve energy harvesting **and** secure offloading in a WPT-MEC system with a passive eavesdropper, using **secure computation task bits** as the joint security-and-computation performance index.

## System model

- **Nodes.** K single-antenna users, one M-antenna AP integrated with an MEC server, an IRS of N passive reflecting elements (IRS controller), and one passive single-antenna eavesdropper (Eve). The model is stated to extend to multi-eavesdropper scenarios.
- **Protocol.** A **harvest-then-offload**, block-based protocol of length T: in the WPT stage $t_0$ the AP broadcasts energy (IRS improves the energy channel); in the remaining $T-t_0$ users offload over **TDMA** time slots $t_k$ (IRS weakens Eve's channel). Local computing runs concurrently with WPT and offloading. Download/result-return time is neglected.
- **Energy & computation.** Linear energy-harvesting model (non-linear EH deferred to future work); harvested energy $E_k=\eta t_0 \mathrm{Tr}(\mathbf{G}_k\mathbf{W})$. Partial offloading splits each task between local compute (energy $\propto T\xi_k f_k^3$, bits $Tf_k/c_k$) and secure offloading.
- **Security metric.** With MRC at the AP, the **secrecy offloading rate** is $R_{s,k}=R_{a,k}-R_{e,k}$ (legitimate minus eavesdropping rate); secure offloading bits are $Bt_k(R_{a,k}-R_{e,k})$. CSI of all channels is assumed perfectly known, so the results are framed as a **performance upper bound**.
- **Objective.** Maximize $\sum_k [Bt_k(R_{a,k}-R_{e,k}) + Tf_k/c_k]$ (sum secure computation task bits) subject to per-user energy-causality (harvested ≥ consumed), unit-modulus IRS phase constraints, AP power budget $\mathrm{Tr}(\mathbf{W})\le P$, the time-allocation budget, and per-user power/frequency caps.

## Method

The variables are tightly coupled, so the non-convex problem (P0) is decomposed into three tractable subproblems solved iteratively (alternating optimization):

- **AP energy beamforming + WPT-stage IRS phase shifts** — handled with **Taylor expansion** and **SDR / semidefinite programming** (with the energy covariance $\mathbf{W}=\mathbb{E}[\mathbf{w}\mathbf{w}^H]\succeq\mathbf{0}$).
- **Offloading-stage IRS phase shifts** — optimized via **SDR** with the other variables fixed.
- **Transmit power + computation time** — obtained via **Lagrange duality and KKT conditions**.
- The three variable groups are updated iteratively until the secure computation task bits converge.

## Key findings

- The proposed IRS-assisted scheme increases users' secure computation task bits over benchmark schemes; the abstract states the improvement is **above 45%** with respect to the AP's maximum transmit power. Increasing AP transmit power or (appropriately) adding IRS reflecting elements is reported to greatly improve performance. Margins beyond the headline figure are figure-derived; treat exact values as indicative.

## Limitations / future work

CSI is assumed perfectly known (so results are an upper bound); a **linear** energy-harvesting model is used (non-linear EH is named as future work); and **TDMA** is chosen for simplicity despite its delay penalty, with more efficient multiple-access methods deferred. The evaluation is simulation-based.

## Relation to the corpus

A **WPT-MEC + security** entry that uniquely fuses all four of {MEC, WPT, IRS, PLS} around a single secure-computation-bits objective, where most corpus neighbors cover only some of these. It grounds [[secure-computation-efficiency]] and shares the [[intelligent-reflecting-surface]] + [[wireless-power-transfer]] substrate with the energy/WPT track — including the SWIPT-MEC SAC design [[chen-2025-swipt-mec-sac]], the IRS-UAV-THz WPT-MEC scheme [[wu-2025-iopo-irs-uav-thz-mec]], and the foundational UAV wireless-powered MEC [[zhou-2018-uav-wireless-powered-mec]]. Its IRS-for-security angle parallels the secure RIS-UAV-MEC IoT work [[michailidis-2024-secure-ris-uav-mec-iot]] and the IRS-secured NOMA-FL aggregation of [[mao-2025-irs-noma-fl-secrecy]], while its AO + SDR solver is the classical-optimization pattern catalogued in [[alternating-optimization-sdr-sca]]. Its **partial (data-split) offloading** grounds [[binary-vs-partial-offloading]].

## Raw artifacts

- `raw/sources/Intelligent_Reflecting_Surface_Assisted_Secure_Computation_of_Wireless_Powered_MEC_System/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
