---
type: source
title: "Convergence of MEC and DRL in Non-Terrestrial Wireless Networks: Key Innovations, Challenges, and Future Pathways"
authors: ["Syed Asad Ullah", "Syed Ali Hassan", "Hatem Abou-Zeid", "Hassaan Khaliq Qureshi", "Haejoon Jung", "Aamir Mahmood", "Mikael Gidlund", "Muhammad Ali Imran", "Ekram Hossain"]
year: 2026
url: "https://doi.org/10.1109/COMST.2025.3576571"
venue: "IEEE Communications Surveys & Tutorials (IEEE COMST)"
tags:
  - source
  - survey
  - mobile-edge-computing
  - deep-reinforcement-learning
  - non-terrestrial-network
  - space-air-ground-integrated-network
  - computation-offloading
  - leo-satellite-edge-computing
related:
  - "[[mobile-edge-computing]]"
  - "[[non-terrestrial-network]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[leo-satellite-edge-computing]]"
  - "[[high-altitude-platform-station]]"
  - "[[task-offloading]]"
  - "[[binary-vs-partial-offloading]]"
  - "[[interdependent-tasks-dag]]"
  - "[[mahboob-2024-ai-ntn-survey]]"
  - "[[mao-2017-mec-survey-communication]]"
  - "[[mach-2017-mec-survey-architecture]]"
  - "[[drl-backbones-across-uav-mec-sources]]"
created: 2026-06-03
updated: 2026-06-03
---

# Convergence of MEC and DRL in Non-Terrestrial Wireless Networks: Key Innovations, Challenges, and Future Pathways

## Citation
Syed Asad Ullah, Syed Ali Hassan, Hatem Abou-Zeid, Hassaan Khaliq Qureshi, Haejoon Jung, Aamir Mahmood, Mikael Gidlund, Muhammad Ali Imran, Ekram Hossain, "Convergence of MEC and DRL in Non-Terrestrial Wireless Networks: Key Innovations, Challenges, and Future Pathways," *IEEE Communications Surveys & Tutorials*, 2026. DOI: 10.1109/COMST.2025.3576571. (Received 25 Sep 2024; revised through 24 May 2025; accepted 26 May 2025; date of publication 4 Jun 2025; date of current version 2 Jan 2026 → year 2026 per the date-of-current-version convention. Corresponding authors: Haejoon Jung; Syed Ali Hassan. NUST Islamabad + Kyung Hee University + University of Calgary + Mid Sweden University + University of Glasgow + University of Manitoba.)

## TL;DR
A survey of how **deep reinforcement learning (DRL)** is applied to **MEC-empowered non-terrestrial wireless networks (MeNT-WiNs)** — the integration of MEC with NTN platforms: autonomous aerial vehicles (AAVs), satellites (LEO/GEO), and high-altitude platforms (HAPs). It reviews DRL fundamentals, the MeNT-WiN architecture and computation-offloading models, then surveys DRL's role in optimizing satellite operations, AAV-swarm management, resource/spectrum/energy allocation, routing, and security, and closes with challenges (computational complexity, real-time adaptability, scalability) and future research directions.

## Problem framing
6G targets ultra-reliable, low-latency, ubiquitous connectivity, but terrestrial infrastructure leaves coverage gaps in remote, rural, and disaster-prone areas. MeNT-WiNs push MEC onto non-terrestrial platforms to bring computation/storage closer to users and cut backhaul congestion. These environments are highly dynamic and large-scale, where **traditional static optimization** (predefined rules, computationally expensive solvers) struggles to adapt to fluctuating demand, interference, and topology. The survey's thesis is that DRL — learning from experience and adapting in real time — is the transformative tool for resource management, decision-making, routing, and security across MeNT-WiNs.

## System model
As a survey, it organizes the field rather than proposing one system:
- **CC vs MEC vs MeNT-WiN:** contrasts cloud computing, MEC (the ETSI edge-of-RAN concept), and their integration with NTN; a CC-vs-MEC comparison table (server scale, proximity, backhaul use, ~10 ms vs >100 ms latency).
- **Computation-offloading models:** **binary offloading** (atomic tasks, the X(M;τ;N) data-size/deadline/workload notation) vs **partial offloading** (data-partition model; the **task-call graph** directed-acyclic-graph K(V;D) for dependency-aware sequential/parallel/general models) — see [[binary-vs-partial-offloading]] and [[interdependent-tasks-dag]].
- **MeNT-WiN architecture:** seamless integration of MEC with LEO/GEO satellites, HAPs, and AAVs for distributed, proximity-based computation; enabling global IoT, disaster recovery, precision agriculture, remote sensing.
- **DRL taxonomy:** an extensive abbreviations table spanning value-based (DQL, DDQN, dueling, D3QN), policy-gradient/actor-critic (A2C/A3C, DDPG, TD3, SAC, PPO/MAPPO, TRPO), multi-agent (MADRL, MADDPG, MAFRL), and federated/distributed variants.

## Method
Survey methodology: it reviews DRL fundamentals, maps DRL applications onto MeNT-WiN sub-problems (autonomous satellite operations such as orbit adjustment / collision avoidance / energy-efficient trajectory; AAV route planning and surveillance; spectrum and energy resource allocation; content delivery; cybersecurity/anomaly detection), and consolidates open challenges and future pathways. No new algorithm or experiments are contributed.

## Key findings
As a survey, its "findings" are organizing claims rather than measured results:
- DRL is positioned as a unifying tool across MeNT-WiN tasks — satellite autonomy, AAV-swarm management, resource/spectrum/energy allocation, routing, and security.
- Traditional optimization is cast as inadequate for the dynamics and scale of non-terrestrial environments, motivating learning-based adaptation.
- Key open challenges named: computational complexity, real-time adaptability, and scalability of DRL-driven MeNT-WiN systems.

## Limitations / future work
- A survey: it synthesizes and taxonomizes rather than validating any single design; specific quantitative claims belong to the cited primary works, not this paper.
- The paper itself frames future work around making DRL practical at non-terrestrial scale (complexity, real-time adaptation, scalability) and tighter MEC+DRL integration.

## Relation to the corpus
This is a survey anchor for the intersection of the corpus's two largest themes — **MEC/computation offloading** and **DRL backbones** — specialized to **non-terrestrial** platforms, complementing [[mahboob-2024-ai-ntn-survey]] (AI-per-NTN-challenge taxonomy) and the canonical MEC surveys [[mao-2017-mec-survey-communication]] and [[mach-2017-mec-survey-architecture]]. Its binary-vs-partial and task-call-graph offloading taxonomy aligns with [[binary-vs-partial-offloading]] and [[interdependent-tasks-dag]], and its DRL taxonomy is a natural reference point for the [[drl-backbones-across-uav-mec-sources]] synthesis. It spans the [[space-air-ground-integrated-network|SAGIN]] platforms (satellite, [[high-altitude-platform-station|HAP]], AAV) the corpus's satellite and aerial-MEC tracks study individually.

## Raw artifacts
- Parse: `raw/sources/Convergence_of_MEC_and_DRL_in_Non-Terrestrial_Wireless_Networks_Key_Innovations_Challenges_and_Future_Pathways/full.md`
- Origin PDF: `raw/sources/Convergence_of_MEC_and_DRL_in_Non-Terrestrial_Wireless_Networks_Key_Innovations_Challenges_and_Future_Pathways/fa7658de-0e7b-40ad-b509-17af655fda95_origin.pdf`
- Figures: `raw/sources/Convergence_of_MEC_and_DRL_in_Non-Terrestrial_Wireless_Networks_Key_Innovations_Challenges_and_Future_Pathways/images/`
