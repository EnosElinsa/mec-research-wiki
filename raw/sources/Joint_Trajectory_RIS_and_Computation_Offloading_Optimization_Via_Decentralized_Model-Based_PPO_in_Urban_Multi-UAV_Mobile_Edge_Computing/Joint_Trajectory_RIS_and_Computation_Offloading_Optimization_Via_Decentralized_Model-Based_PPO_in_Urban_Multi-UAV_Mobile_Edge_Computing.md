# Joint Trajectory, RIS, and Computation Offloading Optimization via Decentralized Model-Based PPO in Urban Multi-UAV Mobile Edge Computing

Liangshun Wu Member, IEEE, Jianbo Du Senior Member, IEEE, and Junsuo Qu\* Member, IEEE

Abstract—Computation offloading in urban multi-UAV MEC networks is challenging because building blockage frequently disrupts line-of-sight links and user demand changes rapidly. RIS can create controllable reflected paths, but effective deployment requires jointly optimizing UAV trajectories, offloading schedules, and RIS phase shifts under limited inter-UAV information exchange. To address this problem, we propose a decentralized model-based MARL framework in which each UAV makes mobility and offloading decisions from local and k-hop observations and submits an RIS phase proposal to a lightweight RIS controller. To improve sample efficiency and training stability, each agent learns a local dynamics model and uses shorthorizon branched rollouts in PPO updates. Simulations show that the proposed method approaches centralized performance while improving throughput and energy efficiency in large-scale urban scenarios.

Index Terms—Reconfigurable Intelligent Surfaces, Uncrewed Aerial Vehicles, Mobile Edge Computing, Multi-Agent Reinforcement Learning

## I. INTRODUCTION

NABLING low-latency and energy-efficient computation wireless networks. Mobile edge computing (MEC) migrates computationally intensive tasks from devices to nearby edge servers, yet dense urban deployments often suffer line of sight (LoS) blockages and unreliable links due to buildings and obstacles. Integrating uncrewed aerial vehicles (UAVs) with reconfigurable intelligent surfaces (RIS) has been shown to effectively mitigate these challenges by exploiting UAV mobility and programmable reflections to create virtual LoS paths, extend base station (BS) coverage, and improve energy efficiency and offloading reliability [1]–[7]. With the shift toward mmWave or THz bands, where coverage shrinks and signals are highly susceptible to blockage, UAV-RIS architectures have emerged as a flexible, cost aware means to fill coverage holes and support latency sensitive MEC [1], [3], [8]–[13]. Recent works focus on optimizing energy efficiency, latency, and quality of experience (QoE) in UAV RIS assisted MEC systems [7], [9]–[20].

Traditional convex optimization and model predictive control (MPC) methods rely on accurate mathematical models [28] and convex assumptions, while heuristic algorithms (e.g. genetic algorithm) depend on handcrafted rules, making them unsuitable for highly dynamic and partially observable RIS-UAV-MEC environments. In contrast, multi-agent reinforcement learning (MARL) learns adaptive and scalable control policies directly from interactions, effectively handling nonlinear coupled dynamics, partial observability, and decentralized decision-making [9]–[11], [14]. However, since MARL algorithms rely on neural network approximations, the training process involves non-convex optimization, where convergence can be difficult to achieve or even diverge [29]. As system scale and complexity grow, it poses challenges on existing MARL methods: Firstly, partial observability. Most MARL methods (e.g. MADDPG) follow centralized training and decentralized execution (CTDE), relying on a global critic to stabilize training but requiring costly information exchange; fully decentralized alternatives avoid this overhead yet often suffer from higher variance and weaker coordination [30]. Secondly, low sample efficiency. The reliance of model-free MARL on costly interactions impedes its practical deployment in large-scale RIS-UAV-MEC systems [7], [31].

Existing studies address these challenges through approaches that reduce communication costs and incorporate learned models. Under communication constraints, agents often share information only with neighboring peers. For instance, I3CNet [24] uses an aggregation function to combine local messages. In addition, truncated policy gradient and Q learning variants can update policies locally, thereby lowering communication overhead [22]–[24], [32]. Nevertheless, many existing methods rely on simplified linear assumptions [33] or i.i.d. assumptions [34], which limits their ability to represent nonlinear dynamics. Sample efficiency can be improved by model based MARL, which increases data utilization by learning environment dynamics or opponent models [25]– [27], with particular relevance to aerial and terrestrial UAV networks [35]–[37]. Diffusion based generative solvers have also been explored for MEC optimization [38], [39], yet they typically require centralized critics, lack rigorous theoretical guarantees on model error bounds and convergence, and do not fully couple model learning with policy optimization [40]. Other techniques, such as prioritized replay, remain largely restricted to tabular settings and are difficult to extend to continuous control tasks.

TABLE I: Representative MARL methods under partial observability and sample-efficiency constraints.
<table><tr><td rowspan=1 colspan=1>Feature / Method</td><td rowspan=1 colspan=1>Comm.-EfficientMARL [21]-[23]</td><td rowspan=1 colspan=1>Neighbor Comm. [24]</td><td rowspan=1 colspan=1>Model-BasedMARL [25]-[27]</td><td rowspan=1 colspan=1>Proposed MB-DRL (Ours)</td></tr><tr><td rowspan=1 colspan=1>Partial        observabilityhandling</td><td rowspan=1 colspan=1>√(local info only)</td><td rowspan=1 colspan=1>√(neighbor aggregationbut fail to capture com-plex, coupled dynamics)</td><td rowspan=1 colspan=1>△(centralized critic)</td><td rowspan=1 colspan=1>√√(decentralized κ-hop)</td></tr><tr><td rowspan=1 colspan=1>Communication cost</td><td rowspan=1 colspan=1>√(compressed  trun-cated updates)</td><td rowspan=1 colspan=1>√(limited to neighbors)</td><td rowspan=1 colspan=1>X(global exchange)</td><td rowspan=1 colspan=1>√√(local κ-hop only)</td></tr><tr><td rowspan=1 colspan=1>Dynamics modeling</td><td rowspan=1 colspan=1>X(model-free)</td><td rowspan=1 colspan=1>X(model-free)</td><td rowspan=1 colspan=1>√(learned transition)</td><td rowspan=1 colspan=1>√√(localized     predictivemodel)</td></tr><tr><td rowspan=1 colspan=1>Sample efficiency</td><td rowspan=1 colspan=1>x</td><td rowspan=1 colspan=1>x</td><td rowspan=1 colspan=1> $\checkmark$ </td><td rowspan=1 colspan=1>√√(branched rollouts)</td></tr><tr><td rowspan=1 colspan=1>Convergence guarantee</td><td rowspan=1 colspan=1>x</td><td rowspan=1 colspan=1> $\pmb { \chi }$ </td><td rowspan=1 colspan=1>△(weak    theoreticalbounds)</td><td rowspan=1 colspan=1>√(bounded model error)</td></tr><tr><td rowspan=1 colspan=1>Scalability to large UAV nets</td><td rowspan=1 colspan=1>△(requires sync)</td><td rowspan=1 colspan=1>√(distributed)</td><td rowspan=1 colspan=1>X(centralized critic)</td><td rowspan=1 colspan=1>√√(fully decentralized)</td></tr></table>

Note: <sup>✓✓</sup>= significant advantage; <sup>✓</sup>= available; △= limited; <sup>✗</sup>= not supported.

We propose a model-based decentralized RL framework (MB-DRL). This setting involves high dimensional continuous control and noisy learning signals under partial observability, where unconstrained policy updates can be unstable. We therefore employ proximal policy optimization (PPO) to limit policy changes via a clipped surrogate objective and support parallel per-agent training. Our contributions are:

1) To handle partial observability and communication constraints, each UAV acts as an autonomous agent that makes decisions using only local observations and limited κ-hop neighbor information, enabling scalable cooperation without centralized coordination. To overcome the linear approximation limitation [33], our method employs a nonlinear representation that jointly encodes local states, neighbor policies, and hidden features through deep LSTM-based fusion. Unlike baselines (e.g., I3CNet [24]) that process only local or mean-field information, our design integrates multi-source contextual cues via concatenated nonlinear transformations of neighborhood states. This enables each agent to capture complex, coupled dynamics across UAVs, RIS, and MEC nodes.

2) To address the reliance on centralized critics and the lack of theoretical guarantees [40], our framework adopts a fully decentralized PPO structure in which each agent performs local policy and value updates using neighbors states. We integrate model learning directly with policy optimization, where locally learned dynamics guide shorthorizon rollouts that refine policy gradients and stabilize learning. Furthermore, we provide a bounded error convergence analysis that explicitly accounts for both model uncertainty and policy uncertainty. Unlike tabular prioritized replay, our method adopts a continuous, experience based sampling scheme that is compatible with neural function approximation, thereby improving sample reuse and training stability.

As summarized in Table I, our proposed MB-DRL framework achieves full decentralization and higher sample efficiency compared with existing methods.

The remainder of this paper is organized as follows: Section II presents the system model and problem formulation of the UAV- and RIS-assisted MEC system. Section III details the proposed decentralized, model-based MARL algorithm, including local dynamics learning, branched rollouts, and decentralized PPO optimization. Section IV discusses experimental settings and performance evaluation. Finally, Section V concludes the paper and outlines future research directions.

Main notations used in context are summarized in Table II.

## II. SYSTEM MODEL

## A. Scenario Setup

To address the relay transmission problem in MEC with UAVs and RIS, we consider a system where multiple UAVs (each with $L \ \geqslant \ 2$ antennas) serve both as computational nodes and relays, offloading tasks from multiple singleantenna user equipments (UEs) to a ground-based access point (AP) equipped with an MEC server. A building-mounted RIS, structured as a URA with $M _ { y } \times M _ { z }$ elements, reflects UAV signals toward the AP, as illustrated in Fig. 1. Direct links from UEs to the RIS and AP are assumed to be blocked or highly attenuated due to obstructions and distance, making RIS-assisted reflection essential for improved service quality. The total transmission period T is divided into N uniform time slots $\delta _ { t } ,$ , with slot set $\mathcal { N } \left( \left| \mathcal { N } \right| = N \right)$

In 3D space, the position of UE k at time slot n is denoted by $( w _ { k } [ n ] , 0 )$ , where $w _ { k } [ n ] = ( x _ { k } [ n ] , y _ { k } )$ , and $x _ { k } [ n ] = x _ { k } [ 0 ] +$ $n ,$ representing the fact that each UE moves one unit along the x-direction per time slot. The AP is located at $( w _ { a } , 0 )$ with $w _ { a } = ( x _ { a } , y _ { a } )$ , the RIS at $( w _ { r } , z _ { r } )$ with $w _ { r } = ( x _ { r } , y _ { r } )$ and $z _ { r }$ as its height, and an interferer/jammer at $( w _ { j } , 0 )$ with $w _ { j } =$ $( x _ { j } , y _ { j } )$ . Only single-bounce RIS reflections are considered due to path loss, all channels are quasi-static flat fading, and full channel state information (CSI) is assumed available for system optimization.

![](images/a1adf6d7e85a5ae9a3797cfc10908e2246899352bb7ce00909e4ffc896d84ff0.jpg)  
Fig. 1: This work considers an RIS-assisted multi-UAV MEC system in which multi-antenna UAVs serve as both computing nodes and decode-and-forward relays for single-antenna UEs. UE tasks are offloaded over wireless links and either processed onboard or forwarded to a ground MEC server via direct and RIS reflected channels. Each UAV acts as an RL agent that jointly optimizes its trajectory, offloading decisions, and RIS phase recommendations, while a lightweight RIS controller aggregates these recommendations to enable coordinated beamforming. The objective is to maximize system energy efficiency under two practical constraints: limited observability and low sample efficiency.

Incorporating a jammer into the system model reflects practical scenarios where communication reliability must be maintained under intentional interference, e.g., illegal jammers near critical infrastructure in urban emergency networks, adversarial jamming in disaster relief or battlefield operations, and proactive interference defense in smart-city or cellular deployments. Explicitly modeling jamming allows us to evaluate robustness and provides a basis for designing anti-jamming strategies to ensure secure and reliable service.

## B. UAV Trajectory

Each UAV operates over a limited duration of $N \delta _ { t }$ seconds, which is divided into N discrete time slots indexed by $n = 1 , 2 , \ldots , N$ . Each slot spans $\delta _ { t }$ seconds—sufficiently short to approximate the UAVs as static within a single slot. $\mathrm { U A V } \ u \in \mathcal { U }$ travels from a known starting position $\mathbf { q } _ { u , 0 } =$ $[ x _ { u , 0 } , y _ { u , 0 } , z _ { u , 0 } ] ^ { T }$ to a designated final destination $\begin{array} { r l } { { \bf q } _ { u , F } } & { { } = } \end{array}$ $[ x _ { u , F } , y _ { u , F } , z _ { u , F } ] ^ { T }$ , with its position at any time slot n given by $\mathbf { q } _ { u } [ n ] = [ x _ { u , n } , y _ { u , n } , z _ { u , n } ] ^ { T } = ( w _ { u } [ n ] , z _ { u } [ n ] )$ with $w _ { u } [ n ] =$ $( x _ { u , n } , y _ { u , n } )$ . We define the velocity and acceleration of UAV u at time slot n as $\mathbf { V } _ { u } [ n ] \ = \ \mathsf { \bar { \Gamma } } [ V _ { u , x } [ n ] , V _ { u , y } [ n ] , V _ { u , z } [ n ] ] ^ { T }$ and $\mathbf { A } _ { u } [ n ] = [ A _ { u , x } [ n ] , A _ { u , y } [ n ] , A _ { u , z } [ n ] ] ^ { T }$ , respectively. The UAV’s movement is governed by the following set of kinematic constraints:

$$
\mathbf { q } _ { u } [ n + 1 ] = \mathbf { q } _ { u } [ n ] + \mathbf { V } _ { u } [ n ] \delta _ { t } + \frac { 1 } { 2 } \mathbf { A } _ { u } [ n ] \delta _ { t } ^ { 2 } , \quad \forall u \in \mathcal { U } , \forall n\tag{1}
$$

