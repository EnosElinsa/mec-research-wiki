---
type: source
title: "UAV-Aided Covert ISAC via Full-Duplex Jamming"
authors: ["Qunshu Wang", "Xiaoqi Qin", "Hu Jin", "Chunguo Li", "Nan Zhao", "Dusit Niyato"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3605370"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 3675-3687"
tags: [source, covert-communication, isac, full-duplex-jamming, location-uncertainty, beamforming, uav-trajectory]
related:
  - "[[full-duplex-receiver-jamming]]"
  - "[[covert-communication]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[sensing-signal-assisted-covertness]]"
  - "[[cooperative-jamming]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[deng-2025-covert-isac-trajectory]]"
  - "[[dusit-niyato]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV-Aided Covert ISAC via Full-Duplex Jamming

## Citation

Wang, Q., Qin, X., Jin, H., Li, C., Zhao, N., & Niyato, D. (2026). *UAV-Aided Covert ISAC via Full-Duplex Jamming*. **IEEE Transactions on Wireless Communications, 25**, 3675-3687. DOI: 10.1109/TWC.2025.3605370.

## TL;DR

A terrestrial ISAC base station sends sensing under both warden hypotheses and adds a covert communication beam only under transmission. The intended UAV receiver simultaneously emits randomized jamming, trading radiometric covertness against residual self-interference and sensing interference.

## Model and guarantee scope

The paper derives the optimal infinite-sample radiometer threshold and model-specific minimum sum error under Rayleigh Alice-Willie fading and uniform UAV jamming power. Optimization enforces a conservative per-slot covertness bound under norm-bounded warden-location uncertainty, plus target echo-SINR, outage, power, and trajectory constraints.

SDR/AGM handles beamforming, SCA handles trajectory, and an outer AO loop has a nondecreasing bounded objective. There is no global joint optimum or stationary-point proof for the original problem. Covertness does not extend to finite samples, alternate detectors, multiple wardens, or misspecified uncertainty.

## Findings

Simulation reports higher rate than fixed-trajectory and random-beamforming baselines. More jamming raises modeled detection error but lowers reliable rate through residual self-interference; larger warden-location uncertainty lowers robust rate; tighter echo-SINR requirements reserve more sensing power and lower rate.

## Limitations

One receiver, one warden, one target, fixed altitude, infinite-channel-use radiometry, prescribed fading/distribution models, no propulsion energy, no legitimate-CSI uncertainty, and simulation-only evaluation. The echo-SINR table uses an inconsistent rate unit, several detector equations are OCR-damaged, and the paper's “optimal trajectory” wording exceeds its local AO/SCA evidence.

## Relation to the corpus

Where [[deng-2025-covert-isac-trajectory]] uses an ISAC sensing waveform as cover for aerial information transmission, this source also lets the legitimate receiver generate randomized [[full-duplex-receiver-jamming]]. It therefore connects [[sensing-signal-assisted-covertness]] and [[cooperative-jamming]], while making the resulting covertness-rate trade-off depend on residual self-interference.

## Raw artifacts

- Parse: `raw/sources/UAV-Aided_Covert_ISAC_via_Full-Duplex_Jamming/UAV-Aided_Covert_ISAC_via_Full-Duplex_Jamming.md`
- Original PDF and extracted figures are in the same folder.
