# UAV Trajectory Planning for AoI-Minimal Data Collection in UAV-Aided IoT Networks by Transformer

Botao Zhu , Ebrahim Bedeer , Member, IEEE, Ha H. Nguyen , Senior Member, IEEE, Robert Barton , Member, IEEE, and Zhen Gao , Member, IEEE

Abstract— Maintaining freshness of data collection in Internetof-Things (IoT) networks has attracted increasing attention. By taking into account age-of-information (AoI), we investigate the trajectory planning problem of an unmanned aerial vehicle (UAV) that is used to aid a cluster-based IoT network. An optimization problem is formulated to minimize the total AoI of the collected data by the UAV from the ground IoT network. Since the total AoI of the IoT network depends on the flight time of the UAV and the data collection time at hovering points, we jointly optimize the selection of hovering points and the visiting order to these points. We exploit the state-of-the-art transformer and the weighted A\*, which is a path search algorithm, to design a machine learning algorithm to solve the formulated problem. The whole UAV-IoT system is fed into the encoder network of the proposed algorithm, and the algorithm’s decoder network outputs the visiting order to ground clusters. Then, the weighted A\* is used to find the hovering point for each cluster in the ground IoT network. Simulation results show that the trained model by the proposed algorithm has a good generalization ability to generate solutions for IoT networks with different numbers of ground clusters, without the need to retrain the model. Furthermore, results show that our proposed algorithm can find better UAV trajectories with the minimum total AoI when compared to other algorithms.

Index Terms— AoI, IoT, transformer, trajectory optimization, UAV.

## I. INTRODUCTION

high maneuvering capability and mobility, UAVs can be used as wireless relays or mobile base stations to provide reliable communications and better coverage for ground devices [1].

Thanks to these advantages, UAVs can be flexibly deployed to provide fast and reliable network access in different applications, such as disasters [2], surveillance [3], monitoring [4], to name a few.

Since UAVs can fly close to the ground devices and provide low-altitude air-to-ground communication links with them, UAVs can be deployed to hover the area of interest to collect data from ground Internet-of-Things (IoT) networks. By doing so, UAV-aided data collection can save the energy of devices in traditional IoT networks, thus extending their lifetime [5]. However, maintaining the freshness of the collected information is an important issue in time-sensitive IoT applications, such as environmental monitoring and safety protection. In these applications, the generated data needs to be sent to the destination as soon as possible. Outdated information can lead to incorrect control and even cause major disasters [6]. Therefore, it is essential to ensure the freshness of the data received at the destination. To measure the freshness of information, the age of information (AoI) as a new performance metric was proposed in [7]. In a nutshell, AoI describes the amount of time elapsed since the generation of the most recent data update. AoI-based data collection can guarantee information freshness in IoT networks, which is quite different from traditional delay-based and throughputbased metrics [8]. As such, it has attracted increasing attention.

Due to the importance of AoI, a number of studies have been carried out on AoI-oriented data collection in UAV-assisted wireless networks. In [9], the authors aimed to minimize the average AoI of the system by optimizing the trajectory of the UAV in a UAV-aided data collection system. In [10], the authors optimized the trajectory of the UAV to minimize the maximal AoI and the average AoI of sensors. In [11], the authors assumed the UAV supports three modes to collect data and jointly optimize the trajectory and data collection modes of the UAV to minimize the average AoI of all ground nodes. In [12], the UAV trajectory, energy, and service time allocation were jointly optimized by an iterative algorithm in order to minimize the overall peak AoI of the system. The authors in [13] developed an energy-efficient navigation policy for the UAV to improve data freshness of the IoT network. In order to minimize the weighted sum of AoI, the authors in [14] jointly optimized the flight trajectory of the UAV and the transmission scheduling of sensors. From the above discussion, it can be seen that AoI-oriented data collection problems in the UAV-assisted IoT network are typically related to UAV’s trajectory design.

When collecting data in the UAV-assisted IoT network, if the UAV is dispatched to visit every ground IoT device, the energy consumption of the UAV will increase because of the increased UAV trajectory. Hence, to reduce the energy consumption of the UAV, clusters-based model have been extensively investigated in UAV-assisted wireless networks. For instance, in [15], to gather compressive data measurements, the authors divide the sensor network into multiple clusters. In each cluster, all nodes build a forwarding tree based on compressive data gathering to send data to the cluster head (CH). The UAV then traverses all CHs to collect the aggregated data. The authors jointly optimized the UAV trajectory, CH selection, and forward tree construction to minimize the total transmit power in the network. In [16], the authors consider a pre-clustered network where a UAV equipped with multiple antennas communicates with multiple ground users simultaneously, in a given time slot, using space division multiple access. The authors jointly optimized the time slot allocation and the UAV hovering time to minimize the overall energy consumption. In [17], the authors con sidered a UAV-enabled data collection system for massive machine-type communications (mMTC) where machine-type communication devices (MTCDs) are divided into severa clusters. A UAV visits each hovering position which corresponds to a MTCD cluster and sequentially collects data from each MTCD in the corresponding cluster. They formulated a problem of minimizing the total energy consumption of the system. In our previous work [5], we considered using a UAV to collect data from a clustered IoT network, where the hovering points of the UAV are determined by the unknown CHs location. In other words, in [5], we jointly select the CHs and their visiting order to minimize the total energy consumption. In this paper, we examine the scenario where the UAV collects data from a group of clusters and the UAV only interact with the CHs. The problem of interest in this paper is to jointly optimize the UAV’s hovering points and trajectory to achieve the minimal AoI data collection in a cluster-based IoT network. The optimization problem is formulated as a traveling salesman problem (TSP) with neighborhoods (TSPN), which is extremely challenging because it includes a continuous problem (optimization of hovering points) and a combinatoria problem (optimization of visiting order).

The hovering points of the UAV and the visiting order to these hovering points have a great impact on the flying time of the UAV and data collection time, which directly influence the total AoI of collected data. There have been some works on solving the TSPN efficiently. In [18], the Dubins TSPN was converted to a generalized TSP (GTSP) by using the sampling-based roadmap method, and then to an asymmetric TSP that can be addressed by the Lin-Kernighan heuristic algorithm. To handle the continuous optimization problem of waypoints within each circular neighborhood, the authors in [19] proposed a discretization scheme that equidistantly samples possible locations along the circular border of the interest neighborhood to determine the locations of the waypoints. In this paper, in order to reduce the computational complexity for solving the joint optimization of the UAV’s hovering points and trajectory to achieve the minimal AoI data collection in a cluster-based IoT network, we transform the formulated continuous optimization TSPN into a GTSP by borrowing the sampling-based idea. The transformed GTSP is a combinatorial optimization problem that can be solved using traditional methods, such as exact algorithms, approximate algorithms, or heuristic algorithms. However, these traditional algorithms may not achieve a good balance between optimality and computational complexity. Thus, by considering optimality, computational complexity, and generality, we shall develop a machine learning-based algorithm to solve the transformed GTSP, i.e., the UAV’s trajectory design problem.

Machine learning has been explored as a promising technique for solving UAV’s trajectory planning problems in UAV-assisted IoT networks. To minimize the weighted sum-AoI in a UAV-assisted network, the authors in [20] applied deep reinforcement learning (DRL) to optimize the UAV’s trajectory using a deep Q network (DQN) and an artificial neural network (ANN). In [21], the authors utilized Q-learning to optimize AoI-optimal UAV path by considering the deadline constraints of data in the UAV-aided sensing network. In [22], the authors jointly optimized the UAV’s trajectory and scheduling of the status update packets to minimize the normalized weighted sum of AoI in a UAV-assisted wireless network. Specifically, they used ANN, DQN, and long short-term memory (LSTM) to develop a DRL algorithm for learning the UAV trajectory in large-scale networks. Different from these works, we employ the state-of-the-art transformer and the weighted A\* search method to design a UAV trajectory planning algorithm for AoI-oriented data collection.

Transformer was originally proposed by Google as a sequence-to-sequence model to deal with machine translation problem [23]. It has achieved great success in many areas of artificial intelligence in the past four years, such as computer vision, audio processing, document summarization, and document generation. Some researchers also attempt to use transformer and its variants to tackle combinatorial problems, such as the TSP. In [24], the cities in the TSP were encoded by a transformer and decoded sequentially through a query consisting of the last three cities in the partial tour. The used transformer was trained by reinforcement learning. In [25], the authors also used the transformer architecture as the encoder network and the decoder network outputs the result sequentially based on the embeddings from the encoder and the outputs generated at previous steps. The encoder and decoder networks were trained using a reinforce algorithm with a deterministic greedy baseline. The authors in [26] proposed a transformer-based framework to automatically learn improved heuristics on two representative routing problems: the TSP and capacitated vehicle routing problem (CVRP). In [27], the authors used the standard transformer architecture to tackle TSP and achieve an improved performance over recent learned heuristics. Inspired by the success of employing transformer in solving various problems of route planning, we propose the transformer-weighted-A\* (TWA\*) algorithm in this paper for solving our formulated GTSP combinatorial optimization problem. Although the Ptr-A\* algorithm proposed in our previous work [5] achieves good performance in solving the GTSP, the TWA\* algorithm has the following two important advantages over the Ptr-A\* algorithm. First, TWA\* does not relay on past hidden states like Ptr- $\mathbf { \nabla } \cdot \mathbf { A } ^ { * }$ , and thus, avoids losing past information. Second, TWA\* has the ability of parallel computation which makes it faster than Ptr- $\mathbf { \nabla } \cdot \mathbf { A } ^ { * }$

The main contributions of this paper are summarized as follows

1) We propose an AoI-oriented data collection model in a cluster-based IoT network and formulate a total AoI-minimal trajectory planning problem where the hovering points of the UAV and the visiting order to these points are jointly optimized.

2) We view the formulated problem as a “machine translation” problem where the “source language” is the whole UAV-IoT network and the “target language” is the UAV trajectory with the minimal total AoI. The state-of-theart TWA\* is employed to solve the formulated problem. The parameters of the proposed algorithm are trained by reinforcement learning that only needs the reward calculation.

3) The learned policy by the proposed algorithm generalizes well on different sizes of problem instances. In other words, the trained model by the proposed algorithm can automatically find a trajectory with the minimal total AoI for new problem instances, without retraining the model.

4) Extensive simulations are conducted to evaluate the performance of the proposed algorithm. Results show that the proposed algorithm achieves significant performance gain in maintaining data freshness while reducing computation time when compared with other baseline algorithms.

The rest of this paper is organized as follows. Section II introduces the system model and presents the formulated problem. Section III develops the proposed algorithm. Section IV provides simulation results. Finally, Section V concludes the paper.

## II. SYSTEM MODEL AND PROBLEM FORMULATION

We consider a UAV-assisted IoT network that consists of one rotary-wing UAV, one ground base station (BS) located at $b _ { 0 } .$ and M clusters of ground sensor nodes. Specifically, each cluster $m , m = 1 , \ldots , M$ , has one CH, located as $b _ { m } ,$ and $N _ { m }$ ordinary sensor nodes, located at as $B _ { m } = \{ b _ { m } ^ { ( 1 ) } , \ldots , b _ { m } ^ { ( N _ { m } ) } \}$ <sup>=</sup>The ground IoT network performs some sensing tasks in the surrounding area where the ordinary sensor nodes are responsible for sampling data and forwarding the collected data to their corresponding CHs. The UAV is dispatched from the start hovering point $c _ { 0 }$ which is directly above $b _ { 0 }$ to visit M mission hovering points $\{ c _ { 1 } , \hdots , c _ { m } , \hdots , c _ { M } \}$ by a pre-designed trajectory for data collection, and then flies back to $c _ { 0 }$ after completing the data collection task. Each hovering point corresponds to one ground cluster and its position will be determined by the proposed algorithm. The three-dimensional (3D) Cartesian coordinates system is considered to define positions of hovering points and all CHs. The coordinate of the m-th hovering point is denoted by $c _ { m } = ( x _ { c _ { m } } , y _ { c _ { m } } , H ) \in \mathbb { R } ^ { 3 }$ , where H is the flight height of <sup>= ( m m )</sup>the UAV, whereas the location of the corresponding ground CH is given by $b _ { m } = ( x _ { b _ { m } } , y _ { b _ { m } } , 0 ) \in \mathbb { R } ^ { 3 }$

![](images/0670c15ab882413ac680ddbb8f5a23f76653c376e364b3e0a4fc3b6c63f2e62c.jpg)  
Fig. 1. System model of a UAV-assisted IoT network.

<sup>= ( m m 0)</sup>We assume that the rotary-wing UAV supports a flying-hovering mode without considering accelerationdeceleration, i.e., it flies to the hovering points with a fixed speed $v _ { \mathrm { U A V } }$ and hovers at these points with static status to collect data from ground CHs. We illustrate the UAV-assisted data collecting process in Fig. 1. The UAV takes off from $^ { c _ { 0 } , }$ determines the position of the hovering point $c _ { 2 }$ that will be visited first and arrives at it. The UAV repeats this procedure until data collection of all clusters is completed, and flies back to $c _ { 0 }$ . Hence, the final trajectory of the UAV in this example is $\{ c _ { 0 } , c _ { 2 } , c _ { 3 } , c _ { 4 } , c _ { 1 } , c _ { 0 } \}$

## A. Data Collection Model

When the UAV arrives at $c _ { m } ,$ it sends a beacon message to wake up the corresponding CH $b _ { m }$ from its sleep mode. The beacon message includes the type of sensor nodes to be activated in response to the beacon, the data collection height of the UAV, a threshold to limit the number of sensor nodes in the CH (if necessary), and a trailer that has error detection capabilities. Then, $b _ { m }$ switches to its active mode and informs its member nodes in the same cluster to sample and send their sampled data sequentially according to the pre-allocated equallength time slots using time-division multiplexing (TDM) protocol to avoid collision. We consider the generate-at-will model [28] as the data sampling model for all ordinary sensor nodes, by which nodes can generate information updates at any time. Specifically, we assume that each node can generate an update message of size $L _ { \mathrm { d a t a } }$ only in its allocated time slot to eliminate the waiting time. Also, each message has a time stamp, which is the start of each time slot. The length of a time slot is denoted as τ seconds. After the CH located at $b _ { m }$ finishes collecting data from its member nodes, it will forward the collected data to the UAV. For ease of analysis, the wake-up time of nodes, including CHs and all ordinary nodes, and the information sampling time of each node are assumed negligible as compared to the data collection time. Thus, the data collection time of the UAV at each hovering point mainly consists of two parts: the data transmission time from ordinary nodes to their CHs and the time consumed for forwarding the collected data from CHs to the UAV.

