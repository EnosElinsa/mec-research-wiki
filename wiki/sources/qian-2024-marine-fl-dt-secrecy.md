---
type: source
title: "Secrecy-Driven Energy Minimization in Federated-Learning-Assisted Marine Digital Twin Networks"
authors: ["Li Ping Qian", "Mingqing Li", "Ping Ye", "Qian Wang", "Bin Lin", "Yuan Wu", "Xiaoniu Yang"]
year: 2024
url: "https://doi.org/10.1109/JIOT.2023.3305711"
venue: "IEEE Internet of Things Journal (IEEE IoT-J)"
tags: [source, federated-learning, digital-twin, maritime-mec, noma, physical-layer-security, energy-minimization, hap]
related:
  - "[[energy-harvesting-mec]]"
  - "[[blockchain-for-fl-aggregation]]"
  - "[[simultaneous-wireless-information-and-power-transfer]]"
  - "[[bin-lin]]"
  - "[[yuan-wu]]"
  - "[[li-2023-secure-marine-iot-jamming]]"
  - "[[lyu-2023-noma-marine-emergency-offloading]]"
created: 2026-06-04
updated: 2026-06-04
---

# Secrecy-Driven Energy Minimization in Federated-Learning-Assisted Marine Digital Twin Networks

## Citation

Qian, L. P., Li, M., Ye, P., Wang, Q., Lin, B., Wu, Y., & Yang, X. (2024). *Secrecy-Driven Energy Minimization in Federated-Learning-Assisted Marine Digital Twin Networks*. **IEEE Internet of Things Journal**, 11(2). DOI: 10.1109/JIOT.2023.3305711. (Received 5 July 2023; accepted 4 August 2023; published 16 August 2023; current version 24 January 2024.)

## TL;DR

Constructs a Marine Internet of Things (M-IoT) digital twin via **federated learning (FL)**: unmanned surface vehicles (USVs) train local models and upload them via **NOMA** to a high-altitude platform (HAP) for global aggregation. The HAP then broadcasts the aggregated model — vulnerable to eavesdropping. Uses **chaotic spread spectrum** to protect HAP broadcasts. Jointly minimizes total energy consumption (USV model upload + HAP broadcast) by optimizing global accuracy, local accuracy, HAP transmit power, and NOMA upload duration, subject to secrecy and latency constraints. A layered decomposition algorithm finds the optimal solution.

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

Dalian Maritime University cluster (Bin Lin ([[bin-lin]])) + University of Macau cluster (Yuan Wu ([[yuan-wu]])). Combines **digital twin** construction, **federated learning**, and **physical layer security** in the maritime setting — extending the maritime MEC corpus ([[li-2023-secure-marine-iot-jamming]], [[lyu-2023-noma-marine-emergency-offloading]]) with FL + digital-twin objectives. The FL energy-minimization + accuracy joint optimization mirrors [[yang-2024-taco-human-digital-twin-edge]] (non-maritime) and the digital twin pattern in [[mou-2025-adm-dt-migration]].

## Raw artifacts

- `raw/sources/Secrecy-Driven_Energy_Minimization_in_Federated-Learning-Assisted_Marine_Digital_Twin_Networks/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
