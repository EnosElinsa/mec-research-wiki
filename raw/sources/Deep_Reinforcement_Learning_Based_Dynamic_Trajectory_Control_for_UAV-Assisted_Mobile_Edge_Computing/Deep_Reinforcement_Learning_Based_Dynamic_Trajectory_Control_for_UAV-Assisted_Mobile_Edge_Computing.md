# Deep Reinforcement Learning Based Dynamic Trajectory Control for UAV-Assisted Mobile Edge Computing

Liang Wang , Kezhi Wang , Senior Member, IEEE, Cunhua Pan , Wei Xu , Senior Member, IEEE, Nauman Aslam , and Arumugam Nallanathan , Fellow, IEEE

Abstract—In this paper, we consider a platform of flying mobile edge computing (F-MEC), where unmanned aerial vehicles (UAVs) serve as equipment providing computation resource, and they enable task offloading from user equipment (UE). We aim to minimize energy consumption of all UEs via optimizing user association, resource allocation and the trajectory of UAVs. To this end, we first propose a Convex optimizAtion based Trajectory control algorithm (CAT), which solves the problem in an iterative way by using block coordinate descent (BCD) method. Then, to make the real-time decision while taking into account the dynamics of the environment (i.e., UAV may take off from different locations), we propose a deep Reinforcement leArning based trajectory control algorithm (RAT). In RAT, we apply the Prioritized Experience Replay (PER) to improve the convergence of the training procedure. Different from the convex optimization based algorithm which may be susceptible to the initial points and requires iterations, RAT can be adapted to any taking off points of the UAVs and can obtain the solution more rapidly than CAT once training process has been completed. Simulation results show that the proposed CAT and RAT achieve the considerable performance and both outperform traditional algorithms.

Index Terms—Deep reinforcement learning, mobile edge computing, Unmanned Aerial Vehicle (UAV), trajectory control, user association

# 1 INTRODUCTION

ITH the popularity of computationally-intensive tasks, e.g., smart navigation and augmented reality, people are expecting to enjoy more convenient life than ever before. However, current smart devices and user equipments (UEs), due to small size and limited resource, e.g., computation and battery, may not be able to provide satisfactory Quality of Service (QoS) and Quality of Experience (QoE) in executing those highly demanding tasks.

Mobile edge computing (MEC) has been proposed by moving the computation resource to the network edge and it has been proved to greatly enhance UE’s ability in executing computation-hungry tasks [1]. Recently, flying mobile edge computing (F-MEC) has been proposed, which goes one step further by considering that the computing resource can be carried by unmanned aerial

Liang Wang, Kezhi Wang, and Nauman Aslam are with the Department of Computer and Informantion Science, Northumbria University, NE1 8ST Newcastle upon Tyne, U.K. E-mail: {liang.wang, kezhi.wang, nauman. aslam}@northumbria.ac.uk.   
Cunhua Pan and Arumugam Nallanathan are with the School of Electronic Engineering and Computer Science, Queen Mary University of London, E1 4NS London, U.K. E-mail: {c.pan, a.nallanathan}@qmul.ac. uk.   
Wei Xu is with the National Mobile Communications Research Lab, Southeast University, Nanjing 210096, China, and also with the Henan Joint International Research Laboratory of Intelligent Networking and Data Analysis, Zhengzhou University, Zhengzhou 450001, China. E-mail: wxu@seu.edu.cn.

Manuscript received 27 Jan. 2020; revised 9 Feb. 2021; accepted 10 Feb. 2021. Date of publication 16 Feb. 2021; date of current version 31 Aug. 2022. (Corresponding authors: Kezhi Wang.) Digital Object Identifier no. 10.1109/TMC.2021.3059691

vehicles (UAVs) [2]. F-MEC inherits the merits of UAV and it is expected to provide more flexible, easier and faster computing service than traditional fixed-location MEC infrastructures. However, the F-MEC also brings several challenges: 1) how to minimize the long-term energy consumption of all UEs by choosing proper user association (i.e., whether UE should offload the tasks and if so, which UAV to offload to, in the case of multiple flying UAVs); 2) how much computations the UAV should allocate to each offloaded UE by considering the limited amount of onboard resource; 3) how to control each UAV’s trajectory in real time (namely, flying direction and distance), especially considering the dynamic environment (i.e., the UAV may serve UEs from different taking off points). Traditional approaches like exhaustive search are hardly to tackle the above problems due to the fact that the decision variable space of F-MEC, e.g., deciding the optimal trajectory and resource allocation, is continuous instead of discrete. In [3], the authors propose a quantized dynamic programming algorithm to address the resource allocation problem of MEC. However, the complexity of this approach is very high as the flying choice of UAV is nearly infinite (as continues variables). Moreover, the authors in [4] discretize the UAV trajectory into a sequence of UAV locations and make their proposed problem tractable. Similarly, in [5], the authors assume that the UAV’s trajectory can be approximated by using the discrete variables and then they deal with it by using the traditional convex optimization approaches. However, the above treatment may decrease the control accuracy of the UAV and also is not flexible. Furthermore, the above contributions only considered a single UAV case. In practice, one UAV may not have enough resource to serve all the users. If the served area is very large, more than one UAV are normally needed, which will undoubtedly increase the decision space and make it very difficult for the traditional convex optimization-based approaches to obtain the optimal control strategies of each UAV. In [6], Liu et al. propose a deep reinforcement learning based DRL-EC3 algorithm, which can control the trajectory of multiple UAVs but did not consider the user association and resource allocation.

Inspired by the challenges mentioned above, in this paper, we first propose a Convex optimizAtion based Trajectory control algorithm (CAT) to minimize the energy consumption of all the UEs, by jointly optimizing user association, resource allocation and UAV trajectory. Specifically, by applying block coordinate descent (BCD) method, CAT is divided into two parts, i.e., subproblems for deciding UAV trajectories and for deciding user association and resource allocation. In each iteration, we solve each part separately while keep the other part fixed, until the convergence is achieved.

Next, we propose a deep Reinforcement leArning based Trajectory control algorithm (RAT) to facilitate the real-time decision making. In RAT, two deep Q networks (DQNs), i.e., actor and critic networks are applied, where the actor network is responsible for deciding the direction and flying distance of the UAV, while the critic network is in charge of evaluating the actions generated by the actor network. Then, we propose a low-complexity matching algorithm to decide the user association and resource allocation with the UAVs. We choose the overall energy consumption of all the UEs as a reward of the RAT. In addition, we deploy a minibatch to collect samples from the experience replay buffer by using a Prioritized Experience Replay (PER) scheme.

Different from traditional optimization based algorithms which normally need iterations and are susceptible to initial points, the proposed RAT can be adapted to any taking off points of the UAVs and can obtain the solutions very rapidly once the training process has been completed. In other words, if the taking off points of UAV are input to the RAT, the trajectories of UAVs will be determined by the proposed RAT with only some simple algebraic calculations instead of solving the original optimization problem through traditional high-complexity optimization algorithms. This attributes to the fact that during the training stages, excessive randomly taking off points of UAV are generated and used to train the networks until they are converged. Also, with the help of prioritized experience reply, the convergence speed will be increased significantly. RAT can be applied to the practical scenarios where the UAVs needs to act and fly swiftly such as the battlefields. By inputting the current coordinates as the taking off points to the networks, the trajectories of the UAVs will be immediately obtained and then all the UAVs can take off and fly according to the obtained trajectories. Also, the resource allocation and user association are determined by the proposed low-complexity matching algorithm. This is particularly useful to some emergence scenarios (e.g., battlefields, earthquake, large fires), as fast decision making is crucial in these areas.

In the simulation, we can see that the proposed RAT can achieve the similar performance as the convex-based solution CAT. They both have considerable performance gain over other traditional algorithms. In addition, we can see that during the learning procedure, the proposed RAT is less sensitive to the hyperparameters, i.e., the size of minibatch and the experience replay buffer, when comparing to tradtional reinforcement learning where PER is not applied.

The remainder of this paper is organized as follows. Section 2 presents the related work. Section 3 describes the system model. Section 4 introduces the proposed CAT algorithm, whereas Section 5 gives the proposed RAT algorithm including the preliminaries of DRL. Section 6 extends the application of proposed RAT algorithm to 3-D scenario. The simulation results are reported in Section 7. Finally, conclusions are given in Section 8.

# 2 RELATED WORK

There are many related works that study UAV, MEC and DRL separately, but only a very few consider them holistically. For UAV aided wireless communications, several scenarios have been studied, such as in areas of relay transmissions [7], cellular system [8], data collection [9], wireless power transfer [10], caching networks [11], and D2D communication [12]. In [13], the authors presented an approach to optimize the altitude of UAV to guarantee the maximum radio coverage on the ground. In [14], the authors presented a fly-hover-and-communicate protocol in a UAV-enabled multiuser communication system. They partitioned the ground terminals into disjoint clusters and deployed the UAV as a flying base station. Then, by jointly optimizing the UAV altitude and antenna beamwidth, they optimized the throughput in UAV-enabled downlink multicasting, downlink broadcasting, and uplink multiple access models. In [4], to maximize the minimum average throughput of covered users in OFDMA system, the authors proposed an efficient iterative algorithm based on block coordinate descent and convex optimization techniques to optimize the UAV trajectory and resource allocation. Furthermore, UAV trajectory optimization research were also investigated. For instance in [15], Zeng et al. proposed an efficient design by optimizing UAV’s flight radius and speed for the sake of maximizing the energy efficiency of UAV communication. In order to maximize the minimum throughput of all mobile terminals in cellular networks, Lyu et al. [16] developed a new hybrid network architecture by deploying UAV as an aerial mobile base station. Different from [4], [13], [14], [15] with the single UAV system, a multi-UAV enabled wireless communication system was considered to serve a group of users in [17]. Also, in [18], resource allocation between communication and computation has been investigated in multi-UAV systems. In [19], Mozaffari et al. investigated the application of UAVs in Internet of Things (IoT) network, and they optimized the mobility of UAVs, the device-UAV association and uplink power control, for minimizing the overall transmit power of ground IoT devices.

In addition, some recent literature made efforts to mobile edge computing, which is considered to be a promising technology for bringing computing resource to the edge of wireless networks [20], where UEs can benefit from offloading their tasks to MEC servers. In [21], partial computation offloading was studied. The computation tasks can be divided into two parts, where one part is executed locally and the other part is offloaded to MEC servers. In [22], binary computation offloading was studied, where the computation tasks can either be executed locally or offloaded to MEC servers.

![](images/6b29226c4b82732e3078aecaafa94116eaecea37a1f30e2ae3eafd6c55d3c751.jpg)

<details>
<summary>text_image</summary>

[Xj(t), Yj(t), Zj(t)]
UE
UAV
x
y
z
Rj max
aij(t)
[xi, y]
Task offloading
Coverage area
Coverage radius
Flying direction
Offloading Local execution T
{Di(1), Fi(1)} {Di(2), Fi(2)} ... Offloading {Di(t), Fi(t)} ...
i-th UE
</details>

Fig. 1. Multi-UAV enabled F-MEC architecture.

By taking advantage of the mobility of UAVs, UAVenabled MEC has been studied in [23], [24]. In [23], authors proposed a heterogeneous MEC (H-MEC) architecture that consists of fixed ground stations and UAVs. In [24], the authors studied UAV-enabled MEC, where wireless power transfer technology is applied to power Internet of things devices and collect data from them. In [25], Zhou et al. investigated an UAV-enabled MEC wireless-powered system, and they tackled the computation maximization problem through optimizing UAV’s speed, partial and binary computation offloading modes. In [26], Asheralieva et al. studied network operation problem in UAV-enabled MEC network, and they developed a framework based on hierarchical game-theoretic and reinforcement learning. In [27], Zhang et al. established a communication and computation optimization model in an MEC-enabled UAV network, where the successful transmission probability was derived through using stochastic geometry.

For most of the above works, optimization theory are mainly applied in order to obtain the optimal and / or suboptimal solutions, e.g., trajectory design and resource allocation. However, solving such optimization problems normally requires plenty of computational resources and take much time. To address this problem, DRL has been applied and attracted much attention recently. In [28], the authors proposed a RL framework that uses DQN as the function approximator. In addition, two important ingredients experience replay and target network are used for improving the convergence performance. In [29], the authors pointed out that the classical DQN algorithm may suffer from substantial overestimations in some scenarios, and proposed a double Q-learning algorithm. In order to solve control problems with continuous state and action space, Lillicrap at al. [30] proposed a policy gradient based algorithm. For the purpose of obtaining faster learning and state-of-art performance, in [31], the authors proposed a more robust and scalable approach named prioritized experience replay. Although DRL has achieved remarkable successes in game-playing scenarios, it is still an open research area in UAV-enabled MEC.

TABLE 1 Main Notations 

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $i, N, \mathcal{N}$ </td><td>index, number, set of UEs.</td></tr><tr><td> $j, M, \mathcal{M}$ </td><td>index, number, set of UAVs.</td></tr><tr><td> $t, T, \mathcal{T}$ </td><td>index, number, set of time slots.</td></tr><tr><td> $I_i(t), D_i(t), F_i(t)$ </td><td> $i$ th UEs’ task in  $t$ th time slot.</td></tr><tr><td> $a_{ij}(t)$ </td><td>user association between  $i$ th UE and  $j$ th UAV.</td></tr><tr><td> $R_j^{\max}$ </td><td>maximal horizontal coverage radius of  $j$ th UAV.</td></tr><tr><td> $\theta_j^h(t), \theta_j^v(t), d_j(t)$ </td><td>flying action of  $j$ th UAV.</td></tr><tr><td> $d^{\max}, v_j(t)$ </td><td>maximal distance, velocity of  $j$ th UAV.</td></tr><tr><td> $[X_j(t), Y_j(t), Z_j(t)]$ </td><td>coordinate of  $j$ th UAV.</td></tr><tr><td> $X^{\max}, Y^{\max}$ </td><td>side length of rectangle-shaped area.</td></tr><tr><td> $T^{\max}$ </td><td>maximal time duration.</td></tr><tr><td> $V^{\max}, f^{\max}$ </td><td>maximal number of tasks, computation resource.</td></tr><tr><td> $[x_i, y_i]$ </td><td>coordinate of  $i$ th UE.</td></tr><tr><td> $R_{ij}(t)$ </td><td>horizontal distance between UE and UAV.</td></tr><tr><td> $B, P^{\text{Tr}}$ </td><td>channel bandwidth, transmitting power.</td></tr><tr><td> $g_0, \sigma^2$ </td><td>channel power gain, noise power.</td></tr><tr><td> $T_{ij}^{\text{O}}(t), T_{ij}^{\text{Tr}}(t), T_{ij}^{\text{C}}(t)$ </td><td>time for task completion, offloading, executing.</td></tr><tr><td> $E_{ij}^{\text{Tr}}(t), E_{ij}^{\text{L}}(t)$ </td><td>energy for offloading, local execution.</td></tr><tr><td> $U, G$ </td><td>set of UAV trajectory, UAV coordinates.</td></tr><tr><td> $A, F$ </td><td>set of user association, resource allocation.</td></tr><tr><td> $s(t), a(t), z(t)$ </td><td>state, action and reward.</td></tr><tr><td> $\pi(\cdot), Q(\cdot), L(\cdot)$ </td><td>policy function, Q function, loss function.</td></tr><tr><td> $K, X$ </td><td>size of mini-batch, experience replay buffer.</td></tr><tr><td> $\phi, \delta, J$ </td><td>network parameter, TD-error, policy gradient.</td></tr><tr><td> $Z^{\min}, Z^{\max}$ </td><td>minimal, maximal altitude value.</td></tr><tr><td> $d_{ij}(t)$ </td><td>distance between the  $j$ th UAV and  $i$ th UE.</td></tr></table>