We consider both the line-of-sight (LoS) and non-line-ofsight (NLoS) links to design the ground-to-air communication when the UAV hovers at mission hovering points. The LoS link probability is related to environment, elevation angle, and transmission distance, which can be expressed as [29]

$$
P _ { c _ { m } } ^ { ( \mathrm { L o S } ) } = \frac { 1 } { 1 + \beta \exp \left( - \widetilde { \beta } \left( \theta _ { c _ { m } } - \beta \right) \right) } ,\tag{1}
$$

where $\beta$ and $\widetilde { \beta }$ are constants determined by the environment, $\begin{array} { r l } { \theta _ { c _ { m } } } & { { } = } \end{array}$ arctan $( H / R _ { ( c _ { m } , b _ { m } ) } )$ is the elevation angle between $b _ { m }$ <sup>m m</sup>and the UAV when it hovers at c<sub>m</sub>, $\begin{array} { r c l } { R _ { ( c _ { m } , b _ { m } ) } } & { = } & { \sqrt { \left( x _ { c _ { m } } - x _ { b _ { m } } \right) ^ { 2 } + \left( y _ { c _ { m } } - y _ { b _ { m } } \right) ^ { 2 } } } \end{array}$ is the horizontal distance between the CH $b _ { m }$ and the hovering point. Correspondingly, the probability of NLoS is given by $P _ { c _ { m } } ^ { ( \mathrm { N L o S } ) } = 1 - P _ { c _ { m } } ^ { ( \mathrm { L o S } ) }$ . In addition, the path loss models of LoS and NLoS between the CH $b _ { m }$ and the UAV follow [30]

$$
L _ { c _ { m } } ^ { ( \mathrm { L o S } ) } = 2 0 \log _ { 1 0 } \left( \frac { 4 \pi f _ { c } d _ { ( c _ { m } , b _ { m } ) } } { v _ { \mathrm { l i g h t } } } \right) + \xi _ { \mathrm { L o S } } ,\tag{2}
$$

$$
L _ { c _ { m } } ^ { ( \mathrm { N L o S } ) } = 2 0 \log _ { 1 0 } \left( \frac { 4 \pi f _ { c } d _ { ( c _ { m } , b _ { m } ) } } { v _ { \mathrm { l i g h t } } } \right) + \xi _ { \mathrm { N L o S } } ,\tag{3}
$$

where $f _ { c }$ is the carrier frequency, v<sub>light</sub> is the speed of light, $d _ { ( c _ { m } , b _ { m } ) } = \sqrt { H ^ { 2 } + R _ { ( c _ { m } , b _ { m } ) } ^ { 2 } }$ is the distance between the UAV and the CH $\dot { b _ { m } } , \xi _ { \mathrm { L o S } }$ and ξ<sub>NLoS</sub> $\left( \xi _ { \mathrm { L o S } } < \xi _ { \mathrm { N L o S } } \right)$ are the excessive path losses in LoS and NLoS links, respectively. We consider the average path loss to describe the link from the ground CH to the UAV, which can be expressed as

$$
\overline { { L } } _ { c _ { m } } = P _ { c _ { m } } ^ { ( \mathrm { L o S } ) } L _ { c _ { m } } ^ { ( \mathrm { L o S } ) } + P _ { c _ { m } } ^ { ( \mathrm { N L o S } ) } L _ { c _ { m } } ^ { ( \mathrm { N L o S } ) } .\tag{4}
$$

To avoid the interference among CHs, we assume that only one CH can transmit data to the UAV at any given time. Hence, the average available transmission rate in bits per second (bps) from CH $b _ { m }$ to the UAV can be expressed as $r _ { c _ { m } } = B _ { \mathrm { w i d t h } } \log _ { 2 } { ( 1 + \gamma _ { c _ { m } } ) }$ , where $B _ { \mathrm { w i d t h } }$ is the channel bandwidth in hertz (Hz), $\gamma _ { c _ { m } } = { P _ { \mathrm { C H } } } / \left( { \sigma ^ { 2 } 1 0 ^ { \overline { { L } } _ { c _ { m } } / 1 0 } } \right)$ is the signal-to-noise ratio (SNR) of the transmission link, $\sigma ^ { 2 }$ is the noise power at the UAV, and $P _ { \mathrm { C H } }$ is the transmission power of the CH. Regarding the transmission quality, we set a SNR threshold $\gamma _ { \mathrm { t h } }$ and the transmission is considered successful if the SNR is greater than the threshold. Thus, the SNR constraint at the UAV receiver is given as

$$
\gamma _ { c _ { m } } \geq \gamma _ { \mathrm { t h } } .\tag{5}
$$

Lemma 1: Given the fixed flight height $H , c _ { m }$ should be located in a horizontal disk region centered at the position that directly above $b _ { m }$ and having the radius $R ^ { * }$ which can

guarantee that the UAV successfully receives data. When $R _ { ( c _ { m } , b _ { m } ) } = R ^ { * }$ , the received SNR of the UAV at $c _ { m }$ is equal <sup>m</sup>to γ<sub>th</sub>.

Proof : See Appendix A.

Based on Lemma 1, we formally define a hovering disk region for each mission hovering point (excluding the start point $c _ { 0 } )$ as

$$
O _ { m } = \{ c _ { m } : | | c _ { m } - b ^ { \prime } { } _ { m } | | = R _ { ( c _ { m } , b _ { m } ) } \leq { } R ^ { * } \}\tag{6}
$$

where $\boldsymbol { b } ^ { \prime } \boldsymbol { m } = ( x _ { b _ { m } } , y _ { b _ { m } } , H ) \in \mathbb { R } ^ { 3 }$ is the center of the disk $O _ { m } .$ , and $R ^ { * }$ <sup>( m m )</sup>is the radius to maintain a pre-defined qualityof-service, which can be found numerically. As long as the UAV enters a hovering disk region, it can collect data from the corresponding ground CH. The total data collection time of the UAV at $c _ { m } \in O _ { m }$ (or its hovering time) can be simply written as

$$
T _ { c _ { m } } ^ { \mathrm { ( h o v ) } } = N _ { m } \tau + \frac { N _ { m } L _ { \mathrm { d a t a } } } { r _ { c _ { m } } }\tag{7}
$$

where the first term in the right hand side is the time consumed for transmitting data from ordinary nodes to their corresponding CH $b _ { m }$ , and the second term is the data transmission time from $b _ { m }$ to the UAV. Therefore, the energy consumption of propulsion-related and communication-related activities of the UAV while hovering at $c _ { m }$ is expressed as

$$
E _ { c _ { m } } = P _ { \mathrm { h o v } } T _ { c _ { m } } ^ { \mathrm { ( h o v ) } } + P _ { \mathrm { c o m } } \frac { N _ { m } L _ { \mathrm { d a t a } } } { r _ { c _ { m } } }\tag{8}
$$

where $P _ { \mathrm { h o v } }$ and $P _ { \mathrm { c o m } }$ are the UAV’s powers for hovering and communication, respectively. After finishing the data collection task, $b _ { m }$ switches to the sleep model for saving energy. The UAV continues to select the next hovering point and executes the same processes to collect the sensed data from the corresponding ground cluster.

## B. UAV’s Mobility Model

Without loss of generality, the flight trajectory of the UAV can be seen as a permutation of the visiting order to M mission hovering points, with the start point being $c _ { 0 } .$ , i.e., $\begin{array} { r c l } { { \pmb { c } } } & { { = } } & { { \left\{ c _ { 0 } , c _ { 1 } , \ldots , c _ { M } \right\} } } \end{array}$ . The set of all pos-<sup>=</sup>sible permutations is denoted as Φ with the size of M . We represent one of the permutations as $\pi =$ $\{ \pi ( 0 ) , \ldots , \pi ( M + 1 ) \}$ and express the ordered hovering points as $c _ { \pi } = \{ c _ { \pi ( 0 ) } , c _ { \pi ( 1 ) } , \ldots , c _ { \pi ( M ) } , c _ { \pi ( M + 1 ) } \}$ , where $c _ { \pi ( t ) } , t =$ $0 , \ldots , M + 1$ <sup>=</sup>, is the hovering point that is visited at step t in the trajectory, and $c _ { \pi ( 0 ) } = c _ { \pi ( M + 1 ) } = c _ { 0 } $ . For ease of understanding, if the hovering point $c _ { m }$ is visited at step t, its corresponding cluster of ground ordinary nodes $( B _ { m } )$ and the number of ordinary nodes $( N _ { m } )$ are redefined as $B _ { \pi ( t ) }$ and $N _ { \pi ( t ) }$ , respectively.

After finishing data collection at $c _ { \pi ( t ) }$ with the hovering model, the UAV horizontally flies to the next hovering point $c _ { \pi ( t + 1 ) }$ along the line segment connecting $c _ { \pi ( t ) }$ and $c _ { \pi ( t + 1 ) }$ The flying time of the UAV during this period is given by

$$
T _ { ( c _ { \pi ( t ) } , c _ { \pi ( t + 1 ) } ) } ^ { ( \mathrm { f i y } ) } = \frac { \left| \left| c _ { \pi ( t ) } - c _ { \pi ( t + 1 ) } \right| \right| } { v _ { \mathrm { U A V } } }\tag{9}
$$

where $| | c _ { \pi ( t ) } - c _ { \pi ( t + 1 ) } | |$ is the Euclidean distance between $c _ { \pi ( t ) }$ and $c _ { \pi ( t + 1 ) }$

Following [31], the propulsion power consumption of the UAV for horizontal movement is the function of speed v<sub>UAV</sub> and given by

$$
\begin{array} { r l r } & { } & { P _ { \mathrm { m o v } } \big ( \boldsymbol { v } _ { \mathrm { U A V } } \big ) = P _ { 0 } \left( 1 + \frac { 3 v _ { \mathrm { U A V } } ^ { 2 } } { U _ { \mathrm { t i p } } ^ { 2 } } \right) + P _ { 1 } \left( \left( 1 + \frac { v _ { \mathrm { U A V } } ^ { 4 } } { 4 v _ { 0 } ^ { 4 } } \right) ^ { 1 / 2 } \right. } \\ & { } & { \qquad \left. - \ \frac { v _ { \mathrm { U A V } } ^ { 2 } } { 2 v _ { 0 } ^ { 2 } } \right) ^ { 1 / 2 } + \frac { 1 } { 2 } d _ { 0 } \rho s _ { 0 } \delta v _ { \mathrm { U A V } } ^ { 3 } } \end{array}\tag{10}
$$

where $P _ { 0 }$ and $P _ { 1 }$ represent, respectively, the blade profile power and induced power in the hovering state, $U _ { \mathrm { t i p } }$ is the tip speed of the rotor blade of the UAV, $v _ { 0 }$ is the mean rotor induced velocity in the hovering state, $d _ { 0 }$ denotes the fuselage drag ratio, $s _ { 0 }$ represents the rotor solidity, $\rho$ is the density of air, and δ denotes the area of the rotor disk. According to the analysis in [31], the power consumption $P _ { \mathrm { m o v } } ( v _ { \mathrm { U A V } } )$ firstly decreases and then increases with the increasing value of the speed $v _ { \mathrm { U A V } }$ . The energy consumption in the UAV’s flight from $c _ { \pi ( t ) }$ to $c _ { \pi ( t + 1 ) }$ is computed as

$$
E _ { ( c _ { \pi ( t ) } , c _ { \pi ( t + 1 ) } ) } = P _ { \mathrm { m o v } } ( v _ { \mathrm { U A V } } ) T _ { ( c _ { \pi ( t ) } , c _ { \pi ( t + 1 ) } ) } ^ { ( \mathrm { f l y } ) } .\tag{11}
$$

In the hovering state, the power consumption of the UAV can be obtained by substituting $v _ { \mathrm { U A V } } = 0$ into (10), $P _ { \mathrm { h o v } } = P _ { \mathrm { 0 } } { + } P _ { \mathrm { 1 } }$ which is a constant value.

## C. Age of Information Model in a UAV-IoT System

We use the AoI metric to measure the freshness of information. According to the definition of AoI in [32], the AoI of a packet collected from node $b _ { \pi ( t ) } ^ { ( n ) }$ in the $\pi ( t )$ -th visited cluster at time ζ is defined as

$$
A _ { \pi ( t ) } ^ { ( n ) } ( \zeta ) = \left( \zeta - u _ { \pi ( t ) } ^ { ( n ) } ( \zeta ) \right) ^ { + }\tag{12}
$$

where $u _ { \pi ( t ) } ^ { ( n ) } ( \zeta )$ is the instant at which the packet is generated, and $( x ) ^ { + } ~ = ~ \operatorname* { m a x } \{ 0 , x \}$ . When $\zeta ~ < ~ u _ { \pi ( t ) } ^ { ( n ) } ( \zeta )$ , we define $A _ { \pi ( t ) } ^ { ( n ) } ( \zeta ) = 0$ . This is because the packet of node $b _ { \pi ( t ) } ^ { ( n ) }$ has not been sampled. It is evident that the AoI of a packet will increase with time. In the considered UAV-IoT system, the BS is seen as the observer, thus, the AoI of a data packet can be seen as the amount of time elapsed from the instant at which the packet is generated to the instant at which the UAV flies back with the collected data to the BS.

For ease of analysis, for any ordinary node $b _ { \pi ( t ) } ^ { ( n ) } , n ~ =$ $1 , \ldots , N _ { \pi ( t ) }$ in the $\pi ( t )$ -th visited cluster, the AoI of its packet can be simply divided into two components. The first component is the time needed for the CH of its associated cluster to collect data from $b _ { \pi ( t ) } ^ { ( n ) }$ and other nodes whose data have not been gathered (i.e., nodes $b _ { \pi ( t ) } ^ { ( n + 1 ) } , \dots , b _ { \pi ( t ) } ^ { ( N _ { \pi ( t ) } ) } )$ and forward the collected data to the UAV. The second component is the time consumed by the UAV to carry the packet of $b _ { \pi ( t ) } ^ { ( n ) }$ to the end point $c _ { \pi ( M + 1 ) }$ . Specifically, this period includes the flight time of the UAV to unvisited ground clusters and the data collection time in these clusters. For example, after completing the data collection at $c _ { \pi ( t ) }$ , the UAV will fly to the next hovering point $c _ { \pi ( t + 1 ) }$ and gather information from the corresponding cluster. During this period, the AoI of the packet of $b _ { \pi ( t ) } ^ { ( n ) }$ increases with time, which is the sum of the flight time $T _ { ( c _ { \pi ( t ) } , c _ { \pi ( t + 1 ) } ) }$ from $c _ { \pi ( t ) } ~ \mathrm { t o } ~ c _ { \pi ( t + 1 ) }$ and data collection time $T _ { c _ { \pi ( t + 1 ) } }$ at hovering point $c _ { \pi ( t + 1 ) }$ . Then, the UAV performs the same process to unvisited clusters until it returns to the end point. The time sequence of data collection in the UAV-IoT system is illustrated in Fig. 2. Mathematically, the total AoI of the packet generated by $\bar { b _ { \pi ( t ) } ^ { ( n ) } }$ in the UAV-IoT system is given as

