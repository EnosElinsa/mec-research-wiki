# Adaptive Digital Twin for UAV-Assisted Integrated Sensing, Communication, and Computation Networks

Bin Li , Member, IEEE, Wenshuai Liu, Wancheng Xie , Ning Zhang , Senior Member, IEEE, and Yan Zhang , Fellow, IEEE

Abstract—In this paper, we study a digital twin (DT)- empowered integrated sensing, communication, and computation network. Specifically, the users perform radar sensing and computation offloading on the same spectrum, while unmanned aerial vehicles (UAVs) are deployed to provide edge computing service. We first formulate a multi-objective optimization problem to minimize the beampattern performance of multi-input multioutput (MIMO) radars and the computation offloading energy consumption simultaneously. Then, we explore the prediction capability of DT to provide intelligent offloading decision, where the DT estimation deviation is considered. To track this challenge, we reformulate the original problem as a multi-agent Markov decision process and design a multi-agent proximal policy optimization (MAPPO) framework to achieve a flexible learning policy. Furthermore, the Beta-policy and attention mechanism are used to improve the training performance. Numerical results show that the proposed method is able to balance the performance tradeoff between sensing and computation functions, while reducing the energy consumption compared with the existing studies.

Index Terms—Digital twin, mobile edge computing, dual function radar and communication, proximal policy optimization.

## I. INTRODUCTION

from end to edge, but also ubiquitous intelligence applications with the features of high-accuracy of sensing and low-latency of computation [1]. Therefore, there is a surge of interest to explore the converging functionalities of sensing, communication, and computation, which is referred to as integrated sensing, communication, and computation (ISCC) [2]. Under ISCC networks, the users first perform radar sensing to obtain multi-view data, and then upload the sensed data to mobile edge computing (MEC) servers to enable the low-latency services.

The performance of ISCC is typically hindered by unfavorable propagation conditions, particularly in disaster-stricken areas [3], remote areas, hot spots, and other scenarios with poor communication conditions [4]. Unmanned aerial vehicle (UAV) has surfaced as a crucial enabling technology for boosting the capacity and wireless coverage owing to its superior ability of high mobility, full maneuverability, and low expense [5]. However, the high-mobility of UAVs may result in a dynamic network environment, thereby leading to increased complexity in facilitating lower energy consumption and real-time computation offloading performance.

Recent research reveals that DT is envisioned as an appealing technology for improving decision-making in optimizing service quality for time-varying wireless networks. This paradigm can create a digital space model to evaluate the state information of entities in the physical networks, and allow for real-time monitoring of the network state [6], [7]. In addition, more powerful AI technologies can be supported by DT to provide users with more timely decisions. Under this architecture, DT can replace the users and edge servers to make offloading decisions in the virtual space in advance, while the computing and communication resources in the physical space can be provided quickly and accurately according to the request of users [8], [9]. In this context, DT serves as a potential solution in 6G network to perceive the time-varying resource supply and demand, as well as achieve intelligent task scheduling and resource allocation, which is of paramount significance to the development of ISCC system.

To fully exploit the potential of employing UAV in ISCC networks, this paper presents the first attempt to introduce DT into ISCC networks to efficiently adjust the multidimensional network resources, and take full advantage of UAVs as edge servers by appropriately designing real-time UAV movement, thereby providing users with communication and computation services. However, the integration of heterogeneous network resources and dynamic information for real-time decision-making and long-term awareness imposes significant challenges in the research of UAV-aided computation offloading. As such, this paper proposes a multiagent deep reinforcement learning (MADRL)-based scheme by considering the characteristics of distributive computation offloading, where DT is adopted to facilitate the centralized training and decentralized execution architecture. The main contributions of this work are summarized as follows.

1) We propose a DT-empowered ISCC network by taking the cooperative relationship between the physical environment and the DT layer into account. Particularly, the users partially deliver their computational tasks to UAVs for edge processing and DT is leveraged to periodically estimate the practical computation requests of users and the operating states of UAV servers, where the mapping deviation of DT is considered.

2) Different from the existing works that either optimize a single objective or a number of objectives via weighted sum, this paper aims to optimize the computation offloading energy consumption and the sensing beampattern gain simultaneously. To effectively address the challenging problem, we reformulate it as a Markov decision process (MDP) and apply the state-of-theart multi-agent proximal policy optimization (MAPPO) method to capture the collaborative policy.

3) To enhance the performance of training and accelerate the convergence speed, we apply Beta distribution and attention mechanism in actor and critic networks, respectively. Via numerical results, the rapid training convergence and effectiveness of our proposed scheme in optimizing the multi-objective problem are verified, while the superior performance of DT depends on the accuracy of DT estimation.

The remainder of this paper is organized as follows. Section II reviews the related work. The system model is described in Section III. The multi-objective optimization problem is formulated in Section IV. The proposed MAPPO algorithm for solving the formulated problem is presented in Section V. In Section VI, the performance of our proposed algorithm is evaluated with detailed discussions. Finally, we conclude this paper in Section VII.

## II. RELATED WORK

The applications of DT in MEC networks have gained growing attention to achieve real-time computing. Specifically, [9] reflected the role of DT in MEC networks to minimize the end-to-end latency, where a joint optimization of transmit power, user association and task offloading is proposed. The authors in [10] considered a stochastic task arrival model in DT-enabled industrial applications and then applied the actorcritic-based DRL algorithm to minimize the long-term energy efficiency. In [11], a DT-assisted intelligent task offloading scheme was proposed and a value-based DRL method was leveraged to minimize the power and time overhead. In [12], the authors proposed a DT-assisted algorithm to manage the resource scheduling and achieve long-term awareness. In distributed networks, [13] utilized an MADRL algorithm to configure the task offloading and resource allocation in a DT-assisted MEC system via accommodating heterogeneous services. Focusing on the flocking motion of UAVs, the authors in [14] used a DT-enabled MADRL framework to achieve higher average reward. However, these works mainly focused on the centralized training at edge servers.

In the literature of ISCC networks, joint resource scheduling has been identified as a crucial factor in enhancing the performance of sensing, communication, and computation. For instance, an energy-efficient design for ISCC networks was proposed in [15], and the computational and communication resources were jointly optimized using an iterative algorithm with the assistance of intelligent reflecting surface. In [16], the authors proposed a non-orthogonal multiple access enabled integrated sensing-communication system, where the communication throughput and effective sensing power are jointly maximized. Aiming at maximizing overall performance and minimizing transmit power simultaneously, the authors of [17] optimized the beamforming design in ISCC networks. As a step forward, the authors of [18] designed a multi-objective problem to minimize the computational energy while optimizing the radar beampattern design in ISCC systems. In [19], the authors investigated the wireless scheduling for ISCC with the aim of maximizing the throughput, while satisfying the heterogeneous requirements on resources. The authors in [20] proposed a deep learning-based approach to predict the beamforming matrix for the sum-rate maximization of vehicular networks. These excellent achievements mainly utilize iterative algorithms to realize the resource allocation in the realm of ISCC.

Despite the aforementioned studies laid an initial foundation on the ISCC networks, they seldom consider the intelligent management of UAV-aided ISCC networks. In contrast to the above research, this paper aims to address this gap by focusing on the DT-empowered ISCC networks with multiple UAV edge servers. Specifically, a distributed training-based method with heterogeneous agents is designed to pursue the dynamically scheduling of the network resources as well as the configuration on sensing, communication, and computation.

## III. SYSTEM MODEL

We consider a DT-empowered ISCC network as shown in Fig. 1, which consists of K users with $N _ { T }$ antennas, M UAVs with $N _ { R }$ antennas, and a control center (e.g., BS). Each user is equipped with dual function system and has wireless communication and radar detection functions at the same time. The user’s radar can sense the surrounding environment and communicate with the UAVs to exchange control information and basic status. Meanwhile, the users will frequently generate computing-intensive tasks and the MEC servers are deployed at UAVs to accelerate the task processing through offloading. The DT layer is deployed at the control center to record the states of users and UAVs (e.g., channel information and service requirements) that facilitates the interaction between users and UAVs and then guides the edge computing service.

![](images/a0b8bff49c4ee57b4911de100f07f7c08924b408949daf41ef4d1dcdb98940aa.jpg)  
Fig. 1. System model of the DT-empowered ISCC networks.

The offloading decision of each task is determined with the support of DT layer in terms of computing ability. Note that a promising method to realize the user’s DFRC is the transmitter shared by communication and radar sensing based on multibeam, where the transmitted signal is the superposition of separately precoded communication symbols and radar waveforms. In addition, the same transmit antennas are shared by signals for sensing and communication.

To facilitate expression and analysis, the user set is defined as $\forall k \in K \triangleq \{ 1 , 2 , \dots , K \}$ and the UAV set is $\forall m \in { \mathcal { M } } \triangleq$ $\{ 1 , 2 , \ldots , M \}$ . The UAVs have a flight period of T, which is divided into sufficiently short time slots with the length of $\delta _ { t } ~ = ~ T / N$ such that the relative positions between UAVs and users are approximately unchanged in a given time slot but different in adjacent time slots. The set of time slots is recorded as $\forall n \in \mathcal { N } \triangleq \{ 1 , 2 , \dots , N \}$ . We use the Cartesian coordinate system to simulate the positions of users and UAVs. Specifically, the time-varying horizontal position of UAV m in time slot n is ${ \bf q } _ { m } [ n ] = [ x _ { m } [ n ] , y _ { m } [ n ] ] ^ { \mathrm { T } }$ , the flying height is H over the ground, and the position of ground user k is ${ \mathbf w } _ { k } =$ $[ x _ { k } , y _ { k } ] ^ { \mathrm { T } }$ . The displacement change of UAVs between different time slots is related to flight speed $\mathbf { v } _ { m } [ n ]$ and acceleration $\mathbf { a } _ { m } [ n ]$ , and the collisions need to be avoided between UAVs, we thus have the following constraints

$$
{ \bf q } _ { m } [ n + 1 ] = { \bf q } _ { m } [ n ] + { \bf v } _ { m } [ n ] \delta _ { t } + \frac { 1 } { 2 } { \bf a } _ { m } [ n ] \delta _ { t } ^ { 2 } ,\tag{1}
$$

$$
\left\| \mathbf { q } _ { i } [ n ] - \mathbf { q } _ { j } [ n ] \ \right\| ^ { 2 } \geq d _ { \operatorname* { m i n } } ^ { 2 } ,\tag{2}
$$

where $d _ { \mathrm { m i n } }$ is the minimum safety distance between UAVs.

## A. Modeling of DT-Empowered ISCC Network

In this paper, the DT-empowered ISCC network consists of two types of entities, i.e., the users and the UAVs. To maintain the virtual twins, the users and the UAVs will upload the critical information of themselves to the DT layer at control center. Although DT model represents the operating state of the real network as accurately as possible, there are still mapping errors due to the limitations of the DT modeling method and the acquisition of modeling data. In addition, the information transmission randomness of wireless networks will further increase the mapping errors.

For each user k, the virtual twin needs to record its task information and location, which can be characterized by

$$
\begin{array} { r } { \mathrm { D T } _ { k } ^ { u } [ n ] = \Big \{ \mathbf w _ { k } , \Omega _ { k } [ n ] , \tilde { f } _ { k } [ n ] \Big \} , } \end{array}\tag{3}
$$

where $\tilde { f } _ { k } [ n ]$ denotes the estimated current computational resource for user k to execute the task at time slot $n , \Omega _ { k } [ n ]$ is the computational task information of users, which will be elaborated in Section III-C.

For each UAV, the DT needs to reflect its scheduling of service, involving the allocation of resource and motivation status. Thus, the virtual twin of UAV m can be characterized by

