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
updated: 2026-11-03
---

# Secrecy-Driven Energy Minimization in Federated-Learning-Assisted Marine Digital Twin Networks

## Citation

Qian, L. P., Li, M., Ye, P., Wang, Q., Lin, B., Wu, Y., & Yang, X. (2024). *Secrecy-Driven Energy Minimization in Federated-Learning-Assisted Marine Digital Twin Networks*. **IEEE Internet of Things Journal**, 11(2). DOI: 10.1109/JIOT.2023.3305711. (Received 5 July 2023; accepted 4 August 2023; published 16 August 2023; current version 24 January 2024.)

## TL;DR

Constructs a Marine Internet of Things (M-IoT) digital twin via **federated learning (FL)**: unmanned surface vehicles (USVs) train local models and upload them via **NOMA** to a high-altitude platform (HAP) for global aggregation. The HAP then broadcasts the aggregated model — vulnerable to eavesdropping. Uses **chaotic spread spectrum** to protect HAP broadcasts. Jointly minimizes total energy consumption (USV model upload + HAP broadcast) by optimizing global accuracy, local accuracy, HAP transmit power, and NOMA upload duration, subject to secrecy and latency constraints. A layered decomposition algorithm finds the optimal solution.

## Modeling Quick-Use Card

> Reuse in a system model or problem formulation section: scenario, model, decisions, constraints, and algorithm.

**Scenario**: Unmanned surface vehicles train local models for a marine digital twin and simultaneously upload them by uplink NOMA to one high-altitude platform for global aggregation. The HAP broadcasts the aggregate through a chaotic spread-spectrum downlink in the presence of an eavesdropper, and both USVs and the HAP have limited communication/computation energy.

**Problem & objective**: Problem TEM, a non-convex layered energy-minimization problem, solves $\min E^{\mathrm{tot}} = N\big[\sum_{i}(E_i^{\mathrm L}+E_i^{U}) + E_S^{E} + E_S^{D}\big]$ over $\epsilon$, $\phi$, $p_S$, and $t^U$ over global accuracy, local accuracies, HAP broadcast power, and NOMA upload duration subject to learning, secrecy, and latency requirements.

**Decision variables**:

| Variable | Symbol | Type / range | Meaning |
|---|---|---|---|
| Global accuracy | $\epsilon$ | continuous, $[0,\epsilon^{\max}]$ | Accuracy target of the aggregated global model |
| Local accuracy | $\phi$ | continuous, $[0,\phi^{\max}]$ | Local training accuracy shared by the USVs |
| HAP transmit power | $p_S$ | continuous, power-bounded | Chaotic spread-spectrum broadcast power |
| NOMA upload duration | $t^U$ | continuous, nonnegative | Time used for simultaneous local-model uploads |

**Constraints**:

| ID | Meaning and key expression |
|---|---|
| (22)-(23) | Accuracy ranges, $0 \le \epsilon \le \epsilon^{\max}$ and $0 \le \phi \le \phi^{\max}$ |
| (25) | USV transmit powers, $p_i \le P_i^{\max}$ |
| (24) | HAP broadcast power, $0 \le p_S \le P_S^{\max}$ |
| (18) | The chaotic spread-spectrum broadcast meets the secrecy probability threshold $\phi_0$ |
| (21) | $N$ rounds of local training, upload, aggregation, and broadcast finish within $T$ |

**Algorithm**: Fix the global and local accuracies and solve TEM-Sub for the HAP power and NOMA upload duration, then substitute these solutions into the upper-level accuracy problem and solve it with the layered low-complexity procedure.

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

- `raw/sources/Secrecy-Driven_Energy_Minimization_in_Federated-Learning-Assisted_Marine_Digital_Twin_Networks/Secrecy-Driven_Energy_Minimization_in_Federated-Learning-Assisted_Marine_Digital_Twin_Networks.md`
- Original PDF and extracted figures (`images/`) in the same folder.
