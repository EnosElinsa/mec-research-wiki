# Task Assignment and Exploration Optimization for Low Altitude UAV Rescue via Generative AI Enhanced Multi-Agent Reinforcement Learning

Xin Tang , Qian Chen , Wenjie Weng, Chao Jin, Zhang Liu , Jiacheng Wang , Geng Sun , Senior Member, IEEE, Xiaohuan Li , Member, IEEE, and Dusit Niyato , Fellow, IEEE

Abstract—The integration of emerging uncrewed aerial vehicle (UAV) with artificial intelligence (AI) and ground-embedded robots (GERs) has transformed emergency rescue operations in unknown environments. However, the high computational demands of such missions often exceed the capacity of a single UAV, making it difficult for the system to continuously and stably provide high-level services. To address these challenges, this paper proposes a novel cooperation framework involving UAVs, GERs, and airships. This framework enables resource pooling through UAV-to-GER (U2G) and UAV-to-airship (U2A) communications, providing computing

Received 16 April 2025; revised 16 July 2025; accepted 25 July 2025. Date of publication 31 July 2025; date of current version 3 December 2025. This work was supported in part by the Guangxi Natural Science Foundation of China under Grant 2025GXNSFAA069687, in part by the National Natural Science Foundation of China under Grant U22A2054, in part by the National Research Foundation, Singapore and Infocomm Media Development Authority under its Future Communications Research & Development Programme under Grant FCP-NTU-RG-2022-010 and under Grant FCP-ASTAR-TG-2022-003, in part by the Singapore Ministry of Education (MOE) Tier 1 under Grant RG87/22 and RG24/24, in part by the NTU Centre for Computational Technologies in Finance (NTU-CCTF), in part by the RIE2025 Industry Alignment Fund - Industry Collaboration Projects (IAF-ICP) under Grant Award I2301E0026, in part by the administered by A\*STAR, and in part by the Graduate Study Abroad Program of GUET under Grant GDYX2024001. Recommended for acceptance by Z. Sun. (Corresponding author: Xiaohuan Li.)

Qian Chen is with the School of Architecture and Transportation Engineering, Guilin University of Electronic Technology (GUET), Guilin 541004, China (e-mail: chenqian@mails.guet.edu.cn).

Wenjie Weng, Chao Jin, and Xiaohuan Li are with the Guangxi University Key Laboratory of Intelligent Networking and Scenario System, School of Information and Communication, Guilin University of Electronic Technology, Guilin 541004, China, and also with the National Engineering Laboratory for Comprehensive Transportation Big Data Application Technology (Guangxi), Nanning 530001, China (e-mail: wwjdzsyx@163.com; kingchao2025@163.com; lxhguet@guet.edu.cn).

Zhang Liu is with the Department of Informatics and Communication Engineering, Xiamen University, Fujian 361102, China (e-mail: zhangliu@stu.xmu.edu.cn).

Jiacheng Wang and Dusit Niyato are with the College of Computing and Data Science, Nanyang Technological University, Singapore 639798 (e-mail: jiacheng.wang@ntu.edu.sg; dniyato@ntu.edu.sg).

Geng Sun is with the College of Computer Science and Technology, Jilin University, Changchun 130012, China, and also with the Key Laboratory of Symbolic Computation and Knowledge Engineering of Ministry of Education, Jilin University, Changchun 130012, China (e-mail: sungeng@jlu.edu.cn).

Digital Object Identifier 10.1109/TMC.2025.3594188

services for UAV offloaded tasks. Specifically, we formulate the multi-objective optimization problem of task assignment and exploration optimization in UAVs as a dynamic long-term optimization problem. Our objective is to minimize task completion time and energy consumption while ensuring system stability over time. To achieve this, we first employ the Lyapunov optimization method to transform the original problem, with stability constraints, into a per-slot deterministic problem. We then propose an algorithm named HG-MADDPG, which combines the Hungarian algorithm with a generative diffusion model (GDM)-based multi-agent deep deterministic policy gradient (MADDPG) approach, to jointly optimize exploration and task assignment decisions. In HG-MADDPG, we first introduce the Hungarian algorithm as a method for exploration area selection, enhancing UAV efficiency in interacting with the environment. We then innovatively integrate the GDM and multi-agent deep deterministic policy gradient (MADDPG) to optimize task assignment decisions, such as task offloading and resource allocation. Simulation results demonstrate the effectiveness of the proposed approach, with significant improvements in task offloading efficiency, latency reduction, and system stability compared to baseline methods.

Index Terms—Task assignment, exploration optimization, lowaltitude economy, uncrewed aerial vehicle (UAV), emergency rescue, generative artificial intelligence, multi-agent reinforcement learning.

## I. INTRODUCTION

I <sup>NFORMATION</sup> <sup>collection</sup> <sup>and</sup> <sup>target</sup> <sup>detection</sup> <sup>from</sup> <sup>the</sup> <sup>dis-</sup> able rescue plan [1]. When ground transportation is interrupted by a disaster, it becomes difficult for human rescuers to enter the affected area. The existing method for rescuing in disaster areas involves using either ground vehicles or aerial robots that operate independently to gather data and transmit rescue information back to a ground commander [2], [3]. Furthermore, groundembedded robots (GERs) are used to explore for life forms and for environmental monitoring, while low-altitude uncrewed aerial vehicles (UAVs) play a significant role in post-disaster search and rescue activities. Emerging UAVs, combined with artificial intelligence (AI), have revolutionized the way emergency rescue is handled [4], [5]. The UAVs offer several advantages in emergency rescue and disaster response. First, they can quickly access areas that are otherwise unreachable due to collapsed infrastructure or hazardous conditions, enabling rapid situational assessment. Second, UAVs equipped with high-resolution cameras and sensors can provide real-time aerial imagery and environmental data, greatly enhancing decision-making efficiency for rescue teams. Third, their flexibility in deployment allows for coordinated missions across wide areas, improving coverage and responsiveness. These capabilities make UAVs a valuable asset in time-sensitive and high-risk rescue operations. Despite the advantages of low-altitude UAVs for emergency rescue, there are still substantial challenges that need to be addressed.

Challenge 1: While existing frameworks utilize UAVs for low-altitude operations, they often neglect the heterogeneous capabilities and practical constraints of collaborating computing nodes in dynamic rescue scenarios. The absence of a unified framework that jointly considers task offloading prioritization, obstacle-aware communication reliability, and resource availability limits the adaptability of rescue systems [6]. This motivates the development of a novel cooperation framework that dynamically coordinates multiple nodes while addressing real-world constraints such as intermittent connectivity and heterogeneous computational capacities [7].

Challenge 2: Existing approaches to computation offloading in UAV rescue scenarios fail to holistically optimize latency, energy consumption, and exploration efficiency under timevarying resource availability and environmental obstacles. The interdependencies among task assignment, energy constraints, and obstacle-induced communication disruptions create a complex trade-off space [8]. Moreover, ensuring long-term system stability while minimizing instantaneous task latency remains an open challenge [9]. This necessitates an online optimization method capable of decomposing long-term objectives into realtime decisions while maintaining robustness against dynamic uncertainties.

Challenge 3: Current multi-agent reinforcement learning (MARL)-based solutions for multi-agent coordination often overlook the impact of agent observation limitations and highdimensional state-action spaces on strategy generation. In rescue scenarios, agents operate with partial observations due to obstacles and limited sensing ranges, which lead to suboptimal task assignment and exploration decisions [10]. Furthermore, the curse of dimensionality in multi-agent systems hinders efficient policy learning [11]. These challenges highlight the need for a hybrid approach that combines low-complexity algorithms with AI techniques to reduce observation space complexity and enhance collaborative decision-making under partial observability.

Motivated by these considerations, we propose a novel computing task assignment method for UAVs that leverages a variety of GERs to provide computing offloading service. Given the dynamics of competition and cooperation between UAVs and GERs, we present a stable task assignment algorithm designed to optimally pair each UAV with the GER that best meets their demand and supply. Moreover, we formulate the task assignment and exploration optimization for UAVs as a mixed-integer nonlinear optimization problem. To address this problem, we employ an online algorithm that transforms the long-term optimization problem into a real-time, instantaneous optimization problem using the Lyapunov optimization method. Furthermore, a Hungarian algorithm and generative diffusion model (GDM)-based MARL method are proposed to solve the instantaneous optimization problem. The main contributions of this paper are summarized as follows:

Framework: We propose a novel cooperation framework involving UAVs, GERs, and airships in low-altitude rescue scenarios, where computationally intensive tasks from UAVs can be offloaded to GERs or airships for more efficient execution. Specifically, UAVs prioritize direct assignment of tasks to GERs to minimize latency. An airship is engaged to handle offloaded tasks only when GERs lack sufficient computation resources. Moreover, in scenarios where obstacles obstruct communication between the ground control center and GERs, the UAVs can detect obstacles, facilitating reliable rescue.

Multi-objective optimization (MOO): We jointly optimize the task assignment, energy consumption and the exploration area selection problem for GERs and UAVs to minimize the completion latency of tasks. We employ an online algorithm that addresses the long-term optimization problem by converting the problem into a real-time, instantaneous optimization problem by using the Lyapunov optimization method. This strategy effectively decouples the minimization of long-term task completion time with stability constraints into a deterministic problem for each time slot.

Solution: To address the complex optimization problem described above, this paper models the MOO problem as a markov decision process (MDP) and proposes a method based on the Hungarian algorithm and GDM-based multiagent deep deterministic policy gradient (MADDPG), named HG-MADDPG. Specifically, we introduce a novel application of the Hungarian algorithm for exploration area selection, which reduces the dimensionality of the observation space. The exploration process involves trajectory generation and obstacle detection. Additionally, we integrate the GDM and MADDPG to enhance the generative decision-making capability of the actor network, enabling the optimization of task assignment.

Validation: Extensive experiments are conducted to illustrate the substantial advantages of the proposed approach in comparison to baseline algorithms, including more stable task completion latency, lower energy consumption, and enhanced system stability.

The rest of the paper is organized as follows. The related works are reviewed in section II. In section III, we present the system model and optimization problem. Section IV reformulates the optimization problem. Section V introduces the novel method based on the HG-MADDPG algorithm for task assignment and exploration optimization. Section VI is dedicated to the simulation experiments and their analysis, while section VII provides the concluding remarks.

## II. RELATED WORK

In this section, we review the related work on the framework of UAV rescue systems, MOO of MARL-based UAV computation offloading, and generative artificial intelligence (GAI)-assisted reinforcement learning.

TABLE I  
A - IN THE TABLE INDICATES THAT THE PERFORMANCE METRICS MEET THE SPECIFIED CRITERIA
<table><tr><td rowspan=1 colspan=3>Ref.</td><td rowspan=1 colspan=5>Task assignmentscenario</td><td></td><td rowspan=1 colspan=2>Task latency</td><td rowspan=1 colspan=1>Energyconsumption</td><td rowspan=1 colspan=1>UAVtrajectory</td><td rowspan=1 colspan=1>Task completionrate</td><td rowspan=1 colspan=1>low-altitudeobstacle</td><td rowspan=1 colspan=1>Resourcevisualization</td><td rowspan=1 colspan=1>Stability</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[12]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=5></td><td></td><td rowspan=1 colspan=2>V</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1>[13]</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=2></td><td rowspan=8 colspan=5>GER to UAV</td><td rowspan=2 colspan=1></td><td rowspan=2 colspan=1></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[14]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[15]</td><td rowspan=1 colspan=1></td><td></td><td></td><td rowspan=1 colspan=2>V</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[16]</td><td rowspan=1 colspan=1></td><td></td><td></td><td rowspan=1 colspan=2>一</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[17]</td><td rowspan=1 colspan=1></td><td></td><td></td><td rowspan=1 colspan=2>4</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>_</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[18]</td><td rowspan=1 colspan=1></td><td></td><td></td><td rowspan=1 colspan=2>V</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[19]</td><td rowspan=1 colspan=1></td><td></td><td></td><td rowspan=1 colspan=2>一</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>_</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[20]</td><td rowspan=1 colspan=1></td><td rowspan=3 colspan=5>UAV to UAV</td><td></td><td rowspan=1 colspan=2>V</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>_</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[21]</td><td rowspan=1 colspan=1></td><td></td><td rowspan=1 colspan=2>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[22]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=2 colspan=2></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td rowspan=1 colspan=2>√</td><td rowspan=1 colspan=1>1</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>V</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[23]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=4></td><td rowspan=1 colspan=2></td><td rowspan=1 colspan=2>V</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>_</td></tr><tr><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>24]</td><td rowspan=1 colspan=1></td><td rowspan=2 colspan=5>UAV to GER</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2> $\overline { { \checkmark } }$ </td><td rowspan=1 colspan=1> $\overline { { \checkmark } }$ </td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>_</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[25]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1></td><td></td><td rowspan=1 colspan=2>V</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>一</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>_</td><td rowspan=1 colspan=1>_</td></tr><tr><td rowspan=1 colspan=3>This work</td><td rowspan=1 colspan=5></td><td></td><td rowspan=1 colspan=2>V</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>7</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>V</td><td rowspan=1 colspan=1>L</td></tr></table>

## A. Framework of UAV Rescue Systems

Extensive research has been done on the use of UAVs in emergency networks. Their high mobility, flexible deployment, and strong adaptability make them a key asset in supporting various applications. UAVs, for instance, can serve as aerial base stations, improving the connectivity of ground-based wireless systems. In [26], the authors formulated a mixed-integer nonlinear programming (MINLP) problem to maximize efficiency while optimizing UAV association, transmission power, and UAV location. In [27], the authors explored a UAV-assisted emergency communication system in post-disaster areas. The method mitigates the additional latency associated with long-distance data communication. The authors in [28] focused on maximizing the spatial exploration ratio while minimizing energy consumption and maintaining connectivity in post-disaster operations. The authors in [24] proposed a three-layer computing architecture integrating UAVs, MEC, and vehicle fog computing, along with a joint optimization problem for resource allocation.

