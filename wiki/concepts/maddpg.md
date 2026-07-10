---
type: concept
title: "Multi-Agent Deep Deterministic Policy Gradient (MADDPG)"
tags: [drl, multi-agent, actor-critic, ctde, deterministic-policy]
related:
  - "[[ddpg]]"
  - "[[multi-agent-td3]]"
  - "[[centralized-training-decentralized-execution]]"
  - "[[masac]]"
  - "[[ma-pomdp]]"
  - "[[seid-2021-madrl-multiuav-iot-edge]]"
  - "[[wang-2021-maddpg-multiuav-trajectory]]"
  - "[[peng-2020-maddpg-uav-vehicular]]"
  - "[[he-2023-fairness-3d-multiuav-maddpg]]"
  - "[[du-2023-maddpg-service-placement-agin]]"
  - "[[feng-2026-prediction-service-migration]]"
  - "[[tang-2026-hg-maddpg-uav-rescue]]"
  - "[[kernel-density-mean-field-marl]]"
  - "[[li-2026-uav-bs-semantic-mfmaddpg-kde]]"
  - "[[wang-2026-rmaddpg-dda-uav-isac-vehicular]]"
  - "[[rmaddpg-dda-uav-isac-control]]"
  - "[[hazarika-2026-dynamo-uav-vehicle-tracking]]"
  - "[[ctde-actor-critic-backbones-in-mec]]"
created: 2026-05-31
updated: 2026-07-10
---

# Multi-Agent Deep Deterministic Policy Gradient (MADDPG)

The multi-agent extension of [[ddpg]]: each agent has its own deterministic actor (acting on local observations) and a **centralized critic** that sees the joint state/actions at training time. This is the canonical **[[centralized-training-decentralized-execution|CTDE]]** instantiation with deterministic policies and a replay buffer — well suited to cooperative MEC problems where many UAVs/servers each make continuous decisions from partial observations ([[ma-pomdp]]).

## Why it appears in MEC papers

- Multi-UAV trajectory + offloading + resource decisions are coupled across agents but must execute on local information; MADDPG's centralized critic resolves the non-stationarity of independent learners while keeping execution decentralized.
- It handles high-dimensional **continuous** action spaces (trajectories, power, resource fractions) that tabular/DQN methods cannot.

## In this wiki

- [[seid-2021-madrl-multiuav-iot-edge]] — clustered multi-UAV IoT-edge offloading as a stochastic game, solved with MADDPG (energy+delay cost).
- [[wang-2021-maddpg-multiuav-trajectory]] — per-UAV MADDPG trajectory control for dual-fairness + energy.
- [[peng-2020-maddpg-uav-vehicular]] — MEC servers (eNodeB + UAV) as MADDPG agents for vehicle association + resource allocation.
- [[he-2023-fairness-3d-multiuav-maddpg]] — fairness-among-UAVs 3D trajectory with MADDPG.
- [[du-2023-maddpg-service-placement-agin]] — MADDPG service placement + offloading in air-ground integrated MEC.
- [[feng-2026-prediction-service-migration]] — MADDPG coordinates multi-UAV trajectory and service-migration decisions after LSTM prediction and Lyapunov cost control.
- [[tang-2026-hg-maddpg-uav-rescue]] — HG-MADDPG combines Hungarian area assignment, Lyapunov queues, and a generative-diffusion-enhanced MADDPG actor for low-altitude UAV rescue.
- [[li-2026-uav-bs-semantic-mfmaddpg-kde]] — MF-MADDPG-KDE uses mean-field MADDPG plus kernel-density action-distribution modeling for 3-D semantic UAV-BS deployment.
- [[wang-2026-rmaddpg-dda-uav-isac-vehicular]] — [[rmaddpg-dda-uav-isac-control]] adds random-network-distillation novelty, parameter sharing, and dynamic data augmentation to MADDPG for UAV-enabled vehicular ISAC.
- [[hazarika-2026-dynamo-uav-vehicle-tracking]] — POMDP-MADDPG controls predictive multi-UAV vehicle tracking after DynaMo prediction and [[dynamic-target-prioritization-metric|DTPM]] prioritization.

## Relation to siblings

Compared with [[multi-agent-td3|MATD3]] (adds clipped double-Q + delayed updates + target smoothing to curb overestimation) and [[masac|MASAC]] (stochastic, max-entropy), MADDPG is the simplest/earliest of the CTDE actor-critic family and remains a common baseline.
