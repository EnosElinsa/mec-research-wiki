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
updated: 2026-06-04
---

# Energy Efficiency Optimization in Intelligent Reflecting Surface-Aided UAV Wireless Power Transfer Networks Using DRL

## Citation

Chhea, K., Muy, S., & Lee, J.-R. (2025). *Energy Efficiency Optimization in Intelligent Reflecting Surface-Aided UAV Wireless Power Transfer Networks Using DRL*. **IEEE Transactions on Vehicular Technology**, 74(4). DOI: 10.1109/TVT.2024.3519591. (Received 16 April 2024; accepted 15 December 2024; published 18 December 2024; current version 18 April 2025.)

## TL;DR

Studies an IRS-assisted UAV network with **SWIPT** (simultaneous wireless information and power transfer) for IoT ground users. The UAV acts as an aerial base station; an IRS boosts signals to GUEs who simultaneously harvest energy and decode information via a power-splitting (PS) receiver. The joint optimization of UAV trajectory, IRS phase shifts, UAV transmit power, and PS ratio to maximize average **energy efficiency** is non-convex. A **DRL** approach is proposed with a reward function derived from an **SINR map** (bivariate normal distribution over the coverage area) for stable and efficient training. Results show better EE, lower energy consumption, and higher data rate than comparison schemes.

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
