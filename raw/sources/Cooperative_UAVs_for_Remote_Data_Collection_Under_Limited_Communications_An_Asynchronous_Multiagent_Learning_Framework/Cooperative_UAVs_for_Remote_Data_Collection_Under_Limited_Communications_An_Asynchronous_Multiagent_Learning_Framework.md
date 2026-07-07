# Cooperative UAVs for Remote Data Collection Under Limited Communications: An Asynchronous Multiagent Learning Framework

Cuong Le , Symeon Chatzinotas , Fellow, IEEE, and Thang X. Vu , Senior Member, IEEE

Abstract—This paper addresses the joint optimization of trajectories and bandwidth allocation for multiple Unmanned Aerial Vehicles (UAVs) to enhance energy efficiency in the cooperative data collection problem. We focus on an important yet underestimated aspect of the system, where action synchronization across all UAVs is impossible. Since most existing learning-based solutions are not designed to learn in this asynchronous environment, we formulate the trajectory planning problem as a Decentralized Partially Observable Semi-Markov Decision Process and introduce an asynchronous multi-agent learning algorithm to learn UAVs’ cooperative policies. Once the UAVs’ trajectory policies are learned, the bandwidth allocation can be optimally solved based on local observations at each collection point. Comprehensive empirical results demonstrate the superiority of the proposed method over other learningbased and heuristic baselines in terms of both energy efficiency and mission completion time. Additionally, the learned policies exhibit robustness under varying environmental conditions.

Index Terms—Asynchronous multiagent systems, cooperative multiagent systems, data collection.

## I. INTRODUCTION

have paved the way for efficient and scalable deployment of Unmanned Aerial Vehicles (UAVs) in real-life applications. Sectors such as agriculture, environmental monitoring, and disaster management increasingly rely on UAVs to collect data quickly and reliably, thanks to their accessibility and highly probable line-of-sight links to ground terminals. For example, UAVs can be used to regularly collect sensory information of the crop conditions in smart agriculture, or monitoring information of windmills in a windfarm. However, distributed autonomous decision-making and efficient cooperation under limited onboard energy remain critical challenges that must be addressed to maximize the potential of UAVs and ensure their sustainable use.

As future network generations promise unparalleled capabilities, including AI-driven automation, multiagent reinforcement learning (MARL) has emerged as a key approach to addressing the above challenges. With its ability to adapt to dynamic environments and enable autonomous collaboration, MARL is increasingly applied to a wide range of UAV cooperative planning problems [2], [3], [4], [5], [6]. However, most existing MARL-based solutions assume that all UAVs are well-synchronized, in the sense that they all make decisions at the same time. While this assumption simplifies algorithm design, it is difficult to achieve in real-world environments for several reasons: i) different UAVs naturally require varying amounts of time to complete their actions; ii) forcing UAVs to wait for one another wastes time and system resources; iii) achieving synchronization across all UAVs requires extensive control signaling, either among agents or between agents and an intermediary medium; and iv) even with an effective synchronization mechanism, unexpected signaling delays or hardware issues can still disrupt synchronization. Moreover, timing mismatches can directly undermine the performance of policies learned under synchronous assumptions. For instance, UAVs may be required to meet periodically to exchange information or confirm task completion. If their actions are not perfectly aligned, they may fail to meet as planned, leading to overlapping exploration, inefficient waiting cycles, or, in the worst case, a complete breakdown of the learned policy. Addressing asynchronous decision-making is therefore crucial for extending MARL solutions beyond laboratory simulations and making them viable in physical environments. Despite its significance, to the best of our knowledge, asynchronous decision-making in wireless communications, specifically in multi-UAV planning, has not yet been examined.

In this study, we consider the joint optimization problem of UAVs’ trajectories and bandwidth allocation at each data collection point to maximize the overall energy efficiency. Our work stands out from existing studies by focusing on an overlooked aspect of the system, where UAVs have to make decisions independently, without time synchronization with one another. This is motivated by the fact that different collection points have varying amounts of data and different transmission channel qualities. As a result, the time required for data collection at each of these points naturally varies. Additionally, since UAVs operate in remote areas with limited inter-UAV communication, synchronizing actions across all UAVs at every step is impossible. The contributions of this paper are as follows:

We consider the UAV-assisted data collection problem under practical conditions: i) the location of available data points and the data size are random and unknown in advance; and ii) different collection points have varying amounts of data and transmission channel qualities, resulting in different time requirements at each point. Under these conditions, offline optimization approaches are infeasible, and online solutions must equip the UAVs with the capability to make decisions asynchronously.

• We introduce a learning-based solution, where the problem is decomposed into two subproblems: trajectory optimization and bandwidth allocation at each hovering point. While bandwidth allocation can be solved independently by each UAV at each hovering point using any convex optimizer, trajectory optimization is more challenging as it requires UAVs to collaborate without explicit time synchronization. To tackle this challenge, we transform it into a Decentralized Partially Observable Semi-Markov Decision Process (Dec-POSMDP), which allows for varying action durations. We then propose Asynchronous-QMIX, a MARL algorithm specifically designed for asynchronous environments. Our algorithm is based on QMIX algorithm [7] - one of the state-of-theart MARL algorithms for synchronous environments. We theoretically show that under our asynchronous setting, local deterministic greedy policies remain applicable for UAVs, as long as a monotonic relationship between the global Q-value and local utility values holds. Additionally, we also introduce a state downsampling technique to reduce the state space and enhance the scalability of the proposed algorithm.

Extensive experiments are conducted to validate the effectiveness of the proposed method. The numerical results show that our solution outperforms existing learningbased and heuristic solutions. Moreover, the policies learned by our algorithm also demonstrated robust performance under varying environmental conditions.

The rest of this paper is organized as follows. Section II provides a brief review of existing studies and their limitations. Section III introduces the system model and problem formulation. Section IV presents the formulation of the trajectory optimization problem as a Dec-POSMDP. Section V presents the Asynchronous-QMIX algorithm for asynchronous environments. Section VI optimizes the bandwidth allocation under imperfect channel state information. Performance evaluation and discussions are presented in Section VII. Finally, conclusions and future work are drawn in Section VIII.

Notations: we use superscripts n, c, and i to indicate the indices of UAVs, cells, and sensor nodes (SNs), respectively; square brackets [k] to index the individual decision-making steps of each UAV; and subscript m to index the joint global environment transition steps.

## II. RELATED WORK

Research on the deployment of UAVs for data collection has flourished in recent years, with a rich body of literature exploring a breadth of system configurations. Early research started with simple scenarios involving a single UAV, with static and deterministic assumptions, allowing traditional optimization approaches to be applied. Most studies focus on UAV trajectory planning and may jointly consider transmission scheduling [8], [9], [10], [11], [12], SN scheduling [9], bandwidth allocation [13], [14], power control [14], [15], [16]. The common objectives are mission completion time minimization [8], energy minimization at UAV or SNs [9], [10], data rate and total collected data maximization [11], [12], [15], outage probability [15] and Age-of-Information (AoI) [17] minimization. As missions spanning larger areas reveal the inadequacy of a single UAV, recent works turned the attention to multiple UAVs to meet the scaling requirements [18], [19], [20], [21], [22]. When the system scale becomes increasingly intricate, traditional optimization methods reveal limitations. Fortunately, reinforcement learning (RL), with its adaptability to complex and dynamic environments, can provide the flexibility needed to cope with practical scenarios. RL approach has been demonstrated as a potential solution for both single-UAV [23], [24], [25] as well as multiple-UAV systems [26], [27], [28], [29].

Despite the attainment of some promising results, there are still technical gaps separating the above studies from practical systems. In particular, studies often assume deterministic systems where either perfect channel state information (CSI) or data collection demand is known in advance at every possible UAV location [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], [21]. Meanwhile, learning-based studies [23], [24], [25], [26], [27], [28], [29] often assume that the central controller and UAVs have the capability to observe the entire collection area in real-time. While these assumptions may facilitate the applications of conventional optimization and learning algorithms, they are not in line with practical scenarios, specifically in the context of remote data collection.

Recent studies have made efforts to tackle the challenges of partial observability, where the problem is often formulated as a Decentralized Partially Observable Markov Decision Process (Dec-POMDP), to which a multi-agent reinforcement learning algorithm is applied. In [2], the authors consider the trajectory planning problem for homogeneous UAVs in dense urban areas to maximize the amount of collected data. The problem is formulated as a Dec-POMDP, and then solved by independent reinforcement learning algorithms in which UAVs have different reward functions and are trained independently, while the coordination between UAVs remains open. The authors of [3] consider two UAV groups, one for data collection and the other for energy transmission with the objectives of minimizing the AoI and maximizing the transmit energy. Therein, actor-critic algorithm is used to overcome the challenges of partial observability, where the centralized critic can access the global states of the environment during training. A similar AoI minimization problem is studied in [4] where the data generation time of SNs is unpredictable. Under the partial observation assumption, a multi-agent algorithm with value-decomposition network (VDN) is adopted to learn UAVs’ policies. In [5], PPO algorithm is employed to optimize UAVs’ trajectories, while UAV-user association is handled as a coalition formation game. The authors of [6] focus on optimizing UAVs’ speeds, directions, and SN-selection at each hovering point to minimize average AoI, while considering various practical kinematic constraints. The problem is formulated as a Dec-POMDP, on which the well-known QMIX algorithm is applied to learn UAVs’ policies. However, due to the representation of SNselection action, the action space grows exponentially in the number of SNs, resulting in poor scalability.

Although offering fairly comprehensive solutions, the above-mentioned works still heavily rely on a critical assumption regarding the synchronization of UAVs for the convenience of mathematical modeling and problem-solving. Specifically, the time evolution is discretized into equally small intervals, and all UAVs simultaneously make decisions at the beginning of each interval. This assumption, however, is very optimistic in real-world scenarios, especially with large areas of interest and limited inter-UAV communication range. Moreover, synchronous decision-making is time-inefficient, as simultaneous actions necessitate unnecessary waiting periods due to the varying nature of decision epochs among different UAVs. Furthermore, discretizing the timeline as described can be theoretically problematic, as the decision-making under Dec-POMDP is itself PSPACE-complete, and the complexity grows double-exponentially in the planning horizon [30]. In addition, the impacts of inter-UAV communications have been overlooked in existing studies. Given its practical feasibility, investigating inter-UAV communications during the mission is essential to enhance the cooperative tactics.

Regarding asynchronous RL, study [31] investigates a coordination problem for multiple robots in continuous environments. The original problem, formulated as a Dec-POMDP, is undecidable over continuous space without approximations or additional assumptions. To address this, the authors reformulate the problem as a Dec-POSMDP, where the original Dec-POMDP is approximated by a discrete environment with a finite number of asynchronous actions. Under Dec-POSMDP, Monte Carlo Search is used to explore sub-optimal policies. Unfortunately, this method is unsuitable for our work due to its inefficient sampling and inapplicability to non-deterministic environments, particularly when data collection demands are not precisely known beforehand. In [32], the authors tackle the problem of bus bunching, where buses arrive at stops too closely, disrupting their schedules. They formulate the bus fleet control problem as an asynchronous reinforcement learning problem and propose an extension of the MADDPG algorithm for asynchronous environments, enabling buses to make decisions independently as they reach stops at different times. Recently, the authors in [33] addressed the challenge of multiple robots collaboratively exploring unknown regions, with the objective of minimizing exploration time. They propose an extension of the multi-agent Proximal Policy Optimization (MAPPO) algorithm tailored for asynchronous settings. While these studies aim to address asynchronous decision-making, their algorithms are tailored specifically for the characteristics of their own problems and are not directly applicable to our scenario. Despite its significance, to the best of our knowledge, asynchronous decision-making has not yet been explored in wireless communication systems.

## III. SYSTEM MODEL AND PROBLEM FORMULATION

We consider a general data collection problem in which there are N rotary-wing UAVs (not necessarily homogeneous)

![](images/3818c90e223d91b26728828b0b26377e8c517d0d486a117a3a71fffdee9c2c18.jpg)  
Fig. 1. Illustration of the investigated system. Blue links represent inter-UAV communication, and orange links represent SN-UAV data transmission. Cells with dark green and bold borders under UAVs represent their observable regions.

