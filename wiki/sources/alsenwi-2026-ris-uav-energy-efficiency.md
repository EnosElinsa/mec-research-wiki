---
type: source
title: "RIS-UAV Integration for Enhanced Coverage and Energy-Efficient 6G Wireless Networks"
authors: ["Madyan Alsenwi", "Mehran Abolhasan", "Justin Lipman"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3573948"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 10, pp. 160-171"
modeling_card: required
tags: [source, ris-uav, energy-efficiency, mmwave, deep-reinforcement-learning, trajectory-control, passive-beamforming, chance-constraint]
related:
  - "[[cloud-trained-edge-executed-drl]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[uav-mounted-ris]]"
  - "[[uav-trajectory-control]]"
  - "[[chance-constraint]]"
  - "[[jains-fairness-index]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
  - "[[qin-2023-ris-uav-mec-ee]]"
  - "[[sheng-2025-ris-online-uav-mec]]"
created: 2026-07-14
updated: 2026-07-16
---

# RIS-UAV Integration for Enhanced Coverage and Energy-Efficient 6G Wireless Networks

## Citation

Alsenwi, M., Abolhasan, M., & Lipman, J. (2026). *RIS-UAV Integration for Enhanced Coverage and Energy-Efficient 6G Wireless Networks*. **IEEE Transactions on Green Communications and Networking, 10**, 160-171. DOI: 10.1109/TGCN.2025.3573948.

## TL;DR

Uses an actor-critic policy to jointly control a UAV-mounted passive RIS, its quantized phase shifts, and BS precoding/transmit power in a blocked mmWave downlink. Training runs on a cloud server, while an edge server executes the policy and returns observations and rewards for periodic retraining.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna BS serves dynamic single-antenna users $\mathcal K$ through a UAV-mounted passive RIS in a blocked mmWave downlink with no direct BS-to-user path. The UAV moves in three dimensions, the RIS has $N$ elements with quantized phases and amplitudes, and channel states vary over time.

**Problem & objective**: The stochastic problem $\max_{x,y,h,W,\Phi}\frac{1}{T}\sum_{t\in\mathcal T}\eta(t)$ maximizes average energy efficiency, where $\eta(t)=\frac{\sum_{k\in\mathcal K}B\log_2(1+\mathrm{SINR}_k(t))}{\sum_{k\in\mathcal K}\|w_k\|^2+P_{\mathrm{uav}}}$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV horizontal coordinate | $x(t),y(t)$ | continuous, bounded by region limits | Horizontal UAV trajectory coordinates |
| UAV altitude | $h(t)$ | continuous, $h_{\min}\le h(t)\le h_{\max}$ | UAV height |
| BS precoding | $W=\{w_k\}$ | continuous complex matrix | Beamforming and transmit-power allocation |
| RIS coefficients | $\Phi(t)$ | mixed discrete-continuous | Quantized phase shifts and amplitudes $b_n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Chance-constrained user QoS: $\Pr\{r_k(t)\ge r_k^{\min}\}\ge1-\varepsilon,\ \forall k$ |
| C2 | BS transmit power: $\sum_{k\in\mathcal K}\|w_k\|^2\le P_{\max}$ |
| C3 | RIS structure: $\Phi=\operatorname{diag}(b_ne^{j\phi_n})$ |
| C4 | Quantized RIS phase: $\phi_n=\frac{\kappa\pi}{2^{c-1}},\ \kappa\in\{0,1,\ldots,2^c-1\}$ |
| C5 | RIS amplitudes are feasible: $b_n\in[0,1]$ |
| C6 | Flight region: $h_{\min}\le h(t)\le h_{\max}$, $x_{\min}\le x(t)\le x_{\max}$, and $y_{\min}\le y(t)\le y_{\max}$ |

**Algorithm**: Model the problem as an MDP with state $\mathbf s(t)=\{\mathbf g_k(t),\mathbf G(t)\}$, action $\mathcal A=\{x,y,h,W,\Phi\}$, and reward $R(t)=\eta(t)+\beta(t)\sum_k[r_k(t)-r_k^{\min}]$; train an actor-critic policy offline at a cloud server with experience replay, execute it online at an edge server, return observations and rewards for periodic retraining, and update dimensions when user cardinality changes.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Alsenwi et al. [x] studied energy-efficient downlink communication from a base station through a UAV-mounted passive RIS to dynamic users in blocked mmWave environments. They formulated a stochastic average-energy-efficiency maximization over UAV coordinates, altitude, BS precoding, and quantized RIS coefficients with chance-constrained minimum data rates and power and flight-region limits. Their actor-critic framework trains offline at a cloud server, executes online at an edge server, and periodically retrains from observed channels and rewards. Simulations reported approximately 6 bit/s/Hz average spectral efficiency, about 97% reliability at a 4 Mbps threshold, and about 80% reliability at an 8 Mbps threshold for the proposed approach.

## Problem and system model

A multi-antenna BS serves dynamic single-antenna users only through a [[uav-mounted-ris]]; the model assumes no direct BS-to-user path. The objective maximizes average bit/Joule energy efficiency over time, with the denominator combining BS transmit power, UAV hovering and circuit power, and per-element RIS hardware power.

The joint variables include UAV position, BS precoding, and RIS amplitudes and quantized phases. A per-user [[chance-constraint]] requires the minimum data rate to be met with a specified probability, alongside BS power, RIS-feasibility, and flight-region constraints. The resulting mixed discrete-continuous, nonlinear problem motivates learning-based online control.

## Method

The state contains current BS-RIS and RIS-user channel information, while the action jointly represents UAV position, precoding, and RIS coefficients. The reward combines energy efficiency with per-user minimum-rate margins. The actor-critic learner uses experience replay and a policy-gradient update.

The deployment pattern is [[cloud-trained-edge-executed-drl]]: computationally intensive training is performed offline at a centralized cloud server, the trained model is deployed to an edge server for instantaneous decisions, and observations and rewards are fed back for periodic retraining. The paper allows model input and output dimensions to be updated when network conditions such as the number of users change; this requires retraining and is not zero-shot cardinality generalization.

## Key findings

- Reward curves are described as stabilizing after approximately 7,500 time steps for 10 users and 10,000 time steps for 20 users. These are readings from Fig. 3 rather than tabulated measurements.
- The proposed policy has the highest [[jains-fairness-index|Jain fairness index]] among the UAV-RIS, Fixed-UAV, Static-Shift, and Random cases, but the parse gives no exact fairness values.
- Figure-derived average spectral efficiencies are approximately 6 bit/s/Hz for the proposed method, 5.4 for Fixed-UAV, 5 for Fixed-RIS, and 3.7 for Random.
- Energy efficiency first increases and then decreases with the number of RIS elements because rate eventually saturates while RIS hardware power continues to grow. The text does not state an exact maximizing element count.
- The minimum-rate success rate is reported at approximately 97% for a 4 Mbps threshold and approximately 80% for an 8 Mbps threshold. Both values are figure-derived.

## Limitations

Evidence is simulation-only, with no flight test, RIS prototype, measured channel trace, or end-to-end cloud/edge latency measurement. The structured channel model assumes no direct BS-user link. UAV energy includes hovering, circuit, and RIS hardware power but omits propulsion energy for horizontal and vertical movement.

The paper states the chance constraint without giving the uncertainty distribution or a deterministic/sample reformulation used in training; an instantaneous rate-margin reward does not establish probabilistic feasibility. It also does not specify how discrete movement and phase choices are produced alongside continuous actions or projected into the feasible set. Baseline naming varies between Fixed-RIS, Static-RIS, and Static-Shift, and no model-based joint optimizer provides an optimality gap.

## Relation to the corpus

This source links [[intelligent-reflecting-surface]] design with [[uav-trajectory-control]] and online wireless control. It is adjacent to the energy-efficiency formulations in [[pan-2025-uav-ris-energy-efficient-comm]] and [[qin-2023-ris-uav-mec-ee]], and to the online RIS/UAV control in [[sheng-2025-ris-online-uav-mec]], but it does not optimize computation offloading.

## Raw artifacts

- Parse: `raw/sources/RIS-UAV_Integration_for_Enhanced_Coverage_and_Energy-Efficient_6G_Wireless_Networks/RIS-UAV_Integration_for_Enhanced_Coverage_and_Energy-Efficient_6G_Wireless_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
