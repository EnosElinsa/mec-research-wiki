---
type: source
title: "Response Delay Optimization in Mobile Edge Computing Enabled UAV Swarm"
authors: ["Qixun Zhang", "Jingran Chen", "Lei Ji", "Zhiyong Feng", "Zhu Han", "Zhiyong Chen"]
year: 2020
url: "https://doi.org/10.1109/TVT.2020.2964821"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, multi-uav-assisted-mec, uav-swarm, stochastic-geometry-network-analysis, queueing-theory, response-delay, hardware-validated]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[queueing-theory]]"
  - "[[mmwave-radar-sensing]]"
  - "[[post-disaster-mec]]"
  - "[[zhang-2019-uav-iot-comp-comm]]"
  - "[[hardware-validation-and-sim-to-real-in-mec]]"
  - "[[zhu-han]]"
  - "[[qixun-zhang]]"
  - "[[zhiyong-feng]]"
created: 2026-05-31
updated: 2026-07-16
modeling_card: required
---

# Response Delay Optimization in Mobile Edge Computing Enabled UAV Swarm

## Citation

Zhang, Q., Chen, J., Ji, L., Feng, Z., Han, Z., & Chen, Z. (2020). *Response Delay Optimization in Mobile Edge Computing Enabled UAV Swarm*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2020.2964821. (Manuscript received 15 May 2019; date of publication 8 Jan 2020; date of current version 12 Mar 2020 → year 2020.)

## TL;DR

A two-layer MEC-enabled UAV swarm — a centralized **MEC-equipped top-UAV (T-UAV)** plus a swarm of distributed **bottom-UAVs (B-UAVs)** — for emergency scenarios (disaster rescue). Using **stochastic geometry** (3-D Poisson point process) the paper derives closed-form **successful transmission probability** for single and grouped links, and using **queueing theory** derives the **optimal response delay** in closed form over four delay indicators. A joint communication-and-computation optimization algorithm configures UAV density and number of VMs to minimize response delay, validated on both a simulator and a real **5G NR mmWave + DJI UAV hardware testbed**.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Bottom UAVs distributed as a three-dimensional Poisson point process send disaster data over mmWave links to a fixed-wing top UAV carrying an MEC server, which compresses the data before forwarding it to a control center. The top UAV supports concurrent SDMA beams, with TDMA or FDMA available for coincident beams; air links include distance-dependent loss, Rayleigh fading, AWGN, and inter-group sidelobe interference.

**Problem & objective**: Problem (38) minimizes end-to-end response delay, $\min T_{\mathrm{all-after}}=T_{\mathrm{comm-w}}+T_{\mathrm{comm-t}}+T_{\mathrm{comp-q}}+T_{\mathrm{comp-p}}+T_{\mathrm{comm-t}}^{T-C}$, by matching communication load and parallel MEC capacity.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Bottom-UAV density | $\lambda_u$ | continuous, positive | Spatial density that determines interference and aggregate arrivals |
| Packet arrival rate | $\lambda$ | continuous, $(0,\rho\mu(m_{\max})]$ | Aggregate task rate entering the top-UAV queue |
| Number of virtual machines | $m$ | integer, $1\leq m\leq m_{\max}$ | Parallel MEC instances on the top UAV |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| 37/38b | Compression must offset queueing and processing delay, $\eta<1-B_2\log(1+\theta_2)(L_q/\lambda+1/\mu)/l$ |
| 38c | Computation load satisfies $\rho=\lambda/(m\mu)>\xi$ |
| 38d | The arrival rate and VM count obey $0<\lambda\leq\rho\mu(m_{\max})$ and $1\leq m\leq m_{\max}$ |
| Queue stability | The M/M/$m$ service load remains below one, $\rho<1$ |

