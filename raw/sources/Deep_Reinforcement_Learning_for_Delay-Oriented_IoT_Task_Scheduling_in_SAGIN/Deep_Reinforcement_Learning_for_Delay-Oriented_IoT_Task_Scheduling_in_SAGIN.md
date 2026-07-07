# Deep Reinforcement Learning for Delay-Oriented IoT Task Scheduling in SAGIN

Conghao Zhou , Graduate Student Member, IEEE, Wen Wu , Member, IEEE,

Hongli He , Member, IEEE, Peng Yang , Member, IEEE, Feng Lyu , Member, IEEE,

Nan Cheng , Member, IEEE, and Xuemin Shen , Fellow, IEEE

Abstract— In this article, we investigate a computing task scheduling problem in space-air-ground integrated network (SAGIN) for delay-oriented Internet of Things (IoT) services. In the considered scenario, an unmanned aerial vehicle (UAV) collects computing tasks from IoT devices and then makes online offloading decisions, in which the tasks can be processed at the UAV or offloaded to the nearby base station or the remote satellite. Our objective is to design a task scheduling policy that minimizes offloading and computing delay of all tasks given the UAV energy capacity constraint. To this end, we first formulate the online scheduling problem as an energy-constrained Markov decision process (MDP). Then, considering the task arrival dynamics, we develop a novel deep risk-sensitive reinforcement learning algorithm. Specifically, the algorithm evaluates the risk, which measures the energy consumption that exceeds the constraint, for each state and searches the optimal parameter weighing the minimization of delay and risk while learning the optimal policy. Extensive simulation results demonstrate that the proposed algorithm can reduce the task processing delay by up to 30% compared to probabilistic configuration methods while satisfying the UAV energy capacity constraint.

Index Terms— Space-air-ground integrated network, IoT, edge computing, reinforcement learning, constrained MDP.

## I. INTRODUCTION

devices, such as high definition cameras, object detectors, and meteorological sensors, play vital roles in a myriad of applications and services [2]. Specifically, IoT devices can be deployed to monitor and sense the environment, offering new opportunities for industrial automation, intelligent transportation management, etc. There are two typical applications of delay-oriented IoT services: intelligent urban transportation management and automated surface mining in suburban areas. For intelligent transportation management, on-board cameras and road-side sensors can reliably detect incidents, such as traffic signal violations, stopped vehicles, and on-road pedestrians. By leveraging deep learning-based image processing techniques, vehicle and pedestrian behaviors can be predicted to prevent potential traffic accidents in advance [3]. Rapidly processing the collected image can save more time in reacting to the complicated transportation scenarios, which enhances the road safety by preventing the transportation emergency. For automated surface mining, a large number of cameras and visual sensors are deployed in the active areas of the drill rigs to assess rock composition and collect environment information (e.g., humidity and temperature). The analytics results of input image/video from these IoT devices can help achieve automated drilling control [4]. In this case, lower delay of image/video analytic can enable more accurate automated surface mining control. Generally, such IoT services are delayoriented which should be processed rapidly to adapt to highly dynamic input.

To support the aforementioned services, ubiquitous delayoriented computing tasks become prevailing on IoT devices, resulting in a surging demand for computing capability [5]. Due to the limited computing capability of IoT devices, executing these delay-oriented tasks locally, such as on-camera image/video processing, can inflict unacceptable service delay and be detrimental to the service lifespan of IoT devices [6]. Edge computing has been proposed as a de-facto paradigm to support computation-intensive IoT services. Within this paradigm, IoT devices can offload computing tasks to nearby terrestrial base stations (BSs), which can not only reduce the latency of task execution, but also save the power consumption of IoT devices [7]. However, purely relying on offloading to terrestrial BSs is hard to guarantee the performance of IoT edge computing robustly. On the one hand, the IoT devices are usually power constrained, which cannot support longdistance transmission for task offloading, especially when the BSs are sparsely deployed or unavailable nearby (e.g., automated mining applications) [8]. On the other hand, the physical computing resources on BSs are scarce and somewhat insufficient, but the IoT computing tasks arrive dynamically with possible bursty conditions (e.g., intelligent transportation applications), which can result in computing resource shortage and deteriorate delay performance [9] [10].

As a remedy to these limitations, satellites and unmanned aerial vehicles (UAVs) are considered as promising complements to enhance the terrestrial network. For satellites, many research and industrial efforts have been devoted to the commercialization of the low earth orbit (LEO) satellite constellation, such as SpaceX and OneWeb [11], which can provide ubiquitous services with acceptable propagation delay (e.g., about 6.44 ms) [12], [13]. For UAVs with flexible deployment and agile management, they have been widely utilized in military and civil applications to provide on-demand communication and computing resources [14]. Besides, the 3rd Generation Partnership Project (3GPP) is also investigating on non-terrestrial networks and specifying novel architectures to complement terrestrial cellular networks [12]. Since satellite, UAV, and BS can complement each other, the integration of them, namely the space-air-ground integrated network (SAGIN), is proposed as a promising next-generation wireless network to serve the massive IoT devices with delay-oriented service requirements [8], [15].

In this article, considering the low transmit power and shortdistance communication range of IoT devices, we propose a delay-orientated IoT task scheduling (DOTS) scheme in SAGIN to process computing tasks in real time. We adopt a UAV (installed with dedicated IoT communication interface such as LoRa and NB-IoT [16], [17]) as the “flying scheduler” to communicate with IoT devices and collect their computing tasks. As the UAV can move sufficiently close to IoT devices, the distance between IoT devices and the UAV can be significantly reduced, which not only saves the IoT devices’ power consumption and prolongs the service lifespan, but also guarantees the transmission reliability [18]. Then, the UAV makes task scheduling decisions in real time, i.e., processing locally, offloading to a nearby BS or the remote LEO satellite constellation.<sup>1</sup> Particularly, the UAV needs to offload tasks as soon as possible when it serves an excessive number of IoT computing tasks, due to the limited computing capability [20]. In addition, the UAV should make decisions in real time to keep the pace of dynamic link conditions and computing task arrival. Therefore, how to obtain an efficient scheduling policy of processing IoT computing tasks at appropriate SGAIN components is a crucial issue, which is quite challenging due to the following three reasons. First, with a large number of IoT devices, task arrivals are dynamic and may be bursty, and even unknown a priori, which poses a real-time requirement for the scheduling policy. Second, UAV, BSs, and LEO satellites have differentiated features in terms of communication and computing capability. As a result, the scheduling policy should select appropriate SAGIN components for task processing in accordance with their features. Third, in the scheduling policy, both the current energy consumption and the energy reservation for future arrived tasks should be considered. The UAV needs to comply with the UAV energy capacity by making sequential task scheduling decisions.

To tackle the above challenges, we formulate the online scheduling problem as a constrained Markov decision process (CMDP) to minimize the time-averaged task processing delay while taking the UAV energy capacity (consumed by communication and computing) into consideration. Inspired by the advantage of reinforcement learning (RL) methods in tackling the uncertainty and dynamics, we design a novel deep risk sensitive RL algorithm to deal with the formulated CMDP problem. The core idea is to define a risk function to capture whether the UAV energy capacity constraint is violated. Thus, satisfying the constraint is transformed into minimizing the risk. Afterward, we replace the typical Q-value function by the sum of two Q-value functions. The former Q-value function evaluates the long-term delay for different state-action pairs, and the latter accounts for the long-term risk. Based on the designed Q-value function, the scheduling policy can be learned by leveraging RL methods. Meanwhile, instead of constructing a space-costly Q-value table caused by the high dimensional state representation, we leverage the parameterized deep neural network (DNN) to approximate the Q-value function. In addition, we add a filter layer after fully connected layers to exclude unavailable actions at different states. Extensive simulations are conducted, which show that the proposed deep RL-based DOTS scheme can achieve a lower time-average task processing delay while satisfying the UAV energy capacity constraint compared to that of benchmark schemes. The main contributions of this article are three-fold:

• We propose a computing task scheduling scheme named DOTS for delay-oriented IoT services in SAGIN, where a UAV flies along a trajectory to collect computing tasks and make real-time scheduling decisions.

• We formulate an integer non-linear optimization problem with uncertainty to minimize the time-averaged task processing delay under the UAV energy capacity constraint. As the UAV location and task backlog evolve in an ergodic way, we reformulate the online IoT task scheduling problem as a CMDP.

• We design a novel deep risk-sensitive RL algorithm to address the CMDP problem, where a risk function is defined to indicate whether the UAV energy consumption violates the constraint. Besides, we leverage DNNs to implement the proposed deep RL-based algorithm in the DOTS scheme.

The remainder of this article is organized as follows. Section II presents the related work. We describe the SAGIN architecture and computing task scheduling models in Section III. In Section IV, we provide the problem formulation. We design the DOTS scheme to make the online scheduling decision in Section V. Section VI presents the simulation results of DOTS, followed by the conclusion and the future work in Section VII.

## II. RELATED WORK

SAGIN is envisioned as a promising architecture to complement the terrestrial network for the next-generation wireless network. To guarantee service requirements in dynamic and heterogeneous SAGIN, a cost-effective scheme for joint service placement and routing is proposed in [21]. To accommodate diverse services, resources of the satellite, aerial, and terrestrial components have been sliced, and a hierarchical resource management scheme is proposed to put available resources into a common and dynamic resource pool [22]. To meet the emerging computation-intensive IoT applications with diverse QoS requirements, an air-ground integrated mobile edge network is presented to realize mobile edge computing [23]. In [8], to address uncertain channel conditions in remote areas, an RL-based scheduling scheme is proposed for the virtual machine assignment and task offloading in SAGIN. However, accommodating IoT computing task scheduling in SAGIN still faces significant challenges since the computing task arrival from IoT devices is highly dynamic and random, and the management for both communication and computing resources is complicated.

Although the research on IoT computing task scheduling in SAGIN is at its initial stage, applying task scheduling for IoT devices in other scenarios has been exploited extensively. To solve the joint problem of partial offloading scheduling and resource allocation for mobile edge computing systems with multiple independent tasks, a two-level alternation method is proposed based on the Lagrangian dual decomposition [24]. To address the multi-user computation offloading problem for mobile-edge cloud computing in a multi-channel wireless interference environment, a distributed computation offloading algorithm is proposed based on a Nash equilibrium [25]. However, it is difficult for an optimization-based algorithm to adapt to the dynamic task arrival scenario since a fixed task number is required. Considering the stochastic task generation, Lyapunov optimization is leveraged in task scheduling schemes. Besides, an asymptotically optimal scheduling scheme is also proposed with partial knowledge in mobile edge computing scenarios by leveraging the Lyapunov drift [26]. In order to minimize the delay due to both radio access and computation, a user-centric energy-aware mobility management scheme is proposed based on Lyapunov functions and multi-armed bandit theories [27]. The Lyapunov-drift-based techniques can schedule tasks to keep the task queue stable based on the current queue backlog. However, the optimality cannot be guaranteed since the information of future status (e.g., future task arrival) is lacking.

