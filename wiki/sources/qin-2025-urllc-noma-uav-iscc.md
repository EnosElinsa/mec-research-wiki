---
type: source
modeling_card: required
title: "URLLC-Aware Trajectory Plan and Beamforming Design for NOMA-Aided UAV Integrated Sensing, Communication, and Computation Networks"
authors: ["Peng Qin", "Yang Fu", "Zhigang Yu", "Jing Zhang", "Xiongwen Zhao"]
year: 2025
url: "https://doi.org/10.1109/TVT.2024.3460813"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, uav-mec, isac, iscc, noma, urllc, beamforming, trajectory-optimization, soft-actor-critic, lyapunov-optimization]
related:
  - "[[integrated-sensing-computation-communication]]"
  - "[[finite-blocklength-urllc]]"
  - "[[lyapunov-optimization]]"
  - "[[soft-actor-critic]]"
  - "[[uav-trajectory-control]]"
  - "[[wu-2024-urllc-uav-mec-latency]]"
  - "[[wen-2024-iscc-edge-ai]]"
created: 2026-06-04
updated: 2026-07-16
---

# URLLC-Aware Trajectory Plan and Beamforming Design for NOMA-Aided UAV Integrated Sensing, Communication, and Computation Networks

## Citation

Qin, P., Fu, Y., Yu, Z., Zhang, J., & Zhao, X. (2025). *URLLC-Aware Trajectory Plan and Beamforming Design for NOMA-Aided UAV Integrated Sensing, Communication, and Computation Networks*. **IEEE Transactions on Vehicular Technology**, 74(1). DOI: 10.1109/TVT.2024.3460813. (Received 29 February 2024; accepted 11 September 2024; published 16 September 2024; current version 16 January 2025.)

## TL;DR

Proposes a NOMA-aided UAV ISCC (Integrated Sensing, Communication, and Computation) network where a multi-antenna UAV: (i) performs edge computing for ground users' URLLC tasks; (ii) transmits an ISAC beam that simultaneously senses targets and delivers communication; (iii) offloads partial tasks to a fog node. Jointly maximizes computation throughput by optimizing UAV trajectory, beamforming design (TPBD), and compute resource allocation under sensing quality, URLLC, and power constraints. URLLC constraints are handled via **extreme value theory + Lyapunov optimization** to bound queue tail probabilities; the joint trajectory + beamforming problem is solved by a **SAC-TPBD** (Soft Actor-Critic) DRL algorithm that adapts in real time to queue backlogs and URLLC deviations. Claims comparable performance to convex-approximation baselines with higher implementation efficiency.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: A multi-antenna UAV serves ground URLLC users with an edge server and a fog node. Uplink NOMA carries partial offloading, while a dual-function ISAC beam senses targets and communicates; sensing quality, queue-tail reliability, computation, and mobility are coupled in each slot.

**Problem & objective**: A Lyapunov-constrained non-convex program maximizes computation throughput, $\max\sum_k R_k^{\mathrm{comp}}$, subject to extreme-value-theory URLLC tail bounds, sensing SINR, power, task, and UAV-trajectory constraints.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| UAV trajectory | $\mathbf q(t)$ | continuous 2-D position | UAV movement over slots |
| ISAC beamforming | $\mathbf W(t)$ | complex continuous matrix | Dual-function sensing and communication beam |
| Offloading ratio | $\beta_k(t)$ | continuous, $[0,1]$ | Fraction of user $k$'s task sent to the UAV/fog node |
| Compute allocation | $f_k(t)$ | continuous, nonnegative | UAV edge-compute resource for user $k$ |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Queue-tail violation probabilities satisfy the URLLC bound derived from extreme-value theory |
| C2 | ISAC sensing SINR and beampattern quality exceed their thresholds |
| C3 | NOMA transmit powers and UAV total power remain within budgets |
| C4 | Offloaded bits, UAV/fog CPU capacity, and per-slot latency remain feasible |
| C5 | UAV trajectory obeys region, speed, and endpoint constraints |