$$
\mathbf { q } _ { u } [ 0 ] = \mathbf { q } _ { u , 0 } , \quad \mathbf { q } _ { u } [ N ] = \mathbf { q } _ { u , F } , \quad \forall u \in \mathcal { U }\tag{2}
$$

$$
{ \bf V } _ { u } [ n + 1 ] = { \bf V } _ { u } [ n ] + { \bf A } _ { u } [ n ] \delta _ { t } , \quad \forall u \in \mathcal { U } , \forall n , n \leq N\tag{3}
$$

$$
\| \mathbf { q } _ { u } [ n ] - \mathbf { q } _ { u } [ n - 1 ] \| \leq \delta _ { t } V _ { \operatorname* { m a x } } , \quad \forall u \in \mathcal { U } , n = 2 , 3 , \ldots , N\tag{4}
$$

Here, $V _ { \mathrm { m a x } }$ represents the UAV’s top allowable speed. According to the above, each UAV’s future position is a function of its current state and motion dynamics. The initial and final positions are fixed at the first and last time slots, respectively. Velocity is incrementally updated based on acceleration, and each UAV’s displacement per slot must not exceed its maximum travel distance, ensuring feasible mobility.

## C. RIS Phase Control

The RIS is mounted on a building wall parallel to the xzplane and consists of $M = M _ { y } \times M _ { z }$ elements arranged in a URA. The reflection phase coefficient matrix of the RIS at time slot n is obtained by averaging the phase recommendations of all UAVs:

$$
\Theta [ n ] = \bar { \Theta } [ n ] = \frac { \sum _ { u = 1 } ^ { U } \Theta _ { u } [ n ] } { U } .\tag{5}
$$

Specifically,

$$
\Theta _ { u } [ n ] = \mathrm { d i a g } \left( e ^ { j \theta _ { u , 1 } [ n ] } , e ^ { j \theta _ { u , 2 } [ n ] } , \dots , e ^ { j \theta _ { u , M } [ n ] } \right) ,\tag{6}
$$

represents the phase parameter vector recommended by UAV u at time slot n through UAV-RIS link, where each $\theta _ { u , m } [ n ] \in$ [0, 2π) controls the phase of the m-th RIS element to enable intelligent beam steering.<sup>1</sup>

## D. Channel Modeling

1) UAV-RIS-AP Link: For UAV $u \in \mathcal { U }$ and the AP, the effective uplink channel incorporating both direct and RISassisted paths is modeled as:

$$
\bar { \mathbf { h } } _ { u a } [ n ] = \mathbf { h } _ { u a } ^ { H } [ n ] + \mathbf { h } _ { r a } ^ { H } [ n ] \Theta [ n ] \mathbf { h } _ { u r } [ n ] ,\tag{7}
$$

where $\mathbf { h } _ { u a } ^ { H } [ n ] \in \mathbb { C } ^ { 1 \times L }$ is the direct channel from UAV u to the AP, $\mathbf { h } _ { u r } [ n ] \in \mathbb { C } ^ { M \times L }$ is the LoS dominated channel from UAV u to the RIS, $\mathbf { h } _ { r a } ^ { H } [ n ] \in \mathbb { C } ^ { 1 \times M }$ is the LoS channel from RIS to the AP.

TABLE II: List of Main Symbols
<table><tr><td>Symbol</td><td>Description</td></tr><tr><td>U, K</td><td>Sets of UAVs and user equipments (UEs)</td></tr><tr><td> $u , k , n$ </td><td>UAV, UE, and time-slot indices</td></tr><tr><td> $N , \delta _ { t } , T$ </td><td>Number of time slots, slot duration, and total</td></tr><tr><td> ${ \mathbf q } _ { u } [ n ]$ </td><td>period 3D position of UAV u at slot n</td></tr><tr><td> $[ x _ { u , n } , y _ { u , n } , z _ { u , n } ] ^ { T }$ </td><td></td></tr><tr><td> ${ \mathbf V } _ { u } [ n ] , { \mathbf A } _ { u } [ n ]$ </td><td>Velocity and acceleration vectors of UAV u</td></tr><tr><td> $V _ { \mathrm { m a x } }$ </td><td>Maximum UAV speed</td></tr><tr><td> ${ \bf q } _ { u , 0 } , { \bf q } _ { u , F }$ </td><td>Initial and final positions of  $\mathrm { U A V } ~ u$ </td></tr><tr><td> $\Theta [ n ]$ </td><td>RIS phase-shift matrix at slot n</td></tr><tr><td> $\theta _ { m } [ n ]$   $M = M _ { y } \times M _ { z }$ </td><td>Reflection phase of the m-th RIS element</td></tr><tr><td> $\mathbf { h } _ { u r } [ n ] , \mathbf { h } _ { r a } [ n ] , \mathbf { h } _ { u a } [ n ]$ </td><td>Total number of RIS elements (URA configura- tion)</td></tr><tr><td> $\bar { \mathbf { h } } _ { u a } [ n ]$ </td><td>Channels of UAV-RIS, RIS-AP, and UAV-AP links</td></tr><tr><td> $\beta _ { 0 }$ </td><td>Effective UAV-RIS-AP channel</td></tr><tr><td> $\alpha _ { i } , K _ { i }$ </td><td>Reference path loss at 1 m Path-loss exponent and Rician K-factor of link</td></tr><tr><td></td><td>i</td></tr><tr><td> $d _ { i } [ n ]$   $B$ </td><td>Link distance at slot n</td></tr><tr><td> $p _ { t } , p _ { j }$ </td><td>System bandwidth</td></tr><tr><td> $\mathbf { w } _ { u , k } [ n ]$ </td><td>Transmit powers of UE and jammer</td></tr><tr><td> ${ \mathbf { u } } _ { u , k } [ n ]$ </td><td>Transmit beamforming vector for UAV u, UE k</td></tr><tr><td> $\gamma _ { u , k } [ n ] , \gamma _ { a , u , k } [ n ]$ </td><td>Receive beamforming vector for UAV u, UE k</td></tr><tr><td></td><td>SNR of UE-UAV and UAV–AP links</td></tr><tr><td> $\tau _ { u , k } ^ { o } [ n ] , \tau _ { u , k } ^ { R } [ n ]$ </td><td>Time allocations for offloading and relay phases</td></tr><tr><td> $l _ { u , k } ^ { o } [ n ]$ </td><td>Offloaded bits from UE k to UAV u</td></tr><tr><td> $l _ { a , u , k } ^ { R } [ n ]$ </td><td>Relayed bits from UAV u to AP</td></tr><tr><td> $l _ { u , k } ^ { \mathrm { l o c } } [ n ] , l _ { u , k } ^ { \mathrm { c o m p } } [ n ]$ </td><td>Bits computed locally (UE) and by UAV u</td></tr><tr><td> $L _ { k }$ </td><td>Total task size of UE k (bits to be processed)</td></tr><tr><td> $c _ { u } , c _ { a }$ </td><td>CPU cycles required per bit at UAV and AP</td></tr><tr><td> $F _ { u } ^ { \mathrm { m a x } } , F _ { a } ^ { \mathrm { m a x } }$ </td><td>Maximum CPU frequency of UAV and AP</td></tr><tr><td> $E _ { k } ^ { \mathrm { t x } } [ n ] , E _ { k } ^ { \mathrm { c o m p } } [ n ]$ </td><td>Transmission and computation energy of UE k</td></tr><tr><td> $E _ { u } ^ { \mathrm { c o m p } } [ n ] , E _ { u } ^ { \mathrm { f f y } } [ n ]$ </td><td>Computation and propulsion energy of UAV u</td></tr><tr><td> $\vartheta _ { 1 } , \vartheta _ { 2 }$ </td><td>Propulsion power coefficients (drag, hover loss)</td></tr><tr><td> $\mu _ { k } , \mu _ { u }$ </td><td>Effective switched-capacitance coefficients (DVFS model)</td></tr><tr><td> $E [ n ]$ </td><td>Total system energy consumption at slot n</td></tr><tr><td> $\pi ^ { \theta _ { u } } , V ^ { \phi _ { u } }$ </td><td>Policy and value networks of UAV u</td></tr><tr><td> $\hat { p } _ { u }$ </td><td>Learned local transition (dynamics) model</td></tr><tr><td> $\mathcal { D } _ { u } ^ { E } , \mathcal { D } _ { u } ^ { M }$ </td><td>Environment and model replay buffers</td></tr><tr><td> $\mathcal { N } _ { u } ^ { ( \kappa ) }$ </td><td>κ-hop neighbor set of UAV u</td></tr><tr><td> $r _ { u } [ n ]$ </td><td>Reward of UAV u at time slot n</td></tr><tr><td> $\beta$ </td><td>Weight controlling throughput-interference or</td></tr><tr><td> $_ T$ </td><td>entropy regularization Rollout horizon for model-based simulation</td></tr><tr><td>3</td><td>Upper bound of model error tolerance</td></tr><tr><td>z</td><td>Vector of all optimization variables</td></tr></table>

$\mathbf { h } _ { u r } [ n ]$ is modeled as:

$$
{ \bf h } _ { u r } [ n ] = \frac { \beta _ { 0 } } { \left\| { \bf q } _ { u } [ n ] - { \bf p } _ { r } \right\| } { \bf a } _ { r u } ^ { R } [ n ] { \bf a } _ { u } ^ { T } [ n ] ,\tag{8}
$$

where $\beta _ { 0 }$ is the reference path loss at 1 meter, $\begin{array} { r l } { \mathbf { p } _ { r } } & { { } = } \end{array}$ $[ x _ { r } , y _ { r } , z _ { r } ] ^ { T }$ is the position of the RIS, $\mathbf { a } _ { u } ^ { T } [ n ] \in \mathbb { C } ^ { L \times 1 }$ is the UAV’s transmit array response vector,

$$
\mathbf { a } _ { u } ^ { T } [ n ] = \left[ 1 , e ^ { - j { \frac { 2 \pi } { \lambda } } d \cos \theta _ { u r } [ n ] } , \dots , e ^ { - j { \frac { 2 \pi } { \lambda } } ( L - 1 ) d \cos \theta _ { u r } [ n ] } \right] ^ { T } ,\tag{9}
$$

where $\theta _ { u r } [ n ]$ is the angle of departure (AoD) from the UAV to the RIS in the elevation domain. $\mathbf { a } _ { r u } ^ { R } [ n ] \in \mathbb { C } ^ { 1 \times M }$ is the RIS receive array response vector.

$$
\begin{array} { r l } & { \mathbf { a } _ { r u } ^ { R } [ n ] = \mathbf { a } _ { r y } ^ { R } [ n ] \otimes \mathbf { a } _ { r z } ^ { R } [ n ] \in { \mathbb { C } } ^ { 1 \times M } , } \\ & { \mathbf { a } _ { r y } ^ { R } [ n ] = [ 1 , e ^ { - j \frac { 2 \pi } { \lambda } d _ { y } \sin { \theta _ { u r } [ n ] } \cos { \phi _ { u r } [ n ] } } , } \\ & { \phantom { \frac { \alpha _ { r y } ^ { R } [ n ] } { \alpha _ { r y } ^ { R } [ n ] } = } \cdot \cdot \cdot , e ^ { - j \frac { 2 \pi } { \lambda } ( M _ { y } - 1 ) d _ { y } \sin { \theta _ { u r } [ n ] } \cos { \phi _ { u r } [ n ] } } ] , } \\ & { \mathbf { a } _ { r z } ^ { R } [ n ] = [ 1 , e ^ { - j \frac { 2 \pi } { \lambda } d _ { z } \sin { \theta _ { u r } [ n ] } \sin { \phi _ { u r } [ n ] } } , } \\ & { \phantom { \frac { \alpha _ { r y } ^ { R } [ n ] } { \alpha _ { r y } ^ { R } [ n ] } = } \cdot \cdot \cdot , e ^ { - j \frac { 2 \pi } { \lambda } ( M _ { z } - 1 ) d _ { z } \sin { \theta _ { u r } [ n ] } \sin { \phi _ { u r } [ n ] } } ] . } \end{array}\tag{10}
$$

where $d _ { y }$ is the spacing between adjacent RIS elements along the $y \mathrm { - a x i s , }$ , and $( M _ { y } - 1 ) d _ { y }$ represents the maximum physical span of the RIS array in the y-direction. So do $d _ { x }$ and $( M _ { x } - 1 ) d _ { x }$ . The array response vector uses these spacings to model the phase shifts experienced by a plane wave arriving at different elements due to their spatial separation.

The spatial angles are defined as:

$$
\begin{array} { r l } & { \sin \theta _ { u r } [ n ] = \frac { z _ { r } - z _ { u } [ n ] } { \| \mathbf { q } _ { u } [ n ] - \mathbf { p } _ { r } \| } , } \\ & { \cos \phi _ { u r } [ n ] = \frac { y _ { r } - y _ { u } [ n ] } { \sqrt { ( x _ { r } - x _ { u } [ n ] ) ^ { 2 } + ( y _ { r } - y _ { u } [ n ] ) ^ { 2 } } } , } \\ & { \sin \phi _ { u r } [ n ] = \frac { x _ { r } - x _ { u } [ n ] } { \sqrt { ( x _ { r } - x _ { u } [ n ] ) ^ { 2 } + ( y _ { r } - y _ { u } [ n ] ) ^ { 2 } } } . } \end{array}\tag{11}
$$

Fig. 2 gives a schematic diagram of the geometric meaning of the UAV-RIS-AP link.

![](images/b8b9ac4b97a1cc01375b97bb87d7fb1f111c36223d66214a4c8db2f5f2662567.jpg)  
Fig. 2: Geometric meaning of angles. The phase shift $\theta _ { m } [ n ]$ applied by each RIS element is designed to align the reflected signal toward the AP, effectively corresponding to the angle of departure (AoD) from the RIS element to the AP. The angle $\theta _ { u r } [ n ]$ denotes the angle of departure (AoD) from the UAV to the RIS element, representing the elevation direction of the incoming wave. The azimuth angle $\phi _ { u r } [ n ]$ characterizes the angle of arrival (AoA) of the UAV’s signal at the RIS element projected onto the xy-plane.

2) UE-to-UAV, RIS-to-AP, and UAV-to-AP Links (Rician Fading): All other channels, including UE-to-UAV, RIS-to-AP,

