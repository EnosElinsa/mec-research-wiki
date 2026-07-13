---
type: source
title: "UAV-Enabled Wireless Power Transfer: A Tutorial Overview"
authors: ["Lifeng Xie", "Xiaowen Cao", "Jie Xu", "Rui Zhang"]
year: 2021
url: "https://doi.org/10.1109/TGCN.2021.3093718"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN), vol. 5, no. 4, pp. 2042-2064"
tags: [source, wireless-power-transfer, uav-trajectory-control, resource-allocation, wireless-powered-communication-network, wireless-powered-mec, tutorial]
related:
  - "[[wireless-power-transfer]]"
  - "[[rf-energy-harvesting]]"
  - "[[uav-trajectory-control]]"
  - "[[multi-location-hovering]]"
  - "[[successive-hover-and-fly-trajectory]]"
  - "[[wireless-powered-communication-network]]"
  - "[[energy-causality-constraint]]"
  - "[[computation-causality-constraint]]"
  - "[[mobile-edge-computing]]"
  - "[[energy-harvesting-mec]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[lin-2026-uav-wpucn-time-allocation]]"
  - "[[xu-2018-uav-wpt-trajectory]]"
  - "[[zhou-2018-uav-wireless-powered-mec]]"
  - "[[wang-2018-wpt-mec-joint-offloading]]"
  - "[[liu-2020-wpt-cooperative-uav-mec]]"
  - "[[wu-2018-multiuav-minrate-trajectory]]"
  - "[[jie-xu]]"
created: 2026-07-14
updated: 2026-07-14
---

# UAV-Enabled Wireless Power Transfer: A Tutorial Overview

## Citation

Xie, L., Cao, X., Xu, J., & Zhang, R. (2021). *UAV-Enabled Wireless Power Transfer: A Tutorial Overview*. **IEEE Transactions on Green Communications and Networking**, 5(4), 2042-2064. DOI: 10.1109/TGCN.2021.3093718.

## TL;DR

An invited tutorial that organizes UAV-enabled [[wireless-power-transfer|wireless power transfer]] around single-UAV and multi-UAV energy delivery, [[wireless-powered-communication-network|wireless-powered communication networks]], and wireless-powered MEC. Its recurring design toolkit is speed-relaxed [[multi-location-hovering]], flight-feasible [[successive-hover-and-fly-trajectory|successive hover-and-fly]], and time-quantized SCA. The tutorial is careful about scope: relaxed solutions are upper bounds, generic multi-UAV WPT remains open, and the full wireless-powered MEC formulation with computation causality is posed but not solved.

## Problem

Fixed energy transmitters suffer severe distance loss, require dense deployment for wide-area charging, and create a near-far fairness problem. A low-altitude UAV can shorten charging distance through controllable mobility and line-of-sight links, but finite mission time couples where it flies, how long it hovers, which devices transmit, and how energy, communication, and computation resources are allocated.

## System model

- The single-UAV WPT model serves `K` devices at known locations from a fixed altitude and maximizes the minimum weighted harvested energy over a finite horizon.
- The multi-UAV model jointly designs `M` trajectories and transmit covariance matrices under flight, collision-separation, and transmit-power constraints. The tutorial studies fixed-formation swarming with cooperative beamforming and geographic device clustering as tractable heuristics.
- The [[wireless-powered-communication-network|WPCN]] model uses TDD/TDMA for downlink WPT and per-device uplink information transmission. Each device's cumulative transmit energy is limited by its initial and harvested energy through an [[energy-causality-constraint]].
- The wireless-powered MEC model adds task offloading, UAV execution, result downloading, and local computing. Completely partitionable tasks may be processed locally and remotely in parallel.
- MEC execution obeys [[computation-causality-constraint|computation causality]]: cumulative UAV execution cannot exceed received task input, and cumulative result downloading cannot exceed generated output; all offloaded inputs and outputs must be completed by the deadline.

## Method

For single-UAV WPT, dropping the speed constraint yields a time-sharing problem with strong duality. Lagrange duality, a two-dimensional search, and a linear program produce an optimal [[multi-location-hovering]] solution for the relaxed problem. Because that solution ignores travel time, it is an upper bound for the speed-constrained mission. A [[successive-hover-and-fly-trajectory]] visits the relaxed hover points along a shortest route at maximum speed and allocates the remaining dwell time by linear programming; time quantization and SCA then locally refine the feasible trajectory.

