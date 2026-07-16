---
type: source
title: "Energy Efficient Resource Allocation for Wireless Powered UAV Wireless Communication System With Short Packet"
authors: ["Jin Xie", "Zheng Chang", "Xijuan Guo", "Timo Hämäläinen"]
year: 2023
url: "https://doi.org/10.1109/TGCN.2022.3218314"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 7, no. 1, pp. 101-113"
modeling_card: required
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
updated: 2026-07-16
---

# Energy Efficient Resource Allocation for Wireless Powered UAV Wireless Communication System With Short Packet

## Citation

Xie, J., Chang, Z., Guo, X., & Hämäläinen, T. (2023). *Energy Efficient Resource Allocation for Wireless Powered UAV Wireless Communication System With Short Packet*. **IEEE Transactions on Green Communications and Networking**, 7(1), 101-113. DOI: 10.1109/TGCN.2022.3218314.

## TL;DR

A fixed-altitude UAV hybrid access point first powers IoT devices and then receives their TDMA finite-blocklength uploads. Alternating SCA and fractional-programming updates optimize horizontal placement, downlink WPT powers, and a continuous symbol-allocation relaxation; heuristic rounding restores integer frame symbols.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A fixed-altitude multi-antenna UAV acts as a hybrid access point, first transferring energy to single-antenna IoT devices and then receiving their finite-blocklength uplink packets through TDMA.

**Problem & objective**: Problem P1 maximizes finite-blocklength energy efficiency, $\max_{\mathbf q,\mathbf n,\mathbf p}\mathrm{EE}(\mathbf q,\mathbf n,\mathbf p)$, by jointly selecting UAV placement, frame-symbol allocation, and downlink WPT power.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV horizontal position | $\mathbf q=[x,y]^T$ | Continuous in a bounded region | Select the static HAP placement |
| WPT blocklength | $n_0$ | Nonnegative integer | Symbols used for downlink energy transfer |
| Uplink blocklengths | $n_k$ | Nonnegative integers | Symbols assigned to device $k$ for short-packet upload |
| WPT powers | $p_k$ | Continuous, positive | UAV power allocated to charge device $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Horizontal placement satisfies the per-axis bounds in (11b) and (11c) |
| C2 | The total frame length is bounded, $\sum_{k=0}^{K}n_k\leq N$ |
| C3 | Symbol allocations are integral and nonnegative, $n_k\in\mathbb N$ |
| C4 | Total WPT power is bounded, $\sum_{k=1}^{K}p_k\leq P_m$ |
| C5 | Each charging power is positive, $p_k>0$ |

**Algorithm**: After relaxing blocklength integrality, the method alternates an SCA placement update, a fractional-programming blocklength update, and a Lagrangian power update until energy efficiency converges, then applies largest-remainder rounding and recomputes placement and power.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Xie et al. [x] considered energy-efficient resource allocation for a wireless-powered UAV hybrid access point with finite-blocklength uplink communication. Their mixed-integer fractional model jointly optimizes static UAV placement, downlink charging powers, and the WPT and uplink symbol allocations under placement, frame-length, integrality, and power constraints. The proposed solver alternates successive convex approximation and fractional or dual updates before using heuristic integer conversion for the symbol counts. Simulations show that joint optimization outperforms equal allocation and partial-optimization baselines, while energy efficiency decreases as more devices share the finite frame.

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