$$
\mathrm { D T } _ { m } ^ { U } [ n ] = \Big \{ \{ { \bf q } _ { m } [ n ] , \alpha _ { k , m } , \tilde { f } _ { k , m } [ n ] , \forall k \in \mathcal { K } \Big \} ,\tag{4}
$$

where $\alpha _ { k , m }$ and $\tilde { f } _ { k , m } [ n ]$ are defined as the association factor of the network and the estimated computation resource allocated to user k by UAV m, which will be illustrated in Sections III-B and III-C.

The DT layer creates virtual twins of users and UAVs whose real-time states are synchronized with their counterparts in the physical world for further jointly optimization of heterogeneous resources. Furthermore, DT performs an optimization framework to train MADRL models illustrated in Section V and to download the decisions to the users and UAVs. Based on this fact, the network topology, the system state information, the virtual twins, and the MADRL training information are jointly managed by the DT layer.

## B. Communication Model

For the communication function, user k transmits L symbols at time slot n and the l-th symbol is given as [21]

$$
\begin{array} { r } { { \mathbf { x } } _ { k } [ n , l ] = { \mathbf { W } } _ { r , k } [ n ] { \mathbf { s } } _ { k } [ n , l ] + { \mathbf { W } } _ { c , k } [ n ] { \mathbf { c } } _ { k } [ n , l ] , } \end{array}\tag{5}
$$

where $\mathbf { s } _ { k } [ n , l ] \ \in \ \mathbb { C } ^ { N _ { T } \times 1 }$ is an individual radar waveform, $\mathbf { W } _ { r , k } [ n ] \stackrel {  } { } \in \mathbb { C } ^ { N _ { T } \times N _ { T } }$ denotes the precoding matrix of radar waveforms, $\mathbf { c } _ { k } [ n , l ] ~ \in ~ \mathbb { C } ^ { d \times 1 }$ represents d communication symbols transmitted to UAVs, and $\begin{array} { r l } { \mathbf { W } _ { r , k } [ n ] } & { { } \in } \end{array}$ $\mathbb { C } ^ { N _ { T } \times d }$ is the precoding matrix of communication symbols.

According to [18], we note that the user’s radar signal and communication signal are zero mean, time whitening, and generalized stationary random processes. The user’s radar waveform is not related to the communication signal. The covariance matrix of the same communication signal is unit matrix, and the covariance matrix between different communication signals is zero matrix. The covariance matrix of the same radar waveform is unit matrix, and the covariance matrix of different radar waveforms is zero matrix.

In the considered network, user k uses the radar waveform for object detection, based on which the covariance of its transmission waveform is expressed as

$$
\begin{array} { r l } & { { { \bf { X } } _ { k } } [ n ] = { { \mathbb E } } { \left[ { { { \bf { x } } _ { k } } [ n , l ] { { \bf { x } } _ { k } } [ n , l ] ^ { \mathrm { H } } } \right] } } \\ & { \quad \quad \quad \quad = { { \bf W } _ { r , k } } [ n ] { { \bf W } _ { r , k } ^ { \mathrm { H } } } [ n ] \ + { { \bf W } _ { c , k } } [ n ] { { \bf W } _ { c , k } ^ { \mathrm { H } } } [ n ] , } \end{array}\tag{6}
$$

and the transmission power of user k is expressed as

$$
\begin{array} { r } { \mathrm { t r } ( \mathbf { X } _ { k } [ n ] ) = \mathrm { t r } \Big ( \mathbf { W } _ { r , k } [ n ] \mathbf { W } _ { r , k } ^ { \mathrm { H } } [ n ] \mathbf { \Phi } + \mathbf { W } _ { c , k } [ n ] \mathbf { W } _ { c , k } ^ { \mathrm { H } } [ n ] \Big ) . } \end{array}\tag{7}
$$

In practical implementations, the channel between user k and UAV m is modeled as the Rician fading channel model, which is expressed as follows

$$
\mathbf { H } _ { k , m } [ n ] = \sqrt { \frac { \psi _ { 0 } } { d _ { k , m } ^ { 2 } [ n ] } } \left( \sqrt { \frac { \varsigma } { \varsigma + 1 } } \bar { \mathbf { H } } _ { k , m } [ n ] + \sqrt { \frac { 1 } { \varsigma + 1 } } \hat { \mathbf { H } } _ { k , m } [ n ] \right) ,\tag{8}
$$

where ψ denotes the channel power gain at the reference distance, $d _ { k , m } ^ { 2 } [ n ] \ = \ \| \mathbf { q } _ { m } [ n ] - \mathbf { w } _ { k } \| ^ { 2 } + H ^ { 2 } , \ { \bar { \mathbf { H } } } _ { k , m } [ n ] \ \in$ $\mathbb { C } ^ { N _ { R } \times N _ { T } }$ represents the line-of-sight channel component, $\hat { \mathbf { H } } _ { k , m } [ n ] \in \dot { \mathbb { C } } ^ { \mathbf { N } _ { R } \times N _ { T } }$ represents the non-line-of-sight channel component. $\hat { \mathbf { H } } _ { k , m } [ n ]$ follows the complex Gaussian distribution with 0-means and covariance matrix as the identity matrix, i.e., $\hat { \mathbf { H } } _ { k , m } [ n ] \sim \mathcal { C N } ( 0 , \mathbf { I } _ { N _ { R } } )$ , ς is the Rician factor specifying the power ratio.

The signal received by UAV m from user k can be expressed as

$$
\begin{array} { l } { { \displaystyle { \bf y } _ { k , m } [ n ] = \alpha _ { k , m } { \bf H } _ { k , m } [ n ] { \bf x } _ { k } [ n , l ] } } \\ { ~ + \displaystyle { \sum _ { i = 1 , i \neq k } ^ { K } \sum _ { j = 1 } ^ { M } \alpha _ { i , j } { \bf H } _ { i , j } [ n ] { \bf x } _ { i } [ n , l ] + { \bf z } [ n , l ] } } \\ { ~ = \alpha _ { k , m } { \bf H } _ { k , m } [ n ] \mathbf { W } _ { e , k } [ n ] { \bf x } _ { k } [ n , l ] } \\ { { \displaystyle ~ + \sum _ { i = 1 } ^ { K } \sum _ { j = 1 } ^ { M } \alpha _ { i , j } { \bf H } _ { i , j } [ n ] { \bf W } _ { r , i } [ n ] { \bf s } _ { 1 } [ n , l ] } } \\  { ~ + \displaystyle { \sum _ { i = 1 , i \neq k } ^ { K } \sum _ { j = 1 } ^ { M } \alpha _ { i , j } { \bf H } _ { i , j } [ n ] { \bf W } _ { e , i } [ n ] { \bf e } _ { 1 } [ n , l ] + { \bf z } [ n , l ] } . } \end{array}\tag{9}
$$

where $\mathbf { z } [ n , l ] \sim \mathcal { C N } ( 0 , \sigma _ { c } ^ { 2 } \mathbf { I } _ { N _ { k } } )$ and $\sigma _ { c } ^ { 2 }$ is the noise power. The signal-to-interference-plus-noise ratio can be calculated as

$$
\mathbf { \Gamma } \mathbf { { r } } _ { k , m } [ n ] = \mathbf { H } _ { k , m } [ n ] \mathbf { W } _ { c , k } [ n ] \mathbf { W } _ { c , k } ^ { \mathrm { H } } [ n ] \mathbf { H } _ { k , m } ^ { \mathrm { H } } [ n ] \mathbf { N } _ { k , m } ^ { - 1 } [ n ] ,\tag{10}
$$

where

$$
\mathbf { N } _ { k , m } [ n ] = \sum _ { i = 1 } ^ { K } \sum _ { j = 1 } ^ { M } \alpha _ { i , j } \mathbf { H } _ { i , j } [ n ] \mathbf { W } _ { r , i } [ n ] \mathbf { W } _ { r , i } ^ { \mathrm { H } } [ n ] \mathbf { H } _ { i , j } ^ { \mathrm { H } } [ n ]
$$

$$
\begin{array} { r l r } { \mathrm { ~ } } & { + \displaystyle \sum _ { i = 1 , i \neq k } ^ { K } \sum _ { j = 1 } ^ { M } \alpha _ { i , j } \mathbf { H } _ { i , j } [ n ] \mathbf { W } _ { c , i } [ n ] \mathbf { W } _ { c , i } ^ { \mathrm { H } } [ n ] \mathbf { H } _ { i , j } ^ { \mathrm { H } } [ n ] } & \\ { \mathrm { ~ } } & { + \sigma _ { c } ^ { 2 } \mathbf { I } _ { N _ { R } } . } & { ( 1 1 ) } \end{array}
$$

It follows from (10) that the transmission rate from user k to UAV m is given by

$$
R _ { k , m } [ n ] = B \log _ { 2 } \operatorname* { d e t } \bigl ( \mathbf { I } _ { N _ { R } } + \mathbf { I } _ { k , m } [ n ] \bigr ) ,\tag{12}
$$

where B is total available bandwidth. As a result, the transmission rate of user k is given by

$$
R _ { k } [ n ] = \sum _ { m = 1 } ^ { M } \alpha _ { k , m } R _ { k , m } [ n ] .\tag{13}
$$

## C. Computation Model

The wealth of sensing data is usually computation-intensive, user k offloads its computation workload to UAV edge server to enable low-latency services. Defining a three tuple $\Omega _ { k } [ n ] =$ $( D _ { k } [ n ] , C _ { k } [ n ] , t _ { k } ^ { \mathrm { m a x } } [ n ] )$ at the beginning of each time slot, where $D _ { k } [ n ]$ is the input data size of the generated computational task, and $C _ { k } [ n ]$ is the average number of CPU cycles required to process unit bit of data in the task, and $t _ { k } ^ { \operatorname* { m a x } } [ n ] ( 0 \leq t _ { k } ^ { \operatorname* { m a x } } [ n ] \leq \delta _ { t } )$ is the allowable maximum delay. We utilize the partial offloading mode and the task can be divided into two parts, where one part with the data size of $L _ { k } ^ { o } [ n ] = \rho _ { k } [ n ] D _ { k } [ n ]$ offloaded to UAV for executing, and the other part with the data size of $L _ { k } ^ { l } [ n ] = ( 1 - \rho _ { k } [ n ] ) D _ { k } [ n ]$ calculated locally. $\rho _ { k } [ n ] ~ ( 0 ~ \leq ~ \ddot { \rho _ { k } } [ n ] ~ \leq ~ 1 )$ is defined as the task-partition factor. In addition, the two parts can be processed simultaneously.

1) Local Computing: It is understood that the DT layer can’t fully represent the state of users and UAVs, especially for CPU frequency [9], [11]. We first express the estimated local computing time of user k as $\begin{array} { r } { \tilde { t } _ { k } ^ { l } [ n ] = \frac { L _ { k } ^ { l } [ n ] C _ { k } [ n ] } { \tilde { f } _ { k } ^ { l } [ n ] } } \end{array}$ , where $\tilde { f } _ { k } ^ { l } [ n ]$ is the estimated value of user k’s CPU frequency. Hence, the gap of local computing time between DT estimation and actual value is given by

$$
\Delta t _ { k } ^ { l } [ n ] = \frac { - L _ { k } ^ { l } [ n ] C _ { k } [ n ] \hat { f } _ { k } ^ { l } [ n ] } { \tilde { f } _ { k } ^ { l } [ n ] \Big ( \tilde { f } _ { k } ^ { l } [ n ] + \hat { f } _ { k } ^ { l } [ n ] \Big ) } .\tag{14}
$$

where $\hat { f } _ { k } ^ { l } [ n ]$ is the estimated deviation of actual frequency $f _ { k } ^ { l } [ n ] = \ddot { \bar { f } } _ { k } ^ { l } [ n ] + \hat { f } _ { k } ^ { l } [ n ]$

Accordingly, the actual value for local computing time is given by

$$
t _ { k } ^ { l } [ n ] = \tilde { t } _ { k } ^ { l } [ n ] + \Delta t _ { k } ^ { l } [ n ] .\tag{15}
$$

2) Computation Offloading: We define the association factor between user k and UAV m as $\alpha _ { k , m }$ . When user k is associated with UAV m, we have $\alpha _ { k , m } ~ = ~ 1$ , otherwise $\alpha _ { k , m } = 0$ . For user k, the transmission delay in offloading is calculated by $\begin{array} { r } { t _ { k } ^ { o } [ n ] \ = \ \frac { \rho _ { k } [ n ] \ D _ { k } [ n ] } { R _ { k } [ n ] } } \end{array}$ . Denoting the estimated value for allocated frequency of user k by UAV m as $\tilde { f } _ { k , m } [ n ]$ the estimated computing time of UAV m is given by