and UAV-to-AP, are modeled using a Rician fading model:

$$
\begin{array} { l } { { \displaystyle { \bf h } _ { i } [ n ] = \sqrt { \beta _ { 0 } d _ { i } ^ { - \alpha _ { i } } [ n ] } \left( \sqrt { \frac { K _ { i } } { 1 + K _ { i } } } { \bf h } _ { i } ^ { \mathrm { L o S } } [ n ] + \sqrt { \frac { 1 } { 1 + K _ { i } } } { \bf h } _ { i } ^ { \mathrm { N L o S } } [ n ] \right) ^ { - } } } \\ { { \displaystyle i \in \{ ( u , k ) , ( r , a ) , ( u , a ) \} , } } \end{array}\tag{12}
$$

where $\beta _ { 0 }$ is the reference path loss at 1 meter, $K _ { i }$ is the Rician K-factor for link $i , \ \alpha _ { i }$ is the path-loss exponent for link $i , d _ { i } [ n ]$ is the Euclidean distance of link i at time slot n. $\mathbf { h } _ { i } ^ { \mathrm { L o S } } [ n ]$ is the deterministic line-of-sight component. For links involving antenna arrays (e.g., UAV or AP), this is modeled as an array response vector depending on the angle of arrival (AoA) or angle of departure (AoD): ${ \bf h } _ { i } ^ { \mathrm { L o S } } [ n ] \ = \ { \bf a } _ { i } ( \theta _ { i } [ n ] )$ where ${ \bf a } _ { i } ( \theta _ { i } [ n ] )$ is the corresponding array steering vector. $\mathbf { h } _ { i } ^ { \mathrm { N L o S } } [ n ]$ is the non-line-of-sight component, modeled as: $\mathbf { h } _ { i } ^ { \mathrm { \check { N } L o S } } [ n ] \sim \mathcal { C N } ( 0 , \mathbb { I } )$ , representing Rayleigh fading with i.i.d. complex Gaussian entries.

The corresponding link distances are:

$$
\begin{array} { r l r } & { } & { d _ { u k } [ n ] = \sqrt { \| w _ { u } [ n ] - w _ { k } [ n ] \| ^ { 2 } + z _ { u } [ n ] ^ { 2 } } , } \\ & { } & { d _ { u a } [ n ] = \sqrt { \| w _ { u } [ n ] - w _ { a } \| ^ { 2 } + z _ { u } [ n ] ^ { 2 } } , \quad \quad } \\ & { } & { d _ { r a } = \sqrt { \| w _ { r } - w _ { a } \| ^ { 2 } + z _ { r } ^ { 2 } } . \quad \quad } \end{array}\tag{13}
$$

3) JU and JR Links: We consider two interference links involving a ground-based jammer: the jammer-to-UAV (JU) and jammer-to-RIS (JR) links. These are modeled using Rician fading with elevation-angle-dependent K-factors to reflect the impact of spatial geometry.

JU Link is modeled as:

$$
\begin{array} { l } { { \displaystyle { \bf h } _ { j u } [ n ] = \sqrt { \beta _ { 0 } d _ { j u } ^ { - \alpha _ { j u } } [ n ] } } } \\ { { \displaystyle \left( \sqrt { \frac { K _ { j u } [ n ] } { 1 + K _ { j u } [ n ] } } { \bf h } _ { j u } ^ { \mathrm { L o S } } [ n ] + \sqrt { \frac { 1 } { 1 + K _ { j u } [ n ] } } { \bf h } _ { j u } ^ { \mathrm { N L o S } } [ n ] \right) } }  \end{array}\tag{14}
$$

where $d _ { j u } [ n ] = \sqrt { \| w _ { u } [ n ] - w _ { j } \| ^ { 2 } + z _ { u } [ n ] ^ { 2 } } , \ \alpha _ { j u }$ is the path loss exponent, $\mathbf { h } _ { j u } ^ { \mathrm { L o S } } [ n ]$ is the deterministic LoS component (e.g., phase shift), $\bar { \mathbf { h } } _ { i u } ^ { \mathrm { N L o S } } [ n ] \sim \mathcal { C N } ( 0 , 1 )$ is the Rayleigh fading NLoS component, $\check { K } _ { j u } [ n ]$ is an elevation-dependent Rician $K \mathfrak { - }$ factor.

The elevation-based Rician K-factor is defined as: $\begin{array} { r l r } { K _ { j u } [ n ] } & { { } = } & { \xi _ { 1 } \exp \left( \xi _ { 2 } \theta _ { j u } [ n ] \right) } \end{array}$ , where: $\begin{array} { r l } { \theta _ { j u } [ n ] } & { { } = } \end{array}$ arcsin $\left( \frac { z _ { u } [ n ] - z _ { j } } { d _ { j u } [ n ] } \right)$ , is the elevation angle from jammer to UAV, and $\xi _ { 1 } , \xi _ { 2 }$ are fitting constants depending on the environment.

JR Link is modeled as:

$$
\begin{array} { l } { { \displaystyle { \bf h } _ { j r } [ n ] = \sqrt { \beta _ { 0 } d _ { j r } ^ { - \alpha _ { j r } } [ n ] } } } \\ { { \displaystyle \left( \sqrt { \frac { K _ { j r } } { 1 + K _ { j r } } } { \bf h } _ { j r } ^ { \mathrm { L o S } } [ n ] + \sqrt { \frac { 1 } { 1 + K _ { j r } } } { \bf h } _ { j r } ^ { \mathrm { N L o S } } [ n ] \right) , } } \end{array}\tag{15}
$$

where $d _ { j r } [ n ] ~ = ~ \sqrt { \| w _ { r } - w _ { j } \| ^ { 2 } + z _ { r } ^ { 2 } }$ is the jammer-to-RIS distance, $\alpha _ { j r }$ is the path loss exponent for the JR link, $K _ { j r }$ is the Rician K-factor (assumed static for fixed RIS), $\mathbf { h } _ { i r } ^ { \mathsf { L o S } } [ n ] \ \in \ \mathbb { C } ^ { M \times 1 }$ is the RIS URA array response vector, $\mathbf { h } _ { j r } ^ { \mathrm { N L o \bar { S } } } [ n ] \sim \mathcal { C N } ( \mathbf { 0 } , \mathbb { I } )$ is the i.i.d. Rayleigh fading vector.

The LoS component $\mathbf { h } _ { i r } ^ { \mathrm { L o S } } [ n ]$ is modeled as a 2D URA response vector: $\bar { \mathbf { h } } _ { j r } ^ { \mathrm { L o S } } [ n ] = \mathbf { a } _ { r } ^ { \mathrm { J \bar { R } } } [ n ] = \mathbf { a } _ { r y } ^ { \mathrm { J R } } [ n ] \otimes \mathbf { a } _ { r z } ^ { \mathrm { J R } } [ n ]$ , where:

$$
\begin{array} { r l } & { \mathbf { a } _ { r y } ^ { \mathrm { J R } } [ n ] = [ 1 , e ^ { - j \frac { 2 \pi } { \lambda } d _ { y } \sin \theta _ { j r } [ n ] \cos \phi _ { j r } [ n ] } , } \\ & { \quad \quad \quad \quad \quad \cdot \cdot , e ^ { - j \frac { 2 \pi } { \lambda } ( M _ { y } - 1 ) d _ { y } \sin \theta _ { j r } [ n ] \cos \phi _ { j r } [ n ] } ] ^ { T } , } \\ & { \mathbf { a } _ { r z } ^ { \mathrm { J R } } [ n ] = [ 1 , e ^ { - j \frac { 2 \pi } { \lambda } d _ { z } \sin \theta _ { j r } [ n ] \sin \phi _ { j r } [ n ] } , } \\ & { \quad \quad \quad \quad \quad \quad \cdot \cdot , e ^ { - j \frac { 2 \pi } { \lambda } ( M _ { z } - 1 ) d _ { z } \sin \theta _ { j r } [ n ] \sin \phi _ { j r } [ n ] } ] ^ { T } . } \end{array}
$$

The spatial angles $\theta _ { j r } [ n ]$ and $\phi _ { j r } [ n ]$ are calculated as:

$$
\begin{array} { l } { \sin \theta _ { j r } [ n ] = \displaystyle \frac { z _ { r } - z _ { j } } { d _ { j r } [ n ] } , } \\ { \cos \phi _ { j r } [ n ] = \displaystyle \frac { y _ { r } - y _ { j } } { \sqrt { ( x _ { r } - x _ { j } ) ^ { 2 } + ( y _ { r } - y _ { j } ) ^ { 2 } } } , } \\ { \sin \phi _ { j r } [ n ] = \displaystyle \frac { x _ { r } - x _ { j } } { \sqrt { ( x _ { r } - x _ { j } ) ^ { 2 } + ( y _ { r } - y _ { j } ) ^ { 2 } } } . } \end{array}\tag{16}
$$

## E. Task Offloading

To enable coordinated edge computing, each time slot of duration $\delta _ { t }$ is divided into S sub-slots. The first $s / 2$ subslots are allocated for task offloading from UE $k \in \mathcal { K }$ to its associated ${ \mathrm { U A V ~ } } u \in { \mathcal { U } }$ , with $\tau _ { u , k } ^ { o } [ n ]$ denoting the duration allocated for this transmission during slot $n .$ The remaining $s / 2$ sub-slots are used for relaying data from UAV u to the AP, with $\tau _ { u , k } ^ { R } [ n ]$ denoting the relay duration. The total duration of both phases in each time slot must not exceed the slot length:

$$
\sum _ { u \in \mathcal { U } } \sum _ { k \in \mathcal { K } } \left( \tau _ { u , k } ^ { o } [ n ] + \tau _ { u , k } ^ { R } [ n ] \right) \leq \delta _ { t } , \quad \forall n .\tag{17}
$$

Each offloaded task is partitioned at the UAV: one part is computed locally, while the rest is forwarded to the AP. UAVs operate in a decode-and-forward (DF) relay mode with a oneslot delay. Therefore, slot $n = 1$ is only used for receiving data from UEs, and slot $n = N$ is reserved for final computation, captured by: $\tau _ { u , k } ^ { R } [ 0 ] = 0 , \tau _ { u , k } ^ { R } [ N ] = 0 , \tau _ { u , k } ^ { o } [ N ] = 0 , \mathbf { \dot { \forall } } u \in \mathcal { U } ,$ $k \in \mathcal { K }$

Let $s _ { k } [ n ]$ denote the transmitted symbol from UE k at time slot $n ,$ modeled as a unit-variance symbol, i.e., $\mathbb { E } [ | s _ { k } [ n ] | ^ { 2 } ] =$ 1. Each UE transmits with power $p _ { t } .$ . The received signal at UAV u is: $\mathbf { y } _ { u , k } [ n ] \ = \ { \sqrt { p _ { t } } } \mathbf { h } _ { u , k } [ n ] s _ { k } [ n ] + \mathbf { n } _ { u } [ n ]$ , where $\mathbf { h } _ { u , k } [ n ] \in \mathbb { C } ^ { L \times 1 }$ is the channel from UE k to UAV u, and $\mathbf { n } _ { u } [ n ] \sim \mathcal { C N } ( \mathbf { 0 } , \sigma ^ { 2 } \mathbb { I } _ { L } )$ is the AWGN at UAV u.

To decode $s _ { k } [ n ]$ , UAV u applies a receive beamforming vector $\mathbf { u } _ { u , k } [ n ] \in \mathbf { \bar { \mathbb { C } } } ^ { L \times 1 }$ , yielding:

$$
\begin{array} { r l r } {  { \hat { s } _ { u , k } [ n ] = \mathbf { u } _ { u , k } ^ { H } [ n ] \mathbf { y } _ { u , k } [ n ] } } \\ & { } & { = \sqrt { p _ { t } } \mathbf { u } _ { u , k } ^ { H } [ n ] \mathbf { h } _ { u , k } [ n ] s _ { k } [ n ] + \mathbf { u } _ { u , k } ^ { H } [ n ] \mathbf { n } _ { u } [ n ] . } \end{array}\tag{18}
$$

The resulting SNR at UAV u is given by:

$$
\gamma _ { u , k } [ n ] = \frac { p _ { t } \left| \mathbf { u } _ { u , k } ^ { H } [ n ] \mathbf { h } _ { u , k } [ n ] \right| ^ { 2 } } { \sigma ^ { 2 } \| \mathbf { u } _ { u , k } [ n ] \| ^ { 2 } } .\tag{19}
$$

1) Relay Phase to $A P { \cdot }$ In the second half of each time slot, UAV u forwards the decoded data $\tilde { s } _ { u , k } [ n ]$ to the AP. The equivalent channel including both the direct UAV-AP link and the RIS-assisted reflection is denoted by:

$$
\bar { \mathbf { h } } _ { u a } ^ { H } [ n ] = \mathbf { h } _ { u a } ^ { H } [ n ] + \mathbf { h } _ { r a } ^ { H } [ n ] \Theta [ n ] \mathbf { h } _ { u r } [ n ] ,\tag{20}
$$

as previously defined. The transmitted signal is: ${ \bf Y } _ { u , k } [ n ] =$ $\bar { \mathbf { h } } _ { u a } ^ { H ^ { - } } [ n ] \mathbf { w } _ { u , k } [ n ] \tilde { s } _ { u , k } [ n ] + n _ { a } [ n ]$ , where $\mathbf { w } _ { u , k } [ n ] \ \in \ \mathbb { C } ^ { L \times 1 }$ is the transmit beamforming vector of UAV u and $n _ { a } [ n ] \ \sim$ $\mathcal { C N } ( 0 , \sigma ^ { 2 } )$ is the noise at the AP.

The received SNR at the AP is:

$$
\gamma _ { a , u , k } [ n ] = \frac { { { \left| { { { \bar { \mathbf { h } } } _ { u a } ^ { H } [ n ] } { { \mathbf { w } } _ { u , k } [ n ] } } \right| } ^ { 2 } } } { { { \sigma ^ { 2 } } + { \mathcal { T } } _ { u , k } [ n ] } } ,\tag{21}
$$

where $\mathcal { T } _ { u , k } [ n ]$ denotes the interference power at the $\mathrm { A P \ i e . g . }$ due to jammer), which can be modeled separately depending on the jammer’s strategy. For example:

$$
\begin{array} { r } { \mathcal { T } _ { u , k } [ n ] = p _ { j } \left( \| \mathbf { h } _ { j r } [ n ] \| ^ { 2 } + \| \mathbf { h } _ { j u } [ n ] \| ^ { 2 } \right) , } \end{array}
$$

if both JR and JU links contribute to AP interference.

2) Offloading Rate Model: Let B be the system bandwidth. The number of task bits offloaded from UE k to UAV u in time slot n is:

$$
l _ { u , k } ^ { o } [ n ] = \tau _ { u , k } ^ { o } [ n ] B \log _ { 2 } \left( 1 + \gamma _ { u , k } [ n ] \right) ,\tag{22}
$$

while the number of task bits forwarded from UAV u to the AP is:

$$
l _ { a , u , k } ^ { R } [ n ] = \tau _ { u , k } ^ { R } [ n ] B \log _ { 2 } \left( 1 + \gamma _ { a , u , k } [ n ] \right) .\tag{23}
$$

3) Computation Model: Let $l _ { u , k } ^ { \mathrm { c o m p } } [ n ]$ be the number of task bits from UE k processed by UAV u in slot n. The onboard computing capacity at UAV u is constrained by:

$$
\sum _ { k \in \mathcal { K } } l _ { u , k } ^ { \mathrm { c o m p } } [ n ] c _ { u } \leq F _ { u } ^ { \operatorname* { m a x } } \delta _ { t } , \quad \forall u \in \mathcal { U } ,\tag{24}
$$

where $c _ { u }$ is the number of CPU cycles per bit, and $F _ { u } ^ { \mathrm { m a x } }$ is the CPU capacity of UAV u in cycles per second.

Similarly, the AP computation capacity is:

$$
\sum _ { u \in \mathcal { U } } \sum _ { k \in \mathcal { K } } l _ { a , u , k } ^ { R } [ n ] c _ { a } \leq F _ { a } ^ { \operatorname* { m a x } } \delta _ { t } .\tag{25}
$$

4) Data Causality Constraint: Due to the one-slot relay delay, the bits received by UAV u at slot n can only be computed or forwarded at slot n + 1:

$$
\begin{array} { r l } & { l _ { u , k } ^ { o } [ n ] \leq l _ { a , u , k } ^ { R } [ n + 1 ] + l _ { u , k } ^ { \mathrm { c o m p } } [ n + 1 ] , } \\ & { \qquad \forall u \in \mathcal { U } , k \in { \mathcal { K } } , n = 1 , \ldots , N - 1 . } \end{array}\tag{26}
$$

5) UE Local Computation and Task Completion: Let $l _ { u , k } ^ { \mathrm { l o c } } [ n ]$ be the number of bits computed locally at UE k during time slot n. The total number of processed bits by UE k in slot n is: $L _ { k } [ n ] = l _ { u , k } ^ { \mathrm { l o c } } [ n ] + l _ { u , k } ^ { o } [ n ]$ . To meet application-level processing requirements, each UE must process at least $L _ { k }$ bits over the total horizon:

$$
\sum _ { n = 1 } ^ { N } \big ( l _ { u , k } ^ { \mathrm { l o c } } [ n ] + l _ { u , k } ^ { o } [ n ] \big ) \geq L _ { k } , \forall k \in \mathcal { K } .\tag{27}
$$

## F. Energy Consumption

The system energy consumption includes communication, computation, and propulsion energy from both UEs and UAVs. We model these components as follows:

1) UE Energy Consumption: Each UE $k \in \mathcal K$ incurs energy in two ways: offloading to a UAV and local task processing.

i. Transmission energy: The energy consumed by UE k to offload data to its associated UAV u in time slot n is:

$$
\begin{array} { r } { E _ { k } ^ { \mathrm { t x } } [ n ] = p _ { u , k } [ n ] \tau _ { u , k } ^ { o } [ n ] , } \end{array}\tag{28}
$$

where $p _ { u , k } [ n ]$ is the transmission power of UE k during slot n.

ii. Local computation energy: Modeled using dynamic voltage and frequency scaling (DVFS) theory [9], the energy consumed by UE k for local processing is:

$$
E _ { k } ^ { \mathrm { c o m p } } [ n ] = \frac { \mu _ { k } \left( l _ { u , k } ^ { \mathrm { l o c } } [ n ] \right) ^ { 3 } } { \delta _ { t } ^ { 2 } } ,\tag{29}
$$

where $\mu _ { k }$ is the switched capacitance coefficient of UE k, and $l _ { u , k } ^ { \mathrm { l o c } } [ n ]$ is the number of locally processed bits.

2) UAV Energy Consumption: Each UAV $u \in \mathcal { U }$ consumes energy for computation and flying.

i. Computation energy: To process offloaded bits from all associated UEs, UAV u consumes:

$$
E _ { u } ^ { \mathrm { c o m p } } [ n ] = \sum _ { k \in \mathcal { K } } \frac { \mu _ { u } \left( l _ { u , k } ^ { \mathrm { c o m p } } [ n ] \right) ^ { 3 } } { \delta _ { t } ^ { 2 } } ,\tag{30}
$$

where $\mu _ { u }$ is the capacitance coefficient of UAV u.

ii. Propulsion energy: The flying energy of UAV u at slot n is modeled as:

$$
E _ { u } ^ { \mathrm { H y } } [ n ] = \delta _ { t } \left( \vartheta _ { 1 } \left\| \mathbf { V } _ { u } [ n ] \right\| + \frac { \vartheta _ { 2 } } { \left\| \mathbf { V } _ { u } [ n ] \right\| } \right) ,\tag{31}
$$

where ${ \mathbf V } _ { u } [ n ]$ $[ V _ { u , x } [ n ] , V _ { u , y } [ n ] , V _ { u , z } [ n ] ] ^ { T }$ is the UAV velocity vector, $\Vert \mathbf { V } _ { u } [ n ] \Vert$ $\sqrt { V _ { u , x } ^ { 2 } [ n ] + V _ { u , y } ^ { 2 } [ n ] + V _ { u , z } ^ { 2 } [ n ] }$ is the UAV’s speed, $\displaystyle { \dot { \vartheta } } _ { 1 } , { \vartheta } _ { 2 }$ are aerodynamic constants reflecting linear and inverse-speed power terms (e.g., air drag and hover-related inefficiencies).

3) Total Energy Consumption: The total system energy consumption at time slot n is the sum of all UE and UAV contributions:

$$
E [ n ] = \sum _ { k \in { \mathcal K } } \big ( E _ { k } ^ { \mathrm { t x } } [ n ] + E _ { k } ^ { \mathrm { c o m p } } [ n ] \big ) + \sum _ { u \in { \mathcal U } } \big ( E _ { u } ^ { \mathrm { c o m p } } [ n ] + E _ { u } ^ { \mathrm { f l y } } [ n ] \big ) .\tag{32}
$$

## III. PROBLEM FORMULATION

We aim to maximize the system-wide energy efficiency (in bits/Joule) over the total N time slots:

$$
\begin{array} { c } { { \displaystyle \operatorname* { m a x } _ { z } \frac { \displaystyle \sum _ { n = 1 } ^ { N } \sum _ { k \in { \mathcal K } } \Big ( l _ { u , k } ^ { \mathrm { l o c } } [ n ] + l _ { u , k } ^ { o } [ n ] \Big ) } { \displaystyle \sum _ { n = 1 } ^ { N } [ \sum _ { k \in { \mathcal K } } \Big ( E _ { u , k } ^ { \mathrm { t x } } [ n ] + E _ { u , k } ^ { \mathrm { c o m p } } [ n ] \Big )  } } } \\ { { \displaystyle  \sum _ { n = 1 } ^ { N } [ \begin{array} { c } { { \displaystyle \sum _ { k \in { \mathcal U } } \Big ( E _ { u } ^ { \mathrm { c o m p } } [ n ] + E _ { u } ^ { \mathrm { f l y } } [ n ] \Big ) } } \\ { { \displaystyle + \sum _ { u \in { \mathcal U } } \Big ( E _ { u } ^ { \mathrm { c o m p } } [ n ] + E _ { u } ^ { \mathrm { f l y } } [ n ] \Big ) } } \end{array} ] } } \end{array}\tag{33}
$$

[UAV Kinematics Constraints]

C1: $\begin{array} { r } { { \bf q } _ { u } [ n + 1 ] = { \bf q } _ { u } [ n ] + { \bf V } _ { u } [ n ] \delta _ { t } + \frac { 1 } { 2 } { \bf A } _ { u } [ n ] \delta _ { t } ^ { 2 } , \quad \forall u , n , } \end{array}$

C2a: ${ \bf q } _ { u } [ 0 ] = { \bf q } _ { u , 0 } , \quad { \bf q } _ { u } [ N ] = { \bf q } _ { u , F } , \quad \forall u ,$

$$
\left\{ \begin{array} { l l } { x _ { \mathrm { m i n } } \leq x _ { u } [ n ] \leq x _ { \mathrm { m a x } } , } \\ { y _ { \mathrm { m i n } } \leq y _ { u } [ n ] \leq y _ { \mathrm { m a x } } , \quad \forall u , n , } \\ { z _ { \mathrm { m i n } } \leq z _ { u } [ n ] \leq z _ { \mathrm { m a x } } , } \end{array} \right.\tag{C2b:}
$$

$$
\begin{array} { r } { \begin{array} { r l } { \mathbf { C 3 : } } & { { } \mathbf { V } _ { u } [ n + 1 ] = \mathbf { V } _ { u } [ n ] + \mathbf { A } _ { u } [ n ] \delta _ { t } , \quad \forall u , n , } \end{array} } \end{array}
$$

C4a: $\| \mathbf { q } _ { u } [ n ] - \mathbf { q } _ { u } [ n - 1 ] \| \leq \delta _ { t } V _ { \operatorname* { m a x } } , \quad \forall u , n = 2 , \dots , N ,$

C4b: $\| { \bf q } _ { u } [ n ] - { \bf q } _ { u , F } \| _ { 2 } \leq ( N - n ) V _ { \mathrm { m a x } } \delta _ { t }$

C5: $\| \mathbf { V } _ { u } [ n ] \| \leq V _ { \operatorname* { m a x } } , \quad \forall u , n .$

(34)

[RIS Phase Constraints]

$$
\begin{array} { r } { \begin{array} { l l } { \mathbf { { C 6 } : } } & { \theta _ { m } [ n ] \in [ 0 , 2 \pi ) , \quad \forall m = 1 , \ldots , M , \forall n , } \end{array} } \end{array}
$$

$$
\begin{array} { r } { \begin{array} { r l } { \mathbf { C } 7 : } & { \Theta [ n ] = \operatorname { d i a g } ( e ^ { j \theta _ { 1 } [ n ] } , \dots , e ^ { j \theta _ { M } [ n ] } ) \in \mathbb { C } ^ { M \times M } , \quad \forall n . } \end{array} } \end{array}
$$

[Time Allocation Constraints]

$$
{ \mathrm { C 8 } } \mathrm { : } \quad \tau _ { u , k } ^ { o } [ n ] \geq 0 , \quad \tau _ { u , k } ^ { R } [ n ] \geq 0 , \quad \forall u , k , n ,\tag{35}
$$

$$
{ \mathrm { C 9 } } \colon \tau _ { u , k } ^ { R } [ 0 ] = 0 , \quad \tau _ { u , k } ^ { R } [ N ] = 0 , \quad \tau _ { u , k } ^ { o } [ N ] = 0 , \quad \forall u , k ,
$$

$$
\mathrm { C 1 0 : ~ } \sum _ { u \in \mathcal { U } } \sum _ { k \in \mathcal { K } } \left( \tau _ { u , k } ^ { o } [ n ] + \tau _ { u , k } ^ { R } [ n ] \right) \le \delta _ { t } , \quad \forall n .\tag{36}
$$

[UAV Transmission Power Constraints]

$$
\begin{array} { r } { \begin{array} { r l } { \mathrm { C 1 1 : } } & { { } \| \mathbf { w } _ { u , k } [ n ] \| ^ { 2 } \leq P _ { u } ^ { \operatorname* { m a x } } , \quad \forall u , k , n , } \end{array} } \end{array}
$$

$$
\mathrm { C 1 2 : } \quad \frac { 1 } { N \delta _ { t } } \sum _ { n = 1 } ^ { N } \sum _ { k \in { \cal K } } \tau _ { u , k } ^ { R } [ n ] \| { \bf w } _ { u , k } [ n ] \| ^ { 2 } \leq P _ { u } ^ { \mathrm { a v e } } , \quad \forall u .\tag{37}
$$

[Task and Computation Constraints]

$$
\begin{array} { r } { \begin{array} { l l l } { \mathrm { C 1 3 : } } & { l _ { u , k } ^ { o } [ n ] \leq l _ { a , u , k } ^ { R } [ n + 1 ] + l _ { u , k } ^ { \mathrm { c o m p } } [ n + 1 ] , } & { \forall u , k , n , } \end{array} } \end{array}
$$

$$
\sum _ { k \in \mathcal { K } } l _ { u , k } ^ { \mathrm { c o m p } } [ n ] c _ { u } \leq F _ { u } ^ { \mathrm { m a x } } \delta _ { t } , \quad \forall u , n ,\tag{C15:}
$$

$$
\sum _ { u \in \mathcal { U } } \sum _ { k \in \mathcal { K } } l _ { a , u , k } ^ { R } [ n ] c _ { a } \leq F _ { a } ^ { \operatorname* { m a x } } \delta _ { t } , \quad \forall n ,\tag{38}
$$

$$
\mathrm { C 1 6 : ~ } \sum _ { n = 1 } ^ { N } \big ( l _ { u , k } ^ { \mathrm { l o c } } [ n ] + l _ { u , k } ^ { o } [ n ] \big ) \geq L _ { k } , \quad \forall k .
$$

where C2b enforces spatial boundary conditions for UAV flight, ensuring that each UAV remains within the operational area $( x _ { \mathrm { m i n } } , x _ { \mathrm { m a x } } ) \times ( y _ { \mathrm { m i n } } , y _ { \mathrm { m a x } } )$ and within the altitude range $[ z _ { \mathrm { m i n } } , z _ { \mathrm { m a x } } ]$ . C4b ensures that from any time step, the UAV can still reach the destination within the remaining time slots under the maximum feasible velocity constraint.

Optimization variables:

$$
z = \big \{ \mathbf { V } _ { u } [ n ] , \mathbf { A } _ { u } [ n ] , \boldsymbol { \Theta } [ n ] , \boldsymbol { \tau } _ { u , k } ^ { o } [ n ] , \boldsymbol { \tau } _ { u , k } ^ { R } [ n ] \big \} .
$$

$$
\mathrm { I V . \ : \ : M o D E L - B A S E D \ : D E C E N T R A L I Z E D \ : R L }
$$

To address joint trajectory planning, RIS control, and task offloading under limited global observability and low sample efficiency, we propose a model-based decentralized reinforcement learning (MB-DRL) framework for multi-UAV, multi-UE RIS-assisted MEC networks. Each UAV (agent) $u \in \mathcal { U }$ learns a policy $\pi ^ { \theta _ { u } }$ from its local state and κ-hop neighbor interactions, without requiring global observability.

## A. Motivation

Our method targets two coupled issues. First, global information is limited: distributed UAVs operate with sparse coordination, so each agent only observes its own state and those of κ-hop neighbors $\mathcal { N } _ { u } ^ { ( \kappa ) }$ . Second, model-free exploration is sample-inefficient: real-world data are costly, while purely analytical link and mobility models miss uncertainties (interference, blockage, nonstationary traffic). We therefore let each agent learns a localized predictive model for shorthorizon rollouts that enhance sample efficiency and stabilize PPO-based policy updates under partial observability.

1) Why neighbor UAV states matter?: Decisions on trajectory, RIS phases, and task allocation are coupled through wireless and kinematic constraints. From (6), the received signal at the AP depends on the RIS phase matrix $\Theta [ n ]$ which is jointly affected by concurrent agent proposals and can cause beam conflicts and interference. Constraint C10 implies a shared per-slot time budget: $\tau _ { u , k } ^ { o } [ n ]$ and $\tau _ { u , k } ^ { R } [ n ]$ . Kinematic constraints C1–C4 imply path overlap increases collision risk and propulsion energy, while task variables $l _ { u , k } ^ { o } [ n ] , ~ l _ { u , k } ^ { \mathrm { c o m p } } [ n ]$ depend on SNR and candidate agents’ loads, both shaped by neighbors’ locations and queues. Hence each agent observes κ-hop neighbors’ positions, velocities, queues, and recent RIS controls to make decentralized yet coordinated decisions.

2) Comparison with traditional MARL: CTDE methods such as MADDPG assume global state access and a centralized critic, which degrades scalability under partial observability and constrained links. Our approach is fully decentralized: each agent uses only local and κ-hop observations, learns a predictive transition model, and employs short-horizon modelbased rollouts for efficiency. We adopt PPO with parameterized policy $\pi ^ { \theta _ { u } }$ and value $V ^ { \phi _ { u } }$ because the clipped surrogate yields stable, near-monotonic improvement under noisy rewards and high-dimensional states, and supports parallel local training.

