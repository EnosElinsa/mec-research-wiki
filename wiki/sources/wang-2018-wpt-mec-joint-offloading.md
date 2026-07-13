---
type: source
title: "Joint Offloading and Computing Optimization in Wireless Powered Mobile-Edge Computing Systems"
authors: ["Feng Wang", "Jie Xu", "Xin Wang", "Shuguang Cui"]
year: 2018
url: "https://doi.org/10.1109/TWC.2017.2785305"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, wireless-power-transfer, mobile-edge-computing, energy-beamforming, partial-offloading, resource-allocation, energy-efficiency]
related:
  - "[[simultaneous-wireless-information-and-power-transfer]]"
  - "[[energy-harvesting-mec]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[mao-2016-lodco-eh-mec-offloading]]"
  - "[[jie-xu]]"
created: 2026-06-04
updated: 2026-07-14
---

# Joint Offloading and Computing Optimization in Wireless Powered Mobile-Edge Computing Systems

## Citation

Wang, F., Xu, J., Wang, X., & Cui, S. (2018). *Joint Offloading and Computing Optimization in Wireless Powered Mobile-Edge Computing Systems*. **IEEE Transactions on Wireless Communications**, 17(3). DOI: 10.1109/TWC.2017.2785305. (Received 26 May 2017; accepted 12 December 2017; published 22 December 2017; current version 8 March 2018.)

## TL;DR

Proposes a unified **MEC + WPT** design where a multi-antenna AP broadcasts wireless power to charge multiple users; users rely entirely on harvested energy to execute computation tasks locally or offload partial tasks to the AP's MEC server via TDMA. Jointly optimizes AP energy transmit beamforming, per-user CPU frequencies, offloaded bit counts, and TDMA time allocation to **minimize total AP energy consumption** subject to per-user computation latency constraints. Derives the optimal solution in **semi-closed form**. Key finding: at the optimum, local computing is always beneficial (strictly positive local bits at every user).

## Problem framing

IoT devices are energy-constrained; replacing/recharging batteries is costly. WPT provides energy wirelessly from a dedicated AP. MEC allows task offloading to reduce local compute burden. Combining MEC and WPT so users execute entirely on harvested energy eliminates the need for on-device energy storage, but introduces strong coupling between the WPT (supply side) and MEC (demand side) optimization. This joint design was not previously studied at the time.

## System model

- **Multi-antenna AP** (integrated MEC server + energy transmitter). **K single-antenna users**, each with a computation task that can be partially offloaded.
- **Downlink WPT:** AP uses transmit energy beamforming over downlink; each user's rectifier harvests energy. Uplink for offloading is on an orthogonal frequency band.
- **Partial offloading:** each user partitions task into local bits + offloaded bits; local computation uses harvested energy; offloaded bits are transmitted via TDMA.
- **Objective:** minimize total AP energy consumption (WPT radiated energy + MEC computing energy for offloaded tasks), subject to per-user end-to-end latency constraints.
- **Convex reformulation** + KKT conditions yield a semi-closed-form optimal solution.

## Key findings

- At the optimal solution, **local computing is always strictly beneficial** — it is never optimal for a user to offload all bits; the optimal partition always leaves some bits for local computation (parse contribution bullets + Section II results).
- The proposed joint WPT+MEC design **significantly reduces AP energy consumption** compared to benchmark schemes without joint optimization (parse contribution bullets / Section IV).
- Optimal offloading rate and transmit power for each user depend critically on the channel power gain and circuit power (parse Section III analysis).
- The TDMA offloading protocol with energy beamforming achieves efficient spatial multiplexing of energy delivery.

## Limitations / future work

Single-hop TDMA offloading only; no relay or multi-hop. Non-linear energy harvesting (rectifier nonlinearity) not modeled — assumed linear. Static channel (CSI known perfectly at AP). The parse notes this is extended by subsequent works to include non-linear EH and stochastic channel models.

## Relation to the corpus

Foundational MEC + WPT paper establishing that **local computing is always beneficial** under wireless-powered partial offloading — a result complementing [[mao-2016-lodco-eh-mec-offloading]] (which uses Lyapunov for online EH-MEC). The energy transmit beamforming + TDMA MEC design recurs in [[an-2024-multilayer-ris-hap-swipt]] and [[chhea-2025-irs-uav-swipt-drl]]. Connects [[energy-harvesting-mec]] and [[simultaneous-wireless-information-and-power-transfer]] to the partial-offloading literature.

## Raw artifacts

- `raw/sources/Joint_Offloading_and_Computing_Optimization_in_Wireless_Powered_Mobile-Edge_Computing_Systems/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
