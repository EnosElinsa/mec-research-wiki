---
type: source
title: "Decentralized Intelligence for Energy-Efficient 6G TN-NTN: A Cooperative Multi-Agent DRL Framework for Active RIS-Aided UAV-NOMA Communications"
authors: ["Monzur Morshed", "Mostafa Zaman Chowdhury", "Yeong Min Jang"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2026.3696806"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, active-ris, uav, noma, mappo, ctde, energy-efficiency, fairness]
related:
  - "[[decentralized-active-ris-uav-noma-control]]"
  - "[[active-ris]]"
  - "[[uav-mounted-ris]]"
  - "[[noma]]"
  - "[[mappo]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[jains-fairness-index]]"
  - "[[non-terrestrial-network]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-12
updated: 2026-07-12
---

# Decentralized Intelligence for Energy-Efficient 6G TN-NTN: A Cooperative Multi-Agent DRL Framework for Active RIS-Aided UAV-NOMA Communications

## Citation

Morshed, M., Chowdhury, M. Z., & Jang, Y. M. (2026). *Decentralized Intelligence for Energy-Efficient 6G TN-NTN: A Cooperative Multi-Agent DRL Framework for Active RIS-Aided UAV-NOMA Communications*. **IEEE Transactions on Green Communications and Networking**, 10, 3162-3173. DOI: 10.1109/TGCN.2026.3696806.

## TL;DR

Splits active-RIS UAV-NOMA control among BS, UAV, and RIS agents. A shared-critic MAPPO policy jointly learns NOMA power coefficients, UAV movement, and active-RIS gain/phase under a reward combining rate, energy efficiency, Jain fairness, outage, and airspace penalties.

## Problem

Cell-edge NOMA users face interference and weak direct links in a terrestrial/non-terrestrial network. A UAV-mounted active RIS can amplify and redirect the BS signal, but jointly controlling mobility, element gains/phases, and NOMA power creates a high-dimensional non-convex action space. A monolithic controller becomes increasingly expensive as users and RIS elements grow.

## System model

- One serving BS communicates with four NOMA user pairs through a UAV-mounted active RIS while one fixed neighboring BS interferes.
- Each pair contains a center and edge user. Power-domain NOMA assigns at least half the pair power to the edge user and assumes perfect SIC at the center user.
- Weak direct NLoS links coexist with the BS-RIS-user path. Each RIS element independently controls phase and amplification.
- The joint variables are per-pair NOMA power coefficients, discrete UAV motion, and continuous RIS gain/phase vectors.
- Total power includes BS transmit power, simplified UAV movement/hover power, RIS static power, and active-amplifier power.

## Method

The cooperative MMDP uses three local actors under [[centralized-training-decentralized-execution|CTDE]]: the BS actor selects NOMA coefficients, the UAV actor moves the platform, and the RIS actor selects element gains and phases. All receive the same composite reward. Offline [[mappo|MAPPO]] training collects joint rollouts, estimates advantages with GAE, updates a shared global critic, and applies clipped PPO plus entropy regularization to each actor. At execution the critic is discarded and each physical controller acts from its local observation.

## Key findings

- Table V reports `19.31 bps/Hz` spectral efficiency and `1.61 Mbits/Joule` energy efficiency for MAPPO, versus `18.00`/`1.15` for centralized SARL and `19.54`/`1.13` for DDPG. MAPPO has the best energy efficiency, while DDPG is slightly higher in raw spectral efficiency.
- Relative to SARL, the abstract reports more than `40%` energy-efficiency improvement and `7.2%` spectral-efficiency improvement.
- On an Intel i7-7700 CPU, parallel MAPPO inference is `2.85 ms` for the reported 2-pair/16-element case, about `57%` below SARL's `6.68 ms`; the larger tested settings remain near 3 ms.
- Active RIS, UAV mobility, and agent decomposition each improve the plotted performance, but most ablation magnitudes are figure-only.

## Limitations / parse caveats

Evaluation is simulation-only with one serving BS, one UAV/RIS, one fixed interferer, random-walk users, perfect CSI/SIC, weak direct NLoS links, and a simplified propulsion model. Imperfect CSI/signaling delay, RSMA, multi-UAV, and THz operation are future work. Several equations/table columns are OCR-damaged. The parse title misspells "Efficient"; the exact-title Crossref record supplies the corrected bibliographic title and otherwise absent 2026 TGCN metadata. Technical claims come only from the parse.

## Relation to the corpus

[[decentralized-active-ris-uav-noma-control]] joins [[active-ris]], [[uav-mounted-ris]], and [[noma]] through physical agent decomposition. Unlike centralized trajectory/phase optimizers, it assigns each subsystem a local policy while retaining a shared training objective for rate, energy, fairness, and outage.

## Raw artifacts

- Parse: `raw/sources/Decentralized_Intelligence_for_Energy-Efficient_6G_TN-NTN_A_Cooperative_Multi-Agent_DRL_Framework_for_Active_RIS-Aided_UAV-NOMA_Communications/Decentralized_Intelligence_for_Energy-Efficient_6G_TN-NTN_A_Cooperative_Multi-Agent_DRL_Framework_for_Active_RIS-Aided_UAV-NOMA_Communications.md`
- Origin PDF: `raw/sources/Decentralized_Intelligence_for_Energy-Efficient_6G_TN-NTN_A_Cooperative_Multi-Agent_DRL_Framework_for_Active_RIS-Aided_UAV-NOMA_Communications/Decentralized_Intelligence_for_Energy-Efficient_6G_TN-NTN_A_Cooperative_Multi-Agent_DRL_Framework_for_Active_RIS-Aided_UAV-NOMA_Communications.pdf`
- Figures: `raw/sources/Decentralized_Intelligence_for_Energy-Efficient_6G_TN-NTN_A_Cooperative_Multi-Agent_DRL_Framework_for_Active_RIS-Aided_UAV-NOMA_Communications/images/`
