---
type: source
title: "Ampli-Flection for 6G: Active-RIS-Aided Aerial Backhaul With Full 3-D Coverage"
authors: ["Hong-Bae Jeon", "Chan-Byoung Chae"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3672500"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, active-ris, wireless-backhaul, aerial-base-station, uav-bs, energy-efficiency, beamforming, 6g]
related:
  - "[[aerial-active-ris-backhaul]]"
  - "[[active-ris]]"
  - "[[wireless-backhaul]]"
  - "[[intelligent-reflecting-surface]]"
  - "[[drone-cell-3d-placement]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[zhu-2024-crb-active-ris-isac]]"
  - "[[pan-2025-uav-ris-energy-efficient-comm]]"
  - "[[chan-byoung-chae]]"
created: 2026-07-11
updated: 2026-07-13
---

# Ampli-Flection for 6G: Active-RIS-Aided Aerial Backhaul With Full 3-D Coverage

## Citation

Jeon, H.-B., & Chae, C.-B. (2026). *Ampli-Flection for 6G: Active-RIS-Aided Aerial Backhaul With Full 3-D Coverage*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3672500.

## TL;DR

Proposes [[aerial-active-ris-backhaul]], a high-altitude active-RIS platform that reflects and amplifies blocked backhaul signals to support UAV base stations and ground users with full 3-D coverage. The paper optimizes platform placement, RIS array partitioning, phase control, and equal amplification gain to maximize UAV-BS energy efficiency.

## Problem framing

UAV base stations can rapidly cover traffic surges, but dense urban blockage makes their backhaul unreliable. Passive RISs can restore reflected paths but suffer multiplicative fading over long aerial cascaded links. Active RIS elements add amplification, at the cost of power consumption and dynamic noise, so the key question is whether aerial active RIS can improve backhaul energy efficiency after accounting for that cost.

## System model

- An urban region contains randomly distributed ground users served by stationary UAV-BSs.
- A ground source provides backhaul through a high-altitude aerial active RIS; the direct source-to-UAV-BS path is assumed blocked.
- The aerial RIS is modeled as a ULA with `N` active reflecting elements, equal-gain amplification, element-wise phase shifts, active hardware power, and dynamic noise.
- UAV-BS fronthaul throughput and backhaul rate are balanced so backhaul does not bottleneck the access link.
- The simulation setup includes `10^3` random user realizations, a `500 x 500 m` target region, 50 MHz backhaul bandwidth, `H = 180 m`, `N = 300`, and 16 source antennas in the default table.

## Method

The paper derives the minimum total power required to satisfy UAV-BS backhaul rates under active-RIS amplification and dynamic-noise terms. It uses MRT at the source, phase alignment/array partitioning to keep UAV-BSs in the RIS main lobe, equal amplification gain across active RIS elements, and a global-criterion/Pareto operating point for placement and phase-target selection. It then optimizes amplification gain against total source plus active-RIS power.

## Key findings

- Against an aerial AF relay, the proposed aerial-active-RIS architecture reports 25.48 dB and 27.19 dB total-power gains at `d_G = 1000 m` and `1200 m`.
- Compared with aerial passive RIS, the proposed algorithm reports about 32.20 dB and 30.17 dB gains at 800 m and 1200 m.
- With aerial-RIS height increasing from 160 m to 190 m, reported gains over passive-RIS benchmarks are about 31.87 dB and 31.28 dB.
- With `N = 120` and `N = 300`, the reported active-versus-passive gains are about 36.11 dB and 30.98 dB.
- The feasibility plot places the source-power upper bound around 12-15 dBm while simulated total power remains below 10 dBm, so the proposed settings remain feasible under the paper's assumptions.

## Limitations / future work

The conclusion does not state explicit future work. The analysis is simulation-based and assumes blocked direct backhaul, LoS-dominated aerial-RIS links, ULA geometry, equal active-RIS gain, stationary UAV-BSs, perfect/available channel information, and rate-balanced fronthaul/backhaul. It is a physical-layer backhaul paper rather than an MEC offloading formulation.

## Relation to the corpus

This source broadens [[active-ris]] from receiver-side anti-jamming and ISAC/MEC optimization toward [[wireless-backhaul]] for UAV-BSs. It is adjacent to [[drone-cell-3d-placement]] because UAV-BSs need 3-D service placement, but the paper's main variable is the aerial active-RIS backhaul platform rather than the access-cell UAV positions.

## Raw artifacts

- `raw/sources/Ampli-Flection_for_6G_Active-RIS-Aided_Aerial_Backhaul_With_Full_3-D_Coverage/Ampli-Flection_for_6G_Active-RIS-Aided_Aerial_Backhaul_With_Full_3-D_Coverage.md`
- Original PDF and extracted figures (`images/`) in the same folder.

## Metadata notes

The parsed Markdown is silent on DOI/venue/year metadata. DOI, venue, and year were verified by exact-title DOI lookup; technical claims and numbers above are grounded in the local parse.