Although these works focus on the navigation, communication, and civilian applications of UAVs, the frameworks ignore the feasibility of various types of robots in executing tasks, particularly from the perspectives of comprehensiveness and practicality in low-altitude UAV rescue.

## B. MOO of MARL-Based for UAV Computation Offloading

Task offloading in UAV networks using MARL is mainly divided into policy-based and value-based approaches. Examples of policy-based methods include MADDPG [29], multiagent twin delayed DDPG (MATD3) [30], and multiagent proximal policy optimization (MAPPO) [19]. The authors in [30] proposed a cooperative multi-agent deep reinforcement learning framework to derive the joint strategy for trajectory design, task allocation, and power management. In [29], the authors proposed a framework for multiaccess MEC in air–ground networks and employed a MADDPG algorithm for efficient, adaptive decision-making under complex constraints. The authors [19] proposed a UAV-assisted MEC network with a digital twin to enhance service for mobile users. They formulated a resource scheduling problem as an MDP and emphasized the role of MAPPO in optimizing computation offloading. The value-based methods primarily include QMIX [31] and value-decomposition networks [23]. The authors [31] proposed aerial edge computing networks using UAVs for computation offloading. A MARL algorithm based on QMIX was introduced to manage the complexity of joint computation offloading and trajectory optimization. The authors [23] leveraged a MARL algorithm with value decomposition using a double deep Q-Network to optimize data aggregation and enhance offloading efficiency for UAV-enabled IoT systems in post-disaster contexts.

However, existing work has not comprehensively considered the practical challenges of computation offloading for lowaltitude UAV rescue, such as obstacle constraints, resource availability in rescue operations, and system stability. To differentiate this work from existing works in the research area, a comparative analysis of various works is summarized in Table I.

## C. GAI-Assisted Reinforcement Learning

Generative AI is a prominent subfield of machine learning focused on the conceptualization and creation of content. It arises from the goal of enabling machines to generate novel and original data that accurately reflects the underlying patterns, structures, and nuances present in the training datasets. Generative AI encompasses a variety of advanced models, including generative adversarial networks (GANs), transformer-based models, and GDM, each employing distinct methodologies for learning and generating data [32]. In [33], a GAN-driven auxiliary training mechanism for MARL is proposed. This approach reduces the overhead of real-world interactions and enables the agent’s policy to be well-suited for real-world execution environments by performing offline training using generated environment statuses. The authors in [34] combined Transformer with deep reinforcement learning (DRL) to address the scalability of the network and proposed a Transformer-based MARL algorithm for scalable multi-UAV area coverage. In [35], the authors integrated AI-generated optimal decisions with DRL to develop the deep diffusion soft actor-critic algorithm, improving the efficiency and effectiveness of selecting AI-generated content service providers.

Although these works demonstrate that GAI holds substantial promise for enhancing the capabilities of multi-agent systems [35], they primarily focus on improving MARL’s strategy generation while overlooking critical factors that influence this process, such as the observations of agents.

![](images/895dae742959ad43e55d4f4047f5d82565153114582617667da216c757a09a69.jpg)  
Fig. 1. System model. First, the GER computing power distribution map of the rescue area is divided into multiple subareas. Then, each UAV is assigned to multiple subareas. In each subarea, the UAV selects a suitable GER based on real-time observations to approach and perform computing task offloading.

## III. SYSTEM MODEL

In this section, we first introduce the application scenario and the proposed framework. We then define the mobility model, communication model, task completion latency model, and energy consumption model. The optimization problem is subsequently formulated.

## A. Application Scenario and Framework

We consider a low-altitude UAV rescue mission in which multiple UAVs, operating at below 300 meters <sup>1</sup>, are deployed to perform object detections using a convolutional neural network model, such as Yolov8s [23], [36], in situations where the conventional communication infrastructure, including base stations, is unavailable [23], [36]. Fig. 1 illustrates a system model framework for this application scenario. To improve the efficiency of rescue area exploration, UAV hovering is excluded from the scenario. Instead, UAVs process tasks online or offload them via U2G and U2A communications while in motion. Due to the disruption of the existing communication network, multiple airships are employed to provide communication coverage via airship-to-airship (A2A) communication. The airship, which has a longer flight duration and greater computational capabilities, hovers within 300-1000 meters higher than the UAVs, ensuring that all UAVs stay within its communication range <sup>2</sup>. The UAVs within the communication range of the airship are represented by the set $\mathcal { U } = \{ 1 , 2 , \dots , U \}$ , and $u \in \mathcal { U } ,$ where each UAV is assigned to multiple subareas, and these subareas do not overlap. Furthermore, we assume that both UAVs and GERs feature compatible communication interfaces, allowing for seamless networking and enabling UAVs to offload tasks to GERs. Let ${ \mathcal { I } } ,$ ${ \mathcal { G } } ,$ and B represent the sets of GERs, airships, and subareas, respectively, where $j \in \mathcal { I } , g \in \mathcal { G } ,$ and $b \in B .$ . A three-dimensional Cartesian coordinate system [37] is used to describe the locations of these entities. Without loss of generality, the UAVs operate at a constant hovering height H. The fixed hovering altitude minimizes energy consumption by avoiding frequent altitude changes due to terrain or buildings, which reduces the UAVs’ movement energy [38]. The parameters are presented in Table II.

TABLE II SELECTED SYMBOLS AND DEFINITIONS
<table><tr><td> $\overline { { d _ { u } ( t _ { i } ) } }$ </td><td>Symbol</td><td>Definition</td></tr><tr><td>Ssm ssddel</td><td> $D _ { u } ( t _ { i } )$   $l _ { u , j } ( t _ { i } )$   $L _ { u } ( t _ { i } )$   $s _ { u } ( t _ { i } )$   $E ^ { t o t { \dot { a } } } ( t _ { i } )$   $\mathcal { T }$   $\mathcal { I }$   $M$   $R _ { u , j } ( t _ { i } )$   $T _ { u } ^ { U A V } ( t _ { i } )$   $T _ { u , j } ^ { G E R } ( t _ { i } )$   $T ^ { t o t a } ( t _ { i } )$   $\mathcal { U }$   $U$   $\mathcal { G }$   $W$   $Z$ </td><td>Euclidean distance between the starting and ending coordinate of UAV u in time slot  $t _ { i } ^ { - }$  Size of task Channel power gain between UAV u and GER j at time slot  $t _ { i }$  Coordinates of UAV u at time slot  $t _ { i }$  Status of UAV u at time slot  $t _ { i }$  Total energy consumption of a UAV Set of time slots Set of GERs Set of computation resource allocations Transmission rate between UAV u and GER j The computing latency of UAV u to process the task in time slot  $t _ { i }$  The total service latency of task processed by UAV u at GER j in time slot ti Total task completion latency for all UAVs Set of UAVs within the coverage of airship Set of UAVs that choose to offload tasks to GERs Set of airships Set of UAV trajectory control decisions</td></tr><tr><td>AIithhm</td><td> $\delta$   $\overline { { A _ { i } ^ { u } } }$   $L ( Q ( t _ { i } ) )$   $\mathcal { L } _ { t }$   $O _ { i }$   $p ( \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } )$   $Q ( t )$   $\mathrm { Q }$   $\mathbf { x } _ { 0 }$   $\theta _ { Q }$   $\theta _ { \pi } , \dot { \theta } _ { \pi ^ { \prime } }$   $V$ </td><td>Set of risk sources Duration of each time slot The agent&#x27;s action of each time slot t The queue congestion The loss function for the denoising network Set of agent observation The conditional probability distribution of the inverse process from time step t to t — 1 The virtual queue representing the accumulated energy consumption The sets of critic networks for all agents The observation of agent n at the initial time Sets of parameters for the critic networks Sets of parameters for the actor networks and target actor networks The weighting factor for balancing task latency and energy consumption</td></tr></table>

## B. Mobility Model

We divide the system timeline T into I discrete time intervals, $\mathcal { T } = \{ 1 , 2 , \hdots , I \}$ , and $i \in \mathcal { Z } ,$ each with equal length $\delta ,$ i.e., <sup>= 1 2</sup>T Iδ. Within the coverage area of an airship g, the numbers of UAVs and GERs are fixed for every time interval. Let $t _ { 0 }$ signify the starting of $T ,$ , and ti denote the time within the i-th interval, where $t _ { i } \in [ t _ { 0 } + ( i - 1 ) \delta , t _ { 0 } + i \delta ]$ . In the i-th time slot, the coordinate of UAV u is given by $L _ { u } ( t _ { i } ) = [ x _ { u } ( t _ { i } ) , y _ { u } ( t _ { i } ) , H ]$ where $[ x _ { u } ( t _ { i } ) , y _ { u } ( t _ { i } ) ]$ is the horizontal coordinate of UAV u in the i-th time slot. The starting and ending coordinates of UAV u are predefined, denoted as $\begin{array} { r } { L _ { u } ^ { s t a r t } = \Bigl \lceil x _ { u } ^ { s t a r t } , y _ { u } ^ { s t a r t } , H \Bigr \rceil } \end{array}$ and $L _ { u } ^ { e n d } = \left\lceil x _ { u } ^ { e n d } , y _ { u } ^ { e n d } , H \right\rceil$ , respectively. The coordinates of UAV u in the i-th time slot remain fixed if δ is sufficiently small. By combining the coordinates of UAV u across i time slots, the Euclidean distance between the starting and ending coordinates of UAV u is as follows:

$$
\begin{array} { r l } & { d _ { u } ( t _ { i } ) = \Vert L _ { u } ( t _ { i } ) - L _ { u } ( t _ { i - 1 } ) \Vert } \\ & { \qquad = \sqrt { \left( x _ { u } ( t _ { i } ) - x _ { u } ( t _ { i - 1 } ) \right) ^ { 2 } + \left( y _ { u } ( t _ { i } ) - y _ { u } ( t _ { i - 1 } ) \right) ^ { 2 } } . } \end{array}\tag{1}
$$

The flight trajectory of UAV u over time $T$ can be modeled as: $L _ { u } = \{ L _ { u } ^ { s t a r t } , L _ { u } ( t _ { i } ) , L _ { u } ^ { e n d } \}$ , where $L _ { u } ( t _ { i } ) =$ $\{ L _ { u } ( t _ { 1 } ) , L _ { u } ( t _ { 2 } ) , \ldots , L _ { u } ( t _ { I } ) \}$ <sup>( ) ( ) =</sup>. The UAV’s flight trajectory is <sup>( ) ( ) ( )</sup>modeled as a set of flight segments corresponding to each time slot. In the i-th time slot, the status of UAV u is expressed as:

$$
s _ { u } ( t _ { i } ) = ( L _ { u } ( t _ { i } ) , \theta _ { u } ( t _ { i } ) , v _ { u } ( t _ { i } ) ) ,\tag{2}
$$

where $\theta _ { u } ( t _ { i } )$ is the angle between the UAV’s flight tangent direction and the reference heading (i.e., the due north direction), and $v _ { u } ( t _ { i } )$ is the real-time velocity of UAV u, which adheres to the maneuverability constraints. When UAV u flies from the starting coordinate $L _ { u } ^ { s t a r t }$ to the ending coordinate $L _ { u } ^ { e n d }$ , it can follow many optimal or suboptimal mobile trajectories. The UAV’s trajectory planning can be defined as $s _ { u } ^ { s t a r t } \xrightarrow { \mathfrak { S } } s _ { u } ^ { e n d } ,$ where S denotes the set of all flight trajectories that meet the constraints.

## C. Communication Model

In low-altitude UAV rescue scenarios, both Line-of-Sight (LoS) and Non-Line-of-Sight (NLoS) conditions are considered for U2G. The channel power gain between a UAV and a GER is determined by integrating the probabilistic LoS transmissions with both small-scale and large-scale fading [39]. For uplink communication, the channel power gain between UAV u and GER $j$ during time slot $t _ { i }$ can be expressed as:

$$
l _ { u , j } ( t _ { i } ) = p _ { u , j } ^ { L } l _ { u , j } ^ { L } ( t _ { i } ) + \left( 1 - p _ { u , j } ^ { L } \right) l _ { u , j } ^ { N L } ( t _ { i } ) ,\tag{3}
$$

where $p _ { u , j } ^ { L }$ represents the probability of LoS link, $l _ { u , j } ^ { L } ( t _ { i } )$ and $l _ { u , j } ^ { N L } ( t _ { i } )$ represent the gain between UAV u and GER j for LoS and NLoS links, respectively, which is defined as:

$$
l _ { u , j } ^ { L } ( t _ { i } ) = \lvert \mathcal { H } _ { u , j } ^ { L } ( t _ { i } ) \rvert ^ { 2 } \left( \mathcal { L } _ { u , j } ^ { L } ( t _ { i } ) \right) ^ { - 1 } 1 0 ^ { \frac { - \mathcal { F } _ { \sigma } ^ { L } ( t _ { i } ) } { 1 0 } } ,\tag{4a}
$$

$$
l _ { u , j } ^ { N L } ( t _ { i } ) = | \mathcal { H } _ { u , j } ^ { N L } ( t _ { i } ) | ^ { 2 } \left( \mathcal { L } _ { u , j } ^ { N L } ( t _ { i } ) \right) ^ { - 1 } 1 0 ^ { \frac { - \mathcal { F } _ { \sigma } ^ { N L } ( t _ { i } ) } { 1 0 } } ,\tag{4b}
$$

