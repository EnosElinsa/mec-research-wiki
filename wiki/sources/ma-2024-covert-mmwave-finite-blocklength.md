---
type: source
title: "Covert mmWave Communications With Finite Blocklength Against Spatially Random Wardens"
authors: ["Ruiqian Ma", "Weiwei Yang", "Xinrong Guan", "Xingbo Lu", "Yi Song", "Dechuan Chen"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2023.3296414"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags:
  - source
  - covert-communication
  - finite-blocklength-urllc
  - physical-layer-security
  - stochastic-geometry
  - mmwave
  - multi-antenna-beamforming
related:
  - "[[covert-communication]]"
  - "[[finite-blocklength-urllc]]"
  - "[[physical-layer-security]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[cooperative-jamming]]"
  - "[[wu-2024-urllc-uav-mec-latency]]"
created: 2026-06-03
updated: 2026-11-03
modeling_card: required
---

# Covert mmWave Communications With Finite Blocklength Against Spatially Random Wardens

## Citation
Ruiqian Ma, Weiwei Yang, Xinrong Guan, Xingbo Lu, Yi Song, Dechuan Chen, "Covert mmWave Communications With Finite Blocklength Against Spatially Random Wardens," *IEEE Internet of Things Journal*, 2024. DOI: 10.1109/JIOT.2023.3296414. (Manuscript received 11 Jan 2022; revised through 5 Jun 2023; accepted 14 Jul 2023; date of publication 18 Jul 2023; date of current version 8 Jan 2024 → year 2024 per the date-of-current-version convention. Corresponding author: Xinrong Guan. National University of Defense Technology + Army Engineering University of PLA + Academy of Military Sciences of PLA + Huaiyin Normal University + Nanyang Normal University.)

## TL;DR
This paper studies **covert millimeter-wave (mmWave) communication with finite blocklength** when **spatially random wardens** (Willies, modeled as a Poisson point process) try to detect whether a multi-antenna transmitter (Alice) is sending to a legitimate receiver (Bob). It derives tractable **covertness-constraint** and **average effective covert throughput (AECT)** expressions for two beamforming schemes — the conventional **phase array (PA)** and the **linear frequency diverse array (LFDA)** — then jointly optimizes the **transmit power and blocklength** to maximize AECT under a maximal-blocklength limit. Optimizing blocklength beats a fixed-blocklength benchmark, and the gain grows with warden density; increasing the maximal blocklength does not always help (a power-vs-blocklength trade-off), while more antennas does. The best scheme (PA vs LFDA) depends on the legitimate receiver's direction.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna mmWave Alice transmits to Bob while spatially random non-colluding Willies form a Poisson point process. Beamforming uses a phase array or linear frequency diverse array, and finite-blocklength coding determines covert throughput over a quasi-static dominant-path channel.

**Problem & objective**: Finite-blocklength covert-throughput optimization, a stochastic-geometry constrained continuous problem, maximizes average effective covert throughput, $\max_{N,P_a}\bar\eta_P$ in (30) for PA and $\max_{N,P_a}\bar\eta_L$ in (39) for LFDA, subject to the covertness condition and $N\le N_{\max}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Transmit power | $P_a$ | continuous, nonnegative | Alice's beamforming transmit power |
| Blocklength | $N$ | integer, $N\le N_{\max}$ | Number of channel uses for the finite-blocklength code |
| Beamforming scheme | $s$ | discrete, PA or LFDA (compared) | Phase-array or frequency-diverse beam selection |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (12) | Covertness against every PPP warden: $\min_{w_l\in\Phi_w}\xi_{w_l}^*\ge1-\varepsilon$ |
| (21) / (35) | Tractable covertness condition used in (30) for PA and in (39) for LFDA: an upper bound proportional to $P_a\sqrt N\,\Omega_P$ (or $\Omega_L$) over $2\sigma^2$ is at most $\varepsilon$ |
| (30) / (39), 2nd–3rd constraints | Blocklength limit: $N\le N_{\max}$, $N\in\mathbb N^+$ |
| Model rule | AECT is $\bar\eta=NR(1-\mathbb E(\delta))$ ((25), (38)), with Bob's decoding error from the finite-blocklength normal approximation |
| Model rule | PA and LFDA beam gains follow the ULA geometry; the scheme is compared, not optimized |

**Algorithm**: Derive PPP covertness and AECT expressions for PA and LFDA → optimize power and blocklength jointly under the covertness bound → compare the two beamforming schemes over warden density, antenna number, and receiver direction.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Ma et al. [x] studied covert mmWave communication with finite blocklength against spatially random wardens modeled by a Poisson point process. They formulated an average effective covert throughput maximization problem that jointly selects transmit power and blocklength under a covertness constraint and a maximum-blocklength limit. The analysis compares conventional phase-array and linear frequency-diverse-array beamforming using finite-blocklength decoding error and stochastic-geometry expressions. Optimal power and blocklength are derived for both schemes, exposing a trade-off between extra coding symbols and covert power. Numerical evaluations report higher AECT for the optimized blocklength than the fixed $N=N_{\max}$ benchmark, with the gain growing as warden density increases; a larger $N_{\max}$ does not always raise the maximum AECT, and whether PA or LFDA is better depends on Bob's direction.

## Problem framing
Beyond hiding message **content** (encryption, classic [[physical-layer-security|PLS]]), some settings need to hide the **existence** of a transmission — covert / low-probability-of-detection communication (e.g. Internet of Battlefield Things, where even detecting a link leaks military activity). mmWave is attractive (directional beams, compact multi-antenna arrays), but prior covert-mmWave work mostly assumed a **single** warden and **infinite** blocklength. With multiple randomly located wardens, a warden may fall inside the beam and obtain high antenna gain, degrading covertness; and IoT/vehicular latency-power limits make **finite blocklength** realistic — which also limits a warden's observations. The paper redesigns covert-mmWave transmission against **spatially random** wardens in the finite-blocklength regime.

## System model
- **Network (Fig. 1):** Alice has M antennas (uniform linear array); Bob and each Willie are single-antenna. Non-colluding Willies are a homogeneous PPP Φ_w with density λ_w. Finite blocklength of N channel uses with Gaussian codebooks.
- **Channel:** single dominant-path mmWave model (line-of-propagation), path gain a_i ~ CN(0,1), path-loss exponent α; quasi-static over a block.
- **Beamforming:** **PA** (same frequency across elements; steering vector depends on direction θ) and **LFDA** (frequency increments across elements; steering vector depends on both direction θ and distance d, so the beam pattern is range-dependent). Alice's beamformer maximizes antenna gain toward Bob, giving received SNR γ_b = P_a M |a_b|² d_ab^{−α} / σ².
- **Detection / covertness:** each Willie runs a binary hypothesis test; total detection error ξ = P_FA + P_MD. Communication is covert when min over wardens of ξ* ≥ 1−ε (tolerance ε), characterized via total-variation distance / KL divergence between the transmitting and silent output distributions.
- **Effectiveness:** finite-blocklength effective throughput η = N·R·(1−δ) with decoding-error probability δ given by the normal-approximation Q-function in γ_b, R, and N; AECT averages η over the channel/warden randomness.

## Method
- **Stochastic-geometry covertness analysis:** using PPP tools, tractable expressions for the covert-communication constraint are derived for both PA and LFDA, exploiting the line-of-propagation property of mmWave (see [[stochastic-geometry-network-analysis]]).
- **AECT expression:** AECT is written as a function of transmit power, blocklength, antenna number, and warden density, for both beamforming schemes.
- **Joint power + blocklength optimization:** the AECT-maximization problem under a maximal-available-blocklength constraint is formulated and the **optimal transmit power and blocklength** are derived for PA and LFDA, revealing a nontrivial power-vs-blocklength trade-off.

## Key findings
Grounded in the abstract and contributions (numerical magnitudes are figure-derived, treated as indicative):
- Optimizing blocklength yields higher AECT than a fixed-blocklength benchmark, and the gap **widens as warden density increases**.
- Covertness performance **deteriorates as warden density rises** — more potential detectors make hiding harder.
- Increasing the maximal available blocklength **does not always** improve maximum AECT (due to the power-vs-blocklength trade-off), but using **more antennas** can still improve it.
- The maximum AECT depends on the legitimate receiver's **direction** relative to the array, so Alice can adaptively pick **PA or LFDA** to enhance covertness.

## Limitations / future work
- Analysis is built on idealized assumptions: single dominant-path mmWave channel, non-colluding wardens, homogeneous-PPP warden locations, and quasi-static fading.
- Validation is analytical + numerical (no hardware/measurement campaign).
- LFDA's range-dependent beam relies on small frequency-increment approximations (MΔf ≪ f_c, MD ≪ d).
- This is a physical-layer covert-communication study; it is not an MEC/offloading paper and is filed as a security/PHY anchor.

## Relation to the corpus
This is a **covert-communication** anchor — hiding a transmission's existence, beyond content-hiding [[physical-layer-security|PLS]] — newly defined in the [[covert-communication]] concept page. It combines three threads the corpus tracks separately: [[finite-blocklength-urllc|finite blocklength]] (shared with [[wu-2024-urllc-uav-mec-latency]], which uses the same short-packet regime for URLLC latency rather than covertness), [[stochastic-geometry-network-analysis|stochastic geometry]] for spatially random adversaries, and multi-antenna mmWave beamforming. Its warden-uncertainty mechanism is adjacent to the corpus's [[cooperative-jamming]]-based covertness designs but exploits limited warden observations from short blocklength instead of injected noise.

## Raw artifacts
- Parse: `raw/sources/Covert_mmWave_Communications_With_Finite_Blocklength_Against_Spatially_Random_Wardens/Covert_mmWave_Communications_With_Finite_Blocklength_Against_Spatially_Random_Wardens.md`
- Origin PDF: `raw/sources/Covert_mmWave_Communications_With_Finite_Blocklength_Against_Spatially_Random_Wardens/Covert_mmWave_Communications_With_Finite_Blocklength_Against_Spatially_Random_Wardens.pdf`
- Figures: `raw/sources/Covert_mmWave_Communications_With_Finite_Blocklength_Against_Spatially_Random_Wardens/images/`
