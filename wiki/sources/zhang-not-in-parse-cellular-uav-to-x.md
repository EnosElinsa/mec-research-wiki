---
type: source
title: "Cellular UAV-to-X Communications: Design and Optimization for Multi-UAV Networks"
authors: ["Shuhang Zhang", "Hongliang Zhang", "Boya Di", "Lingyang Song"]
year: ""
url: ""
venue: ""
tags: [source, uav-communications, cellular-connected-uav, uav-to-uav, spectrum-sharing, resource-allocation, mobile-relaying]
related:
  - "[[uav-to-x-communication]]"
  - "[[cellular-connected-uav]]"
  - "[[device-to-device-communication]]"
  - "[[overlay-underlay-spectrum-access]]"
  - "[[uav-mobile-relaying]]"
  - "[[air-to-ground-channel-model]]"
  - "[[uav-trajectory-control]]"
created: 2026-07-12
updated: 2026-07-12
---

# Cellular UAV-to-X Communications: Design and Optimization for Multi-UAV Networks

## Citation

Zhang, S., Zhang, H., Di, B., & Song, L. *Cellular UAV-to-X Communications: Design and Optimization for Multi-UAV Networks*. Venue / year / DOI: **not in parse**.

## TL;DR

Builds a cellular UAV sensing network in which high-SNR UAVs upload directly to a base station through UAV-to-network links, while low-SNR UAVs forward data to nearby UAV relays through underlaid UAV-to-UAV links. A cooperative sense-and-send protocol and the iterative ISASOA solver jointly allocate subchannels and control speed along predetermined trajectories to maximize uplink sum rate.

## Problem

UAV-to-UAV spectrum reuse couples interference across U2U, U2N, and cellular-user links, while sensing UAVs must still finish predetermined paths by their deadlines and satisfy minimum U2U rates. The resulting binary/continuous subchannel-and-speed problem is NP-hard.

## System model

- One cellular cell contains a base station, `M` fixed cellular users, and `N` UAVs moving on predetermined trajectories.
- Each slot has sensing and transmission phases. An SNR threshold selects direct U2N mode or U2U relay mode, and a low-SNR UAV is paired with its nearest U2N-mode UAV.
- U2N links overlay cellular transmission, while U2U links reuse U2N and cellular-user subchannels as underlay.
- The objective maximizes U2N-plus-cellular-user uplink sum rate over U2N/CU subchannel assignment, U2U subchannel reuse, and per-slot UAV speed, subject to U2U-rate, speed, path-completion, fairness, and subchannel constraints.

## Method

The six-phase cooperative sense-and-send protocol covers sensing, reporting, mode selection, resource-allocation instructions, link establishment, and transmission. ISASOA then iterates three blocks: a relaxed linear program for U2N/CU subchannel allocation, a feasible-solution search plus branch-and-bound for U2U subchannel allocation, and convexified speed optimization. The paper proves convergence and shows that the U2N/CU relaxation retains binary solutions.

## Key findings

- The main setup uses 10 subchannels, 20 UAVs including 5 U2U-mode UAVs, 5 cellular users, 23 dBm transmit power, -96 dBm noise, 1 GHz carrier, at most 2 subchannels per link, maximum speed 10 m/slot, 300 m trajectories, minimum U2U rate 10 bit/(s Hz), and a 10 dB U2N-mode SNR threshold.
- UAV positions are sampled in a `2 km x 2 km x h_max` volume with `h_max` equal to 100 or 200 m, and reported curves aggregate more than 1,000 algorithm instances.
- A 50-slot horizon gives about 7% more uplink sum rate than 30 slots, and the 200 m maximum-height case gives about 3% more than the 100 m case.
- ISASOA reports about 10% more uplink sum rate than the greedy baseline. The greedy baseline obtains about 5% more total U2U rate, but leaves less capacity for U2N links.
- Uplink sum rate rises strongly with maximum speed up to 20 m/slot and becomes stable above 30 m/slot in the tested range.
- The stated complexity is `O((N_h(t) + M) 2^(N_l(t)))`, reflecting the U2U branch-and-bound block.

## Limitations / parse caveats

The evidence is theoretical analysis and simulation, not a deployment. Trajectory geometry is predetermined and only speed is controlled; cellular users are fixed. Speed convexification assumes LoS probability varies more slowly than path loss and that U2U distance is much larger than one-slot movement. The model is single-cell, and the paper leaves multi-cell association and inter-cell interference as extensions. The parse corrupts some coordinates and equation labels, so the page relies on stable prose and table values.

## Relation to the corpus

This source expands [[cellular-connected-uav]] from a direct aerial-user model into [[uav-to-x-communication]], where U2N and U2U modes cooperate within one cellular system. Its underlaid U2U relay path links [[device-to-device-communication]], [[overlay-underlay-spectrum-access]], and [[uav-mobile-relaying]], while its mobility variable is speed over a fixed path rather than free-form trajectory design.

## Raw artifacts

- Parse: `raw/sources/Cellular_UAV-to-X_Communications_Design_and_Optimization_for_Multi-UAV_Networks/Cellular_UAV-to-X_Communications_Design_and_Optimization_for_Multi-UAV_Networks.md`
- Origin PDF: `raw/sources/Cellular_UAV-to-X_Communications_Design_and_Optimization_for_Multi-UAV_Networks/Cellular_UAV-to-X_Communications_Design_and_Optimization_for_Multi-UAV_Networks.pdf`
- Figures: `raw/sources/Cellular_UAV-to-X_Communications_Design_and_Optimization_for_Multi-UAV_Networks/images/`
