---
type: source
title: "Embodied Intelligence-Enhanced Anti-Jamming Resource Allocation for Low-Altitude Communication Networks"
authors: ["Helin Yang", "Honglin Du", "Qing Geng", "Changyuan Xu", "Zehui Xiong"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3677272"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC), vol. 25, pp. 14750-14765"
tags: [source, low-altitude-network, anti-jamming, embodied-intelligence, multi-agent-ddqn, spectrum-allocation, power-control, hardware-experiment]
related:
  - "[[embodied-anti-jamming-resource-allocation]]"
  - "[[anti-jamming-mec]]"
  - "[[multi-domain-uav-anti-jamming]]"
  - "[[spectrum-sensing-channel-selection]]"
  - "[[ddqn]]"
  - "[[prioritized-experience-replay]]"
  - "[[zehui-xiong]]"
  - "[[shao-2024-drl-antijamming-mec]]"
  - "[[chen-2026-maddpg-uav-swarm-antijamming]]"
created: 2026-07-13
updated: 2026-07-13
---

# Embodied Intelligence-Enhanced Anti-Jamming Resource Allocation for Low-Altitude Communication Networks

## Citation

Yang, H., Du, H., Geng, Q., Xu, C., & Xiong, Z. (2026). *Embodied Intelligence-Enhanced Anti-Jamming Resource Allocation for Low-Altitude Communication Networks*. **IEEE Transactions on Wireless Communications**, 25, 14750-14765. DOI: 10.1109/TWC.2026.3677272.

## TL;DR

Treats each UAV-to-UAV link as an embodied resource-allocation agent that observes channel, load, deadline, and jammer state, then selects a reused uplink sub-band and discrete transmit power. A multi-agent DDQN combines prioritized replay with transferred source-task experiences to reduce U2U/U2I delay and energy penalties under swept jamming.

## Problem

LoS-dominant low-altitude links expose UAV traffic to malicious jamming and co-channel interference. The controller must allocate spectrum and power online while protecting U2U signaling, U2I access, transmission deadlines, and UAV energy in a changing channel environment.

## System model

- Multiple constant-altitude UAVs maintain U2U links and U2I uplinks. Each U2I link has an orthogonal sub-band and fixed power; U2U links cognitively reuse those bands.
- Channels combine distance loss, log-normal shadowing, and Rician fading. The jammer sweeps channels, while UAV position is quasi-static inside a decision slot.
- Each agent observes channel/band state, jammer behavior, data load, and remaining transmission time. Its action is a sub-band and one discrete U2U power level.
- The reward penalizes weighted U2U/U2I delay, flight/transmit energy, and deadline failure. All agents share the cooperative return.

## Method

E-MA-DDQN-PER-TL-IRA separates action selection and target evaluation through DDQN, samples shared replay transitions by TD-error priority, and seeds the target replay buffer with source-MDP experiences. UAVs execute locally after common replay-based training and share sensing/action information during learning.

The paper calls this [[embodied-anti-jamming-resource-allocation]] because an aircraft senses the radio environment, decides, and physically applies resource actions. Its evaluated embodiment is channel/jammer-state control; vision, radar, and lidar are mentioned as possible sensors but are not implemented in the reported controller.

## Key findings

- Simulations use a `500 x 500 m` grid, 10-30 UAVs, 7-19 sub-bands, 100 m UAV/jammer altitude, and 23 dBm jammer power.
- U2U delay falls as UAV count grows, whereas U2I delay rises as more UAVs contend for infrastructure access; at the densest simulated setting, the paper notes a slight DDQN advantage rather than universal dominance by the proposed method.
- The prose reports only `3%` transmission-success degradation as jammer power rises, but the linked plot shows a materially larger drop and uses different baseline labels. The percentage is therefore source-conflicted and is not treated as a verified curve value.
- A hardware-channel experiment equips UAV-side platforms with Raspberry Pi 4B boards and uses a USRP N210 ground receiver. It reproduces the qualitative delay trends, but the parse omits airframe count, geometry, jammer hardware, repetitions, and uncertainty statistics.

## Limitations / parse caveats

The parse alternates between one and two jammers, and its optimization equation is too damaged to reconstruct. Remaining energy appears in method prose but not the printed state vector; equation references and complexity notation conflict; baseline names differ between setup and figures; and no confidence intervals or independent-run counts are given. Transfer can be harmful when source experience is poorly matched, but no similarity gate or negative-transfer test is reported. The conclusion's lower-complexity claim is not established by the per-iteration analysis.

## Relation to the corpus

This is a value-based counterpart to the MADDPG controller in [[chen-2026-maddpg-uav-swarm-antijamming]]. It is adjacent to [[shao-2024-drl-antijamming-mec]], but protects communication delay rather than task-offloading service. The distinctive additions are experience-transfer DDQN and the explicit perception-decision-action framing.

## Raw artifacts

- Parse: `raw/sources/Embodied_Intelligence-Enhanced_Anti-Jamming_Resource_Allocation_for_Low-Altitude_Communication_Networks/Embodied_Intelligence-Enhanced_Anti-Jamming_Resource_Allocation_for_Low-Altitude_Communication_Networks.md`
- Origin PDF: `raw/sources/Embodied_Intelligence-Enhanced_Anti-Jamming_Resource_Allocation_for_Low-Altitude_Communication_Networks/Embodied_Intelligence-Enhanced_Anti-Jamming_Resource_Allocation_for_Low-Altitude_Communication_Networks.pdf`
- Figures: `raw/sources/Embodied_Intelligence-Enhanced_Anti-Jamming_Resource_Allocation_for_Low-Altitude_Communication_Networks/images/`