![](images/25b7b59cbf07ec308418546917a6ee1e3c25c646260eb8c3a3780e089b10f914.jpg)  
Fig. 2. The time sequence of data collection in the considered UAV-IoT system.

$$
\begin{array} { l } { { \displaystyle { \cal A } _ { \pi ( t ) } ^ { ( n ) } = \underbrace { \left( N _ { \pi ( t ) } - ( n - 1 ) \right) \tau + \frac { N _ { \pi ( t ) } L _ { \mathrm { d a t a } } } { r _ { c _ { \pi ( t ) } } } } _ { \mathrm { f r s t ~ c o m p o n e n t } } } } \\ { { + \underbrace { \sum _ { g = t } ^ { M - 1 } \left( T _ { ( c _ { \pi ( g ) } , c _ { \pi ( g + 1 ) } ) } ^ { ( \mathrm { f l y } ) } + T _ { c _ { \pi ( g + 1 ) } } ^ { ( \mathrm { h o v } ) } \right) + T _ { ( c _ { \pi ( M ) } , c _ { \pi ( M + 1 ) } ) } ^ { ( \mathrm { f l y } ) } } _ { \mathrm { s e c o n d ~ c o m p o n e n t } } } } \end{array}\tag{13}
$$

which can be further simplified as

$$
A _ { \pi ( t ) } ^ { ( n ) } = \sum _ { g = t } ^ { M } \left( T _ { c _ { \pi ( g ) } } ^ { ( \mathrm { h o v } ) } + T _ { ( c _ { \pi ( g ) } , c _ { \pi ( g + 1 ) } ) } ^ { ( \mathrm { f l y } ) } \right) - ( n - 1 ) \tau .\tag{14}
$$

For packets of nodes in the same cluster, we have

$$
A _ { \pi ( t ) } ^ { ( 1 ) } > A _ { \pi ( t ) } ^ { ( 2 ) } \cdot \cdot \cdot > A _ { \pi ( t ) } ^ { ( N _ { \pi ( t ) } ) } .\tag{15}
$$

On the other hand, the AoIs of packets in different clusters should satisfy

$$
{ \cal A } _ { \pi ( 1 ) } ^ { ( n ) } > { \cal A } _ { \pi ( 2 ) } ^ { ( n ) } > \cdots > { \cal A } _ { \pi ( M ) } ^ { ( n ) } .\tag{16}
$$

## D. Problem Formulation

The total AoI of all ordinary nodes in the network can be computed as

$$
\begin{array} { l } { { \overline { { A } } = \displaystyle \sum _ { t = 1 } ^ { M } \sum _ { n = 1 } ^ { N _ { \pi ( t ) } } A _ { \pi ( t ) } ^ { ( n ) } } } \\ { { \ } } \\ { { \displaystyle \quad = \sum _ { t = 1 } ^ { M } \sum _ { n = 1 } ^ { N _ { \pi ( t ) } } \sum _ { g = t } ^ { M } \left( T _ { c _ { \pi ( g ) } } ^ { \mathrm { ( h o v ) } } + T _ { ( c _ { \pi ( g ) } , c _ { \pi ( g + 1 ) } ) } ^ { \mathrm { ( f l y ) } } \right) } } \\ { { \displaystyle \qquad - \sum _ { t = 1 } ^ { M } \sum _ { n = 1 } ^ { N _ { \pi ( t ) } } ( n - 1 ) \tau . } } \end{array}\tag{17}
$$

According to (17), the total AoI is expressed as a weighted sum of the flight time of the UAV and the data collection time at each hovering point, which is determined by the locations of hovering points c, the visiting order to these hovering points π. It is evident that the hovering points of the UAV and its trajectory have a strong impact on the total AoI of data. If the position of any hovering point $c _ { m }$ is close to the center of the disk region $O _ { m }$ , a high data transmission rate can be achieved. As a result, the data transmission time from CHs to the UAV can be reduced, even though the UAV may have a longer flight trajectory, and hence the flight time. Conversely, if the UAV is located near the boundary of the disk region, the length of the UAV’s trajectory might be reduced, but it will result in a lower data transmission rate, and hence increased data transmission time.

Our objective is to jointly find the hovering point from each disk and plan the visiting order to these hovering points for the UAV to minimize the total AoI of data in the considered UAV-IoT system. The optimization problem is expressed as follows

$$
\mathcal { P } _ { 1 } : \operatorname* { m i n } _ { c , \pi } \ : \ : \overline { { A } } \left( c , \pi \right) ,\tag{18a}
$$

$$
( 5 ) , ( 7 ) , ( 9 ) , ( 1 5 ) , \mathrm { a n d } ( 1 6 ) .\tag{18b}
$$

Constraint (18b) is the trajectory constraint. The SNR constraint is given in (5), and (7) is the data collection constraint. The flight time constraint is expressed as (9). AoI constraints are (15) and (16). It is evident that the formulated problem $\mathcal { P } _ { 1 }$ is a TSPN [33], which combines the determination of hovering points at each disk with the problem of trajectory planning of the UAV. The traditional TSPN problem involves finding a minimum-cost tour (i.e., the total length of the tour is minimum) that travels each region exactly once for a collection of compact regions before returning to the initial departure point [34]. However, our formulated problem not only considers the traveling cost but also the cost spent at each hovering point. The problem $\mathcal { P } _ { 1 }$ is extremely challenging because it is composed of a continuous problem (optimization of hovering points c) and a combinatorial problem (optimization of visiting order π). Given a set of hovering points c, the optimization of $\pi$ can be viewed as the TSP, which can be normally be solved quite effectively by some dedicated TSP solvers, such as Concorde [35], etc. However, the optimization of hovering points c consists of an infinite number of variables, which is infeasible to be solved optimally. To reduce computational time, we leverage the sampling approach that samples finite discrete sets of hovering points from a continuous state space to transform the continuous TSPN in $\mathcal { P } _ { 1 }$ into the GTSP. Specifically, each disk $O _ { m }$ is equally partitioned into $L _ { \mathrm { s u b } } \times L _ { \mathrm { s u b } }$ sub-regions and the center of each sub-region is selected as the possible hovering point. For some marginal sub-regions with non-square shape, we choose the centers of their actual areas. Hence, we can obtain a cluster $G _ { m }$ of sampling points with the size of $L _ { \mathrm { s u b } } ^ { 2 }$ from $O _ { m }$ . As a result, our objective is changed to jointly select hovering points from M clusters of sampled hovering points and plan the UAV’s trajectory to visit selected hovering points exactly once to minimize the total AoI. Using the sampling approach, the formulated problem $\mathcal { P } _ { 1 }$ is converted to

$$
\mathcal { P } _ { 2 } : \operatorname* { m i n } _ { c , \pi } \ : \ : \overline { { { A } } } \left( c , \pi \right) ,\tag{19a}
$$

$$
\mathrm { s . t . } \quad c _ { m } \in G _ { m } , G _ { m } \in O _ { m } , m \in \{ 1 , \ldots , M \} ,\tag{19b}
$$

$$
( 5 ) , ( 7 ) , ( 9 ) , ( 1 5 ) , ( 1 6 ) , \mathrm { a n d } ( 1 8 \mathrm { b } ) .
$$

Obviously, the formulated problem $\mathcal { P } _ { 2 }$ is a combinatorial optimization problem, and hence, NP-hard. There are two traditional methods to handle combinatorial problems: exact algorithms and heuristic algorithms. Exact algorithms can find optimal solutions, but they will become intractable when the size of problems grows. Heuristic algorithms’ complexity is polynomial and they commonly find sub-optimal solutions. In contrast, we cast the proposed GTSP as a sequenceto-sequence problem where the source sequence is a set of clusters of hovering points and CHs and the target sequence is a set of selected hovering points and the visiting order to these points. We adopt the transformer, the weighted $\mathbf { A } ^ { * }$ , and reinforcement learning to efficiently solve this problem.

## III. TRANSFORMER-WEIGHTED A\* ALGORITHM

Because the UAV needs to sequentially collect data from each ground cluster in the IoT network, we view the problem of the total AoI-minimal trajectory planning as a “machine translation” problem that is common in natural language processing. The whole UAV-IoT network as the “source language” is translated into the “target language”, i.e., the UAV trajectory, by using our proposed TWA\* algorithm. The TWA\* algorithm is composed of an encoder network, a decoder network, and the weighted $\mathbf { A } ^ { * }$ search algorithm which can effectively find the trajectory policy from hidden patterns behind a large number of training datasets.

## A. Encoder

The role of the encoder network is to take the UAV-IoT network represented as an input sequence and map it into an abstract representation that is the learned information. The input sequence includes the start point of the UAV, each and every CH, number of nodes in each ground cluster, and all sampling points from each hovering disk. Specifically, we define $\bar { h _ { 0 } ^ { ( \mathrm { i n } ) } } = c _ { 0 } \in \mathbb { R } ^ { 3 }$ , and $h _ { m } ^ { \mathrm { ( i n ) } } = ( G _ { m } , b _ { m } , N _ { m } ) \in$ $\mathbb { R } ^ { 3 ( L _ { \mathrm { s u b } } ^ { 2 } + 1 ) + 1 } , m \ \in \ \{ 1 , \dots , M \}$ , where the cluster $G _ { m }$ of sampling points is represented as a $3 L _ { \mathrm { s u b } } ^ { 2 }$ -dimensional vector as it includes $L _ { \mathrm { s u b } } ^ { 2 }$ points with 3D Cartesian coordinates, the CH $b _ { m }$ is a 3-dimensional vector, and the number of nodes $N _ { m }$ is a constant. Hence, the input can be expressed as $\pmb { H } ^ { \mathrm { ( i n ) } } = \left( \pmb { h } _ { 0 } ^ { \mathrm { ( i n ) } } ; \pmb { h } _ { 1 } ^ { \mathrm { ( i n ) } } ; \ldots ; \pmb { h } _ { M } ^ { \mathrm { ( i n ) } } \right)$ . The encoder network used in this paper is the standard transformer encoder with one embedding layer and six identical encoder layers as in [27]. Each encoder layer is composed of one multi-head self attention sub-layer and one point-wise feed-forward network sub-layer. Each sub-layer adds a residual connection and layer normalization. The embedding layer is to map each element of input to the $d _ { \mathrm { e m } } .$ -dimensional vector space by a learnable linear projection. Specifically, to enable the model to distinguish the start point of the UAV from clusters, we separately utilize different parameters to compute the embeddings of the start point and the other clusters as follows

