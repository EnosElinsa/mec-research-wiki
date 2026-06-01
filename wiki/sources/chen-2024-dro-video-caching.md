---
type: source
title: "Adaptive Bitrate Video Caching in UAV-Assisted MEC Networks Based on Distributionally Robust Optimization"
authors: ["Yali Chen", "Min Liu", "Bo Ai", "Yuwei Wang", "Sheng Sun"]
year: 2024
url: "https://doi.org/10.1109/TMC.2023.3304624"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, mobile-edge-computing, multi-uav-assisted-mec, service-caching-mec, distributionally-robust-optimization, video-transcoding-tradeoff, energy-latency-tradeoff]
related:
  - "[[distributionally-robust-optimization]]"
  - "[[service-caching-mec]]"
  - "[[computational-task-caching]]"
  - "[[video-transcoding-tradeoff]]"
  - "[[video-analytics-offloading]]"
  - "[[air-to-ground-channel-model]]"
  - "[[energy-latency-tradeoff]]"
  - "[[jia-2025-dro-uav-hap-mec]]"
  - "[[bao-2025-ddpg-video-offloading]]"
  - "[[gao-2024-service-experience-cache-uav]]"
  - "[[zhao-2024-caching-service-placement-uav]]"
  - "[[query-when-does-dro-beat-drl-for-csi-uncertainty]]"
created: 2026-06-02
updated: 2026-06-02
---

# Adaptive Bitrate Video Caching in UAV-Assisted MEC Networks Based on Distributionally Robust Optimization

## Citation

Chen, Y., Liu, M., Ai, B., Wang, Y., & Sun, S. (2024). *Adaptive Bitrate Video Caching in UAV-Assisted MEC Networks Based on Distributionally Robust Optimization*. **IEEE Transactions on Mobile Computing**. DOI: 10.1109/TMC.2023.3304624. (Manuscript received 11 November 2022; revised 7 July 2023; accepted 6 August 2023; date of publication 14 August 2023; date of current version 4 April 2024 → year 2024.)

## TL;DR

A **UAV-assisted MEC video-caching** scheme that is **robust to unknown content-popularity distributions**. A static-deployed UAV carries an MEC server that caches and **transcodes** adaptive-bitrate video, serving users directly (cache hit), via local higher-to-lower-bitrate transcoding (transcoding hit), or via backhaul retrieval from the ground BS (miss). Because user requests / popularity are time-varying and hard to predict, the authors formulate **joint cache placement and video-delivery scheduling under the worst-case distribution** as a **distributionally robust optimization (DRO)** problem that minimizes total expected system latency subject to an energy budget. They characterize uncertainty with **ζ-structure probability metrics** (five family members) to build a data-driven confidence set from historical data, then solve the resulting mixed-integer non-convex problem with a convex-optimization-based **distributionally robust latency optimization algorithm**. Evaluation uses a real-world YouTube video dataset.

## Problem framing

Video is the dominant share of mobile traffic, and adaptive-bitrate streaming serves different users at different bitrates. UAV-mounted MEC caches popular content during off-peak periods and transcodes higher-bitrate versions down on demand, reducing duplicate BS transmissions and content-acquisition latency while saving storage versus caching every bitrate separately. The hard part is that most prior caching work assumes a fixed Zipf popularity, which deviates from reality; ML predictors lack a quantifiable robustness guarantee. Robust optimization (worst-case over an uncertainty set) is overly conservative, whereas **DRO** uses statistical distribution information to form a confidence set — capturing distribution characteristics without excess conservatism — making it the chosen tool for risk-averse caching under uncertain popularity.

## System model

- **Topology.** A static UAV with an MEC server (storage + processing) acts as an aerial small BS over a hot-spot cellular network; UAV–user links use mm-wave, the BS–UAV backhaul uses the cellular band. Direct BS–user links are excluded as unsatisfactory.
- **Channel.** Log-normal shadowing with probabilistic LoS/NLoS path loss and an elevation-angle-dependent LoS probability ([[air-to-ground-channel-model]]); backhaul modeled with its own path-loss law.
- **Content library.** M videos × N ascending bitrate variants; file size = bitrate × playtime. Three delivery modes per request: direct hit, transcoding hit (video split into chunks, each obtained by local transcoding or backhaul), and miss (backhaul retrieval + forward).
- **Objective.** Minimize total expected system latency under the worst-case popularity distribution, with caching + transcoding + hovering energy constrained by a system energy budget.

## Method

- **Uncertainty set.** ζ-structure probability metrics (five members) characterize the gap between a reference distribution (from observed historical data) and the real distribution, forming a confidence set that also acts as a constraint to predict content popularity.
- **Formulation.** Joint cache placement (binary) + delivery scheduling (how much of each chunk comes from cache / transcoding / backhaul) → a mixed-integer non-convex problem under distributional uncertainty.
- **Algorithm.** A **distributionally robust latency optimization algorithm** built on convex optimization theory transforms the worst-case problem into a tractable form and returns a risk-averse solution.

## Key findings

- On a real-world YouTube dataset, the proposed DRO scheme is evaluated against a deterministic scheme and other feasible schemes on both efficiency (latency) and robustness, with the paper reporting performance gains across metrics under popularity-distribution disturbance (the headline numeric margins live in the parse's figures, so treat exact values as indicative).
- The DRO formulation provides a theoretically grounded robustness guarantee that the paper argues ML-based popularity predictors cannot, while avoiding the over-conservatism of classical robust optimization.

## Limitations / future work

The UAV is statically deployed — trajectory is not optimized — and transcoding is restricted to higher→lower bitrate only. Results are simulation-based (albeit on real video traces), and the model targets a single-UAV hot-spot scenario.

## Relation to the corpus

A **distributionally-robust** caching counterpart to the corpus's other DRO-for-CSI/demand-uncertainty work, most directly [[jia-2025-dro-uav-hap-mec]] (DRO for UAV-HAP MEC offloading) — both feed the open question [[query-when-does-dro-beat-drl-for-csi-uncertainty]]. On the application side it sits with the UAV video / caching thread: [[bao-2025-ddpg-video-offloading]] (DDPG video offloading), [[gao-2024-service-experience-cache-uav]] (fairness-aware cache-enabled UAV-MEC), and [[zhao-2024-caching-service-placement-uav]] (joint caching + service placement), and its transcode-vs-backhaul tradeoff grounds [[video-transcoding-tradeoff]] and [[computational-task-caching]].

## Raw artifacts

- `raw/sources/Adaptive_Bitrate_Video_Caching_in_UAV-Assisted_MEC_Networks_Based_on_Distributionally_Robust_Optimization/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
