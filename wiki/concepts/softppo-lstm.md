---
type: concept
title: "SoftPPO-LSTM"
tags: [drl, ppo, lstm, collaborative-beamforming, iot, action-space, softmax]
related:
  - "[[ppo]]"
  - "[[omrp-overlap-routing]]"
  - "[[collaborative-beamforming]]"
  - "[[hybrid-action-representation]]"
  - "[[beta-policy-drl]]"
  - "[[j-ppo-vs-pdqn]]"
  - "[[hot-spot-problem-iot]]"
  - "[[li-2025-omrp-cb-iot]]"
created: 2026-06-03
updated: 2026-06-03
---

# SoftPPO-LSTM

SoftPPO-LSTM is a [[ppo]]-based DRL algorithm for combinatorial node selection in IoT collaborative beamforming (CB). It extends PPO with two targeted modifications — **softmax output control** and an **LSTM feature encoder** — and is proposed in [[li-2025-omrp-cb-iot]] for selecting CB nodes in an [[omrp-overlap-routing]]-based IoT framework.

## Problem it solves
Selecting which subset of N IoT nodes participates in CB is a 2^N combinatorial problem. SoftPPO-LSTM converts it to a continuous N-dimensional **scoring** problem: the actor outputs a score vector, and the top NCB nodes are selected. This is a lightweight alternative to full hybrid-action formulations such as [[hybrid-action-representation]] or [[parameterized-dqn]].

## Softmax enhancement
Softmax is applied to the actor's raw output scores before action sampling. It compresses score variance to stabilize backpropagation gradients in the large discrete-selection landscape, produces a probability distribution that guides systematic exploration, and smooths policy updates on top of PPO's clip mechanism. Reported ablation: softmax contributes +2.6% throughput over plain PPO.

## LSTM encoder
An LSTM layer in the shared feature network (before the actor and critic heads) handles long episodes (hundreds of rounds) where credit assignment is hard for feedforward networks, and adapts to the heuristic OMRP environment whose topology changes each round, giving the agent implicit access to temporal context. Reported ablation: LSTM contributes +6.5% throughput over plain PPO.

## MDP formulation
- **State:** {eᵢ(t), dᵢₛ(t)} for all nodes — residual energy and distance to the current sink node.
- **Action:** an N-dimensional continuous score vector; the top NCB scores select the beamforming nodes.
- **Reward:** rₜ = ζ₁Cₜ − ζ₂ Σᵢ(eᵢ(t) − eᵢ(t+1)) — throughput minus total network energy drain.

## Reported performance
Against DDPG / SAC / PPO on the 400-node simulation with OMRP routing, [[li-2025-omrp-cb-iot]] reports SoftPPO-LSTM transmitting ≈ 1.37×10⁹ bits: +8.3% over PPO, +10.9% over SAC, +19.5% over DDPG. Hardware deployment on a Raspberry Pi 4B used a 16 MB model with 324 MB peak memory and 0.02 s inference once the model is preloaded.

## Position in the wiki
SoftPPO-LSTM sits alongside [[beta-policy-drl]] and [[j-ppo-vs-pdqn]] as examples of policy-output engineering for large or structured action spaces. Unlike [[parameterized-dqn]] or [[j-ppo]], it stays entirely within PPO's on-policy framework — softmax is the only action-space modification — making it a minimal-overhead option when the main challenge is gradient stability rather than discrete/continuous action coupling.
