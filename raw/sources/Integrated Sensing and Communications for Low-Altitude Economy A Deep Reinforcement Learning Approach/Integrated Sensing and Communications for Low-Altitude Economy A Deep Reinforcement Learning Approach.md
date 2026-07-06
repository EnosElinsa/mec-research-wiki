# Integrated Sensing and Communications for Low-Altitude Economy: A Deep Reinforcement Learning Approach

Xiaowen Ye , Yuyi Mao , Senior Member, IEEE, Xianghao Yu , Senior Member, IEEE, Shu Sun , Senior Member, IEEE, Liqun Fu , Senior Member, IEEE, and Jie Xu , Fellow, IEEE

Abstract—This paper studies an integrated sensing and communications (ISAC) system for low-altitude economy (LAE), where a ground base station (GBS) provides communication and navigation services for authorized unmanned aerial vehicles (UAVs), while sensing the low-altitude airspace to monitor the unauthorized mobile target. The expected communication sumrate over a given flight period is maximized by jointly optimizing the beamforming at the GBS and UAVs’ trajectories, subject to the constraints on the average signal-to-noise ratio requirement for sensing, the flight mission and collision avoidance of UAVs, as well as the maximum transmit power at the GBS. Typically, this is a sequential decision-making problem with the given flight mission. Thus, we transform it to a specific Markov decision process (MDP) model called episode task. Based on this modeling, we propose a novel LAE-oriented ISAC scheme, referred to as Deep LAE-ISAC (DeepLSC), by leveraging the deep reinforcement learning (DRL) technique. In DeepLSC, a reward function and a new action selection policy termed constrained noise-exploration policy are judiciously designed to fulfill various constraints. To enable efficient learning in episode tasks, we develop a hierarchical experience replay mechanism, where the gist is to employ all experiences generated within each

Jie Xu is with the School of Science and Engineering (SSE), Shenzhen Future Network of Intelligence Institute (FNii-Shenzhen), and Guangdong Provincial Key Laboratory of Future Networks of Intelligence, The Chinese University of Hong Kong, Shenzhen, Guangdong 518172, China (e-mail: xujie@cuhk.edu.cn).

Digital Object Identifier 10.1109/TWC.2025.3583950 episode to jointly train the neural network. Besides, to enhance the convergence speed of DeepLSC, a symmetric experience augmentation mechanism, which simultaneously permutes the indexes of all variables to enrich available experience sets, is proposed. Simulation results demonstrate that compared with benchmarks, DeepLSC yields a higher sum-rate while meeting the preset constraints, achieves faster convergence, and is more robust against different settings.

Index Terms—Low-altitude economy (LAE), integrated sensing and communications (ISAC), joint beamforming and trajectory design, deep reinforcement learning (DRL).

## I. INTRODUCTION

OW-ALTITUDE economy (LAE), composed of various manned aircraft, such as unmanned aerial vehicles (UAVs) and electric vertical take-off and landing (eVTOL), has gained widespread attention from academia and industry [1]. It is expected that LAE could support a wide variety of important applications, including but not limited to transportation, environmental monitoring, tourism, and agriculture [2]. However, the successful implementation of LAE requires the strictly safe operation (e.g., collision-free) of all aircraft, especially in the presence of massive aircraft and unauthorized targets [3]. Therefore, it is imperative to provide seamless communication and navigation for authorized aircraft, as well as ubiquitous surveillance of unauthorized targets in the lowaltitude airspace.

One possible solution that could facilitate the implementation of LAE is to jointly adopt wireless communications and radar sensing technologies. Conventionally, these two technologies are designed and implemented independently. This, however, results in low spectrum utilization and expensive hardware overhead. Fortunately, integrated sensing and communications (ISAC), a key technique for next-generation wireless networks, is capable of simultaneously performing wireless communications and radar sensing based on the common spectrum resource and hardware infrastructures [4]. With ISAC, the ground base station (GBS) provides communication and navigation services for authorized aircraft, while sensing the low-altitude airspace to monitor unauthorized targets.

## A. Related Work

Currently, there have been substantial bodies of works studying the integration of aircraft (specifically UAVs) and

ISAC systems, which can be divided into two main paradigms according to the role that UAVs play [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], [31], [32], [33], [34], [35]. The first paradigm is referred to as UAV-assisted ISAC services, where each UAV operates as a new aerial platform (e.g., aerial base station or relay) to serve ground users. For example, towards the goal of minimizing the age of information of sensed data, a joint extremum principles and dynamic programming scheme was proposed in [5] to optimize the UAV power and trajectory, whereas in [6], a successive convex approximation (SCA) iterative method was used to refine the UAV trajectory and time allocation for both communication and sensing. These two works, however, were merely concerned about the communication performance, while ignoring the sensing requirement. By contrast, the works [7], [8], [9], [10], [11] considered both simultaneously. Specifically, in [7], Wang et al. investigated a dual-function multi-UAV wireless network, in which the sum-rate was maximized by jointly optimizing the UAV location, transmit power, and user association under the Cramer-Rao bound constraint.´ In [8], Chang et al. proposed a joint scheduling strategy for control, communication, and sensing in millimeter-wave UAV networks, such that the communication and sensing requirements can be met while maintaining good control performance. By jointly employing the alternating optimization and SCA method, the authors of [9] proposed a joint UAV deployment and power control scheme to maximize the minimum detection probability, whilst the authors of [10] optimized the deployment and joint communication and sensing precoder to balance communication rate and sensing accuracy. Besides, the potential of UAVs for physical layer security provisioning in ISAC systems was explored in [11].

The aforementioned research, however, mainly focused on the ISAC in quasi-static UAV scenarios, without exploiting the controllable mobility over the three-dimensional (3D) space. To explore the advantages of UAV mobility, literature [12], [13], [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], [24] studied the UAV trajectory optimization for ISAC applications. To be specific, by optimizing the UAV trajectory, the real-time secrecy rate was maximized in [12], while the UAV propulsion consumption was minimized in [13]. Furthermore, in [14], [15], [16], [17], [18], [19], [20], [21], [22], [23], and [24], other variables are jointly optimized with the UAV trajectory, e.g., UAV transmit power and user scheduling [14], [15], [16], [17], bandwidth allocation for users [18], UAV-user association [19], UAV transmit beamforming [20], [21], [22], [23], and offloading task size [24]. These above works were dedicated to the case with a single UAV and thus exempted from the UAV collision-avoidance constraint. On the contrary, investigations [25] and [26] focused on a multi-UAV-assisted ISAC network, where the trajectory of individual UAVs and their association with users are jointly optimized subject to the minimum collision avoidance distance. In addition, to circumvent the high computational complexity and poor adaptability of conventional optimization methods, several intelligent UAVaided ISAC schemes were developed in [27], [28], [29], [30], [31], [32], and [33].

The inherent limitation of the first paradigm is not being applicable to terrestrial ISAC oriented towards LAE, where authorized UAVs (as communication users) with missions (e.g., cargo delivery) and unauthorized targets (as sensing targets) are located at low altitudes in the 3D space. Instead, the second paradigm, which focuses on the use of GBS to provide aircraft with ISAC services, aligns better with LAE-oriented ISAC. Currently, there are few studies on this paradigm [34], [35]. In particular, the authors of [34] considered a system with one GBS and multiple UAVs, where a novel dual identity association-based ISAC approach was designed to enable fast and accurate beamforming towards different UAVs. Unlike [34], the authors of [35] studied a networked ISAC system, where multiple GBSs cooperatively transmit unified ISAC signals to communicate with multiple authorized UAVs and concurrently detect unauthorized targets. In prior works, the unauthorized target is presumed to be static, and the alternating algorithms that focus on instantaneous optimization problems are adopted to optimize different groups of variables. In practical LAE-oriented ISAC systems, however, (i) the locations of unauthorized targets are highly dynamic; (ii) the channel state information (CSI) is time-correlated since the next locations of the target and UAVs depend on their current locations; and (iii) the beamforming and trajectory are jointly optimized subject to UAVs’ flight missions that last for a long period. As a result, the LAE-oriented ISAC problem is typically a long-term optimization problem, in which all variables should be jointly optimized with respect to the average system performance during the flight mission.

Such a problem can be transformed and solved under the Markov decision process (MDP) model, in which an agent continuously optimizes its decisions towards the given long-term objective. Generally, an efficient solution for MDP can be derived through dynamic programming algorithms, if the accurate state transition (e.g., the CSI transition) of the system is available [36]. However, in practical LAE-oriented ISAC systems, the mobility model of the target is difficult to obtain, in the sense that the state transition of the system is unknown. Fortunately, model-free deep reinforcement learning (DRL) excels at finding an efficient strategy for MDP in unknown environments, through a large number of trial-anderror interactions and reward-decision iterations [37]. In this regard, DRL is a promising candidate for solving long-term optimization problems in LAE oriented-ISAC systems. So far, DRL has shown its powerful capability in solving a wide range of sequential decision-making problems, e.g., robot control, game playing, and wireless communications [38]. To the best of our knowledge, DRL has not been explored yet in designing LAE-oriented ISAC schemes.

## B. Contributions

In this paper, we investigate an LAE-oriented ISAC system with the objective of maximizing the expected communication sum-rate of all UAVs over a given flight period, by jointly optimizing the GBS’s beamforming and authorized UAVs’ trajectories. In addition, the constraints, including the average sensing signal-to-noise ratio (SNR) requirement for monitoring the mobile target, the UAVs’ flight missions, the UAV collision avoidance, and the GBS’s maximum transmit power, are considered. Overall, the main contributions of this paper are summarized below:

1) A problem is formulated as a specific MDP model termed episode task [36] to jointly optimize the GBS’s beamforming and $\mathrm { U A V s } '$ trajectories, where each flight period is considered as an episode and the flight mission corresponds to the episode task. To find an efficient solution, we propose an ISAC scheme capable of supporting LAE, referred to as Deep LAE-ISAC (DeepLSC), by exploiting the DRL technique. The underpinning algorithm in DeepLSC is deep deterministic policy gradient (DDPG) [39], since the formulated problem involves continuous control variables. The salient advantages of DeepLSC are that it (i) does not require the prior mobility information of the target and (ii) well caters the long-term optimization objective of the LAE-oriented ISAC system.

2) A new action selection policy, termed constrained noise-exploration policy, is developed for DeepLSC to guarantee the flight mission and maximum power constraints. The gist is to (i) introduce a scaling factor to refine the beamforming from the conventional noise-exploration policy [39] and (ii) decide whether to follow the trajectory decision of the conventional noiseexploration policy or choose straight flight based on the real-time locations of UAVs. In addition, we judiciously design a reward function for action evaluation, which incorporates the communication sum-rate, average sensing SNR requirement, and collision avoidance into the learning process.

3) A new hierarchical experience replay mechanism is proposed for DeepLSC to train the deep neural network (DNN). Specifically, in the traditional experience replay mechanism [40], since different experiences generated within a specific episode are collected and utilized in a separate manner, they cannot be guaranteed to appear together during training. DeepLSC, however, is tailored for episode tasks. To efficiently learn from the episode task, the hierarchical experience replay mechanism employs the experience sets, each containing all experiences within an episode, to jointly train the DNN.

4) We devise a symmetric experience augmentation mechanism to promote the convergence speed of DeepLSC. To be specific, DeepLSC is an online learning scheme, in the sense that the agent (i.e., the GBS) needs a lot of trial and error with the environment to generate sufficient experiences for training. Consequently, an efficient joint beamforming and trajectory policy takes a long time to learn. To circumvent this issue, the symmetric experience replay mechanism generates more new experience sets by simultaneously permuting the indexes of all variables, based on a prior experience set.

5) Extensive experimental results show that DeepLSC outperforms various schemes including the DeepLSC-CNE (i.e., DeepLSC with the conventional noise-exploration policy [39]), DeepLSC-CER (i.e., DeepLSC with the conventional experience replay mechanism [40]), and

<table><tr><td rowspan=1 colspan=1> $\overline { { N } }$ </td><td rowspan=1 colspan=1>Number of antennas at BS</td></tr><tr><td rowspan=1 colspan=1> $\overline { { M / M } }$ </td><td rowspan=1 colspan=1>Number/Set of UAVs</td></tr><tr><td rowspan=1 colspan=1> $T$ </td><td rowspan=1 colspan=1>Number of time slots within a flight period</td></tr><tr><td rowspan=1 colspan=1> ${ \bf b } / { \bf g } / { \bf u } _ { m }$ </td><td rowspan=1 colspan=1>Horizontal location of the GBS/target/UAV m</td></tr><tr><td rowspan=1 colspan=1> $H _ { \mathrm { T a r } } / H _ { m }$ </td><td rowspan=1 colspan=1>Height of the target/UAV m</td></tr><tr><td rowspan=1 colspan=1> $\phi / \varphi$ </td><td rowspan=1 colspan=1>Moving azimuth/elevation angle of the target</td></tr><tr><td rowspan=1 colspan=1> $\psi _ { m }$ </td><td rowspan=1 colspan=1>AoD from the GBS to UAV m</td></tr><tr><td rowspan=1 colspan=1> ${ \bf H } _ { \mathrm { s } } / { \bf H } _ { \mathrm { c } }$ </td><td rowspan=1 colspan=1>Communication/Sensing CSI</td></tr><tr><td rowspan=1 colspan=1> $\varsigma _ { m }$ </td><td rowspan=1 colspan=1>Path loss exponent</td></tr><tr><td rowspan=1 colspan=1> ${ \mathbf W } _ { \mathrm { s } } / { \mathbf W } _ { \mathrm { c } }$ </td><td rowspan=1 colspan=1>Communication/Sensing beamforming</td></tr><tr><td rowspan=1 colspan=1> $\mathrm { S N R } _ { \mathrm { T a r } } / \mathrm { T } _ { \mathrm { m i n } }$ </td><td rowspan=1 colspan=1>Sensing SNR/Sensing SNR requirement</td></tr><tr><td rowspan=1 colspan=1> $R _ { \mathrm { t o t a l } }$ </td><td rowspan=1 colspan=1>Communication sum-rate</td></tr><tr><td rowspan=1 colspan=1> $\overline { { Q ( \mathbf { S } , \mathbf { A } ) } }$ </td><td rowspan=1 colspan=1>Action-value function</td></tr><tr><td rowspan=1 colspan=1> ${ \bf S } ( t ) / { \bf A } ( t ) / r ( t ) / e ( t )$ </td><td rowspan=1 colspan=1>State/Action/Reward/Experience</td></tr><tr><td rowspan=1 colspan=1> $\delta _ { 1 } / \delta _ { 2 }$ </td><td rowspan=1 colspan=1>Reward coefficient</td></tr><tr><td rowspan=1 colspan=1> $\pi _ { \mathrm { a } } / \pi _ { \mathrm { a } } ^ { - }$ </td><td rowspan=1 colspan=1>Policy of the eval-actor/target-actor</td></tr><tr><td rowspan=1 colspan=1> $\Theta _ { \mathrm { a } } / \Theta _ { \mathrm { c } }$ </td><td rowspan=1 colspan=1>Parameter of the eval-actor/eval-critic</td></tr><tr><td rowspan=1 colspan=1> $\chi _ { \mathrm { a } } / \chi _ { \mathrm { c } }$ </td><td rowspan=1 colspan=1>Update coefficient of the target-actor/target-critic</td></tr><tr><td rowspan=1 colspan=1> $\kappa / \sigma _ { \mathrm { m i n } }$ </td><td rowspan=1 colspan=1>Initial exploration variance/Decay factor</td></tr><tr><td rowspan=1 colspan=1>€</td><td rowspan=1 colspan=1>Scaling factor</td></tr><tr><td rowspan=1 colspan=1> $\alpha _ { \mathrm { a } } / \alpha _ { \mathrm { c } }$ </td><td rowspan=1 colspan=1>Learning rate of the eval-actor/eval-target</td></tr><tr><td rowspan=1 colspan=1> $D / N _ { \mathrm { e } }$ </td><td rowspan=1 colspan=1>Size of the experience buffer/mini-batch</td></tr><tr><td rowspan=1 colspan=1>Ω/r</td><td rowspan=1 colspan=1>Permutation/Symmetric group</td></tr><tr><td rowspan=1 colspan=1>ζ</td><td rowspan=1 colspan=1>Augmentation factor</td></tr></table>

MAIN NOTATIONS OF THIS PAPER  
TABLE I

AC2 (i.e., the actor-critic algorithm [36] with the constrained noise-exploration policy), in terms of both communication and sensing performance. Compared with DeepLSC-w (i.e., DeepLSC without symmetric experience augmentation), DeepLSC converges faster. Furthermore, under different simulation setups, DeepLSC is more robust than these baselines.

Notations: Vectors (matrices) are denoted by boldface lower (upper) case letters, $\mathbb { C } ^ { N \times M }$ represents the space of $N { \times } M$ complex matrices, | · | represents the absolute value, || · ||<sub>2</sub> represents the 2-norm, <sup>E</sup>[·] represents the statistical expectation, while $\operatorname { T r } ( \cdot ) , ( \cdot ) ^ { T }$ , and $( \cdot ) ^ { \hat { H } }$ represent the trace, transpose, and conjugate transpose, respectively. blueFor reference, we list the main notations of this paper in TABLE I.

## II. SYSTEM MODEL

