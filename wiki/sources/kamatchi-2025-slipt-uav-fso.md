---
type: source
title: "SLIPT Enabled Ground-to-UAV FSO Communication for SAGNET in 6G-IoT Systems"
authors: ["Kavitha Kamatchi", "Kavitha Pillappan", "V. Angayarkanni", "Prabu Krishnan"]
year: 2025
url: "https://doi.org/10.1109/TGCN.2024.3514689"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), 9(3), 1268-1279"
tags: [source, simultaneous-lightwave-information-and-power-transfer, free-space-optical-communication, ground-to-uav, energy-harvesting, optical-channel-modeling, 6g-iot]
related:
  - "[[simultaneous-lightwave-information-and-power-transfer]]"
  - "[[ground-to-uav-fso-channel]]"
  - "[[fov-aware-optical-uav-reception]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[wireless-power-transfer]]"
  - "[[energy-harvesting-mec]]"
  - "[[an-2024-multilayer-ris-hap-swipt]]"
created: 2026-07-14
modeling_card: not_applicable
updated: 2026-07-16
---

# SLIPT Enabled Ground-to-UAV FSO Communication for SAGNET in 6G-IoT Systems

## Citation

Kamatchi, K., Pillappan, K., Angayarkanni, V., & Krishnan, P. (2025). *SLIPT Enabled Ground-to-UAV FSO Communication for SAGNET in 6G-IoT Systems*. **IEEE Transactions on Green Communications and Networking, 9**(3), 1268-1279. DOI: 10.1109/TGCN.2024.3514689.

## TL;DR

Analyzes a hovering UAV that receives information and harvests energy from the same ground-to-UAV free-space optical signal. Closed-form harvested-energy, outage, and M-PSK symbol-error expressions compare AC-DC separation, time switching, power splitting, and hybrid time-switching/power-splitting receivers under atmospheric attenuation, Malaga turbulence, pointing error, and field-of-view interruption. In the tested settings, the hybrid TSPS receiver harvests the most energy, while beamwidth and receiver FOV expose a reliability-energy tradeoff.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Kamatchi et al. [x] analyzed simultaneous lightwave information and power transfer on a hovering ground-to-UAV free-space optical link. They derived closed-form harvested-energy, outage-probability, and M-PSK symbol-error expressions for AC-DC separation, time switching, power splitting, and hybrid time-switching and power-splitting receivers under atmospheric attenuation, Malaga turbulence, pointing error, and field-of-view interruption. Parameter sweeps examined distance, weather, turbulence, beamwidth, field of view, and angle-of-arrival fluctuations. The hybrid TSPS receiver produced the largest harvested energy among the tested methods and reached 0.04 mJ under strong turbulence. The reported design also achieved a symbol error rate of $10^{-4}$ at 30 dB and identified field-of-view values that balance interruption against background noise.

## Problem framing

UAV endurance is battery-limited, yet optical air-ground links are expected to provide high-rate connectivity in 6G-IoT integrated networks. The paper asks whether one optical waveform can carry data and replenish UAV energy through [[simultaneous-lightwave-information-and-power-transfer]], and how weather, turbulence, misalignment, angle-of-arrival fluctuations, beamwidth, and receiver FOV shape the result.

## System model

- One ground FSO transmitter serves a hovering UAV equipped with a SLIPT receiver. Harvested energy may support a later RF/FSO relay hop, but that hop is not modeled.
- Subcarrier intensity modulation/direct detection carries M-PSK symbols on an RF subcarrier added to a DC-biased optical signal. Peak-current and nonnegative-intensity constraints prevent clipping and negative optical intensity.
- Four receivers are evaluated: AC-DC separation (ADS), time switching (TS), power splitting (PS), and time switching-power splitting (TSPS).
- The [[ground-to-uav-fso-channel]] combines Beer-Lambert atmospheric attenuation, generalized Malaga turbulence, nonzero-boresight pointing error, and binary interruption when angle of arrival exceeds the receiver FOV.
- Gaussian position and orientation deviations lead to modified-Rayleigh approximations for radial displacement and angle of arrival; the resulting channel and SNR distributions are written with Meijer-G functions.

## Method

The paper derives a unified composite-channel PDF/CDF, substitutes each receiver's active duration and current into a photovoltaic harvested-energy model, obtains outage from the SNR CDF, and averages conditional M-PSK SER over the SNR density. Numerical sweeps then compare receiver strategy, time-switching factor `tau`, power-splitting factor `rho`, link distance, weather, turbulence, pointing severity, beam waist, FOV, angle-of-arrival spread, and average SNR. This is an analytical performance study rather than a joint resource-allocation or trajectory-optimization problem.