# 3 SYSTEM MODEL

As shown in Fig. 1, we consider a scenario that there are N UEs with the set denoted as $\mathcal { N } = \{ 1 , 2 , \dots , N \}$ and M UAVs with the set denoted as $\mathcal { M } = \{ 1 , 2 , \dots , M \}$ g, which form an M ¼ f gF-MEC platform. To make it clear, the main notations used in this paper are listed in Table 1.

We assume that the ith UE generates one task $I _ { i } ( t )$ in the ð Þtth time slot, which has to be executed within a maximal time duration T max, due to the QoS requirement. In this paper, we assume the entire process lasts for T time slots. Thus, T tasks will be generated for each UE and we have t $\mathcal { T } = \{ 1 , 2 , \hdots , T \}$ and

$$
I _ {i} (t) = \{D _ {i} (t), F _ {i} (t) \}, \forall i \in \mathcal {N}, t \in \mathcal {T}, \tag {1}
$$

where D t denotes the size of data required to be transmitð Þted to a UAV if the UE chooses to offload the task, and $F _ { i } ( t )$ ð Þdenotes the total number of CPU cycles needed to execute this task. Assume that each UE can choose either to offload the task to one of the UAVs or execute the task locally. Then one can have

$$
a _ {i j} (t) = \{0, 1 \}, \forall i \in \mathcal {N}, j \in \mathcal {M}, t \in \mathcal {T}, \tag {2}
$$

where $a _ { i j } ( t ) = 1 , j \neq 0$ implies that the ith UE decides to offð Þ ¼ 6¼load the task to the jth UAV in the tth time slot, while $a _ { i j } ( t ) =$ $1 , j = 0$ ð Þ ¼means that the ith UE executes the task itself in the ¼tth time slot, and otherwise, $a _ { i j } ( t ) = 0$ . Define a new set $j \in$ $\mathcal { M } ^ { \prime } = \{ 0 , 1 , 2 , \dots , M \}$ ð Þ ¼ 2to represent the possible place where M ¼ f gthe tasks from UEs can be executed, where $j = 0$ indicates ¼that UE conducts its own task locally without offloading.

In addition, we assume that each UE can only be served by at most one UAV or itself, and each task only has one place to execute. Then, it follows

$$
\sum_ {j = 0} ^ {M} a _ {i j} (t) = 1, \forall i \in \mathcal {N}, t \in \mathcal {T}. \tag {3}
$$

Additionally, in this paper, the OFDM is applied, which means that each UAV can only accept $V ^ { \mathrm { m a x } }$ tasks in each time slot, due to the number of limited sub-carriers. Thus, one has

$$
\sum_ {i = 1} ^ {N} a _ {i j} (t) \leq V ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}. \tag {4}
$$

# 3.1 UAV Movement

Assume that the jth UAV flies at the altitude and it has a maximal horizontal coverage, which depends on the azimuth angle of antennas and the flying altitude [14]. Also, assume that in the tth time slot, the jth UAV can fly with a horizontal direction as

$$
0 \leq \theta_ {j} ^ {h} (t) \leq 2 \pi , \forall j \in \mathcal {M}, t \in \mathcal {T}, \tag {5}
$$

and distance as

$$
0 \leq d _ {j} (t) \leq d ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}, \tag {6}
$$

where $d ^ { \mathrm { m a x } }$ is the maximal flying distance that the UAV can move in each time slot, due to the limited power budget. In our paper, we describe the UAV’s movement based on the Cartesian Coordinate system. Thus, we denote the coordinate of the jth UAV in the tth time slot as $[ X _ { j } ( t ) , Y _ { j } ( t ) , Z _ { j } ]$ , where $\begin{array} { r l r } { X _ { j } ( t ) = X _ { j } ( 0 ) + \sum _ { l = 1 } ^ { t } d _ { j } ( l ) \cos { \big ( \theta _ { i } ^ { h } ( l ) \big ) } , } & { { } } & { \ Y _ { j } ( t ) = } \end{array}$ $\begin{array} { r } { Y _ { j } ( 0 ) + \sum _ { l = 1 } ^ { t } \dot { d } _ { j } ( l ) } \end{array}$ ¼sin $\left( { \theta } _ { j } ^ { h } ( l ) \right)$ ¼ and $[ \dot { X } _ { j } ( 0 ) , \dot { Y _ { j } } ( 0 ) , \dot { Z } _ { j } ]$ ð Þ ¼is the inið Þ þ ¼ ð Þ ð Þtial coordinate of the jth UAV.

Additionally, each UAV can only move within a rectangle-shaped area, whose side length is denoted as $X ^ { \mathrm { m a x } }$ , and $\bar { Y } ^ { \mathrm { m a x } }$ . Then, it has

$$
0 \leq X _ {j} (t) \leq X ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}, \tag {7}
$$

and

$$
0 \leq Y _ {j} (t) \leq Y ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}. \tag {8}
$$

We denote that the jth UAV can move with a constant velocity $v _ { j } ( t )$ , which varies with the flying distance $d _ { j } ( t )$ in ð Þeach time slot. Thus, it has

$$
v _ {j} (t) = \frac {d _ {j} (t)}{T ^ {\max}}, \forall j \in \mathcal {M}, t \in \mathcal {T}. \tag {9}
$$

In this paper, we ignore the communication related energy, including communication circuitry and signal processing.

# 3.2 Task Execution

If the ith UE decides to offload the task to the jth UAV in the tth time slot, then the horizontal distance $R _ { i j } ( t )$ can be written as

$$
R _ {i j} (t) = \sqrt {(X _ {j} (t) - x _ {i}) ^ {2} + (Y _ {j} (t) - y _ {i}) ^ {2}}, \tag {10}
$$

where $[ x _ { i } , y _ { i } ]$ is the coordinate of the ith UE. Additionally, ½ we assume that each UAV has a maximal azimuth angle $\theta ^ { \operatorname* { m a x } } . ^ { 1 }$ Thus, in each time slot, the maximal horizontal coverage of the jth UAV $R ^ { \mathrm { m a x } }$ can be obtained as follows

$$
R ^ {\max} = Z _ {j} \tan (\theta^ {\max}). \tag {11}
$$

Thus, it has

$$
a _ {i j} (t) R _ {i j} (t) \leq R ^ {\max}, \forall i \in \mathcal {N}, j \in \mathcal {M}, t \in \mathcal {T}. \tag {12}
$$

In this paper, the free space channel model is applied. Thus, the uplink data rate is given by

$$
r _ {i j} (t) = B \log_ {2} \left(1 + \frac {\alpha P ^ {\mathrm{Tr}}}{Z _ {j} ^ {2} + R _ {i j} ^ {2} (t)}\right), \forall i \in \mathcal {N}, j \in \mathcal {M}, t \in \mathcal {T}, \tag {13}
$$

where B is the bandwidth for each communication channel; $P ^ { \mathrm { T r } }$ is the transmitting power of the ith UE; $\begin{array} { r } { \alpha = \frac { g _ { 0 } G _ { 0 } } { \sigma ^ { 2 } } } \end{array}$ with $G _ { 0 }$ $\approx 2 . 2 8 4 6 \ [ 1 8 ] ; g _ { 0 }$ is the channel power gain at the reference distance 1 m and $\sigma ^ { 2 }$ is the noise power. Note that we consider each user applies orthogonal frequency division multiplexing (OFDM) channel and there is no interference among them.

If the ith UE decides to offload its task to the jth UAV in the tth time slot, the total task completion time is given by

$$
T _ {i j} ^ {\mathrm{O}} (t) = T _ {i j} ^ {\mathrm{Tr}} (t) + T _ {i j} ^ {\mathrm{C}} (t), \forall t \in \mathcal {T}, \tag {14}
$$

where $T _ { i j } ^ { \mathrm { T r } } ( t )$ is the time to offload the data from the ith UE ð Þto the jth UAV in the tth time slot, given by

$$
T _ {i j} ^ {\mathrm{Tr}} (t) = \frac {D _ {i} (t)}{r _ {i j} (t)}, \forall t \in \mathcal {T}, \tag {15}
$$

and $T _ { i j } ^ { \mathrm { C } } ( t )$ is the time required to execute the task at the ðUAV as

$$
T _ {i j} ^ {\mathrm{C}} (t) = \frac {F _ {i} (t)}{f _ {i j} ^ {\mathrm{C}} (t)}, \forall t \in \mathcal {T}, \tag {16}
$$

where $f _ { i j } ^ { \mathrm { C } } ( t )$ is the computation resource that the jth UAV ð Þcan provide to the ith UE in the tth time slot.

Note that the time needed for returning the results back to UE from UAV is ignored, similar to [32]. The overall energy consumption of the ith UE to the jth UAV in the tth time slot is given by

$$
E _ {i j} ^ {\mathrm{Tr}} (t) = P ^ {\mathrm{Tr}} T _ {i j} ^ {\mathrm{Tr}} (t), \forall t \in \mathcal {T}. \tag {17}
$$

If the UE decides to execute the task locally, the power consumption can be evaluated as $k _ { i } ( f _ { i j } ^ { \mathrm { L } } ( t ) ) ^ { v _ { i } }$ [33], where $k _ { i } \geq 0$ ð ðis the effective switched capacitance, $v _ { i }$ is typically set to $^ { 3 , }$ , and $f _ { i j } ^ { \mathrm { L } } ( t )$ is the computation resource that the ith UE ð Þapplies to execute the task. The overall time for local execution can be given by

$$
T _ {i j} ^ {\mathrm{L}} (t) = \frac {F _ {i} (t)}{f _ {i j} ^ {\mathrm{L}} (t)}. \tag {18}
$$

Thus, the total energy consumption for local execution is

$$
E _ {i j} ^ {\mathrm{L}} (t) = k _ {i} (f _ {i j} ^ {\mathrm{L}} (t)) ^ {v _ {i}} T _ {i j} ^ {\mathrm{L}} (t), t \in \mathcal {T}. \tag {19}
$$

To sum up, the overall energy consumption for task execution $E _ { i j } ( t )$ is given by

$$
E _ {i j} (t) = \left\{ \begin{array}{l l} E _ {i j} ^ {\mathrm{L}} (t), & \text { local   execution }, \\ E _ {i j} ^ {\mathrm{Tr}} (t), & \text { offloading }, \end{array} \right. \tag {20}
$$

and the time to complete the task $T _ { i j } ( t )$ is expressed as

$$
T _ {i j} (t) = \left\{ \begin{array}{l l} T _ {i j} ^ {\mathrm{L}} (t), & \text { local   execution }, \\ T _ {i j} ^ {\mathrm{O}} (t), & \text { offloading }. \end{array} \right. \tag {21}
$$

Without loss of generality, we assume that each task has to be completed within maximal time duration $T ^ { \mathrm { m a x } }$ , which is consistent with the maximal flying time in each time slot as

$$
T _ {i j} (t) \leq T ^ {\max}, \forall i \in \mathcal {N}, j \in \mathcal {M} ^ {\prime}, t \in \mathcal {T}. \tag {22}
$$

In each time slot, since the computation resource that each UAV can provide is limited, we have

$$
\sum_ {i = 1} ^ {N} a _ {i j} (t) f _ {i j} ^ {\mathrm{C}} (t) \leq f ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}, \tag {23}
$$

where $f ^ { \mathrm { m a x } }$ is the maximal computation resource that the jth UAV can provide in each time slot. Next, we show our proposed problem formulation.

# 3.3 Problem Formulation

Denote $U ~ = ~ \{ { \theta } _ { i } ^ { h } ( t ) , d _ { j } ( t ) , \forall j \in { \mathcal { M } } , t \in T \} , ~ A ~ = ~ \{ a _ { i j } ( t ) , \forall i \in$ $\mathcal { N } , j \in \mathcal { M } ^ { \prime } , t \in \mathcal { T } \} , F = \{ f _ { i j } ( t ) , \forall i \in \mathcal { N } , j \in \mathcal { M } ^ { \prime } , t \in \bar { \mathcal { T } } \}$ ð Þ 8 2. Then, N 2 M 2 T g f ð Þ 8 2 N 2 M 2 T gthe energy minimization for all UEs is formulated as

$$
\mathcal {P} 1: \min _ {U, A, F} \sum_ {i = 1} ^ {N} \sum_ {j = 0} ^ {M} \sum_ {t = 1} ^ {T} a _ {i j} (t) E _ {i j} (t) \tag {24a}
$$

subject to:

$$
a _ {i j} (t) = \{0, 1 \}, \forall i \in \mathcal {N}, j \in \mathcal {M} ^ {\prime}, t \in \mathcal {T}, \tag {24b}
$$

$$
\sum_ {j = 0} ^ {M} a _ {i j} (t) = 1, \forall i \in \mathcal {N}, t \in \mathcal {T}, \tag {24c}
$$

$$
\sum_ {i = 1} ^ {N} a _ {i j} (t) \leq V ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}, \tag {24d}
$$

$$
0 \leq \theta_ {j} ^ {h} (t) \leq 2 \pi , \forall j \in \mathcal {M}, t \in \mathcal {T}, \tag {24e}
$$

$$
0 \leq d _ {j} (t) \leq d ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}, \tag {24f}
$$

$$
0 \leq X _ {j} (t) \leq X ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}, \tag {24g}
$$

$$
0 \leq Y _ {j} (t) \leq Y ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}, \tag {24h}
$$

$$
a _ {i j} (t) R _ {i j} (t) \leq R ^ {\max}, \forall i \in \mathcal {N}, j \in \mathcal {M}, t \in \mathcal {T}, \tag {24i}
$$

$$
T _ {i j} (t) \leq T ^ {\max}, \forall i \in \mathcal {N}, j \in \mathcal {M} ^ {\prime}, t \in \mathcal {T}, \tag {24j}
$$