Consider an LAE-oriented ISAC system shown in Fig. 1, where one GBS equipped with N transmit/receive-antennas serves M single-antenna authorized UAVs for downlink communications and simultaneously detects a low-altitude target (e.g., unauthorized UAV). The location of the GBS is represented by the 3D Cartesian coordinate (b, 0) with $\mathbf { b } = [ \hat { x } , \hat { y } ]$ denoting the horizontal coordinate, and the location of the target is $( \mathbf { g } , H _ { \mathrm { T a r } } )$ , wherein $\mathbf { g } = [ \tilde { x } , \tilde { y } ]$ and $H _ { \mathrm { T a r } } > 0$ denote the horizontal and vertical coordinates, respectively. The UAVs are indexed by $m \in \mathcal { M } = \{ 1 , 2 , \cdots , M \}$ , and each UAV m flies at a pre-assigned altitude $H _ { m }$ with the mission of transporting cargo from a source to a destination within a given time duration of $\Delta _ { \mathrm { T } }$ . In other words, the initial and final locations of UAV m are predetermined as $\left( \mathbf { u } _ { m } ^ { \mathrm { I } } , H _ { m } \right)$ and $\bigl ( \mathbf { u } _ { m } ^ { \mathrm { F } } , H _ { m } \bigr )$ respectively, wherein $\mathbf { u } _ { m } ^ { \mathrm { I } } = [ x _ { m } ^ { \mathrm { I } } , y _ { m } ^ { \mathrm { I } } ]$ and $\mathbf { u } _ { m } ^ { \mathrm { F } } = [ x _ { m } ^ { \mathrm { F } } , y _ { m } ^ { \mathrm { F } } ]$

![](images/c6cffc0d4a44f135c57944a7a2ff05845507403d35d43ebfb3c594894b34f637.jpg)  
Fig. 1. LAE-oriented ISAC systems.

## A. UAV/Target Trajectory Model

We discretize the duration $\Delta _ { \mathrm { T } }$ into T time slots, indexed by $t \in \mathcal T = \{ 1 , 2 , \cdot \cdot \cdot , T \}$ . The slot duration $\Delta _ { \mathrm { t } } = \Delta _ { \mathrm { T } } / T$ is sufficiently small, such that the locations of the target and UAVs can be assumed as unchanged within each time slot.

1) UAV Flight Model: Within a specific time period $\Delta _ { \mathrm { T } } ,$ the trajectory of UAV m is a $( T ~ + ~ 1 )$ -length sequence, i.e., $\{ ( \mathbf { u } _ { m } ^ { \mathrm { { I } } } , H _ { m } ) , ( \mathbf { u } _ { m } ( t ) , H _ { m } ) | t \ = \ 1 , 2 , \cdot \cdot \cdot , \bar { T } \}$ with $\mathbf { u } _ { m } ( t ) \triangleq \ [ x _ { m } ( t ) , \ y _ { m } ( t ) ]$ . We assume that UAV m flies at a constant speed $v _ { m } .$ . Thus, its flight distance in one time slot is given as $v _ { m } \Delta _ { t }$ , leading to the following constraint:

$$
\| \mathbf { u } _ { m } ( t + 1 ) - \mathbf { u } _ { m } ( t ) \| _ { 2 } = v _ { m } \Delta _ { \mathrm { t } } , \ \forall m \in \mathcal { M } , t \in \mathcal { T } .\tag{1}
$$

In addition, the initial and final locations of M UAVs (i.e., the flight mission constraints) are given by

$$
\begin{array} { r } { \mathbf { u } _ { m } ( 0 ) = \mathbf { u } _ { m } ^ { \mathrm { I } } \mathrm { a n d } \mathbf { u } _ { m } ( T ) = \mathbf { u } _ { m } ^ { \mathrm { F } } , \forall m \in \mathcal { M } . } \end{array}\tag{2}
$$

To avoid collision among different UAVs, the following collision avoidance constraints are enforced:

$$
\begin{array} { r l r } & { } & { \left\| { \bf { u } } _ { m } ( t ) - { \bf { u } } _ { i } ( t ) \right\| _ { 2 } ^ { 2 } + ( H _ { m } - H _ { i } ) ^ { 2 } \geq D _ { \operatorname* { m i n } } ^ { 2 } , } \\ & { } & { \forall m , i \in \mathcal { M } , m \neq i , t \in \mathcal { T } , } \end{array}\tag{3}
$$

where $D _ { \mathrm { m i n } }$ denotes the minimum allowed distance between any two UAVs. Similarly, each UAV also needs to maintain a minimum distance from the target to avoid collision, i.e.,

$$
\begin{array} { r } { \left\| \mathbf { u } _ { m } ( t ) - \mathbf { g } ( t ) \right\| _ { 2 } ^ { 2 } + ( H _ { m } - H _ { \mathrm { T a r } } ( t ) ) ^ { 2 } \geq D _ { \operatorname* { m i n } } ^ { 2 } , } \\ { \forall m \in \mathcal { M } , t \in \mathcal { T } . \qquad } \end{array}\tag{4}
$$

2) Target Mobility Model: For simplify, we assume that the target moves at a constant speed $v _ { \mathrm { T a r } }$ and its flight distance within one time slot is $v _ { \mathrm { T a r } } \Delta _ { \mathrm { t } }$ . To better model the mobility of a realistic target, a Gauss-Markov process is introduced to capture the temporal correlation of the movement direction [41]. Let $\phi ( t )$ and $\varphi ( t )$ denote the azimuth and elevation angles at which the target moves at time slot t, respectively. They are modeled as

$$
\begin{array} { r } { \int \phi ( t ) = \mu _ { \mathrm { a } } \phi ( t - 1 ) + ( 1 - \mu _ { \mathrm { a } } ) \xi _ { \mathrm { a } } + \sqrt { 1 - \mu _ { \mathrm { a } } ^ { 2 } } \hat { \phi } ( t ) , } \\ { \varphi ( t ) = \mu _ { \mathrm { e } } \varphi ( t - 1 ) + ( 1 - \mu _ { \mathrm { e } } ) \xi _ { \mathrm { e } } + \sqrt { 1 - \mu _ { \mathrm { e } } } ^ { 2 } \hat { \varphi } ( t ) , } \end{array}\tag{5}
$$

where $\mu _ { \mathrm { a } } \in [ 0 , 1 ]$ and $\mu _ { \mathrm { e } } \in [ 0 , 1 ]$ are the time correlation coefficients, modulating the degree of temporal dependency. For example, $\mu _ { \mathrm { a } } = 0$ indicates that the target moves at a fully random azimuth angle, while $\mu _ { \mathrm { a } } = 1$ indicates that the horizontal movement direction is unchanged. Parameters $\xi _ { \mathrm { a } }$ and $\xi _ { \mathrm { e } }$ are asymptotic means of $\phi ( t )$ and $\varphi ( t )$ , respectively, as t→∞. Parameters $\hat { \phi } ( t )$ and $\hat { \varphi } ( t )$ are independent, uncorrelated, and stationary Gaussian processes with $\mathcal { N } ( 0 , \sigma _ { \phi } ^ { 2 } )$ and $\mathcal { N } ( 0 , \sigma _ { \varphi } ^ { 2 } )$ respectively, wherein $\sigma _ { \phi }$ and $\sigma _ { \varphi }$ correspond to the asymptotic standard deviations.

Hence, given φ(t) and $\varphi ( t )$ , the location of the target at time slot t + 1 can be obtained as

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \mathbf { g } ( t + 1 ) = \mathbf { g } ( t ) + v _ { \mathrm { T a r } } \Delta _ { \mathrm { t } } \mathrm { c o s } \left( \varphi ( t ) \right) \left[ \cos \left( \phi ( t ) \right) , \sin \left( \phi ( t ) \right) \right] , } \\ { H _ { \mathrm { T a r } } ( t + 1 ) = H _ { \mathrm { T a r } } ( t ) + v _ { \mathrm { T a r } } \Delta _ { \mathrm { t } } \mathrm { s i n } \left( \varphi ( t ) \right) . } \end{array} \right. } \end{array}\tag{6}
$$

## B. Channel Model

Denote $\mathbf { h } _ { \mathrm { s } } ( t ) \in \mathbb { C } ^ { N \times 1 }$ by the channel vector between the GBS and the target at time slot t. The bidirectional channel matrix that the signal experiences from forward transmission to echo can be represented as H $\mathbf { \Phi } _ { 3 } ( t ) = \mathbf { h } _ { \mathrm { s } } ( t ) \mathbf { h } _ { \mathrm { s } } ^ { T } ( t ) \in \mathbb { C } ^ { N \times N }$ . Furthermore, let $\mathbf { H } _ { \mathrm { c } } ( t ) \ = \ [ \mathbf { h } _ { 1 } ( t ) , \mathbf { h } _ { 2 } ( t ) , \cdots , \mathbf { h } _ { M } ( t ) ] \in \mathbb { C } ^ { N \times M }$ denote the channel matrix between the GBS and all UAVs at time slot t, wherein $\mathbf { h } _ { m } ( t ) \in \mathbb { C } ^ { N \times 1 }$ is the channel vector between the GBS and UAV m.

Due to the relatively high altitude of the target and UAVs, there generally exists a strong line-of-light (LoS) link between the GBS and them. As such, the air-ground communication links are dominated by the LoS channel. For example, $ { \mathbf { h } } _ { m } ( t ) , \forall m \in \mathcal { M }$ is represented as

$$
\mathbf { h } _ { m } ( t ) = \sqrt { \omega _ { m } ( t ) } \mathbf { c } \left( \psi _ { m } ( t ) \right) ,\tag{7}
$$

where

$$
\omega _ { m } ( t ) = L _ { 0 } \frac { D _ { 0 } } { \big ( \big \| \mathbf { b } - \mathbf { u } _ { m } ( t ) \big \| _ { 2 } ^ { 2 } + H _ { m } ^ { 2 } \big ) \varsigma _ { m } }
$$

is the path loss with $L _ { 0 }$ as the path loss constant at reference distance $D _ { 0 } .$ , and $\varsigma _ { m }$ as the path loss exponent. Furthermore, $\mathbf c \left( \psi _ { m } ( t ) \right) = \Big [ 1 , e ^ { \jmath 2 \pi \frac { d } { \lambda } \cos \psi _ { m } ( t ) } , \cdot \cdot \cdot , e ^ { \jmath 2 \pi \frac { d } { \lambda } ( N - 1 ) \cos \psi _ { m } ( t ) } \Big ] ^ { T }$ is the steering vector with $\psi _ { m } ( t )$ being the angle of departure (AoD) at the GBS, given by

$$
\psi _ { m } ( t ) = \operatorname { a r c c o s } \frac { H _ { m } } { \sqrt { \left\| \mathbf { b } - \mathbf { u } _ { m } ( t ) \right\| _ { 2 } ^ { 2 } + H _ { m } ^ { 2 } } } .\tag{8}
$$

A similar channel model is adopted for ${ \bf h } _ { \mathrm { s } } ( t )$

## C. Signal Model

In each time slot $t ,$ the transmit signal of the GBS is a weighted sum of communication symbols and radar probing signals [4], which is expressed as

$$
\mathbf { x } ( t ) = \mathbf { W } _ { \mathrm { c } } ( t ) \mathbf { v } _ { \mathrm { c } } ( t ) + \mathbf { W } _ { \mathrm { s } } ( t ) \mathbf { v } _ { \mathrm { s } } ( t ) ,\tag{9}
$$

where $\mathbf { v } _ { \mathrm { c } } ( t ) \in \mathbb { C } ^ { M \times 1 }$ is the communication symbol with $\mathbb { E } \{ { \bf v } _ { \mathrm { c } } ( t ) { \bf v } _ { \mathrm { c } } ^ { \dot { H } } ( t ) \} ~ = ~ { \bf I } _ { M } , ~ { \bf v } _ { \mathrm { s } } ( t ) \in \mathbb { C } ^ { N \times 1 }$ is the radar probing signal with $\begin{array} { r } { \vec { \mathbb { E } } \{ { \bf v } _ { \mathrm { s } } ( t ) { \bf v } _ { \mathrm { s } } ^ { H } ( t ) \} ~ = ~ { \bf I } _ { N } , ~ { \bf W } _ { \mathrm { c } } ( t ) \in \mathbb { C } ^ { N \times M } } \end{array}$ is the communication precoding matrix, and $\mathbf { W } _ { \mathrm { s } } ( t ) \in \mathbb { C } ^ { N \times N }$ is the radar precoding matrix. In addition, $\mathbf { v } _ { \mathrm { c } } ( t )$ and ${ \bf v } _ { \mathrm { s } } ( t )$ are statistically independent, leading to $\mathbb { E } ( \mathbf { v } _ { \mathrm { c } } ( t ) \mathbf { v } _ { \mathrm { s } } ^ { H } ( t ) ) = \mathbf { 0 }$ . Denote $\mathbf { W } ( t ) { \triangleq } [ \mathbf { W } _ { \mathrm { c } } ( t ) , \mathbf { W } _ { \mathrm { s } } ( t ) ]$ and $\mathbf { v } ( t ) \triangleq \left[ \mathbf { v } _ { \mathrm { c } } ^ { T } ( t ) , \mathbf { v } _ { \mathrm { s } } ^ { T } ( t ) \right] ^ { T }$ . Thus, we have $\mathbf { x } ( t ) = \mathbf { W } ( t ) \mathbf { v } ( t )$ , and the power constraint is given by

$$
\begin{array} { r } { \mathrm { T r } \left( \mathbf { W } _ { \mathrm { c } } ^ { H } ( t ) \mathbf { W } _ { \mathrm { c } } ( t ) \right) + \mathrm { T r } \left( \mathbf { W } _ { \mathrm { s } } ^ { H } ( t ) \mathbf { W } _ { \mathrm { s } } ( t ) \right) \leq P _ { \operatorname* { m a x } } , \forall t \in \mathcal { T } . } \end{array}\tag{10}
$$

1) Communication Model: With the transmit signal ${ \bf x } ( t )$ the received signal at UAV m is expressed as $y _ { m } ( t ) \ =$ $\mathbf { h } _ { m } ^ { T } ( t ) \mathbf { x } ( t ) + n _ { m } \bar { ( } t )$ , where $n _ { m } ( t ) \sim \mathcal { C N } ( 0 , \sigma _ { m } ^ { 2 } )$ is the additive white Gaussian noise (AWGN), and $\sigma _ { \mathrm { m } } ^ { 2 }$ is the noise power. As a result, the communication signal-to-interference-and-noise ratio (SINR) at UAV m is given by

$$
\mathrm { S I N R } _ { m } ( t ) = \frac { \big \vert \mathbf { h } _ { m } ^ { T } ( t ) \mathbf { w } _ { m } ( t ) \big \vert ^ { 2 } } { \displaystyle \sum _ { k = 1 , k \neq m } ^ { N + M } \big \vert \mathbf { h } _ { m } ^ { T } ( t ) \mathbf { w } _ { k } ( t ) \big \vert ^ { 2 } + \sigma _ { m } ^ { 2 } } ,\tag{11}
$$

where ${ \bf w } _ { m }$ is the m-th column of W. Accordingly, the sum-rate of all UAVs can be calculated by

$$
\mathbf { R } _ { \mathrm { t o t a l } } ( t ) = \sum _ { m = 1 } ^ { M } \log _ { 2 } \left( 1 + \mathbf { S I N R } _ { m } ( t ) \right) .\tag{12}
$$

## D. Sensing Model

As shown in Fig. 1, the radar probing signal is reflected by the target to GBS via the direct and reflected/refracted links. Thus, the echo signal from the target to GBS is expressed as ${ \bf y } _ { \mathrm { s } } ( t ) = { \bf H } _ { \mathrm { s } } ( t ) { \bf x } ( t ) + { \bf n } _ { \mathrm { B } } ( t )$ , wherein ${ \bf n } _ { \mathrm { B } } ( t ) \sim \mathcal { C N } ( { \bf 0 } _ { N } , \ \sigma _ { \boldsymbol { \mathrm { b } } } ^ { 2 } { \bf I } _ { N } )$ is the AWGN, and $\sigma _ { \mathrm { b } } ^ { 2 }$ is the noise power. Furthermore, the sensing SNR of the target is given by

$$
\begin{array} { r l } & { \mathbf { S N R } _ { \mathrm { T a r } } ( t ) = \frac { \mathbb { E } \left\{ | \mathbf { H } _ { \mathrm { s } } ( t ) \mathbf { W } ( t ) \mathbf { v } ( t ) | ^ { 2 } \right\} } { \sigma _ { \mathrm { b } } ^ { 2 } } } \\ & { \qquad = \frac { \mathrm { T r } \left( \mathbf { W } ^ { H } ( t ) \mathbf { H } _ { \mathrm { s } } ^ { H } ( t ) \mathbf { H } _ { \mathrm { s } } ( t ) \mathbf { W } ( t ) \right) } { \sigma _ { \mathrm { b } } ^ { 2 } } . } \end{array}\tag{13}
$$

## III. PROBLEM FORMULATION AND TRANSFORMATION

This section formulates the joint beamforming and trajectory optimization problem as a constrained sequential decision problem. Then, it is transformed to an unconstrained problem with a judiciously designed reward function.

## A. Problem Formulation

Our objective is to maximize the expected sum-rate of all UAVs over T time slots while satisfying the sensing SNR requirement, flight mission, collision avoidance, and maximum transmit power constraints. The communication beamforming ${ \bf W } _ { \mathrm { c } } ( t )$ , sensing beamforming $\mathbf { W } _ { \mathrm { s } } ( t )$ , and trajectory ${ \bf u } _ { m } ( t )$ of each UAV are jointly optimized. Mathematically, this optimization problem is formulated as