$$
\pmb { h } _ { m } ^ { ( 0 ) } = \left\{ \begin{array} { l l } { W _ { 0 } \pmb { h } _ { m } ^ { \mathrm { ( i n ) } } + W _ { b _ { 0 } } , ~ m = 0 } \\ { W _ { 1 } \pmb { h } _ { m } ^ { \mathrm { ( i n ) } } + W _ { b } , ~ m = 1 , \ldots , M } \end{array} \right.\tag{20}
$$

where $W _ { 0 } ~ \in ~ \mathbb { R } ^ { d _ { \mathrm { e m } } \times 3 }$ $W _ { 1 } ~ \in ~ \mathbb { R } ^ { d _ { \mathrm { c m } } \times ( 3 ( L _ { \mathrm { s u b } } ^ { 2 } + 1 ) + 1 ) }$ $W _ { b _ { 0 } } \in$ <sup>Rd</sup>em , and $W _ { b } ~ \in ~ \mathbb { R } ^ { d _ { \mathrm { e m } } }$ are learnable parameters. Then, the embeddings ${ \pmb { H } } ^ { ( 0 ) } = \left( { \pmb h } _ { 0 } ^ { ( 0 ) } ; { \pmb h } _ { 1 } ^ { ( 0 ) } ; \ldots ; { \pmb h } _ { M } ^ { ( 0 ) } \right) \in \mathbb { R } ^ { ( M + 1 ) \times d _ { \mathrm { e m } } }$ are fed into the encoder layers. Note that we do not consider the positional decoding used in the original transformer in [23] because the order of the input sequence is irrelevant to the GTSP.

The attention layer in each encoder layer uses the multihead self-attention mechanism with 8 heads to jointly attend to information from different representation subspaces at different positions. The 8 heads perform the attention calculation in parallel and their results are merged to produce an input for the next step. In the encoder layer $l , l = 1 , \ldots , 6$ , the output of self-attention on the h-th head, $h = 1 , \ldots , 8 .$ , is computed as

$$
\begin{array} { r l } & { Z _ { h } ^ { ( l ) } = \mathrm { A t t e n t i o n } ( Q _ { h } ^ { ( l ) } , { K } _ { h } ^ { ( l ) } , { V } _ { h } ^ { ( l ) } ) } \\ & { ~ = \mathrm { s o f t m a x } \left( \frac { Q _ { h } ^ { ( l ) } { K } _ { h } ^ { ( l ) } } { \sqrt { d _ { \mathrm { v } } } } \right) { V } _ { h } ^ { ( l ) } } \end{array}\tag{21}
$$

where $d _ { \mathrm { v } }$ is used for scaling the dot products, $Q _ { h } ^ { ( l ) } ~ \in ~$ $\mathbb { R } ^ { ( M + 1 ) \times d _ { \mathrm { v } } } , K _ { h } ^ { ( l ) } \in \mathbb { R } ^ { ( M + 1 ) \times \breve { d } _ { \mathrm { v } } }$ , and $\bar { V _ { h } ^ { ( l ) } } \in \mathbb { R } ^ { ( M + 1 ) \times \bar { d } _ { \mathrm { v } } }$ are matrices query, key, and value for the h-th head, respectively. They can be created by projecting the input query $Q ^ { ( l ) }$ key $\mathbf { \delta } _ { K } ( l )$ , and value $V ^ { ( l ) }$ of multi-head self attention with three learnable weight matrices $W _ { h } ^ { Q ( l ) } \in \mathbb { R } ^ { d _ { \mathrm { e m } } \times d _ { \mathrm { v } } } , W _ { h } ^ { K ( l ) } \in$ $\mathbb { R } ^ { d _ { \mathrm { { c m } } } \times d _ { \mathrm { { v } } } }$ , and $W _ { h } ^ { V ( \tilde { l } ) } \in \mathbb { R } ^ { d _ { \mathrm { e m } } \times d _ { \mathrm { v } } }$ , respectively, as follows

$$
\begin{array} { r } { \pmb { Q } _ { h } ^ { ( l ) } = \pmb { Q } ^ { ( l ) } \pmb { W } _ { h } ^ { \pmb { Q } ( l ) } , \pmb { K } _ { h } ^ { ( l ) } = \pmb { K } ^ { ( l ) } \pmb { W } _ { h } ^ { K ( l ) } , \pmb { V } _ { h } ^ { ( l ) } = \pmb { V } ^ { ( l ) } \pmb { W } _ { h } ^ { V ( l ) } } \end{array}\tag{22}
$$

where $\pmb { Q } ^ { ( l ) } = \pmb { K } ^ { ( l ) } = \pmb { V } ^ { ( l ) } = \pmb { H } ^ { ( l - 1 ) }$ . In this paper $\pmb { H } ^ { ( l - 1 ) }$ is the output of the encoder layer $( l - 1 )$ or the output of the embedding layer before the encoder layer 1. Matrices $Q _ { h } ^ { ( l ) }$ $\pmb { K } _ { h } ^ { ( l ) }$ , and $\dot { V } _ { h } ^ { ( \bar { l } ) }$ can be further expressed as

$$
\pmb { Q } _ { h } ^ { ( l ) } = \left( \begin{array} { c } { { \pmb q _ { 0 } } } \\ { { \vdots } } \\ { { \pmb q _ { M } } } \end{array} \right) , \pmb { K } _ { h } ^ { ( l ) } = \left( \begin{array} { c } { { \pmb k _ { 0 } } } \\ { { \vdots } } \\ { { \pmb k _ { M } } } \end{array} \right) , \pmb { V } _ { h } ^ { ( l ) } = \left( \begin{array} { c } { { \pmb v _ { 0 } } } \\ { { \vdots } } \\ { { \pmb v _ { M } } } \end{array} \right)\tag{23}
$$

where $\forall q , k , v \in \mathbb { R } ^ { d _ { v } }$ . Then, we can obtain the scaled attention scores

$$
\begin{array} { r l r } { \frac { Q _ { h } ^ { ( l ) } \left( { \pmb K } _ { h } ^ { ( l ) } \right) ^ { T } } { \sqrt { d _ { \mathrm { v } } } } = \frac { 1 } { \sqrt { d _ { \mathrm { v } } } } \left( \begin{array} { c c c } { ( q _ { 0 } , k _ { 0 } ) } & { \dots } & { ( q _ { 0 } , k _ { M } ) } \\ { ( q _ { 1 } , k _ { 0 } ) } & { \dots } & { ( q _ { 1 } , k _ { M } ) } \\ { \dots } & { ( q _ { i } , k _ { j } ) } & { \dots } \\ { ( q _ { M } , k _ { 0 } ) } & { \dots } & { ( q _ { M } , k _ { M } ) } \end{array} \right) } & \\ { = \left( \begin{array} { c c c } { u _ { 0 0 } } & { \dots } & { u _ { 0 M } } \\ { u _ { 1 0 } } & { \dots } & { u _ { 1 M } } \\ { \dots } & { u _ { i j } } & { \dots } \\ { u _ { M 0 } } & { \dots } & { u _ { M M } } \end{array} \right) } & { ( 2 4 ) } \end{array}
$$

where $( \pmb { q } _ { i } , \pmb { k } _ { j } ) , i , j \in \{ 0 , \ldots , M \}$ is the inner product of vectors, which measures the similarity of vector q<sub>i</sub> and vector $k _ { j }$ . The row-wise softmax function is used on each element of the above scaled attention scores matrix, which is given by $\overline { { u } } _ { i j } = e ^ { u _ { i j } } / \sum _ { j ^ { \prime } = 0 } ^ { M } e ^ { u _ { i j ^ { \prime } } }$ . Then, the output $Z _ { h } ^ { ( l ) } \in \mathbb { R } ^ { ( \breve { M } + 1 ) \times \breve { d } \mathrm { v } }$ of the h-th head is expressed as

$$
\begin{array} { r } { Z _ { h } ^ { ( l ) } = \left( \begin{array} { c } { \sum _ { j = 0 } ^ { M } \overline { { u } } _ { 0 j } v _ { j } } \\ { \sum _ { j = 0 } ^ { M } \overline { { u } } _ { 1 j } v _ { j } } \\ { \vdots } \\ { \sum _ { j = 0 } ^ { M } \overline { { u } } _ { M j } v _ { j } } \end{array} \right) = \left( \begin{array} { c } { \overline { { \overline { { u } } } } _ { 0 } } \\ { \overline { { \overline { { u } } } } _ { 1 } } \\ { \vdots } \\ { \overline { { \overline { { u } } } } _ { M } } \end{array} \right) . } \end{array}\tag{25}
$$

Hence, we end up with 8 different outputs from 8 heads where each head could learn something different. These outputs are concatenated and multiplied by an additional learnable weight matrix $W _ { \mathrm { o } } ^ { ( l ) } \in \mathbb { R } ^ { 8 d _ { \mathrm { v } } \times \dot { d } _ { \mathrm { c m } } }$ to generate the final output of the multi-head attention layer, as follows

$$
\begin{array} { r } { \pmb { Z } ^ { ( l ) } = \left( \pmb { Z } _ { 1 } ^ { ( l ) } , \ldots , \pmb { Z } _ { 8 } ^ { ( l ) } \right) \pmb { W } _ { \mathrm { o } } ^ { ( l ) } , \pmb { Z } ^ { ( l ) } \in \mathbb { R } ^ { ( M + 1 ) \times d _ { \mathrm { e m } } } . } \end{array}\tag{26}
$$

To facilitate the understanding of multi-head attention layer, all operations from (21) to (26) are defined as a function $\mathrm { \mathbf { M H A } } ( \cdot )$ . Thus, $\begin{array} { r } { \pmb { Z } ^ { ( l ) } = \mathrm { M H A } \left( \pmb { Q } ^ { ( l ) } , \pmb { K } ^ { ( l ) } , \pmb { V } ^ { ( l ) } \right) } \end{array}$ . Then, $Z ^ { ( l ) }$ is added to the input of the multi-head attention in this encoder, which is a residual connection operation. Subsequently, the output of the residual connection is fed into a batch normalization, defined as a function $\mathrm { B N } ( \cdot )$ , and it is written as $Z ^ { ' ( l ) } =$ BN $\left( \pmb { H } ^ { ( l - 1 ) } + \pmb { Z } ^ { ( l ) } \right)$ <sup>) =</sup>. The use of the residual connection is to avoid the degradation problem of the network in training, while the layer normalization can improve the training speed and the stability of the networks. The normalized residual output goes through a pointwise feed-forward network (defined as a function $\mathrm { F F N } ( \cdot ) )$ , which is a couple of linear layers with a ReLU activation in between. Then, the output of the pointwise feed-forward network is added to its input by a residual connection and further normalized to obtain the final output $\pmb { H } ^ { ( l ) } \in \mathbb { R } ^ { ( M + 1 ) \times d _ { \mathrm { e m } } }$ of the encoder layer l, which is given by $\begin{array} { r } { \pmb { H } ^ { ( l ) } = \mathrm { B N } \left( \pmb { Z } ^ { \prime ( l ) } + \mathrm { F F N } \left( \pmb { Z } ^ { \prime ( l ) } \right) \right) } \end{array}$ . In each encoder layer, we perform the same computational process and finally output the final result of the encoder part at layer 6, $H ^ { ( 6 ) } =$ $\left( \dot { h } _ { 0 } ^ { ( 6 ) } ; h _ { 1 } ^ { ( 6 ) } ; \ldots ; h _ { M } ^ { ( 6 ) } \right) \in \mathbb { R } ^ { ( M + 1 ) \times d _ { \mathrm { e m } } }$ , which is the continuous representation with attention information of the input $\pmb { H } ^ { \mathrm { ( i n ) } }$ All of these operations will help the decoder network focus on the appropriate elements in the input during the decoding process.

## B. Decoder

The decoding is autoregressive and generates the result one by one. The output of the decoder network can be represented as an ordered sequence of the input of the encoder. The decoder begins with the start point at decoding step 0 since the trajectory of the UAV should start at the start point as well as end at this point. The output of each decoding step is based on the information from the encoder and the already-generated previous output in the decoder. Hence, the decoding process can be modelled using the probability chain rule

$$
P ( \pi | { \cal H } ^ { \mathrm { ( i n ) } } ) = \prod _ { t = 0 } ^ { M + 1 } P ( \pi ( t ) | \pi ( 0 ) , \ldots , \pi ( t - 1 ) , { \cal H } ^ { \mathrm { ( i n ) } } ) .\tag{27}
$$

The decoding process aims at finding the optimal π to maximize $P ( \pi | \mathbf { H } ^ { \mathrm { ( i n ) } } )$ .

The decoder network is composed of two identical decoder layers, and a single-head attention layer. Each decoder layer contains two multi-head attention sub-layers which employ a residual connection around them followed by layer normalization. These sub-layers have the same structure as the sub-layers in the encoder network but each of them has a different job. Since the output of the decoder network is related to the order, we need to inject some information about the positions into the input sequence of the decoder network. The locations are implicitly represented by the order of the data input to the decoder network. Hence, the input of the decoder network is the output of the encoder network combined with the positional encoding. Suppose the outputs of the decoder network at previous t decoding steps are $\pi ( 0 ) , \pi ( 1 ) , \ldots , \pi ( t )$ , the decoder wants to predict the output at $t + 1$ step. Then, the input to the decoder network is expressed as $\widehat { \pmb { H } } _ { t + 1 } ^ { ( 0 ) } = \left( \widehat { \pmb { h } } _ { \pi ( 0 ) } ^ { ( 0 ) } ; \widehat { \pmb { h } } _ { \pi ( 1 ) } ^ { ( \bar { 0 } ) } ; \ldots ; \widehat { \pmb { h } } _ { \pi ( t ) } ^ { ( 0 ) } \right)$ . Each element in $\widehat { \pmb { H } } _ { t + 1 } ^ { ( 0 ) }$ can be calculated by $\widehat { \pmb { h } } _ { \pi ( t ) } ^ { ( 0 ) } = { \pmb h } _ { \pi ( t ) } ^ { ( 6 ) } + \mathtt { P E } _ { t }$ , where $h _ { \pi ( t ) } ^ { ( 6 ) } ~ \in$ $\mathbb { R } ^ { 1 \times d _ { \mathrm { { c m } } } }$ is one element in $\dot { \pmb { H } } ^ { ( 6 ) }$ which is decoded at the t-th step, $\mathrm { P E } _ { t } \in \mathbb { R } ^ { 1 \times d _ { \mathrm { e m } } }$ is the positional encoding based on the sinusoidal function, which is given by [36]

$$
\begin{array} { r } { \mathrm { P E } _ { t } ( d _ { i } ) = \left\{ \begin{array} { l l } { \sin { ( \omega _ { d _ { i } } t ) } , } & { \mathrm { i f ~ } d _ { i } \mathrm { ~ i s ~ e v e n } } \\ { \cos { ( \omega _ { d _ { i } } t ) } , } & { \mathrm { i f ~ } d _ { i } \mathrm { ~ i s ~ o d d } } \end{array} \right. } \end{array}\tag{28}
$$

where $d _ { i }$ is the dimension, $1 ~ \leqslant ~ d _ { i } ~ \leqslant ~ d _ { \mathrm { { e m } } } , ~ \omega _ { d _ { i } }$ is the hand-crafted frequency for each dimension. The position encoding of each position successfully provides the position information to the decoder network. The input $\widehat { \pmb { H } } _ { t + 1 } ^ { ( 0 ) }$ gets fed into the first multi-head attention sub-layer of the first decoder layer and pass through the residual connection and layer normalization (denoted as a function LN(·)) to prepare the query for the next multi-head attention sub-layer, as follows

$$
\widehat { \pmb { Z } } _ { t + 1 } ^ { ( 1 ) } = \mathrm { M H A } \left( \widehat { \pmb { h } } _ { \pi ( t ) } ^ { ( 0 ) } , \widehat { \pmb { H } } _ { t + 1 } ^ { ( 0 ) } , \widehat { \pmb { H } } _ { t + 1 } ^ { ( 0 ) } \right) , \widehat { \pmb { Z } } _ { t + 1 } ^ { ( 1 ) } \in \mathbb { R } ^ { 1 \times d _ { \mathrm { e m } } }\tag{29}
$$

$$
\widehat { \pmb { Z } } _ { t + 1 } ^ { \prime ( 1 ) } = \mathrm { L N } \left( \widehat { \pmb { h } } _ { \pi ( t ) } ^ { ( 0 ) } + \widehat { \pmb { Z } } _ { t + 1 } ^ { ( 1 ) } \right) , \widehat { \pmb { Z } } _ { t + 1 } ^ { \prime ( 1 ) } \in \mathbb { R } ^ { 1 \times d _ { \mathrm { e m } } }\tag{30}
$$

where $\widehat { h } _ { \pi ( t ) } ^ { ( 0 ) }$ is the query, $\widehat { \pmb { H } } _ { t + 1 } ^ { ( 0 ) }$ works as the key and the value matrices in the current multi-head attention sub-layer. The second multi-head attention sub-layer is used to match the encoder’s input to the decoder’s input to allow the decoder network to decide the next possible output among the nonvisited elements. For this sub-layer, the encoder network’s output $H ^ { ( 6 ) }$ is the key and the value matrices, and ${ \widehat { \pmb { Z } } } ^ { \prime } ( 1 )$ is the query matrix. The calculations are given by

$$
\widehat { \pmb { Z } } _ { t + 1 } ^ { \prime \prime ( 1 ) } = \mathrm { M H A } \left( \widehat { \pmb { Z } } _ { t + 1 } ^ { \prime ( 1 ) } , \pmb { H } ^ { ( 6 ) } , \pmb { H } ^ { ( 6 ) } \right) , \widehat { \pmb { Z } } _ { t + 1 } ^ { \prime \prime ( 1 ) } \in \mathbb { R } ^ { 1 \times d _ { \mathrm { e m } } }\tag{31}
$$

$$
\widehat { \pmb { H } } _ { t + 1 } ^ { ( 1 ) } = \mathrm { L N } \left( \widehat { \pmb { Z } } _ { t + 1 } ^ { \prime ( 1 ) } + \widehat { \pmb { Z } } _ { t + 1 } ^ { \prime \prime ( 1 ) } \right) , \widehat { \pmb { H } } _ { t + 1 } ^ { ( 1 ) } \in \mathbb { R } ^ { 1 \times d _ { \mathrm { e m } } } .\tag{32}
$$

Note that we add the mask of visited elements to the scaled attention scores in this sub-layer. Then, $\widehat { \pmb { H } } _ { t + 1 } ^ { ( 1 ) }$ goes through the second decoder layer to get the output $\widehat { \pmb { H } } _ { t + 1 } ^ { ( 2 ) } \in \mathbb { R } ^ { 1 \times d _ { \mathrm { e m } } }$ In order for the decoder network to compute output probabilities $P ( \pi ( t + 1 ) | \pi ( 0 ) , \ldots , \pi ( t ) , \pmb { H } ^ { ( 6 ) } ) , \overbrace { \pmb { H } _ { t + 1 } ^ { ( 2 ) } }$ and the output $H ^ { ( 6 ) }$ of the encoder network get fed into a single-head attention to get a distribution over the non-visited elements,

which is given by [27]

$$
P _ { t + 1 } = \mathrm { s o f t m a x } \left( \operatorname { t a n h } \left( \frac { \widehat { Q } _ { t + 1 } \widehat { K } _ { t + 1 } ^ { T } } { \sqrt { d _ { \mathrm { e m } } } } \odot \mathcal { M } _ { t + 1 } \right) \right)\tag{33}
$$

where $\widehat { Q } _ { t + 1 } = \widehat { H } _ { t + 1 } ^ { ( 2 ) } \widehat { W } _ { 1 } , \widehat { K } _ { t + 1 } = H ^ { ( 6 ) } \widehat { W } _ { 2 } , \widehat { W } _ { 1 } \in \mathbb { R } ^ { d _ { \mathrm { e m } } \times d _ { \mathrm { e m } } }$ and $\widehat { \pmb { W } } _ { 2 } \ \in \ \mathbb { R } ^ { d _ { \mathrm { e m } } \times d _ { \mathrm { e m } } }$ are learnable weight matrices, $\mathcal { M } _ { t + 1 }$ is the mask of the visited elements considered in this layer, $\odot$ is the Hadamard product, and $P _ { t + 1 } \in \mathbb { R } ^ { 1 \times ( M + 1 ) }$ is the distribution over the non-visited elements, which is composed of probability scores. Then, the output that will be selected is sampled from the distribution with three decoding methods:

1) Greedy: At each decoding step, this method greedily selects the element with the largest probability $P ( \pi ( t ~ +$ $1 ) | \pi ( 0 ) , \ldots , \pi ( t ) , H ^ { ( 6 ) } \rangle$ .

2) Random Sampling: This method randomly samples $W _ { \mathrm { s a m p l i n g } }$ solutions, where each solution includes fully visiting order, and selects the solution with the highest probability as the final result.

3) Beam Search: This method chooses the top $W _ { \mathrm { { b e a m } } }$ possible solutions that have the highest probability at each step, where $W _ { \mathrm { { b e a m } } }$ is the beam width. Those $W _ { \mathrm { { b e a m } } }$ solutions will move to the next time step, and the process repeats. Then, we can obtain a tree of solutions of each step and the $\pi$ that has the highest overall probability is picked as the final result.

We assume that the index of the highest probability score in $P _ { t + 1 }$ is selected with the greedy decoding as the output $\pi ( t + 1 )$ at step $t + 1$ . Thus $\pi ( t + 1 )$ points to the element at the same position of the input sequence $\pmb { H } ^ { \mathrm { ( i n ) } }$ of the encoder network, which is represented as $h _ { \pi ( t + 1 ) } ^ { \mathrm { ( i t ) } }$ . Then, the decoder network takes the encoding information of $h _ { \pi ( t + 1 ) } ^ { \mathrm { ( i t ) } }$ from ${ \cal H } ^ { ( 6 ) } , \mathrm { i . e . , } h _ { \pi ( t + 1 ) } ^ { ( 6 ) }$ , and adds it with its position encoding to the list of the decoder input to continue decoding for the next step. Finally, we can obtain a set of the visiting order, π. As shown in the example in Fig. 3, $\begin{array} { r l } { \pmb { H } ^ { \mathrm { ( i n ) } } } & { { } = } \end{array}$ $\left( c _ { 0 } ; \left( G _ { 1 } , b _ { 1 } , N _ { 1 } \right) ; \left( G _ { 2 } , b _ { 2 } , N _ { 2 } \right) ; \left( G _ { 3 } , b _ { 3 } , N _ { 3 } \right) ; \left( G _ { 4 } , b _ { 4 } , N _ { 4 } \right) \right)$ <sup>=</sup>is the input to the encoder network and the decoder network outputs the final visiting order $\pi = \{ \pi ( 0 ) , \pi ( 1 ) , \pi ( 2 ) , \pi ( 3 ) , \pi ( 4 ) \}$ to elements in $\pmb { H } ^ { \mathrm { ( i n ) } }$

## C. Selection of Hovering Points

Given the visiting order π, we know the visiting order to all hovering points clusters and construct a graph containing all of them, as illustrated in Fig. 3. Each layer of the graph is composed of one hovering points cluster. Then, we will calculate the path with the minimal total AoI starting from the start point (marked as $\pi ( 0 )$ in the visiting order), going through each cluster $G _ { m } .$ , and ending at the clone of the start point (marked as $\pi ( M + 1 )$ in the visiting order). To guarantee that at most one hovering point is selected from each cluster, we assume that all edges between possible hovering points of consecutive clusters to be directed by π. We use the weighted $\mathbf { A } ^ { * }$ search algorithm [37] to quickly find the hovering point from each cluster to build the path with the minimal cost (total AoI). We assume that the UAV currently reaches the point $s ^ { \prime }$ and will decide the next point to be expanded by the following

![](images/944c754b128d8232b41e8d823026d036984d2602c4b28da19f453c0ceea5d763.jpg)  
Fig. 3. The proposed algorithm framework.

![](images/9350e3464a1bab8e2a719ceacc0eff9630ecee04b2f3a69b7504b9c929e9dabf.jpg)  
Fig. 4. Multi-head self attention.

cost function

$$
f ( s ) = g ( s ) + \omega h ( s )\tag{34}
$$

where s is any neighbor point of $s ^ { \prime } , g ( s )$ is the total movement <sup>( )</sup>cost on the path from the start point $c _ { 0 }$ to $s , \ h ( s )$ is the <sup>( )</sup>heuristic function to estimate cost from s to the end point ${ c _ { 0 } } ^ { \prime } .$ , and $\omega ~ > ~ 1$ is a constant factor. The neighbor point with a minimal $f ( s )$ value is expanded. The pseudocode is described in Algorithm 1. We use COST and FRONTIER to keep track of $g ( s )$ and the expanding process, respectively. Each point that has been reached keeps a pointer to its parent in

CAME\_FROM so that we can know where it came from. With CAME\_FROM, we can construct a path having the minimal AoI from the start point to the end point, as illustrated by the solid red line with arrow in the example in Fig. 3.

## D. Computational Complexity Analysis

In the encoder network, each encoder layer is the standard transformer encoder with quadratic computational complexity $O ( ( M + 1 ) ^ { 2 } d _ { \mathrm { { e m } } } )$ [23]. Since the number of layers is constant, the computational complexity of the encoder network is still $O ( ( M + 1 ) ^ { 2 } d _ { \mathrm { { e m } } } )$ . In the decoder network, although each decoder layer contains two multi-head attention sub-layers, its computational complexity is still estimated to be quadratic $O ( ( M + 1 ) ^ { 2 } d _ { \mathrm { { e m } } } )$ [23]. Likewise, the number of decoder layers does not affect the computational complexity of the decoder network. In addition, the computational complexity of the single-head attention used in the final step of the decoder network is also quadratic $O ( ( M + 1 ) ^ { 2 } \bar { d _ { \mathrm { e m } } } )$ [23]. Hence, the employed transformer model has the computational complexity $O ( ( M + 1 ) ^ { 2 } d _ { \mathrm { { e m } } } )$ , which is quadratic in the length of the input sequence. Different data structures used to implement the weighted $\mathbf { A } ^ { * }$ algorithm, and hence, affect its computational complexity. We use the min heap to implement the weighted $\mathbf { A } ^ { * }$ algorithm. We assume that at most $M L _ { \mathrm { s u b } } ^ { 2 }$ points (the total number of points in the search graph) are visited, and the min heap uses $O ( \log ( M L _ { \mathrm { s u b } } ^ { 2 } ) )$ computational complexity to extract a point each time [38]. The weighted $\mathbf { A } ^ { * }$ algorithm’s computational complexity is estimated to be $O ( \bar { M } L _ { \mathrm { s u b } } ^ { 2 } \log ( M L _ { \mathrm { s u b } } ^ { \bar { 2 } } )$ . Hence, the computational complexity of the proposed algorithm is $O ( ( M \pm )$ $1 ) ^ { 2 } d _ { \mathrm { e m } } ) + \bar { O ( M L _ { \mathrm { s u b } } ^ { 2 } \log ( M L _ { \mathrm { s u b } } ^ { 2 } ) }$

Algorithm 1: Pseudocode for Weighted $\mathbf { A } ^ { * }$ Search Algo  
rithm to Find Hovering Points   
Input: created graph   
1: FRONTIER = PriorityQueue()   
2: FRONTIER.put(c<sub>0</sub>, 0)   
3: $\mathbf { C A M E \_ F R O M } = \left[ \mathbf { \Phi } \right]$   
4: $\mathrm { { C O S T } = [ ] }$   
<sup>[ ]</sup>5: CAME\_FROM c<sub>0</sub> = None   
6: $\mathrm { C O S T } [ c _ { 0 } ] = 0$   
<sup>[ ]</sup>7: while FRONTIER is not empty do   
8: current point $s ^ { \prime } = \mathrm { F R O N T I E R }$ .get()   
9: if $s ^ { \prime } = { c _ { 0 } } ^ { \prime }$ then   
10: <sup>=</sup>break   
11: end if   
12: for each neighbor s of $s ^ { \prime }$ do   
13: $g ( s ) = \mathrm { C O S T } [ s ^ { \prime } ] +$ the total AoI from $s ^ { \prime }$ to s   
14: <sup>( ) = [ ]+</sup>if s not in COST or $g ( s ) < \mathrm { C O S T } [ s ]$ then   
15: $\mathrm { C O S T } [ s ] = \mathrm { g } ( \mathrm { s } )$   
16: $f ( s ) = g ( s ) + \omega h ( s )$   
17: <sup>( ) = ( ) +</sup>FRONTIER.put(s, $f ( s ) )$   
18: $\mathrm { C A M E \_ F R O M } [ s ] = s ^ { \prime }$   
19: end if   
20: end for   
21: end while   
22: calculate $\overline { { A } }$ according to CAME\_FROM

## E. Training

To enable the transformer model to produce the optimal π, we use the well-known policy gradient approaches to train it. The transformer model is parameterized by ϑ, which includes all trainable variables in the encoder and the decoder networks. We regard the UAV as an agent to learn a good policy π to maximize long-term rewards by iteratively interacting with the environment to optimize parameter ϑ. At each step, the agent in a given state chooses an action by its decision policy, which actually is the mapping from states to actions.

1) State: The state consists of the environment encoded by the encoder network and the visited clusters before the current step in the decoder, which are $H ^ { ( 6 ) }$ and $\widehat { \pmb { H } } _ { t + 1 } ^ { ( 0 ) }$ in the transformer, respectively.

2) Action: At each step, the agent makes an action $\pi ( t )$ based on its state, which can be seen as the processes of the right-hand side of (27). Thus, we view all operations in the decoder network as the action.

