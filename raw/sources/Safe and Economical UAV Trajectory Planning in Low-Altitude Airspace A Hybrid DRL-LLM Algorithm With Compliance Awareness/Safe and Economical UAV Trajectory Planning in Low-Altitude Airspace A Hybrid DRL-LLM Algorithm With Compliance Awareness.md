# Safe and Economical UAV Trajectory Planning in Low-Altitude Airspace: A Hybrid DRL-LLM Algorithm with Compliance Awareness

Yanwei Gong, Junchao Fan, Ruichen Zhang, Dusit Niyato, Fellow, IEEE, Yingying Yao, and Xiaolin Chang

Abstract—The rapid growth of the low-altitude economy has driven the widespread adoption of unmanned aerial vehicles (UAVs). This growing deployment presents new challenges for UAV trajectory planning in complex urban environments. However, existing studies often overlook key factors, such as urban airspace constraints and economic efficiency, which are essential in low-altitude economy contexts. Deep reinforcement learning (DRL) is regarded as a promising solution to these issues, while its practical adoption remains limited by low learning efficiency. To overcome this limitation, we propose a novel UAV trajectory planning algorithm that integrates DRL with the large language model (LLM) reasoning to enable safe, compliant, and economically viable trajectory planning. Specifically, we model the trajectory planning task as a partially observable Markov decision process, explicitly incorporating obstacle avoidance, regulation awareness, and energy constraints. We design a hybrid optimization algorithm based on the soft actor-critic algorithm and LLM reasoning to enable adaptive decision-making in uncertain and dynamic environments. Experimental results demonstrate that our algorithm achieves the best overall performance, with the highest data collection rate (99.50%), almost zero collision avoidance rate and regulation violation rate, a successful landing rate of nearly 100%, and the lowest energy consumption rate (76.95%). These results validate the effectiveness of our algorithm in addressing UAV trajectory planning key challenges under constraints of the low-altitude economy networking

Index Terms—Data Collection, Large Language Model, Low-Altitude Economy, Reinforcement Learning, Trajectory Planning

## 1 INTRODUCTION

With the rapid advancement of the low-altitude economy, low-altitude airspace has emerged as a critical strategic resource to drive urban intelligence, industrial upgrading, and digital economic transformation [1], [2]. This evolving domain integrates diverse sectors such as general aviation and urban air mobility, wherein unmanned aerial vehicles (UAVs) play an increasingly vital role in applications including logistics, agricultural monitoring, infrastructure inspection, and environmental protection [3]. However, the high-density and regulation-intensive nature of low-altitude airspace also poses unique challenges for intelligent trajectory planning and safe autonomous operation.

In this context, UAV-based data acquisition represents a fundamental technology enabling high-precision, multimodal environmental sensing [4]. The UAV data acquisition process typically involves task assignment, flight trajectory planning, sensor data collection, and data transmission and processing. Effective trajectory planning is crucial to maximize area coverage and data quality, thereby supporting downstream applications with accurate and timely information [5]. It also serves as a key enabler for intelligent and autonomous decision-making in dense and dynamic airspaces.

Despite its potential, trajectory planning for UAV data acquisition in low-altitude airspace faces the following important challenges:

Challenge 1: Robust Obstacle Avoidance in Urban Airspaces. Due to the existence of airspace reuse in the low-altitude economy [35], operating in low-altitude urban environments exposes the data collection UAVs (DCU) not only to static obstacles (e.g., buildings) but also to dynamic obstacles (e.g., other UAVs). These obstacles are often partially observable and highly uncertain. Moreover, the DCU must also avoid restricted no-fly zones (NFZs) over sensitive areas. Ensuring robust obstacle avoidance under such conditions remains a core challenge. Traditional optimization methods typically lack the adaptability to handle such stochastic environments, and standard deep reinforcement learning (DRL) struggles to accumulate sufficient successful trajectories, leading to low learning efficiency [6].

Challenge 2: Intelligent Planning for the Economy with Compliance. In the low-altitude economy, the DCU must not only maximize data acquisition but also minimize energy consumption to ensure cost-effectiveness. Moreover, the DCU must adhere to evolving, location-specific regulations where the DCU is to reduce speed to minimize noise [7]. These decisions introduce additional requirements on mission efficiency and regulatory compliance. Traditional methods struggle with multi-objective adaptation under uncertainty, while conventional DRL approaches often fail to incorporate the domain knowledge needed to make economically viable decisions.

Challenge 3: Real-Time Decision-Making Under Uncertainty. Trajectory planning in real-world scenarios requires real-time decision making across multiple dimensions under dynamic and uncertain conditions, including obstacle avoidance, route selection, and data collection. Traditional optimization methods are often computationally intensive and lack responsiveness, whereas standard DRL policies may require extensive exploration due to task complexity.

Most existing methods address only isolated objectives or assume simplified environments, which prevents them from achieving a unified balance among safety, compliance, and economy. To address these limitations, this paper proposes a novel hybrid DRL and large language model (LLM) algorithm for safe and economical DCU trajectory planning in low-altitude airspace with compliance-awareness. The motivation is that, while the LLM offers strong reasoning abilities and can infer safe actions based on highlevel semantic input, it lacks the ability to learn optimal control policies through interaction with dynamic environments [33]. Conversely, DRL excels at learning adaptive control policies via trial and error, but struggles to incorporate abstract constraints such as regulatory rules [34]. Therefore, we introduce an LLM to enhance the DCU’s decision-making capability in complex, uncertain scenarios where rule compliance, contextual awareness, and obstacle interpretation are critical. The main contributions of this paper are summarized as follows:

• Unified modeling of low-altitude UAV trajectory planning. We formulate the DCU trajectory planning task for low-altitude data acquisition as a partially observable Markov decision process (POMDP), which jointly captures constraints including both static and dynamic obstacle avoidance mentioned in Challenge 1, regulation awareness, and energy efficiency mentioned in Challenge 2, under partial observability.

• A hybrid SAC and LLM-based trajectory planning algorithm. We develop a novel optimization algorithm that combines the soft actor-critic (SAC) algorithm with an LLM. By combining the adaptive decision-making capabilities of SAC with the contextual reasoning strength of the LLM, the proposed algorithm enables the DCU to perform trajectory planning in real time, with robust obstacle avoidance, regulatory compliance, and economical data collection in uncertainty, thus addressing Challenge 3.

• Comprehensive experimental validation and performance improvement. Extensive experiments verify that the proposed algorithm consistently outperforms stateof-the-art baselines across all key metrics. Compared with the best-performing baseline, our method improves the data collection rate by 2.9%, reduces the collision rate and regulation violation rate to nearly 0%, achieves a 100% successful landing rate, and lowers the energy consumption rate by 1.9%. These results confirm the algorithm’s effectiveness in addressing the Challenges 1-3.

The remainder of this paper is organized as follows. Section 2 reviews the related work. Section 3 describes the overall system architecture, while Section 4 presents the formal problem definition. Section 5 introduces the POMDPbased modeling approach and elaborates on the proposed algorithm. Section 6 reports the experimental results and performance evaluations. Finally, Section 7 concludes the paper and outlines future research directions.

## 2 RELATED WORK

In this section, we review existing UAV trajectory planning methods from three perspectives, including traditional optimization algorithms, DRL-based approaches, and LLMenhanced methods. Table 1 summarizes representative studies and their characteristics.

## 2.1 UAV Trajectory Planning with Traditional Algorithms

Early studies mainly adopted optimization-based algorithms to jointly optimize UAV trajectory, communication, and energy efficiency. Qin et al. [8] used Dinkelbach’s method and block coordinate descent (BCD) for joint trajectory and resource optimization in reconfigurable intelligent surface-assisted UAV mobile edge computing (MEC) systems. Pan et al. [9] combined an improved nondominated sorting genetic algorithm II (NSGA-II) with a customized particle swarm optimization (PSO) variant for multi-objective power and trajectory planning. Pervez et al. [10] formulated a multi-UAV MEC optimization using game theory and successive convex approximation (SCA). Zhang et al. [11] applied differential evolution to balance UAV deployment and flight planning for Internet of Things (IoT) data collection. Heo et al. [12] incorporated NFZ constraints using quadratic transform and SCA. Other works [13]–[15] explored swarm intelligence and distributed optimization for beamforming and energy efficiency.

Traditional optimization algorithms are effective in structured or static environments but lack adaptability to dynamic and uncertain low-altitude airspace conditions, and they cannot efficiently handle the stochastic nature of real-world obstacle distributions (Challenge 1).

## 2.2 UAV Trajectory Planning with DRL

To improve adaptability, many studies employed DRL for UAV trajectory control and resource management. Silvirianti et al. [16] proposed a layerwise quantum DRL method for joint trajectory and power optimization. Chen et al. [17] applied DRL to solve a multi-stage mixed-integer problem for UAV-assisted MEC. Ning et al. [18] introduced distributed DRL with game theory for collaborative control. Song et al. [19] formulated a multi-objective Markov decision process (MDP) with a trace-based experience replay mechanism. Ding et al. [20] developed a multi-agent advantage actor-critic (A2C)–deep deterministic policy gradient (DDPG) scheme with attention-based inference. Wang et al. [21] incorporated safety constraints into DRL under a constrained MDP framework. He et al. [22] and Liu et al. [23] extended multi-agent DRL to cooperative trajectory planning. Ning et al. [24] adopted constrained DRL for UAV mobility and connection optimization in IoT networks. Zhu et al. [25] applied an exploration-enhanced DRL framework to joint trajectory and resource optimization in UAV-enabled MEC systems.

DRL-based methods can adapt to partially observable and dynamic environments, but they often require extensive exploration to incorporate domain-specific rules such as regulatory or economic constraints (Challenge 2 and Challenge 3).

## 2.3 UAV Trajectory Planning with LLM

Recent research has introduced LLMs to enhance UAV autonomy by integrating reasoning and natural language understanding. Zhong et al. [26] combined lightweight object detection with an LLM for vision-based UAV planning in dynamic scenes. Phadke et al. [27] explored LLM-driven UAV control via natural language interfaces for improved mission coordination and safety. Xiao et al. [28] proposed a foundation model-guided trajectory framework integrating LLMs and vision-language models (VLMs) for semantic reasoning and perception. Samma et al. [29] utilized an LLM-based vision system to plan UAV trajectories in GPSdenied indoor environments. Cai et al. [30] designed an LLM–model predictive control (MPC) hybrid landing system for enhanced safety in unstructured scenarios. Li et al. [31] proposed an LLM-enabled multi-objective evolutionary algorithm for UAV-based integrated sensing and communications. Emami et al. [32] introduced an LLMenabled in-context learning framework for data collection scheduling in UAV-assisted sensor networks.

LLM-enhanced approaches offer semantic reasoning and interpretability but face challenges in real-time decisionmaking for UAVs, including excessive resource consumption and limited real-time performance.

## 2.4 Discussion

Existing UAV trajectory planning methods contribute valuable insights but exhibit limitations when applied to lowaltitude data collection missions. Traditional algorithms [8]- [15] cannot adapt to dynamic and uncertain obstacle patterns in real urban airspaces. DRL-based methods [16]- [25] improve adaptability but overlook regulatory compliance and economic trade-offs. LLM-based frameworks [26]- [32] offer strong reasoning but lack real-time adaptability. Consequently, none of these approaches can simultaneously ensure robust obstacle avoidance, compliance with evolving regulations, and energy-efficient trajectory design in lowaltitude environments. To overcome these issues, this paper proposes a hybrid DRL–LLM algorithm that integrates adaptive control and semantic reasoning to achieve safe, compliant, and economical UAV trajectory planning.

## 3 SYSTEM DESCRIPTION

In this section, we provide a comprehensive description of the system, including the system model and the associated models for UAV mobility, data transmission, and energy consumption. The system model defines the main entities involved. The models for mobility, data transmission, and energy consumption characterize the UAV’s movement, communication behavior, and energy usage, respectively, in a manner consistent with real-world operations. This modeling approach enhances the credibility of experimental results presented in Section 6. The notation used throughout the remainder of the paper is summarized in Table 2.

![](images/49196ab5095545a7d5dc0504f91ff9f0a5e37501097e895ffad23897b1c36285.jpg)  
Fig. 1: System model of low-altitude UAV trajectory planning. The DCU collects data from GE while avoiding static obstacles (BZs, NFZs, RZs) and dynamic obstacles (OUs) under energy and compliance constraints.

## 3.1 System Model

The system model is shown in Fig. 1. The DCU collects data in the area <sup>A</sup>. The length, width, and height of <sup>A</sup> are X, Y , and Z, respectively. The system entities include the data collection UAV (DCU), other UAVs (OUs), and ground equipment (GE), which are detailed as follows.

DCU. The DCU is responsible for the data collection in the low-altitude economy and flies at a fixed altitude H. It takes off from <sup>TA</sup>, then conducts data collection in $\mathbb { A } ,$ and eventually reaches <sup>LA</sup>. When conducting data collection, the DCU is not allowed to fly into NFZs. Furthermore, when the DCU flies into residential zones (RZs), to ensure noise control, its flight speed must be less than v [26]. The DCU must also ensure that it does not collide with building zones (BZs) and OUs in the low-altitude economic networking. Therefore, we assume that the DCU is equipped with a sensing device with a perception radius of P R. Through this device, the DCU can detect the positions and flight directions of OUs and thereby adjust its flight trajectory to avoid collisions.

OUs. Considering the existence of airspace reuse in the low-altitude economy [35], there will also be OUs performing other tasks in the system. These UAVs may appear on the flight trajectories where the DCU collects data. To avoid collisions, the algorithm proposed in this paper considers this issue when optimizing the DCU’s flight trajectory.

GE. GE refers to devices that generate data in the lowaltitude economy, such as intelligent traffic devices, power infrastructure equipment, and environmental monitoring devices [36]. These data are collected regularly by the DCU. $N _ { \mathrm { G E } }$ GEs are placed independently and uniformly at random over <sup>A</sup>, while maintaining appropriate clearance from obstacle boundaries and zones (NFZ/BZ/RZ). Such random deployment is widely adopted in UAV-enabled data collection trajectory planning scenarios, as it captures diverse and unpredictable real-world layouts without imposing artificial structural patterns.