$$
\operatorname* { m a x } _ { \mathbf { W } _ { \mathrm { c } } ( t ) , \mathbf { W } _ { \mathrm { s } } ( t ) , \mathbf { u } _ { m } ( t ) } \mathbb { E } \left[ \sum _ { { t = 1 } } ^ { T } { \mathbf { R } } _ { \mathrm { t o t a l } } ( t ) \right]\tag{14a}
$$

$$
{ \mathrm { s . t . ~ } } ( 1 ) , ( 2 ) , ( 3 ) , ( 4 ) , ( 6 ) ,\tag{14b}
$$

$$
\mathbb { E } \left[ \frac { 1 } { T } \sum _ { t = 1 } ^ { T } \mathbf { S N R } _ { \mathrm { T a r } } ( t ) \right] \geq \Gamma _ { \mathrm { m i n } } ,\tag{14c}
$$

$$
\begin{array} { r l r } & { \mathrm { T r } \left( \mathbf { W } _ { \mathrm { c } } ^ { H } ( t ) \mathbf { W } _ { \mathrm { c } } ( t ) \right) + \mathrm { T r } \left( \mathbf { W } _ { \mathrm { s } } ^ { H } ( t ) \mathbf { W } _ { \mathrm { s } } ( t ) \right) } & { } \\ & { \leq P _ { \mathrm { m a x } } , \forall t \in \mathcal { T } , } & { ( 1 } \end{array}\tag{4d}
$$

with the expectation in (14a) taken over varying target mobility, which is unknown to the GBS. Besides, constraint (14b) specifies the flight constraints of the target and UAVs; constraint (14c) guarantees the average SNR requirement $\Gamma _ { \mathrm { m i n } }$ for sensing the target [3]; and constraint (14d) limits the transmit power of the GBS to $P _ { \mathrm { m a x } }$

Typically, problem (14) is a sequential decision-making problem, which can be transformed and solved under the MDP model [36]. This corresponds to one particular MDP form, referred to as episode task [36], where the task ends in a terminal status (i.e., the final location of the UAV) that separates the agent-environment interactions into episodes with each containing T time slots. Different episodes are independent of each other, and a new episode will start from the starting status (i.e., the initial location of the UAV) after each episode ends. Besides, within each episode, the agent has to satisfy the preset constraints (14b)–(14d). Thus, problem (14) is actually a constrained episode task. Generally, an efficient solution that can handle this problem is hard to derive [36], which therefore motivates us to transform problem (14) into an unconstrained MDP problem.

## B. Unconstrained MDP Transformation

We define the basic MDP elements, including agent, environment, action, state, transition probability, and reward function, as follows.

1) Agent and Environment O: The GBS is considered as the agent, while the target, UAVs, and wireless channels are treated as the environment. In each time slot, the GBS first decides an efficient joint beamforming and trajectory strategy. Afterward, it performs the communication beamforming to provide data transmission and navigation for all UAVs, while monitoring the mobile target via the sensing beamforming.

2) Action Space A: The action space A is composed of all possible actions that could be potentially executed by the agent. In the light of (14), the agent needs to decide three types of sub-actions, including the communication beamforming ${ \bf W } _ { \mathrm { c } } ( t )$ , the sensing beamforming $\mathbf { W } _ { \mathrm { s } } ( t )$ and all UAVs’ movement directions ${ \bf a } _ { \mathrm { u } } ( t )$ , in each time slot. Specifically, the sub-action ${ \bf a } _ { \mathrm { u } } ( t )$ is represented as $[ a _ { \mathrm { u } , 1 } ( t ) , a _ { \mathrm { u } , 2 } ( t ) , \ \cdot \cdot \cdot , a _ { \mathrm { u } , M } ( t ) ]$ , where $a _ { \mathrm { u } , m } ( t )$ is the movement direction of UAV m at time slot t. With $\boldsymbol { a } _ { \mathrm { u } , m } ( t )$ , the horizontal location of UAV m at time slot t+1 becomes ${ \bf u } _ { m } ( t +$ $1 ) = [ x _ { m } ( t ) + v _ { m } \Delta _ { \mathrm { t } } \cos ( a _ { \mathrm { u } , m } ( t ) ) , y _ { m } ( t ) + v _ { m } \Delta _ { \mathrm { t } } \sin ( a _ { \mathrm { u } , m } ( t ) ) ]$ In ${ \mathbf W } _ { \mathrm { c } } ( t ) , { \mathbf W } _ { \mathrm { s } } ( t )$ , and ${ \bf a } _ { \bf u } ( t )$ , each element is a continuous variable to be optimized by the agent. Overall, the action of the agent at time slot t can be denoted by $\begin{array} { r l } { \mathbf { A } ( t ) } & { { } = } \end{array}$ $( \mathbf { W } _ { \mathrm { c } } ( t ) , \mathbf { W } _ { \mathrm { s } } ( t ) , \mathbf { a } _ { \mathrm { u } } ( t ) )$

3) State Space S: The state space $s$ is a set of all possible states, each of which contains enough useful information for decision-making. To be specific, at time slot t, the observable state ${ \bf S } ( t )$ is determined by the communication CSI ${ \bf H } _ { \mathrm { c } } ( t )$

the sensing CSI H (t), and all UAVs’ locations $\begin{array} { r l } { \mathbf { U } ( t ) } & { { } = } \end{array}$ $[ { \bf u } _ { 1 } ( t ) , { \bf u } _ { 2 } ( t ) , \cdot \cdot \cdot , { \bf u } _ { M } ( t ) ]$ ], which can be represented as

$$
\mathbf { S } ( t ) = \big [ \mathbf { H } _ { \mathrm { c } } ( t ) , \mathbf { H } _ { \mathrm { s } } ( t ) , \mathbf { U } ( t ) \big ] .\tag{15}
$$

4) Transition Probabilities P: The transition probability, denoted by $p \left( \mathbf { S } ( t + 1 ) = \mathbf { S } ^ { \prime } | \mathbf { S } ( t ) = \mathbf { S } , \mathbf { A } ( t ) = \mathbf { A } \right)$ ), describes the probability that the state transits from S to S<sup>0</sup> after action A is conducted [36]. Since the mobility information of the target is not available, the transition probability $p \left( \mathbf { S } ^ { \prime } | \mathbf { S } , \mathbf { A } \right)$ is unknown. As a result, problem (14) is a partially observable MDP problem.

5) Reward Function R: The reward function, denoted by $r ( t + 1 ) = \mathcal { R } ( \mathbf { S } ( t ) , \mathbf { A } ( t ) )$ , presents the award or penalty to evaluate how good A(t) is under S(t). In the design of the reward function, we address constraints (3), (4), and (14c), apart from the optimization objective (14a). In Section IV-B, we will detail how to guarantee constraints (2) and (14d) from the perspective of action selection.

• First, considering only the optimization objective of maximizing the sum-rate of all UAVs, the reward is given by $r ( t + 1 ) = \mathbf { R } _ { \mathrm { t o t a l } } ( t )$

• Second, the agent needs to be aware of its unwise decisions, i.e., the collision avoidance constraint (3) or (4) cannot be met. Thus, when a collision occurs at time slot t, the corresponding reward $r ( t + 1 )$ should be a penalty $- \delta _ { 1 }$ , wherein $\delta _ { 1 } > 0$ is the penalty coefficient corresponding to the collision avoidance constraint, balancing the utility and cost [38]. The larger $\delta _ { 1 }$ is, the more the agent attaches importance to the given constraint.

Third, according to constraint (14c), the agent needs to satisfy the preset sensing SNR requirement $\Gamma _ { \mathrm { m i n } } .$ . In this regard, if the average sensing SNR over the whole flight period (i.e., episode)<sup>1</sup> is less than $\Gamma _ { \mathrm { m i n } } .$ , a penalty $- \delta _ { 2 } \left( \Gamma _ { \mathrm { m i n } } - \sum _ { t = 1 } ^ { T } \mathrm { S N R } _ { \mathrm { T a r } } ( t ) / T \right)$ should be added to $r ( t + 1 )$ , wherein $\delta _ { 2 } ~ > ~ 0$ is the penalty coefficient corresponding to the sensing SNR requirement constraint. As such, the agent can be encouraged to optimize its strategy, so as to meet the average SNR requirement for sensing the target in subsequent episodes.

Overall, the reward function of the agent is designed as (16), shown at the bottom of the page. Note that since ${ \textstyle \sum _ { t = 1 } ^ { T } } \mathbf { S } \mathbf { N } \mathbf { R } _ { \mathrm { T a r } } ( t ) / T$ is not revealed until the end of each episode, the rewards $\{ r ( t + 1 ) | t = 1 , 2 , \cdot \cdot \cdot , \ T \}$ are only available at the agent in time slot $t = T ,$

Thus far, we have reformulated problem (14) as an unconstrained MDP problem. At each time slot, given the system

<sup>1</sup>This paper uses the terms “flight period” and “episode” interchangeably.

$$
r ( t + 1 ) = \left\{ \begin{array} { l l } { \displaystyle - \delta _ { 1 } - \delta _ { 2 } \left( \Gamma _ { \mathrm { m i n } } - \frac { 1 } { T } \sum _ { t = 1 } ^ { T } \mathrm { S N R } _ { \mathrm { T a r } } ( t ) \right) , } & \\ { \displaystyle - \delta _ { 1 } , } & \\ { \displaystyle \mathrm { R } _ { \mathrm { t o t a l } } ( t ) - \delta _ { 2 } \left( \Gamma _ { \mathrm { m i n } } - \frac { 1 } { T } \sum _ { t = 1 } ^ { T } \mathrm { S N R } _ { \mathrm { T a r } } ( t ) \right) , } & \\ { \displaystyle \mathrm { R } _ { \mathrm { t o t a l } } ( t ) , } & \end{array} \right.
$$

state S(t), the agent makes an decision ${ \bf A } ( t )$ to interact with the environment by trial-and-error according to a policy $\pi ( \mathbf { A } ( t ) | \mathbf { S } ( t ) )$ . Afterward, the environment feeds back a reward $r ( t + 1 )$ to the agent, and enters a new state $\mathbf { S } ( t + 1 )$ with probability $p \left( \mathbf { S } ^ { \prime } | \mathbf { S } , \mathbf { A } \right)$ . Over the lifetime, the agent aims to search for an optimal policy $\pi ^ { * } \left( \mathrm { i . e . } \right.$ ., the optimal joint GBS’s beamforming and UAVs’ trajectories policy) to maximize the cumulative reward $\begin{array} { r } { G ( t ) = \sum _ { l = t } ^ { T } r ( l + 1 ) } \end{array}$ [36]. Furthermore, the action-value that reflects the expected cumulative reward at state $\mathbf { S } ( t )$ given ${ \bf A } ( t )$ is chosen can be defined as

$$
{ Q } _ { \pi } \left( { \mathbf { S } } ( t ) , { \mathbf { A } } ( t ) \right) = \mathbb { E } _ { \pi } \left[ G ( t ) | { \mathbf { S } } ( t ) , { \mathbf { A } } ( t ) \right] .\tag{17}
$$

In the above MDP problem, if the channel model is accurately known, the state transition probability $p \left( \mathbf { S } ^ { \prime } | \mathbf { S } , \mathbf { A } \right)$ is easy to obtain. At this time, this MDP problem can be well tackled by dynamic programming. However, the mobility model of the target is unavailable at the GBS, which motivates the use of model-free DRL techniques.

## IV. DEEPLSC SCHEME

In this section, we present DeepLSC, a DRL-enabled ISAC scheme, to solve the formulated MDP problem. The underpinning algorithm in DeepLSC is DDPG [39], and the major reasons why we favor DDPG are as follows: (i) Problem (14) involves continuous control variables, whereas valuebased DRL methods, e.g., deep Q-network (DQN) [37], are limited to discrete control problems. (ii) Conventional policybased approaches, e.g., policy gradient [42], are capable of solving continuous control issues, but they suffer from unstable learning and slow convergence. DDPG, which integrates the advantages of value-based and policy-based methods, can effectively circumvent the above challenges. Fig. 2 shows the DeepLSC framework, and the details are elaborated below.

## A. Actor-Critic Architecture

There are two types of DNNs in DeepLSC, referred to as actor and critic. Each of them consists of two DNNs with the same structure but different parameters, i.e., the eval-actor with parameter $\Theta _ { \mathrm { a } } ,$ the target-actor with parameter $\Theta _ { \mathrm { a } } ^ { - }$ , the evalcritic with parameter $\mathbf { \sigma } \Theta _ { \mathrm { c } } ,$ , and the target-critic with parameter $\Theta _ { \mathrm { c } } ^ { - }$ . As shown in Fig. 2, all DNNs share the same structure, i.e., one input layer, one gated recurrent unit (GRU) layer [43], one fully connected (FC) layer [44], and one output layer, but their roles are different.

if (3) or (4) is not met and (14c) is not met,

(16)

if (3) and (4) are met but (14c) is not met,

if (3), (4), and (14c) are all met.

![](images/4e9a7c0feaca8c1bf68da97c74f93cbd02ee801942ff9e333af8264b662cb322.jpg)  
Fig. 2. DeepLSC framework, including the execution phase and the training phase. During the execution phase, based on S(t), the eval-actor outputs the temporary joint beamforming and trajectory decision $\pi _ { \mathrm { a } } ( \mathbf { S } ( t ) , \Theta _ { \mathrm { a } } )$ , which is refined by the constrained noise-exploration policy. During the training phase, some experience sets sampled from the experience buffer are augmented to form the mini-batch for training the actor-critic architecture.

1) Eval-Actor: At each time slot, the eval-actor makes a temporary joint beamforming and trajectory decision $\pi _ { \mathrm { a } } \left( \mathbf { S } ( t ) ; \Theta _ { \mathrm { a } } \right)$ based on the state ${ \bf S } ( t )$ . Specifically, since the DNN cannot process complex numbers, we divide ${ \bf { H } } _ { \mathrm { { c } } } ( t )$ and ${ \bf H } _ { \mathrm { s } } ( t )$ into the corresponding real and imaginary parts, and concatenate them together with U(t). After obtaining the preprocessed state S(t), the input layer delivers it into the GRU layer. Afterward, the GRU layer extracts the underlying temporal correlation from the input sequence and imports it into the FC layer for analysis.<sup>2</sup> Since DNNs cannot generate complex numbers, it is not feasible to directly get a matrix with size $N { \times } M$ as $\mathbf { W } _ { \mathrm { c } } ( t )$ and a matrix with size $N \times N$ as $\mathbf { W } _ { \mathrm { s } } ( t )$ Thus, after receiving the processed information from the FC layer, the output layer generates $\pi _ { \mathrm { a } } \left( \mathbf { S } ( t ) ; \Theta _ { \mathrm { a } } \right)$ containing three vectors, wherein the first vector with size 2N M is related to the temporary communication beamforming, the second vector with size $2 N ^ { 2 }$ is related to the temporary sensing beamforming, and the last vector with size M is the temporary trajectory decision. In particular, with the first vector in $\pi _ { \mathrm { a } } \left( \mathbf { S } ( t ) ; \Theta _ { \mathrm { a } } \right)$ , the temporary communication beamforming can be generated via element-wise concatenation, i.e., the first NM elements are treated as the real parts of individual elements in the temporary communication beamforming and the remaining elements are the corresponding imaginary parts. The temporary sensing beamforming can also be generated in a similar way. In Section IV-B, a new action selection policy will be designed to determine the real joint beamforming and trajectory decision A(t).

2) Eval-Critic: After acquiring the action A(t) from the eval-actor, the agent feeds it together with S(t) to the evalcritic for evaluating the action-value $Q ( \mathbf { S } ( t ) , \mathbf { A } ( t ) ; \mathbf { \Theta } _ { \mathrm { c } } )$ . To cater to the input of the DNN, the eval-critic preprocesses each element in both S(t) and A(t) in a similar way as the eval-actor. Then, the evaluated action-value will be used to compute the action gradient, i.e., $\nabla _ { \mathbf { A } ( t ) } Q ( \mathbf { S } ( t ) , \mathbf { A } ( t ) ; \mathbf { \Theta } _ { \mathrm { c } } )$ , so as to train the eval-actor as detailed in Section IV-C.

3) Target-Actor and Target-Critic: The role of both the target-actor and the target-critic is to compute the target value of $Q ( \mathbf { S } ( t ) , \mathbf { A } ( t ) ; \mathbf { \Theta } _ { \mathrm { c } } )$ when the eval-critic is trained. To further enhance the stability of the algorithm, the parameters of the eval-actor and the eval-critic are fully updated, whereas the parameters of the target-actor and the target-critic are partially updated via the soft-update approach in Section IV-E.

## B. Constrained Noise-Exploration Policy

Given the optimization objective (14), the eval-actor aims to find the optimal policy of joint beamforming and trajectory $\pi _ { \mathrm { a } } ^ { \ast }$ Recall that in Section III-B, constraints (3), (4), and (14c) have been considered from the perspective of reward design. We now illustrate how to guarantee the maximum power constraint (14d) and the flight mission constraint (2) from the perspective of action selection. Specifically, according to constraints (14d) and (2), the signal power used for communication and sensing cannot exceed the preset maximum value $P _ { \mathrm { m a x } } ,$ , and the trajectory should ensure all UAVs to complete their flight missions within each episode. Given the temporary joint beamforming and trajectory decision $\pi _ { \mathrm { a } } \left( \mathbf { S } ( t ) ; \Theta _ { \mathrm { a } } \right)$ from the eval-actor based on ${ \bf S } ( t )$ , the conventional noise-exploration policy in DDPG [39] generates a refined decision by adding randomness, i.e.,