3) Reward: The negative of the total AoI $\overline { { A } }$ in (17) is used as the reward.

Our objective for training is given by

$$
J \left( \vartheta | { \cal H } ^ { \mathrm { ( i n ) } } \right) = \mathbb { E } _ { \pi \sim P _ { \vartheta } \left( \cdot | { \cal H } ^ { \mathrm { ( i n ) } } \right) } \left( \overline { { \cal A } } \right) .\tag{35}
$$

The gradient of (35) is calculated using the REINFORCE algorithm [39] with the greedy rollout baseline $\overline { { A } } ^ { ( \mathrm { B L } ) }$ [25]

$$
\begin{array} { r l } & { \nabla _ { \vartheta } J \left( \vartheta \vert \boldsymbol { H } ^ { \mathrm { ( i n ) } } \right) } \\ & { ~ = \mathbb { E } _ { \pi \sim P _ { \vartheta } \left( \cdot \vert \boldsymbol { H } ^ { \mathrm { ( i n ) } } \right) } \left[ \left( \overline { { \boldsymbol { A } } } - \overline { { \boldsymbol { A } } } ^ { \mathrm { ( B L ) } } \right) \nabla _ { \vartheta } \log P _ { \vartheta } \left( \pi \vert \boldsymbol { H } ^ { \mathrm { ( i n ) } } \right) \right] } \end{array}\tag{36}
$$

Algorithm 2: Training $\overline { { \mathrm { \ T W A } ^ { * } } }$ by REINFORCE With   
Rollout Baseline   
Input: Epochs $E _ { \mathrm { e p o c h s } } ,$ training steps $S ,$ batch size $\boldsymbol { B } _ { \mathrm { s i z e } }$   
1: Initialize parameters $\vartheta , \vartheta ^ { \mathrm { ( B L ) } } \dot {  } \vartheta$   
2: for epoch = 1 to $E _ { \mathrm { e p o c h s } }$ do   
3: for step = 1 to $S$ do   
4: $\pmb { H } _ { i } ^ { \mathrm { ( i n ) } }$ ← generate instances() $\forall i \in \{ 1 , \ldots , B \mathrm { { s i z e } } \}$   
5: π ← Sampling solution $P _ { \vartheta }$ $\left( \cdot | H _ { i } ^ { \mathrm { ( i n ) } } \right)$   
6: $\pi _ { i } ^ { ( \mathrm { B L } ) }$ ← Greedy solution $\dot { P _ { \vartheta ^ { ( \mathrm { B L } ) } } } \left( \cdot | \dot { \cal H } _ { i } ^ { ( \mathrm { i n } ) } \right)$   
7: $\overline { { A } } _ { i } \gets$ weighted $\mathbf { A } ^ { * } \left( \pi _ { i } \right)$   
8: A<sup>(BL)</sup> ← weighted $\overset { \cdot } { \mathbf { A } ^ { * } } \left( \pi _ { i } ^ { ( \mathrm { B L } ) } \right)$   
9: $\begin{array} { r } { \nabla _ { \vartheta } J \gets \sum _ { i = 1 } ^ { B _ { \mathrm { s i z e } } } \left( \overline { { A } } _ { i } - \overline { { A } } _ { i } ^ { ( \mathrm { B L } ) } \right) ^ { \prime } \nabla _ { \vartheta } } \end{array}$ log $P _ { \vartheta } \left( \pi _ { i } | H _ { i } ^ { \mathrm { ( i n ) } } \right)$   
10: $\vartheta \gets \mathrm { A }$ dam $( \vartheta , \dot { \nabla } _ { \vartheta } J )$   
11: end for   
12: if $t \mathrm { - t e s t } ( P _ { \vartheta } ( \cdot ) , P _ { \vartheta ^ { ( \mathrm { B L } ) } } ( \cdot ) ) < 5 \%$ then   
13: $\vartheta ^ { ( \mathrm { B L } ) }  \dot { \vartheta }$   
14: end if   
15: end for