$$
\tilde { t } _ { k } ^ { e } [ n ] = \frac { L _ { k } ^ { o } [ n ] C _ { k } [ n ] } { \displaystyle \sum _ { m = 1 } ^ { M } \alpha _ { k , m } [ n ] \tilde { f } _ { k , m } [ n ] } .\tag{16}
$$

Similar to the method above, the computing latency gap of UAV m between DT and real value can be calculated as

$$
\Delta t _ { k , m } ^ { e } [ n ] = \frac { - L _ { k } ^ { o } [ n ] C _ { k } [ n ] \hat { f } _ { k , m } [ n ] } { \tilde { f } _ { k , m } [ n ] \Big ( \tilde { f } _ { k , m } [ n ] + \hat { f } _ { k , m } [ n ] \Big ) } .\tag{17}
$$

where $\hat { f } _ { k , m } [ n ]$ is the estimated deviation of actual frequency $f _ { k , m } [ n ] = \tilde { f } _ { k , m } [ n ] + \hat { f } _ { k , m } [ n ]$

Hence, the actual value of edge computing time for user k can be derived by

$$
t _ { k } ^ { e } [ n ] = \tilde { t } _ { k } ^ { e } [ n ] + \sum _ { m = 1 } ^ { M } \alpha _ { k , m } [ n ] \Delta T _ { k , m } ^ { \mathrm { c o m p } } [ n ] .\tag{18}
$$

Based on the above discussions, the total latency imposed by computation offloading is calculated by $t _ { k } ^ { o } [ n ] + t _ { k } ^ { e } [ n ]$

## D. Radar Sensing Model

In this work, the radar receiver of each user can accurately obtain the transmitted communication symbol, and the communication signal can also be utilized for radar sensing. Therefore, the interference imposed by communication signal is negligible with respect to the radar receivers. During a duration for radar pulse repetition, the Doppler frequency shift caused by moving targets is usually assumed to be constant, so the range-Doppler parameters can be fully compensated [18], [22]. According to the radar target, if a far single point target is located at the $\theta _ { k }$ direction, the echo received by user k at time slot n can be written as

$$
\begin{array} { l } { { \displaystyle { \bf { y } } _ { k , r } [ n , l ] = \psi _ { 0 } { \bf { A } } _ { k } ( \theta _ { k } ) { \bf { x } } _ { k } [ n , l ] + \sum _ { i = 1 , i \neq k } ^ { K } { \bf { H } } _ { k , i } { \bf { x } } _ { i } [ n , l ] } \ ~ } \\ { { \displaystyle ~ + \ { \bf { z } } _ { k } [ n , l ] . } \ ~ } \end{array}\tag{19}
$$

Denoting $\mathbf { a } _ { T , k } ( \theta _ { k } ) \ \in \ \mathbb { C } ^ { N _ { T } \times 1 }$ and $\mathbf { a } _ { R , k } ( \theta _ { k } ) \ \in \ \mathbb { C } ^ { N _ { T } \times 1 }$ as the transmit and receive array steering vectors of the radar for user k, respectively, we have $\begin{array} { r l } { \mathbf { A } _ { k } ( \theta _ { k } ) } & { { } = } \end{array}$ ${ \bf a } _ { R , k } ( \theta _ { k } ) { \bf a } _ { T , k } ^ { \mathrm { H } } ( \theta _ { k } )$ . In addition, ω denotes the Doppler frequency shift, ${ \mathbf z } _ { k } [ n , l ]$ denotes the additive white Gaussian noise with ${ \bf z } _ { k } [ n , l ] \sim \bar { \mathcal { C } } \mathcal { N } ( 0 , \sigma _ { R } ^ { 2 } { \bf I } _ { N _ { T } } )$ , and $\mathbf { H } _ { k , i } \in \mathbb { C } ^ { N _ { T } \times N _ { T } }$ is the channel interference from user i to user k. It is noteworthy that $\begin{array} { r c l c r c l } { \mathbf { a } _ { k } ( \theta _ { k } ) } & { = } & { \mathbf { a } _ { T , k } ( \theta _ { k } ) } & { = } & { \mathbf { a } _ { R , k } ( \theta _ { k } ) } & { = } & { } \end{array}$ $[ 1 , e ^ { j \frac { 2 \pi } { \lambda } d _ { k } \sin ( \theta _ { k } ) } , . . . , e ^ { j \frac { 2 \pi } { \lambda } d _ { k } ( N _ { T } - 1 ) \sin ( \theta _ { k } ) } ] ^ { \mathrm { T } }$ , where λ is the antenna spacing of users, $d _ { k }$ is the signal wavelength, and we set $d _ { k } = \lambda / 2$

In the case with multiple users, the signal interference between users imposed by radar affects the performance of radar detection. It is nature to consider the average interference-to-noise ratio (INR) as a constraint to guarantee the quality of the signal received from the radar sensing, based on which the average INR of user k is given by

$$
\begin{array} { l } { \displaystyle \eta _ { k } [ n ] = \frac { \mathbb { E } [ \underset { i = 1 , i \neq k } { K } [ \| \mathbf { H } _ { k , i } \mathbf { x } _ { i } [ n ] \| _ { F } ^ { 2 } ] } { \mathbb { E } [ \| \mathbf { z } _ { k } \| _ { F } ^ { 2 } ] } } \\ { = \frac { \underset { i = 1 , i \neq k } { K } ( \| \mathbf { H } _ { k , i } \mathbf { W } _ { r , i } [ n ] \| _ { F } ^ { 2 } + \| \mathbf { H } _ { k , i } \mathbf { W } _ { c , i } [ n ] \| _ { F } ^ { 2 } ) } { \ L { N } _ { T } \sigma _ { R } ^ { 2 } } . } \end{array}\tag{20}
$$

## E. Energy Consumption Model

1) The Energy Consumption of Users: The effective capacitance coefficient of the CPU of user k is $\kappa _ { 1 }$ . At the time slot n, the user $k \mathrm { { s } }$ energy consumption during local computing is as follows

$$
E _ { k } ^ { l } [ n ] \ = \kappa _ { 1 } f _ { k } ^ { l } [ n ] ^ { 2 } ( 1 - \rho _ { k } [ n ] ) D _ { k } [ n ] C _ { k } [ n ] .\tag{21}
$$

The transmission energy consumption of user k is expressed as

$$
E _ { k } ^ { o } [ n ] = t _ { k } ^ { o } [ n ] \Vert \mathbf { W } _ { c , k } [ n ] \Vert _ { F } ^ { 2 } .\tag{22}
$$

According to the above analysis, the energy consumption of user k yields

$$
E _ { k } [ n ] = E _ { k } ^ { l } [ n ] + E _ { k } ^ { o } [ n ] .\tag{23}
$$

2) The Energy Consumption of UAVs: The effective capacitance coefficient of the CPU of the UAV is $\kappa _ { 2 }$ . When UAV m provides computational service for user k at time slot n, the computing energy is as follows

$$
{ E } _ { m } ^ { e } [ n ] \ = \sum _ { k = 1 } ^ { K } \kappa _ { 2 } \alpha _ { k , m } f _ { k , m } ^ { 2 } [ n ] \ \rho _ { k } [ n ] \ D _ { k } [ n ] \ .\tag{24}
$$

The flight power of UAV m is calculated as

$$
\begin{array} { r } { p _ { m } ^ { \mathrm { f d y } } [ n ] = P _ { 0 } \Bigg ( 1 + \frac { 3 \| \mathbf { v } _ { m } [ n ] \| ^ { 2 } } { U _ { \mathrm { t i p } } ^ { 2 } } \Bigg ) + \frac { 1 } { 2 } d _ { 0 } \rho s A \| \mathbf { v } _ { m } [ n ] \| ^ { 3 } } \\ { + P _ { i } \Bigg ( \sqrt { 1 + \frac { \| \mathbf { v } _ { m } [ n ] \| ^ { 4 } } { 4 v _ { 0 } ^ { 4 } } } - \frac { \| \mathbf { v } _ { m } [ n ] \| ^ { 2 } } { 2 v _ { 0 } ^ { 2 } } \Bigg ) ^ { \frac { 1 } { 2 } } , ~ ( \mathbf { \overline { { \Sigma } } } } \end{array}\tag{25}
$$

where $P _ { 0 }$ is the power of UAV’s blade, $P _ { i }$ is the induced power during hovering, $v _ { 0 }$ is the mean velocity of rotors. $U _ { \mathrm { t i p } }$ is the blade’s tip speed, $d _ { 0 }$ is the fuselage drag ratio, s is the rotor solidity, A is the area of rotors, and $\rho$ denotes the air density.

Then, the flight energy consumption of UAV m is calculated by

$$
E _ { m } ^ { \mathrm { H y } } [ n ] = p _ { m } ^ { \mathrm { f i y } } [ n ] \delta _ { t } ,\tag{26}
$$

and the energy consumption of UAV m at time slot n is expressed as

$$
E _ { m } [ n ] = E _ { m } ^ { \mathrm { f l y } } [ n ] + E _ { m } ^ { e } [ n ] .\tag{27}
$$

## IV. PROBLEM FORMULATION

The proposed ISCC network includes the functions of radar detection, computation offloading, and UAV trajectory planning. Therefore, the corresponding performance indicators and constraints should be clarified.

## A. Radar Beampattern Design

MIMO radar beampattern is an important design index of radar perception in the ISCC system, and high beampattern gain can be achieved in a given beam direction by carefully designing the covariance matrix of the sensing signal. Denoting the covariance matrix of the transmitted waveforms as $\mathbf { R } _ { d , k }$ , and the minimum square error problem is established as follows

$$
\operatorname* { m i n } _ { \mu _ { k } , \mathbf { R } _ { d , k } } \ \sum _ { l = 1 } ^ { L } | \mu _ { k } P _ { d , k } ( \boldsymbol { \theta } _ { l } ) - \mathbf { a } _ { k } ^ { \mathrm { H } } ( \boldsymbol { \theta } _ { l } ) \mathbf { R } _ { d , k } \mathbf { a } _ { k } ( \boldsymbol { \theta } _ { l } ) | ^ { 2 }
$$

$$
\mathrm { s . t . } \quad \mu _ { k } \geq 0 , \forall k \in \mathcal { K } ,\tag{28a}
$$

$$
\mathrm { t r } \big ( \mathbf { R } _ { d , k } \big ) = p _ { \mathrm { m a x } } , \forall k \in \mathcal { K } , n \in \mathcal { N } ,\tag{28b}
$$

$$
\mathbf { R } _ { d , k } \succeq 0 , \mathbf { R } _ { d , k } = \mathbf { R } _ { d , k } ^ { \mathrm { H } } , \forall k \in \mathcal { K } ,\tag{28c}
$$

where $p _ { \mathrm { m a x } }$ is the maximum ISCC power of users, $P _ { d , k } ( \theta _ { l } )$ is the ideal beampattern gain at angle $\theta _ { l } \in [ - \frac { \pi } { 2 } , \frac { \pi } { 2 } ]$ ${ \bf a } _ { k } ( \theta _ { l } )$ denotes the steering vector, $\mu _ { k }$ is a scaling factor, and $\mathbf { R } _ { d , k }$ is user $k \mathrm { { s } }$ desired waveform covariance matrix.

## B. Multi-Objective Optimization

It is clear that the covariance matrix $\mathbf { R } _ { d , k }$ can be designed via solving problem (28). However, the obtained $\mathbf { R } _ { d , k }$ may not be suitable for actual radar design, due to the requirements of computational latency and the average INR of radar receiver. Similar to the previous work [18], [22], we first minimize the constrained Frobeniusnorm square. It is noteworthy that MIMO radars usually work with the maximum available power to enhance the sensing. Specifically, if the functions of ISCC networks focus on radar detection, it is better to reduce the communication transmission power, otherwise the radar sensing power has to be reduced. Furthermore, the energy consumption of users and UAVs is a significant factor to evaluate the expense of the ISCC network, which can be represented by the weighted energy consumption.

Herein, we construct a multi-objective optimization problem (MOOP) by jointly designing the precoding matrix of radar waveform $\mathbf { \bar { W } } _ { r } \triangleq \{ \mathbf { W } _ { r , k } [ n ] , \mathbf { \bar { \Psi } } k \in \mathbf { \bar { K } } , n \in \bar { \mathcal { N } } \}$ , the precoding matrix of communication symbols ${ \cal W } _ { c } \triangleq \{ { \bf W } _ { c , k } [ n ] , \forall k \in \} $ ${ \mathcal { K } } , n \in { \mathcal { N } } \}$ , the association factor of users $\pmb { \alpha } \triangleq \{ \alpha _ { k , m } , \forall k \in$ $\mathcal { K } , m \in \mathcal { M } , n \in \mathcal { N } \}$ , the CPU frequency of users $\tilde { { \pmb f } } _ { i } \triangleq $ $\{ \tilde { f } _ { k } ^ { l } [ n ] , \forall k \in K , n \in \mathcal { N } \}$ , the computational resource allocation of UAVs $\tilde { \pmb { f } } _ { e } \triangleq \{ \tilde { f } _ { k , m } [ n ] , \forall k \in \mathcal { K } , m \in \mathcal { M } , n \in \mathcal { N } \}$ , and the trajectory planning of UAVs $\pmb q \triangleq \{ \mathbf q _ { m } [ n ] , \forall m \in \mathcal { M } , n \in$ $\mathcal { N } \}$ , which is in nature given as