For multi-UAV WPT, the tutorial applies analogous relaxed, hover-and-fly, and time-quantized designs to fixed-formation swarming. Its clustering alternative neglects energy from nonassociated UAVs so that the problem decomposes into single-UAV subproblems. Neither heuristic globally solves the generic joint trajectory/covariance problem.

For WPCNs, a speed-relaxed dual solution again gives an optimal multi-location-hovering/resource-allocation upper bound, followed by flight-feasible hover-and-fly and time-quantized alternating/SCA designs. For wireless-powered MEC, the tutorial formulates the full fair-computation problem but reports the computation-causality-constrained version as unaddressed. Multi-location hovering and related methods apply only to simplified formulations that omit those constraints; discrete-time SCA is suggested as a direction for the full problem.

## Key findings

- In the 10-device single-UAV example, the relaxed solution uses four hovering locations. Time quantization outperforms hover-and-fly, and both outperform static hovering; the feasible designs approach the relaxed upper bound as mission duration grows.
- In the 4-UAV, 20-device example, clustering performs better for short durations (illustrated below 10 s), while swarming performs better for longer durations (illustrated above 11 s), when cooperative energy beamforming has time to offset travel and coordination costs.
- In the 10-device WPCN example, the relaxed design uses three WPT locations and ten information-reception locations, one above each device. The time-quantized design beats static hovering and approaches the relaxed upper bound as mission duration increases.
- A one-device toy simulation reports a 30 dB harvested-power gain over fixed WPT at `T = 100 s` under its stated geometry, channel, and power assumptions. This is scenario-specific and is not a universal UAV-WPT gain.
- The tutorial presents no numerical solution for the full wireless-powered MEC problem with computation causality; that section is a formulation and research agenda.

## Limitations / parse caveats

The main models assume known fixed device locations, fixed UAV altitude, mostly free-space line-of-sight path loss, linear harvesting, constant WPT power, and offline deterministic trajectory knowledge. Worked trajectory designs generally retain only maximum speed from a broader set of possible flight constraints. Multi-UAV swarming fixes the formation and uses one-device-at-a-time beamforming; clustering uses a simple geographic partition and neglects cross-cluster energy.

The tutorial identifies nonlinear harvesting, CSI acquisition cost and accuracy, online adaptation, and more complete multi-UAV, WPCN, and MEC designs as open issues. In particular, transmit energy beamforming presumes CSI whose training and feedback consume device time and energy. The parse also contains a one-device travel-condition inconsistency: the stated `T V_max >= D` condition conflicts with its own `T - 2D/V_max` hover duration, which requires `T V_max >= 2D`. Several equation labels and symbols are OCR-damaged, so the intact prose and equations should govern interpretation.

## Relation to the corpus

This tutorial consolidates the UAV-WPT trajectory framework introduced by [[xu-2018-uav-wpt-trajectory]] and connects it to communication and computation. [[zhou-2018-uav-wireless-powered-mec]], [[wang-2018-wpt-mec-joint-offloading]], and [[liu-2020-wpt-cooperative-uav-mec]] instantiate parts of the wireless-powered MEC line, but the tutorial explicitly separates those simplified treatments from its unsolved full causality-aware formulation. [[lin-2026-uav-wpucn-time-allocation]] cites this tutorial and specializes its energy-delivery setting to underground devices, soil propagation, CSI-free arrays, and fixed-geometry phase-duration optimization rather than trajectory design.

## Raw artifacts

- Parse: `raw/sources/UAV-Enabled_Wireless_Power_Transfer_A_Tutorial_Overview/UAV-Enabled_Wireless_Power_Transfer_A_Tutorial_Overview.md`
- Origin PDF: `raw/sources/UAV-Enabled_Wireless_Power_Transfer_A_Tutorial_Overview/UAV-Enabled_Wireless_Power_Transfer_A_Tutorial_Overview.pdf`
- Figures: `raw/sources/UAV-Enabled_Wireless_Power_Transfer_A_Tutorial_Overview/images/`