where $\overline { { A } }$ is the cost of a solution that is obtained from the current training transformer model by sampling decoding. We set the greedy policy as the baseline policy in our model, and hence, $\overline { { A } } ^ { ( \mathrm { B L } ) }$ is the cost of a solution of the deterministic greedy decoding, which is used to eliminate variance during training. By doing so, the transformer model is trained to improve over its (greedy) self. The training process is summarized in Algorithm 2. In each training step, new instances are generated first (line 4). Then, the transformer model uses sampling decoding and greedy decoding to produce $\pi _ { i }$ and $\pi _ { i } ^ { \mathrm { ( B L ) } }$ (lines 5 and 6), respectively. The total AoIs are further obtained from the weighted $\mathbf { A } ^ { * }$ (lines 7 and 8). The gradient in (36) is approximated with Monte Carlo sampling in a batch size $\boldsymbol { B } _ { \mathrm { s i z e } }$ (line 9). The model parameter ϑ is updated using the Adam optimizer (line 10). We compare the current policy with the greedy baseline policy and update the parameter $\dot { \boldsymbol { \vartheta } } ^ { ( \mathrm { B L } ) }$ only if the improvement is significant according to a paired t-test [25].

As pointed out earlier, Ptr-A\* proposed in our previous work [5] can also be used to solve the formulated GTSP in this work. Here, we give comparisons between TWA\* and Ptr-$\mathbf { A } ^ { * }$ in detail. First, they have different structures. In Ptr-A\*, the encoder network consists of the LSTM networks, and the decoder network is composed of the LSTM networks and the attention mechanism. The LSTM networks have the form of a chain of repeating modules of a neural network. The key to the LSTM networks is the cell state, which is the hidden state. In theory, the hidden state can carry relevant information throughout the processing of the sequence. Since the LSTM networks process the elements of the input sequence one by one, the hidden state of each element of the input sequence is calculated by the current element and the previous hidden state. The final hidden state of the encoder network is fed into the LSTM networks of the decoder network. Then, the attention mechanism uses the hidden state of the decoder network to generate the output sequence. In TWA\*, the encoder network includes six identical encoder layers in which each encoder layer is mainly composed of one multi-head self-attention sublayer and one point-wise feed-forward network. The decoder network of $\mathrm { T W A ^ { * } }$ consists of two identical decoder layers and one single-head attention layer. The encoder network is used to map the input ${ \pmb H } ^ { ( 0 ) } = \left( \bar { h _ { 0 } ^ { ( 0 ) } } ; h _ { 1 } ^ { ( 0 ) } ; \dots ; h _ { M } ^ { ( 0 ) } \right)$ to a sequence of continuous representations. The decoder network receives the output of the encoder together with the decoder output at the previous time step to generate the output sequence. Multi-head self-attention is an attention mechanism relating different positions of a single sequence in order to compute a representation of the sequence. Multi-head self-attention helps TWA\* to look at all elements in the input sequence for clues that can help lead to a better encoding. Unlike hidden states used in Ptr-A\*, TWA\* does not rely on past hidden states to capture dependencies with previous elements in the sequence. As a result, TWA\* does not suffer from long dependency issues, which are very common in recurrent-based networks, such as RNNs and LSTMs, and hence does not lost past information.

Second, TWA\* can process sequences in parallel, which is faster than Ptr-A\*. In Ptr-A\*, the elements of a sequence must be processed one by one and each element’s hidden state is assumed to be dependent only on the previously hidden state. Hence, Ptr-A\*’s recurrent structure makes it hard to use parallel computing to process sentences and this means that it is very slow in training and inference. All elements in a sequence are processed in TWA\* as a whole rather than one by one. Because of the use of multi-head self-attention that is designed in parallel, TWA\* has the ability of parallel computation.

Third, the training method used in this work is different from the training method in [5]. In [5], in order to obtain the optimal parameter of Ptr-A\*, we use the actor-critic architecture to train Ptr-A\* where a second critic network must be trained. In this work, we use the greedy rollout baseline where the TWA\* model is trained to improve over its (greedy) self. This training method can avoid all the inherent training difficulties associated with the actor-critic architecture.

## IV. NUMERICAL RESULTS

We conduct extensive experiments to investigate the performance of the proposed TWA\* algorithm in solving the problem of trajectory planning to minimize the total AoI for the UAV-IoT network. The proposed model is implemented by Pytorch 1.7 and Python 3.8 and trained on a machine with 1 NVIDIA RTX 2080Ti GPU.

## A. Test Settings

1) Decoding Strategies: As we mentioned in Section III-D, the random sampling decoding and the greedy decoding are employed for training the model. At inference, we evaluate performance of all three decoding methods on test instances and they are marked as TWA\*–greedy, TWA\*–sampling $( W _ { \mathrm { s a m p l i n g } } = 5 1 2 0 )$ , and TWA\*–beam search $( W _ { \mathrm { b e a m } } = 1 0 0 )$

TABLE I  
SIMULATION PARAMETERS
<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>H</td><td rowspan=1 colspan=1>100 m</td><td rowspan=1 colspan=1> $\overline { { \beta } }$ </td><td rowspan=1 colspan=1>12.08</td></tr><tr><td rowspan=1 colspan=1> $\tilde { \beta }$ </td><td rowspan=1 colspan=1>0.11</td><td rowspan=1 colspan=1> $P _ { \mathrm { C H } }$ </td><td rowspan=1 colspan=1>0.1 W</td></tr><tr><td rowspan=1 colspan=1> $\underline { { \gamma _ { \mathrm { t h } } } }$ </td><td rowspan=1 colspan=1>20 dB (default)</td><td rowspan=1 colspan=1> $\xi _ { \mathrm { L o S } }$ </td><td rowspan=1 colspan=1>1 dB</td></tr><tr><td rowspan=1 colspan=1> $\xi _ { \mathrm { N L o S } }$ </td><td rowspan=1 colspan=1>20 dB</td><td rowspan=1 colspan=1> $\overline { { \sigma ^ { 2 } } }$ </td><td rowspan=1 colspan=1>-110 dBm</td></tr><tr><td rowspan=1 colspan=1> ${ \underline { { v _ { \mathrm { U A V } } } } }$ </td><td rowspan=1 colspan=1>15 m/s</td><td rowspan=1 colspan=1> $\overline { { f _ { c } } }$ </td><td rowspan=1 colspan=1>2 GHz</td></tr><tr><td rowspan=1 colspan=1> $L _ { \mathrm { d a t a } }$ </td><td rowspan=1 colspan=1>5Mb</td><td rowspan=1 colspan=1> $\underline { { B _ { \mathrm { w i d t h } } } }$ </td><td rowspan=1 colspan=1>1 MHz</td></tr><tr><td rowspan=1 colspan=1> $\overline { { P _ { \mathrm { c o m } } } }$ </td><td rowspan=1 colspan=1>0.1 W</td><td rowspan=1 colspan=1> $L _ { \mathrm { s u b } }$ </td><td rowspan=1 colspan=1>5</td></tr><tr><td rowspan=1 colspan=1> $\overline { { \boldsymbol { P } _ { 0 } } }$ </td><td rowspan=1 colspan=1>99.66 W</td><td rowspan=1 colspan=1> $\overline { { P _ { 1 } } }$ </td><td rowspan=1 colspan=1>120.16 W</td></tr><tr><td rowspan=1 colspan=1> $\underline { { U _ { \mathrm { t i p } } } }$ </td><td rowspan=1 colspan=1>120 m/s</td><td rowspan=1 colspan=1> $v _ { 0 }$ </td><td rowspan=1 colspan=1>0.002 m/s</td></tr><tr><td rowspan=1 colspan=1> $d _ { \mathrm { 0 } }$ </td><td rowspan=1 colspan=1>0.48</td><td rowspan=1 colspan=1> $\rho$ </td><td rowspan=1 colspan=1>1.225 kg/m³</td></tr><tr><td rowspan=1 colspan=1> $\tau$ </td><td rowspan=1 colspan=1>0.1 s</td><td rowspan=1 colspan=1>δ</td><td rowspan=1 colspan=1>0.5</td></tr><tr><td rowspan=1 colspan=1> $s _ { 0 }$ </td><td rowspan=1 colspan=1>0.0001</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr></table>

2) Comparison Algorithms: To evaluate the effectiveness of the proposed model with different decoding methods, we compare it with the genetic algorithm [40], the simulated annealing (SA) algorithm [41], and Ptr-A\* with the sampling strategy [5]. Common parameters are selected for the genetic algorithm: The population size is the number of all possible hovering points in one instance, the maximal iteration is 10000, crossover is 0.1, and mutation probability is 0.8. The parameters of SA for the initial temperature, cooling coefficient, and maximal iteration are taken as 100, 0.99, and 1000, respectively.

3) Data Generation: We assume there is a probability distribution over a family of problems. During training, problem instances are generated according to this distribution, and any test examples are also produced from the same distribution at inference. For any problem instances, all CHs $\left\{ b _ { 1 } , \dotsc , b _ { M } \right\}$ are randomly sampled from the distribution U torch.FloatTensor 1, 2 .uniform 0, 3000 . With the SNR threshold $\gamma _ { \mathrm { t h } }$ and environment parameters, we can calculate the hovering disk $O _ { m }$ for each CH $b _ { m } ,$ and each cluster of candidate hovering points Gn $G _ { m }$ is sampled from $O _ { m } .$ . The number of nodes $N _ { m }$ in each ground cluster is randomly chosen from $\{ 5 , 1 0 , 1 5 , 2 0 , 2 5 , 3 0 \}$ . Hence, any of the problem instances is obtained as $\begin{array} { r l } { H ^ { \mathrm { ( i n ) } } } & { { } = } \end{array}$ $( c _ { 0 } ; ( G _ { 1 } , b _ { 1 } , N _ { 1 } ) ; . . . ; ( G _ { m } , b _ { m } , N _ { m } ) ; . . . ; ( G _ { M } , b _ { M } , N _ { M } ) ) |$

<sup>; ( ) ; ; ( ) ; ; ( ))</sup>4) Environment Parameters and Hyperparameters: We consider a ground network with a size of 3 km × 3 km, and the start position of the UAV is located at  m,  m, H m . <sup>(0 0 )</sup>Environment parameters are listed in Table I. The embedding dimension $d _ { \mathrm { e m } }$ is equal to 512 and $d _ { \mathrm { v } }$ is equal to 64. We train the proposed model using the Adam optimizer with a learning rate of 0.0001 on $E _ { \mathrm { e p o c h s } } = 2 0 0$ epochs, where each epoch includes $S ~ = ~ 1 0 0 0$ training steps. At each training step, the batch size $\boldsymbol { B } _ { \mathrm { s i z e } }$ is equal to 512, which means there are 512 instances in each batch. In each instance, we set M .

## B. Analysis of the Results

We first compare the total AoI between our proposed algorithm against the genetic and SA algorithms on the trained model when the value of M varies. Although the model is trained on 10-clusters IoT networks $( M ~ = ~ 1 0 )$ , it still shows good performance on IoT networks with different sizes, like 20-clusters, 30-clusters, etc., as can be seen in Fig. 5 (a). Specifically, the TWA\*-sampling algorithm always obtains the minimal total AoI when compared with other two decoding methods, as well as the three other algorithms under comparison. The TWA\*-beam search and TWA\*-greedy algorithms exhibit an obviously superior performance than the genetic and SA algorithms in reducing the total AoI. The above observations indicate that the proposed algorithm with the three different decoding methods achieves an excellent generalization ability with respect to the size of the IoT network used for training. When M , TWA\*-sampling, TWA\*-beam search, TWA\*-greedy, Ptr-A\*, and the genetic algorithms obtain almost the same total AoI; however, the SA algorithm has a higher total AoI when compared to our proposed algorithm with all three decoding strategies. As the value of M increases, the performance gap increases gradually between our proposed algorithm and comparison algorithms. For instance, when M , the total AoI values of the TWA\*-sampling, TWA\*-beam search, TWA\*-greedy, Ptr-A\*, genetic, and SA algorithms are 13134, 13134, 13546, 13431, 15205, and 15452 seconds, respectively. Compared to Ptr-A\*, TWA\*-sampling has a performance gain of . . As M <sup>2 2%</sup>increases to 45, the total AoI values obtained by the TWA\*- sampling, TWA\*-beam search, and TWA\*-greedy algorithms are 42803, 43971, and 46118 seconds, respectively. Compared to Ptr-A\* with a AoI value of 45663 seconds, TWA\*-sampling has a performance gain of . . However, the total AoI values of the genetic and SA algorithms are 54061 and 59537 seconds, respectively, which are obviously inferior than what obtained by our proposed algorithm. In summary, our proposed algorithm using any of the three decoding methods can obtain better total AoI results than both the genetic and SA algorithms. In addition, TWA\*-sampling always obtains better AoI values than Ptr-A\* with the sampling strategy. This comparison result is consistent with the conclusions in [25] and [27] that the transformer-based technique outperforms the pointer network-based technique.

![](images/5d2031d22c21dd4f18296f519b5d021e7d89fe15582d31e2419caffbfcdc6106.jpg)  
(a) Comparison of the total AoI when M varies.

![](images/2e097a95b1db1efc1273f1a3c1639112179632c4b75ccc01196651107dad5db5.jpg)  
(b) Comparison of the oldest packet's AoI when M varies.  
Fig. 5. Comparison when M varies.

![](images/017712fe7076ec971585e858939944642e6b76235d6274a4b12ba66976f6317f.jpg)  
Fig. 6. Comparison of energy consumption when M varies.

Next, we compare the AoI of the oldest packet which is from the node $b _ { \pi ( 1 ) } ^ { ( 1 ) }$ that samples data first in the whole IoT network, among different algorithms. As can be seen in Fig. 5 (b), our proposed algorithm also exhibits a good performance in reducing the AoI of the oldest packet when compared with the genetic and SA algorithms. Furthermore, the TWA\*-sampling algorithm obtains the best results among the three decoding methods and Ptr-A\*.

