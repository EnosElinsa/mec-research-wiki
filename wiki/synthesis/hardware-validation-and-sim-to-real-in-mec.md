---
type: synthesis
title: "Hardware validation and the sim-to-real gap in the MEC corpus"
tags: [synthesis, sim-to-real, hardware-validation, uav, comparison]
related:
  - "[[sun-2024-asap-uav-swarm]]"
  - "[[shao-2024-drl-antijamming-mec]]"
  - "[[zhang-2020-response-delay-uav-swarm]]"
  - "[[qu-ecoei-uav-swarm]]"
  - "[[bai-2024-delay-aware-cooperative-edge-cloud]]"
  - "[[sun-2024-imssa-uav-secure-cb]]"
  - "[[query-real-world-validation-of-jppo-en-convntm]]"
  - "[[drl-simulation-with-pomdp-formulation]]"
  - "[[liu-2026-jppo-en-convntm]]"
created: 2026-06-01
updated: 2026-06-01
---

# Hardware validation and the sim-to-real gap in the MEC corpus

The corpus is overwhelmingly **simulation-only**: of the 171 curated sources, a handful touch real hardware, and they do so at very different depths. This page inventories exactly what each hardware-touching source built, separates genuine algorithm deployment from model-verification and proof-of-concept, and distils the sim-to-real challenges the sources themselves name. It is the evidence base behind cross-cutting observation #8 in [[overview]] and the corpus-level counterpart to the framework-specific [[query-real-world-validation-of-jppo-en-convntm]].

## What "validated" actually means here

"Hardware-validated" is not one thing. The sources fall on a ladder from a full system running on real airborne devices down to a real platform used only to check a model's numbers. Reading the parses, four rungs appear:

| Rung | Meaning | Sources |
|---|---|---|
| **Full algorithm on real devices** | The proposed system/algorithm runs on real compute + (some) real UAVs/RF | [[sun-2024-asap-uav-swarm]], [[shao-2024-drl-antijamming-mec]], [[zhang-2020-response-delay-uav-swarm]] |
| **Proof-of-concept prototype** | A scaled-down build demonstrating feasibility/elasticity, not benchmarked at scale | [[qu-ecoei-uav-swarm]] |
| **Practicality demonstration** | The method ported to a real device to show it runs, alongside a mostly-simulation study | [[sun-2024-imssa-uav-secure-cb]] |
| **Model verification on a real platform** | A real platform measured to confirm the *model* is correct; the algorithm itself evaluated in data-driven simulation | [[bai-2024-delay-aware-cooperative-edge-cloud]] |

Everything else in the corpus is pure simulation.

## The validated builds, grounded

- **[[sun-2024-asap-uav-swarm]] (ASAP)** — the deepest hardware story. Per the parse, ASAP was deployed on **24 airborne computers** (20 Jetson Nano + 2 Jetson Xavier TX2 + 2 Jetson Xavier NX) over WiFi for indoor scaling experiments, and on **5 real-world quad-rotor UAVs** over an ad-hoc link for outdoor experiments. It runs real collaborative DNN inference (ResNet/Faster-style workloads) and demonstrates elastic rescheduling when nodes drop. This is in-swarm *inference*, not RL training. Reported computing-latency cuts (up to 92.66% vs offloading) are measured on this testbed.
- **[[shao-2024-drl-antijamming-mec]]** — a DRL (PER-MATD3) anti-jamming resource manager validated on an **indoor** testbed: per the parse, a **Raspberry Pi 4B** mounted on each UAV for compute/communication, **USRP N210** (receive) and **USRP X310** (generate jamming) at 2.4 GHz over 5 channels, with the jammer attacking one channel. Channel selection holds latency ~4 s vs ~10.9-13.7 s without it. The authors flag the testbed as deliberately ideal (indoor, stable, large jamming power for clean sensing).
- **[[zhang-2020-response-delay-uav-swarm]]** — a stochastic-geometry + queueing response-delay design validated on **two DJI M100 quad-rotor UAVs** plus a **5G NR mmWave** system (28 GHz, 8x100 MHz carriers, 64-element phased arrays, hybrid beamforming). Running SURF-based video target detection on the MEC-equipped T-UAV cut packets transmitted to the control center by **89.9%** vs no-MEC (a 52 s / 7.84 Mbit stream reduced to nine key frames totalling 775.9 kbit). The headline algorithm result is a 10%-20% response-delay decrease.