where $\mathcal { H } _ { u , j } ^ { L } ( t _ { i } ) , \ \mathcal { H } _ { u , j } ^ { N L } ( t _ { i } ) , \ \mathcal { L } _ { u , j } ^ { L } ( t _ { i } ) , \ \mathcal { L } _ { u , j } ^ { N L } ( t _ { i } ) , \ \mathcal { F } _ { \sigma } ^ { L } ( t _ { i } )$ and $\mathcal { F } _ { \sigma } ^ { N L } ( t _ { i } )$ are the components of path loss, shadowing, and smallscale fading for LoS and NLoS links, respectively.

The small-scale fading of the channel is modeled using the Nakagami-m fading model [40]. This model is parametric, scalable, and provides a good fit to the observed data. To avoid confusion with UAV identifiers, we use w instead of m to represent the shape parameter. Therefore, we refer to it as Nakagami-w. Specifically, $\mathcal { H } _ { u , j } ^ { L } ( t _ { i } )$ and $\mathcal { H } _ { u , j } ^ { N L } ( t _ { i } )$ follow the Nakagami distribution with fading parameters $w ^ { L }$ and $w ^ { N L }$ which can be given as:

$$
\mathcal { H } _ { u , j } ^ { L } ( t _ { i } ) = \frac { 2 \left( w ^ { L } \right) ^ { w ^ { L } } h ^ { ( 2 w ^ { L } - 1 ) } e ^ { \left( - \frac { w ^ { L } h ^ { 2 } } { \overline { { p } } } \right) } } { \Gamma \left( w ^ { L } \right) \overline { { p } } ^ { w ^ { L } } } ,\tag{5a}
$$

$$
\mathcal { H } _ { u , j } ^ { N L } ( t _ { i } ) = \frac { 2 ( w ^ { N L } ) ^ { w ^ { N L } } h ^ { ( 2 w ^ { N L } - 1 ) } e ^ { \left( - \frac { w ^ { N L } h ^ { 2 } } { \overline { { p } } } \right) } } { \Gamma \left( w ^ { N L } \right) \overline { { p } } ^ { w ^ { N L } } } ,\tag{5b}
$$

where $\overline { { p } }$ represents the average power of the received signal in the fading envelope. · represents the Gamma function. h represents the signal amplitude.

The path loss between UAV u and GER $j$ for LoS or NLoS link is defined as:

$$
\mathscr { L } _ { u , j } ^ { L } ( t _ { i } ) = \frac { \left( 4 \pi d _ { 0 } f _ { c } \right) ^ { 2 } } { c ^ { 2 } } \left( \frac { d _ { u , j } ( t _ { i } ) } { d _ { 0 } } \right) ^ { \beta ^ { L } } ,\tag{6a}
$$

$$
\mathcal { L } _ { u , j } ^ { N L } ( t _ { i } ) = \frac { ( 4 \pi d _ { 0 } f _ { c } ) ^ { 2 } } { c ^ { 2 } } \left( \frac { d _ { u , j } ( t _ { i } ) } { d _ { 0 } } \right) ^ { \beta ^ { N L } } ,\tag{6b}
$$

where $f _ { c }$ represents the carrier frequency, c is the speed of light, $d _ { 0 }$ is the reference distance, $d _ { u , j } ( t _ { i } )$ is the distance between UAV u and GER $j ,$ and $\beta ^ { L }$ and $\beta ^ { N \bar { L } }$ are the path loss exponents for LoS and NLoS links, respectively. Next, the shadowing refers to the large-scale signal attenuation caused by obstacles, and it can be modeled as a zero-mean Gaussian distributed random variable:

$$
\mathcal { F } _ { \sigma } ^ { L } ( t _ { i } ) \sim \mathcal { O } \left( 0 , \left( \sigma ^ { L } \right) ^ { 2 } \right) ,\tag{7a}
$$

$$
\begin{array} { r } { \mathcal { F } _ { \sigma } ^ { N L } ( t _ { i } ) \sim \mathcal { O } \left( 0 , \left( \sigma ^ { N L } \right) ^ { 2 } \right) , } \end{array}\tag{7b}
$$

where $\sigma ^ { L }$ and $\sigma ^ { N L }$ are the standard deviations of shadowing for LoS and NLoS links, respectively [39].

Accordingly, we use orthogonal frequency-division multiple access [41] to reduce interference and support multiple UAVs simultaneously. In time slot $t _ { i }$ , the data transmission rate between UAV u and GER $j$ can be given as:

$$
R _ { u , j } ( t _ { i } ) = B _ { w } \log _ { 2 } \left( 1 + \frac { P _ { u } l _ { u , j } ( t _ { i } ) } { \sigma ^ { 2 } } \right) ,\tag{8}
$$

where $B _ { w }$ is the channel bandwidth and $P _ { u }$ is the transmission power of the UAV. σ<sup>2</sup> is the noise power. $\sigma ^ { 2 }$

## D. Task Completion Latency Model

UAV computing latency: The task of UAV u generated in time slot $t _ { i }$ is characterized as $\{ D _ { u } ( t _ { i } ) , C _ { u } , \tau _ { u } \}$ , wherein $D _ { u } ( t _ { i } )$ is the data size in bits, $C _ { u }$ is the computation intensity of the task in cycles per bit, and $\tau _ { u }$ denotes the deadline of the task. The service latency depends on the task offloading decision $\varsigma _ { u , j } ( t _ { i } )$ which indicates the proportion or number of layers of the UAV’s task offloaded to the GER. The computing latency of UAV u to process task $D _ { u } ( t _ { i } )$ locally in time slot $t _ { i }$ can be given as:

$$
T _ { u } ^ { U A V } ( t _ { i } ) = \frac { \varsigma _ { u , j } ( t _ { i } ) D _ { u } ( t _ { i } ) C _ { u } } { f _ { u } } ,\tag{9}
$$

where $f _ { u }$ denotes the computing capability of UAV u.

GER computing latency: The computing latency of UAV u to offload task $D _ { u } ( t _ { i } )$ to GER j in time slot $t _ { i }$ mainly consists <sup>( )</sup>of the transmission delay and processing delay. Specifically, the transmission delay can be given as:

$$
T _ { u , j } ^ { t r a n } ( t _ { i } ) = \frac { ( 1 - \varsigma _ { u , j } ( t _ { i } ) ) D _ { u } ( t _ { i } ) } { R _ { u , j } ( t _ { i } ) } .\tag{10}
$$

Moreover, the processing delay can be expressed as:

$$
T _ { j } ^ { c o m p } ( t _ { i } ) = \frac { ( 1 - \varsigma _ { u , j } ( t _ { i } ) ) D _ { u } ( t _ { i } ) C _ { u } } { f _ { j , u } ( t _ { i } ) } ,\tag{11}
$$

where $f _ { j , u }$ indicates the computing capability allocated by GER j to the UAV u.

Given that the results are typically much smaller in comparison to the input data for most applications, the result download delay is ignored. Therefore, the service latency for GER computing latency and the total task completion latency for all UAVs can be calculated as:

$$
T _ { u , j } ^ { G E R } ( t _ { i } ) = T _ { u , j } ^ { t r a n } ( t _ { i } ) + T _ { j } ^ { c o m p } ( t _ { i } ) ,\tag{12}
$$

$$
T ^ { t o t a } ( t _ { i } ) = \sum _ { u = 1 } ^ { U } \sum _ { j = 1 } ^ { J } T _ { u } ^ { U A V } ( t _ { i } ) + T _ { u , j } ^ { G E R } ( t _ { i } ) .\tag{13}
$$

## E. Energy Consumption Model

Transmission energy consumption: The transmission energy consumption is approximated as the product of the transmission power $P _ { u }$ and the transmission latency $T _ { u , j } ^ { t r a n } ( t _ { i } )$ of the intermediate result of the task as follows:

$$
E _ { u , j } ^ { t r a n } ( t _ { i } ) = P _ { u } T _ { u , j } ^ { t r a n } ( t _ { i } ) .\tag{14}
$$

Computation energy consumption: The computation energy consumption of UAV u to process the task $K _ { u } ( t _ { i } )$ in the slot $t _ { i }$ can be given as:

$$
\begin{array} { r } { E _ { u } ^ { c o m p } ( t _ { i } ) = \kappa _ { u } ( f _ { u } ) ^ { 2 } D _ { u } ( t _ { i } ) C _ { u } , } \end{array}\tag{15}
$$

where $\kappa _ { u }$ is the capacitance coefficient of UAV u, which is related to the chip structure of the CPU [42].

Propulsion energy consumption: The propulsion loss of UAV u is dependent on its flight speed [43]. We assume that UAV u travels at a constant speed $V _ { u } ( t _ { i } )$ within each time slot, and the speeds can be different in different time slots. The propulsion energy consumption is given as follows:

$$
E _ { u } ^ { p r o p } ( t _ { i } ) = w _ { u } v _ { u } ( t _ { i } ) ^ { 2 } ,\tag{16}
$$

where $w _ { u }$ is related to the weight of the UAV.

Detection energy consumption: Throughout the entire flight of UAV u, there are unavoidable risks such as obstacles, adverse weather conditions, and complicated terrain. To estimate the energy expenditure for detecting risks during UAV’s flight, we define the risk sources as a set $\mathcal { Z } = \{ 1 , 2 , \dots , Z \}$ , and $z \in { \mathcal { Z } } .$ . In this case, the UAV’s flight distance in the i-th time slot is divided into m equal-length segments, and the Euclidean distance from the risk source z to the central point of each segment is denoted by $\{ d _ { z _ { 1 } } , d _ { z _ { 2 } } , \ldots , d _ { z _ { m } } \}$ . When UAV u travels from its starting coordinate L<sup>start</sup><sub>u</sub> to its ending coordinate $L _ { u } ^ { e n d }$ , its trajectory must be free of collisions. As such, UAV u must monitor the specific rescue area of the risk source z within each segment to ensure safe flying. Hence, the energy consumed by UAV u in detecting the risk source z during the i-th time slot is defined as $\begin{array} { r } { E _ { u } ^ { z } ( t _ { i } ) = \varpi \sum _ { k = 1 } ^ { m } d _ { z _ { k } } } \end{array}$ , where  is the unit energy consumed by UAV u for sensing the risk source z [25]. When UAV u encounters multiple risk sources from the set <sup>Z</sup> during flight, the total energy consumption for detection due to the surrounding risks can be expressed as:

$$
E _ { u } ^ { d e t e } ( t _ { i } ) = \sum _ { z \in \mathbb { Z } } E _ { u } ^ { z } ( t _ { i } ) .\tag{17}
$$

To ensure that the UAV can provide long-term services at a low cost, the total energy consumption should be within an acceptable bound over a period of time, $\mathrm { e . g . }$ ., hours. Then, the total energy consumption is

$$
\begin{array} { r } { E ^ { t o t a } ( t _ { i } ) = E _ { u , j } ^ { t r a n } ( t _ { i } ) + E _ { u } ^ { c o m p } ( t _ { i } ) + E _ { u } ^ { p r o p } ( t _ { i } ) + E _ { u } ^ { d e t e } ( t _ { i } ) . } \end{array}\tag{18}
$$

We use $\bar { E } _ { u }$ to denote the long-term average cost budget over time T . Then, a constraint is introduced to outline the system’s long-term cost budget expectations for total energy consumption as follows [43]:

$$
\frac { 1 } { T } \sum _ { i = 1 } ^ { I } \mathbb { E } \left[ E ^ { t o t a } ( t _ { i } ) \right] \leq \bar { E } _ { u } .\tag{19}
$$

## F. Problem Formulation

The objectives of this paper are to reduce the overall task completion latency, minimize the total energy consumption of UAVs, and maximize the task offloading rate. To achieve these goals, three key elements are optimized: 1) The allocation of computational resources, denoted as $\mathbf { M } = \{ m _ { j , u } ( t _ { i } ) , \forall u \in \mathcal { U } , \forall j \in \mathcal { T } \}$ ; 2) The task offloading decisions, denoted as $\mathbf { F } = \{ \varsigma _ { u , j } ( t _ { i } ) , \forall u \in$ $\mathcal { U } , j \in \mathcal { T } \}$ <sup>= ( )</sup>, where u represents a UAV that chooses to offload its task to a ground edge resource (GER); 3) The UAV trajectory control, denoted as $\mathbf { W } = \{ w _ { j } ( t _ { i } ) , \forall j \in \mathcal { T } \}$ . Accordingly, the MOO problem is formulated as follows:

$$
\mathbf { P 1 } : \operatorname* { m i n } _ { \mathbf { F } , \mathbf { M } , \mathbf { W } } \left\{ \sum _ { i = 1 } ^ { I } T ^ { t o t a } ( t _ { i } ) \right\}\tag{20}
$$

$$
\mathrm { s . t . } \quad \frac { 1 } { T } \sum _ { i = 1 } ^ { I } \mathbb { E } [ E ^ { t o t a } ( t _ { i } ) ] \leq \bar { E } _ { u } , \forall u \in \mathcal { U } ,\tag{20a}
$$

$$
0 \leq \varsigma _ { u , j } ( t _ { i } ) \leq 1 , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{20b}
$$

$$
\sum _ { j = 1 } ^ { J } \varsigma _ { u , j } ( t _ { i } ) \leq 1 , \forall u \in \mathcal { U } ,\tag{20c}
$$

$$
\sum _ { u = 1 } ^ { U } \varsigma _ { u , j } ( t _ { i } ) \leq 1 , \forall j \in \mathcal { T } ,\tag{20d}
$$

$$
\varsigma _ { u , j } ( t _ { i } ) \cdot T ^ { U A V } ( t _ { i } ) \leq \tau _ { u } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{20e}
$$

