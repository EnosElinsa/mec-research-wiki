---
type: source
title: "Generalizable Pareto-Optimal Offloading With Reinforcement Learning in Mobile Edge Computing"
authors: ["Ning Yang", "Junrui Wen", "Meng Zhang", "Ming Tang"]
year: 2025
url: "https://doi.org/10.1109/TSC.2025.3604371"
venue: "IEEE Transactions on Services Computing (IEEE TSC)"
tags: [source, mobile-edge-computing, multi-objective-reinforcement-learning, soft-actor-critic, contextual-momdp, task-offloading, energy-latency-tradeoff]
related:
  - "[[multi-objective-reinforcement-learning]]"
  - "[[multi-objective-mdp-vectorial-reward]]"
  - "[[contextual-momdp]]"
  - "[[soft-actor-critic]]"
  - "[[task-offloading]]"
  - "[[energy-latency-tradeoff]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[non-dominated-sorting-genetic-algorithm]]"
  - "[[song-2024-mol-aoi-energy]]"
created: 2026-07-07
updated: 2026-07-07
---

# Generalizable Pareto-Optimal Offloading With Reinforcement Learning in Mobile Edge Computing

## Citation

Yang, N., Wen, J., Zhang, M., & Tang, M. (2025). *Generalizable Pareto-Optimal Offloading With Reinforcement Learning in Mobile Edge Computing*. **IEEE Transactions on Services Computing**. DOI: 10.1109/TSC.2025.3604371.

## TL;DR

Frames MEC offloading as a **multi-objective** delay-vs-energy problem with unknown user preferences and heterogeneous edge deployments. Instead of training one policy per weight vector, the proposed GMORL trains a single **Discrete-SAC** policy conditioned on preference weights, server count, and CPU frequencies. A histogram-based state encoding and masked fixed-size server action head let the policy generalize across MEC systems with different numbers of edge servers and compute capacities. The reported hypervolume is close to a multi-policy MORL upper-bound baseline while requiring only one deployable policy.

## Problem framing

Classical MEC offloading often fixes a weighted energy-latency objective before optimization, but real operators may change preferences between latency and battery life. Training a separate RL policy for every weight is expensive and does not transfer well when the number or speed of edge servers changes. This paper targets a reusable policy that approximates the Pareto frontier across both **preference context** and **system context**.

## System model

- **Topology.** Multiple users submit tasks to one cloud server and $E$ edge servers.
- **Time model.** Tasks arrive under a stochastic process and are queued FIFO; execution is modeled in continuous time with discrete decision steps.
- **Offloading action.** Each task is assigned to one server; the problem is binary server selection, not partial bit splitting.
- **Objectives.** Vector reward tracks delay utility and energy utility; preference vector $(\omega_T,\omega_E)$ scalarizes the reward only for policy optimization.
- **Context.** The policy observes the preference vector, number of edge servers, and CPU-frequency profile.

## Method

GMORL formulates the problem as a contextual multi-objective MDP. The state encodes server-level information including task size, data rate, CPU frequency, current executing tasks, server count, and a histogram of residual task sizes; dummy edge servers pad the action/state shape. The policy uses a per-server neural architecture with masking to ignore nonexistent servers, and a Discrete-SAC update to learn stochastic offloading decisions. The same trained policy can be queried with different preference vectors to sweep the Pareto frontier.

## Key findings

- Overall hypervolume is reported as 64.1 for GMORL, compared with 57.9 for LinUCB, 64.3 for a multi-policy MORL reference, 30.2 for simulated annealing, and 29.0 for random scheduling.
- GMORL improves hypervolume by 10.7% versus LinUCB, 112.3% versus simulated annealing, and 121.0% versus random scheduling, while remaining only 0.3% below the multi-policy reference.
- Under CPU-frequency generalization, GMORL reports a hypervolume of 80.29 versus an 81.69 reference, about 1.7% error.
- Generalization to a server count outside the training range works but shows a larger gap, indicating server-count extrapolation is harder than CPU-frequency interpolation.

## Limitations / future work

The maximum number of schedulable edge servers is fixed by the network architecture and training maximum, and performance degrades for server counts outside the training context. Explicit future-work statements are `not in parse`.

## Relation to the corpus

This is a **general MEC offloading theory** entry rather than a UAV-specific one. It complements [[song-2024-mol-aoi-energy]] by replacing multi-policy evolutionary MORL with a single context-conditioned SAC policy. It also contrasts with fixed-weight [[energy-latency-tradeoff]] formulations by keeping the preference vector as an input and with [[non-dominated-sorting-genetic-algorithm]]-style Pareto search by learning a reusable scheduler.

## Raw artifacts

- `raw/sources/Generalizable_Pareto-Optimal_Offloading_With_Reinforcement_Learning_in_Mobile_Edge_Computing/Generalizable_Pareto-Optimal_Offloading_With_Reinforcement_Learning_in_Mobile_Edge_Computing.md`
- Original PDF and extracted figures (`images/`) in the same folder.