indexed by $\mathcal { N } = \{ 1 , 2 , \dots , N \}$ . Each UAV is equipped with $N _ { t x }$ antennas and cooperates with other UAVs to collect data from sensor nodes (SNs) in a given area, as illustrated in Fig. 1. The UAV n departs from an initial location $\mathbf { w } _ { 0 } ^ { n } \in \mathbb { R } ^ { 2 }$ , travels around the monitored area to explore and collect data from SNs, and then returns to a final destination $\mathbf { w } _ { \mathrm { F } } ^ { n } \in \mathbb { R } ^ { 2 }$ . The monitored area is divided into a grid of $H \times H$ equal-sized cells indexed by $\mathcal { C } = \{ 1 , 2 , \ldots , H \times H \}$ , whose centers are denoted by the set $\mathcal { Q } _ { \mathrm { C } } = \{ \mathbf { q } _ { \mathrm { C } } ^ { c } \in \mathbb { R } ^ { 2 } : c \in \mathcal { C } \}$ . Let $\mathcal { T } = \{ 1 , 2 , \hdots , I \}$ be the set of I SNs, where SN i is located at a fixed location $\mathbf { q } _ { \mathrm { S N } } ^ { i } \in \mathbb { R } ^ { 2 }$

In many UAV-assisted applications, the amount of data to be collected is unknown prior to the UAV deployment, as it depends on dynamic and unpredictable factors. For instance, in search and rescue missions, the required data can fluctuate depending on the discovery of new targets or environmental obstacles encountered during flight. Similarly, in wildlife and habitat monitoring, the amount of data collected can be influenced by changing animal behaviors or the need for detailed imagery in specific areas. To capture this stochastic quantity, let $D ^ { i }$ be the amount of data at the ith SN that needs to be collected. The UAVs can move between the centers of cells to explore the data availability, or can hover above these points to collect data. When a UAV decides to hover and collect data from a cell, it will only leave once all available data in that cell has been collected. The UAV can only communicate with other UAVs within its limited communication range. We also define the termination conditions for a UAV, wherein it concludes the task and flies to its final destination either when it is about to run out of energy or once it has verified that all data have been collected. Furthermore, the termination of each UAV does not affect the operations of the others.

## A. UAVs’ Trajectories and Energy Consumption

Let ${ \mathcal { T } } ^ { n } = \{ t ^ { n } [ 0 ] , t ^ { n } [ 1 ] , \dots , t ^ { n } [ K ^ { n } ] \}$ represent the instants of time at which the n-th UAV makes decisions (detailed actions will be defined in Section IV-B) during its flight, and ${ \cal K } ^ { n } = \{ 0 , 1 , \ldots , K ^ { n } \}$ be the indices of these decisions. Assume that all UAVs operate at the same fixed altitude $h ,$ the trajectory of the n-th UAV can be denoted as $\mathbf { w } ^ { n }$ $\{ \mathbf { w } ^ { n } [ 0 ] , \mathbf { w } ^ { n } [ 1 ] , \dots , \mathbf { w } ^ { n } [ K ^ { n } + 1 ] \}$ , where $\mathbf { w } ^ { n } [ k ] \in \mathcal { Q } _ { \mathrm { C } }$ is the projection on the ground of the UAV’s position at time $t ^ { n } [ k ]$

We have the first constraints regarding to the departure and arrival locations of UAVs given by

$$
\mathbf { w } ^ { n } [ 0 ] = \mathbf { w } _ { 0 } ^ { n } , \mathbf { w } ^ { n } [ K ^ { n } + 1 ] = \mathbf { w } _ { \mathrm { F } } ^ { n } , \forall n \in \mathcal { N } .\tag{1}
$$

Let $\tau _ { \mathrm { H } } ^ { n } [ k ]$ represent the amount of time the n-th UAV hovers above $\mathbf { w } ^ { n } [ k ]$ , and $\tau _ { \mathrm { F } } ^ { n } [ k ]$ represent the amount of time required for this UAV to fly from $\mathbf { w } ^ { n } [ k ]$ to $\mathbf { w } ^ { n } [ k + 1 ]$ . If, at time $t ^ { n } [ k ]$ the UAV decides to hover above its current location $\mathbf { w } ^ { n } [ k ]$ to collect data, we have $\mathbf { w } ^ { n } [ k + 1 ] = \mathbf { w } ^ { n } [ k ]$ and $\tau _ { \mathrm { F } } ^ { n } [ k ] = { \mathrm { 0 } }$ Otherwise, we have $\tau _ { \mathrm { H } } ^ { n } [ k ] = 0$ and $\begin{array} { r } { \tau _ { \mathrm { F } } ^ { n } [ k ] = \frac { \| \mathbf { w } ^ { n } [ k + 1 ] - \mathbf { w } ^ { n } [ k ] \| _ { 2 } } { v ^ { n } } } \end{array}$ where $v ^ { n }$ is the fixed velocity of the n-th UAV. The total operating time of the n-th UAV can then be calculated by

$$
T ^ { n } = \sum _ { k = 0 } ^ { K ^ { n } } \tau _ { \mathrm { { F } } } ^ { n } [ k ] + \sum _ { k = 1 } ^ { K ^ { n } } \tau _ { \mathrm { { H } } } ^ { n } [ k ] ,\tag{2}
$$

and the mission completion time is $T = \operatorname* { m a x } _ { n \in \mathcal { N } } T ^ { n }$

The n-th UAV is powered by an on-board battery with limited capacity of $E _ { \mathrm { m a x } } ^ { n }$ . Since the communication energy is negligible compared to that required for propulsion [34], we ignore this component in our analyses. Following [34], the propulsion power consumption of a UAV operating at a fixed altitude is given by

$$
P _ { \mathrm { U A V } } ( V ) = P _ { 0 } \left( 1 + \frac { 3 V ^ { 2 } } { U _ { \mathrm { t i p } } ^ { 2 } } \right) + P _ { 1 } \left( \sqrt { 1 + \frac { V ^ { 4 } } { 4 v _ { 0 } ^ { 4 } } } - \frac { V ^ { 2 } } { 2 v _ { 0 } ^ { 2 } } \right) ^ { \frac { 1 } { 2 } }\tag{3}
$$

where $V$ is the UAV’s speed, $U _ { \mathrm { t i p } }$ is the tip speed of the rotor blade, and $v _ { 0 }$ represents the mean rotor-induced speed in hover, $P _ { 0 } , P _ { 1 }$ and $P _ { 2 }$ are constants depending on the UAV design and operating environment, which respectively represent the blade profile power, induced power and parasite power.

Let $E ^ { n } [ k ]$ be the remaining energy of UAV n at the time $t ^ { n } [ k ]$ and all UAVs start with full batteries, i.e., $\begin{array} { r } { E ^ { n } [ 0 ] = E _ { \mathrm { m a x } } ^ { n } . } \end{array}$ The remaining energy $E ^ { n } [ k ]$ at $t ^ { n } [ k ]$ can be calculated as

$$
E ^ { n } [ k ] = E _ { \mathrm { m a x } } ^ { n } - P _ { \mathrm { U A V } } ( 0 ) \sum _ { k ^ { \prime } = 1 } ^ { k - 1 } \tau _ { \mathrm { H } } ^ { n } [ k ^ { \prime } ] - P _ { \mathrm { U A V } } ( v ^ { n } ) \sum _ { k ^ { \prime } = 0 } ^ { k - 1 } \tau _ { \mathrm { F } } ^ { n } [ k ^ { \prime } ] .\tag{4}
$$

To ensure safety during the mission, we impose the following constraints (for all $n , k )$ to guarantee that UAVs always have sufficient energy to reach their final destinations

$$
\begin{array} { r } { E _ { \mathrm { m a x } } ^ { n } - E ^ { n } [ k ] - P _ { \mathrm { U A V } } ( 0 ) \tau _ { \mathrm { H } } ^ { n } [ k ] \geq \xi ^ { n } ( \mathbf { w } ^ { n } [ k ] ) + \epsilon } \end{array}\tag{5}
$$

$$
\begin{array} { r } { E _ { \mathrm { m a x } } ^ { n } - E ^ { n } [ k ] - P _ { \mathrm { U A V } } ( v ^ { n } ) \tau _ { \mathrm { F } } ^ { n } [ k ] \geq \xi ^ { n } ( \mathbf { w } ^ { n } [ k + 1 ] ) + \epsilon } \end{array}\tag{6}
$$

where $\begin{array} { r } { \xi ^ { n } ( \mathbf { x } ) = \frac { P _ { \mathrm { U A V } } ( v ) \| \mathbf { x } - \mathbf { w } _ { \mathrm { F } } ^ { n } \| _ { 2 } } { \eta n } } \end{array}$ is the energy required to fly to the final destination $\mathbf { w } _ { \mathrm { F } } ^ { n }$ from x, and  is a small safety energy margin. Let $\mathbf { w } = [ \mathbf { w } ^ { 1 } , \mathbf { w } ^ { 2 } , \dots , \mathbf { w } ^ { N } ]$ be the trajectories of all UAVs and b be the bandwidth allocation strategy (which will be defined more details in the following subsection). The total energy consumed by all UAVs can be calculated by

$$
\psi ( \mathbf { w } , \mathbf { b } ) = \sum _ { n \in \mathcal { N } } \sum _ { k \in \mathcal { K } ^ { n } } \left( P _ { \mathrm { U A V } } ( 0 ) \tau _ { \mathrm { H } } ^ { n } [ k ] + P _ { \mathrm { U A V } } ( v ^ { n } ) \tau _ { \mathrm { F } } ^ { n } [ k ] \right) .\tag{7}
$$

We note that the bandwidth allocation b directly affects the energy consumption in (7).

## B. Data Transmission Model

Let $\pmb { h } ^ { i n } ( t ) \in \mathbb { C } ^ { N _ { t x } \times 1 }$ be the channel coefficients between the n-th UAV and the i-th SN at the time t, which can be modeled as

$$
\pmb { h } ^ { i n } ( t ) = \sqrt { \alpha ^ { i n } ( t ) } \pmb { g } ^ { i n } ( t )\tag{8}
$$

where $\alpha ^ { i n } ( t )$ is large-scale fading channel including pathloss and shadowing, and $g ^ { i n } ( t )$ is small-scale channels, and $N _ { t x }$ is the number of receive antennas of the UAV. We adopt the common probabilistic modelling to present the large-scale fading channel, in which the channel is in line-of-sight with a probability of $P _ { L o S } ^ { i n } ( t )$ and in non-LoS with a probability of $P _ { N L o S } ^ { i n } ( t ) = 1 - \tilde { P } _ { L o S } ^ { i n } ( t )$ . Following [35], the LoS probability can be approximated as

$$
P _ { L o S } ^ { i n } ( t ) = \frac { 1 } { 1 + a \exp ( - b [ \theta ^ { i n } ( t ) - a ] ) }\tag{9}
$$

where a and b are environment-dependent parameters, $\begin{array} { r l r } { \theta ^ { i n } ( t ) } & { { } = } & { \frac { 1 8 0 } { \pi } \tan ^ { - 1 } \left( \frac { H } { \parallel \mathbf { w } ^ { n } ( t ) - \mathbf { q } _ { \mathrm { S N } } ^ { i } \parallel _ { 2 } } \right) } \end{array}$ is the elevation angle between the i-th SN located at ${ \bf q } _ { \mathrm { S N } } ^ { \imath }$ and the projection $\mathbf { w } ^ { n } ( t )$ on the ground of the n-th UAV at time t. Therefore, we have