$$
\operatorname* { m i n } _ { W _ { c } , W _ { r } } \ \sum _ { n = 1 } ^ { N } \sum _ { k = 1 } ^ { K } \| \mathbf { X } _ { k } [ n ] - \mathbf { R } _ { d , k } \| _ { F } ^ { 2 } ,
$$

$$
\operatorname* { m i n } _ { \substack { W _ { c } , W _ { r } , q , \tilde { f } _ { i } , \tilde { f } _ { e } , \rho } } \omega \sum _ { n = 1 } ^ { N } \sum _ { m = 1 } ^ { M } E _ { m } [ n ] + \sum _ { n = 1 } ^ { N } \sum _ { k = 1 } ^ { K } E _ { k } [ n ]
$$

$$
\mathrm { s . t . } \alpha _ { k , m } \in \{ 0 , 1 \} , \sum _ { m = 1 } ^ { M } \alpha _ { k , m } \leq 1 , \forall k \in \mathcal { K } ,
$$

$$
m \in { \mathcal { M } } ,\tag{29a}
$$

$$
\mathrm { t r } ( \mathbf { X } _ { k } [ n ] ) = p _ { \mathrm { m a x } } , \forall k \in \mathcal { K } , n \in \mathcal { N } ,\tag{29b}
$$

$$
\eta _ { k } [ n ] \leq \zeta _ { k } , \forall k \in \mathcal { K } , m \in \mathcal { M } ,\tag{29c}
$$

$$
\operatorname* { m a x } \Bigl \{ t _ { k } ^ { l } [ n ] , t _ { k } ^ { o } [ n ] + t _ { k } ^ { e } [ n ] \Bigr \} \le t _ { k } ^ { \operatorname* { m a x } } [ n ] ,
$$

$$
\forall k \in K , n \in N ,\tag{29d}
$$

$$
0 \leq \tilde { f } _ { k } ^ { l } [ n ] \ \leq f _ { k } ^ { \operatorname* { m a x } } , \forall k \in { \mathcal { K } } , n \in { \mathcal { N } } ,\tag{29e}
$$

$$
0 \leq \tilde { f } _ { k , m } [ n ] \leq f _ { m } ^ { \operatorname* { m a x } } ,
$$

$$
0 \leq \sum _ { k = 1 } ^ { K } \alpha _ { k , m } \tilde { f } _ { k , m } [ n ] \leq f _ { m } ^ { \operatorname* { m a x } } ,\tag{29f}
$$

$$
0 \leq \rho _ { k } [ n ] \leq 1 , \forall k \in K , n \in \mathcal N ,\tag{29g}
$$

$$
\| \mathbf { a } _ { m } [ n ] \| \leq a _ { \operatorname* { m a x } } , \| \mathbf { v } _ { m } [ n ] \ \| \leq v _ { \operatorname* { m a x } } ,
$$

$$
\forall n \in { \mathcal { N } } , m \in { \mathcal { M } } ,\tag{29h}
$$

$$
\| \mathbf { q } _ { i } [ n ] \ - \mathbf { q } _ { j } [ n ] \ \| ^ { 2 } \geq d _ { \operatorname* { m i n } } ^ { 2 } , \forall i ,
$$

$$
j \in \mathcal { M } , i \neq j ,\tag{29i}
$$

where ω denotes the non-negative constant weight factor for $\mathrm { U A V } , \zeta _ { k }$ is the maximum tolerable INR level of user $k , f _ { k } ^ { \mathrm { m a x } }$ is the maximum computational resources of user $k , \ f _ { m } ^ { \mathrm { m a x } }$ is the maximum computational resources of $\mathrm { U A V } m ,$ a<sub>max</sub> is the maximum acceleration of UAV $m ,$ and $v _ { \mathrm { m a x } }$ is the maximum flight speed of UAV m, and $\zeta _ { k }$ is the maximum tolerable INR level of user k. Constraint (29a) ensures that the user only associates to at most one UAV. Constraint (29b) specifies the transmission power of the user. Constraint (29c) is the INR level required by user $k .$ Constraint (29d) indicates the tolerable computation delay, which is related to the DT estimation deviations $\tilde { f } _ { k } ^ { l } [ n ]$ and $\mathrm { \bar { \boldsymbol { f } } } _ { k , m } [ { \boldsymbol { n } } ]$ . Constraint (29e) limits the estimated computation resource $\tilde { f } _ { k } ^ { l } [ n ]$ for user k in DT layer. Constraint (29f) limits the estimated computation resource $\tilde { f } _ { k , m } [ n ]$ allocated to user k by UAV m in DT layer. Constraint (29g) is the task-partition factor. Constraint (29h) are the acceleration and speed limitation of UAV. Constraint (29i) denotes the minimum safe distance between UAVs.

## V. DT-DRIVEN MADRL APPROACH

It can be readily derived that problem (29) is a nonlinear and non-convex MOOP with highly-coupled and integer variables. This is very difficult to be solved by traditional offline optimization methods in the presence of time-varying channel conditions [23], [24], [25]. To tackle the challenge of addressing high-dimensional state and action spaces, in this section we consider to design an MAPPO-based training framework because it is capable of involving multiple types of policies to cooperatively and distributively decide the optimization variables.

## A. Modeling of Multi-Agent MDP

Since multiple UAVs and users participate in the network, the optimization problem has the characteristics of distribution in real scenarios. Therefore, our problem can be formulated as a multi-agent MDP. Typically, the elements of MDP involves a global state space S, a global action space A, and the reward function R. In the multi-agent MDP, the state of environment is partially observable to agents, especially in privacy-awared systems and distributed frameworks. Denote the observation of agent $i \in \mathcal { T } \triangleq \{ 1 , 2 , \dots , I \}$ at time step t as $o _ { t } ^ { i } .$ , and thus the global state of environment $s _ { t }$ can be obtained by combining the partial observations of agents. To fully relieve the difficulty of decision-making for agents and pursue the near-optimal solutions, we consider to decompose the general policy on optimization variables into three policies. The global state space and action space can be respectively denoted as ${ \mathcal S } = { \mathcal O } _ { 1 } \times \ldots \times { \mathcal O } _ { I }$ and $\mathcal { A } = \mathcal { A } _ { 1 } \times . . . \times \mathcal { A } _ { I }$ , which are extended as the Cartesian product of observation spaces $\mathcal { O } _ { i }$ and action spaces $\mathbf { \mathcal { A } } _ { i }$ of all the agents. The three types of agents, which corresponding to three types of policies in the multi-agent system, are described as follows:

1) Offloading-Configuration Agents: This type of agents mainly focus on the offloading configuration for tasks. The index set of offloading-configuration agents is defined as $I _ { 1 } \triangleq$ $\{ 1 , 2 , \ldots , K \}$ . To decide the offloading proportion and association to UAVs, they need to observe their task information, locations of themselves and locations of UAVs.

Observation: The observation for offloading-configuration agents is as follows

$$
o _ { t } ^ { k } = \{ k , \mathbf { w } _ { k } [ n ] , \mathbf { q } _ { m } [ n ] , \Omega _ { k } [ n ] , \forall m \in \boldsymbol { M } \} .\tag{30}
$$

Note that each user can only obtain its own location via positioning service, and knows the information of all UAVs since the UAVs act as servers. For the huge difference on values of coordinates and task information, we scale them into [0,1] according to the lower-bounds and upper-bounds of these variables decided by the ground width of region and the distribution of data size. In order to minimize the computational energy, the CPU frequency $\tilde { f } _ { k } [ n ]$ can be simply set and estimated by following equation according to dynamic voltage frequency scaling technology [26]

$$
\tilde { f } _ { k } [ n ] = \operatorname* { m i n } \biggr \{ f _ { k } ^ { \operatorname* { m a x } } , \frac { 1 } { t _ { k } [ n ] } D _ { k } [ n ] C _ { k } [ n ] \biggr \} .\tag{31}
$$

Action: The action for this type of agents should represent the decision variables, and thus can be defined as $a _ { t } ^ { k } = \{ \rho _ { k } [ n ] , \alpha _ { k , m } , \forall m \in \mathcal { M } \}$

For the constraint (29a) on α, we select $\begin{array} { r l } { m _ { k } } & { { } = } \end{array}$ $\arg \operatorname* { m a x } _ { \mathbf { \alpha } , \mathbf { \hat { \alpha } } } \{ \hat { \alpha } _ { k , m } , \forall m \ \in \ \mathcal { M } \}$ as the associated UAV of user m $k ,$ where $\hat { \alpha } _ { k , m }$ is the output value of policy model. In addition, we let $\hat { \rho } _ { k } [ n ] \leq 0$ to represent the fully local computing case for user k at time slot $n ,$ where the range of output ${ \hat { \rho } } _ { k } [ n ]$ can be mapped into $[ - \varepsilon , 1 ]$ with $\varepsilon > 0$ . We then set $\rho _ { k } [ n ] = \alpha _ { k , m _ { k } } = \lceil \hat { \rho } _ { k } [ n ] \hat { \alpha } _ { k , m _ { k } } \rceil ^ { + }$ to ensure the feasibility of action, where $\lceil x \rceil ^ { + } = \operatorname* { m a x } ( 0 , x )$

Reward: The reward function of offloading-configuration agent needs to involve objective and penalty for not satisfying the latency requirements. The energy consumption of users and their associated UAVs need to be decomposed for each user. Thus, the reward of agent k is given by

$$
r _ { t } ^ { k } = - \bar { E } _ { k } ^ { \omega } [ n ] P _ { T , k } ^ { u } ( t ) ,\tag{32}
$$

where

$$
P _ { t , T } ^ { k } = P \Bigg ( \sum _ { \stackrel { m = 1 } { t _ { k } ^ { \operatorname* { m a x } } } [ n ] , t _ { k } ^ { \operatorname* { m a x } } [ n ] \big ) , } ^ { M }  \alpha _ { k , m } \operatorname* { m a x } \Big \{ { t _ { k } ^ { l } [ n ] , t _ { k } ^ { o } [ n ] + t _ { k } ^ { e } [ n ] \Big \} } ,\tag{33}
$$

and we calculate

$$
P ( x , a , b ) = 2 - \exp \Bigl ( - \lceil ( x - a ) / b \rceil ^ { + } \Bigr )\tag{34}
$$

as the exponential penalty function, where

