---
type: concept
title: "Expert-Guided Warm-Start RL"
tags: [drl, imitation-learning, exploration, sample-efficiency, actor-critic]
related:
  - "[[drl-backbones-across-uav-mec-sources]]"
  - "[[ddpg]]"
  - "[[mou-2025-adm-dt-migration]]"
  - "[[li-2026-la4h-uav-active-tracking]]"
  - "[[expert-assisted-anomaly-aware-tracking]]"
  - "[[li-2026-secrecy-ee-uav-ris-iov]]"
  - "[[chen-2026-hammurabi-cooperation]]"
created: 2026-06-03
updated: 2026-07-13
---

# Expert-Guided Warm-Start RL

A training technique that bootstraps a reinforcement-learning agent with **expert demonstrations** before (and during the early phase of) ordinary trial-and-error learning. The agent is first pre-trained to imitate an expert policy, and the proportion of expert guidance is then **progressively diminished** so the agent transitions from imitation toward autonomous policy improvement. The aim is to overcome poor exploration in sparse or hard-to-reach state spaces and to accelerate convergence.

## Why it helps

In environments where useful states are rarely visited by a randomly-initialized policy — e.g. fast-changing topologies driven by high mobility — a from-scratch agent wastes many episodes before encountering informative transitions. Seeding the policy with expert behavior gives it meaningful actions from the first episodes, then the decaying-demonstration schedule lets it surpass the (possibly sub-optimal) expert rather than being capped by it.

## In the corpus

[[mou-2025-adm-dt-migration]] applies this pattern to adaptive digital-twin migration in vehicular edge networks: it saves a Greedy heuristic's trajectories as the expert, pre-trains an off-policy actor-critic agent on them, and decays the demonstration proportion over training. The reported final-reward ordering ADM > DRL-PT (pre-training only) > DRL (from scratch) > Greedy isolates the contribution of both the pre-training and the warm-start schedule. Because the expert is a heuristic, the warm-start's floor is bounded by that heuristic's quality. It is a sample-efficiency lever orthogonal to the choice of [[drl-backbones-across-uav-mec-sources|DRL backbone]].

[[li-2026-la4h-uav-active-tracking]] is adjacent but not identical: [[expert-assisted-anomaly-aware-tracking]] treats expert help as an online recovery action during UAV active tracking, while still using teacher-student distillation to make the policy deployable.

[[li-2026-secrecy-ee-uav-ris-iov]] uses a looser heuristic-guided variant: a firefly optimizer generates high-quality UAV-coordinate samples that seed a DDPG replay buffer. It does not imitate a demonstrated policy, but it applies the same warm-start principle of replacing uninformative early exploration with structured prior experience.

[[chen-2026-hammurabi-cooperation]] exposes a second risk: demonstrations transfer social behavior as well as useful actions. Its [[pretrained-policy-cooperation-shaping]] diagnoses rule policies as relatively cooperative or defect-oriented before selecting inequality-aversion reward shaping for fine-tuning.
