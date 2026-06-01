---
type: source
title: "Cost-Efficient Computation Offloading in SAGIN: A Deep Reinforcement Learning and Perception-Aided Approach"
tags:
  - source
  - sagin
  - computation-offloading
  - deep-reinforcement-learning
  - perception
  - uav-mec
  - leo-satellite
related:
  - "[[space-air-ground-integrated-network]]"
  - "[[task-offloading]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[ddpg]]"
  - "[[deep-q-network]]"
  - "[[lyapunov-optimization]]"
  - "[[self-adaptive-global-best-harmony-search]]"
  - "[[mmwave-radar-sensing]]"
  - "[[yolov7-object-detection]]"
  - "[[perception-aided-offloading]]"
  - "[[multi-source-data-fusion]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[xie-2026-uav-multisource-fusion]]"
  - "[[bao-2025-ddpg-video-offloading]]"
  - "[[lyapunov-guided-drl]]"
created: 2026-05-29
updated: 2026-06-02
authors:
  - Yulan Gao
  - Ziqiang Ye
  - Han Yu
year: 2024
url: https://doi.org/10.1109/JSAC.2024.3459073
venue: "IEEE Journal on Selected Areas in Communications (JSAC), vol. 42, no. 12, Dec. 2024"
---

# Cost-Efficient Computation Offloading in SAGIN: A Deep Reinforcement Learning and Perception-Aided Approach

## TL;DR
In a [[space-air-ground-integrated-network]] (SAGIN), UAVs act as a sensing-and-control layer: they carry mmWave radar and vision (YOLOv7) sensors to perceive ground-device distance, speed, direction, and type, then decide how to host and offload compute-intensive tasks to local UAV processors, ground base stations, or an LEO satellite. The authors minimize long-term time-averaged network cost under queue-stability constraints by combining [[lyapunov-optimization]] (drift-plus-penalty) with [[ddpg]] (offloading + UAV resources), a [[deep-q-network]] (UAV–BS association), and a [[self-adaptive-global-best-harmony-search]] metaheuristic (BS resource allocation). Feeding perception into the DRL state — [[perception-aided-offloading]] — is the central novelty and yields the lowest cost and most stable queues against all baselines.

## Problem
Remote areas typically lack 5G/B5G coverage, yet low-power devices there still need to run computation-intensive applications. SAGIN with [[mobile-edge-computing]] can bridge this gap, but prior work largely (a) optimizes only short-term performance and (b) assumes perfectly known air-to-ground channels and stationary devices. Real SAGIN deployments face random task arrivals, time-varying channels, and uncertain, mobile users — fast-moving devices in particular cause task-execution failures. This paper studies a scenario with many ground devices moving at different speeds between covered and uncovered areas, and seeks dynamic long-term strategies for four coupled decisions: task hosting (device→UAV), computation offloading, UAV–BS association control, and compute-resource allocation. The objective is to minimize time-averaged network cost while keeping all task queues stable, despite uncertainty in device location, speed, and type.

## System model
- **Three tiers.** Space: one LEO satellite cluster for always-on cloud compute (see [[leo-satellite-edge-computing]]). Air: `M` solar-powered UAVs serving as the central control layer and mobile edge nodes ([[multi-uav-assisted-mec]]); UAV trajectory is fixed/established and not optimized. Ground: `N` base stations and `K` mobile devices.
- **Mobility.** Devices follow a random-walk model (constant speed, periodic random direction changes); UAV coverage of devices fluctuates over time, and a device about to leave coverage is offloaded directly to the satellite.
- **Time structure.** Discrete slots of duration τ; each slot has Phase 1 (duration Δ: perception + task-hosting decision) and Phase 2 (offloading refinement).
- **Channels.** UAV–BS over C-band (4 GHz) with Rayleigh fading + shadowing + path loss; UAV–satellite over Ka-band with Rician LoS/NLoS; Shannon-capacity rates for all links.
- **Perception.** mmWave FMCW radar derives distance (IF beat frequency), velocity (Doppler phase), and angle (cross-antenna phase difference); YOLOv7 classifies device/object type and behavior. The fused stream is [[multi-source-data-fusion]] for [[integrated-sensing-and-communication]]-style decision support — see [[mmwave-radar-sensing]] and [[yolov7-object-detection]].
- **Tasks & offloading.** Partial offloading at the UAV layer ([[binary-vs-partial-offloading]]); four routes — local UAV, UAV→BS, UAV→satellite, and device→satellite (direct, when unhosted).
- **Energy/cost.** UAV local compute uses κ·f³ dynamic frequency scaling; transmission energy = power × data / rate; satellite compute-usage cost ∝ data × cycles/bit. Per-UAV operational cost aggregates collection, local, BS, satellite, and direct-offload terms.
- **Queues.** UAV compute queue and BS compute queue are modeled with backlog dynamics; the satellite is assumed to process instantly with no queue; buffers are assumed sufficient.