$$
\begin{array} { r } { ( { \bf a } _ { \mathrm { c } } ( t ) , { \bf a } _ { \mathrm { s } } ( t ) , { \bf a } _ { \mathrm { u } } ( t ) ) = \pi _ { \mathrm { a } } \left( { \bf S } ( t ) ; \Theta _ { \mathrm { a } } \right) + ( { \bf d } _ { \mathrm { c } } ( t ) , { \bf d } _ { \mathrm { s } } ( t ) , { \bf d } _ { \mathrm { u } } ( t ) ) , } \end{array}\tag{18}
$$

where ${ \bf a } _ { \mathrm { c } } ( t )$ and ${ \bf a } _ { \mathrm { s } } ( t )$ are vectors with size 2NM and $2 N ^ { 2 }$ respectively. Vector $\mathbf { d } _ { i } ( t ) , \forall i \in \{ \mathrm { c } , \mathrm { s } , \mathbf { u } \}$ , has the same size as ${ \bf a } _ { i } ( t )$ , each element of which is Gaussian distributed with zero mean and variance $\sigma _ { i } ^ { 2 } ( t )$ . By doing so, the agent is encouraged to explore random actions for better solutions. Generally, too much exploration is unnecessary once an efficient solution is learned. Hence, we introduce a decay factor $\kappa \in ( 0 , 1 )$ to reduce $\sigma _ { i } ^ { 2 } ( t )$ over time. Denote the initial variances by $\sigma _ { i , \mathrm { i n i t } } ^ { 2 } ,$ then $\sigma _ { i } ^ { 2 } ( t )$ at time slot t can be represented as $\boldsymbol { \sigma } _ { i , \mathrm { i n i t } } ^ { 2 } \kappa ^ { t }$

The conventional noise-exploration policy, however, only improves the exploration capability of the agent, while ignoring constraints (14d) and (2). To cope with this issue, we develop a new action selection policy for DeepLSC, referred to as constrained noise-exploration policy. The gist is to (i) introduce a scaling factor to refine the beamforming decided by the conventional noise-exploration policy, so as to meet constraint (14d), and (ii) decide whether to use the conventional noise-exploration policy based on the real-time location of each UAV, so as to satisfy constraint (2). The details are elaborated below.

1) Decision-Making of Communication and Sensing Beamforming: As a first step, with ${ \bf a } _ { \mathrm { c } } ( t )$ and ${ \bf a } _ { \mathrm { s } } ( t )$ , two matrices $\mathbf { \bar { A } } _ { \mathrm { c } } ( t ) \in \mathbb { C } ^ { N \times M }$ and $\bar { \mathbf { A } _ { \mathrm { s } } } ( t ) \in \mathbb { C } ^ { N \times N }$ can be generated via element-wise concatenation, i.e., the first NM $( N ^ { 2 } )$ elements of ${ \bf a } _ { \mathrm { c } } ( t ) ( { \bf a } _ { \mathrm { s } } ( t ) )$ are treated as the real parts of individual elements in $\mathbf { A } _ { \mathrm { c } } ( t ) ( \mathbf { A } _ { \mathrm { s } } ( t ) )$ and the remaining elements are the corresponding imaginary parts. Thereafter, to obtain the communication beamforming $\mathbf { W } _ { \mathrm { c } } ( t )$ and the sensing beamforming $\mathbf { W } _ { \mathrm { s } } ( t )$ that satisfy the preset power constraint (14d), a scaling factor, defined as $\epsilon = P _ { \mathrm { m a x } } / \big ( \mathrm { T r } \left( \mathbf { A } _ { \mathrm { c } } ^ { H } ( t ) \mathbf { A } _ { \mathrm { c } } ( t ) \right) +$ $\operatorname { T r } \left( \mathbf { A } _ { \mathrm { s } } ^ { H } ( t ) \mathbf { A } _ { \mathrm { s } } ( t ) \right)$ , is introduced to refine ${ \bf A } _ { \mathrm { c } } ( t )$ and ${ \bf A } _ { \mathrm { s } } ( t )$ as follows:

$$
\mathbf { W } _ { \mathrm { c } } ( t ) = \sqrt { \epsilon } \mathbf { A } _ { \mathrm { c } } ( t ) , \ \mathbf { W } _ { \mathrm { s } } ( t ) = \sqrt { \epsilon } \mathbf { A } _ { \mathrm { s } } ( t ) .\tag{19}
$$

2) Decision-Making of UAVs’ Trajectories: Within each episode, all UAVs’ trajectories $\begin{array} { r c l } { \{ \mathbf { a } _ { \mathbf { u } } ( t ) } & { = } & { [ a _ { \mathbf { u } , 1 } ( t ) , a _ { \mathbf { u } , 2 } ( t ) , \cdots , \quad a _ { \mathbf { u } , M } ( t ) ] | t \in \mathcal { T } \} } \end{array}$ decided by the agent should fulfill the preset flight mission. For this purpose, the constrained noise-exploration policy that decides $\boldsymbol { a } _ { \mathrm { u } , m } ( t )$ limits the movement directions of UAV m in the last $T - t - 1$ time slots within each episode: at time slot t, if the minimum required number of time slots from the current location to reach the desired location is not less than $T - t - 1 ^ { 3 }$ , UAV m has to fly in a straight line toward the desired location $\mathbf { u } _ { m } ^ { \mathrm { F } }$ , i.e., $a _ { \mathbf { u } , m } ( t ) \ = \ \cdot$ “straight flight”. Within other time slots, the movement decision $a _ { \mathrm { u } , m } ( t )$ can be directly determined through the conventional noiseexploration policy, in the sense that the agent is not subject to constraint (2) and thus can derive more efficient movement directions for UAVs towards other optimization objectives. Overall, the movement decision of UAV m at time slot t is given as follows:

$$
\begin{array} { r l } & { a _ { \mathrm { u } , m } ( t ) } \\ & { \ = \left\{ a _ { \mathrm { u } , m } ( t ) , \quad \mathrm { i f ~ } \lceil \frac { \| \mathbf { u } _ { m } ( t ) - \mathbf { u } _ { m } ^ { F } \| _ { 2 } } { v _ { m } \Delta _ { t } } \rceil < T - t - 1 , \right. } \\ & { \mathrm { s t r a i g h t ~ } \mathrm { H i g h t } , \quad \mathrm { o t h e r w i s e } , } \end{array}\tag{20}
$$

where dxe represents the smallest integer not less than x.

<sup>3</sup>Intuitively, to complete the flight mission, UAV m only needs to fly in a straight line towards the desired location $\mathbf { u } _ { m } ^ { \mathrm { F } }$ when the number of its available time slots is equal to the minimum required number of time slots. However, there are some special cases. For example, the movement distance of UAV m in each time slot is 1 m, the number of time slots available to UAV m at time slot t is 11, and at least 10 time slots are required to reach the desired location ${ \bf u } _ { , m } ^ { \mathrm { F } } .$ If UAV m moves in the opposite direction of the desired location at time slot t, the number of time slots available to UAV m at time slot t + 1 will be 10 but at this time at least 11 time slots will be required to reach the desired location. Consequently, UAV m will never complete the flight mission in the subsequent time slots. Therefore, in (20), we relax $T - t { \mathrm { ~ t o ~ } } ^ { \circ } T - t - 1 .$

## C. Hierarchical Experience Replay

Since DeepLSC is developed for episode tasks, all experiences from different time slots within each episode should be jointly used to train both the eval-actor and the eval-critic. However, in the conventional experience replay mechanism of DDPG [40], the experiences generated in different time slots are separately gathered and utilized. In other words, during training, the experiences from different time slots within a specific episode cannot be guaranteed to appear in full. Consequently, the agent fails to learn an efficient joint beamforming and trajectory strategy in LAE-oriented ISAC systems. To fill this gap, a new hierarchical experience replay mechanism is designed for DeepLSC, which makes use of experience sets each containing all experiences generated within each episode to train the eval-actor and the eval-critic.

As a first step, to store and reuse historical experiences, a first-input-first-output (FIFO) experience buffer D with size D is used. As mentioned in Section III-B, within each episode, the rewards $\{ r ( t + 1 ) | t \ = \ 1 , 2 , \cdot \cdot \cdot , T \}$ are not available until time slot T. Thus, in time slot T of each episode, after calculating the reward $r ( t + 1 )$ via (16), the agent collects the experience $e ( t )$ in the form of $( \mathbf { S } ( t ) , \mathbf { A } ( t ) , r ( t + 1 ) , \mathbf { S } ( t + 1 ) )$ where $\mathbf { A } ( t ) ~ = ~ [ \mathbf { W } _ { \mathrm { c } } ( t ) , \mathbf { W } _ { \mathrm { s } } ( t ) , \mathbf { a } _ { \mathrm { u } } ( t ) ]$ . With all experiences generated over the whole episode, an experience set ${ \mathcal { E } } =$ $\{ e ( t ) | t = 1 , 2 , \cdot \cdot \cdot , T \}$ is formed and stored in D. During training, $N _ { \mathrm { e } }$ experience sets are randomly sampled from D to form the mini-batch B. Afterward, the loss function for training the eval-critic is given as

$$
L ( \boldsymbol { \Theta } _ { \mathrm { c } } ) = \frac { 1 } { N _ { \mathrm { e } } } \sum _ { \mathcal { E } \subset \mathcal { B } } \Bigg ( \sum _ { t = 1 } ^ { T } \big ( z ( t + 1 ) - Q \left( \mathbf { S } ( t ) , \mathbf { A } ( t ) ; \boldsymbol { \Theta } _ { \mathrm { c } } \right) \big ) ^ { 2 } \Bigg ) ,\tag{21}
$$

where $\begin{array} { r l r } { z ( t { \mathrm { ~ + ~ } } 1 ) } & { { } = } & { r ( t + 1 ) \mathrm { ~ + ~ } Q \big ( { \mathbf { S } } ( t + 1 ) , \pi _ { \mathrm { a } } ^ { - } \big ( { \mathbf { S } } ( t { \mathrm { ~ + ~ } } } \end{array}$ 1); $\Theta _ { \mathrm { a } } ^ { - } ) ; \Theta _ { \mathrm { c } } ^ { - } )$ is the target value related to the eval-actor, and $\pi _ { \mathrm { a } } ^ { - }$ is the policy of the target-actor. Furthermore, by performing the stochastic gradient descent (SGD) algorithm [36], the parameter Θ<sub>c</sub> is updated as follows:

$$
\Theta _ { \mathrm { c } } \{ - \Theta _ { \mathrm { c } } - \alpha _ { \mathrm { c } } \nabla \Theta _ { \mathrm { c } } L ( \Theta _ { \mathrm { c } } ) ,\tag{22}
$$

where $\alpha _ { \mathrm { c } }$ is the learning rate of $\mathbf { \Theta } \Theta _ { \mathrm { c } } .$ . On the other hand, the parameter $\Theta _ { \mathrm { a } }$ of the eval-actor can be updated via the sampled policy gradient algorithm [39], i.e.,

$$
\begin{array} { c } { { \displaystyle \Theta _ { \mathrm { a } } { \gets } \Theta _ { \mathrm { a } } - \alpha _ { \mathrm { a } } \frac { 1 } { N _ { \mathrm { e } } } \sum _ { \varepsilon \subset B } \left( \sum _ { t = 1 } ^ { T } \left( \nabla _ { \mathbf { A } ( t ) } Q \big ( \mathbf { S } ( t ) , \mathbf { A } ( t ) ; \Theta _ { \mathrm { c } } \big ) \right. \right. } } \\ { { \displaystyle \left. \left. \times \nabla _ { \Theta _ { \mathrm { a } } \pi _ { \mathrm { a } } } \big ( \mathbf { S } ( t ) ; \Theta _ { \mathrm { a } } \big ) \right) \right) , } } \end{array}\tag{23}
$$

with $\alpha _ { \mathrm { a } }$ being the learning rate of $\mathbf { \Theta } _ { \mathbf { e } } .$

## D. Symmetric Experience Augmentation

In DeepLSC, to gain enough experiences for DNN training, the agent needs to perform a lot of trial and error with the environment. Consequently, an efficient joint beamforming and trajectory strategy usually takes a long time to derive. If the experience set $\{ ( \mathbf { S } ( t ) , \mathbf { A } ( t ) , r ( t + 1 ) , \mathbf { S } ( t + 1 ) ) | t \ =$

$1 , 2 , \cdots , T \}$ can be generated based on existing experience sets, the experience buffer D will effectuate experience augmentation and greatly boost the convergence speed. Actually, in problem (14), the index of each UAV is artificially specified. Thus, in terms of the system performance, if the indices of different UAVs are permuted, the new optimization problem is equivalent to the original problem [45]. For example, when $M = 2$ and N = 2, the communication CSI is given as

$$
\mathbf { H } _ { \mathrm { c } } ( t ) = \left[ \begin{array} { l l } { \mathbf { h } _ { 1 , 1 } ( t ) } & { \ \mathbf { h } _ { 1 , 2 } ( t ) } \\ { \mathbf { h } _ { 2 , 1 } ( t ) } & { \ \mathbf { h } _ { 2 , 2 } ( t ) } \end{array} \right] .\tag{24}
$$

where $\mathtt { h } _ { n , m }$ is the channel component of antenna n to UAV m. If we permute the indexes of UAV 1 and UAV 2, the communication CSI will be transformed into

$$
\mathbf { H } _ { \mathrm { c } } ( t ) = \left[ \begin{array} { l l } { \mathbf { h } _ { 1 , 2 } ( t ) } & { \ \mathbf { h } _ { 1 , 1 } ( t ) } \\ { \mathbf { h } _ { 2 , 2 } ( t ) } & { \ \mathbf { h } _ { 2 , 1 } ( t ) } \end{array} \right] .\tag{25}
$$

At this time, if the indexes of UAV 1 and UAV 2 in the communication beamforming ${ \bf W } _ { \mathrm { c } } ( t )$ , the sensing beamforming $\mathbf { W } _ { \mathrm { s } } ( t )$ , the UAVs’ movement decisions ${ \bf a } _ { \bf u } ( t )$ , and the sensing CSI H<sub>s</sub>(t) are synchronously permuted, the new optimization problem will be equivalent to the original problem.

Inspired by this, we propose the symmetric experience augmentation mechanism, and the main idea is to simultaneously exchange the indexes of all variables to generate more new experience sets. Specifically, denote $\begin{array} { r l r } { \Upsilon } & { { } = } & { \{ \{ v _ { 1 } , v _ { 2 } , v _ { 3 } , \cdot \cdot \cdot , v _ { M } \} , \quad \{ v _ { 2 } , v _ { 1 } , v _ { 3 } , \cdot \cdot \cdot , } \end{array}$ $v _ { M } \} , \cdots , \ \{ v _ { M } , v _ { M - 1 } , v _ { M - 2 } , \cdots , v _ { 1 } \} \}$ } by the symmetric group of finite integer set $\mathcal { F } = \{ v _ { 1 } , v _ { 2 } , \cdots , v _ { M } \}$ , where group elements are bijection of $\mathcal { F }$ to itself. Let $\Omega _ { v _ { i } }$ denote the permutation of $v _ { i } .$ . Then the permutation of individual elements in $\mathcal { F }$ can be represented as

$$
\Omega = \left( \begin{array} { c c c c c } { \upsilon _ { 1 } } & { } & { \upsilon _ { 2 } } & { } & { \cdot \cdot \cdot } & { } & { \upsilon _ { M } } \\ { \Omega _ { \upsilon _ { 1 } } } & { \Omega _ { \upsilon _ { 2 } } } & { } & { \cdot \cdot \cdot } & { \Omega _ { \upsilon _ { M } } } \end{array} \right) ,\tag{26}
$$

where the first row is the elements of ${ \mathcal { F } } _ { : }$ , and the second row is the corresponding permutation under Ω. In the above example, the permutation is given as $\Omega = { \binom { 1 } { 2 } }$ . Consider a system with M UAVs. Under all possible permutations Ω, there will be a total of M ! group elements in Υ. Besides, to distinguish the variables before and after the permutation, we superscript the permuted communication beamforming, sensing beamforming, UAVs’ movement decisions, communication CSI, and sensing CSI by Ω as $\mathbf { W } _ { \mathrm { c } } ^ { \Omega } ( t ) , \ \mathbf { W } _ { \mathrm { s } } ^ { \Omega } ( t ) , \ \mathbf { a } _ { \mathrm { u } } ^ { \Omega } ( t ) , \ \mathbf { H } _ { \mathrm { c } } ^ { \Omega } ( t )$ , and ${ \bf H } _ { \mathrm { s } } ^ { \Omega } ( t )$ respectively.

Therefore, the experience sets used for DeepLSC training can be significantly enriched through various permutations. In particular, given a prior experience set $\{ e ( i ) ~ =$ $( { \bf S } ( i ) , { \bf A } ( i ) , r ( i + 1 ) , { \bf \bar { S } } ( i + 1 { \bf \bar { \Delta } } ) ) | i \ = \ 1 , 2 , \cdots , T \}$ that is acquired via the agent-and-environment interaction, $M ! - 1$ new experience sets, i.e., $\{ \{ e ^ { \Omega } ( i ) \mid i = 1 , 2 , \cdot \cdot \cdot , T \} \mid \Omega \in$ $\Upsilon \}$ , can be generated based on the symmetric group Υ. In each experience set $e ^ { \Omega } ( i )$ , the elements are given as

$$
\begin{array} { r } { \left\{ \begin{array} { l l } { \mathbf { S } ^ { \Omega } ( i ) = [ \mathbf { H } _ { \mathrm { c } } ^ { \Omega } ( i ) , \mathbf { H } _ { \mathrm { s } } ^ { \Omega } ( i ) , \mathbf { U } ^ { \Omega } ( i ) ] } \\ { \mathbf { A } ^ { \Omega } ( i ) = [ \mathbf { W } _ { \mathrm { c } } ^ { \Omega } ( i ) , \mathbf { W } _ { \mathrm { s } } ^ { \Omega } ( i ) , \mathbf { a } _ { \mathrm { u } } ^ { \Omega } ( i ) ] , } \\ { r ^ { \Omega } ( i + 1 ) = r ( i + 1 ) , } \\ { \mathbf { S } ^ { \Omega } ( i + 1 ) = [ \mathbf { H } _ { \mathrm { c } } ^ { \Omega } ( i + 1 ) , \mathbf { H } _ { \mathrm { s } } ^ { \Omega } ( i + 1 ) , \mathbf { U } ^ { \Omega } ( i + 1 ) ] . } \end{array} \right. } \end{array}\tag{27}
$$

The symmetric mapping, despite increasing the number of available experience sets, may lead to strong correlation among experience sets [36]. The consequence is that DeepLSC will fall into overfitting and converge to a sub-optimal joint beamforming and trajectory strategy. Actually, at the beginning of training, it is difficult to get enough experience sets. In this case, it is beneficial to augment existing experience sets based on the symmetric group Υ. However, as the number of episodes increases, the experience sets from agent-andenvironment interactions become miscellaneous. As a result, it is no longer necessary to use the symmetric mapping to enrich the available experience sets. Hence, we introduce a dynamic augmentation factor $\zeta \in ( 0 , 1 )$ to adjust the number of augmented experience sets as follows:

$$
\Lambda ( \omega ) = \lfloor ( M ! - 1 ) \zeta ^ { \omega } \rfloor ,\tag{28}
$$

where bxc represents the largest integer less than x, and ω is the number of training times. During each training, $N _ { \mathrm { e } }$ experience sets, i.e., $\{ \{ e ( i , j ) | i = 1 , 2 , \cdot \cdot \cdot , T \} | j =$ $1 , 2 , \cdots , N _ { \mathrm { e } } \}$ ,, are sampled from D in random, and each of which is augmented based on $\Lambda ( \omega )$ random group elements (i.e., permutations Ω) of the symmetric group Υ. Thereafter, all augmented experience sets are merged with $N _ { \mathrm { e } }$ original experience sets to form the mini-batch $\boldsymbol { B }$ for training the evalactor and eval-critic.

## E. Soft-Update for Target-Actor and Target-Critic

The parameters $\Theta _ { \mathrm { a } } ^ { - }$ and $\Theta _ { \mathrm { c } } ^ { - }$ of the target-actor and the target-critic are updated based on the parameters $\mathbf { \Theta } _ { \mathbf { \Theta } } \Theta _ { \mathrm { a } }$ and $\Theta _ { \mathrm { c } }$ of the eval-actor and the eval-critic. A simple approach is to update the parameters of the target-actor and the target-critic by $\Theta _ { \mathrm { a } } ^ { - }  \Theta _ { \mathrm { a } }$ and $\mathbf { \Theta } \Theta _ { \mathrm { c } } ^ { - }  \mathbf { \Theta } \Theta _ { \mathrm { c } }$ . However, this approach is not suitable for the continuous control task, since it may lead to large prediction errors of the target-actor and the target-critic [39]. To circumvent this issue, the soft-update approach was proposed in [36], which updates both $\Theta _ { \mathbf { a } } ^ { - }$ and $\Theta _ { \mathrm { c } } ^ { - }$ as follows:

$$
\Theta _ { \mathrm { a } } ^ { - }  \chi _ { \mathrm { a } } \Theta _ { \mathrm { a } } + ( 1 - \chi _ { \mathrm { a } } ) \Theta _ { \mathrm { a } } ^ { - } , \Theta _ { \mathrm { c } } ^ { - }  \chi _ { \mathrm { c } } \Theta _ { \mathrm { c } } + ( 1 - \chi _ { \mathrm { c } } ) \Theta _ { \mathrm { c } } ^ { - } ,\tag{29}
$$

where $\chi _ { \mathrm { a } } \in [ 0 , 1 ]$ and $\chi _ { \mathrm { c } } \in [ 0 , 1 ]$ are the update factors of the target-actor and the target-critic, respectively. To be specific, the soft-update enables the target-actor and the target-critic to maintain a certain continuity during the update process, so as to better adapt to the continuous control task.

## F. Detailed Operations of DeepLSC

Thus far, we have presented the main elements of the DeepLSC scheme, and Algorithm 1 provides the corresponding pseudocode. Overall, the operations of DeepLSC include: (i) decide the temporary joint beamforming and trajectory decision $\pi _ { \mathrm { a } } \left( \mathbf { S } ( t ) ; \Theta _ { \mathrm { a } } \right)$ via the eval-actor with the current state S(t) (lines $7 \sim 8 ) ;$ (ii) decide ${ \bf a } _ { \mathrm { c } } ( t ) , { \bf a } _ { \mathrm { s } } ( t )$ , and ${ \bf a } _ { \bf u } ( t )$ via (18) (lines $9 \sim 1 0 )$ ; (iii) determine the communication beamforming ${ \bf W } _ { \mathrm { c } } ( t )$ and the sensing beamforming W<sub>s</sub>(t) via (19), and the movement directions ${ \bf a } _ { \bf u } ( t )$ via (20) (lines $1 1 \sim 1 3 ) ;$ (iv) obtain the next state $\mathbf { S } ( t + 1 )$ according to (15) (line 14); (v) calculate the reward $\{ r ( t + 1 ) | t = 1 , 2 , \cdot \cdot \cdot , T \}$ via (16)

Algorithm 1 DeepLSC Scheme   
1: Initialize $N , M , T , \boldsymbol { \mathbf { b } } , \boldsymbol { \mathbf { u } } _ { m } ^ { \mathrm { I } } , \boldsymbol { \mathbf { u } } _ { m } ^ { \mathrm { F } } , \{ H _ { m } | m \in \mathcal { M } \} , v _ { m } , \Gamma _ { \mathrm { m i n } } .$   
2: Initialize ${ \bf g } ( 0 ) , H _ { \mathrm { T a r } } ( 0 ) , \delta _ { 1 } , \delta _ { 2 } , \sigma _ { \mathrm { m i n } } , \kappa , \alpha _ { \mathrm { a } } , \alpha _ { \mathrm { c } } , \Upsilon , \Omega .$   
3: Initialize $\omega = 0 , \{ \sigma _ { i , \mathrm { i n i t } } ^ { 2 } | i = { \mathrm { c } } , { \mathrm { s } } , { \mathrm { u } } \} , \zeta , \mathcal { E } , D , N _ { \mathrm { e } } , \chi _ { \mathrm { a } } , \chi _ { \mathrm { c } } .$   
4: Initialize $\Theta _ { \mathrm { a } } , \Theta _ { \mathrm { a } } ^ { - } , \Theta _ { \mathrm { c } } , \Theta _ { \mathrm { c } } ^ { - } .$   
5: for episode $= 1 , 2 , \cdots$ do   
6: for $t = 1 , 2 , \cdots , T$ do   
7: Input S(t) into the eval-actor;   
8: Make the temporary decision $\pi _ { \mathrm { a } } \left( \mathbf { S } ( t ) ; \Theta _ { \mathrm { a } } \right) ;$   
9: Generate $\mathbf { a } _ { \mathrm { c } } ( t ) , \mathbf { a } _ { \mathrm { s } } ( t ) ,$ , and ${ \bf a } _ { \mathrm { u } } ( t )$ via (18);   
10: Update $\sigma _ { i } ^ { 2 } ( t )$ to $\sigma _ { i , \mathrm { i n i t } } ^ { 2 } \kappa ^ { t } ;$   
11: Obtain $\mathbf { W } _ { \mathrm { c } } ( t )$ and $\mathbf { W } _ { \mathrm { s } } ( t )$ via (19);   
12: Refine ${ \bf a } _ { \mathrm { u } } ( t )$ via (20);   
13: Take ${ \bf A } ( t )$ to interact with the environment;   
14: Obtain $\mathbf { S } ( t + 1 )$ via (15).   
15: end for   
16: Compute $\{ r ( t + 1 ) | t = 1 , 2 , \cdot \cdot \cdot , T \}$ via (16);   
17: Form $\{ e ( t ) | t = 1 , 2 , \cdot \cdot \cdot , T \}$ to store into $\mathcal { D } ;$   
18: Randomly sample $N _ { \mathrm { e } }$ experience sets from $\mathcal { D } ;$   
19: Augment each experience set with $\Lambda ( \omega )$ via (27);   
20: Set $\omega $ episode and update $\Lambda ( \omega ) ;$   
21: Merge sampled and augmented experiences to form $\begin{array} { r } { B ; { } } \end{array}$   
22: Calculate $L ( \Theta _ { \mathrm { c } } )$ via (21);   
23: Train $\mathbf { \Theta } _ { \mathbf { \Theta } } \Theta _ { \mathrm { a } }$ via (22) and $\Theta _ { \mathrm { c } }$ via (23);   
24: Update $\Theta _ { \mathbf { a } } ^ { - }$ and $\Theta _ { \mathrm { c } } ^ { - }$ via (29).   
25: end for

at the end of each episode (line 16); (vi) form the experience set $\{ e ( t ) = ( \mathbf { S } ( t ) , \ \mathbf { a } ( t ) , \ r ( t + 1 ) , \ \mathbf { S } ( t + 1 ) ) | t = 1 , 2 , \cdot \cdot \cdot , T \}$ and store it in the experience buffer D (line 17); (vii) randomly sample $N _ { \mathrm { e } }$ experience sets from D and augment each of them with $\Lambda ( \omega )$ via (27) (lines $1 8 \sim 2 0 ) $ (viii) integrate the sampled and augmented experience sets to form the mini-batch B for training the eval-actor and the eval-critic via (22) and (23), respectively (lines $2 1 \sim 2 3 )$ ; and (ix) update the parameters of both the target-actor and the target-critic via (29) (line 14).

## V. COMPLEXITY AND IMPLEMENTATION ANALYSIS

In this section, we first analyze the computational complexity of DeepLSC. Then, detailed implementation procedures in practical systems are presented.

## A. Computational Complexity Analysis

As shown in Fig. 2, the actor-critic architecture serves as the DNN model of DeepLSC, where both the actor and the critic comprise one input layer, one GRU layer, one FC layer, and one output layer. According to [43], (i) the computational complexity of GRU for forward-propagation is given as $\mathcal { O } ( K _ { 1 } K _ { 2 } ^ { 2 } )$ , wherein $K _ { 1 }$ and $K _ { 2 }$ are the number of neurons in the input layer and the GRU layer, respectively; and (ii) the computational complexity for back-propagation is given as $\mathcal { O } ( N _ { \mathrm { T r a i n } } K _ { 1 } K _ { 2 } ^ { 2 } )$ , with $N _ { \mathrm { T r a i n } }$ being the number of experiences for training, respectively. Besides, in the light of [44], (i) the computational complexity of FC for forwardpropagation is given as $\mathcal { O } ( K _ { 2 } K _ { 3 } )$ , wherein $K _ { 3 }$ is the number of neurons in the FC layer; and (ii) the computational complexity for back-propagation is given as $\mathcal { O } ( N _ { \mathrm { T r a i n } } K _ { 3 } K _ { 4 } )$ , with $K _ { 4 }$ being the number of neurons in the output layer. On the other hand, as demonstrated in [44], the computational complexity of the output layer and the input layer needs to be considered in the forward and backward propagation stages, respectively; and their computational complexity is calculated in the same way as the FC layer. Thus, given the DNN model in Fig. 2, the total computational complexity for forward-propagation and back-propagation is calculated as $\mathcal { O } ( K _ { 1 } K _ { 2 } ^ { 2 } + K _ { 2 } K _ { 3 } + K _ { 3 } K _ { 4 } )$ and $\mathcal { O } ( N _ { \mathrm { T r a i n } } ( K _ { 1 } K _ { 2 } + K _ { 1 } K _ { 2 } ^ { 2 } + K _ { 3 } K _ { 4 } ) )$ , respectively.

In the following, we analyze the computational complexity of DeepLSC without the symmetric experience augmentation mechanism and DeepLSC, respectively. (i) In DeepLSC without the symmetric experience augmentation mechanism, the size of the pre-processed input matrix ${ \bf S } ( t )$ is $2 N ( N +$ $M ) + 2 M ,$ the total number of all optional sub-actions is $2 N ( N + M ) + M$ , and the GRU and FC layers share the same number of neurons, denoted by K. In addition, the number of experiences used for training $( \mathrm { i . e . }$ , backpropagation) is $N _ { \mathrm { e } } T$ . Thus, the total computational complexity of DeepLSC without symmetric experience augmentation for both forward-propagation and back-propagation is calculated as $\mathcal { O } \big ( N _ { \mathrm { e } } T ( \bar { N } ^ { 2 } + \bar { N } M + M ) K ^ { 2 } \big )$ . (ii) The symmetric experience augmentation mechanism, while enriching available experiences, increases the computational overhead of DeepLSC during the back-propagation stage. In particular, with this mechanism, the number of experiences used for training is $N _ { \mathrm { e } } T \Lambda ( \omega )$ . As a result, the total computational complexity of DeepLSC for both forward-propagation and back-propagation is $\mathcal { O } \big ( N _ { \mathrm { e } } T \Lambda ( \omega ) ( N ^ { 2 } + N M + M ) K ^ { 2 } \big )$

Overall, the proposed symmetric experience augmentation mechanism, while significantly enriching the experiences for DeepLSC training, introduces additional computational complexity of $\mathcal { O } \big ( N _ { \mathrm { e } } T ( \Lambda ( \omega ) - 1 ) ( N ^ { 2 } + N M + M ) K ^ { 2 } \big )$

## B. Practical Implementation

The DeepLSC scheme can be easily implemented in practical LAE-oriented ISAC systems, where the GBS with sufficient computational resources serves as the agent to execute the scheme. In the following, we provide the detailed procedures for applying DeepLSC in practical scenarios.

1) Training Phase: Similar to previous works [15] and [46], the agent interacts with a simulation environment built using mathematical models, rather than relying on prior training data. The state-of-the-art mathematical models, including the Gauss-Markov-based target random mobility model, the LoS channel model, and the UAV flight mission models, are derived from real-world data to ensure realistic simulations. In this regard, the DeepLSC scheme trained in this environment can be effectively applied to real-world scenarios. Through interactions within the simulation environment, the agent collects data to train the DeepLSC scheme for joint beamforming and trajectory optimization. Once the DNN model converges, the trained DeepLSC scheme can be deployed in realistic systems.

2) Deployment Phase: During the deployment phase, the GBS does not require the real-time sum-rate and average sensing SNR to calculate the reward. Instead, it employs the well-trained DeepLSC scheme to make joint decisions. Specifically, the GBS/agent feeds the state generated according to (15) into the eval-actor to determine joint decisions for data transmission, UAV control, and target detection.

3) Environmental Changes: When the deployment environment undergoes significant changes (e.g., the number of UAVs or the number of time slots within a flight period changes), the GBS retrains the DeepLSC scheme online accordingly. At this time, the DNN parameters of the previously trained DeepLSC scheme can be fine-tuned based on the training results in the new environment. During this process, some efficient training techniques, e.g., transfer learning [47] and the proposed symmetric experience augmentation mechanism, can be used to improve the convergence of the DNN model.

Likewise, in emergency situations such as UAV failure, the GBS can update the set of available UAVs in the simulation and retrain the DeepLSC scheme accordingly. Since this process can be done in simulated environments beforehand, the GBS can pre-train multiple versions of the DeepLSC scheme with different configurations (e.g., different numbers and initial positions of UAVs). By doing so, real-time adaptation can be achieved and the performance of the ISAC system can be maintained without significant downtime.

## VI. PERFORMANCE EVALUATION

This section evaluates the performance of DeepLSC based on Python 3.6 simulation platform, where the Keras library [48] builds all DNN models.

## A. Parameter Settings

1) System Setups: We consider a scenario with one GBS, one target, and M = 4 UAVs, unless stated otherwise. The GBS is located at (0, 0, 0) m, the initial location of the target is (−60, 100, 70) m, the initial locations of UAVs are uniformly chosen from the area [−150, −80] m ×[60, 150] m ×80 m, and the final locations of UAVs are uniformly chosen from the area [90, 160] m ×[50, 160] m ×80 m. The movement speed of the target and UAVs are 10 m per time slot, and the number of time slots within an episode i.e., T, is 40 time slots, by default. The movement azimuth and elevation of the target are initialized to 30<sup>◦</sup>, the time correlation coefficients $\mu _ { \mathrm { a } }$ and $\mu _ { \mathrm { e } }$ for the target movement are 0.9, and the corresponding asymptotic means and standard deviations, i.e., $\xi _ { \mathrm { a } } , \xi _ { \mathrm { e } } , \sigma _ { \phi } ,$ , and $\sigma _ { \varphi } ,$ , are 10<sup>◦</sup>. The number of antennas and the transmit power are $N = 6$ and $P _ { \mathrm { m a x } } = 4 0$ dBm, respectively. The noise power $\sigma _ { \mathrm { b } } ^ { 2 }$ and $\sigma _ { m } ^ { 2 }$ are −80 dBm, The path loss exponent is 3.2, the reference distance $D _ { 0 }$ is 1 m, and the path loss $L _ { 0 }$ for $D _ { 0 }$ is −30 dB. The sensing SNR requirement $\Gamma _ { \mathrm { m i n } }$ is set to 1 dB.