Given that the proposed algorithm can find the best UAV trajectory with the minimal AoI in the UAV-IoT network among all the algorithms under comparison, it is of interest to further investigate the effective energy consumption of the UAV. It can be seen from (8) and (11) that the energy consumption of the UAV is related to its flying time and hovering time. The effective energy consumption is defined as the energy consumption of the UAV from the first visited hovering point to the end point, i.e., in completing its data collection task. Fig. 6 compares the effective energy consumptions for all the algorithms for different values of M . In particular, plotted in the figure are the average ratios of the effective energy consumptions by different algorithms with over that of the TWA\*-sampling algorithm. As can be seen, our proposed algorithm with any of the three decoding methods has a better performance when compared to the genetic and SA algorithms, whereas the TWA\*-sampling algorithm obtains the best result. The results in Fig. 6 are in line with expectations because with our proposed algorithm, the UAV spends less time to gather data than with the other two algorithms, which helps to reduce the effective energy consumption of the UAV.

Table II compares the running time at inference. As M increases, the running time of all the algorithms increases, which is well expected. We can see that among all the algorithms and for all the values of M , the running time of the

TABLE II  
COMPARISON OF RUNNING TIME (SECOND)
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=6>Algorithm</td></tr><tr><td rowspan=1 colspan=1>M</td><td rowspan=1 colspan=1>TWA*-sampling</td><td rowspan=1 colspan=1>TWA*-beam search</td><td rowspan=1 colspan=1>TWA*-greedy</td><td rowspan=1 colspan=1>Ptr-A*</td><td rowspan=1 colspan=1>Genetic</td><td rowspan=1 colspan=1>SA</td></tr><tr><td rowspan=1 colspan=1>10</td><td rowspan=1 colspan=1>1.9693</td><td rowspan=1 colspan=1>2.0653</td><td rowspan=1 colspan=1>1.9556</td><td rowspan=1 colspan=1>11.1556</td><td rowspan=1 colspan=1>47.57</td><td rowspan=1 colspan=1>5.5345</td></tr><tr><td rowspan=1 colspan=1>15</td><td rowspan=1 colspan=1>2.1412</td><td rowspan=1 colspan=1>2.2861</td><td rowspan=1 colspan=1>2.1055</td><td rowspan=1 colspan=1>19.3212</td><td rowspan=1 colspan=1>95.46</td><td rowspan=1 colspan=1>6.4262</td></tr><tr><td rowspan=1 colspan=1>20</td><td rowspan=1 colspan=1>2.3392</td><td rowspan=1 colspan=1>2.4900</td><td rowspan=1 colspan=1>2.3037</td><td rowspan=1 colspan=1>27.9023</td><td rowspan=1 colspan=1>163.41</td><td rowspan=1 colspan=1>6.8623</td></tr><tr><td rowspan=1 colspan=1>25</td><td rowspan=1 colspan=1>2.6006</td><td rowspan=1 colspan=1>2.8087</td><td rowspan=1 colspan=1>2.5778</td><td rowspan=1 colspan=1>36.9560</td><td rowspan=1 colspan=1>261.69</td><td rowspan=1 colspan=1>7.4619</td></tr><tr><td rowspan=1 colspan=1>30</td><td rowspan=1 colspan=1>2.8700</td><td rowspan=1 colspan=1>3.0876</td><td rowspan=1 colspan=1>2.8300</td><td rowspan=1 colspan=1>43.5498</td><td rowspan=1 colspan=1>392.97</td><td rowspan=1 colspan=1>8.3378</td></tr><tr><td rowspan=1 colspan=1>35</td><td rowspan=1 colspan=1>3.2018</td><td rowspan=1 colspan=1>3.4531</td><td rowspan=1 colspan=1>3.1536</td><td rowspan=1 colspan=1>52.4981</td><td rowspan=1 colspan=1>562.25</td><td rowspan=1 colspan=1>9.2576</td></tr><tr><td rowspan=1 colspan=1>40</td><td rowspan=1 colspan=1>3.8059</td><td rowspan=1 colspan=1>3.7506</td><td rowspan=1 colspan=1>3.5583</td><td rowspan=1 colspan=1>61.6301</td><td rowspan=1 colspan=1>749.16</td><td rowspan=1 colspan=1>9.6988</td></tr><tr><td rowspan=1 colspan=1>45</td><td rowspan=1 colspan=1>4.5112</td><td rowspan=1 colspan=1>4.5190</td><td rowspan=1 colspan=1>3.8995</td><td rowspan=1 colspan=1>75.8817</td><td rowspan=1 colspan=1>991.85</td><td rowspan=1 colspan=1>10.2019</td></tr></table>

TWA\*-greedy algorithm is always shortest. Although TWA\*- sampling obtains the best performance in reducing the total AoI as well as the AoI of the oldest packet (as can be seen from Fig. 5 (a) and Fig. 5 (b)), it has a longer running time than TWA\*-greedy, which is reasonable. Similarly, TWA\*-beam search takes slightly more time than TWA\*-greedy because it needs more computational time to search for a better solution than TWA\*-greedy. We can observe that the genetic algorithm takes the longest time among all the algorithms and its running time significantly increases as M increases. The running time of SA is acceptable in comparison with the genetic algorithm. Overall, the computational performance of our proposed model with all three decoding methods is significantly better than the SA and genetic algorithms. The running time of Ptr-A\* is much greater than that of TWA\*-sampling, TWA\*-beam search, and TWA\*-greedy. For example, when M , the running time of the Ptr-A\* is 11.9 times that of TWA\*- sampling. When M increases to 45, the running time of the Ptr-A\* is 16.8 times that of TWA\*-sampling. This is because transformer-based techniques can process a sequence in parallel. However, with Ptr-A\*, the elements of a sequence must be processed one by one. Hence, our proposed TWA\* with three decoding methods is faster than Ptr-A\*.

In order to provide insights about the effect of $\gamma _ { \mathrm { t h } }$ on the total AoI, we set the same number of devices, namely $N _ { m } = 2 0 .$ , in each ground cluster and evaluate in Fig. 7 (a) the performance of TWA\*-sampling for different values of $\gamma _ { \mathrm { t h } } .$ According to Lemma 1 and (6), the smaller the value of $\gamma _ { \mathrm { t h } }$ is, the larger the area of each hovering disk $O _ { m }$ will be. This will affect the positions of hovering points and thus the total AoI. As we can see in Fig. 7 (a), for any given number of ground clusters, the total AoI gradually increases as the value of $\gamma _ { \mathrm { t h } }$ decreases. For example, when M , the values of total AoI in 10 dB, 20 dB, and 30 dB are 22707, 21655, and 20457 seconds, respectively. We can also observe that the total AoI gap among three values of $\gamma _ { \mathrm { t h } }$ increases as $\gamma _ { \mathrm { t h } }$ becomes higher.

Next, we compare the total flying time and the total hovering time of the UAV that make up of the AoI value $A _ { \pi ( 1 ) } ^ { ( 1 ) ^ { - } }$ of the oldest packet in networks with different number of clusters. Specifically these total flying time and total hovering time of the UAV are calculated as $\scriptstyle \sum _ { t = 1 } ^ { M } T _ { ( c _ { \pi ( t ) } , c _ { \pi ( t + 1 ) } ) } ^ { ( \mathrm { f l y } ) } $ and $\textstyle \sum _ { t = 1 } ^ { M } T _ { c _ { \pi ( t ) } } ^ { ( \mathrm { h o v } ) }$ , respectively. In each network, we also compare these portions of time when $\gamma _ { \mathrm { t h } }$ varies. Note that, the AoI values of the oldest packet are different for different $\gamma _ { \mathrm { t h } }$ values in a network. The percentages of the total hovering and the total flying time that contribute to the AoI value of the oldest packet are plotted in Fig. 7 (b). When $M = 1 0$ , the total flying time is always higher than the total hovering time for any thresholds $\gamma _ { \mathrm { t h } }$ . In addition, as γ<sub>th</sub> increases, the flying time portion increases. This is because the selected hovering point may be closer to the center of each hovering disk if the value of $\gamma _ { \mathrm { t h } }$ is large, which will cause the flight distance to be longer and thus increases the total flying time. When M increases, the UAV needs more time to collect data, and we can see that the hovering time portion slowly increases as expected.

![](images/44f0620a685dd21fa2d4f6528505358502f367479e041ddcfbb6225ab702972a.jpg)  
(a) Comparison of the total AoI for different values of $\gamma _ { \mathrm { t h } } .$

![](images/ac635bff019fab6575b4f8a453dea0d942fbf71c64a89550fa50ab0de638fa1d.jpg)  
(b) Percentages of the total flying time and the total hovering time for different values of $\gamma _ { \mathrm { t h } }$  
Fig. 7. Comparison for different values of $\gamma _ { \mathrm { t h } } .$

Fig. 8 (a) compares the total AoI for different algorithms and for different numbers of devices in each cluster. We test the trained model on a 20-clusters instance with the same number of devices in each cluster. It can be seen that the proposed algorithm with the sampling decoding method always obtains the minimal values when compared to the genetic and SA algorithms. This clearly shows that our proposed algorithm can find a better trajectory in reducing the total AoI. As N increases, there is a large performance gap between TWA\*- sampling and the two algorithms under comparison.

![](images/6cf820df900c0321850a5fcfd765576379bdff41deae15f5bee57047a7c2db3a.jpg)  
(a) Comparison of the total AoI when N varies

![](images/14d30dd6c569391a0b35048b441a9af0f5706f29fa07fa4c11c5d38ac42198a9.jpg)  
(b) Percentages of flying time and hovering time when N varies  
Fig. 8. Comparison when N varies.

Fig. 8 (b) plots the percentages of the total flying time and the total hovering time that make up of the AoI value of the oldest packet in the 20-clusters network when N varies. For all the algorithms considered in Fig. 8 (b), as N increases, the percentage of the total hovering time gradually increases. This trend is justified because the UAV needs more time to collect data from a larger number of ground nodes.

## V. CONCLUSION

In this paper, we have investigated and solved the problem of AoI-oriented data collection in UAV-enabled cluster-based IoT networks. With the aim of minimizing the total AoI of the collected data, we formulated the trajectory optimization problem as the GTSP by jointly optimizing the selection of hovering points of the UAV and the visiting order to these hovering points. To solve the formulated problem, we designed a novel algorithm framework based on the state-of-the-art transformer. In particular, the formulated trajectory planning problem is viewed as a “translation problem”. The whole UAV-IoT network serves as the “source language” to the proposed model and the “target language” of the model is the UAV’s trajectory with the minimal total AoI, where the transformer is utilized to generate the visiting order and the weighted $\mathbf { A } ^ { * }$ is used to quickly find the hovering points. The proposed model is trained by reinforcement learning to learn a trajectory planning policy. Comprehensive experiments were conducted to evaluate the performance of the proposed algorithm. The obtained simulation results showed that the learned policy by the proposed algorithm has a strong generalization ability. When compared with other algorithms, our proposed algorithm with three different decoding methods not only reduces the total AoI, but also reduces the AoI of the oldest packet and the effective energy consumption of the UAV. Moreover, our method also has lower computation time. In future, we plan to extend the system model and the proposed algorithm to the multiple UAVs-assisted IoT network.

## APPENDIX I PROOF OF LEMMA 1

