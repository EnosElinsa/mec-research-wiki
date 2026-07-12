---
type: source
title: "Energy Efficient Resource Allocation for Wireless Powered UAV Wireless Communication System With Short Packet"
authors: ["Jin Xie", "Zheng Chang", "Xijuan Guo", "Timo Hämäläinen"]
year: 2023
url: "https://doi.org/10.1109/TGCN.2022.3218314"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 7, no. 1, pp. 101-113"
tags: [source, wireless-power-transfer, short-packet-communication, finite-blocklength, uav-hybrid-access-point, energy-efficiency, resource-allocation, iot]
related:
  - "[[wireless-power-transfer]]"
  - "[[finite-blocklength-urllc]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[zheng-chang]]"
  - "[[xu-2018-uav-wpt-trajectory]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[wu-2024-urllc-uav-mec-latency]]"
  - "[[wang-2026-glint-aoi-wireless-powered-edge]]"
created: 2026-07-13
updated: 2026-07-13
---

# Energy Efficient Resource Allocation for Wireless Powered UAV Wireless Communication System With Short Packet

## Citation

Xie, J., Chang, Z., Guo, X., & Hämäläinen, T. (2023). *Energy Efficient Resource Allocation for Wireless Powered UAV Wireless Communication System With Short Packet*. **IEEE Transactions on Green Communications and Networking**, 7(1), 101-113. DOI: 10.1109/TGCN.2022.3218314.

## TL;DR

A fixed-altitude UAV hybrid access point first powers IoT devices and then receives their TDMA finite-blocklength uploads. Alternating SCA and fractional-programming updates optimize horizontal placement, downlink WPT powers, and a continuous symbol-allocation relaxation; heuristic rounding restores integer frame symbols.

## Problem

Short-packet rates depend jointly on where the UAV hovers, how long it transfers energy, how uplink symbols are split among devices, and how much WPT power each device receives. The resulting mixed-integer fractional problem must preserve reliability and a finite frame budget.

## System model

- One multi-antenna UAV acts as a hybrid access point for fixed single-antenna IoT devices at a fixed flight altitude.
- A frame first allocates `n_0 T_c` to downlink WPT, then gives each device `n_k T_c` for TDMA uplink transmission.
- Downlink and uplink channels use quasi-static Nakagami fading. Each device immediately spends all modeled harvested energy on its upload.
- The finite-blocklength rate includes decoding-error probability and channel dispersion rather than using Shannon capacity alone.
- Energy efficiency divides successfully decoded aggregate throughput by downlink WPT energy. Propulsion, hovering, circuitry, storage losses, and device circuitry are omitted.

## Method

The solver relaxes integer blocklengths and alternates three blocks. A Taylor/SCA surrogate and KKT root update the UAV location; a concave lower bound plus a Dinkelbach-style subtractive transform and Lambert-W expression update blocklengths; and another fractional/KKT dual routine updates WPT powers. Largest-remainder rounding restores integer symbols before placement and power are recomputed.

## Key findings

- The proposed blocklength allocation nearly overlaps exhaustive search for the small comparison and substantially exceeds equal allocation.
- Energy efficiency increases with total frame blocklength and falls as the number of served devices grows in the reported simulations.
- Joint position, blocklength, and power optimization outperforms the three partial-optimization variants across the decoding-error sweep.
- The prose reports an optimum near `7 dBm` per-device WPT power: efficiency rises below that point and falls above it. The alternating routine stabilizes in roughly six iterations in the displayed convergence study.

## Limitations / parse caveats

The study is simulation-only and optimizes one static hover point with linear harvesting, fixed decoding error, known device locations/channels, and immediate use of all harvested energy. It omits propulsion, battery dynamics, rectifier nonlinearity, CSI overhead, and mobility. Integer conversion is heuristic and has no stated optimality bound. The parse leaves the energy norm undefined, uses natural logarithms while labeling the metric bits per channel use per joule, damages several SCA derivatives and the convergence chain, duplicates one Fig. 6 legend label, and gives Fig. 8 the wrong caption.

## Relation to the corpus

This source connects [[wireless-power-transfer]] with [[finite-blocklength-urllc]] at a static UAV HAP. [[xu-2018-uav-wpt-trajectory]] optimizes delivered energy rather than the short-packet return link, [[zhou-2018-uav-wireless-powered-mec]] uses harvested energy for computation offloading, and [[wu-2024-urllc-uav-mec-latency]] uses finite blocklength for latency rather than WPT energy efficiency.

## Raw artifacts

- Parse: `raw/sources/Energy_Efficient_Resource_Allocation_for_Wireless_Powered_UAV_Wireless_Communication_System_With_Short_Packet/Energy_Efficient_Resource_Allocation_for_Wireless_Powered_UAV_Wireless_Communication_System_With_Short_Packet.md`
- Origin PDF: `raw/sources/Energy_Efficient_Resource_Allocation_for_Wireless_Powered_UAV_Wireless_Communication_System_With_Short_Packet/Energy_Efficient_Resource_Allocation_for_Wireless_Powered_UAV_Wireless_Communication_System_With_Short_Packet.pdf`
- Figures: `raw/sources/Energy_Efficient_Resource_Allocation_for_Wireless_Powered_UAV_Wireless_Communication_System_With_Short_Packet/images/`
