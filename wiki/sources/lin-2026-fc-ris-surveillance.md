---
type: source
title: "UAV-Borne FC-RIS Empowered Wireless Information Surveillance With Threshold-Based Antenna Selection"
authors: ["Shuying Lin", "Yulong Zou", "Hongyu Li", "Bin Li", "Derrick Wing Kwan Ng"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3623963"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 6160-6176"
tags: [source, wireless-information-surveillance, monitoring-success-probability, fully-connected-ris, antenna-selection, uav-mounted-ris]
related:
  - "[[wireless-information-surveillance]]"
  - "[[monitoring-success-probability]]"
  - "[[fully-connected-ris]]"
  - "[[threshold-based-antenna-selection]]"
  - "[[beyond-diagonal-ris]]"
  - "[[uav-mounted-ris]]"
  - "[[physical-layer-security]]"
  - "[[two-timescale-optimization]]"
  - "[[air-to-ground-channel-model]]"
  - "[[guo-2024-multiuav-proactive-eavesdropping]]"
  - "[[wang-2026-covert-cognitive-radio]]"
  - "[[wang-2026-fd-covert-isac]]"
  - "[[zhan-2026-star-ris-aerial-monitoring]]"
  - "[[yan-2026-uav-trajectory-monitoring]]"
  - "[[aerial-observation-control-covertness-surveillance-and-monitoring]]"
  - "[[derrick-wing-kwan-ng]]"
created: 2026-07-14
updated: 2026-07-16
modeling_card: required
---

# UAV-Borne FC-RIS Empowered Wireless Information Surveillance With Threshold-Based Antenna Selection

## Citation

Lin, S., Zou, Y., Li, H., Li, B., & Ng, D. W. K. (2026). *UAV-Borne FC-RIS Empowered Wireless Information Surveillance With Threshold-Based Antenna Selection*. **IEEE Transactions on Wireless Communications, 25**, 6160-6176. DOI: 10.1109/TWC.2025.3623963.

## TL;DR

A UAV-borne fully connected RIS creates the legitimate monitor's otherwise blocked reception path for a suspicious transmission. Reflecting-sub-link CSI selects one receive antenna before a single FC-RIS optimization, with round-robin, full-search, and threshold schemes trading monitoring success probability against CSI and examination overhead.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A suspicious source transmits to a suspicious destination while a legitimate monitor with multiple antennas listens through a UAV-borne fully connected RIS. The direct source-monitor path is blocked; one monitor antenna is selected per slot, and channels combine distance-dependent loss, LoS probability, and Nakagami fading.

**Problem & objective**: FC-RIS wireless-information-surveillance design, a two-timescale probabilistic optimization, maximizes monitoring success probability (MSP), $\max \Pr\{R_{\mathrm{LM}}>R_{\mathrm{SD}}\}$, while selecting an antenna, configuring the FC-RIS, and placing the UAV under a monitoring non-outage constraint.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Monitor antenna selection | $a_n$ | binary, one antenna | Antenna used by the legitimate monitor |
| FC-RIS scattering matrix | $\mathbf S$ | complex symmetric unitary | Fully connected RIS configuration |
| UAV-RIS location | $\mathbf q$ | continuous 3-D position | Long-term aerial platform placement |
| TAS threshold | $\gamma_{th}$ | continuous, nonnegative | Threshold used by sequential antenna selection |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Exactly one monitor antenna is selected in each slot |
| C2 | FC-RIS scattering matrix is symmetric, unitary, and lossless |
| C3 | The selected monitor rate satisfies the monitoring event against the suspicious-destination rate |
| C4 | UAV placement remains in the allowed flight region and obeys the average monitoring non-outage constraint |
| C5 | TAS accepts the first antenna above $\gamma_{th}$ and falls back to the maximum-gain antenna otherwise |

**Algorithm**: Select an antenna by round-robin, full-search, or threshold-based TAS → configure FC-RIS with matrix decomposition and Cauchy-Schwarz alignment → derive MSP/order-statistic expressions → optimize long-term placement with statistical CSI and short-term selection/configuration with instantaneous CSI.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Lin et al. [x] studied wireless information surveillance using a UAV-borne fully connected RIS and a multi-antenna legitimate monitor. They formulated a monitoring-success-probability design that selects one monitor antenna and configures the symmetric-unitary FC-RIS while placing the UAV under a monitoring non-outage condition. The AS-FRRC framework uses reflecting-channel CSI to select an antenna, then obtains the FC-RIS configuration through matrix decomposition and Cauchy-Schwarz phase alignment. Round-robin, full-search, and threshold-based selection trade monitoring probability against CSI and examination overhead, while statistical or large-scale CSI supports the long-term UAV placement. Numerical analysis reports higher MSP for UAV-borne FC-RIS schemes than corresponding diagonal-RIS and terrestrial-RIS surveillance schemes in the evaluated settings.

## Problem

Monitoring succeeds when the selected legitimate-monitor antenna's achievable rate exceeds the suspicious destination's rate. The paper seeks lower-cost joint antenna selection and FC-RIS configuration, using [[monitoring-success-probability]] as the main metric, and separately chooses the UAV-RIS location from statistical or large-scale CSI by maximizing an upper bound on average monitoring rate subject to an average monitoring non-outage condition.

## System model

A suspicious source communicates with a suspicious destination over a direct and FC-RIS-reflected path. A passive legitimate monitor has multiple co-located receive antennas, but its direct source link is blocked, so it receives only through an $L$-element [[uav-mounted-ris]]. Channels combine distance-dependent loss, elevation-dependent LoS probability, and Nakagami-$m$ fading.

The ideal [[fully-connected-ris]] uses a complex symmetric, unitary scattering matrix rather than a diagonal phase matrix. The main schemes select one monitor antenna per slot: round-robin RAS-FR, maximum-reflecting-gain ASC-FRRC, or sequential [[threshold-based-antenna-selection|TAS-FRRC]], which accepts the first antenna above a threshold and falls back to the maximum if none qualifies.

## Method

The AS-FRRC framework selects an antenna from FC-RIS-to-monitor reflecting-channel CSI, then configures the FC-RIS once for that antenna through a matrix decomposition and Cauchy-Schwarz phase alignment. It derives closed-form MSP expressions using Gamma/order-statistic models and an exponential approximation for the suspicious composite-channel gain.

The [[two-timescale-optimization|two-timescale design]] uses statistical or large-scale CSI for long-term UAV-RIS placement and instantaneous reflecting-channel CSI for short-term selection and configuration. At fixed altitude and under equal path-loss exponents, the horizontal-placement problem reduces to cascaded path-gain maximization under the monitoring-rate bound; altitude behavior is studied numerically rather than globally optimized.

## Guarantee scope and findings

For one selected antenna, the FC-RIS construction is reported, by attribution to prior work, to attain the Cauchy-Schwarz upper bound under the ideal symmetric-unitary model. This is not a global-optimality result for the joint selection, configuration, and location problem. The horizontal placement result assumes fixed altitude and equal path-loss exponents, while the MSP closed forms require integer Nakagami parameters and an exponential channel-gain approximation. The asymptotic MSP-to-one result is model-scoped and does not guarantee finite-$L$ or hardware-robust monitoring.

One FC-RIS optimization costs $O(L^3)$, versus $O(NL^3)$ when repeated for all $N$ antennas, excluding common comparison costs. Analytical MSP curves agree closely with Monte Carlo markers in the tested settings. Raising the TAS-FRRC threshold improves MSP while increasing CSI and examination overhead; its low- and high-threshold limits approach round-robin and full-search behavior, respectively. FC-RIS schemes outperform corresponding diagonal-RIS schemes across the plotted ranges, with no exact percentage gain stated in the prose.

## Limitations

The analysis assumes a passive monitor, blocked direct source-monitor link, co-located antennas with identical large-scale fading, one selected RF chain, ideal lossless symmetric-unitary FC-RIS hardware, integer Nakagami parameters, and independent channel components. The tractable placement result fixes altitude and equalizes path-loss exponents; full 3D placement is not solved globally. UAV energy, hardware loss, mutual-coupling error, control latency, and synchronization imperfections are not modeled. Algorithm 1, Proposition 1's equation number, the two-timescale discussion, and the simulation table contain OCR or internal inconsistencies, so exact formulas and reconstructed default parameters require PDF verification.

## Relation to the corpus

This source specializes [[beyond-diagonal-ris]] for [[wireless-information-surveillance]], using passive channel shaping rather than the proactive jamming in [[guo-2024-multiuav-proactive-eavesdropping]]. It connects [[physical-layer-security]] to a partial-sub-link-CSI antenna-selection design: the threshold directly controls the performance-overhead trade-off, while long-term aerial placement follows the corpus's [[two-timescale-optimization]] pattern.

The legitimate monitor's desired decode event differs from the wardens' activity tests in [[wang-2026-covert-cognitive-radio]] and [[wang-2026-fd-covert-isac]]. It also differs from camera observation in [[zhan-2026-star-ris-aerial-monitoring]] and echo-based trajectory tracking in [[yan-2026-uav-trajectory-monitoring]]. The shared aerial channel-control surface and the incompatible observer outcomes are separated in [[aerial-observation-control-covertness-surveillance-and-monitoring]].

## Raw artifacts

- Parse: `raw/sources/UAV-Borne_FC-RIS_Empowered_Wireless_Information_Surveillance_With_Threshold-Based_Antenna_Selection/UAV-Borne_FC-RIS_Empowered_Wireless_Information_Surveillance_With_Threshold-Based_Antenna_Selection.md`
- Origin PDF: `raw/sources/UAV-Borne_FC-RIS_Empowered_Wireless_Information_Surveillance_With_Threshold-Based_Antenna_Selection/UAV-Borne_FC-RIS_Empowered_Wireless_Information_Surveillance_With_Threshold-Based_Antenna_Selection.pdf`
- Figures: `raw/sources/UAV-Borne_FC-RIS_Empowered_Wireless_Information_Surveillance_With_Threshold-Based_Antenna_Selection/images/`
