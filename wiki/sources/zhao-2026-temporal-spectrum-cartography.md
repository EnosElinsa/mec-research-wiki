---
type: source
title: "Temporal Spectrum Cartography in Low-Altitude Economy Networks: A Generative AI Framework With Multi-Agent Learning"
authors: ["Changyuan Zhao", "Ruichen Zhang", "Jiacheng Wang", "Dusit Niyato", "Geng Sun", "Hongyang Du", "Zan Li", "Abbas Jamalipour", "Dong In Kim"]
year: 2026
url: "https://doi.org/10.1109/TMC.2025.3647029"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC), vol. 25, no. 6, pp. 8016-8033, Jun. 2026"
tags: [source, low-altitude-economy, temporal-spectrum-cartography, generative-ai, generative-diffusion-model, multi-agent-learning, uav-trajectory-control]
related:
  - "[[temporal-spectrum-cartography]]"
  - "[[multi-agent-diffusion-policy]]"
  - "[[low-altitude-intelligent-network]]"
  - "[[spectrum-sensing-channel-selection]]"
  - "[[uav-trajectory-control]]"
  - "[[generative-ai-for-mec]]"
  - "[[generative-diffusion-model]]"
  - "[[maddpg]]"
  - "[[ppo]]"
modeling_card: required
created: 2026-07-07
updated: 2026-07-16
---

# Temporal Spectrum Cartography in Low-Altitude Economy Networks: A Generative AI Framework With Multi-Agent Learning

## Citation

Zhao, C., Zhang, R., Wang, J., Niyato, D., Sun, G., Du, H., Li, Z., Jamalipour, A., & Kim, D. I. (2026). *Temporal Spectrum Cartography in Low-Altitude Economy Networks: A Generative AI Framework With Multi-Agent Learning*. **IEEE Transactions on Mobile Computing**, 25(6), 8016-8033. DOI: 10.1109/TMC.2025.3647029. DOI evidence appears in the local parse and was cross-checked against title-matched DOI metadata.

## TL;DR

Builds temporal RF power maps for low-altitude economy networks using sparse static and mobile sensor measurements. The two-stage framework combines a RecMAE masked-autoencoder reconstructor for temporal spectrum maps with MADP, a multi-agent diffusion policy that plans mobile UAV sensor movement to reduce reconstruction error over time.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Static sensors and fixed-altitude UAV-mounted dynamic sensors sample RSSI on a gridded low-altitude economy network over multiple time slots. The model uses sensing footprints rather than a multiple-access scheduler and generates RF power maps with probabilistic LoS/NLoS path loss and spatially correlated shadow fading.

**Problem & objective**: Equations (13)-(17), a constrained temporal tensor-completion and cooperative POMDP problem, minimize cumulative reconstruction error $E=\sum_{t=1}^{n_T}\lVert\tilde{\mathbf P}^{t}-\hat{\mathbf P}^{t}\rVert_2$ by selecting time-varying UAV sensing locations.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Sensing mask | $\mathbf W^t$ | Binary matrix | Mark grid cells observed by a static or dynamic sensor in slot $t$ |
| Dynamic-sensor positions | $\mathcal U_t=\{(x_u^t,y_u^t)\}$ | Discrete grid coordinates | Locations of all UAV sensors in slot $t$ |
| UAV movement action | $a_t^i$ | Continuous actor output, bounded by $a_{\max}=1$ and mapped to feasible grid motion | Select UAV $i$'s next sensing position |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | A mask entry is one only when the grid cell lies within a dynamic or static sensor's sensing radius, as in (15) |
| C2 | Each UAV move is bounded by $d((x_u^t,y_u^t),(x_u^{t+1},y_u^{t+1}))\le d_m$ |
| C3 | Sensor counts remain fixed at $M_d$ dynamic UAV sensors and $M_s$ static sensors for every slot |
| C4 | UAV actions remain within the gridded sensing region and the configured per-slot movement limit |