## Below full validation

- **[[qu-ecoei-uav-swarm]] (eCoEI)** is a **proof-of-concept**, not a benchmark: a magazine architecture article whose prototype uses **four** Jetson devices (one Nano plans; one TX2 + two Nanos execute Faster R-CNN on a video stream, static UAV selection given the small swarm). It demonstrates elasticity — frame rate drops from ~3 FPS to ~2 FPS when a node's communication is disabled and recovers when it returns — but does not claim scaled performance. (Its **year is not in the parse**.) It is the architecture-level companion to the fully-validated ASAP from the same NUAA group.
- **[[sun-2024-imssa-uav-secure-cb]]** ports its collaborative-beamforming secure-communication algorithm onto a **Raspberry Pi** to demonstrate practicality "in real-world scenarios," but the study is otherwise simulation-based and the quantitative hardware results are figure-derived/indicative. It is a practicality demonstration, not a deployment — and a rare hardware touch in the otherwise simulation-only collaborative-beamforming track.
- **[[bai-2024-delay-aware-cooperative-edge-cloud]]** builds a **real UAV-edge platform to verify its model's correctness**; the delay-minimization algorithm itself is then evaluated in data-driven simulation on real-world datasets. So the platform validates the *modeling assumptions*, not the deployed algorithm — a distinct and weaker claim than ASAP's.

## Common sim-to-real challenges named by the sources

These are the gaps the sources themselves raise (grounded in their parses), not speculative — they are the concrete reasons simulation results may not transfer:

- **Testbeds are deliberately idealized.** [[shao-2024-drl-antijamming-mec]] runs **indoors** with a stable channel and intentionally large jamming power for clean spectrum sensing, and explicitly lists **outdoor settings** (weather, mobility) as future work. Clean-room conditions overstate real performance.
- **Scale is small and partly tethered.** ASAP's outdoor portion is **5 UAVs** (its 24-node experiments are stationary airborne computers over WiFi, not flying); eCoEI is **4** devices with static selection; zhang-2020 flies **2** UAVs. None approaches the swarm sizes assumed in the simulation literature, and node count is where ASAP's own results show latency can rebound.
- **Real flight dynamics break the simulation models.** [[query-real-world-validation-of-jppo-en-convntm]] enumerates the specifics for a representative DRL framework ([[liu-2026-jppo-en-convntm]], whose simulation setup is captured in [[drl-simulation-with-pomdp-formulation]]): wind/turbulence and battery telemetry that violate the constant-speed flight model, channel fluctuations that break LoS-only assumptions, hardware-induced action latency (the policy commits several steps before the UAV physically does), and unmodelled interference between concurrent uplinks.
- **Fault tolerance is asserted but lightly tested.** Both ASAP and eCoEI demonstrate recovery from a *single* induced node/link failure; volatile multi-failure swarm behaviour is flagged as open in both parses (eCoEI lists fast backups for the NP-hard partition problem under sudden unavailability as future work).
- **DRL training is never done on hardware.** Every validated build runs *inference* or a *pre-derived* policy/configuration on the device; none trains the RL policy on real hardware. The sim-to-real burden therefore lands entirely on whether a simulation-trained policy survives deployment — exactly the transfer question [[query-real-world-validation-of-jppo-en-convntm]] poses.

## Takeaways

- **Hardware validation is rare and shallow.** Three full deployments, one proof-of-concept, one practicality demo, and one model-verification platform — out of 171 sources. Any corpus-wide claim about real-world performance rests on this thin base.
- **The deepest validations are inference/configuration, not learning.** ASAP (collaborative inference), zhang-2020 (configuration + video detection), and shao-2024 (a trained DRL policy run on-device) all execute on hardware, but the *training* stays in simulation.
- **The sim-to-real gap is named consistently:** idealized testbeds, small/tethered scale, unmodelled flight-and-channel dynamics, and single-failure-only fault tests. These are the challenges a future deployment study would have to close, and they are grounded in what the sources already admit.

## See also

- [[query-real-world-validation-of-jppo-en-convntm]] — the framework-specific sim-to-real question this page generalizes.
- [[drl-simulation-with-pomdp-formulation]] — what a representative simulation setup actually models.
- [[overview]] — cross-cutting observation #8 (most papers are still simulation-only).
