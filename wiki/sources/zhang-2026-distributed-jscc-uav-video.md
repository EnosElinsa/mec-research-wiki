---
type: source
title: "Distributed Deep Joint Source-Channel Coding of Videos in Unmanned Aerial Vehicle Networks"
authors: ["Zhenguo Zhang", "Qianqian Yang", "Yiping Duan", "Zhiguo Shi", "Shibo He", "Xiaoming Tao", "Jiming Chen"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3700200"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, deep-jscc, distributed-video-coding, semantic-communication, dqn, uav-relaying, energy-balancing]
related:
  - "[[distributed-joint-source-channel-coding]]"
  - "[[semantic-communication]]"
  - "[[deep-q-network]]"
  - "[[energy-balancing-uav]]"
  - "[[uav-mobile-relaying]]"
  - "[[air-to-ground-channel-model]]"
created: 2026-07-13
updated: 2026-07-13
---

# Distributed Deep Joint Source-Channel Coding of Videos in Unmanned Aerial Vehicle Networks

## Citation

Zhang, Z., Yang, Q., Duan, Y., Shi, Z., He, S., Tao, X., & Chen, J. (2026). *Distributed Deep Joint Source-Channel Coding of Videos in Unmanned Aerial Vehicle Networks*. **IEEE Transactions on Mobile Computing**, 1-16. DOI: 10.1109/TMC.2026.3700200.

## TL;DR

Moves most video-reconstruction complexity from resource-constrained UAV encoders to ground decoders through distributed DeepJSCC with key and Wyner-Ziv-inspired frames. Per-UAV DQNs jointly select direct or amplify-forward links and transmit power to balance reconstruction quality against residual transmission energy.

## Problem

UAV video requires high fidelity under mobile, bandwidth-limited links, but deep video encoders are expensive onboard and repeated high-power transmission shortens network life. Traditional distributed video coding shifts work to the decoder but can require feedback and inaccurate side information. The paper combines lightweight neural source-channel encoding with receiver-side reconstruction and adaptive relay/power control.

## System model

- Multiple UAVs at varying altitudes transmit video to mobile ground users directly or through another UAV acting as a two-hop amplify-forward relay.
- Topology updates in time slots; UAVs and users follow exogenous random walks, with minimum UAV separation and quasi-static channel state inside each slot.
- Links use probabilistic LoS/NLoS loss, AWGN, and assumed perfect receiver-side Doppler mitigation.
- Each GoP has two key frames and intermediate predictive frames. Key and Wyner-Ziv-inspired features are independently encoded onboard; decoded key frames provide receiver-side information for predictive-frame reconstruction.
- The system constrains power, energy, association, one served destination per UAV/slot, spatial bounds, minimum video quality, and mode-dependent direct/relay SNR.

## Method

[[distributed-joint-source-channel-coding]] uses strided embedding/merging and FastNet split-process-concatenate blocks so only part of each feature map receives expensive spatial convolution. Receiver-side key-frame decoders use convolution, IGDN, PReLU, noise attention, and attention-feature modules. The predictive branch interpolates side information between decoded key frames and fuses it with transmitted features through dense, UNet, squeeze-excitation, attention, and deformable-convolution modules.

After codec training, one [[deep-q-network|DQN]] per UAV maps normalized UAV/user location, channel/noise state, and residual energy to transmit power plus direct-user or relay association. Replay memory, a target network, and epsilon-greedy exploration train the policy. Reward gives effective transmission utility minus an energy-dependent power penalty; as residual energy falls, costly links and powers receive larger penalties.

## Key findings

- For 1080p video, UAV-side complexity is `82.88 GFLOPs`, versus `4593.79G` for DCVC, `2859.12G` for DVC, `500.45G` for L-DVC, and `503.66G` for FIVSSC; this is `1.81%`, `2.89%`, and `16.56%` of the first three baselines.
- Removing side information lowers PSNR by `0.642 dB` and MS-SSIM by `0.023`; removing the predictive-frame decoder lowers them by `0.596 dB` and `0.021`.
- Relative to nearest-user greedy selection, completed rounds rise by `13.62%` with four UAVs and `24.36%` with twelve; termination residual energy is `8.03%` lower and reported swarm operational lifetime is `17.34%` longer.
- Relay-link-only and power-only ablations shorten hovering time by `11.04%` and `6.07%` relative to joint optimization.
- Under poor channels the method generally trails heavier neural codecs; under favorable channels it can match or exceed them at much lower UAV-side complexity.

## Limitations / parse caveats

The GoP boundary model idealizes the preceding last key frame as identical to the next first key frame. The design is Wyner-Ziv-inspired neural JSCC rather than classical syndrome/binning coding. Mobility is exogenous random walk, per-slot CSI is quasi-static, and Doppler compensation is perfect. Complexity is shifted to a receiver with the highest reported decoding time. The lifetime result excludes propulsion and encoder-computation energy, so it concerns transmission-energy network operation rather than total airborne endurance. Each UAV learns an individual DQN in small simulated swarms, and dense-network interference/contention remain open. Several equations and reward symbols are OCR-damaged. Publication metadata is absent from the parse and was verified through the exact-title Crossref record.

## Relation to the corpus

This source gives [[semantic-communication]] a resource-constrained video implementation distinct from image-oriented [[zhang-2025-gsc-diffusion-semcom]]. It combines distributed receiver-heavy coding with [[uav-mobile-relaying]] and [[energy-balancing-uav|residual-energy balancing]]; the paper's JSCC acronym means joint source-channel coding and is unrelated to the joint sensing/communication/computation controller named MAPPO-JSCC elsewhere in the corpus.

## Raw artifacts

- Parse: `raw/sources/Distributed_Deep_Joint_Source-Channel_Coding_of_Videos_in_Unmanned_Aerial_Vehicle_Networks/Distributed_Deep_Joint_Source-Channel_Coding_of_Videos_in_Unmanned_Aerial_Vehicle_Networks.md`
- Origin PDF: `raw/sources/Distributed_Deep_Joint_Source-Channel_Coding_of_Videos_in_Unmanned_Aerial_Vehicle_Networks/Distributed_Deep_Joint_Source-Channel_Coding_of_Videos_in_Unmanned_Aerial_Vehicle_Networks.pdf`
- Figures: `raw/sources/Distributed_Deep_Joint_Source-Channel_Coding_of_Videos_in_Unmanned_Aerial_Vehicle_Networks/images/`