**Algorithm**: Build the three-dimensional PPP, derive single-link and grouped-link successful-transmission probabilities, and map UAV density to packet arrival rate; compute communication and M/M/$m$ queueing delays; traverse feasible VM counts and arrival rates; return the density and VM configuration that minimizes response delay while satisfying the MEC-benefit and load constraints.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Zhang et al. [x] studied response delay optimization in a mobile-edge-computing-enabled UAV swarm for disaster rescue. They modeled bottom-UAV locations with a three-dimensional Poisson point process, derived successful-transmission probabilities for single and grouped links, and represented the top-UAV computation system as an M/M/$m$ queue with virtual-machine multiplexing degradation. Their joint communication and computation problem minimizes response delay over waiting, transmission, queueing, and processing components by configuring UAV density and the number of virtual machines. The resulting algorithm computes link success probabilities, evaluates the delay components, and searches feasible communication and computation configurations. Simulations report a 10% to 20% response-delay reduction relative to UAVs without MEC capability. A 5G NR mmWave and DJI UAV testbed further reports an 89.9% reduction in video packets forwarded from the top UAV to the control center after MEC processing.

## Problem framing

UAVs must relay urgent information (fire, survivors) to a control center under tight communication and computation constraints; the bottleneck is the capacity-limited wireless backhaul from the swarm to the control center. Prior work treated 2-D networks, single UAVs, or local optimization, and rarely combined MEC with the joint communication+computation optimization needed to bound response delay for a 3-D-distributed UAV swarm.

## System model

- **Two hops.** B-UAV → T-UAV (first hop, 28 GHz mmWave, SDMA via phased arrays) and T-UAV → control center (second hop, backhaul). B-UAVs are small rotary-wing (comms only, no MEC); the fixed-wing T-UAV carries the MEC server.
- **Spatial model.** B-UAVs follow a 3-D PPP with intensity λ_u in a bounded volume between altitudes H₁ and H₂; directional pencil beams; inter-group side-lobe interference modeled, intra-group main-lobe interference neglected. See [[stochastic-geometry-network-analysis]].
- **Compute model.** Parallel computing via VMs on the T-UAV; VM-multiplexing degradation factor d inflates expected service time as T_m = T₁(1+d)^(m−1). See [[queueing-theory]].

## Method

- Derive successful transmission probability P(γ > θ) for single and grouped links from the 3-D PPP + directional-antenna model.
- Formulate response delay via four delay indicators (communication + computation) using queueing theory and obtain closed-form optimal response delay; the optimization algorithm picks UAV distribution density and VM count at a target delay threshold under communication+computation constraints.

## Key findings

- Versus conventional UAVs without MEC, the proposed algorithm yields a **10%–20% decrease in response delay** in the disaster-rescue scenario (stated verbatim).
- On the **hardware testbed** (two DJI M100 quad-rotors + 5G NR mmWave, 28 GHz, 8×100 MHz carriers, 64-element phased arrays), running SURF-based video-stream target detection on the T-UAV reduced the total packets transmitted from T-UAV to control center by **89.9%** versus no-MEC (verbatim); a 52 s / 7.84 Mbit video stream was reduced to nine key frames totaling 775.9 kbit.
- Measured per-frame computation delay grows roughly linearly with frame index (e.g. ~94 ms at frame 167 up to ~946 ms at frame 1325 — read from Fig. 15(b), indicative).

## Limitations / future work

The parse's conclusion does not enumerate explicit future-work targets → `not in parse`. Transmission/computation-delay magnitudes beyond the verbatim 10–20% and 89.9% figures are read from testbed plots (indicative).

## Relation to the corpus

A **hardware-validated** (real DJI UAVs + 5G NR mmWave testbed) UAV-swarm MEC entry, joining the small set of non-simulation-only sources ([[sun-2024-asap-uav-swarm]], [[shao-2024-drl-antijamming-mec]], [[qu-ecoei-uav-swarm]]). Its analytical backbone — [[stochastic-geometry-network-analysis]] + [[queueing-theory]] for response delay — is distinctive in the UAV-swarm track and contrasts with the DRL/game-theoretic swarm sources; it grounds the new [[queueing-theory]] concept. Shares senior co-author [[zhu-han|Zhu Han]] with the NUAA aerial/maritime cluster. Reinforces [[multi-uav-assisted-mec]] and the disaster-rescue framing of [[post-disaster-mec]].

## Raw artifacts

- `raw/sources/Response_Delay_Optimization_in_Mobile_Edge_Computing_Enabled_UAV_Swarm/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