TABLE 1: Comparison of Related Works on UAV Trajectory Planning
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=3>Ref.</td><td rowspan=1 colspan=1>Main Method / Algorithm</td><td rowspan=1 colspan=1>Obstacle Avoidance</td><td rowspan=1 colspan=1>Compliance</td></tr><tr><td rowspan=8 colspan=1>Tradinal</td><td rowspan=1 colspan=2>Qin et al. 2023 [8]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Dinkelbach&#x27;s method, BCD</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>x</td></tr><tr><td rowspan=1 colspan=2>Pan et al. 2024 [9]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>NSGA-II, PSO variant</td><td rowspan=1 colspan=1>Static only</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Pervez et al. 2024 [</td><td rowspan=1 colspan=1>10]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Game theory, SCA</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Zhang et al. 2024</td><td rowspan=1 colspan=1>[11]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Evolutionary algorithm</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Heo et al. 2024 [</td><td rowspan=1 colspan=1>12]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Quadratic transform, SCA</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Li et al. 2024 [</td><td rowspan=1 colspan=1>13]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Swarm intelligence-based algorithm</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Fu et al. 2025 [</td><td rowspan=1 colspan=1>14]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Distributed approximate Newton, BCD</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Wang et al. 2025 [</td><td rowspan=1 colspan=1>15]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Ant colony optimization</td><td rowspan=1 colspan=1>Static only</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=10 colspan=1>DRL</td><td rowspan=1 colspan=1>Silvirianti et al. 2024 [</td><td rowspan=1 colspan=1>16]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Layerwise quantum-DRL</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>x</td></tr><tr><td rowspan=1 colspan=1>Chen et al. 2024</td><td rowspan=1 colspan=1>[17]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DRL</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Ning et al. 2024</td><td rowspan=1 colspan=1>[18]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DRL, game theory</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>x</td></tr><tr><td rowspan=1 colspan=1>Song et al. 2024 [</td><td rowspan=1 colspan=1>19]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Multi-objective RL</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Ding et al. 2024 [</td><td rowspan=1 colspan=1>20]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DDPG, DAI</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Wang et al. 2024</td><td rowspan=1 colspan=1>[21]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Safe DRL</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>x</td></tr><tr><td rowspan=1 colspan=1>He et al. 2024</td><td rowspan=1 colspan=1>[22]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>DRL</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Liu et al. 2025</td><td rowspan=1 colspan=1>[23]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Multi-agent RL, SCA</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Ning et al. 2025</td><td rowspan=1 colspan=1>[24]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Constrained DRL</td><td rowspan=1 colspan=1> $\overline { { S \mathrm { t a t i c ~ o n l y } } }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Zhu et al. 2025 [</td><td rowspan=1 colspan=1>25]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Exploration-enhanced DRL</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=7 colspan=1>MTM</td><td rowspan=1 colspan=1>Zhong et al. 2024 [2</td><td rowspan=1 colspan=1>6]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Apply LLM directly</td><td rowspan=1 colspan=1> $\overline { { \mathrm { D y n a m i c ~ o n l y } } }$ </td><td rowspan=1 colspan=1>x</td></tr><tr><td rowspan=1 colspan=1>Phadke et al. 2024[</td><td rowspan=1 colspan=1>27</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Apply LLM directly</td><td rowspan=1 colspan=1> $\mathbf { \dot { S } t a t i c \ o n l y }$ </td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Xiao et al. 2025</td><td rowspan=1 colspan=1>[28]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>LLM, VLM</td><td rowspan=1 colspan=1>Static only</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Samma et al. 2025</td><td rowspan=1 colspan=1>[29]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Fine-tuned LLM</td><td rowspan=1 colspan=1>Both dynamic and static</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Cai et al. 2025 [</td><td rowspan=1 colspan=1>30]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>LLM, MPC</td><td rowspan=1 colspan=1>Both dynamic and static</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Li et al. 2025 [</td><td rowspan=1 colspan=1>31]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Apply LLM directly</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>Emami et al. 2025 [3</td><td rowspan=1 colspan=1>2]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>Apply LLM directly</td><td rowspan=1 colspan=1> $\overline { x }$ </td><td rowspan=1 colspan=1>X</td></tr></table>

Note: <sup>✗</sup> indicates not considered.

## 3.2 Models Related to UAV

This section presents models about how UAV moves, transmits data, and consumes energy in our system.

## 3.2.1 Mobility Model

The movement model is used to describe how the position of the DCU changes. The high velocity and dynamic topology of UAVs can lead to Doppler frequency shift (DFS) and fast-fading effects, which significantly degrade communication quality during data collection [40]. To mitigate these effects and maintain stable links with mobile devices, DCU adopts a hover-and-fly strategy [41]. In this scheme, the DCU first travels within the designated area <sup>A</sup> to locate an optimal communication position and then hovers at that point to collect data. This hovering mechanism effectively stabilizes the communication channel by reducing DFSinduced distortion and intercarrier interference.

To model this process in a tractable manner, the entire trajectory planning period is divided into equal time slots of length $\Delta t ,$ where $\bar { t } \in [ 0 , T ]$ denotes the slot index and $T$ is the total number of time slots determined by mission duration. Each time slot is equally divided into a flight phase and a data collection phase. During the flight phase, the DCU moves within <sup>A</sup> to search for a better position, and during the data collection phase, it hovers to communicate with mobile devices. In practice, there may be cases where no devices are within the sensing range during data collection, causing idle waiting and unnecessary energy consumption.

To minimize this energy waste and maintain modeling simplicity, the duration of both phases is set to 1 s, yielding a total slot length of $\Delta t \ = \ \bar { 2 } \ \mathbf { s } .$ . This fine-grained time division allows the DCU to frequently adjust its position while ensuring stable communication in each slot. The DCU is equipped with a single antenna and moves within the area <sup>A</sup>. The DCU flies at a fixed altitude H with a maximum speed $v _ { \mathrm { m a x } }$ and can communicate with at most one device per slot.

