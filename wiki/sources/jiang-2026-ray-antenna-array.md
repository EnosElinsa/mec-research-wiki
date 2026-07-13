---
type: source
title: "Ray Antenna Array Achieves Uniform Angular Resolution Cost-Effectively for Low-Altitude UAV Swarm ISAC"
authors: ["Haoyu Jiang", "Yong Zeng"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3643458"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 9200-9213, 2026"
tags: [source, ray-antenna-array, integrated-sensing-and-communication, uav-swarm, uniform-angular-resolution, ofdm-isac, music, zero-forcing, hybrid-beamforming]
related:
  - "[[ray-antenna-array]]"
  - "[[yong-zeng]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[extremely-large-scale-mimo]]"
  - "[[mmwave-radar-sensing]]"
  - "[[autonomous-uav-swarms]]"
  - "[[jing-2024-isac-trajectory-localization]]"
  - "[[lu-2026-uav-swarm-two-level-ma]]"
created: 2026-07-14
updated: 2026-07-14
---

# Ray Antenna Array Achieves Uniform Angular Resolution Cost-Effectively for Low-Altitude UAV Swarm ISAC

## Citation

Jiang, H., & Zeng, Y. (2026). *Ray Antenna Array Achieves Uniform Angular Resolution Cost-Effectively for Low-Altitude UAV Swarm ISAC*. **IEEE Transactions on Wireless Communications**, 25, 9200-9213. DOI: 10.1109/TWC.2025.3643458. Online publication: 19 December 2025; final-volume year: 2026.

## TL;DR

Adapts the [[ray-antenna-array]] to an OFDM low-altitude UAV-swarm ISAC receiver. Radially oriented simple ULAs directly combine their elements without per-element phase shifters, while a limited number of RF chains access selected ray outputs. Under stated coverage and element-pattern assumptions, the architecture has direction-independent angular resolution and supports AoA, delay, and Doppler estimation through MUSIC, zero-forcing separation, and a two-dimensional periodogram.

## Problem

Fully digital large arrays require an RF chain per element, while conventional hybrid arrays retain many phase shifters. A linear array also loses angular resolution away from boresight, which is problematic when a UAV swarm moves across a wide angular range. The paper studies whether radial array geometry can reduce the modeled hardware cost and preserve sensing resolution while supporting communication and bistatic sensing.

## System model

A single-antenna transmitter communicates with a multi-antenna receiver in a channel containing one LoS path and target-induced reflected paths. The receiver's RAA has many radially oriented simple ULAs, each with half-wavelength-spaced elements directly combined into one ray output. A ray-selection network connects the highest-energy outputs to the available RF chains after sweeping the ports.

The OFDM signal spans spatial, subcarrier, and symbol dimensions: AoA is encoded across selected rays, delay across subcarriers, and Doppler across symbols. The derivation assumes a cyclic prefix longer than the maximum delay, approximately constant Doppler within each OFDM symbol, and channel parameters that remain stable during the coherent processing interval.

## Method

The array orientations place adjacent ray peaks and first nulls according to the simple-ULA response. Under full directional coverage and an element beamwidth wider than the array-factor mainlobe, the analysis gives the direction-independent resolution `arcsin(2/M)` and proves it is no worse than that of an equal-array-gain conventional ULA, with equality only at boresight.

The receiver sweeps ray ports and retains the highest-energy outputs. An RAA-specific MUSIC spectrum estimates target AoAs because the manifold lacks the rotational invariance of a conventional ULA. Zero-forcing spatial filters then isolate each estimated direction, and a two-dimensional periodogram over subcarriers and OFDM symbols estimates delay and Doppler. A component-price calculation compares the switch-based RAA with a fully connected phase-shifter HBF array.

## Key findings

- The analytic result gives uniform angular resolution `arcsin(2/M)` under the paper's coverage and radiation-pattern assumptions; the equal-gain ULA is no better and matches it only at boresight.
- A worked 38-GHz component-price example estimates USD 46,278 for the RAA and USD 268,700 for the HBF comparator, or 17.2%. This is a cost model, not a bill of materials or prototype measurement.
- In figure-based simulations, both arrays resolve five closely spaced targets at moderate AoA, but the ULA loses detections as the swarm moves toward large AoA while RAA error remains nearly unchanged. The prose does not provide exact curve values or a universal failure threshold.
- The illustrated zero-forcing and delay-Doppler processing separates all five targets. Equal bandwidth and OFDM duration give the two architectures the same delay/Doppler resolution in the simulation.
- The communication plot shows higher RAA achievable rate than the selected ULA/HBF benchmark, especially with directional elements, but the text does not state an exact rate gain.
- For the main configuration, 201 ray ports and 8 RF chains require 26 sweeps within a 2048-symbol coherent interval; this overhead result is parameter-specific.

## Limitations

Evidence is analytical and simulation-based; there is no fabricated array, RF-network calibration, chamber measurement, or UAV flight test. The angular model is one-dimensional, while full 3-D coverage remains future work. The architecture uses more elements and a larger physical structure, and the price comparison omits packaging, cabling, insertion loss, power, weight, and aerodynamic effects. Inter-ray blockage, communication-decoding errors before sensing data removal, switching latency, and end-to-end processing runtime are not evaluated.

## Relation to the corpus

The paper contributes a receiver architecture to [[integrated-sensing-and-communication]], with [[mmwave-radar-sensing]]-adjacent angle/delay/Doppler processing at 39 GHz. It is relevant to [[extremely-large-scale-mimo]] through hardware scaling but does not study near-field propagation. [[jing-2024-isac-trajectory-localization]] shares UAV-ISAC localization context, while [[lu-2026-uav-swarm-two-level-ma]] and author [[yong-zeng]] connect it to a distinct movable-antenna swarm design. [[autonomous-uav-swarms]] is system context only; the paper does not optimize swarm control or coordination.

## Raw artifacts

- Parse: `raw/sources/Ray_Antenna_Array_Achieves_Uniform_Angular_Resolution_Cost-Effectively_for_Low-Altitude_UAV_Swarm_ISAC/Ray_Antenna_Array_Achieves_Uniform_Angular_Resolution_Cost-Effectively_for_Low-Altitude_UAV_Swarm_ISAC.md`
- Origin PDF: `raw/sources/Ray_Antenna_Array_Achieves_Uniform_Angular_Resolution_Cost-Effectively_for_Low-Altitude_UAV_Swarm_ISAC/Ray_Antenna_Array_Achieves_Uniform_Angular_Resolution_Cost-Effectively_for_Low-Altitude_UAV_Swarm_ISAC.pdf`
- Figures: `raw/sources/Ray_Antenna_Array_Achieves_Uniform_Angular_Resolution_Cost-Effectively_for_Low-Altitude_UAV_Swarm_ISAC/images/`