2) Algorithm Setups: In DeepLSC, the GRU and FC layers contain 128 neurons. The underpinning algorithm in DeepLSC is DDPG, where all hyper-parameters are set according to previous investigations [39] and [49], combined with fine-tuning. Specifically, the work [39] proposed the DDPG algorithm and provided default hyper-parameters, while the work [49] comprehensively analyzed the impact of different hyper-parameters on the performance of DDPG. TABLE II summarizes the detailed hyper-parameters used in DeepLSC, and in

TABLE II  
ALGORITHM HYPER-PARAMETERS
<table><tr><td rowspan=1 colspan=1>Hyper-parameter</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>Hyper-parameter</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>Learning rate $\overline { { ( \alpha _ { \mathrm { a } } ) } }$ </td><td rowspan=1 colspan=1>1e-4</td><td rowspan=1 colspan=1>Reward coefficient $\overline { { ( \delta _ { 1 } / \delta _ { 2 } ) } }$ </td><td rowspan=1 colspan=1>20/10</td></tr><tr><td rowspan=1 colspan=1>Learning rate (αc)</td><td rowspan=1 colspan=1>2e-4</td><td rowspan=1 colspan=1>Update coefficient $\overline { { ( \chi _ { \mathrm { a } } ) } }$ </td><td rowspan=1 colspan=1>0.001</td></tr><tr><td rowspan=1 colspan=1>Buffer size (D)</td><td rowspan=1 colspan=1>2000</td><td rowspan=1 colspan=1>Update coefficient $\overline { { ( \chi _ { \mathrm { c } } ) } }$ </td><td rowspan=1 colspan=1>0.001</td></tr><tr><td rowspan=1 colspan=1>Mini-batch size (Ne)</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>Initial exploration (σinit)</td><td rowspan=1 colspan=1>0.9</td></tr><tr><td rowspan=1 colspan=1>Decay factor (κ)</td><td rowspan=1 colspan=1>0.999</td><td rowspan=1 colspan=1>Augmentation factor (ζ)</td><td rowspan=1 colspan=1>0.999</td></tr></table>

TABLE III

AVERAGE SENSING SNR [DB] OF VARIOUS SCHEMES WHEN THE NUMBER OF UAVS IS 4
<table><tr><td rowspan=1 colspan=1>Scheme</td><td rowspan=1 colspan=1>Average sensing SNR</td><td rowspan=1 colspan=1>Target sensing SNR</td></tr><tr><td rowspan=1 colspan=1>DeepLSC</td><td rowspan=1 colspan=1>1.12</td><td rowspan=1 colspan=1>1.00</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-CNE</td><td rowspan=1 colspan=1>1.24</td><td rowspan=1 colspan=1>1.00</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-CER</td><td rowspan=1 colspan=1>1.03</td><td rowspan=1 colspan=1>1.00</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-w</td><td rowspan=1 colspan=1>1.12</td><td rowspan=1 colspan=1>1.00</td></tr><tr><td rowspan=1 colspan=1>AC2</td><td rowspan=1 colspan=1>0.86</td><td rowspan=1 colspan=1>1.00</td></tr></table>

Section VI-E, we will further discuss the impact of different hyper-parameters on the performance of DeepLSC. In the simulation, the following schemes are considered:

• DeepLSC: This is our designed DRL-based ISAC scheme for supporting LAE.

DeepLSC-CNE: This scheme replaces the constrained noise-exploration policy with the conventional noiseexploration policy [39]. To meet the signal power constraint for communication and sensing, the scaling factor  is retained in the conventional noise-exploration policy.

• DeepLSC-CER: This scheme replaces the proposed hierarchical experience replay mechanism with the conventional experience replay mechanism [40].

• DeepLSC-w: This scheme removes the proposed symmetric experience augmentation mechanism to evaluate its effectiveness in DeepLSC.

• AC2: This scheme utilizes the actor-critic algorithm [36] with the constrained noise-exploration policy to optimize GBS’s beamforming and UAVs’ trajectories. Its basic elements, including state, action, and reward function, are exactly the same as DeepLSC. Furthermore, AC2 usually uses a single instantaneous experience set to train its DNN, instead of random historical experience sets.

3) Metric Setups: We consider 5000 episodes, each of which contains T time slots in which all UAVs fulfill the preset flight missions. The performance metrics include the communication sum-rate, the sensing SNR, and whether the flight missions of all UAVs are met. Specifically, the communication sum-rate at each episode is a short-term average, which is calculated by averaging $\scriptstyle \sum _ { t = 1 } ^ { T } \mathbf { R } _ { \mathrm { t o t a l } } ( t )$ over the previous 200 episodes; and the short-term average sensing SNR at each episode is calculated by averaging ${ \textstyle \sum _ { t = 1 } ^ { T } } \mathbf { S } \mathbf { N } \mathbf { R } _ { \mathrm { T a r } } ( t ) / T$ over the previous 200 episodes. To ensure the reliability of experiments, all simulations run 20 times to obtain the average result.

## B. Learning Curves

Fig. 3 and TABLE III provide the communication sumrate and average sensing SNR achieved by various schemes, respectively. As can be seen from Fig. 3, due to the random mobility of the target, all the curves are in fluctuation. In other words, in different episodes, the joint beamforming and trajectory strategies derived from the same scheme may be different. Fig. 4 depicts the flight trajectory of a specific UAV under various schemes in the last simulation episode.

![](images/775f683340831ae847094b65b92fd464774b76e0246896affe2b4e098ebb4efe.jpg)

Fig. 3. Communication sum-rate achieved by various schemes when the number of UAVs is 4.  
![](images/24359489094a31a41a446d50126eee0535878945b21365dd4562a6cc27109e3c.jpg)  
Fig. 4. Flight trajectory of a specific UAV under various schemes.

1) DeepLSC Versus DeepLSC-CNE: As presented in Fig. 3, among all the schemes, DeepLSC-CNE achieves the highest communication sum-rate while guaranteeing the given sensing SNR constraint. To be specific, compared with DeepLSC, the communication sum-rate gain of DeepLSC-CNE is around 11.14%. This is because DeepLSC-CNE is designed to maximize the communication sum-rate and satisfy the average sensing SNR requirement, while ignoring the flight mission constraint. As a result, under DeepLSC-CNE, UAVs tend to stay in a specific area instead of flying from initial locations to desired locations within each episode, as shown in Fig. 4. On the contrary, owing to the constrained noise-exploration policy, DeepLSC can well guide UAVs to reach their desired locations within an episode, although sacrificing both communication and sensing performance to some certain. This result demonstrates the effectiveness of the proposed constrained noise-exploration policy in fulfilling the flight mission.

2) DeepLSC Versus AC2: Similar to DeepLSC, AC2 employs the constrained noise-exploration policy to decide the movement directions of UAVs. It, however, not only fails to satisfy the given average sensing SNR requirement, but also achieves a much lower communication sum-rate than DeepLSC. In particular, compared with DeepLSC, the sumrate reduction of AC2 is more than 22.73%. The underlying reasons are as follows. First, before executing the constrained noise-exploration policy, DeepLSC derives a deterministic joint beamforming and trajectory decision, whereas AC2 usually generates a probability distribution corresponding to all possible actions and randomly samples an action from this distribution, resulting in inefficient decisions. Second, during DNN training, DeepLSC makes full use of random historical experience sets, but AC2 relies on a single instantaneous experience set. As a consequence, the parameters of the DNN are strongly correlated before and after the update, which reduces the efficiency of the decision-making [36]. Besides, in DeepLSC, the target-actor and target-critic are utilized to assist in training eval-actor and eval-critic, which further boosts the stability of the algorithm, whilst AC2 lacks this consideration.

3) DeepLSC Versus DeepLSC-CER: Unlike AC2, the underpinning algorithm in DeepLSC-CER is DDPG [37], which circumvents the above issues well. Thus, in comparison to AC2, while meeting the preset average sensing SNR requirement, DeepLSC-CER yields a significant communication sum-rate gain of about 15.88%. DeepLSC-CER, however, does not cater well to the formulated optimization problem. Specifically, the formulated optimization problem is an episode task, in the sense that all experiences generated within an episode should be jointly used to train the DNN. Unfortunately, the DNN training mechanism adopted in DeepLSC-CER, i.e., conventional experience replay [40], separately collects and utilizes the experiences from different time slots. The consequence is that all experiences generated within an episode cannot be guaranteed to appear in full during training. By contrast, benefiting from the hierarchical experience replay mechanism, DeepLSC is able to take advantage of experience sets, each composed of all experiences generated within an episode. Thus, DeepLSC can well handle the formulated problem and further improve the sum-rate of LAE-oriented ISAC systems: compared with DeepLSC-CER, the improvement attained by DeepLSC is about 11.68%.

4) DeepLSC Versus DeepLSC-w: From Fig. 3, it can also be found that DeepLSC-w experiences more episodes before convergence compared to DeepLSC, DeepLSC-CNE, and DeepLSC-CER, although they are all online learning schemes. <sup>4</sup> In particular, compared with the other three schemes, DeepLSC-w consumes over 130.60% more episodes to converge. The main reasons are below. In DeepLSC-w, the experience sets can only be obtained through interactions with the environment. In general, to efficiently train the DNN, a sufficient number of experience sets are essential. As a result, the learning process of the agent is slow. Unlike DeepLSC-w, based on the limited existing experience sets, DeepLSC, DeepLSC-CNE, and DeepLSC-CER schemes exploit the symmetric experience augmentation mechanism to enrich the available experience sets. Therefore, these three schemes can acquire massive experience sets in a short time, thereby significantly accelerating the convergence speed. On the other hand, in terms of communication and sensing performance, DeepLSC-w is the same as DeepLSC after convergence; and the UAV trajectories generated by the two are also similar, as provided in Fig. 4. This is because the proposed symmetric experience augmentation mechanism will not impair algorithm performance despite achieving faster convergence.

![](images/7d13551c623b49072593f75467cea4d9ac8f6e48d8052f8560c0a8a06f3c1d3f.jpg)  
Fig. 5. Sum-rate of various schemes under different numbers of UAVs.  
TABLE IV

PERFORMANCE OF VARIOUS SCHEMES IN SATISFYING THE AVERAGE SENSING SNR AND FLIGHT MISSION CONSTRAINTS UNDER DIFFER-ENT NUMBERS OF UAVS
<table><tr><td rowspan=1 colspan=5>Average sensing SNR constraint</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>M = 2</td><td rowspan=1 colspan=1>M = 3</td><td rowspan=1 colspan=1>M = 4</td><td rowspan=1 colspan=1>M = 5</td></tr><tr><td rowspan=1 colspan=1>DeepLSC</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-CNE</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-CER</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>×</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-w</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>AC2</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Flight</td><td rowspan=1 colspan=1>mission</td><td rowspan=1 colspan=1>constraint</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>M = 2</td><td rowspan=1 colspan=1>M = 3</td><td rowspan=1 colspan=1>M = 4</td><td rowspan=1 colspan=1>M = 5</td></tr><tr><td rowspan=1 colspan=1>DeepLSC</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-CNE</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-CER</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-w</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>AC2</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr></table>

## C. Robustness to Different Numbers of UAVs

This subsection evaluates the robustness of various schemes against different numbers of UAVs, in which M increases from 2 to 5 with a step size of 1. Fig. 5 and TABLE IV present the communication sum-rate and constraint satisfactory of various schemes, respectively.

It can be observed that as M increases, the communication sum-rate achieved by all schemes are gradually improved.

![](images/6fe84796e5be82e045637597c5dd8b5d7732c99c67775f2315ec4e1187e19c9c.jpg)  
Fig. 6. Communication sum-rate achieved by various schemes when the number of UAVs is 20.

TABLE V  
PERFORMANCE OF VARIOUS SCHEMES IN SATISFYING THE AVERAGE SENSING SNR AND FLIGHT MISSION CONSTRAINTS WHEN THE NUM-BER OF UAVS IS 20
<table><tr><td rowspan=1 colspan=5>Average sensing SNR constraint</td></tr><tr><td rowspan=1 colspan=1>DeepLSC</td><td rowspan=1 colspan=1>DeepLSC-CNE</td><td rowspan=1 colspan=1>DeepLSC-CER</td><td rowspan=1 colspan=1>DeepLSC-w</td><td rowspan=1 colspan=1>AC2</td></tr><tr><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>×</td></tr><tr><td rowspan=1 colspan=5>Flight mission constraint</td></tr><tr><td rowspan=1 colspan=1>DeepLSC</td><td rowspan=1 colspan=1>DeepLSC-CNE</td><td rowspan=1 colspan=1>DeepLSC-CER</td><td rowspan=1 colspan=1>DeepLSC-w</td><td rowspan=1 colspan=1>AC2</td></tr><tr><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr></table>

This is because when M increases, the GBS can support more parallel transmissions. At this time, under a reasonable beamforming design, spatial multiplexing can be further improved, thereby increasing the communication sum-rate. In addition, with the increase of M, the sum-rate gap between DeepLSC and DeepLSC-CER/AC2 increases. For example, when M increases from 2 to 5, the sum-rate gain of DeepLSC increases from 14.43 bps/Hz to 21.42 bps/Hz compared with DeepLSC-CER. On the other hand, as summarized in TABLE IV, due to the inefficient DNN training mechanism, both DeepLSC-CER and AC2 cannot always meet the average sensing SNR requirement under different values of M, whereas DeepLSC-CNE fails to fulfill the flight mission since it lacks the guidance of the constrained noise-exploration policy. Thus, among all the schemes, only DeepLSC and DeepLSC-w satisfy all constraints under various settings. DeepLSC-w, however, converges much slower than DeepLSC, as elaborated in Section VI-B. Overall, the above results exemplify that compared with other schemes, DeepLSC is more robust against different numbers of UAVs in LAE-oriented ISAC systems.

To further evaluate the scalability of DeepLSC when the number of UAVs, i.e., M, increases significantly, we consider a scenario where the GBS is equipped with 20 antennas to serve 20 UAVs and sense the randomly moving target. Fig. 6 and TABLE V show the communication sum-rate and constraint satisfactory of various schemes, respectively. As can be seen, although M is quite large, DeepLSC can still achieve much better overall system performance than other solutions. On the other hand, as presented in Section V-A, the computational complexity of DeepLSC increases linearly with the increase of M. In other words, as M increases, DeepLSC can achieve excellent communication and sensing performance without incurring too much additional computational overhead. The scalability of DeepLSC makes it highly favorable for realistic systems.

![](images/e3aafccc04db48e891dd1456a4dcdd17c2a45d58fbb6a0942c2995a8163e8114.jpg)  
Fig. 7. Sum-rate of various schemes under different numbers of time slots within a flight period.

TABLE VI  
PERFORMANCE OF VARIOUS SCHEMES IN SATISFYING THE AVERAGE SENSING SNR AND FLIGHT MISSION CONSTRAINTS UNDER DIFFER-ENT NUMBERS OF TIME SLOTS WITHIN A FLIGHT PERIOD
<table><tr><td rowspan=1 colspan=5>Average sensing SNR constraint</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1> $\overline { { T = 4 0 } }$ </td><td rowspan=1 colspan=1> $\overline { { T = 5 0 } }$ </td><td rowspan=1 colspan=1> $T = 6 0$ </td><td rowspan=1 colspan=1> $T = 7 0$ </td></tr><tr><td rowspan=1 colspan=1>DeepLSC</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-CNE</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-CER</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-w</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>AC2</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Flight</td><td rowspan=1 colspan=1>mission</td><td rowspan=1 colspan=1>constraint</td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1> $\overline { { T = 4 0 } }$ </td><td rowspan=1 colspan=1> $\overline { { T = 5 0 } }$ </td><td rowspan=1 colspan=1> $T = 6 0$ </td><td rowspan=1 colspan=1> $T = 7 0$ </td></tr><tr><td rowspan=1 colspan=1>DeepLSC</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-CNE</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>×</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-CER</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>DeepLSC-w</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>AC2</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr></table>

## D. Robustness to Different Numbers of Time Slots Within a Flight Period

This simulation evaluates the robustness of various schemes to different numbers of time slots within a flight period. In the considered flight area, the maximum possible flight distance of a UAV is calculated to be $\sqrt { ( 1 6 0 + 1 5 0 ) ^ { 2 } + ( 1 6 0 - 6 0 ) ^ { 2 } } =$ 325.73 m. Since the movement speed of UAVs is 10 m per time slot, a UAV needs at most 33 time slots to complete the maximum distance flight. In this regard, to ensure that the flight mission can be completed, we initialize T to 40 and increase it to 70 with a step size of 10. The communication sum-rate and constraint satisfactory of various schemes are shown in Fig. 7 and TABLE VI, respectively.

