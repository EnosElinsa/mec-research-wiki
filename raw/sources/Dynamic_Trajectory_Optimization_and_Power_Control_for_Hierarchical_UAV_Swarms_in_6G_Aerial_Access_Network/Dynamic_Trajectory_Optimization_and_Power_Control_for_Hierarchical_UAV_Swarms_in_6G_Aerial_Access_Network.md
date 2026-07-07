# Dynamic Trajectory Optimization and Power Control for Hierarchical UAV Swarms in 6G Aerial Access Network

Ziye Jia , Member, IEEE, Jia He, Lijun He , Member, IEEE, Min Sheng , Fellow, IEEE, Junyu Liu , Member, IEEE, Qihui Wu , Fellow, IEEE, and Zhu Han , Fellow, IEEE

Abstract—Uncrewed aerial vehicles (UAVs) can serve as aerial base stations (BSs) to extend the ubiquitous connectivity for ground users (GUs) in the sixth-generation (6G) era. However, it is challenging to cooperatively deploy multiple UAV swarms in large-scale remote areas. Hence, in this paper, we propose a hierarchical UAV swarms structure for 6G aerial access networks, where the head UAVs serve as aerial BSs, and tail UAVs (T-UAVs) are responsible for relay. In detail, we jointly optimize the dynamic deployment and trajectory of UAV swarms, which is formulated as a multi-objective optimization problem (MOP) to concurrently minimize the energy consumption of UAV swarms and GUs, as well as the delay of GUs. However, the proposed MOP is a mixed integer nonlinear programming and NPhard to solve. Therefore, we develop a K-means and Voronoi diagram based area division method, and construct Fermat points to establish connections between GUs and T-UAVs. Then, an improved non-dominated sorting whale optimization algorithm is proposed to seek Pareto optimal solutions for the transformed MOP. Finally, extensive simulations are conducted to verify the performance of proposed algorithms by comparing with baseline mechanisms, resulting in a 50% complexity reduction.

Index Terms—6G aerial access network (AAN), UAV swarm trajectory planning, multi-objective optimization problem (MOP), Voronoi diagram, Fermat point, improved nondominated sorting whale optimization algorithm (INS-WOA).

## I. INTRODUCTION

(6G) wireless networks, it is necessary to provide

Received 6 December 2024; revised 17 July 2025; accepted 24 August 2025. Date of publication 11 September 2025; date of current version 22 December 2025. This work was supported in part by the National Natural Science Foundation of China under Grant 62301251 and Grant 62201463, in part by the Natural Science Foundation on Frontier Leading Technology Basic Research Project of Jiangsu under Grant BK20222001, in part by the Aeronautical Science Foundation of China under Grant 2023Z071052007, and in part by the Young Elite Scientists Sponsorship Program by China Association for Science and Technology (CAST) under Grant 2023QNRC001. The associate editor coordinating the review of this article and approving it for publication was F. Hou. (Corresponding author: Min Sheng.)

Lijun He is with the School of Information and Control Engineering, China University of Mining and Technology, Xuzhou 221116, China (e-mail: lijunhe@cumt.edu.cn).

Min Sheng and Junyu Liu are with the State Key Laboratory of Integrated Services Networks, Xidian University, Xi’an 710071, China (e-mail: msheng@mail.xidian.edu.cn; junyuliu@xidian.edu.cn).

Zhu Han is with the University of Houston, Houston, TX 77004 USA, and also with the Department of Computer Science and Engineering, Kyung Hee University, Seoul 446-701, South Korea (e-mail: hanzhu22@gmail.com).

Ziye Jia, Jia He, and Qihui Wu are with the College of Electronic and Information Engineering, Nanjing University of Aeronautics and Astronautics, Nanjing 211106, China (e-mail: jiaziye@nuaa.edu.cn; 071940128hejia@nuaa.edu.cn; wuqihui@nuaa.edu.cn).

Digital Object Identifier 10.1109/TWC.2025.3603432 seamless and ubiquitous services for a massive number of ground users (GUs). However, it lacks ground base stations (BSs) in most remote areas, which is challenging for realizing ubiquitous communication services [1], [2]. Uncrewed aerial vehicles (UAVs) are envisioned as a promising paradigm due to the mobility and flexibility [3], [4], [5], which can serve as aerial BSs for both data collection and relay in the 6G aerial access network (AAN) [6]. Moreover, since UAVs can fly close to GUs and establish low-altitude ground-to-air (G2A) communication links, they can be deployed to hover over the target areas, which can help save the energy cost and prolong the operational lifetime of GUs [7]. However, the limited capacity of a single UAV seriously constrains the ability to provide timely services for multiple GUs, especially in large areas.

UAV swarms are proposed to provide large-area coverage services and improve the data collection efficiency in AAN, since the cooperation of multiple UAVs enables stronger capacities and flexibilities [8], [9]. Moreover, the transmission delay is a significant metric for time-sensitive GUs, such as in scenarios of emergency monitoring and safety protection [10], [11]. Consequently, the deployment and trajectory of UAV swarms are more intractable, in which the comprehensive consideration of UAV energy efficiency, GUs energy cost, and transmission delay of GUs is imperative [12], [13]. Besides, the balance among these metrics is significant. Therefore, how to satisfy the energy consumption and transmission delay requirements of remote GUs through flexible deployment of UAV swarms, dynamic adjustment of UAV trajectories and appropriate power control is a key issue.

To this end, we first propose a hierarchical framework for large-area data collection in AAN, with each swarm composed of a head UAV (H-UAV) and several tail UAVs (T-UAVs). Then, to jointly optimize the dynamic deployment and trajectory of UAV swarms, as well as the power control of GUs and T-UAVs, we formulate the UAV swarms assisted data collection multi-objective optimization problem (USDC-MOP) to simultaneously minimize the total energy consumption of UAV swarms, the energy consumed by each GU, and the transmission delay of GUs. Since the proposed multiobjective optimization problem (MOP) is a mixed-integer nonlinear programming (MINLP) and NP-hard to solve, we present the algorithm to facilitate the pre-deployment of UAV swarms by designing the K-means and Voronoi diagram based area division method, and Fermat points based connections establishment mechanism. Then, to efficiently tackle the transformed USDC-MOP with discrete and continuous variables, we propose an improved non-dominated sorting whale optimization algorithm (INS-WOA) to search for Pareto optimal solutions.

The main contributions of this paper are summarized as follows.

1) We propose a hierarchical UAV swarm model with H-UAVs as aerial BSs and T-UAVs for the data collection in remote areas. T-UAVs can dynamically adjust trajectories to meet transmission delay demands and ensure the optimal coverage for remote GUs.

2) We optimize the UAV swarm deployment, trajectories, and power control for the GUs and T-UAVs. It is formulated as a USDC-MOP to minimize the energy consumption of UAV swarms and GUs, and transmission delay of GUs simultaneously. Additionally, it clearly illustrates the balance among these significant metrics.

3) To efficiently solve the USDC-MOP, we propose a UAV swarm pre-deployment algorithm that leverages K-means and Voronoi diagrams to partition GUs into regions for dynamic deployments. The fermat points are generated within each region to facilitate connections between GUs and T-UAVs across varying hovering positions. Additionally, an INS-WOA method is implemented to effectively tackle the transformed USDC-MOP.

4) Extensive simulations are conducted to evaluate the performance of the proposed algorithms under various circumstances. The results demonstrate their superiorities over benchmark MOP schemes in the effectiveness and low time complexity.

The rest of this paper is organized as follows. Related works are presented in Section II. In Section III, we introduce the system model and formulate the USDC-MOP. Furthermore, algorithms are designed in Section IV. Section V conducts simulations and analyzes the results. Finally, conclusions are drawn in Section VI.

## II. RELATED WORKS

## A. Single UAV

As for the single UAV assisted data collection, [14] presented a UAV-aided data collection framework to minimize the completion time from multiple sensors, where a novel successive-hover-fly structure was presented for the UAV. Meanwhile, to enable the efficient trajectory design, the convex approximation and an iterative algorithm were employed to jointly optimize the UAV trajectory and sensor assignment. The work of [15] considered an orthogonal frequency division multiple access (OFDMA) based UAV relay network, and the communication mode, sub-channel allocation, power allocation, as well as the UAV trajectory were jointly optimized to improve the quality of service of users. In [16], a hybrid offline-online optimization scheme was developed for the UAV-enabled data harvesting scenario, which jointly designed the UAV trajectory and communication scheduling by leveraging both the statistical and instantaneous channel state information. It is observed that in the scenario of a single

UAV, the limited energy capacity of the UAV restricts the performance of large-scale data collection.

## B. Multiple UAVs

For multiple UAV-assisted scenarios, [17] studied the problem of minimizing the total average age of information in a multi-UAV data collection system via a multi-agent deep reinforcement learning algorithm. Since the optimization for multiple UAVs trajectory was coupled with communication resource allocation, [18] considered the various mobility constraints and proposed an offline convex optimization method and an online convex-assisted reinforcement learning method to jointly optimize UAV trajectories, user association, and power control. The work of [19] studied the joint optimization of trajectory planning, communication design for multiple UAVs BSs, and access control of GUs, by presenting a multi-head attention mechanism to ensure efficient and fair communication. Reference [20] proposed a novel graph attention multi-agent trust region reinforcement learning framework to solve the multi-UAV assisted communication problem, by introducing the graph recurrent network to process and analyze the complex topology of communication networks. However, these works have not taken full advantages of the cooperation among UAVs for higher efficiency. Comparatively, UAV swarms are more applicable for complex missions in both military and civilian fields, due to the close collaboration and flexible large-scale coverage.

## C. UAV Swarms

Several recent works have begun to study the UAV swarmenabled data collection. The authors in [21] discussed a UAV swarm assisted time-sensitive data collection system for remote sensors, highlighting the complexities in planning UAV swarm trajectories with constraints of UAV capabilities and budget limitations. In work [22], authors suggested the integration of formation flight and swarm deployment for multiple UAVs by designing a distributed control framework inspired by biological systems, enabling efficient formation and collision avoidance in dynamic environments. In [23], the authors considered a scenario of UAV swarm deployment and trajectory to realize three-dimensional (3D) coverage with the effects of obstacles, and presented the Q-learning method to minimize the total trajectory loss of the UAV swarm. The work in [24] investigated a UAV swarm-assisted aerial-ground collaborative computing system to enhance the computation efficiency for ground smart mobile devices by optimizing the group formation, UAV trajectories, and resource allocation. However, unlike homogeneous UAVs in [21], [22], [23], and [24], our hierarchical structure decouples base-station functions with H-UAVs and T-UAVs for reducing data delay, enabling the dynamic trajectory design in each swarm.

Although the above works have been studied towards UAV swarm-assisted data collection, most of them have not investigated the hierarchical swarm framework of heterogeneous UAVs for data collection. Furthermore, most studies focused on the deployment of the individual UAV swarm, without the consideration of the collaborative deployment among multiple

![](images/8c2807da468e0c0c9db3f2df834ef06d7d4afa92b245d3cb0b91e1baa90481c0.jpg)  
Fig. 1. Hierarchical UAV swarms assisted 6G AAN data collection.

UAV swarms. Besides, the energy efficiency and transmission delay of GUs are mostly ignored, which are crucial metrics for service qualities. Unlike the existing works focusing on the single swarm deployment, our hierarchical model enables the large-scale cooperative coverage, while the joint optimization of trajectory and power control addresses the trade-off between the energy efficiency and latency-critical services.

## III. SYSTEM MODEL AND PROBLEM FORMULATION

As shown in Fig. 1, we consider a hierarchical UAV swarms assisted 6G AAN data collection scenario. In particular, a set $\mathcal { U } = \{ 1 , 2 , \cdots , U \}$ of GUs are distributed in a remote largescale area to sense the environment information, and a set $\mathcal { S } = \{ 1 , 2 , \cdots , S \}$ of UAV swarms are deployed to provide data collection services. Specifically, any UAV swarm $s \in S$ consists of one H-UAV $h _ { s } \in \mathscr { H } = \{ h _ { 1 } , h _ { 2 } , \cdot \cdot \cdot , h _ { S } \}$ served as the aerial BS, and a set ${ \mathcal { V } } _ { s } = \left\{ v _ { 1 } ^ { s } , v _ { 2 } ^ { s } , \cdot \cdot \cdot , V _ { M _ { s } } ^ { s } \right\}$ of T-UAVs responsible for collecting and relaying data for multiple GUs, where $v _ { m } ^ { s }$ denotes the m-th T-UAV in UAV swarm s. Notably, $M _ { s }$ is an integer variable denoting the number of T-UAVs in swarm $s ,$ which is optimized depending on the distribution of GUs. In other words, we can flexibly adjust the number of T-UAV $M _ { s }$ in different UAV swarms to improve data collection efficiency, and the following constraints should be satisfied,