## Key findings

- TSPS provides the largest harvested energy among the four tested strategies because it harvests during both phases. The abstract states **0.04 mJ under strong turbulence**.
- **Figure-derived (Fig. 5):** at about 100 m under strong turbulence and beam waist `w_z = 3 m`, approximate harvested energies are 0.040/0.033 mJ for TSPS, 0.034/0.027 mJ for ADS, 0.031/0.024 mJ for TS, and 0.020/0.016 mJ for PS at FOVs of 12/6 mrad, respectively. These are visual plot readings, not tabulated values.
- The text discussing Fig. 6 states that reducing pointing severity by changing the coefficient from 5.07 to 9.02 raises harvested energy by **0.22 mJ for TSPS** and about **0.015 mJ for ADS**. The TSPS value conflicts with the plot's roughly hundredths-of-a-mJ scale and is retained as a stated inconsistency.
- For a 200 m link, the reported optimal FOVs are 12, 20, and 32 mrad for angle-of-arrival spreads of 3.2, 6.4, and 9.9 mrad. A wider FOV initially reduces interruption, but background noise/interference eventually offsets that benefit; this grounds [[fov-aware-optical-uav-reception]].
- To retain at least half the clear-air harvested energy, the stated maximum ranges are 370 m in haze, 270 m in moderate rain, and 220 m in heavy rain.
- Outage worsens with distance, pointing-error severity, and threshold SNR. The abstract reports SER of `10^-4` at 30 dB SNR; for the illustrated 250 m case with `tau = rho = 0.5`, TSPS has lower frame-scaled average SER than ADS.
- Larger beamwidth can improve SER by reducing pointing sensitivity, subject to the paper's condition `zeta_mod^2 >= beta`, but excessive beam spreading reduces harvested energy.

## Limitations / future work

The model is a quasi-static single link with a hovering UAV: it omits trajectory and propulsion energy, battery/charging dynamics, the proposed second relay hop, hardware experiments, and field-channel validation. Results depend on the Malaga/modified-Rayleigh approximations, Gaussian motion/orientation errors, ideal receiver branch separation and switching, SIM/DD M-PSK, and the photovoltaic energy model.

Several formulation details require care. The PS derivation scales signal and AWGN by the same `rho` and therefore sets PS SER equal to ADS SER, without splitter loss, extra receiver noise, circuit power, or nonlinear hardware. TS/TSPS SER is scaled by information-mode duration, which mixes decoded-symbol reliability with frame-averaged error contribution. Equation (11) adds TSPS phase currents without explicit `tau` and `1-tau` weights, whereas the operative final harvested-energy expression in equation (36) weights phase energies. Equation (45)'s minimum-beamwidth expression is malformed in the parse and should be checked against the PDF before algebraic reuse.

The title says **SAGNET**, while the body repeatedly defines **SAGIN** as Space-Air-Ground Integrated Network; the page preserves that title/body inconsistency. The authors propose adaptive power allocation and beam pointing as future work.

## Relation to the corpus

This source is the corpus's optical [[simultaneous-lightwave-information-and-power-transfer]] anchor and a focused [[ground-to-uav-fso-channel]] analysis. It complements the RF/HAP SWIPT receiver in [[an-2024-multilayer-ris-hap-swipt]] but studies a single optical uplink rather than an MEC offloading system or a joint network optimizer. Its relation to [[wireless-power-transfer]] and [[energy-harvesting-mec]] is therefore neighboring rather than equivalent, while its body-level architecture belongs to [[space-air-ground-integrated-network]].

## Raw artifacts

- `raw/sources/SLIPT_Enabled_Ground-to-UAV_FSO_Communication_for_SAGNET_in_6G-IoT_Systems/SLIPT_Enabled_Ground-to-UAV_FSO_Communication_for_SAGNET_in_6G-IoT_Systems.md`
- `raw/sources/SLIPT_Enabled_Ground-to-UAV_FSO_Communication_for_SAGNET_in_6G-IoT_Systems/SLIPT_Enabled_Ground-to-UAV_FSO_Communication_for_SAGNET_in_6G-IoT_Systems.pdf`
- Extracted figures in `raw/sources/SLIPT_Enabled_Ground-to-UAV_FSO_Communication_for_SAGNET_in_6G-IoT_Systems/images/`.

## Metadata notes

The Markdown parse supplies the title and author order but omits the final journal header. Volume, issue, pages, DOI, and 2025 publication metadata are taken from the embedded first-page PDF header; the paper was published online in December 2024 and appears in the September 2025 issue.
