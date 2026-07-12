---
type: source
title: "Energy Minimization for NOMA-Based Data Collection and Computation in UAV-Assisted Marine IoT"
authors: ["Qian Wang", "Li Zou", "Li Ping Qian", "Wei Jiang", "Bin Lin", "Yuan Wu"]
year: 2026
url: "https://doi.org/10.1109/TGCN.2025.3605919"
venue: "IEEE Transactions on Green Communications and Networking (IEEE TGCN)"
tags: [source, maritime-mec, marine-iot, noma, uav-data-collection, edge-computing, energy-minimization, td3]
related:
  - "[[maritime-mec]]"
  - "[[noma]]"
  - "[[uav-data-collection]]"
  - "[[mobile-edge-computing]]"
  - "[[uav-trajectory-control]]"
  - "[[td3]]"
  - "[[air-to-ground-channel-model]]"
  - "[[qian-2022-uav-maritime-iot-noma]]"
  - "[[dai-2023-hybrid-noma-fdma-marine]]"
  - "[[ji-2021-uav-mec-noma-oma-energy-min]]"
  - "[[qian-wang]]"
  - "[[liping-qian]]"
  - "[[bin-lin]]"
  - "[[yuan-wu]]"
created: 2026-07-13
updated: 2026-07-13
---

# Energy Minimization for NOMA-Based Data Collection and Computation in UAV-Assisted Marine IoT

## Citation

Wang, Q., Zou, L., Qian, L. P., Jiang, W., Lin, B., & Wu, Y. (2026). *Energy Minimization for NOMA-Based Data Collection and Computation in UAV-Assisted Marine IoT*. **IEEE Transactions on Green Communications and Networking**, 10, 1010-1024. DOI: 10.1109/TGCN.2025.3605919.

## TL;DR

One fixed-altitude UAV acts as both aerial base station and MEC server for marine sensing devices. Devices upload required sensing data through uplink NOMA, the UAV processes each data set after collection completes, and results are returned to improve later sensing. A min-max-normalized TD3 controller jointly selects the UAV motion, device powers, and UAV compute allocation to minimize device transmit, UAV compute, and weighted propulsion energy.

## Problem framing

Marine sensing devices have limited energy and computing capacity, while distant terrestrial infrastructure makes raw-data transfer expensive. A nearby UAV can collect and process the data, but its movement changes NOMA channel ordering and interference, and collection completion times determine when compute resources become useful. Trajectory, power, computation, latency, and UAV energy therefore have to be coordinated over the whole mission.

## System model

- Fixed marine sensing devices upload mandatory data volumes to one fixed-altitude UAV over uplink power-domain [[noma|NOMA]]. The UAV decodes devices in descending channel-gain order.
- When a device finishes uploading in one slot, the UAV begins computing its data in the next. Allocated compute resources remain assigned rather than being released and reallocated.
- Result-feedback data volume, downlink latency, and downlink energy are treated as negligible.
- The objective combines sensing-device transmit energy, UAV computation energy, and a weighted UAV propulsion term. The UAV energy cap covers propulsion and computation, not device transmission.
- The model uses fixed device locations, distance-only LoS channels, perfect information for SIC ordering and control, a fixed UAV altitude, and a mission narrative in which the UAV returns to its start for replenishment.

## Method

The original formulation includes trajectory, device powers, per-slot compute-resource ratios, and per-device compute allocations. By combining the per-slot allocation and cross-slot ratio constraints, the paper eliminates the auxiliary ratio and obtains an equivalent continuous problem over trajectory, powers, and compute allocations.

The remaining problem is cast as an MDP. The state contains UAV position, each device's remaining data and collection/computation phase, and remaining UAV energy and compute capacity. The action contains UAV speed and heading, all device transmit powers, and all per-device compute allocations. Reward is negative slot energy plus boundary and feasibility penalties.

Before learning, each state feature is min-max normalized to `[0,1]`. The [[td3|TD3]] learner uses twin critics, the smaller target value, delayed actor updates, target-policy smoothing, replay, and soft target updates. The UAV trajectory is induced from the selected speed and heading rather than chosen as independent waypoints.

## Key findings

- At equal data volume, NOMA reduces reported total energy by 20.21% versus FDMA and 32.34% versus TDMA. At equal total compute capacity, the reductions are 13.4% and 31.65%.
- TD3 reduces average energy versus PSO by 21.79% in the data-volume comparison and 28.56% in the sensing-device-count comparison.
- Joint control reduces average energy by 18.02% versus fixed transmit power, 15.11% versus fixed/equal compute allocation, and 36.6% versus a random UAV trajectory.
- Min-max-normalized TD3 converges at about 500 episodes. Its final energy is reported as 20.27% of unnormalized TD3 and 27.35% of logarithmically normalized TD3 in the stated experiment.
- Raising maximum UAV speed from 10 to 20 m/s produces a marked energy reduction, with diminishing gains above 20 m/s.

## Limitations / future work

The evaluation is simulation-only; a demonstrator and real UAV experiments are future work. The design has one UAV, fixed sensing devices, fixed altitude, a distance-only LoS channel, negligible feedback cost, and no local-versus-offloaded computation decision. The displayed equivalent constraint list does not contain the return-to-start condition repeatedly stated in prose, and its `rho_2/v` propulsion term is singular at zero speed even though zero is allowed. The parse also contains incomplete original-formulation rows, inconsistent state-normalization equations, ambiguous reward-penalty pseudocode, and actor-update pseudocode that omits the delayed-update condition described in prose.

## Relation to the corpus

This paper extends the same Zhejiang/Dalian/University-of-Macau maritime cluster as [[qian-2022-uav-maritime-iot-noma]], with recurring authors [[qian-wang]], [[liping-qian]], [[bin-lin]], and [[yuan-wu]]. The earlier source uses mobile USVs, partial task offloading, DDPG trajectory learning, and a Lagrangian resource allocator. This source instead uses fixed sensing devices, mandatory collection followed by UAV computation, and joint TD3 control. [[dai-2023-hybrid-noma-fdma-marine]] uses a different two-hop underwater/aerial access structure with secrecy constraints, while [[ji-2021-uav-mec-noma-oma-energy-min]] provides a separate NOMA-versus-OMA energy comparison.

## Raw artifacts

- Parse: `raw/sources/Energy_Minimization_for_NOMA-Based_Data_Collection_and_Computation_in_UAV-Assisted_Marine_IoT/Energy_Minimization_for_NOMA-Based_Data_Collection_and_Computation_in_UAV-Assisted_Marine_IoT.md`
- Origin PDF: `raw/sources/Energy_Minimization_for_NOMA-Based_Data_Collection_and_Computation_in_UAV-Assisted_Marine_IoT/Energy_Minimization_for_NOMA-Based_Data_Collection_and_Computation_in_UAV-Assisted_Marine_IoT.pdf`
- Figures: `raw/sources/Energy_Minimization_for_NOMA-Based_Data_Collection_and_Computation_in_UAV-Assisted_Marine_IoT/images/`