As expected, the communication sum-rate attained by various schemes improves monotonically as T increases. The main reasons are below. As T increases, the number of time slots during which all UAVs can fly freely without the flight mission constraint increases. In this regard, all schemes possess more time degrees of freedom to optimize the joint beamforming and trajectory strategy, so as to maximize the communication sum-rate while satisfying the average sensing SNR requirement. Besides, under different T, DeepLSC, DeepLSC-CER, and DeepLSC-w schemes can always satisfy all preset constraints, whilst both DeepLSC-CNE and AC2 fail. Thanks to a more intelligent and efficient strategy, DeepLSC achieves a higher communication sum-rate than DeepLSC-CER. To be specific, compared with DeepLSC-CER, DeepLSC yields a more than 11.68% sum-rate gain for all simulation setups.

More importantly, as T increases, the communication sumrate gap between DeepLSC and DeepLSC-CNE keeps almost unchanged, whereas that between DeepLSC and DeepLSC-CER/AC2 increases. In particular, when M increases from 40 to 70, the sum-rate improvement of DeepLSC increases (i) from 18.42 bps/Hz to 39.56 bps/Hz compared with DeepLSC-CER and (ii) from 40.03 bps/Hz to 76.63 bps/Hz compared with AC2. The above observations show that under different numbers of time slots within a flight period, DeepLSC is more robust than other schemes.

## E. Impact of Different Hyper-Parameters

The above simulation results have demonstrated the superiority of DeepLSC compared to other schemes. We now study the impact of different hyper-parameters on the performance of DeepLSC. In particular, the following hyper-parameters are considered: the learning rate of the eval-actor $\left( \alpha _ { \mathrm { a } } \right)$ , the learning rate of the eval-critic $( \alpha _ { \mathrm { c } } )$ , the update coefficient of the targetactor $\left( \chi _ { \mathrm { a } } \right)$ , the update coefficient of the target-critic $( \chi _ { \mathrm { c } } )$ , the size of the experience buffer (D), the size of the mini-batch $( N _ { \mathrm { e } } )$ , the augmentation factor (ζ), and the initial exploration variance and decay factor in the constrained noise-exploration policy $( \sigma _ { \mathrm { i n i t } }$ and κ). Under various simulation setups, DeepLSC can strictly satisfy the flight mission constraint through the constrained noise-exploration policy and thus this performance metric is omitted in this subsection. TABLE VII summarizes the communication sum-rate and sensing SNR constraint satisfactory of DeepLSC under different hyper-parameters.

It can be seen that among all the hyper-parameters, only the change of the augmentation factor ζ has no impact on the performance of DeepLSC. This is because ζ is employed to adjust the number of augmented experiences in the symmetric experience augmentation mechanism, which only affects the convergence of DeepLSC. Besides, the impact of other hyperparameters on the performance of DeepLSC is as follows.

• Impact of learning rates $\alpha _ { \mathrm { a } }$ and $\alpha _ { \mathrm { c } } \mathrm { : }$ According to [49], to enable the efficient learning of the agent, the learning rate of the eval-critic should be greater than that of the eval-actor. In addition, as shown in TABLE VII, when $\alpha _ { \mathrm { a } }$ and $\alpha _ { \mathrm { c } }$ are too small, DeepLCS learns slowly and fails to find an efficient solution. Increasing $\alpha _ { \mathrm { a } }$ and $\alpha _ { \mathrm { c } }$ gradually improves both communication and sensing performance. However, too large $\alpha _ { \mathrm { a } }$ and $\alpha _ { \mathrm { c } }$ result in overly aggressive learning, leading to sub-optimal policy convergence.

• Impact of update coefficients $\chi _ { \mathrm { a } }$ and $\chi _ { \mathrm { c } } \mathrm { : }$ As demonstrated in [49], the update coefficients of the target actor and the target critic are typically set to the same value. TABLE VII reveals that the performance change trend of DeepLSC under different update coefficients is the same as that under different learning rates. Besides, both $\chi _ { \mathrm { a } }$ and $\chi _ { \mathrm { c } }$ exhibit a stronger influence on the performance of DeepLSC compared to $\alpha _ { \mathrm { a } }$ and $\alpha _ { \mathrm { c } } .$

TABLE VII  
PERFORMANCE OF DEEPLSC IN COMMUNICATION SUM-RATE AND SATIS-FYING THE AVERAGE SENSING SNR CONSTRAINT UNDER DIFFERENT HYPER-PARAMETERS
<table><tr><td rowspan=1 colspan=1>αa</td><td rowspan=1 colspan=1>1e-6</td><td rowspan=1 colspan=1>1e-5</td><td rowspan=1 colspan=1>1e-4</td><td rowspan=1 colspan=1>1e-3</td></tr><tr><td rowspan=1 colspan=1>Sum-rate [× 1e2 bps/Hz]</td><td rowspan=1 colspan=1>1.67</td><td rowspan=1 colspan=1>1.71</td><td rowspan=1 colspan=1>1.76</td><td rowspan=1 colspan=1>1.58</td></tr><tr><td rowspan=1 colspan=1>Constraint (14c) is satisfied or not</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>×</td></tr><tr><td rowspan=1 colspan=1> $\alpha _ { \mathrm { c } }$ </td><td rowspan=1 colspan=1> $\overline { { 2 \mathrm { e } ^ { - 6 } } }$ </td><td rowspan=1 colspan=1> $\overline { { 2 \mathrm { e } \mathrm { - } 5 } }$ </td><td rowspan=1 colspan=1> $\overline { { 2 \mathrm { e } { - } 4 } }$ </td><td rowspan=1 colspan=1> $\overline { { 2 \mathrm { e } ^ { - 3 } } }$ </td></tr><tr><td rowspan=1 colspan=1>Sum-rate [×1e2 bps/Hz]</td><td rowspan=1 colspan=1>1.66</td><td rowspan=1 colspan=1>1.69</td><td rowspan=1 colspan=1>1.76</td><td rowspan=1 colspan=1>1.58</td></tr><tr><td rowspan=1 colspan=1>Constraint (14c) is satisfied or not</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>×</td></tr><tr><td rowspan=1 colspan=1>Xa</td><td rowspan=1 colspan=1>1e-5</td><td rowspan=1 colspan=1>1e-4</td><td rowspan=1 colspan=1>1e-3</td><td rowspan=1 colspan=1>1e-2</td></tr><tr><td rowspan=1 colspan=1>Sum-rate [× 1e2 bps/Hz]</td><td rowspan=1 colspan=1>1.65</td><td rowspan=1 colspan=1>1.69</td><td rowspan=1 colspan=1>1.76</td><td rowspan=1 colspan=1>1.56</td></tr><tr><td rowspan=1 colspan=1>Constraint (14c) is satisfied or not</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>×</td></tr><tr><td rowspan=1 colspan=1> $\chi _ { \mathrm { c } }$ </td><td rowspan=1 colspan=1>1e-5</td><td rowspan=1 colspan=1>1e-4</td><td rowspan=1 colspan=1>1e-3</td><td rowspan=1 colspan=1>1e-2</td></tr><tr><td rowspan=1 colspan=1>Sum-rate [× 1e2 bps/Hz]</td><td rowspan=1 colspan=1>1.64</td><td rowspan=1 colspan=1>1.68</td><td rowspan=1 colspan=1>1.76</td><td rowspan=1 colspan=1>1.54</td></tr><tr><td rowspan=1 colspan=1>Constraint (14c) is satisfied or not</td><td rowspan=1 colspan=1>了</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>×</td></tr><tr><td rowspan=1 colspan=1>D</td><td rowspan=1 colspan=1>1e2</td><td rowspan=1 colspan=1>1e3</td><td rowspan=1 colspan=1>2e3</td><td rowspan=1 colspan=1>5e3</td></tr><tr><td rowspan=1 colspan=1>Sum-rate [×1e2 bps/Hz]</td><td rowspan=1 colspan=1>1.56</td><td rowspan=1 colspan=1>1.70</td><td rowspan=1 colspan=1>1.76</td><td rowspan=1 colspan=1>1.74</td></tr><tr><td rowspan=1 colspan=1>Constraint (14c) is satisfied or not</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1> $\overline { { N _ { \mathrm { e } } } }$ </td><td rowspan=1 colspan=1>16</td><td rowspan=1 colspan=1>32</td><td rowspan=1 colspan=1>64</td><td rowspan=1 colspan=1>128</td></tr><tr><td rowspan=1 colspan=1>Sum-rate [×1e2 bps/Hz]</td><td rowspan=1 colspan=1>1.52</td><td rowspan=1 colspan=1>1.66</td><td rowspan=1 colspan=1>1.76</td><td rowspan=1 colspan=1>1.76</td></tr><tr><td rowspan=1 colspan=1>Constraint (14c) is satisfied or not</td><td rowspan=1 colspan=1>×</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>ζ</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>0.99</td><td rowspan=1 colspan=1>0.999</td><td rowspan=1 colspan=1>0.9999</td></tr><tr><td rowspan=1 colspan=1>Sum-rate [×1e2 bps/Hz]</td><td rowspan=1 colspan=1>1.76</td><td rowspan=1 colspan=1>1.76</td><td rowspan=1 colspan=1>1.76</td><td rowspan=1 colspan=1>1.76</td></tr><tr><td rowspan=1 colspan=1>Constraint (14c) is satisfied or not</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>σinit</td><td rowspan=1 colspan=1>0.3</td><td rowspan=1 colspan=1>0.6</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>1.2</td></tr><tr><td rowspan=1 colspan=1>Sum-rate [× 1e2 bps/Hz]</td><td rowspan=1 colspan=1>1.63</td><td rowspan=1 colspan=1>1.69</td><td rowspan=1 colspan=1>1.76</td><td rowspan=1 colspan=1>1.75</td></tr><tr><td rowspan=1 colspan=1>Constraint (14c) is satisfied or not</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>κ</td><td rowspan=1 colspan=1>0.9</td><td rowspan=1 colspan=1>0.99</td><td rowspan=1 colspan=1>0.999</td><td rowspan=1 colspan=1>0.9999</td></tr><tr><td rowspan=1 colspan=1>Sum-rate [× 1e2 bps/Hz]</td><td rowspan=1 colspan=1>1.64</td><td rowspan=1 colspan=1>1.71</td><td rowspan=1 colspan=1>1.76</td><td rowspan=1 colspan=1>1.75</td></tr><tr><td rowspan=1 colspan=1>Constraint (14c) is satisfied or not</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr></table>

• Impact of the experience buffer size D: A too small value of D causes high sample correlation, thus reducing the training efficiency. In this case, the communication sumrate decreases and the sensing SNR constraint cannot be met. Instead, a too large value of D results in too old experiences used in training, negatively impacting the agent’s learning.

• Impact of the mini-batch size $N _ { \mathrm { e } } \mathrm { : }$ : When $N _ { \mathrm { e } }$ is small, the experiences used for training lacks diversity, causing DNN overfitting. As $N _ { \mathrm { e } }$ increases, the communication and sensing performance of DeepLSC is improved, but it incurs high computational overhead.

• Impact of the initial exploration variance $\sigma _ { \mathrm { i n i t } } \colon \mathrm { I f } ~ \sigma _ { \mathrm { i n i t } }$ is too small, the agent fails to adequately explore different strategies, thus converging to sub-optimal solutions. On the contrary, an excessively large $\sigma _ { \mathrm { i n i t } }$ causes persistent exploration, which prevents the agent from efficiently utilizing learned strategies.

• Impact of the exploration decay factor κ: Similar to $\sigma _ { \mathrm { i n i t } } .$ κ balances exploration and exploitation. As shown in TABLE VII, κ should be close to 1.0 (e.g., 0.999) to gradually reduce the exploration variance and prevent premature exploration termination. However, an excessively large κ hinders the agent from using learned strategies.

Overall, different hyper-parameters affect the performance of DeepLSC to varying degrees. Among them, the learning rates $( \alpha _ { \mathrm { a } }$ and $\alpha _ { \mathrm { c } } )$ , update coefficients $( \chi _ { \mathrm { a } }$ and $\chi _ { \mathrm { c } } )$ , experience buffer size (D), and mini-batch size $( N _ { \mathrm { e } } )$ demonstrate particularly significant influence compared to other hyper-parameters.

## VII. CONCLUSION

This paper put forth a new ISAC scheme for LAE, termed DeepLSC, based on the DRL technique. By jointly optimizing GBS’s beamforming and UAVs’ trajectories, DeepLSC aims to maximize the expected communication sum-rate over the flight period, subject to the average sensing SNR requirement, flight mission, collision avoidance, and maximum transmit power constraints. DeepLSC, on the one hand, is model-free since it does not require prior mobility information of the target; on the other hand, it is capable of episode tasks thanks to an appropriate structural design. First, to meet various constraints, a constrained noise-exploration policy and a reward function were judiciously designed in DeepLSC for action selection and action evaluation, respectively. Thereafter, we developed a hierarchical experience replay mechanism for DNN training, where all experiences within an episode are jointly utilized to enable DeepLSC to efficiently learn from episode tasks. Besides, to promote the convergence speed of DeepLSC, a symmetric experience augmentation mechanism was further proposed. Simulation results demonstrated compared with other schemes, DeepLSC (i) yields a much higher communication sum-rate while meeting all constraints, (ii) converges faster, and (iii) is more robust against different settings.

In the current work, we focused on maximizing the communication sum-rate under the constraints of flight mission, collision avoidance, and average sensing SNR. However, in realistic systems, the energy of UAVs is typically limited. Therefore, how to minimize the energy consumption of UAVs is also a crucial issue in LAE-oriented ISAC systems. Generally, there is a fundamental trade-off between communication sum-rate maximization and UAV energy consumption minimization. In our future work, a new LAE-oriented ISAC scheme will be designed to balance these two conflicting objectives.

## REFERENCES

[1] Y. Jiang et al., “6G non-terrestrial networks enabled low-altitude economy: Opportunities and challenges,” 2023, arXiv:2311.09047.

[2] China Telecom, Ericsson, Nokia, Huawei, ZTE, CICT Mobile, OPPO, Xiaomi, vivo, Lenovo, Qualcomm, Mediatek, UNISOC,. (2024). The Low-altitude Network By Integrated Sensing and Communication. [Online]. Available: https://www.zte.com.cn/content/dam/zte-site/ res-www-zte-com-cn/mediares/zte/%E6%97%A0%E7%BA%BF% E6%8E%A5%E5%85%A5/%E7%99%BD%E7%9A% AE%E4%B9%A6/Low altitude network by ISAC.pdf

[3] J. Mu, R. Zhang, Y. Cui, N. Gao, and X. Jing, “UAV meets integrated sensing and communication: Challenges and future directions,” IEEE Commun. Mag., vol. 61, no. 5, pp. 62–67, May 2023.

[4] F. Liu et al., “Integrated sensing and communications: Toward dualfunctional wireless networks for 6G and beyond,” IEEE J. Sel. Areas Commun., vol. 40, no. 6, pp. 1728–1767, Jun. 2022.

[5] K. Zhang and C. Shen, “UAV aided integrated sensing and communications,” in Proc. IEEE 94th Veh. Technol. Conf. (VTC-Fall), Sep. 2021, pp. 1–6.

[6] S. Zhang, H. Zhang, Z. Han, H. V. Poor, and L. Song, “Age of information in a cellular Internet of UAVs: Sensing and communication trade-off design,” IEEE Trans. Wireless Commun., vol. 19, no. 10, pp. 6578–6592, Oct. 2020.

[7] X. Wang, Z. Fei, J. A. Zhang, J. Huang, and J. Yuan, “Constrained utility maximization in dual-functional radar-communication multi-UAV networks,” IEEE Trans. Commun., vol. 69, no. 4, pp. 2660–2672, Apr. 2021.

[8] B. Chang, W. Tang, X. Yan, X. Tong, and Z. Chen, “Integrated scheduling of sensing, communication, and control for mmWave/THz communications in cellular connected UAV networks,” IEEE J. Sel. Areas Commun., vol. 40, no. 7, pp. 2103–2113, Jul. 2022.

[9] W. Ding et al., “Multi-UAV-Enabled integrated sensing and communications: Joint UAV placement and power control,” in Proc. IEEE Globecom Workshops, Dec. 2023, pp. 842–847.

[10] G. Abdissa Bayessa, R. Chai, C. Liang, D. Kumar Jain, and Q. Chen, “Joint UAV deployment and precoder optimization for multicasting and target sensing in UAV-assisted ISAC networks,” IEEE Internet Things J., vol. 11, no. 20, pp. 33392–33405, Oct. 2024.

[11] X. Yu, J. Xu, N. Zhao, X. Wang, and D. Niyato, “Security enhancement of ISAC via IRS-UAV,” IEEE Trans. Wireless Commun., vol. 23, no. 10, pp. 15601–15612, Jul. 2024.

[12] J. Wu, W. Yuan, and L. Hanzo, “When UAVs meet ISAC: Realtime trajectory design for secure communications,” IEEE Trans. Veh. Technol., vol. 71, no. 12, pp. 16766–16771, Dec. 2023.

[13] S. Hu, X. Yuan, W. Ni, and X. Wang, “Trajectory planning of cellular-connected UAV for communication-assisted radar sensing,” IEEE Trans. Commun., vol. 70, no. 9, pp. 6385–6396, Sep. 2022.

[14] Y. Liu, S. Liu, X. Liu, Z. Liu, and T. S. Durrani, “Sensing fairnessbased energy efficiency optimization for uav enabled integrated sensing and communication,” IEEE Wireless Commun. Lett., vol. 12, no. 10, pp. 1702–1706, Oct. 2023.