$$
\varsigma _ { u , j } ( t _ { i } ) \cdot T ^ { G E R } ( t _ { i } ) \leq \tau _ { u } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{20f}
$$

$$
0 \leq f _ { j , u } ( t _ { i } ) \leq f _ { j } ^ { \operatorname* { m a x } } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{20g}
$$

<table><tr><td>Optimization problems</td><td>Variables</td><td>Algorithms</td></tr><tr><td>Multiple objective optimization (P1)</td><td>F, M, W</td><td rowspan="3">Lyapunov algorithm</td></tr><tr><td>↓</td><td></td></tr><tr><td colspan="2">Long-term optimization problem(P3)</td></tr><tr><td>↓</td><td></td><td></td></tr><tr><td>UAV exploration optimization</td><td>W K</td><td>HG-MADDPG Hungarian algorithm</td></tr><tr><td>↓</td><td></td><td></td></tr><tr><td>Task assignment decision</td><td>F, M</td><td>GDM-MADDPG</td></tr></table>

Fig. 2. The decomposition process of the optimization problem.

$$
\sum _ { u = 1 } ^ { U } f _ { j , u } ( t _ { i } ) \leq f _ { j } ^ { \operatorname* { m a x } } , \forall j \in \mathcal { T } ,\tag{20h}
$$

$$
\delta \cdot d _ { u } ^ { \operatorname* { m i n } } / T \leq d _ { u } ( t _ { i } ) \leq \delta \cdot V _ { u } ^ { \operatorname* { m a x } } , \forall j \in \mathcal { I } ,\tag{20i}
$$

$$
\sum _ { i = 1 } ^ { I } d _ { u } ( t _ { i } ) \leq L _ { u } ^ { \operatorname* { m a x } } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{20j}
$$

$$
\| L _ { u } ( t _ { i } ) - L _ { u + 1 } ( t _ { i } ) \| \geq D , \forall u \in \mathcal { U } , j \in \mathcal { T } .\tag{20k}
$$

where the constraint (20a) represents the system’s long-term cost budget expectations for total energy consumption. $\bar { E } _ { u }$ denotes the long-term average cost budget over time $T$ . Constraints (20b)-(20d) represent the task offloading constraints of UAVs. Constraints (20e) and (20f) indicate the deadline of the tasks. Constraints (20g) and (20h) limit the computation resource of UAV. Constraint (20i) defines the mobility limitation of UAV u, where $V _ { u } ^ { \mathrm { m a x } }$ denotes the maximum velocity of UAV u. Constraint (20j) specifies the flight distance of UAV u during the i-th time slot. The flight trajectory of UAV u consists of I segments with varying lengths traversed during each time slot. $L _ { u } ^ { \mathrm { m a x } }$ indicates the maximum allowable flight distance. Constraint (20k) addresses the spatial restriction for UAV u and UAV u operating in the i-th time slot, with D representing the minimum safe distance between two UAVs.

In general, the optimization problem outlined above cannot be solved in a single iteration due to the dynamic environment and the long-term objectives and constraints involved. Predicting dynamic channel conditions and user mobility over an extended period is highly challenging, and making real-time decisions under these long-term constraints is complex. Therefore, to efficiently solve P1, we employ an online algorithm capable of transforming the long-term optimization problem into an MDP. Problem P1 involves integer variables (i.e., task offloading F) and continuous variables (i.e., M and W), while the inequalities in (20b)-(20j) are non-convex constraints. Consequently, problem P1 is an MINLP problem, which is also non-convex and NP-hard [44]. Additionally, existing complexity analyses in [45] have formally confirmed this specific programming class as NP-hard.

As illustrated in Fig. 2, P1 can be decoupled into a longterm deterministic optimization problem that incorporates stability considerations, which is addressed using the Lyapunov algorithm, denoted as P3. Additionally, the UAV exploration optimization problem is solved iteratively using the Hungarian algorithm. Subsequently, the task assignment decisions for the UAV, including computation resource allocation, task offloading ratio, and GER selection, are determined through the application of the HG-MADDPG method.

## IV. LYAPUNOV-BASED DECOUPLING METHOD FOR DYNAMIC LONG-TERM PROBLEM

In this section, we first introduce the motivation for adopting Lyapunov optimization for the proposed problem and then use the Lyapunov algorithm to decouple problem P1 into deterministic per-slot optimization problems.

## A. Motivation of Adapting Lyapunov Optimization

Lyapunov optimization is a powerful method for transforming long-term stochastic optimization into sequential per-slot deterministic problems while ensuring system stability [9]. While this paper focuses on an application scenario involving continuous and random tasks, where multiple objectives must be optimized simultaneously. The mobile edge computing terminals in this scenario include UAVs and GERs, which are deployed for rescue missions. Additionally, the stability of the system, composed of multiple resource-constrained mobile edge computing terminals, must be taken into account. We adapt the Lyapunov optimization method to the problem by using the Lyapunov function derived in (23) to jointly optimize energy consumption and task completion latency, and to quantify the accumulation of virtual queues Q ti , thereby improving system stability.

## B. Decoupling of P1 Via Lyapunov Algorithm

For problem P1, the key idea is to trade off the latency performance and the total energy consumption in the long run. In this section, the Lyapunov optimization method is employed to decouple the long-term optimization problem. Specifically, we introduce a virtual queue $Q ( t _ { i } )$ as the cost queue containing the accumulated energy consumption, as follows:

$$
\begin{array} { r l } & { Q ( t _ { i + 1 } ) = \operatorname* { m a x } \left\{ Q ( t _ { i } ) + E ^ { t o t a l } ( t _ { i } ) - \bar { E } _ { u } , 0 \right\} } \\ & { ~ = \operatorname* { m a x } \left\{ Q ( t _ { i } ) + y _ { k } ( t _ { i } ) , 0 \right\} , } \end{array}\tag{21}
$$

where the value of $Q ( t _ { i } )$ represents the queue length, indicating the excess total energy consumption over the budget by the end of time slot $t _ { i }$ . To simplify the calculation, we add queue $E ^ { t o t a l } ( t _ { i } )$ and constant $\bar { E } _ { u }$ to obtain $y _ { k } ( t _ { i } )$

A large value of the virtual queue $Q ( t _ { i } )$ suggests that the current load status of energy consumption is likely to exceed the budget in the long run. Therefore, to satisfy the long-term constraint (20a), the queue $Q ( t _ { i } )$ should be stable, as follows:

$$
\operatorname* { l i m } _ { T \to \infty } \frac { Q ( T ) } { T } = 0 .\tag{22}
$$

To further solve equation (22), we employ a Lyapunov function to control the virtual queues in each time slot. Next, the Lyapunov function is as follows:

$$
L ( Q ( t _ { i } ) ) = \frac { 1 } { 2 } Q ^ { 2 } ( t _ { i } ) ,\tag{23}
$$

where $L ( Q ( t _ { i } ) )$ quantifies the congestion of the queue. The stability of the queue $Q ( t _ { i } )$ can be maintained if a policy function consistently drives the Lyapunov function towards a bounded value [46]. Next, we present a one-step conditional Lyapunov drift function $\Delta L ( Q ( t _ { i } ) )$ . The stability of $Q ( t _ { i } )$ can be attained by minimizing $\Delta L ( Q ( t _ { i } ) )$ as:

$$
\Delta L ( Q ( t _ { i } ) ) = \mathbb { E } \left\{ L ( Q ( t _ { i + 1 } ) ) - L ( Q ( t _ { i } ) ) | Q ( t _ { i } ) \right\} ,\tag{24}
$$

The drift-plus-penalty function of Lyapunov is expressed as:

$$
\Delta L \left( Q \left( t _ { i } \right) \right) + V \mathbb { E } \left[ T ^ { t o t a } ( t _ { i } ) \right] ,\tag{25}
$$

where $V \geq 0$ is a weighting factor to balance the total task completion latency and queue stability.

The problem P1 can be converted into a series of deterministic problems for each time slot, given by

$$
\mathbf { P 2 } : \operatorname* { m i n } _ { \mathbf { F } , \mathbf { M } , \mathbf { W } } \left\{ \Delta L \left( Q ( t _ { i } ) \right) + V \mathbb { E } \left[ T ^ { t o t a } ( t _ { i } ) \right] | Q ( t _ { i } ) \right\}\tag{26}
$$

$$
\begin{array} { r } { \mathrm { s . t . } 0 \leq \varsigma _ { u , j } ( t _ { i } ) \leq 1 , \forall u \in \mathcal { U } , j \in \mathcal { I } , } \end{array}\tag{26a}
$$

$$
\sum _ { j = 1 } ^ { J } \varsigma _ { u , j } ( t _ { i } ) \leq 1 , \forall u \in \mathcal { U } ,\tag{26b}
$$

$$
\sum _ { u = 1 } ^ { U } \varsigma _ { u , j } ( t _ { i } ) \leq 1 , \forall j \in \mathcal { T } ,\tag{26c}
$$

$$
\varsigma _ { u , j } ( t _ { i } ) \cdot T ^ { U A V } ( t _ { i } ) \leq \tau _ { u } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{26d}
$$

$$
\varsigma _ { u , j } ( t _ { i } ) \cdot T ^ { G E R } ( t _ { i } ) \leq \tau _ { u } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{26e}
$$

$$
0 \leq f _ { j , u } ( t _ { i } ) \leq f _ { j } ^ { \operatorname* { m a x } } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{26f}
$$

$$
\sum _ { u = 1 } ^ { U } f _ { j , u } ( t _ { i } ) \leq f _ { j } ^ { \operatorname* { m a x } } , \forall j \in \mathcal { T } ,\tag{26g}
$$

$$
\delta \cdot d _ { u } ^ { \operatorname* { m i n } } / T \leq d _ { u } ( t _ { i } ) \leq \delta \cdot V _ { u } ^ { \operatorname* { m a x } } , \forall j \in \mathcal { I } ,\tag{26h}
$$

$$
\sum _ { i = 1 } ^ { I } d _ { u } ( t _ { i } ) \leq L _ { u } ^ { \operatorname* { m a x } } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{26i}
$$

$$
\| L _ { u } ( t _ { i } ) - L _ { u + 1 } ( t _ { i } ) \| \geq D , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{26j}
$$

$$
\operatorname* { l i m } _ { T \to \infty } \frac { Q ( T ) } { T } = 0 .\tag{26k}
$$

Minimizing Lyapunov drift-plus-penalty function (25) needs the information of future time slots due to $\Delta L ( Q ( t _ { i } ) )$ . To avoid involving future information, we derive and minimize its upper bound. By using the fundamental inequality, $\{ x , 0 \} ^ { 2 } \leq { \overline { { x } } } ^ { 2 }$ the upper bound of (24) is given by

$$
\begin{array} { r l r } {  { \Delta ( Q ( t _ { i } ) ) = \mathbb { E } [ L ( Q ( t _ { i + 1 } ) ) - L ( Q ( t _ { i } ) ) | Q ( t _ { i } ) ] } } \\ & { } & \\ & { } & { \leq \mathbb { E } \big [ \frac { 1 } { 2 } y _ { k } ( t _ { i } ) ^ { 2 } + Q ( t _ { i } ) y _ { k } ( t _ { i } ) ) \big ] \leq \Theta + Q ( t _ { i } ) y _ { k } ( t _ { i } ) , } \end{array}\tag{27}
$$

where is a constant that upper bounds the first term on the right side of the above inequality. Such a constant exists because the $y _ { k } ( t _ { i } )$ values are bounded [46].

A solution to problem P2 can be obtained by minimizing the upper bound on the right-hand side of (26a) in each time slot, as given below:

$$
\mathbf { P 3 } : \operatorname* { m i n } _ { \mathbf { F } } \left\{ \Theta + V \mathbb { E } \left[ T ^ { t o t a } ( t _ { i } ) \right] + Q ( t _ { i } ) y _ { k } ( t _ { i } ) \mid Q ( t _ { i } ) \right\}\tag{28}
$$

$$
\begin{array} { r } { \mathrm { s . t . ~ } 0 \leq \varsigma _ { u , j } ( t _ { i } ) \leq 1 , \forall u \in \mathcal { U } , j \in \mathcal { I } , } \end{array}\tag{28a}
$$

$$
\sum _ { j = 1 } ^ { J } \varsigma _ { u , j } ( t _ { i } ) \leq 1 , \forall u \in \mathcal { U } ,\tag{28b}
$$

$$
\sum _ { u = 1 } ^ { U } \varsigma _ { u , j } ( t _ { i } ) \leq 1 , \forall j \in \mathcal { T } ,\tag{28c}
$$

$$
\varsigma _ { u , j } ( t _ { i } ) \cdot T ^ { U A V } ( t _ { i } ) \leq \tau _ { u } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{28d}
$$

$$
\varsigma _ { u , j } ( t _ { i } ) \cdot T ^ { G E R } ( t _ { i } ) \leq \tau _ { u } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{28e}
$$

$$
0 \leq f _ { j , u } ( t _ { i } ) \leq f _ { j } ^ { \operatorname* { m a x } } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{28f}
$$

$$
\sum _ { u = 1 } ^ { U } f _ { j , u } ( t _ { i } ) \leq f _ { j } ^ { \operatorname* { m a x } } , \forall j \in \mathcal { T } ,\tag{28g}
$$

$$
\delta \cdot d _ { u } ^ { \operatorname* { m i n } } / T \leq d _ { u } ( t _ { i } ) \leq \delta \cdot V _ { u } ^ { \operatorname* { m a x } } , \forall j \in \mathcal { I } ,\tag{28h}
$$

$$
\sum _ { i = 1 } ^ { I } d _ { u } ( t _ { i } ) \leq L _ { u } ^ { \operatorname* { m a x } } , \forall u \in \mathcal { U } , j \in \mathcal { I } ,\tag{28i}
$$

