---
type: source
modeling_card: required
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
updated: 2026-07-16
---

# Embodied Intelligence-Enhanced Anti-Jamming Resource Allocation for Low-Altitude Communication Networks

## Citation

Yang, H., Du, H., Geng, Q., Xu, C., & Xiong, Z. (2026). *Embodied Intelligence-Enhanced Anti-Jamming Resource Allocation for Low-Altitude Communication Networks*. **IEEE Transactions on Wireless Communications**, 25, 14750-14765. DOI: 10.1109/TWC.2026.3677272.

## TL;DR

Treats each UAV-to-UAV link as an embodied resource-allocation agent that observes channel, load, deadline, and jammer state, then selects a reused uplink sub-band and discrete transmit power. A multi-agent DDQN combines prioritized replay with transferred source-task experiences to reduce U2U/U2I delay and energy penalties under swept jamming.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A constant-altitude multi-UAV network contains $N$ U2U signaling links and $L$ U2I uplinks over OFDM sub-bands. U2I links have preassigned orthogonal bands and fixed powers, while U2U links cognitively reuse those bands under co-channel interference and swept malicious jamming.

**Problem & objective**: The anti-jamming resource problem minimizes the weighted U2U delay, U2I delay, and UAV energy represented by the negative base reward, $\min\ \eta T_n^{U2U}[l,t]+(1-\eta)T_l^{U2I}[l,t]+\chi\sum_{n\in\mathcal N}(P_{\mathrm{fly}}+P_n[l])\Delta t$.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Spectrum-reuse indicator | $\rho_n[l]$ | binary, $\{0,1\}$ | Selects the U2I sub-band reused by U2U link $n$ |
| U2U transmit power | $P_n[l]$ | discrete, $P_n[l]\in\{P_1,P_2,P_3,P_4\}$ | Chooses the transmit-power level on the selected band |
| Agent action | $a_t=[P_t,V_t]$ | discrete joint action | Combines power selection and sub-band selection at slot $t$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| a-b | Binary spectrum indicators enforce non-overlapping admissible reuse allocations |
| c | U2U power is selected from the four-level set $\{P_1,P_2,P_3,P_4\}$ |
| d | Each UAV transmit power is capped by $P_{\max}$ |
| e-g | Mission duration, energy, and designated flight-area limits are enforced |
| h | A link succeeds only when $0\le O_t^n\le O_{\max}^n$ |

**Algorithm**: The MAMDP state includes U2U and U2I channel conditions, jammer behavior, current band, payload, and remaining time. E-MA-DDQN-PER-TL learns cooperative actions with DDQN target evaluation, prioritizes high temporal-difference-error experiences, and transfers source-MDP experiences into the target replay buffer before decentralized execution.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Yang et al. [x] studied spectrum reuse and power control for multi-UAV U2U and U2I links exposed to swept jamming and co-channel interference. Their mixed discrete resource problem minimizes weighted transmission delay and energy while enforcing admissible band reuse, finite power levels, power budgets, flight limits, and transmission deadlines. Each U2U link is modeled as an embodied agent whose action selects a reused sub-band and a discrete transmit-power level from observed channel, jammer, load, and deadline states. The E-MA-DDQN-PER-TL solver combines double Q-learning, prioritized experience replay, and transferred source-task experiences to learn a cooperative anti-jamming policy. Simulations and the reported hardware-assisted channel experiment show lower transmission delay and higher successful-transmission probability than the compared DQN and DDQN variants.

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