$$
\sum_ {i = 1} ^ {N} a _ {i j} (t) f _ {i j} ^ {\mathrm{C}} (t) \leq f ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}. \tag {24k}
$$

One can see that the above problem 1 is a mixed integer Pnonlinear programming (MINLP), as it includes both integer variable, A and continuous variables, F and $U ,$ which is very difficult to solve in general. We first propose a convex optimization based algorithm CAT to address it iteratively. Then, we propose a Deep Reinforcement Learning (DRL) based RAT to facilitate fast decision-making, which can be applied in dynamic environment. Note that in practice, if the ith UE does not generate the tasks in the tth time slot and then the corresponding $D _ { i } ( t )$ and $F _ { i } ( t )$ can be set to zero.

# 4 PROPOSED CAT ALGORITHM

In this section, a convex optimization based CAT is proposed to solve the above problem 1. We first define a set Pof new variables to denote the trajectories of UAVs as $G =$ $\{ G _ { j } ( t ) , \forall j \in \mathcal { M } , t \in \mathcal { T } \}$ , where the coordinate is $G _ { j } ( t ) =$ $\begin{array} { r } { [ X _ { j } ( t ) , Y _ { j } ( t ) ] , \quad X _ { j } ( t ) = X _ { j } ( 0 ) + \sum _ { l = 1 } ^ { t } d _ { j } ( l ) \cos \big ( \theta _ { j } ^ { h } ( l ) \big ) } \end{array}$ ð Þ ¼and $\begin{array} { r } { Y _ { j } ( t ) = \dot { Y } _ { j } ( 0 ) + \sum _ { l = 1 } ^ { t } d _ { j } ( l ) } \end{array}$ ðsin $\left( \theta _ { j } ^ { h } ( l ) \right)$ ¼ ð Þ ð Þ. Thus, the optimization ð Þ ¼problem $\mathcal { P } 1$ Þ þ ¼ ð Þ ð Þcan be reformulated as

$$
\mathcal {P} 2: \min _ {\boldsymbol {G}, \boldsymbol {A}, \boldsymbol {F}} \sum_ {i = 1} ^ {N} \sum_ {j = 0} ^ {M} \sum_ {t = 1} ^ {T} a _ {i j} (t) E _ {i j} (t) \tag {25a}
$$

subject to: 24b ; 24c ; 24d ; 24g ; 24h ; 24j ; 24k ;

$$
\left. a _ {i j} (t) \right| \left| G _ {j} (t) - q _ {i} \right| ^ {2} \leq \left(R ^ {\max}\right) ^ {2}, \forall i \in \mathcal {N}, j \in \mathcal {M}, t \in \mathcal {T}, \tag {25b}
$$

$$
\left| \left| G _ {j} (t + 1) - G _ {j} (t) \right| \right| ^ {2} \leq \left(d ^ {\max}\right) ^ {2}, \forall t \in \{0, 1, \dots , T - 1 \}, \tag {25c}
$$

where $q _ { i } = [ x _ { i } , y _ { i } ]$ . In order to solve ${ \mathcal { P } } 2 ,$ , we divide it into two ¼ ½  Psubproblems and apply the block coordinate descent method to address it. To this end, we first optimize the user association A and resource allocation F given the UAV trajectory G. Then, we optimize the UAV trajectory G given the user association A and resource allocation $F .$ . We solve the two optimization problems iteratively, until the convergence is achieved.

# 4.1 User Association and Resource Allocation

Given the UAV trajectory $G ,$ the subproblem to decide user association A and resource allocation F can be formulated as

$$
\min _ {\boldsymbol {A}, \boldsymbol {F}} \sum_ {i = 1} ^ {N} \sum_ {j = 0} ^ {M} \sum_ {t = 1} ^ {T} a _ {i j} (t) E _ {i j} (t) \tag {26a}
$$

subject to: 24b ; 24c ; 24d ; 24j ; 24k ; 25b :

One can see that (24j) can be written as

$$
f _ {i j} ^ {\mathrm{C}} (t) \geq \frac {F _ {i} (t)}{T ^ {\max} - \frac {D _ {i} (t)}{r _ {i j} (t)}}, \forall j \in \mathcal {M}, t \in \mathcal {T}, \tag {27}
$$

if the ith UE chooses to offload the task, and

$$
f _ {i j} ^ {\mathrm{L}} (t) \geq \frac {F _ {i} (t)}{T ^ {\max}}, j = 0, \forall t \in \mathcal {T}, \tag {28}
$$

if the ith UE decides to execute the task locally. It is readily to see that equality holds for both (27) and (28).

Then, (26) can be re-written as

$$
\min _ {\boldsymbol {A}, \boldsymbol {F}} \sum_ {i = 1} ^ {N} \sum_ {j = 0} ^ {M} \sum_ {t = 1} ^ {T} \left(a _ {i j} (t) E _ {i j} ^ {\mathrm{Tr}} (t) + \left(1 - a _ {i j} (t)\right) E _ {i j} ^ {\mathrm{L}} (t)\right) \tag {29a}
$$

subject to: 24b ; 24c ; 24d ; 25b ;

$$
f _ {i j} ^ {\mathrm{L}} (t) = \frac {F _ {i} (t)}{T ^ {\max}}, j = 0, \forall t \in \mathcal {T}, \tag {29b}
$$

$$
\sum_ {i = 1} ^ {N} a _ {i j} (t) \frac {F _ {i} (t)}{T ^ {\max} - \frac {D _ {i} (t)}{r _ {i j} (t)}} \leq f ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}. \tag {29c}
$$

It is ready to find (29) is similar to a Multiple-Choice Multi-Dimensional 0-1 Knapsack Problem (MMKP), which is difficult to solve in general. Fortunately, it may be addressed by applying Branch and Bound method via a standard Python package PULP [34].

# 4.2 UAV Trajectory Optimization

Given the user association and resource allocation from (29) and removing the constant, 2 can be simplified as

$$
\min _ {\boldsymbol {G}} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {M} \sum_ {t = 1} ^ {T} a _ {i j} (t) \frac {P ^ {\mathrm{Tr}} D _ {i} (t)}{\operatorname{Blog} _ {2} \left(1 + \frac {\alpha P ^ {\mathrm{Tr}}}{Z _ {j} ^ {2} + \left\| G _ {j} (t) - q _ {i} \right\| ^ {2}}\right)} \tag {30a}
$$

subject to: 24g ; 24h ; 25b ; 25c ;

$$
\frac {D _ {i} (t)}{B \log_ {2} \left(1 + \frac {\alpha P ^ {\mathrm{Tr}}}{Z _ {j} ^ {2} + \left\| G _ {j} (t) - q _ {i} \right\| ^ {2}}\right)} + \frac {F _ {i} (t)}{f _ {i j} ^ {\mathrm{C}} (t)} \leq T ^ {\max}, \tag {30b}
$$

$$
\forall i \in \mathcal {N}, j \in \mathcal {M}, t \in \mathcal {T}.
$$

It is easy to see that the above optimization problem is non-convex with respect to $G _ { j } ( t )$ . Next, we introduce a set $\eta = \{ \eta _ { i j } ( t ) , \forall i \in \mathcal { N } , j \in \mathcal { M } , t \in \mathcal { T } \}$ , where $\eta _ { i j } ( t ) = a _ { i j } ( t )$ $\begin{array} { r } { \frac { P ^ { \mathrm { T r } } D _ { i } ( t ) } { B \log _ { 2 } ( 1 + \frac { \alpha P ^ { \mathrm { T r } } } { Z _ { j } ^ { 2 } + \left| \left| G _ { j } ( t ) - q _ { i } \right| \right| ^ { 2 } } ) } } \end{array}$ Blog 2 1 ð Þ 8PTrD t ð ÞaP Tr , then, problem (30) can be transformed

$$
\min _ {\boldsymbol {G}, \boldsymbol {\eta}} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {M} \sum_ {t = 1} ^ {T} \eta_ {i j} (t) \tag {31a}
$$

subject to: 24g ; 24h ; 25b ; 25c ;

$$
B \log_ {2} \left(1 + \frac {\alpha P ^ {\mathrm{Tr}}}{Z _ {j} ^ {2} + | | G _ {j} (t) - q _ {i} | | ^ {2}}\right) \geq \frac {a _ {i j} (t) P ^ {\mathrm{Tr}} D _ {i} (t)}{\eta_ {i j} (t)},
$$

$$
\forall i \in \mathcal {N}, j \in \mathcal {M}, t \in \mathcal {T}, \tag {31b}
$$

$$
B \log_ {2} \left(1 + \frac {\alpha P ^ {\mathrm{Tr}}}{Z _ {j} ^ {2} + \left\| G _ {j} (t) - q _ {i} \right\| ^ {2}}\right) \geq \frac {D _ {i} (t)}{T ^ {\max} - \frac {F _ {i} (t)}{f _ {i j} ^ {C} (t)}}, \tag {31c}
$$

$$
\forall i \in \mathcal {N}, j \in \mathcal {M}, t \in \mathcal {T}.
$$

One observes that (31b) and (31c) are convex with respect to $| | G _ { j } ( t ) - q _ { i } | | .$ , respectively. Thus, (31b) and (31c) are nonjj ð Þ  jjconvex constraints. Then, similar to [4], [5], we apply the successive convex approximation (SCA) to solve this problem. Specifically, for any given local point $G _ { j } ^ { r } ( t )$ in ${ \bf \bar { \Psi } } _ { G ^ { r } } =$ $\{ G _ { j } ^ { r } ( t ) , \mathsf { \bar { \forall } } j \in \mathcal { M } , t \in \mathcal { T } \}$ ð Þ ¼, one can have the following inequalf ðity as

$$
\begin{array}{l} w _ {i j} (t) = B \log_ {2} \left(1 + \frac {\alpha P ^ {\mathrm{Tr}}}{Z _ {j} ^ {2} + \left| \left| G _ {j} (t) - q _ {i} \right| \right| ^ {2}}\right) (32) \\ \geq K _ {i j} ^ {r} (t) \left(\left| \left| G _ {j} (t) - q _ {i} \right| \right| ^ {2} - \left| \left| G _ {j} ^ {r} (t) - g _ {i} \right| \right| ^ {2}\right) + B _ {i j} ^ {r} (t) (32) \\ \triangleq w _ {i j} ^ {l b, r} (t), \\ \end{array}
$$

where

$$
K _ {i j} ^ {r} (t) = - \frac {B \alpha P ^ {\mathrm{Tr}} \log_ {2} (e)}{\left(Z _ {j} ^ {2} + \left| \left| G _ {j} ^ {r} (t) - q _ {i} \right| \right| ^ {2}\right) \left(Z _ {j} ^ {2} + \left| \left| G _ {j} ^ {r} (t) - q _ {i} \right| \right| ^ {2} + \alpha P ^ {\mathrm{Tr}}\right)}, \tag {33}
$$

and

$$
B _ {i j} ^ {r} (t) = B \log_ {2} \left(1 + \frac {\alpha P ^ {\mathrm{Tr}}}{Z _ {j} ^ {2} + | | G _ {j} ^ {r} (t) - q _ {i} | | ^ {2}}\right). \tag {34}
$$

Then, problem (31) can be written as

$$
\min _ {\boldsymbol {G}, \boldsymbol {\eta}} \sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {M} \sum_ {t = 1} ^ {T} \eta_ {i j} (t) \tag {35a}
$$

subject to: 24g ; 24h ; 25b ; 25c ;

$$
w _ {i j} ^ {l b, r} (t) \geq \frac {a _ {i j} (t) P ^ {\mathrm{Tr}} D _ {i} (t)}{\eta_ {i j} (t)}, \forall i \in \mathcal {N}, j \in \mathcal {M}, t \in \mathcal {T}, \tag {35b}
$$

$$
w _ {i j} ^ {l b, r} (t) \geq \frac {D _ {i} (t)}{T ^ {\max} - \frac {F _ {i} (t)}{f _ {i j} ^ {C} (t)}}, \forall i \in \mathcal {N}, j \in \mathcal {M}, t \in \mathcal {T}. \tag {35c}
$$

The above problem is a convex quadratically constrained quadratic program (QCQP) and it can be solved by a standard Python package CVXPY [35].

# 4.3 Overall Algorithm Design

In this section, a convex optimization-based CAT is proposed to solve Problem 2, where we optimize user association and Presource allocation subproblem iteratively with the UAV trajectory subproblem until the convergence is achieved. We describe the pseudo code of proposed CAT in Algorithm 1.

Algorithm 1. CAT Algorithm 

<table><tr><td>1: Set r = 0, and initialize $ G^{r} $;</td></tr><tr><td>2: repeat</td></tr><tr><td>3: Solve Problem (29) by Branch and Bound method for given $ G^{r} $, and denote the optimal solution as $ A^{r+1} $ and $ F^{r+1} $;</td></tr><tr><td>4: Solve Problem (35) for given $ A^{r+1} $ and $ F^{r+1} $, and denote the solution as $ G^{r+1} $;</td></tr><tr><td>5: $ r = r + 1 $;</td></tr><tr><td>6: until the convergence is achieved.</td></tr></table>

Discussions. Algorithm 1 needs to run once the initial taking off locations of the UAVs change. However, the complexity of Algorithm 1 is high as the solutions are iteratively obtained and each subproblem involves a huge number of optimization variables especially when the total number of time slots is high. Precisely, as shown in Algorithm 1, assume that the overall iteration number is $K ^ { r }$ . In each iteration, Problem (29) has $N ( M + 1 ) T$ variables, and it can be ð þ Þsolved by Branch and Bound method, in which the Simplex technique for solving linear programs is used. Thus, the computational complexity is $\overset { \bullet } { \mathcal { O } } ( 2 ^ { N ( M + 1 ) T } )$ in the worst case. Oð ÞFurthermore, according to the analysis in [4], [36], in Problem (35), G has 2MT variables, h has NMT variables. Hence, the total number of variables is N 2 MT . As a result, the ðnumber of iterations required is $\mathcal { O } ( \sqrt { ( N + 2 ) M T } \log _ { 2 } ( \frac { 1 } { \epsilon _ { 1 } } ) )$ , where $\epsilon _ { 1 }$ is the accuracy of SCA for solving Problem (35). Similarly, the overall number of constraints in Problem (35) is $M T ( \bar { 3 } N + 2 ) + T$ . Then, the computational complexity is $\mathcal { O } ( ( ( N + 2 ) M T ) ^ { 2 } \sqrt { ( N + 2 ) M T } \log _ { 2 } ( \frac { 1 } { \epsilon _ { 1 } } ) ( M T \left( 3 N + 2 \right) + T ) )$ , Oððð þ Þ Þ ð þwhich is equivalent to $\mathcal { O } ( 3 ( N M T ) ^ { 3 . 5 } \mathrm { l o g } _ { 2 } ( \frac { 1 } { \epsilon _ { 1 } } ) )$ þ Þ þ ÞÞ. Overall, the total complexity of CAT algorithm is $\bar { \mathcal { O } } ( K ^ { r } ( 2 ^ { N ( M + 1 ) T } +$ $3 ( N M T ) ^ { 3 . 5 } \mathrm { l o g } _ { 2 } ( \textstyle { \frac { 1 } { \epsilon _ { 1 } } } ) ) )$ Oð ð þ. Hence, Algorithm 1 is not suitable for ð Þ ð 1 ÞÞÞsome emergence scenarios (e.g., battlefields, earthquake, large fires), where fast decision making is highly demanded. This motivates the algorithm developed based on DRL in the following section.