Given the DCU’s position $L _ { \mathrm { D C U } , t } = ( x _ { \mathrm { D C U } , t } , y _ { \mathrm { D C U } , t } , H$ and the velocity v<sub>DCU</sub> $( t ) = ( v _ { x } ( t ) , v _ { y } ( t ) , 0 )$ at the beginning of time slot $t ,$ the DCU’s position at time $t + 1$ is as follows:

$$
\begin{array} { r l } & { L _ { \mathrm { D C U } , t + 1 } = } \\ & { ( x _ { \mathrm { D C U } , t } + v _ { x } ( t ) t _ { \mathrm { f l y } } , \ y _ { \mathrm { D C U } , t } + v _ { y } ( t ) t _ { \mathrm { f l y } } , \ H ) , } \end{array}\tag{1}
$$

where $t _ { \mathrm { f l y } } = \Delta t / 2$ is the length of the flight phase. Given the maximum flight speed of the DCU, the distance between $L _ { \mathrm { D C U } , t + 1 }$ and $L _ { \mathrm { D C U } , t }$ should satisfy the following constraint:

$$
\begin{array} { r } { \| L _ { \mathrm { D C U } , t + 1 } - L _ { \mathrm { D C U } , t } \| \leq v _ { \operatorname* { m a x } } t _ { \mathrm { f l y } } . } \end{array}\tag{2}
$$

If the DCU flies into $\mathbb { R } _ { \mathrm { R Z } } ,$ the distance between L<sub>DCU,t+1</sub> and $\boldsymbol { L } _ { \mathrm { D C U } , t }$ should satisfy the following constraint:

$$
\begin{array} { r } { \| L _ { \mathrm { D C U } , t + 1 } - L _ { \mathrm { D C U } , t } \| \le v _ { \mathrm { l i m i t } } t _ { \mathrm { f l y } } , } \end{array}\tag{3}
$$

where $v _ { \mathrm { l i m i t } }$ is the speed limit in $\mathbb { R } _ { \mathrm { R Z } }$ for the DCU.

The OUs follow the same mobility model as the DCU described in Eq. (1). However, unlike the DCU, whose trajectory is optimized by the proposed algorithm, the trajectories of all OUs are randomly generated prior to simulation. Each OU’s velocity v<sub>OU</sub>(t) is sampled from a uniform distribution within $[ 0 , { v _ { \mathrm { m a x } } } ] ,$ , and its movement direction is randomly initialized and updated according to the same motion equations as the DCU. During trajectory generation, each OU’s path is constrained to ensure that it does not intersect with any BZs or NFZs, thereby maintaining physically valid and collision-free motion throughout the environment. This stochastic trajectory generation emulates the unpredictable movement of other UAVs or aerial entities in low-altitude airspace, introducing dynamic uncertainty for the DCU’s

TABLE 2: Notations and Descriptions
<table><tr><td>Notation</td><td>Description</td></tr><tr><td> $\overline { { \mathbb { A } = ( X , Y , Z ) } }$ </td><td>Area where the DCU conducts data collection, with length X, width  $Y ,$ </td></tr><tr><td> $B _ { \mathrm { G E } _ { i } } ( t )$ </td><td>and height Z Effective rate between the DCU and GEi in the time slot t</td></tr><tr><td> $d _ { t , \mathrm { X X } }$ </td><td>Distance between the DCU and XX at the beginning of time slot t  $( \mathsf { X X } = \mathbb { A } ,$ </td></tr><tr><td> $d _ { \mathrm { m i n , X X } }$ </td><td>LA, OU, BZ, or NFZ) Minimum distance between the DCU and  $\mathsf { X } \mathsf { X } \left( \mathsf { X } \mathsf { X } = \mathbb { A } , \mathrm { O U } , \mathrm { B Z } , \right.$  or NFZ)</td></tr><tr><td> $d _ { \mathrm { s a f e , X X } }$ </td><td>Safe distance between the DCU and XX (XX = A, OU, BZ, or NFZ)</td></tr><tr><td> $D V _ { G E _ { i } , t }$ </td><td>Data volume of the i-th GE at the beginning of time slot t</td></tr><tr><td> $E ( t )$ </td><td>Remaining energy at the beginning of time slot t</td></tr><tr><td> $E _ { \mathrm { l i m i t } }$ </td><td>Maximum energy that the DCU can</td></tr><tr><td> $E _ { \mathrm { t o t a l } }$ </td><td>consume Total energy the DCU has</td></tr><tr><td> $e ( t )$ </td><td>Energy consumed in the time slot t of the DCU</td></tr><tr><td> $e _ { \mathrm { f l y } } ( t )$ </td><td>Flight energy consumption in the time slot t of the DCU</td></tr><tr><td> $e _ { \mathrm { h o v e r } } ( t )$ </td><td>Hover energy consumption in the time slot t of the DCU</td></tr><tr><td> $\operatorname { \mathrm { E L } } _ { H } = ( x _ { \mathrm { E L } } , y _ { \mathrm { E L } } , z _ { \mathrm { E L } } )$ </td><td>Ending location of the DCU</td></tr><tr><td> $\mathbb { L } \mathbb { A } = ( p _ { \mathbb { L } \mathbb { A } } , l _ { \mathbb { L } \mathbb { A } } , w _ { \mathbb { L } \mathbb { A } } )$ </td><td>Fixed flight altitude of the DCU and OUs</td></tr><tr><td> $L _ { \mathrm { G E } _ { i } } = ( x _ { \mathrm { G E } _ { i } } , y _ { \mathrm { G E } _ { i } } , 0 )$ </td><td>Landing area location of the DCU Location of the i-th GE</td></tr><tr><td>Lxx,t 二</td><td>Location of XX at the beginning of</td></tr><tr><td> $( x _ { \mathrm { X X , } t } , y _ { \mathrm { X X , } t } , z _ { \mathrm { X X , } t } )$   $N _ { X X }$ </td><td>time slot t (XX = DCU or OU)</td></tr><tr><td></td><td>Number of XX (XX = GE, OU, NFZ, BZ, or RZ)</td></tr><tr><td>PR</td><td>Perception radius of the DCU</td></tr><tr><td> $\mathrm { S L } = ( x _ { \mathrm { S L } } , y _ { \mathrm { S L } } , z _ { \mathrm { S L } } )$   $\mathrm { S N R } _ { \mathrm { G E } _ { i } } ( t )$ </td><td>Starting location of the DCU</td></tr><tr><td> $\mathbb { T } \mathbb { A } = ( p _ { \mathbb { T } \mathbb { A } } , l _ { \mathbb { T } \mathbb { A } } , w _ { \mathbb { T } \mathbb { A } } )$ </td><td>The signal-to-noise ratio at the begin- ning of time slot t of GEi</td></tr><tr><td></td><td>Take-off area location with lower- left coordinate point, length  $l _ { \mathbb { T A } } ,$  and width wTA</td></tr><tr><td>T  $T D _ { \mathrm { G E } _ { i } } ( t )$ </td><td>Total number of time slots</td></tr><tr><td></td><td>Data transmitted between the DCU and GEi in the time slot t</td></tr><tr><td> $T P _ { \mathrm { G E } _ { i } }$ </td><td>Transmit power of the i-th GE</td></tr><tr><td>tfy</td><td>Time used for flight in the time slot t of the DCU</td></tr><tr><td> $t _ { \mathrm { h o v e r } }$ </td><td>Time used for hovering in the time slot</td></tr><tr><td> $\begin{array} { l } { { v _ { \mathrm { D C U } } } ( t ) } \\ { ( v _ { x } ( t ) , v _ { y } ( t ) , v _ { z } ( t ) ) } \end{array}$  二</td><td>t of the DCU Flight speed of the DCU at the begin-</td></tr><tr><td>vmax</td><td>ning of time slot t Maximum flight speed of the DCU</td></tr><tr><td></td><td>and OUs</td></tr><tr><td>Vlimit</td><td>Speed limit in  $\mathbb { R } _ { \mathrm { R Z } }$  for the DCU and OUs</td></tr><tr><td>∧</td><td>Logical AND operator</td></tr><tr><td></td><td>Hadamard (element-wise) product</td></tr><tr><td> $\| C P 1 - C P 2 / A \|$ </td><td>Distance between two coordinate points or to area A</td></tr><tr><td></td><td>Location of the x-th XX in A  $( \mathrm { X X } ~ =$ </td></tr><tr><td> $\begin{array} { r l } {  { \mathbb { R } _ { \mathrm { X X } _ { x } } } } \\ & { ( p _ { \mathrm { X X } _ { x } } , l _ { \mathrm { X X } _ { x } } , w _ { \mathrm { X X } _ { x } } ) } \\ & { { \boldsymbol { \Lambda } } + } \end{array}$ </td><td>NFZ, BZ, or RZ)</td></tr><tr><td>△t</td><td>Fixed time slot duration  $\mathrm { S N R } _ { \mathrm { G E } _ { i } } ( t )$ </td></tr></table>

trajectory planning.

## 3.2.2 Data Transmission Model

The data transmission model describes how much the data collection volume of the DCU collects in the time slot t. Before giving how to compute it, we first present the effective information rate of the DCU in the time slot t. The DCU collects data from a single selected GE within its communication range in each time slot by using the standard time division multiple access [37]. When DCU collects data, it is in a hovering state without moving. The DCU begins to collect data at time $t + t _ { \mathrm { f l y } } \ ( t _ { \mathrm { f l y } } = \Delta t / 2 )$ and lasts for $t _ { \mathrm { h o v e r } } = \Delta t - t _ { \mathrm { f i y } }$ . As a result, assuming the GE that is currently collecting data is $\operatorname { G E } _ { i } ,$ the effective information rate during the time slot t is as follows:

$$
B _ { \mathrm { G E } _ { i } } ( t ) = \log _ { 2 } \left( 1 + \mathrm { S N R } _ { \mathrm { G E } _ { i } } ( t ) \right) ,\tag{4}
$$

where $\mathrm { S N R } _ { \mathrm { G E } _ { i } } ( t ) = T P _ { \mathrm { G E } _ { i } } \cdot G _ { \mathrm { G E } _ { i } } ( t ) / \mathcal { N }$ is the signal-tonoise ratio at the beginning of time slot $t , T P _ { \mathrm { G E } _ { i } }$ is the transmit power of $\mathrm { G E } _ { i } , G _ { \mathrm { G E } _ { i } } ( t )$ is the channel power gain from the DCU to GE<sub>i</sub> at the beginning of time slot $t ,$ and N is the noise power.

Given the fixed flight altitude of the DCU H, the communication link with GE is assumed to follow a line-of-sight (LoS) air-to-ground (A2G) channel model [49]. This assumption aligns well with the characteristics of UAV-assisted data collection, where the DCU actively approaches each GE and performs data acquisition at short distances during hovering. Such close-range outdoor A2G communication typically presents dominant LoS components, making the LoS model a widely adopted and effective abstraction in UAV data collection trajectory planning scenarios. The free-space pathloss model is used to compute $G _ { \mathrm { G E } _ { i } } ( t )$ as follows [42]:

$$
\frac { G _ { \mathrm { G E } _ { i } } ( t ) = } { \sqrt { | | ( x _ { \mathrm { D C U } , i + t _ { \mathrm { f l y } } } , y _ { \mathrm { D C U } , i + t _ { \mathrm { f l y } } } , H ) - ( x _ { \mathrm { G E } _ { i } } , y _ { \mathrm { G E } _ { i } } , 0 ) | | ^ { 2 } } } ,\tag{5}
$$

where α is the channel power gain $\begin{array} { r l } & { \sqrt { \left\| \left( x _ { \mathrm { D C U } , i + t _ { \mathrm { f l y } } } , y _ { \mathrm { D C U } , i + t _ { \mathrm { f l y } } } , H \right) - \left( x _ { \mathrm { G E } _ { i } } , y _ { \mathrm { G E } _ { i } } , 0 \right) \right\| ^ { 2 } } \ = \ 1 } \\ & { \mathrm { d i s t a n c e . } } \end{array}$

Note that, if the DCU wants to transmit data, $\operatorname { S N R } _ { \mathrm { G E } _ { i } } ( t )$ must exceed a certain threshold τ [43]. Therefore, according to Eqs. (4) and (5), the data collection volume of the DCU collected in the time slot t $T D _ { \mathrm { G E } _ { i } } ( t )$ can be computed as follows:

$$
T D _ { \mathrm { G E } _ { i } } ( t ) = \left\{ \begin{array} { l l } { B _ { \mathrm { G E } _ { i } } ( t ) t _ { \mathrm { h o v e r } } , } & { \mathrm { i f } \ D V _ { \mathrm { G E } _ { i } , t } > B _ { \mathrm { G E } _ { i } } ( t ) } \\ & { \mathrm { a n d } \ \mathrm { S N R } _ { \mathrm { G E } _ { i } } ( t ) \geq \tau , } \\ { D V _ { \mathrm { G E } _ { i } , t } , } & { \mathrm { i f } \ D V _ { \mathrm { G E } _ { i } , t } \leq B _ { \mathrm { G E } _ { i } } ( t ) } \\ & { \mathrm { a n d } \ \mathrm { S N R } _ { \mathrm { G E } _ { i } } ( t ) \geq \tau , } \\ { 0 , } & { \mathrm { i f } \ \mathrm { S N R } _ { \mathrm { G E } _ { i } } ( t ) < \tau , } \end{array} \right.\tag{6}
$$

where $D V _ { \mathrm { G E } _ { i } , t }$ is the data volume of the i-th GE at the beginning of time slot t.

## 3.2.3 Energy Consumption Model

The energy consumption model is used to describe how much the remaining energy of the DCU changes in the time slot t. The energy consumption of the DCU in the time slot t can be divided into two parts: the energy consumed by flying (denoded as $e _ { \mathrm { f l y } } ( t ) )$ and the energy consumed by hovering (denoted by $e _ { \mathrm { h o v e r } } ( t ) )$ . For $e _ { \mathrm { f l y } } ( t )$ , it can be computed as follows [45]:

$$
\begin{array} { r l } & { e _ { \mathrm { f l y } } ( t ) = } \\ & { \Bigl ( \displaystyle \frac { \lambda } { 8 } \rho \eta A _ { r } \mathbb { S } ^ { 3 } r _ { \mathrm { r o t o r } } ^ { 3 } \left( 1 + \frac { 3 v _ { \mathrm { D C U } } ( t ) ^ { 2 } } { U _ { \mathrm { t i p } } ^ { 2 } } \right) + \frac { 1 } { 2 } d _ { 0 } \rho s A _ { r } v _ { \mathrm { D C U } } ( t ) ^ { 3 } \Bigr ) t _ { \mathrm { f l y } } . } \end{array}\tag{7}
$$

where $\lambda$ denotes the profile drag coefficient, A<sub>r</sub> the rotor disc area, ℑ the blade angular velocity, $r _ { \mathrm { r o t o r } }$ the rotor radius, $d _ { 0 }$ denotes the fuselage drag coefficient, $\rho$ the density of air, η the rotor solidity factor, $\breve { U } _ { \mathrm { t i p } }$ the tip velocity of the rotor blade, and $v _ { \mathrm { D C U } }$ the velocity of DCU.

For $e _ { \mathrm { h o v e r } } ( t )$ , it can be computed as follows:

$$
\begin{array} { r l } & { e _ { \mathrm { h o v e r } } ( t ) = } \\ & { \left( ( 1 + \Re ) w ^ { 3 / 2 } \sqrt { 1 + \frac { v _ { \mathrm { D C U } } ( t ) ^ { 4 } } { 4 v _ { 0 } ^ { 4 } } } - \frac { v _ { \mathrm { D C U } } ( t ) ^ { 2 } / 2 v _ { 0 } } { \sqrt { 2 \rho A _ { r } } } \right) t _ { \mathrm { h o v e r } } , } \end{array}\tag{8}
$$

where ℜ is the incremental correction factor to induced power, w the weight of DCU, and $v _ { 0 }$ the mean rotor induced velocity in hover.

Note that since the energy consumed by DCU for communication is much less than that consumed for hovering [44], when calculating $e _ { \mathrm { h o v e r } } ( t )$ , we ignore the energy consumed by DCU for data transmission. Besides, the UAVrelated parameter values in this section follow the settings provided in [45].

## 4 OPTIMIZATION PROBLEM

In this section, we present the main requirements behind the optimization problem to highlight the motivation before formally defining it. Then we detail the formalized problem and its characteristics.

## 4.1 Requirement Analysis

The optimization problem involves two primary requirements. The first requirement includes the constraints imposed by the physical environment, and the second one involves the task-specific requirements associated with data collection in the low-altitude economy. For the former, the following requirement is taken into consideration:

R1) Limited Mobility. The moving distance of DCU during each time slot should satisfy the Eq. (2).

For the latter, the following requirements are taken into consideration:

R2) Robust Obstacle Avoidance. Since data collection in the low-altitude economy is concentrated in urban areas and there is airspace reuse in low-altitude areas [35], when the DCU conducts data collection, it not only needs to avoid $\mathbb { R } _ { \mathrm { B Z } } , \mathbb { R } _ { \mathrm { N F Z } } ,$ , but also OUs.

R3) Compliance. Unlike general trajectory planning tasks, DCU operating in urban low-altitude environments must comply with strict regulations. They must reduce speed near $\mathbb { R } _ { \mathrm { R Z } }$ to minimize noise and meet regulatory standards.

R4) Economy. Within the low-altitude economy, trajectory planning tasks must jointly consider the maximization of data acquisition and the minimization of energy consumption to maximize the trajectory planning task benefits. Consequently, the DCU is required not only to collect sufficient data but also to complete the task along an energyefficient trajectory that minimizes energy costs.

## 4.2 Problem Formulation

According to the requirement analysis introduced in Section 4.1, we try to optimize the flight trajectory of DCU while maximizing the amount of collected data. The optimization problem can be formally formulated as follows:

$$
\mathbf { O P } \colon \ \operatorname { a r g m a x } \ \sum _ { t = 1 } ^ { T } T D _ { \mathrm { G E } _ { i } } ( t )\tag{9}
$$

s.t.

$$
\mathrm { G E } _ { i } = \arg \operatorname* { m a x } \left( \{ B _ { \mathrm { G E } _ { i } } ( t ) \} _ { i = 1 } ^ { N _ { \mathrm { G E } } } \land \left( \mathrm { S N R } _ { \mathrm { G E } _ { i } } ( t ) \geq \tau \right) \right)\tag{9a}
$$

L<sub>DCU,t+1</sub>

$$
\begin{array} { r l } & { = ( x _ { \mathrm { D C U } , t } + v _ { x } ( t ) t _ { \mathrm { f l y } } , \ y _ { \mathrm { D C U } , t } + v _ { y } ( t ) t _ { \mathrm { f l y } } , \ H ) , } \end{array}\tag{9b}
$$

$$
v _ { \mathrm { D C U } } ( t ) = ( v _ { x } ( t ) , v _ { y } ( t ) , 0 ) \leq v _ { \mathrm { m a x } } , \quad \forall t ,\tag{9c}
$$

$$
v _ { \mathrm { D C U } } ( t ) \leq v _ { \mathrm { l i m i t } } , \quad \mathrm { i f ~ } L _ { \mathrm { D C U } , t } \in \{ \mathbb { R } _ { \mathrm { R Z } , m } \} _ { m = 1 } ^ { N _ { \mathrm { R Z } } } ,\tag{9d}
$$

$$
\left( L _ { \mathrm { D C U } , t } , L _ { \mathrm { O U } , t } \right) \in \mathbb { A } , \quad \forall t ,\tag{9e}
$$

$$
\left( L _ { \mathrm { D C U } , t } , L _ { \mathrm { O U } , t } \right) \notin \left\{ \mathbb { R } _ { \mathrm { N F Z } , l } \right\} _ { l = 1 } ^ { N _ { \mathrm { N F Z } } } , \quad \forall t ,
$$

$$
( L _ { \mathrm { D C U } , t } , L _ { \mathrm { O U } , t } ) \notin \{ \mathbb { R } _ { \mathrm { B Z } , n } \} _ { n = 1 } ^ { N _ { \mathrm { B Z } } } , \quad \forall t ,\tag{9f}
$$

(9g)

$$
\begin{array} { r } { \left\| L _ { \mathrm { D C U } , t } - L _ { \mathrm { O U } _ { j } , t } \right\| > 0 , \quad \forall t , \ j \in [ 1 , N _ { \mathrm { O U } } ] , } \end{array}\tag{9h}
$$

$$
( L _ { \mathrm { D C U } , 1 } = \mathrm { S L } \in \mathbb { T A } ) \wedge ( L _ { \mathrm { D C U } , T } = \mathrm { E L } \in \mathbb { L A } ) ,\tag{9i}
$$

$$
\sum _ { t = 1 } ^ { T } ( e _ { \mathrm { f l y } } ( t ) + e _ { \mathrm { h o v e r } } ( t ) ) \leq E _ { \mathrm { l i m i t } } , \quad \forall t .\tag{9j}
$$

The objective function OP maximizes the amount of data collected over the given time slots. Constraint (9a) selects a GE to collect data because the DCU follows a maximum signal strength policy to connect to the GE with the highest received signal power [49]. Note that constraint (9a) defines the feasible region for data collection, where a GE can be served only when the DCU is within its communication range, instead of enforcing a distance-priority rule. Once the DCU enters the feasible range of a GE, data collection occurs automatically. When multiple GEs have the same effective rate $B _ { \mathrm { G E } _ { i } } ( t )$ , a randomly GE will be collected data by the DCU. Constraint (9b) governs the position updates of the DCU according to the mobility model. Constraint (9c) enforces the maximum speed limit, and Constraint (9d) enforces the maximum speed limit in $\mathbb { R } _ { \mathrm { R Z } }$ to satisfy R1 and R3. Constraints (9e), (9f), (9g), and (9h) ensure that the DCU operates within $\mathbb { A } ,$ avoids $\mathbb { R } _ { \mathrm { N F Z } } ,$ , and prevents collisions with $\mathbb { R } _ { \mathrm { B Z } }$ or OUs to satisfy R2 and R3. constraint (9i) ensures DCU takes off from <sup>TA</sup> and lands off in <sup>LA</sup>, while constraint (9j) ensures the maximum energy consumption of the DCU in a trajectory planning task to satisfy R4.

## 4.3 Problem Characteristics

This optimization problem involves continuous control, nonlinear constraints, dynamic environmental factors (such as OUs), as well as regulatory and energy limitations, making it structurally complex and difficult. Traditional optimization algorithms often perform inefficiently and lack adaptability when dealing with such high-dimensional, dynamic, and partially observable problems. In contrast, DRL offers adaptive learning capabilities, making it well-suited for continuous control and long-term optimization. LLMs, on the other hand, can provide rule-compliant and reasoning decisions in critical scenarios by leveraging rich prior knowledge. The integration of DRL and LLM leverages efficiency, generalization, and safety, making it more suitable than traditional methods to solve complex UAV trajectory planning problems.