$$
M _ { s } \leq M _ { m a x } , \forall s ,
$$

and

(1)

$$
\sum _ { s = 1 } ^ { S } M _ { s } = M ,\tag{2}
$$

where $M _ { m a x }$ and M represent the maximum number of T-UAVs within a UAV swarm and total number of T-UAVs. The key notations used in this paper are summarized in Table I.

We employ a 3D Cartesian coordinate Θ to describe the data collection scenario, i.e.,

![](images/1c19794003d58aa4d00abf6f6afd8dc03e959c2a8b9a66058dbc112eb4d86053.jpg)

$$
\begin{array}{c} \begin{array} { r } { \Theta = \left\{ \left. \left( x , y , z \right) \middle | \left. Y _ { \operatorname* { m i n } } \leq x \leq X _ { \operatorname* { m a x } } \right. \right\} , \right\} \\ { Z _ { \operatorname* { m i n } } \leq y \leq Y _ { \operatorname* { m a x } } } \end{array} } ,  \end{array}\tag{3}
$$

<table><tr><td></td><td>H-UAV</td><td>-·-&gt;</td><td>A2A link</td><td>Fermat point</td></tr><tr><td></td><td>T-UAV</td><td></td><td>G2A link</td><td>N GUs</td></tr><tr><td></td><td>UAV swarm</td><td></td><td>A</td><td>Trajectory of T-UAV</td></tr></table>

KEY NOTATIONS  
TABLE I
<table><tr><td>Notation</td><td>Description</td></tr><tr><td>U, S, H</td><td>Set of GUs, UAV swarms, H-UAVs</td></tr><tr><td>U, S, M</td><td>Number of GUs, UAV swarms, and T-UAVs</td></tr><tr><td> $q _ { u } , q _ { s } , q _ { m } ^ { s }$ </td><td>3D Coordinates of GU u, H-UAV  $h _ { s }$  , and T-UAV  $v _ { m } ^ { s }$ </td></tr><tr><td> $\nu _ { s }$ </td><td>Set of T-UAVs in UAV swarm s</td></tr><tr><td> $M _ { s }$ </td><td>Integer variable indicating the number of T-UAVs in swarm s</td></tr><tr><td> $N$ </td><td>Number of hovering points of all T-UAVs</td></tr><tr><td> $N _ { m } ^ { s }$ </td><td>Number of hovering points of the T-UAV  $v _ { m } ^ { s }$ </td></tr><tr><td> $\phi _ { m } ^ { s }$ </td><td>Trajectory path variable of T-UAV  $v _ { m } ^ { s }$ </td></tr><tr><td> $\Psi _ { m } ^ { s }$ </td><td>Set of visiting sequences for T-UAV  $v _ { m } ^ { s }$ </td></tr><tr><td> $\gamma _ { u , m , s } ^ { n }$ </td><td>Connection variable between GU u and T-UAV  $v _ { m } ^ { s }$ </td></tr><tr><td> $d _ { u , m }$ </td><td>Distance between GU u and T-UAV  $v _ { m } ^ { s }$ </td></tr><tr><td> $d _ { m , s }$ </td><td>Distance between  $\mathrm { T - U A V } ~ v _ { m } ^ { s }$  and H-UAV hs</td></tr><tr><td> $h _ { u , m }$ </td><td>Channel gain between GU u and T-UAV  $v _ { m } ^ { s }$ </td></tr><tr><td> $h _ { m , s }$ </td><td>Channel gain between  $\mathrm { T - U A V } ~ v _ { m } ^ { s }$  and H-UAV  $h _ { s }$ </td></tr><tr><td> $R _ { u , m } ^ { t r }$ </td><td>Transmission rate from GU u to T-UAV  $v _ { m } ^ { s }$ </td></tr><tr><td> $R _ { m } ^ { t r }$  s</td><td>Transmission rate from T-UAV  $v _ { m } ^ { s }$  and H-UAV h8 </td></tr><tr><td> $p _ { u }$ </td><td>Transmission power variable of GU u</td></tr><tr><td> $p _ { m } ^ { s }$ </td><td>Transmission power variable of T-UAV  $v _ { m } ^ { s }$ </td></tr><tr><td> $T _ { u }$ </td><td>Transmission delay of GU u</td></tr><tr><td> $T _ { u , m }$ </td><td>Transmission delay of G2A</td></tr><tr><td> $T _ { m , s }$ </td><td>Transmission delay of A2A</td></tr><tr><td> $T _ { m } ^ { n }$ </td><td>Hovering duration of T-UAV  $v _ { m } ^ { s }$  at hovering position  $q _ { m } ^ { s } ( n )$ </td></tr><tr><td> $T _ { m } ^ { n , n + 1 }$ </td><td>Flight duration of T-UAV  $v _ { m } ^ { s }$  from two hovering positions</td></tr><tr><td> $E _ { m }$ </td><td>Energy consumption of T-UAV  $v _ { m } ^ { s }$ </td></tr><tr><td> $E _ { u }$ </td><td>Energy consumption of GU u</td></tr><tr><td> $E _ { s }$ </td><td>Energy consumption of H-UAV  $h _ { s }$ </td></tr></table>

where $( x , y , z ) \in \Theta$ represents the 3D coordinate of a random position. Hence, the coordinate of GU u is expressed as $q _ { u } =$ $( x _ { u } , y _ { u } , z _ { u } )$ . Taking the real terrain into account, the heights of GUs are not uniform. The positions of H-UAV $h _ { s }$ and T-UAV $v _ { m } ^ { s }$ in UAV swarm s are denoted by $q _ { s } = ( x _ { s } , y _ { s } , z _ { s } )$ and $q _ { m } ^ { s } = ( x _ { m } ^ { s } , y _ { m } ^ { s } , z _ { m } ^ { s } )$ , respectively. The distance $d _ { u , m }$ between GU u and T-UAV $v _ { m } ^ { s }$ is calculated as

$$
d _ { u , m } = { \sqrt { ( x _ { m } ^ { s } - x _ { u } ) ^ { 2 } + ( y _ { m } ^ { s } - y _ { u } ) ^ { 2 } + ( z _ { m } ^ { s } - z _ { u } ) ^ { 2 } } } .\tag{4}
$$

Similarly, the distance $d _ { m , s }$ between T-UAV $v _ { m } ^ { s }$ and H-UAV $h _ { s }$ can be derived as

$$
d _ { m , s } = \sqrt { ( x _ { m } ^ { s } - x _ { s } ) ^ { 2 } + ( y _ { m } ^ { s } - y _ { s } ) ^ { 2 } + ( z _ { m } ^ { s } - z _ { s } ) ^ { 2 } } .\tag{5}
$$

## A. Deployment and Trajectory of UAV Swarms

The deployment and trajectory of the UAV swarms are designed following the successive-hover-fly mode [14]. In other words, at the beginning, UAV swarms are deployed at locations $\boldsymbol { q _ { s } } ~ = ~ \{ q _ { s } , \forall s \}$ . Then, the T-UAVs depart from the swarm deployment positions and successively fly to their designated hovering locations to collect data from GUs, while the H-UAVs remain hovering at the deployment locations to receive data relayed from the T-UAVs, shown in Fig. 1. The trajectory path $\phi _ { m } ^ { s }$ of T-UAV $v _ { m } ^ { s }$ is described as the visiting sequence of $N _ { m } ^ { s }$ hovering positions, i.e., $\begin{array} { r l } { \phi _ { m } ^ { s } } & { { } = } \end{array}$ $\{ q _ { m } ^ { s } ( 0 ) , q _ { m } ^ { s } ( 1 ) , \cdot \cdot \cdot , q _ { m } ^ { s } ( \ddot { N } _ { m } ^ { s } ) \}$ , where $q _ { m } ^ { s } ( n )$ is the n-th hovering positions of T-UAV $v _ { m } ^ { s } \ ( n \in \{ 1 , 2 , \cdots , N _ { m } ^ { s } \} )$ , and the initial position is $q _ { m } ^ { s } ( 0 ) = q _ { s }$ . Further, the trajectory path $\phi _ { m } ^ { s }$ is selected from the visiting sequence set $\Psi _ { m } ^ { s } , \mathrm { i . e . , } \phi _ { m } ^ { s } \in \Psi _ { m } ^ { s } .$ Besides, the size of visiting sequence set $\Psi _ { m } ^ { s }$ is related with the number of hovering positions $N _ { m } ^ { s }$ , which indicates that there are total $N _ { m } ^ { s } !$ possible trajectory paths to be selected for each T-UAV $v _ { \underline { { m } } } ^ { s }$ . The number of hovering locations for all T-UAVs is $N = \sum _ { s = 1 } ^ { S } \sum _ { m = 1 } ^ { M _ { s } } N _ { m } ^ { s }$

## B. Data Collection Model

As illustrated in Fig. 1, the channel models include the G2A model from GUs to T-UAVs, and the air-to-air (A2A) relay model from T-UAVs to the H-UAV. To avoid interference during data collection, we assume that the OFDMA technique is adopted in both the G2A and A2A models, which implies that the T-UAV can simultaneously serve multiple GUs at the hovering points.

1) G2A Channel Model: The G2A channel is considered as a probabilistic path loss model, which consists of both line-of-sight (LoS) and non-LoS (NLoS) links with different probabilities. In particular, the probability of the LoS link [25], [26] between GU u and T-UAV $v _ { m } ^ { s }$ is

$$
\mathcal { P } _ { u , m } ^ { \mathrm { L o S } } = \frac { 1 } { 1 + \alpha \exp \{ - \beta ( \theta _ { u , m } - \alpha ) \} } , \forall u , m ,\tag{6}
$$

where α and $\beta$ are S-curve parameters depending on the environment, and $\theta _ { u , m }$ is the elevation angle from GU u to T-UAV $v _ { m } ^ { s }$

$$
\theta _ { u , m } = \frac { 1 8 0 } { \pi } \arctan \left( \frac { z _ { m } ^ { s } - z _ { u } } { \sqrt { ( x _ { m } ^ { s } - x _ { u } ) ^ { 2 } + ( y _ { m } ^ { s } - y _ { u } ) ^ { 2 } } } \right) , \forall u , m .\tag{7}
$$

Therefore, the G2A channel gain between GU u and T-UAV $v _ { m } ^ { s }$ is

$$
h _ { u , m } = h _ { u , m } ^ { S } h _ { u , m } ^ { F } , \forall u , m .\tag{8}
$$

wherein, $h _ { u , m } ^ { S }$ and $h _ { u , m } ^ { F }$ respectively denote the channel power gain for the small-scale fading and free space fading, i.e.,

$$
h _ { u , m } ^ { S } = \mathcal { P } _ { u , m } ^ { L o S } \eta _ { L o S } + \mathcal { P } _ { u , m } ^ { N L o S } \eta _ { N L o S } , \forall u , m ,\tag{9}
$$

and

$$
h _ { u , m } ^ { F } = { \left( \frac { c } { 4 \pi f d _ { u , m } } \right) } ^ { 2 } , \forall u , m ,\tag{10}
$$

where $\mathcal { P } _ { u , m } ^ { N L o S } \ : = \ : 1 - \mathcal { P } _ { u , m } ^ { L o S } \cdot \ : \eta _ { L o S }$ and $\eta _ { N L o S }$ indicate the mean additional losses for LoS and NLoS links, respectively. $f$ is the carrier frequency. According to the Shannon formula, the G2A channel capacity from GU u to T-UAV $v _ { m } ^ { s }$ is

$$
R _ { u , m } ^ { t r } = B _ { u , m } \mathrm { l o g } _ { 2 } \left( 1 + \frac { h _ { u , m } p _ { u } } { B _ { u , m } \sigma ^ { 2 } } \right) , \forall u , m ,\tag{11}
$$

