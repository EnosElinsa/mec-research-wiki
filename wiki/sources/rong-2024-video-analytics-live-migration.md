---
type: source
title: "Live Migration of Video Analytics Applications in Edge Computing"
authors: ["Chenghao Rong", "Jessie Hui Wang", "Jilong Wang", "Yipeng Zhou", "Jun Zhang"]
year: 2024
url: "https://doi.org/10.1109/TMC.2023.3246539"
venue: "IEEE Transactions on Mobile Computing, 23(3)"
modeling_card: not_applicable
tags: [source, edge-computing, video-analytics, container-migration, state-migration, kubernetes]
related:
  - "[[service-migration]]"
  - "[[stateful-edge-microservice-migration]]"
  - "[[ma-2019-layered-container-migration]]"
  - "[[calagna-2024-robust-stateful-migration]]"
created: 2026-08-27
updated: 2026-08-27
---

# Live Migration of Video Analytics Applications in Edge Computing

## Citation

Rong, C., Wang, J. H., Wang, J., Zhou, Y., & Zhang, J. (2024). *Live Migration of Video Analytics Applications in Edge Computing*. **IEEE Transactions on Mobile Computing, 23**(3). DOI: 10.1109/TMC.2023.3246539.

## TL;DR

This prototype separates video-analytics memory into permanent, crucial, and ephemeral states, then migrates them by warm-up, synchronization, and replay. A Kubernetes implementation using a state store and sidecar reports application interruption below 405 ms for the tested workloads.

## Related Work Paragraph

> Ready to reuse in a literature review. Replace `[x]` with the formal citation number.

Rong et al. [x] measured why general checkpoint, Pre-copy, and Post-copy techniques perform poorly for edge video-analytics applications. They separated memory into permanent model and library state, crucial persistent application state, and ephemeral intermediate state. Their system warms permanent state at the destination, synchronizes crucial state through a store, and reconstructs ephemeral state by replaying input frames. A Kubernetes prototype with state-store and sidecar components reports interruption below 405 ms across the evaluated applications. The approach assumes a stable model within the migration window and requires developers to identify application-specific crucial state.

## Problem and system model

Video-analytics applications have large permanent model state, frequently modified tracking state, and volatile intermediate inference state. Treating every page identically creates excessive transfer, non-convergent dirty-page copying, or unpredictable post-copy stalls.

## Method

The destination warms unchanged libraries and model parameters before handoff. The application exposes crucial state through stateGET and statePUT operations backed by a distributed store, while the destination replays marked video frames to reconstruct ephemeral state. A sidecar mediates state and frame traffic with minimal application changes.

## Key findings

- The worst reported first-frame latency gap is 405 ms at 5 frames per second, with 159 ms and 284 ms reported at 2 and 3 frames per second.
- Migration finishes within 25 seconds in the evaluated cases, while synchronization and replay account for roughly 1% of that time.
- Performance degradation after migration lasts fewer than nine frames and less than two seconds in the tested workloads.

## Limitations / future work

The design assumes the video model remains unchanged during the relevant lifetime or window. Identifying crucial state can burden developers; the paper proposes static and dynamic analysis as future assistance.

## Relation to the corpus

This source adds application-semantic state classification to [[stateful-edge-microservice-migration]]. It complements [[ma-2019-layered-container-migration]], which removes redundant storage transfer, and [[calagna-2024-robust-stateful-migration]], which models container migration timing and connection continuity.

## Raw artifacts

- Parse: `raw/sources/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing/Live_Migration_of_Video_Analytics_Applications_in_Edge_Computing.md`
- Origin PDF and extracted figures are in the same folder.