## 5 PROPOSED ALGORITHM

This section first formulates the optimization problem from Section 4 as a POMDP to enable solution via DRL. We then present the SAC algorithm, which serves as the foundation for our algorithm. Finally, we introduce the proposed algorithm and demonstrate its effectiveness in addressing the formulated problem.

## 5.1 POMDP Modeling

As the future position of the DCU is determined solely by its current state $( \mathrm { i . e . , }$ position and velocity), the trajectory planning problem satisfies the Markov property. Nevertheless, due to the DCU’s limited ability to perceive the full environmental state, the problem is more appropriately formulated as a POMDP, defined by a corresponding tuple $( \mathcal { O } , \mathcal { A } , r , \mathcal { P } , \delta )$ , where the observation space O replaces the state space [46]. Then, the details of $\mathcal { O } , A ,$ and $r$ in $( \mathcal { O } , \mathcal { A } , r , \mathcal { P } , \delta )$ are as follows:

Observation Space $\begin{array} { r l r l } { \mathcal { O } \colon } & { { } o _ { t } } & { \in } & { { } \mathcal { O } } \end{array}$ is the state that the DCU can observe at time $t ,$ where $\begin{array} { r l } { O _ { t } } & { { } = } \end{array}$ $\left( o _ { \mathrm { G E } , t } , o _ { Z , t } , o _ { \mathrm { O U } , t } , o _ { \mathrm { D C U } , t } \right)$

• o<sub>GE,t</sub> is the state about all GEs and $\begin{array} { r l } { O _ { \mathrm { G E } , t } \quad } & { { } = } \end{array}$ $\{ L _ { \mathrm { G E } _ { i } } , D V _ { \mathrm { G E } _ { i } , t } , T P _ { \mathrm { G E } _ { i } } \} _ { i = 1 } ^ { N _ { \mathrm { G E } } }$

${ } _ { O } { } _ { Z , t }$ is the state about all zones and $\begin{array} { r l } { O Z , t } & { { } = } \end{array}$ $\{ \{ \mathbb { R } _ { \mathrm { N F Z } , l } \} _ { l = 1 } ^ { N _ { \mathrm { N F Z } } } , \{ \mathbb { R } _ { \mathrm { R Z } , m } \} _ { m = 1 } ^ { N _ { \mathrm { R Z } } } , \{ \mathbb { R } _ { \mathrm { B Z } , n } \} _ { n = 1 } ^ { N _ { \mathrm { B Z } } } \}$

$\scriptstyle O \mathrm { O U } , t$ represents the state information of OUs located within the perception radius of the DCU during time slot t. It is defined as $o _ { \mathrm { O U } , t } ~ = ~ \{ ( L _ { \mathrm { O U } _ { j } , t } , v _ { \mathrm { O U } _ { j } , t } ) \} _ { j = 1 } ^ { N _ { \mathrm { O U } } } ,$ where $\boldsymbol { L } _ { \mathrm { O U } _ { j } , t }$ and $v _ { \mathrm { O U } _ { j } , t }$ denote the position and velocity of $\mathrm { O U } _ { j }$ at the beginning of time slot t. The number of OUs within the perception radius of the DCU may vary across different time slots, resulting in changes in the dimension of $\boldsymbol { o } _ { \mathrm { O U } , t }$ . To maintain a consistent input size, the zero-padding method is employed to standardize the dimension of o<sub>OU,t</sub>.

$O _ { \mathrm { Ḋ } \mathrm { Ḋ } \mathrm { Ḋ } \mathrm { Ḍ C U Ḍ , t Ḍ } }$ is the state about DCU itself and $o _ { \mathrm { D C U } , t } =$ $\{ L _ { \mathrm { D C U } , t } , v _ { \mathrm { D C U } , t } , E ( t ) , T D _ { \mathrm { G E } _ { i } } ( t ) , \mathbb { T A } , \mathbb { L A } \}$

Action Space A: $a _ { t } \in \mathcal A$ is the sampled action at time t and $a _ { t } = ( v _ { x } ( t ) , v _ { y } ( t ) )$ , which means the DCU will move at the velocity $( v _ { x } ( t ) , v _ { y } ( t ) )$ at time t.

Reward function $r \cdot  { r }$ is used to effectively guide the trajectory planning during the data collection process and plays a critical role in both the efficiency and performance of policy learning. To facilitate learning an optimal policy aligned with the objective function OP and its associated constraints, we formulate a composite reward function, expressed as follows:

$$
r _ { t } = r _ { 1 t } + r _ { 2 t } + r _ { 3 t } + r _ { 4 t } + r _ { 5 t } + r _ { 6 t } + r _ { 7 t } + r _ { 8 t } + r _ { 9 t } .\tag{10}
$$

$r _ { 1 t }$ encourages the DCU to collect data, and is as follows:

$$
r _ { 1 t } = \left\{ \begin{array} { l l } { \sigma _ { 1 } , } & { \mathrm { i f } \ T D _ { \mathrm { G E } _ { i } } ( t + 1 ) \geq 0 , } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right.\tag{11}
$$

$r _ { 2 t }$ is used to ensure that the DCU will not collide with OUs and is as follows:

$$
r _ { 2 t } = \left\{ \begin{array} { l l } { 0 , } & { \mathrm { i f ~ } d _ { t , \mathrm { O U } } \geq d _ { \mathrm { s a f e } , \mathrm { O U } } , } \\ { - \sigma _ { 2 } \frac { d _ { \mathrm { s a f e } , \mathrm { O U } } - d _ { t , \mathrm { O U } } } { d _ { \mathrm { s a f e } , \mathrm { O U } } - d _ { \mathrm { m i n } , \mathrm { O U } } } , } & { \mathrm { i f ~ } d _ { \mathrm { m i n } , \mathrm { O U } } < d _ { t , \mathrm { O U } } . } \\ { - \sigma _ { 2 } , } & { \mathrm { i f ~ } d _ { t , \mathrm { O U } } \leq d _ { \mathrm { m i n } , \mathrm { O U } } , } \end{array} \right.\tag{12}
$$

where $d _ { t , \mathrm { O U } } = \arg \operatorname* { m i n } \{ | | L _ { \mathrm { D C U } , t } - L _ { \mathrm { O U } _ { j } , t } | | \} _ { j = 1 } ^ { N _ { \mathrm { O U } } } , d _ { \mathrm { m i n , O U } }$ is the minimum safe distance between the DCU and OUs, which is used for the DCU to adjust the speed to avoid collisions, and $d _ { \mathrm { s a f e , O U } }$ is the safe distance threshold between the DCU and OUs.

$r _ { 3 t }$ is used to ensure that the DCU will not collide with tall buildings and is as follows:

$$
\begin{array} { r } { r _ { 3 t } = \left\{ \begin{array} { l l } { 0 , } & { \mathrm { i f ~ } d _ { t , \mathrm { B Z } } \geq d _ { \mathrm { s a f e } , \mathrm { B Z } } , } \\ { - \sigma _ { 3 } \times \frac { d _ { \mathrm { s a f e } , \mathrm { B Z } } - d _ { t , \mathrm { B Z } } } { d _ { \mathrm { s a f e } , \mathrm { B Z } } - d _ { \mathrm { m i n } , \mathrm { B Z } } } , } & { \mathrm { i f ~ } d _ { \mathrm { m i n } , \mathrm { B Z } } < d _ { t , \mathrm { B Z } } } \\ & { \mathrm { a n d ~ } d _ { t , \mathrm { B Z } } < d _ { \mathrm { s a f e } , \mathrm { B Z } } , } \\ { - \sigma _ { 3 } , } & { \mathrm { i f ~ } d _ { t , \mathrm { B Z } } \leq d _ { \mathrm { m i n } , \mathrm { B Z } } , } \end{array} \right. } \end{array}\tag{13}
$$

where $d _ { t , \mathrm { B Z } } \ = \ \arg \operatorname* { m i n } \{ | | L _ { \mathrm { D C U } , t } \ - \ \mathbb { \mathbb { R } } _ { \mathrm { B Z } , n } | | \} _ { n = 1 } ^ { N _ { \mathrm { B Z } } } , \ d _ { \mathrm { m i n , B Z } }$ is the minimum safe distance between the DCU and tall buildings, which is used for the DCU to adjust the speed to avoid collisions, and $d _ { \mathrm { s a f e , B Z } }$ is the safe distance threshold between the DCU and tall buildings.

$r _ { 4 t }$ is used to ensure that the DCU will not fly into NFZs and is as follows:

$$
\begin{array} { r l } & { r _ { 4 t } = } \\ & { \left\{ \begin{array} { l l } { 0 , } & { \mathrm { i f ~ } d _ { t , \mathrm { N F Z } } \geq d _ { \mathrm { s a f e } , \mathrm { N F Z } } , } \\ { - \sigma _ { 4 } \times \frac { d _ { \mathrm { s a f e } , \mathrm { N F Z } } - d _ { t , \mathrm { N F Z } } } { d _ { \mathrm { s a f e } , \mathrm { N F Z } } - d _ { \mathrm { m i n } , \mathrm { N F Z } } } , } & { \mathrm { i f ~ } d _ { \mathrm { m i n } , \mathrm { N F Z } } < d _ { t , \mathrm { N F Z } } } \\ & { \mathrm { a n d ~ } d _ { t , \mathrm { N F Z } } < d _ { \mathrm { s a f e } , \mathrm { N F Z } } , } \\ { - \sigma _ { 4 } , } & { \mathrm { i f ~ } d _ { t , \mathrm { N F Z } } \leq d _ { \mathrm { m i n } , \mathrm { N F Z } } , } \end{array} \right. } \end{array}\tag{14}
$$

where $\begin{array} { r l } { d _ { t , \mathrm { N F Z } } } & { { } = } \end{array}$ arg min $\{ \| L _ { \mathrm { D C U } , t } - \mathbb { R } _ { \mathrm { N F Z } , l } \| \} _ { l = 1 } ^ { N _ { \mathrm { N F Z } } } ,$ $d _ { \mathrm { m i n , N F Z } }$ is the minimum safe distance between the DCU and NFZs, which is used for the DCU to adjust the speed to avoid collisions, and $d _ { \mathrm { s a f e , N F Z } }$ is the safe distance threshold between the DCU and NFZs.

$r _ { 5 t }$ is used to ensure that the speed of the DCU when flying into residential areas meets the speed limit and is as follows:

$$
\begin{array} { r } { r _ { 5 t } = \left\{ \begin{array} { l l } { 0 , } & { \mathrm { i f ~ } v _ { \mathrm { D C U } } ( t ) \leq v _ { \mathrm { l i m i t } } \mathrm { ~ a n d ~ } } \\ & { L _ { \mathrm { D C U } , t } \in \{ \mathbb { R } _ { \mathrm { R Z } , m } \} _ { m = 1 } ^ { N _ { \mathrm { R Z } } } , } \\ { - \sigma _ { 5 } \times \frac { v _ { \mathrm { D C U } } ( t ) - v _ { \mathrm { l i m i t } } } { v _ { \mathrm { m a x } } - v _ { \mathrm { l i m i t } } } , } & { \mathrm { i f ~ } v _ { \mathrm { l i m i t } } < v _ { \mathrm { D C U } } ( t ) \leq v _ { \mathrm { m a x } } } \\ & { \mathrm { a n d ~ } L _ { \mathrm { D C U } , t } \in \{ \mathbb { R } _ { \mathrm { R Z } , m } \} _ { m = 1 } ^ { N _ { \mathrm { R Z } } } . } \end{array} \right. } \end{array}\tag{15}
$$

r<sub>6t</sub> is used to ensure that the DCU should not fly out of the given area and is as follows:

$$
\begin{array} { r } { r _ { 6 t } = \left\{ \begin{array} { l l } { 0 , } & { \mathrm { i f ~ } d _ { t , \mathrm { A } } \geq d _ { \mathrm { s a f e } , \mathrm { A } } , } \\ { - \sigma _ { 6 } \times \displaystyle \frac { d _ { \mathrm { s a f e } , \mathbb { A } } - d _ { t , \mathrm { A } } } { d _ { \mathrm { s a f e } , \mathrm { A } } - d _ { \operatorname* { m i n } , \mathrm { A } } } , } & { \mathrm { i f ~ } d _ { \mathrm { m i n } , \mathrm { A } } < d _ { t , \mathrm { A } } < d _ { \mathrm { s a f e } , \mathrm { A } } , } \\ { - \sigma _ { 6 } , } & { \mathrm { i f ~ } L _ { \mathrm { D C U } , t } \not \in \mathrm { A } , } \end{array} \right. } \end{array}\tag{16}
$$

where $d _ { t , \mathbb { A } } = \| L _ { \operatorname { D C U } , t } - \mathbb { A } \|$ is the distance between the DCU and the boundary of <sup>A</sup> in the time slot $t , d _ { \mathrm { m i n , A } }$ is the minimum safe distance between the DCU and the boundary of $\mathbb { A } ,$ which is used for the DCU to adjust the speed to avoid flying out, and $d _ { \mathrm { s a f e , A } }$ is the safe distance threshold between the DCU and the boundary of <sup>A</sup>.

r<sub>7t</sub> is used to encourage that the DCU can land within the landing area and is as follows:

$$
r _ { 7 t } = \left\{ \begin{array} { l l } { 0 , } & { \mathrm { i f ~ } d _ { t , \mathbb { L } \mathbb { A } } \ge d _ { t a r , \mathbb { L } \mathbb { A } } , } \\ { \displaystyle - \sigma _ { 7 } \times \left( 1 - \frac { d _ { t , \mathbb { L } \mathbb { A } } } { d _ { t a r , \mathbb { L } \mathbb { A } } } \right) , } & { \mathrm { i f ~ } 0 < d _ { t , \mathbb { L } \mathbb { A } } < d _ { t a r , \mathbb { L } \mathbb { A } } . } \end{array} \right.\tag{17}
$$

$r _ { 8 t }$ is used to encourage the DCU to return to the landing area before its energy is exhausted and is as follows:

$$
r _ { 8 t } = \left\{ \begin{array} { l l } { \displaystyle 0 , } & { \mathrm { i f ~ } E ( t ) \geq E _ { \mathrm { m i n } } ( t ) , } \\ { \displaystyle - \sigma _ { 8 } \times \frac { E _ { \mathrm { m i n } } ( t ) - E ( t ) } { E _ { \mathrm { m i n } } ( t ) } , } & { \mathrm { i f ~ } E ( t ) < E _ { \mathrm { m i n } } ( t ) , } \end{array} \right.\tag{18}
$$

where $E _ { \mathrm { m i n } } ( t )$ is the minimum energy required for DCU to reach the <sup>LA</sup> at the beginning of time slot t and $E _ { \mathrm { m i n } } ( t ) =$ $e _ { \mathrm { f l y } } ( t ) \cdot d _ { t , \mathbb { L A } } / v _ { \mathrm { m a x } }$

r<sub>9t</sub> is used to encourage the DCU to complete the data collection quickly to reduce energy consumption, and is as follows:

$$
r _ { 9 t } = - \sigma _ { 9 } .\tag{19}
$$

## 5.2 SAC Algorithm

SAC is an off-policy DRL method based on the maximumentropy framework [38], [39]. Its off-policy property enables efficient training and easy incorporation of LLM guidance, making it suitable for continuous-control problems such as UAV trajectory planning.

SAC maximizes both the expected cumulative reward and the policy entropy:

$$
\pi ^ { * } = \arg \operatorname* { m a x } _ { \pi } \sum _ { t = 0 } ^ { \infty } \mathbb { E } _ { \mathcal { P } , \pi } \big [ \delta ^ { t } \big ( r _ { t } + \mu \mathcal { H } ( \pi ( \cdot \mid o _ { t } ) ) \big ) \big ] ,\tag{20}
$$

where δ is the discount factor, $\mu$ is the temperature parameter, and $\begin{array} { r } { \mathcal { H } ( \pi ( \cdot  { | } \mathbf { \phi } _ { o _ { t } } ) ) = - \int \pi ( a _ { t }  { | } \mathbf { \phi } _ { o _ { t } } ) \log \pi ( a _ { t }  { | } \mathbf { \phi } _ { o _ { t } } ) \hat { d } a _ { t } } \end{array}$ is the policy entropy. The soft Bellman equation is defined as:

$$
\left\{ \begin{array} { l l } { \displaystyle Q _ { \mathrm { s o f t } } \big ( o _ { t } , a _ { t } \big ) = r _ { t } + \delta \mathbb { E } _ { \mathcal { P } } \big [ V _ { \mathrm { s o f t } } \big ( o _ { t + 1 } \big ) \big ] , } \\ { \displaystyle V _ { \mathrm { s o f t } } \big ( o _ { t } \big ) = \mathbb { E } _ { a _ { t } \sim \pi } \big [ Q _ { \mathrm { s o f t } } \big ( o _ { t } , a _ { t } \big ) - \mu \log \pi \big ( a _ { t } \mid o _ { t } \big ) \big ] . } \end{array} \right.\tag{21}
$$

The critic network minimizes the following loss:

$$
J _ { Q } ( \varphi _ { i } ) = \mathbb { E } _ { ( o _ { t } , a _ { t } , r _ { t } , o _ { t + 1 } ) \sim D } \Big [ \big ( Q _ { i } ^ { \theta } \big ( o _ { t } , a _ { t } \big ) - y _ { t } \big ) ^ { 2 } \Big ] ,\tag{22}
$$

with target value y<sub>t</sub> = r<sub>t</sub> + $\delta \Bigl ( \operatorname* { m i n } _ { j } Q _ { j } ^ { \theta _ { \mathrm { t a r } } } \Bigl ( o _ { t + 1 } , \tilde { a } _ { t + 1 } \Bigr ) - \mu \log \bar { \pi } ^ { \phi } \bigl ( \tilde { a } _ { t + 1 } \mid o _ { t + 1 } \bigr ) \Bigr ) ,$ where $\boldsymbol { D } ^ { \setminus }$ is the experience pool, and $\theta _ { \mathrm { t a r } }$ denotes target critic parameters. The actor is optimized via reparameterization:

$$
\begin{array} { r l r } & { } & { J _ { \pi } ( \phi ) = \mathbb { E } _ { o _ { t } \sim D , \varsigma \sim K ( 0 , 1 ) } \Big [ \mu \log \pi ^ { \phi } ( \tilde { a } _ { t } ^ { \phi } ( o _ { t } , \varsigma ) \mid o _ { t } ) } \\ & { } & { \qquad - Q ^ { \theta } ( o _ { t } , \tilde { a } _ { t } ^ { \phi } ( o _ { t } , \varsigma ) ) \Big ] , } \end{array}\tag{23}
$$

where $\widetilde { a } _ { t } ^ { \phi } ( o _ { t } , \varsigma ) = \operatorname { t a n h } \bigl ( \beta ^ { \phi } ( o _ { t } ) + \alpha ^ { \phi } ( o _ { t } ) \odot \varsigma \bigr ) , \beta ^ { \phi }$ and $\alpha ^ { \phi }$ denote the Gaussian mean and standard deviation, ς is a

standard normal noise, and ⊙ is element-wise multiplication.

Through iterative updates of $\pi , Q ,$ and V , SAC achieves a stable, high-performance policy for continuous control under uncertainty.

## 5.3 Our Algorithm

This section presents the core design principles of our trajectory planning algorithm, outlines its detailed implementation, and provides a comprehensive analysis of its computational complexity.

## 5.3.1 Main Idea

Based on the POMDP formulation in Section 5.1 and the continuous nature of DCU’s velocity, we adopt SAC algorithm to optimize the DCU’s flight trajectory during the data collection. However, in the context of low-altitude economy scenarios, where strict regulatory compliance and robust obstacle-avoidance capability are critical, the use of DRL alone may be insufficient due to its reliance on trialand-error learning and lack of prior domain knowledge. To address this issue, we propose an enhanced decisionmaking algorithm by integrating an LLM into the action selection module, as illustrated in Fig. 2. Specifically, at a given moment during data collection, the DCU continuously monitors its surroundings through onboard sensors. When the sensed distance to any nearby obstacle (e.g., BZs, NFZs, RZs, or OUs) falls below a predefined safety threshold, a decision condition is met, thereby triggering the LLM-based action selection pathway. In this mode, a Prompt Generator compiles semantic information, including environmental context, DCU status, and obstacle details, into a structured prompt, which is then input to an LLM. The LLM responds with a recommended action, leveraging its rich prior knowledge to ensure safety and regulatory compliance. An Extractor then parses the LLM’s response into actionable control parameters for the DCU. Conversely, when no immediate obstacle is detected, the system defaults to the standard SAC policy network for action selection. This hybrid structure enables the agent to benefit from both data-driven learning and knowledge-driven reasoning. The SAC component provides efficient trajectory planning in general scenarios, while the LLM supplements decisionmaking in critical or unfamiliar environments requiring sophisticated judgment. By combining the generalization capability of DRL with the reasoning capability and prior knowledge of an LLM, the proposed algorithm achieves superior performance in complex real-world scenarios, ensuring not only energy efficiency but also operational safety and compliance.

## 5.3.2 Algorithm Detail

Our proposed algorithm, which is detailed in Algorithm 1, is designed to enable the DCU to effectively perform trajectory planning by learning an optimal velocity control policy that guides its trajectory to maximize data acquisition and avoid collision. The main process of our algorithm is shown in Fig. 2.

The proposed algorithm takes the environment as input (Line 1) and outputs an optimal policy network (Line 2)

![](images/2f83328f447b3a7abc534927efc136a3207aa6686d08a89c1a06bc076fc8e64c.jpg)  
Fig. 2: The proposed algorithm integrates an LLM into SAC for conditional action selection. The LLM is invoked to generate actions when obstacles are detected; otherwise, actions are selected by the SAC policy network. The chosen actions interact with the environment, and transitions are stored to train the critic networks

![](images/17f6bc7a920c272d01f32bbd42866b278fb2571a6502820b7c5005e8583072d9.jpg)  
Fig. 3: CoT-based prompt generator used for UAV control. Part (a) defines the task and observation, (b) describes the reasoning principles, and (c) specifies the action format and compact JSON output.

that governs the DCU velocity control. Upon initialization (Line 3), the initialization of the Q-function parameters, policy network parameters, the LLM, the experience pool, and the target network parameters is conducted.

For each training episode, the environment is first reset (Line 5). Then, at each time step within the episode, the algorithm observes the current state and determines whether to invoke the LLM for action selection (Lines 7– 8). It is important to note that this state (o˜<sub>t</sub>) differs from the state (o<sub>t</sub>) used by the policy network. Specifically, it refers to the pre-processed, semantically rich environmental information, such as the positions of obstacles within the DCU’s observation range, as illustrated in Fig. 2. If the decision condition is met, i.e., there are obstacles near the DCU, the LLM is utilized to select an action for the DCU based on the semantic state information generated by the prompt generator. Otherwise, the action is selected using the policy network (Lines 9–12). The selected action is then executed, resulting in the next state and corresponding reward for the subsequent time slot. Simultaneously, the current state, action, and reward are stored in the experience pool (Lines 14–15). The algorithm then checks whether the current episode has terminated. If so, it proceeds to the next episode (Line 17).

For each gradient update step, a batch of samples is drawn from the experience pool (Line 21). Based on this batch, the target values are computed, and the Q-function, policy network, and target network parameters are updated accordingly (Lines 22–24). This process repeats until the episode concludes, after which the next episode begins. Upon completion of all training episodes, the algorithm outputs the final optimized policy network.

After the hybrid SAC–LLM training process described above, we further detail the design of the LLM Prompt Generator, which enables the integration of LLM-based reasoning into the decision loop. When the decision condition is triggered, the prompt generator converts the UAV’s structured observation into a semantically rich text prompt that guides the LLM’s inference. As shown in Fig. 3, the generator follows a chain-of-thought (CoT) design composed of three tightly connected parts: (i) task definition and observation description, which specifies the UAV’s operating environment and observation elements; (ii) reasoning guidelines, which instruct the LLM to reason according to safety, compliance, and efficiency rules; and (iii) output format, which constrains the model to produce a strict JSON object representing a continuous velocity vector $( v _ { x } , v _ { y } ) .$ confidence score, and reasoning summary. This prompt structure ensures interpretability and physical validity of the LLM’s output, enabling seamless conversion into executable control actions for the UAV. Additionally, to address the potential issue of hallucination by LLM, which can lead to the failure of producing valid actions, an Extractor is employed. The extractor first checks whether any action is produced. If no action is generated, the LLM is called again, with a threshold of 10 attempts. If this threshold is exceeded, the episode is terminated. Furthermore, after receiving the action, the extractor verifies whether the magnitude of the velocity vector is less than $v _ { \mathrm { m a x } } .$ . If the velocity exceeds v<sub>max</sub>, the LLM is called again, with the same 10-attempt threshold. If the limit is exceeded again, the episode is terminated. This process ensures the robustness of the decision-making loop and maintains valid and feasible UAV control actions.

Algorithm 1 SAC with LLM-based Trajectory Planning Al  
gorithm   
1: Input: The environment E   
2: Output: The optimal policy network $\pi ^ { * }$   
3: Initialize: Q-function parameters $\theta _ { 1 } , \theta _ { 2 } ,$ policy parame  
ter $\phi ,$ the LLM $\pi ^ { L L M } .$ , experience pool D, target param  
eters $\theta _ { \mathrm { 1 , t a r } } , \theta _ { \mathrm { 2 , t a t } }$   
4: for episode $= 1 , 2 , \ldots , L$ do   
5: Initialize environment: $\varepsilon \gets$ EnvReset()   
6: for each step $= 1 , 2 , \ldots , N$ do   
7: Observe state: $o _ { t }  \mathrm { O b s S t a t e } ( \mathcal { E } )$   
8: Judge if using the LLM: bool ← useLLM(˜o<sub>t</sub>)   
9: if bool then   
10: Select action from the LLM: $a _ { t }  \pi ^ { L L M } ( \tilde { o } _ { t } )$   
11: else   
12: Select action from policy network: $a _ { t } \gets$   
$\pi ^ { \phi } ( o _ { t } )$   
13: end if   
14: Execute action and get new state and reward:   
$( o _ { t + 1 } , r _ { t } , \mathrm { d o n e } ) \gets \mathrm { E x e A c t } ( a _ { t } )$   
15: Store transition in experience pool:   
$( o _ { t } , r _ { t } , a _ { t } , o _ { t + 1 } )  D$   
16: if done then   
17: Reset the environment and continue   
18: end if   
19: end for   
20: for each gradient step do   
21: Randomly sample a batch: $( o _ { t } , r _ { t } , a _ { t } , o _ { t + 1 } ) \gets D$   
22: Compute targets and update Q-functions: $Q _ { 1 } ^ { \theta } , Q _ { 2 } ^ { \theta }$   
23: Update policy network $\pi ^ { \phi }$   
24: Update target parameters: $\theta _ { \mathrm { 1 , t a r } } , \theta _ { \mathrm { 2 , t a r } }$   
25: end for   
26: end for

## 5.3.3 Algorithm Computational Complexity Analysis

During training, our algorithm largely follows the SAC framework for policy optimization. However, unlike standard SAC, our algorithm intermittently replaces the policy network’s action outputs with those generated by an external LLM based on specific conditions. As a result, the overall training complexity consists of two components: the standard SAC update steps and the LLM inference overhead incurred during action selection. Due to each SAC training step including policy network updates with complexity ${ \cal O } ( \bar { d } _ { \pi } )$ , Q-network updates with complexity $O ( d _ { Q } )$ , and target network updates with negligible computational cost, the training computation complexity of SAC is $O ( n { \cdot } ( d _ { \pi } { + } 2 d _ { Q } ) )$ where n is the batch size [50]. Assuming the LLM is queried for p · n samples per batch, the training computation complexity of the LLM is $O ( p \cdot n \cdot L _ { \mathrm { L L M } } \cdot \dot { d } _ { \mathrm { L L M } } ^ { 2 } )$ , where L<sub>LLM</sub> is the number of tokens and $d _ { \mathrm { L L M } }$ is the LLM hidden layer size [51]. Therefore, the training computation complexity of our algorithm is $O ( ( 1 - p ) \cdot n \cdot ( \bar { d } _ { \pi } + 2 \hat { d } _ { Q } ) + p \cdot n \cdot L _ { \mathrm { L L M } } \cdot d _ { \mathrm { L L M } } ^ { 2 } )$

It is important to clarify that the LLM is employed only during the offline training phase to assist the DRL process, rather than during real-time deployment. Specifically, the

LLM provides high-level semantic guidance to the SAC agent, helping it select more informative and regulationcompliant actions during exploration, thereby accelerating policy convergence and improving training stability. Once the SAC policy network is fully trained, the LLM is completely removed from the control loop. During online execution, the UAV relies solely on the lightweight SAC policy for real-time trajectory planning and obstacle avoidance. This design ensures that the runtime control algorithm operates efficiently and achieves collision-free navigation without invoking any LLM inference, thereby fully guaranteeing real-time performance and computational feasibility.

## 6 EXPERIMENTS

In this section, we present the experimental results of the proposed algorithm. Prior to that, we describe the experimental setup and evaluation metrics.

## 6.1 Experiment Setting

For the hardware, all experiments in this study were conducted on a computing platform equipped with Intel® Xeon® Gold 6230 CPUs and NVIDIA GeForce RTX 4090 GPUs.

TABLE 3: Environment Parameters Setting
<table><tr><td>Para.</td><td>Value</td><td>Para.</td><td>Value</td><td>Para.</td><td>Value</td></tr><tr><td> $\overline { { N _ { \mathrm { G E } } } }$ </td><td>[11, 15]</td><td> $v _ { \mathrm { m a x } }$ </td><td>10 m/s</td><td>N</td><td> $\overline { { 1 0 ^ { - 6 } } }$ </td></tr><tr><td> $D V _ { \mathrm { G E } _ { i } }$ </td><td>[1, 3]</td><td> $v _ { \mathrm { l i m i t } }$ </td><td>5 m/s</td><td>PR</td><td>20 m</td></tr><tr><td> $T P _ { \mathrm { G E } _ { i } }$ </td><td>0.01 W</td><td> $E _ { \mathrm { t o t a l } }$ </td><td> $1 \times 1 0 ^ { 6 } \ : \mathrm { J }$ </td><td> $d _ { \mathrm { m i n } } , d _ { \mathrm { s a f e } }$ </td><td>5 m, 15 m</td></tr><tr><td> $\underline { { N _ { \mathrm { O U } } } }$ </td><td>[3,7]</td><td> $\underline { { E _ { \mathrm { l i m i t } } } }$ </td><td> $8 \times 1 0 ^ { 5 } \ : \mathrm { J }$ </td><td>T</td><td>3.6</td></tr></table>

## 6.1.1 Environment Parameters

The experimental environment is simplified to a twodimensional space with <sup>A</sup> of 500 m in both length and width. <sup>TA</sup> and <sup>LA</sup> are square regions measuring $2 5 \times 2 5$ m, located at the top-left and bottom-right corners of $\mathbb { A } ,$ respectively. Given the urban deployment scenario, the environment includes rectangular <sup>R</sup><sub>NFZ</sub>, <sup>R</sup><sub>RZ</sub>, and <sup>R</sup><sub>BZ</sub> with the range of [50, 200] m for both length and width. The number of such regions is randomly chosen from the range [1, 3]. The weights assigned to the components of the reward function are set to [8, 0.4, 0.4, 0.4, 0.6, 0.4, 0.6, 1, 0.01] and can be flexibly adjusted to reflect different task priorities. Other environmental parameters are detailed in Table 3.

## 6.1.2 Algorithm Parameters

For the algorithm, hyperparameters used by the proposed algorithm and other baselines, including SAC+LLM, SAC, Proximal Policy Optimization (PPO) [52], DDPG [53], and Constrained Policy Optimization (CPO) [56], are shown in Table 4. For the LLM used in our algorithm and other baselines, including LLM and SAC+LLM, we choose the DeepSeek-R1, which has a total of 672B parameters and 37B activated parameters [47].

TABLE 4: Hyperparameters Setting
<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Learning rate of actor network</td><td>0.0001</td></tr><tr><td>Learning rate of critic network</td><td>0.0003</td></tr><tr><td>Number of episodes</td><td>4000</td></tr><tr><td>Clip range</td><td>0.2</td></tr><tr><td>Batch size</td><td>256</td></tr><tr><td>Discount factor</td><td>0.99</td></tr><tr><td>Number of hidden layers of DNNs</td><td>2</td></tr><tr><td>Hidden layer size</td><td>64</td></tr></table>

## 6.2 Evaluation Metrics

For the metrics used to evaluate the proposed algorithm and other baselines, we use the metrics commonly adopted in general UAV data collection trajectory planning tasks [48]. In addition, we include metrics that reflect the specific requirements in this paper. All metrics are directly aligned with the core demands of urban low-altitude data collection in the emerging low-altitude economy, where robust obstacle avoidance (R2), compliance (R3), and economy (R4), mentioned in Section 4.1, are essential. Assuming $\dot { N } _ { \mathrm { t o t a l } }$ is the number of experimental tests:

• Data collection rate (DCR): This metric quantifies the average ratio of successfully collected data by the DCU relative to the total target data volume in $N _ { \mathrm { t o t a l } }$ data collection:

$$
\mathrm { D C R } = \frac { \sum _ { i = 1 } ^ { N _ { \mathrm { t e s t } } } D _ { \mathrm { D C U } , i } } { \sum _ { i = 1 } ^ { N _ { \mathrm { t e s t } } } D _ { \mathrm { t o t a l } , i } } ,\tag{24}
$$

where $D _ { \mathrm { D C U } , i }$ is the collected data volume and $D _ { \mathrm { t o t a l , \cdot } }$ <sub>i</sub> is the total target data volume in the i-th task.

• Collision rate (CR): This metric quantifies the ratio of trajectory planning tasks in which the DCU collides with OUs, <sup>R</sup><sub>BZ</sub>, or flies into <sup>R</sup><sub>NFZ</sub>:

$$
\mathrm { C R } = \frac { N _ { \mathrm { C } } } { N _ { \mathrm { t o t a l } } } ,\tag{25}
$$

where $N _ { \mathrm { C } }$ is the number of tasks involving collisions or regulatory violations.

• Successful landing rate (SLR): This metric quantifies the ratio of trajectory planning tasks in which the DCU can return to <sup>LA</sup> before depleting its energy:

$$
\mathrm { S L R } = \frac { N _ { \mathrm { S L R } } } { N _ { \mathrm { t o t a l } } } ,\tag{26}
$$

where $N _ { \mathrm { S L R } }$ is the number of tasks where the DCU successfully lands.

In addition to the commonly used metrics mentioned above, the following indicators are also employed to evaluate the effectiveness of satisfying the requirement for data collection trajectory planning under the low-altitude economy.

• Regulatory violation rate (RVR): This metric quantifies the ratio of tasks in which the DCU exceeds speed limits within <sup>R</sup><sub>RZ</sub>:

$$
\mathrm { R V R } = \frac { N _ { \mathrm { R V R } } } { N _ { \mathrm { t o t a l } } } ,\tag{27}
$$

where $N _ { \mathrm { R V R } }$ is the number of such violations.

• Energy consumption rate (ECR): This metric quantifies the average ratio of energy consumed by the DCU relative to the total energy:

$$
\mathrm { E C R } = \frac { \sum _ { i = 1 } ^ { N _ { \mathrm { t e s t } } } E _ { \mathrm { E C R } , i } } { \sum _ { i = 1 } ^ { N _ { \mathrm { t e s t } } } E _ { \mathrm { t o t a l } , i } } ,\tag{28}
$$

where $E _ { \mathrm { E C R } , i }$ is the consumed energy and $E _ { \mathrm { t o t a l } , i }$ is the total available energy in the i-th task.

## 6.3 Experiment Results

In this section, we present a comparative analysis between the proposed algorithm and several baseline methods in terms of the DCU flight trajectories and the evaluation metrics mentioned above. The parameter settings of these baselines are introduced in Section 6.1.2. The baselines are as follows:

• Heuristic method: A greedy-based policy<sup>1</sup> is used to determine the actions of the DCU for data acquisition and obstacle avoidance. If a static obstacle such as <sup>R</sup><sub>NFZ</sub> or <sup>R</sup><sub>BZ</sub> is encountered, the DCU performs detouring maneuvers. For dynamic obstacles like OUs, it either hovers in place or retreats to avoid collision until the OU moves away. To limit the noise impact when flying over <sup>R</sup><sub>RZ</sub>, the DCU must reduce its speed below $v _ { \mathrm { l i m i t } }$ in accordance with regulatory requirements [7]. Furthermore, if the remaining energy is only sufficient for returning to <sup>LA</sup>, the DCU will immediately head back.

• LLM: An LLM, DeepSeek-R1, is used in real-time to decide the actions of the DCU. We provide the LLM with the state information within a 20 m radius around the DCU, as well as the positions and remaining data of GEs. In addition, we also provide the LLM with $E _ { \mathrm { l i m i t } }$ of the DCU.

• SAC+Heuristic: Similar to SAC+LLM, this variant employs the heuristic rule-based policy for obstacle avoidance instead of using the LLM. Specifically, when the DCU encounters potential collisions with OUs or static obstacles such as $\mathbb { R } _ { \mathrm { N F Z } }$ or $\mathbb { R } _ { \mathrm { B Z } }$ , the heuristic controller overrides the SAC policy to execute avoidance or speedreduction maneuvers according to predefined rules. This baseline serves to evaluate the effectiveness of integrating domain-specific expert knowledge into the SAC framework.

• SAC+LLM (Fixed-f p): SAC is used during training, with a certain probability $( f p \in \{ 0 . 3 , 0 . 4 , 0 . 5 , 1 . 0 \} )$ of delegating action selection to the LLM instead of the policy network. The LLM used here is the same as the one employed in the proposed algorithm, i.e., DeepSeek-R1.

• SAC: A pure deep reinforcement learning approach using the SAC without LLM integration<sup>2</sup>, which also implements PPO and DDPG, all available within the same repository.

• PPO: A representative on-policy reinforcement learning method, implemented within the same codebase as SAC, following the same architecture and parameterization.

![](images/3f4fca348acbf09e2f54f90aa94f2e1a7fcef51820593f00826710f310e9fdc4.jpg)  
Fig. 4: Training reward curves of the proposed algorithm and all baseline methods over 4000 episodes, including SAC, PPO, DDPG, CPO, Theile et al. [54], Wang et al. [55], SAC+Heuristic, and SAC+LLM variants with different invocation probabilities.

• DDPG: A classic off-policy actor-critic method designed for continuous control, also implemented within the SAC codebase, ensuring consistency in experimental setup.

• CPO: A constrained reinforcement learning baseline based on safety-starter-agents from OpenAI<sup>3</sup>. It optimizes the expected cumulative reward while enforcing a safety constraint on the discounted cumulative cost. In our implementation, the instantaneous cost c<sub>t</sub> is defined as a weighted combination of safety violations, including boundary collisions, OUs collisions, tall buildings collisions, and entries into NFZs. The threshold d is set to 0.05, corresponding to an acceptable violation rate of 5%. The policy and value networks follow the same architecture as SAC, and the trust-region constraint on policy update is enforced with a maximum KL divergence of 0.01.

• Existing methods: We also include two recent RL approaches [54], [55] for comparison to benchmark against state-of-the-art path planning and cooperative UAV control methods<sup>45</sup>.

## 6.3.1 Training Reward Curves about DRL Baselines and Our Algorithm

We show the training reward curves of all DRL baselines and the proposed algorithm, as illustrated in Fig. 4. Over 4000 training episodes, the proposed method achieves the highest and most stable cumulative rewards, indicating superior learning efficiency and policy quality. SAC and PPO converge well, with PPO showing slightly slower improvement, while DDPG reaches a lower reward plateau under complex constraints. The CPO algorithm exhibits stable but lower convergence due to its conservative optimization. Theile et al. [54] achieves faster and more stable convergence through equivariant ensemble regularization, whereas Wang et al. [55] converges slowly with lower final rewards. The SAC+Heuristic method shows early stability but limited long-term performance. Overall, the proposed hybrid LLM-augmented DRL algorithm achieves the best trade-off among efficiency, stability, and safety, outperforming both traditional and enhanced baselines.

## 6.3.2 Metrics about Baselines and Our Algorithm

The experimental results in Figs. 5–10 evaluate five core metrics (DCR, CR, SLR, RVR, and ECR) under varying numbers of OUs, GEs, NFZs, BZs, and RZs, verifying how our algorithm satisfies the requirements of robust obstacle avoidance (R2), compliance (R3), and economy (R4) while addressing Challenges 1–3.

Fig. 5 shows the performance under increasing OUs. Our method consistently achieves the highest DCR and the lowest CR and ECR, confirming its robustness and energy efficiency in dynamic environments. SAC and PPO converge well but suffer from rising CR, while SAC+LLM becomes unstable with CR exceeding 90%. DDPG performs moderately, and the standalone LLM and heuristic methods remain conservative with limited DCR. Among new baselines, CPO achieves slightly lower DCR but lower CR than PPO, Theile et al. [54], and Wang et al. [55] perform between SAC and PPO, and SAC+Heuristic outperforms the heuristic baseline with better safety and efficiency.

Fig. 6 presents the results under increasing GEs. Our algorithm maintains DCR ≈ 1.0 and SLR ≈ 1.0, showing excellent reliability. SAC, PPO, and DDPG exhibit moderate declines in DCR and SLR as complexity rises. SAC+LLM collapses under high complexity, while CPO reduces CR at the cost of minor DCR loss. Theile et al. [54] and Wang et al. [55] remain close to PPO, and SAC+Heuristic balances performance and safety better than the rule-based baseline. These results demonstrate the superior adaptability of our method to complex mission scenarios.

Figs. 7 and 8 examine static obstacle cases (NFZs and BZs). Our approach maintains DCR ≈ 1.0 and CR ≈ 0, achieving the best obstacle avoidance and lowest ECR. SAC and PPO perform well but show rising CR with denser obstacles, while CPO achieves slightly lower DCR yet improved safety. Theile et al. [54] and Wang et al. [55] remain moderate, and SAC+Heuristic improves both DCR and CR over the heuristic baseline. These confirm the algorithm’s effectiveness in static, constrained environments (Challenges 1–2).

Fig. 9 evaluates compliance under increasing RZs. Our method sustains the highest DCR with minimal CR and RVR, indicating excellent trade-offs between efficiency and regulatory adherence. SAC+LLM achieves high DCR but violates more frequently, while SAC, PPO, and DDPG show moderate compliance. CPO further lowers violations, Theile et al. [54] and Wang et al. [55] stay between SAC and PPO, and SAC+Heuristic enhances both safety and DCR compared to heuristic control. Overall, our algorithm uniquely balances safety, compliance, and efficiency under soft constraints (Challenge 3).

The radar chart in Fig. 10 clearly demonstrates the superior performance of our proposed algorithm across all five metrics. It achieves high DCR and low ECR, indicating effective data collection and energy-efficient mission completion (R4). Simultaneously, it maintains high SLR and low CR and RVR, ensuring both obstacle avoidance and regulatory compliance, critical for safe operation in urban, airspacereused environments (R2 and R3).

Heuristic LLM SAC+LLM (0.3) SAC DDPG PPO Ours  
Heuristic ITLLM SAC+LLM (0.3) SACDDPG PPO CPO Theile et al. →Wang et al. SAC+Heuristic Ours  
![](images/537caeef28bb7616b1d0eb5b960233ac78aab4c160c0abc5b5f984b0f44bce5f.jpg)

![](images/4fc74385c6485e553cd28a4126dad83dc2ac13aa9b4350b0571e8d9e63d9dc1d.jpg)

![](images/29f8b195b0cf3781065de485d5bba2d15ba74e446ef635f41346261caaca279a.jpg)

Fig. 5: The DCR, CR, and ECR about baselines and our algorithm when $N _ { \mathrm { O U } }$ increases. The proposed algorithm consistentl achieves the highest DCR with almost zero CR and lowest ECR, demonstrating superior efficiency and safety.  
![](images/80c7398d028fd94601ba32db0d6d71c4fa918a0d2e770c6c9c6ed94f22f8a7a9.jpg)

![](images/ce5bc403d21c9b67ab5a7187d106072fa622995858db61733f5f62a8681bead6.jpg)

![](images/6df8ba9c9abfce1be6d0d1823ae2c3dac19ee749d73ef639c663e8f6dcc29467.jpg)

Fig. 6: The DCR, CR, and SLR about baselines and our algorithm when $N _ { \mathrm { G E } }$ increases. Our algorithm maintains a stable and high DCR and CR of almost zero, while other baselines show declining performance and increased collisions. This highlights our algorithm’s robustness in complex environments.  
![](images/b52409c28162f023b7672e06c1f6de98a0d11a7463cd730f3cf9aec386237067.jpg)

![](images/98fe2455b147a30e3ff84da8625eac8ed5809a5e72c068f474b3465cedd85a41.jpg)

![](images/b17633d3edccf5b44b413484cd5f2b620dfefda43e5e37c3f74f89de885d3704.jpg)  
Fig. 7: The DCR, CR, and ECR about baselines and our algorithm when $N _ { \mathrm { { N F Z } } }$ increases. While other algorithms suffer from reduced data collection or increased collisions, our algorithm sustains DCR approaching 1.0 and near-zero CR, with lower energy consumption.

In summary, the results validate that our algorithm, by selectively engaging the LLM for obstacle avoidance, empowers the DCU to make informed and adaptive decisions in complex, dynamic environments. This targeted integration enables our algorithm to uniquely balance the three core demands of the low-altitude economy: R2, R3, and R4. By meeting these requirements, our algorithm effectively addresses the corresponding Challenges 1–3. No other baseline achieves comparable comprehensive performance across these dimensions. Thus, our algorithm stands out as a practical solution for urban low-altitude data collection trajectory planning scenarios.

![](images/7066a2dc7ba3df99d5bbc7abdc6da953b5684474f80467cd2434799295484a9a.jpg)

Fig. 8: The DCR, CR, and ECR about baselines and our algorithm when $N _ { \mathrm { B Z } }$ increases. The proposed algorithm preserves a high DCR and almost avoids collisions entirely, while other baselines experience noticeable performance degradation.  
![](images/4edefbd43d34c2721766b8da032ce0548a15ef9eef542cf3eed3c6d8faadca9e.jpg)  
Fig. 9: The DCR, CR, and RVR about baselines and our algorithm when $N _ { \mathrm { R Z } }$ increases. Our algorithm maintains full compliance (RVR 0), with high data collection efficiency and no collisions, while other baselines fail to adapt to regulatory constraints.

![](images/64cb6857334b383f636ebb56cd5546e1c7eaf614e59f957a05931aa1849ff98d.jpg)  
Fig. 10: Average performance summary across all environmental configurations. Our algorithm achieves the highest DCR (99.49%), lowest CR (0%), and strong compliance (RVR 0% and ECR 76.95%), validating its overall effectiveness across diverse low-altitude scenarios.

## 6.3.3 Parameters Sensitive Analysis

To comprehensively evaluate the robustness and generalization capability of the proposed algorithm, we conduct a series of sensitivity analyses covering four aspects: (1) hyperparameters of the training process, (2) weight coefficients of the reward function, (3) the invocation threshold distance for triggering the LLM-based decision process, and (4) the reasoning objectives embedded in the LLM prompt. The detailed analyses and corresponding results are presented as follows.

As shown in Fig. 11, variations in the actor and critic learning rates and batch size cause only minor fluctuations in performance. DCR and SLR stay close to 1.0, while CR and RVR remain nearly zero, indicating stable learning and strong safety. ECR varies slightly within [0.76, 0.78], showing consistent energy efficiency. Overall, the proposed model exhibits high robustness to hyperparameter changes.

To evaluate the impact of reward composition, we vary the weights of $r _ { 1 } , \ r _ { 2 } , \ r _ { 5 } ,$ , and $r _ { 8 } ,$ which correspond to task efficiency, obstacle avoidance, compliance, and energy return, respectively. As shown in Fig. 12, increasing r<sub>1</sub> enhances DCR and SLR but slightly raises ECR and CR, while higher $r _ { 2 }$ effectively lowers CR at a small cost of DCR. Increasing $r _ { 5 }$ improves compliance (lower RVR) but slightly reduces efficiency, and larger $r _ { 8 }$ values yield better energy use and landing stability with a minor DCR drop. Overall, the proposed algorithm remains stable and well-balanced under moderate reward weight variations.

DCR ECR SLR CR RVR  
![](images/0f4e08704851cbd3092bf0057384b7741906c53bc51bad094001414945e70544.jpg)

![](images/cad2cc44b311dbd5a7a175904b98ab4069877a34046cb7331e0a86499bb3d78a.jpg)

![](images/3a6588ec19f36f8197b13be1c112f8546c4f60df3933cfa8b29c69fdbe0b51f7.jpg)

Fig. 11: Variations of DCR, CR, ECR, SLR, and RVR under different hyperparameter settings of (a) actor LR, (b) critic LR, and (c) batch size.  
![](images/7d4389df40fb61bfa07afbf47febd4d2296d6d87647c4403d36c99afdf185d11.jpg)

![](images/861a3d1418cbbbb8c161f2487bce9012526688f952907f9f71369395796f361d.jpg)

![](images/347768ffb631c45cbc8e30014aa771476468487de69a90bc7927e8013963682b.jpg)  
DCR ECR SLR IT CR IRVR

![](images/06f32c6e111a5f214393bcc47c7b853698ec5b687f5cf2c0e31d016e7e587e3f.jpg)

Fig. 12: Variations of DCR, CR, ECR, SLR, and RVR under different reward weight settings for $r _ { 1 } , r _ { 2 } , r _ { 5 } ,$ and $r _ { 8 } .$  
![](images/c427cc0fe56d50a9b63d9b237b424cd1bd134e3863c07497091eb60bca32b3f1.jpg)  
Fig. 13: Sensitivity analysis of the LLM invocation threshold the threshold. The figure shows the impact of varying $d _ { \mathrm { t h } } \in \{ 5 , 1 0 , 1 5 , 2 0 , 2 5 \}$ m on five key performance metrics (DCR, CR, ECR, SLR, and RVR). Excessively small thresholds (e.g., 5 m) cause delayed LLM activation, leading to higher collision rates and lower DCR, while overly large thresholds (e.g., 25 m) result in frequent LLM invocations and increased energy consumption. The threshold of 15 m achieves the best trade-off between safety, efficiency, and energy consumption, validating the choice used in the main experiments.

As shown in Fig. 13, the variation of the LLM invocation threshold exhibits a clear trade-off among safety, efficiency, and energy consumption. When the threshold is too small (e.g., 5 m), the LLM is triggered too late, leading to occasional collisions and reduced data collection efficiency.

![](images/d5bbf7f7029f48107fc5dfc3f42a3ab4d00793203dbf123248745a27c89d4ffb.jpg)  
Fig. 14: Ablation on reasoning objectives embedded in the LLM prompt. Bars compare the Complete Prompt with four variants that remove one objective at a time (without Safety, without Compliance, without Data efficiency, without Energy efficiency) across five metrics (DCR, CR, ECR, SLR, RVR).

Conversely, excessively large thresholds (e.g., 25 m) cause premature or frequent invocations, increasing energy consumption and slightly reducing stability. Moderate thresholds such as 10 m and 20 m achieve similar performance to 15 m, but the latter offers the best balance, maintaining high DCR and SLR with low CR and ECR. Therefore, 15 m is adopted as the default setting in all subsequent experiments.

We ablate the four reasoning objectives in the LLM prompt by removing one component at a time and compare against the complete prompt shown in Fig. 3. The result is shown in Fig. 14. Removing Safety increases CR and slightly reduces DCR, confirming its primary role in risk control. Removing Compliance markedly degrades RVR despite similar CR, indicating the necessity of explicit compliance guidance. Removing Data efficiency lowers DCR and slightly changes ECR, showing that prioritizing informative targets contributes to sustained task completion. Removing Energy efficiency harms energy behavior and landing stability, demonstrating that explicit energy-aware reasoning helps maintain safe mission termination. Overall, the complete prompt provides the best balance across safety, compliance, and efficiency.

In summary, all sensitivity analyses consistently demonstrate the robustness and adaptability of the proposed algorithm under diverse parameter and configuration settings. Neither hyperparameter tuning nor moderate reward reweighting leads to noticeable performance degradation, and both the LLM invocation threshold and reasoning objectives exhibit stable behavior with interpretable effects. These results collectively validate that the proposed hybrid SAC–LLM algorithm maintains a well-balanced trade-off among safety, compliance, efficiency, and energy performance, even when the underlying parameters or decision conditions vary across different environments.

## 7 CONCLUSION

This paper has developed a hybrid unmanned aerial vehicle (UAV) trajectory planning algorithm that combines deep reinforcement learning with large language model reasoning for low-altitude data collection in complex urban environments. The proposed algorithm has jointly considered obstacle avoidance, regulation awareness, and energy efficiency, achieving safe and adaptive decision-making under uncertainty.

Future work will explore extending the algorithm to multi-UAV collaboration and large-scale city scenarios. Another direction is to enhance three-dimensional obstacle avoidance and communication-aware coordination under partial or unstable network conditions. In addition, incorporating more realistic air-to-ground channel models, including probabilistic line-of-sight and non-line-of-sight propagation in urban environments, will help capture complex communication dynamics. Furthermore, integrating real sensor noise, multimodal perception, and dynamic regulatory feedback will be essential for improving robustness and realworld applicability in low-altitude economy networks.

## REFERENCES

[1] R. Zhang, J. He, X. Luo, D. Niyato, J. Kang, Z. Xiong, Y. Li, and B. Sikdar, “Toward democratized generative AI in next-generation mobile edge networks,” IEEE Network, early access, 2025, doi: 10.1109/MNET.2025.3541078.

[2] R. Zhang, H. Du, Y. Liu, D. Niyato, J. Kang, Z. Xiong, A. Jamalipour, and D. I. Kim, “Generative AI agents with large language model for satellite networks via a mixture of experts transmission,” IEEE Journal on Selected Areas in Communications, vol. 42, no. 12, pp. 3581–3596, Dec. 2024, doi: 10.1109/JSAC.2024.3459037.

[3] M. Ahmed, A. A. Soofi, F. Khan, S. Raza, W. U. Khan, L. Su, F. Xu, and Z. Han, “Toward a sustainable low-altitude economy: A survey of energy-efficient RIS-UAV networks,” arXiv preprint, arXiv:2504.02162, Apr. 2025. [Online]. Available: https://arxiv. org/abs/2504.02162.

[4] R. Zhang, K. Xiong, Y. Lu, P. Fan, D. W. K. Ng, and K. B. Letaief, “Energy efficiency maximization in RIS-assisted SWIPT networks with RSMA: A PPO-based approach,” IEEE Journal on Selected Areas in Communications, vol. 41, no. 5, pp. 1413–1430, May 2023, doi: 10.1109/JSAC.2023.3240707.

[5] R. Zhang et al., “Generative AI for Space-Air-Ground Integrated Networks,” IEEE Wireless Communications, vol. 31, no. 6, pp. 10– 20, Dec. 2024, doi: 10.1109/MWC.016.2300547.

[6] N. Zhang, M. Zhang, and K. H. Low, “3D trajectory planning and real-time collision resolution of multirotor drone operations in complex urban low-altitude airspace,” Transportation Research Part C: Emerging Technologies, vol. 129, p. 103123, 2021, doi: 10.1016/j.trc.2021.103123.

[7] H. J. Hadi, Y. Cao, K. U. Nisa, Y. Mekdad, A. Aris, L. Babun, A. E. Fergougui, M. Conti, R. Lazzeretti, and A. S. Uluagac, “A comprehensive survey on security, privacy issues and emerging defence technologies for UAVs,” Journal of Network and Computer Applications, vol. 213, p. 103607, 2023, doi: 10.1016/j.jnca.2023.103607.

[8] X. Qin, Z. Song, T. Hou, W. Yu, J. Wang, and X. Sun, “Joint optimization of resource allocation, phase shift, and UAV trajectory for energy-efficient RIS-assisted UAV-enabled MEC systems,” IEEE Transactions on Green Communications and Networking, vol. 7, no. 4, pp. 1778–1792, Dec. 2023, doi: 10.1109/TGCN.2023.3287604.

[9] H. Pan, Y. Liu, G. Sun, J. Fan, S. Liang, and C. Yuen, “Joint power and 3D trajectory optimization for UAV-enabled wireless powered communication networks with obstacles,” IEEE Transactions on Communications, vol. 71, no. 4, pp. 2364–2380, Apr. 2023, doi: 10.1109/TCOMM.2023.3240697.

[10] F. Pervez, A. Sultana, C. Yang, and L. Zhao, “Energy and latency efficient joint communication and computation optimization in a multi-UAV-assisted MEC network,” IEEE Transactions on Wireless Communications, vol. 23, no. 3, pp. 1728–1741, Mar. 2024, doi: 10.1109/TWC.2023.3291692.

[11] Y. Zhang, Y. Huang, C. Huang, H. Huang, and A.-T. Nguyen, “Joint optimization of deployment and flight planning of multi-UAVs for long-distance data collection from large-scale IoT devices,” IEEE Internet of Things Journal, vol. 11, no. 1, pp. 791–804, Jan. 2024, doi: 10.1109/JIOT.2023.3285942.

[12] K. Heo, G. Park, and K. Lee, “Joint optimization of UAV trajectory and communication resources with complete avoidance of no-fly-zones,” IEEE Transactions on Intelligent Transportation Systems, vol. 25, no. 10, pp. 14259–14265, Oct. 2024, doi: 10.1109/TITS.2024.3403887.

[13] J. Li, G. Sun, L. Duan, and Q. Wu, “Multi-objective optimization for UAV swarm-assisted IoT with virtual antenna arrays,” IEEE Transactions on Mobile Computing, vol. 23, no. 5, pp. 4890–4907, May 2024, doi: 10.1109/TMC.2023.3298888.

[14] Z. Fu, J. Liu, Y. Mao, L. Q. Qu, L. F. Xie, and X. Wang, “Energyefficient UAV-assisted federated learning: Trajectory optimization, device scheduling, and resource management,” IEEE Transactions on Network and Service Management, vol. 22, no. 2, pp. 974–988, Jun. 2025, doi: 10.1109/TNSM.2025.3531237.

[15] Z. Wang, J. Wen, J. He, L. Yu, and Z. Li, “Energy efficiency optimization of RIS-assisted UAV search-based cognitive communication in complex obstacle avoidance environments,” IEEE Transactions on Cognitive Communications and Networking, early access, Feb. 2025, doi: 10.1109/TCCN.2025.3544267.

[16] S. Silvirianti, B. N. Narottama, and S. Y. Shin, “Layerwise quantum deep reinforcement learning for joint optimization of UAV trajectory and resource allocation,” IEEE Internet of Things Journal, vol. 11, no. 1, pp. 430–443, Jan. 2024, doi: 10.1109/JIOT.2023.3285968.

[17] Y. Chen, Y. Yang, Y. Wu, J. Huang, and L. Zhao, “Joint trajectory optimization and resource allocation in UAV-MEC systems: A Lyapunov-assisted DRL approach,” IEEE Transactions on Services Computing, early access, Feb. 2025, doi: 10.1109/TSC.2025.3544124.

[18] Z. Ning, Y. Yang, X. Wang, Q. Song, L. Guo, and A. Jamalipour, “Multi-agent deep reinforcement learning based UAV trajectory optimization for differentiated services,” IEEE Transactions on Mobile Computing, vol. 23, no. 5, pp. 5818–5834, May 2024, doi: 10.1109/TMC.2023.3312276.

[19] F. Song, M. Deng, H. Xing, Y. Liu, F. Ye, and Z. Xiao, “Energyefficient trajectory optimization with wireless charging in UAVassisted MEC based on multi-objective reinforcement learning,” IEEE Transactions on Mobile Computing, vol. 23, no. 12, pp. 10867– 10884, Dec. 2024, doi: 10.1109/TMC.2024.3384405.

[20] R. Ding, F. Zhou, Q. Wu, and D. W. K. Ng, “From external interaction to internal inference: An intelligent learning framework for spectrum sharing and UAV trajectory optimization,” IEEE Transactions on Wireless Communications, vol. 23, no. 9, pp. 12099– 12114, Sept. 2024, doi: 10.1109/TWC.2024.3387980.

[21] T. Wang, W. Du, C. Jiang, Y. Li, and H. Zhang, “Safety constrained trajectory optimization for completion time minimization for UAV

communications,” IEEE Internet of Things Journal, vol. 11, no. 21, pp. 34482–34491, Nov. 2024, doi: 10.1109/JIOT.2024.3355906.

[22] H. He, W. Yuan, S. Chen, X. Jiang, F. Yang, and J. Yang, “Deep reinforcement learning-based distributed 3D UAV trajectory design,” IEEE Transactions on Communications, vol. 72, no. 6, pp. 3736–3751, Jun. 2024, doi: 10.1109/TCOMM.2024.3361534.

[23] Z. Liu, J. Zhang, Y. Zeng, and B. Ai, “Energy-efficient multi-agent reinforcement learning for UAV trajectory optimization in cell-free massive MIMO networks,” IEEE Transactions on Wireless Communications, early access, Mar. 2025, doi: 10.1109/TWC.2025.3550266.

[24] Z. Ning, H. Ji, X. Wang, E. C. H. Ngai, L. Guo, and J. Liu, “Joint optimization of data acquisition and trajectory planning for UAVassisted wireless powered Internet of Things,” IEEE Transactions on Mobile Computing, vol. 24, no. 2, pp. 1016–1030, Feb. 2025, doi: 10.1109/TMC.2024.3470831.

[25] S. Zhu, B. Zhu, K. Chi, K. Yu, and S. Mumtaz, “Long-Term Computation Rate Maximization in UAV-Enabled Wirelessly Powered MEC,” IEEE Transactions on Communications, vol. 73, no. 11, pp. 12545–12560, Nov. 2025, doi: 10.1109/TCOMM.2025.3578838.

[26] J. Zhong, M. Li, Y. Chen, Z. Wei, F. Yang, and H. Shen, “A safer vision-based autonomous planning system for quadrotor UAVs with dynamic obstacle trajectory prediction and its application with LLMs,” in Proc. IEEE/CVF Winter Conference on Applications of Computer Vision Workshops (WACV Workshops), 2024, pp. 920–929.

[27] A. Phadke, A. Hadimlioglu, T. Chu, and C. N. Sekharan, “Integrating large language models for UAV control in simulated environments: A modular interaction approach,” arXiv preprint, arXiv:2410.17602, 2024. [Online]. Available: https://arxiv.org/ abs/2410.17602.

[28] J. Xiao, C. Tsao, Y. Zhang, and M. Feroskhan, “FM-Planner: Foundation model guided trajectory planning for autonomous drone navigation,” arXiv preprint, arXiv:2505.20783, 2025. [Online]. Available: https://arxiv.org/abs/2505.20783.

[29] H. Samma and S. El-Ferik, “UAV visual trajectory planning using large language models,” Transportation Research Procedia, vol. 84, pp. 339–345, 2025, doi: 10.1016/j.trpro.2025.03.081.

[30] S. Cai, Y. Wu, and L. Zhou, “LLM-Land: Large language models for context-aware drone landing,” arXiv preprint, arXiv:2505.06399, 2025. [Online]. Available: https://arxiv.org/abs/2505.06399.

[31] H. Li, M. Xiao, K. Wang, D. I. Kim, and M. Debbah, “Large Language Model Based Multi-Objective Optimization for Integrated Sensing and Communications in UAV Networks,” IEEE Wireless Communications Letters, vol. 14, no. 4, pp. 979–983, 2025, doi: 10.1109/LWC.2025.3529082.

[32] Y. Emami, H. Zhou, S. Nabavirazavi, and L. Almeida, “LLM-Enabled In-Context Learning for Data Collection Scheduling in UAV-Assisted Sensor Networks,” IEEE Internet of Things Journal, vol. 12, no. 23, pp. 51664–51676, 2025, doi: 10.1109/JIOT.2025.3615410.

[33] P. Li, Z. An, S. Abrar, and L. Zhou, “Large language models for multi-robot systems: a survey,” arXiv preprint, arXiv:2502.03814, Feb. 2025. [Online]. Available: https://arxiv.org/abs/2502.03814.

[34] P. Razzaghi et al., “A survey on reinforcement learning in aviation applications,” Engineering Applications of Artificial Intelligence, vol. 115, pp. 1–18, Aug. 2023.

[35] Y. Wang, Z. Wei, H. Wu, and Z. Feng, “Toward Realization of Low-Altitude Economy Networks: Core Architecture, Integrated Technologies, and Future Directions,” arXiv preprint, arXiv:2504.21583, Apr. 2025. [Online]. Available: https://arxiv.org/abs/2504.21583.

[36] Z. Wei et al., “UAV-assisted data collection for Internet of Things: A survey,” IEEE Internet of Things Journal, vol. 9, no. 17, pp. 15460– 15483, Sept. 2022, doi: 10.1109/JIOT.2022.3182483.

[37] D. D. Falconer, F. Adachi, and B. Gudmundson, “Time division multiple access methods for wireless personal communications,” IEEE Communications Magazine, vol. 33, no. 1, pp. 50–57, Jan. 1995.

[38] Y. Li, “Deep reinforcement learning: An overview,” arXiv preprint, arXiv:1701.07274, Jan. 2017. [Online]. Available: https://arxiv.org/ abs/1701.07274.

[39] X. Tang, Y. Wang, Q. Huang, Y. Li, and C. Wang, “Highway decision-making and motion planning for autonomous driving via soft actor-critic,” IEEE Transactions on Vehicular Technology, vol. 71, no. 5, pp. 4706–4717, May 2022, doi: 10.1109/TVT.2022.3151651.

[40] Q. Zhang et al., “Data-Aided Doppler Frequency Shift Estimation and Compensation for UAVs,” IEEE Internet of Things Journal, vol. 7, no. 1, pp. 400–415, Jan. 2020, doi: 10.1109/JIOT.2019.2943608.

[41] H.-T. Ye, X. Kang, J. Joung, and Y.-C. Liang, “Optimization for Full-Duplex Rotary-Wing UAV-Enabled Wireless-Powered IoT Net-

works,” IEEE Transactions on Wireless Communications, vol. 19, no. 7, pp. 5057–5072, Jul. 2020, doi: 10.1109/TWC.2020.2989302.

[42] C. Wen, L. Qiu, and X. Liang, “Securing UAV communication with mobile UAV eavesdroppers: Joint trajectory and communication design,” in Proc. IEEE Wireless Communications and Networking Conference (WCNC), 2021, pp. 1–6, doi: 10.1109/WCNC49053.2021.9417318.

[43] X. Wang, M. C. Gursoy, T. Erpek, and Y. E. Sagduyu, “Collision-aware UAV trajectories for data collection via reinforcement learning,” in Proc. IEEE Global Communications Conference (GLOBECOM), 2021, pp. 1–6, doi: 10.1109/GLOBE-COM46510.2021.9686015.

[44] S. Rahim, L. Peng, and P.-H. Ho, “TinyFDRL-Enhanced Energy-Efficient Trajectory Design for Integrated Space-Air-Ground Networks,” IEEE Internet of Things Journal, pp. 1–1, 2024, doi: 10.1109/JIOT.2024.3361394.

[45] Y. Zeng, J. Xu, and R. Zhang, “Energy Minimization for Wireless Communication With Rotary-Wing UAV,” IEEE Transactions on Wireless Communications, vol. 18, no. 4, pp. 2329–2345, Apr. 2019, doi: 10.1109/TWC.2019.2902559.

[46] D. Chen and W. Hua, “Hierarchical VAE Based Semantic Communications for POMDP Tasks,” in Proc. IEEE Int. Conf. Acoust., Speech Signal Process. (ICASSP), Apr. 2024, pp. 5540–5544, doi: 10.1109/ICASSP48485.2024.10445833.

[47] DeepSeek, “DeepSeek: Large Language Models and Multimodal Intelligence,” [Online]. Available: https://www.deepseek.com/. [Accessed: May 27, 2025].

[48] X. Wang, M. C. Gursoy, T. Erpek, and Y. E. Sagduyu, “Learning-Based UAV Trajectory planning for Data Collection With Integrated Collision Avoidance,” IEEE Internet of Things Journal, vol. 9, no. 17, pp. 16663–16676, Sep. 2022, doi: 10.1109/JIOT.2022.3153585.

[49] J. Fan et al., “Energy-constrained safe trajectory planning for UAVassisted data collection of mobile IoT devices,” IEEE Internet of Things Journal, vol. 11, no. 24, pp. 39971–39983, Dec. 2024, doi: 10.1109/JIOT.2024.3448537.

[50] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, “Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor,” in Proc. 35th Int. Conf. Mach. Learn. (ICML), Stockholm, Sweden, 2018, pp. 1861–1870.

[51] J. Kaplan et al., “Scaling Laws for Neural Language Models,” arXiv preprint, arXiv:2001.08361, 2020. [Online]. Available: https://arxiv. org/abs/2001.08361.

[52] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal Policy Optimization Algorithms,” arXiv preprint, arXiv:1707.06347, Jul. 2017. [Online]. Available: https://arxiv.org/ abs/1707.06347.

[53] T. Lillicrap et al., “Continuous control with deep reinforcement learning,” arXiv preprint, arXiv:1509.02971, Sep. 2015. [Online]. Available: https://arxiv.org/abs/1509.02971.

[54] M. Theile, H. Cao, M. Caccamo, and A. L. Sangiovanni-Vincentelli, “Equivariant ensembles and regularization for reinforcement learning in map-based path planning,” in Proc. IEEE/RSJ Int. Conf. Intell. Robots Syst. (IROS), Oct. 2024, pp. 14164–14171.

[55] H. Wang, C. H. Liu, H. Yang, G. Wang, and K. K. Leung, “Ensuring threshold AoI for UAV-assisted mobile crowdsensing by multiagent deep reinforcement learning with transformer,” IEEE/ACM Trans. Netw., vol. 32, no. 1, pp. 566–581, 2023.

[56] J. Achiam, D. Held, A. Tamar, and P. Abbeel, “Constrained policy optimization,” in Proc. Int. Conf. Mach. Learn. (ICML), Sydney, Australia, Jul. 2017, pp. 22–31.