$$
\bar { E } _ { k } ^ { w } [ n ] = \left( \omega \sum _ { m = 1 } ^ { M } \alpha _ { k , m } E _ { m } [ n ] + E _ { k } [ n ] \right)\tag{35}
$$

denotes the average weighted energy consumption of user $k .$ 2) Beampattern-Configuration Agents: In the ISCC network, the users should balance the performance of sensing and communication by deciding the beampatterns for these functions. Denoting the index set of this type of agent as $\mathcal { T } _ { 2 } ~ \triangleq ~ \{ K \ : + \ : 1 , K \ : + \ : 2 , \ldots , 2 K \}$ , we illustrate the MDP elements as follows:

Observation: The effect of beampatterns on objectives are associated with covariance matrix $\mathbf { R } _ { d , k }$ and the relative position between user k and their associated UAV. We define the observation of each beampattern-configuration agent as follows

$$
o _ { t } ^ { K + k } = \{ k , \mathbf { R } _ { d , k } , \mathbf { H } _ { k , m _ { k } } [ n ] , \mathbf { q } _ { m _ { k } } [ n ] , \mathbf { w } _ { k } [ n ] , \boldsymbol { \Omega } _ { k } [ n ] \} .\tag{36}
$$

It is worth noting that deep neural networks are typically not able to address complex values. For complex value $z = a + b \mathrm { j }$ we first transform it into $z = | z | e ^ { \mathrm { j \angle z } }$ . In addition, $| z |$ and $\angle z$ are scaled into [0,1]. For instance, the entries of matrix $\mathbf { R } _ { d , k }$ are rewritten into complex pairs $\{ | z | , \angle z \}$ , where the modular $| z |$ is divided by its trace <sup>p</sup><sub>max</sub>. Furthermore, the modular of complex pairs for $\mathbf { H } _ { k , m _ { k } } [ n ]$ are normalized. Then, the pairs can be concatenated as vectors.

Action: To decide the beampattern for sensing and communication, the agents should give the action as follows

$$
a _ { t } ^ { K + k } = \{ \mathbf { W } _ { c , k } [ n ] , \mathbf { W } _ { r , k } [ n ] \} .\tag{37}
$$

To tackle constraint (29b), the traces of matrices ${ \mathbf W } _ { c , k } [ n ]$ and ${ \mathbf W } _ { r , k } [ n ]$ can be given specifically by the output of neural networks and then be divided by $\operatorname { t r } ( \mathbf { X } [ n ] )$ .

Reward: Since the beampatterns ${ \mathbf W } _ { c , k } [ n ]$ and ${ \mathbf W } _ { r , k } [ n ]$ need to strike a balance between sensing and communication, the reward needs to consider the both functions. However, the part of objective function with respect to ${ \mathbf W } _ { c , k } [ n ]$ is much more sophisticated than that of ${ \mathbf W } _ { r , k } [ n ]$ , and partial observation on channel state of each user sharply increases the difficulty for all agents to jointly provide optimal solution. To pursue a sub-optimal policy on beampatterns, we first evaluate the desired beampatterns for communication ${ \bf R } _ { d , k } ^ { c } [ n ]$ , which have the maximum gain on the horizontal direction from users to the associated UAVs. The ${ \bf R } _ { d , k } ^ { c } [ n ]$ can also be added into input state-vector of neural networks. Therefore, the reward can be designed as

$$
\begin{array} { r l } & { r _ { t } ^ { K + k } = \Big ( 2 - \omega _ { s } \varepsilon _ { s } - ( 1 - \omega _ { s } ) \varepsilon _ { c } \Big ) \cdot } \\ & { ~ \Big ( 2 - P _ { t , T } ^ { k } + P ( \eta _ { k } [ n ] , \zeta _ { k } [ n ] , \zeta _ { k } [ n ] ) \Big ) / 2 , } \end{array}\tag{38}
$$

where

$$
\varepsilon _ { s } = \frac { \Vert \mathbf { X } _ { k } [ n ] - \mathbf { R } _ { d , k } \Vert _ { F } } { \Vert \mathbf { R } _ { d , k } \Vert _ { F } } ,\tag{39}
$$

and

$$
\varepsilon _ { c } = \frac { \| \mathbf { W } _ { c , k } [ n ] - \mathbf { R } _ { d , k } ^ { c } \| _ { F } } { \| \mathbf { R } _ { d , k } ^ { c } \| _ { F } } .\tag{40}
$$

3) UAV Agents: The UAVs are required to control their speed, and allocate the CPU frequency for users. Denoting the index set of UAV agents as $\mathcal { T } _ { 3 } \triangleq \{ 2 K + 1 , 2 K + 2 , \dots , 2 K +$ <sup>M</sup> }, the MDP elements are as follows:

Observation: Each UAV can obtain the location and task information of users served by it. Therefore, the observation can be expressed as

$$
\begin{array} { c } { o _ { t } ^ { 2 K + m } = \{ m , \mathbf q _ { m } [ n ] , \mathbf q _ { - m } [ n ] , \mathbf w _ { k } [ n ] , \boldsymbol \Omega _ { k } [ n ] , \rho _ { k } [ n ] , } \\ { \forall k \in \mathcal K _ { m } \} , } \end{array}\tag{41}
$$

where $\kappa _ { m }$ denotes the users served by UAV m, and −m denotes the indexes in set $\mathcal { M } \backslash \{ m \}$

Action: The UAVs need allocate their CPU frequency to execute users’ tasks, and decide their movement to enhance the fairness of users. Therefore, the actions of users are given by

$$
\begin{array} { r } { a _ { t } ^ { 2 K + m } = \Bigl \{ \mathbf { a } _ { m } [ n ] , \tilde { f } _ { k , m } [ n ] , \forall k \in  { \mathcal { K } } _ { m } \Bigr \} . } \end{array}\tag{42}
$$

Note that the output acceleration from policy model can be expressed as $\hat { \mathbf { a } } _ { m } [ n ] = [ \lVert \mathbf { a } _ { m } [ n ] \rVert , \phi _ { m } [ n ] ]$ , where $\phi _ { m } [ n ]$ is the angular acceleration. The proportion of computational resource with respect to UAV’s available CPU frequency and the proportion allocated for each user can also be represented by a vector with the length of $K { + 1 }$ , where the entries of the users not served by UAV m are multiplied by zero masks. Hence, the CPU frequency mapped from the action can be treated as an estimated value.

Reward: For UAV k, it needs to consider the weighted energy consumption as well as the distance to users in order to enhance the channel gain and fairness. Meanwhile, the collision and flying-out penalty should also be considered. Therefore, we design the reward as follows

$$
r _ { t } ^ { 2 K + m } = ( k _ { 1 } \bar { E } _ { m } ^ { w } [ n ] + k _ { 2 } P ( \| \mathbf { q } _ { m } [ n ] - \frac { 1 } { \vert K _ { m } \vert } \sum _ { k = 1 } ^ { K } \alpha _ { k , m } \mathbf { w } _ { k } [ n ] \| , 
$$

$$
d _ { \mathrm { t h } } , X \bigg ) \bigg ) P _ { t , T } ^ { m } P _ { t , O } ^ { m } P _ { t , C } ^ { m } ,\tag{43}
$$

where $k _ { 1 }$ and $k _ { 2 }$ denote the adjusting factors, $d _ { \mathrm { t h } }$ is the threshold adjusting the distance from UAVs to users, and X is the width of square service region. $\bar { E } _ { m } ^ { w } [ n ]$ is the average energy consumption of UAVs, which is defined as

$$
\bar { E } _ { m } ^ { w } [ n ] = \frac { 1 } { | { \cal K } _ { m } | } \sum _ { k \in { \cal K } _ { m } } \alpha _ { k , m } E _ { k } [ n ] + \varpi _ { m } E _ { m } [ n ] .\tag{44}
$$

The penalties are denoted by $P _ { t , T } ^ { m } , P _ { t , O } ^ { m }$ , and $P _ { t , C } ^ { m }$ respectively, where

$$
P _ { t , T } ^ { m } = \frac { 1 } { \vert \mathcal { K } _ { m } \vert } \sum _ { k \in \mathcal { K } _ { m } } P \Big ( \alpha _ { k , m } \operatorname* { m a x } \Big \{ t _ { k } ^ { l } [ n ] , t _ { k } ^ { o } [ n ] + t _ { k } ^ { e } [ n ] \Big \} ,
$$

$$
t _ { k } ^ { \operatorname* { m a x } } [ n ] , t _ { k } ^ { \operatorname* { m a x } } [ n ] \bigg )\tag{45}
$$

is the penalty for the latency requirements of users served by UAV $m _ { : }$

$$
P _ { t , O } ^ { m } = 1 + \frac { 1 } { v _ { \operatorname* { m a x } } } \| \mathbf { q } _ { m } [ n ] - \mathrm { c l i p } ( \mathbf { q } _ { m } [ n ] , 0 , X ) \|\tag{46}
$$

is the penalty when UAV tries to fly out of the square service region, and

$$
P _ { t , C } ^ { m } = \sum _ { \substack { j = 1 , j \neq m } } ^ { M } P \big ( d _ { \operatorname* { m i n } } , \| \mathbf { q } _ { m } [ n ] - \mathbf { q } _ { j } [ n ] \| , d _ { \operatorname* { m i n } } \big )\tag{47}
$$

is the penalty for disobeying safety distance between UAVs.

## B. DT for MADRL Training Framework

It is widely acknowledged that MAPPO is an on-policy MADRL algorithm with state-of-art performance on various tasks [27], which derives from trust policy optimization under the actor-critic framework. Accordingly, the continuous and discrete actions can be expressed by the output of actor network $\theta _ { u } ,$ , and the state-value function is evaluated by critic network $\omega _ { u }$ . The actor network for u-th type of agents represents the shared policy of the homogeneous agents, which is denoted as $\pi _ { \boldsymbol { \theta } _ { u } }$

For the convenience of deployment in distributed DTempowered ISCC networks, the centralized training and decentralized executing (CTDE) framework is utilized as shown in Fig. 2, where the agents execute actions with their actor networks, and train the centralized critic networks for each policy. Moreover, the rewards typically need the information of other agents, which are difficult to be independently evaluated by users and UAVs. To tackle this, we consider a CTDE framework enabled by DT, where the observations and actions are first collected during the interaction between agents and physical environment at each time step, and then are delivered to the DT layer for updating the virtual twins. Therefore, DT layer evaluates the rewards by the uploaded information, such as the actual computing time and the energy consumption. Meanwhile, the hyperparameters such as the distribution of task information can be timely estimated in DT layer. The global state $s _ { t }$ is merged by observations in DT layer, and is sent to the critic networks of each type of agent, which work as the centralized state-value functions.

During training process, the centralized state-value function of u-th type of agent is defined by

$$
V _ { u , i } ^ { \pi } ( s _ { t } ; \theta _ { u } ) = \mathbb { E } \Bigg \{ \sum _ { l = 0 } ^ { \infty } \gamma _ { u } ^ { l } \mathcal { R } _ { u , i } ( s _ { t + l } , a _ { t + l } ) | s _ { t } = s , \pi \Bigg \} ,\tag{48}
$$

where $\mathbb { E } \{ \cdot \}$ denotes the expectation operation, $a _ { t }$ denotes the joint action of all the agents, $\mathcal { R } _ { u , i }$ is the reward function for agent i in u-th type of agents, and π denotes the general policy of all agents. $\gamma _ { u }$ denotes the discount factor that reveals the significance of future reward to agents. In addition, the actionvalue function is defined as

$$
Q _ { u , i } ^ { \pi } ( s _ { t } , a _ { t } ) = \mathbb { E } \Bigg \{ \sum _ { l = 0 } ^ { \infty } \gamma _ { u } ^ { l } \mathcal { R } _ { u , i } ( s _ { t + l } , a _ { t + l } ) | s _ { t } = s , a _ { t } = a , \pi \Bigg \} .\tag{49}
$$

![](images/2536bd9585ad3789a8df190769af5e27d6cde66b9ccdf46a6dd03c8da89ab208.jpg)  
Fig. 2. The training framework of MADRL.