where $B _ { u , m }$ denotes the bandwidth between GU u and T-UAV $v _ { m } ^ { s } , \sigma ^ { 2 }$ represents the average noise power spectrum density, and $p _ { u }$ is the transmission power of GU u. Note that the communication uplink is established only if the transmission rate satisfies the following constraint:

$$
R _ { u , m } ^ { t r } \geq R _ { m i n } ^ { t r } , \forall u , m ,\tag{12}
$$

where $R _ { m i n } ^ { t r }$ represents the threshold of transmission rate.

2) A2A Channel Model: The data collected by T-UAVs should be promptly relayed to the hovering H-UAVs for further processing. The NLoS fading are ignored due to the wider view of the A2A model. Hence, the A2A transmission rate from T-UAV $v _ { m } ^ { s }$ to H-UAV $h _ { s }$ is

$$
R _ { m , s } ^ { t r } = B _ { m , s } \log _ { 2 } \left( 1 + \frac { \eta _ { L o S } p _ { m } ^ { s } } { B _ { m , s } \sigma ^ { 2 } } \right) , \forall m , s ,\tag{13}
$$

where $p _ { m } ^ { s }$ represents the transmission power of T-UAV $v _ { m } ^ { s } ,$ and $B _ { m , s }$ is the bandwidth between T-UAV $v _ { m } ^ { s }$ and H-UAV $h _ { s }$ . Similarly, the transmission rate is expected to satisfy the following constraint

$$
R _ { m , s } ^ { t r } \geq R _ { s , m i n } ^ { t r } , \forall m , s ,\tag{14}
$$

where $R _ { s , m i n } ^ { t r }$ represents the threshold of transmission rate between the T-UAV and H-UAV.

## C. Delay Model

The delay model of T-UAV $v _ { m } ^ { s }$ and related H-UAV $h _ { s }$ is illustrated in Fig. 2. Let binary variable $\gamma _ { u , m , s } ^ { n } \in \{ 0 , 1 \}$ denote the connection relationship between GU u and T-UAV $v _ { m } ^ { s }$ at the hovering location $q _ { m } ^ { s } ( n )$ , i.e.,

$$
\begin{array}{c} \begin{array} { r l } & { \gamma _ { u , m , s } ^ { n } } \\ & { = \left\{ 1 , \mathrm { i f ~ G U ~ } u \mathrm { i s ~ c o n n e c t e d ~ t o ~ T \mathrm { - U A V } ~ } v _ { m } ^ { s } \mathrm { a t ~ } q _ { m } ^ { s } ( n ) , \right. } \\ & { = \left\{ 0 , \mathrm { o t h e r w i s e . } \right.} \end{array}   \end{array}\tag{15}
$$

The implementation process of T-UAV includes two phases: the data collection phase and flight phase. As for the data collection phase, the transmission delay $T _ { u }$ of GU u at hovering position $q _ { m } ^ { s } ( n )$ is calculated as

$$
T _ { u } = \sum _ { s = 1 } ^ { S } \sum _ { m = 1 } ^ { M _ { s } } \sum _ { n = 1 } ^ { N _ { m } ^ { s } } \gamma _ { u , m , s } ^ { n } ( T _ { u , m } + T _ { m , s } ) , \forall u ,\tag{16}
$$

![](images/033ffc132006a001bbe568fc2cac47b4b781232ca52aeb763ff73367309f2161.jpg)  
Fig. 2. Time sequence of T-UAV data collection.

where $T _ { u , m }$ and $T _ { m , s }$ are the transmission delays of G2A and A2A communication links, respectively:

$$
T _ { u , m } = \frac { Q _ { u } } { R _ { u , m } ^ { t r } } , \forall u , m ,\tag{17}
$$

and

$$
T _ { m , s } = \frac { Q _ { u } } { R _ { m , s } ^ { t r } } , \forall u , m , s ,\tag{18}
$$

where $Q _ { u }$ is the data size of GU $u . \ : Q _ { u }$ significantly influences the transmission delay, and as data volume of GUs increases, the transmission power rises proportionally. Nevertheless, due to the disparity in transmission delays of different GUs, the hovering duration $T _ { m } ^ { n }$ of T-UAV $v _ { m } ^ { s }$ on the n-th hovering position should be no less than the longest transmission delay among these GUs, as illustrated in Fig. 2, which is calculated as

$$
T _ { m } ^ { n } = \operatorname* { m a x } _ { u \in \{ 1 , 2 , \cdots , U \} } \left\{ \gamma _ { u , m , s } ^ { n } \left( T _ { u , m } + T _ { m , s } \right) \right\} , \forall s , m , n .\tag{19}
$$

After finishing data collection and relay at position $q _ { m } ^ { s } ( n )$ T-UAV $v _ { m } ^ { s }$ flies to the next hovering position $q _ { m } ^ { s } ( n + 1 )$ . The time cost of T-UAV $v _ { m } ^ { s }$ from $q _ { m } ^ { s } ( n )$ to $q _ { m } ^ { s } ( n + 1 )$ is

$$
T _ { m } ^ { n , n + 1 } = \frac { | | q _ { m } ^ { s } ( n ) - q _ { m } ^ { s } ( n + 1 ) | | } { | | \vartheta | | } , \forall m , n ,\tag{20}
$$

where $| | q _ { m } ^ { s } ( n ) - q _ { m } ^ { s } ( n { + } 1 ) | |$ | represents the Euclidean distance between $q _ { m } ^ { s } ( n )$ and $q _ { m } ^ { s } ( n + 1 )$ . ϑ is the uniform velocity of each T-UAV, denoted by $\boldsymbol { \vartheta } = ( \vartheta _ { x } , \vartheta _ { y } , \vartheta _ { z } )$ . Accordingly, it is assumed that all UAVs fly at the same velocity during data collection. Moreover, H-UAV $h _ { s }$ keeps hovering at the position $q _ { s }$ until the last T-UAV $v _ { m } ^ { s }$ complete data collection. Different flight velocities affect the flight time of T-UAVs, thereby influencing the flight energy consumption of the entire UAV swarm. In this paper, we focus on optimizing the multiobjective problem under the same flight velocity. Thus, the time cost of H-UAV $h _ { s } ,$ consisting of all the following T-UAVs from initial hovering point $q _ { s }$ to the last hovering point $q _ { m } ^ { s }$ , is calculated as

$$
T _ { s } = \operatorname* { m a x } _ { m \in \{ 1 , 2 , \cdots , M _ { s } \} } \left\{ \sum _ { n = 1 } ^ { N _ { m } ^ { s } } T _ { m } ^ { n } + \sum _ { n = 0 } ^ { N _ { m } ^ { s } - 1 } T _ { m } ^ { n , n + 1 } \right\} , \forall s .\tag{21}
$$

In summary, variable $\gamma _ { u , m , s } ^ { n } = 1$ can force T-UAV $v _ { m } ^ { s }$ to hover at $q _ { m } ^ { s } ( n )$ until the GU’s data is delayed. Therefore, to minimize the transmission delay $T _ { u } .$ , we can adopt the trajectory design, by optimizing hovering positions $q _ { m } ^ { s } ( n )$ to reduce hovering durations $T _ { u , m }$ in (17), and sequencing waypoints $\phi _ { m } ^ { s }$ to reduce flight durations in (20).

## D. Energy Consumption Model

Evaluating the energy consumption of UAV swarms and GUs is crucial in assessing the performance of AAN data collection. Therefore, we present the energy consumption models of UAV swarms and GUs, respectively.

1) Energy Consumption of UAV Swarms: The energy consumption of UAVs is mainly composed of the propulsion and communication [27]. As for the T-UAV, the energy consumption primarily consists of three components: the flight energy, hovering energy, and communication energy. Specifically, the energy consumption $E _ { m }$ of the T-UAV $v _ { m } ^ { s }$ during the data collection task is calculated as

$$
E _ { m } = E _ { m } ^ { t r } + E _ { m } ^ { h o v } + E _ { m } ^ { f l y } , \forall m ,\tag{22}
$$

where $E _ { m } ^ { t r }$ denotes the relay energy consumption of T-UAV $v _ { m } ^ { s }$

$$
E _ { m } ^ { t r } = p _ { m } ^ { s } \sum _ { u = 1 } ^ { U } \sum _ { n = 1 } ^ { N _ { m } ^ { s } } \gamma _ { u , m } ^ { n } T _ { m , s } , \forall m , s .\tag{23}
$$

wherein, $p _ { m } ^ { s }$ is the transmission power of T-UAV $v _ { m } ^ { s }$ . Further, $E _ { m } ^ { h o v }$ and $E _ { m } ^ { f l y }$ represent the hovering and flight energy consumption of T-UAV $v _ { m } ^ { s }$ , respectively. Moreover, we leverage the successive-hover-fly model for the UAV, i.e., T-UAV is unable to communicate with either GUs or the H-UAV during the flight. Considering the 3D scenario, the energy consumption models for horizontal and vertical movements of the UAV are different. Hence, the power consumption for the UAV flying in a straight-and-level manner [28] with the horizontal velocity $\begin{array} { r } { \vartheta _ { x , y } = ( \vartheta _ { x } , \vartheta _ { y } ) } \end{array}$ is calculated as

$$
\begin{array} { l } { \displaystyle P _ { f l y } ( | | \vartheta _ { x , y } | | ) = P _ { 0 } \left( 1 + \frac { 3 | | \vartheta _ { x , y } ^ { 2 } | | } { \mathbb { U } _ { t i p s } ^ { 2 } } \right) } \\ { \displaystyle \qquad + P _ { 1 } \left( \sqrt { 1 + \frac { | | \vartheta _ { x , y } ^ { 4 } | | } { 4 v _ { 0 } ^ { 4 } } } - \frac { | | \vartheta _ { x , y } ^ { 2 } | | } { 2 v _ { 0 } ^ { 2 } } \right) ^ { \frac 1 2 } } \\ { \displaystyle \qquad + \frac 1 2 d _ { 0 } \rho _ { 0 } s _ { 0 } A _ { 0 } | | \vartheta _ { x , y } ^ { 3 } | | , } \end{array}\tag{24}
$$

where $P _ { 0 }$ and $P _ { 1 }$ denote the blade profile power and induced power in hovering status, respectively. $\mathbb { U } _ { t i p s }$ is the tip speed of the rotor blade, and $v _ { 0 }$ represents the mean rotor induced velocity. $d _ { 0 }$ is the fuselage drag ratio, $\rho _ { 0 }$ is the air density, $s _ { 0 }$ is the rotor solidity, and $A _ { 0 }$ is the rotor disc area. Further, when ϑ is 0, the hovering power consumption can be calculated as

$$
P _ { h o v } = P _ { 0 } + P _ { 1 } .\tag{25}
$$

The vertical flight power consumption of the T-UAV is

$$
P _ { v e r } ( | | \vartheta _ { z } | | ) = W \mathbf { g } | | \vartheta _ { z } | | ,\tag{26}
$$

where W is the mass of the UAV, g is the gravitational acceleration, and $\vartheta _ { z }$ is the UAV vertical velocity. Thus, $E _ { m } ^ { h o v }$ and $E _ { m } ^ { f l y }$ can be respectively calculated as

$$
E _ { m } ^ { h o v } = P _ { h o v } \sum _ { n = 1 } ^ { N _ { m } ^ { s } } T _ { m } ^ { n } , \forall m ,\tag{27}
$$

and

$$
E _ { m } ^ { f l y } = ( P _ { f l y } ( | | \vartheta _ { x , y } | | ) + P _ { v e r } ( | | \vartheta _ { z } | | ) ) \sum _ { n = 0 } ^ { N _ { m } ^ { s } - 1 } T _ { m } ^ { n , n + 1 } , \forall m\tag{28}
$$

Furthermore, H-UAV $h _ { s }$ remains hovering at the deployment point $q _ { s }$ during the data collection. Hence, the energy consumption of H-UAV $h _ { s }$ is calculated as

$$
E _ { s } = P _ { h o v } T _ { s } , \forall s .\tag{29}
$$

2) Energy Consumption of GUs: Based on the G2A channel model, the energy consumption $E _ { u }$ of GU u is mainly for data transmission to T-UAV $v _ { m } ^ { s }$ , which is calculated as

