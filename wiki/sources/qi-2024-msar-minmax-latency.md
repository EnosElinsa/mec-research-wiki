---
type: source
title: "Minimizing Maximum Latency of Task Offloading for Multi-UAV-Assisted Maritime Search and Rescue"
authors: ["Shuang Qi", "Bin Lin", "Yiqin Deng", "Xianhao Chen", "Yuguang Fang"]
year: 2024
url: "https://doi.org/10.1109/TVT.2024.3384570"
venue: "IEEE Transactions on Vehicular Technology (IEEE TVT)"
tags: [source, maritime-mec, multi-uav-assisted-mec, task-offloading, min-max-latency, successive-convex-approximation, branch-and-bound, disaster-surveillance]
related:
  - "[[maritime-mec]]"
  - "[[multi-uav-assisted-mec]]"
  - "[[task-offloading]]"
  - "[[uav-trajectory-control]]"
  - "[[video-analytics-offloading]]"
  - "[[two-stage-decomposition]]"
  - "[[wang-2026-aerial-marine-msar]]"
  - "[[binary-vs-partial-offloading]]"
created: 2026-05-31
updated: 2026-05-31
---

# Minimizing Maximum Latency of Task Offloading for Multi-UAV-Assisted Maritime Search and Rescue

## Citation

Qi, S., Lin, B., Deng, Y., Chen, X., & Fang, Y. (2024). *Minimizing Maximum Latency of Task Offloading for Multi-UAV-Assisted Maritime Search and Rescue*. **IEEE Transactions on Vehicular Technology**. DOI: 10.1109/TVT.2024.3384570. (Manuscript received 5 December 2023; date of publication 3 April 2024; date of current version 19 September 2024 → year 2024.)

## TL;DR

A **Maritime Search and Rescue (MSAR)** system of multiple **Surveillance UAVs (S-UAVs)** plus one **Relay UAV (R-UAV)**: S-UAVs collect disaster-area video, pre-process it on onboard MEC, and relay it shoreward through the R-UAV. The paper minimizes the **maximum total latency among all S-UAVs** (so that per-UAV video delay is small and balanced) by jointly optimizing **computing-offloading decisions**, **R-UAV deployment**, and the **S-UAV–to–rescue-target association**, while keeping all targets monitored, under S-UAV/R-UAV energy constraints. The non-convex problem is split into three sub-problems solved iteratively.

## Problem framing

For MSAR, video-transmission delay must be both **low and balanced** across S-UAVs so the shore Rescue Coordination Center (RCC) can act quickly and jitter is mitigated. S-UAVs have limited payload/compute/energy; a larger-payload R-UAV is introduced as a relay with extra computational capability. The objective is explicitly a **min-max latency** (not a sum-latency), distinguishing it from sum-delay/energy offloading work.

## System model

- **Actors.** Multiple S-UAVs (camera + onboard MEC, limited payload) and a single R-UAV (relay + stronger compute).
- **Coupling.** S-UAV positions are adjusted via the S-UAV–target association to keep drowning targets centered and observed at close range (monitoring integrity).
- **Objective.** Minimize the maximum total latency among all S-UAVs subject to energy constraints of R-UAV and S-UAVs.
- **Decisions.** Offloading decisions, R-UAV deployment (position), and S-UAV–target association.

## Method

An **iterative optimization algorithm** decomposes the original non-convex problem into three tractable sub-problems (per the parse):

1. **Offloading optimization** — solved via **linearization**.
2. **R-UAV position optimization** — solved via **Successive Convex Approximation (SCA)**.
3. **Association optimization** (S-UAV ↔ targets) — solved via a **Branch and Bound (BnB)** algorithm.

The three are alternated to reach a near-optimal solution.

## Key findings

- Numerical simulations show the proposed algorithm is effective across various performance parameters (stated qualitatively in the parse; specific comparison curves are in the figures and not asserted here as exact magnitudes).

## Limitations / future work

The parse's conclusion (Section VII) confirms effectiveness but does not enumerate explicit quantitative future-work targets in the captured text → `not in parse`.

## Relation to the corpus

A **maritime MEC** entry that joins the corpus's 10-source maritime track. It is closely related to — but distinct from — [[wang-2026-aerial-marine-msar]] (also Bin Lin's group, also maritime *search and rescue*): that paper builds a three-tier UAV+HAPS+MASS architecture with matching + convex + PGD (JCORA), whereas this one is a **two-tier S-UAV/R-UAV video-surveillance** system minimizing **max latency** via linearization + SCA + BnB. Its min-max objective and discrete-then-continuous structure connect to [[two-stage-decomposition]], and its video pre-processing motivation links [[video-analytics-offloading]]. Shares first-author group lead [[bin-lin]] with the Dalian-Maritime maritime cluster.

## Raw artifacts

- `raw/sources/Minimizing_Maximum_Latency_of_Task_Offloading_for_Multi-UAV-Assisted_Maritime_Search_and_Rescue/full.md`
- Original PDF (`f97dc680-9b1d-4870-9526-c51a056a7c53_origin.pdf`) and extracted figures (`images/`) in the same folder.