Preliminary results of this work have been presented [1], in which the task arrival pattern is assumed to be known to

![](images/c324f9d0d4b901c52858988c067e1c84ea78250e53f07f22caf043d1259b4eb1.jpg)  
Fig. 1. The network model.  
the UAV. In practice, this information may be difficult to be obtained. To accommodate to dynamic task arrival, we propose an IoT task scheduling scheme in SAGIN relying on deep risksensitive RL to minimize the time-averaged task processing delay while considering the UAV energy capacity.

## III. SYSTEM MODEL

In this section, we first introduce the proposed DOTS scheme in SAGIN architecture, and then describe the computing, communication, and energy consumption models for IoT task offloading.

## A. The SAGIN Architecture and the DOTS Scheme

As shown in Fig. 1, the UAV flies along a trajectory to collect delay-oriented computing tasks from IoT devices.<sup>2</sup> As the rotary-wing UAV can hover in the air, and fly with a low height sufficiently close to IoT devices, we adopt the rotary-wing UAV to collect the computing tasks [29]. Taking the computing functionality of the UAV [14], BSs [25], and LEO satellites [8] into account in the SAGIN, the UAV can schedule computing tasks on three different destination network components, i.e., processing tasks on the UAV locally, offloading to the nearby BS, or offloading the LEO satellite constellation. Let indexes <sup>, , . . . , N</sup> , and denote the LEO satellite constellation and the BSs, respectively. Then, the set of the network components that computing tasks can be offloaded to (i.e., <sup>N</sup> BSs and the LEO satellite constellation) is denoted by $\mathcal { N } = \{ 0 , 1 , 2 , . . . , N \}$ . Due to the UAV’s limited on-board battery capacity, the computing capability at the UAV is limited [14]. The UAV cannot process all computing tasks alone, and thus some computing tasks can be offloaded to BSs or the LEO satellite constellation. BSs and the LEO satellite constellation have different characteristics. The BS has high computing capacity, while its coverage area is limited. The LEO satellite constellation can always cover the area and act as a complementary offloading solution for terrestrial networks, while the propagation delay of the UAV-satellite link cannot be neglected. Therefore, computing tasks should be scheduled appropriately to different destination network components in SAGIN to reduce the service delay.

We adopt the discrete epoch-based system with an equal time duration of $\tau$ in each epoch. In epoch $t ,$ the location of the deployed UAV is denoted by $l _ { t } .$ As the UAV flies along the trajectory, the set of available offloading destination network components also varies at different locations, which is denoted by $\mathcal { L } _ { t } \subseteq \mathcal { N } .$ . Supposing that multiple computing tasks can be offloaded from the UAV in each epoch, only one offloading destination (i.e., a BS or the satellite) can be chosen. In summary, the UAV collects and schedules IoT computing tasks according to the following steps in each epoch:

1) The UAV collects tasks from IoT devices and locally processes their tasks within the computing queue. The collected tasks that have not been processed or offloaded will wait in the computing queue at the UAV.

2) The UAV can offload a certain number of computing tasks from the computing queue to a BS or the satellite. The offloaded tasks that have not been forwarded will wait in the forwarding queue at the UAV.

3) Newly arrived tasks from IoT devices are stored in the computing queue at the UAV. Once the computing queue is full, newly arrived tasks will be dropped.

4) The UAV flies to the next location along the predefined trajectory, and continues to collect computing tasks.

As shown in Fig. 2, an exemplary work flow of the DOTS scheme in SAGIN is illustrated. In epoch 1, four tasks are collected, one of which is processed locally at the UAV, and three of which are offloaded to BS and moved into the forwarding queue. In epoch 2, the UAV cannot move new tasks into the forwarding queue due to the uncompleted task forwarding. Only one task is processed locally at the UAV, and all tasks in the forwarding queue are transmitted. In epoch $^ { 3 , }$ two tasks are offloaded to the satellite and moved into the forwarding queue. In epoch 4, all tasks can only be executed locally at the UAV. The details of the scheme are introduced in the following subsections.

## B. Computing Model

In general, we adopt a tuple <sup>φ,</sup> <sup>γ</sup> to model a computing task [8]. Here, <sup>φ</sup> represents the input data size (in bits) of a computing task, and $\gamma$ (in central processing unit (CPU) cycles per bit) indicates the computing workload of the task, i.e., how many CPU cycles are required to process one bit input data.<sup>3</sup> Note that task uploading is the key point of scheduling policy at the UAV in the considered scenario, and the downloading of the computing result can be ignored in this work.<sup>4</sup> For instance, IoT devices upload images for analysis and download text messages as the output, and the uploaded data size is much larger than that of downloaded data [5]. As the UAV can offload tasks to either the nearby BS or the remote LEO satellite, or execute tasks locally, the corresponding computing delay is analyzed in the next.

1) Task Offloading: Denote the task offloading decision by $\alpha _ { t }$ in epoch <sup>t</sup>, i.e., the offloading destination network components in epoch <sup>t</sup>. The UAV offloads the tasks to the satellite when $\begin{array} { r l r } { \alpha _ { t } } & { { } = } & { 0 , } \end{array}$ or offloads tasks to BS <sup>n</sup> when $\alpha _ { t } = n , \forall n \neq 0 .$ . Denote by $\beta _ { t } \le \beta ^ { \operatorname* { m a x } } , \beta _ { t } \in \mathbb { N }$ the number of <sup>= = 0</sup>offloaded tasks in epoch <sup>t</sup>, where $\beta ^ { \mathrm { m a x } }$ is the maximal number of tasks that can be forwarded by the UAV in each epoch. Meanwhile, due to the occupation of the communication interface, we assume that new tasks cannot be forwarded if the offloading process of the last task is not completed. Let binary variable $F _ { t }$ indicate whether collected IoT tasks on the UAV can be offloaded or not. Fig. 2 illustrates an example of the task forwarding. When $F _ { t } = 0$ , the UAV can offload tasks in epoch <sup>t</sup> since the channel is not occupied (i.e., $\alpha _ { t } \in \mathcal { L } _ { t } , \beta _ { t } \le \beta ^ { \operatorname* { m a x } } )$ . $F _ { t } = 1$ represents that the UAV cannot offload new tasks since a certain number of tasks are waiting to be transmitted in the forwarding queue $( \mathrm { i . e . , ~ } \alpha _ { t } = - 1 , \beta _ { t } = 0 )$

Denote by the computing capabilities (in CPU cycles per second) of BS <sup>n</sup> and the satellite by $f _ { n } , n \ne 0$ and $f _ { 0 } ,$ respectively. The computing delay of all $\beta _ { t }$ tasks at offloading destination network component <sup>n</sup> is given by:

$$
d _ { 1 } ( \alpha _ { t } , \beta _ { t } ) = \frac { \beta _ { t } \phi \gamma } { f _ { \alpha _ { t } } } , \ \alpha _ { t } \in \mathcal { L } _ { t } ,\tag{1}
$$

where $f _ { \alpha _ { t } }$ represents the computing capability of offloading destination network component $\alpha _ { t }$

2) Local Processing: Since the computing capability of the UAV is limited, the collected tasks may not be processed locally or offloaded completely at the UAV within an epoch. We assume that the remaining tasks wait to be scheduled in the computing queue at the UAV. As a result, the delay of processing task locally at UAV includes two parts, i.e., local computing delay and queuing delay. To model the computing queue, we first denote the unaccomplished task backlog at the beginning of epoch <sup>t</sup> by $H _ { t } \in [ 0 , \rho ]$ , where $\rho$ is the maximum length of the computing queue. Then, given unaccomplished task backlog $H _ { t }$ and the number of offloaded tasks $\beta _ { t }$ , the number of queuing tasks $O _ { t }$ in epoch <sup>t</sup> within the computing queue is given by:

$$
O _ { t } = \operatorname* { m a x } \left\{ H _ { t } - \lfloor \frac { f _ { \mathrm { U } } \tau } { \phi \gamma } \rfloor - \beta _ { t } , 0 \right\} ,\tag{2}
$$

where $f _ { \mathrm { U } }$ is the computing capability (in CPU cycles per second) of the UAV, and $\lfloor f _ { \mathrm { U } } \tau / \phi \gamma \rfloor$ is the greatest integer less than the number of tasks executed by the UAV in epoch <sup>t</sup>. Given the number of newly collected tasks $M _ { t }$ from the IoT devices, the unaccomplished task backlog $H _ { t + 1 }$ can be updated at the end of epoch <sup>t</sup> as follows:

$$
H _ { t + 1 } = \operatorname* { m i n } \left\{ O _ { t } + M _ { t } , \rho \right\} ,\tag{3}
$$

where $\{ \cdot \}$ is the function to return the smallest value. Then, the delay of local task execution at the UAV can be

![](images/f20fd50944b44dd37b2ae5ff2972fd6f44c4e4f39bef14ad81789e5d2768af75.jpg)  
Fig. 2. An illustration of the DOTS scheme in SAGIN, where different colors of tasks are used to distinguish the collection in different epochs.

calculated as the following equation:

$$
d _ { 2 } ( \alpha _ { t } , \beta _ { t } ) = \frac { \operatorname* { m i n } \left\{ \big \lfloor \frac { f _ { \mathrm { U } } \tau } { \phi \gamma } \big \rfloor , H _ { t } \right\} \phi \gamma } { f _ { \mathrm { U } } } + O _ { t } \tau ,\tag{4}
$$

where $\{ \lfloor \frac { f _ { \mathrm { U } } \tau } { \phi \gamma } \rfloor , H _ { t } \} \phi \gamma / f _ { \mathrm { U } }$ is the local computing delay within each epoch, and $O _ { t } \tau$ is the queuing delay of all $O _ { t }$ tasks waiting in the computing queue.

## C. Communication Model

We suppose two communication interfaces are equipped in this work [32], i.e., one for LEO satellites, and the other for BSs. Each of them uses different spectrum bands, which leads to no interference between BSs and the satellite [33]. In the following, the transmission delay of offloading tasks to the satellite and the BSs are discussed in detail.<sup>5</sup>

1) Offload to Satellite: Currently, the wireless communications between an LEO satellite and terrestrial users are enabled by Ka or Ku frequency band, the channel condition of which is mainly impacted by the communication distance and the rain attenuation (rain fading) [33]. Supposing the meteorologica environment remains stationary during the IoT task collection, the channel gain of the UAV-satellite link is mainly determined by the distance between the UAV and the satellite. Generally, the moving distance of the UAV (e.g., the maximum flight distance of the UAV is about 2 km) is much shorter than the altitude of the satellite (e.g., the LEO satellites are with an altitude of 200 km to 2,000 km), which results in the negligible variation of the distance between the UAV and the satellite [8]. Therefore, the channel gain <sup>h</sup> of the UAV-satellite link can be assumed to be the same with the location of UAV. Then, the data rate of the UAV-satellite link in epoch <sup>t</sup> denoted by $r _ { \alpha _ { t } }$ is given by:

$$
r _ { \alpha _ { t } } = W _ { \mathrm { S } } \log _ { 2 } \left( 1 + \frac { P _ { \mathrm { S } } \cdot | h | ^ { 2 } } { \sigma _ { \mathrm { S } } ^ { 2 } } \right) , \quad \alpha _ { t } = 0 ,\tag{5}
$$

where $W _ { \mathrm { S } }$ is the channel bandwidth of the UAV-satellite link, $P _ { \mathrm { S } }$ is the transmission power of UAV-satellite link, and $\sigma _ { \mathrm { S } } ^ { 2 }$ indicates the power of noise. Due to the long distance between the LEO satellite and the UAV, the propagation delay cannot be ignored, which is denoted by $d _ { \mathrm { S } }$ . Thus, given offloading decision $\alpha _ { t }$ and offloaded task number $\beta _ { t }$ , transmission delay of offloading tasks to the satellite can be calculated as following equation:

$$
d _ { 3 } ( \alpha _ { t } , \beta _ { t } ) = \frac { \beta _ { t } \phi } { r _ { \alpha _ { t } } } + d _ { 5 } , ~ \alpha _ { t } = 0 .\tag{6}
$$

2) Offload to BS: Denote by $K _ { \alpha _ { t } } , \alpha _ { t } \neq 0$ the duration that UAV will stay in the coverage of BS <sup>n</sup> since epoch <sup>t</sup>. As the UAV needs to guarantee that the forwarding process of all $\beta _ { t }$ tasks can be completed before the UAV flies out of the BS’s coverage, the number of forwarded tasks $\beta _ { t }$ satisfies the following constraint:

$$
\arg \operatorname* { m i n } _ { k } \left( \sum _ { i = t } ^ { t + k } r _ { \alpha _ { i } } \tau \geq \beta _ { t } \phi \right) \leq K _ { \alpha _ { t } } , \alpha _ { t } \in \mathcal { L } _ { t } , \alpha _ { t } \neq 0 ,\tag{7}
$$

which means that the transmission time of $\beta _ { t }$ tasks is shorter than the duration that the UAV stays in the BS’s coverage. Notice that duration $K _ { \alpha _ { t } }$ can be known a priori for the deployed UAV as it depends on the BSs’ location and the UAV trajectory [8].

Given the pathloss of the UAV-BS link $P L$ , data rate $r _ { \alpha _ { t } }$ of the UAV-BS <sup>n</sup> link can be calculated as

$$
r _ { \alpha _ { t } } = W _ { \mathrm { B } } \log _ { 2 } \left( 1 + { \frac { P _ { \mathrm { B } } \cdot 1 0 ^ { \frac { P L } { 1 0 } } } { \sigma _ { \mathrm { B } } ^ { 2 } } } \right) , \quad \alpha _ { t } \neq 0 ,\tag{8}
$$

where $W _ { \mathrm { B } }$ indicates the channel bandwidth of UAV-BS link, $P _ { \mathrm { B } }$ represents the transmission power of from the UAV to a BS, and $\sigma _ { \mathrm { B } } ^ { 2 }$ indicates the power of the background noise. Denote by $d _ { 3 }$ the transmission delay of offloading tasks to the BS, which is given by:

$$
d _ { 3 } ( \alpha _ { t } , \beta _ { t } ) = \frac { \beta _ { t } \phi } { r _ { \alpha _ { t } } } , ~ \alpha _ { t } \in \mathcal { L } _ { t } , \alpha _ { t } \neq 0 ,\tag{9}
$$

where $\alpha _ { t }$ and $\beta _ { t }$ represent offloading destination and offloaded task number, respectively.

## D. Energy Consumption Model

Generally, UAV energy consumption includes propulsion energy, communication-related energy, and computing-related energy. Since UAV propulsion energy is mainly depends on different trajectories and aircraft parameters, it can be considered as a constant in our work [29]. Thus, we aim to guarantee the remaining components of energy consumption, i.e., computing-related and communication-related energy, do not exceed the UAV energy capacity. Denote by $e _ { 0 }$ the communication-related energy caused by the transmission of tasks, which can be calculated as follows:

$$
e _ { 0 } ( \alpha _ { t } , \beta _ { t } ) = \left\{ \begin{array} { l l } { P _ { \mathrm { S } } d _ { 4 } ( \alpha _ { t } , \beta _ { t } ) , } & { \alpha _ { t } = 0 } \\ { P _ { \mathrm { B } } d _ { 4 } ( \alpha _ { t } , \beta _ { t } ) , } & { \alpha _ { t } \in \mathcal { L } _ { t } , \alpha _ { t } \ne 0 . } \end{array} \right.\tag{10}
$$

Meanwhile, processing computing task on the UAV also consumes energy, which depends on the computing workload of the computing task and the computing capability of the UAV. Denoted by $e _ { \mathrm { l } }$ the computing-related energy, which can be expressed as follows:

$$
e _ { \mathrm { l } } ( \alpha _ { t } , \beta _ { t } ) = \mathrm { m i n } \left\{ H _ { t } \phi \gamma , f _ { \mathrm { U } } \tau \right\} \cdot \xi \left( f _ { \mathrm { U } } \right) ^ { 2 } ,\tag{11}
$$

where $\xi$ indicates the effective switched capacitance determined by the chip architecture [8]. Denote by $E _ { t }$ the cumulative energy consumption in epoch <sup>t</sup>. Given the communication-related and computing-related energy consumption, the cumulative energy consumption can be calculated as the following equation:

$$
E _ { t } = E _ { t - 1 } + e _ { 0 } ( \alpha _ { t } , \beta _ { t } ) + e _ { 1 } ( \alpha _ { t } , \beta _ { t } ) .\tag{12}
$$

The cumulative energy consumption can be leveraged to evaluate whether the UAV satisfies the energy capacity or not.

## IV. PROBLEM FORMULATION

In our work, we aim to minimize the long-term delay of all computing tasks while satisfying the UAV energy consumption constraint. The total delay of all tasks in epoch <sup>t</sup> can be calculated as follows:

$$
D _ { t } = \left\{ \begin{array} { l l } { \displaystyle \frac { \beta _ { t } \phi \gamma } { f _ { \alpha _ { t } } } + \frac { \operatorname* { m i n } \left\{ \lfloor \frac { f _ { \mathrm { U } } \tau } { \phi \gamma } \rfloor , H _ { t } \right\} \phi \gamma } { f _ { \mathrm { U } } } } & \\ { + O _ { t } \tau + \frac { \beta _ { t } \phi } { r _ { \alpha _ { t } } } + d _ { S } , } & { \alpha _ { t } = 0 } \\ { \displaystyle \frac { \beta _ { t } \phi \gamma } { f _ { \alpha _ { t } } } + \frac { \operatorname* { m i n } \left\{ \lfloor \frac { f _ { \mathrm { U } } \tau } { \phi \gamma } \rfloor , H _ { t } \right\} \phi \gamma } { f _ { \mathrm { U } } } } & \\ { + O _ { t } \tau + \frac { \beta _ { t } \phi } { r _ { \alpha _ { t } } } , } & { \alpha _ { t } \neq 0 , } \end{array} \right.\tag{13}
$$

where both the computing delay and the transmission delay are included. Let $\pmb { \alpha } = \{ \alpha _ { t } , \forall t \}$ and $\beta = \{ \beta _ { t } , \forall t \}$ denote the set of task offloading decisions and the number of offloaded tasks in each epoch, respectively. As link availability and task arrival are highly dynamic, we concentrate on minimizing the timeaveraged delay of all tasks. The delay minimization problem can be formulated as follows:

$$
\operatorname { P 1 : } \operatorname* { m i n } _ { \{ \alpha , \beta \} } \operatorname* { l i m } _ { T \to \infty } \frac { 1 } { T } \sum _ { t = 1 } ^ { T } D _ { t }\tag{14a}
$$

$$
{ \mathrm { s . t . } } \quad ( 7 ) ,\tag{14b}
$$

$$
\operatorname* { l i m } _ { T  \infty } \frac { 1 } { T } \sum _ { t = 1 } ^ { T } [ e _ { 0 } ( \alpha _ { t } , \beta _ { t } ) + e _ { 1 } ( \alpha _ { t } , \beta _ { t } ) ] \leq \varepsilon ,
$$

$$
\alpha _ { t } \leq N , \alpha _ { t } \in \mathcal L _ { t } ,\tag{14c}
$$

$$
\beta _ { t } \le \beta _ { \operatorname* { m a x } } , \beta _ { t } \in \mathbb { N } ,\tag{14d}
$$

(14e)

where (14a) is the objective that minimizes the time-average delay of all collected tasks over <sup>T</sup> epochs, and (14b) limits the offloading destinations and the number of offloading tasks. (14c) restricts the time-averaged energy consumption of the UAV where <sup>ε</sup> is the UAV energy capacity. (14d) and (14e) constrain task offloading decisions and the numbers of offloaded tasks, respectively. Problem P1 is an integer nonlinear optimization problem with unknown number of newly collected tasks in each epoch, which is difficult to solve. Considering the UAV location and the backlog of unaccomplished task in the computing queue evolve in an ergodic way, we adopt the stationary decision to address this problem, which is time-invariant and only depends on the current system status. Therefore, the problem can be reformulated as a Markov decision process (MDP) for a stationary decision which is the optimal in the ergodic system [35].

We define a tuple $\mathcal { M } : = \langle S , A , P , C , \Pi \rangle$ to model the MDP, which is a sequential decision-making process. Specifically, S represents the set of states. A is the set of actions. $P : = S \times A \times S \to \mathbb { R }$ is set of state transition probabilities. $C : = S \times A $ <sup>R</sup> indicates the cost function. Π is the policy that is a decision rule mapping from a state $s \in S$ to an action $\mathbf { \delta } _ { a } \in \mathbf { \delta } _ { A }$ . Meanwhile, $C ( s , a )$ is defined as the cost when the system stays in state s with adopting action a. For the aforementioned problem, the states, actions, and cost in an MDP model are formulated as follows.

1) State: In epoch <sup>t</sup>, a tuple denoted by $\begin{array} { r l } { s _ { t } } & { { } = } \end{array}$ $( l _ { t } , F _ { t } , H _ { t } , E _ { t } ) , s _ { t } \in S$ is used to describe the system state, where $l _ { t } , F _ { t } , H _ { t } , E _ { t }$ represent UAV location, the number of offloaded tasks in the forwarding queue, the unaccomplished task backlog in the computing queue and the cumulative energy consumption, respectively.

2) Action: An action is made based on the current state, and the decision is denoted by a tuple $\mathbf { } a _ { t } = ( \alpha _ { t } , \beta _ { t } ) , \mathbf { } a _ { t } \in A$ in epoch $t ,$ where $\alpha _ { t }$ <sup>= ( )</sup>is used to indicate offloading destination, and $\beta _ { t }$ denotes the number of the offloaded tasks.

3) State Transition: The state transition includes four components: the update of $l _ { t } .$ , which only depends on the predefined UAV trajectory and the evolutions of $F _ { t } , H _ { t } , E _ { t }$ , which are discussed in the preceding section.