## B. MDP Formulation

Each agent u acts on a local state containing its 3D position ${ \mathbf { q } } _ { u } [ n ]$ and residual energy; per-user task metrics $\bar { l } _ { u , k } ^ { \mathrm { l o c } } [ n ] , l _ { u , k } ^ { o } [ \bar { n } ]$ , and $l _ { u , k } ^ { \mathrm { c o m p } } [ n ] ;$ ; the last RIS phase vector $\Phi [ n -$ $1 ] \ = \ \{ \phi _ { m } [ n - 1 ] \} _ { m = 1 } ^ { M } $ , and the corresponding diagonal phase-shift matrix $\Theta [ n - 1 ] = \mathrm { d i a g } ( e ^ { \mathrm { j } \phi _ { 1 } [ n - 1 ] } , \ldots , \breve { e } ^ { \mathrm { j } \phi _ { M } [ \breve { n - 1 } ] } ) ;$ as well as the positions and velocities of neighbors in $\mathcal { N } _ { u } ^ { ( \kappa ) } { : } \{ \mathbf { q } _ { u ^ { \prime } } , \mathbf { V } _ { u ^ { \prime } } \} _ { u ^ { \prime } \in \mathcal { N } _ { * } ^ { ( \kappa ) } }$ . The action consists of UAV acceleration A [n] (and the implied velocity), time allocations $\tau _ { u , k } ^ { o } [ n ]$ and $\tau _ { u , k } ^ { R } [ n ]$ , and a local RIS phase proposal $\Phi _ { u } [ n ]$ A lightweight controller co-located with the RIS aggregates proposals as $\Phi [ n ] = \mathrm { A g g } \big ( \{ \Phi _ { u } [ n ] \} _ { u \in \mathcal { U } } \big )$ , where $\mathrm { A g g ( \cdot ) }$ is a stateless function using only the submitted proposals $( \mathrm { e . g . }$ weighted averaging: $\begin{array} { r } { \Theta [ n ] = \bar { \Theta } [ n ] = \frac { \sum _ { u = 1 } ^ { U } \Theta _ { u } [ n ] } { I ^ { \prime } } , \Theta _ { u } [ n ] = } \end{array}$ dia $\begin{array} { r } { \begin{array} { l c l } { \mathrm { g } ( \Phi _ { u } [ n ] ) } & { = } & { \mathrm { d i a g } \left( e ^ { j \theta _ { u , 1 } [ n ] } , e ^ { j \theta _ { u , 2 } [ n ] } , \dots , e ^ { j \theta _ { u , M } [ n ] } \right) } \end{array} } \end{array}$ , or winner-takes-most on a codebook).

The per-slot reward for agent u is as:

$$
r _ { u } [ n ] = \frac { \sum _ { k \in \mathcal { K } } \big ( l _ { u , k } ^ { \mathrm { l o c } } [ n ] + l _ { u , k } ^ { o } [ n ] \big ) } { \sum _ { k \in \mathcal { K } } \big ( E _ { u , k } ^ { \mathrm { t x } } [ n ] + E _ { u , k } ^ { \mathrm { c o m p } } [ n ] \big ) + E _ { u } ^ { \mathrm { f l y } } [ n ] } - \beta I _ { u } [ n ] ,\tag{39}
$$

![](images/40a464724e6e796eaf953570dd2f4b1444cf679acf76f509d837072773c0bebb.jpg)  
Fig. 3: Workflow of the decentralized model-based RL for UAV–RIS–MEC systems. The diagram illustrates how realenvironment and model-based replay buffers are leveraged to train the policy (actor) and value (critic) networks via T -step branched rollouts with local and κ-hop neighbor observations, and how PPO-style updates refine both networks.

![](images/190deed8709ea9256bf262068f71ede5db6d469fae8631e878cef60440c5e700.jpg)  
Fig. 4: In our approach: (a) We distinguish three transition kernels: (i) $p ( s ^ { \prime } | s , a )$ , the true environment dynamics; (ii) $\bar { p } ( s ^ { \prime } | s , a )$ the factorized “networked” dynamics using only local κ-hop information (induces dependency bias); (iii) $\hat { p } ( s ^ { \prime } | s , a )$ , the learned predictive model (incurs model error). Their discrepancies give rise to dependency bias $D ( p \| \bar { p } )$ , model error $D ( p \| \hat { p } )$ , and independence-approximation error $D ( \bar { p } \| \hat { p } )$ . (b) The model learning process repeatedly samples experiences from the model buffer. Here, $s _ { t }$ denotes the actual system state at step t, while $s _ { t } ^ { \prime }$ indicates the state predicted by the model at the same step. (c) With short branched rollouts, model-predicted transitions align with real dynamics and $D ( p \| \hat { p } ) \approx D ( p \| \bar { p } ) \leq \xi$ , where $\xi$ is the upper bound of model error tolerance. This ensures a monotonic policy improvement.

where $I _ { u } [ n ]$ measures interference imposed on neighbors via overlapping RIS beams or transmit directions; here $\beta$ controls the throughput–contention tradeoff (the same symbol $\beta$ also appears later as the entropy regularization weight in the PPO loss; meanings are distinguished by context).

## C. Localized Communication

Define the κ-hop neighborhood of UAV u as the set of UAVs that are geographically closest to u at time slot n :

$$
\mathcal { N } _ { u } ^ { ( \kappa ) } [ n ] = \mathop { \mathrm { a r g m i n } } _ { S \subseteq \mathcal { U } \setminus \{ u \} , | S | = \kappa } \sum _ { v \in S } \big \| \mathbf { q } _ { u } [ n ] - \mathbf { q } _ { v } [ n ] \big \| _ { 2 }\tag{40}
$$

where ${ \bf q } _ { u } [ n ] \in \mathbb { R } ^ { 3 }$ denotes the 3D position.

Unlike I3CNet [24], where each UAV u updates its hidden state by simple aggregation

$$
h _ { u } [ n ] = \mathrm { L S T M } \big ( h _ { u } [ n - 1 ] , \mathrm { r e l u } ( s _ { \mathcal { N } _ { u } ^ { ( \kappa ) } } [ n ] ) \big ) ,\tag{41}
$$

which fails to capture nonlinear coupled dynamics; our method introduces localized inter-agent communication through explicit neighborhood aggregation. Specifically, each UAV u updates its internal state by combining its own processed input relu $\left( s _ { \mathcal { N } _ { n } ^ { \left( \kappa \right) } } [ n ] \right)$ and the recent behaviors (policy $\pi _ { u } [ n - 1 ]$ and hidden state $h _ { u } [ n - 1 ] )$

$$
\begin{array} { r } { h _ { u } [ n ] = \mathrm { L S T M } ( h _ { u } [ n - 1 ] , \mathrm { c o n c a t } ( \mathrm { r e l u } ( s _ { { \mathcal N } _ { u } ^ { ( \kappa ) } } [ n ] ) ,   } \\ { \mathrm { r e l u } ( \pi _ { u } [ n - 1 ] ) ,    } \\ { \mathrm { r e l u } ( h _ { u } [ n - 1 ] ) )  ) . } \end{array}\tag{42}
$$

This formulation realizes local communication via direct neighborhood aggregation—each agent exchanges only lowdimensional hidden and policy features within its κ-hop neighborhood, without any global broadcast.

For comparison, distributed PPO (DPPO) and centralized PPO (CPPO) represent two opposite extremes of communication scope:

• In CPPO, a centralized critic or coordinator collects all agents’ states and actions for joint updates:

$$
V [ n ] = \mathrm { L S T M } \left( \mathrm { c o n c a t } \left( \left\{ s _ { u } [ n ] , a _ { u } [ n ] \right\} _ { u = 1 } ^ { N } \right) \right) ,\tag{43}
$$

This achieves full observability but suffers from heavy communication and poor scalability.

• In DPPO, each agent learns completely independently, using only its local trajectory data:

$$
V _ { u } [ n ] = \mathrm { L S T M } ( \mathrm { r e l u } ( s _ { u } [ n ] ) ) ,\tag{44}
$$

which eliminates communication but cannot model interagent coupling.

By contrast, our proposed neighbor-aggregated update provides a middle ground between CPPO’s global coupling and DPPO’s isolation.

Although each UAV observes only its κ-hop neighborhood, the approximation error introduced by ignoring distant agents is theoretically bounded. The formal notion of a ξ-dependent networked system (Appendix B) shows that if the inter-agent coupling decays sufficiently fast, the global dynamics can be well approximated by local transition models within a bounded error $\xi .$

## D. Policy Learning

Note that all “true dynamics” discussed in this paper are instantiated by the system level model. The training objective of the model-based environment is therefore twofold: to approximate the system model while being corrected by real reward feedback. In other words, the learned model is not merely a surrogate to replicate the analytical system model, but rather a predictive environment aligned with maximizing task rewards. Since the system model cannot fully capture real-world uncertainties, reward signals are indispensable to ground the learning process.

Each agent u maintains a policy $\pi ^ { \theta _ { u } }$ , a value function $V ^ { \phi _ { u } }$ a local transition model $\hat { p } _ { u } ,$ , and two FIFO replay buffers: an environment buffer $\mathcal { D } _ { u } ^ { E }$ (capacity $N _ { E } )$ and a model buffer $\mathcal { D } _ { u } ^ { M }$ (capacity $N _ { M } )$ . A single sampled transition (mini-batch index i) is written as

$$
D _ { i } = \big ( s _ { t } ^ { ( i ) } , a _ { t } ^ { ( i ) } , r _ { t } ^ { ( i ) } , s _ { t + 1 } ^ { ( i ) } \big ) ^ { \mathrm { T } } ,\tag{45}
$$

from a mini-batch $\pmb { \cal B } = ( D _ { 1 } , D _ { 2 } , \dots , D _ { | B | } )$ , where $s _ { t } ^ { ( i ) }$ denotes the observed state at time t for the i-th sample. Each $D _ { i }$ is drawn from the union buffer: $D _ { i } \in \mathcal { D } _ { u } ^ { E } \cup \mathcal { D } _ { u } ^ { \bar { M } }$

Training iterates over four phases. (i) Real interaction. Execute $a _ { u } [ n ] \ \sim \ \pi ^ { \theta _ { u } } ( \cdot \ | \ s _ { t } )$ , observe $r _ { u } [ n ]$ and the next state $s _ { t + 1 }$ , and push $( s _ { t } , a _ { u } [ n ] , r _ { u } [ n ] , s _ { t + 1 } )$ into $\mathcal { D } _ { u } ^ { E }$ . (ii) Environment-model learning. Fit the one-step predictor $\hat { p } _ { u }$ with supervised regression on minibatches $B _ { E } ~ \subset ~ { \mathcal { D } } _ { u } ^ { E }$ as Eq. (49), where the second term is optional (reward head) with weight $\eta \geq 0$ . (iii) Branched rollouts. Sample anchor states from $\mathcal { D } _ { u } ^ { E }$ , roll out $\hat { p } _ { u }$ for a short horizon T under the current policy to generate $( \hat { s } _ { t + 1 } , a _ { t + 1 } , \hat { r } _ { t + 1 } , \hat { s } _ { t + 2 } ) , . . . ,$ , and push them into $\mathcal { D } _ { u } ^ { M }$ . (iv) Policy improvement. Form mixed mini-batches $B \subset \tilde { \mathcal { D } _ { u } ^ { E } } \cup \mathcal { D } _ { u } ^ { M }$ , compute advantages ${ \hat { A } } _ { u , i } \ ( \mathrm { e . g . }$ ., generalized advantage estimator (GAE) with parameter $\lambda _ { \mathrm { G A E } } \in [ 0 , 1 ] ) \colon$ for each sampled time index t in mini-batch i, define the TD residual