$$
\alpha ^ { i n } ( t ) = \left\{ \begin{array} { l l } { \alpha _ { 0 } \left( d ^ { i n } ( t ) \right) ^ { - \eta } , } & { \mathrm { w . p . ~ } P _ { L o S } ^ { i n } ( t ) } \\ { \alpha _ { 0 } \beta \left( d ^ { i n } ( t ) \right) ^ { - \eta } , } & { \mathrm { o t h e r w i s e } } \end{array} \right.\tag{10}
$$

where $\alpha _ { 0 } = \left( 4 \pi f _ { c } / c \right) ^ { - 2 }$ is the free-space channel power gain at distance of 1m, $d ^ { i n } ( t ) = \sqrt { \| \mathbf { w } ^ { n } ( t ) - \mathbf { q } _ { \mathrm { S N } } ^ { i } \| _ { 2 } ^ { 2 } + h ^ { 2 } }$ is the distance between the i-th SN and the n-th UAV at time t, $\eta \geq 2$ is the pathloss exponent, β is the attenuation due to NLoS, $f _ { c }$ is the carrier frequency, and c is the speed of light. We adopt the popular Rician channel model for UAV-SN links [6], [11] which reads: $g ^ { i n } ( t ) = \bar { g } ^ { i n } \sqrt { \kappa ^ { i n } ( t ) / ( \kappa ^ { i n } ( t ) + 1 ) } +$ $\hat { \pmb { g } } ^ { i n } \sqrt { 1 / ( \kappa ^ { i n } ( t ) + 1 ) }$ , where $\bar { g } ^ { i n }$ is the deterministic LoS component with $| \bar { g } ^ { i n } | = 1 , \hat { g } ^ { i n } \sim \mathcal { C } \mathcal { N } ( 0 , { \bf 1 } )$ represents NLOS parts, $\kappa ^ { i n } ( t )$ is the Rician-factor that depends on the elevation angle $\theta ^ { i n } ( t )$ as $\kappa ^ { i n } ( t ) = A _ { 1 } \exp \left( A _ { 2 } \theta ^ { i n } ( t ) \right)$ , with $A _ { 1 }$ and $A _ { 2 }$ being environment-dependent constants.

When hovering to collect data, the UAVs employ Frequency Division Multiple Access (FDMA) to receive data from all active SNs in the current cell. To mitigate inter-UAV interference, the UAVs operate in orthogonal frequency bands of the same bandwidth $\begin{array} { r } { { \bf \tilde { B } } = \frac { B _ { m a x } } { N } } \end{array}$ , where $B _ { m a x }$ is the system bandwidth. Thus, the bandwidth allocation at one UAV is independent from other UAVs. Let $b ^ { i n } ( t )$ be the bandwidth that UAV n allocates to active SN i at time t (only active SNs have data to transmit). We have the following constraint for $b ^ { i n } ( t ) , \forall n \in \mathcal { N } , t \in \mathcal { T } ^ { n }$

$$
\sum _ { i \in \mathbb { Z } _ { n } ( t ) } b ^ { i n } ( t ) \leq B\tag{11}
$$

where ${ { T } _ { n } } ( t )$ be the set of active SNs serving by UAV n at timet . The instantaneous achievable upload data rate (bps) from SN i to UAV n at time t, assuming maximum ratio combining (MRC) receiver for low complexity and perfect CSI (imperfect CSI will considered in Section VI), can be calculated as

$$
R ^ { i n } ( t ) = b ^ { i n } ( t ) \log _ { 2 } \Big ( 1 + \| h ^ { i n } ( t ) \| ^ { 2 } P _ { s } / ( b ^ { i n } ( t ) N _ { 0 } ) \Big )\tag{12}
$$

where $P _ { s }$ is the fixed transmit power of SNs and $N _ { 0 }$ is the noise power spectral density.

Consider a particular time $t = t ^ { n } [ k ]$ when the n-th UAV makes its k-th decision. Due to the strong LoS of the UAV-SN channel when hovering, and for ease of notations, we assume that the channels remain unchanged during UAV’s hovering, the hovering time above $\mathbf { w } ^ { n } [ k ]$ can then be determined as

$$
\tau _ { \mathrm { H } } ^ { n } [ k ] = \operatorname* { m a x } _ { i \in \mathcal { L } _ { n } ( t ^ { n } [ k ] ) } \left\{ \frac { D ^ { i } } { R ^ { i n } ( t ^ { n } [ k ] ) } ~ \bigg | ~ R ^ { i n } ( t ^ { n } [ k ] ) > 0 \right\} .\tag{13}
$$

Let $b ^ { i n } [ k ] = b ^ { i n } ( t ^ { n } [ k ] )$ and $\boldsymbol { \mathsf { b } } ^ { n } = \{ b ^ { i n } [ k ] : i \in \mathcal { I } , k \in K ^ { n } \}$ be the bandwidth allocation strategy of UAV n. Given trajectories w and bandwidth allocation strategies $\mathbf { b } = [ \mathbf { b } ^ { 1 } , \mathbf { b } ^ { 2 } , \dots , \mathbf { b } ^ { N } ] ,$ we have the total collected data given by

$$
\Phi ( \mathbf { w } , \mathbf { b } ) = \sum _ { n \in \mathcal { N } } \sum _ { k \in \mathcal { K } ^ { n } } \sum _ { i \in \mathbb { Z } _ { n } ( t ^ { n } [ k ] ) } D ^ { i } .\tag{14}
$$

Finally, we have a constraint representing termination conditions of UAVs as follows

$$
\begin{array} { r } { ( E ^ { n } [ K ^ { n } + 1 ] - \epsilon ) \left( \sum _ { i \in \mathcal { I } } D ^ { i } - \Phi ( \mathbf { w } , \mathbf { b } ) \right) \leq 0 , \forall n \in \mathcal { N } } \end{array}\tag{15}
$$

where $E ^ { n } [ K ^ { n } + 1 ]$ is the remaining energy of the $n \cdot$ -th UAV when arriving at its final destination $\mathbf { w } _ { \mathrm { F } } ^ { n }$ . This constraint forces UAVs to continue exploring and collecting data until either their energy falls below the safety level or all active data in the current mission is collected.

## C. Problem Formulation

Our aim is to jointly optimize the trajectories w and bandwidth allocation strategies b of all N UAVs, such that the overall energy efficiency is maximized. This problem can be mathematically formulated as follows

$$
\begin{array} { r l } { \underset { \mathbf { w } , \mathbf { b } } { \operatorname* { m a x } } } & { { } \frac { \Phi ( \mathbf { w } , \mathbf { b } ) } { \psi ( \mathbf { w } , \mathbf { b } ) } } \\ { \mathrm { s . t . } } & { { } ( 1 ) , ( 5 ) , ( 6 ) , ( 1 1 ) , ( 1 5 ) } \end{array}\tag{P}
$$

where $\Phi ( \mathbf { w } , \mathbf { b } )$ and $\psi ( \mathbf { w } , \mathbf { b } )$ are given in (14) and $( 7 ) ,$ respectively. In the above problem, constraint (1) determines the initial and final locations of the UAVs. Constraints (5) and (6) ensure that, at every step, the UAVs have sufficient energy to reach their final locations. Constraint (11) guarantees that the total bandwidth used by each UAV does not exceed its available bandwidth. Finally, constraint (15) ensures that a UAV heads to its final location only when all data has been collected or it is about to run out of energy. Problem (P) is intractable due to i) high level of uncertainty of CSI and stochasticity of data collection demands; ii) non-deterministicity of the planning horizon $K ^ { n }$ and non-convexity in the objective function and constraints; iii) uncertainty in such multi-agent systems, where the operation of each UAV influences the environment and consequently affects the decisions of other UAVs. Besides, effective cooperation among UAVs is hindered by limitations in their observation and communication abilities. Therefore, it is difficult, if not impossible, to jointly solve problem (P) to optimality using conventional methods.

## IV. TRAJECTORY OPTIMIZATION UNDER DEC-POSMDP

As pointed out in the previous subsection, optimizing the UAVs’ trajectory using conventional optimization methods is infeasible due to the lack of information about the SNs activities as well as the full system states. In this section, we first introduce the Dec-POSMDP framework for trajectory optimization and then define its relevant components in detail.

## A. Dec-POSMDP Framework for Trajectory Optimization

The trajectory optimization problem can be represented by a tuple $\langle N , S , \mathcal { A } , P , R , \mathcal { Z } , \gamma \rangle$ , where S is the global state space of the environment, $\mathcal { A } = \times _ { n \in \mathcal { N } } \mathcal { A } ^ { n }$ is the joint action space, $P : S \times A \times S  [ 0 , 1 ]$ is the environment transition kernel, $R : \mathcal { A } \times \mathcal { S } $ <sup>R</sup> is a shared reward function contributed by all UAVs, $\mathcal { Z } = \times _ { n \in \mathcal { N } } \mathcal { Z } ^ { n }$ is the joint observation space, and finally, γ is the discount factor. Note that our proposed solution is model-free, meaning it does not assume or require any knowledge about P . Let $z ^ { n } [ k ] \in \mathcal { Z } ^ { n }$ be the local observation received by the n-th UAV and $u ^ { n } [ k ] \ \in \ A ^ { n }$ be the action chosen by this UAV at time $t ^ { n } [ k ]$ . We have the joint actionobservation history of the n-th UAV until $t ^ { n } [ k ]$ defined as follows

$$
H ^ { n } [ k ] = ( z ^ { n } [ 1 ] , u ^ { n } [ 1 ] , z ^ { n } [ 2 ] , \dots , u ^ { n } [ k - 1 ] , z ^ { n } [ k ] ) .\tag{16}
$$

Let $\begin{array} { r } { \mathcal { T } \ = \ \bigcup _ { n \in \mathcal { N } } \mathcal { T } ^ { n } \ = \ \{ \hat { t } _ { 1 } , \hat { t } _ { 2 } , \dotsc , \hat { t } _ { m } , \dotsc \} } \end{array}$ be the set of all decision-making instants of all UAVs sorted in the nondecreasing order. Let $s _ { m }$ denote the global state captured at time $\hat { t } _ { m }$ and $\mathbf { u } _ { m } = \bigl ( u _ { m } ^ { 1 } , u _ { m } ^ { 2 } , \ldots , u _ { m } ^ { N } \bigr )$ be the joint action of all UAVs taken at this time. The joint action $\mathbf { u } _ { m }$ here includes two parts, including a new action calculated by a UAV that finishes its action at $\hat { t } _ { m }$ and the on going actions of other UAVs calculated before $\hat { t } _ { m }$ . Let define the reward function for executing the joint action $\mathbf { u } _ { m }$ in state $s _ { m }$ at time $\hat { t } _ { m }$ by

$$
R ( s _ { m } , \mathbf { u } _ { m } ) = \int _ { \hat { t } _ { m } } ^ { \hat { t } _ { m + 1 } } \gamma ^ { t - \hat { t } _ { m } } \widehat { R } ( s _ { m } , \mathbf { u } _ { m } , t ) d t\tag{17}
$$

where $\widehat { R } ( s _ { m } , \mathbf { u } _ { m } , t )$ is the total instantaneous reward received by all UAVs at time t for taking action $\mathbf { u } _ { m }$ in state $s _ { m } ,$ which will be detailed in the next subsection. Precisely, $R ( s _ { m } , \mathbf { u } _ { m } )$ is the total reward accumulated by all UAVs from $\hat { t } _ { m }$ to $\hat { t } _ { m + 1 }$ Let $\pi ~ = ~ \times _ { n \in { \mathcal { N } } } \pi ^ { n }$ be the decentralized joint policy where $\pi ^ { n }$ is the local policy of UAV n that maps the local actionobservation history $H ^ { n } [ k ]$ to the next action $u ^ { n } [ k ]$ . Under the policy $\pi ,$ let define the joint state value function as

$$
V _ { \mathrm { t o t } } ^ { \pi } ( s _ { m } ) = \mathbb { E } _ { \pi } \left[ \sum _ { m = 0 } ^ { \infty } \gamma ^ { \hat { t } _ { m } } R ( s _ { m } , \mathbf { u } _ { m } ) \ | \ s _ { 0 } = s _ { m } \right] ,\tag{18}
$$

and the state-action value function as

$$
\begin{array} { l } { Q _ { \mathrm { t o t } } ^ { \pi } \left( s _ { m } , \mathbf { u } _ { m } \right) } \\ { = \mathbb { E } _ { \pi } \left[ \displaystyle \sum _ { m = 0 } ^ { \infty } \gamma ^ { \hat { t } _ { m } } R ( s _ { m } , \mathbf { u } _ { m } ) \ | \ s _ { 0 } = s _ { m } , \mathbf { u } _ { 0 } = \mathbf { u } _ { m } \right] . } \end{array}\tag{19}
$$

The problem can then be defined as finding the joint policy $\pi ^ { * }$ to maximize the values of all states:

$$
\begin{array} { r } { \pi ^ { * } = \arg \operatorname* { m a x } _ { \pi } V _ { \mathrm { t o t } } ^ { \pi } ( s _ { m } ) , \forall s _ { m } \in \mathcal { S } . } \end{array}\tag{20}
$$

## B. Detailed Components

We now transform the trajectory optimization problem into the Dec-POSMDP by defining its components as follows.