**Algorithm**: Train RecMAE with pixel-level and patch-level masks $\rightarrow$ use reconstruction error as the shared planning reward $\rightarrow$ encode observation histories with 3D convolution and temporal attention $\rightarrow$ generate decentralized UAV actions with diffusion actors and train centralized critics from replayed experience.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhao et al. [x] studied temporal spectrum cartography in low-altitude economy networks with sparse static sensors and mobile UAV sensors. They formulated dynamic sensor placement as a temporal tensor-completion and cooperative trajectory-planning problem that minimizes cumulative spectrum-map reconstruction error. Their two-stage generative AI framework first trains RecMAE with pixel-level and patch-level masking to reconstruct temporally varying RF power maps. It then uses MADP, a multi-agent diffusion policy with temporal-attention encoding and centralized critic training, to select UAV sensing trajectories. Simulations report a cumulative reconstruction MSE of 50.00 for MADP, compared with 153.91 for CNN-based MADDPG, 95.04 for its attention variant, 192.91 for PPO, and 361.77 for random movement.

## Problem

Low-altitude UAV, UAM, logistics, agriculture, and surveillance services intensify spectrum congestion and interference. Static spectrum maps do not capture fast temporal variation, and dense sensing is expensive. The paper therefore treats temporal spectrum cartography as a sparse sensing plus mobile sensor placement problem.

## System model

The scenario is a gridded urban low-altitude network with static sensors and dynamic UAV-mounted sensors at a fixed altitude. Each sensing period is split into slots: sensors measure a grid-state/RSSI map, dynamic sensors move to adjacent grids for the next slot, and the objective is to reconstruct the temporal spectrum tensor. The propagation model includes probabilistic LoS/NLoS path loss and spatially correlated shadow fading. The optimization target is cumulative reconstruction error under movement and sensor-count constraints.

## Method

The framework has two stages:

- **RecMAE reconstructor.** A masked autoencoder uses 3D tubelet/patch embedding, transformer encoder/decoder blocks, fixed sinusoidal positional encodings, and dual masking. Pixel-level masking simulates sparse sensors; patch-level masking withholds regions.
- **MADP planner.** A multi-agent POMDP controls dynamic UAV sensors. A diffusion-based actor with a temporal-attention state encoder proposes movement policies; a centralized critic supports training and decentralized execution. The shared reward is tied to spectrum-map reconstruction error.

## Key findings

- RecMAE is strongest in sparse sensing. At 3% sensing, the parse reports MSE 0.90 in Urban-1 versus 7.95 for AE, 3.94 for cGAN, and 2.11 for Kriging; in Urban-2, 0.178 versus 23.56, 1.81, and 0.382; in Suburban, 0.119 versus 15.42 for AE and 178.81 for cGAN.
- RecMAE inference takes about 24-26 seconds over the test dataset and under 6 seconds per batch in the parse, slower than AE/cGAN but much faster than NN/Kriging baselines and acceptable relative to the sensing-window discussion.
- MADP achieves cumulative MSE 50.00 versus 153.91 for CNN, 95.04 for CNN-Attention, 192.91 for PPO, and 361.77 for Random in the reported comparison.
- Static sensor density matters: the parse reports MSE 20.34 at spacing 4, 34.10 at spacing 8, 50.00 at spacing 16, and 225.71 without static sensors.
- More dynamic UAV sensors improve reconstruction: one, two, and three UAVs degrade relative to the four-UAV case in the parse.

## Limitations / future work

The conclusion in the parse does not list future work. The paper notes practical cost tradeoffs: the diffusion planner adds multi-step inference overhead, RecMAE is slower than AE/cGAN despite acceptable timing in the reported setup, and removing static sensors severely degrades reconstruction.

## Relation to the corpus

This source turns the LAE spectrum problem into [[temporal-spectrum-cartography]] rather than conventional channel selection. It complements [[yang-2026-generative-radio-map-lae]] on generative radio maps and [[zhao-2025-networked-isac-uav-handover]] on sensing-aware LAE control. Methodologically it adds [[multi-agent-diffusion-policy]] to the wiki's generative-AI optimization vocabulary.

## Raw artifacts

- `raw/sources/Temporal_Spectrum_Cartography_in_Low-Altitude_Economy_Networks_A_Generative_AI_Framework_With_Multi-Agent_Learning/Temporal_Spectrum_Cartography_in_Low-Altitude_Economy_Networks_A_Generative_AI_Framework_With_Multi-Agent_Learning.md`
- Original PDF and extracted figures (`images/`) in the same folder.