$$
\delta _ { u , t } ^ { ( i ) } = r _ { t } ^ { ( i ) } + \gamma \left( 1 - d _ { t } ^ { ( i ) } \right) V ^ { \phi _ { u } } \left( s _ { t + 1 } ^ { ( i ) } \right) - V ^ { \phi _ { u } } \left( s _ { t } ^ { ( i ) } \right) ,\tag{46}
$$

where $d _ { t } ^ { ( i ) } \in \{ 0 , 1 \}$ indicates trajectory termination (or branch end) at t.

$$
\hat { A } _ { u , t } ^ { ( i ) } = \sum _ { \ell = 0 } ^ { L _ { t } ^ { ( i ) } - 1 } \left( \gamma \lambda _ { \mathrm { G A E } } \right) ^ { \ell } \left( \prod _ { j = 0 } ^ { \ell - 1 } ( 1 - d _ { t + j } ^ { ( i ) } ) \right) \delta _ { u , t + \ell } ^ { ( i ) } ,\tag{47}
$$

with truncation length $\boldsymbol { L } _ { t } ^ { ( i ) }$ given by the remaining real/model steps until termination or branch end. The bootstrapped return target is

$$
R _ { u , t } ^ { ( i ) } = \hat { A } _ { u , t } ^ { ( i ) } + V ^ { \phi _ { u } } \Big ( s _ { t } ^ { ( i ) } \Big ) .\tag{48}
$$

Update parameters with Eq. (50) and $\operatorname { E q . }$ (51).

The theoretical basis of this model-based learning strategy is established in Appendix A, which proves that the true return $\eta [ \pi ]$ is lower-bounded by the model-estimated return $\hat { \eta } [ \pi ]$ minus a bounded discrepancy term $C \left( p , { \hat { p } } , \pi , \pi _ { \mathrm { D } } \right)$ . This guarantee ensures safe and consistent policy improvement, as long as each update increases the model-based return more than the possible modeling error-precisely the condition maintained in our algorithm through frequent model retraining and PPO clipping.

$$
\mathcal { L } _ { \mathrm { m o d e l } } ^ { ( u ) } = \frac { 1 } { \vert B _ { E } \vert } \sum _ { ( s _ { t } , a _ { t } , s _ { t + 1 } ) \in \mathcal { B } _ { E } } \left. s _ { t + 1 } - \hat { p } _ { u } ( s _ { t } , a _ { t } ) \right. ^ { 2 } + \eta \frac { 1 } { \vert B _ { E } \vert } \sum _ { ( s _ { t } , a _ { t } , r _ { t } ) \in \mathcal { B } _ { E } } \left( r _ { t } - \hat { r } _ { u } ( s _ { t } , a _ { t } ) \right) ^ { 2 } ,\tag{49}
$$

$$
\mathcal { L } \left( \boldsymbol { \theta } _ { u } \right) = \frac { 1 } { \left| \mathcal { B } \right| } \sum _ { i = 1 } ^ { | \mathcal { B } | } \left( - \frac { \pi ^ { \theta _ { u } } \left( a _ { t } ^ { ( i ) } \mid \boldsymbol { s } _ { t } ^ { ( i ) } \right) } { \pi ^ { \theta _ { u } ^ { \mathrm { o l d } } } \left( a _ { t } ^ { ( i ) } \mid \boldsymbol { s } _ { t } ^ { ( i ) } \right) } \hat { A } _ { u , i } + \beta H \left( \pi ^ { \theta _ { u } } ( \cdot \mid \boldsymbol { s } _ { t } ^ { ( i ) } ) \right) \right)\tag{50}
$$

$$
\mathcal { L } \left( \phi _ { u } \right) = \frac { 1 } { \left| \mathcal { B } \right| } \sum _ { i = 1 } ^ { \left| \mathcal { B } \right| } \left( V ^ { \phi _ { u } } \left( s _ { t } ^ { ( i ) } \right) - R _ { u , t } ^ { ( i ) } \right) ^ { 2 } .\tag{51}
$$

## E. Branched Rollout and Model Error Control

From each real transition in $\mathcal { D } _ { u } ^ { E }$ , the model simulates only the next T −1 steps. Fig. 4 visualizes the process: panel (a) contrasts predicted and real trajectories; panel (b) shows model error constrained; panel (c) highlights steady policy improvement. We track a bounded tolerance $\xi$ via $D ( p \parallel \hat { p } ) \approx$ $D ( p \parallel \bar { p } ) = \xi ,$ , but implementation relies on the operational criterion above (short $T _ { \ast }$ , anchor-at-real states).

As formally analyzed in Appendix C, long-horizon (vanilla) model rollouts can accumulate model bias and lead to loose performance guarantees, while short T -step branched rollouts effectively bound the discrepancy between true and modeled returns. The derived bound (Eq. (66)) shows that the influence of model error $\epsilon _ { m _ { i } }$ is truncated after $T$ steps, which explains the empirically observed monotonic improvement in Fig. 4(d). Furthermore, Corollary 1 extends this guarantee to the general ξ-dependent case, confirming that even with limited inter-agent coupling, the expected return deviation remains bounded and diminishes.

The step-by-step training procedure of the proposed MB-DRL framework is summarized in Algorithm 1.

## V. SIMULATION

## A. Setup

1) Network Topology and Mobility: We consider a 1, 000m × 1, 000m square area of interest (AoI). Three singleantenna UEs $( K = 1 0 )$ are randomly distributed within a 200m × 200m square centered at (200, 200) on the ground plane $( z ~ = ~ 0 )$ . A MEC-enabled AP with a single antenna is deployed at coordinates $( x _ { a } , y _ { a } ) \ : = \ : ( 1 0 0 , 8 5 0 )$ at ground level $( z _ { a } ~ = ~ 0 )$ . A uniform rectangular RIS is placed at $( x _ { r } , y _ { r } ) ~ = ~ ( 6 5 0$ , 200) at height $z _ { r } ~ = ~ 2 0 ~ \mathrm { ~ m ~ }$ , consisting of $M _ { y } = 8$ and $M _ { z } = 8$ elements, i.e., $M = 6 4$ elements. The network is assisted by $U = 1 0 \ \mathrm { U A V s } ,$ each equipped with $L = 4$ antennas, whose initial and final positions are (0, 0, 20) and $( 1 0 0 0 , 8 0 0 , 2 0 )$ . The altitude of each UAV is restricted within $z _ { \mathrm { m i n } } ~ =$ 10m and $z _ { \mathrm { m a x } } ~ = ~ 2 0 0 \mathrm { m } .$ , and must remain inside the AoI boundary. In addition, a ground-based jammer is located at (100, 800) with fixed transmit power $p _ { j } = 0 . 5 \mathrm { W }$

2) Time and Resource Allocation: The total mission duration is $T = 1 0 0 \mathrm { s } .$ , uniformly divided into $N = 1 0 0$ time slots of $\delta _ { t } ~ = ~ 1 \mathrm { s }$ each. Every slot is further partitioned into six equal sub-slots. The available bandwidth is $B = \mathrm { 1 M H z }$ Each UE is assigned a task load of $L _ { k } ~ = ~ 2 \times 1 0 ^ { 5 }$ bits to be processed before the mission ends. The maximum computational capacities are $F _ { u } ^ { \mathrm { m a x } } = 1 0 ^ { 9 }$ cycles/s for each UAV and $F _ { a } ^ { \mathrm { m a x } } ~ = ~ 1 0 ^ { 1 0 }$ cycles/s for the AP, with per-bit computational complexity $c _ { u } = c _ { a } = 1 0 ^ { 3 }$ cycles/bit.

```tcl
Algorithm 1 Model-Based Decentralized RL (MB-DRL)
Require: Agents U, horizon $N ,$ rollout length T , neighbor
hood size κ
1: Initialize $\{ \pi ^ { \theta _ { u } } , V ^ { \phi _ { u } } , \hat { p } _ { u } , D _ { u } ^ { E } , { \cal D } _ { u } ^ { M } \}$ u∈U
2: for each training episode do
3: (I) Sampling
4: Reset environment
5: for $n = 0$ to $N - 1$ do
6: for each UAV $u \in \mathcal { U }$ do
7: Observe $s _ { u } [ n ]$ (local + κ-hop neighbors)
8: Sample $a _ { u } \dot { [ } n \dot { ] } \sim \pi ^ { \theta _ { u } } ( \cdot | s _ { u } [ n ] )$ and propose RIS
phases $\Phi _ { u } [ n ]$
9: end for
10: Aggregate RIS: $\Phi [ n ] = \mathrm { A g g } ( \{ \Phi _ { u } [ n ] \} _ { u \in \mathcal { U } } )$ and ap
ply $\Theta [ n ]$
11: Step environment; obtain $\{ r _ { u } [ n ] , s _ { u } [ n + 1 ] \} _ { u \in \mathcal { U } }$
12: for each UAV $u \in \mathcal { U }$ do
13: Store $( s _ { u } [ n ] , a _ { u } [ n ] , r _ { u } [ n ] , s _ { u } [ n + 1 ] )$ into $\mathcal { D } _ { u } ^ { E }$
14: end for
15: end for
16: for each UAV $u \in \mathcal { U }$ do
17: (II) Local model learning
18: Sample minibatch $B _ { E } \subset \breve { D } _ { u } ^ { E }$ and update $\hat { p } _ { u }$ (and $\hat { r } _ { u } )$
via (49)
19: (III) Branched rollout
20: Sample anchor states $\left\{ \hat { s } _ { 0 } \right\}$ from $\mathcal { D } _ { u } ^ { E }$
21: for $t = 0$ to $T - 1$ do
22: Sample $\hat { a } _ { t } \sim \pi ^ { \theta _ { u } } ( \cdot | \hat { s } _ { t } )$ , predict $\hat { s } _ { t + 1 } = \hat { p } _ { u } ( \hat { s } _ { t } , \hat { a } _ { t } )$
(and $\hat { r } _ { t } )$
23: Store $\left( \hat { s } _ { t } , \hat { a } _ { t } , \hat { r } _ { t } , \hat { s } _ { t + 1 } \right)$ into $\mathcal { D } _ { u } ^ { M }$
24: end for
25: (IV) PPO policy and value update
26: Form mixed minibatch $B \subset \mathcal { D } _ { u } ^ { \hat { E } } \cup \mathcal { D } _ { u } ^ { M }$
27: Update $\theta _ { u }$ and $\phi _ { u }$ using $( 5 0 ) \AA - ( 5 1 )$ with GAE advan
tages
28: end for
29: end for
```

3) Energy and Mobility Models: DVFS parameters are set as $\mu _ { u } ~ = ~ 1 0 ^ { - 2 8 }$ and $\mu _ { u , k } ~ = ~ 1 0 ^ { - 2 8 }$ . UAV flight energy consumption is modeled using parameters $\vartheta _ { 1 } = 9 . 2 6$ and $\vartheta _ { 2 } =$ 2250. UAV mobility is constrained by a maximum velocity

$V _ { \mathrm { m a x } } = 2 0 \mathrm { m / s }$ and an acceleration bound $| { \bf A } _ { u } [ n ] | \leq 2 \mathrm { m / s ^ { 2 } }$ for all u and n.

4) Channel and Propagation Parameters: The reference path gain is $\beta _ { 0 } = - 3 0 \mathrm { d B }$ at a distance of 1 m. The path-loss exponent is set to $\alpha _ { i } = 2 . 2$ for line-of-sight (LoS) links and $\alpha _ { i } ~ = ~ 3 . 5$ for non-line-of-sight (NLoS) links. Rician fading is considered, with K-factors $\beta _ { i } = 1 0 \mathrm { d B }$ for UE–UAV and UAV–RIS links, and $\beta _ { i } ~ = ~ 5 \mathrm { d B }$ for other cases. The noise power is fixed at $\sigma ^ { 2 } = - 1 0 0 \mathrm { d B m }$

5) Reinforcement Learning Hyperparameters: The reinforcement learning setup uses a rollout horizon of 10 steps per simulation episode. Neighborhood communication is limited to $\kappa ~ = ~ 1$ hop in the local graph. Two replay buffers are maintained: one for real interactions with size $| \mathcal { D } ^ { E } | = 1 0 ^ { 5 }$ and one for model-generated interactions with size $| \dot { \mathcal { D } } ^ { M } | = 1 0 ^ { 5 }$ The batch size is 32 for model learning and 64 for policy updates. The learning rate is set to $3 \times 1 0 ^ { - 4 }$ . For PPO training, the clipping ratio is 0.2, entropy coefficient is 0.01, discount factor $\gamma = 0 . 9 9$ , and GAE parameter $\lambda _ { \mathrm { G A E } } = 0 . 9 5$ . Training over 2,000 episodes, each consisting of $N = 1 0 0 ~ \mathrm { s t e p s }$

6) Baselines: The benchmarks include CPPO, a centralized PPO with full global information serving as the upper bound; DPPO, a fully decentralized PPO relying only on local observations; IC3Net [24], as presented in Section III, which augments MARL with differentiable inter-agent communication; and Ours, a model-based decentralized PPO that exploits short-horizon rollouts and κ-hop local modeling for joint UAV mobility, offloading, and RIS phase control.

We introduce four state-of-the-art (SOTA) competitors for comparison, all of them were implemented in the same simulation environment to ensure consistency:

• Wu et al. [9] employ a model-free MATD3 offloading policy without explicit inter-UAV communication or modelbased rollout.

• Qin et al. [2] adopt an iterative Dinkelbach–BCD optimization framework, solving convex subproblems per time slot without reinforcement learning or local interaction.

• Yang et al. [1] combine deep reinforcement learning with successive convex approximation (DRL–SCA) for joint caching and computing optimization but remain modelfree and globally coupled.