1) UAVs’ Termination Conditions: as defined in (15), the termination of a UAV depends on its energy level and the completion of collecting task. To mitigate the chance of having an empty battery during the flight, before taking actions the UAV checks if the remaining energy approaches the minimum safety level defined in constraints (5) and (6). To handle the second condition, each UAV n maintains a completion map $G ^ { n } \ \in \ \{ 0 , 1 \} ^ { H ^ { 2 } \times 1 }$ indicating its belief about the status of every cell. This map is initialized to zeros at the beginning, indicating the ‘yet-completed’ status. Over time, the map is updated after every UAV action based on its observations. Specifically, $G ^ { c n }$ is set to 1, or ‘completed’, if the n-th UAV collects all data in the c-th cell or observes that there is no data in the cell. The task is then considered completed by UAV n if all elements of $G ^ { n }$ are equal to one.

2) State Space: each state $s _ { m } \in \mathcal { S }$ includes positions, energy levels, and completion maps of all UAVs, and the true completion map.

3) Observation: the local observation $z ^ { n } [ k ]$ of the n-th UAV includes its remaining energy, current position, local completion map $G ^ { n }$ , and total data collection demand of each cell within its current observable region.

4) Action Space: the action space of the UAV n consists of five actions $\mathcal { A } ^ { n } = \{ 0 , 1 , 2 , 3 , 4 \}$ , which represent the action of hovering to collect data, moving forward, to the right, backward, and to the left, respectively. To enhance sample efficiency and prevent UAVs from taking nonsensical actions, we impose the following constraint: if a UAV moves to a specific location, it is not allowed to immediately return to its previous location. Specifically, the UAV cannot perform two consecutive actions of (1, 3), (3, 1), (2, 4), or (4, 2) in successive time steps. This is achieved by simply masking the prohibited actions during the sampling process.

5) Communication Message Between UAVs: When two UAVs are within their communication range, they share positions and synchronize the completion map to assist each other in verifying the mission completion for efficient exploration.

6) Reward Function: as defined in (17), the reward function $R ( s _ { m } , \mathbf { u } _ { m } )$ under the joint policy π is the accumulation of the instantaneous reward $\widehat { R } ( s _ { m } , \mathbf { u } _ { m } , t )$ . Here, we define this instantaneous reward as follows:

$$
\widehat { R } ( s _ { m } , \mathbf { u } _ { m } , t ) = \sum _ { n \in \mathcal { N } } \sum _ { i \in \mathcal { I } } \varphi ^ { i n } ( t ) + \alpha \Gamma ( \pi ) \mathbb { 1 } ( s _ { m } , \mathbf { u } _ { m } , t )\tag{21}
$$

where<sup>1</sup>

$$
\varphi ^ { i n } ( t ) = \left\{ { \begin{array} { l l } { R ^ { i n } ( t ) , } & { { \mathrm { i f ~ } } u _ { m } ^ { n } = 0 } \\ { - 0 . 0 1 , } & { { \mathrm { o t h e r w i s e } } . } \end{array} } \right.\tag{22}
$$

In the above equations, $R ^ { i n } ( t )$ is the upload data rate given in (12), α is a scaling parameter, $\Gamma ( \pi )$ is the energy efficiency achieved under the policy π given in the objective function of (P), and $\mathbb { 1 } ( s _ { m } , \mathbf { u } _ { m } , t )$ is an indicator function indicating whether taking action $\mathbf { u } _ { m }$ in state $s _ { m }$ leads to the termination of the last UAV at time t. This reward function can be simply interpreted as follows. If taking action $\mathbf { u } _ { m }$ in state $s _ { m }$ does not lead to the termination state, the reward $\hat { R } ( s _ { m } , \mathbf { u } _ { m } , t )$ at time t is the total reward of all UAVs, where the reward contributed by UAV n is its data collection rate $R ^ { i n } ( t )$ if it is collecting data (indicated by its action $u _ { m } ^ { n } = 0 )$ , and a small negative reward of −0.01 if it is moving between cells. On the other hand, if taking action $\mathbf { u } _ { m }$ in state $s _ { m }$ leads to the termination state (i.e., mission completion), the UAVs receive a reward proportional to their energy efficiency. The immediate reward $\varphi ^ { i n } ( t )$ in (21) serves as a shaping function to support the main learning goal of maximizing energy efficiency, which is only activated at the final moment when the last UAV reaches its destination. With a sufficiently large scaling parameter α (which is set to $\operatorname* { m a x } _ { n \in { \cal N } } \{ E _ { \operatorname* { m a x } } ^ { n } \}$ in our experiments), equation (21) ensures that UAVs receive a large reward only when all of them complete the mission. Moreover, by assigning a small negative reward to each movement action, UAVs are incentivized to cooperate and complete the mission in as few steps as possible, thereby reducing energy consumption and enhancing energy efficiency. Combine (17) and (21), we obtain the form of the reward function as follows

$$
\begin{array} { r l } & { { \cal R } ( s _ { m } , { \bf u } _ { m } ) } \\ & { = \displaystyle \int _ { i _ { m } } ^ { i _ { m + 1 } } \gamma ^ { t - \bar { t } _ { m } } \left( \displaystyle \sum _ { i \in \mathcal { X } } \varphi ^ { i n } ( t ) + \alpha \Gamma ( \pi ) { \mathbb 1 } ( s _ { m } , { \bf u } _ { m } , t ) \right) d t } \\ & { = \displaystyle \sum _ { i \in \mathcal { X } } \varphi ^ { i n } \left( \hat { t } _ { m } \right) \int _ { \hat { t } _ { m } } ^ { \hat { t } _ { m + 1 } } \gamma ^ { t - \bar { t } _ { m } } d t + \gamma ^ { \bar { \prime } _ { m } } \alpha \Gamma ( \pi ) { \mathbb 1 } ( s _ { m } , { \bf u } _ { m } ) } \\ & { = \displaystyle \frac { \gamma ^ { \hat { \prime } _ { m } } - 1 } { 1 \mathrm { e } ^ { \mathcal { X } } } \displaystyle \sum _ { i \in \mathcal { X } } \varphi ^ { i n } \left( \hat { t } _ { m } \right) + \gamma ^ { \bar { \prime } _ { m } } \alpha \Gamma ( \pi ) { \mathbb 1 } ( s _ { m } , { \bf u } _ { m } ) ( 2 ; \quad } \end{array}\tag{3}
$$

where $\hat { \tau } _ { m } = \hat { t } _ { m + 1 } - \hat { t } _ { m }$ is the duration of action $\mathbf { u } _ { m }$ taken in state $s _ { m }$ and $\hat { \mathbb { 1 } } ( s _ { m } ,  { \mathbf { u } } _ { m } )$ indicating whether taking action $\mathbf { u } _ { m }$ in state $s _ { m }$ leads to the termination of the last UAV. Here, the second equation is due to the assumption that channel states remain unchanged during $\mathrm { U A V } ^ { \ , } \mathbf { s }$ hovering, and that $\mathbb { 1 } ( s _ { m } , \mathbf { u } _ { m } , t )$ is only activated at the last moment when the last UAV arrives at its final destination.

## V. ASYNCHRONOUS LEARNING ALGORITHM

This section introduces an asynchronous learning algorithm for learning UAVs’ trajectory policies. To enhance the scalability of the proposed algorithm, we also propose state downsampling method to reduce the state space. Finally, a computational complexity analysis is provided, where we focus on the computational overhead required for each UAV to calculate an action in the deployment.

## A. Asynchronous QMIX

The conventional QMIX algorithm [7] aims to learn a centralized action-value function $Q _ { \mathrm { t o t } } ( s , \mathbf { u } )$ , which is factorized into N individual utility functions $Q ^ { n } ( H ^ { n } , u ^ { n } )$ representing the goodness of taking action $u ^ { n }$ on history $H ^ { n }$ . The principal premise that makes QMIX efficient is the consistent relationship between the deterministic greedy centralized policy and the deterministic greedy decentralized policies, which results from the monotonicity between $Q _ { \mathrm { t o t } }$ and $Q ^ { n }$ , i.e., $\partial Q _ { \sf t o t } / \partial Q ^ { n } \geq 0 , \forall n \in \hat { \cal N }$ . When such monotonicity is assured, the centralized training can be executed relying on the following relation (neglecting the order of UAVs)

![](images/c7d3ac35cb7afd86b9117e229f8679f0bafcfcf1f6509906c3853aea3557681d.jpg)  
Fig. 2. The architecture of the proposed algorithm. The green, blue, and red blocks represent UAVs’ policy networks, mixing network, and the hypernetwork. A downsampling layer is included in the hypernetwork to reduce the state space.

$$
\underset { \mathbf { u } \in \mathcal { A } } { \mathrm { a r g m a x } } Q _ { \mathrm { t o t } } ( s , \mathbf { u } ) = \left. \underset { u ^ { n } \in \mathcal { A } ^ { n } } { \mathrm { a r g m a x } } Q ^ { n } ( H ^ { n } , u ^ { n } ) \right. _ { n \in \mathcal { N } } .\tag{24}
$$

This result implies that local actions that improve the local $Q ^ { n }$ values will also enhance the joint action-value function $Q _ { \mathrm { t o t } } ,$ enabling decentralized agents to operate independently based on the greedy policy applied to their local $Q ^ { n }$ values.

It is worth noting that the above-mentioned original QMIX algorithm is only designed for synchronous environments in which all agents take actions simultaneously at each time step. As will be shown in Section VII-A, when this assumption does not hold, its performance significantly degrades. To enable QMIX to be applicable in our asynchronous environment, we make an important modification to the QMIX algorithm as follows. Let nˆ be the UAV that finishes its action at time $\hat { t } _ { m }$ , and $H _ { m } ^ { n }$ be the local joint action-observation history of UAV n recorded until $\hat { t } _ { m } ^ { \phantom { \dagger } } ( \mathrm { i . e . , ~ } H _ { m } ^ { n } \ = \ H ^ { n } [ k ^ { * } ]$ where $\begin{array} { r }  k ^ { * } \ = \ \mathrm { a r g m a x } _ { k \in \mathcal { K } ^ { n } } \{ t ^ { n } [ k ] \ | \ t ^ { n } [ k ] \ \leq \ \hat { t } _ { m } \ddot { \} ) } \end{array}$ . As mentioned in the preceding section, there is a new action $u _ { m } ^ { \hat { n } }$ calculated by UAV nˆ at $\hat { t } _ { m } .$ , while the actions of other UAVs being executed. Let $\mathbf { u } _ { m } ^ { - \hat { n } }$ denote the set of these ongoing actions, we have the joint action at time $\hat { t } _ { m }$ given by $\mathbf { u } _ { m } ^ { - } = \bar { \{ u _ { m } ^ { n } \} } \cup \mathbf { u } _ { m } ^ { - \hat { n } }$ . The aim of the asynchronous algorithm is to learn a joint (centralized) action-value function $Q _ { \mathrm { t o t } } ( s _ { m } , \mathbf { u } _ { m } | \mathbf { u } _ { m } ^ { - \hat { n } } )$ conditioned on the ongoing actions $\mathbf { u } _ { m } ^ { - \hat { n } }$ . We have the following result for our asynchronous algorithm.

Lemma 1: Given that $\begin{array} { r } { \frac { \partial Q _ { \mathrm { t o t } } } { \partial Q ^ { n } } \geq 0 \forall n \in \mathcal { N } . } \end{array}$ , and that

$$
\begin{array} { r l } & { Q _ { \mathrm { t o t } } \left( s _ { m } , \mathbf { u } _ { m } \vert \mathbf { u } _ { m } ^ { - \hat { n } } \right) } \\ & { \ = Q _ { \mathrm { t o t } } \left( Q ^ { \hat { n } } ( H _ { m } ^ { \hat { n } } , u _ { m } ^ { \hat { n } } ) , \{ Q ^ { n } ( H _ { m } ^ { n } , u _ { m } ^ { n } ) \} _ { n \in \mathcal { N } \backslash \{ \hat { n } \} } \right) , } \end{array}
$$

then we have

$$
\underset { \mathbf { u } _ { m } \in \mathcal { A } } { \mathrm { a r g m a x } } Q _ { \mathrm { t o t } } \left( s _ { m } , \mathbf { u } _ { m } \vert \mathbf { u } _ { m } ^ { - \hat { n } } \right) = \{ \underset { u _ { m } ^ { \hat { n } } \in \mathcal { A } ^ { \hat { n } } } { \mathrm { a r g m a x } } Q ^ { \hat { n } } \left( H _ { m } ^ { \hat { n } } , u _ { m } ^ { \hat { n } } \right) \} \cup \mathbf { u } _ { m } ^ { - \hat { n } } .
$$

Proof: Since $\frac { \partial Q _ { \mathrm { t o t } } } { \partial Q ^ { n } } \geq 0 \forall n \in \mathcal N .$ , we have

$$
\begin{array} { r l } & { Q _ { \mathrm { t o t } } \left( Q ^ { \hat { n } } ( H _ { m } ^ { \hat { n } } , u _ { m } ^ { \hat { n } } ) , \{ Q ^ { n } ( H _ { m } ^ { n } , u _ { m } ^ { n } ) \} _ { n \in \mathcal { N } \backslash \{ \hat { n } \} } \right) } \\ & { \leq Q _ { \mathrm { t o t } } \left( \underset { u _ { m } ^ { \hat { n } } \in \mathcal { A } ^ { \hat { n } } } { \operatorname* { m a x } } Q ^ { \hat { n } } ( H _ { m } ^ { \hat { n } } , u _ { m } ^ { \hat { n } } ) , \{ Q ^ { n } ( H _ { m } ^ { n } , u _ { m } ^ { n } ) \} _ { n \in \mathcal { N } \backslash \{ \hat { n } \} } \right) } \\ & { = \underset { u _ { m } ^ { \hat { n } } \in \mathcal { A } ^ { \hat { n } } } { \operatorname* { m a x } } Q _ { \mathrm { t o t } } \left( Q ^ { \hat { n } } ( H _ { m } ^ { \hat { n } } , u _ { m } ^ { \hat { n } } ) , \{ Q ^ { n } ( H _ { m } ^ { n } , u _ { m } ^ { n } ) \} _ { n \in \mathcal { N } \backslash \{ \hat { n } \} } \right) . } \end{array}
$$

Moreover, since an agent only receives a new observation, updates local history and calculates a new action when an action is finished, $Q ^ { n } ( H _ { m } ^ { n } , u _ { m } ^ { n } )$ remains unchanged for $n \in$ $\mathcal { N } \backslash \{ \hat { n } \}$ . Combined with the definition of $Q _ { \mathrm { t o t } } ( s _ { m } , \mathbf { u } _ { m } | \mathbf { u } _ { m } ^ { - \hat { n } } )$ we have

$$
\begin{array} { r l } { } & { \underset { \mathbf { u } _ { m } \in \mathcal { A } } { \operatorname* { m a x } } Q _ { \mathrm { t o t } } ( s _ { m } , \mathbf { u } _ { m } | \mathbf { u } _ { m } ^ { - \hat { n } } ) } \\ & { = \underset { \mathbf { u } _ { m } \in \mathcal { A } } { \operatorname* { m a x } } Q _ { \mathrm { t o t } } \left( Q ^ { \hat { n } } ( H _ { m } ^ { \hat { n } } , u _ { m } ^ { \hat { n } } ) , \{ Q ^ { n } ( H _ { m } ^ { n } , u _ { m } ^ { n } ) \} _ { n \in \mathcal { N } \backslash \{ \hat { n } \} } \right) } \\ & { = \underset { u _ { m } ^ { \hat { n } } \in \mathcal { A } ^ { \hat { n } } } { \operatorname* { m a x } } Q _ { \mathrm { t o t } } \left( Q ^ { \hat { n } } ( H _ { m } ^ { \hat { n } } , u _ { m } ^ { \hat { n } } ) , \{ Q ^ { n } ( H _ { m } ^ { n } , u _ { m } ^ { n } ) \} _ { n \in \mathcal { N } \backslash \{ \hat { n } \} } \right) } \end{array}
$$

which directly implies the result and completes the proof. 

This lemma implies that once the monotonicity between $Q _ { \mathrm { t o t } }$ <sub>t</sub> and $Q ^ { n }$ is established, the local deterministic greedy policies remain applicable for agents to calculate their actions in asynchronous environments.

Fig. 2 illustrates the network architecture in our proposed algorithm. Specifically, the architecture includes two components: i) agent networks that take local action-observation histories and the agent indices as input and output the local $Q ^ { n }$ values, and ii) a mixing network that uses the global state information to produce $Q _ { \mathrm { t o t } }$ from N local $Q ^ { n }$ values. We employ DRQN [36] with parameter sharing for each agent network, while for the mixing network, a two-layer fullyconnected neural network with ELU nonlinearity is used. To establish the monotonic relationship between $Q _ { \mathrm { t o t } }$ and $Q ^ { n }$ $( \mathrm { i } . \mathrm { e } . , \partial Q _ { \mathrm { t o t } } / \partial Q ^ { n } \geq 0 )$ , all weights of the mixing network are constrained to be non-negative. To this end, a hypernetwork is used to generate weights and biases for the mixing network, taking the global state as the input. Fully-connected layers with ReLU activation, followed by an absolute function, are employed to ensure non-negative weights. Since each agent network is conditional on its local observation and history, the learned policies can be extracted and executed independently without any negative impact on performance. We note that although having similar network architecture (except the down-sampling layer) as in the QMIX algorithm [7], our proposed asynchronous learning algorithm operates differently, especially in the way each agents takes its action.

