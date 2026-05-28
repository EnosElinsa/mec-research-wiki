# Wiki Index

## Entities

- [[lihan-liu]] — first author, Beijing Wuzi University
- [[hongrui-miao]] — co-author, University of Tennessee Knoxville
- [[chunhui-qu]] — co-author, AIR / Chinese Academy of Sciences
- [[zhuwei-wang]] — co-author, Beijing University of Technology
- [[haijun-zhang]] — co-author, USTB, IEEE Fellow
- [[zhidu-li]] — co-author, CQUPT, IEEE Senior Member
- [[pytorch]] — DL framework used for the reference implementation

## Concepts

- [[mobile-edge-computing]] — pushing compute to the radio-access edge
- [[multi-uav-assisted-mec]] — UAVs as mobile MEC servers
- [[high-density-mobile-device-scenarios]] — the dense / mobile target regime
- [[gauss-markov-mobility-model]] — stochastic device-mobility model
- [[task-offloading]] — split compute between device and edge
- [[uav-trajectory-control]] — continuous-action component
- [[uav-charging-scheduling]] — discrete-action component
- [[ppo]] — Proximal Policy Optimization
- [[gae]] — Generalized Advantage Estimation
- [[pomdp]] — Partially Observable MDP framing
- [[hybrid-action-decision-making]] — joint continuous + discrete actions
- [[ntm]] — Neural Turing Machine background
- [[convlstm]] — recurrent convolutional baseline
- [[stn]] — Spatial Transformer Network front-end
- [[en-convntm]] — enhanced ConvNTM with 3-D memory + STN
- [[j-ppo]] — PPO with hybrid continuous/discrete actions
- [[j-ppo-en-convntm]] — the full framework
- [[equilibrium-efficiency-metric]] — Ω = ψ·f / κ
- [[spatial-equity-index]] — Jain-style fairness
- [[energy-expenditure-coefficient]] — energy-spent-vs-available

## Sources

- [[liu-2026-jppo-en-convntm]] — Liu, Miao, Qu, Wang, Zhang, Li (2026). Multi-UAV path planning for MEC with high-density mobile devices.

## Methodology

- [[drl-simulation-with-pomdp-formulation]] — POMDP simulation protocol used in [[liu-2026-jppo-en-convntm]]

## Findings

- [[en-convntm-beats-baselines]] — EN-ConvNTM > the four ablations on Ω
- [[neuralmap-loses-spatial-info]] — why NeuralMap fares worst
- [[uav-count-inverted-u-energy]] — fleet size has a finite optimum
- [[charging-stations-improve-efficiency]] — more stations always helps
- [[hybrid-action-beats-pure-drl]] — j-PPO+EN-ConvNTM beats DDPG/TD3/A2C/DQN
- [[finding-optimal-loss-entropy-weight-coefs]] — best c₁, c₂, c₃ values

## Thesis

- [[hybrid-action-memory-augmented-drl-wins-uav-mec]] — current working thesis (`supported`, medium confidence)

## Queries

- [[query-real-world-validation-of-jppo-en-convntm]] — sim-to-real?
- [[query-does-en-convntm-generalize-beyond-uav-mec]] — generalization?

## Comparisons

- [[ddpg-vs-jppo]] — continuous-only DRL vs hybrid-action DRL
- [[j-ppo-baselines]] — encoder ablation: EN-ConvNTM / ConvNTM / ConvLSTM / NeuralMap / raw

## Synthesis

- [[design-recipe-multi-uav-mec]] — 10-step recipe for DRL-controlled UAV-MEC
