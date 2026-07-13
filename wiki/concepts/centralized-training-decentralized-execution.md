---
type: concept
title: Centralized Training, Decentralized Execution (CTDE)
tags: [drl, multi-agent, training-paradigm]
related:
  - "[[li-2026-credit-aware-uav-irs-secrecy]]"
  - "[[lu-2026-aoi-trajectory-channel]]"
  - "[[wen-2026-cooperative-jamming-uav]]"
  - "[[ma-pomdp]]"
  - "[[masac]]"
  - "[[zhang-2025-mcma-task-migration]]"
  - "[[peng-2025-drudm-cfg]]"
  - "[[ctde-actor-critic-backbones-in-mec]]"
  - "[[ctde-multi-agent-drl-protocol]]"
  - "[[chen-2026-maddpg-uav-swarm-antijamming]]"
  - "[[gao-2023-uav-mcs-uma]]"
  - "[[qmix]]"
  - "[[shi-2025-aoi-energy-replenishment-multiuav]]"
  - "[[ensemble-qmix]]"
  - "[[zhang-2026-ensemble-marl-uav-target-search]]"
  - "[[wu-not-in-parse-aoi-sampling-buffering-routing]]"
  - "[[zhou-2026-a2g-madrl-air-ground-vcs]]"
  - "[[yang-2025-hcdrl-pursuit-evasion]]"
  - "[[cooperative-uav-pursuit-evasion]]"
  - "[[le-2026-asynchronous-uav-data-collection]]"
  - "[[asynchronous-qmix]]"
  - "[[wang-2026-wutf-fair-communication]]"
  - "[[wireless-powered-uav-fair-service-control]]"
  - "[[morshed-2026-active-ris-uav-noma-mappo]]"
  - "[[decentralized-active-ris-uav-noma-control]]"
  - "[[wang-2026-glint-aoi-wireless-powered-edge]]"
  - "[[dual-network-sequential-aoi-control]]"
  - "[[qin-2023-symmetry-augmented-uav-isac]]"
  - "[[zhou-2026-multiscale-dt-uav-delivery]]"
  - "[[zhang-2026-distance-attention-uav-navigation]]"
  - "[[liu-2020-distributed-uav-coverage-navigation]]"
  - "[[liu-2021-edivert-mobile-crowdsensing]]"
  - "[[ape-x-actor-learner-replay]]"
  - "[[he-2026-memdrl-uav-navigation]]"
  - "[[memory-augmented-multi-uav-navigation]]"
  - "[[betalo-2026-meta-uav-scheduling]]"
  - "[[mw-mad3pg]]"
created: 2026-05-28
updated: 2026-07-14
---

# Centralized Training, Decentralized Execution (CTDE)

[[zhang-2026-ensemble-marl-uav-target-search]] adds the ensemble QMIX/value-decomposition form of CTDE to the curated corpus. Its [[ensemble-qmix]] controller trains centralized mixing networks but executes per-UAV majority-voted local actions. [[shi-2025-aoi-energy-replenishment-multiuav]] adds the direct [[qmix|QMIX]] and VDN comparison for rechargeable multi-UAV IoT data collection.

A canonical paradigm for cooperative multi-agent DRL:

- **Training time:** a centralized critic has access to all agents' observations and actions, plus any global state. It uses this view to compute stable value estimates.
- **Execution time:** each agent uses only its local observation through a decentralized actor. The centralized critic is discarded.

## Why this works

- Centralized critic eliminates the non-stationarity that plagues independent learners (each agent's policy is changing, so the environment looks non-stationary from any one agent's perspective).
- Decentralized execution stays deployable — no inter-agent communication required at inference.

## Standard backbones

- **MADDPG** — deterministic policies, replay buffer.
- **[[masac|MASAC]]** — stochastic policies + entropy bonus.
- **MAPPO** — on-policy clipped objective.
- **MATD3** — twin-Q critics, delayed updates.
- **Qmix / VDN** — value decomposition for fully cooperative discrete settings.
- **COMA** — counterfactual baseline for credit assignment.

## In this wiki

CTDE shows up explicitly in [[zhang-2025-mcma-task-migration]] (server-as-agent for vehicular MEC), [[peng-2025-drudm-cfg]] (UAV-as-agent for post-disaster MEC), and [[kang-2023-mappo-hierarchical-aerial]] (UAV-as-agent for hierarchical aerial MEC). It also appears in adjacent non-offloading control, including [[chen-2026-maddpg-uav-swarm-antijamming]] for jammed UAV-swarm communications, [[gao-2023-uav-mcs-uma]] for multi-UAV mobile-crowd-sensing coverage/calibration, [[wu-not-in-parse-aoi-sampling-buffering-routing]] for all-aerial AoI sampling/buffering/routing, and [[zhou-2026-a2g-madrl-air-ground-vcs]] for sequential UAV/UGV crowdsensing. Across these, the *backbone* differs (MAPPO / MADDPG / MASAC / value decomposition / sequential policy generation), but the training/execution split is shared. The engineering protocol is expanded in [[ctde-multi-agent-drl-protocol]].

[[betalo-2026-meta-uav-scheduling]] uses a related coordinated-critic pattern in [[mw-mad3pg]], but its neighbor/server replay and adaptation sharing mean it should not be read as a strictly communication-free execution design.

[[yang-2025-hcdrl-pursuit-evasion]] uses centralized lower-layer critics for continuous counter-UAV maneuver learning. [[le-2026-asynchronous-uav-data-collection]] uses the value-decomposition branch through [[asynchronous-qmix]], retaining global-state mixing during training while agents select actions at unequal local completion times.

Three wireless-powered/active-surface cases illustrate different CTDE factorizations. [[wang-2026-wutf-fair-communication]] gives one speed/yaw actor per UAV with a global critic; [[morshed-2026-active-ris-uav-noma-mappo]] assigns actors to the BS, UAV, and active RIS; [[wang-2026-glint-aoi-wireless-powered-edge]] uses two sequential actors per UAV and a monotonic value mixer.

## Limitation

Centralized critic input dimension grows with agent count. Beyond ~20 agents you typically need attention-based aggregation, value decomposition, or mean-field approximation to keep the critic tractable.
