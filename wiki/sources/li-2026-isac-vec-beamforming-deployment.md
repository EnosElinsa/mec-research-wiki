---
type: source
title: "Joint Beamforming and UAV Deployment Optimization for ISAC-Enhanced UAV-Assisted VEC"
authors: ["Chunlin Li", "Wenhao Wu", "Zhihao Zhang", "Tianbing Ma", "Shaohua Wan"]
year: 2026
url: "https://doi.org/10.1109/TWC.2026.3694912"
venue: "IEEE Transactions on Wireless Communications (IEEE TWC)"
tags: [source, vehicular-mec, isac, uav-assisted-vec, beamforming, uav-deployment, sparrow-search-algorithm]
related:
  - "[[vehicular-mec]]"
  - "[[integrated-sensing-and-communication]]"
  - "[[sparrow-search-algorithm]]"
  - "[[alternating-optimization-sdr-sca]]"
  - "[[cramer-rao-bound]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[li-2025-energy-latency-uav-vec]]"
created: 2026-07-07
updated: 2026-07-07
---

# Joint Beamforming and UAV Deployment Optimization for ISAC-Enhanced UAV-Assisted VEC

## Citation

Li, C., Wu, W., Zhang, Z., Ma, T., & Wan, S. (2026). *Joint Beamforming and UAV Deployment Optimization for ISAC-Enhanced UAV-Assisted VEC*. **IEEE Transactions on Wireless Communications**. DOI: 10.1109/TWC.2026.3694912.

## TL;DR

Uses UAVs as flexible ISAC support for urban vehicular edge computing when fixed RSUs cannot cover temporary congestion or hot spots. The paper jointly optimizes UAV deployment positions and beamforming to maximize communication capacity under energy and sensing constraints. It decomposes the problem into UAV deployment and beamforming blocks, using a refraction-based-learning sparrow search algorithm for deployment and an SCA / first-order-Taylor convexification loop for beamforming.

## Problem framing

Urban VEC hotspots are spatially uneven and time-varying. Fixed RSUs can be overloaded or poorly placed, while UAVs can reposition to improve coverage and sensing. The difficulty is the communication-sensing-energy tradeoff: stronger coverage and radar information may require unfavorable UAV locations, beam powers, or flight energy.

## System model

- A two-layer in-vehicle terminal / edge architecture lets vehicles upload complex tasks to edge computing stations, with UAVs supporting coverage and sensing.
- The TDD frame separates downlink, flexible, and uplink parts; sensing and communication are both active in downlink, while uplink carries communication.
- Communication capacity and Cramer-Rao-bound-style sensing metrics enter an ISAC sensing-communication effectiveness function.
- The main case considers spatially separated crossing roads and neglects inter-UAV co-channel interference; the parse also reports a denser multi-UAV interference scenario.

## Method

- Formulate a joint optimization problem over UAV deployment and beamforming with communication capacity, sensing performance, and UAV energy constraints.
- Apply block-coordinate decomposition: optimize deployment and beamforming as separate subproblems.
- Use an improved [[sparrow-search-algorithm]] with refraction-based learning for UAV deployment.
- Use SCA and first-order Taylor expansion to convexify the beamforming subproblem, aligning it with the broader [[alternating-optimization-sdr-sca]] family.

## Key findings

- The proposed algorithm converges faster and more smoothly than the tested benchmark functions in the parse.
- In the 30-vehicle case, reported coverage is 9.6%, 20.1%, and 4.4% higher than DDPG, PSO, and TPaPBA baselines, respectively.
- Across UAV-scale settings from 3 to 5 UAVs, the paper reports an average 10.51% coverage improvement over baselines and a 19.83% reduction in UAV energy consumption.
- Ablations show that fixed-sequence optimization reduces communication capability and radar mutual information; omitting sensing can slightly improve communication but loses the ISAC balance; fixing the sensing/communication split degrades communication and cost.

## Limitations / future work

The evaluation is simulation-based, including Veins-style traffic modeling. The main scenario simplifies interference by placing UAVs over spatially separated roads; the denser interference case is reported separately. Future work named in the parse is collaborative optimization among UAVs and vehicles.

## Relation to the corpus

This VEC entry makes [[integrated-sensing-and-communication]] central to UAV-assisted vehicular edge deployment. It complements [[li-2025-energy-latency-uav-vec]], which used UAV-assisted VEC for FL participant selection and resource allocation, by focusing instead on deployment plus beamforming for coverage/sensing. Methodologically it adds [[sparrow-search-algorithm]] to the swarm-metaheuristic family and pairs it with classical SCA beamforming.

## Raw artifacts

- `raw/sources/Joint Beamforming and UAV Deployment Optimization for ISAC-Enhanced UAV-Assisted VEC/Joint Beamforming and UAV Deployment Optimization for ISAC-Enhanced UAV-Assisted VEC.md`
- Original PDF and extracted figures (`images/`) in the same folder.
