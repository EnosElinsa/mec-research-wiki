---
type: source
modeling_card: required
title: "Joint Optimization of Resource Allocation, Phase Shift, and UAV Trajectory for Energy-Efficient RIS-Assisted UAV-Enabled MEC Systems"
authors: ["Xintong Qin", "Zhengyu Song", "Tianwei Hou", "Wenjuan Yu", "Jun Wang", "Xin Sun"]
year: 2023
url: "https://doi.org/10.1109/TGCN.2023.3287604"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, intelligent-reflecting-surface, uav-mec, noma, fractional-programming-dinkelbach, alternating-optimization-sdr-sca, energy-efficiency, csi-estimation-error]
related:
  - "[[intelligent-reflecting-surface]]"
  - "[[noma]]"
  - "[[fractional-programming-dinkelbach]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[uav-trajectory-control]]"
  - "[[csi-estimation-error]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[xiao-2025-star-ris-bidirectional-uav-mec]]"
created: 2026-07-07
updated: 2026-07-16
---

# Joint Optimization of Resource Allocation, Phase Shift, and UAV Trajectory for Energy-Efficient RIS-Assisted UAV-Enabled MEC Systems

## Citation

Qin, X., Song, Z., Hou, T., Yu, W., Wang, J., & Sun, X. (2023). *Joint Optimization of Resource Allocation, Phase Shift, and UAV Trajectory for Energy-Efficient RIS-Assisted UAV-Enabled MEC Systems*. **IEEE Transactions on Green Communications and Networking**, 7(4), 1778-1792. DOI: 10.1109/TGCN.2023.3287604.

## TL;DR

Studies an RIS-assisted UAV-MEC system where IoT devices partially offload tasks to a UAV-mounted MEC server using [[noma]]. A building-mounted [[intelligent-reflecting-surface|RIS]] creates a controllable reflected path around blockage. The objective is energy efficiency, defined as completed task bits divided by total energy consumption, optimized over local/offloaded bits, transmit power, RIS phase shifts, and UAV trajectory through a Dinkelbach + BCD + DC/SCA pipeline.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Fixed IoT devices partially offload tasks over uplink NOMA to one UAV-mounted MEC server, while a building-mounted RIS creates a reflected path around blockage. The mission is slotted, devices use local CPU or offload bits, and the UAV flies between prescribed endpoints with bounded speed; CSI errors are modeled in the resource design.

**Problem & objective**: A non-convex fractional program maximizes energy efficiency, $\max \frac{\text{completed task bits}}{E_{\mathrm{local}}+E_{\mathrm{offload}}+E_{\mathrm{UAV\ flight}}}$, over task allocation, transmit power, RIS phases, and UAV trajectory.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Local/offloaded bits | $d_i^{\mathrm l}[n],d_i^{\mathrm o}[n]$ | continuous, nonnegative | Task bits computed locally or offloaded by device $i$ |
| Device transmit power | $p_i[n]$ | continuous, power-bounded | NOMA uplink power |
| RIS phase | $\theta_m[n]$ | continuous, phase-feasible | Phase applied by RIS element $m$ |
| UAV trajectory | $\mathbf q[n]$ | continuous position sequence | UAV-MEC location in slot $n$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Local plus offloaded bits meet each device's task requirement |
| C2 | NOMA rates support offloaded bits under the SIC ordering |
| C3 | IoT and UAV CPU allocations stay within their computing capacities |
| C4 | RIS phases satisfy their feasible unit-modulus/phase domain |
| C5 | UAV trajectory obeys initial/final positions and maximum-speed limits |
| C6 | Device power and per-slot latency constraints remain feasible |