# 5 PROPOSED RAT ALGORITHM

To facilitate the fast decision making, the DRL-based RAT algorithm is proposed in this section. We first give some preliminaries as follows.

# 5.1 Preliminaries

# 5.1.1 DQN

In a standard reinforcement learning, an agent is assumed to interact with the environment and select the optimal actions that can maximize the accumulated reward. In [28], a Deep Q Network (DQN) structure developed by Google Deepmind, integrates the deep neural networks with traditional reinforcement learning. The DQN is used to estimate the well-known Q-value defined as

$$
Q (s (t), c (t)) = \mathbb {E} [ Z (t) | s (t), c (t) ], \tag {36}
$$

where $s ( t )$ and $c ( t )$ denote the state and action respectively, $\mathbb { E } [ \cdot ]$ ð Þ ð Þdenotes the expectation, whereas $\begin{array} { r } { Z ( t ) = \sum _ { j ^ { \prime } = t } ^ { T } \dot { \gamma } z ( t ^ { \prime } ) } \end{array}$ is a

reward and $\gamma \in [ 0 , 1 ]$ is the discount factor and $z ( t ^ { \prime } )$ is a 2 ½  ð Þreward function in the t th time step (or time slot). As the objective is to maximize the reward, a widely used policy is $\begin{array} { r } { \pi ( \dot { s } ( t ) | \phi ^ { Q } ) = \operatorname * { a r g m a x } _ { c ( t ) } Q ( s ( t ) , c ( t ) | \phi ^ { Q } ) } \end{array}$ , where $\phi ^ { Q ^ { \star } }$ is the ð ð Þj Þ ¼ ð Þ ð ð Þ ð Þj Þparameter of the deep neural network. Then, the DQN can be trained by minimizing the loss function [28]. Also, since the deep networks are known to be unstable and very difficult to converge, two effective approaches, i.e., target network and experience replay, have been introduced in [28]. The target network has the same structure as the original DQN but the parameters are updated more slowly. The experience replay stores the state transition samples which can help the DQN converge. However, the DQN was originally designed to solve the problem with discrete variables. Although we can adapt the DQN to continuous problems by discretizing the action space, it may unfortunately result in a huge searching space and therefore intractable to deal with.

# 5.1.2 DDPG

To deal with the problem with continuous variables, $\mathrm { e . g . , }$ the trajectory control of UAV, one may apply the actor-critic approach, which was developed in [37]. DeepMind has proposed a deep deterministic policy gradient (DDPG) approach [30] by integrating the actor-critic approach into DRL. DDPG includes two DQNs, one of the DQNs, named actor network with function $\pi ( s ( t ) | \phi ^ { \pi } )$ is applied to generate action $c ( t )$ ð ð Þj Þfor a given state s t . The other DQN named critic ð Þnetwork with function $Q ( s ( t ) , c ( t ) | \phi ^ { Q } )$ , is used to generate ð ð Þ ð Þj Þthe Q-value, which evaluates the action produced by the actor network. In order to improve the learning stability, two adjacent target networks corresponding to the actor and critic networks, $\pi ^ { \prime } ( \cdot ) , Q ^ { \prime } ( \cdot )$ with respective parameters $\phi ^ { \pi ^ { \prime } } , \phi ^ { Q ^ { \prime } } ,$ ð, are also applied.

Then, the critic network can be updated with the loss function, ${ \cal L } ( \phi ^ { Q } )$ , as

$$
L (\phi^ {Q}) = \frac {1}{K} \sum_ {k = 1} ^ {K} \delta_ {k} ^ {2}, \tag {37}
$$

¼where in each time step, the mini-batch randomly samples K constituting experiences from experience replay buffer, and $\delta _ { k }$ is temporal difference (TD)-error [38] which is given by

$$
\begin{array}{l} \delta_ {k} = z (k) + \gamma Q ^ {\prime} (s (k + 1), \pi^ {\prime} (s (k + 1) | \phi^ {\pi^ {\prime}}) | \phi^ {Q ^ {\prime}}) \tag {38} \\ - Q (s (k), \pi (s (k) | \phi^ {\pi}) | \phi^ {Q}). \\ \end{array}
$$

On the other hand, the actor network can be updated by applying the policy gradient, which is described as [30].

$$
\begin{array}{l} \bigtriangledown_ {\phi^ {\pi}} J \approx \frac {1}{K} \sum_ {k = 1} ^ {K} \bigtriangledown_ {c} Q (s, c | \phi^ {Q}) | _ {s = s (k), c = \pi (s (k) | \phi^ {\pi})} \\ = \frac {1}{K} \sum_ {k = 1} ^ {K} \left[ \bigtriangledown_ {c} Q (s, c | \phi^ {Q}) | _ {s = s (k), c = \pi (s (k))} \cdot \bigtriangledown_ {\phi^ {\pi}} \pi (s | \phi^ {\pi}) | _ {s = s (k)} \right]. \tag {39} \\ \end{array}
$$

# 5.2 The RAT Algorithm

In this section, we introduce the DRL based RAT algorithm, which includes deep neural networks (i.e., actor and critic networks) and the matching algorithms. In order to apply the DRL, we first define the state, action and reward as follows:

![](images/910f4622d2ff041bcf63928c4a3477ce40f83b1100ef3b6bdb0dabe24046cf71.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Environment"] --> B["Agent"]
    B -->|Action State| C["State Actor: π(s(t) |Φ^π)"]
    B -->|State Action State| D["State Actor: π(s(t) |Φ^π)"]
    D --> E["Policy Gradient"]
    E --> F["Loss Function"]
    F --> G["Updating Parameter"]
    G --> H["Critic: Q(s(t), c(t)|Φ^Q)"]
    H --> I["Q value"]
    I --> J["Last Step"]
    J --> K["Per"]
    K --> L["Mini-batch"]
    L --> M["Experience Replay Buffer"]
    M --> N["Next State"]
    N --> O["Matching Algorithm"]
    O --> P["Reward [s(t), c(t), z(t), s(t+1)"]]
    P --> Q["Experience"]
    Q --> R["PER"]
    R --> S["Mini-batch"]
    S --> T["Last Step"]
    T --> U["Last Step"]
    U --> V["Policy Gradient"]
    V --> W["Last Step"]
    W --> X["Last Step"]
    X --> Y["Policy Gradient"]
    Y --> Z["Last Step"]
    Z --> AA["Policy Gradient"]