Algorithm 1 Asynchronous-QMIX   
1: Initialize the training environment, agents’ policy and   
value networks, and buffer $\mathcal { D }  \mathcal { D } ;$   
2: $m \gets 1 ;$   
3: Observe $\mathbf { z } _ { 1 }$ and sample action ${ \bf u } _ { 1 } ;$   
4: Initialize $\mathcal { Q }  \{ ( n , \tau _ { 1 } ^ { n } ) : n \in \mathcal { N } \} ; / / \tau _ { m } ^ { n }$ is the time taken   
by agent n to complete $u _ { m } ^ { n }$   
5: while environment not terminal do   
6: $( \hat { n } , \hat { t } _ { m + 1 } ) \gets \arg \operatorname* { m i n } _ { ( n , t ) \in \mathcal { Q } } t ;$   
7: Agent nˆ observes reward $R ( s _ { m } , \mathbf { u } _ { m } )$ and new obser  
vation $z _ { m + 1 } ^ { \hat { n } } ;$   
8: Agent nˆ updates local history:   
$\bar { H _ { m + 1 } ^ { \hat { n } } } \gets \bar { ( H _ { m } ^ { \hat { n } } , u _ { m } ^ { \hat { n } } , z _ { m + 1 } ^ { \hat { n } } ) } ;$   
9: Agent nˆ selects new action:   
$\begin{array} { r } { u _ { m + 1 } ^ { \hat { n } }  \arg \operatorname* { m a x } _ { u \in \mathcal { A } ^ { \hat { n } } } Q ^ { \hat { n } } ( H _ { m + 1 } ^ { \hat { n } } , u ) ; } \end{array}$   
10: Update joint action and observation:   
$\mathbf { u } _ { m + 1 }  \{ u _ { m + 1 } ^ { \hat { n } } \} \cup \mathbf { u } _ { m } ^ { - \hat { n } } ; \mathbf { z } _ { m + 1 }  \{ z _ { m + 1 } ^ { \hat { n } } \} \cup \mathbf { z } _ { m } ^ { - \hat { n } } ;$   
11: Compute the new finish time: $t _ { \mathrm { n e w } } \gets \hat { t } _ { m } + \tau _ { m + 1 } ^ { \hat { n } } ;$   
12: $\mathcal { Q }  \mathcal { Q } \cup \{ ( \hat { n } , t _ { \mathrm { n e w } } ) \} ;$   
13: $\mathcal { D }  \mathcal { D } \cup \{ ( s _ { m } , \mathbf { z } _ { m } , \mathbf { u } _ { m } , R ( s _ { m } , \mathbf { u } _ { m } ) , s _ { m + 1 } , \mathbf { z } _ { m + 1 } ) \} ;$   
14: Update agents’ policy and value networks;   
15: m $ m + 1 ;$   
16: end while

The training is end-to-end based on a replay buffer, aiming to minimize the loss function

$$
\mathcal { L } ( \boldsymbol { \theta } _ { m } ) = \mathbb { E } \left[ \left( y _ { \mathrm { t o t } } - Q _ { \mathrm { t o t } } \left( s _ { m } , \mathbf { u } _ { m } \vert \mathbf { u } _ { m } ^ { - \hat { n } } ; \boldsymbol { \theta } _ { m } \right) \right) ^ { 2 } \right]\tag{25}
$$

where $y _ { \mathrm { \ t o t } }$ is the target value estimated by one-step bootstrapping as

$$
y _ { \mathrm { t o t } } = R ( s _ { m } , \mathbf { u } _ { m } ) + \gamma ^ { \hat { \tau } _ { m } } \underset { \mathbf { u } _ { m + 1 } } { \mathrm { m a x } } Q _ { \mathrm { t o t } } ( s _ { m + 1 } , \mathbf { u } _ { m + 1 } | \mathbf { u } _ { m + 1 } ^ { - \hat { n } } ; \boldsymbol { \theta } _ { m } ^ { - } )
$$

wherein $\theta _ { m }$ and $\theta _ { m } ^ { - }$ is the parameters of the primary and the target networks.

We name the proposed framework Asynchronous-QMIX (AQMIX), which is outlined in Algorithm 1. Since different actions of different agents are completed at different timestamps, the idea is to maintain a list Q that records when each agent finishes its action. At each training step m, only the agent with the smallest associated timestamp is processed, i.e., its observation is updated and a new action is generated. This asynchrony is the key distinction between the proposed algorithm and the canonical synchronous QMIX.

## B. Enhance Scalability Through State Downsampling

The hypernetwork in the mixing network requires the positions of UAVs and their completion maps to generate the mixing parameters benefiting the UAVs cooperation. However, the incorporation of these maps into the state significantly expands the state space. With N UAVs and a monitored area of $H ^ { 2 }$ cells, incorporating the completion maps exponentially expands the state space by $2 ^ { N H ^ { 2 } }$ . In fact, when the numbers of cells and UAVs grow, the state space dimension is dominated by the size of these maps. This expansion not only increases training time but also makes the model harder to train due to the curse of dimensionality, potentially degrading learning performance (as we will show in the experiment later). Moreover, including the completion status of each UAV at every cell may be redundant. This is because, from the global mixing network perspective, knowing UAVs’ positions and their completion status in each collecting region (i.e., group of cells in close proximity) is sufficient for approximately evaluating a cooperative strategy among UAVs.

Motivated by the observations above, we employ a sumpooling layer to downsample the resolution of completion maps before feeding them into the hypernetwork of the mixing network. With a kernel size of $M \times M$ and non-overlapping sampling windows, this layer can reduce the state space by a factor of $2 ^ { M ^ { 2 } }$ , thereby reducing the size of the mixing network and the training time. The downsampling layer is also illustrated Fig. 2 as the first block of the hypernetwork.

## C. Computational Complexity in Deployment

Since only agent networks are extracted and deployed on UAVs after training, the complexity of calculating actions in deployment does not depend on the mixing network. The input of each agent network includes UAV’s position, energy level, data collection demands of observable cells, and the completion map $G ^ { n } \in \{ 0 , 1 \} ^ { H ^ { 2 } \times 1 }$ . Since the number of observable cells does not exceed the size of completion mapG<sup>n</sup> , the input size is dominated by $H ^ { 2 }$ . As illustrated in Fig. 2, each agent network comprises one fully-connected input layer, followed by a GRU layer, and finally, a fully-connected output layer. Given that the complexity of a fully-connected layer with input size $N _ { \mathrm { x } }$ and hidden size $N _ { \mathrm { h } }$ is $\mathcal { O } ( N _ { \mathrm { x } } N _ { \mathrm { h } } )$ , the complexity of a GRU cell with the same input size $N _ { \mathrm { x } }$ and hidden size $N _ { \mathrm { h } }$ is $\mathcal { O } ( N _ { \mathrm { x } } ^ { 2 } { + } N _ { \mathrm { x } } N _ { \mathrm { h } } ) ~ [ 3 7 ]$ , and the fact that we use the same number of $N _ { \mathrm { h } }$ units for all hidden layers of the policy networks, the complexity to calculate an action for a UAV at each step is given by $\dot { \mathcal { O } } ( H ^ { 2 } N _ { \mathrm { h } } + N _ { \mathrm { h } } ^ { 2 } )$