$$
\| L _ { u } ( t _ { i } ) - L _ { u + 1 } ( t _ { i } ) \| \geq D , \forall u \in \mathcal { U } , j \in \mathcal { T } .\tag{28j}
$$

It can be proved that (26k) always holds during the solution process of P3. Therefore, this constraint can be omitted when solving the problem [46]. From P3, it can be obtained that solving the problem is equivalent to solving the MOO problem proposed in Section III-F. By solving P3, the optimal solution of P1 can be obtained, i.e., it can be obtained by

$$
\varsigma _ { u , j } \left( t _ { i } \right) = \underset { \varsigma _ { u , j } \left( t _ { i } \right) \in { \bf F } } { \mathrm { a r g m i n } } \mathbb { E } \left[ \Theta + V T ^ { t o t a } ( t _ { i } ) + Q \left( t _ { i } \right) y _ { k } \left( t _ { i } \right) | Q ( t _ { i } ) \right] .\tag{29}
$$

Remarks: P3 is freed from the constraint in (19) in comparison to P1. As a result, P3 can be solved in an online fashion, without the need for global offline data. The objectives of P3 are the task completion latency and the energy consumption of the UAV, which are weighted by a parameter V and the energy consumption queue $Q ( t _ { i } )$ , respectively. Adjusting these weighted factors allows for a balanced trade-off between task completion latency and the UAV’s energy budget. Generally, V provides a static adjustment that remains constant during GERassisted UAV’s task offloading. A higher V helps in reducing the task completion latency. Additionally, the energy consumption queue $Q ( t _ { i } )$ provides dynamic control, which fluctuates based on the energy consumption of the UAV. An increased energy consumption queue indicates a lower remaining energy in the UAV, driving it to optimize energy usage in future time slots. This enables dynamic adjustment of the UAV’s energy consumption in the optimization problem P3. Solving this online optimization yields efficient GER-assisted UAV task offloading for P1.

![](images/6fa9c38c02625805d12a0b5de9604ec8b63ba869088386936db867b27a954be1.jpg)  
Fig. 3. Architecture of HG-MADDPG. 1 Environmental observation, the HG-MADDPG makes each agent only needs to focus on the exploration subarea it selects, which reduces the dimension of the agent’s observation space. 2 Action generation, the HG-MADDPG designs the inverse diffusion process of GDM to replace the action network, which can generate the optimal decision in dynamic environment. 3 Interaction between the agent and the environment, the agent based on the observations to realize the distributed execution to obtain their respective rewards. 4 Agent-agent interaction, agents share experience by exchanging strategy sample sets, so that each agent has global training samples and realizes centralized training.

## V. THE PROPOSED HG-MADDPG ALGORITHM

In this section, we first provide an overview of the proposed HG-MADDPG algorithm. Next, we give our motivation for adopting the Hungarian algorithm for exploration area selection. Then, we introduce the motivation for adopting GDM and MADDPG, followed by elaborating on the offloading decision optimization for task assignment, modeling the problem as an MDP. We then present the interaction of the agent with the HG-MADDPG algorithm and conclude with an analysis of its computational complexity.

## A. Overview of the HG-MADDPG Algorithm

The framework of the HG-MADDPG is shown in Fig. 3. The observation mechanism for the environment incorporates an area selection method based on the Hungarian algorithm, as illustrated in Algorithm 1. This method eliminates the need for the agent (i.e., UAV) to acquire the status of all GERs or the task data size across different areas, thereby conserving the computational resources of the UAV. The reverse diffusion process seeks to recover the original data from noisy observations. Specifically, its training process iteratively predicts the noise distribution and trains the reverse diffusion model, enabling the agent to extract more information about data distributions from the environment’s observations, generate actions, and execute them. The agent adjusts its parameters (such as denoising steps, batch size, and learning rate) based on feedback rewards, aiming to maximize long-term rewards and make optimal decisions. The task assignment and exploration optimization based on HG-MADDPG is detailed in Algorithm 2.

## B. Hungarian-Based Area Selection for Exploration Optimization

1) Motivation of Adopting Hungarian Algorithm: In lowaltitude UAV systems with unknown environments, assigning flight areas effectively is crucial to maximize coverage and minimize redundancy or gaps. As the complexity of the environment increases, the observation space of agents expands, which introduces challenges for existing MARL methods like MADDPG. The motivation is driven by the need for optimal coverage while ensuring efficient UAV exploration. The Hungarian algorithm, with its optimal matching capability, ensures that each UAV is assigned to a specific area in a way that minimizes the total travel cost while covering all areas. Moreover, the Hungarian algorithm benefits from its low computational complexity, high efficiency, and stability, making it suitable for a variety of scenarios for solving matching problems [47]. Furthermore, the complexity is $O ( \operatorname* { m a x } ( U , B ) ^ { 3 } )$ , where U is the number of UAVs and B is the number of subareas. This results in improved coverage efficiency, balanced workload distribution among UAVs, and reduced operational costs, making it a suitable choice for UAV exploration in unknown environments.

2) Area Selection for Exploration Optimization: The exploration optimization involves trajectory generation and obstacle detection (see Section III-E). Specifically, the UAV first selects an exploration area based on the Hungarian algorithm. Within the selected area, task offloading and GER selection are then performed using GDM-MADDPG. Once the GER is determined, the UAV’s trajectory is defined by its movement toward the selected GER to maximize the channel power gain (see Section III-C). During this process, the UAV also conducts low-altitude obstacle detection to avoid potential collisions. The

```powershell
Algorithm 1: Hungarian-Based Area Selection for UAV
Exploration.
1 Initialize the label values and matching array: Set all
the row labels α to the minimum value, i.e.,
$\alpha _ { u } =$ min $( \mathbb { C } [ u ] [ 1 ] , \dots , \mathbb { C } [ u ] [ B ] )$ , set all the column
labels $\beta _ { b } = 0$
2 for each $U A V u = 1 , 2 , \ldots , U$ do
3 Search for a column that satisfies the matching
condition $\mathbb { C } [ u ] [ b ] \le \alpha _ { u } + \beta _ { b }$ and has not been
matched by any other row. Then match the
current row with this column and mark the
column as matched.
4 Adjust the label values:
5 During the process of finding an augmenting
trajectory, adjust the row and column labels so
that new matches can be found while
maintaining the relationship between the cost
matrix elements and the label values.
6 if All areas are selected to UAVs then
7 Break the loop.
8 end
9 end
10 Calculate the total cost.
```

Hungarian algorithm is based on the bipartite graph matching theory. It continuously searches for augmenting trajectories and updates matching relationships to achieve the optimal matching solution. In this paper, the predetermined rescue area is divided into B subareas. UAVs incur varying costs when performing different tasks. The cost is as follows:

$$
\mathit { c o s t } = \parallel \mathit { L } _ { u } ( t _ { i } ) - \mathit { L } _ { b } \parallel + \mathit { D } _ { b } + \mathit { C } _ { b } - e _ { u } ^ { r e m a } ( t _ { i } ) - \mathit { f } _ { b } ,\tag{30}
$$

where $L _ { b }$ is the coordinate of the center point of the area, $e _ { u } ^ { r }$ ema is the remaining energy of the UAV, $D _ { b }$ is the data size, $C _ { b }$ is the area task calculation intensity (cycle/bit), and $f _ { b }$ represents the average computing power of GER.

The cost matrix of each UAV to each area is represented by $\mathbb { C } [ u ] [ b ] = c o s t _ { u , b }$ . The area selection approach based on the Hungarian algorithm is detailed in Algorithm 1. The specific steps are as follows:

Step 1 (Line 1 of the Algorithm 1): Initialize the label values of rows and columns, and the matching array.

Step 2 (Line 2-line 9): For each row (i.e., UAV) in the cost matrix, the algorithm finds the optimal matching area, i.e., the optimal matching area for each UAV. If the optimal matching solution cannot be found directly, the algorithm adjusts the label value to ensure that a new matching relationship can be found. This process continues to iterate until all UAVs are assigned to the corresponding areas.

Step 3 (Line 10): Based on the final matching relationship and the original cost matrix, the algorithm computes whether the total cost reaches the optimal area selection, i.e., the total cost is minimized.

## C. HG-MADDPG-Based Task Assignment and Exploration Optimization

1) Motivation of Adopting GDM and MADDPG: The motivation for adopting GDM and MADDPG lies in their ability to enhance decision optimization in multi-agent environments, especially with limited offline training data, and GDM’s generative capabilities enable dynamic decision-making [48]. Moreover, integrating GDM and MADDPG into UAV systems refines training processes and optimizes decision strategies to enhance coordination and adaptability in unknown environments. Furthermore, the Hungarian algorithm and GDM are innovatively integrated into MARL, which respectively realizes the computational complexity of the observation space and the generation capability of the action space, thus improving the observation and execution effects of multiple agents.

2) Markov Decision Process Modeling: The problem of exploration optimization and task assignment for UAVs is modeled as a multi-agent MDP, denoted by a tuple $( o _ { i } ^ { u } , A _ { i } ^ { u } , r _ { i } ^ { u } , o _ { i + 1 } ^ { u } , u )$ where $o _ { i } ^ { u }$ <sup>(</sup>represents the observation of the agent, $r _ { i } ^ { u }$ <sup>)</sup>indicates the reward received by the agent, and $o _ { i + 1 } ^ { u }$ is the subsequent observation of the agent after performing the selected action. The agent learns an optimal task assignment strategy according to its own task number and computation resources, as well as the location and computing power of the GER, aiming to achieve the optimal task completion latency and energy consumption.

Observations: In each time slot t, the UAV collects environmental observations $O _ { i } = \{ o _ { i } ^ { 1 } , o _ { i } ^ { 2 } , . . . , o _ { i } ^ { u } \}$ . Then, the observation of an agent is defined as:

$$
o _ { i } ^ { u } = \{ L _ { u } ( t _ { i } ) , f _ { u } , L _ { j } , f _ { j } \} ,\tag{31}
$$

where $L _ { u }$ and $f _ { u }$ denote the UAV’s coordinate and computing power, and $L _ { j }$ and $f _ { j }$ denote the GER’s coordinate and computing power, respectively.

Actions: At time slot t, the action of an agent is $A _ { i } ^ { u }$ , which includes the task offloading target and the associated offloading ratio. The agent’s action is represented as:

$$
\mathrm { A } _ { i } ^ { u } = \{ m _ { u , j } ( t _ { i } ) , \mathrm { p } _ { u , j } ( t _ { i } ) \} ,\tag{32}
$$

where $m _ { u , j } ( t _ { i } )$ represents the offloading GER of UAV u at time slot $i ,$ and $\mathrm { p } _ { u , j } ( t _ { i } )$ represents the offloading ratio at time slot i.

Rewards: Since the actions of agents are limited by energy consumption and directly impact task completion latency, the reward obtained for an action is given by

$$
r _ { i } ^ { u } = \mathbb { E } \left[ V \cdot T ^ { t o t a } + Q ( t _ { i } ) y _ { k } ( t _ { i } ) | Q ( t _ { i } ) \right] .\tag{33}
$$

3) UAVs Interacting With Environment: In a multi-agent setup, the agent’s actor network generates specific actions based on its observations. These observations serve as inputs for the GDM’s inverse diffusion process, which incrementally predicts and denoises the sampled Gaussian noise to generate actions according to the current conditions. For agent $u ,$ the purpose of the inverse diffusion process is to infer the task ratio $\mathbf { x } _ { 0 } ^ { u }$ that is offloaded to the selected GER in the subarea from the Gaussian noise $\mathbf { x } _ { T } ^ { u } { \sim } N ( 0 , I )$ . Since the number of GERs is random, the dimension of $\mathbf { x } _ { 0 } ^ { u }$ depends on the maximum number of GERs in the subarea, that is, the dimension of the action space. If the probability $p ( \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } )$ is learned, it is feasible to get sampling $\mathbf { x } _ { t }$ from a standard normal distribution and samples from $p ( \mathbf { x } _ { 0 } )$ via the inverse denoising process. However, the estimation of $\dot { \mathbf { \rho } } p ( \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } )$ is computationally complex in practice. <sup>( )</sup>Therefore, the objective is to approximate $p ( \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } )$ using $\begin{array} { r } { p _ { \theta } ( \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } ) = \mathcal { N } ( \mathbf { x } _ { t - 1 } ; \mu _ { \theta } ( \mathbf { x } _ { t } , t ) , \Sigma _ { \theta } ( \mathbf { x } _ { t } , t ) ) } \end{array}$ <sup>( )</sup>. The probability <sup>( ) = ( ; ( ) (</sup>from xT to x<sub>0</sub> can then be expressed as:

$$
{ p _ { \theta } } ( \mathbf { x } _ { 0 : T } ) = { p _ { \theta } } ( \mathbf { x } _ { T } ) \prod _ { t = 1 } ^ { T } { p _ { \theta } } \left( \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } \right) .\tag{34}
$$

The training of GDM involves optimizing the negative loglikelihood function of the training data. By adding conditional information <sup>ð</sup>, i.e., the agent’s observation $o _ { i } ^ { u }$ , during the denoising process. The airship assigns subareas to achieve load balancing of UAV exploration. Therefore, the UAV only needs to handle the offloading decision of the assigned subarea to achieve the minimum task completion delay and energy consumption, which can not only maintain the optimal decision of a single subarea and the global optimal allocation but also reduce the computational complexity. At each time step, the conditioning the model predicts the parameters of the Gaussian distribution, specifically the mean $\mu _ { \theta } ( \mathbf { x } _ { t } , t )$ and the covariance matrix $\Sigma _ { \theta } ( \mathbf { x } _ { t } , t )$ <sup>( )</sup>. Based on [49], incorporating conditional information <sup>ð</sup> during the denoising process enables the model to be treated as a prediction model for noise, and the covariance matrix is fixed to $p _ { \theta } ( \mathbf { x } _ { 0 : T } )$ and $\begin{array} { r } { \sum _ { \theta } ( \mathbf { x } _ { t } , \vec { \mathbf { \sigma } } ) , t ) = \beta _ { t } I , } \end{array}$ . The mean is calculated as follows:

$$
\mu _ { \theta } ( \mathbf { x } _ { t } , \vec { 0 } , t ) = \frac { 1 } { \sqrt { \alpha _ { t } } } \left( \mathbf { x } _ { t } - \frac { \beta _ { t } } { \sqrt { 1 - \overline { { \alpha } } _ { t } } } \epsilon _ { \theta } ( \mathbf { x } _ { t } , \vec { 0 } , t ) \right) .\tag{35}
$$

Next, $\mathbf { x } _ { T }$ sampled from $N ( 0 , I )$ . The sampling dimension <sup>(0 )</sup>depends on the number of GERs in each subarea. Then, through the inverse denoising process parameterized by θ, we sample $\mathbf { x } _ { t - 1 } \mid \mathbf { x } _ { t }$ as follows:

$$
\mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } = \frac { \mathbf { x } _ { t } } { \sqrt { \alpha _ { t } } } - \frac { \beta _ { t } } { \sqrt { \alpha _ { t } ( 1 - \overline { { \alpha } } _ { t } ) } } \epsilon _ { \theta } ( \mathbf { x } _ { t } , \vec { \mathbf { \sigma } } , t ) + \sqrt { \beta _ { t } } \epsilon ,\tag{36}
$$

where $\epsilon \sim N ( 0 , I )$ represents a standard normal distribution, and $t = 1 , \dots , T$

The loss function of the denoising network is defined by

$$
\mathcal { L } _ { t } = \mathbb { E } _ { \mathbf { x } _ { 0 } , t , \epsilon } \left[ | | \epsilon - \epsilon _ { \theta } \big ( \sqrt { \overline { { \alpha _ { t } } } } \mathbf { x } _ { 0 } + \sqrt { 1 - \overline { { \alpha _ { t } } } } \epsilon , t \big ) | | ^ { 2 } \right] .\tag{37}
$$

4) UAVs Interacting With Each Other: The experience information $( o _ { i } ^ { u } , A _ { i } ^ { u } , r _ { i } ^ { u } , o _ { i + 1 } ^ { u } , u )$ generated by the agent in the process of interacting with the environment is stored in the experience replay memory. Then, multiple agents share the experience by exchanging sample sets. Furthermore, the agent uses the time difference error to assign priorities to the experience information so that important data is sampled more frequently, thereby improving learning efficiency and performance. The critic network assesses the effectiveness of the action produced by the actor network through rewards, i.e., the impact of the generated action on the long-term reward. When each agent calculates the forward propagation of the critic network, it splices the observations of all agents, including itself, into the observation vector $O _ { i } = \{ o _ { i } ^ { 1 } , o _ { i } ^ { 2 } , \ldots , o _ { i } ^ { U } \}$ , splices the actions of all agents into the action vector $A _ { i } = \{ A _ { i } ^ { 1 } , A _ { i } ^ { 2 } , \ldots , A _ { i } ^ { U } \}$ , and uses $( O _ { i } , A _ { i } )$ as the input of the critic network and outputs a one-dimensional $Q$ value, i.e., $Q _ { \theta _ { \mathcal { O } } ^ { u } } ( O _ { i } , A _ { i } )$ . In other words, the agent uses the information of all other agents in the environment to centrally train its own evaluation network. Next, the target actor network calculates the action $A _ { i + 1 }$ taken by the agent in the next observation through the sample $O _ { i + 1 }$ in the experience replay memory, and then constructs the MSE loss function of $Q _ { \theta _ { O } ^ { u } } ( O _ { i } , A _ { i } )$ and $Q _ { \theta _ { O } ^ { u } } ( O _ { i + 1 } , A _ { i + 1 } )$ with the time difference error and uses gradient descent to update the parameter $\theta _ { Q } ^ { u }$ . The loss function and gradient formula are as follows:

```powershell
Algorithm 2: HG-MADDPG-Based Task Assignment and
Exploration Optimization.
1 The parameters of the actor-critic network and the
inverse process of GDM
2 for episode = 0 → E do
3 Initialize the agent environment
4 for $i = 1 , 2 , \dots , \mathbb { I }$ do
5 Get the selected area using Algorithm 1
6 for $u = 1 , 2 , \ldots , U$ do
7 Agent u obtains observation $o _ { i } ^ { u }$ of the
selected area b
8 for $t = T , \dots , 1 , 0$ do
9 Gaussian noise € is predicted and
denoised, obtaining $\mathbf { x } _ { 0 } ^ { u }$
10 end
11 An action selected by agent u according to
$o _ { i } ^ { u }$
12 end
13 Execute action and obtain $r _ { i } ^ { u }$ and the next
$o _ { i + 1 } ^ { u }$
14 $o _ { i } ^ { u } \stackrel { \cdot } {  } o _ { i + 1 } ^ { u }$
15 if the experience replay memory isn't full then
16 Store the training sample
$( o _ { i } ^ { u } , A _ { i } ^ { u } , r _ { i } ^ { u } , o _ { i + 1 } ^ { u } , u )$ into the memory
17 else
18 Update the memory
19 for $u = 1 , 2 , \ldots , U$ do
20 Samples are taken from the memory
$( o _ { i } ^ { u } , A _ { i } ^ { u } , r _ { i } ^ { u } , o _ { i + 1 } ^ { u } , u ) , \forall i = 1 , 2 , \ldots , \bar { } I$
21 Update the actor network by Eq. (38)
and the critic network by Eq. (39)
22 end
23 Update the parameters of the target
network according to $\psi$
24 end
25 end
26 end
```

$$
\begin{array} { l } { \displaystyle \underset { \theta _ { Q } ^ { u } } { \mathrm { m i n } } \log = \frac { \mathrm { m i n } } { \theta _ { Q } ^ { u } } \mathbb { E } _ { ( o _ { i } ^ { u } , A _ { i } ^ { u } , r _ { i } ^ { u } , o _ { i + 1 } ^ { u } , u ) \sim D } \left[ \left( Q _ { \theta _ { Q } } ( O _ { i } , A _ { i } ) \right. \right. } \\ { \displaystyle \left. \left. - \left( r _ { i } ^ { u } + \gamma Q _ { \theta _ { Q } } ( O _ { i + 1 } , A _ { i + 1 } ) \right) \right) ^ { 2 } \right] , \qquad ( \mathrm { ~ o ~ } } \end{array}\tag{38}
$$

$$
\begin{array} { r l } & { \nabla _ { \theta _ { Q } ^ { u } } J ( \theta _ { Q } ^ { u } ) = \nabla _ { \theta _ { Q } ^ { u } } \mathbb { E } _ { ( o _ { i } ^ { u } , A _ { i } ^ { u } , r _ { i } ^ { u } , o _ { i + 1 } ^ { u } , u ) \sim D } \Big [ \left( Q _ { \theta _ { Q } } ( O _ { i } , A _ { i } ) \right. } \\ & { \left. \qquad - \left( r _ { i } ^ { u } + \gamma Q _ { \theta _ { Q } } ( O _ { i + 1 } , A _ { i + 1 } ) \right) \right) ^ { 2 } \Big ] , \qquad ( \mathrm { ~ a ~ n ~ d ~  ~ { \mathbb ~ } ~ } ) } \end{array}\tag{39}
$$

where $Q = \{ Q _ { 1 } , Q _ { 2 } , \dots , Q _ { u } \}$ represents the sets of critic networks for all agents. Let $\theta _ { Q } = \{ \theta _ { Q } ^ { 1 } , \theta _ { Q } ^ { 2 } , \dots , \theta _ { Q } ^ { u } \}$ denote the sets of parameters for the critic networks.

5) Complexity Analysis of HG-MADDPG Algorithm: In this section, we analyze the computational and space complexity of the proposed algorithm from the training and execution stages of the model, respectively.

• Training stage: The computational complexity is given by $\mathcal { O } ( 2 \vert \theta _ { \mu } \vert + 2 \vert \theta _ { Q } \vert + \mathbb { E } \delta \vert \theta _ { \mu } \vert + \mathbb { E } \delta H \xi + U ( 2 \vert \theta _ { \mu ^ { \prime } } \vert + 2 \vert \theta _ { Q ^ { \prime } } \vert ) )$ <sup>(2 + 2 + + + (2 + 2 ))</sup>which can be broken down as follows [50]. The complexity of Parameters initialization of actor-critic network is $\mathcal { O } ( 2 \vert \theta _ { \mu } \vert$ $2 | \theta _ { Q } | )$ , where $| \theta _ { \mu } |$ and $| \theta _ { Q } |$ are the number of parameters of the actor-critic networks, respectively. The complexity of Observation-action pair sampling is $\mathcal { O } ( \mathbb { E } \delta | \theta _ { \mu } | )$ , where <sup>E</sup> is the total number of episodes. The complexity of Experience replay memory collection is $\mathcal { O } ( \mathbb { E } \delta H \xi )$ , where H denotes the computational cost of the Hungarian algorithm, and ξ denotes the complexity of interacting with the environment. The complexity of Target actor-critic network update is $\mathcal { O } ( U ( 2 | \theta _ { \mu ^ { \prime } } | + 2 | \theta _ { Q ^ { \prime } } | ) )$ The target network parameters are updated U times. The space complexity denotes $\mathcal { O } ( 2 | \theta _ { \mu } | + 2 | \theta _ { Q } | + \zeta ( 2 | o _ { i } ^ { u } | + | \mathrm { A } _ { i } ^ { u } | + 2 ) )$ where ζ means the size of the memory. |o<sub>i</sub> | and $\left| \mathrm { A } _ { i } ^ { u } \right|$ represent the dimension sizes of the observation and the action spaces, respectively. The complexity includes both the parameters of the neural network and the memory storing the tuples $( o _ { i } ^ { u } , A _ { i } ^ { u } , r _ { i } ^ { u } , o _ { i + 1 } ^ { u } , u )$

• Execution stage: The computational complexity is $\mathcal { O } ( | \theta _ { \mu } | )$ which is due to action inference of the actor network with the corresponding observation. Therefore, The space complexity is also $\mathcal { O } ( | \theta _ { \mu } | )$ .

## VI. EXPERIMENT SETUP AND PERFORMANCE EVALUATION

In this section, we introduce the experimental setup and evaluate the performance of HG-MADDPG in terms of convergence, stability, task completion latency, exploration capability, and resource visualization.

## A. Experiment Setup

For the first input layer in the actor network, the dimension of the observation space determines the number of neurons, while the third output layer has a number of neurons equal to the action dimension. The second hidden layer contains 256 neurons. For the critic network, the first input layer’s neuron count depends on both the observation space dimension and the number of agents, with the hidden layer also containing 256 neurons. The learning rate of the actor-critic networks is $\gamma = 1 0 ^ { - 4 }$ , and the size of the mini-batch is 512. The discount factor is $\gamma _ { m } = 0 . 9$ with the exploration rate $\epsilon _ { 0 } = 0 . 9$ and the decay rate $\beta = 1 0 ^ { - 4 }$ The setup includes an airship at 600 meters altitude and nine UAVs at 50 meters, covering a $\mathrm { 5 0 \times 5 0 ~ k m ^ { 2 } }$ rescue zone. The airship is centrally located, with UAVs evenly distributed. All UAVs are within the airship’s coverage and communicate with each other. Yolov8s is used as the convolutional neural network model for performance evaluation in the experiments. A complete summary of the parameters and their corresponding values is presented in Table III. To assess its advantages, a set of benchmark algorithms is also evaluated.

TABLE III EXPERIMENT PARAMETERS [21], [24]
<table><tr><td rowspan=1 colspan=1>Symbol</td><td rowspan=1 colspan=1>Definition</td><td rowspan=1 colspan=2>Value(Unit)</td></tr><tr><td rowspan=1 colspan=1> $\vec { U }$ </td><td rowspan=1 colspan=1>Number of UAVs</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>3, 10]</td></tr><tr><td rowspan=1 colspan=1>J</td><td rowspan=1 colspan=1>Number of GERs</td><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>75, 300]</td></tr><tr><td rowspan=1 colspan=1> $\overline { { B } }$ </td><td rowspan=1 colspan=1>Number of subareas</td><td rowspan=1 colspan=2>[15, 50]</td></tr><tr><td rowspan=1 colspan=1>I</td><td rowspan=1 colspan=1>Number of rounds</td><td rowspan=1 colspan=2>5</td></tr><tr><td rowspan=1 colspan=1> $\mathbb { L } _ { I }$ </td><td rowspan=1 colspan=1>Data size of task</td><td rowspan=1 colspan=2>[12.5, 125] GB</td></tr><tr><td rowspan=1 colspan=1> $\overline { { v _ { u } ^ { m a x } } }$ </td><td rowspan=1 colspan=1>UAV propulsion speed</td><td rowspan=1 colspan=2>30m/s</td></tr><tr><td rowspan=1 colspan=1> $\underline { { e _ { u } ^ { m a x } } }$ </td><td rowspan=1 colspan=1>Maximum UAV power</td><td rowspan=1 colspan=2>200 Wh</td></tr><tr><td rowspan=1 colspan=1> $\underline { { f _ { u } } }$ </td><td rowspan=1 colspan=1>UAV computing power</td><td rowspan=1 colspan=2>5 TFPLOPs</td></tr><tr><td rowspan=1 colspan=1> ${ \underline { { v _ { q } } } }$ </td><td rowspan=1 colspan=1>Average processing rate of UAV</td><td rowspan=1 colspan=2>12.5GB/min</td></tr><tr><td rowspan=1 colspan=1> $C _ { b }$ </td><td rowspan=1 colspan=1>Computational complexity</td><td rowspan=1 colspan=2>[200, 500]cycle/bi</td></tr><tr><td rowspan=1 colspan=1> $\overline { { P _ { n } } }$ </td><td rowspan=1 colspan=1>Maximum transmission power</td><td rowspan=1 colspan=2>[10, 100] mW</td></tr><tr><td rowspan=1 colspan=1> $\overline { { B _ { w } } }$ </td><td rowspan=1 colspan=1>Maximum bandwidth</td><td rowspan=1 colspan=2>[1, 10] Gbps</td></tr><tr><td rowspan=1 colspan=1> $\overline { { P _ { N } } }$ </td><td rowspan=1 colspan=1>Noise power</td><td rowspan=1 colspan=2>-115 dBm</td></tr><tr><td rowspan=1 colspan=1> $\overline { { f _ { j } } }$ </td><td rowspan=1 colspan=1>Computing power of GER</td><td rowspan=1 colspan=2>[0, 10] TFPLOPs</td></tr></table>