**Algorithm**: Introduce Lyapunov virtual queues for URLLC violations → solve joint trajectory and beamforming with SAC-TPBD using queue-backlog observations → solve compute allocation by convex optimization → update virtual queues and repeat per slot.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Qin et al. [x] studied URLLC-aware trajectory and beamforming design for a NOMA-aided UAV integrated sensing, communication, and computation network. They formulated a throughput-maximization problem that jointly optimizes UAV trajectory, ISAC beamforming, partial offloading, and compute resources under sensing-quality, power, queue-tail, and URLLC constraints. Extreme value theory and Lyapunov optimization transform the long-term tail constraint into per-slot virtual-queue problems. SAC-TPBD learns the joint trajectory and beamforming block, while a convex subproblem allocates computation resources. The paper reports comparable computation and beampattern performance to convex-approximation baselines with higher implementation efficiency and lower task queue backlogs in the evaluated simulations.

## Problem framing

ISCC systems face intrinsic conflicts: radar sensing competes with communication for power; task offloading signals interfere with sensing echoes; URLLC requires bounding the *tail* of delay distributions (not just the mean), which classical convex optimization cannot handle. NOMA addresses inter-functionality interference via SIC (decode and cancel offloading signals before processing radar echoes). UAV mobility provides extra DoFs to position the aerial node favorably for all three functions. Handling long-term URLLC tail constraints while co-optimizing a continuous trajectory + beamforming + resource allocation is the core challenge.

## System model

- **UAV** with M antennas + edge server; **fog node** (powerful offsite compute); **K offloading users** (URLLC tasks); **P sensing targets**.
- **NOMA uplink:** multiple users share the uplink band; SIC at UAV decodes offloading signals before processing radar echoes, suppressing inter-functionality interference.
- **ISAC beam:** dual-function beam serves both downlink communication and radar sensing toward targets; beampattern quality is a constraint (sensing SINR ≥ threshold).
- **URLLC constraint:** characterized via extreme value theory (tail of queue delay distribution); Lyapunov optimization decouples original long-term problem into per-slot problems with virtual queue backlogs.
- **Decomposition:** subproblem 1 — joint trajectory + beamforming (SAC-TPBD, DRL); subproblem 2 — compute resource allocation (convex, solved given DRL output).
- **SAC-TPBD:** state includes real-time task queue backlogs and URLLC constraint violation counters; SAC (off-policy, entropy-regularized) adapts trajectory and beamforming to minimize URLLC violations while maximizing computation throughput.

## Key findings

- SAC-TPBD achieves **comparable computation performance and beampattern gains** to state-of-the-art convex approximation (SCA/SDR) algorithms with **higher implementation efficiency** (lower per-iteration complexity) (parse abstract + Section V).
- **Task queue backlogs are significantly reduced** by the URLLC-aware trajectory adaptation (UAV flies closer to users with large backlog), enabling URLLC constraint satisfaction (parse contributions + Section V).
- SAC-TPBD **converges faster and exhibits lower reward variance** than baseline DRL schemes (parse contribution 3 + Section V).
- NOMA-based SIC effectively alleviates inter-functionality interference in the ISCC setting compared to OMA baselines (parse contribution 1 + motivation).

## Limitations / future work

Single UAV. Fixed fog node — no joint fog placement optimization. The parse does not enumerate numerical figures for all metrics explicitly in extractable text.

## Relation to the corpus

Combines [[integrated-sensing-computation-communication]], [[finite-blocklength-urllc]] handling via Lyapunov tail-constraint analysis, [[soft-actor-critic]] DRL, and NOMA in a single UAV-ISCC paper — a configuration unique in the corpus. Connects to [[wu-2024-urllc-uav-mec-latency]] (also URLLC UAV-MEC, but convex optimization + finite-blocklength) and [[wen-2024-iscc-edge-ai]] (task-oriented ISCC for edge-AI inference). The Lyapunov + DRL hybrid pattern is shared with [[bai-2024-delay-aware-cooperative-edge-cloud]] and [[wang-2025-maddpg-lc-dynamic-trajectory]].

## Raw artifacts

- `raw/sources/URLLC-Aware_Trajectory_Plan_and_Beamforming_Design_for_NOMA-Aided_UAV_Integrated_Sensing_Communication_and_Computation_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