As a result, we obtain the advantage function as

$$
A _ { t , u , i } = Q _ { u , i } ^ { \pi } ( s _ { t } , a _ { t } ) - V _ { u , i } ^ { \pi } ( s _ { t } ) ,\tag{50}
$$

which can be estimated by state-value $V _ { u } ( s _ { t } )$ as

$$
\hat { \boldsymbol A } _ { u } ( \boldsymbol s _ { t } ) = \sum _ { l = 0 } ^ { \infty } ( \gamma _ { u } \lambda ) ^ { l } \Bigl ( \boldsymbol r _ { t + l } + \gamma _ { u } V _ { u } ( \boldsymbol s _ { t + l + 1 } ) - V _ { u } ( \boldsymbol s _ { t } ) \Bigr ) .\tag{51}
$$

We utilize generalized advantage estimation (GAE) to evaluate the advantage function. The GAE factor λ controls the tradeoff between variance and bias of reward, and $\begin{array} { r l } { \delta _ { t } } & { { } = } \end{array}$ $( r _ { t } + \gamma _ { u } V _ { u } ( s _ { t + 1 } ) \ – \ V _ { u } ( s _ { t + l } ) )$ is the temporal-difference error. Accordingly, the critic can be updated by following loss function

$$
J ( w _ { u } ) = \frac { 1 } { 2 } \Big [ \hat { V } _ { \omega _ { u } } ( s _ { t } ) - V _ { u } ( s _ { t } ) \Big ] ^ { 2 } .\tag{52}
$$

For the actor networks, PPO algorithm introduces a clipping factor  to limit the update ratio of policy and thereby efficiently substitutes the calculation of trust region, based on which we can express the loss function of actor networks as

$$
\begin{array} { r l r } & { } & { J ( \theta _ { u } ) = \mathbb { E } \Big \{ \operatorname* { m i n } \big [ \mathrm { c l i p } \left( \frac { \pi _ { \theta _ { u } } \left( a _ { t } | s _ { t } \right) } { \pi _ { \theta _ { u } ^ { \prime } } \left( a _ { t } | s _ { t } \right) } , 1 - \epsilon , 1 + \epsilon \right) \hat { A } _ { u } ( s _ { t } ) , } \\ & { } & { \frac { \pi _ { \theta _ { u } } \left( a _ { t } | s _ { t } \right) } { \pi _ { \theta _ { u } ^ { \prime } } \left( a _ { t } | s _ { t } \right) } \hat { A } _ { u } ( s _ { t } ) \big ] + \psi S _ { t , u } \Big \} , \qquad ( 5 } \end{array}\tag{3}
$$

where $\theta _ { u } ^ { \prime }$ represents the parameters of old policy for agent type $u , \frac { \pi _ { \theta } { \left( { a } _ { t } \vert s _ { t } \right) } } { \pi _ { \theta ^ { \prime } } { \left( { a } _ { t } \vert s _ { t } \right) } }$ is the update ratio, and $\psi S _ { t , u }$ denotes the policy entropy representing the degree of exploration. In implement, the old policy $\theta _ { u } ^ { \prime }$ can be substituted by the logprobability of the actions and policy entropy $S _ { t , u } ,$ which are stored in the experience buffers of DT layer after previous update. Therefore, the actor networks and critic networks can be updated by gradients $\begin{array} { r } { \nabla \theta _ { u } = \frac { \partial J ( \theta _ { u } ) } { \partial \theta _ { u } } } \end{array}$ and $\begin{array} { r } { \nabla \omega _ { u } = \frac { \partial J ( \omega _ { u } ) } { \partial \omega _ { u } } } \end{array}$

## C. New Attention Critic Mechanism

1) Beta Policy: It is worth noting that Gaussian distribution is widely adopted in the output of actor networks for policybased DRL algorithms. However, in a majority of scenarios, the actions have both lower and upper bounds. On the contrary, Gaussian distribution is unbounded, and thus the action needs to be force clipped into given bounds, thereby leading to the boundary effects and estimation bias on policy gradient [28]. Furthermore, if the initial variance of Gaussian distribution is set small to reduce the boundary effect, the exploration ability will also decrease since the probability density will be more concentrated. If the variance becomes larger, the increasing probability of force-clipping on actions also makes the value of actions more likely to stay on boundaries, thereby leading to the reduction of exploration. Hence, we apply the Beta distribution for the output of actor networks. Denoting the parameters α and $\beta ,$ the Beta distribution with respect to x is given by

$$
f ( x , \alpha , \beta ) = \frac { \Gamma ( \alpha + \beta ) } { \Gamma ( \alpha ) \Gamma ( \beta ) } x ^ { \alpha - 1 } ( 1 - x ) ^ { \beta - 1 } .\tag{54}
$$

It is obvious that (54) has a bounded domain, thus being adaptive to the actions with double boundaries. In addition, it is beneficial for the algorithm to pursue a more uniform exploration at initial stage of training. Corresponding to this, the probability density of Beta distribution is typically higher closing to the boundaries than that of Gaussian distribution.

2) Attention Critic: The critic networks need to input large global state concatenated by observations. Therefore, the complexity of model sharply ascends when increasing the number of agents, which leads to the performance loss and slow convergence for typical full-connected networks. To address this difficulty, we utilize the attention mechanism in the critic networks. It is notable that attention mechanism can enhance the ability of agents to focus on the information of other agents in environment, some of which may have higher effect on the value function. It has been demonstrated that the learning speed and the performance can be scaled up by attention mechanism [29]. The elements of attention mechanism is calculated as follows:

For agent type u, the observations $\{ o _ { t } ^ { i } , \forall i \in \mathcal { I } _ { u } \}$ are first sent to the multi-layer perceptron (MLP) encoders, where the observations of different agent types are respectively encoded, to get the feature values $\{ \mathbf { f } _ { u , i } , \forall i \in \mathcal { T } \}$ . Subsequently, the feature values $\{ \mathbf { f } _ { u , i } , \forall i \in \mathcal { T } \}$ are sent to attention heads of uth type of agents, and thus the weighted attention values ${ \bf x } _ { u , i }$ are calculated by $\mathbf { x } _ { u , i } = \sum _ { j \neq i } \alpha _ { u , i , j } \mathbf { W } _ { \mathrm { v a l } } \mathbf { f } _ { u , j }$ , with

Algorithm 1 Proposed ATB-MAPPO Training Framework   
1: Initialize $n = 1 .$ , episode length El, PPO epochs $\mathrm { R p }$ , and   
maximum training episodes Me.   
2: Initialize actor networks $\theta _ { i }$ , critic networks $\omega _ { i }$ on users   
and $\mathrm { U A V s } , \forall e \in \{ 1 , 2 , 3 \} ;$   
3: for Episode = 1, . . . , Me do   
4: for $t = 1 , \ldots , \operatorname { E l }$ do   
5: if n = 1 then   
6: Obtain beampattern $\mathbf { R } _ { d , k }$ by solving problem (28)   
$\forall \in K ;$   
7: end if   
8: The agents of users obtain observations $o _ { t } ^ { i }$ from   
environment, $\forall i \in \mathbb { Z } _ { 1 } \cup \mathbb { Z } _ { 2 } ;$   
9: The agents of users execute actions $a _ { t } ^ { i } , \forall i \in \mathcal { T } _ { 1 } \cup \mathcal { T } _ { 2 } ;$   
10: The agents of UAVs obtain $o _ { t } ^ { i }$ from environment,   
$\forall i \in { \mathcal { T } } _ { 3 } ;$   
11: The agents of UAVs execute actions $a _ { t } ^ { i } , \forall i \in \mathcal { I } _ { 3 } ;$   
12: Update $n = n$ mod $N + 1 ;$   
13: if DT information uploading is required by DT layer   
then   
14: The users and UAVs upload their observations and   
actions to DT layer;   
15: The DT layer updates the virtual twins and evalu  
ates the rewards $r _ { t } ^ { i } ;$   
16: end if   
17: end for   
18: Calculate log-probability $\mathrm { p r } _ { t } ^ { i }$ in the DT layer, $\forall i \in$   
${ \mathcal { T } } , \forall t \in \{ 1 , \ldots , \operatorname { E l } \} ;$   
19: The DT layer summarizes the transitions   
${ \mathrm { T r } } _ { t } ^ { i } = \{ o _ { t } ^ { i } , a _ { t } ^ { i } , r _ { t } ^ { i } , s ( t ) , { \mathrm { p r } } _ { t } ^ { i } \} , \forall i \in { \mathbb { Z } } , \forall t \in \{ 1 , \dots , { \mathrm { E l } } \}$   
in buffers;   
20: for epoch = 1, . . . , Rp do   
21: for agents $i \in \mathcal { T }$ do   
22: Update actor and critic networks according to (53)   
and (52) by $\forall \mathrm { T r } _ { t } ^ { i } \in B _ { i } ;$   
23: end for   
24: end for   
25: end for

$$
\alpha _ { u , i , j } = \mathrm { S o f t m a x } \left( \frac { \mathbf { f } _ { u , j } ^ { \mathrm { T } } \mathbf { W } _ { \mathrm { k e y } } ^ { \mathrm { T } } \mathbf { W } _ { \mathrm { q u e } } \mathbf { f } _ { u , i } } { \sqrt { d _ { \mathrm { k e y } } } } \right) ,\tag{55}
$$

where $\{ \mathbf { f } _ { u , j } , \forall j \neq i \}$ are the feature values of other agents in $\mathcal { T } _ { u }$ except $i , \ d _ { \mathrm { k e y } }$ denotes the variance of ${ \bf x } _ { u , i } W _ { \mathrm { q u e } } W _ { \mathrm { k e y } } ^ { \mathrm { T } } { \bf f } _ { u , j } ^ { \mathrm { T } }$ Matrix $W _ { \mathrm { q u e } }$ transforms $f _ { u , i }$ into a query, matrix ${ \bf W } _ { \mathrm { k e y } }$ transforms $f _ { u , j }$ into a $k e y { \mathrm { . } }$ , and matrix $W _ { \mathrm { v a l } }$ transforms $f _ { u , j }$ into a value. Finally, ${ \bf x } _ { u , i }$ and $o _ { t } ^ { i }$ are concatenated and then sent to the last MLP in the critic network of agent type u to get the estimated state value $V _ { \omega _ { u } } ( t )$ . Based on the above-mentioned discussions, we summarize the ATB-MAPPO training framework in Algorithm 1.

## VI. NUMERICAL RESULTS

In this section, we carry out simulation experiments to evaluate the performance of proposed ATB-MAPPO training framework in DT-empowered ISCC network. We compare the performance of proposed scheme with the benchmarks as follows:

Beta-MAPPO: Proposed MAPPO-based training algorithm with Beta distribution on actor network and without attention mechanism.

Pure-MAPPO: Proposed MAPPO-based training algorithm with widely adopted Gaussian distribution and without adopting attention mechanism [27].

MADDPG: The multi-agent deep deterministic policy gradient (MADDPG) algorithm, which is an off-policy MADRL algorithm with deterministic action output and noise for exploration [23]. Each agent is corresponding to two shared actor and two critic networks.

Random offloading: The users randomly give actions, while the UAVs equally allocate the computational resource and move randomly.

## A. Simulation Scenario and Parameter Setting

