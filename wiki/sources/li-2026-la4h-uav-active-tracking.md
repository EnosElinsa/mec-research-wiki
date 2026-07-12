---
type: source
title: "A Novel Expert-Assisted Anomaly-Aware Embodied Learning Framework for UAV Active Target Tracking"
authors: ["Jiahao Li", "Fuhui Zhou", "Qihui Wu"]
year: 2026
url: "https://doi.org/10.1109/TMC.2026.3666656"
venue: "IEEE Transactions on Mobile Computing (IEEE TMC)"
tags: [source, uav, active-target-tracking, embodied-ai, anomaly-detection, expert-assistance, knowledge-distillation, pomdp]
related:
  - "[[expert-assisted-anomaly-aware-tracking]]"
  - "[[expert-guided-warm-start-rl]]"
  - "[[knowledge-distillation-for-drl]]"
  - "[[pomdp]]"
  - "[[uav-enabled-its]]"
  - "[[attention-based-uav-target-search]]"
  - "[[zhu-2026-hab-mappo-target-search]]"
  - "[[zhu-2024-zdrl-uav-tracking]]"
  - "[[fuhui-zhou]]"
created: 2026-07-10
updated: 2026-07-13
---

# A Novel Expert-Assisted Anomaly-Aware Embodied Learning Framework for UAV Active Target Tracking

## Citation

Li, J., Zhou, F., & Wu, Q. (2026). *A Novel Expert-Assisted Anomaly-Aware Embodied Learning Framework for UAV Active Target Tracking*. **IEEE Transactions on Mobile Computing (IEEE TMC)**, 25(7), 11063-11083. DOI: 10.1109/TMC.2026.3666656.

## TL;DR

Introduces LA4H, a "learning to ask for help" framework for UAV active target tracking under prolonged occlusion and intense distractor interference. The UAV policy uses cross-modal anomaly cognition to detect abnormal tracking states, decides whether to request expert assistance, and distills a heavier teacher tracker into a deployable student policy.

## Problem

Active UAV tracking is hard when the target disappears behind obstacles or when distractors create multiple plausible visual peaks. The paper argues that passive trackers cannot proactively recover targets after occlusion, while fully autonomous active trackers can take irrational actions in partial-observation and out-of-distribution visual states.

The design goal is not to replace autonomy with manual control. LA4H tries to learn when expert help is worth its cost, so the UAV can recover from anomalous states while reducing unnecessary expert intervention.

## System model

- The active tracking task is formulated as a POMDP with normal, prolonged-occlusion, and intense-interference states.
- The state includes current and historical visual observations, UAV position state, and a semantic similarity map.
- The UAV uses an onboard optoelectronic pod plus localization inputs such as IMU/GPS.
- The action space contains 12 discrete 3-D movement and yaw/rotation actions.
- Anomalies are recognized through tracking confidence, temporal consistency, anomaly probability, semantic-map degradation, multiple high-confidence peaks, peak proximity, and cross-modal scores.

## Method

LA4H combines three pieces:

- **Cross-modal anomaly cognition**, which aligns temporal visual features with text prompts for occlusion and interference states.
- **An assistance decision policy**, which decides whether to continue autonomous tracking or request expert help.
- **Teacher-student policy learning**, where a heavier teacher policy supports temporal-semantic distillation into a lighter student tracker.

The expert can be a human or an algorithmic expert with privileged simulator state. The parsed paper describes algorithmic help using Gazebo ground truth, `A*`/`RRT*`-style global path planning for occlusion recovery, and ground-truth bounding boxes plus identity verification for distractor confusion.

## Key findings

- The parse reports headline gains of 361.4% success-rate increase, 54.4% task-completion-efficiency improvement, and 40.3% expert-intervention reduction.
- In training, LA4H reaches normalized reward near 40 after about 56K episodes and a success rate close to 95%.
- With 9 distractors, LA4H reports SR 88.9%, RPL 4.7, and SRPL 0.19 in one test, and the generalization table reports SR 84.8%, RPL 5.1, and SRPL 0.166.
- At 70% occlusion, LA4H reports SR 84.1%, RPL 5.2, and SRPL 0.16 in one test, and the generalization table reports SR 80.3%, RPL 5.9, and SRPL 0.136.
- The ablation table at 7 distractors and 50% occlusion reports full LA4H at SR 85.3%, RPL 4.5, SRPL 0.190, and EP 48.2%.
- On the Prometheus600 / Jetson Xavier NX setup, the full LA4H model is reported at 9.1M parameters, 2.94G FLOPs, 30.6 ms inference time, 32.7 FPS, 10.2 W, and 312.1 mJ per frame.

## Limitations / future work

The local parse is silent on DOI, venue, and year; the bibliographic metadata above is title-matched DOI metadata, while the technical claims are grounded in the parse. Some parsed table rows are malformed, especially helper-method rows, and the parse does not provide code availability or a released dataset. The real-world section gives occlusion/interference examples and onboard-efficiency results, but the parse does not establish a large-scale field deployment study.

## Relation to the corpus

LA4H is an adjacent UAV-sensing source rather than an MEC offloading paper. It complements [[zhu-2026-hab-mappo-target-search]], which couples target search with offloaded image processing, and [[zhu-2024-zdrl-uav-tracking]], which handles multi-UAV target localization through TDOA and Z-function-decomposition RL. Methodologically, [[expert-assisted-anomaly-aware-tracking]] extends the corpus's expert-guided theme beyond warm-start demonstrations: expert help becomes an online recovery action, and [[knowledge-distillation-for-drl]] makes the assisted tracker more deployable.

## Raw artifacts

- Parse: `raw/sources/A_Novel_Expert-Assisted_Anomaly-Aware_Embodied_Learning_Framework_for_UAV_Active_Target_Tracking/A_Novel_Expert-Assisted_Anomaly-Aware_Embodied_Learning_Framework_for_UAV_Active_Target_Tracking.md`
- Origin PDF: `raw/sources/A_Novel_Expert-Assisted_Anomaly-Aware_Embodied_Learning_Framework_for_UAV_Active_Target_Tracking/A_Novel_Expert-Assisted_Anomaly-Aware_Embodied_Learning_Framework_for_UAV_Active_Target_Tracking.pdf`
- Figures: `raw/sources/A_Novel_Expert-Assisted_Anomaly-Aware_Embodied_Learning_Framework_for_UAV_Active_Target_Tracking/images/`