## Method
- **Formulation.** Minimize long-term time-averaged operational cost (Eq. 35) under compute-capacity, single-UAV/single-BS association, and queue-stability constraints — a time-coupled stochastic MINLP.
- **Lyapunov decoupling.** A quadratic Lyapunov function on queue backlogs gives a drift-plus-penalty objective `F(H(t)) = ΔL(H(t)) + V·E{cost}` with balancing parameter `V`; Theorem 1 provides an upper bound that decouples the multi-slot problem into per-slot problems. See [[lyapunov-optimization]].
- **Three subproblems per slot.**
  - **P1 — offloading `Q(t)` + UAV compute `f^u(t)`:** solved with [[ddpg]] (continuous actions). State includes UAV-BS/UAV-sat rates, hosted task volume, and the radar/vision device-type recognition `CT(t)`; reward = −P1 objective. This is where [[perception-aided-offloading]] enters the loop.
  - **P2 — UAV–BS association `y_{m,n}(t)` (0/1 MINLP):** solved with a [[deep-q-network]]; reward = −Eq.(44).
  - **P3 — BS compute allocation `f^{bs}(t)`:** solved with [[self-adaptive-global-best-harmony-search]] (Algorithm 1), with adaptive bandwidth and normally-distributed HMCR/PAR.
- **Orchestration (Algorithm 2).** Each slot: perceive distance/velocity/angle → release leaving devices to satellite → collect tasks → iterate DDPG → DQN → SGHS until no further improvement.

## Key findings
- **Setup:** 1 LEO satellite (780 km), 5 UAVs (100 m, circular path radius 1000 m, 16.67 m/s), 2 BSs, 10 users; 4 GHz / 400 MHz; N0 = −174 dBm/Hz; Rician factor 7; antenna gain 43.3 dBi; task size 10 MB; UAV f_max = 3×10⁸ Hz, satellite 10×10⁹ Hz, BS 5×10⁹ Hz.
- **P1 optimality:** DDPG converges quickly to the CVX-toolbox optimum (~30 cost units), versus Complete Offloading ~225 and Perception Free ~50.
- **Overall convergence (Fig. 3):** proposed ~37 (matches CVX) vs Complete Offloading ~120, Random ~75, Perception Free ~50–60.
- **Dynamic time-averaged cost (Fig. 4):** proposed ~30 vs Simulated Annealing ~40, Random ~50, Perception Free ~51, Complete Offloading ~79 — lowest and most stable.
- **Stability:** UAV/BS queue backlogs stabilize at low levels; Random and Complete Offloading fluctuate more because they ignore limited UAV compute and association control.
- **Scaling:** cost rises with datasize and UAV/BS CPU frequency, but the proposed method stays lowest and the gap widens as CPU frequency grows.
- **Perception value:** the Perception-Free baseline is consistently second-worst in dynamic settings, quantifying the benefit of fused mmWave + vision sensing.
- **Behavior modeling:** 60 user-action types are drawn from the AVA dataset (437 movies; e.g. run/jog, swim, dance, kick, hug, fight). SGHS converges robustly across HMCR/PAR settings (HMCR=0.9 fastest).

## Limitations
Evaluation is numerical-simulation-only — no hardware or field trial. UAV trajectory is fixed (explicitly out of scope), so [[uav-trajectory-control]] benefits are not captured. Mobility is a simplified random-walk model. The LEO satellite is assumed to process instantly with zero queueing delay, and UAV/BS buffers are assumed always sufficient. Perception is assumed effective; YOLOv7/radar recognition and estimation errors are not modeled as a degrading factor. Instances are small (5 UAVs, 2 BSs, 10 users, single satellite), and the three subproblems are solved sequentially rather than fully jointly.

## Relation to the corpus
This paper sits at the intersection of SAGIN offloading and onboard perception. It shares the SAGIN/UAV-MEC backbone with [[nabi-2025-jour-hierarchical-aerial]] and [[jia-2025-dro-uav-hap-mec]], and like [[xie-2026-uav-multisource-fusion]] it relies on [[multi-source-data-fusion]] from UAV sensors to drive decisions — though here the fusion (mmWave + YOLOv7) is single-platform onboard perception rather than multi-agent [[cooperative-perception]]. Its sensing-aided angle connects to [[integrated-sensing-and-communication]] surveys such as [[jiang-2025-isac-lae-overview]]. Methodologically it is a DRL-plus-Lyapunov pipeline: it reuses [[ddpg]] for continuous offloading control (cf. [[bao-2025-ddpg-video-offloading]]), a [[deep-q-network]] for discrete association (cf. the DQN-family approach in [[ma-2025-pdqn-vehicular-mec]]), and [[lyapunov-optimization]] for long-term stability. The new vocabulary it contributes — [[perception-aided-offloading]], [[mmwave-radar-sensing]], [[yolov7-object-detection]], and [[self-adaptive-global-best-harmony-search]] — extends the corpus toward perception-driven, metaheuristic-augmented [[task-offloading]] in [[space-air-ground-integrated-network]] settings.

## Raw artifacts
- `raw/sources/Cost-Efficient_Computation_Offloading_in_SAGIN_A_Deep_Reinforcement_Learning_and_Perception-Aided_Approach/full.md`
