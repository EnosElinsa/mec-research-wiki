---
type: concept
title: Task Offloading
tags: [mec, computation, decision]
related:
  - "[[mobile-edge-computing]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[liu-2026-jppo-en-convntm]]"
  - "[[ning-2023-uav-mec-offloading-deployment]]"
  - "[[mohammadi-2026-star-ris-uav-mec-noma]]"
  - "[[wang-2026-blockchain-lae-fl-mappo]]"
  - "[[xiao-2025-star-ris-bidirectional-uav-mec]]"
  - "[[ma-2026-mean-field-green-aec]]"
  - "[[tong-2026-uneven-terrain-uav-mec]]"
  - "[[sequential-task-offloading]]"
  - "[[teng-2026-gstrl-sequential-offloading]]"
  - "[[wen-2026-hybridrag-low-carbon-lae]]"
  - "[[tun-2025-thz-sag-mec-resource-allocation]]"
  - "[[guo-2026-aot-uav-inspection-offloading]]"
  - "[[zhan-2026-gatd3qn-dependent-offloading]]"
  - "[[wang-2026-llm-qos-multiuav-resource]]"
  - "[[ye-2026-flight-speed-battery-swapping]]"
  - "[[hu-2026-ertatd3-secure-caching]]"
  - "[[chen-2026-qos-noma-multiuav]]"
  - "[[diallo-2026-system-cost-uav-leo-offloading]]"
  - "[[bui-2025-noma-near-far-offloading]]"
  - "[[tang-2026-hg-maddpg-uav-rescue]]"
  - "[[song-2026-thz-multiuav-mec]]"
  - "[[beishenalieva-2026-secrecy-aware-uav-path-planning]]"
  - "[[wu-2025-security-aware-multiuav-service-placement]]"
created: 2026-05-28
updated: 2026-07-07
---

# Task Offloading

The decision of how much of a task an IoT device computes locally versus ships to an edge server (here, a UAV). Parameterized by a per-device-per-UAV ratio $\lambda_{u,d,n} \in [0,1]$, with $\sum_u \lambda_{u,d,n} \le 1$ enforcing that no more than 100% of the workload is offloaded.

## Cost components per task

- **Uplink transmission:** $T^{\text{Offload}}_{u,d,n} = \lambda_{u,d,n} L_{d,n} / R_{u,d,n}(p_d)$
- **Edge compute:** $T^{\text{Compute}}_{u,d,n} = \lambda_{u,d,n} L_{d,n} C_u / f_u$
- **Result downlink:** $T^{\text{Transmit}}_{u,d,n} = \lambda_{u,d,n} \tilde L_{d,n} / R_{u,d,n}(p_u)$
- **Local compute:** $T^{\text{Local}}_{d,n} = (1 - \sum_u \lambda_{u,d,n}) L_{d,n} C_d / f_d$

Energy follows a cubic-frequency rule on both ends ($\eta f^3 T$ for the device, $\mu f_u^3 T$ for the UAV, plus $p_d T$ and $p_u T$ on the radio side).

In [[liu-2026-jppo-en-convntm]] the offloading ratios are part of the discrete action vector $\mathbf{1}_n$ (quantized via the policy network), jointly optimized with UAV trajectories.

Across the corpus, the same offloading decision appears in several forms. [[ning-2023-uav-mec-offloading-deployment]] uses a binary local-versus-UAV-server choice inside a stochastic-game deployment loop. [[mohammadi-2026-star-ris-uav-mec-noma]] splits task bits across local, UAV-MEC, and BS-MEC execution through a UAV-mounted STAR-RIS, while [[xiao-2025-star-ris-bidirectional-uav-mec]] schedules one user per slot and sends task bits bidirectionally to UAV and BS MEC servers. [[wang-2026-blockchain-lae-fl-mappo]] treats offloading as part of a larger low-altitude FL-MAPPO problem with caching, queueing, energy, and blockchain overhead. [[ma-2026-mean-field-green-aec]] frames task allocation for metaverse users as a large-population energy-balancing problem rather than a single-link offloading ratio. [[tong-2026-uneven-terrain-uav-mec]] invokes a second-level actor-critic task-allocation policy only when serviceable UEs are covered by the UAV over uneven terrain. [[teng-2026-gstrl-sequential-offloading]] and [[zhan-2026-gatd3qn-dependent-offloading]] add dependency-aware task graphs, while [[wen-2026-hybridrag-low-carbon-lae]] and [[wang-2026-llm-qos-multiuav-resource]] connect offloading/resource decisions to LLM-assisted formulation or teacher-student policy generation. [[ye-2026-flight-speed-battery-swapping]] couples offloading with flight-speed and battery-swapping cost, [[hu-2026-ertatd3-secure-caching]] joins offloading with secure result caching in UAV-assisted vehicular networks, [[chen-2026-qos-noma-multiuav]] makes task priority and NOMA transmission part of the offloading objective, [[diallo-2026-system-cost-uav-leo-offloading]] adds task dropping and LEO satellite execution, [[bui-2025-noma-near-far-offloading]] makes near-/far-field NOMA propagation part of the offloading design, [[tang-2026-hg-maddpg-uav-rescue]] offloads rescue tasks to ground embedded robots and airship support, [[song-2026-thz-multiuav-mec]] uses UAVs as THz relays to MEC servers, [[beishenalieva-2026-secrecy-aware-uav-path-planning]] treats ITS sensing uploads as secrecy-aware offloading, and [[wu-2025-security-aware-multiuav-service-placement]] makes offloading feasible only when the UAV caches the required service program and satisfies secrecy constraints.