![](images/66c001af59c49c3c1f67f8cfe536cbf71304f9c2aab16a5b7a480c48964c9b01.jpg)  
Fig. 4. Convergence comparison of different algorithms.

MADDPG is a decentralized actor–centralized critic algorithm designed primarily for environments with continuous action spaces [29]. The algorithm enables each agent to learn its own deterministic policy while leveraging centralized training to learn global information, which facilitates coordination among agents in partially observable settings. However, MADDPG can face challenges in training stability and scalability as the number of agents grows.

\- MAPPO is a policy-gradient-based method adapted from PPO, which uses clipped surrogate objectives to improve training stability and sample efficiency [19]. MAPPO supports centralized training with decentralized execution and works well in both discrete and continuous action spaces.

![](images/2064520aa4b9c0ed0daa2cc84567dc1b5f02c2efa432cf92298e2a9e073dbb66.jpg)  
(a) Reward vs. denoising step.

![](images/d6d273ef8c2ca314c286d1bfe0f395edb9d3eaa8e9eebc9d6d2fed74ea6c364f.jpg)  
(b) Reward vs. batch size.

![](images/c207b6fcaccd9dff472d08744367eba87bffbbfaca2a3a6f5f54dab26bf63a44.jpg)  
(c) Reward vs. learning rate.

Fig. 5. The reward of different denoising steps, batch sizes, and learning rates.  
![](images/a7a0365303563e71dcc7e725b38595f030d8a1d00c205af91ee5fedfea5242cb.jpg)  
(a) Queuing energy vs. weighting factor.

![](images/4b9cbda79a2c176a9e6074d5a555ee3319a8f8afc29697a84e6be6e075ff0d5f.jpg)  
(b) Queuing energy vs. computing power.

![](images/7834350c3dd28992ecb09150916c6f22e3f7fbce57e2c971f759bc85c24dadd1.jpg)  
(c) Queuing energy vs. data size.  
Fig. 6. Queuing energy of different weighting factor V , computing power, and data sizes.

## B. Performance Evaluation

1) Convergence of Training Process: In Fig. 4, although the convergence of the HG-MADDPG is slower, it consistently outperforms the MADDPG and MAPPO. The reward of HG-MADDPG increases steadily throughout the whole training process, eventually stabilizing at approximately 1200 after around 300 episodes. The improvement is due to the generative advantage of GDM, which enhances action sample efficiency by denoising steps.

A set of experiments is performed to determine the optimal values for three key parameters affecting HG-MADDPG performance: denoising steps, batch size, and learning rate. From the results in Fig. 5(a), it is evident that when the number of denoising steps is 5, the training process and the reward stability are superior to other step numbers. This suggests that five denoising steps are most effective for the denoising performance of the method proposed in this paper. Fig. 5(b) shows that a batch size of 300 yields the best performance. Fig. 5(c) demonstrates the convergence of the reward function under different learning rates. Clearly, the learning rates of 0.01 and 0.000001 do not support convergence, while a learning rate of 0.0001 accelerates convergence. Using a learning rate of 0.0001, we then evaluate the effect of batch sizes on the model training performance.

2) Stability of Queuing Energy and Latency: In Fig. 6, we investigate the queuing energy online control achieved by incorporating the Lyapunov technique into our approach. Fig. 6(a) presents the queuing energy for various V values. The queuing energy is monitored as the number of training episodes increases. Queuing energy refers to the average difference between the UAV’s energy consumption in the current round and that in the previous episode. It reflects both the energy consumption trend across different task processing stages and the overall energy level of the task queue. The reason is that the diffusion model in HG-MADDPG is used to enhance the learning ability of the policy network so that it can more accurately understand the dynamic changes in energy consumption. Similarly, Fig. 6(b) and (c) present the queuing energy under varying computing power and data sizes, respectively.

To further demonstrate the significant impact of the Lyapunov technique introduced in this paper on system stability, we focus on the stability requirements of task completion latency in low-altitude UAV rescue emergency systems. Verification experiments were conducted to assess the system’s task completion latency under varying conditions of GER computing power, available computation resources, and data sizes. The task completion latency of the system remains within a relatively stable range, as illustrated in Fig. 7. The observed convergence behavior of these evolving task queues confirms the stability of task assignment, ensuring the reliable operation of the system as outlined in this study.

![](images/e3811d8466ba9679b690c23834e92b3ea2e7ffb700114749c14c0c1200ae0745.jpg)  
(a) Latency vs. computing power.

![](images/e0016afbc6fc9c2c9544491417a4157cce40409910c70489f73368594b7570d9.jpg)  
(b) Latency vs. number of GERs.

![](images/18ba104eaf6776e1ccbed863be6de75570ee90cab0c4be52ac2c9b726f42ea22.jpg)  
(c) Latency vs. data size.

Fig. 7. Stability of task completion latency under different data sizes, computing powers, and number of GERs.  
![](images/fea1f02c0e73615bb8d3f7f4a7814cc4ad2b796ecc53fb255a4754db64addfe8.jpg)  
(a) Latency vs. computing power.

![](images/7dd1a61458def3318d7686977671b50bda94d44b8e85d7085204651cc303b7e9.jpg)  
(b) Latency vs. number of GERs.

![](images/df13d860cee22562f512bcd526e792358fa5e727f3be30fa90c870d975eceea0.jpg)  
(c) Latency vs. data size.  
Fig. 8. Task completion latency of various algorithms under the condition of ensuring successful task completion.

3) Task Completion Latency: The Fig. 8(a) and (b) illustrate how the task completion latency is affected by progressively increasing the computing power and number of GERs. This experiment was conducted with 3 UAVs and V . . As the computing power and number of GERs increase, the task completion latency decreases. HG-MADDPG achieves the largest reduction in average task completion latency, outperforming MADDPG and MAPPO by 20.35 and 12.56 , respectively. This is because HG-MADDPG has a faster decision generation capability and has fewer observation space dimensions. Furthermore, as shown in Fig. 8(c), while the computing power and number of GERs remain unchanged, as the task data size increases, the task queue becomes longer and the completion time increases accordingly. Compared with the other two baseline methods, the task completion time based on HG-MADDPG is the shortest. This is because the UAV based on HG-MADDPG will consider the current computing power of GER when selecting the offloading object and select the GER with strong current computing power and low task completion delay for task offloading. This shows that the above experimental results can clearly illustrate that the proposed method is feasible and in line with common sense.

4) Altitude Exploration and Resource Visualization: In lowaltitude UAV rescue scenarios, the conditions in the rescue area are often unknown. Therefore, conducting efficient autonomous exploration of such unknown environments presents a challenge. To address this, as in Fig. 9, different subareas are marked by colors. We set the number of UAVs to 3 and assigned each UAV 5 operating time slots, dividing the entire rescue area into 15 subareas for exploration. Fig. 9(a) illustrates the operation of three UAVs conducting a flight within a designated area. These UAVs collaborate with one another, utilizing coordinated strategies to successfully execute the rescue mission within the area. The proposed algorithm demonstrates effective performance in exploration optimization within unknown lowaltitude environments. It is capable of identifying the optimal flight trajectory in environments containing diverse obstacles, employing autonomous decision-making to navigate around these obstacles, and ultimately reaching the target destination, as in illustration Fig. 9(b). This highlights the algorithm’s ability to ensure autonomous exploration and trajectory planning, offering a novel approach for the widespread use of UAVs in unknown low-altitude environments.

![](images/bb60bba23be02be2397cfdea0d3ae8d507823d531b03d4001085041dd4065b2b.jpg)  
(a) Subarea (colors) and 2D trajectory.

![](images/43a439a66be027965c41602508d5ac224cfc71c706c396a280dfbe8d4528c845.jpg)  
(b) 3D trajectory and obstacle avoidance.  
Fig. 9. Exploration optimization and GER distribution.

![](images/f1dc7de5e3d34c662d037a6c9e33b6632bc94acfce41f328837736afccec434d.jpg)  
(c) Visualization of computing power.

Fig. 9(c) illustrates the distribution and utilization of computing power resources of GERs in a rescue area. The main purpose of this figure is to present the remaining computation resources of each GER. From a quantitative perspective, it can be observed that UAVs can autonomously select subareas and GERs based on their coordinates and available resources, as validated in Fig. 9(a). From a qualitative perspective, during rescue operations, emergency command decision-makers can quickly assess the available computation resources of GERs in the area through the visualization of their distribution and usage. This facilitates informed decision-making for the scheduling of rescue resources and the allocation of efforts.

## VII. CONCLUSION

In this study, we have addressed the joint problem of task assignment and exploration optimization in low-altitude UAV rescue as a dynamic long-term optimization problem. The primary objective is to minimize the task completion time and energy consumption while ensuring system stability over an extended period. To solve this, we have first employed the Lyapunov optimization method to transform the long-term optimization problem, which includes stability constraints, into a per-slot deterministic problem. Subsequently, we have solved the UAV exploration optimization problem iteratively through the use of the Hungarian algorithm. Following this, the task assignment decisions for the UAV, including the allocation of computation resources, task offloading ratio, and GER selection, are determined by applying the HG-MADDPG method. Through extensive numerical simulations, we have demonstrated that the proposed method outperforms existing benchmark solutions in terms of performance. In future work, we plan to incorporate three-dimensional trajectory planning and network topology optimization to enhance the reliability of low-altitude UAV networks and better address the demands of low-altitude economic applications in complex environments.

## REFERENCES

[1] Z. Fang, S. Hu, J. Wang, Y. Deng, X. Chen, and Y. Fang, “Prioritized information bottleneck theoretic framework with distributed online learning for edge video analytics,” IEEE Trans. Netw., vol. 33, no. 3, pp. 1203–1219, Jun. 2025.

[2] B. Karaman, I. Basturk, S. Taskin, F. Kara, E. Zeydan, and H. Yanikomeroglu, “Enhancing resiliency of integrated space-air-groundsea networks with renewable energies: A use case after the 2023 t\,” urkiye earthquake,” 2024, arXiv:2405.17635.

[3] J. He et al., “Advancing non-intrusive load monitoring: Predicting appliance-level power consumption with indirect supervision,” IEEE Trans. Netw. Sci. Eng., vol. 12, no. 4, pp. 2957–2973, Jul./Aug. 2025.

[4] G. Liu et al., “Generative AI for unmanned vehicle swarms: Challenges, applications and opportunities,” 2024, arXiv:2402.18062.

[5] X. Tang, Q. Chen, R. Yu, and X. Li, “Digital twin-empowered task assignment in aerial MEC network: A resource coalition cooperation approach with generative model,” IEEE Trans. Netw. Sci. Eng., vol. 12, no. 1, pp. 13–27, Jan./Feb. 2025.

[6] L. Xiaohuan et al., “An aggregate flow based scheduler in multi-task cooperated UAVs network,” Chin. J. Aeronaut., vol. 33, no. 11, pp. 2989–2998, 2020.

[7] X. Li et al., “Cloud-edge-end collaborative intelligent service computation offloading: A digital twin driven edge coalition approach for industrial IoT,” IEEE Trans. Netw. Service Manag., vol. 21, no. 6, pp. 6318–6330, Dec. 2024.

[8] L. Sun, Z. Liu, Z. Ning, J. Wang, and X. Fu, “Multi-agent Q-Net enhanced coevolutionary algorithm for resource allocation in emergency human-machine fusion UAV-MEC system,” IEEE Trans. Automat. Sci. Eng., vol. 22, pp. 4473–4489, 2024.

[9] Z. Liu et al., “DNN partitioning, task offloading, and resource allocation in dynamic vehicular networks: A lyapunov-guided diffusion-based reinforcement learning approach,” IEEE Trans. Mobile Comput., vol. 24, no. 3, pp. 1945–1962, Mar. 2025.

[10] G. Sun et al., “Generative AI for advanced UAV networking,” 2024, arXiv:2404.10556.

[11] Z. Liu et al., “Two-timescale model caching and resource allocation for edge-enabled AI-generated content services,” 2024, arXiv:2411.01458.

[12] G. Sun et al., “Task delay and energy consumption minimization for low-altitude MEC via evolutionary multi-objective deep reinforcement learning,” 2025, arXiv:2501.06410.

[13] T. Azfar, K. Huang, and R. Ke, “Enhancing disaster resilience with UAVassisted edge computing: A reinforcement learning approach to managing heterogeneous edge devices,” 2025, arXiv:2501.15305.

