---
type: source
title: "A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach for UAV-Assisted Vehicular Networks With Delayed CSI Feedback"
authors: ["Zhang Liu", "Lianfen Huang", "Zhibin Gao", "Xianbin Wang", "Dusit Niyato", "Xuemin Shen"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3680987"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, vehicular-mec, uav-enabled-its, low-altitude-intelligent-network, lyapunov-optimization, diffusion-model-as-optimizer, ddpg, csi-estimation-error, uav-trajectory-control]
related:
  - "[[vehicular-mec]]"
  - "[[uav-enabled-its]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[lyapunov-optimization]]"
  - "[[diffusion-model-as-optimizer]]"
  - "[[generative-diffusion-model]]"
  - "[[ddpg]]"
  - "[[csi-estimation-error]]"
  - "[[uav-trajectory-control]]"
  - "[[air-to-ground-channel-model]]"
  - "[[dai-2024-uav-vehicular-offloading-lyapunov]]"
  - "[[peng-2020-maddpg-uav-vehicular]]"
  - "[[liu-2025-mad2rl-dnn-vec]]"
  - "[[dusit-niyato]]"
  - "[[xuemin-shen]]"
  - "[[xianbin-wang]]"
created: 2026-07-06
updated: 2026-07-14
---

# A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach for UAV-Assisted Vehicular Networks With Delayed CSI Feedback

## Citation

Liu, Z., Huang, L., Gao, Z., Wang, X., Niyato, D., & Shen, X. (2026). *A Lyapunov-Guided Diffusion-Based Reinforcement Learning Approach for UAV-Assisted Vehicular Networks With Delayed CSI Feedback*. **IEEE Transactions on Wireless Communications**, 25, 14797-14812. DOI: 10.1109/TWC.2026.3680987.

## TL;DR

Optimizes a UAV-assisted vehicular network where V2U links upload sensing data to a UAV aerial base station while V2V links exchange local safety data, and where V2V CSI arrives with feedback delay. The paper maximizes V2U sum rate under V2V reliability, joint channel/power/altitude decisions, and a long-term UAV energy constraint. Its solver combines Lyapunov drift-plus-penalty with a diffusion-model actor inside DDPG, producing a D3PG policy with an action-amender layer for feasible channel, power, and altitude choices.

## Problem framing

UAV-assisted vehicular networks can restore or supplement infrastructure in remote or post-disaster highway settings, but they must manage UAV energy while serving highly mobile vehicles. The hard part is not just trajectory or radio allocation alone: the controller must jointly choose V2V channel reuse, V2U/V2V transmit powers, and UAV altitude while respecting V2V reliability and long-term UAV propulsion energy. Delayed V2V CSI makes this harder because the controller observes aged channel states rather than the true instantaneous ones.

The parse frames the resulting long-term optimization as an NP-hard MINLP with binary channel allocation, continuous power/altitude variables, a long-term energy constraint, and delayed-CSI channel dynamics.

## System model

- A single UAV aerial base station follows vehicles on a unidirectional highway where terrestrial infrastructure is unavailable or damaged.
- V2U links upload sensing data to the UAV; V2V links exchange local data for incident reporting.
- OFDM divides the spectrum into orthogonal V2U channels; V2V pairs may reuse those channels with one V2V pair per V2U channel.
- V2U propagation uses a LoS/NLoS weighted air-to-ground channel model, while delayed V2V CSI is modeled by a first-order Gauss-Markov process with a Bessel-function correlation term.
- UAV communication power is treated as negligible relative to flight power, so the long-term UAV energy constraint is driven by propulsion.

## Method

- Introduces a virtual energy queue $Q(t)$ to track UAV flight-energy excess over the allowed threshold.
- Uses Lyapunov drift-plus-penalty with control weight $V$ to convert the long-term constrained objective into per-slot optimization subproblems.
- Represents D3PG state with V2U/V2V channel gains and the virtual queue; actions cover channel allocation, transmit powers, and altitude adjustment.
- Replaces the standard DDPG MLP actor with a diffusion-model denoiser actor, while retaining critic/target networks, replay buffer, TD updates, policy gradient, and soft target updates.
- Uses an action amender to map normalized continuous actor outputs into feasible channel, power, and altitude decisions.

## Key findings

- The authors report that denoising steps help until an intermediate value, after which too many steps degrade reward; they set the later experiments to four denoising steps.
- D3PG achieves the highest episodic reward against D3PG-WCSI, DDPG, and H-DDQN baselines.
- At 6 V2V links, D3PG improves V2U sum rate by 4.37% over D3PG-WCSI, 15.34% over DDPG, and 30.67% over H-DDQN; at 10 V2V links, the corresponding gains are 6.39%, 12.55%, and 23.25%.
- The moving-average UAV propulsion energy stays below the predefined long-term threshold, and D3PG reduces moving-average energy consumption by 2.15%, 4.58%, and 9.02% versus D3PG-WCSI, DDPG, and H-DDQN.
- As CSI feedback delay grows from 2 ms to 10 ms, outdated CSI becomes less correlated with the true channel and the performance gap between D3PG and the complete-CSI variant widens.
- Runtime is reported as 2.64-3.34 ms per slot for 6-10 V2V links, about 0.33% of a 1 s slot.

## Limitations / future work

The model uses a single UAV. The authors name three future directions: model V2U small-scale fading as Rician or Rayleigh depending on altitude/environment, extend to multi-UAV scenarios with inter-UAV coordination, and integrate faster generative sampling such as flow matching.

## Relation to the corpus

This is the vehicular counterpart to the corpus's broader [[lyapunov-optimization]] + DRL hybrid pattern. It is closest to [[dai-2024-uav-vehicular-offloading-lyapunov]] because both use Lyapunov machinery for UAV-assisted vehicular systems, but differs by adding delayed CSI and using a [[diffusion-model-as-optimizer|diffusion actor]] inside [[ddpg]]. It also complements [[liu-2025-mad2rl-dnn-vec]], where diffusion is used for VEC task offloading and DNN partitioning rather than V2X channel/power/altitude control. Co-authors [[dusit-niyato]] and [[xuemin-shen]] tie it to the wiki's recurring senior MEC/resource-management network.

## Raw artifacts

- Parse: `raw/sources/A_Lyapunov-Guided_Diffusion-Based_Reinforcement_Learning_Approach_for_UAV-Assisted_Vehicular_Networks_With_Delayed_CSI_Feedback/A_Lyapunov-Guided_Diffusion-Based_Reinforcement_Learning_Approach_for_UAV-Assisted_Vehicular_Networks_With_Delayed_CSI_Feedback.md`
- Origin PDF: `raw/sources/A_Lyapunov-Guided_Diffusion-Based_Reinforcement_Learning_Approach_for_UAV-Assisted_Vehicular_Networks_With_Delayed_CSI_Feedback/A_Lyapunov-Guided_Diffusion-Based_Reinforcement_Learning_Approach_for_UAV-Assisted_Vehicular_Networks_With_Delayed_CSI_Feedback.pdf`
- Figures: `raw/sources/A_Lyapunov-Guided_Diffusion-Based_Reinforcement_Learning_Approach_for_UAV-Assisted_Vehicular_Networks_With_Delayed_CSI_Feedback/images/`