$$
E _ { u } = p _ { u } \sum _ { s = 1 } ^ { S } \sum _ { m = 1 } ^ { M _ { s } } \sum _ { n = 1 } ^ { N _ { m } ^ { s } } \gamma _ { u , m , s } ^ { n } T _ { u , m } , \forall u ,\tag{30}
$$

where $p _ { u }$ is the transmission power of GU u.

## E. Problem Formulation

We formulate the USDC-MOP to cooperatively minimize the total energy consumption of UAVs swarms, the energy consumed by GUs, and transmission delay of GUs, by jointly optimizing the deployment of UAV swarms $q _ { s } = \{ q _ { s } , \forall s \}$ the number of T-UAVs in UAV swarms $M _ { s } = \{ M _ { s } , \forall s \}$ the trajectory path of T-UAVs $\textbf { \Phi } = ~ \{ \phi _ { m } ^ { s } , \forall s , m \}$ , as well as the transmission power $P = \{ p _ { u } , p _ { m } ^ { s } , \forall u , s , m \}$ of GUs and T-UAVs. Further, the connection variable set is $\gamma =$ $\{ \gamma _ { u , m , s } ^ { n } , \forall u , m , s , n \}$ . Thus, all variables of the problem are summarized as $\mathbb { A } = \{ q _ { s } , M _ { s } , \Phi , P , \gamma \}$ [29], and three optimization objectives are illustrated as

$$
\left\{ \begin{array} { r l } { f _ { 1 } \left( \mathbb { A } \right) = } & { { } \displaystyle \sum _ { s = 1 } ^ { S } { \bigg ( } E _ { s } + \sum _ { m = 1 } ^ { M _ { s } } E _ { m } { \bigg ) } , } \\ { f _ { 2 } \left( \mathbb { A } \right) = } & { { } \displaystyle \frac { 1 } { U } \sum _ { u = 1 } ^ { U } E _ { u } , } \\ { f _ { 3 } \left( \mathbb { A } \right) = } & { { } \displaystyle \frac { 1 } { U } \sum _ { u = 1 } ^ { U } T _ { u } . } \end{array} \right.\tag{31}
$$

wherein, $f _ { 1 } ( \mathbb { A } )$ is the total energy consumption of the UAV swarms (TEU), which is critical for evaluating the effectiveness of the UAV swarms assisted data collection. $f _ { 2 } ( \mathbb { A } )$ represents the average energy consumption of GUs (AEG). $f _ { 3 } ( \mathbb { A } )$ is the average transmission delay of GUs (ADG). The total objective of the USDC-MOP is to simultaneously minimize TEU, AEG, and ADG, which is formulated as

$$
\begin{array} { r l } { { \bf { P 0 } } : } & { \displaystyle { \operatorname* { m i n } _ { \mathbb { A } } ~ F ( \mathbb { A } ) } = [ { f _ { 1 } } ( \mathbb { A } ) , { f _ { 2 } } ( \mathbb { A } ) , { f _ { 3 } } ( \mathbb { A } ) ] } \\ & { \mathrm { ~ s . t . ~ } ( 1 ) , ( 2 ) , ( 1 2 ) , ( 1 4 ) , } \\ & { \displaystyle \quad \sum _ { s = 1 } ^ { S } \sum _ { m = 1 } ^ { M _ { s } } \sum _ { n = 1 } ^ { N _ { m } ^ { s } } \gamma _ { u , m , s } ^ { n } = 1 , \forall u , } \end{array}\tag{32a}
$$

![](images/2cfbb17966a52f65505d1c1df3664a832bd4f3c9ef44065a5c915f3a2215d639.jpg)  
Fig. 3. Overview of the designed algorithms.

$$
\sum _ { u = 1 } ^ { U } \gamma _ { u , m , s } ^ { n } \leq U _ { m a x } , \forall s , m , n ,\tag{32b}
$$

$$
T _ { u } \le T _ { u } ^ { \operatorname* { m a x } } , \forall u ,\tag{32c}
$$

$$
\gamma _ { u , m , s } ^ { n } \in \{ 0 , 1 \} , \forall u , m , n ,
$$

$$
q _ { s } \in \Theta , \forall s ,\tag{32d}
$$

(32e)

$$
\phi _ { m } ^ { s } \in \Psi _ { m } ^ { s } , \forall s , m , n ,\tag{32f}
$$

$$
p _ { u } \in \left[ P _ { u } ^ { \operatorname* { m i n } } , P _ { u } ^ { \operatorname* { m a x } } \right] , \forall u ,\tag{32g}
$$

$$
p _ { m } ^ { s } \in \left[ P _ { m } ^ { \operatorname* { m i n } } , P _ { m } ^ { \operatorname* { m a x } } \right] , \forall s , m .\tag{32h}
$$

Wherein, constraint (32a) specifies that each GU can only establish the connection with one T-UAV at one hovering location $q _ { m } ^ { s } ( n )$ , and (32b) indicates that each T-UAV can simultaneously serve $U _ { m a x }$ GUs. Constraint (32c) denotes the maximum tolerated delay $T _ { u } ^ { m a x }$ of GU $u .$ The maximum tolerated delay $T _ { u } ^ { m a x }$ varies across GUs depending on their time-sensitive nature, which imposes additional constraints on the coverage capability and data collection efficiency of UAV swarms. Constraints (32e) restricts the deployment spatial range of H-UAVs and T-UAVs, respectively. Constraint (32f) limits the trajectory path according to the set of all visiting sequences $\Psi _ { m } ^ { s }$ of T-UAV $v _ { m } ^ { s }$ . Constraints (32g) and (32h) indicate the range of transmit power for GU u and T-UAV $v _ { m } ^ { s } .$ , respectively.

Due to the binary connections variable between GUs and T-UAVs, the integer variable for the allocation of T-UAVs, and the non-linear form of the objective functions, problem P0 is an MINLP problem [30], [31], which is generally NP-hard to solve [32]. Furthermore, these three optimization objective functions in P0 must be optimized simultaneously, and a balanced trade-off exists among these objectives, making P0 more intractable to figure out. Therefore, multi-objective optimization algorithms are regarded as the preferred algorithms for solving MOPs. However, P0 is an MOP with various discrete and continuous variables due to the the existence of integer variables $M _ { s } , \gamma$ and $\Phi ,$ and thus, we simplify the original P0 with the Voronoi diagram and Fermat points based pre-deployment method and propose the INS-WOA to handle the transformed USDC-MOP.

## IV. ALGORITHM DESIGN

To tackle P0 efficiently, we present two sequential algorithms, as depicted in Fig. 3. Wherein, Algorithm 1 is designed for the pre-deployment of UAV swarms, in which the Kmeans and Voronoi diagram based area division method and Fermat point based connection method are proposed to obtain the key variables of the pre-deployment positions $\pmb { q } _ { s }$ of swarms, number of T-UAVs $M _ { s }$ assigned to s-th UAV swarm, and connections $\gamma .$ . Thus, the original problem P0 can be transformed into P1 with variables of {Φ, P }, which is a small-scale MOP. Then, we propose the INS-WOA to deal with P1 via introducing a greedy selection mechanism, and obtain the Pareto solutions set.

Algorithm 1 Pre-Deployment of UAV Swarms   
Input: Locations of GUs U, number of UAV swarms $S ,$ and   
number of total T-UAVs M.   
1 Initialize $M _ { s } = 0 , \gamma _ { u , m , s } ^ { n } = 0 _ { : }$ , and maximum number of   
iterations $I _ { m a x } .$   
2 Cluster U into M clusters using K-means method to obtain   
cluster centers $\mathcal { C } = \{ C _ { 1 } , C _ { 2 } , \cdot \cdot \cdot , C _ { M } \}$   
3 Construct Voronoi diagram W using centers $\mathcal { C }$ to obtain   
the set of Voronoi subregions $\mathcal { L } = \{ L _ { 1 } , L _ { 2 } , \cdot \cdot \cdot , L _ { M } \}$ and   
intersections of diagrams $\Omega = \{ \omega _ { 1 } , \omega _ { 2 } , \cdot \cdot \cdot , \omega _ { \varsigma } \}$   
4 Select $\pmb { q } _ { s }$ from the set of intersections Ω and obtain the   
$M _ { s }$ due to constraints (1) and (2).   
5 for $s = 1 , 2 , \cdots , S$ do   
6 for $m = 1 , 2 , \cdots , M _ { s }$ do   
7 for $n = 1 , 2 , \cdots , N _ { m } ^ { s }$ do   
8 Generate Fermat points $\mathcal { F } _ { m } ^ { s } ( n )$ according to and   
connect the GU u to $\mathrm { T - U A V } \ v _ { m } ^ { s }$ at the hovering   
location $q _ { m } ^ { s } ( n )$ , i.e., $\gamma _ { u , m , s } ^ { n } ~ = ~ 1$ according to   
constraints (32a) and (32b).   
9 end for   
10 end for   
11 end for   
Output: Voronoi diagram W, pre-deployment positions of   
UAV swarms $\mathbf { \delta } \mathbf { q } _ { s } ,$ , number of T-UAVs $M _ { s }$ assigned to each   
UAV swarm, and connection relationships γ.

## A. Pre-Deployment Algorithm for UAV Swarms

Generally, the effective deployment of UAV swarms can significantly enhance the efficiency of data collection. However, it is intricate to select the deployment locations $\pmb { q } _ { s }$ from the large task areas $\Theta _ { s } ,$ which seriously enlarges the search space of the algorithm. GUs can be effectively clustered by the K-means algorithm. However, the cluster centers are not the ideal deployment locations for swarms. Therefore, we propose to divide the area based on the GU distributions leveraging the Voronoi diagram, with UAV swarms deployed at the intersections of diagrams, i.e., $\Omega = \{ \omega _ { 1 } , \omega _ { 2 } , \cdot \cdot \cdot , \omega _ { \varsigma } \}$ where $\omega _ { S }$ denotes the intersection of the Voronoi diagram. Then, we can assign $M _ { s }$ T-UAVs to the s-th UAV swarm, and the inner T-UAVs are dispatched to their respective subregions to complete data collection. As supplementary, the Voronoi diagram is a widely used partitioning mechanism in mathematics, computational geometry, and spatial analysis [33]. It can divide a plane or space into several regions, where each point within a region is closer to a specific point (referred to as the generator or seed point). Such partitioning is based on the nearest neighbor relationships. Therefore, we construct a two-dimensional (2D) Voronoi diagram based on K-means method for GUs partitions.

Besides, constraint (32a) illustrates that T-UAVs are required to complete the data collection tasks for all GUs. Since we have already determined the deployment locations of UAV swarms and the GUs that each T-UAV needs to serve, then we should determine at which specific hovering positions the T-UAVs establish connections with GUs. However, we are unable to determine the specific locations of the hovering points of T-UAVs. Fermat points [34] can ensure a shortest sum distance from the hovering point to vertices in a Delaunay triangle constructed by GUs. Therefore, we deploy the method of generating Fermat points to represent the pre-deployment hovering positions and establish connection relationships γ with the GUs.

![](images/e34d53a87954ac8faee2bc714ee9496dc35ae6490efc68debccabcdc831dc120.jpg)  
Fig. 4. Area partitioning based on the Voronoi diagram, including the connection relationship between the Fermat points and GUs.

In detail, the pre-deployment of UAV swarms is presented in Algorithm 1. Firstly, we cluster the GUs U into M clusters by the K-means method [35] to obtain the seed points C (step 1). Then, we construct the 2D Voronoi diagram W with seed points ${ \mathcal { C } } ,$ as well as the cluster center points (step $^ { 1 ) , }$ as illustrated in Fig. 4. Subsequently, we calculate the 2D coordinates of the Voronoi vertices and obtain the predeployment locations $\pmb { q } _ { s }$ with the fixed deployment altitude of UAV swarms from Ω (step 1). Further, we obtain the number of T-UAVs $M _ { s }$ assigned to different UAV swarms according to constraints (1) and (2). Based on Voronoi diagram $\mathcal { W } ,$ we obtain Voronoi subregions $\mathcal { L } = \{ L _ { 1 } , L _ { 2 } , \cdot \cdot \cdot , L _ { M } \}$ Furthermore, we generate $N _ { m } ^ { s }$ Fermat points within each subregion using the geometric median method. For instance, we can generate the Fermat points for three GUs according to $\begin{array} { r } { \underset { \mathcal { F } _ { m } ^ { s } ( n ) } { \operatorname* { m i n } } \sum _ { u = 1 } ^ { 3 } \| \mathcal { F } _ { m } ^ { s } \left( n \right) - \overset { \cdot } { q } _ { u } \| . \ H _ { n } } \end{array}$ GUs are accordingly assigned to their nearest Fermat points, shown in Fig. 4. Then, the connection relationships $\gamma$ between GUs and T-UAVs are determined. Therefore, the variables $\{ q _ { s } , M _ { s } , \gamma \}$ of P0 are obtained.

## B. INS-WOA Design

After the implementation of Algorithm 1, P0 is turned into P1 as

$$
\begin{array} { r l } { \mathbf { P 1 : } } & { \underset { \mathbb { B } } { \operatorname* { m i n } } \ F ^ { \prime } ( \mathbb { B } ) = [ f _ { 1 } ^ { \prime } ( \mathbb { B } ) , f _ { 2 } ^ { \prime } ( \mathbb { B } ) , f _ { 3 } ^ { \prime } ( \mathbb { B } ) ] } \\ & { \mathrm { ~ s . t . ~ } \quad ( 3 2 c ) , ( 3 2 f ) - ( 3 2 h ) , ( 1 2 ) , ( 1 4 ) . } \end{array}\tag{33a}
$$

Wherein,

$$
\left\{ \begin{array} { l l } { \displaystyle f _ { 1 } ^ { \prime } \left( \mathbb { B } \right) = \sum _ { s = 1 } ^ { S } E _ { s } + \sum _ { m = 1 } ^ { M } E _ { m } , } \\ { \displaystyle f _ { 2 } ^ { \prime } \left( \mathbb { B } \right) = \frac { 1 } { U } \sum _ { u = 1 } ^ { U } p _ { u } T _ { u , \bar { m } } , } \\ { \displaystyle f _ { 3 } ^ { \prime } \left( \mathbb { B } \right) = \frac { 1 } { U } \sum _ { u = 1 } ^ { U } ( T _ { u , \bar { m } } + T _ { \bar { m } , \bar { s } } ) . } \end{array} \right.\tag{34}
$$

are obtained according to the original multi-objective functions in (31), and, $\mathbb { B } ~ = ~ \{ \Phi , P \}$ denotes the set of unresolved variables. Since the connections variable $\gamma$ is obtained by Algorithm 1, m¯ and s¯ in (34) are determined by u. However, P1 is still an MINLP problem, and the traditional mathematical methods are unable to balance multiple conflicting objectives. Hence, to tackle P1 efficiently, we design the INS-WOA to obtain variables Φ and P .

The traditional WOA is a bio-inspired optimization technique [36], drawing inspiration from the unique hunting strategies of humpback whales. WOA updates the positions of solutions by emulating three primary hunting strategies of these whales, including encircling prey, bubble-net attacking method, and search for prey. The NS-WOA incorporates a non-dominated sorting (NDS) mechanism, crowding distance calculation and sorting mechanism to solve complex MOP. However, P1 is intractable to solve with the discrete variable Φ by using the NS-WOA. Thus, we propose an INS-WOA, where a greedy selection mechanism is introduced to select the visiting sequence on the basis of the NS-WOA. The detailed INS-WOA to solve P1 is designed as follows.

1) NDS Mechanism: NDS is a pivotal mechanism for multiobjective optimization. It classifies the solutions into different non-dominated fronts, known as Pareto fronts (PF) [37], where no solution within the same front dominates any other. The mechanism aids WOA in identifying efficient solutions for MOP, ensuring that the obtained solution set balances the performance across all objective functions in P1.

2) Crowding Distance Calculation and Sorting: The purpose is to ensure that the solutions are uniformly distributed along the PF, rather than clustered together in specific regions. The crowding distance for each solution is calculated as the sum of normalized distances between neighboring solutions in each objective dimension. A larger crowding distance indicates a more isolated solution, which is preferred to maintain diversity in the solution set.