[14] J. Xu, K. Ota, and M. Dong, “Ideas in the air: Unmanned aerial semantic communication for post-disaster scenarios,” IEEE Wireless Commun. Lett., vol. 14, no. 6, pp. 1598–1602, Jun. 2025.

[15] K. Zhao, L. Peng, and B. Tak, “Joint DRL-based UAV trajectory planning and TEG-based task offloading,” IEEE Trans. Consum. Electron., 2025.

[16] H. Xiao, X. Hu, W. Wang, Z. Su, K.-K. Wong, and K. Yang, “STAR-RIS and UAV combination in MEC networks: Simultaneous task offloading and communications,” IEEE Trans. Commun., to be published, doi: 10.1109/TCOMM.2025.3535895.

[17] R. Zhou et al., “User preference oriented service caching and task offloading for UAV-assisted MEC networks,” IEEE Trans. Serv. Comput., vol. 18, no. 2, pp. 1097–1109, Mar./Apr. 2025.

[18] X. Tang et al., “Digital-twin-assisted task assignment in multi-UAV systems: A deep reinforcement learning approach,” IEEE Internet Things J., vol. 10, no. 17, pp. 15362–15375, Sep. 2023.

[19] W. Liu, B. Li, W. Xie, Y. Dai, and Z. Fei, “Energy efficient computation offloading in aerial edge networks with multi-agent cooperation,” IEEE Trans. Wireless Commun., vol. 22, no. 9, pp. 5725–5739, Sep. 2023.

[20] B. Hazarika et al., “Generative AI-augmented graph reinforcement learning for adaptive UAV swarm optimization,” IEEE Internet Things J., vol. 12, no. 8, pp. 9508–9524, Apr. 2025.

[21] X. Tang et al., “DNN task assignment in UAV networks: A generative AI enhanced multi-agent reinforcement learning approach,” IEEE Internet Things J., vol. 12, no. 10, pp. 13340–13352, May 2025.

[22] H. Sun et al., “All-sky autonomous computing in UAV swarm,” IEEE Trans. Mobile Comput., 2024.

[23] A. M. Raivi and S. Moh, “JDACO: Joint data aggregation and computation offloading in UAV-enabled Internet of Things for post-disaster scenarios,” IEEE Internet Things J., vol. 11, no. 9, pp. 16529–16544, May 2024.

[24] G. Sun et al., “Joint task offloading and resource allocation in aerialterrestrial UAV networks with edge and fog computing for post-disaster rescue,” IEEE Trans. Mobile Comput., vol. 23, no. 9, pp. 8582–8600, Sep. 2024.

[25] Y. Wang et al., “Task offloading for post-disaster rescue in unmanned aerial vehicles networks,” IEEE/ACM Trans. Netw., vol. 30, no. 4, pp. 1525–1539, Aug. 2022.

[26] X. Tang, F. Chen, F. Wang, and Z. Jia, “Disaster resilient emergency communication with intelligent air-ground cooperation,” IEEE Internet Things J., vol. 11, no. 3, pp. 5331–5346, Feb. 2024.

[27] R. Khalid, Z. Shah, M. Naeem, A. Ali, A. Al-Fuqaha, and W. Ejaz, “Computational efficiency maximization for UAV-assisted MEC networks with energy harvesting in disaster scenarios,” IEEE Internet Things J., vol. 11, no. 5, pp. 9004–9018, Mar. 2024.

[28] J. Wang, Y. Sun, B. Wang, and T. Ushio, “Mission-aware UAV deployment for post-disaster scenarios: A worst-case sac-based approach,” IEEE Trans. Veh. Technol., vol. 73, no. 2, pp. 2712–2727, Feb. 2024.

[29] J. Du et al., “MADDPG-based joint service placement and task offloading in MEC empowered air-ground integrated networks,” IEEE Internet Things J., vol. 11, no. 6, pp. 10600–10615, Mar. 2024.

[30] N. Zhao, Z. Ye, Y. Pei, Y.-C. Liang, and D. Niyato, “Multi-agent deep reinforcement learning for task offloading in UAV-assisted mobile edge computing,” IEEE Trans. Wireless Commun., vol. 21, no. 9, pp. 6949–6960, Sep. 2022.

[31] H. Yu, S. Leng, and F. Wu, “Joint cooperative computation offloading and trajectory optimization in heterogeneous UAV-swarm-enabled aerial edge computing networks,” IEEE Internet Things J., vol. 11, no. 6, pp. 17700–17711, May 2024.

[32] R. Zhang et al., “Generative AI for space-air-ground integrated networks,” IEEE Wireless Commun., vol. 31, no. 6, pp. 10–20, Dec. 2024.

[33] Y. Li, L. Feng, Y. Yang, and W. Li, “GAN-powered heterogeneous multiagent reinforcement learning for UAV-assisted task offloading,” Ad Hoc Netw., vol. 153, 2024, Art. no. 103341.

[34] D. Chen, Q. Qi, Q. Fu, J. Wang, J. Liao, and Z. Han, “Transformer-based reinforcement learning for scalable multi-UAV area coverage,” IEEE Trans. Intell. Transp. Syst., vol. 25, no. 8, pp. 10062–10077, Aug. 2024.

[35] H. Du et al., “Diffusion-based reinforcement learning for edge-enabled AI-generated content services,” IEEE Trans. Mobile Comput., vol. 23, no. 9, pp. 8902–8918, Sep. 2024.

[36] X.-Y. Zhang, Y. Xuan, C. Mu, Z. Ding, H. Wang, and P. Guo, “Robust lightweight UAV inspection system for consumer electronics applications in smart grids,” IEEE Trans. Consum. Electron., early access, Feb. 7, 2025, doi: 10.1109/TCE.2025.3539652

[37] L. Zhang, Z. Zhao, Q. Wu, H. Zhao, H. Xu, and X. Wu, “Energy-aware dynamic resource allocation in UAV assisted mobile edge computing over social internet of vehicles,” IEEE Access, vol. 6, pp. 56700–56715, 2018.

[38] F. Zhou, Y. Wu, R. Q. Hu, and Y. Qian, “Computation rate maximization in UAV-enabled wireless-powered mobile-edge computing systems,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 1927–1941, 2018.

[39] B. Yang, G. Mao, M. Ding, X. Ge, and X. Tao, “Dense small cell networks: From noise-limited to dense interference-limited,” IEEE Trans. Veh. Technol., vol. 67, no. 5, pp. 4262–4277, May 2018.

[40] A. Boumaalif and O. Zytoune, “Power distribution of device-to-device communications under nakagami fading channel,” IEEE Trans. Mobile Comput., vol. 21, no. 6, pp. 2158–2167, Jun. 2022.

[41] Z. Han, Z. Ji, and K. R. Liu, “Non-cooperative resource competition game by virtual referee in multi-cell OFDMA networks,” IEEE J. Sel. Areas Commun., vol. 25, no. 6, pp. 1079–1090, Aug. 2007.

[42] T. D. Burd and R. W. Brodersen, “Processor design for portable systems,” J. VLSI Signal Process. Syst. Signal Image Video Technol., vol. 13, no. 2, pp. 203–221, 1996.

[43] X. Dai, Z. Xiao, H. Jiang, and J. C. Lui, “UAV-assisted task offloading in vehicular edge computing networks,” IEEE Trans. Mobile Comput., vol. 23, no. 4, pp. 2520–2534, Apr. 2024.

[44] I. E. Grossmann and Z. Kravanja, Mixed-Integer Nonlinear Programming: A Survey of Algorithms and Applications. Berlin, Germany: Springer, 1997.

[45] F. Meshkati, H. V. Poor, and S. C. Schwartz, “Energy-efficient resource allocation in wireless networks,” IEEE Signal Process. Mag., vol. 24, no. 3, pp. 58–68, May 2007.

[46] M. Neely, Stochastic Network Optimization With Application to Communication and Queueing Systems. San Rafael, CA, USA: Morgan & Claypool Publishers, 2010.

[47] T. H. Cormen, C. E. Leiserson, R. L. Rivest, and C. Stein, Introduction to algorithms. Cambridge, MA, USA: MIT Press and McGraw-Hill, 3rd ed., 2009.

[48] N. Chen et al., “GainNet: Coordinates the odd couple of generative AI and 6G networks,” IEEE Netw., vol. 38, no. 5, pp. 56–65, Sep. 2024.

[49] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” in Proc. Adv. Neural Inf. Process. Syst., 2020, pp. 6840–6851.

[50] W. Xie et al., “Joint optimization of UAV-carried irs for urban low altitude mmWave communications with deep reinforcement learning,” 2025, arXiv:2501.02787.

![](images/d8f8561aa293b3c624c44a74d15210cff0f2ef57ae98daf6a6d00294b450ac5d.jpg)

Xin Tang received the BS and MS degrees from the Guilin University of Electronic Technology, Guilin, China, in 2011 and 2015, respectively, where he is currently working toward the PhD degree in information and communication engineering. Since 2015, he has been with the China Mobile Communications Corporation Guangxi Branch. In 2016, he joined the Institute of Information Technology, Guilin University of Electronic Technology, where he is currently a senior engineer. He was engaged in a graduate study abroad program at Nanyang Technological University, Singapore, from July 2024 to July 2025. His research interests include edge computing, multi-agent systems, UAV networks, and intelligent transportation systems.

![](images/00d77b83bfad1c03b7aa9ebdd8e8f0655c1f3eea9eb9f4b7ca46135819146edc.jpg)  
of Things systems.

Qian Chen received the BS and MS degrees from the Guilin University of Electronic Technology, Guangxi, China, in 2007 and 2012, respectively. From 2007 to 2015, she joined the Institute of Information Technology of Guilin University of Electronic Technology, where she is a full-time lecturer. Since 2016, she has been working with the Guilin University of Electronic Technology as a senior engineer with the School of Architecture and Transportation Engineering. Her current research interests include air-ground integrated networks, vehicular networks, and Internet

![](images/3a4151b6d26776fc81bc02f465b472bfaa145f6a8b78eb234d484a834051803f.jpg)  
Wenjie Weng received the BS degree from Jimei University, in Fujian, China, in 2023. He is currently working toward the MS degree with the Guilin University of Electronic Technology. His research interests include primarily focused on mobile edge computing, reinforcement learning, and generative artificial intelligence.

![](images/82f9d4c9b41f76e8a420ef18f3bf8961fbca72d8e4304baca68357c276446b57.jpg)

Geng Sun (Senior Member, IEEE) received the BS degree in communication engineering from Dalian Polytechnic University, and the PhD degree in computer science and technology from Jilin University, in 2011 and 2018, respectively. He was a visiting researcher with the School of Electrical and Computer Engineering, Georgia Institute of Technology, USA. He is a professor with the College of Computer Science and Technology, Jilin University, and his research interests include wireless networks, UAV communications, collaborative beamforming, and optimizations.

![](images/be55f84999aa820750fb92c9ea90c088a7df432ce68752d9ba81f57afdc494fe.jpg)

Chao Jin received the BS degree from the Beijing Institute of Technology, in 2023. He is currently working toward the MS degree with the Guilin University of Electronic Technology. His research interests are primarily focused on mobile edge computing, reinforcement learning, and generative artificial intelligence.

![](images/3b62c6b4944ad4a042699c13c911e4a287565d904416690002c4a12850390bb9.jpg)

![](images/e614bcc6eb35d74a613232604f2662e4358dfac8f1a07e3d4316ee8eda0b540b.jpg)

Xiaohuan Li (Member, IEEE) received the BS and MS degrees from the Guilin University of Electronic Technology, Guangxi, China, in 2006 and 2009, respectively, and the PhD degree from the South China University of Technology, Guangdong, China, in 2015. He was a visiting scholar with the Université de Nantes, France, in 2014. He is currently a professor with the School of Information and Communication, Guilin University of Electronic Technology and a research fellow with the National Engineering Laboratory of Application Technology of Integrated Trans-

Zhang Liu received the BE degree from the East China University of Science and Technology, Shanghai, China, in 2019. He is currently working toward the PhD degree with the School of Informatics and Communication Engineering, Xiamen University, Xiamen, China. He was a visiting Ph.D. student with the College of Computing and Data Science, Nanyang Technological University, Singapore, from 2023 to 2024. He served as the TPC chair member of the 2024 IEEE 35th Annual International Symposium on Personal, Indoor, and Mobile Radio Communiportation Big Data (Beihang University). His current research interests include wireless sensor networks, vehicular networks, UAV networks, and cognitive radios.

cations (PIMRC). He was awarded the Exemplary Reviewer by the IEEE Communications Society for Wireless Communications Magazine in 2024. His research interests include intelligent communications, vehicular networks, resource management, and reinforcement learning.

![](images/a460ea6ae2835ef7b12868201bd4644dc66696a6b234936df92f2ca89b5f7ef1.jpg)

![](images/4927943003153a6c11b818e1f8344566c86929faadef7da8992218f74b403dcc.jpg)

Dusit Niyato (Fellow, IEEE) received the BEng degree from the King Mongkuts Institute of Technology Ladkrabang (KMITL), Thailand, and the PhD degree in electrical and computer engineering from the University of Manitoba, Canada. He is a professor with the College of Computing and Data Science, Nanyang Technological University, Singapore. His research interests include the areas of mobile generative AI, edge intelligence, decentralized machine learning, and incentive mechanism design.

Jiacheng Wang received the MS and PhD degrees from the School of Communication and Information Engineering, Chongqing University of Posts and Telecommunications, in 2018 and 2022, respectively. From 2021 to 2022, he was a visiting researcher with the College of Computing and Data Science, Nanyang Technological University, Singapore, where he is now the postdoc research fellow. His research interests include generative AI, integrated sensing and communications, network optimization, and edge intelligence.