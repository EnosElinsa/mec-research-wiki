---
type: concept
title: "UAV-Enabled Intelligent Transportation Systems (ITS)"
tags: [its, uav, traffic, surveillance, data-fusion]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[multi-source-data-fusion]]"
  - "[[completion-time-difference]]"
  - "[[hou-2025-pbia-air-iscc-uav-its]]"
  - "[[peng-2024-energy-time-uav-its]]"
  - "[[ji-2026-llm-iov-uav-offloading]]"
  - "[[beishenalieva-2026-secrecy-aware-uav-path-planning]]"
  - "[[li-2026-la4h-uav-active-tracking]]"
  - "[[wang-2026-rmaddpg-dda-uav-isac-vehicular]]"
  - "[[hazarika-2026-dynamo-uav-vehicle-tracking]]"
  - "[[chen-2026-maddpg-uav-swarm-antijamming]]"
  - "[[du-2025-autonomous-intelligent-uav-swarms]]"
  - "[[zang-2026-uav-ev-priority-cav-speed]]"
  - "[[multi-domain-uav-anti-jamming]]"
  - "[[speed-coordinated-robust-optimization-control]]"
created: 2026-05-29
updated: 2026-07-10
---

# UAV-Enabled Intelligent Transportation Systems (ITS)

Use of UAV swarms for traffic surveillance, accident reporting, parking-space detection, traffic-flow prediction, and similar transportation-management tasks. UAVs are dispatched to monitoring locations, collect surveillance data (image, video), and process it locally or via offloading to a ground edge server. Processing results then feed into a control center that fuses multi-source data to make centralized decisions.

Distinct from **vehicular MEC** ([[vehicular-mec]]) — vehicular MEC offloads tasks generated *by vehicles*; UAV-ITS offloads tasks generated *by UAVs observing vehicles*. The compute side looks similar but the workload differs.

Key wiki source: [[peng-2024-energy-time-uav-its]], which adds the **completion-time-difference** objective (synchronize finish times for fusion quality) on top of standard energy minimization. [[ji-2026-llm-iov-uav-offloading]] is adjacent but vehicle-task-driven: UAVs provide 3D coverage and edge offloading support for dense IoV traffic, with LLM-assisted resource adjustment for long-tail failures.

[[hou-2025-pbia-air-iscc-uav-its]] adds an Air-ISCC view: UAVs sense blocked or accident-affected road environments, communicate with IoTDs, and compute offloaded tasks under a PPO-based swarm policy. [[beishenalieva-2026-secrecy-aware-uav-path-planning]] adds the security view: UAVs act as mobile aggregators when RSUs fail or congest, while policy-gradient control and PSO slot scheduling protect ITS sensing uploads from malicious aerial eavesdroppers and jammers.

Adjacent tracking sources broaden the sensing side of the concept. [[li-2026-la4h-uav-active-tracking]] focuses on visual active target tracking under occlusion and distractor interference, [[wang-2026-rmaddpg-dda-uav-isac-vehicular]] controls UAV-enabled vehicular ISAC with MARL, and [[hazarika-2026-dynamo-uav-vehicle-tracking]] prioritizes fast-moving vehicles using prediction uncertainty, link quality, and freshness rather than [[age-of-information]] alone.

The latest adjacent ITS additions split the role of the UAV even further. [[chen-2026-maddpg-uav-swarm-antijamming]] protects U2U/U2G traffic-monitoring links through [[multi-domain-uav-anti-jamming]], [[zang-2026-uav-ev-priority-cav-speed]] uses UAVs as sensing/relay infrastructure for emergency-vehicle CAV speed coordination, and [[du-2025-autonomous-intelligent-uav-swarms]] supplies the broader swarm-autonomy taxonomy behind such deployments.