## VI. BANDWIDTH ALLOCATION UNDER IMPERFECT CSI

Once the UAVs have learned the trajectory policy, they fly through each cell and hover to collect data using the FDMA protocol. To minimize the hovering time of the UAV, this section optimizes the bandwidth allocation to active SNs considering the practical imperfect CSI. In practice, perfect CSI is infeasible, resulting channel estimation error. Let $\boldsymbol { h } ^ { i n } ( t ) , \boldsymbol { \hat { h } } ^ { i n } ( t )$ be the true and estimated channel coefficients between UAV n and SN $i ,$ respectively. Under imperfect CSI, we have ${ \pmb h } ^ { i n } ( t ) = \hat { { \pmb h } } ^ { \ i n } ( t ) + e ^ { i n } ( t )$ , where $e ^ { i n } ( t )$ is the estimation error that is statistically independent from the estimated channel and its elements are modelled as random variables with zero mean and variance $\sigma _ { e } ^ { 2 } / N _ { t x }$ . Under FDMA transmission mode, there is no interference at the receiver side.

The received signal from SN i under MRC receiver at UAV n is given as

$$
\hat { y } ^ { i n } ( t ) = \sqrt { P _ { s } } \frac { \tilde { h } ^ { H } } { \| \tilde { h } \| } \big ( \hat { h } ^ { i n } ( t ) + e ^ { i n } ( t ) \big ) x ^ { i } ( t ) + \frac { \tilde { h } ^ { H } } { \| \tilde { h } \| } n ^ { i n } ( t )\tag{26}
$$

where $\tilde { \pmb { h } } \triangleq \hat { \pmb { h } } ^ { i n } ( t ) , x ^ { i } ( t )$ is the transmitted symbol with unit average power over the symbol constellation and ${ \mathbf { } } n ^ { i n } ( t )$ is the thermal Gaussian noise. By treating the channel estimation error as noise, the achievable rate for SN i is given by

$$
\bar { R } ^ { i n } ( t ) = b ^ { i n } ( t ) \log _ { 2 } \left( 1 + \frac { { \| \hat { \pmb { h } } ^ { i n } ( t ) \| } ^ { 2 } P _ { s } } { P _ { s } \sigma _ { e } ^ { 2 } + b ^ { i n } ( t ) N _ { 0 } } \right) .\tag{27}
$$

Let $\mathcal { T } _ { n } ( t )$ be the set of active SNs of the cell serving by UAV n at time t. The bandwidth allocation optimization problem for the n-th UAV at the time t to minimize the hovering time can be formulated as follows:

$$
\operatorname* { m i n } _ { \{ b ^ { i n } ( t ) \geq 0 \} } \operatorname* { m a x } _ { i \in \mathbb { Z } _ { n } ( t ) } \frac { D ^ { i } } { \bar { R } ^ { i n } ( t ) } ; \mathrm { ~ s . t . ~ } \sum _ { i \in \mathbb { Z } _ { n } ( t ) } b ^ { i n } ( t ) \leq B .\tag{28}
$$

To solve problem (28), we introduce an auxiliary variable $\zeta \geq 0$ as the total hovering time of UAV n. The hovering time needs to guarantee that all data is collected, i.e.,

$$
\bar { R } ^ { i n } ( t ) \geq D ^ { i } / \zeta , \forall i \in \mathcal { T } _ { n } ( t ) .\tag{29}
$$

These non-convex constraints can be convexified by dividing both sides by a positive ζ. Thus, problem (28) can be reformulated as follows:

$$
\operatorname* { m i n } _ { \{ b ^ { i n } ( t ) \geq 0 \} , \zeta \geq 0 } \zeta ; \mathrm { ~ s . t . ~ } ( 2 9 ) \mathrm { a n d ~ } \sum _ { i \in \mathcal { T } _ { n } ( t ) } { b ^ { i n } ( t ) } \leq B .\tag{30}
$$

It can be shown that the rate function in (27) is a concave function with respect to variable $b ^ { i n } ( t )$ , though the proof is omitted due to space limitation. Thus, problem (30) is a convex optimization problem with a linear objective function and convex constraints, and can be efficiently solved by standard methods, $\mathrm { e . g . }$ , interior point. Since this problem only depends on the information at the current cell c, it can be solved to optimality based on local observation of the UAV at each hovering point.

## VII. SIMULATION RESULTS AND DISCUSSIONS

In this section, we evaluate the performance of the proposed method in solving problem (P). We first describe the simulation setups and baseline algorithms. Performance comparisons and analyses will be discussed subsequently.

## A. Simulation Setups

The monitored area is divided into a grid of cells, each with a size of 50m×50m. To evaluate the scalability of the algorithms, we use different grid sizes, including $8 \times 8 .$ $1 0 \times 1 0 , 1 5 \times 1 5 ,$ , and $2 0 \times 2 0$ cells. Additionally, we assess the algorithms with varying numbers of UAVs, ranging from 1 to 6. Since the state space grows exponentially with the number of cells, and adding more UAVs directly amplifies the nonstationarity of the environment, larger grid sizes and more UAVs make it increasingly difficult for the algorithms to learn and make effective decisions. As sensors are often deployed non-uniformly in practice, with a higher concentration around targets, we randomly divide the cells into two groups, including sparse cells and dense cells with ratio of 7:3, respectively. The number of SNs in each cell is generated using Poisson distribution Pois(λ), where $\lambda = 1 0$ for dense cells and $\lambda = 1$ for sparse cells. The SNs are then uniformly placed within each cell, as illustrated in Fig. 3. To generate data availability for collection, we first generate the number of cells containing data following Poisson distribution with the mean value $\lambda \stackrel { = } { = } \phi H ^ { 2 }$ , where $\phi$ is used to control the density of data demands. Once the number of cells containing data is determined, their locations are randomly assigned. The data size of active SNs is randomly generated from [0.1, 1.0] Mbits, following some stable distribution. We set the transmit power of SNs $P = 1 0$ dBm, attenuation due to NLoS $\beta \ = \ 0 . 2 ,$ total bandwidth $B = 1$ MHz, noise power spectral density $N _ { 0 } = - 1 5 0$ dBm, and the pathloss exponent $\eta = 2 . 6$ . The UAVs are assumed to fly at h = 100 m altitude. For the environment parameters, we set $a = 1 1 . 9 5 , b = 0 . 1 4 , A _ { 1 } = 1 . 0 ,$ and $A _ { 2 } ~ = ~ 4 . 3 9$ , following the settings in [6], [11]. Initial locations and final destinations of all UAVs are set at the same position, at the center of the bottom-left cell depicted in Fig. 3. The observable region of each UAV is an area of $3 \times 3$ cells centered at its location. All UAVs are trained with energy budgets of $E _ { \operatorname* { m a x } } ^ { n } = 1 0 0 0$ kJ each. Unless otherwise indicated, the following default parameters are used. There are $N = 2 \ \mathrm { U A V s }$ with different velocities of 5 m/s and 10 m/s, data density $\phi = 0 . 3$ , and inter-UAV communication range is set to 200 m. All other UAVs’ parameters are retained as in [34].

![](images/aa7ccafda76475087c8fc168a7a8d40024356578e63f7e2d7d6ebe917076a83e.jpg)  
Fig. 3. Distribution of SNs over the $8 \times 8$ cell collecting area. The colors of SNs represent an example of data collection demands with available data size ranging from 0 to 1 Mbits.

The proposed AQMIX algorithm is compared with following reference schemes:

Independent learning (AIQL): this is a fully decentralized baseline obtained by removing the mixing network from the architecture of AQMIX, which is analogous to the paradigm used in [2]. The policies are learned only based on local action-observation histories without using the global state.

![](images/1046a27ec514d9fb9a0f5b92770bc0b00d449e0ad833862f2ddd61e77a8d74fc.jpg)  
(a) $1 0 \times 1 0$ cells

![](images/1a5c6e5a4cb1bfb6f900285d68d818f04358d7a12f5eb087a5bf33c838f02cb5.jpg)  
(b) $1 5 \times 1 5$ cells

![](images/afffe44575a004d8161d1fd2f96e865614fbe5fb7a23acc4aa2aeb09db98faa2.jpg)  
(c) $2 0 \times 2 0$ cells  
Fig. 4. Total reward per episode during training on different network sizes.

QMIX [6]: this algorithm was designed only for synchronous environments. To adapt it in our asynchronous setting, we employ a synchronous training - asynchronous deployment mechanism as follows. During training, if a UAV completes its action before others, it waits until all UAVs complete their actions, allowing them to calculate their new actions simultaneously. Since all learned policies can be extracted and executed distributively, we then deploy them in our asynchronous environment without inter-UAV synchronization. This baseline enables us to evaluate both the learning performance of the proposed algorithm relative to the original QMIX, as well as the performance of the existing synchronous MARL algorithm in asynchronous environments.

• Heuristic (HERT): a very naive but feasible solution to (P) is to partition the area into multiple sectors and assign each part to one UAV. UAVs then fly over their assigned sub-areas, exploring and collecting data cell by cell.

To prevent algorithms from learning trivial solutions by memorizing specific trajectories, the data collection demands are randomly regenerated at the beginning of each episode, encouraging agents to learn more general behaviors. The hyperparameters are hand-tuned for reasonable performance and are used across all methods. Specifically, we use a learning rate of 5e-5, a discount factor of $\gamma = 0 . 9 9 \ :$ , a batch size of 32, a replay buffer size of 1e6 samples, and a target network update rate of 1e-2. We set the number of neurons to 256 in all hidden layers of the policies and the mixing network. The state downsampling is performed with kernel size of $3 \times 3 .$ . The reward function is scaled down by the maximum generated data size (which is 1.0 Mbits) to avoid numerical issues. Besides, we adopt the equal bandwidth allocation during training to minimize the training time, and only perform bandwidth optimization during the testing phase.

## B. Performance Comparisons and Analyses

1) Learning Performance: We first examine the learning performance of all learning-based solutions on different numbers of cells. Fig. 4 plots the total reward per episode during training, where we train two UAVs to collect data over areas of $1 0 \times 1 0$ $1 5 \times 1 5 .$ , and $2 0 \times 2 0$ cells. In this figure, each line represents the average values over 10 different trainings and the shaded areas represent the standard deviation. It can be seen that AQMIX clearly outperforms QMIX and AIQL across all network sizes. The superiority of AQMIX over QMIX can be explained by the fact that QMIX requires UAVs to wait for synchronization with others before making decisions, resulting in inefficient use of hovering energy. These results demonstrate that we have successfully extended QMIX, preserving its advantages in an asynchronous environment. While AQMIX and QMIX exhibit consistent convergence trends during learning, the results of AIQL show significant variance in learning performance. These performance fluctuations can be attributed to the absence of cooperation mechanisms between agents, which is a common limitation of independent learning methods.

Fig. 5 plots the total reward per episode during training, where we train 1, 2, 4, and 6 UAVs to collect data over areas of $1 0 \times 1 0$ cells. As expected, sub-fig. 5a shows that when there is only one UAV, all algorithms exhibit the same learning performance. This is because, in this case, asynchronous and synchronous environments are identical, and all learning algorithms function as single-agent RL algorithms. As the number of UAVs increases, the gaps between algorithms become clearer, with AQMIX standing out as the best solution. Notably, the performance of AIQL significantly drops as the number of UAVs increases. This is because a greater number of UAVs leads to a higher likelihood of inter-UAV communication, i.e., more frequent synchronization of information among UAVs. In the case of AQMIX and QMIX, this synchronization is beneficial due to their cooperative mechanisms. However, due to the absence of cooperation management mechanisms in AIQL, these synchronizations inadvertently trigger unexpected interactions between UAVs, exacerbating the inherent instability of the algorithm.

Overall, AQMIX has proven to be the most effective learning solution in asynchronous environments, as demonstrated by its stable and highly competitive performance. In contrast, AIQL fails to leverage the benefits of increasing the number of UAVs, as well as the potential of inter-UAV communication.

2) Robustness of Learned Policies: to evaluate the robustness of learned policies, we select the best policy obtained by each method,<sup>2</sup> and then evaluate these policies on a same set of 1000 different scenarios of data generations. In the next two figures, we report the testing results on the test benchmark of 10 × 10 cells.

