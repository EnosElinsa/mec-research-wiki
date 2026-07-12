---
type: source
title: "Energy-Efficient STAR-RIS Enhanced UAV-Enabled MEC Networks With Bi-Directional Task Offloading"
authors: ["Han Xiao", "Xiaoyan Hu", "Weile Zhang", "Wenjie Wang", "Kai-Kit Wong", "Kun Yang"]
year: 2025
url: "https://doi.org/10.1109/TWC.2025.3529252"
venue: "IEEE Transactions on Wireless Communications"
tags: [source, star-ris, uav-mec, task-offloading, energy-efficiency, trajectory-optimization, dinkelbach, sca]
related:
  - "[[star-ris]]"
  - "[[uav-mounted-ris]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[rotary-wing-propulsion-energy-model]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[ji-2021-uav-mec-noma-oma-energy-min]]"
  - "[[kai-kit-wong]]"
created: 2026-07-07
updated: 2026-07-13
---

# Energy-Efficient STAR-RIS Enhanced UAV-Enabled MEC Networks With Bi-Directional Task Offloading

## Citation

Xiao, H., Hu, X., Zhang, W., Wang, W., Wong, K.-K., & Yang, K. (2025). *Energy-Efficient STAR-RIS Enhanced UAV-Enabled MEC Networks With Bi-Directional Task Offloading*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2025.3529252.

## TL;DR

Proposes a UAV-enabled MEC system where a horizontally mounted [[star-ris]] lets one scheduled user offload task bits concurrently to a ground BS-MEC server and a UAV-MEC server. The energy-efficiency objective jointly optimizes user scheduling, resource allocation, STAR-RIS passive beamforming, and UAV trajectory with a BCD algorithm that combines Dinkelbach fractional programming and SCA.

## Problem

Existing two-way RIS/UAV MEC designs often make the UAV both an MEC server and a relay, requiring receive-decode-forward behavior across slots. This paper uses STAR-RIS transmission/reflection to create two simultaneous offloading paths, aiming to improve system energy efficiency while satisfying per-user QoS task-bit requirements.

## System model

- Network: a ground BS with MEC, a UAV with one antenna and an MEC server, a horizontally mounted STAR-RIS with multiple elements, and multiple single-antenna users.
- STAR-RIS protocol: energy splitting; each element can transmit and reflect incident signals simultaneously.
- Offloading: reflected components support user-to-BS offloading, and transmitted components support user-to-UAV offloading.
- Access: TDMA user scheduling; only one user is selected to offload in each time slot.
- Channels: LoS is assumed for ground-user/BS links through the aerial STAR-RIS, and the UAV-to-STAR-RIS link is modeled as a near-field channel because of the short fixed distance.
- Energy: the objective uses completed task bits over total energy, including a rotary-wing UAV flying-energy model and UAV/communication-side energy terms as defined in the parse.

## Method

The fractional energy-efficiency problem is transformed with Dinkelbach's algorithm and separated into three blocks: resource allocation plus user scheduling, STAR-RIS passive beamforming, and UAV trajectory. The subproblems are solved with SCA and closed-form/MRT-style phase updates where available, then iterated in a BCD loop. The paper reports convergence and compares against conventional RIS, fixed-trajectory, heuristic, and SDR-style baselines.

## Key findings

- Energy efficiency improves as the number of STAR-RIS elements increases, with diminishing returns; the proposed scheme gains most when the element count is limited.
- Mission duration has a non-monotonic effect: more time initially helps trajectory optimization, but after the channel-quality benefit saturates, extra UAV energy can reduce energy efficiency.
- Increasing UAV MEC CPU frequency improves energy efficiency with diminishing returns; increasing required CPU cycles per bit reduces energy efficiency.
- Higher QoS task-bit requirements reduce energy efficiency, especially once UAV computation energy becomes the dominant cost.
- In the reported task-allocation plot, the UAV handles most offloaded bits, while users with more scheduled slots can send more bits toward the BS path.

## Limitations / future work

The model is simulation-based and assumes centralized optimization, known geometry/CSI, a single-antenna UAV, and one scheduled user per time slot. The energy-efficiency definition in the parse excludes the energy used to process user tasks received at the BS, which is important when interpreting BS-offloading gains.

## Relation to the corpus

This source is the closest counterpart to [[mohammadi-2026-star-ris-uav-mec-noma]]. Both use UAV-mounted [[star-ris]] for aerial-terrestrial MEC, but Xiao et al. maximize energy efficiency with TDMA and bidirectional task offloading through a horizontally mounted STAR-RIS, while Mohammadi et al. minimize weighted energy under NOMA and mode-switching STAR-RIS elements. It also sits in the broader [[task-offloading]] and [[uav-trajectory-control]] optimization family anchored by [[ji-2021-uav-mec-noma-oma-energy-min]] and related SCA/AO sources.

## Raw artifacts

- Parse: `raw/sources/Energy-Efficient STAR-RIS Enhanced UAV-Enabled MEC Networks With Bi-Directional Task Offloading/Energy-Efficient STAR-RIS Enhanced UAV-Enabled MEC Networks With Bi-Directional Task Offloading.md`
- Origin PDF: `raw/sources/Energy-Efficient STAR-RIS Enhanced UAV-Enabled MEC Networks With Bi-Directional Task Offloading/Energy-Efficient STAR-RIS Enhanced UAV-Enabled MEC Networks With Bi-Directional Task Offloading.pdf`
- Figures: `raw/sources/Energy-Efficient STAR-RIS Enhanced UAV-Enabled MEC Networks With Bi-Directional Task Offloading/images/`
