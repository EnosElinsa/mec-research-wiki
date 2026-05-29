---
type: source
title: "Joint Deployment and Task Scheduling Optimization for Large-Scale Mobile Users in Multi-UAV-Enabled Mobile Edge Computing"
authors: ["Yong Wang", "Zhi-Yang Ru", "Kezhi Wang", "Pei-Qiu Huang"]
year: 2019
url: "https://doi.org/10.1109/TCYB.2019.2935466"
venue: "IEEE Transactions on Cybernetics (IEEE TCYB)"
tags: [source, multi-uav-assisted-mec, uav-deployment, task-scheduling, differential-evolution, two-layer-optimization, energy-minimization]
related:
  - "[[multi-uav-assisted-mec]]"
  - "[[weighted-kmeans-uav-deployment]]"
  - "[[two-stage-decomposition]]"
  - "[[differential-evolution]]"
  - "[[constrained-multi-objective-evolutionary-algorithm]]"
  - "[[peng-2022-cmop-uav-path-planning]]"
  - "[[wang-acve-constraint-violation-cmop]]"
created: 2026-05-29
updated: 2026-05-29
---

# Joint Deployment and Task Scheduling Optimization for Large-Scale Mobile Users in Multi-UAV-Enabled Mobile Edge Computing

## Citation

Wang, Y., Ru, Z.-Y., Wang, K., & Huang, P.-Q. (2019). *Joint Deployment and Task Scheduling Optimization for Large-Scale Mobile Users in Multi-UAV-Enabled Mobile Edge Computing*. **IEEE Transactions on Cybernetics**. DOI: 10.1109/TCYB.2019.2935466.

## TL;DR

A multi-UAV MEC system where UAVs act as flying edge clouds for large-scale mobile users. The authors jointly optimize **UAV deployment** (number + locations) and **task scheduling** (offloading decision + resource allocation per user) to minimize system energy, using a **two-layer optimization method (ToDeTaS)**: a differential-evolution algorithm with an elimination operator adaptively tunes the number/locations of UAVs in the upper layer, and a greedy algorithm solves the lower-layer 0-1 integer task-scheduling problem.

## Problem framing

To serve many users with UAV edge clouds, one must decide how many UAVs to deploy and where, plus whether each user offloads and how resources are allocated. A key derived property: the number of UAVs should be as small as possible subject to completing all tasks under delay constraints. Evolutionary algorithms face large-scale search space + mixed variables and usually ignore the deployment↔scheduling correlation.

## System model

- **Actors.** Multiple UAVs as flying edge clouds; large-scale mobile users.
- **Upper layer.** UAV deployment — each individual encodes a UAV location, the population an entire deployment; the number of UAVs equals the population size.
- **Lower layer.** Task scheduling as a 0-1 integer program (offloading decision + resource allocation) given the deployment.
- **Objective.** Minimize system energy consumption.

## Method

- **ToDeTaS** two-layer method:
  - **Upper:** [[differential-evolution]] with an **elimination operator** that gradually reduces UAV count until at least one task can't meet its delay constraint — an adaptive UAV-number adjustment.
  - **Lower:** an efficient **greedy algorithm** for the near-optimal 0-1 task-scheduling solution at much lower time cost.

## Key findings

- The two-layer method reduces decision-variable dimensionality versus the original joint problem and is shown effective for the established multi-UAV MEC system (qualitative; specific results in the paper).

## Limitations / future work

The parse emphasizes the large-scale + mixed-variable challenge; explicit future-work items are not enumerated in the extracted conclusion.

## Relation to the corpus

An **evolutionary-computation** anchor (differential evolution + two-layer decomposition) that predates and informs the CMOP-evolutionary UAV-MEC lineage ([[peng-2022-cmop-uav-path-planning]], [[wu-2026-terrain-aware-uav-mec]]) — note the shared "Yong Wang / Central South University" thread also behind the methods paper [[wang-acve-constraint-violation-cmop]]. Its two-layer (deployment/scheduling) split connects to [[two-stage-decomposition]] and the deployment concept [[weighted-kmeans-uav-deployment]].

## Raw artifacts

- `raw/sources/Joint_Deployment_and_Task_Scheduling_Optimization_for_Large-Scale_Mobile_Users_in_Multi-UAV-Enabled_Mobile_Edge_Computing/full.md`
- Original PDF and extracted figures in the same folder.