Fig. 6 plots the average results over 1000 testing scenarios, with the energy budget for each UAV varying from 100kJ to 400kJ. The methods are evaluated under three criteria: the percentage of collected data (Fig. 6a), the mission completion time (Fig. 6b), and energy efficiency (Fig. 6c). It’s worth noting that all tested policies were trained only with $E _ { \mathrm { m a x } } ^ { n } = 1 0 0 0 \mathbf { k J }$ . sub-fig. 6a shows that 150kJ is sufficient for AQMIX, QMIX, and HERT to collect all data, while this number for AIQL is above 400kJ. Having the energy budget exceed this required level does not have a significant impact on the solution quality, as shown in sub-fig. 6b and sub-fig. 6c, where the completion time and energy efficiency remain unchanged as the energy budget increases. Overall, the proposed AQMIX algorithm provides outstanding performance in all three criteria compared to the benchmark schemes, demonstrated by its higher energy efficiency and the ability to collect the most data with the least time and energy consumption. The results also suggest that mission completion time and total collected data can be optimized indirectly by maximizing energy efficiency.

![](images/033b6d44e0c5815feaaa355d3b09cf38a98f0998c706f3832e21444577fb2ad1.jpg)  
(a) 1 UAV

![](images/92d627effb3ea3d3075d30637d9e7e1ea193db7ed27baa686053369616e725cc.jpg)  
(b) 2 UAVs

![](images/5ab80a3668a814ffd3310ad30e4266f343f68b73e84ede8a38b0a9003720e133.jpg)  
(c) 4 UAVs

![](images/d0ffe60bb727fad472985f14e9261825539790d82fda96f5a792433f02a7c9c4.jpg)  
(d) 6 UAVs

Fig. 5. Total reward per episode during training with different numbers of UAVs.  
![](images/94fe827499dcec51683a149d3bb20172d58054d76ec31da31b18ecde32cea4a7.jpg)  
(a) Percentage of collected data

![](images/9f68f1be042c2d73b5fa173fb132cf8f61b6e5f5368e69268c4e5e2cf9beb0c3.jpg)  
(b) Completion time

![](images/92c6b4b90e7023840789b01867a1b063de39c78cadb5af7bfbfa8dd35b6ce2fe.jpg)  
(c) Energy efficiency

Fig. 6. Testing results on different levels of energy budget.  
![](images/f6380509e1539d6a04d9df8553ade542b43db71018b0a22c5f6fd1809d8ab7b0.jpg)  
(a) Completion time

![](images/d486321d51980791bbafc7b66ac9e026a46641b638f13e42235472d0fa435f57.jpg)  
(b) Energy efficiency

![](images/a4fade00ee2a134b564c45d03dc1a66e220c810113466e3289f070e6bef7b01c.jpg)  
(a) Completion time

![](images/69767649b3464fd869b1ba8959005e858b2b0fffdac644622913ba37ddbf018c.jpg)  
(b) Energy efficiency  
Fig. 7. Testing result on different density levels of data collection demands.  
Fig. 8. Testing results of policies trained with different numbers of UAVs.

Fig. 7 shows the average completion time and energy efficiency achieved by all schemes, where the data density parameter φ is varied between 0.1 and 0.5. It’s also worth noting that all tested policies were trained only at $\phi = 0 . 3 .$ As shown in Fig. 7, both the completion time (sub-fig. 7a)

and energy efficiency (sub-fig. 7b) tend to increase as the amount of data to collect increases. This is because, as more data is available in the same area, the energy cost per unit of data collected decreases. This leads to improved energy efficiency, as the UAVs can collect more data without a proportional increase in energy consumption. Similar to the previous experiment, AQMIX consistently outperforms the benchmark schemes.

In summary, Fig. 6 and Fig. 7 demonstrate that the proposed AQMIX algorithm not only outperforms other reference schemes, but also exhibits robustness and strong generalization ability across varying conditions of data availability and UAV energy budgets.

3) Impacts of the Number of UAVs: Fig. 8 plots the testing results where policies are trained with different numbers of UAVs to collect data over areas of $1 0 \times 1 0$ cells. In this figure, the results of AQMIX and QMIX reveal a trade-off between completion time and energy efficiency. In particular, increasing the number of UAVs significantly reduces the completion time (sub-fig. 8a) but also decreases the energy efficiency (sub-fig. 8b). While the reduction in completion time is straightforward, the decline in energy efficiency can be attributed to the overlapping UAV trajectories as the number of UAVs increases. Additionally, having more UAVs makes the environment more challenging to learn due to increased noise and uncertainty in the UAVs’ observations. Notably, increasing the number of UAVs from one to two reduces the completion time by approximately 75% in AQMIX, while efficiency decreases only slightly, by less than 10%. This tradeoff ratio is significantly better than that of QMIX, which sacrifices 30% of energy efficiency for a 50% reduction in completion time. In the case of HERT, the completion time decreases proportionally with the number of UAVs, while the energy efficiency remains unchanged. This is because each UAV is assigned a specific, non-overlapping area, meaning the total energy consumption by all UAVs remains roughly the same as in the single-UAV case. Finally, AIQL demonstrates poor performance when the number of UAVs increases, since this algorithm struggles to learn when there are more than two UAVs, as discussed previously. Overall, AQMIX achieves the lowest completion time and the highest energy efficiency in all cases.

![](images/ae3d368583b38e122d9d7f77e5a63b34e1d9efa30daf1acbf2b340c3f56e88ea.jpg)  
(a)

![](images/85571e7e683715e6c69b19c5e66a725a16bfb7f5cb00d1e4ed8ffff608981139.jpg)  
(b)  
Fig. 9. Testing results of policies trained with different inter-UAV communication ranges. $\mathrm { \ddot { \Omega } N C ^ { , - } } \mathrm { ~ . ~ } \mathrm { n o }$ communication between UAVs; $\mathbf { \tilde { \Sigma } } ^ { 6 } \mathbf { F } \mathbf { C } ^ { \ast }$ - full-communication to all UAVs.

4) Impacts of Inter-UAV Communication: Fig. 9 plots the completion time and energy efficiency as functions of the inter-UAV communication range, which varies from no communication between UAVs to full communication, where UAVs can exchange information any time and from any position. Note that inter-UAV communication does not affect the performance of the heuristic method, as UAVs in this approach operate independently within preassigned collecting sub-areas. The results in Fig. 9 show that extending the communication range enhances the performance of QMIX and AQMIX, demonstrated by the reduced completion time and the increased energy efficiency. This improvement occurs because a longer communication range allows UAVs to better synchronize their observations and assist each other in verifying mission completion, thereby reduces the total energy consumption. In contrast, increasing the communication range does not benefit AIQL and may even amplify non-stationarity in its learning process. These findings further confirm the effectiveness of the cooperation strategies learned by QMIX and AQMIX. Overall, AQMIX proves to be the superior approach.

5) Impacts of the State Downsampling: In Fig. 10, we report the results on ${ \textbf { a } } 1 5 \times 1 5$ grid with 2 UAVs, testing kernel sizes of $1 \times 1$ (no downsampling), $2 \times 2 , 3 \times 3 , 4 \times 4$ and $5 \times 5 .$ . The results show that very small or very large kernels either overload the models with excessive detail or discard important spatial information, both leading to degraded policy performance. Based on these observations, a practical guideline for selecting the kernel size is to choose a value no larger than the agent’s observable region, ideally matching the size of this region. In our setup, each UAV observes a $3 \times 3$ window, and a $3 \times 3$ kernel provided the best trade-off between state compactness and information retention.

![](images/3228f167c9444660c62177eed0b66c093230faca9c7f20b09aaa92152d5dffb0.jpg)  
Fig. 10. Learning curves of AQMIX with different kernel sizes used in state downsampling.

![](images/7059ed68ec74f820bb709965ef59b7fe216cbed4a89b79f7d386b54dd5773a82.jpg)  
(a)

![](images/ab3842004f2816b61452c82d472bd2e32a7d9dab89eff37063d56b738e2bd7a8.jpg)  
(b)

${ \mathrm { F i g . } }$ 11. Impact of channel estimation error to the performance of AQMIX.  
![](images/dc2945719bb96295e042553eb2fecd145320b5885afb8a5841dc62dbbc2e9049.jpg)  
(a)

![](images/7f2b333433f953514b3e555deb8fc1b2b4ebbd85f3e5942bb3f893fd344c1391.jpg)  
(b)  
Fig. 12. Impact of bandwidth optimization to performance of AQMIX at different levels of collection demands, with estimation error of $\sigma _ { e } ^ { 2 } = 0 . 0 1$

6) Impacts of Channel Estimation Error and Bandwidth Optimization: Fig. 11 plots the total time spent by all UAVs for collecting data and the energy efficiency of the best policy learned by AQMIX in the testing phase on an area of $8 \times 8$ cells. The proposed optimal bandwidth allocation is compared with the equal bandwidth allocation counterpart, where each active SN is assigned an equal frequency bandwidth. The advantage of the proposed bandwidth optimization is clearly demonstrated via superior performance compared to the equal allocation scheme. Furthermore, the robustness of the proposed optimization is also confirmed via the operation under different CSI errors.

Fig. 12 compares the proposed bandwidth optimization with the equal allocation for various data density parameters. While the performance gain is marginal in low data densities, it becomes substantial for denser data scenarios. This is because, when data availability is spare, the collection time is relatively short compared to the total operating time, making the gain from reducing the communication time negligible. On the other hand, when there are more data to collect, the impact of bandwidth optimization becomes more pronounced, leading to noticeable performance improvements.

![](images/9697ab38bd8d1a1b2c223418ef336e97f8c5f0c656a9bfb4ba5aeb87117040b3.jpg)  
(a) Proposed AQMIX

![](images/9ebadfcc6c653d7eb9e7061d244651624738c30ff5f0a623f4396783bf52068e.jpg)  
(b) QMIX

![](images/620f7d5056717e245e91e910ccfc18f270c63651f40782d76c41c0e8ccc3e73c.jpg)  
(c) AIQL  
Fig. 13. Trajectories generated by learned policies. Green ‘X’ symbols represent UAV’s initial/final locations, stars represent hovering locations, small black and gray dots represents SNs containing and non-containing data, respectively.

Finally, Fig. 13 visualizes the trajectories generated by all learned policies for one of the testing scenarios, on the collecting area of $8 \times 8$ cells with two UAVs. This figure once again highlights the superiority of the proposed method, AQMIX, as demonstrated by the cooperation between UAVs, which helps avoid trajectory overlaps between different UAVs, as observed in the other algorithms.

## VIII. CONCLUSION

In this work, we have presented a solution to the problem of cooperative UAV data collection under realistic conditions characterized by asynchronization in the learning environment, primarily driven by stochastic data availability and limited inter-UAV communication. A key challenge addressed in this study is the incomplete information and asynchronous decision-making among UAVs, which are inherent to such scenarios. To tackle these issues, we introduced an asynchronous multi-agent learning framework, AQMIX, which has demonstrated superior performance and robustness compared to existing reference schemes. Moreover, we conducted a thorough sensitivity analysis of the proposed framework, evaluating its performance under varying system parameters such as communication range, energy budget, and data density. Our results highlight the adaptability and robustness of the framework across a wide range of operational conditions.

While the results presented in this paper are promising, there remains a gap between our solution and its practical implementation. One of the key challenges is the design of an efficient UAV-UAV communication protocol, particularly in determining when a UAV should initiate communication with another and how it should respond while simultaneously moving or collecting data. Another topic is to further enhance the bandwidth utilization efficiency, by allowing the UAVs to operate the full system bandwidth. In this case, inter-UAV interference can be approximated from the channel statistics when computing the UAV hovering time. Beyond the specific case study examined here, we believe that our novel modeling approach and proposed model-free learning solution can offer valuable insights and be applied to other systems where asynchrony exists.

## ACKNOWLEDGMENT

For the purpose of open access, and in fulfilment of the obligations arising from the grant agreement, the author has applied a Creative Commons Attribution 4.0 International (CC BY 4.0) license to any Author Accepted Manuscript version arising from this submission.

## REFERENCES

[1] C. Le, T. X. Vu, and S. Chatzinotas, “Cooperative UAVs with asynchronous multi-agent learning for remote data collection,” in Proc. IEEE Globecom Workshops (GC Wkshps), Dec. 2024, pp. 1–6.