4) Cost Function: Considering an intuitive policy that the UAV does not offload tasks and keep the queue full, and almost all newly arrived tasks will be dropped. In such case, although the cost (delay) can be minimized, an excessive number of dropped tasks lead to practical infeasibility. To minimize the cost while avoiding the excessive task dropping, a penalty $\Lambda _ { t }$ is introduced as follows:

$$
\Lambda _ { t } = \lambda \operatorname* { m a x } \left( M _ { t } + O _ { t } - \rho , 0 \right) ,\tag{15}
$$

where $( M _ { t } + O _ { t } - \rho , 0 )$ represents the excessive number of the newly collected tasks will be dropped, and <sup>λ</sup> is a constant penalty weight. With the objective of minimizing long-term delay of all IoT tasks, the cost function can be defined as $C ( \pmb { \mathscr { s } } _ { t } , \pmb { \mathscr { a } } _ { t } ) = D _ { t } + \Lambda _ { t } ,$ , where $\Lambda _ { t }$ is the penalty to avoid excessive drop of computing tasks.

5) Policy: Denote by π the stationary policy, which means that state $\mathbf { } _ { s _ { t } }$ is assigned with action $\mathbf { } \mathbf { a } _ { t }$ and this action will be chosen whenever the system stays in this state.

Therefore, MDP based delay-oriented tasks scheduling problem can be formulated as follows:

$$
\mathrm { P 2 } \mathrm { : } \operatorname* { m i n } _ { \pi } \operatorname* { l i m } _ { T  \infty } \mathbb { E } [ \frac { 1 } { T } \sum _ { t = 1 } ^ { T } C _ { t } ( s _ { t } , a _ { t } ) \bigg | \pi ]\tag{16a}
$$

$$
\mathrm { s . t . } \quad ( 1 4 \mathrm { b } ) , ( 1 4 \mathrm { d } ) , ( 1 4 \mathrm { e } )
$$

$$
\operatorname* { l i m } _ { T \to \infty } \mathbb { E } \left[ \frac { E _ { t } } { T } \Big | \pi \right] \leqslant \varepsilon ,\tag{16b}
$$

(16c)

where (16a) represents the expected average cost and expected energy consumption. Problem P1 is transformed into problem P2 to find the optimal policy π with respect to a cost ${ \cal C } _ { t } ( s _ { t } , a _ { t } )$ for choosing action a at state s, which minimizes the expected average cost. Above problem P2 is a constrained MDP (CMDP) problem, which is a typical MDP problem with additional constraints. Solving such a CMDP problem with uncertainty is challenging. On the one hand, typical MDP problems are well-investigated, which can be solved by iterative methods by finding a deterministic policy, such as the policy iteration and the value iteration [36]. However, these methods for MDP cannot cope with the CMDP problem since constraints and the objective cannot be optimized simultaneously. On the other hand, although CMDP problems with the known transition probability can be solved simply via a linear programming method, the linear programming method cannot address the CMDP problem with uncertainty, since transition probability $P ( H _ { t + 1 } | H _ { t } )$ is unknown due to the uncertainty of the arrived task number.

## V. DEEP RISK-SENSITIVE RL ALGORITHM

In this section, we first introduce the preliminary of RL methods. Afterward, by tailoring the typical RL methods, we propose the deep risk-sensitive RL algorithm to address problem P2. Finally, we present the details of DNN-based implementation of the proposed algorithm.

## A. Preliminary

In problem P2, since the objective is to find policy π that chooses appropriate actions at different states to minimize the long-term cost (delay), which consists of the immediate cost (generated in the current epoch) and the future cost (generated in the following epochs) for each state-action pair. Because the future cost is related to both the current scheduling action and the actions in the following epochs, it is challenging to model the relationship between the current action and the future cost, particularly in the case with unknown state transition probability. Therefore, the discounted cost model is designed to balance the immediate cost and the future cost for each state-action pair, which is calculated as $\begin{array} { r } { \sum _ { t = 0 } ^ { \infty } \varsigma ^ { t } C ( \pmb { s } _ { t } , \pmb { a } _ { t } ) } \end{array}$ [35]. Note that the discount factor, denoted by $\varsigma \in [ 0 , 1 ]$ is to prevent the long-term cost from going to negative infinity.

Then, to measure the long-term cost starting from state s under policy π, a value function is defined to determine the value of expected long-term discounted cost when the system is at state s. Denote by $V _ { \pi } ( s )$ the value function, which is given by:

$$
V _ { \pi } ( s ) = \mathbb { E } \left[ \sum _ { t = 0 } ^ { \infty } \varsigma ^ { t } C ( s _ { t } , a _ { t } ) | \pi , s _ { 0 } = s \right] .\tag{17}
$$

Based on 17, a Q-value function is defined to further evaluate state-action pairs, which is denoted by $Q _ { \pi } ( s _ { t } , \pmb { a } _ { t } )$ . Such the Q-value function measures the expected long-term discounted cost that the system may get from being at state s, following policy π and choosing action a, which is given by:

$$
Q _ { \pi } ( s _ { t } , \pmb { a } _ { t } ) = C ( \pmb { s } _ { t } , \pmb { a } _ { t } ) + \sum _ { \pmb { s } _ { t + 1 } } \varsigma P ( \pmb { s } _ { t + 1 } | \pmb { s } _ { t } , \pmb { a } _ { t } ) V _ { \pmb { \pi } } ( \pmb { s } _ { t + 1 } ) .\tag{18}
$$

With the objective of the cost minimization, we choose the minimum Q-value as the optimal Q-value, which is denoted by $\begin{array} { r } { Q _ { \pi } ^ { * } ( s , { \pmb a } ) = \operatorname* { m i n } _ { \pi } Q _ { \pi } ( s , { \pmb a } ) } \end{array}$

<sup>( ) = min ( )</sup>Generally, due to the unknown state transition probability, the basic idea behind model-free RL methods is temporal difference (TD) learning, i.e., the current approximation of Qvalue function (which might not be accurate) can be leveraged to update the estimated value for the following states [37]. The mechanism of the RL methods allows the UAV to iteratively update and approximate the Q-value function and then choose actions based on the approximated Q-value function. Therefore, RL methods can learn online and interact with the environment simultaneously, which is suitable for the considered case with unknown task arrival. Denote by ${ \mathbf { } } ^ { a ^ { * } } =$ arg mir $\mathbf { \lambda } _ { \mathbf { { a } } _ { t } \in \mathbf { { } } A } Q _ { \pi } ( \mathbf { { \overset { . } { s _ { t } } } } , \mathbf { { \overset { . } { a _ { t } } } } )$ the greedy action which acquires the optimal Q-value. The Q-value can be updated based on the following TD backup equation:

$$
Q _ { \pi } ^ { \prime } ( s _ { t } , a _ { t } ) = Q _ { \pi } ( s _ { t } , a _ { t } ) + \eta \left[ \boldsymbol { C } ( s _ { t } , a _ { t } ) + \varsigma Q _ { \pi } ( s _ { t + 1 } , a ^ { * } ) \right] ,\tag{19}
$$

where the learning rate denoted by <sup>η</sup> is to determine how much newly acquired cost should be accepted to adjust the evaluation of Q-value function. Note that $0 < \eta < 1$ is a constant value in the learning process. The convergence of such RL methods based on Q-value iteration has been proved, i.e., the Q-values converge to the optimal Q-values [35].

Conventional RL methods update Q-values based on a Q-value table, i.e., all state-action pairs are listed in a table, and each pair is updated iteratively and independently. However, tabular methods require a large memory to store all stateaction pairs, which increases exponentially with the state and action space [37]. Due to the curse of dimensionality in the considered scenario (e.g., a large number of UAV locations, the large size of the computing queue backlog), conventional tabular RL methods cannot be applied practically. To deal with the aforementioned problem, instead of tabular methods, DNN is adopted to approximate Q-value function [38]. Let <sup>ϑ</sup> be the parameters of DNN, which includes neural network weights and biases. Denote by $Q _ { \pi } ( \boldsymbol { s } _ { t } , \boldsymbol { a } _ { t } ; \boldsymbol { \vartheta } )$ the DNN-based Q-value function, which is updated by minimizing the following loss function:

$$
L ( \vartheta ) = | C ( s _ { t } , a _ { t } ) + \varsigma Q _ { \pi } ( s _ { t + 1 } , a ^ { * } ; \vartheta ) - Q _ { \pi } ( s _ { t } , a _ { t } ; \vartheta ) | ^ { 2 } ,\tag{20}
$$

where $L ( \vartheta )$ is named as the TD error. Similar to tabular RL methods, DNN-based RL methods can also allow the UAV to iteratively update the DNN-based Q-value function and then choose actions based on the approximated DNN-based Q-value function in an online manner.

## B. The Deep Risk-Sensitive RL Algorithm Design

In problem P2, apart from the objective of cost minimization, there is an extra constraint of energy capacity that needs to be satisfied. However, since the energy consumption is not a component of the cost function, conventional RL methods mentioned above cannot satisfy the constraint in problem P2. Therefore, we propose a deep risk-sensitive RL algorithm to deal with the CMDP problem. Specifically, in addition to the cost function, an extra risk function is defined to capture whether the UAV energy consumption in the current epoch violates the UAV energy capacity constraint, and then a corresponding Q-value function is defined to evaluate the value of risk. Therefore, the algorithm has two Q-value functions, i.e., one Q-value function to evaluate the cost and the other Q-value function to evaluate the risk. Afterward, the proposed deep risk-sensitive RL algorithm updates two different Q-value functions independently and chooses the action based on the sum of two Q-value functions.

Define the set of error states as $\varPhi \subseteq S .$ . An error state $s _ { t } ~ \in ~ \varPhi$ represents the energy consumption of the UAV in epoch <sup>t</sup> exceeds the UAV energy capacity, i.e., $E _ { t } > \varepsilon t$ . Then, to measure how much consumed energy that exceeds the UAV energy capacity when the system is at state s choosing action $^ { a , }$ we denote the risk function by $R ( s _ { t } , \pmb { a } _ { t } )$ , which is given by:

$$
R ( \pmb { s } _ { t } , \pmb { a } _ { t } ) = \left\{ \begin{array} { l l } { | E _ { t } - \varepsilon t | , } & { \mathrm { i f } \ \pmb { s } _ { t } \in \varPhi } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.\tag{21}
$$

The value of risk that are at a non-error state is zero, and the value of risk at an error state is equivalent to the exceeding part of the energy consumption. Consequently, if the current state of the system is an error state, the following states will also be error states with the increased value of risk. To satisfy the UAV energy capacity constraint in problem P2, the value of risk at each state should be zero. Thus, we transform the goal that keeps the energy consumption below the energy capacity into the goal that minimize the risk. Note that the risk minimization is not equivalent to energy consumption minimization since the energy consumption minimization is not the objective of this problem.

Similar to the aforementioned cost minimization, the risk minimization can be achieved by using another Q-value function, which is operated separately. Based on the discounted risk, we define the expected long-term discounted risk as the value function $\bar { V } _ { \pi } ( s )$ of state s under policy π, which is given by:

$$
\bar { V } _ { \pi } ( s ) = \mathbb { E } \left[ \sum _ { t = 0 } ^ { \infty } \bar { \varsigma } ^ { t } R ( s _ { t } , { a } _ { t } ) | \pi , s _ { 0 } = s \right] ,\tag{22}
$$

where $\bar { \zeta }$ is the discount factor for the discounted risk. Then, to measure the expected long-term discounted risk that the UAV may get from being at state s, following policy π and choosing action a, the corresponding Q-value function, $\bar { Q } _ { \pi } ( s _ { t } , { \pmb a } _ { t } )$ , is defined as follows:

$$
\bar { Q } _ { \pi } ( s _ { t } , \mathbf { a } _ { t } ) = R ( s _ { t } , \mathbf { a } _ { t } ) + \sum _ { s _ { t + 1 } } \bar { \varsigma } P ( s _ { t + 1 } | s _ { t } , \mathbf { a } _ { t } ) \bar { V } _ { \pi } ( s _ { t + 1 } ) .\tag{23}
$$

Based on the TD learning, the Q-value function of risk can also be estimated based on the following equation:

$$
\bar { Q } _ { \pi } ^ { \prime } ( s _ { t } , a _ { t } ) = \bar { Q } _ { \pi } ( s _ { t } , a _ { t } ) + \bar { \eta } \left[ R ( s _ { t } , a _ { t } ) + \bar { \zeta } \bar { Q } _ { \pi } ( s _ { t + 1 } , \bar { a } ^ { * } ) \right] ,\tag{24}
$$

where <sup>η</sup> is the learning rate for the risk minimization, and greedy action $\begin{array} { r } { \bar { \pmb { a } } ^ { * } = \arg \operatorname* { m i n } _ { \pmb { a } _ { t } \in \pmb { A } } \bar { Q } _ { \pi } ( s _ { t } , \pmb { a } _ { t } ) } \end{array}$ is adopted to acquire the optimal Q-value. $\mathbf { A } \mathbf { s } \ \bar { \mathbf { a } } ^ { * }$ and $\mathbf { \delta } \mathbf { \textit { a } } ^ { * }$ are two different greedy actions based on different goals, i.e., cost minimization and risk minimization, the chosen actions may not be the same at each state. However, only one action can be selected when each state is reached. Thus, we need to design a new Q-value function to combine two goals. which is given by:

$$
Q _ { \pi } ^ { \delta } ( s _ { t } , \mathbf { a } _ { t } ) = Q _ { \pi } ( s _ { t } , \mathbf { a } _ { t } ) + \delta \bar { Q } _ { \pi } ( s _ { t } , \mathbf { a } _ { t } ) ,\tag{25}
$$

where <sup>δ</sup> is a weight parameter to balance two different goals. If <sup>δ</sup> is fixed, $Q ^ { \delta }$ forms a standard Q-value function of stateaction pair with respect to the new reward $C + \delta R$ , which is same as the Q-value function in typical RL methods [39] [40]. Specifically, when $\delta = 0 , Q ^ { \delta } = Q$ , the minimization of the weighted sum of the cost and the risk leads to the optimal policy for cost minimization, which is same as the cost minimization without constraints. When <sup>δ</sup> tends to infinity, the minimization of the weighted sum of the cost and the risk leads to the optimal policy for the risk minimization. As the adaption of $\delta$ provides a method to find the space of feasible polices, <sup>δ</sup> can be adjusted to produce the optimal policy to minimize the cost while satisfying the constraint. Therefore, there exists the optimal deterministic policy for the designed new Q-value function, and the convergence of proposed deep risk-sensitive RL algorithm can be guaranteed if discount factors <sup>ς</sup> and <sup>ς</sup> are equivalent [37].

Algorithm 1 Deep Risk-Sensitive RL Algorithm   
1 Initialize: $\varepsilon ,$ replay memory $D ; \vartheta , \vartheta ^ { \prime } , \bar { \vartheta } , \bar { \vartheta } ^ { \prime } ;$ state $s _ { \mathrm { 0 } } ;$   
step size $\Delta ; \delta ;$   
2 for $k = 1 , 2 , 3 , \cdots , K$ do   
3 for $t = 1 , 2 , 3 , \cdots , T$ do   
4 <sup>= 1</sup>Choose $\mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf \mathbf { } \mathbf \mathbf \mathbf \mathbf \Psi \mathbf \Psi \mathbf \Psi \mathbf \Psi \mathbf \Psi \mathbf \Psi \mathbf \Psi \mathbf \Psi \mathbf \Psi \mathbf $ select a random action with probability   
<sup></sup>, or select $\left[ Q ( s _ { t } , \pmb { a } ; \vartheta ) + \delta \bar { Q } ( s _ { t } , \pmb { a } ; \bar { \vartheta } ) \right]$   
with probability $\stackrel { a } { 1 } - \stackrel { \cdot } { \epsilon } ;$   
5 Perform action $\mathbf { } \mathbf { a } _ { t }$ and observe cost $C _ { t } ,$ risk $R _ { t }$ and   
next state $s _ { t + 1 } ;$   
6 Store transition $\left( { { s _ { t } } , { a _ { t } } , { C _ { t } } , { R _ { t } } , { s _ { t + 1 } } } \right)$ in $D ;$   
7 Sample random mini-batch of transitions   
$( s _ { j } , { \pmb a } _ { j } , C _ { j } , R _ { j } , { \pmb s } _ { j + 1 } )$ from $D ;$   
8 <sup>(</sup>Set $y _ { j } = \stackrel { \_ } { C _ { j } } + \stackrel { \_ } { \varsigma } \operatorname* { m i n } _ { \binom { \prime } { \rho ^ { \prime } } } ( s _ { j + 1 } , \pmb { a } ^ { \prime } ; \vartheta ^ { \prime } ) ) ;$   
ma   
9 Set $\bar { y } _ { j } = R _ { j } + \bar { \varsigma } \operatorname* { m i n } _ { { \alpha ^ { \prime } } } ( \bar { Q } ^ { \prime } ( s _ { j + 1 } , { \pmb a } ^ { \prime } ; \bar { \vartheta } ^ { \prime } ) ) ;$   
10 Perform a gradient descent step on   
$\mathbb { E } _ { ( s _ { j } , a _ { j } , C _ { j } , R _ { j } , \pmb { s } _ { j + 1 } ) \sim U ( D ) } \big [ ( y _ { j } - Q ( \pmb { s } _ { j } , \pmb { a } _ { j } ; \vartheta ) ) ^ { 2 } \big ]$   
with respect to <sup>ϑ</sup>;   
11 Perform a gradient descent step on   
$\mathbb { E } _ { ( s _ { j } , a _ { j } , C _ { j } , R _ { j } , \pm _ { j + \underline { { 1 } } } ) \sim U ( D ) } \left[ \left( \bar { y } _ { j } - \bar { Q } ( s _ { j } , \pmb { a } _ { j } ; \bar { \vartheta } ) \right) ^ { 2 } \right]$   
with respect to <sup>ϑ</sup>;   
12 Set $\vartheta ^ { \prime } = \vartheta ,$ and $\bar { \vartheta } ^ { \prime } = \bar { \vartheta } ;$   
13 end   
14 if $\begin{array} { r } { \frac { E _ { T } } { T } > \varepsilon } \end{array}$ then   
15 $\begin{array} { r } { \hat { \delta }  \delta + \Delta ; } \end{array}$   
16 else   
17 $\delta \longleftarrow \delta - \Delta ;$   
18 end   
19 end   
20 Output: DNN models with parameters $\vartheta$ and ${ \bar { \vartheta } } ,$ and   
weight parameter <sup>δ</sup>

Due to the curse of dimensionality, we adopt DNN to approximate the Q-value function of risk as the approximation of the DNN-based Q-value function of cost. Denote by $\bar { Q } _ { \pi } ( s _ { t } , { \mathbf { \em a } } _ { t } )$ the DNN-based Q-value function of risk, where <sup>( )ϑ</sup> is the parameter of the corresponding neural network. The update of DNN-based Q-value function of risk is the same as that of Q-value function of cost in (20). As shown in Algorithm 1, we propose a two-cycle algorithm to minimize the cost while minimizing the risk, i.e., learn the appropriate parameters of DNNs in the inner cycle, and search the appropriate weight parameter to balance two goals in the outer cycle. The former is shown from line 4 to line 20, and each inner cycle is named as an iteration. In one iteration, the DNN parameters of $Q _ { \pi } ( \boldsymbol { s } _ { t } , \boldsymbol { a } _ { t } ; \boldsymbol { \vartheta } )$ and $\bar { Q } _ { \pi } ( s _ { t } , \pmb { a } _ { t } ; \bar { \vartheta } )$ are updated separately and iteratively. The searching in the outer cycle is shown from line 3 to line 21. Each outer cycle is named as an episode. In each outer cycle, the optimal weight parameter <sup>δ</sup> is updated according to the energy consumption, which is shown from line 16 to line 20. Based on whether the energy consumption in the current episode satisfies the constraint, weight parameter <sup>δ</sup> is increased or decreased with a fixed step size denoted by $\Delta .$ . The partial detail of Algorithm 1 is introduced in the next subsection.

## C. DNN-Based Implementation

Instead of constructing space-costly Q-tables in conventional RL methods, we implement the proposed algorithm by approximating the Q-value function via DNNs. However, directly replacing the Q-table by a DNN model meets several challenges, e.g., unavailable actions at each state cannot be deleted simply by DNNs due to the “black-box” characteristic of DNN. Therefore, we should design the DNN model to fit the proposed algorithm, the details of which are introduced as follows. As shown in Fig. 3, four significant modules are introduced, i.e., DNN replacement, filter layer design, experience replay, and <sup></sup>-greedy selection.

1) DNN Replacement: For a more stable training, we adopt two DNNs to estimate a Q-value function, i.e., one for a target network and the other for a prediction network. The target network has the same DNN architecture as the prediction network but with frozen parameters. For every certain number of iterations, the parameters from the prediction network are copied to the target network, and this procedure is called DNN replacement. Since the TD error is used as the loss function in DNN backpropagation to approximate Q-value function by DNNs, the backpropagation requires the output gradient of DNN with respect to weights for input epoch <sup>t</sup>, and this gradient needs to be saved until we have the new TD error at epoch <sup>t</sup> . Thus, there always exists a predicted value for epoch <sup>t</sup> when we compute gradient at epoch <sup>t</sup>. If we use the same DNN to calculate the predicted value (e.g., <sup>Q</sup><sub>π</sub> s<sub>t</sub><sup>,</sup> a<sub>t</sub> <sup>ϑ</sup> ) and the target value $( \mathrm { e . g . } , C ( s _ { t } , { \pmb a } _ { t } ) + \varsigma Q _ { \pi } ( s _ { t + 1 } , { \pmb a } ^ { * } ; \vartheta ) )$ , the DNN can become destabilized in the feedback loops between the target value and the predicted value [37]. Considering cost minimization and risk minimization are independent, we leverage two DNNs to approximate Q-value function of cost, and another two DNNs to estimate Q-value function of risk, which are shown in Fig. 3.