• Song et al. [41] apply a pure SCA-based iterative solver for joint UAV trajectory and phase optimization, also without communication or dynamic rollout modules.

Thus, all SOTA baselines are model-free and communicationfree, executed under the same UAV–RIS–MEC setup.

7) Performance Metrics: We evaluate performance using average episode reward (sum of UAV rewards over all slots) measuring training convergence and policy stability; energy efficiency (processed bits per Joule) measuring how effectively communication, computation, and mobility resources are utilized; throughput $( l _ { u , k } ^ { \mathrm { l o c } } [ n ] + l _ { u , k } ^ { o } [ n ]$ , average bits local processed and offloaded per second) and data rate $( l _ { u , k } ^ { o } [ n ]$ average bits offloaded per second) quantifing service capability and offloading quality, respectively; and the energy efficiency index (EEI), defined as the inverse of total energy consumption in $\mathrm { K J ^ { - 1 } }$ , directly highlights the energy cost associated with the achieved performance.

## B. Results

1) Convergent speed comparison: As shown in Fig. 5, the centralized CPPO still achieves the highest cumulative reward due to full-state observability, serving as the upper performance bound. Under both model-free and model-based settings, our decentralized approach $( ^ { 6 } \mathrm { { O u r s } ^ { 3 3 } ) }$ rapidly converges toward CPPO, clearly outperforming I3CNet and DPPO. In the model-free case, the improvement mainly stems from localized communication and neighborhood-aware coordination, which mitigate partial observability. When the learned predictive model is introduced (model-based case), convergence becomes faster and smoother because short-horizon branched rollouts enrich training data and reduce the variance of value estimation. This indicates that model-based local simulation allows each UAV to capture short-term transition regularities and correct for delayed or missing neighbor information, thereby improving both sample efficiency and stability without requiring centralized state access or dense inter-agent communication.

![](images/09d312f0a52809aed33af606859cf9e21b52439fcfc2bea434b34aa447b85cb1.jpg)

![](images/e23484ae271bb4d795a49d80762f0ea956e21be850392c602fb3e9664deccccb.jpg)  
(a) Model-free.  
(b) Model-based.  
Fig. 5: Convergence curves.

2) Performance metrics comparison with baselines: As shown in Fig. 6(a) - 6(d), the cumulative distribution functions (CDFs) of throughput, EEI, data rate, and energy efficiency clearly demonstrate the performance trade-offs among methods. Fig. 6(a): CPPO achieves the highest throughput due to full observability, while our decentralized method (“Ours”) closely approaches it, outperforming I3CNet and DPPO—showing that localized neighborhood communication preserves coordination efficiency without global information. Fig. 6(b): Both CPPO and our method consume less propulsion and computation energy, as model-based policy learning yields smoother trajectories and lower control effort. Fig. 6(c): Our approach maintains higher data rates through adaptive trajectory and power allocation guided by the learned dynamics model. Fig. 6(d): Consequently, in energy efficiency (bits/Joule), our method achieves the best trade-off among decentralized schemes, approaching the centralized upper bound.

3) Performance metrics comparison with SOTA: As shown in Table III, the centralized CPPO achieves the lowest policy and total losses and thus represents the upper bound of performance under full observability. Our proposed method (“Ours”)

TABLE III: The comparison results of various performance indicators of multiple algorithms with time slots, including baseline, our method, and four SOTA competitor algorithms.
<table><tr><td>Type</td><td>Time Slots</td><td colspan="4">Policy loss</td><td colspan="4">Total loss</td><td colspan="4">Energy efficiency (bits/J)</td><td colspan="4">Throughput (Kbps)</td></tr><tr><td></td><td></td><td>CPPO</td><td>DPPO</td><td>IC3Net</td><td>Ours</td><td>CPPO</td><td>DPPO</td><td>IC3Net</td><td>Ours</td><td>CPPO DPPO</td><td>IC3Net</td><td>Ours</td><td>CPPO</td><td>DPPO</td><td>IC3Net</td><td>Ours</td></tr><tr><td rowspan="7">Baselines</td><td>0</td><td>0.42 0.82</td><td>0.58</td><td></td><td>0.48 1.36</td><td>1.88</td><td>1.56</td><td>1.30</td><td>88</td><td>50</td><td>70</td><td>82</td><td>14500</td><td>9000</td><td>12000</td><td>13800</td></tr><tr><td>100</td><td>0.40</td><td>0.80 0.55</td><td>0.45</td><td>1.34</td><td>1.86</td><td>1.54</td><td>1.27</td><td>92</td><td>53</td><td>73</td><td>86</td><td>15500</td><td>9800</td><td>12800</td><td>14600</td></tr><tr><td>200</td><td>0.38</td><td>0.79</td><td>0.52</td><td>0.43</td><td>1.84</td><td>1.50</td><td>1.24</td><td>96</td><td>56</td><td>76</td><td>90</td><td>16500</td><td>10500</td><td>13500</td><td>15600</td></tr><tr><td>300</td><td>0.36</td><td>0.78 0.50</td><td></td><td>1.32 1.30</td><td>1.83</td><td>1.48</td><td>1.22</td><td>99</td><td>58</td><td>78</td><td>93</td><td>17500</td><td>11200</td><td>14200</td><td>16600</td></tr><tr><td>400</td><td>0.35</td><td>0.77 0.49</td><td></td><td>0.41 0.40</td><td>1.28 1.82</td><td>1.46</td><td>1.20</td><td>101</td><td>60</td><td>80</td><td>95</td><td>18500</td><td>11800</td><td>15000</td><td>17600</td></tr><tr><td>500</td><td>0.34</td><td>0.76 0.48</td><td></td><td>0.38</td><td>1.26 1.80</td><td>1.45</td><td>1.18</td><td>103</td><td>62</td><td>82</td><td>97</td><td>19500</td><td>12500</td><td>15800</td><td>18500</td></tr><tr><td></td><td>Wu [9]</td><td>Qin [2]</td><td>Yang [1] Song [41]</td><td></td><td>Wu [9] Qin [2]</td><td>Yang [1] Song [41]</td><td></td><td></td><td></td><td>[Wu [9] Qin [2] Yang [1] Song [41]</td><td></td><td>Wu [9]</td><td>Qin [2]</td><td>Yang [1]</td><td>Song [41]</td></tr><tr><td rowspan="6">0 SOTA</td><td></td><td>0.56</td><td>0.52</td><td></td><td>0.49</td><td>1.62 1.54</td><td>1.58</td><td>1.52</td><td>68</td><td>72</td><td>74</td><td>76</td><td>12000</td><td>12600</td><td>13000</td><td>13300</td></tr><tr><td>100</td><td>0.54</td><td>0.50 0.48</td><td>0.50</td><td>0.47</td><td>1.60</td><td>1.52</td><td></td><td></td><td>74</td><td>76</td><td>78</td><td>12600</td><td>13200</td><td>13600</td><td>13900</td></tr><tr><td></td><td>0.53</td><td>0.47 0.49</td><td>0.46</td><td>1.58</td><td>1.50</td><td>1.56 1.54</td><td>1.50 1.48</td><td>70 72</td><td>76</td><td>78</td><td>80</td><td>13200</td><td>13800</td><td>14200</td><td>14600</td></tr><tr><td>200 300</td><td>0.52</td><td>0.46 0.48</td><td></td><td>0.45</td><td>1.56 1.49</td><td>1.52</td><td>1.46</td><td>73</td><td>77</td><td>80</td><td>82</td><td>13600</td><td>14200</td><td>14800</td><td>15200</td></tr><tr><td>400</td><td>0.51 0.45</td><td>0.47</td><td>0.44</td><td>1.55</td><td>1.47</td><td>1.50</td><td>1.44</td><td>74</td><td>78</td><td>82</td><td>84</td><td>14000</td><td>14600</td><td>15200</td><td>15600</td></tr><tr><td>500</td><td>0.50</td><td>0.44 0.46</td><td></td><td>0.43</td><td>1.54 1.46</td><td>1.48</td><td>1.42</td><td>75</td><td>79</td><td>84</td><td>86</td><td>14400</td><td>15000</td><td>15600</td><td>16000</td></tr></table>

![](images/6124d1d05d6b61b68fff4f254f65fef7ac0916f26c26c40f4db8f09b72262d1c.jpg)  
(a) CDF of throughput (Kbps).

![](images/3a92d8a3a3f6229c0ee584e9694f1b299d5228051f662ba6116669849c944088.jpg)  
(b) CDF of energy (KJ).

![](images/91746f3b65616709e0d262c850ad57a5c89a046804b91bc636c9f0cc00969de6.jpg)  
(c) CDF of data rate (Kbps).

![](images/f25893ee5331f74bff90ff60e9bbd1c33b0febb53e003fa57ff6731e1fa36b49.jpg)  
(d) CDF of energy efficiency (bits/Joule).  
Fig. 6: Performance metrics comparison.

consistently ranks second across all metrics, demonstrating that localized communication and short-horizon model-based rollouts effectively stabilize learning and improve efficiency. Compared with the decentralized I3CNet and DPPO, our approach significantly enhances both energy efficiency and throughput while maintaining lower optimization loss. Among SOTA competitors, all methods were re-implemented under the same simulation environment and parameter settings for fairness; they remain model-free and communication-free, leading to slower convergence and suboptimal coordination. These results highlight that incorporating lightweight neighborhood aggregation and model-based prediction enables decentralized UAV agents to approach centralized performance with reduced communication overhead.

4) Ablation study: We have four algorithm variants:

• Full (All innovations included)

• No-BR (no branched rollout)

• No-LM (remove local behaviors)

• No-KH (without kappa-hop communication)

As shown in Table IV, removing either the neighborhood communication (No-KH) or the model-based rollout (No-BR) leads to a clear degradation in both energy efficiency and throughput. The full model achieves the lowest losses and highest performance, confirming that localized communication enhances cooperative awareness, while model-based rollouts improve sample efficiency and stability. Together, these components enable decentralized agents to approach centralized learning performance with lower communication cost.

TABLE IV: Ablation study on different model components. “Full” represents the complete model with localized communication and model-based rollout.
<table><tr><td>Method</td><td>Policy loss (↓)</td><td>Total loss (↓)</td><td>Energy eff. (bits/J) (↑)</td><td>Throughput (Kbps) (↑)</td></tr><tr><td>No-KH</td><td>0.68</td><td>1.86</td><td>165</td><td>9300</td></tr><tr><td>No-BR</td><td>0.59</td><td>1.73</td><td>275</td><td>11800</td></tr><tr><td>No-LM</td><td>0.54</td><td>1.65</td><td>320</td><td>13200</td></tr><tr><td>Full</td><td>0.46</td><td>1.48</td><td>410</td><td>14100</td></tr></table>

5) Policy loss and total loss comparsion: Fig. 7(a)–(c) illustrate the policy loss evolution for UAVs 1, 5, and 10. The centralized CPPO maintains the lowest and most stable loss due to full-state observability and synchronized updates. Our proposed method (“Ours”) achieves comparable stability and clearly outperforms I3CNet and DPPO, indicating that localized communication and model-based rollouts enable consistent policy improvement even under decentralized settings. In contrast, DPPO suffers from significant variance and slow convergence, while I3CNet partially reduces this variance through message passing but still accumulates noise over time. Fig. 7(d)–(f) show the total loss (policy + value) for the same UAVs. Again, our method achieves the lowest loss among decentralized approaches and remains close to the centralized upper bound (CPPO). This suggests that integrating short-horizon predictive models effectively stabilizes both policy and value updates by reducing estimation bias and enhancing credit assignment. Overall, the results confirm that our neighborhood-aware, model-based learning framework improves convergence consistency and reduces interagent performance disparity across UAVs.

![](images/3c3d674e1acef277a6823203ee0ee1dfdc8ffb74c78947f2035636ebeb8edfb6.jpg)  
(a) Policy loss of UAV 1.

![](images/f68125c65189092399881d6ebdb5d0115e70b0820442fb17819be0a3f9e0d422.jpg)  
(b) Policy loss of UAV 5.

![](images/ad7a64ebc2bc4c1ac8691f08b7a90b0aa8c9220633ead1ab6ae0d8f27efb00b2.jpg)

![](images/43e590c5c8c066c4e536007eb42a4d7eba27dce842a1c3760d6f4bf4726b68e3.jpg)  
(d) Total loss of UAV 1.

(c) Policy loss of UAV 10.  
![](images/48b95390f190fd4001c2fe31c15a23c20e4cb6c991964df2b385e40b7ecd4f6f.jpg)  
(e) Total loss of UAV 5.

![](images/7172a3fafca8e7452c594e3a19b62ad2c2da33d07973647e11bbe8d1e903c97a.jpg)  
(f) Total loss of UAV 10.  
Fig. 7: Policy loss and total loss across UAVs (total loss= policy loss+value loss).

6) UAV trajectory plotting: As shown in Fig.8, our method produces smoother and more directed UAV trajectories compared with the baseline algorithms. By leveraging localized communication and neighbor-aware state aggregation, each UAV can anticipate nearby agents’ movements and coordinate task coverage more efficiently. Consequently, our trajectories exhibit fewer detours and abrupt turns, and less “zigzag”, approaching near-straight paths between task areas. In contrast, DPPO and I3CNet show erratic, oscillatory motion due to limited observability and lack of cooperative awareness, while CPPO achieves stable but overly centralized flight patterns with reduced adaptability. These results confirm that our decentralized yet communication-aware policy effectively balances coordination and autonomy in UAV navigation.

![](images/d694b294683b6d4a5332905e4e96b40d053674179c2e5754390c8de69db127f3.jpg)  
Fig. 8: UAV trajectory plotting under CPPO, DPPO, IC3Net, and our method (avg. of 10 UAVs).

7) Parameter analysis: To further dissect the effectiveness of individual design choices, Fig. 9(a) investigates the impact of increasing the neighborhood size κ, while Fig. 9(b) examines the number of branches and rollout length used in shorthorizon rollouts. Specifically, increasing κ allows UAV agents to incorporate information from more neighbors into their local state, thereby better capturing interference patterns (e.g., RIS beam collisions, overlapping task forwarding) and enabling proactive coordination. This leads to higher throughput and reduced oscillation during training, especially under congested network scenarios. As shown in Fig. 9(b), increasing both the rollout length and the number of model-based branches consistently improves energy efficiency. Longer rollouts allow agents to anticipate long-term rewards, while multiple branches enhance exploration and reduce policy variance. However, the marginal gain diminishes beyond four branches, indicating that excessive branching adds computational cost without proportional benefit.