[2] H. Bayerlein, M. Theile, M. Caccamo, and D. Gesbert, “Multi-UAV path planning for wireless data harvesting with deep reinforcement learning,” IEEE Open J. Commun. Soc., vol. 2, pp. 1171–1187, 2021.

[3] O. S. Oubbati, M. Atiquzzaman, H. Lim, A. Rachedi, and A. Lakas, “Synchronizing UAV teams for timely data collection and energy transfer by deep reinforcement learning,” IEEE Trans. Veh. Technol., vol. 71, no. 6, pp. 6682–6697, Jun. 2022.

[4] Z. Li, P. Tong, J. Liu, X. Wang, L. Xie, and H. Dai, “Learningbased data gathering for information freshness in UAV-assisted IoT networks,” IEEE Internet Things J., vol. 10, no. 3, pp. 2557–2573, Feb. 2023.

[5] G. Chen, X. B. Zhai, and C. Li, “Joint optimization of trajectory and user association via reinforcement learning for UAV-aided data collection in wireless networks,” IEEE Trans. Wireless Commun., vol. 22, no. 5, pp. 3128–3143, May 2023.

[6] X. Wang, M. Yi, J. Liu, Y. Zhang, M. Wang, and B. Bai, “Cooperative data collection with multiple UAVs for information freshness in the Internet of Things,” IEEE Trans. Commun., vol. 71, no. 5, pp. 2740–2755, May 2023.

[7] T. Rashid, M. Samvelyan, C. S. D. Witt, G. Farquhar, J. Foerster, and S. Whiteson, “Monotonic value function factorisation for deep multiagent reinforcement learning,” J. Mach. Learn. Res., vol. 21, no. 178, pp. 1–51, 2020.

[8] X. Yuan, Y. Hu, J. Zhang, and A. Schmeink, “Joint user scheduling and UAV trajectory design on completion time minimization for UAVaided data collection,” IEEE Trans. Wireless Commun., vol. 22, no. 6, pp. 3884–3898, Jun. 2023.

[9] C. Zhan, Y. Zeng, and R. Zhang, “Energy-efficient data collection in UAV enabled wireless sensor network,” IEEE Wireless Commun. Lett., vol. 7, no. 3, pp. 328–331, Jun. 2018.

[10] Z. Wang, R. Liu, Q. Liu, J. S. Thompson, and M. Kadoch, “Energyefficient data collection and device positioning in UAV-assisted IoT,” IEEE Internet Things J., vol. 7, no. 2, pp. 1122–1139, Feb. 2020.

[11] C. You and R. Zhang, “3D trajectory optimization in Rician fading for UAV-enabled data harvesting,” IEEE Trans. Wireless Commun., vol. 18, no. 6, pp. 3192–3207, Jun. 2019.

[12] C. Sun, X. Xiong, Z. Zhai, W. Ni, T. Ohtsuki, and X. Wang, “Max–min fair 3D trajectory design and transmission scheduling for solar-powered fixed-wing UAV-assisted data collection,” IEEE Trans. Wireless Commun., vol. 22, no. 12, pp. 8650–8665, Dec. 2023.

[13] M. Samir, S. Sharafeddine, C. M. Assi, T. M. Nguyen, and A. Ghrayeb, “UAV trajectory planning for data collection from time-constrained IoT devices,” IEEE Trans. Wireless Commun., vol. 19, no. 1, pp. 34–46, Jan. 2020.

[14] D.-H. Tran, V.-D. Nguyen, S. Chatzinotas, T. X. Vu, and B. Ottersten, “UAV relay-assisted emergency communications in IoT networks: Resource allocation and trajectory optimization,” IEEE Trans. Wireless Commun., vol. 21, no. 3, pp. 1621–1637, Mar. 2022.

[15] T. Feng, L. Xie, J. Yao, and J. Xu, “UAV-enabled data collection for wireless sensor networks with distributed beamforming,” IEEE Trans. Wireless Commun., vol. 21, no. 2, pp. 1347–1361, Feb. 2022.

[16] P. Du, F. Xie, S. Chen, and X. Zhang, “Time-constrained UAV-aided data collection for IoT networks with energy harvesting,” in Proc. IEEE Conf. Comput. Commun. Workshops (INFOCOM WKSHPS), May 2023, pp. 1–6.

[17] H. Hu, K. Xiong, G. Qu, Q. Ni, P. Fan, and K. B. Letaief, “AoI-minimal trajectory planning and data collection in UAV-assisted wireless powered IoT networks,” IEEE Internet Things J., vol. 8, no. 2, pp. 1211–1223, Jan. 2021.

[18] C. Zhan and Y. Zeng, “Completion time minimization for multi-UAV-enabled data collection,” IEEE Trans. Wireless Commun., vol. 18, no. 10, pp. 4859–4872, Oct. 2019.

[19] C. Zhan and Y. Zeng, “Aerial–ground cost tradeoff for multi-UAVenabled data collection in wireless sensor networks,” IEEE Trans. Commun., vol. 68, no. 3, pp. 1937–1950, Mar. 2020.

[20] J. Zhang et al., “Minimizing the number of deployed UAVs for delaybounded data collection of IoT devices,” in Proc. IEEE Conf. Comput. Commun., May 2021, pp. 1–10.

[21] W. Xu et al., “Minimizing the deployment cost of UAVs for delaysensitive data collection in IoT networks,” IEEE/ACM Trans. Netw., vol. 30, no. 2, pp. 812–825, Apr. 2022.

[22] A. Mostaani, T. X. Vu, H. Habibi, S. Chatzinotas, and B. Ottersten, “Task-oriented communication design at scale,” IEEE Trans. Commun., vol. 73, no. 1, pp. 378–393, Jan. 2025.

[23] R. Ding, F. Gao, and X. S. Shen, “3D UAV trajectory design and frequency band allocation for energy-efficient and fair communication: A deep reinforcement learning approach,” IEEE Trans. Wireless Commun., vol. 19, no. 12, pp. 7796–7809, Dec. 2020.

[24] Y. Wang et al., “Trajectory design for UAV-based Internet of Things data collection: A deep reinforcement learning approach,” IEEE Internet Things J., vol. 9, no. 5, pp. 3899–3912, Mar. 2022.

[25] X. Fan, M. Liu, Y. Chen, S. Sun, Z. Li, and X. Guo, “RIS-assisted UAV for fresh data collection in 3D urban environments: A deep reinforcement learning approach,” IEEE Trans. Veh. Technol., vol. 72, no. 1, pp. 632–647, Jan. 2023.

[26] J. Hu, H. Zhang, L. Song, R. Schober, and H. V. Poor, “Cooperative Internet of UAVs: Distributed trajectory design by multi-agent deep reinforcement learning,” IEEE Trans. Commun., vol. 68, no. 11, pp. 6807–6821, Nov. 2020.

[27] O. S. Oubbati, M. Atiquzzaman, A. Lakas, A. Baz, H. Alhakami, and W. Alhakami, “Multi-UAV-enabled AoI-aware WPCN: A multi-agent reinforcement learning strategy,” in Proc. IEEE Conf. Comput. Commun. Workshops (INFOCOM WKSHPS), May 2021, pp. 1–6.

[28] Y. Emami, K. Li, Y. Niu, and E. Tovar, “AoI minimization using multiagent proximal policy optimization in UAVs-assisted sensor networks,” in Proc. IEEE Int. Conf. Commun., May 2023, pp. 228–233.

[29] K. Messaoudi, O. S. Oubbati, A. Rachedi, and T. Bendouma, “UAV-UGV-based system for AoI minimization in IoT networks,” in Proc. IEEE Int. Conf. Commun., May 2023, pp. 4743–4748.

[30] D. S. Bernstein, R. Givan, N. Immerman, and S. Zilberstein, “The complexity of decentralized control of Markov decision processes,” Math. Operations Res., vol. 27, no. 4, pp. 819–840, Nov. 2002.

[31] S. Omidshafiei, A.-A. Agha-Mohammadi, C. Amato, and J. P. How, “Decentralized control of partially observable Markov decision processes using belief space macro-actions,” in Proc. IEEE Int. Conf. Robot. Autom. (ICRA), May 2015, pp. 5962–5969.

[32] J. Wang and L. Sun, “Reducing bus bunching with asynchronous multiagent reinforcement learning,” in Proc. 30th Int. Joint Conf. Artif. Intell., Aug. 2021, pp. 426–433.

[33] C. Yu et al., “Asynchronous multi-agent reinforcement learning for efficient real-time multi-robot cooperative exploration,” in Proc. Int. Joint Conf. Auto. Agents Multiagent Syst., May 2023, pp. 1107–1115.

[34] Y. Zeng, J. Xu, and R. Zhang, “Energy minimization for wireless communication with rotary-wing UAV,” IEEE Trans. Wireless Commun., vol. 18, no. 4, pp. 2329–2345, Apr. 2019.

[35] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6, pp. 569–572, Dec. 2014.

[36] M. Hausknecht and P. Stone, “Deep recurrent Q-learning for partially observable MDPs,” in Proc. AAAI fall Symp. Ser., 2015, pp. 9–37.

[37] K. Cho et al., “Learning phrase representations using RNN encoder–decoder for statistical machine translation,” 2014, arXiv:1406.1078.

![](images/a0e5363412bc2ce379019219aa5cc205a2982b553f37ba72511627e48cdb0a12.jpg)

Cuong Le received the B.S. and M.S. degrees in computer science from Hanoi University of Science and Technology, Vietnam, in 2021 and 2023, respectively. He is currently pursuing the Ph.D. degree with the Department of Computer Science, National University of Singapore. His research interests are in theoretical computer science, with a current focus on complexity theory and approximation algorithms.

![](images/6ff56f53a4e559b57e2d663ea487292352f603bac27a10ed571ad46308f36aa1.jpg)

Symeon Chatzinotas (Fellow, IEEE) received the M.Eng. degree in telecommunications from the Aristotle University of Thessaloniki, Greece, in 2003, and the M.Sc. and Ph.D. degrees in electronic engineering from the University of Surrey, U.K., in 2006 and 2009, respectively. He is currently a Full Professor/a Chief Scientist I and the Head of the Research Group SIGCOM, Interdisciplinary Centre for Security, Reliability and Trust, University of Luxembourg. In the past, he has lectured as a Visiting Professor with the University of Parma,

Italy, and contributed in several research and development projects for the Institute of Informatics and Telecommunications, the National Center for Scientific Research “Demokritos,” the Institute of Telematics and Informatics, the Center of Research and Technology Hellas, and the Mobile Communications Research Group, Center of Communication Systems Research, University of Surrey. He has authored more than 700 technical papers in refereed international journals, conferences, and scientific books. He received several awards and recognitions, including the IEEE Fellowship and the IEEE Distinguished Contributions Award. He is currently in the editorial board of IEEE TRANSACTIONS ON COMMUNICATIONS, IEEE OPEN JOURNAL OF VEHICULAR TECHNOLOGY, and International Journal of Satellite Communications and Networking.

![](images/88f6dec8d1b9b0329df9ae4fcf4472235aa336676e46aa91c45842b2d7a7202a.jpg)

Thang X. Vu (Senior Member, IEEE) received the B.S. and M.Sc. degrees in electronics and telecommunications engineering from the VNU University of Engineering and Technology, Vietnam, in 2007 and 2009, respectively, and the Ph.D. degree in electrical engineering from the University Paris-Sud, France, in 2014. In 2010, he received the Allocation de Recherche Fellowship to study Ph.D. in France. From July 2014 to January 2016, he was a Post-Doctoral Researcher with Singapore University of Technology and Design (SUTD), Singapore.

Currently, he is a Research Scientist with the Interdisciplinary Centre for Security, Reliability and Trust (SnT), University of Luxembourg. He has successfully acquired several Luxembourg national and ESA projects with a total funding of 2.6 MEURs, as a PI and a vice PI. His research interests include wireless communications and non-terrestrial networks, with particular interests in open RAN and applications of optimization and machine learning on design and analyze the multi-layer 6G networks. He was a recipient of the SigTelCom 2019 Best Paper Award. He has served as an Associate Editor for IEEE COMMUNICATIONS LETTERS. He is serving as an Associate Editor for IEEE COMMUNICATIONS SURVEYS AND TUTORIALS.