2) Filter Layer Design: We adopt a filter layer to exclude the outputs of unavailable actions. In the considered problem, the available action set at different states is different. For example, the UAV can only offload tasks to the nearby BSs, and thus available action set $\mathcal { L } _ { t }$ changes with the location of UAV $l _ { t } .$ . However, since the output size of a fully connected layer in DNN is fixed, the number of Q-value outputs from DNN cannot be changed according to the various number of actions in the available set. As a result, the unavailable actions are included in the DNN-based approximation of Q-value, which is incorrect. Furthermore, constraint (7) needs to be guaranteed and requires the various available action set at different states. Thus, we adopt a binary coding in the filter layer, which can select available action depending on the current state. Then, to exclude unavailable actions, the Q-value of these actions can be increased (i.e., add a constant to the original Q-value, which is a hyper-parameter depending on the magnitude of Q-values). These actions are excluded since only the minimal Q-value is selected to feed into the loss function. As shown in Fig. 3, a filter layer is added to help the target network exclude invalid actions and output real Q-values.

3) Experience Replay: Considering the high correlation between continuous states in this scenario (e.g., cumulative energy consumption $E _ { t }$ is highly correlated with $E _ { t + 1 }$ due to the accumulative sum), DNN can be easily over-fitting if high correlation data is fed. Furthermore, the DNN is required to not only learn from current interaction with the environment but also a more varied array of past experiences (e.g., past task arrival pattern). To this end, experience replay is utilized to store experiences including state transitions, costs, risks, and actions, which are necessary to perform the proposed deep risk-sensitive RL. As shown in Fig. 3, the replay memory, denoted by $D ,$ is used to store experience, and mini-batches of experiences are fed to train DNNs. In Algorithm 1, minibatches of experience $( { \pmb s } _ { j } , { \pmb a } _ { j } , C _ { j } , R _ { j } , { \pmb s } _ { j + 1 } ) \ \sim \ U ( D )$ are uniformly draw at random from the replay memory to update DNNs. This technique has the following merits: 1) reducing the correlation among experiences in updating DNNs, 2) reusing the previous state transitions to avoid catastrophic forgetting, and 3) increasing learning efficiency with minibatches and learning stability.

![](images/962e13128e18033fd4b60f9287379aae720791a3e40daef0c0640cdec8ec8b2e.jpg)  
Fig. 3. An overview of the deep RL-based DOTS scheme.

4) <sup></sup>-Greedy Selection: To learn how to react to all possible states in the environment, it must be exposed to as many as possible states. The UAV needs to explore different energy consumption and the number of tasks in the buffer. However, the UAV needs to exploit the exposed experiences to learn a decent task scheduling policy, which conflicts the experience exploration. Thus, the proposed learning policy should deal with such an exploration and exploitation trade-off. To deal with this problem, the <sup></sup>-greedy selection approach is leveraged to balance the trade-off. The UAV selects the action based on approximated Q-value function most of the time, but occasionally chooses the action randomly. In the realization of Algorithm 1, parameter <sup></sup> is an adjustable parameter which determines the probability of taking a random action, rather than the action based on the Q-value function.

## VI. PERFORMANCE EVALUATION

In this section, extensive simulations are carried out to evaluate the proposed deep RL-based DOTS scheme. Specifically, we first elaborate on the simulation settings, and benchmark strategies. Afterward, the overall performance evaluation of the proposed scheme is conducted.

## A. Simulation Settings

In the experiments, locations of IoT devices follow a uniform distribution [8]. The computing task arrival is set to follow a Poisson distribution with arrival rate $\mu ,$ which is unknown a priori for the UAV [1]. Referring to well-studied UAV trajectory design algorithm [29], a UAV is dispatched. The UAV flies along with main areas of IoT devices, which can be more effective to accommodate the IoT service demand. The UAV trajectory is generated by the VISSIM which is a simulation tool in transportation research [15]. The altitude of the UAV is set to 10 m, and the size of computing queue $\rho$ is set to 20. Additionally, by adopting the pathloss (in dB) model of UAV communication in [8], the pathloss of UAV-BS links is given by:

$$
\begin{array} { r } { P L \left( x , \theta \right) = 1 0 A _ { 0 } \log \left( x \right) + B _ { 0 } \left( \theta - \theta _ { 0 } \right) e ^ { \frac { \theta _ { 0 } - \theta } { C _ { 0 } } } + \eta _ { 0 } , } \end{array}\tag{26}
$$

where <sup>x</sup> represents the distance between the UAV and a BS, and $\theta$ is the corresponding vertical angle. Both <sup>x</sup> and <sup>θ</sup> can be obtained based on UAV location $l _ { t }$ and the BS location. Due to the mobility of the deployed UAV, <sup>x</sup> and <sup>θ</sup> vary over different locations. Parameters <sup>A</sup><sub>0</sub>, <sup>θ</sup><sub>0</sub>, <sup>B</sup><sub>0</sub>, $C _ { 0 }$ and $\eta _ { 0 }$ in (26) are configured as 3.04, -3.61, -23.29, 4.14, and 20.7, respectively [8]. Meanwhile, the LEO satellite connection is always available for the UAV. The Weibull-based channel model is adopted to model the rain attenuation of UAV-satellite links [41]. Other simulation parameters are listed in Table I.

The proposed DNN-based scheme is implemented via Python 3.7 and Tensorflow open-source machine learning library [42]. The training of DNNs is conducted with a NVDIA 1660 Ti GPU. The DNN of cost minimization includes four fully-connected hidden layers with (256, 128, 128, 64) neurons, and the DNN of risk minimization includes four fully-connected hidden layers with (512, 256, 128, 128) neurons, respectively. ReLU function is adopted as the activation function to realize nonlinear approximation after the fully connected layers. Additionally, L2 regularization is used to reduce the possibility of DNN over-fitting. Meanwhile, Adam optimizer is adopted in the DNN training. In each episode, the behavior policy during training is <sup></sup>-greedy with <sup></sup> increases linearly from 0 to 0.9995 over 35,000 iterations.

TABLE I  
SIMULATION PARAMETERS
<table><tr><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td><td rowspan=1 colspan=1>Parameter</td><td rowspan=1 colspan=1>Value</td></tr><tr><td rowspan=1 colspan=1> $N$ </td><td rowspan=1 colspan=1>5</td><td rowspan=1 colspan=1> $f _ { \mathrm { U } }$ </td><td rowspan=1 colspan=1>1 Gigacycle/s</td></tr><tr><td rowspan=1 colspan=1> $\phi$ </td><td rowspan=1 colspan=1>5MB</td><td rowspan=1 colspan=1> $f _ { 0 }$ </td><td rowspan=1 colspan=1>5 Gigacycle/s</td></tr><tr><td rowspan=1 colspan=1> $\gamma$ </td><td rowspan=1 colspan=1>25 cycles/bit</td><td rowspan=1 colspan=1> $f _ { n } , n$ ≠0</td><td rowspan=1 colspan=1>10 Gigacycle/s</td></tr><tr><td rowspan=1 colspan=1> $W _ { \mathrm { B } }$ </td><td rowspan=1 colspan=1>3MHz</td><td rowspan=1 colspan=1> $N _ { 0 }$ </td><td rowspan=1 colspan=1>-174 dBm/Hz</td></tr><tr><td rowspan=1 colspan=1> $W _ { \mathrm { S } }$ </td><td rowspan=1 colspan=1>2MHz</td><td rowspan=1 colspan=1> $P _ { \mathrm { { B } } }$ </td><td rowspan=1 colspan=1>1.6W</td></tr><tr><td rowspan=1 colspan=1> $P _ { \mathrm { S } }$ </td><td rowspan=1 colspan=1>5W</td><td rowspan=1 colspan=1> $\xi$ </td><td rowspan=1 colspan=1> $\overline { { 1 0 ^ { - 2 8 } } }$ </td></tr><tr><td rowspan=1 colspan=1> $d _ { \mathrm { S } }$ </td><td rowspan=1 colspan=1>6.44 ms</td><td rowspan=1 colspan=1> $\overline { { \beta ^ { \mathrm { m a x } } } }$ </td><td rowspan=1 colspan=1> $^ { 7 }$ </td></tr></table>

Benchmark schemes adopted in this computing task scheduling problem are introduced below:

1) Random Probabilistic Configuration (RPC): In this scheme, the random policy is adopted, which means that actions are selected randomly in different states. All available actions are selected with the same probability.

2) Sampling-Based Probabilistic Configuration (SPC): In this scheme, the probability of available actions on each state is fixed. Based on a large number of historical sampling experiments, the probability of different actions is configured to meet the UAV energy capacity.

## B. Simulation Results

We show the simulation results of our proposed algorithm from two parts. Firstly, we evaluate the convergence performance of the proposed deep RL-based DOTS scheme. Secondly, we compare the performance of the proposed deep RL-based DOTS scheme with other benchmark schemes.

1) Convergence Performance: The convergence performance of the two-cycle structure of the proposed algorithm is shown in this subsection, i.e., the convergence performance of the inner cycle in Fig. 4 and that of the outer cycle in Fig. 5.

Fig. 4(a) shows the convergence performance of the delay and the energy consumption in the inner cycle (in one episode), respectively, where the orange line is the moving average results of the previous 100 iterations. It can be seen that the delay converges after 16,000 iterations, when UAV energy capacity <sup>ε</sup> is set to 55 Joule. However, the convergence trends of delay and energy consumption vary differently due to the differentiated functions of the cost and the risk. Specifically, the delay performance gradually decreases and converges after around 16,000 iterations, while the energy consumption performance exhibits a turning point at around the 11,000 th iteration. Compared to the simple policy of minimizing the risk, e.g., the UAV can offload fewer tasks to reduce energy consumption intuitively, the policy of minimizing the cost is related to both the task arrival and the policy of minimizing the risk. As a result, as shown in Fig. 4(b), from iteration 0 to iteration 11,000, the policy of minimizing the risk has been well learned, while the learning process of cost minimization is still ongoing as shown in Fig. 4(a). After 16,000 iterations, the policy of delay minimization is learned while the energy consumption is approximately equivalent to the UAV energy capacity.

The convergence performance of delay and energy consumption in the outer cycle are shown in Fig. 5(a) and Fig. 5(b), respectively. To evaluate the convergence performance of the proposed DOTS scheme, we adopt different values of the UAV energy capacity, i.e., 50 Joule, 55 Joule, and 60 Joule. It can be seen that the average delay and average energy consumption converge after 70 episodes, where one episode consists of 35,000 iterations. Both the average delay and the average energy consumption oscillate at the beginning of the learning process due to the inaccurate weight parameter $\delta ,$ which takes time to approach to the optimal weight parameter. In Fig. 5(a), we can observe that the average delay of the learned policy decreases as the increase of the UAV energy capacity of the UAV, which happens since more energy can be consumed by the UAV to offload more tasks to either the BS or the satellite. In Fig. 5(b), the impact of energy consumption is shown on different energy consumption capacities. As expected, the energy consumption of different cases is approximately equivalent to the pre-set energy consumption capacities. Therefore, based on aforementioned convergence performance, the DOTS scheme can work well in scenarios with different energy consumption capacities.