By substituting (1)–(4) into (5), we can get the formulation (A.1), shown at the bottom of the page. For a fixed H, $2 0 \log _ { 1 0 } \Big ( 4 \pi f _ { c } \sqrt { H ^ { 2 } + R _ { ( c _ { m } , b _ { m } ) } ^ { 2 } } / c \Big )$ is monotonically increasing with respect to $R _ { ( c _ { m } , b _ { m } ) }$ <sup>m</sup>. As the analysis in [29] shows, $P _ { c _ { m } } ^ { \mathrm { ( L o S ) } }$ is monotonically increasing with respect to $\theta _ { c _ { m } } .$ Since $\theta _ { c _ { m } } = \arctan ( H / R _ { ( c _ { m } , b _ { m } ) } ) , \overset { \mathrm { ~ \tiny ~ ( L o S ) ~ } } { P } _ { c _ { m } } ^ { \mathrm { ( L o S ) } }$ is monotonically <sup>= arctan(</sup>decreasing with respect to $R _ { ( c _ { m } , b _ { m } ) }$ for a fixed H. Then, $\left( \xi _ { \mathrm { L o S } } - \xi _ { \mathrm { N L o S } } \right) \bigg / \bigg ( 1 + \beta \exp { \left( - \widetilde { \beta } \left( \theta _ { c _ { m } } - \beta \right) \right) } \bigg )$ is monotonically increasing with respect to $R _ { ( c _ { m } , b _ { m } ) }$ because $\xi _ { \mathrm { L o S } } <$ $\xi _ { \mathrm { N L o S } }$ . Finally, we arrive at the conclusion that the left side of (A.1) is monotonically decreasing with respect to $R _ { ( c _ { m } , b _ { m } ) }$ for a fixed H. When the SNR $\gamma _ { c _ { m } }$ <sup>m m</sup>decreases to the threshold $\gamma _ { \mathrm { t h } } .$ , we can obtain the maximum $R ^ { * }$ . Hence, for any $c _ { m } .$ , the UAV can successfully receive data from $b _ { m }$ if $R _ { ( c _ { m } , b _ { m } ) } \leq R ^ { * }$

$$
\begin{array} { r l r } & { } & { P _ { \mathrm { C H } } \frac { 1 } { \sigma ^ { 2 } \left( P _ { c _ { m } } ^ { ( \mathrm { L o S } ) } L _ { c _ { m } } ^ { ( \mathrm { L o S } ) } + \left( 1 - P _ { c _ { m } } ^ { ( \mathrm { L o S } ) } \right) L _ { c _ { m } } ^ { ( \mathrm { N L o S } ) } \right) } \geq \gamma _ { \mathrm { { t h } } } , } \\ & { } & { P _ { \mathrm { C H } } \frac { 1 } { \sigma ^ { 2 } \left( 2 0 \log _ { 1 0 } \left( \frac { 4 \pi f _ { c } d _ { ( c _ { m } , b _ { m } ) } } { v _ { \mathrm { l i g h } } } \right) + P _ { c _ { m } } ^ { ( \mathrm { L o S } ) } \left( \xi _ { \mathrm { L o S } } - \xi _ { \mathrm { N L o S } } \right) + \xi _ { \mathrm { N L o S } } \right) } \geq \gamma _ { \mathrm { { t h } } } , } \\ & { } & { P _ { \mathrm { C H } } \frac { 1 } { \sigma ^ { 2 } \left( 2 0 \log _ { 1 0 } \left( \frac { 4 \pi f _ { c } \sqrt { H ^ { 2 } + R _ { ( c _ { m } , b _ { m } ) } ^ { 2 } } } { v _ { \mathrm { l i g h } } } \right) + \frac { \xi _ { \mathrm { l a s } } - \xi _ { \mathrm { N L o S } } } { 1 + \beta \exp \left( - \beta ( \theta _ { c _ { m } } - \beta ) \right) } + \xi _ { \mathrm { N L o S } } \right) } \geq \gamma _ { \mathrm { { t h } } } . } \end{array}\tag{A.1}
$$

## REFERENCES

[1] S. Hu, X. Chen, W. Ni, E. Hossain, and X. Wang, “Distributed machine learning for wireless communication networks: Techniques, architectures, and applications,” IEEE Commun. Surveys Tuts., vol. 23, no. 3, pp. 1458–1493, 3rd Quart., 2021.

[2] M. Mozaffari, W. Saad, M. Bennis, Y.-H. Nam, and M. Debbah, “A tutorial on UAVs for wireless networks: Applications, challenges, and open problems,” IEEE Commun. Surveys Tuts., vol. 21, no. 3, pp. 2334–2360, 3rd Quart., 2019.

[3] S. Hu, W. Ni, X. Wang, A. Jamalipour, and D. Ta, “Joint optimization of trajectory, propulsion, and thrust powers for covert UAV-on-UAV video tracking and surveillance,” IEEE Trans. Inf. Forensics Security, vol. 16, pp. 1959–1972, 2021.

[4] S. Hu, Q. Wu, and X. Wang, “Energy management and trajectory optimization for UAV-enabled legitimate monitoring systems,” IEEE Trans. Wireless Commun., vol. 20, no. 1, pp. 142–155, Jan. 2021.

[5] B. Zhu, E. Bedeer, H. H. Nguyen, R. Barton, and J. Henry, “UAV trajectory planning in wireless sensor networks for energy consumption minimization by deep reinforcement learning,” IEEE Trans. Veh. Technol., vol. 70, no. 9, pp. 9540–9554, Sep. 2021.

[6] S. Zhang, H. Zhang, Z. Han, H. V. Poor, and L. Song, “Age of information in a cellular internet of UAVs: Sensing and communication trade-off design,” IEEE Trans. Wireless Commun., vol. 19, no. 10, pp. 6578–6592, Oct. 2020.

[7] S. Kaul, R. Yates, and M. Gruteser, “Real-time status: How often should one update,” in Proc. IEEE Conf. Comput. Commun. (INFOCOM), Mar. 2012, pp. 2731–2735.

[8] H. Hu, K. Xiong, G. Qu, Q. Ni, P. Fan, and K. B. Letaief, “AoI-minimal trajectory planning and data collection in UAV-assisted wireless powered IoT networks,” IEEE Internet Things J., vol. 8, no. 2, pp. 1211–1223, Jan. 2021.

[9] J. Liu, X. Wang, B. Bai, and H. Dai, “Age-optimal trajectory planning for UAV-assisted data collection,” in Proc. IEEE Int. Conf. Comput. Commun. Workshops (INFOCOM), Apr. 2018, pp. 553–558.

[10] J. Liu, P. Tong, X. Wang, B. Bai, and H. Dai, “UAV-aided data collection for information freshness in wireless sensor networks,” IEEE Trans. Wireless Commun., vol. 20, no. 4, pp. 2368–2382, Apr. 2021.

[11] Z. Jia, X. Qin, Z. Wang, and B. Liu, “Age-based path planning and data acquisition in UAV-assisted IoT networks,” in Proc. IEEE Int. Conf. Commun. Workshops (ICC Workshops), May 2019, pp. 1–6.

[12] M. A. Abd-Elmagid and H. S. Dhillon, “Average peak age-ofinformation minimization in UAV-assisted IoT networks,” IEEE Trans. Veh. Technol., vol. 68, no. 2, pp. 2003–2008, Feb. 2019.

[13] S. F. Abedin, M. S. Munir, N. H. Tran, Z. Han, and C. S. Hong, “Data freshness and energy-efficient UAV navigation optimization: A deep reinforcement learning approach,” IEEE Trans. Intell. Transp. Syst., vol. 22, no. 9, pp. 5994–6006, Sep. 2021.

[14] M. Yi, X. Wang, J. Liu, Y. Zhang, and B. Bai, “Deep reinforcement learning for fresh data collection in UAV-assisted IoT networks,” in Proc. IEEE INFOCOM Workshops, Jul. 2020, pp. 716–721.

[15] D. Ebrahimi, S. Sharafeddine, P.-H. Ho, and C. Assi, “UAV-aided projection-based compressive data gathering in wireless sensor networks,” IEEE Internet Things J., vol. 6, no. 2, pp. 1893–1905, Apr. 2019.

[16] Y. Yuan, L. Lei, T. X. Vu, S. Chatzinotas, S. Sun, and B. Ottersten, “Energy minimization in UAV-aided networks: Actor-critic learning for constrained scheduling optimization,” IEEE Trans. Veh. Technol., vol. 70, no. 5, pp. 5028–5042, May 2021.

[17] L. Shen, N. Wang, Z. Zhu, Y. Fan, X. Ji, and X. Mu, “UAV-enabled data collection for mMTC networks: AEM modeling and energy-efficient trajectory design,” in Proc. IEEE Int. Conf. Commun. (ICC), Jun. 2020, pp. 1–6.

[18] J. T. Isaacs and J. P. Hespanha, “Dubins traveling salesman problem with neighborhoods: A graph-based approach,” Algorithms, vol. 6, no. 1, pp. 84–99, Feb. 2013.

[19] R. Penicka, J. Faigl, P. Vana, and M. Saska, “Dubins orienteering problem with neighborhoods,” in Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS), Jun. 2017, pp. 1555–1562.

[20] M. A. Abd-Elmagid, A. Ferdowsi, H. S. Dhillon, and W. Saad, “Deep reinforcement learning for minimizing Age-of-Information in UAV-assisted networks,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), Dec. 2019, pp. 1–6.

[21] W. Li, L. Wang, and A. Fei, “Minimizing packet expiration loss with path planning in UAV-assisted data sensing,” IEEE Wireless Commun. Lett., vol. 8, no. 6, pp. 1520–1523, Dec. 2019.

[22] A. Ferdowsi, M. A. Abd-Elmagid, W. Saad, and H. S. Dhillon, “Neural combinatorial deep reinforcement learning for age-optimal joint trajectory and scheduling design in UAV-assisted networks,” IEEE J. Sel. Areas Commun., vol. 39, no. 5, pp. 1250–1265, May 2021.

[23] A. Vaswani et al., “Attention is all you need,” in Proc. Adv. Neural Inf. Process. Syst. (NIPS), Jun. 2017, pp. 5998–6008.

[24] M. Deudon, P. Cournut, A. Lacoste, Y. Adulyasak, and L.-M. Rousseau, “Learning heuristics for the TSP by policy gradient,” in Proc. Int. Conf. Integr. Constraint Program., Artif. Intell., Oper. Res. (CPAIOR), Jun. 2018, pp. 170–181.

[25] W. Kool, H. Van Hoof, and M. Welling, “Attention, learn to solve routing problems!” in Proc. Int. Conf. Learn. Represent. (ICLR), May 2019, pp. 1–25.

[26] Y. Wu, W. Song, Z. Cao, J. Zhang, and A. Lim, “Learning improvement heuristics for solving routing problems,” IEEE Trans. Neural Netw. Learn. Syst., vol. 33, no. 9, pp. 1–13, Apr. 2021.

[27] X. Bresson and T. Laurent, “The transformer network for the traveling salesman problem,” 2021, arXiv:2103.03012.

[28] Y. Sun, E. Uysal-Biyikoglu, R. D. Yates, C. E. Koksal, and N. B. Shroff, “Update or wait: How to keep your data fresh,” IEEE Trans. Inf. Theory, vol. 63, no. 11, pp. 7492–7508, Nov. 2017.

[29] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6, pp. 569–572, Dec. 2014.

[30] J. Yao and N. Ansari, “QoS-aware power control in Internet of Drones for data collection service,” IEEE Trans. Veh. Technol., vol. 68, no. 7, pp. 6649–6656, Jul. 2019.

[31] Y. Zeng, J. Xu, and R. Zhang, “Energy minimization for wireless communication with rotary-wing UAV,” IEEE Trans. Wireless Commun., vol. 18, no. 4, pp. 2329–2345, Apr. 2019.

[32] P. Tong, J. Liu, X. Wang, B. Bai, and H. Dai, “UAV-enabled age-optimal data collection in wireless sensor networks,” in Proc. IEEE Int. Conf. Commun. Workshops (ICC), May 2019, pp. 1–6.

[33] A. Dumitrescu and J. S. B. Mitchell, “Approximation algorithms for TSP with neighborhoods in the plane,” J. Algorithms, vol. 48, no. 1, pp. 135–159, Aug. 2003.

[34] B. Yuan, M. Orlowska, and S. Sadiq, “On the optimal robot routing problem in wireless sensor networks,” IEEE Trans. Knowl. Data Eng., vol. 19, no. 9, pp. 1252–1261, Sep. 2007.

[35] Concorde. [Online]. Available: http://www.math.uwaterloo.ca/tsp/concorde.html

[36] T. Lin, Y. Wang, X. Liu, and X. Qiu, “A survey of transformers,” 2021, arXiv:2106.04554.

[37] R. Ebendt and R. Drechsler, “Weighted A search unifying view and application,” Artif. Intell., vol. 173, no. 14, pp. 1310–1342, Sep. 2009.

[38] G. Ramalingam and T. Reps, “On the computational complexity of dynamic graph problems,” Theor. Comput. Sci., vol. 158, nos. 1–2, pp. 233–277, May 1996.

[39] R. J. Williams, “Simple statistical gradient-following algorithms for connectionist reinforcement learning,” Mach. Learn., vol. 8, nos. 3–4, pp. 229–256, May 1992.

[40] J. Yang, C. Wu, H. P. Lee, and Y. Liang, “Solving traveling salesman problems using generalized chromosome genetic algorithm,” Prog. Natural Sci., vol. 18, no. 7, pp. 887–892, Jul. 2008.

[41] S.-H. Zhan, J. Lin, Z.-J. Zhang, and Y.-W. Zhong, “List-based simulated annealing algorithm for traveling salesman problem,” Comput. Intell. Neurosci., vol. 2016, pp. 1–12, Mar. 2016.

![](images/600988e3fc51de1c98517fe22e9287963d5b1f25aa0bb0f7aebef23ccbfcb0e4.jpg)  
Botao Zhu is currently pursuing the Ph.D. degree with the Department of Electrical and Computer Engineering, University of Saskatchewan, Saskatoon, Canada. His current research interests include wireless sensor networks, the Internet-of-Things, machine learning, and unmanned aerial vehicles.

![](images/8f71930ff234a8028ddba3a934b47a4ad3b0525d48dbb0119b2152ca084ad6a7.jpg)

Ebrahim Bedeer (Member, IEEE) received the B.Sc. (Hons.) and M.Sc. degrees from Tanta University, Tanta, Egypt, and the Ph.D. degree from Memorial University, St. Johns, NL, Canada, all in electrical engineering.

In 2019, he joined the Department of Electrical and Computer Engineering, University of Saskatchewan as an Assistant Professor. Before that, he was an Assistant Professor (Lecturer in the U.K.) at Ulster University, U.K., and a Postdoctoral Fellow at Carleton University, Ottawa, ON, Canada, and The

University of British Columbia, Kelowna, BC, Canada. His current research interests include applications of optimization techniques in signal processing and wireless communications, spectral efficient communication systems, and the Internet-of-Things (IoT). He is a Registered Member of the Association of Professional Engineers and Geoscientists of Saskatchewan (APEGS).

![](images/5272f3b5033fa6d846fcfbe1ef1ac9ba45c76178dcbfba0ae09f4c3017940f9e.jpg)

Ha H. Nguyen (Senior Member, IEEE) received the B.Eng. degree from the Hanoi University of Technology (HUT), Hanoi, Vietnam, in 1995, the M.Eng. degree from the Asian Institute of Technology (AIT), Bangkok, Thailand, in 1997, and the Ph.D. degree from the University of Manitoba, Winnipeg, MB, Canada, in 2001, all in electrical engineering. He joined the Department of Electrical and Computer Engineering, University of Saskatchewan, Saskatoon, SK, Canada, in 2001, and became a Full Professor in 2007. He currently holds the position of NSERC/Cisco Industrial Research Chair in low-power wireless access for sensor networks. He is the coauthor (with Ed Shwedyk) of the textbook A First Course in Digital Communications (published by Cambridge University Press). His research interests fall into broad areas of communication theory, wireless communications, and statistical signal processing. He is a fellow of the Engineering Institute of Canada (EIC) and a Registered Member of the Association of Professional Engineers and Geoscientists of Saskatchewan (APEGS). He served as a technical program chair for numerous IEEE events. He was an Associate Editor of the IEEE TRANSACTIONS ON WIRELESS COMMUNICATIONS and IEEE WIRELESS COMMUNICATIONS LETTERS from 2007 to 2011 and from 2011 to 2016. He currently serves as an Associate Editor for the IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY.

![](images/183a4e8c75687bf477797d5a4e4928ceae1bb2a7fa9ab169de187752fffa3a45.jpg)

Robert Barton (Member, IEEE) received the degree in engineering physics from The University of British Columbia. He is currently a Distinguished Engineer at the Cisco’s Digital Transformation and Innovation Group, where he has the role of the Chief Architect for Cisco Canada and Cisco’s Global IoT Sales Organization. He has worked in the IT industry for over 23 years, the last 20 of which have been at Cisco. He is a published author, with titles on the subjects of network QoS, wireless, the IoT, machine learning, and data analytics. He has also

contributed to many academic papers, and leads Cisco’s university research partnership program. He also holds many patents in the areas of wireless communications, segment routing, and machine learning. His current areas of work include wireless communications, industrial networking, the IoT, and AI/ML in networking systems.

![](images/f5c74c7b68dc6e5797b131f64566302c0a6ecad10422fae61779f332609c2fa8.jpg)

Zhen Gao (Member, IEEE) received the B.S. degree in information engineering from the Beijing Institute of Technology, Beijing, China, in 2011, and the Ph.D. degree in communication and signal processing with the Tsinghua National Laboratory for Information Science and Technology, Department of Electronic Engineering, Tsinghua University, Beijing, in 2016. He is currently an Associate Professor with the Beijing Institute of Technology. His research interests are in wireless communications, with a focus on multicarrier modulations,

multiple antenna systems, and sparse signal processing. He was a recipient of the IEEE Broadcast Technology Society 2016 Scott Helt Memorial Award (Best Paper), the Exemplary Reviewer of IEEE COMMUNICATION LETTERS in 2016, IET Electronics Letters Premium Award (Best Paper) in 2016, and the Young Elite Scientists Sponsorship Program (2018–2021) from the China Association for Science and Technology.