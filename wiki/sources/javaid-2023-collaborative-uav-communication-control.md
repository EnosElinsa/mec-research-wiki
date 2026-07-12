---
type: source
title: "Communication and Control in Collaborative UAVs: Recent Advances and Future Trends"
authors: ["Shumaila Javaid", "Nasir Saeed", "Zakria Qadir", "Hamza Fahim", "Bin He", "Houbing Song", "Muhammad Bilal"]
year: 2023
url: "https://doi.org/10.1109/TITS.2023.3248841"
venue: "IEEE Transactions on Intelligent Transportation Systems (IEEE T-ITS)"
tags: [source, survey, collaborative-uav, uav-swarm, communication, control, autonomy]
related:
  - "[[collaborative-uav-communication]]"
  - "[[autonomous-uav-swarms]]"
  - "[[uav-to-x-communication]]"
  - "[[cellular-connected-uav]]"
  - "[[high-altitude-platform-station]]"
  - "[[space-air-ground-integrated-network]]"
  - "[[federated-learning]]"
  - "[[mobile-edge-computing]]"
  - "[[du-2025-autonomous-intelligent-uav-swarms]]"
created: 2026-07-12
updated: 2026-07-12
---

# Communication and Control in Collaborative UAVs: Recent Advances and Future Trends

## Citation

Javaid, S., Saeed, N., Qadir, Z., Fahim, H., He, B., Song, H., & Bilal, M. (2023). *Communication and Control in Collaborative UAVs: Recent Advances and Future Trends*. **IEEE Transactions on Intelligent Transportation Systems**, 24(6), 5719-5739. DOI: 10.1109/TITS.2023.3248841.

## TL;DR

Reviews collaborative multi-UAV systems through the joint requirements of communication, flight control, autonomy, sensing, computation, and resource sharing. It organizes UAV-to-infrastructure and UAV-to-UAV links, control functions, collaborative tasks, urban applications, use cases, and open research directions.

## Scope

Multi-UAV autonomy and reliability are limited by intermittent connectivity, high mobility, channel uncertainty, finite communication range, constrained onboard resources, and reliance on centralized control. The review asks what communication and control capabilities let a swarm coordinate tasks as one system rather than as independent aircraft.

## Communication and control taxonomy

- Network paths include UAV-to-terrestrial, UAV-to-satellite, UAV-to-HAP, and direct UAV-to-UAV communication.
- Candidate UAV-to-UAV technologies include Wi-Fi, UHF, cellular, LoRaWAN, free-space optical, and satellite links.
- Control functions include takeoff and landing, trajectory tracking, localization, collision avoidance, formation, and resource management.
- Collaborative tasks span trajectory formation, localization, data collection, task offloading, sensing, and joint decision-making.
- Application domains include ITS, environmental monitoring, surveillance, edge resource management, disaster response, remote sensing, agriculture, and connectivity extension.

## Key synthesis

The paper treats [[collaborative-uav-communication]] as a cross-layer requirement: network connectivity, flight control, sensing, computation, and task allocation must be designed together. Its future directions emphasize trajectory and scheduling optimization, resource-aware [[federated-learning]], cellular integration, self-organization, collaborative offloading, and energy efficiency.

The review does not contribute an original experiment. Contextual values such as a 400 MHz UHF example, a 900 MHz LoRaWAN band, and cited disaster-routing results are secondary evidence from the reviewed literature rather than results of this paper.

## Limitations / parse caveats

This is a narrative review, not a systematic review with stated search and inclusion criteria or a quantitative meta-analysis. Several tables are flattened in the parse. The local parse states the publication dates and DOI; the full journal name, volume, pages, and DOI URL were verified against a title-matched Crossref record.

## Relation to the corpus

This source complements [[du-2025-autonomous-intelligent-uav-swarms]] by centering the coupling between communication and control, while the later survey emphasizes the broader autonomy and robotics stack. It also provides survey-level context for [[uav-to-x-communication]], [[cellular-connected-uav]], [[space-air-ground-integrated-network]], and the communication assumptions imported by UAV-MEC papers.

## Raw artifacts

- Parse: `raw/sources/Communication_and_Control_in_Collaborative_UAVs_Recent_Advances_and_Future_Trends/Communication_and_Control_in_Collaborative_UAVs_Recent_Advances_and_Future_Trends.md`
- Origin PDF: `raw/sources/Communication_and_Control_in_Collaborative_UAVs_Recent_Advances_and_Future_Trends/Communication_and_Control_in_Collaborative_UAVs_Recent_Advances_and_Future_Trends.pdf`
- Figures: `raw/sources/Communication_and_Control_in_Collaborative_UAVs_Recent_Advances_and_Future_Trends/images/`