3) Encircling Prey: The NS-WOA simulates the behavior of whales encircling their prey by adjusting the positions of individual whales to progressively obtain an optimal solution [38]. This encircling behavior promotes the exploration and exploitation processes within the NS-WOA, facilitating the development of high-quality solutions, i.e.,

$$
\vec { D } = \left| \vec { C } \odot \overrightarrow { X ^ { * } } \left( i \right) - \vec { X } \left( i \right) \right| ,\tag{35}
$$

and

$$
\vec { X } \left( i + 1 \right) = \overrightarrow { X ^ { \ast } } \left( i \right) - \vec { A } \odot \vec { D } ,\tag{36}
$$

where i is the current iteration, $\vec { D }$ denotes the position of the target prey, $\overrightarrow { X ^ { * } } \left( i \right)$ is the position of the best search agent,

denotes the the element-wise multiplication, and || is the absolute value. Further, $\vec { A }$ and $\vec { C }$ are coefficient vectors calculated as

$$
\vec { A } = 2 \vec { a } \odot \vec { r } - \vec { a } ,\tag{37}
$$

and

$$
{ \vec { C } } = 2 \odot { \vec { r } } ,\tag{38}
$$

where parameter $\vec { a }$ is linearly decreased from 2 to 0 during the iterations, governing both the exploration and exploitation phases. Parameter \~r is a random vector uniformly distributed within the range [0, 1]. Let $I _ { m a x } ^ { \prime }$ denote the maximum number of iterations. Accordingly, parameter $\vec { a }$ is updated according to $\vec { a } = 2 ( 1 - i / I _ { m a x } ^ { \prime } )$ . The primary objective of (37) and (38) is to strike a balance between exploration and exploitation for USDC-MOP solutions. Parameter $\vec { r }$ is randomly generated in both equations, and introduces randomness into the position updating mechanism of the agent population. Such randomness helps diversify the search process, preventing premature convergence and ensuring that NS-WOA can effectively explore the solution space while also exploiting unknown solutions.

4) Bubble-Net Attacking: The shrinking encircling and spiral updating position mechanisms are employed concurrently to simulate the bubble-net hunting strategy of humpback whales. To replicate the helix-shaped movement characteristic of humpback whales, the spiral equation defining the relationship between the $\mathrm { p r e y } ^ { \prime } \mathbf { s }$ location and the whale can be expressed as

$$
\begin{array} { r } { \vec { D ^ { \prime } } = \left| \overrightarrow { X ^ { * } } ( i ) - \overrightarrow { X } ( i ) \right| , } \end{array}\tag{39}
$$

in which

$$
\vec { X } ( i + 1 ) = \vec { D ^ { \prime } } \odot e ^ { b l } \odot \cos ( 2 \pi l ) + \vec { X } ^ { * } ( i ) ,\tag{40}
$$

where $^ b$ is a constant used to define the logarithmic spiral shape, and l is a random number within [−1, 1].

Since humpback whales simultaneously swim around their preys in a shrinking circle and follow a spiral-shaped path, the shrinking encircling method and the spiral approach are employed concurrently in the model. To accurately represent this behavior, it is assumed that each mechanism is executed with a probability of 50% as

$$
\vec { X } ( i + 1 ) = \left\{ \begin{array} { l l } { \overrightarrow { X } ^ { \ast } ( i ) - \vec { A } \odot \vec { D } , } & { \mathrm { i f ~ } \tau < 0 . 5 , } \\ { \overrightarrow { D ^ { \prime } } \odot e ^ { b l } \cos ( 2 \pi l ) + \overrightarrow { X } ^ { \ast } ( i ) , } & { \mathrm { i f ~ } \tau \geq 0 . 5 , } \end{array} \right.\tag{41}
$$

where τ is a parameter within [0, 1].

5) Search for Prey: The similar approach used in the shrinking encircling mechanism can be applied to the prey search process. Besides, the coefficient vector $\vec { A }$ with $\vec { A } > 1$ is employed, and the position $\overrightarrow { X ^ { * } } \left( i \right)$ of the best search agent is replaced by the position $\overline { { X _ { r a n d } } }$ of a randomly selected whale from the current population. This adjustment forces the humpback whales to move away from a randomly chosen whale, thereby enabling the NS-WOA algorithm to expand the search space and conduct a global search. The mathematical model for the prey search can be expressed as

$$
\vec { D } = \left| \vec { C } \odot \overrightarrow { X _ { r a n d } } - \vec { X } \left( i \right) \right| ,\tag{42}
$$

and

$$
\vec { X } \left( i + 1 \right) = \overrightarrow { X _ { r a n d } } - \vec { A } \odot \vec { D } .\tag{43}
$$

6) Greedy Selection Mechanism: In the process of solving optimization problems, it usually needs to go through a series of steps, and at each step, multiple choices are faced. However, the greedy selection mechanism makes the nearly optimal choice at present step when solving problems. As for P1, a greedy mechanism is utilized to select the next hovering positions for T-UAVs from the solutions obtained by NS-WOA, with the selection based on minimizing a weighted sum of objective changes, i.e.,

$$
\Delta F ^ { \prime } ( \mathbb { B } ) = \frac { \Delta f _ { 1 } ^ { \prime } ( \mathbb { B } ) } { f _ { 1 } ^ { \prime } ( \mathbb { B } ) ^ { * } } + \frac { \Delta f _ { 2 } ^ { \prime } ( \mathbb { B } ) } { f _ { 2 } ^ { \prime } ( \mathbb { B } ) ^ { * } } + \frac { \Delta f _ { 3 } ^ { \prime } ( \mathbb { B } ) } { f _ { 1 } ^ { \prime } ( \mathbb { B } ) ^ { * } } .\tag{44}
$$

wherein, $\Delta f _ { j } ( { \mathbb { B } } )$ is the predicted change in objective $j ,$ and $f _ { j } ^ { \prime } ( \mathbb { B } ) ^ { * }$ is the current best value.

Algorithm 2 INS-WOA for P1   
Input: Locations of GUs ${ \overline { { \mathcal { U } } } } ,$ Voronoi diagram W, pre  
deployment positions $\mathbf { \delta } q _ { s } ,$ number of assigned T-UAVs   
$M _ { s } ,$ , and connection relationships $\gamma .$   
1 Initialize the population X of whales agents, number of   
whales agent $J _ { m a x } ,$ maximum number of iterations $I _ { m a x } ^ { \prime } ,$   
and the control parameters ${ \vec { A } } , { \vec { C } } , \tau ,$ and l.   
2 for each hovering position $n = 0$ to $N _ { m } ^ { s }$ do   
3 Evaluate the fitness of each whale in the population.   
4 Apply NDS to classify the population into fronts.   
5 Compute crowding distances for solutions within each   
front.   
6 Select the best solution $\mathbf { X } ^ { * }$ based on the rank and   
crowding distance.   
7 for each iteration i = 1 to $I _ { m a x } ^ { \prime }$ do   
8 for each whale $j = 1$ to $J _ { \underline { { m } } a x }$ do   
9 Update parameters A<sup>\~</sup>, C<sup>\~</sup> , τ , and l.   
10 $\mathbf { i f } \ p < 0 . 5$ then   
11 if $| { \vec { A } } | < 1$ then   
12 Update $\vec { D }$ and $\vec { X } \left( i \right)$ due to (35) and (36),   
respectively.   
13 else   
14 Select a random whale $\overrightarrow { X _ { r a n d } }$ and update   
$\vec { D }$ according to (41).   
15 end if   
16 else   
17 Update $\overrightarrow { D ^ { \prime } }$ via (42) and $\vec { X } ( i + 1 )$ via (40).   
18 end if   
19 end for   
20 Repeat steps 3-6.   
21 end for   
22 Select the next hovering position $q _ { m } ^ { s } ( n + 1 )$ for T-UAV   
$v _ { m } ^ { s }$ according to the greedy selection mechanism that   
minimizes (44).   
23 end for   
Output: The PFs solutions Φ, P and MOP objectives $f _ { 1 } ^ { \prime } ( { \mathbb { B } } )$   
f <sup>0</sup> (<sup>B</sup>), f <sup>0</sup> (<sup>B</sup>) of P1.

