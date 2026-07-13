---
type: source
title: "Secure Low-altitude Maritime Communications via Intelligent Jamming"
authors: ["Jiawei Huang", "Aimin Wang", "Geng Sun", "Jiahui Li", "Jiacheng Wang", "Weijie Yuan", "Xianbin Wang"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3688701"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), accepted for publication"
tags: [source, maritime-communications, physical-layer-security, friendly-jamming, soft-actor-critic, conditional-variational-autoencoder, lstm, multi-objective-optimization]
related:
  - "[[advantage-conditioned-cvae-policy]]"
  - "[[lstm-eavesdropper-trajectory-prediction]]"
  - "[[friendly-jamming-uav]]"
  - "[[cooperative-jamming]]"
  - "[[physical-layer-security]]"
  - "[[maritime-mec]]"
  - "[[pomdp]]"
  - "[[soft-actor-critic]]"
  - "[[multi-objective-reinforcement-learning]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[jiawei-huang]]"
  - "[[aimin-wang]]"
  - "[[geng-sun]]"
  - "[[jiahui-li]]"
  - "[[jiacheng-wang]]"
  - "[[weijie-yuan]]"
  - "[[xianbin-wang]]"
  - "[[huang-2026-uav-friendly-jamming-transsac]]"
created: 2026-07-14
updated: 2026-07-14
---

# Secure Low-altitude Maritime Communications via Intelligent Jamming

## Citation

Huang, J., Wang, A., Sun, G., Li, J., Wang, J., Yuan, W., & Wang, X. (2026). *Secure Low-altitude Maritime Communications via Intelligent Jamming*. **IEEE Transactions on Mobile Computing**. Accepted for publication. DOI: 10.1109/TMC.2026.3688701.

## TL;DR

Coordinates a relay UAV and a friendly-jamming UAV around a moving vessel and an uncertain aerial eavesdropper. SAC-CVAE conditions action generation on normalized advantage, while an LSTM predicts an unobserved eavesdropper position; simulations report higher secrecy with competitive propulsion energy, but the supplied accepted manuscript omits the appendices cited for ablation and prediction-error evidence.

## Problem

Maritime UAV links are exposed to mobile eavesdroppers whose trajectories may be unknown when decisions are made. A relay UAV should remain useful to the vessel, while a jammer should approach the eavesdropper without causing excessive interference or propulsion cost. The paper formulates this as a long-horizon, partially observed two-objective control problem rather than assuming a predetermined eavesdropper path.

## System model

- A marine user follows an exogenous route. Relay UAV Alice transmits data to it; eavesdropping UAV Eve moves according to a memory-based Gauss-Markov process; jammer UAV Bob transmits artificial interference toward Eve.
- Alice-MU and Bob-MU links use a maritime Rician composite model with wave-induced Gaussian fading. Alice-Eve and Bob-Eve air-to-air links use free-space path loss.
- MU rate treats Bob's signal as interference, while Eve rate treats it as jamming. Instantaneous secrecy is modeled as `[R_M-R_E]^+`.
- Rotary-wing energy includes sustained propulsion, kinetic-energy change, and gravitational-energy change. Communication energy and acceleration/deceleration phases are neglected.
- The secure and energy-efficient maritime communication multi-objective problem maximizes total secrecy and minimizes Alice-plus-Bob energy over both 3-D trajectories and transmit powers.
- Constraints cover flight and power bounds, cumulative power budgets, minimum MU rate, and an interference-temperature limit at the MU. Rate and interference constraints enter the learned reward as penalties.
- Once Eve is unobservable, an LSTM estimates its current 3-D position from a stored trajectory. The parse does not give the tested history length or clearly reconcile the prose observation-loss threshold with Algorithm 1's `n >= Z` condition.

## Method

The authors scalarize secrecy, energy, rate violations, and interference violations into a POMDP reward and use one joint policy for Alice and Bob. This is not a multi-agent learner despite controlling two UAVs.

The SAC backbone uses entropy-regularized continuous control, replay, stochastic reparameterization, and soft target updates. [[advantage-conditioned-cvae-policy]] augments the state with normalized advantage `tanh(Q-V)` and learns latent action modes. During policy optimization, the decoder is queried at the maximum normalized condition `zeta*=1`, while lower-quality action samples supervise their corresponding conditions.

[[lstm-eavesdropper-trajectory-prediction]] replaces the full trajectory history in the policy state with Eve's observed or predicted current position, reducing the controller's state dimension. Training is server-side; trained inference is deployed to the UAVs. The paper supplies symbolic network complexity but no measured onboard latency or energy cost.

## Key findings

- Exact selected settings include a `100 m x 100 m` randomized initialization area, UAV altitude `50-70 m`, total UAV power `400 mW`, carrier `2.4 GHz`, `I_0=-74 dBm`, noise `-107 dBm`, replay batch 128, discount `0.9`, and the selected objective weights `(0.6,0.4)`.
- **Figure-read approximate:** when Eve approaches the MU, intelligent jamming settles near `245 bps/Hz` versus around zero without jamming; when Eve moves away, it settles near `210 bps/Hz` versus roughly `-25 bps/Hz`. The no-jamming plot uses the unclipped difference `R_M-R_E`, which explains negative values despite the clipped secrecy definition in the model.
- **Figure-labeled exact, Eve approaching:** total secrecy is `135.3/0.06/99.32/133.8/199.8/249.5 bps/Hz` for Greedy/DDPG/TD3/PPO/SAC/SAC-CVAE. Total UAV energy is `24000/4183/7342/4908/5505/4221 J` in the same order.
- **Figure-labeled exact, Eve moving away:** total secrecy is `128/0/62.19/140.6/181.7/217.8 bps/Hz`; energy is `22200/5237/5278/8957/5128/5121 J`. SAC-CVAE is best on both displayed objectives in this scenario.
- The selected weight pair `(0.6,0.4)` is identified as the plotted knee point. Individual heat-map cells are not numerically labeled, so their values should not be treated as exact.
- A two-pair extension changes the objective to max-min secrecy. **Figure-read approximate:** intelligent jamming settles near `145 bps/Hz`, versus about `-75 bps/Hz` without jamming; this is evidence for a small extension, not broad scalability.

## Limitations

Evidence is simulation-only and the main scenario contains one vessel, one eavesdropper, one relay, and one jammer. Eve follows the same Gauss-Markov family used by the simulator, so robustness to abrupt, adversarial, coordinated, or differently modeled motion is not established. The paper omits measured channel data, sea or flight tests, onboard inference timing, and controller energy overhead.

Important learning details are unavailable in the parse, including the LSTM history length, observation-loss threshold, prediction errors, CVAE latent dimension, and several network hyperparameters. Section 7 points to Appendix A for ablations and Appendix B for prediction-error results, but the supplied 18-page accepted manuscript ends without either appendix. The text also states `4 x 10^5` training iterations while displayed curves end at 5,000 or 10,000, without explaining the mismatch.

The NP-hardness discussion discretizes power for a nonlinear knapsack analogy but does not establish a global-optimality result for the original continuous problem. Communication energy, acceleration/deceleration energy, generalization beyond the simulated Eve process, and scaling beyond the two-pair extension remain unresolved.

## Relation to the corpus

This source combines [[friendly-jamming-uav]], [[physical-layer-security]], and maritime mobility with learned partial-observation control. [[huang-2026-uav-friendly-jamming-transsac]] shares the lead Jilin/NTU research cluster and SAC-based maritime jamming, while [[huang-2025-dual-aav-maritime-secure-cb]] uses collaborative beamforming rather than an advantage-conditioned generative policy. [[sun-2024-imssa-uav-secure-cb]] is adjacent on uncertain eavesdropper security, and [[li-2023-secure-marine-iot-jamming]] provides a marine cooperative-jamming comparator.

## Raw artifacts

- Parse: `raw/sources/Secure_Low-altitude_Maritime_Communications_via_Intelligent_Jamming/Secure_Low-altitude_Maritime_Communications_via_Intelligent_Jamming.md`
- Accepted-version PDF: `raw/sources/Secure_Low-altitude_Maritime_Communications_via_Intelligent_Jamming/Secure_Low-altitude_Maritime_Communications_via_Intelligent_Jamming.pdf`
- Figures: `raw/sources/Secure_Low-altitude_Maritime_Communications_via_Intelligent_Jamming/images/`

## Metadata notes

The supplied file is an accepted author version carrying 2026 copyright and DOI metadata. It identifies **IEEE Transactions on Mobile Computing** as the accepting journal but does not provide a final volume, issue, or journal page range; the 18 manuscript pages are not final pagination.
