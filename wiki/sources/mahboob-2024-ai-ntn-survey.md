---
type: source
title: "Revolutionizing Future Connectivity: A Contemporary Survey on AI-Empowered Satellite-Based Non-Terrestrial Networks in 6G"
authors: ["Shadab Mahboob", "Lingjia Liu"]
year: 2024
url: "https://doi.org/10.1109/COMST.2023.3347145"
venue: "IEEE Communications Surveys & Tutorials (IEEE COMST)"
modeling_card: not_applicable
tags: [source, non-terrestrial-network, space-air-ground-integrated-network, leo-satellite-edge-computing, federated-learning, survey, 6g]
related:
  - "[[non-terrestrial-network]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[seamless-handover]]"
  - "[[federated-learning]]"
  - "[[decentralized-federated-learning]]"
  - "[[network-slicing]]"
  - "[[task-offloading]]"
  - "[[han-2024-sagin-fl-handover]]"
  - "[[lee-2024-dho-leo-handover]]"
  - "[[mao-2024-fso-leo-hierarchical-routing]]"
  - "[[cheng-2025-dos-satellite-edge-computing]]"
created: 2026-06-01
updated: 2026-07-16
---

# Revolutionizing Future Connectivity: A Contemporary Survey on AI-Empowered Satellite-Based Non-Terrestrial Networks in 6G

## Citation

Mahboob, S., & Liu, L. (2024). *Revolutionizing Future Connectivity: A Contemporary Survey on AI-Empowered Satellite-Based Non-Terrestrial Networks in 6G*. **IEEE Communications Surveys & Tutorials**. DOI: 10.1109/COMST.2023.3347145. (Manuscript received 9 June 2023; accepted 13 December 2023; date of publication 19 January 2024; date of current version 23 May 2024 → year 2024.)

## TL;DR

A survey arguing that **artificial intelligence (AI)** is a key enabler for **satellite-based non-terrestrial networks (NTN)** in 6G. It provides background on NTN platforms/architecture/characteristics and on AI/ML/DL techniques, then organizes existing work by **NTN research thrust** — mapping which AI approach fits which NTN challenge — and reviews industry/research efforts to implement AI-enabled NTN via software-defined (O-RAN / RIC, SDR) platforms, closing with practical challenges and recommendations.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Mahboob and Liu [x] surveyed artificial-intelligence methods for satellite-based non-terrestrial networks integrated with future 6G systems. They organized existing work around NTN challenges including channel and Doppler estimation, beam management, resource allocation, handover, spectrum sharing, routing, slicing, offloading, and security, and reviewed satellite testbeds and software-defined O-RAN integration efforts. Their synthesis recommends supervised learning for labeled prediction and estimation tasks, reinforcement learning for feedback-driven control, and distributed learning for scalable satellite-terrestrial operation. The survey identified limited onboard capability, time-varying topology, propagation delay, feedback overhead, security, and energy efficiency as coupled implementation challenges requiring low-complexity, secure, and online learning designs.

## Problem framing

6G targets extreme data rate (peak up to 1 Tbps), µs-order latency, and ubiquitous coverage that terrestrial-only networks cannot guarantee. NTN — space and aerial platforms, especially satellites at lower altitudes (~600 km LEO) — fills the coverage gap, but introduces unique challenges: long propagation delay, high Doppler shift, frequent handovers, spectrum-sharing complexity, and intricate beam/resource allocation; integrating NTN with terrestrial networks adds task offloading, network routing, and network slicing. The survey's thesis: AI can capture the intricate correlations among these dynamic parameters better than classical methods, and the **right learning paradigm depends on the problem** — supervised learning for prediction/estimation, reinforcement learning for closed-loop control.

## System model

Not an optimization paper — a survey. Its organizing structure:

- **NTN background.** Platform types (GEO ~35,786 km with ~270 ms delay, MEO, LEO ~600 km), 6G use cases (uMBB, mULC, etc.), general architecture, and fundamental characteristics (propagation delay/loss, moving base stations, large coverage).
- **AI background.** ML/DL taxonomy (supervised/unsupervised/reinforcement learning), offline vs online learning, and **distributed learning paradigms** — [[federated-learning]], decentralized learning, and split learning — as the synergy points between AI and NTN.
- **Research thrusts.** AI applied per NTN challenge: channel estimation, Doppler-shift estimation, beam-hopping/management, resource management, handover/mobility management, spectrum sharing, network routing, network slicing, computational offloading, and security (physical-layer authentication, intrusion detection, anti-jamming, traffic prediction).
- **Implementation.** AI/ML testbeds for satellite networks and adaptation of SDR-based OAI 4G/5G stacks (O-RAN, RIC) for NTN.

## Key findings

- Tailoring the learning approach to the problem is the survey's central recommendation: **supervised learning** suits prediction/estimation problems, **reinforcement learning** suits closed-loop control — leverage each technique's strengths rather than a one-size-fits-all model (conclusion, parse).
- Realizing AI-enabled NTN in 6G requires overcoming **cost-limited onboard satellite capabilities**, the **highly time-varying** network, and **long propagation delays** — and these are interconnected, so **joint** solutions are needed.
- **Low-complexity and distributed learning architectures** with efficient control-feedback are essential for real-time/online implementation; secure, compact, energy-efficient NTN platform design is integral.

## Limitations / future work

A survey: no original system/experiments. It frames practical complications (onboard constraints, time-variability, delay, security, energy) as **open future issues** rather than solving them, and provides insights/recommendations rather than quantitative results.

## Relation to the corpus

A **non-terrestrial-network / SAGIN** survey anchor ([[non-terrestrial-network]], [[space-air-ground-integrated-network]]) that organizes the AI-per-challenge landscape the corpus's NTN sources instantiate: FL across ground-to-satellite/SAGIN ([[han-2024-sagin-fl-handover]], using the same distributed-learning paradigms the survey catalogs), **handover** management ([[lee-2024-dho-leo-handover]]), **routing** ([[mao-2024-fso-leo-hierarchical-routing]]), and **computational offloading / satellite edge computing** ([[cheng-2025-dos-satellite-edge-computing]]). It is a high-level companion to the application-specific LEO/SAGIN sources, mapping which AI tool fits which NTN problem.

## Raw artifacts

- `raw/sources/Revolutionizing_Future_Connectivity_A_Contemporary_Survey_on_AI-Empowered_Satellite-Based_Non-Terrestrial_Networks_in_6G/full.md`
- Original PDF and extracted figures (`images/`) in the same folder.