In detail, the INS-WOA for P1 is presented in Algorithm 2, the input includes locations of GUs U, Voronoi diagram W, the pre-deployment positions of UAV swarms $\mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta } \mathbf { \delta \delta } \mathbf { \delta \delta } \mathbf { \delta \delta } \mathbf { \delta \delta } \delta \mathbf { \delta \delta } \delta \mathbf  \delta \delta \delta \delta \delta \delta \delta \delta \delta \mathbf \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta \delta $ the assigned number of T-UAVs $M _ { s }$ , and connection relationships γ. Then, the related parameters are initialized, encompassing key aspects of the population of whale agents X, along with setting the maximum number of iterations $I _ { m a x } ^ { \prime }$ and the control parameters of the NS-WOA $\vec { A } , \vec { C } , \tau ,$ and l. Subsequently, we utilize the NS-WOA method to determine the continuous variables $q _ { m } ^ { s } ( n )$ and P at each hovering position. Specifically, the fitness of each whale agent in the population is assessed (step 3). The NDS procedure is employed to categorize the population into distinct PFs (step 4). Additionally, the crowding distances are calculated to evaluate the solution diversity (step 5). The best solution $\mathbf { X } ^ { * }$ , which acts as the leader, is selected based on a combination of non-dominated rank and crowding distance (step 6). This selection process ensures that the leader represents a high-quality solution and maintains a diverse set of options for exploration. The main loop iterates over the number of iterations, i.e., $i \in [ 1 , \underline { { I } } _ { m a x } ^ { \prime } ]$ . For each whale agent $j \in [ 1 , J _ { m a x } ]$ , the parameters $\vec { A , C , \tau }$ and l are iteratively updated (step hyperref[algorithm:1]9). Then, the solution $\mathbf { X } ^ { * }$ is updated according to different strategies based on the value of p (steps 11-18). After updating the positions, the fitness of each whale is re-evaluated. The population is sorted into fronts using the NDS process, and the crowding distances are recalculated. The best solution is selected based on the rank and crowding distance (step 20). Repeat the steps 3-6 to update solutions. The above process is repeated until the result converges. Further, the greedy selection mechanism is applied to select the next hovering position $q _ { m } ^ { s } ( n { + } 1 )$ (step 22). Then, we alternatively execute NS-WOA and greedy selection mechanism until obtaining the visiting sequence $\phi _ { m } ^ { s }$ for T-UAV $v _ { m } ^ { s }$ . Finally we obtain the set of NDS {Φ, P }, i.e., the Pareto optimal solutions.

## C. Time Complexity Analysis

The time complexity of Algorithm 1 is related to the number of GUs U and T-UAVs M. The time complexity of K-means method is $\mathcal { O } ( I _ { m a x } U M )$ [35]. The time complexity of constructing the Voronoi diagram with cluster centers is $\mathcal { O } ( M ^ { 2 } )$ . The time complexity of the Fermat points method is $\mathcal { O } ( M N _ { m } ^ { s } H ^ { n } l o g H ^ { n } )$ . In addition, the time complexity of Algorithm 2 is related with three parts: the NS procedure and the WOA algorithm, and the selection greedy mechanism. The time complexity of NS is influenced by the population size $J _ { m a x }$ and the number of objective function dimensions $K ,$ with the worst complexity $\mathcal { O } ( K J _ { m a x } ^ { 2 } )$ . Besides, the time complexity of WOA is mainly dependent on the population size $J _ { m a x }$ and the maximum iteration count $I _ { m a x } ^ { \prime } ,$ which is calculated as $\mathcal { O } ( N _ { m } ^ { s } J _ { m a x } I _ { m a x } ^ { \prime } )$ . The time complexity of greedy selection mechanism is related to the number of hovering positions $N _ { m } ^ { s } ,$ , i.e., $\mathcal { O } ( N _ { m } ^ { s } l o g N _ { m } ^ { s } )$ . Consequently, we can obtain the time complexity of the INS-WOA as $\mathcal { O } ( M N _ { m } ^ { s } l o g N _ { m } ^ { s } ( K J _ { m a x } ^ { 2 } + N _ { m } ^ { s } J _ { m a x } I _ { m a x } ^ { \prime } ) )$ . Moreover, as a hybrid algorithm combining WOA with NDS, INS-WOA maintains the proven convergence properties of WOA [36] while ensuring the Pareto front diversity.

TABLE II PARAMETER SETTING
<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1>α</td><td rowspan=1 colspan=1>9.6</td><td rowspan=1 colspan=1>β</td><td rowspan=1 colspan=1>0.28</td></tr><tr><td rowspan=1 colspan=1>f</td><td rowspan=1 colspan=1>2.4 GHz</td><td rowspan=1 colspan=1> $^ c$ </td><td rowspan=1 colspan=1> $3 \times 1 0 ^ { 8 } \mathrm { m / s }$ </td></tr><tr><td rowspan=1 colspan=1>g</td><td rowspan=1 colspan=1> $9 . 8 ~ \mathrm { m } / \mathrm { s } ^ { 2 }$ </td><td rowspan=1 colspan=1> $Q _ { u , m }$ </td><td rowspan=1 colspan=1>10 Mb</td></tr><tr><td rowspan=1 colspan=1> $P _ { u } ^ { m i n } , P _ { m } ^ { m i n }$ </td><td rowspan=1 colspan=1>0.001 W</td><td rowspan=1 colspan=1> $P _ { m } ^ { m a x }$ </td><td rowspan=1 colspan=1>5W</td></tr><tr><td rowspan=1 colspan=1> $T _ { u } ^ { m a x }$ </td><td rowspan=1 colspan=1>0.4 s</td><td rowspan=1 colspan=1> $P _ { u } ^ { m a x }$ </td><td rowspan=1 colspan=1>1W</td></tr><tr><td rowspan=1 colspan=1> $B _ { u , m }$ </td><td rowspan=1 colspan=1>1.8 MHz</td><td rowspan=1 colspan=1> $B _ { m , s }$ </td><td rowspan=1 colspan=1>5MHz</td></tr><tr><td rowspan=1 colspan=1> $\mathbb { U } _ { t i p s }$ </td><td rowspan=1 colspan=1>120 m/s</td><td rowspan=1 colspan=1> $W$ </td><td rowspan=1 colspan=1>4.25 kg</td></tr><tr><td rowspan=1 colspan=1> $A _ { 0 }$ </td><td rowspan=1 colspan=1> $0 . 5 ~ \mathrm { m ^ { 2 } }$ </td><td rowspan=1 colspan=1> $v _ { 0 }$ </td><td rowspan=1 colspan=1>0.002 m/s</td></tr><tr><td rowspan=1 colspan=1> $P _ { 0 }$ </td><td rowspan=1 colspan=1>99.66 W</td><td rowspan=1 colspan=1> $P _ { 1 }$ </td><td rowspan=1 colspan=1>120.16 W</td></tr><tr><td rowspan=1 colspan=1> $\rho _ { 0 }$ </td><td rowspan=1 colspan=1> $1 . 2 2 5 \mathrm { k g } / \mathrm { m } ^ { 3 }$ </td><td rowspan=1 colspan=1> $d _ { 0 }$ </td><td rowspan=1 colspan=1>0.48</td></tr><tr><td rowspan=1 colspan=1> $| | \vartheta _ { x , y } | |$ </td><td rowspan=1 colspan=1>15 m/s</td><td rowspan=1 colspan=1> $| | \vartheta _ { z } | |$ </td><td rowspan=1 colspan=1>6 m/s</td></tr><tr><td rowspan=1 colspan=1> $s _ { 0 }$ </td><td rowspan=1 colspan=1>0.0001</td><td rowspan=1 colspan=1> $\sigma ^ { 2 }$ </td><td rowspan=1 colspan=1>-174 dBm/Hz</td></tr><tr><td rowspan=1 colspan=1> $\eta _ { L o S }$ </td><td rowspan=1 colspan=1>0.1</td><td rowspan=1 colspan=1> $\eta _ { N L o S }$ </td><td rowspan=1 colspan=1>20</td></tr></table>

![](images/f0758ed208b1fb1288adcf0da4cbab0757cfe574c6991d6b716ac7596cd3557a.jpg)  
Fig. 5. Deployment and trajectory of UAV swarms obtained by INS-WOA with 60 GUs.

## V. SIMULATION RESULTS AND ANALYSES

We conduct extensive simulations in this section to investigate the performance of the proposed algorithms, using MATLAB R2020b as the simulation platform for validation. The size of the 3D data collection area is set to $2 , 0 0 0 \ \times \ 2 , 0 0 0 \ \times \ 1 2 0 \ \mathrm { \ m ^ { 3 } }$ . Moreover, there are a total of 3 UAV swarms, consisting of 3 H-UAVs and 8 T-UAVs. The flight spatial range of H-UAVs and T-UAVs are set as $\Theta _ { s } \ = \ \{ [ 0 , 2 , 0 0 0 ] , [ 0 , 2 , 0 0 0 ] , 1 2 0 \} \mathrm { { n } }$ and $\Theta _ { m } =$ {[0, 2, 000] , [0, 2, 000] , [30, 100]}m, respectively. Then, the maximum number of served GUs for the T-UAV at one hovering location is limited to $U _ { m a x } = 6 ,$ and each swarm can consist of up to $M _ { m a x } = 3 \ \mathrm { T – U A V s }$ . Furthermore, the maximum tolerated delay $T _ { u } ^ { m a x }$ is set as 0.5s according to the requirements of GUs. The major parameters are summarized in Table II.

The distribution of 60 GUs is depicted in Fig. 4. Algorithm 1 is applied to obtain the deployment positions of UAV swarms, and the number of T-UAVs M<sub>s</sub> assigned to the s-th UAV swarm as well as the trajectory path are shown in Fig. 5. It is observed that 3 H-UAVs are deployed at the intersections of Voronoi diagrams, and 8 T-UAVs are dispatched to collect data from GUs.

![](images/d35617dd845fc4cb18009e7fdce7256604502af3ac051c07553a1e46f5319972.jpg)

Fig. 6. Energy consumption of UAV swarms with different number of GUs.  
![](images/1a20b1b1fab0283f96f9c65c5aaac6fefd8d13244ab408e0db38c21d64f6675b.jpg)  
Fig. 7. Average energy consumption of GUs with different number of GUs.

We evaluate the proposed INS-WOA in terms of performances across all three objectives, i.e., TEU, AEG and ADG, by comparing it with other scheduling MOP algorithms, including the non-dominated sorting genetic algorithm II (NSGA-II) [39], multi-objective grey wolf optimizer (MOGWO) [40], and multi-objective artificial hummingbird algorithm (MOAHA) [41]. In detail, NSGA-II, as a classic multi-objective evolutionary algorithm, has been regarded as a benchmark in the field of multi-objective optimization. Derived from the grey wolf optimizer, MOGWO is a powerful multi-objective swarm intelligence optimization algorithm. As a novel multi-objective optimization algorithm, MOAHA has attracted attentions in recent years due to its unique foraging behavior simulation and excellent balance between the exploration and exploitation. Moreover, with the same size of the UAV swarms, we alter the number U and distribution of GUs to obtain multiple results.

Fig. 6 verifies the total energy consumption of UAV swarms under scenarios with different numbers of GUs for various algorithms. It is obvious that the INS-WOA exhibits a significant performance advantage in terms of TEU solutions. Furthermore, the number of hovering points of T-UAVs N increases with the growth of the number of GUs, which subsequently leads to an increment in the total energy consumption of UAV swarms.

Fig. 7 evaluates the average energy consumption of GUs versus different numbers of GUs for various algorithms. As the number of GUs increases, the energy consumption of GUs in the proposed INS-WOA remains stable at around 0.02 J, which is reduced by 30% compared with the MOGWO and

![](images/7970b9d2fd77cb7f515b6738f19007ccee5ef25c6e24dd21379d63808b5cf11f.jpg)

Fig. 8. Average transmission delay with different number of GUs.  
![](images/fee60b440d9e14f16cf87584fd8ccaa082f3464b79d00cb6e9f263f88d69efcb.jpg)

