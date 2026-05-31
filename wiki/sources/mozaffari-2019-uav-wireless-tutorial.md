---
type: source
title: "A Tutorial on UAVs for Wireless Networks: Applications, Challenges, and Open Problems"
authors: ["Mohammad Mozaffari", "Walid Saad", "Mehdi Bennis", "Young-Han Nam", "Mérouane Debbah"]
year: 2019
url: "https://doi.org/10.1109/COMST.2019.2902862"
venue: "IEEE Communications Surveys & Tutorials (IEEE COMST)"
tags: [source, uav, tutorial, survey, aerial-base-station, cellular-connected-uav, channel-modeling, 3d-deployment]
related:
  - "[[cellular-connected-uav]]"
  - "[[air-to-ground-channel-model]]"
  - "[[high-altitude-platform-station]]"
  - "[[stochastic-geometry-network-analysis]]"
  - "[[zeng-2019-uav-comm-tutorial-5g]]"
  - "[[al-hourani-2014-optimal-lap-altitude]]"
  - "[[zeng-2019-rotary-wing-energy-min]]"
  - "[[mozaffari-2017-uav-iot-energy-efficient]]"
  - "[[mohammad-mozaffari]]"
  - "[[walid-saad]]"
created: 2026-05-31
updated: 2026-06-01
---

# A Tutorial on UAVs for Wireless Networks: Applications, Challenges, and Open Problems

## Citation

Mozaffari, M., Saad, W., Bennis, M., Nam, Y.-H., & Debbah, M. (2019). *A Tutorial on UAVs for Wireless Networks: Applications, Challenges, and Open Problems*. **IEEE Communications Surveys & Tutorials**. DOI: 10.1109/COMST.2019.2902862.

## TL;DR

A comprehensive tutorial on using UAVs ("drones") in wireless communications, organized around two roles: UAVs as **aerial base stations** (to enhance coverage, capacity, reliability, and energy efficiency) and UAVs as **flying user equipment** ([[cellular-connected-uav|cellular-connected UAVs]]). It surveys the key UAV challenges — 3D deployment, performance analysis, channel modeling, and energy efficiency — and the analytical toolbox used to tackle them: optimization theory, machine learning, [[stochastic-geometry-network-analysis|stochastic geometry]], transport theory, and game theory.

## Problem framing

Conventional UAV research focused on navigation, control, and autonomy, treating communication as secondary. This tutorial re-centers the discussion on wireless communication and networking: how to analyze, optimize, and design UAV-based wireless systems. It distinguishes UAV types by altitude — **high-altitude platforms (HAPs)**, above ~17 km and quasi-stationary, versus **low-altitude platforms (LAPs)**, tens of meters to a few kilometers, fast-moving and flexible — and by airframe (fixed-wing vs rotary-wing), noting their differing endurance, mobility, and deployment trade-offs.

## System model

Not a single-system paper; it frames recurring UAV-communication settings:

- **Drone-BS scenario.** Design considerations include performance characterization, optimal 3D deployment, wireless/computational resource allocation, flight-time and trajectory optimization, and network planning.
- **Drone-UE (cellular-connected) scenario.** Challenges include handover management, channel modeling, low-latency control, 3D localization, and interference management.
- **Regulatory context.** Tabulates per-country maximum altitudes and stand-off distances (e.g. US 122 m, Australia 120 m), reflecting that regulation is a first-order deployment constraint.

## Method

A tutorial/survey rather than a single proposed algorithm. It catalogs analytical frameworks and shows how each maps to UAV problems — e.g. [[stochastic-geometry-network-analysis|stochastic geometry]] for coverage/interference analysis, optimization theory for 3D deployment and trajectory, machine learning for autonomous decision-making, transport theory for cell-association, and game theory for distributed UAV interactions — with representative results for each challenge area.

## Key findings

- UAV base stations can complement terrestrial cellular by adjusting altitude, avoiding obstacles, and raising the likelihood of **line-of-sight** links to ground users, providing on-demand capacity to hotspots and coverage to hard-to-reach areas.
- Altitude is a fundamental design lever: LAPs deploy rapidly and support data collection / time-sensitive use; HAPs offer long endurance and wide-area coverage at higher cost and slower deployment.
- Identifies open problems across deployment, channel modeling, energy efficiency, and the coexistence of aerial and ground users — positioned as a research agenda for UAV wireless networking.

## Limitations / future work

By design a tutorial; it consolidates open problems and research directions rather than reporting a measured system. It predates much of the UAV-MEC corpus and does not address computation offloading directly.

## Relation to the corpus

A **foundational survey/tutorial anchor** for the UAV side of the wiki, complementary to the 5G-and-beyond UAV-communications tutorial [[zeng-2019-uav-comm-tutorial-5g]]. The aerial-base-station, 3D-deployment, and channel-modeling threads it surveys are formalized in corpus anchors such as [[al-hourani-2014-optimal-lap-altitude]] (air-to-ground LoS probability and optimal LAP altitude) and [[zeng-2019-rotary-wing-energy-min]] (rotary-wing propulsion energy), and put to work by the same group's [[mozaffari-2017-uav-iot-energy-efficient]] (joint UAV 3D placement + mobility + uplink power control for IoT collection). The Virginia Tech (Wireless@VT) authors [[mohammad-mozaffari]] and [[walid-saad]] anchor this UAV-communications thread. Reinforces [[cellular-connected-uav]], [[air-to-ground-channel-model]], [[high-altitude-platform-station]], and [[stochastic-geometry-network-analysis]].

## Raw artifacts

- `raw/sources/A_Tutorial_on_UAVs_for_Wireless_Networks_Applications_Challenges_and_Open_Problems/full.md`
- Original PDF and extracted figures in the same folder.