2) Performance Comparison: To compare DOTS with benchmark schemes, we plot cumulative distribution functions (CDFs) of delay and energy consumption in Fig. 6(a) and Fig. 6(b), respectively. Note that average delay and energy consumption are calculated for the period that UAV flies back to the same destination along the same trajectory. Considering the dynamics of task arrival, we show the delay and energy consumption performance over 1,000 flights. We can see that DOTS is able to enhance the performance that the delay in 90 flights which is below 9 seconds. Meanwhile, 60 flights satisfy energy capacity of <sup>ε</sup>   Joule. The RPC scheme cannot guarantee the UAV energy capacity constraint. Although the SPC scheme can satisfy the energy capacity, the delay of most flights is longer than 8.5 seconds. Therefore, the proposed DOTS scheme can work efficiently in different task arrival scenarios.

Figure 7(a) and 7(b) show the delay and energy consumption performance under DOTS, RPC, and SPC schemes, where the energy capacity is set to <sup>ε</sup>  Joule. In the simulation, we set the probability of offloading tasks in the SPC scheme to satisfy energy capacity 55 Joule. It can be seen that the DOTS scheme and the SPC scheme are able to guarantee the UAV energy capacity constraint. However, the delay performance of the SPC scheme is worse than DOTS before 40 episodes, and the RPC scheme is always worse than the DOTS scheme. At the beginning of the learning process, the delay can be minimized, but the UAV energy capacity is exceeded. Due to the untuned weight <sup>δ</sup> at the beginning of the learning process, the goal of the policy is to minimize the cost. With the learning episode increasing, the policy of risk minimization can be found. Therefore, after 60 episodes, the delay-minimized policy is learned without exceeding the UAV energy capacity. Compared with the other two schemes, the proposed scheme has the lowest time-averaged task processing delay when the optimal policy has been learned.

![](images/8758d609b3711487b4eb51247838f29603ed9683575bd925d93d69a08a49d2b2.jpg)  
(a)

![](images/6bb5560489f6cf2ba589d7500df10315ff0f3d050737d0608da62d8724728858.jpg)  
(b)

Fig. 4. Convergence performance of the proposed deep RL-based DOTS scheme in one episode.  
![](images/aa07956e3e34dd8773cb7d28c846e1ddd0223d54af028ba4f0f8a9bf72f6790f.jpg)  
(a)

![](images/9ffe723b1cbd7267946c668a5fed67931189c654ee7fd813fd05652fdf57c703.jpg)  
(b)

Fig. 5. Convergence performance of the proposed deep RL-based DOTS scheme.  
![](images/d7f2661b38c65689ead23ab5f6496b1107bc361ef0b922c1ddf35c89f9d98e64.jpg)  
(a)  
Fig. 6. CDFs of delay and energy consumption.

![](images/08e7ea9c66c4cca9b29634b81c6fdfcc8e423595ebce9ebad012a9ec633dc7b5.jpg)  
(b)

Figure 8 shows the offloading proportion under different policies with $\varepsilon \ = \ 5 5 { \mathrm { J o u l e } } .$ . The action proportion of SPC and RPC schemes is similar, as both of them are based on probabilistic selection. However, RPC cannot guarantee the UAV energy capacity constraint. Although the SPC scheme can bound the energy consumption, SPC selects actions based on the historical experience, and thus it cannot learn to schedule proper number of tasks in different scenarios according to the future information. Particularly, the SPC scheme and the RPC scheme may offload the tasks at inappropriate states (e.g., low data rate), in which task offloading to other BSs or satellite should be suppressed and wait for more appropriate states (e.g., high data rate). Unlike the benchmark schemes, the proposed DOTS scheme can make the UAV offload a certain number of tasks to BSs when they are covered by BS, and offload to the satellite when it is out of the BS coverage. As offloading tasks to the satellite is an important complementary solution for offloading tasks to BSs, it effectively reduces the queuing delay when the UAV is out of the BS coverage. Therefore, the RL-based DOTS scheme can schedule the optimal number of tasks to BS or satellite according to the learned knowledge, such as the task arrival pattern.

![](images/4864dc75b000489d95a3ba9d6ff3cabc7c00a7c7310280f0da59dbebf7fc2d8d.jpg)  
(a)

Fig. 7. Performance of delay and energy consumption.  
![](images/9f9811672ea6d245713a7f9f7a7097bcda03704884b9fa278fcc6a901e90c927.jpg)  
Fig. 8. Offloading proportion under different policies for ε = 55 Joule.

## VII. CONCLUSION AND FUTURE WORK

In this article, we have proposed a novel IoT computing task scheduling scheme named DOTS in SAGIN, where a UAV is dispatched to collect tasks from IoT devices and then make online scheduling decisions to process the tasks. Considering the limited UAV energy capacity and the dynamics of task arrival, we have formulated the online scheduling problem as a CMDP. With the objective of minimizing the longterm average delay without violating the constraint, we have designed the deep risk-sensitive RL algorithm to make online task scheduling decisions. Extensive simulation results have demonstrated that the deep RL-based DOTS scheme can significantly reduce the delay of processing IoT computing tasks while satisfying the UAV energy capacity constraint. The proposed scheme can provide low-latency IoT services and extend the service lifespan for massive IoT devices with limited power supply. In the future work, we will investigate the task scheduling strategy based on the cooperation of multiple UAVs in SAGIN.

![](images/efa6700e0d9189e9fa4f95b39f87cbeaa864c3bc365024224dc5eb85e28e6187.jpg)  
(b)

## REFERENCES

[1] C. Zhou et al., “Delay-aware IoT task scheduling in space-air-ground integrated network,” in Proc. IEEE Globecom, Waikoloa, HI, USA, Dec. 2019, pp. 1–6.

[2] F. Wang, J. Xu, and S. Cui, “Optimal energy allocation and task offloading policy for wireless powered mobile edge computing systems,” IEEE Trans. Wireless Commun., vol. 19, no. 4, pp. 2443–2459, Apr. 2020.

[3] X. Shen et al., “AI-assisted network-slicing based next-generation wireless networks,” IEEE Open J. Veh. Technol., vol. 1, pp. 45–66, Jan. 2020.

[4] X. Wang, Y. Han, V. C. M. Leung, D. Niyato, X. Yan, and X. Chen, “Convergence of edge computing and deep learning: A comprehensive survey,” IEEE Commun. Surveys Tuts., vol. 22, no. 2, pp. 869–904, 2nd Quart., 2020.

[5] P. Yang, F. Lyu, W. Wu, N. Zhang, L. Yu, and X. Shen, “Edge coordinated query configuration for low-latency and accurate video analytics,” IEEE Trans. Ind. Informat., vol. 16, no. 7, pp. 4855–4864, Jul. 2020.

[6] Z. Zhou, Q. Wu, and X. Chen, “Online orchestration of cross-edge service function chaining for cost-efficient edge computing,” IEEE J. Sel. Areas Commun., vol. 37, no. 8, pp. 1866–1880, Aug. 2019.

[7] Z. Zhou, X. Chen, E. Li, L. Zeng, K. Luo, and J. Zhang, “Edge intelligence: Paving the last mile of artificial intelligence with edge computing,” Proc. IEEE, vol. 107, no. 8, pp. 1738–1762, Aug. 2019.

[8] X. Cheng et al., “Space/aerial-assisted computing offloading for IoT applications: A learning-based approach,” IEEE J. Sel. Areas Commun., vol. 37, no. 5, pp. 1117–1129, May 2019.

[9] Y. Huo, X. Fan, L. Ma, X. Cheng, Z. Tian, and D. Chen, “Secure communications in tiered 5G wireless networks with cooperative jamming,” IEEE Trans. Wireless Commun., vol. 18, no. 6, pp. 3265–3280, Jun. 2019.

[10] F. Lyu et al., “Characterizing urban vehicle-to-vehicle communications for reliable safety applications,” IEEE Trans. Intell. Transp. Syst., vol. 21, no. 6, pp. 2586–2602, Jun. 2020.

[11] E. Buchen, “Small satellite market observations,” in Proc. 29th Annu. AIAA/USU Conf. Samll Satell., Atlanta, GA, USA, 2015, pp. 1–5.

[12] Technical Specification Group Radio Access Network; Study on New Radio (NR) to Support Non-Terrestrial Networks (Release 15), document TR 38.811 V15.2.0, 3GPP, Oct. 2019.

[13] B. Di, L. Song, Y. Li, and H. V. Poor, “Ultra-dense LEO: Integration of satellite access networks into 5G and beyond,” IEEE Wireless Commun., vol. 26, no. 2, pp. 62–69, Apr. 2019.

[14] Q. Wu, Y. Zeng, and R. Zhang, “Joint trajectory and communication design for multi-UAV enabled wireless networks,” IEEE Trans. Wireless Commun., vol. 17, no. 3, pp. 2109–2121, Mar. 2018.

[15] S. Zhang, W. Quan, J. Li, W. Shi, P. Yang, and X. Shen, “Air-ground integrated vehicular network slicing with content pushing and caching,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 2114–2127, Sep. 2018.

[16] N. Abbas, Y. Zhang, A. Taherkordi, and T. Skeie, “Mobile edge computing: A survey,” IEEE Internet Things J., vol. 5, no. 1, pp. 450–465, Feb. 2018.

[17] D. Zeng, L. Gu, S. Guo, Z. Cheng, and S. Yu, “Joint optimization of task scheduling and image placement in fog computing supported software-defined embedded system,” IEEE Trans. Comput., vol. 65, no. 12, pp. 3702–3712, Dec. 2016.

[18] N. Kato et al., “Optimizing space-air-ground integrated networks by artificial intelligence,” IEEE Wireless Commun., vol. 26, no. 4, pp. 140–147, Aug. 2019.

[19] M. Li, Y. Hong, C. Zeng, Y. Song, and X. Zhang, “Investigation on the UAV-to-satellite optical communication systems,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 2128–2138, Sep. 2018.

[20] Z. Zhou, J. Feng, C. Zhang, Z. Chang, Y. Zhang, and K. M. S. Huq, “SAGECELL: Software-defined space-air-ground integrated moving cells,” IEEE Commun. Mag., vol. 56, no. 8, pp. 92–99, Aug. 2018.

[21] A. Varasteh et al., “Mobility-aware joint service placement and routing in space-air-ground integrated networks,” in Proc. IEEE ICC, Shanghai, China, May 2019, pp. 1–7.

[22] N. Zhang, S. Zhang, P. Yang, O. Alhussein, W. Zhuang, and X. Shen, “Software defined Space-Air-Ground integrated vehicular networks: Challenges and solutions,” IEEE Commun. Mag., vol. 55, no. 7, pp. 101–109, Jul. 2017.

[23] N. Cheng et al., “Air-ground integrated mobile edge networks: Architecture, challenges, and opportunities,” IEEE Commun. Mag., vol. 56, no. 8, pp. 26–32, Aug. 2018.