The simulation settings are illustrated as follows. We consider an ISCC network with a 1000 m × 1000 m square area. The UAVs and the users are uniformly located at the height of 200 m and on the ground, respectively. The size of task data is uniformly distributed in [0.5 Mb, $D ^ { \mathrm { m a x } } ]$ , where $D ^ { \mathrm { m a x } }$ is set to be 1.5 Mb as default. The latency requirements of tasks $t _ { k } ^ { \mathrm { m a x } } [ n ]$ is uniformly distributed in [0.7 s, 1.0 s], and the average number of cycles required for each bit of task is $C _ { k } [ n ] \in [ 5 0 0 , 1 5 0 0 ]$ cycles. The estimation deviation of DT is set as 5%, i.e., $| \tilde { f } _ { k } [ n ] | \leq 5 \% f _ { k } [ n ]$ . The path loss model for channels can be referred from [17]. The average INR requirement is set as $\zeta _ { k } = 0 . 7$ for all users. For algorithm setup, the value normalization is used and the reward is clipped into [−5, 5]. The number of hidden layers for each MLP is $^ { 2 , }$ and the sizes of hidden layers are set as 64 and 128 neurons. The length of feature values V is 64. Unless otherwise specified, the channel bandwidth is set as B = 10 MHz, the noise power is −65 dBm, the Rician factor is ς = 10, the maximum ISCC power for users is set as <sup>p</sup> = 0.5 W, the number of antennas for users and UAVs is set as $N _ { T } = N _ { R } = 4 .$ , the channel power gain at the reference distance of 1 m is −30 dB, the capacitance coefficient is set as $\kappa _ { 1 } = \kappa _ { 2 } = 1 0 ^ { - 2 7 }$ the maximum CPU frequency of users and UAVs are set as $f _ { k } ^ { \mathrm { m a x } } = 1 \mathrm { G H z }$ and $f _ { m } ^ { \mathrm { m a x } } = 1 0 ~ \mathrm { G H z }$ , respectively, the time period is set as $N = 4 0 \ \mathrm { s } ,$ the duration of time slot $\delta _ { t } = 1$ ${ \bf S } ,$ the maximum velocity of UAVs is $v _ { \mathrm { m a x } } = 2 0$ m/s, the maximum acceleration of $\mathrm { U A V s ~ \it a _ { m a x } = 5 m / s ^ { 2 } . }$ , the UAV settings $P _ { 0 } , P _ { i } , U _ { \mathrm { t i p } } , v _ { 0 } ,$ <sup>A</sup> and s are set as 59.03 W, 79.07 W, 120 m/s, 3.6 m/s and $0 . 5 0 3 0 \ \mathrm { m } ^ { 2 }$ respectively, the safe distance between UAVs is set as $d _ { \operatorname* { m i n } } = 3$ m, and the weight factor is $\omega = 0 . 0 0 1$ . For algorithm settings, we have the maximum training episodes Me = 300 episodes, the episode length El = 200 steps, the learning rate is 0.0005, the discount factor is $\gamma _ { u } = 0 . 9 8$ , the penalty factors $\mu _ { o }$ and $\mu _ { t }$ are the same as 0.1, the number of PPO epochs $\mathrm { R p } \ = \ 5 , $ , the number of attention heads is 4, the adjusting factors $k _ { 1 }$ and $k _ { 2 }$ are 0.3 and 0.7, respectively, the distance threshold $d _ { \mathrm { t h } } = 3 5 0 ~ \mathrm { m } .$ , and the adopted optimizer is Adam.

![](images/660698b291e17c3c59a77696cfbe30dc79c6a98c179ca6249053ef4f0e6ab1d5.jpg)  
Fig. 3. Convergence versus offloading configuration agents.

![](images/9da6aec6a6d4a560082c3d670525f3660997386bf5318697b4314888b6eec75d.jpg)  
Fig. 4. Convergence versus UAV agents.

## B. Performance Evaluation

The convergence of deep neural network is extremely challenging and hard to be theoretically analyzed. The reason lies in that the convergence is highly dependent on DRL hyperparameters, in which the quantitative relationship between deep neural network convergence and the hyper-parameters is sophisticated. Therefore, a reasonable choice of the hyperparameters is required in order to achieve the convergence. We use numerical simulations (see Fig. 3–Fig. 5) to validate the convergence of the proposed PPO algorithm.

We first compare the convergence behavior of proposed ATB-MAPPO scheme with other MADRL benchmarks in Figs. 3 and 4, with K = 25 users and M = 5 UAVs. Intuitively, as the training steps increase, the reward of all the schemes gradually ascends, which confirms the effectiveness of MADRL algorithms in computation offloading. It is clear that the proposed ATB-MAPPO reaches at the highest reward, has a faster convergence rate than Beta-MAPPO, and has a higher reward than Pure-MAPPO with Gaussian distribution. This proves that Beta distribution is superior to Gaussian distribution in the actions of proposed ISCC network. As shown in Figs. 3 and 4, the convergence speed and the reward of MAPPO-based schemes achieve a remarkable improvement compared to the MADDPG-based scheme. As expected, it is readily found from Fig. 3 that the reward of offloading-configuration agents gradually improves and the average episode reward of proposed ATB-MAPPO scheme achieves to about -0.40 as the highest value. Fig. 4 reveals that the UAV agents also improve their policy for trading off the energy consumption and relative position to users. Another observation is that the reward slightly declines at the initial stage of training, and this is mainly because the users are exploring to offload their tasks to UAVs, which is still learning to appropriately allocate the computational resource for users and control their speed, thereby leading to the growth of computational time for penalty and energy consumption.

![](images/a56a97b7e8cbcefea9a957befb563c01fbfb22abd4f528d03e28428c1c4d48b3.jpg)  
Fig. 5. Convergence versus different sensing-communication factors.

We then evaluate the impact of sensing-communication weight factor $\omega _ { s }$ on the reward of beampattern-configuration agents with $K = 2 5$ users and $M = 5 \mathrm { U A V s }$ . We can see from Fig. 5 that as the $\omega _ { s }$ varies from 0.2 to 0.6, the reward reduces in general but ascends during training. This result reveals that the agents are able to trade off the performance of two functions under the design of MSE-based reward. Furthermore, when $\omega _ { s } > 0 . 6 ,$ , the reward increases in general, where the radar beampattern has been paid more attention. We will further evaluate the effect of $\omega _ { s }$ on beampatterns in the following Fig. 10.

Fig. 6 evaluates the impact of estimation deviation of DT on the system performance. Note that when the estimation deviation is 0, the perfect DT is achieved. It is observable that as the estimation deviation increases from 0% to 25%, the average weighted energy consumption of users has the tendency of increasing. It indicates that the deviation of CPU frequency may impose the fluctuating of computing time, the penalty, and thereby the quality of policy’s distribution. Notably, the superior performance of DT comes from the accuracy of DT estimation. Also, the result show that the weighted energy consumption increases with an increasing K, where K is chosen from {20, 30, 40}.

![](images/b4adf61f806c98ae4ecba24b264572a09bec7dbb2f2cc84ac519e3ea0d746429.jpg)  
Fig. 6. The impact of estimation deviation of DT.

![](images/db8c2a72fa5c57785247d6638bd8aea92b44dd0bac6a34ac3f10e187f7541a79.jpg)  
Fig. 7. Performance comparison versus different number of users.

Fig. 7 compares the weighted energy consumption under different number of users with $M = 5 ~ \mathrm { U A V s }$ . It can be readily observed that as the number of users becomes large, the weighted energy consumption of UAVs and users accordingly grows. As expected, the proposed ATB-MAPPO has the best performance, and the performance gaps between MADDPG and MAPPO-based schemes remain large. Another observation is that the performance gap between adjacent settings has the trend of increasing, which means that the average weighted energy of users also increases. This is because as more users join in the network, the signal interference between users grows and the transmission rate reduces, resulting in more computational resource is required for less available computing time with respect to latency requirements.

Fig. 8 evaluates the average weighted energy of users under different settings of bandwidth and task size with $K = 2 0$ We can find that as the maximum task size $D ^ { \mathrm { m a x } }$ grows, the energy consumption of users gradually grows, while the energy consumption reduces as the bandwidth grows. This can be explained by the fact that the increase of communication resource enhances the transmission rate of users, and the increase of task size makes the average computational energy increases. It can also be seen that the performance gap between different bandwidth gradually increases. This mainly because the increase of bandwidth makes the users willing to offload more tasks, which relieves the local computational load. In addition, less transmission time spares the available time for computation. Therefore, the CPU frequencies of users and UAVs can be jointly saved, leading to the rapid decreases of computational energy.

![](images/1e6012a4395a2ad086020a0a77b1c54f9b6195acc6d283b5bf45d61c468465c1.jpg)  
Fig. 8. The performance versus different task size and bandwidth.

![](images/a147def177e8fa71ad1826ecfde68f69a196bf2af2fae31e19217abcee4933e9.jpg)  
Fig. 9. Performance comparison versus different number of UAVs.

In Fig. 9, we compare the performance obtained by the five schemes versus different number of UAVs under $K = 3 0$ users. It can be observed that as the number of UAV grows, the average weighted energy consumption of users reduces, verifying the fact that more UAVs provide more computational resource, and the agents can seek the balance between computational load on UAVs and users to reduce the energy consumption. Furthermore, the gap between MADDPG and

![](images/7437abe63507e757b04bdba010ad04ab7f1a15164fccfe85eb17886fb7750ece.jpg)

![](images/11f1e4fd3244113b8eef3851217cf63a85b6e1efb69844f0e16accb54b9fdb8d.jpg)

![](images/81f56b9c2b795b8342e31e1fae33459fc9ca71203b38e6ed71b75760affcaec9.jpg)

![](images/4980b87a62f8c01f076876d38caef1e21eb23c8d169207035619ef9810151ca2.jpg)  
Fig. 10. The examples of beampatterns for sensing and communication.

![](images/a24b65c7c3702498edf9ffe27d5e40a65612982c8610d71bd118f1d53a917095.jpg)  
Fig. 11. The example of trajectories of UAVs under $K = 3 0$ and $M = 6 .$

MAPPO-based schemes gradually reduces as the number of UAVs increases, and the proposed algorithm constantly outperforms benchmarks. As such, we have presented that the proposed ATB-MAPPO scheme can efficiently optimize the policy for weighted energy consumption minimization in the service.

We then present the examples of optimized beampattern gain from −90 deg to 90 deg with respect to sensingcommunication weight factor $\omega _ { s }$ in Fig. 10. The azimuth angle for the evaluated user to its associated UAV is set to be $0 ,$ the beampattern gain for covariance matrix A at $\theta _ { l }$ is calculated as $\mathbf { a } ( \theta _ { l } ) ^ { \bar { \mathrm { H } } } \mathbf { A } \mathbf { a } ( \theta _ { l } )$ , where $\mathbf { a } ( \theta _ { l } )$ is the steering vector at $\theta _ { l } .$ . We can see that when $\omega _ { s } = 0 . 2$ and $\omega _ { s } = 0 . 4 $ , the primary beams of ${ \bf X } _ { k } [ n ]$ and ${ \mathbf W } _ { c , k } [ n ]$ focus on the direction for communication. When $\omega _ { s }$ becomes larger, the primary beams move to fit better with the desired beampattern $\mathbf { R } _ { d , k }$ of sensing. Hence, the performance for sensing and communication can be approximately traded off by $\omega _ { s } .$ In this regard, the effectiveness of reinforcement learning method for tackling beampatterns and channels is verified.

In Fig. 11, we present the example of $\mathrm { U A V s } '$ trajectories with $K = 3 0$ and $M = 6$ . It can be observed that UAVs are able to select the regions with more users, and can adaptively update their positions according to the distribution of associated users. Moreover, it implies that the reward can guide the UAVs to find the relative fair area for users and then hover slowly to save flying energy. The trajectories are jointly smooth, which makes it applicable for practical UAV movement compared with simply controlling the direction and velocity like [23], revealing the effectiveness of UAV agents in trajectories design.

## VII. CONCLUSION

In this paper, we proposed a multi-UAV-enabled ISCC network to jointly optimize the computation offloading and sensing performance. A cooperative MADRL framework was developed to solve the challenging multi-objective optimization problem. Considering the high-dimensional hybrid action spaces, we introduced the MAPPO method with attention mechanism and Beta distribution to obtain the optimal learning strategy effectively. Numerical results verified that the proposed scheme can significantly reduce the network energy consumption compared with the benchmark approaches. Meanwhile, the obtained radar beampattern can fit the ideal radar beam well.

## REFERENCES

[1] Z. Feng, Z. Wei, X. Chen, H. Yang, Q. Zhang, and P. Zhang, “Joint communication, sensing, and computation enabled 6G intelligent machine system,” IEEE Netw., vol. 35, no. 6, pp. 34–42, Nov./Dec. 2021.