**Algorithm**: Apply Dinkelbach's transform to the energy-efficiency ratio → alternate bit/power, RIS-phase, and trajectory blocks with BCD → solve allocation by Lagrange-dual/convex updates → use DC/semidefinite relaxation for phases → use SCA for trajectory → repeat until energy efficiency converges.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Qin et al. [x] studied energy-efficient RIS-assisted UAV mobile edge computing with partial NOMA offloading from fixed IoT devices. They formulated a fractional problem that jointly optimizes local and offloaded bits, transmit power, RIS phase shifts, and UAV trajectory under task, CPU, phase, power, speed, and latency constraints. Their solver applies Dinkelbach transformation and block coordinate descent, with Lagrange-dual allocation, difference-of-convex RIS optimization, semidefinite relaxation, and successive convex approximation for the trajectory. Simulations report convergence in about five to six iterations and higher energy efficiency than no-RIS, random-phase, no-trajectory-optimization, and full-offloading schemes. Under ten RIS elements, the reported NOMA gain over OMA is 10% with perfect CSI and 7% with imperfect CSI.

## Problem framing

UAV-enabled MEC improves coverage but suffers from energy limits and blocked direct links in urban environments. RIS can improve the channel, but random phase shifts are nearly useless and the UAV trajectory must be co-designed with the RIS and task-bit allocation. NOMA adds spectral efficiency, but it also becomes more sensitive to CSI errors because inter-user interference depends on channel ordering.

## System model

- One UAV with an MEC server serves multiple fixed IoT devices.
- An RIS is installed on a surrounding building wall; both direct IoT-to-UAV and RIS-reflected links are modeled.
- IoT devices can compute locally and offload part of their task input bits to the UAV during a mission period divided into time slots.
- NOMA is used for offloading, with IoT devices ordered by channel gain at the UAV.
- The optimization includes minimum task-completion requirements, IoT/UAV CPU limits, RIS phase-shift feasibility, UAV start/end locations, and maximum UAV speed.

## Method

- The outer loop applies [[fractional-programming-dinkelbach|Dinkelbach's method]] to handle the energy-efficiency ratio.
- The inner loop uses BCD to split the coupled problem into three subproblems.
- Bit allocation and transmit power are solved through Lagrange-dual / convex optimization.
- RIS phase shifts are handled through DC programming and semidefinite programming-style relaxation.
- UAV trajectory is handled by successive convex approximation, placing the work in the [[alternating-optimization-sdr-sca]] family.

## Key findings

- The proposed algorithm converges quickly in the plotted examples, reaching stable energy efficiency in about 5-6 iterations.
- With RIS, the optimized UAV trajectory tends to move closer to the RIS rather than only toward the IoT devices, because coherent reflected paths can improve received signal power.
- Energy efficiency is higher than no-trajectory-optimization, random-phase, no-RIS, and full-offloading baselines.
- Energy efficiency first increases and then decreases as the mission period grows: longer time helps offloading/computing initially, but UAV flying energy dominates later.
- Under imperfect CSI, energy efficiency drops and the NOMA-over-OMA gain shrinks. At `M = 10` RIS elements, the reported NOMA gain over OMA is 10% with perfect CSI and 7% under imperfect CSI.

## Limitations / future work

The paper is a model-driven simulation study. It assumes fixed IoT-device locations, a fixed building-mounted RIS, and bounded CSI-error models rather than measured online CSI. The conclusion does not name a detailed future-work program beyond the reported imperfect-CSI analysis.

## Relation to the corpus

This source is an early fixed-RIS UAV-MEC energy-efficiency anchor for [[intelligent-reflecting-surface]], [[noma]], and [[fractional-programming-dinkelbach]]. It is distinct from [[mohammadi-2026-star-ris-uav-mec-noma]] and [[xiao-2025-star-ris-bidirectional-uav-mec]], which use UAV-mounted STAR-RIS architectures. Here the RIS is on a building wall and the UAV itself carries the MEC server, making it a bridge between fixed RIS-aided MEC and later UAV-mounted-RIS offloading designs.

## Raw artifacts

- `raw/sources/Joint Optimization of Resource Allocation- Phase Shift- and UAV Trajectory for Energy-Efficient RIS-Assisted UAV-Enabled MEC Systems/Joint Optimization of Resource Allocation- Phase Shift- and UAV Trajectory for Energy-Efficient RIS-Assisted UAV-Enabled MEC Systems.md`
- Original PDF and extracted figures (`images/`) in the same folder.
