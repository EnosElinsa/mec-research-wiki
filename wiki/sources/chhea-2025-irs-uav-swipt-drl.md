---
type: source
title: "Energy Efficiency Optimization in Intelligent Reflecting Surface-Aided UAV Wireless Power Transfer Networks Using DRL"
authors: ["Kimchheang Chhea", "Sengly Muy", "Jung-Ryun Lee"]
year: 2025
url: "https://doi.org/10.1109/TVT.2024.3519591"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, irs-uav, energy-efficiency, swipt, drl, trajectory-optimization, wireless-power-transfer]
related:
  - "[[simultaneous-wireless-information-and-power-transfer]]"
  - "[[active-ris]]"
  - "[[uav-trajectory-control]]"
  - "[[an-2024-multilayer-ris-hap-swipt]]"
created: 2026-06-04
updated: 2026-07-16
modeling_card: required
---

# Energy Efficiency Optimization in Intelligent Reflecting Surface-Aided UAV Wireless Power Transfer Networks Using DRL

## Citation

Chhea, K., Muy, S., & Lee, J.-R. (2025). *Energy Efficiency Optimization in Intelligent Reflecting Surface-Aided UAV Wireless Power Transfer Networks Using DRL*. **IEEE Transactions on Vehicular Technology**, 74(4). DOI: 10.1109/TVT.2024.3519591. (Received 16 April 2024; accepted 15 December 2024; published 18 December 2024; current version 18 April 2025.)

## TL;DR

Studies an IRS-assisted UAV network with **SWIPT** (simultaneous wireless information and power transfer) for IoT ground users. The UAV acts as an aerial base station; an IRS boosts signals to GUEs who simultaneously harvest energy and decode information via a power-splitting (PS) receiver. The joint optimization of UAV trajectory, IRS phase shifts, UAV transmit power, and PS ratio to maximize average **energy efficiency** is non-convex. A **DRL** approach is proposed with a reward function derived from an **SINR map** (bivariate normal distribution over the coverage area) for stable and efficient training. Results show better EE, lower energy consumption, and higher data rate than comparison schemes.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A single-antenna UAV base station serves $M$ ground user equipments through direct and single-reflection Rician-fading links aided by one $N_r\times N_c$ passive IRS. Each user applies SWIPT power splitting so that a fraction $\rho_m$ supports information decoding and the remaining fraction supports energy harvesting.

**Problem & objective**: Problem (15) is a nonconvex average energy-efficiency maximization, $\max_{q_u,\rho_m,p_m,\Theta}\frac{1}{M}\sum_{m=1}^{M}EE_m(q_u,\rho_m,p_m,\Theta)[t]$, with $EE_m=R_m/ED_m$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV route | $q_u[t]$ | Continuous position | Sets the UAV location in each slot |
| Power-splitting ratio | $\rho_m[t]$ | Continuous, $(0,1]$ | Divides received power between decoding and harvesting |
| Transmit power | $p_m[t]$ | Continuous, $p_m[t]\leq p_{\max}$ | Allocates UAV downlink power to user $m$ |
| IRS phase steer | $\Theta[t]$ | Continuous phase, $[0,2\pi]$ | Controls the passive reflecting elements |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Transmit-power ceiling: $p_m[t]\leq p_{\max}$ |
| C2 | IRS phase range: $0\leq\Theta[t]\leq2\pi$ |
| C3 | SWIPT split: $0<\rho_m[t]\leq1$ |
| C4 | UAV displacement: $\lVert q_u[t+1]-q_u[t]\rVert\leq D_{\max}$ |

**Algorithm**: Cast the joint control as an MDP with state $s^t=\{q_u[t],\rho[t],p[t],\Theta[t],\mathbf h_m^H[t],t\}$ and discretized action increments $a^t=\{\Delta q_u[t],\Delta\rho[t],\Delta p[t],\Delta\Theta[t]\}$, construct an expected-SINR map over UAV locations, use its bivariate-normal energy-efficiency reward to shape learning, and train a deep Q-learning agent with experience replay.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Chhea et al. [x] studied energy-efficiency optimization in an IRS-aided UAV downlink where ground users simultaneously decode information and harvest energy through SWIPT power splitting. They maximized average user energy efficiency by jointly controlling the UAV route, IRS phase steer, UAV transmit power, and power-splitting ratios under power, phase, splitting, and displacement limits. Their deep Q-learning method used a reward derived from an expected-SINR map to guide the discretized high-dimensional controller. Simulations reported higher energy efficiency than SHF, REINFORCE, gradient search, and DRL without IRS, while also reporting high data rate and lower user energy consumption than the principal comparison schemes.

## Problem framing

UAVs as aerial BSs have limited onboard energy; IRS can boost coverage without UAV expending additional transmit power. Incorporating SWIPT allows IoT devices to harvest energy from the UAV's downlink while receiving data, extending network lifetime. The four-variable joint optimization (UAV trajectory + IRS phase shifts + transmit power + PS ratio) is highly non-convex; classical iterative methods are computationally expensive. A DRL approach with a spatially-aware SINR-map reward is proposed for tractable online optimization.

## System model

- **Single-antenna UAV** BS + **single IRS** (N_r × N_c UPA of passive reflecting elements) + M GUEs.
- **No direct BS-to-device path** assumed (building blockage); all signals go via IRS reflection.
- **SWIPT at each GUE:** power splitter divides received signal between energy harvester (EH) and information decoder (ID).
- **Channels:** UAV-to-IRS (3D distance-dependent) and IRS-to-GUE (element-wise phase-shift-controlled).
- **DRL reward:** SINR map — bivariate normal distribution over the coverage area, centered at each GUE, giving the agent a spatially smooth EE signal that improves training stability.

## Method

- **DRL** (specific backbone not fully named in parse header — uses a reward derived from SINR map). The agent selects discrete UAV position updates + IRS phase shifts + power + PS ratio.
- SINR map reduces reward sparsity and stabilizes training in a continuous/high-dimensional space.
- Computational complexity analysis provided (parse Section V).

## Key findings

- Proposed DRL achieves **lower energy consumption, higher data rate, and improved EE** compared to comparison schemes (parse Abstract, Section VI).
- IRS integration significantly reduces node energy consumption in the network (parse Section VI, contribution point 3).
- SINR-map reward provides smoother training and better convergence than a naive per-step SINR reward (parse Section IV description).

## Limitations / future work

Parse does not name the specific DRL backbone (deep Q-network vs. actor-critic vs. other); exact numerical gains vs. benchmarks not in parse header. Single IRS, single UAV. SWIPT non-linear energy harvesting model not discussed.

## Relation to the corpus

Connects [[simultaneous-wireless-information-and-power-transfer]] and IRS-assisted UAV communications to an energy-efficiency objective solved by DRL — a combination distinct from the corpus's SCA/AO-heavy IRS-UAV papers (e.g., [[an-2024-multilayer-ris-hap-swipt]]). The SINR-map reward concept is an unusual DRL training stabilization technique not seen elsewhere in the corpus.

## Raw artifacts

- `raw/sources/Energy_Efficiency_Optimization_in_Intelligent_Reflecting_Surface-Aided_UAV_Wireless_Power_Transfer_Networks_Using_DRL/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
