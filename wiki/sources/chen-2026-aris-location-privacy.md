---
type: source
title: "RIS-Based Communication Enhancement and Location Privacy Protection in UAV Networks"
authors: ["Ziqi Chen", "Jun Du", "Chunxiao Jiang", "Tony Q. S. Quek", "Zhu Han"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3655342"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 11270-11285"
tags: [source, active-ris, location-privacy, artificial-noise, virtual-partition, uav-network, crlb]
related:
  - "[[virtual-partitioned-active-ris-location-privacy]]"
  - "[[active-ris]]"
  - "[[cramer-rao-bound]]"
  - "[[physical-layer-security]]"
  - "[[jun-du]]"
  - "[[chunxiao-jiang]]"
  - "[[tony-q-s-quek]]"
  - "[[zhu-han]]"
created: 2026-07-14
updated: 2026-07-14
---

# RIS-Based Communication Enhancement and Location Privacy Protection in UAV Networks

## Citation

Chen, Z., Du, J., Jiang, C., Quek, T. Q. S., & Han, Z. (2026). *RIS-Based Communication Enhancement and Location Privacy Protection in UAV Networks*. **IEEE Transactions on Wireless Communications, 25**, 11270-11285. DOI: 10.1109/TWC.2026.3655342.

## TL;DR

Adds an artificial-noise generator to an active RIS and virtually partitions its elements between legitimate-UAV communication and malicious-UAV RSS-localization interference, trading sum rate against source-location error.

## Problem and system model

A multi-antenna source UAV communicates with legitimate single-antenna receiver UAVs through an active RIS. Colluding malicious UAVs use received signal strength and their known locations to estimate the source position. The source, RIS, and legitimate receivers share location information; the quasi-static source is sufficiently distant for a plane-wave model.

Unlike designs requiring the source to emit artificial noise, the RIS contains its own controllable phase, reflection amplifier, noise generator, and power supply.

## Method

[[virtual-partitioned-active-ris-location-privacy]] divides elements and power between ARIS-CE for communication and one ARIS-LI partition per malicious UAV. An RSS Fisher-information derivation supplies the localization CRLB. Closed-form average-channel allocation chooses partition sizes and power; fractional-programming alternating optimization updates source beamforming and ARIS-CE precoding, while FP and semidefinite programming update ARIS-LI precoding and artificial-noise factors.

## Key findings

- Beyond 400 m malicious-UAV distance, adaptive partitioning raises localization RMSE by 37.65% while reducing legitimate sum rate by 3.69% relative to fixed partition/power.
- Relative to an unpartitioned baseline, the same case gives 4.41 times larger localization error at 9.96% lower sum rate.
- At 200 m, localization RMSE rises 148.53% while sum rate falls 21.21% relative to fixed partitioning.
- With 200 RIS elements, adaptive partitioning increases localization RMSE by 138.64% relative to fixed partitioning. With 14 malicious UAVs, the proposed scheme increases RMSE by 258.16% at a 12.8% sum-rate cost; the comparison sentence does not explicitly identify its baseline.
- Increasing the privacy weight changes the partition until the communication constraint becomes active around weight 0.8 in the tested setup.

## Limitations

Evidence is analytical and simulation-only. The model assumes quasi-static geometry, shared legitimate locations, colluding malicious receivers, available channel feedback, ideal controllable active-RIS noise generation, and no mobility/trajectory dynamics. Closed-form partitioning relies on average-channel approximations and neglected small terms; alternating FP/SDP is computationally heavy and does not prove global optimality.

## Relation to the corpus

This source protects position rather than message secrecy: the adversary may receive signals but should estimate the source location poorly. It therefore complements [[physical-layer-security]] and is distinct from [[trajectory-privacy]], which constrains where a UAV route exposes sensitive areas.

## Raw artifacts

- Parse: `raw/sources/RIS-Based_Communication_Enhancement_and_Location_Privacy_Protection_in_UAV_Networks/RIS-Based_Communication_Enhancement_and_Location_Privacy_Protection_in_UAV_Networks.md`
- Origin PDF and extracted figures (`images/`) are in the same folder.