[15] Z. Liu, X. Liu, Y. Liu, V. C. M. Leung, and T. S. Durrani, “UAV assisted integrated sensing and communications for Internet of Things: 3D trajectory optimization and resource allocation,” IEEE Trans. Wireless Commun., vol. 23, no. 8, pp. 8654–8667, Jan. 2024.

[16] Y. Liu et al., “Secure rate maximization for ISAC-UAV assisted communication amidst multiple eavesdroppers,” IEEE Trans. Veh. Technol., vol. 73, no. 10, pp. 15843–15847, Jun. 2024.

[17] J. Zhang, J. Xu, W. Lu, N. Zhao, X. Wang, and D. Niyato, “Secure transmission for IRS-aided UAV-ISAC networks,” IEEE Trans. Wireless Commun., vol. 23, no. 9, pp. 12256–12269, Apr. 2024.

[18] X. Jing, F. Liu, C. Masouros, and Y. Zeng, “ISAC from the sky: UAV trajectory design for joint communication and target localization,” IEEE Trans. Wireless Commun., vol. 23, no. 10, pp. 12857–12872, Oct. 2024.

[19] K. Meng, Q. Wu, S. Ma, W. Chen, K. Wang, and J. Li, “Throughput maximization for UAV-enabled integrated periodic sensing and communication,” IEEE Trans. Wireless Commun., vol. 22, no. 1, pp. 671–687, Jan. 2023.

[20] K. Meng, Q. Wu, S. Ma, W. Chen, and T. Q. S. Quek, “UAV trajectory and beamforming optimization for integrated periodic sensing and communication,” IEEE Wireless Commun. Lett., vol. 11, no. 6, pp. 1211–1215, Jun. 2022.

[21] Z. Lyu, G. Zhu, and J. Xu, “Joint maneuver and beamforming design for UAV-enabled integrated sensing and communication,” IEEE Trans. Wireless Commun., vol. 22, no. 4, pp. 2424–2440, Apr. 2023.

[22] Z. Wu, X. Li, Y. Cai, and W. Yuan, “Joint trajectory and resource allocation design for RIS-assisted UAV-enabled ISAC systems,” IEEE Wireless Commun. Lett., vol. 13, no. 5, pp. 1384–1388, May 2024.

[23] C. Deng, X. Fang, and X. Wang, “Beamforming design and trajectory optimization for UAV-empowered adaptable integrated sensing and communication,” IEEE Trans. Wireless Commun., vol. 22, no. 11, pp. 8512–8526, Nov. 2023.

[24] T. V. Chien, M. D. Cong, N. C. Luong, T. Nhu, D. I. Kim, and S. Chatzinotas, “Joint computation offloading and target tracking in integrated sensing and communication enabled UAV networks,” IEEE Commun. Lett., vol. 28, no. 6, pp. 1327–1331, Apr. 2024.

[25] J. Wu, W. Yuan, and L. Bai, “On the interplay between sensing and communications for UAV trajectory design,” IEEE Internet Things J., vol. 10, no. 23, pp. 20383–20395, Dec. 2023.

[26] R. Zhang, Y. Zhang, R. Tang, H. Zhao, Q. Xiao, and C. Wang, “A joint UAV trajectory, user association, and beamforming design strategy for multi-UAV assisted ISAC systems,” IEEE Internet Things J., vol. 11, no. 8, pp. 29360–29374, Jul. 2024.

[27] T. Zhang, K. Zhu, S. Zheng, D. Niyato, and N. C. Luong, “Trajectory design and power control for joint radar and communication enabled multi-UAV cooperative detection systems,” IEEE Trans. Commun., vol. 71, no. 1, pp. 158–172, Jan. 2023.

[28] Z. Xie, Z. Wang, Z. Zhang, J. Wang, Z. Jiang, and Z. Han, “Distributed UAV swarm for device-free integrated sensing and communication relying on multi-agent reinforcement learning,” IEEE Trans. Veh. Technol., vol. 73, no. 12, pp. 19925–19930, Aug. 2024.

[29] X. Chen, X. Cao, L. Xie, and Y. He, “DRL-based joint trajectory planning and beamforming optimization in aerial RIS-assisted ISAC system,” in Proc. IEEE Int. Workshop Radio Freq. Antenna Technol. (iWRF&AT), Shenzhen, China, May 2024, pp. 510–515.

[30] H. Cho, S. Yoo, B. C. Jung, and J. Kang, “Enhancing battlefield awareness: An aerial RIS-assisted ISAC system with deep reinforcement learning,” in Proc. IEEE MILCOM, Washington, DC, USA, Dec. 2024, pp. 469–474.

[31] G. Fontanesi et al., “A deep-NN beamforming approach for dual function radar-communication THz UAV,” IEEE Trans. Veh. Technol., vol. 74, no. 1, pp. 746–760, Sep. 2024.

[32] Y. Qin, Z. Zhang, X. Li, W. Huangfu, and H. Zhang, “Deep reinforcement learning based resource allocation and trajectory planning in integrated sensing and communications UAV network,” IEEE Trans. Wireless Commun., vol. 22, no. 11, pp. 8158–8169, Nov. 2023.

[33] C. Dai, T. Wu, G. Sun, Y. Zuo, Z. Guo, and F. Xiao, “Joint UAV trajectory and beamforming design for RIS-aided integrated sensing and communication system,” in Proc. IEEE INFOCOM Workshops, Vancouver, BC, Canada, May 2024, pp. 01–06.

[34] Y. Cui et al., “Specific beamforming for multi-UAV networks: A dual identity-based ISAC approach,” in Proc. IEEE ICC, Rome, Italy, May 2023, pp. 4979–4985.

[35] G. Cheng, X. Song, Z. Lyu, and J. Xu, “Networked ISAC for low-altitude economy: Coordinated transmit beamforming and UAV trajectory design,” IEEE Trans. Commun., early access, Feb. 11, 2025, doi: 10.1109/TCOMM.2025.3541027.

[36] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction. Cambridge, MA, USA: MIT Press, 2018.

[37] V. Mnih et al., “Human-level control through deep reinforcement learning,” Nature, vol. 518, no. 7540, pp. 529–533, Feb. 2015.

[38] X. Ye, Y. Yu, and L. Fu, “Multi-channel opportunistic access for heterogeneous networks based on deep reinforcement learning,” IEEE Trans. Wireless Commun., vol. 21, no. 2, pp. 794–807, Feb. 2022.

[39] T. Lillicrap et al., “Continuous control with deep reinforcement learning,” in Proc. Int. Conf. Learn. Represent., May 2016, pp. 1–14.

[40] L.-J. Lin, “Self-improving reactive agents based on reinforcement learning, planning and teaching,” Mach. Learn., vol. 8, no. 3, pp. 293–321, May 1992.

[41] H. Tabassum, M. Salehi, and E. Hossain, “Fundamentals of mobilityaware performance characterization of cellular networks: A tutorial,” IEEE Commun. Surveys Tuts., vol. 21, no. 3, pp. 2288–2308, 3rd Quart., 2019.

[42] R. S. Sutton, D. McAllester, S. Singh, and Y. Mansour, “Policy gradient methods for reinforcement learning with function approximation,” in Proc. Adv. Neural Inf. Process. Syst., Nov. 1999, pp. 1057–1063.

[43] K. Cho et al., “Learning phrase representations using RNN encoder–decoder for statistical machine translation,” in Proc. EMNLP, Sep. 2014, pp. 1724–1734.

[44] I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning. Cambridge, MA, USA: MIT Press, 2016.

[45] A. Seress,<sup>´</sup> Permutation Group Algorithms. Cambridge, U.K.: Cambridge Univ. Press, 2003.

[46] P. Wang et al., “Decentralized navigation with heterogeneous federated reinforcement learning for UAV-enabled mobile edge computing,” IEEE Trans. Mob. Comput., vol. 23, no. 12, pp. 13621–13638, Aug. 2024.

[47] X. Ye, Y. Mao, X. Yu, and L. Fu, “Intelligent omni-surfaceaided integrated sensing and communications based on deep reinforcement learning with knowledge transfer,” IEEE Trans. Wireless Commun., vol. 24, no. 5, pp. 4344–4360, May 2025, doi: 10.1109/ TWC.2025.3542780.

[48] F. Chollet. (2018). Keras: The Python Deep Learning Library. [Online]. Available: https://keras.io

[49] Y. Duan, X. Chen, R. Houthooft, J. Schulman, and P. Abbeel, “Benchmarking deep reinforcement learning for continuous control,” in Proc. Int. Conf. Mach. Learn., Jun. 2016, pp. 1329–1338.

![](images/b4c9e8a95b454066d78752022458d6c1e8224b55b81a3c7c9883e8367df3072a.jpg)

Xiaowen Ye received the Ph.D. degree in communication and information systems from Xiamen University, Xiamen, China, in 2024. He was a Post-Doctoral Research Fellow with the Department of Electrical Engineering, City University of Hong Kong, from 2024 to 2025. He is an Associate Professor with the College of Photonic and Electronic Engineering, Fujian Normal University, China. His research interests include deep reinforcement learning, wireless network optimization, and dynamic resource allocation.

![](images/7885f6ecf7570e1d06ac68738984135aa22dacf9ab26160887c555513f5c8261.jpg)

Yuyi Mao (Senior Member, IEEE) received the B.Eng. degree in information and communication engineering from Zhejiang University (ZJU), Hangzhou, China, in 2013, and the Ph.D. degree in electronic and computer engineering from The Hong Kong University of Science and Technology (HKUST), Hong Kong, in 2017. He was a Lead Engineer with The Hong Kong Applied Science and Technology Research Institute Company Ltd. (ASTRI), Hong Kong, a Senior Researcher with the Theory Lab, 2012 Labs, Huawei Tech. Investment

Co., Ltd., Hong Kong, and a Research Assistant Professor with the Department of Electrical and Electronic Engineering, The Hong Kong Polytechnic University (PolyU), Hong Kong. He is currently an Assistant Professor with the School of Computer Science and Engineering, Macau University of Science and Technology (MUST), Macau. His research interests include wireless communications and networking, mobile edge computing and learning, and wireless artificial intelligence.

Dr. Mao was a recipient of the 2021 IEEE Communications Society Best Survey Paper Award and the 2019 IEEE Communications Society and Information Theory Society Joint Paper Award. He was also recognized as an Exemplary Reviewer of the IEEE WIRELESS COMMUNICATIONS LETTERS in 2019 and 2021 and IEEE TRANSACTIONS ON COMMUNICATIONS in 2020. He is an Editor of the IEEE WIRELESS COMMUNICATIONS LETTERS, an Associate Editor of IEEE TRANSACTIONS ON MOBILE COMPUTING, the EURASIP Journal on Wireless Communications and Networking, and the HKIE Transactions.

![](images/37098f03d2184c38ac38a082e448a682af4cc98e2b0c452a06e65079e08ddd2a.jpg)

Xianghao Yu (Senior Member, IEEE) received the B.Eng. degree in information engineering from Southeast University, Nanjing, China, in 2014, and the Ph.D. degree in electronic and computer engineering from The Hong Kong University of Science and Technology (HKUST), Hong Kong, China, in 2018.

He is currently an Assistant Professor with the Department of Electrical Engineering, City University of Hong Kong (CityU), Hong Kong, China. From 2018 to 2020, he was a Humboldt Post-

Doctoral Research Fellow with the Institute for Digital Communications, Friedrich-Alexander University of Erlangen-Nuremberg (FAU), Erlangen, Germany. Before joining CityU, he was a Research Assistant Professor with the Department of Electronic and Computer Engineering, HKUST. He has coauthored the book Stochastic Geometry Analysis of Multi-Antenna Wireless Networks (Springer, 2019). His research interests include intelligent reflecting surface-assisted communications, integrated sensing and communications, near-field communications, and wireless artificial intelligence.

Dr. Yu received the IEEE Global Communications Conference (GLOBE-COM) 2017 Best Paper Award, the 2018 IEEE Signal Processing Society Young Author Best Paper Award, the IEEE GLOBECOM 2019 Best Paper Award, the 2023 IEEE Communications Society Leonard G. Abraham Prize, and the 2024 IEEE ComSoc Asia-Pacific Outstanding Young Researcher Award. He is the Symposium Co-Chair of the IEEE ICC 2026 Wireless Communications Symposium and serves as the Secretary for the IEEE Wireless Communications Technical Committee (WTC). He was also recognized as an Exemplary Reviewer of IEEE TRANSACTIONS ON WIRELESS COMMUNICA-TIONS in 2017 and 2018 and IEEE TRANSACTIONS ON COMMUNICATIONS in 2021 and 2022. He is an Editor of IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE TRANSACTIONS ON MOBILE COMPUTING, and IEEE COMMUNICATIONS LETTERS. He was listed as the World’s Top 2% Scientist by Stanford University from 2020 to 2023.

![](images/f336f41acab25ad1e93266bb0cb96a19d4cee56049c976c3021d483062eea0f3.jpg)

Shu Sun (Senior Member, IEEE) received the B.S. degree in applied physics from Shanghai Jiao Tong University (SJTU), China, in 2012, and the Ph.D. degree in electrical engineering from New York University, USA, in 2018. She held summer internship positions at Nokia Bell Labs in 2014 and 2015. She was a Systems Engineer at Intel Corporation. She is a tenure-track Associate Professor with the School of Information Science and Electronic Engineering, SJTU. Her current research interests include channel modeling, millimeter-wave communications, integrated sensing and communication, and holographic MIMO. She received multiple international academic awards, including the 2023 and 2017 IEEE Neil Shepherd Memorial Best Propagation Paper Awards, the 2017 Marconi Society Young Scholar Award, the IEEE VTC2016-Spring Best Paper Award, and the 2015 IEEE Donald G. Fink Award. She is an Associate Editor or Guest Editor of IEEE TRANSACTIONS ON MOBILE COMPUTING, IEEE Internet of Things Magazine, and IEEE OPEN JOURNAL OF ANTENNAS AND PROPAGATION. She also served as a Guest Editor for the IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS.

![](images/e3f34d36913e37b970cd2d205a99dccedf40767056fcec06c21d827f8f08a458.jpg)

Liqun Fu (Senior Member, IEEE) received the Ph.D. degree in information engineering from The Chinese University of Hong Kong in 2010.

She was a Post-Doctoral Research Fellow with the Institute of Network Coding, The Chinese University of Hong Kong, from 2011 to 2013, and the ACCESS Linnaeus Centre, KTH Royal Institute of Technology, from 2013 to 2015. She was with ShanghaiTech University as an Assistant Professor from 2015 to 2016. She is a Full Professor with the School of Informatics, Xiamen University, China. Her research interests are mainly in communication theory, optimization theory, game theory, and learning theory, with applications in wireless networks. She also serves as a TPC Member for many leading conferences in communications and networking, such as the IEEE INFOCOM, ICC, and GLOBECOM. She served as the Technical Program Co-Chair for IEEE/CIC ICCC 2021 and the GCCCN Workshop of the IEEE INFOCOM 2014, the Publicity Co-Chair for the GSNC Workshop of the IEEE INFOCOM 2016, and the Web Chair for the IEEE WiOpt 2018. She is on the Editorial Board of IEEE TRANSACTIONS ON MOBILE COMPUTING (TMC), IEEE COMMUNICATIONS LETTERS, and the Journal of Communications and Information Networks (JCIN).

![](images/1ee10c06a18228209bddd0cc86eef830ab6aa514e5524d114b098044248538af.jpg)

Jie Xu (Fellow, IEEE) received the B.E. and Ph.D. degrees from the University of Science and Technology of China. He is currently an Associate Professor (Tenured) with the School of Science and Engineering, Shenzhen Future Network of Intelligence Institute (FNii-Shenzhen), and Guangdong Provincial Key Laboratory of Future Networks of Intelligence, The Chinese University of Hong Kong, Shenzhen. His research interests include wireless communications, wireless information and power transfer, UAV communications, edge computing and

intelligence, and integrated sensing and communication (ISAC). He was a recipient of the 2017 IEEE Signal Processing Society Young Author Best Paper Award, the IEEE/CIC ICCC 2019 Best Paper Award, the 2019 IEEE Communications Society Asia-Pacific Outstanding Young Researcher Award, and the 2019 Wireless Communications Technical Committee Outstanding Young Researcher Award. He is the Symposium Co-Chair of the IEEE GLOBECOM 2019 Wireless Communications Symposium and the IEEE ICC 2025 Communication Theory Symposium, the workshop co-chair of several IEEE ICC and GLOBECOM workshops, the Tutorial Co-Chair of the IEEE/CIC ICCC 2019/2022, the Chair of the IEEE Wireless Communications Technical Committee (WTC), and the Vice Co-Chair of the IEEE Emerging Technology Initiative (ETI) on ISAC. He served or is serving as an Associate Editor-in-Chief for IEEE TRANSACTIONS ON MOBILE COMPUTING; an Editor for IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS, IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE WIRELESS COMMUNICA-TIONS LETTERS, and Journal of Communications and Information Networks; an Associate Editor for IEEE ACCESS; and a Guest Editor for the IEEE WIRELESS COMMUNICATIONS, IEEE JOURNAL ON SELECTED AREAS IN COMMUNICATIONS, IEEE Internet of Things Magazine, Science China Information Sciences, and China Communications. He is a Distinguished Lecturer of IEEE Communications Society.