![](images/f5b59f5995ee283dd8cde82fdec705e33528d4fcb1989d9ee0286aa6f7380171.jpg)  
     -

(a) Impact of κ (κ-hop communication).  
![](images/14cf605a895ffb2df2d56047e64e34471d2787e31eb478cb132244974d62f5d4.jpg)  
(b) Impact of branches and rollout length.  
Fig. 9: Parameter analysis results.

## VI. CONCLUSION

We propose a decentralized, model-based RL framework for multi-UAV RIS-assisted MEC networks, where each UAV optimizes its trajectory, task offloading, and RIS control using only κ-hop local observations and short-horizon branched rollouts. Unlike conventional model-free or message-passing MARL approaches, our method integrates localized neighboraware communication and predictive model rollouts to jointly enhance coordination and sample efficiency under partial observability.

Extensive simulations show that our approach converges nearly as fast as centralized PPO (CPPO) while substantially outperforming decentralized baselines (DPPO, I3CNet) in terms of throughput, energy efficiency, and stability. The ablation and parameter analyses further confirm that neighborhood aggregation mitigates interference and model-based rollouts suppress value-estimation variance, enabling UAVs to follow smoother, energy-saving trajectories.

Future work will extend this framework by jointly learning the neighborhood-aggregation operator and an event-triggered communication schedule together with the policy under bandwidth/latency constraints, and by making branched rollouts uncertainty-aware via adaptive horizons $T$ and branch counts guided by epistemic uncertainty. We will also pursue tighter decentralized convergence guarantees that explicitly couple dependency bias and model error, and incorporate jammeraware trajectory and RIS beam adaptation with interference prediction to enable anti-jamming communications.

## REFERENCES

[1] X. Yang, Q. Wang, B. Yang, and X. Cao, “Energy-efficient aerial star-ris-aided computing offloading and content caching for wireless sensor networks,” Sensors, 2025. [Online]. Available: https: //pmc.ncbi.nlm.nih.gov/articles/PMC11769421/

[2] X. Qin, Z. Song, T. Hou, W. Yu, J. Wang, and X. Sun, “Joint optimization of resource allocation, phase shift, and uav trajectory for energy-efficient ris-assisted uav-enabled mec systems,” IEEE Transactions on Green Communications and Networking, vol. 7, no. 4, pp. 1778–1792, 2023.

[3] F. Naaz, A. Nauman, T. Khurshaid, and S.-W. Kim, “Empowering the vehicular network with ris technology: A state-of-the-art review,” Sensors, vol. 24, no. 2, p. 337, 2024.

[4] A. Khan, V. Kumar, and A. Ribeiro, “Large scale distributed collaborative unlabeled motion planning with graph policy gradients,” IEEE Robotics and Automation Letters, vol. 6, no. 3, pp. 5340–5347, 2021.

[5] F. Yang and N. Matni, “Communication topology co-design in graph recurrent neural network based distributed control,” in 2021 60th IEEE Conference on Decision and Control (CDC), pp. 3619–3626. IEEE, 2021.

[6] A. Bansal, N. Agrawal, K. Singh, C.-P. Li, and S. Mumtaz, “Ris selection scheme for uav-based multi-ris-aided multiuser downlink network with imperfect and outdated csi,” IEEE Transactions on Communications, vol. 71, no. 8, pp. 4650–4664, 2023.

[7] K. Wang, T. Cao, and X. Li, “A survey on trajectory planning and resource allocation in unmanned aerial vehicle-assisted edge computing networks,” Journal of Electronics & Information Technology, 2025. [Online]. Available: https://jeit.ac.cn/en/article/doi/10.11999/JEIT241071

[8] G. Sun, Y. Wang, Z. Sun, Q. Wu, J. Kang, D. Niyato, and V. C. Leung, “Multi-objective optimization for multi-uav-assisted mobile edge computing,” IEEE Transactions on Mobile Computing, 2024.

[9] L. Wu, C. Zhang, B. Zhang, J. Du, and J. Qu, “Towards energyefficiency: Integrating matd3 reinforcement learning method for computational offloading in ris-aided uav-mec environments,” IEEE Internet of Things Journal, 2025.

[10] S. Jiang, X. Wang, J. Lin, C. Huang, Z. Qian, and Z. Han, “A delayoriented joint optimization approach for ris-assisted mec-mimo system,” IEEE Transactions on Mobile Computing, 2024.

[11] J. Wang and H. Liu, “Real-time uav-ris cooperation with dynamic channel learning for mec networks,” IEEE Internet of Things Journal, 2024.

[12] M. Saif, M. Javad-Kalbasi, and S. Valaee, “Effectiveness of reconfigurable intelligent surfaces to enhance connectivity in uav networks,” IEEE Transactions on Wireless Communications, 2024.

[13] S. Prabhashana, D. V. Huynh, and S. Mumtaz, “Machine learning-based resource allocation in 6g integrated space and terrestrial networks-aided intelligent autonomous transportation,” IEEE Transactions on Vehicular Technology, 2025.

[14] A. A. Khalil, M. Y. Selim, and M. A. Rahman, “Deep learningbased energy harvesting with intelligent deployment of ris-assisted uavcfmmimos,” Computer Networks, vol. 229, p. 109784, 2023.

[15] E. T. Michailidis, M.-G. Volakaki, N. I. Miridakis, and D. Vouyioukas, “Optimization of secure computation efficiency in uav-enabled risassisted mec-iot networks with aerial and ground eavesdroppers,” IEEE Transactions on Communications, 2024.

[16] L. He, G. Sun, Z. Sun, Q. Wu, J. Kang, D. Niyato, Z. Han, and V. C. Leung, “Qoe maximization for multiple-uav-assisted multi-access edge computing via an online joint optimization approach,” IEEE Transactions on Networking, 2025.

[17] T. L. Nguyen, G. Kaddoum, T. N. Do, and Z. J. Haas, “Ground-touav and ris-assisted uav-to-ground communication under channel aging: Statistical characterization and outage performance,” IEEE Transactions on Communications, 2025.

[18] A. Abdalla and V. Marojevic, “Enhancing secrecy energy efficiency in ris-aided aerial mobile edge computing networks: A deep reinforcement learning approach,” arXiv preprint arXiv:2505.10815, 2025. [Online]. Available: https://arxiv.org/abs/2505.10815

[19] W. Chen, Y. Zou, J. Zhu, and L. Zhai, “Energy efficiency optimization of active flying-ris assisted mobile edge computing networks: A deep reinforcement learning approach,” IEEE Internet of Things Journal, 2025.

[20] Y. Wang, J. Farooq, H. Ghazzai, and G. Setti, “Joint positioning and computation offloading in multi-uav mec for low latency applications: a proximal policy optimization approach,” IEEE Transactions on Mobile Computing, 2025.

[21] T. Chu, S. Chinchali, and S. Katti, “Multi-agent reinforcement learning for networked system control,” arXiv preprint arXiv:2004.01339, 2020.

[22] Y. Wang, T. Duhan, J. Li, and G. Sartoretti, “Lns2+ rl: Combining multiagent reinforcement learning with large neighborhood search in multiagent path finding,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 39, no. 22, pp. 23 343–23 350, 2025.

[23] G. Qu, Y. Lin, A. Wierman, and N. Li, “Scalable multi-agent reinforcement learning for networked systems with average reward,” Advances in Neural Information Processing Systems, vol. 33, pp. 2074–2086, 2020.

[24] A. Singh, T. Jain, and S. Sukhbaatar, “Learning when to communicate at scale in multiagent cooperative and competitive tasks,” arXiv preprint arXiv:1812.09755, 2018.

[25] L. Han, P. Sun, Y. Du, J. Xiong, Q. Wang, X. Sun, H. Liu, and T. Zhang, “Grid-wise control for multi-agent reinforcement learning in video game ai,” in International conference on machine learning, pp. 2576–2585. PMLR, 2019.

[26] M. Deisenroth and C. E. Rasmussen, “Pilco: A model-based and data-efficient approach to policy search,” in Proceedings of the 28th International Conference on machine learning (ICML-11), pp. 465–472, 2011.

[27] Z. Wu, C. Yu, C. Chen, J. Hao, and H. H. Zhuo, “Models as agents: Optimizing multi-step predictions of interactive local models in modelbased multi-agent reinforcement learning,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 37, no. 9, pp. 10 435–10 443, 2023.

[28] M. Morari, C. E. Garcia, and D. M. Prett, “Model predictive control: Theory and practice,” IFAC Proceedings Volumes, vol. 21, no. 4, pp. 1–12, 1988.

[29] S. Wang, J. Duan, D. Shi, C. Xu, H. Li, R. Diao, and Z. Wang, “A datadriven multi-agent autonomous voltage control framework using deep reinforcement learning,” IEEE Transactions on Power Systems, vol. 35, no. 6, pp. 4644–4654, 2020.

[30] J. Liu, P. Hang, X. Na, C. Huang, and J. Sun, “Cooperative decisionmaking for cavs at unsignalized intersections: A marl approach with attention and hierarchical game priors,” IEEE Transactions on Intelligent Transportation Systems, 2024.

[31] F. Hairi, Z. Zhang, and J. Liu, “Sample and communication efficient fully decentralized marl policy evaluation via a new approach: Local td update,” arXiv preprint arXiv:2403.15935, 2024.

[32] T. D. Simao and M. T. Spaan, “Safe policy improvement with baseline bootstrapping in factored environments,” in Proceedings of the AAAI Conference on Artificial Intelligence, vol. 33, no. 01, pp. 4967–4974, 2019.

[33] K. Zhang, Z. Yang, H. Liu, T. Zhang, and T. Basar, “Fully decentralized multi-agent reinforcement learning with networked agents,” in International conference on machine learning, pp. 5872–5881. PMLR, 2018.

[34] Y. Du, C. Ma, Y. Liu, R. Lin, H. Dong, J. Wang, and Y. Yang, “Scalable model-based policy optimization for decentralized networked systems,” in 2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 9019–9026. IEEE, 2022.

[35] G. Sun, J. Xiao, J. Li, J. Wang, J. Kang, D. Niyato, and S. Mao, “Aerial reliable collaborative communications for terrestrial mobile users via evolutionary multi-objective deep reinforcement learning,” IEEE Transactions on Mobile Computing, vol. 24, no. 7, pp. 5731–5748, 2025.

[36] J. Li, G. Sun, L. Duan, and Q. Wu, “Multi-objective optimization for uav swarm-assisted iot with virtual antenna arrays,” IEEE Transactions on Mobile Computing, vol. 23, no. 5, pp. 4890–4907, 2024.

[37] G. Sun, L. He, Z. Sun, Q. Wu, S. Liang, J. Li, D. Niyato, and V. C. M. Leung, “Joint task offloading and resource allocation in aerial-terrestrial uav networks with edge and fog computing for post-disaster rescue,” IEEE Transactions on Mobile Computing, vol. 23, no. 9, pp. 8582–8600, 2024.

[38] R. Liang, B. Yang, Z. Yu, B. Guo, X. Cao, M. Debbah, H. V. Poor, and C. Yuen, “Diffsg: A generative solver for network optimization with diffusion model,” IEEE Communications Magazine, vol. 63, no. 6, pp. 16–24, 2025.

[39] R. Liang, B. Yang, P. Chen, X. Cao, Z. Yu, M. Debbah, D. Niyato, H. V. Poor, and C. Yuen, “Gdsg: Graph diffusion-based solution generator for optimization problems in mec networks,” IEEE Transactions on Mobile Computing, vol. 24, no. 10, pp. 10 264–10 277, 2025.

[40] D. Guo, S. Ji, Y. Yao, and C. Chen, “A decentralized path planning model based on deep reinforcement learning,” Computers and Electrical Engineering, vol. 117, p. 109276, 2024.

[41] X. Song, Y. Zhao, Z. Wu, Z. Yang, and J. Tang, “Joint trajectory and communication design for irs-assisted uav networks,” IEEE Wireless Communications Letters, vol. 11, no. 7, pp. 1538–1542, 2022.

VII. BIOGRAPHY SECTION  
![](images/055b92a450a25cf12e8cb388fcea679579bd47fe2a7cbe19442b6c3cff3447c8.jpg)  
Liangshun Wu (Member, IEEE) received the B.Eng. degree from Central South University, Changsha, China, in 2014, and the M.S. and Ph.D. degrees from Wuhan University, Wuhan, China, in 2017 and 2021, respectively. He was a Visiting Scholar with the University of Electro-Communications, Tokyo, Japan, in 2024. He is currently a postdoctoral researcher with Shanghai Jiao Tong University, Shanghai, China. His research interests include RIS/IRS/RHS, mobile edge computing, and vehicular networks.

![](images/bed200a662fec558f9a65e1ea94f96d357ce2fb3b0a33e1c4a80b2ef7fcf7121.jpg)

Jianbo Du (Senior Member, IEEE) received the Ph.D. degree in communication and information systems from Xidian University, Xi’an, Shaanxi, China, in 2018. She is an Associate Professor at Xi’an University of Posts and Telecommunications. She was a Visiting Scholar at Carleton University in 2019. With over 50 publications and 2,500+ citations, six of her papers are ESI Top 1% highly cited. Named among the world’s Top 2% scientists in 2022 and 2023. She has received multiple IEEE Excellent Reviewer awards.

![](images/65eafd57a7f532823131f1bcb5c3786c72e39f9baa0fc4cd3f71cc81e574c01f.jpg)

Junsuo Qu (Member, IEEE) received his B.S. in Telecommunication Engineering from Chongqing Institute of Posts & Telecommunications in 1991 and his M.S. in Communication and Information Systems from Xidian University in 1998. He is a Full Professor at the School of Automation, Xi’an University of Posts & Telecommunications, and Director of the Xi’an Key Laboratory of Advanced Control and Intelligent Process. His research interests include future communication architectures and Internet of Things.