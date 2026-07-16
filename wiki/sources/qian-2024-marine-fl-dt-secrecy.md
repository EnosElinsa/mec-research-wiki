---
type: source
modeling_card: required
title: "Secrecy-Driven Energy Minimization in Federated-Learning-Assisted Marine Digital Twin Networks"
authors: ["Li Ping Qian", "Mingqing Li", "Ping Ye", "Qian Wang", "Bin Lin", "Yuan Wu", "Xiaoniu Yang"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2023.3305711"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, federated-learning, digital-twin, maritime-mec, noma, physical-layer-security, energy-minimization, hap]
related: ["[[energy-harvesting-mec]]", "[[blockchain-for-fl-aggregation]]", "[[simultaneous-wireless-information-and-power-transfer]]", "[[qian-wang]]", "[[liping-qian]]", "[[bin-lin]]", "[[yuan-wu]]", "[[wang-2026-noma-marine-data-computation]]", "[[li-2023-secure-marine-iot-jamming]]", "[[lyu-2023-noma-marine-emergency-offloading]]"]
created: 2026-06-04
updated: 2026-07-16
---

# Secrecy-Driven Energy Minimization in Federated-Learning-Assisted Marine Digital Twin Networks

## Citation

Qian, L. P., Li, M., Ye, P., Wang, Q., Lin, B., Wu, Y., & Yang, X. (2024). *Secrecy-Driven Energy Minimization in Federated-Learning-Assisted Marine Digital Twin Networks*. **IEEE Internet of Things Journal**, 11(2). DOI: 10.1109/JIOT.2023.3305711. (Received 5 July 2023; accepted 4 August 2023; published 16 August 2023; current version 24 January 2024.)

## TL;DR

Constructs a Marine Internet of Things (M-IoT) digital twin via **federated learning (FL)**: unmanned surface vehicles (USVs) train local models and upload them via **NOMA** to a high-altitude platform (HAP) for global aggregation. The HAP then broadcasts the aggregated model — vulnerable to eavesdropping. Uses **chaotic spread spectrum** to protect HAP broadcasts. Jointly minimizes total energy consumption (USV model upload + HAP broadcast) by optimizing global accuracy, local accuracy, HAP transmit power, and NOMA upload duration, subject to secrecy and latency constraints. A layered decomposition algorithm finds the optimal solution.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Unmanned surface vehicles train local models for a marine digital twin and simultaneously upload them by uplink NOMA to one high-altitude platform for global aggregation. The HAP broadcasts the aggregate through a chaotic spread-spectrum downlink in the presence of an eavesdropper, and both USVs and the HAP have limited communication/computation energy.

**Problem & objective**: Problem TEM, a non-convex layered energy-minimization problem, solves $\min_{\Theta,\boldsymbol\phi,p_S,t^U}E^{\mathrm{tot}}$ over global accuracy, local accuracies, HAP broadcast power, and NOMA upload duration subject to learning, secrecy, and latency requirements.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Global accuracy target | $\Theta$ | continuous feasible accuracy | Required accuracy of the aggregated digital-twin model |
| Local accuracy | $\phi_i$ | continuous feasible accuracy | Training accuracy selected for USV $i$ |
| HAP transmit power | $p_S$ | continuous, power-bounded | Chaotic spread-spectrum broadcast power |
| NOMA upload duration | $t^U$ | continuous, nonnegative | Time used for simultaneous local-model uploads |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| C1 | Global and local accuracies remain in their feasible ranges and meet the target model quality |
| C2 | NOMA upload rates deliver all local model parameters within $t^U$ |
| C3 | HAP broadcast power remains within its transmit-power budget |
| C4 | The chaotic spread-spectrum downlink satisfies the required secrecy probability |
| C5 | Local training, upload, aggregation, and broadcast complete within the latency bound |

**Algorithm**: Fix the global and local accuracy variables → derive closed-form lower-bound solutions for HAP power and NOMA duration from monotonicity → substitute them into the upper problem → transform the remaining accuracy problem into a one-to-one logarithmic domain → solve the unique optimum with the proposed layered low-complexity procedure.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Qian et al. [x] studied secrecy-driven energy minimization for a federated-learning-assisted marine digital-twin network. Unmanned surface vehicles upload local models to a high-altitude platform through NOMA, and the HAP protects its global-model broadcast with chaotic spread spectrum. They formulated a non-convex problem that minimizes USV and HAP energy by jointly optimizing global accuracy, local accuracy, HAP transmit power, and NOMA upload duration under secrecy and latency constraints. Their layered algorithm first derives unique power and duration solutions for fixed accuracies and then solves the transformed upper-level accuracy problem. Numerical results report lower energy than the evaluated fixed-accuracy, non-spread-spectrum, and TDMA schemes.

## Problem framing

M-IoT devices (USVs, maritime sensors) operate in areas with limited energy supply. Building an M-IoT digital twin via centralized data collection is infeasible (privacy, bandwidth). FL distributes training to USVs, but multiple rounds of HAP model broadcasts are exposed to eavesdroppers. Chaotic spread spectrum (wide-band, noise-like spectrum) protects broadcasts without imposing complex encryption overhead. The joint optimization of FL accuracy and energy efficiency across the HAP-USV-eavesdropper system is the key challenge.

## System model

- **Architecture:** HAP (aggregator + broadcaster) + I USVs (local FL trainers) + 1 eavesdropper. USVs upload local models to HAP via NOMA; HAP broadcasts aggregated model with chaotic spread spectrum protection.
- **FL model:** global accuracy depends on number of rounds + local convergence; local accuracy per USV is a function of local computation.
- **NOMA upload:** all USVs share the same uplink channel; SIC decoding at HAP.
- **Secrecy:** chaotic spreading at HAP increases eavesdropper detection difficulty; security probability quantifies QoS.
- **Objective:** minimize total energy (USV + HAP) subject to (i) target global FL accuracy, (ii) per-USV local accuracy, (iii) secrecy probability, (iv) latency.
- **Layered decomposition:** top-level problem solves for global + local accuracy; subproblem (given accuracy) solves for HAP power + NOMA duration. Optimal solutions to both levels proven unique.

## Key findings

- Proposed algorithm outperforms benchmarks: fixed-accuracy scheme (no accuracy optimization), non-spread-spectrum scheme, and TDMA transmission scheme in terms of energy efficiency (parse abstract + Section VI).
- NOMA achieves higher energy efficiency than TDMA for USV model uploads due to simultaneous channel access (parse comparison + Section VI).
- Layered decomposition yields a low-complexity algorithm with unique optimal solutions at both levels (parse Sections IV–V).
- Chaotic spread spectrum enables secrecy provisioning without sacrificing energy efficiency significantly (parse Section VI).

## Limitations / future work

Single HAP topology (no multi-hop or satellite backhaul). Eavesdropper CSI assumed known to the system for secrecy analysis. The parse does not detail robustness to estimation errors.

## Relation to the corpus

Combines **digital twin** construction, **federated learning**, and **physical layer security** in the maritime setting through the recurring Zhejiang/Dalian/University-of-Macau collaboration of [[qian-wang]], [[liping-qian]], [[bin-lin]], and [[yuan-wu]]. It extends the maritime MEC corpus ([[li-2023-secure-marine-iot-jamming]], [[lyu-2023-noma-marine-emergency-offloading]]) with FL and digital-twin objectives; [[wang-2026-noma-marine-data-computation]] uses the same author cluster for NOMA sensing-data collection followed by UAV computation. The FL energy-minimization and accuracy optimization also mirrors [[yang-2024-taco-human-digital-twin-edge]] and the digital-twin pattern in [[mou-2025-adm-dt-migration]].

## Raw artifacts

- `raw/sources/Secrecy-Driven_Energy_Minimization_in_Federated-Learning-Assisted_Marine_Digital_Twin_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
