---
type: source
modeling_card: required
title: "UAV-Aided Covert ISAC via Full-Duplex Jamming"
authors: ["Qunshu Wang", "Xiaoqi Qin", "Hu Jin", "Chunguo Li", "Nan Zhao", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3605370"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 3675-3687"
tags: [source, covert-communication, isac, full-duplex-jamming, location-uncertainty, beamforming, uav-trajectory]
related:
  - "[[wang-2026-covert-cognitive-radio]]"
  - "[[qunshu-wang]]"
  - "[[full-duplex-receiver-jamming]]"
  - "[[covert-communication]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[sensing-signal-assisted-covertness]]"
  - "[[cooperative-jamming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[deng-2025-covert-isac-trajectory]]"
  - "[[lin-2026-fc-ris-surveillance]]"
  - "[[yan-2026-uav-trajectory-monitoring]]"
  - "[[huang-2026-intelligent-jamming-maritime]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
  - "[[dusit-niyato]]"
  - "[[chunguo-li]]"
created: 2026-07-14
updated: 2026-07-16
---

# UAV-Aided Covert ISAC via Full-Duplex Jamming

## Citation

Wang, Q., Qin, X., Jin, H., Li, C., Zhao, N., & Niyato, D. (2026). *UAV-Aided Covert ISAC via Full-Duplex Jamming*. **IEEE Transactions on Wireless Communications, 25**, 3675-3687. DOI: 10.1109/TWC.2025.3605370.

## TL;DR

A terrestrial ISAC base station sends sensing under both warden hypotheses and adds a covert communication beam only under transmission. The intended UAV receiver simultaneously emits randomized jamming, trading radiometric covertness against residual self-interference and sensing interference.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna terrestrial ISAC base station illuminates one target and covertly communicates with a fixed-altitude full-duplex UAV. The UAV emits randomized artificial jamming, while one uncertain-location warden applies radiometric detection under Rayleigh fading.

**Problem & objective**: Problem (36) is a robust non-convex design that maximizes the UAV's covert transmission rate, $\max_{\mathbf W_c,\mathbf W_s,\mathbf Q}\sum_t R_b[t]$, under sensing, covertness, outage, power, and mobility constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Communication beam | $\mathbf w_c[t]$ | complex continuous vector | Covert downlink beam in slot $t$ |
| Sensing beam | $\mathbf w_s[t]$ | complex continuous vector | Target-illumination and masking beam |
| UAV trajectory | $\mathbf q_b[t]$ | continuous horizontal position | Full-duplex receiver position at fixed altitude |
| Convexification variables | $u[t],L[t]$ | continuous slacks | SDR and SCA surrogates for rate and distance terms |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 36a | Target echo SINR remains above $\Gamma_{\mathrm{th}}$ |
| 36b | The worst-case warden detection error satisfies the covertness threshold |
| 36c | BS communication and sensing beams respect the transmit-power budget |
| C4 | UAV outage probability remains below its reliability threshold |
| C5 | The trajectory satisfies fixed endpoints, flight region, and per-slot displacement limits |

**Algorithm**: Derive the infinite-sample radiometer and robust covertness bound → fix trajectory and optimize transmit beams with SDR and arithmetic-geometric-mean approximations → fix beams and update trajectory with SCA and distance slacks → alternate until the covert-rate objective stops increasing.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Wang et al. [x] studied UAV-aided covert integrated sensing and communication with a full-duplex jamming UAV receiver and an uncertain-location warden. They derived the optimal infinite-sample radiometer threshold and the average minimum detection error under the assumed fading and randomized-jamming model. The resulting robust problem maximizes covert transmission rate over communication and sensing beams and the UAV trajectory under echo-SINR, outage, power, mobility, and covertness constraints. Their alternating method applies semidefinite relaxation and arithmetic-geometric-mean approximations to beamforming and successive convex approximation to trajectory control. Simulations report higher covert rate than the evaluated fixed-trajectory and random-beamforming baselines.

## Model and guarantee scope

The paper derives the optimal infinite-sample radiometer threshold and model-specific minimum sum error under Rayleigh Alice-Willie fading and uniform UAV jamming power. Optimization enforces a conservative per-slot covertness bound under norm-bounded warden-location uncertainty, plus target echo-SINR, outage, power, and trajectory constraints.

SDR/AGM handles beamforming, SCA handles trajectory, and an outer AO loop has a nondecreasing bounded objective. There is no global joint optimum or stationary-point proof for the original problem. Covertness does not extend to finite samples, alternate detectors, multiple wardens, or misspecified uncertainty.

## Findings

Simulation reports higher rate than fixed-trajectory and random-beamforming baselines. More jamming raises modeled detection error but lowers reliable rate through residual self-interference; larger warden-location uncertainty lowers robust rate; tighter echo-SINR requirements reserve more sensing power and lower rate.

## Limitations

One receiver, one warden, one target, fixed altitude, infinite-channel-use radiometry, prescribed fading/distribution models, no propulsion energy, no legitimate-CSI uncertainty, and simulation-only evaluation. The echo-SINR table uses an inconsistent rate unit, several detector equations are OCR-damaged, and the paper's “optimal trajectory” wording exceeds its local AO/SCA evidence.

## Relation to the corpus

Where [[deng-2025-covert-isac-trajectory]] uses an ISAC sensing waveform as cover for aerial information transmission, this source also lets the legitimate receiver generate randomized [[full-duplex-receiver-jamming]]. It therefore connects [[sensing-signal-assisted-covertness]] and [[cooperative-jamming]], while making the resulting covertness-rate trade-off depend on residual self-interference.

Its observer roles contrast with [[lin-2026-fc-ris-surveillance]], where the legitimate station seeks to decode a suspicious signal. Its echo-SINR constraint also stops short of the motion-estimation and association pipeline in [[yan-2026-uav-trajectory-monitoring]]. [[huang-2026-intelligent-jamming-maritime]] uses a separate friendly jammer against Eve's payload decoder rather than Bob's full-duplex activity-detector mask. These distinctions are organized in [[aerial-observation-control-covertness-surveillance-and-monitoring]].

## Raw artifacts

- Parse: `raw/sources/UAV-Aided_Covert_ISAC_via_Full-Duplex_Jamming/UAV-Aided_Covert_ISAC_via_Full-Duplex_Jamming.md`
- Original PDF and extracted figures are in the same folder.