Fig. 9. Power control of GUs with different objective solutions.  
![](images/faf3eb22c49d3f099e413e80a86688bd4f42b6040098b1395998c759041f535c.jpg)  
Fig. 10. Performance of time complexity under different GUs scales.

NSGA-II methods. This is explained by the fact that INS-WOA demonstrates a distinct advantage in power control to ensure relatively low energy consumption of GUs.

The average transmission delay of GUs is shown in Fig. 8. It is observed that the INS-WOA outperforms other methods in terms of average transmission delay performance under different number of GUs. Therefore, we obtain the conclusion that the INS-WOA method has applicability in optimizing average transmission delay and energy consumption of GUs.

Fig. 9 illustrates the transmission power distribution of 60 GUs under different objective solutions. For the sake of comparison, we standardize and normalize the Pareto solution set, selecting a compromise solution among the three objectives for data analysis. Three objectives are respectively normalized to [0, 1] via the min-max scaling method of $B _ { n o r m } =$ $\frac { B - B _ { m i n } } { B _ { m a x } - B _ { m i n } }$ , where $B _ { n o r m }$ is the normalized solution, B is the original solution. $B _ { m a x }$ and $B _ { m i n }$ are the maximum and minimal solutions, respectively. For the compromise solution, the transmission power of the 80% GUs is controlled within a relatively low range of [0W, 0.5W]. Furthermore, for the TEU solution, the distribution of transmission power is relatively dispersed. However, the power distributions of the AEG and ADG solutions show completely opposite trends. For the AEG solution considering the energy of GUs, the transmission of 70% GUs is below 0.25W . For comparison, the transmission power of 60% GUs is over 0.75W for the ADG solution. It is explained that the energy consumption of GUs increases as the transmission power grows, while the transmission delay decreases due to the increasing transmission speed caused by the power increment.

![](images/1e27d4a8f5c3d1db2a85afbd9bb84a6f7c8dd97f9d3dc483d49ca6762173bf31.jpg)  
(a) Energy consumption of UAV swarms.

![](images/cf3a17495bf1eecf18a55d8e3bfefaeab2bcc3797853138503293c6a4110c1d5.jpg)  
(b) Average energy consumption of GUs.

![](images/b8a0a6f51fe9888d2bc4111d315a0faf0143349f71cf1ea2c962cc2c3938e33c.jpg)  
(c) Average transmission delay of GUs.  
Fig. 11. Comparison of compromise solutions under different algorithms with 60 GUs.

![](images/51bc258713ad2adfa4655ea2dfcd1d77729d4cd814d887d5417f6cd7c315f08f.jpg)  
(a) 3D trajectory with the TEU solution

![](images/3dc94fb1cf0346e0639f3c7958a449218d4376522db7adbd4341be645bb0fa90.jpg)  
(b) 3D trajectory with the AEG solution.

![](images/0f07f32e34ea90b07687e033257d931f4f78d546d3b56bbc000470a3ee913255.jpg)  
(c) 3D trajectory with the ADG solution

![](images/348f42bb8e3ac51889bf95028c1c1b31c215219886f503e51d02ed0ef31c24dc.jpg)  
(d) 2D trajectory with the TEU solution.

![](images/9d1e118d2bb99635dad4124365c700b4eb822f3cf6c99c4e6205ecca6479bee8.jpg)  
(e) 2D trajectory with the AEG solution.

![](images/181981bd70a51319c8cf697ce1f50de939f88c92a7b77a59c91c5c24ca78a171.jpg)  
(f) 2D trajectory with the ADG solution.  
Fig. 12. Deployment and trajectory of UAV swarms.

Fig. 10 provides the time complexity of different algorithms. The INS-WOA algorithm shows obvious superiority by achieving lower time complexity than NSGA-II, MOGWO, and MOAHA. Moreover, as the scale of GUs increases, the time complexity of INS-WOA grows almost linearly, which provides the possibility for applications in large-scale scenarios.

Considering the trade-off relationship among multiple objectives in MOPs, Fig. 11 presents the results of the three optimization objectives under the compromise solutions of different algorithms. It is observed that the proposed algorithm can achieve relatively satisfied results in all three optimization objectives simultaneously under different scenarios, essentially in the first two objectives illustrated in Fig. 11(a) and Fig. 11(b). However, as shown in Fig. 11(c), for the optimization objective of transmission delay, the INS-WOA method fails to reach the optimal solution. This is accounted for the fact that compared with other algorithms, the compromise solution of the INS-WOA algorithm tends to reduce the energy consumption of UAV swarms and GUs at the cost of transmission delay, so as to achieve the balance and tradeoff among multiple objectives. Further, by comparing Fig. 6 with Fig. 11(a), we find that the TEU solution is significantly superior to the compromise solution in terms of the energy consumption of UAV swarms. Similarly, it is also the case for both the energy consumption and transmission delay of GUs.

Subsequently, Fig. 12 illustrates the deployment and trajectory schematics of the UAV swarms under the three optimization solutions selected from Pareto solutions, respectively. For TEU solution, T-UAVs tend to hover at higher positions to reduce the path length depicted in Fig. 12(a). This occurs because, when executing the TEU solution, T-UAVs hover at higher altitudes to reduce the flight energy consumption. Consequently, GUs should employ increased transmission power to ensure timely data transmission. In contrast, for both AEG and TEU, T-UAVs are expected to fly close to the GUs at lowest hovering altitude 30m to decrease the energy consumption and transmission delay, shown in Fig. 12(b) and Fig. 12(c), respectively.

## VI. CONCLUSION

In this work, we investigated a hierarchical UAV swarms model for large area data collection in 6G AAN. We focused on optimizing the deployment and trajectory of UAV swarms, as well as the power control of GUs and T-UAVs. To tackle the proposed USDC-MOP which simultaneously minimized the total energy consumption of the UAV swarms, the energy consumed by GUs, and the transmission delay of GUs, we proposed two algorithms. Specifically, a pre-deployment method by utilizing the Voronoi diagram and Fermat Points for UAV swarms was presented to deal the original MOP. Then, we proposed the INS-WOA approach with greedy mechanism to tackle the transformed MOP. Extensive simulations were carried out to thoroughly assess the performance and effectiveness of the proposed algorithms in three objectives. Compared with other benchmark algorithms, the proposed algorithm significantly reduced the energy consumption of UAV swarms and transmission delay across different scenarios, with less time complexity.

## REFERENCES

[1] J.-H. Kim, M.-C. Lee, and T.-S. Lee, “Generalized UAV deployment for UAV-assisted cellular networks,” IEEE Trans. Wireless Commun., vol. 23, no. 7, pp. 7894–7910, Jul. 2024.

[2] Z. Jia et al., “Cooperative cognitive dynamic system in UAV swarms: Reconfigurable mechanism and framework,” IEEE Veh. Technol. Mag., vol. 19, no. 3, pp. 90–101, Sep. 2024.

[3] H. Yang, S. Liu, L. Xiao, Y. Zhang, Z. Xiong, and W. Zhuang, “Learning-based reliable and secure transmission for UAV-RIS-assisted communication systems,” IEEE Trans. Wireless Commun., vol. 23, no. 7, pp. 6954–6967, Jul. 2024.

[4] R. G. Ribeiro, L. P. Cota, T. A. M. Euzebio, J. A. Ram´ ´ırez, and F. G. Guimaraes, “Unmanned-aerial-vehicle routing problem with˜ mobile charging stations for assisting search and rescue missions in postdisaster scenarios,” IEEE Trans. Syst., Man, Cybern., Syst., vol. 52, no. 11, pp. 6682–6696, Nov. 2022.

[5] Z. Feng, M. Huang, D. Wu, E. Q. Wu, and C. Yuen, “Multi-agent reinforcement learning with policy clipping and average evaluation for UAV-assisted communication Markov game,” IEEE Trans. Intell. Transp. Syst., vol. 24, no. 12, pp. 14281–14293, Dec. 2023.

[6] Z. Mou, Y. Zhang, F. Gao, H. Wang, T. Zhang, and Z. Han, “Deep reinforcement learning based three-dimensional area coverage with UAV swarm,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 3160–3176, Oct. 2021.

[7] B. Zhu, E. Bedeer, H. H. Nguyen, R. Barton, and J. Henry, “UAV trajectory planning in wireless sensor networks for energy consumption minimization by deep reinforcement learning,” IEEE Trans. Veh. Technol., vol. 70, no. 9, pp. 9540–9554, Sep. 2021.

[8] K. Liu and J. Zheng, “UAV trajectory optimization for time-constrained data collection in UAV-enabled environmental monitoring systems,” IEEE Internet Things J., vol. 9, no. 23, pp. 24300–24314, Dec. 2022.

[9] L. Yan, X. Fang, Y. Fang, L. Hao, Q. Xue, and C. Xu, “KF-LSTM based beam tracking for UAV-assisted mmWave HSR wireless networks,” IEEE Trans. Veh. Technol., vol. 71, no. 10, pp. 10796–10807, Oct. 2022.

[10] S. Zhang, H. Zhang, Z. Han, H. V. Poor, and L. Song, “Age of information in a cellular Internet of UAVs: Sensing and communication trade-off design,” IEEE Trans. Wireless Commun., vol. 19, no. 10, pp. 6578–6592, Oct. 2020.

[11] Z. Jia, M. Sheng, J. Li, D. Niyato, and Z. Han, “LEO-satellite-assisted UAV: Joint trajectory and data collection for Internet of Remote Things in 6G aerial access networks,” IEEE Internet Things J., vol. 8, no. 12, pp. 9814–9826, Jun. 2021.

[12] X. Zhang, C. Liu, and M. Peng, “Three-dimensional trajectory designs for unmanned aerial vehicle-enabled communications with kinematic constraints,” IEEE Trans. Veh. Technol., vol. 71, no. 10, pp. 10910–10922, Oct. 2022.

[13] H. Pan, Y. Liu, G. Sun, J. Fan, S. Liang, and C. Yuen, “Joint power and 3D trajectory optimization for UAV-enabled wireless powered communication networks with obstacles,” IEEE Trans. Commun., vol. 71, no. 4, pp. 2364–2380, Apr. 2023.

[14] X. Yuan, Y. Hu, J. Zhang, and A. Schmeink, “Joint user scheduling and UAV trajectory design on completion time minimization for UAVaided data collection,” IEEE Trans. Wireless Commun., vol. 22, no. 6, pp. 3884–3898, Jun. 2023.

[15] S. Zeng, H. Zhang, B. Di, and L. Song, “Trajectory optimization and resource allocation for OFDMA UAV relay networks,” IEEE Trans. Wireless Commun., vol. 20, no. 10, pp. 6634–6647, Oct. 2021.

[16] C. You and R. Zhang, “Hybrid offline-online design for UAV-enabled data harvesting in probabilistic LoS channels,” IEEE Trans. Wireless Commun., vol. 19, no. 6, pp. 3753–3768, Jun. 2020.

[17] X. Wang, M. Yi, J. Liu, Y. Zhang, M. Wang, and B. Bai, “Cooperative data collection with multiple UAVs for information freshness in the Internet of Things,” IEEE Trans. Commun., vol. 71, no. 5, pp. 2740–2755, May 2023.

[18] C.-W. Fu, M.-L. Ku, Y.-J. Chen, and T. Q. S. Quek, “UAV trajectory, user association, and power control for multi-UAV-enabled energy-harvesting communications: Offline design and online reinforcement learning,” IEEE Internet Things J., vol. 11, no. 6, pp. 9781–9800, Mar. 2024.

[19] Z. Lu, Z. Jia, Q. Wu, and Z. Han, “Joint trajectory planning and communication design for multiple UAVs in intelligent collaborative air–ground communication systems,” IEEE Internet Things J., vol. 11, no. 19, pp. 31053–31067, Oct. 2024.

[20] Z. Feng, D. Wu, M. Huang, and C. Yuen, “Graph-attention-based reinforcement learning for trajectory design and resource assignment in multi-UAV-assisted communication,” IEEE Internet Things J., vol. 11, no. 16, pp. 27421–27434, Aug. 2024.

[21] A. H. M. Jakaria et al., “Trajectory synthesis for a UAV swarm based on resilient data collection objectives,” IEEE Trans. Netw. Service Manage., vol. 20, no. 1, pp. 138–151, Mar. 2023.

