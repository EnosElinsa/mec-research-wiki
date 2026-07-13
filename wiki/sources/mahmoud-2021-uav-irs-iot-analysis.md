---
type: source
title: "Intelligent Reflecting Surfaces Assisted UAV Communications for IoT Networks: Performance Analysis"
authors: ["Abdulla Mahmoud", "Sami Muhaidat", "Paschalis C. Sofotasios", "Ibrahim Abualhaol", "Octavia A. Dobre", "Halim Yanikomeroglu"]
year: 2021
url: "https://doi.org/10.1109/TGCN.2021.3068739"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, uav-mounted-ris, iot, performance-analysis, outage-probability, ergodic-capacity, symbol-error-rate, cascaded-channel]
related:
  - "[[uav-mounted-ris]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[air-to-ground-channel-model]]"
  - "[[octavia-a-dobre]]"
  - "[[halim-yanikomeroglu]]"
created: 2026-07-13
updated: 2026-07-13
---

# Intelligent Reflecting Surfaces Assisted UAV Communications for IoT Networks: Performance Analysis

## Citation

Mahmoud, A., Muhaidat, S., Sofotasios, P. C., Abualhaol, I., Dobre, O. A., & Yanikomeroglu, H. (2021). *Intelligent Reflecting Surfaces Assisted UAV Communications for IoT Networks: Performance Analysis*. **IEEE Transactions on Green Communications and Networking**. DOI: 10.1109/TGCN.2021.3068739.

> **Metadata grounding note.** The parse's first-page author line is truncated. The complete ordered author list, DOI, venue, and year were verified through the exact-title Crossref journal record and agree with the author biographies retained in the parse.

## TL;DR

Analyzes a static UAV carrying a planar IRS between one base station and one beyond-horizon IoT user with no direct LoS link. Under ideal phase alignment and an elevation-angle-dependent large-scale channel, it derives SNR bounds and performance expressions for error rate, capacity, and outage, showing the expected quadratic SNR scaling with IRS element count.

## System model

- One single-antenna BS communicates with one single-antenna ground IoT user only through an IRS mounted on a UAV.
- BS-IRS and IRS-user small-scale coefficients are independent complex Gaussian variables; ideal continuous phases cancel the cascaded phase element by element.
- Large-scale loss includes distance, elevation-dependent LoS probability, and the BS antenna's downtilt/sidelobe effect; one common path-loss value is used across each array link.
- The UAV position and IRS size are parameters for analysis, not optimized trajectories or online controls.

## Method

The paper derives upper and lower average-SNR bounds, then obtains an upper-bound SNR distribution and MGF for average symbol-error rate, ergodic capacity, outage probability, and outage capacity. A central-limit approximation handles large IRS arrays; Monte Carlo simulations check the expressions and placement trends.

## Key findings

- The analysis gives average received SNR proportional to the square of the number of reflecting elements, and the CLT approximation is reported close to simulation for **N >= 16**.
- In one distance sweep, capacity rises from **0.1574** at N=1 to **8.4148 bit/s/Hz** at N=64 for a 2300 m BS-user separation; the paper also reports 5% outage capacity **8.0912 bit/s/Hz** for that N=64 case.
- The reported capacity multipliers vary strongly with geometry and use N=1 as the denominator (for example, 53.46x at 2300 m and 1332.75x at 1150 m). They should not be generalized as a universal gain over a conventional relay or UAV link.
- Positioning the aerial IRS near either endpoint can help; the N=64 curve also exhibits a broad placement plateau in the reported setup.

## Limitations / interpretation

The study is analytical plus simulation, with no prototype or flight test. It assumes perfect instantaneous CSI, ideal continuous phase control, independent Rayleigh small-scale links even while LoS probability affects path loss, identical large-scale loss across all elements, one BS and one user, a static UAV, and no external interference. UAV propulsion, station keeping, channel estimation, and IRS control energy are omitted.

## Relation to the corpus

This is an early analytical anchor for [[uav-mounted-ris]]. Later corpus entries mainly optimize placement, trajectory, phase quantization, energy, or MEC decisions; this paper instead isolates the cascaded aerial-IRS link and derives interpretable error/capacity/outage behavior.

## Raw artifacts

- `raw/sources/Intelligent_Reflecting_Surfaces_Assisted_UAV_Communications_for_IoT_Networks_Performance_Analysis/Intelligent_Reflecting_Surfaces_Assisted_UAV_Communications_for_IoT_Networks_Performance_Analysis.md`
- Original PDF and extracted figures (`images/`) in the same folder.
