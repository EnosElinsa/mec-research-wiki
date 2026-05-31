---
type: source
title: "Optimizing Secrecy Rate for Federated Learning Model Aggregation With Intelligent Reflecting Surface Toward 6G Ubiquitous Intelligence"
authors: ["Bomin Mao", "Yingying Wu", "Jiajia Liu", "Hongzhi Guo", "Jiadai Wang", "Nei Kato"]
year: 2025
url: "https://doi.org/10.1109/TCCN.2024.3454256"
venue: "IEEE Transactions on Cognitive Communications and Networking (IEEE TCCN)"
tags: [source, federated-learning, intelligent-reflecting-surface, noma, physical-layer-security, ddpg, secrecy-rate, 6g]
related:
  - "[[federated-learning]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[noma]]"
  - "[[physical-layer-security]]"
  - "[[ddpg]]"
  - "[[mao-2025-bcsa-frl]]"
  - "[[han-2024-ground-satellite-fl]]"
  - "[[bomin-mao]]"
created: 2026-06-01
updated: 2026-06-01
---

# Optimizing Secrecy Rate for Federated Learning Model Aggregation With Intelligent Reflecting Surface Toward 6G Ubiquitous Intelligence

## Citation

Mao, B., Wu, Y., Liu, J., Guo, H., Wang, J., & Kato, N. (2025). *Optimizing Secrecy Rate for Federated Learning Model Aggregation With Intelligent Reflecting Surface Toward 6G Ubiquitous Intelligence*. **IEEE Transactions on Cognitive Communications and Networking**. DOI: 10.1109/TCCN.2024.3454256. (Manuscript received 1 January 2024; accepted 30 August 2024; date of publication 4 September 2024; date of current version 9 April 2025 → year 2025 per the date-of-current-version convention.)

## TL;DR

Secures the **model-uploading phase of NOMA-based federated learning (FL)** with an **intelligent reflecting surface (IRS)**. Because NOMA-based FL involves frequent model-parameter uploads over stochastic wireless channels, it suffers degraded rate and risks **privacy leakage** to an eavesdropper (Eve) sited near the base station (BS). The paper defines the **secrecy rate** as the device→BS rate minus the device→Eve rate, and formulates a **max-min secrecy-rate** problem over the devices' transmit powers and the IRS phase shifts, subject to a transmit-power budget. The non-convex, coupled problem is solved with a **Deep Deterministic Policy Gradient (DDPG)** agent; numerical results show the IRS improves the secrecy rate.

## Problem framing

6G envisions massive IoT connectivity with ubiquitous, privacy-preserving intelligence, for which FL keeps data local. NOMA lets many devices share radio blocks to involve enough participants for a reliable model, but the stochastic NOMA channels and frequent BS↔device communication degrade transmission rate and FL performance, and the complex propagation enables eavesdropping. Traditional jamming-based security adds energy cost for resource-constrained IoT and degrades FL, and over-the-air covertness schemes are inflexible. An IRS can instead reconfigure the propagation environment passively (low cost), strengthening the device→BS channel while suppressing the device→Eve channel — improving both rate and security.

## System model

- **Setup.** An IRS-assisted NOMA-based FL system (MU-MIMO): one BS with $N_T$ antennas, $N_d$ single-antenna devices, one single-antenna Eve near the BS intercepting uploaded parameters, and one IRS with $N_I$ passive reflecting elements (ideal unit-modulus reflection). CSI assumed available; channels quasi-static across FL iterations.
- **FL model.** FedAvg: devices minimize local loss via SGD then upload models; BS aggregates by data-size-weighted averaging. Focus is the **NOMA-based model-uploading phase**.
- **Channels.** Log-distance path loss + Rayleigh small-scale fading; effective device→BS and device→Eve channels combine the direct link and the IRS-reflected link via the phase-shift diagonal matrix. NOMA receiver uses successive interference cancellation (decode strongest channel first).
- **Secrecy rate.** $R_{sn} = R_{nb} - R_{ne}$ (device→BS minus device→Eve rate).
- **Objective.** Maximize the **minimum** secrecy rate across devices (FL is bottlenecked by the slowest/least-secure user) over transmit-power matrix $\mathbf{P} \le P_\text{Max}$ and IRS phase shifts $|\Phi_l|^2 = 1$.

## Method

- The max-min secrecy-rate problem is non-convex (unit-modulus IRS constraint + coupling between $\mathbf{P}$ and $\Phi$), so it is cast as a Markov decision process and solved with **DDPG** ([[ddpg]]).
- **DDPG structure.** Actor-critic with target networks and experience replay; the action jointly outputs the device transmit powers and IRS phase shifts, the state observes current power + high-dimensional CSI, and the reward tracks the minimum secrecy rate. DDPG (continuous action) is chosen over discrete Q-learning because of the huge continuous state/action space.

## Key findings

- Numerical results **validate the algorithm's efficiency** and demonstrate that the **IRS improves the secrecy rate** of NOMA-based FL model aggregation (abstract/parse; specific gains are in the simulation figures and are indicative).
- Casting the joint power + phase-shift design as a DRL problem handles the continuous, high-dimensional CSI-dependent action space that closed-form solutions cannot.

## Limitations / future work

The model assumes available CSI, quasi-static channels, a single Eve close to the BS, and ideal lossless IRS reflection. The parse does not enumerate an explicit future-work list → `not in parse`.

## Relation to the corpus

A **secure federated-learning** entry from the NWPU non-terrestrial/security cluster led by [[bomin-mao]] (with [[jiajia-liu]], [[hongzhi-guo]], [[jiadai-wang]], [[nei-kato]]) — adjacent to the trust/security/federation track via [[mao-2025-bcsa-frl]] (blockchain-secured FRL) and to the FL-over-networks thread of [[han-2024-ground-satellite-fl]]. Its distinctive lever is using an **IRS for physical-layer security of FL aggregation** (rather than jamming or differential privacy), combining [[intelligent-reflecting-surface]], [[noma]], [[federated-learning]], and [[physical-layer-security]], solved with [[ddpg]]. The secrecy-rate metric ties it to the wiki's PLS sources ([[su-2024-sensing-aided-isac-pls]], [[yao-2025-secure-isac-dual-eavesdropping]]).

## Raw artifacts

- `raw/sources/Optimizing_Secrecy_Rate_for_Federated_Learning_Model_Aggregation_With_Intelligent_Reflecting_Surface_Toward_6G_Ubiquitous_Intelligence/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