[22] J. Wu, C. Luo, Y. Luo, and K. Li, “Distributed UAV swarm formation and collision avoidance strategies over fixed and switching topologies,” IEEE Trans. Cybern., vol. 52, no. 10, pp. 10969–10979, Oct. 2022.

[23] J. He, Z. Jia, C. Dong, J. Liu, Q. Wu, and J. Liu, “UAV swarm deployment and trajectory for 3D area coverage via reinforcement learning,” in Proc. Int. Conf. Wireless Commun. Signal Process. (WCSP), Hangzhou, China, Nov. 2023, pp. 683–688.

[24] H. Hu, Z. Chen, F. Zhou, R. Q. Hu, and H. Zhu, “Computation-efficient grouping, trajectory, and resource allocation for UAV swarm-assisted aerial–ground collaborative computing networks,” IEEE Internet Things J., vol. 11, no. 7, pp. 12510–12525, Apr. 2024.

[25] Z. Jia et al., “Distributionally robust optimization for aerial multiaccess edge computing via cooperation of UAVs and HAPs,” IEEE Trans. Mobile Comput., early access, May 19, 2025, doi: 10.1109/ TMC.2025.3571023.

[26] Y. Zhang, Z. Mou, F. Gao, J. Jiang, R. Ding, and Z. Han, “UAV-enabled secure communications by multi-agent deep reinforcement learning,” IEEE Trans. Veh. Technol., vol. 69, no. 10, pp. 11599–11611, Oct. 2020.

[27] C. Zhan, H. Hu, X. Sui, Z. Liu, and D. Niyato, “Completion time and energy optimization in the UAV-enabled mobile-edge computing system,” IEEE Internet Things J., vol. 7, no. 8, pp. 7808–7822, Aug. 2020.

[28] Y. Zeng, J. Xu, and R. Zhang, “Energy minimization for wireless communication with rotary-wing UAV,” IEEE Trans. Wireless Commun., vol. 18, no. 4, pp. 2329–2345, Apr. 2019.

[29] R. T. Marler and J. S. Arora, “Survey of multi-objective optimization methods for engineering,” Struct. Multidisciplinary Optim., vol. 26, no. 6, pp. 369–395, Apr. 2004.

[30] J. Li, G. Sun, L. Duan, and Q. Wu, “Multi-objective optimization for UAV swarm-assisted IoT with virtual antenna arrays,” IEEE Trans. Mobile Comput., vol. 23, no. 5, pp. 4890–4907, May 2024.

[31] R. S. Burachik, C. Y. Kaya, and M. M. Rizvi, “Algorithms for generating Pareto fronts of multi-objective integer and mixed-integer programming problems,” Eng. Optim., vol. 54, no. 8, pp. 1413–1425, Jun. 2021.

[32] X. Zhu, L. Zhai, N. Li, Y. Li, and F. Yang, “Multi-objective deployment optimization of UAVs for energy-efficient wireless coverage,” IEEE Trans. Commun., vol. 72, no. 6, pp. 3587–3601, Jun. 2024.

[33] A. Andreou, C. X. Mavromoustakis, J. M. Batalla, E. K. Markakis, and G. Mastorakis, “UAV-assisted RSUs for V2X connectivity using Voronoi diagrams in 6G+ infrastructures,” IEEE Trans. Intell. Transp. Syst., vol. 24, no. 12, pp. 15855–15865, Dec. 2023.

[34] L. Lyu, Z. Chu, B. Lin, Y. Dai, and N. Cheng, “Fast trajectory planning for UAV-enabled maritime IoT systems: A Fermat-point based approach,” IEEE Wireless Commun. Lett., vol. 11, no. 2, pp. 328–332, Feb. 2022.

[35] T. M. Hoang, N. M. Nguyen, and T. Q. Duong, “Detection of eavesdropping attack in UAV-aided wireless systems: Unsupervised learning with one-class SVM and K-means clustering,” IEEE Wireless Commun. Lett., vol. 9, no. 2, pp. 139–142, Feb. 2020.

[36] Q.-V. Pham, S. Mirjalili, N. Kumar, M. Alazab, and W.-J. Hwang, “Whale optimization algorithm with applications to resource allocation in wireless networks,” IEEE Trans. Veh. Technol., vol. 69, no. 4, pp. 4285–4297, Apr. 2020.

[37] S. Mishra, A. Mondal, and S. Mondal, “A multi-objective optimization framework for electric vehicle charge scheduling with adaptable charging ports,” IEEE Trans. Veh. Technol., vol. 72, no. 5, pp. 5702–5714, May 2023.

[38] S. Zhang, D. Niu, Z. Zhou, Y. Duan, J. Chen, and G. Yang, “Prediction method of direct normal irradiance for solar thermal power plants based on VMD-WOA-DELM,” IEEE Trans. Appl. Supercond., vol. 34, no. 8, pp. 1–4, Nov. 2024.

[39] H. Pan, Y. Liu, G. Sun, P. Wang, and C. Yuen, “Resource scheduling for UAVs-aided D2D networks: A multi-objective optimization approach,” IEEE Trans. Wireless Commun., vol. 23, no. 5, pp. 4691–4708, May 2024.

[40] J. Tian, D. Yang, X. Zhang, J. Yin, and Q. Zhang, “An intelligent charging scheme for lithium-ion batteries of electric vehicles considering internal attenuation modes,” IEEE J. Emerg. Sel. Topics Power Electron., vol. 12, no. 1, pp. 82–94, Feb. 2024.

[41] W. Zhao, Z. Zhang, S. Mirjalili, L. Wang, N. Khodadadi, and S. M. Mirjalili, “An effective multi-objective artificial hummingbird algorithm with dynamic elimination-based crowding distance for solving engineering design problems,” Comput. Methods Appl. Mech. Eng., vol. 398, Aug. 2022, Art. no. 115223.

![](images/e2054c20e54d547303e160d7ce39573e173901453016a9906dc5e637ed541803.jpg)

Ziye Jia (Member, IEEE) received the B.E., M.S., and Ph.D. degrees in communication and information systems from Xidian University, Xi’an, China, in 2012, 2015, and 2021, respectively. From 2018 to 2020, she was a Visiting Ph.D. Student with the Department of Electrical and Computer Engineering, University of Houston. She is currently an Associate Professor with the Key Laboratory of Dynamic Cognitive System of Electromagnetic Spectrum Space, Ministry of Industry and Information Technology, Nanjing University of Aeronautics and Astronautics,

Nanjing, China. Her current research interests include space-air-ground networks, aerial access networks, UAV networking, resource optimization, and machine learning.

![](images/e1505be85fcf11f13902fcf942c3a988d489558094fe4f1071d0e18b119555d8.jpg)

Jia He is currently pursuing the master’s degree with the College of Electronic and Information Engineering, Nanjing University of Aeronautics and Astronautics, Nanjing, China. His current research interests include aerial access networks, trajectory planning, and resource optimization.

![](images/b576a5d196e164ae02e205dc1043d7e93f786b1c8265171f28c678b4e67e715d.jpg)

Lijun He (Member, IEEE) received the B.S. degree in electronic information science and technology from Anqing Normal University, Anhui, China, in 2013, and the Ph.D. degree in military communications from the State Key Laboratory of ISN, Xidian University, Xi’an, China, in 2020. From September 2018 to September 2019, he was with the University of Toronto, Toronto, ON, Canada, as a Visiting Scholar funded by China Scholarship Council (CSC). From June 2020 to July 2022, he was a Post-Doctoral Researcher with the School of

Software, Northwestern Polytechnical University (NPU), where he was an Associate Professor with the School of Software from July 2022 to September 2024. He is currently an Associate Professor with the School of Information and Control Engineering, China University of Mining and Technology. His current research interests include routing, scheduling, resource allocation, and satellite communications.

![](images/84046bc48d92402ca53f560a6566d297cc7fedcf90eec166e40d16b5fc6e2236.jpg)

Min Sheng (Fellow, IEEE) received the M.S. and Ph.D. degrees in communication and information systems from Xidian University, Shaanxi, China, in 2000 and 2004, respectively. She is currently a Full Professor and the Director of the State Key Laboratory of Integrated Service Networks, Xidian University. Her research interests include mobile adhoc networks, 5G mobile communication systems, and satellite communications networks. She is a fellow of China Institute of Electronics (CIE) and China Institute of Communications (CIC). She was

awarded as a Distinguished Young Researcher from NSFC and a Changjiang Scholar from the Ministry of Education, China.

![](images/432a392db914e25d4dbbc368b1a1a6591c8c0e0c2897f424fadfeffff52c2c65.jpg)

Junyu Liu (Member, IEEE) received the Ph.D. degree in physics from California Institute of Technology in June 2021. He is a Theoretical Physicist working with Liang’s Group as an IBM Post-Doctoral Fellow with the Chicago Quantum Exchange. He has a keen interest in the combination of physics and computing, especially machine learning, and other modern computing technologies. His work encompasses areas such as quantum machine learning, variational quantum circuits, quantum optimization, quantum networks, and quantum sensing.

His research, published in leading journals and conferences like Physical Review Letters, Nature Communications, Physics Review X Quantum, and IEEE, has garnered significant attention in both academia and industry.

![](images/d9eb67baf14aabea7de8e6c5b1d20662e76b15cf17c058918d79fb629b8feb65.jpg)

Qihui Wu (Fellow, IEEE) received the B.S. degree in communications engineering and the M.S. and Ph.D. degrees in communications and information systems from the Institute of Communications Engineering, Nanjing, China, in 1994, 1997, and 2000, respectively. From 2003 to 2005, he was a Post-Doctoral Research Associate with Southeast University, Nanjing. From 2005 to 2007, he was an Associate Professor with the College of Communications Engineering, PLA University of Science and Technology, Nanjing, where he was a Full Professor from 2008 to 2016. From March 2011 to September 2011, he was an Advanced Visiting Scholar with the Stevens Institute of Technology, Hoboken, NJ, USA. Since May 2016, he has been a Full Professor with the College of Electronic and Information Engineering, Nanjing University of Aeronautics and Astronautics, Nanjing. His current research interests include wireless communications and statistical signal processing, with an emphasis on system design of software defined radio, cognitive radio, and smart radio.

![](images/213774e34ea932c34b8d922718f051d8a072e855ae8c62d90011cdeb0a6ee634.jpg)

Zhu Han (Fellow, IEEE) received the B.S. degree in electronic engineering from Tsinghua University in 1997 and the M.S. and Ph.D. degrees in electrical and computer engineering from the University of Maryland, College Park, MD, USA, in 1999 and 2003, respectively. From 2000 to 2002, he was a Research and Development Engineer with JDSU, Germantown, MD, USA. From 2003 to 2006, he was a Research Associate at the University of Maryland. From 2006 to 2008, he was an Assistant Professor at Boise State University, Boise, ID, USA. Currently, he is a John and Rebecca Moores Professor at the Electrical and Computer Engineering Department and the Computer Science Department, University of Houston, Houston, TX, USA. His main research targets on the novel gametheory related concepts critical to enabling efficient and distributive use of wireless networks with limited resources. His other research interests include wireless resource allocation and management, wireless communications and networking, quantum computing, data science, smart grid, carbon neutralization, and security and privacy. He was an AAAS Fellow since 2019 and an ACM Fellow since 2024. He received an NSF Career Award in 2010, the Fred W. Ellersick Prize of the IEEE Communication Society in 2011, the EURASIP Best Paper Award for the Journal on Advances in Signal Processing in 2015, the IEEE Leonard G. Abraham Prize in Communications Systems (Best Paper Award in IEEE JSAC) in 2016, the IEEE Vehicular Technology Society 2022 Best Land Transportation Paper Award, and several best paper awards in IEEE conferences. He is also the Winner of the 2021 IEEE Kiyo Tomiyasu Award (an IEEE Field Award), for outstanding early to mid-career contributions to technologies holding the promise of innovative applications, with the following citation: for contributions to game theory and distributed management of autonomous communication networks. He was an IEEE Communications Society Distinguished Lecturer from 2015 to 2018 and an ACM Distinguished Speaker from 2022 to 2025. He is a 1% Highly Cited Researcher since 2017 according to Web of Science.