```
</details>

Fig. 2. The structure of RAT algorithm.

1) State $\boldsymbol s ( t ) \colon \boldsymbol s ( t ) = \{ [ X _ { j } ( t ) , Y _ { j } ( t ) , Z _ { j } ] , \forall j \in \mathcal { M } \}$ , s t is ð Þ ð Þ ¼ f½ ð Þ ð Þ  8the set of the coordinates of all UAVs.   
2) Action $c ( t ) \colon c ( t )$ is the set of the actions of all UAVs, ð Þ ð Þincluding the horizontal direction $\theta _ { i } ^ { h } ( t )$ and distance $d _ { j } ( t )$ ð Þ. Then, the action set can be defined as $c ( t ) =$ $\{ [ \theta _ { j } ^ { h } ( t ) , d _ { j } ( t ) ] , \forall j \in \mathcal { M } \}$ .   
f½ ð Þ3) Reward $z ( t ) { : } z ( t )$ 2 Mgis defined as the minus of the overall ð Þ ð Þenergy consumption of all the UEs in each time slot as

$$
z (t) = - \sum_ {i = 1} ^ {N} \sum_ {j = 0} ^ {M} a _ {i j} (t) E _ {i j} (t) - p, \tag {40}
$$

where p is the penalty if any of UAV flies out of the target area, which means (24g) or (24h) is not satisfied.

The algorithm framework used in this paper is depicted in Fig. 2, where an agent, which could be deployed in the control center of the base station, is assumed to interact with the environment. An actor network $\pi ( s ( t ) | \phi ^ { \pi } )$ is ð ð Þj Þapplied to generate the action, which includes the flying direction and distance for each UAV. The critic network $Q ( s ( t ) , c ( t ) | \phi ^ { Q } )$ is used to obtain the Q-value of the action ð ð Þ ð Þj Þ(i.e., to evaluate the action generated by actor network). In each time slot, the agent sends the action generated by actor network to each UAV. Then, each UE tries to associate with one UAV in its coverage, i.e., (12) by using a matching algorithm in Algorithm 3. More specifically, each UE tries to connect the UAV which can save more offloading energy. If the minimum offloading energy is larger than the energy of local execution, the UE will decide to conduct the task locally. Note that RAT has the same optimization strategy for resource allocation as CAT.

Also, each UAV selects the UEs based on the following criteria: 1) UE should be within its coverage area; 2) UE could save more energy, i.e., the more of $\begin{array} { r } { E _ { i j } ^ { \mathrm { L } } ( t ) - E _ { i j } ^ { \mathrm { C } } ( t ) } \end{array}$ will ð Þ  ð Þbe given higher priority in offloading to this UAV. We will introduce the details of the proposed matching algorithm in Algorithm 3. After the matching algorithm, the reward in (40) can be obtained.

We assume that there is an experience replay buffer for the agent to store the experience $[ s ( t ) , c ( t ) , z ( t ) , s ( t + 1 ) ] .$ .

Once the experience replay buffer is full, the learning procedure starts. A mini-batch with K experiences can be obtained from the experience replay buffer to train the networks.

Algorithm 2. RAT Algorithm   
1: Initialize actor network $\pi(s(t)|\phi^{\pi})$ with parameters $\phi^{\pi}$ and critic network $Q(s(t), s(t)|\phi^{Q})$ with parameters $\phi^{Q}$ ;
2: Initialize target networks $Q'(\cdot)$ with parameters $\phi^{Q'} = \phi^{Q}$ and $\pi'(\cdot)$ with parameters $\phi^{\pi'} = \phi^{\pi}$ ;
3: Initialize experience replay buffer X;
4: for epoch = 1, ..., $k_{max}$ do
5: Initialize $s(t)$ ;
6: for time slot $t = 1, \ldots, T$ do
7: $\pi(s(t)|\phi^{\pi}) + \rho N'$ where $N'$ is the random noise and $\rho$ decays with t;
8: for UAV $j = 1, \ldots, M$ do
9: Execute $c(t)$ ;
10: Obtain $s(t + 1)$ ;
11: end for
12: Obtain the user association with UAVs using matching algorithm proposed in Algorithm 3;
13: Obtain the reward $z(t)$ from (40);
14: Store experience $[s(t), c(t), z(t), s(t + 1)]$ into the replay buffer;
15: if the replay buffer is full then
16: for $k = 1, \ldots, K$ do
17: Sample kth experience with probability $P(k)$ from (41);
18: Calculate $|\delta_k|$ and $\omega_k$ from (38) and (42) respectively;
19: end for
20: Update parameters of the critic network $\phi^{Q}$ by minimizing its loss function according to (43);
21: Update parameters of the actor network $\phi^{\pi}$ by using policy gradient approach according to (39);
22: Update two target networks with the updating rate $\tau$ :
23: end if
24: end for
25: end for

In the classical DRL algorithms, such as Q-learning [39], SARSA [40] and DDPG [30], the mini-batch uniformly samples experiences from the experience replay buffer. However, since TD-error in (38) is used to update the Q-value network, experience with high TD-error often indicates the successful attempts. Therefore, a better way to select the experience is to assign different weights to samples. Schaul et al. [31] developed a prioritized experience replay scheme, in which the absolute TD-error $\left| \delta _ { k } \right|$ is used to evaluate the j jprobability of the sampled kth experience from the minibatch. Then, the probability of sampling the kth experience can be given by

$$
P (k) = \frac {p _ {k} ^ {\beta}}{\sum_ {m \in K} p _ {m} ^ {\beta}}, \tag {41}
$$

where $p _ { k } = | \delta _ { k } | + \epsilon , \epsilon = 0 . 0 0 1$ is a positive constant to avoid ¼ j j þ ¼the edge-case of transitions not being revisited if $\lvert \delta _ { k } \rvert \mathrm { i s } 0 , \beta =$ j j0:6 is denoted as a factor to determine the prioritization [31].

However, frequently sampling experiences with high $\left| \delta _ { k } \right|$ j jcan cause divergence and oscillation. To tackle this issue, the importance-sampling weight [41] is introduced to represent the importance of sampled experience, which can be given by

$$
\omega_ {k} = \frac {1}{(X \cdot P (k)) ^ {\mu}}, \tag {42}
$$

where X is size of experience replay buffer, $\mu$ is given as 0.4 [31]. Thus, the loss function $L ( { \dot { \phi } } ^ { Q } )$ in (37) is updated as

$$
L (\phi^ {Q}) = \frac {1}{K} \sum_ {k = 1} ^ {K} \omega_ {k} \delta_ {k} ^ {2}, \tag {43}
$$

which is used in our proposed RAT to train the networks. Next, we describe the pseudo code of the overall RAT framework in Algorithm 2.

We first initialize the actor, critic, two target networks, and experience replay buffer in Line 1-3. In the beginning of each epoch, all UAVs start to serve UEs from different taking off points. Note that for better exploration, we add a random noise $N ^ { \prime }$ to the action, where $N ^ { \prime }$ follows a normal distribution with 0 mean and variance 1, $\rho$ is set to 2 and decays with a rate of 0.9995 in each time step. From Line 8-11, each UAV flies according to the generated action c t and enters the ð Þnext state s t  1 . Then, we obtain the user association by ð þ Þusing Algorithm 3. Next, the reward z t is obtained according to (40) $( \mathrm { i . e . , }$ ð ÞLine 13). The experience is also stored in the replay buffer. When the buffer is full, the mini-batch samples K experiences by applying the prioritized experience replay (i.e., Line 16-19). Then, we update the actor and critic networks by using loss function in (43) and policy gradient in (39) respectively. Finally, we update the target networks by using the following equations as (i.e., Line 22)

$$
\phi^ {Q ^ {\prime}} \leftarrow \tau \phi^ {Q} + (1 - \tau) \phi^ {Q ^ {\prime}}, \tag {44}
$$

and

$$
\phi^ {\pi^ {\prime}} \leftarrow \tau \phi^ {\pi} + (1 - \tau) \phi^ {\pi^ {\prime}}, \tag {45}
$$

where t is the updating rate.

Next, we introduce the low-complexity matching algorithm which can decide the user association and resource allocation given UAVs’ trajectories, as shown in Algorithm 3. First, we denote A with size N to record the user association between UEs and UAVs. If $A ( i ) = j ,$ , the ith UE matches with the jth UAV, while if $A ( i ) = 0$ Þ ¼, the ith UE is not matched yet ð Þ ¼and has to execute its task locally. In addition, we denote a preference list $E _ { j }$ for the jth UAV to record UEs that can benefit from offloading. Then, from Line 2 to 10, we generate the preference list $E _ { j }$ for the jth UAV. Precisely, if constraint (12) is met, we obtain $E _ { i j } ^ { \mathrm { L } } ( t ) , \dot { E } _ { i j } ^ { \mathrm { T r } } ( t )$ , and $f _ { i j } ^ { \mathrm { C } } ( t )$ according to (19), ð Þ ð Þ ð Þ(17), and (27), respectively. UEs that benefit from offloading will be stored in $\bar { E _ { j } }$ . Since UAVs need to save as much energy of UEs as possible, we sort the preference list $E _ { j }$ with descending order with respect to $\hat { E _ { i j } ^ { \mathrm { L } } } ( t ) - \hat { E _ { i j } ^ { \mathrm { T r } } } ( t )$ , as shown in ð Þ  ð ÞLine 11. The UE that can save more energy via offloading will be matched with a higher priority. Next, from Line 13 to 23, we conduct the matching process. Each UAV keeps selecting UEs according to its preference list, and constantly checking the constraints (4) and (23) based on A. In the meantime, the selected UE will determine whether to match with the UAV or not. Precisely, from Line 17 to 19, if the selected UE is not matched before, or matching with the jth UAV

could save more energy than previous match, the corresponding A i will be updated. We do this process until all ð Þthe UEs in each preference list are checked. Then, the final user association can be obtained from A.

Algorithm 3. Matching Algorithm   
1: Initialize A and $F_{j}, \forall j \in M, \forall i \in N;$ 2: for UAV $j = 1, \ldots, M$ do
3:    for UE $i = 1, \ldots, N$ do
4:    if (12) is met then
5:    Calculate $E_{ij}^{\mathrm{L}}(t), E_{ij}^{\mathrm{Tr}}(t)$ and $f_{ij}^{\mathrm{C}}(t);$ 6:    if $E_{ij}^{\mathrm{L}}(t) > E_{ij}^{\mathrm{Tr}}(t)$ then
7:    Store i into $E_{j};$ 8:    end if
9:    end if
10: end for
11: Sort the element in $E_{j}$ in descending order with respect to $E_{ij}^{\mathrm{L}}(t) - E_{ij}^{\mathrm{Tr}}(t);$ 12: end for
13: repeat
14: for UAV $j = 1, \ldots, M$ do
15: $i = GetTopItem(E_{j})$ ;
16:    if (4), (23) are met then
17:    if $E_{ij}^{\mathrm{Tr}}(t) < E_{iA(i)}^{\mathrm{Tr}}(t)$ or $A(i) = 0$ then
18: $A(i) = j;$ 19:    end if
20:    RemoveTopItem( $E_{j}$ );
21:    end if
22: end for
23: until Each UE in $E_{j}$ is checked.
24: Return A

According to [30], our RAT algorithm is an offline learning and off-policy DRL-based algorithm as the experience replay mechanism is applied, and the mini-batch will sample several uncorrelated experiences for training networks in each time step. Additionally, the training procedure can be deployed in a simulator, and the RAT model can be easily deployed in reality when the convergence is achieved, which will inevitably reduce the payoff of implementation. Furthermore, once the whole networks are converged, the solutions can be generated very fast with only some simple algebraic calculations instead of solving the original MINLP. This is due to the fact that during the training stages, random taking off points of all the UAVs are generated and the networks are trained to converge.

Discussions. after adequate training process, the RAT model, including the networks is saved for testing. In each time slot, the action of all UAVs is generated together by actor network. In our paper, as the fully-connected hidden layers are applied, the computational complexity for generating action of UAVs is $\begin{array} { r } { \hat { \mathcal { O } } \big ( \sum _ { l = 1 } ^ { L } n _ { l } \cdot n _ { l - 1 } \big ) ^ { * } } \end{array}$ , where L is the O ¼  number of network layers, n is the number of neurons in the lth layer. Then, the computational complexity of matching algorithm is NM . The overall complexity of RAT Oð Þalgorithm in testing process is $\begin{array} { r } { \mathcal { O } \big ( ( \sum _ { l = 1 } ^ { L } n _ { l } \cdot \hat { n _ { l - 1 } } + \mathbf { \bar { N } } M ) T \big ) } \end{array}$ .

# 6 EXTENSION TO 3-D CHANNEL MODEL

In this section, in order to consider the more practical environment and the impacts of blockage and shadowing, we extend the previous free-space to 3-D channel model proposed in [13]. In each time slot, we assume the UAV can fly with a vertical direction $\theta _ { j } ^ { v } ( t ) \in [ 0 , \pi ]$ , a horizontal direction $\theta _ { i } ^ { h } ( t ) \in [ 0 , 2 \pi ]$ ð Þ 2 ½ , and a flying distance $d _ { j } ( t ) \in [ 0 , d ^ { \operatorname* { m a x } } ]$ . We ð Þ 2 ½  ð Þ 2 ½ define the coordinate of the jth UAV in the tth time slot as $\begin{array} { r } { [ X _ { j } ( t ) , Y _ { j } ( t ) , Z _ { j } ( t ) ] , \quad \mathrm { w h e r e } \quad X _ { j } ( t ) = X _ { j } ( 0 ) + \sum _ { l = 1 } ^ { t } d _ { j } ( l ) } \end{array}$ sin $\begin{array} { r } { \big ( \theta _ { j } ^ { \bar { v } } ( l ) \big ) \cos \big ( \theta _ { j } ^ { h } ( l ) \big ) , \qquad Y _ { j } ( t ) = X _ { j } ( 0 ) + \sum _ { l = 1 } ^ { t } d _ { j } ( l ) \sin \big ( \theta _ { j } ^ { v } ( l ) \big ) } \end{array}$ sin $\begin{array} { r } { \big ( \theta _ { j } ^ { \hbar } ( l ) \big ) , Z _ { j } ( \dot { t } ) = Z _ { j } ( 0 ) + \sum _ { l = 1 } ^ { t } } \end{array}$ ðcos $\left( \theta _ { j } ^ { v } ( l ) \right)$ ¼ ð Þ, and $[ X _ { j } ( 0 ) , \dot { Y } _ { j } ( 0 )$ ; $\check { Z _ { j } } ( 0 ) \check { ] }$ ð Þ ¼ ð Þ þ ¼  ð Þ ½ ð Þ ð Þis the initial coordinate of the UAV. For collision ð Þavoidance, we consider

$$
Z ^ {\min} \leq Z _ {j} (t) \leq Z ^ {\max}, \forall t \in \mathcal {T}, \tag {46}
$$

where $Z ^ { \mathrm { m i n } }$ and $Z ^ { \mathrm { m a x } }$ are the minimal and maximal flying altitude of the UAV.

Thus, the distance between the jth UAV and the ith UE in tth time slot is given by

$$
d _ {i j} (t) = \sqrt {\left(X _ {j} (t) - x _ {i}\right) ^ {2} + \left(Y _ {j} (t) - x _ {i}\right) ^ {2} + Z _ {j} ^ {2} (t)}, \tag {47}
$$

$$
\forall j \in \mathcal {M}, i \in \mathcal {N}, t \in \mathcal {T}.
$$

The coverage radius of the jth UAV in the tth time slot can be given by

$$
R _ {j} ^ {\max} (t) = Z _ {j} (t) \tan (\theta^ {\max}). \tag {48}
$$

The mean path loss between the jth UAV and the ith UE in the tth time slot can be expressed as [13]

$$
L _ {i j} (t) = \frac {\eta_ {\mathrm{LoS}} - \eta_ {\mathrm{NLoS}}}{1 + a \exp (- b (\theta_ {i j} (t) - a))} + 2 0 \log_ {1 0} \left(d _ {i j} (t)\right) \tag {49}
$$

$$
+ 2 0 \log_ {1 0} \left(\frac {4 \pi f _ {c}}{c}\right) + \eta_ {\mathrm{NLoS}},
$$

where $\eta _ { \mathrm { L o S } } , ~ \eta _ { \mathrm { N L o S } }$ are the path loss of achieving LoS and NLoS links, a and b are constant values that can be obtained in [13], $\begin{array} { r } { \theta _ { i j } ( t ) = \arctan ( \frac { Z _ { j } ( t ) } { R _ { i i } ( t ) } ) } \end{array}$ is the elevation angle between ð Þ ¼the UAV and the $\mathrm { U E } , f _ { c }$ ð ÞÞis the carrier frequency, and c is the light speed. Then, we can show the data rate as follows:

$$
r _ {i j} (t) = B \log_ {2} \left(1 + \frac {P ^ {\mathrm{Tr}}}{\sigma^ {2}} 1 0 ^ {- \frac {L _ {i j} (t)}{1 0}}\right). \tag {50}
$$

Additionally, we consider to maximize the energy efficiency of UAVs and motivated by [42], we show the power consumed by the jth UAV in the tth time slot as follows

$$
\begin{array}{l} P _ {j} (t) = P _ {o} \left(1 + 3 \left(\frac {v _ {j} (t)}{U _ {b}}\right) ^ {2}\right) + P _ {s} \left(\sqrt {1 + \frac {1}{4} \left(\frac {v _ {j} (t)}{V _ {h}}\right) ^ {4}} - \frac {1}{2} \left(\frac {v _ {j} (t)}{V _ {h}}\right) ^ {2}\right) ^ {\frac {1}{2}} \\ + \frac {\pi}{2} d _ {0} \rho_ {a} r _ {s} R _ {r} ^ {2} v _ {j} (t) ^ {3} + w g v _ {j} (t) \cos \left(\theta_ {j} ^ {v} (t)\right), \tag {51} \\ \end{array}
$$

where $P _ { o }$ and $P _ { s }$ are fixed constants that can be obtained in $[ 4 3 ] , U _ { b }$ is the tip speed of the rotor blade, $V _ { h }$ denotes the mean rotor induced velocity when hovering, $d _ { 0 }$ is the drag ratio of main body, $\rho _ { a }$ is the air density, $r _ { s }$ is the rotor solidity, R means the rotor radius, w is the weight of $\mathrm { U A V } ,$ , and g is the gravity acceleration.

Thus, the remaining energy of the jth UAV in the tth time slot is defined as

$$
e _ {j} (t) = e ^ {\max} - \sum_ {l = 1} ^ {t} P _ {j} (l) T ^ {\max}, \tag {52}
$$

where $e ^ { \mathrm { m a x } }$ is the maximal energy of each UAV.

Thus, the optimization problem can be written as follows:

$$
\mathcal {P} 1: \min _ {\boldsymbol {U}, \boldsymbol {A}, \boldsymbol {F}} \sum_ {t = 1} ^ {T} \left(\sum_ {j = 0} ^ {M} \sum_ {i = 1} ^ {N} a _ {i j} (t) E _ {i j} (t) + k _ {z} \sum_ {j = 1} ^ {M} P _ {j} (t) T ^ {\max}\right) \tag {53a}
$$

subject to: 24b ; 24c ; 24d ; 24e ; 24f ;

$$
(2 4 \mathrm{g}), (2 4 \mathrm{h}), (2 4 \mathrm{j}), (2 4 \mathrm{k}), \tag {53b}
$$

$$
0 \leq \theta_ {j} ^ {v} (t) \leq \pi , \forall j \in \mathcal {M}, t \in \mathcal {T},
$$

$$
Z ^ {\min} \leq Z _ {j} (t) \leq Z ^ {\max}, \forall j \in \mathcal {M}, t \in \mathcal {T}, \tag {53c}
$$

$$
a _ {i j} (t) R _ {i j} (t) \leq R _ {j} ^ {\max} (t), \forall i \in \mathcal {N}, j \in \mathcal {M}, t \in \mathcal {T}. \tag {53d}
$$

where $U = \{ \theta _ { j } ^ { v } ( t ) , \theta _ { j } ^ { h } ( t ) , d _ { j } ( t ) , \ \forall j \in \mathcal { M } , t \in T \}$ , $k _ { z }$ is the ¼ fweight factor.

To solve the above problem, we define the state and action as follows:

1) State $\boldsymbol { s } ( t ) \colon \boldsymbol { s } ( t ) = \{ [ X _ { j } ( t ) , Y _ { j } ( t ) , Z _ { j } ( t ) , e _ { j } ( t ) ] , \ \forall j \in \mathcal { M } \}$ .   
2) Action $c ( t ) \colon$ ð Þ ¼ f½ ð Þ ð Þ ð Þ ð Þ 8 2the action set can be defined as $c ( t ) =$ $\{ [ \theta _ { j } ^ { v } ( t ) , \theta _ { j } ^ { h } ( t ) , d _ { j } ( t ) ] , \ \forall j \in \mathcal { M } \} .$ .   
f½ ð Þ ð Þ ð Þ 8 2 Mg3) Reward z t : we define the reward as follows

$$
z (t) = - \sum_ {j = 0} ^ {M} \sum_ {i = 1} ^ {N} a _ {i j} (t) E _ {i j} (t) - k _ {z} \sum_ {j = 1} ^ {M} P _ {i} (t) T ^ {\max} - p, \tag {54}
$$

where $p$ is the penalty if any of UAV flies out of the target area, i.e., if (24g), (24h) or (53c) is not satisfied.

Thus, having defined the state, action and reward, the above problem can be solved by the proposed RAT algorithm as introduced before.

# 7 SIMULATION RESULTS

In this section, both convex optimization-based CAT and DRL-based RAT are evaluated with simulations implemented on Intel i5-3450t, NVIDIA GTX 1050Ti, Python $3 . 6 ,$ , PULP 1.6.10, CVXPY 1.1.7, and Tensorflow 1.15.0. We deploy three fully-connected hidden layers with 1,024, 800 and 600 neurons in both actor and critic networks in RAT. The actor network is trained by applying RMSPropOptimizer with the learning rate 0.001, whereas the critic network is trained by using AdamOptimzer with the learning rate 0.001. In the simulation, we assume there are 60 time slots in each training epoch. There are 100 UEs randomly distributed in a rectangle-shaped area with the side length of $X ^ { \mathrm { m a x } } = 4 0 0$ m and $Y ^ { \mathrm { m a x } } = 4 0 0 ~ \mathrm { m }$ . Additionally, there are 2 ¼ ¼UAVs deployed to serve UEs within the target area. Note that for RAT, each UAV has 20 different taking off points during the training procedure. Besides, in each time slot, UE generates a task with communication requirement $D _ { i } ( t ) \bar { \in } \left[ 1 0 , 5 0 \right] \ \mathrm { K B }$ and computation requirement $F _ { i } ( t ) \in$ $[ 2 \times 1 0 ^ { 9 } , 2 \times 1 0 ^ { 1 0 } ]$ cycles. Other parameters are summarized ½ 	 	 in Table 2. We assume in each time slot, UAVs will send a signal to activate the corresponding UEs, which will either offload the task or execute locally, within the delay requirement.

TABLE 2 Simulation Parameters 

<table><tr><td>Parameters</td><td>Settings</td><td>Parameters</td><td>Settings</td></tr><tr><td> $T$ </td><td>60</td><td> $N$ </td><td>100</td></tr><tr><td> $M$ </td><td>2</td><td> $V^{\max}$ </td><td>30</td></tr><tr><td> $d^{\max}$ </td><td>30 m</td><td> $T^{\max}$ </td><td>1 s</td></tr><tr><td> $X^{\max}$ </td><td>400 m</td><td> $Y^{\max}$ </td><td>400 m</td></tr><tr><td> $\theta^{\max}$ </td><td> $\frac{\pi}{4}$ </td><td> $Z_{j}(0)$ </td><td>75 m</td></tr><tr><td> $v_{i}$ </td><td>3</td><td> $g_{0}$ </td><td> $1.42 \times 10^{-4}$ </td></tr><tr><td> $P^{\text{Tr}}$ </td><td>0.1 W</td><td> $B$ </td><td>10 MHz</td></tr><tr><td> $\sigma^{2}$ </td><td>-90 dbm</td><td> $e^{\max}$ </td><td> $10^{6}$  J</td></tr><tr><td> $k_{i}$ </td><td> $10^{-28}$ </td><td> $f^{\max}$ </td><td>100 GHz</td></tr><tr><td> $\gamma$ </td><td>0.999</td><td> $p$ </td><td>100</td></tr><tr><td> $k^{\max}$ </td><td>3000</td><td> $\rho$ </td><td>2</td></tr><tr><td> $w$ </td><td>2 kg</td><td> $g$ </td><td>10 m/s $^{2}$ </td></tr><tr><td> $\tau$ </td><td>0.001</td><td> $Z^{\min}$ </td><td>50 m</td></tr><tr><td> $Z^{\max}$ </td><td>120 m</td><td> $\eta_{\text{LoS}}$ </td><td>1.6</td></tr><tr><td> $\eta_{\text{NLoS}}$ </td><td>23</td><td> $a$ </td><td>12.08</td></tr><tr><td> $b$ </td><td>0.11</td><td> $f_{c}$ </td><td>2.5 GHz</td></tr><tr><td> $c$ </td><td> $3 \times 10^{8}$  m/s</td><td> $k_{z}$ </td><td>0.0025</td></tr><tr><td> $P_{o}$ </td><td>79.86</td><td> $U_{b}$ </td><td>120 m/s</td></tr><tr><td> $P_{s}$ </td><td>88.63</td><td> $V_{h}$ </td><td>4.03</td></tr><tr><td> $d_{0}$ </td><td>0.6</td><td> $\rho_{a}$ </td><td>1.25 kg/m $^{3}$ </td></tr><tr><td> $r_{s}$ </td><td>0.05</td><td> $R_{r}$ </td><td>0.4 m</td></tr></table>

In order to evaluate the performance of the proposed CAT and RAT, we present the following three algorithms for comparison purpose.

Local Execution (LE): All tasks are executed locally without offloading.   
Random moving (RM): In this setting, each UAV randomly selects the horizontal direction and flying distance to take.   
Cluster moving (CM): We group all the UEs into 10 clusters and each UAV flies in the trajectory connecting all the cluster center one by one. Note that it takes $\textstyle { \frac { T } { 1 0 } }$ time slots for each UAV to move from one cluster center to another one.   
Deep Deterministic Policy Gradient (DDPG) [30]: We set the parameter of DDPG the same as actor and critic networks of RAT, but do not apply the prioritized experience replay. In other words, DDPG uniformly samples the experiences from the experience replay buffer in the training procedure.

Note that both RM, CM, DDPG apply the matching algorithm proposed in Algorithm 3 to decide the user association and resource allocation.

# 7.1 Convergence Evaluation of CAT and RAT

In this subsection, we show the convergence of proposed CAT and RAT. In Fig. 3, we depict the convergence performance of CAT with three different pairs of initial trajectories. Specifically, we group all UEs into one cluster and the UAVs fly in a circle around the cluster center with radius 80 m, 100 m, and 120 m respectively. We denote these three pairs of UAV trajectories as the initial trajectories. As shown in Fig. 3, we can conclude that for any initial trajectory, the overall energy consumption of UEs achieved by CAT always decreases and finally remains stable after several iteration times. However, one can also observe that the convergent solution achieved by CAT will be influenced by the initial trajectory.

![](images/63e9ee344320f8e956182c5fbc93431b22102c53f130cd619c2e5c32c07fd4e9.jpg)

<details>
<summary>line</summary>

| Iteration Times | CAT with Radius 80m | CAT with Radius 100m | CAT with Radius 120m |
| --------------- | ------------------- | -------------------- | -------------------- |
| 0               | 478                 | 505                  | 530                  |
| 10              | 472                 | 495                  | 515                  |
| 20              | 468                 | 488                  | 505                  |
| 30              | 465                 | 482                  | 498                  |
| 40              | 463                 | 478                  | 492                  |
| 50              | 462                 | 475                  | 488                  |
| 60              | 461                 | 473                  | 485                  |
| 70              | 460                 | 472                  | 483                  |
| 80              | 460                 | 471                  | 482                  |
| 90              | 460                 | 470                  | 481                  |
| 100             | 460                 | 469                  | 480                  |
</details>

Fig. 3. The convergence performance of proposed CAT.

![](images/8dba342fd6fc06d99c3133298065554c7db909dc6d545cc8d8f7a8c6561b81ab.jpg)

<details>
<summary>line</summary>

| Training Epoch | RAT with Batch Size 128 | RAT with Batch Size 256 | RAT with Batch Size 512 |
| -------------- | ------------------------ | ------------------------ | ------------------------ |
| 0              | 650                      | 650                      | 650                      |
| 200            | 640                      | 640                      | 640                      |
| 400            | 630                      | 630                      | 630                      |
| 600            | 620                      | 620                      | 620                      |
| 800            | 580                      | 580                      | 580                      |
| 1000           | 550                      | 550                      | 550                      |
| 1200           | 520                      | 520                      | 520                      |
| 1400           | 480                      | 480                      | 480                      |
</details>

(a) The overall energy consumption of RAT with different batch size.

![](images/184c345f681cbe302ae6db2ef17f546a26a9fd0430b88808ce88bad581ffd59d.jpg)

<details>
<summary>line</summary>

| Training Epoch | DDPG with Batch Size 128 | DDPG with Batch Size 236 | DDPG with Batch Size 512 |
| -------------- | ------------------------ | ------------------------ | ------------------------ |
| 0              | 650                      | 650                      | 650                      |
| 200            | 640                      | 640                      | 640                      |
| 400            | 630                      | 630                      | 630                      |
| 600            | 620                      | 620                      | 620                      |
| 800            | 610                      | 610                      | 610                      |
| 1000           | 590                      | 590                      | 590                      |
| 1200           | 570                      | 570                      | 570                      |
| 1400           | 550                      | 550                      | 550                      |
</details>

(b） The overall energy consumption of DDPG with different batch size.

Fig. 4. The convergence performance of RAT and DDPG with different size of mini-batch.   
![](images/0e157b054ead46f46dd287affd15004c76837991443d6e15ce850ba6724af1a3.jpg)

<details>
<summary>line</summary>

| Training Epoch | RAT with Buffer Size 10000 | RAT with Buffer Size 30000 | RAT with Buffer Size 50000 |
| -------------- | -------------------------- | -------------------------- | -------------------------- |
| 0              | 650                        | 650                        | 650                        |
| 200            | 450                        | 600                        | 650                        |
| 400            | 550                        | 550                        | 650                        |
| 600            | 500                        | 500                        | 650                        |
| 800            | 450                        | 450                        | 650                        |
| 1000           | 450                        | 450                        | 450                        |
| 1200           | 450                        | 450                        | 450                        |
| 1400           | 450                        | 450                        | 450                        |
</details>

(a） The overall energy consumption of RAT with different buffer size.

![](images/510fc8dc4803e60411ffa0b8c16a10778deba9490324e310382845b6fa1b8f69.jpg)

<details>
<summary>line</summary>

| Training Epoch | DDPG with Buffer Size 10000 | DDPG with Buffer Size 30000 | DDPG with Buffer Size 50000 |
| -------------- | --------------------------- | --------------------------- | --------------------------- |
| 0              | 650                         | 650                         | 650                         |
| 200            | 670                         | 660                         | 660                         |
| 400            | 680                         | 670                         | 670                         |
| 600            | 690                         | 680                         | 680                         |
| 800            | 700                         | 690                         | 690                         |
| 1000           | 690                         | 680                         | 680                         |
| 1200           | 680                         | 670                         | 670                         |
| 1400           | 670                         | 660                         | 660                         |
</details>

(b） The overall energy consumption of DDPG with different buffer size.   
Fig. 5. The convergence performance of RAT and DDPG with different experience replay buffer.

Then, we show the convergence performance of RAT in training process. From Figs. 4 to 5, we compare the influence of hyperparameters to both DDPG and RAT. Prioritized experience replay is applied in RAT. Both RAT and DDPG start the learning procedure once the experience replay buffer is full. In Fig. 4, we depict the overall energy consumption of RAT and DDPG for different size of minibatches, where the size of experience replay buffer is 50000. To be more specific, from Fig. 4a, we can see that RAT has the similar convergence performance for different size of mini-batches and it becomes more stable during the learning procedure. In Fig. 4b, when the batch size is 128, DDPG has an obvious fluctuation during the learning procedure. When the batch size is 256, the convergence performance of DDPG becomes worse after the 1400th epoch. While DDPG can only have a promising convergence performance when the batch size is 512. Overall, from Fig. 4, it is clear to see that the RAT is less sensitive to the change of mini-batch than DDPG.

![](images/9937435bd0f8922203ffe942dd2ed45952572923a9e66dc725f29dff2f20fb86.jpg)

<details>
<summary>scatter</summary>

| Point | Type  | X (m) | Y (m) |
|-------|-------|-------|-------|
| 1     | UAV1  | 30    | 50    |
| 2     | UAV1  | 20    | 350   |
| 3     | UAV1  | 100   | 250   |
| 4     | UAV1  | 15    | 200   |
| 5     | UAV1  | 80    | 100   |
| 6     | UAV1  | 120   | 200   |
| 7     | UAV1  | 140   | 220   |
| 8     | UAV1  | 130   | 210   |
| 9     | UAV1  | 110   | 180   |
| 10    | UAV1  | 90    | 150   |
| 11    | UAV1  | 70    | 120   |
| 12    | UAV1  | 60    | 100   |
| 13    | UAV1  | 50    | 80    |
| 14    | UAV1  | 40    | 60    |
| 15    | UAV1  | 30    | 50    |
| 16    | UAV1  | 20    | 40    |
| 17    | UAV1  | 15    | 35    |
| 18    | UAV1  | 10    | 30    |
| 19    | UAV1  | 8     | 25    |
| 20    | UAV1  | 6     | 20    |
| 21    | UAV1  | 5     | 15    |
| 22    | UAV1  | 4     | 10    |
| 23    | UAV1  | 3     | 8     |
| 24    | UAV1  | 2     | 6     |
| 25    | UAV1  | 1     | 5     |
| 26    | UAV1  | 0     | 4     |
| 27    | UAV1  | -1    | 3     |
| 28    | UAV1  | -2    | 2     |
| 29    | UAV1  | -3    | 1     |
| 30    | UAV1  | -4    | 0     |
| 31    | UAV1  | -5    | -1    |
| 32    | UAV1  | -6    | -2    |
| 33    | UAV1  | -7    | -3    |
| 34    | UAV1  | -8    | -4    |
| 35    | UAV1  | -9    | -5    |
| 36    | UAV1  | -10   | -6    |
| 37    | UAV1  | -11   | -7    |
| 38    | UAV1  | -12   | -8    |
| 39    | UAV1  | -13   | -9    |
| 40    | UAV1  | -14   | -10   |
| 41    | UAV1  | -15   | -11   |
| 42    | UAV1  | -16   | -12   |
| 43    | UAV1  | -17   | -13   |
| 44    | UAV1  | -18   | -14   |
| 45    | UAV1  | -19   | -15   |
| 46    | UAV1  | -20   | -16   |
| 47    | UAV1  | -21   | -17   |
| 48    | UAV1  | -22   | -18   |
| 49    | UAV1  | -23   | -19   |
| 50    | UAV1  | -24   | -20   |
| 51    | UAV1  | -25   | -21   |
| 52    | UAV1  | -26   | -22   |
| 53    | UAV1  | -27   | -23   |
| 54    | UAV1  | -28   | -24   |
| 55    | UAV1  | -29   | -25   |
| 56    | UAV1  | -30   | -26   |
| 57    | UAV1  | -31   | -27   |
| 58    | UAV1  | -32   | -28   |
| 59    | UAV1  | -33   | -29   |
| 60    | UAV1  | -34   | -30   |
| 61    | UAV1  | -35   | -31   |
| 62    | UAV1  | -36   | -32   |
| 63    | UAV1  | -37   | -33   |
| 64    | UAV1  | -38   | -34   |
| 65    | UAV1  | -39   | -35   |
| 66    | UAV1  | -40   | -36   |
| 67    | UAV1  | -41   | -37   |
| 68    | UAV1  | -42   | -38   |
| 69    | UAV1  | -43   | -39   |
| 70    | UAV1  | -44   | -40   |
| 71    | UAV1  | -45   | -41   |
| 72    | UAV1  | -46   | -42   |
| 73    | UAV1  | -47   | -43   |
| 74    | UAV1  | -48   | -44   |
| 75    | UAV1  | -49   | -45   |
| 76    | UAV1  | -50   | -46   |
| 77    | UAV1  | -51   | -47   |
| 78    | UAV1  | -52   | -48   |
| 79    | UAV1  | -53   | -49   |
| 80    | UAV1  | -54   | -50   |
| 81    | UAV1  | -55   | -51   |
| 82    | UAV1  | -56   | -52   |
| 83    | UAV1  | -57   | -53   |
| 84    | UAV1  | -58   | -54   |
| 85    | UAV1  | -59   | -55   |
| 86    | UAV1  | -60   | -56   |
| 87    | UAV1  | -61   | -57   |
| 88    | UAV1  | -62   | -58   |
| 89    | UAV1  | -63   | -59   |
| 90    | UAV1  | -64   | -60   |
| 91    | UAV1  | -65   | -61   |
| 92    | UAV1  | -66   | -62   |
| 93    | UAV1  | -67   | -63   |
| 94    | UAV1  | -68   | -64   |
| 95    | UAV1  | -69   | -65   |
| 96    | UAV1  | -70   | -66   |
| 97    | UAV1  | -71   | -67   |
| 98    | UAV1  | -72   | -68   |
| 99    | UAV1  | -73   | -69   |
| Note: The data is already in CSV format as it is not available in the image. The extracted data is presented in the code itself. The extracted data is presented in the format as follows: (e.g., “UAV” or “UE”). The extracted data is presented in the format as follows: (e.g., “UAV” or “UE”).
</details>

Fig. 6. Multi-UAV enabled F-MEC controlled by RAT.

![](images/4ef0b57817b4b29c3db5a9ed73d57a3c144d77bcc52814033802aee9ea46fb65.jpg)  
Fig. 7. Multi-UAV enabled F-MEC controlled by CAT.

In Fig. 5, we depict the overall energy consumption of RAT and DDPG for different sizes of experience replay buffer, where the size of mini-batch is set as 128. From Figs. 5a and 5b, when the buffer size is 10000, the proposed RAT finally remains stable between 450 J and 500 J, although it has an obvious fluctuation during the learning process. The DDPG has no convergence tendency during the entire learning procedure. When the buffer size is 50000, DDPG becomes worse after 1000th epoch, and finally reaches 550 J. Overall, we can observe that DDPG can only have a promising performance when the buffer size is 30000, while RAT can always converge and remain stable during the learning procedure, no matter which the buffer size is. Thus, we can conclude that RAT is less sensitive to the size of experience replay buffer than DDPG.

# 7.2 Trajectory Evaluation of CAT and RAT

In Figs. 6 and 7, we show the trajectories obtained by RAT and CAT, respectively. Note that during the training procedure, the UAVs controlled by RAT always starts to serve UEs from 20 different taking off points. Additionally, for fairness, the UAVs controlled by CAT have the same taking off points as RAT. For the initial trajectories, we group all the UEs into 6 clusters and each UAV flies in the trajectory connecting all cluster centers one by one. Note that the iteration number of CAT is 10.

![](images/0154c2f2e3b71b03900b265b4383df0a522b1aacedcd628796d3b38e29194dde.jpg)  
(a) The overall energy consumption ofRAT,CAT,RM,CM,LE with different taking off points.

![](images/3db68b759039caca56cda607b3d76dd9d6c9146238b68558dd0f0af4585bbb61.jpg)

<details>
<summary>line</summary>

| Number of Time Slits | RAT  | CM   | LE   | CAT  | RM   |
| -------------------- | ---- | ---- | ---- | ---- | ---- |
| 5                    | 100  | 100  | 100  | 100  | 100  |
| 15                   | 150  | 150  | 200  | 150  | 200  |
| 25                   | 200  | 200  | 300  | 200  | 300  |
| 35                   | 250  | 250  | 400  | 250  | 400  |
| 45                   | 300  | 300  | 500  | 300  | 500  |
| 55                   | 350  | 350  | 600  | 350  | 600  |
| 60                   | 400  | 400  | 700  | 400  | 700  |
</details>

(b） The overall energy consumption ofRAT,CAT,RM,CM,LE in different number of time slots.   
Fig. 8. The performance comparison of RAT, CAT, RM, CM, and LE.

As shown in Fig. $^ { 6 , }$ we randomly select 5 pairs of taking off points for comparison. One can observe that no matter which the taking off points of the UAVs are, the proposed RAT can guide the UAVs to their certain areas and move around to serve different UEs. This is due to the fact that we train the RAT to converge during the training stage by randomly generating several taking off points of the UAVs. Then, during the testing stage, RAT can intermediately output the best solutions once taking off points are given.

In Fig. 7, one can also see that the trajectories obtained by CAT are similar with the initial trajectories. This may indicate that CAT may fall into the local optimum, whereas the proposed RAT has the global search ability due to the exploration feature of DRL.

# 7.3 Energy Consumption Evaluation of CAT and RAT

In Fig. 8, we compare the performance of RAT, CAT, CM, RM and LE in terms of energy consumption of UEs. As shown in Fig. 8a, we depict the overall energy consumption of UEs achieved by RAT, CAT, CM, RM, and LE with different taking off points. It is obvious to see that LE has the worst performance. This is because all UEs execute their tasks locally without offloading, which will inevitably consume more energy. RM outperforms LE but it fluctuates with the index of taking off points. CM has better performance than RM, which always remains between 520 J and 550 J. CAT outperforms LE, RM, and CM, which remains about 500 J. Additionally, one can observe that RAT achieves the best performance, as expected.

Furthermore, we depict the overall energy consumption of UEs achieved by RAT, CAT, RM, CM, and LE in different number of time slots in Fig. 8b, with the index of taking off points setting as 1. It is readily to see that both the energy consumption of RAT, CAT, RM, CM, and LE increase as the number of time slots increases. LE performs the worst, which consumes above 700 J eventually. Additionally, we can observe that RAT outperforms other algorithms. Moreover, CAT still has considerable performance, which is only slightly worse than RAT.

In Table 3, we show the time consumed by CAT and RAT for each pair of taking off points in Fig. 8. Note that RAT is trained for 3,000 epochs, while the iteration number of CAT is 10. One can see that for all the taking off points, the proposed CAT takes over 1,400 seconds to find solutions, while RAT only takes 1.2 seconds in average, although it takes longer time in training process. This is because once the

TABLE 3 Executed Time of CAT and RAT 

<table><tr><td rowspan="2">Index</td><td rowspan="2">CAT (s)</td><td colspan="2">RAT</td></tr><tr><td>Training (s)</td><td>Testing (s)</td></tr><tr><td>1</td><td>1405.23</td><td>10534.88</td><td>1.23</td></tr><tr><td>2</td><td>1491.74</td><td></td><td>1.22</td></tr><tr><td>3</td><td>1460.46</td><td></td><td>1.20</td></tr><tr><td>4</td><td>1445.11</td><td></td><td>1.21</td></tr><tr><td>5</td><td>1402.48</td><td></td><td>1.21</td></tr></table>

![](images/22cb9371258314357afbf6f0884406f6c3c96b26ab8c546d3d3dfe4d5d2d02d7.jpg)

<details>
<summary>line</summary>

| Number of UAVs | RAT   | CAT   | CM    | RM    |
| -------------- | ----- | ----- | ----- | ----- |
| 1              | 560   | 600   | 610   | 680   |
| 2              | 470   | 500   | 530   | 650   |
| 3              | 390   | 430   | 460   | 640   |
| 4              | 320   | 360   | 430   | 610   |
| 5              | 260   | 310   | 420   | 560   |
</details>

Fig. 9. The overall energy consumption of RAT, CAT, RM, CM, LE with different number of UAVs.

![](images/5f41c29a19755c5ed7c86021f273be136a3f6d6c3a49594172398155f79b4c23.jpg)

<details>
<summary>line</summary>

| Training Epoch | Overall Energy Consumption (I) |
| -------------- | ------------------------------ |
| 0              | 700                            |
| 500            | 680                            |
| 1000           | 690                            |
| 1500           | 670                            |
| 2000           | 650                            |
| 2500           | 500                            |
| 3000           | 380                            |
</details>

Fig. 10. The convergence performance of proposed RAT in 3-D UAV trajectory and 3-D channel model scenario.

RAT are trained properly, it only needs a few number of algebra calculations to obtain the solution.

Additionally, in Fig. 9, we analyse the overall energy consumption of RAT, CAT, RM, CM and LE when we have different number of UAVs. Note that for fairness, the UAVs controlled by RAT, CAT, RM, CM have the same taking off points. Specifically, in Fig. 9, one observes that the energy consumption of UEs achieved by RAT, CAT, RM, and CM decrease with the increasing number of UAVs. This is because deploying more UAVs provides higher computational capacity. Therefore, more UEs will benefit from offloading, which will decrease their overall energy consumption. Besides, we observe that for all the cases, RAT can achieve the best performance, whereas CAT performs slightly worse than RAT. Also, CM, LM and RM have worse performance than CAT, as expected.

![](images/a78f5981b43174c1e34079e4a86d3da354b52e0f5687164fe72cb275f4c1a194.jpg)

<details>
<summary>scatter</summary>

| Point | X (m) | Y (m) | Z (m) |
|-------|-------|-------|-------|
| 1     | 100   | 150   | 80    |
| 2     | 150   | 200   | 60    |
| 3     | 200   | 250   | 40    |
| 4     | 250   | 300   | 20    |
| 5     | 300   | 350   | 0     |
</details>

Fig. 11. 3-D trajectories obtained by RAT in 3-D scenario (blue dots for UEs, red stars for UAV1, and green triangles for UAV2).

![](images/38244743701cd6cdf8daef6579b6e6bbc286ee66b034abd04ffa36c7a4f10128.jpg)

<details>
<summary>line</summary>

| Index of Taking Off Points | RAT  | CM   | RM   |
| -------------------------- | ---- | ---- | ---- |
| 1                          | 370  | 490  | 620  |
| 2                          | 375  | 550  | 605  |
| 3                          | 390  | 540  | 615  |
| 4                          | 380  | 590  | 660  |
| 5                          | 390  | 540  | 630  |
</details>

(a） The overall energy consumption of UEs achieved by RAT,CM,and RM with different taking off points.

![](images/a807b99a69c62250e3c26cd5cba41671ac0732d6af9c8455f8bf3e2041ebc55f.jpg)

<details>
<summary>line</summary>

| Index of Taking Off Points | RAT | CM | RM |
|---|---|---|---|
| 1 | 18000 | 219000 | 23000 |
| 2 | 18000 | 219000 | 23000 |
| 4 | 18500 | 219000 | 23000 |
| 5 | 18500 | 219000 | 23000 |
</details>

(b） The overall energy consumption of UAVs achieved by RAT, CM, and RM with different taking off points.   
Fig. 12. The performance comparison of RAT, CM, and RM.

# 7.4 Extension to 3-D Channel Model

In this subsection, we analyse the performance of proposed RAT in 3-D channel model. We set the number of time slots T as 50, the channel bandwidth as 20 MHz, $D _ { i } ( t ) \in [ 5 , 1 0 ] \ \mathrm { K B } ,$ , $F _ { i } ( t ) \in [ 7 . 5 \times 1 0 ^ { 8 } , 2 \times 1 0 ^ { 9 } ]$ ð Þ 2 ½ cycles, the size of mini-batch is 512, ð Þ 2 ½ 	 	 and the size of experience replay buffer is 100,000. In each training epoch, each UAV starts to serve UEs with the altitude of $Z _ { j } ( 0 ) = 5 0 \mathrm { m }$ . First, we depict the overall energy consumpð Þ ¼tion achieved by the proposed RAT algorithm during the training procedure in Fig. 10. One can see that the overall energy consumption of UEs remains between 600 J and 700 J in the beginning. When the learning process starts, the curve decreases and eventually remains slightly above 350 J.

Then, we depict the UAV trajectories obtained by RAT during testing phase in Fig. 11. Note that blue dots represent UEs, red stars represent the trajectories of UAV1 and green triangles represent the trajectories of UAV2. As shown in Fig. 11, one can see that the UAVs always move from their taking off points to the certain areas, and move around to serve different UEs with the most sufficient distance. In addition, one can observe that each UAV will increase its altitude at the beginning. This is because higher altitude may increase the coverage radius of the UAV, thereby serving more UEs, although it also decreases the data rate of the offloading process.

Furthermore, we analyse the overall energy consumption of UEs and UAVs achieved by RAT, CM, and RM in different scenarios in Fig. 12, where the UAVs controlled by CM first climb from the minimal altitude Zmin to the maximal altitude Zmax in the first 10 time slots, and after that fly horizontally. Also, the RM randomly selects the available flying action for each UAV, including the horizontal flying direction, the vertical flying direction, and the flying distance. More precisely, in Fig. 12a, one can observe that our proposed RAT consistently outperforms CM and RM, whereas CM performs worse than RAT but better than RM, as expected.

Finally, we show the overall energy consumption of UAVs achieved by RAT, CM and RM in Fig. 12b. One observes that our proposed RAT has the best performance, whereas CM has the worse performance than RAT, but better than RM.

# 8 CONCLUSION

In this paper, we have considered the flying mobile edge computing architecture, by taking advantage of the UAVs to serve as the moving platform. We aim to minimize the energy consumption of all the UEs by optimizing the UAVs’ trajectories, user associations and resource allocation. To tackle the multi-UAVs’ trajectories problem, a convex optimization-based CAT has been first proposed. Then, in order to conduct fast decision, a DRL-based RAT including a matching algorithm has also been proposed. Simulation results show that CAT and RAT have considerable performance.

# ACKNOWLEDGMENTS

The authors would like to acknowledge the support from Distinguished Visiting Fellowship of Royal Academy of Engineering (DVFS21819\9\7). This work of W. Xu was supported in part by the NSFC under Grants 62022026 and 61871109.

# REFERENCES

[1] Y. C. Hu, M. Patel, D. Sabella, N. Sprecher, and V. Young, “Mobile edge computing–A key technology towards 5G,” ETSI White Paper, vol. 11, no. 11, pp. 1–16, 2015.   
[2] Y. Du, K. Wang, K. Yang, and G. Zhang, “Energy-efficient resource allocation in UAV based MEC system for IoT devices,” in Proc. IEEE Global Commun. Conf., 2018, pp. 1–6.   
[3] X. Lyu, H. Tian, W. Ni, Y. Zhang, P. Zhang, and R. P. Liu, “Energy-efficient admission of delay-sensitive tasks for mobile edge computing,” IEEE Trans. Commun., vol. 66, no. 6, pp. 2603– 2616, Jun. 2018.   
[4] Q. Wu and R. Zhang, “Common throughput maximization in UAV-enabled OFDMA systems with delay consideration,” IEEE Trans. Commun., vol. 66, no. 12, pp. 6614–6627, Dec. 2018.   
[5] Z. Li, M. Chen, C. Pan, N. Huang, Z. Yang, and A. Nallanathan, “Joint trajectory and communication design for secure UAV networks,” IEEE Commun. Lett., vol. 23, no. 4, pp. 636–639, Apr. 2019.   
[6] C. H. Liu, Z. Chen, J. Tang, J. Xu, and C. Piao, “Energy-efficient UAV control for effective and fair communication coverage: A deep reinforcement learning approach,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 2059–2070, Sep. 2018.   
[7] L. Kong, L. Ye, F. Wu, M. Tao, G. Chen, and A. V. Vasilakos, “Autonomous relay for millimeter-wave wireless communications,” IEEE J. Sel. Areas Commun., vol. 35, no. 9, pp. 2127–2136, Sep. 2017.   
[8] U. Challita, A. Ferdowsi, M. Chen, and W. Saad, “Machine learning for wireless connectivity and security of cellular-connected UAVs,” IEEE Wireless Commun., vol. 26, no. 1, pp. 28–35, Feb. 2019.   
[9] C. Zhan, Y. Zeng, and R. Zhang, “Energy-efficient data collection in UAV enabled wireless sensor network,” IEEE Wireless Commun. Lett., vol. 7, no. 3, pp. 328–331, Jun. 2018.   
[10] J. Xu, Y. Zeng, and R. Zhang, “UAV-enabled wireless power transfer: Trajectory design and energy optimization,” IEEE Trans. Wireless Commun., vol. 17, no. 8, pp. 5092–5106, Aug. 2018.   
[11] N. Zhao et al., “Caching UAV assisted secure transmission in hyper-dense networks based on interference alignment,” IEEE Trans. Commun., vol. 66, no. 5, pp. 2281–2294, May 2018.   
[12] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Unmanned aerial vehicle with underlaid device-to-device communications: Performance and tradeoffs,” IEEE Trans. Wireless Commun., vol. 15, no. 6, pp. 3949–3963, Jun. 2016.

[13] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP altitude for maximum coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6, pp. 569–572, Dec. 2014.   
[14] H. He, S. Zhang, Y. Zeng, and R. Zhang, “Joint altitude and beamwidth optimization for UAV-enabled multiuser communications,” IEEE Commun. Lett., vol. 22, no. 2, pp. 344–347, Feb. 2018.   
[15] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.   
[16] J. Lyu, Y. Zeng, and R. Zhang, “UAV-aided offloading for cellular hotspot,” IEEE Trans. Wireless Commun., vol. 17, no. 6, pp. 3988–4001, Jun. 2018.   
[17] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.   
[18] Z. Yang, C. Pan, K. Wang, and M. Shikh-Bahaei, “Energy efficient resource allocation in UAV-enabled mobile edge computing networks,” IEEE Trans. Wireless Commun., vol. 18, no. 9, pp. 4576–4589, Sep. 2019.   
[19] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Mobile unmanned aerial vehicles (UAVs) for energy-efficient Internet of Things communications,” IEEE Trans. Wireless Commun., vol. 16, no. 11, pp. 7574–7589, Nov. 2017.   
[20] Y. Mao, C. You, J. Zhang, K. Huang, and K. B. Letaief, “A survey on mobile edge computing: The communication perspective,” IEEE Commun. Surveys Tuts., vol. 19, no. 4, pp. 2322–2358, Fourth Quarter 2017.   
[21] C. Wang, C. Liang, F. R. Yu, Q. Chen, and L. Tang, “Computation offloading and resource allocation in wireless cellular networks with mobile edge computing,” IEEE Trans. Wireless Commun., vol. 16, no. 8, pp. 4924–4938, Aug. 2017.   
[22] W. Zhang, Y. Wen, K. Guan, D. Kilper, H. Luo, and D. O. Wu, “Energy-optimal mobile cloud computing under stochastic wireless channel,” IEEE Trans. Wireless Commun., vol. 12, no. 9, pp. 4569–4581, Sep. 2013.   
[23] F. Jiang, K. Wang, L. Dong, C. Pan, W. Xu, and K. Yang, “AI driven heterogeneous MEC system with UAV assistance for dynamic environment: Challenges and solutions,” IEEE Netw., vol. 35, no. 1, pp. 400–408, Mar./Apr. 2021.   
[24] Y. Du, K. Yang, K. Wang, G. Zhang, Y. Zhao, and D. Chen, “Joint resources and workflow scheduling in UAV-enabled wirelesslypowered MEC for IoT systems,” IEEE Trans. Veh. Technol., vol. 68, no. 10, pp. 10187–10200, Oct. 2019.   
[25] F. Zhou, Y. Wu, R. Q. Hu, and Y. Qian, “Computation rate maximization in UAV-enabled wireless-powered mobile-edge computing systems,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 1927–1941, Sep. 2018.   
[26] A. Asheralieva and D. Niyato, “Hierarchical game-theoretic and reinforcement learning framework for computational offloading in UAV-enabled mobile edge computing networks with multiple service providers,” IEEE Internet of Things J., vol. 6, no. 5, pp. 8753–8769, Oct. 2019.   
[27] Q. Zhang, J. Chen, L. Ji, Z. Feng, Z. Han, and Z. Chen, “Response delay optimization in mobile edge computing enabled UAV swarm,” IEEE Trans. Veh. Technol., vol. 69, no. 3, pp. 3280–3295, Mar. 2020.   
[28] V. Mnih et al., “Human-level control through deep reinforcement learning,” Nature, vol. 518, no. 7540, pp. 529–533, Feb. 2015.   
[29] H. van Hasselt, A. Guez, and D. Silver, “Deep reinforcement learning with double Q-learning,” in Proc. 30th AAAI Conf. Artif. Intell., 2016, pp. 2094–2100.   
[30] T. P. Lillicrap et al., “Continuous control with deep reinforcement learning,” 2015, arXiv:1509.02971.   
[31] T. Schaul, J. Quan, I. Antonoglou, and D. Silver, “Prioritized experience replay,” Nov. 2015, arXiv:1511.05952.   
[32] X. Wang et al., “Dynamic resource scheduling in mobile edge cloud with cloud radio access network,” IEEE Trans. Parallel Distrib. Syst., vol. 29, no. 11, pp. 2429–2445, Nov. 2018.   
[33] F. Jiang, K. Wang, L. Dong, C. Pan, W. Xu, and K. Yang, “Deep learning based joint resource scheduling algorithms for hybrid MEC networks,” IEEE Internet of Things J., vol. 7, no. 7, pp. 6252–6265, Jul. 2020.   
[34] S. Mitchell, M. G. O. Sullivan, and I. Dunning, “PuLP : A linear programming toolkit for python,” Python, 2011. [Online]. Available: http://www.optimization-online.org/DB\_FILE/2011/09/3178.pdf   
[35] S. Diamond and S. Boyd, “CVXPY: A Python-embedded modeling language for convex optimization,” J. Mach. Learn. Res., vol. 17, no. 83, pp. 1–5, 2016.

[36] C. Pan, H. Zhu, N. J. Gomes, and J. Wang, “Joint precoding and RRH selection for user-centric green MIMO C-RAN,” IEEE Trans. Wireless Commun., vol. 16, no. 5, pp. 2891–2906, May 2017.   
[37] V. R. Konda and J. N. Tsitsiklis, “Actor-critic algorithms,” in Proc. Int. Conf. Neural Inf. Process. Syst., 2000, pp. 1008–1014.   
[38] H. Van Hasselt, A. Guez, and D. Silver, “Deep reinforcement learning with double Q-learning,” in Proc. 30th AAAI Conf. Artif. Intell., 2016, pp. 2094–2100.   
[39] C. J. Watkins and P. Dayan, “Q-learning,” Mach. Learn., vol. 8, no. 3/4, pp. 279–292, 1992.   
[40] J. Hamari, J. Koivisto, H. Sarsa et al., “Does gamification work?-A literature review of empirical studies on gamification,” in Proc. 47th Hawaii Int. Conf. Syst. Sci., 2014, vol. 14, pp. 3025–3034.   
[41] A. R. Mahmood, H. P. Van Hasselt, and R. S. Sutton, “Weighted importance sampling for off-policy learning with linear function approximation,” in Proc. 27th Int. Conf. Neural Inf. Process. Syst., 2014, pp. 3014–3022.   
[42] R. Ding, F. Gao, and X. S. Shen, “3D UAV trajectory design and frequency band allocation for energy-efficient and fair communication: A deep reinforcement learning approach,” IEEE Trans. Wireless Commun., vol. 19, no. 12, pp. 7796–7809, Dec. 2020.   
[43] Y. Zeng, J. Xu, and R. Zhang, “Energy minimization for wireless communication with rotary-wing UAV,” IEEE Trans. Wireless Commun., vol. 18, no. 4, pp. 2329–2345, Apr. 2019.

![](images/6180d4dda6a9ffbfb796dc6a1295f2db3f36312b76b7f8cf2603c6969b9693b4.jpg)

<details>
<summary>natural_image</summary>

Portrait of a young man wearing glasses (no text or symbols visible)
</details>

Liang Wang received the BEng degree, in 2014 and the MSc degree, in 2015. He is currently working toward the PhD degree in computer science from Northumbria University, Newcastle upon Tyne, U.K. His research interests include UAV communication, mobile edge computing, and machine learning.

![](images/1155a7a86e43c58554fae18b0e967daaf055ad8237e3e6bd3e964b6c06939b33.jpg)

<details>
<summary>natural_image</summary>

Portrait of a smiling man in a white shirt (no text or symbols visible)
</details>

Kezhi Wang (Senior Member, IEEE) received the BE and ME degrees from the School of Automation, Chongqing University, China, in 2008 and 2011, respectively, and the PhD degree in engineering from the University of Warwick, U.K., in 2015. He was a senior research officer in University of Essex, U.K. from 2015-2017. Currently, he is a senior lecturer at the Department of Computer and Information Sciences, Northumbria University, U.K. His research interests include mobile edge computing, intelligent reflection surface (IRS), and machine learning.

![](images/0e9bb458405a8d1044024952700c4548d1c9802e38d5a667689af5734d8253b4.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in formal attire (no text or symbols visible)
</details>

Cunhua Pan received the BS and PhD degrees from the School of Information Science and Engineering, Southeast University, Nanjing, China, in 2010 and 2015, respectively. From 2015 to 2016, he was a research associate with the University of Kent, U.K. He held a postdoctoral position at Queen Mary University of London, U.K., from 2016 and 2019, where he is currently a lecturer. His research interests mainly include reconfigurable intelligent surfaces (RIS), intelligent reflection surface (IRS), ultra-reliable low latency communi-

cation (URLLC), machine learning, UAV, Internet of Things, and mobile edge computing. He serves as a TPC member for numerous conferences, such as ICC and GLOBECOM, and the Student Travel Grant Chair for ICC 2019. He is currently an editor of the IEEE Wireless Communication Letters, the IEEE Communications Letters and IEEE Access. He also serves as a lead guest editor of the IEEE Journal of Selected Topics in Signal Processing (JSTSP) Special Issue on Advanced Signal Processing for Reconfigurable Intelligent Surface-aided 6G Networks, lead guest editor of the IEEE Access Special Issue on Reconfigurable Intelligent Surface Aided Communications for 6G and Beyond.

![](images/25b7b98f99404271d6dd757da33fd59b2249316d73f620dbac6753cdeb69e531.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a person (no text or symbols visible)
</details>

Wei Xu (Senior Member, IEEE) received the BSc degree in electrical engineering and the MS and PhD degrees in communication and information engineering from Southeast University, Nanjing, China, in 2003, 2006, and 2009, respectively. Between 2009 and 2010, he was a postdoctoral research fellow with the Department of Electrical and Computer Engineering, University of Victoria, Canada. He is currently a professor at the National Mobile Communications Research Laboratory, Southeast University, China. He is also an adjunct professor of the University of Victoria, Canada, and a distinguished visiting fellow of the Royal Academy of Engineering, U.K. He has coauthored more than 100 refereed journal papers in addition to 36 domestic patents and four US patents granted. His research interests include information theory, signal processing and machine learning for wireless communications. He was an editor of the IEEE Communications Letters from 2012 to 2017. He is currently an editor of the IEEE Transactions on Communications and an senior editor of the IEEE Communications Letters. He received the best paper awards from a number of prestigious IEEE conferences including IEEE Globecom/ICCC etc. He received the Youth Science and Technology Award of China Institute of Communications, in 2018.

![](images/b6974c47481c8c4dccf45f92331417ec5355fd576c162e81e5773c58650ac891.jpg)

<details>
<summary>natural_image</summary>

Portrait of a smiling man wearing glasses and a suit (no text or symbols visible)
</details>

Nauman Aslam received the PhD degree in engineering mathematics from Dalhousie University, Halifax, NS, Canada, in 2008. He is currently an associate professor at the Department of Computer Science and Digital Technologies, Northumbria University, Newcastle upon Tyne, U.K. He is also an adjunct assistant professor with Dalhousie University, Canada. Prior to joining Northumbria University, United Kingdom, he was an assistant professor with Dalhousie University, Canada. His research interests include wireless sensor network, energy efficiency, security, and WSN health applications.

![](images/88b86f9f19e36f67ce5168489bcd5bad690f1145d875475946a970cebe316557.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man wearing glasses and a suit (no text or symbols visible)
</details>

Arumugam Nallanathan (Fellow, IEEE) is currently a professor of wireless communications and head of the Communication Systems Research (CSR) group in the School of Electronic Engineering and Computer Science, Queen Mary University of London, U.K. since September 2017. He was with the Department of Informatics, King’s College London, U.K from December 2007 to August 2017, where he was a professor of Wireless Communications from April 2013 to August 2017 and a visiting professor from September 2017. He was an assistant professor with the Department of Electrical and Computer Engineering, National University of Singapore, Singapore from August 2000 to December 2007. His research interests include artificial intelligence for wireless systems, beyond 5G wireless networks, Internet of Things (IoT), and molecular communications. He published nearly 500 technical papers in scientific journals and international conferences. He is a co-recipient of the best paper awards presented at the IEEE International Conference on Communications 2016 (ICC’2016), IEEE Global Communications Conference 2017 (GLOBECOM’2017) and IEEE Vehicular Technology Conference 2018 (VTC’2018). He is an IEEE distinguished lecturer. He has been selected as a Web of Science Highly Cited Researcher, in 2016. He is an editor for the IEEE Transactions on Communications and senior editor for the IEEE Wireless Communications Letters. He was an editor for the IEEE Transactions on Wireless Communications (2006-2011), IEEE Transactions on Vehicular Technology (2006-2017), and IEEE Signal Processing Letters. He served as the chair for the Signal Processing and Communication Electronics Technical Committee of IEEE Communications Society and Technical Program Chair and member of Technical Program Committees in numerous IEEE conferences. He received the IEEE Communications Society SPCE Outstanding Service Award 2012 and IEEE Communications Society RCC Outstanding Service Award 2014.

" For more information on this or any other computing topic, please visit our Digital Library at www.computer.org/csdl.