---
type: source
title: "Trajectory Design and Beamforming in UAV-Assisted Wireless Networks: A Fine-Tuned M2LLM-Driven DRL-Based Framework"
authors: ["Baolin Yin", "Xuming Fang", "Xianbin Wang", "Li Yan", "Junjie Wu", "Jingyu Wang"]
year: 2026
url: "https://doi.org/10.1109/TWC.2025.3605277"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 3643-3657"
tags: [source, multi-uav, multimodal-large-language-model, ddpg, trajectory-prediction, beamforming, integrated-sensing-computation-communication]
related:
  - "[[m2llm-state-representation-for-drl]]"
  - "[[prediction-driven-joint-trajectory-beamforming]]"
  - "[[integrated-sensing-computation-communication]]"
  - "[[ddpg]]"
  - "[[uav-trajectory-control]]"
  - "[[sensing-assisted-predictive-beamforming]]"
  - "[[wang-2026-robust-multiuav-jtcra]]"
  - "[[xuming-fang]]"
  - "[[xianbin-wang]]"
created: 2026-07-14
updated: 2026-07-14
---

# Trajectory Design and Beamforming in UAV-Assisted Wireless Networks: A Fine-Tuned M2LLM-Driven DRL-Based Framework

## Citation

Yin, B., Fang, X., Wang, X., Yan, L., Wu, J., & Wang, J. (2026). *Trajectory Design and Beamforming in UAV-Assisted Wireless Networks: A Fine-Tuned M2LLM-Driven DRL-Based Framework*. **IEEE Transactions on Wireless Communications, 25**, 3643-3657. DOI: 10.1109/TWC.2025.3605277.

## TL;DR

Fine-tunes LLaVA with LoRA on AirSim images, sensed mobile-user positions, and task prompts, maps the model's final hidden layer into a fixed-dimensional DRL state, and lets centralized DDPG jointly control multi-UAV motion and beamforming from predicted next-period user trajectories.

## System model

- Multiple fixed-altitude array-equipped UAVs serve pre-associated mobile users in an obstacle-filled environment under communication-rate, sensing-SINR, power, separation, speed, and rotary-wing energy constraints.
- UAVs periodically sense user positions and capture images, then send observations to a base-station edge server over a UAV-BS link whose communication cost and performance are outside the model.
- The same beam supports communication and sensing through time division; narrow beams are assumed to remove inter-UAV interference.
- The non-convex objective is average sum rate over UAV trajectories and beamformers.

## Method

- AirSim supplies multimodal training samples. LoRA-tuned LLaVA predicts next-period user paths from images, position history, and task text.
- [[m2llm-state-representation-for-drl]] maps the model's last hidden layer to a fixed-dimensional state rather than using generated text as control input.
- Centralized DDPG chooses every UAV's direction, speed, and beamforming vector. Output beams are normalized and power is allocated by water filling.
- [[prediction-driven-joint-trajectory-beamforming]] executes prediction and control one period ahead. The method is heuristic: no convergence, optimality, robustness, or generalization theorem is given.

## Findings

- The fine-tuned multimodal predictor is less sensitive to history-window length than the plotted single-modal predictors, but no exact prediction-error values are stated in prose.
- In the tested controller, a 30-dimensional state and DDPG outperform the tested alternatives; this is task-specific model selection, not general DDPG superiority.
- The method remains highest-rate as user speed rises and under one changed AirSim obstacle layout.
- One trajectory figure labels average rates of 233.12 Mbps for the full method, 209.12 Mbps for multimodal prediction with a conventional state, 152.67 Mbps for separated trajectory/beam tracking, and 105.64 Mbps for real-time-state DDPG. These values belong to that plotted example.

## Limitations

All evidence is synthetic AirSim simulation. There is no real multimodal/channel dataset, UAV experiment, hardware latency, memory/energy measurement, confidence interval, or seed analysis. The dedicated observation uplink is unmodeled, user association is fixed, and full observability is assumed. A fixed-dimensional state does not by itself solve the variable-size action vector for changing UAV/user counts. The parsed reward signs and sensing-time accounting are internally questionable, so they are not reproduced as exact equations.

## Relation to the corpus

The complete author team also produced [[wang-2026-robust-multiuav-jtcra]], which controls energy-depletion-aware multi-UAV resources with MARL. This paper instead uses multimodal user-motion prediction and centralized continuous control for beamforming and trajectory decisions.

## Raw artifacts

- Parse: `raw/sources/Trajectory_Design_and_Beamforming_in_UAV-Assisted_Wireless_Networks_A_Fine-Tuned_M2LLM-Driven_DRL-Based_Framework/Trajectory_Design_and_Beamforming_in_UAV-Assisted_Wireless_Networks_A_Fine-Tuned_M2LLM-Driven_DRL-Based_Framework.md`
- Original PDF and extracted figures are in the same folder.