[2] Y. Xu, T. Zhang, Y. Liu, and D. Yang, “UAV-enabled integrated sensing, computing, and communication: A fundamental trade-off,” IEEE Wireless Commun. Lett., vol. 12, no. 5, pp. 843–847, May 2023.

[3] T. Do-Duy, L. D. Nguyen, T. Q. Duong, S. R. Khosravirad, and H. Claussen, “Joint optimisation of real-time deployment and resource allocation for UAV-aided disaster emergency communications,” IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3411–3424, Nov. 2021.

[4] D.-H. Tran, V.-D. Nguyen, S. Chatzinotas, T. X. Vu, and B. Ottersten, “UAV relay-assisted emergency communications in IoT networks: Resource allocation and trajectory optimization,” IEEE Trans. Wireless Commun., vol. 21, no. 3, pp. 1621–1637, Mar. 2022.

[5] Q. Wu et al., “A comprehensive overview on 5G-and-beyond networks with UAVs: From communications to sensing and intelligence,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 2912–2945, Oct. 2021.

[6] Y. Wu, K. Zhang, and Y. Zhang, “Digital twin networks: A survey,” IEEE Internet Things J., vol. 8, no. 18, pp. 13789–13804, Sep. 2021.

[7] C. Alcaraz and J. Lopez, “Digital twin: A comprehensive survey of security threats,” IEEE Commun. Surveys Tuts., vol. 24, no. 3, pp. 1475–1503, 3rd Quart., 2022.

[8] Z. Wang et al., “Mobility digital twin: Concept, architecture, case study, and future challenges,” IEEE Internet Things J., vol. 9, no. 18, pp. 17452–17467, Sep. 2022.

[9] T. Do-Duy, D. V. Huynh, O. A. Dobre, B. Canberk, and T. Q. Duong, “Digital twin-aided intelligent offloading with edge selection in mobile edge computing,” IEEE Wireless Commun. Lett., vol. 11, no. 4, pp. 806–810, Apr. 2022.

[10] Y. Dai, K. Zhang, S. Maharjan, and Y. Zhang, “Deep reinforcement learning for stochastic computation offloading in digital twin networks,” IEEE Trans. Ind. Informat., vol. 17, no. 7, pp. 4968–4977, Jul. 2021.

[11] T. Liu, L. Tang, W. Wang, Q. Chen, and X. Zeng, “Digital-twinassisted task offloading based on edge collaboration in the digital twin edge network,” IEEE Internet Things J., vol. 9, no. 2, pp. 1427–1444, Jan. 2022.

[12] Z. Zhou, Z. Jia, H. Liao, W. Lu, S. Mumtaz, and M. Guizani, “Secure and latency-aware digital twin assisted resource scheduling for 5G edge computing-empowered distribution grids,” IEEE Trans. Ind. Informat., vol. 18, no. 7, pp. 4933–4943, Jul. 2022.

[13] K. Zhang, J. Cao, and Y. Zhang, “Adaptive digital twin and multiagent deep reinforcement learning for vehicular edge computing and networks,” IEEE Trans. Ind. Informat., vol. 18, no. 2, pp. 1405–1413, Feb. 2022.

[14] G. Shen et al., “Deep reinforcement learning for flocking motion of multi-UAV systems: Learn from a digital twin,” IEEE Internet Things J., vol. 9, no. 13, pp. 11141–11153, Jul. 2022.

[15] N. Huang, T. Wang, Y. Wu, Q. Wu, and T. Q. S. Quek, “Integrated sensing and communication assisted mobile edge computing: An energy-efficient design via intelligent reflecting surface,” IEEE Wireless Commun. Lett., vol. 11, no. 10, pp. 2085–2089, Oct. 2022.

[16] Z. Wang, Y. Liu, X. Mu, Z. Ding, and O. A. Dobre, “NOMA empowered integrated sensing and communication,” IEEE Commun. Lett., vol. 26, no. 3, pp. 677–681, Mar. 2022.

[17] Q. Qi et al., “Integrating sensing, computing, and communication in 6G wireless networks: Design and optimization,” IEEE Trans. Commun., vol. 70, no. 9, pp. 6212–6227, Sep. 2022.

[18] C. Ding et al., “Joint MIMO precoding and computation resource allocation for dual-function radar and communication systems with mobile edge computing,” IEEE J. Sel. Areas Commun., vol. 40, no. 7, pp. 2085–2102, Jul. 2022.

[19] L. Zhao, D. Wu, L. Zhou, and Y. Qian, “Radio resource allocation for integrated sensing, communication, and computation networks,” IEEE Trans. Wireless Commun., vol. 21, no. 10, pp. 8675–8687, Oct. 2022.

[20] C. Liu et al., “Learning-based predictive beamforming for integrated sensing and communication in vehicular networks,” IEEE J. Sel. Areas Commun., vol. 40, no. 8, pp. 2317–2334, Aug. 2022.

[21] X. Liu, T. Huang, N. Shlezinger, Y. Liu, J. Zhou, and Y. C. Eldar, “Joint transmit beamforming for multiuser MIMO communications and MIMO radar,” IEEE Trans. Signal Process., vol. 68, pp. 3929–3944, 2020.

[22] F. Liu, C. Masouros, A. Li, H. Sun, and L. Hanzo, “MU-MIMO communications with MIMO radar: From co-existence to joint transmission,” IEEE Trans. Wireless Commun., vol. 17, no. 4, pp. 2755–2770, Apr. 2018.

[23] L. Wang, K. Wang, C. Pan, W. Xu, N. Aslam, and L. Hanzo, “Multiagent deep reinforcement learning-based trajectory planning for multi-UAV assisted mobile edge computing,” IEEE Trans. Cogn. Commun. Netw., vol. 7, no. 1, pp. 73–84, Mar. 2021.

[24] H. Peng and X. Shen, “Multi-agent reinforcement learning based resource management in MEC- and UAV-assisted vehicular networks,” IEEE J. Sel. Areas Commun., vol. 39, no. 1, pp. 131–141, Jan. 2021.

[25] N. Zhao, Z. Ye, Y. Pei, Y.-C. Liang, and D. Niyato, “Multi-agent deep reinforcement learning for task offloading in UAV-assisted mobile edge computing,” IEEE Trans. Wireless Commun., vol. 21, no. 9, pp. 6949–6960, Sep. 2022.

[26] Y. Wang, M. Sheng, X. Wang, L. Wang, and J. Li, “Mobile-edge computing: Partial computation offloading using dynamic voltage scaling,” IEEE Trans. Commun., vol. 64, no. 10, pp. 4268–4282, Oct. 2016.

[27] C. Yu, A. Velu, E. Vinitsky, Y. Wang, A. Bayen, and Y. Wu. “The surprising effectiveness of PPO in cooperative, multi-agent games.” 2021. [Online]. Available: http://arxiv.org/abs/2103.01955

[28] P.-W. Chou, D. Maturana, and S. Scherer, “Improving stochastic policy gradients in continuous control with deep reinforcement learning using the beta distribution,” in Proc. Int. Conf. Mach. Learn. (ICML), vol. 70, Aug. 2017, pp. 834–843.

[29] T. Cai et al., “Cooperative data sensing and computation offloading in UAV-assisted crowdsensing with multi-agent deep reinforcement learning,” IEEE Trans. Netw. Sci. Eng., vol. 9, no. 5, pp. 3197–3211, Sep./Oct. 2022.

![](images/1f3f99ec0f5e74539530179dc4953fd2cb0d32f942d94093eecab49f26db53bb.jpg)

Bin Li (Member, IEEE) received the Ph.D. degree in information and communication engineering from Beijing Institute of Technology, Beijing, China, in 2019. From 2013 to 2014, he was a Research Assistant with the Department of Electronic and Information Engineering, The Hong Kong Polytechnic University, Hong Kong. From 2017 to 2018, he was a visiting student with the Department of Informatics, University of Oslo, Oslo, Norway. In 2019, he joined the School of Computer Science, Nanjing University of Information Science

and Technology, Nanjing, China. His research interests include unmannedaerial-vehicle communications, reconfigurable intelligent surface, and mobileedge computing.

![](images/a7d0268b723ef296ed85968f29d421258eaffc2ec743e2316320348ab8312c94.jpg)

Wenshuai Liu received the B.S. degree in automation from LiRen College, Yanshan University, Qinhuangdao, China, in 2019. He is currently pursuing the M.S. degree with the School of Computer Science, Nanjing University of Information Science and Technology, Nanjing, China. His main research interests include mobile-edge computing, integrated sensing and communications, and deep reinforcement learning.

![](images/1ad1cc4633b62dd86f791dd85f55b0ca3f0f378582a41a4cd7bbb4da2afeaa2f.jpg)

Wancheng Xie received the B.S. degree in computer science and technology from Nanjing University of Information Science and Technology, Nanjing, China, in 2023. He is currently pursuing the master’s degree with Xiamen University. His main research interests include mobile-edge computing, unmanned aerial vehicles, and deep reinforcement learning.

![](images/3bf3b74621b8683d3be8abc5927ef2ff5ba4c7c72d387126ae28296091eaa4aa.jpg)

Ning Zhang (Senior Member, IEEE) received the Ph.D. degree in electrical and computer engineering from the University of Waterloo, Canada, in 2015. After that, he was a Postdoctoral Research Fellow with the University of Waterloo and the University of Toronto. Since 2020, he has been an Associate Professor with the Department of Electrical and Computer Engineering, University of Windsor, Canada. His research interests include connected vehicles, mobile edge computing, wireless networking, and security. He received a number of

Best Paper Awards from conferences and journals, such as IEEE Globecom, IEEE ICC, IEEE ICCC, IEEE WCSP, and Journal of Communications and Information Networks. He also received IEEE TCSVC Rising Star Award and the IEEE ComSoc Young Professionals Outstanding Nominee Award. He is a Highly Cited Researcher (Web of Science). He serves/served as an Associate Editor for IEEE TRANSACTIONS ON MOBILE COMPUTING, IEEE COMMUNICATIONS SURVEYS AND TUTORIALS, IEEE INTERNET OF THINGS JOURNAL, and IEEE TRANSACTIONS ON COGNITIVE COMMUNICATIONS AND NETWORKING. He also serves/served as the TPC Chair for IEEE VTC 2021 and IEEE SAGC 2020, the General Chair for IEEE SAGC 2021, the Chair for track of several international conferences and workshops, including IEEE ICC, VTC, INFOCOM Workshop, and Mobicom Workshop. He serves as the Vice Chair for IEEE Technical Committee on Cognitive Networks and IEEE Technical Committee on Big Data.

![](images/5f0fd17ce5aa9a147ae9d8708cb45b155927823a0d7e269f2241201f1a05cc59.jpg)

Yan Zhang (Fellow, IEEE) is currently a Full Professor with the Department of Informatics, University of Oslo, Norway. His research interests include next-generation wireless networks leading to 6G, green and secure cyber–physical systems. Since 2018, he has been a recipient of the global “Highly Cited Researcher” Award (Web of Science top 1% most cited worldwide) for four years. He is a fellow of IET, and an Elected Member of Academia Europaea, the Royal Norwegian Society of Sciences and Letters, and the Norwegian

Academy of Technological Sciences. He is an Editor of several IEEE transactions/magazine, including IEEE Network Magazine, IEEE TRANSACTIONS ON GREEN COMMUNICATIONS AND NETWORKING, IEEE TRANSACTIONS ON NETWORK SCIENCE AND ENGINEERING, IEEE TRANSACTIONS ON SUSTAINABLE COMPUTING, IEEE TRANSACTIONS ON VEHICULAR TECHNOLOGY, IEEE TRANSACTIONS ON INDUSTRIAL INFORMATICS, IEEE INTERNET OF THINGS JOURNAL, IEEE SYSTEMS JOURNAL, and IEEE Vehicular Technology Magazine. He is the Program/Symposium Chair in a number of conferences, including IEEE IWQoS 2022, IEEE ICC 2021, and IEEE SmartGridComm 2021.