[24] Z. Kuang, L. Li, J. Gao, L. Zhao, and A. Liu, “Partial offloading scheduling and power allocation for mobile edge computing systems,” IEEE Internet Things J., vol. 6, no. 4, pp. 6774–6785, Aug. 2019.

[25] X. Chen, L. Jiao, W. Li, and X. Fu, “Efficient multi-user computation offloading for mobile-edge cloud computing,” IEEE/ACM Trans. Netw., vol. 24, no. 5, pp. 2795–2808, Oct. 2016.

[26] X. Lyu et al., “Optimal schedule of mobile edge computing for Internet of Things using partial information,” IEEE J. Sel. Areas Commun., vol. 35, no. 11, pp. 2606–2615, Nov. 2017.

[27] Y. Sun, S. Zhou, and J. Xu, “EMM: Energy-aware mobility management for mobile edge computing in ultra dense networks,” IEEE J. Sel. Areas Commun., vol. 35, no. 11, pp. 2637–2646, Nov. 2017.

[28] F. Cheng et al., “UAV trajectory optimization for data offloading at the edge of multiple cells,” IEEE Trans. Veh. Technol., vol. 67, no. 7, pp. 6732–6736, Jul. 2018.

[29] Y. Zeng and R. Zhang, “Energy-efficient UAV communication with trajectory optimization,” IEEE Trans. Wireless Commun., vol. 16, no. 6, pp. 3747–3760, Jun. 2017.

[30] J. L. Hennessy and D. A. Patterson, Computer Architecture: A Quantitative Approach. Amsterdam, The Netherlands: Elsevier, 2011.

[31] Z. Wang, L. Duan, and R. Zhang, “Adaptive deployment for UAV-aided communication networks,” IEEE Trans. Wireless Commun., vol. 18, no. 9, pp. 4531–4543, Sep. 2019.

[32] N. Zhang, H. Liang, N. Cheng, Y. Tang, J. W. Mark, and X. S. Shen, “Dynamic spectrum access in multi-channel cognitive radio networks,” IEEE J. Sel. Areas Commun., vol. 32, no. 11, pp. 2053–2064, Nov. 2014.

[33] F. Vatalaro, G. E. Corazza, C. Caini, and C. Ferrarelli, “Analysis of LEO, MEO, and GEO global mobile satellite systems in the presence of interference and fading,” IEEE J. Sel. Areas Commun., vol. 13, no. 2, pp. 291–300, Feb. 1995.

[34] N. Hosseini, H. Jamal, J. Haque, T. Magesacher, and D. W. Matolak, “UAV command and control, navigation and surveillance: A review of potential 5G and satellite systems,” in Proc. IEEE Aerosp. Conf., Big Sky, MT, USA, Mar. 2019, pp. 1–10.

[35] M. L. Puterman, Markov Decision Processes: Discrete Stochastic Dynamic Programming. Hoboken, NJ, USA: Wiley, 2014.

[36] H. He, H. Shan, A. Huang, Q. Ye, and W. Zhuang, “Edgeaided computing and transmission scheduling for LTE-U-enabled IoT,” IEEE Trans. Wireless Commun., early access, Aug. 25, 2020, doi: 10.1109/TWC.2020.3017207.

[37] V. Mnih et al., “Human-level control through deep reinforcement learning,” Nature, vol. 518, no. 7540, p. 529, Feb. 2015.

[38] D. F. Specht, “A general regression neural network,” IEEE Trans. Neural Netw., vol. 2, no. 6, pp. 568–576, Nov. 1991.

[39] P. Geibel and F. Wysotzki, “Risk-sensitive reinforcement learning applied to control under constraints,” J. Artif. Intell. Res., vol. 24, pp. 81–108, Jul. 2005.

[40] L. Xiao et al., “Reinforcement learning based downlink interference control for ultra-dense small cells,” IEEE Trans. Wireless Commun., vol. 19, no. 1, pp. 423–434, Jan. 2020.

[41] S. A. Kanellopoulos, C. I. Kourogiorgas, A. D. Panagopoulos, S. N. Livieratos, and G. E. Chatzarakis, “Channel model for satellite communication links above 10GHz based on Weibull distribution,” IEEE Commun. Lett., vol. 18, no. 4, pp. 568–571, Apr. 2014.

[42] M. Abadi et al., “Tensorflow: A system for large-scale machine learning,” in Proc. OSDI, Savannah, GA, USA, Nov. 2016, pp. 265–283.

![](images/b661f8dbcf423079c4a95b8ae1586a79c1b6d556a5a2597b001ca7010b923c88.jpg)  
Conghao Zhou (Graduate Student Member, IEEE) received the B.S. degree from Northeastern University, Shenyang, China, in 2017, and the M.S. degree from the University of Illinois at Chicago, Chicago, IL, USA, in 2018. He is currently pursuing the Ph.D. degree with the Department of Electrical and Computer Engineering, University of Waterloo, Waterloo, ON, Canada. His research interests include space-air-ground integration networks and machine learning in wireless networks.

![](images/bce6b85a861c9f923d8282df78fb01c6ae6ea035b56bd4259f17332d767c0215.jpg)

Wen Wu (Member, IEEE) received the B.E. degree in information engineering from the South China University of Technology, Guangzhou, China, and the M.E. degree in electrical engineering from the University of Science and Technology of China, Hefei, China, in 2012 and 2015, respectively, and the Ph.D. degree in electrical and computer engineering from the University of Waterloo, Waterloo, ON, Canada, in 2019. Since 2019, he has been a Post-Doctoral Fellow with the Department of Electrical and Computer Engineering, University of Waterloo.

His research interests include millimeter-wave networks and AI-empowered wireless networks.

![](images/51c92d41359125ca117d3f6eff13ac7eb38eaaa8939d6e5b5f6c6ef111c08a7e.jpg)

Hongli He (Member, IEEE) received the B.Sc. and Ph.D. degrees in information and communication engineering from Zhejiang University, Hangzhou, China, in 2014 and 2020, respectively. He is currently working as a Senior Engineer with the Huawei Technologies Company Ltd. His research interests include vehicular ad-hoc networks, cellular networks over unlicensed spectrum, edge computing, and deep reinforcement learning in wireless communications.

![](images/8b219b65be4f2fc315b40d32a1af8f82e87634f3483a7f27c55dd58373a36075.jpg)

Peng Yang (Member, IEEE) received the B.E. degree in communication engineering and the Ph.D. degree in information and communication engineering from the Huazhong University of Science and Technology (HUST), Wuhan, China, in 2013 and 2018, respectively. He was with the Department of Electrical and Computer Engineering, University of Waterloo, Canada, as a Visiting Ph.D. Student from September 2015 to September 2017, and a Post-Doctoral Fellow from September 2018 to December 2019. Since January 2020, he has been a Faculty

Member with the School of Electronic Information and Communications, HUST. His current research interests include mobile edge computing, video streaming, and analytics.

![](images/aa015c1f244a6b60f96f87bd093b7a47dd19e5765b7d4cc4972dd61b41342e0f.jpg)

Feng Lyu (Member, IEEE) received the B.S. degree in software engineering from Central South University, Changsha, China, in 2013, and the Ph.D. degree from the Department of Computer Science and Engineering, Shanghai Jiao Tong University, Shanghai, China, in 2018. From September 2018 to December 2019 and October 2016 to October 2017, he worked as a Post-Doctoral Fellow and a visiting Ph.D. student with the BBCR Group, Department of Electrical and Computer Engineering, University of Waterloo, Canada. He is currently a Professor with

the School of Computer Science and Engineering, Central South University, Changsha, China. His research interests include vehicular networks, beyond 5G networks, big data measurement and application design, and could/edge computing. He was a recipient of the Best Paper Award of the IEEE ICC 2019. He currently serves as an Associate Editor for the IEEE SYSTEMS JOURNAL and a leading Guest Editor for Peer-to-Peer Networking and Applications and served as a TPC member for many international conferences. He is a member of the IEEE Computer Society, the Communication Society, and the Vehicular Technology Society.

![](images/26ddd697694e637a8f94e33559be9e2696b567dad9aa85e7331d65aadedc3a2c.jpg)

Nan Cheng (Member, IEEE) received the B.E. and M.S. degrees from the Department of Electronics and Information Engineering, Tongji University, Shanghai, China, in 2009 and 2012, respectively, and the Ph.D. degree from the Department of Electrical and Computer Engineering, University of Waterloo, in 2016. He worked as a Post-Doctoral Fellow with the Department of Electrical and Computer Engineering, University of Toronto, from 2017 to 2019. He is currently a Professor with the State Key Laboratory of ISN and the School of Telecommuni-

cation Engineering, Xidian University, Shaanxi, China. His current research interests include B5G/6G, space-air-ground integrated networks, big data in vehicular networks, and self-driving systems. His research interests include performance analysis, MAC, opportunistic communications, and application of AI for vehicular networks.

![](images/1cd9af4af8dd219e09e51f7bf23f047e1d58f541625b9629cff13853683fd5cf.jpg)

Xuemin (Sherman) Shen (Fellow, IEEE) received the Ph.D. degree in electrical engineering from Rutgers University, New Brunswick, NJ, USA, in 1990.

He is currently a University Professor with the Department of Electrical and Computer Engineering, University of Waterloo, Canada. His research interests include network resource management, wireless network security, the Internet of Things, 5G and beyond, and vehicular ad-hoc and sensor networks. He is a registered Professional Engineer of Ontario, Canada, an Engineering Institute of Canada Fellow, a Canadian Academy of Engineering Fellow, a Royal Society of Canada Fellow, a Chinese Academy of Engineering Foreign Member, and a Distinguished Lecturer of the IEEE Vehicular Technology Society and Communications Society. He received the R.A. Fessenden Award in 2019 from the IEEE, Canada, the Award of Merit from the Federation of Chinese Canadian Professionals (Ontario) in 2019, the James Evans Avant Garde Award in 2018 from the IEEE Vehicular Technology Society, the Joseph LoCicero Award in 2015 and Education Award in 2017 from the IEEE Communications Society, and Technical Recognition Award from Wireless Communications Technical Committee in 2019, and the AHSN Technical Committee in 2013. He has also received the Excellent Graduate Supervision Award in 2006 from the University of Waterloo and the Premier’s Research Excellence Award (PREA) in 2003 from the Province of Ontario, Canada. He served as the Technical Program Committee Chair/Co-Chair for the IEEE Globecom’16, the IEEE Infocom’14, the IEEE VTC’10 Fall, the IEEE Globecom’07, and the Chair for the IEEE Communications Society Technical Committee on Wireless Communications. He was the elected IEEE Communications Society Vice President for Technical and Educational Activities, the Vice President for Publications, a Member-at-Large on the Board of Governors, a Chair of the Distinguished Lecturer Selection Committee, and a Member of the IEEE ComSoc Fellow Selection Committee. He was the Editor-in-Chief of the IEEE IOT JOURNAL, the IEEE NETWORK, and IET Communications.