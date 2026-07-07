# Secure Low-altitude Maritime Communications via Intelligent Jamming

Jiawei Huang, Aimin Wang, Geng Sun, Senior Member, IEEE, Jiahui Li, Jiacheng Wang, Weijie Yuan, Senior Member, IEEE, Xianbin Wang, Fellow, IEEE

Abstract—Low-altitude wireless networks (LAWNs) have emerged as a viable solution for maritime communications. In these maritime LAWNs, uncrewed aerial vehicles (UAVs) serve as practical low-altitude platforms for wireless communications due to their flexibility and ease of deployment. However, the open and clear UAV communication channels make maritime LAWNs vulnerable to eavesdropping attacks. Existing security approaches often assume eavesdroppers follow predefined trajectories, which fail to capture the dynamic mobility patterns of eavesdroppers in realistic maritime environments. To address this challenge, we consider a low-altitude maritime communication system that employs intelligent jamming to counter dynamic eavesdroppers with uncertain positions to enhance the physical layer security. Since such a system requires balancing the conflicting performance metrics of the secrecy rate and energy consumption of UAVs, we formulate a secure and energy-efficient maritime communication multi-objective optimization problem (SEMCMOP). To solve this dynamic and long-term optimization problem, we first reformulate it as a partially observable Markov decision process (POMDP). We then propose a novel soft actor-critic with conditional variational autoencoder (SAC-CVAE) algorithm, which is a deep reinforcement learning algorithm improved by generative artificial intelligence. Specifically, the SAC-CVAE algorithm employs advantage-conditioned latent representations to disentangle and optimize policies, while enhancing computational efficiency by reducing the state space dimension. Simulation results demonstrate that our proposed intelligent jamming approach achieves secure and energy-efficient maritime communications. Furthermore, comparison results show that the proposed SAC-CVAE algorithm outperforms baseline methods across various eavesdropper movement patterns, simultaneously maximizing the secrecy rate and minimizing the energy consumption of UAVs.

Index Terms—Low-altitude maritime communications, physical layer security, UAV-assisted, multi-objective optimization, deep reinforcement learning.

## 1 INTRODUCTION

port offshore operations, navigation safety, and emergency responses [1]. Nevertheless, the deployment of terrestrial infrastructure in maritime environments faces significant challenges due to harsh marine conditions [2]. Consequently, various auxiliary platforms are deployed to facilitate maritime communications. For instance, satellites can provide wide-area coverage, enabling effective data exchange for vessels at sea [3]. Yet, satellites often suffer from significant propagation latency due to their long transmission distances. Meanwhile, low-altitude wireless networks (LAWNs) have demonstrated promising potential in maritime communications [4]. Specifically, rapidly deployable and highly mobile uncrewed aerial vehicles (UAVs) are well-suited for maritime LAWNs to enable on-demand coverage [5]. Unfortunately, the open and clear wireless channels of UAVs can be vulnerable to eavesdropping by malicious users, posing security risks [6]. Although conventional cryptography methods can mitigate security threats in certain scenarios [7], their complex key distribution and management processes introduce communication latency. Particularly, when handling large-scale data transmissions, these methods impose additional burdens on resourceconstrained maritime environments.

In this case, physical layer security (PLS) can be a promising alternative, which provides an adjustable mechanism through strategic power allocation and artificial noise distribution, thereby enabling adaptation to diverse communication security requirements [8]. For example, UAVs, as mobile jammers, enable dynamic coverage adaptation through rapid deployment and position optimization [9], enabling transmission of friendly-jamming signals to enhance PLS. Likewise, the authors in [10] introduced distributed collaborative beamforming into UAV swarms and handled eavesdropper collusion, thereby avoiding information leakage from known and unknown eavesdroppers. Moreover, the authors in [11] considered a dual UAV clusterassisted secure maritime communication system, in which one cluster transmits data signals while the other jams a remote eavesdropper. Nevertheless, these works considered static marine eavesdroppers, while neglecting their dynamic positional variations. The authors in [12] considered mobile eavesdroppers and used cooperative UAVs to regulate transmission rates, which enhances the secure performance of communication environments. However, this work assumes that the trajectories of eavesdroppers are predetermined, which may invalidate the method when the realtime eavesdropper positions are not known, thus potentially compromising the security mechanism. This leads us to further consider the need to estimate the dynamic and uncertain positions of eavesdroppers in UAV-assisted maritime PLS communication systems.

The implementation of such a system faces several critical challenges. First, the mobility of vessels and eavesdroppers induces dynamic wireless channel conditions, while uncertain eavesdropper trajectories complicate the system, rendering conventional offline optimization approaches (i.e., convex optimization and evolutionary computation) ineffective under time-varying maritime scenarios [13], [14]. In this case, deep reinforcement learning (DRL) algorithms can autonomously learn optimal policies through environmental interactions and enable real-time decision-making [15]. Second, we need to precisely control the 3D positions and transmit powers of cooperative UAVs to ensure system security. Such frequent position adjustments of UAVs significantly increase their energy consumption, which poses a trade-off between security performance and energy efficiency. Thus, traditional single-objective optimization frameworks (e.g., [16], [17]) are insufficient, necessitating a novel approach to capture this trade-off. Finally, our considered system focuses on a long-term trajectory optimization process that inherently demands precise characterization of multi-modal decision spaces, which further adds to system complexity. Therefore, an innovative approach is required to address dynamic uncertainties and multi-objective trade-offs optimization challenges in the maritime PLS communication system.

To overcome these challenges, we formulate a multiobjective optimization problem (MOP) and propose a generative AI (GenAI)-improved DRL algorithm. Our primary contributions are summarized as follows.

Intelligent Jamming for Low-altitude Maritime Communication System: We consider a low-altitude maritime communication system with dynamic and uncertain eavesdropper positioning, in which one UAV, as a relay, sends data signals to a marine vessel, and the other UAV, as a jammer, intelligently sends jamming signals to an eavesdropper. To the best of our knowledge, this work is the first to consider dynamic and uncertain eavesdropper trajectories and to design an intelligent jamming scheme for real-time maritime secure communications.

Dynamic and Long-term Multi-objective Optimization Problem Formulation: In the low-altitude maritime communication system, security performance and energy efficiency conflict with each other, exhibiting inherent trade-offs. In this case, we formulate a secure and energy-efficient maritime communication MOP (SEMCMOP) that simultaneously maximizes the secrecy rate and minimizes the energy consumption of UAVs. The SEMCMOP accounts for the sequential decision-making process of UAVs across time slots. Consequently, this dynamic and long-term problem requires balancing immediate and sustainable performance rewards throughout the mission duration, which further complicates this problem.

Improved DRL Algorithm by Incorporating GenAI: Given the NP-hard complexity and dynamics of the formulated SEMCMOP, we propose a novel soft actor-critic with conditional variational autoencoder (SAC-CVAE) algorithm, which incorporates GenAI capabilities to solve the problem. Specifically, we first transform the problem into a partially observable Markov decision process (POMDP). Then, the SAC-CVAE algorithm can disentangle and optimize policies through an advantage-conditioned latent representation while enhancing computational efficiency by reducing state space dimension via a long shortterm memory (LSTM)-assisted prediction mechanism.

Performance Evaluations and Analyses: Simulation results demonstrate that the proposed intelligent jamming approach can achieve secure and energyefficient maritime communications compared with the non-jamming approach. Moreover, comparison results show that our proposed SAC-CVAE algorithm outperforms other conventional DRL algorithms across various eavesdropper movement patterns, maximizing the secrecy rate and minimizing the energy consumption of UAVs. In addition, performance in the extended scenario further demonstrates the effectiveness and robustness of the proposed SAC-CVAE algorithm.

The rest of this paper is structured as follows: Section 2 reviews the related work. Section 3 presents the models and preliminaries. Section 4 formulates and analyzes the SEMC-MOP. The GenAI-improved DRL algorithm is proposed in Section 5. Section 6 illustrates the simulation results. Section 7 presents some discussions and Section 8 concludes the overall work.

## 2 RELATED WORK

In this section, we present a review of relevant work related to UAV-assisted maritime communications, security mechanisms for maritime networks, and optimization approaches. Moreover, we summarize the differences between related works and this work in Table 1.

## 2.1 UAV-assisted Maritime Communications

Rapidly expanding maritime activities necessitate increasingly reliable maritime communications. Given the high costs and technical challenges of deploying fixed infrastructure across vast ocean areas, auxiliary platforms serve as practical alternatives [36]. For example, the authors in [18] developed an intelligent spectrum-sharing scheme for satellite-maritime integrated networks, improving throughput and spectral efficiency. Moreover, the authors in [19] investigated the distributions of aggregated interference with uplink power control to maximize the probability of effective coverage in satellite-maritime networks. While satellite networks provide wide coverage, they introduce substantial propagation delays that particularly challenge real-time applications. Furthermore, the authors in [20] demonstrated a multi-antenna uncrewed surface vehicle (USV) system to maximize sum throughput through cooperative beamforming and optimal trajectory planning. However, sea surface reflections cause multipath effects that deteriorate the quality of received signals, while wave-induced platform oscillations degrade antenna alignment [21].

TABLE 1  
Comparison between related works and this work
<table><tr><td rowspan=1 colspan=3></td><td rowspan=1 colspan=1>Scenarios</td><td rowspan=1 colspan=2>Security</td><td rowspan=1 colspan=2>Optimization objectives</td><td rowspan=1 colspan=1>Methods</td></tr><tr><td rowspan=1 colspan=3>Reference</td><td rowspan=1 colspan=1>Maritime</td><td rowspan=1 colspan=1>UAV-assisted PLS</td><td rowspan=1 colspan=1>Uncertain eavesdropperpositions</td><td rowspan=1 colspan=1>Secrecy rate</td><td rowspan=1 colspan=1>Energy consumption</td><td rowspan=1 colspan=1>DRL</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>[18]</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>[19]</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>[20]</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>[21]</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>[22]</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>[23]</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>24]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>25]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>26]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>27]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=2>[28]</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=2>29]</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[30]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>31]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>32]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[33]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td></tr><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>[34]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=1>[</td><td rowspan=1 colspan=1>35]</td><td rowspan=1 colspan=1></td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>X</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>X</td></tr><tr><td rowspan=1 colspan=3>This work</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td><td rowspan=1 colspan=1>√</td></tr></table>

In recent years, LAWNs have emerged as an effective solution for maritime communications [4]. Specifically, UAVs, with exceptional operational flexibility and rapid deployment capabilities, can be integrated into LAWNs to address the challenges of infrastructure deployment in marine environments [22]. For instance, the authors in [23] incorporated UAVs into maritime communication networks (MCNs) to complement shore base stations with limited coverage, thereby improving wireless connectivity and resource efficiency. In [24], the authors developed a twolayer UAV-based maritime communication mobile edge computing (MEC) network to minimize latency for both communication and computation. Moreover, the authors in [25] utilized UAVs to form a cognitive mobile computing network for cooperative search and rescue at sea, enhancing communication throughput. Note that the open and clear wireless channels of UAVs make them extremely vulnerable to eavesdropping attacks during data transmission. However, the aforementioned studies focused on communication efficiency and overlooked this critical security risk.

## 2.2 Security Mechanisms of Maritime Networks

To address the security risks in maritime networks, researchers have recently explored various security mechanisms [37]. For example, the authors in [26] provided a routing protocol to enhance inter-UAV communication efficiency while introducing digital twin technology to guarantee network security. Moreover, the authors in [27] presented a federated privacy-preserving framework for UAV data collection to optimize autonomous path planning and protect sensitive maritime information. However, these cryptography methods require significant computational resources when processing large-scale data. The resulting power demands and transmission latency make such methods inadequate for maritime missions requiring real-time communications.

In this case, the PLS mechanism enables dynamic adjustment of protective measures in response to channel characteristics, thereby ensuring reliable and secure maritime communications [28]. Meanwhile, highly mobile and flexible UAVs can serve as friendly-jamming platforms for security enhancement. For instance, the authors in [29] utilized UAVs to form a maritime UAV-enabled virtual antenna array that transmits jamming signals to achieve PLS communications. However, this work considered static eavesdroppers, limiting its applicability in real-world maritime scenarios where threats are typically mobile. Furthermore, the authors in [30] proposed an efficient communication scheme for UAV-relayassisted maritime MEC with a moving eavesdropper to maximize the secure computing capacity. In addition, the authors in [31] investigated a UAV-reconfigurable intelligent surface (RIS)-assisted maritime communication system, maximizing energy efficiency while guaranteeing the quality of service requirements against jamming attacks. Nevertheless, the aforementioned works have a common limitation of assuming predefined eavesdropper trajectories. This assumption disregards the randomness and adaptability of eavesdropper movements, causing performance degradation when the exact positions of eavesdroppers are unknown in real-world scenarios.

## 2.3 Optimization Approaches

Several approaches have been proposed to achieve UAVassisted secure maritime communications. For instance, the authors in [21] investigated a dual-UAV secure communication system and employed a problem decomposition methodology to optimize UAV parameters. However, this method leads to suboptimal solutions, as it treats interconnected system parameters independently. Furthermore, DRL algorithms are common and effective methods for dealing with dynamic optimization problems [38]. For example, the authors in [32] proposed an MCN with aerial RISassisted UAVs against jamming, while designing a novel penalized DRL algorithm to maximize energy efficiency. Moreover, the authors in [33] proposed a UAV relay policy based on reinforcement learning for maritime communications to resist jamming attacks and reduce energy consumption. However, the aforementioned works often treated energy as a constraint and overlooked the complex trade-offs between security and energy consumption, which makes it difficult to obtain appropriate solutions under different energy priority conditions.

To achieve the complex trade-off among competing considerations, the MOP framework offers a mathematical foundation to simultaneously optimize multiple conflicting objectives. This framework enables systematic modeling of objective relationships and identification of optimal compromise solutions under varying conditions [39]. For example, the authors in [34] considered a UAV-enabled secure communication system and formulated an MOP to maximize the worst-case secrecy rate and minimize the energy consumption of UAVs to achieve trade-offs. In addition, the authors in [35] considered a multi-UAV-assisted MEC system and formulated an MOP to meet the computation-intensive and delay-sensitive demands of users. Note that dynamic maritime communication systems require real-time responses to changing wireless channel conditions to ensure reliable signal transmission. However, the aforementioned works employed evolutionary computation methods, which exhibit excessive computational latency and are inadequate for real-time adaptation in such scenarios.

In summary, different from previous works, we consider an intelligent jamming scheme for a low-altitude maritime communication system with dynamic and uncertain eavesdropper positioning. Accordingly, we propose a novel approach to solve the optimization problem that requires balancing conflicting objectives while enabling fast response to changing conditions.

## 3 MODELS AND PRELIMINARIES

In this section, we first consider the low-altitude maritime communication system with dynamic and uncertain eavesdropper positioning. Then, we introduce the vessel movement model and eavesdropping UAV movement model. Subsequently, we present the corresponding communication model. Finally, the energy consumption model of the UAV is introduced. Note that the main notations are shown in Table 2.

TABLE 2  
Main notations
<table><tr><td>Notation</td><td>Definition</td></tr><tr><td></td><td>Notations in the system model</td></tr><tr><td> $A _ { m }$ </td><td>Added mass matrix</td></tr><tr><td> $a _ { r }$ </td><td>Area of the rotor disks</td></tr><tr><td> $\beta _ { U , V }$ </td><td>Path loss of the U2V link</td></tr><tr><td> $\beta _ { U , U }$ </td><td>Path loss of the U2U link</td></tr><tr><td> $c _ { d }$ </td><td>Drag coefficient of the airframe</td></tr><tr><td> $\mathcal { C } _ { U , V }$ </td><td>Composite channel of the U2V link</td></tr><tr><td> $C ( v )$ </td><td>Coriolis coefficient matrix</td></tr><tr><td> $d _ { U , V }$ </td><td>Distance between the UAV and vessel</td></tr><tr><td> $d _ { U , U }$ </td><td>Distance between UAVs</td></tr><tr><td> ${ \pmb D } ( { \pmb v } )$ </td><td>Damping coefficient matrix</td></tr><tr><td> $\lambda _ { \pi }$ </td><td>Gradient parameter of policy network</td></tr><tr><td> $\lambda _ { Q }$ </td><td>Gradient parameter of value network</td></tr><tr><td> $\lambda _ { V }$ </td><td>Gradient parameter of state-value network</td></tr><tr><td> $P _ { A }$ </td><td>Transmit power of Alice</td></tr><tr><td> $P _ { B }$ </td><td>Transmit power of Bob</td></tr><tr><td> $r _ { r }$ </td><td>Rotor solidity</td></tr><tr><td> $\scriptstyle { R _ { m } }$ </td><td>Rigid-body mass matrix</td></tr><tr><td> $s _ { m }$ </td><td>Mean induced flow speed</td></tr><tr><td> $s _ { r }$ </td><td>Tip speed of the rotating blades</td></tr><tr><td> $v _ { h }$ </td><td>UAV horizontal velocity</td></tr><tr><td> $v _ { v }$ </td><td>UAV vertical velocity</td></tr><tr><td> $v _ { f }$ </td><td>UAV forward velocity</td></tr><tr><td> $\rho$   $\varsigma$ </td><td>Atmospheric density</td></tr><tr><td></td><td>Gaussian random variable of the U2V link</td></tr><tr><td> $\boldsymbol { A }$ </td><td>Notations in the algorithm</td></tr><tr><td> $_ \alpha$ </td><td>Action space set</td></tr><tr><td> $\mathbf { c }$ </td><td>Temperature parameter of SAC</td></tr><tr><td> $\mathcal { D }$ </td><td>State-advantage condition of the CVAE</td></tr><tr><td> $\textit { \textbf { \ i } }$ </td><td>Replay buffer</td></tr><tr><td> $L S T M _ { f }$ </td><td>Coefficient for the KL-divergence loss term</td></tr><tr><td> $L S T M _ { i }$ </td><td>Forget gate of the LSTM network</td></tr><tr><td></td><td>Input gate of the LSTM network</td></tr><tr><td> $L S T M _ { o }$   $\scriptscriptstyle \mathcal { O }$ </td><td>Output gate of the LSTM network</td></tr><tr><td></td><td>Observation space set</td></tr><tr><td> $\omega _ { m }$ </td><td>Weights for the optimization objective m</td></tr><tr><td> $p _ { \delta }$   $\pi \Phi$ </td><td>Decoder of the CVAE</td></tr><tr><td> $q _ { \varphi }$ </td><td>Tractable policy Encoder of the CVAE</td></tr><tr><td> $Q _ { \theta }$ </td><td></td></tr><tr><td> $\mathcal { R }$ </td><td>Soft Q-value network Reward value</td></tr><tr><td> $s$ </td><td>Global state space set</td></tr><tr><td> $V _ { \psi }$ </td><td>State-value network</td></tr><tr><td> $Z$ </td><td>Storage length of the historical trajectory sequence</td></tr><tr><td> $\zeta$ </td><td>Advantage value of the CVAE</td></tr><tr><td> $\zeta ^ { * }$ </td><td></td></tr><tr><td></td><td>Maximum advantage value of the CVAE</td></tr><tr><td> $_ { z }$ </td><td>Latent representation of the CVAE</td></tr></table>

## 3.1 System Overview

As shown in Fig. 1, we consider a low-altitude maritime communication system with dynamic and uncertain eavesdropper position, which includes a marine user (MU), a legitimate UAV denoted as Alice, an illegitimate UAV denoted as Eve, and an assisted UAV denoted as Bob. Specifically, an MU may not be able to receive signals from base stations or other long-range users due to the challenges in deploying infrastructure at sea [31]. In such cases, UAVs, with their high mobility and flexibility, serve as efficient low-altitude platforms to forward data to MUs. However, the open and clear channels of UAVs make data signals susceptible to eavesdropping by Eve, whose position is dynamic and uncertain. In this case, another mobile UAV at sea, i.e., Bob, can act as a friendly jammer to jam Eve, so that ensuring

![](images/2dfd562e179e03252bb0abc675ac9f0de3896805ad36410219496ed253704f7b.jpg)  
Fig. 1. A low-altitude maritime communication system with dynamic and uncertain eavesdropper positioning.

data security and integrity.

Without loss of generality, we divide the total serving time T into N time slots with equal duration $d _ { n } = T / N _ { . }$ denoted by the set <sup>N</sup> $\triangleq \{ 1 , 2 , \ldots \} _ { N } \}$ . An MU follows its navigation trajectory, and Alice sends signals through the data link. When Eve attempts to obtain data from Alice via the eavesdropping link, Bob sends jamming signals to Eve to degrade the eavesdropping channel and ensure the security of the data signals. Additionally, the MU navigates along a specified route. However, due to the dynamic and uncertain flight path of Eve, its complete position cannot be obtained in advance. Thus, it is crucial to determine the position of Eve to ensure the effectiveness of the jamming strategy.

In the communication process, we use the threedimensional (3D) Cartesian coordinate system to represent the time-varying locations of the MU, Alice, Eve, and Bob at time slot n as $\check { ( x _ { M } [ n ] ,  y _ { M } [ n ] , z _ { M } [ n ] ) } , ( x _ { A } [ n ] , y _ { A } [ n ] , z _ { A } [ n ] )$ $( x _ { E } [ n ] , y _ { E } [ n ] , z _ { E } [ n ] )$ , and $( x _ { B } [ n ] , y _ { B } [ n ] , z _ { B } [ n ] )$ , respectively. Note that the jamming signals may interfere with an MU, affecting the effective reception of the data. To evaluate this interference and optimize system performance, we next provide the vessel movement model, eavesdropping UAV movement model, and communication model.

## 3.2 Vessel Movement Model

The movement of a vessel is often described by using two 3D right-handed Cartesian coordinate systems [40]. The first is a normal coordinate system, denoted as n, where the origin is placed on the sea surface, $x , \ y ,$ and z axes are aligned with the north, east, and downward directions, respectively. The second system, denoted as ${ \mathfrak { g } } ,$ is fixed relative to the vessel, with the origin at the center of gravity, and $x ^ { \mathfrak { g } } , y ^ { \mathfrak { g } }$ , and $z ^ { \mathfrak { g } }$ axes pointing toward the bow, starboard, and downward, respectively. Moreover, rotation around the $x ^ { { \mathfrak { g } } } .$ $y ^ { { \mathfrak { g } } }$ , and $z ^ { \mathfrak { g } }$ axes corresponds to the roll (ϕ), pitch (θ), and yaw (ψ) of the vessel. The rotations are represented by the Euler angle vector $\boldsymbol { \Omega } ~ = ~ [ \phi , \theta , \psi ] ^ { T }$ . In addition, the movement of the vessel is modeled by using a six-degree-of-freedom system $\langle x , y , z , \phi , \theta , \psi \rangle$ , which mathematically captures the spatial dynamics, and it is expressed by [41]

$$
\dot { \mathbf { \Upsilon } } \dot { \mathbf { \Upsilon } } ( n ] = \mathbf { \Gamma } \mathbf { \Gamma } ( \Omega [ n ] ) \mathbf { \pmb { v } } [ n ] ,\tag{1}
$$

where the vector ${ \mathfrak {Upsilon } } [ n ] = [ x [ n ] , y [ n ] , z [ n ] , \phi [ n ] , \theta [ n ] , \psi [ n ] ] ^ { T }$ is the displacement and rotational state at time slot $n ,$ and $\pmb { v } [ n ] = [ \hat { v _ { x } } [ n ] , v _ { y } [ n ] , v _ { z } [ n ] , v _ { \phi } [ n ] , v _ { \theta } [ n ] , v _ { \psi } [ n ] ] ^ { T }$ describes the translational and rotational velocities at the same time. Moreover, the derivative of $\mathbf { \boldsymbol { \Upsilon } } ( n ]$ , denoted as ${ \dot { \mathbf { Y } } } [ n ]$ , represents the rate of change of the location and orientation, and the matrix Γ describes the transformation between the horizontal plane of {g} and $\{ \mathfrak { n } \}$ . Additionally, the velocity vector is influenced by the following external factors, which can be described by

$$
\begin{array} { r l r } {  { ( { \pmb { R } } _ { m } + { \pmb { A } } _ { m } ) { \pmb { \dot { v } } } [ n ] + C ( { \pmb { v } } [ n ] ) { \pmb { v } } [ n ] + D ( { \pmb { v } } [ n ] ) { \pmb { v } } + { \pmb { r } } ( { \pmb { \Upsilon } } ) } } \\ & { } & { = \pmb { \iota } _ { w } + \pmb { \iota } _ { o } + \pmb { \iota } _ { w a } + \pmb { \iota } _ { t } [ n ] , } \end{array}\tag{2}
$$

where $\scriptstyle { R _ { m } }$ and $A _ { m }$ are the rigid-body and added mass matrices, respectively, and $C ( v )$ and $D \bar { ( \boldsymbol { v } ) }$ denote the Coriolis and damping coefficient matrices, respectively. Moreover, $\dot { \pmb v } [ n ]$ denotes the time derivative of the velocity vector $_ { v , }$ and $r ( \Upsilon )$ is the resilience. Additionally, the vectors $\scriptstyle \prime \ w ,$ ι<sub>o</sub>, and $\scriptstyle \pmb { \iota } _ { w a }$ represent the forces exerted on the vessel by the wind, ocean currents, and waves, respectively, and $\pmb { \iota } _ { t } [ n ]$ corresponds to the thrust generated by the vessel thrusters at time slot n.

The spatial relationship between the vessel and UAV influences the effect of data transmission, and dynamic wireless channel conditions impact the signal reception effectiveness. Therefore, we proceed to introduce the communication model.

## 3.3 Eavesdropping UAV Movement Model

The mobility pattern of the eavesdropping UAV (Eve) employs a memory-based random walk model, which is a common model for simulating the real-world user mobility and encapsulating its temporal dependencies [42]. Specifically, the current velocity and direction of Eve are determined by its previous velocity and direction, thereby establishing the correlations across consecutive time slots, and the velocity and direction of Eve follow a Gauss-Markov stochastic process as follows [43]:

$$
v _ { E } [ n ] = l _ { g } v _ { E } [ n - 1 ] + ( 1 - l _ { g } ) \xi + \sqrt { ( 1 - l _ { g } ^ { 2 } ) } J _ { g } [ n - 1 ] ,\tag{3a}
$$

$$
\Theta _ { E } [ n ] = l _ { g } \Theta _ { E } [ n - 1 ] + ( 1 - l _ { g } ) \xi + \sqrt { ( 1 - l _ { g } ^ { 2 } ) } J _ { g } [ n - 1 ] ,\tag{3b}
$$

where $v _ { E } [ n ]$ and $v _ { E } [ n - 1 ]$ denote the velocities of Eve at time slots n and $n - 1$ , respectively, $\Theta _ { E } [ n ]$ and $\Theta _ { E } [ n - 1 ]$ denote the moving directions of Eve at time slots n and n−1, respectively, $l _ { g } \in \mathsf { \Gamma } ( 0 , 1 )$ represents the memory level, and ξ is the asymptotic mean. Moreover, $J _ { g }$ is an independent, uncorrelated, and stationary Gaussian process with zero mean and variance $\sigma _ { g } ^ { 2 } .$

## 3.4 Communication Model

This system focuses on two primary communication links, involving the UAV-to-vessel (U2V) link and UAV-to-UAV (U2U) link. Specifically, the Alice-to-MU data link of the U2V link is used for sending data signals, which could be eavesdropped on by Eve. Meanwhile, the Bob-to-Eve jamming link of the U2U link is designed to jam Eve, potentially interfering with the effective data reception of the MU. The detailed processes are described as follows.

## 3.4.1 U2V Link to the MU

The U2V link is established based on channel state information (CSI), which can be obtained from the intended flight trajectories of Alice and Bob, and the precalculated location of the MU. Moreover, since the antenna height at UAVs is much higher than that at vessels, the path loss of the U2V link at time slot n can be calculated by

$$
\beta _ { U , V } [ n ] [ d B ] = 1 0 I _ { r } \log _ { 1 0 } \left( \frac { d _ { U , V } [ n ] } { d _ { r } } \right) + \varsigma _ { U , V } [ n ] + P _ { d } ,\tag{4}
$$

where $d _ { U , V } [ n ]$ denotes the distance between the UAV and MU at time slot $n ,$ and $\varsigma { U , V } [ n ]$ is a zero-mean Gaussian random variable with standard deviation $\sigma _ { X v } ,$ , which can reflect wave-induced fading situations [44]. Moreover, $I _ { r }$ is the relevant index, and $P _ { d }$ denotes the parameter for the reference distance $d _ { r }$ . Note that $\beta _ { A , M } [ n ]$ and $\beta _ { B , M } [ n ]$ denote the path losses from Alice and Bob to the MU at time slot $n ,$ respectively.

Then, the composite channel of the U2V link at time slot n can be denoted as follows:

$$
\mathcal { C } _ { U , V } [ n ] = \sqrt { \beta _ { U , V } [ n ] } \left( \sqrt { \frac { F _ { V } } { 1 + F _ { V } } } + \sqrt { \frac { 1 } { 1 + F _ { V } } } h _ { U , V } [ n ] \right) ,\tag{5}
$$

where $F _ { V }$ indicates the Rician factor, which is influenced by sea-surface reflection effect [44], and $h _ { U , V } [ n ] \in \mathcal { C N } ( 0 , 1 )$ Moreover, $\mathcal { C } _ { A , M } [ n ]$ and ${ \mathcal { C } } _ { B , M } [ n ]$ denote the channels from Alice and Bob to the MU at time slot n, respectively.

## 3.4.2 U2U Link to Eve

Given that the U2U link operates in an aerial environment, its signal propagation follows the free-space path loss model, which is expressed mathematically as follows [45]:

$$
\beta _ { U , U } [ n ] [ d B ] = 2 0 \log _ { 1 0 } ^ { ( d _ { U } , \upsilon [ n ] ) } + 2 0 \log _ { 1 0 } ^ { f _ { c } } + 2 0 \log _ { 1 0 } ^ { \frac { 4 \pi } { 3 0 0 } } ,\tag{6}
$$

where $d _ { U , U } [ n ]$ represents the distance between UAVs at time slot n in kilometer (km), and $f _ { c }$ is the carrier frequency in MHz. Note that $\beta _ { A , E } [ n ]$ and $\beta _ { B , E } [ n ]$ are the path losses from Alice and Bob to Eve at time slot $n ,$ respectively.

Based on the U2V and U2U links, the achievable rate of the MU at time slot n can be calculated by

$$
R _ { M } [ n ] = \log _ { 2 } \left( 1 + \frac { P _ { A } [ n ] G _ { A } \left. \mathcal { C } _ { A , M } [ n ] \right. ^ { 2 } } { P _ { B } [ n ] G _ { B } \left. \mathcal { C } _ { B , M } [ n ] \right. ^ { 2 } + \sigma ^ { 2 } } \right) ,\tag{7}
$$

where $P _ { A } [ n ]$ and $P _ { B } [ n ]$ are the transmit powers of Alice and Bob at time slot $n ,$ respectively. Moreover, $G _ { A }$ and $G _ { B }$ denote the antenna gains of Alice and Bob, respectively, and $\sigma ^ { 2 }$ is the additive white Gaussian noise power.

Likewise, the achievable rate of Eve at time slot n is expressed by

$$
R _ { E } [ n ] = \log _ { 2 } \left( 1 + \frac { P _ { A } [ n ] G _ { A } \beta _ { A , E } [ n ] } { P _ { B } [ n ] G _ { B } \beta _ { B , E } [ n ] + \sigma ^ { 2 } } \right) .\tag{8}
$$

Then, we define the immediate secrecy rate of the system, which can be expressed as:

$$
C _ { s } [ n ] = [ R _ { M } [ n ] - R _ { E } [ n ] ] ^ { + } ,\tag{9}
$$

where $C _ { s } [ n ]$ is non-negative, and $[ \chi ] ^ { + } \triangleq m a x ( 0 , \chi )$

Based on the preceding analysis, the controllable 3D locations and transmit powers of Alice and Bob are critical factors to ensure secure maritime communications. During communications, Alice dynamically adapts to the mobile MU, while Bob repositions relative to Eve and MU to optimize jamming effectiveness. These continuous adjustments incur energy costs, requiring careful management for sustained UAV operation. Consequently, we next present the energy consumption model of the UAV.

## 3.5 Energy Consumption Model of the UAV

At each time slot $n ,$ the UAV determines movement by executing a 3D action vector $\boldsymbol { \mathcal { A } } [ \boldsymbol { n } ] = ( A _ { x } [ n ] , A _ { y } [ n ] , A _ { z } [ n ] )$ Specifically, the locational coordinates of the UAV $( { \dot { x } } _ { U } [ n ] , y _ { U } { \dot { [ n ] } } , z _ { U } [ n ] )$ are subsequently updated by using the displacement increment $\dot { \mathcal { A } } [ n ]$ , which is derived from the previous location. The iterative process $( x _ { U } [ n ] , y _ { U } [ n ] , z _ { U } [ \dot { n } ] ) = ( x _ { U } [ n - 1 ] , y _ { U } [ n - 1 ] , z _ { U } [ n - 1 ] ) + A [ n ]$ governs the trajectory of the UAV.

Then, we introduce the energy consumption of the UAV. Specifically, the total energy expenditure of UAVs is categorized into propulsion energy and communication energy. As demonstrated in [46], the propulsion energy dominates the total energy, while communication-related energy consumption can be negligible by comparison. Consequently, we adopt the propulsion power model for calculating the energy consumption of the UAV during horizontal motion, which is denoted as follows:

$$
\begin{array} { c } { { P _ { U } ( v _ { h } [ n ] ) = P _ { I } \displaystyle \left[ \left( 1 + \frac { v _ { h } ^ { 4 } [ n ] } { 4 s _ { m } ^ { 4 } } \right) ^ { \frac { 1 } { 2 } } - \frac { v _ { h } ^ { 2 } [ n ] } { 2 s _ { m } ^ { 2 } } \right] ^ { \frac { 1 } { 2 } } + P _ { p } } } \\ { { + \displaystyle \frac { 3 P _ { B } v _ { h } ^ { 2 } [ n ] } { s _ { r } ^ { 2 } } + \frac { v _ { h } ^ { 3 } [ n ] c _ { d } r _ { r } a _ { r } \rho } { 2 } , } } \end{array}\tag{10}
$$

where $v _ { h } [ n ] ~ = ~ \sqrt { ( A _ { x } [ n ] ) ^ { 2 } + ( A _ { y } [ n ] ) ^ { 2 } } / d _ { n }$ represents the UAV horizontal velocity at time slot n. Moreover, $P _ { I }$ and $P _ { p }$ are the induced power and blade profile power, respectively, and $s _ { r }$ and $s _ { m }$ denote the tip speed of the rotating blades and mean induced flow speed through the rotor disk, respectively. In addition, $c _ { d } , r _ { r } , a _ { r } ,$ , and $\rho$ denote the drag coefficient of the airframe, rotor solidity, area of the rotor disks, and atmospheric density, respectively.

Our model excludes energy consumption during the acceleration and deceleration phases of UAVs, as the transient phases constitute a negligible portion of the total operational duration [47]. Thus, we employ a simplified approximation model to quantify the energy consumption of UAVs in 3D flying paths, which integrates the propulsion energy for sustained flight, kinetic energy during velocity adjustments, and gravitational energy. The energy consumption of a UAV operating in 3D space is denoted by [35]

$$
\begin{array} { c } { { E _ { U } ( N ) \approx \displaystyle \int _ { 0 } ^ { N } P _ { U } \left( v _ { h } [ n ] \right) d n + \frac { 1 } { 2 } m _ { U } \left( v _ { f } [ N ] ^ { 2 } - v _ { f } [ 0 ] ^ { 2 } \right) } } \\ { { + m _ { U } g \left( h _ { U } [ N ] - h _ { U } [ 0 ] \right) , } } \end{array}\tag{11}
$$

where $v _ { f } [ n ] = \sqrt { v _ { h } ^ { 2 } [ n ] + v _ { v } ^ { 2 } [ n ] }$ represents the forward velocity of the UAV at time slot n, of which $v _ { v } [ n ] = | A _ { z } [ n ] | / d _ { n }$ is the vertical velocity of the UAV at the same time. Additionally, m<sub>U</sub> and g represent the mass of the UAV and gravitational acceleration, respectively, and $h _ { U } [ n ]$ denotes the flight height of the UAV at time slot n.

## 4 PROBLEM FORMULATION AND ANALYSES

In this section, we first present the problem statement, then formulate the optimization problem, and proceed with problem analyses.

## 4.1 Problem Statement

Given the challenges of deploying communication infrastructure at sea, the flexible UAV serves as a low-altitude auxiliary platform to facilitate signal transmission to the vessel. However, the signals are vulnerable to eavesdropping by an illegitimate UAV. In this case, another assisted UAV can send jamming signals toward the eavesdropper, thereby degrading the eavesdropping channel and enabling secure maritime communications. However, the jamming signals might interfere with the vessel. To address this issue, we need to precisely control jamming signals, enhancing the effect on the eavesdropper while minimizing interference with the vessel. Therefore, we aim to maximize the secrecy rate of the system.

Since the vessel follows its engine-determined routes and executes specific tasks, its location cannot be controlled. Moreover, the location of an external hostile eavesdropper is inherently unmanageable. Therefore, the achievable rates of the MU and Eve are controlled by 3D locations and transmit powers of both Alice and Bob. Note that adjusting the 3D locations of the UAVs leads to increased energy consumption. Thus, minimizing the locational adjustments of UAVs is crucial for improving overall energy efficiency.

Combining the aforementioned factors, the decision variables to be jointly optimized are the following parameters: (i) $\mathbb { L } _ { A } = \{ \mathbb { X } _ { A } , \mathbb { Y } _ { A } , \mathbb { Z } _ { A } \}$ denotes the 3D location set of Alice over N time slots, where $\mathbb { X } _ { A } \ = \ \left\{ x _ { A } [ n ] \right\} _ { n = 1 } ^ { N } , \ \mathbb { Y } _ { A } \ =$ $\left\{ y _ { A } [ n ] \right\} _ { n = 1 } ^ { N } ,$ and $\mathbb { Z } _ { A } = \left\{ z _ { A } [ n ] \right\} _ { n = 1 } ^ { N } . ~ ( i i ) ~ \mathbb { P } _ { A } = \left\{ P _ { A } [ n ] \right\} _ { n = 1 } ^ { N }$ is the transmit power of Alice over N time slots. (iii) <sup>L</sup><sub>B</sub> $\mathbf { \Psi } = \left\{ \mathbb { X } _ { B } , \mathbb { Y } _ { B } , \mathbb { Z } _ { B } \right\}$ denotes the 3D location set of Bob over N time slots, where $\mathbb { X } _ { B } = \left\{ x _ { B } [ n ] \right\} _ { n = 1 } ^ { N } , \mathbb { Y } _ { B } = \left\{ y _ { B } [ n ] \right\} _ { n = 1 } ^ { N } ,$ and $\mathbb { Z } _ { B } = \left\{ z _ { B } [ n ] \right\} _ { n = 1 } ^ { N } . \left( i v \right) \mathbb { P } _ { B } = \left\{ P _ { B } [ n ] \right\} _ { n = 1 } ^ { N }$ is the transmit power of Bob over N time slots.

## 4.2 Problem Formulation

In our considered system, we focus on the following optimization objectives simultaneously.

Optimization Objective 1: To achieve secure lowaltitude maritime communications, the first optimization objective is to maximize the total secrecy rate of the system over N time slots, which is expressed by

$$
f _ { 1 } ( \mathbb { L } _ { A } , \mathbb { P } _ { A } , \mathbb { L } _ { B } , \mathbb { P } _ { B } ) = \sum _ { n = 1 } ^ { N } C _ { s } [ n ] .\tag{12}
$$

Optimization Objective 2: The achievement of the above objective requires frequent adjustments to the positions of Alice and Bob, which consumes their energy. Given the limited energy supply available at sea, the second objective is to minimize the total energy consumption of Alice and Bob over N time slots as follows:

$$
f _ { 2 } ( \mathbb { L } _ { A } , \mathbb { L } _ { B } ) = \sum _ { n = 1 } ^ { N } \left( E _ { A } [ n ] + E _ { B } [ n ] \right) ,\tag{13}
$$

where $E _ { A } [ n ]$ and $E _ { B } [ n ]$ are the energy consumptions of Alice and Bob at time slot n, respectively.

The abovementioned two optimization objectives are conflicting. Specifically, we need to control the positions of Alice and Bob to maximize the secrecy rate of the system, which conflicts with minimizing their energy consumption. Moreover, based on Eq. (10), higher UAV velocity results in increased energy consumption, while lower velocity prolongs communication time and increases hovering energy consumption. Therefore, the two optimization objectives conflict with each other, necessitating an appropriate modeling method to balance this conflict. In this case, the MOP modeling provides a mathematical framework that simultaneously optimizes multiple conflicting objectives [39], which is well-suited for capturing trade-offs and can be used to formulate our problem.

Accordingly, we formulate the SEMCMOP as follows:

$$
\operatorname* { m i n } _ { \left\{ \mathbb { L } _ { A } , \mathbb { P } _ { A } , \mathbb { L } _ { B } , \mathbb { P } _ { B } \right\} } F = \left\{ - f _ { 1 } , f _ { 2 } \right\} ,\tag{14a}
$$

$$
\mathrm { s . t . } C 1 : \mathbb { L } _ { A m i n } \leq \mathbb { L } _ { A } [ n ] \leq \mathbb { L } _ { A m a x } , \forall n \in \mathbb { N } ,\tag{14b}
$$

$$
C 2 : P _ { m i n } \leq P _ { A } [ n ] \leq P _ { m a x } , \forall n \in \mathbb { N } ,\tag{14c}
$$

$$
C 3 : \mathbb { L } _ { B m i n } \leq \mathbb { L } _ { B } [ n ] \leq \mathbb { L } _ { B m a x } , \forall n \in \mathbb { N } ,\tag{14d}
$$

$$
C 4 : P _ { m i n } \leq P _ { B } [ n ] \leq P _ { m a x } , \forall n \in \mathbb { N } ,
$$

$$
C 5 : R _ { M } [ n ] > R _ { m i n } , \forall n \in \mathbb { N } ,\tag{14e}
$$

$$
C 6 : \textstyle \sum _ { n = 1 } ^ { N } P _ { { \cal A } } [ n ] \le P _ { T } , \forall n \in \mathbb { N } ,\tag{14f}
$$

$$
C 7 : \textstyle \sum _ { n = 1 } ^ { N } P _ { B } [ n ] \leq P _ { T } , \forall n \in \mathbb { N } ,\tag{14g}
$$

(14h)

$$
C 8 : P _ { B } [ n ] G _ { B } \left| \mathcal { C } _ { B , M } [ n ] \right| ^ { 2 } \leq I _ { 0 } , \forall n \in \mathbb { N } ,\tag{14i}
$$

where C1 and C3 constrain 3D flight ranges of Alice and Bob, respectively, C2 and C4 constrain the transmit powers of Alice and Bob, respectively. Moreover, C5 constrains the minimum achievable rate for the MU where $R _ { M } [ n ]$ needs to exceed a threshold value $R _ { m i n }$ to ensure transmission effectiveness. In addition, C6 and C7 are the total power constraints of Alice and Bob, respectively, with $P _ { T }$ denoting the maximum total power of UAVs over N time slots. Additionally, C8 limits the interference temperature from Bob to the MU, with $I _ { 0 }$ indicating the maximum interference power to ensure that the interference does not affect the communication of other maritime devices.

## 4.3 Problem Analyses

Furthermore, we provide the corresponding analyses of the SEMCMOP.

(i) Dynamic Optimization: In the considered scenario, Alice dynamically adjusts its data transmissions to track the moving MU, making the data link channel time-varying. At this point, Eve continuously adjusts its position to eavesdrop on the signals from Alice. Meanwhile, Bob requires real-time adjustments based on Eve and MU for effective jamming, causing the jamming link channel to be dynamic. Thus, the SEMCMOP is a dynamic optimization problem.

(ii) Long-term Optimization Objectives: The continuous movements of the MU, Alice, Eve, and Bob introduce timevarying channel conditions that significantly influence the optimization objectives. Moreover, the SEMCMOP focuses on the sequential decision-making process of UAVs and aggregates objective evaluations over N time slots, meaning that solutions optimized for individual time slots may perform poorly when evaluated over the complete operational duration. Consequently, the SEMCMOP features long-term optimization objectives.

(iii) NP-hard Complexity: For simplicity in analysis, we investigate the first optimization objective under constrained operational parameters. Specifically, by fixing the positions of the MU and Eve, while quantizing the transmit powers of Alice and Bob $( \mathbb { P } _ { A }$ and $\bar { \mathbb { P } _ { B } } )$ to a finite set of discrete values, the original problem reduces to the following simplified formulation:

$$
\operatorname* { m i n } _ { \left\{ \mathbb { L } _ { A } , \mathbb { P } _ { A } , \mathbb { L } _ { B } , \mathbb { P } _ { B } \right\} } F = - f _ { 1 } ,\tag{15a}
$$

$$
\mathrm { s . t . } \mathrm { E q s . } ( 1 4 b ) , ( 1 4 d ) , ( 1 4 f ) - ( 1 4 i ) ,\tag{15b}
$$

$$
P _ { A } [ n ] \in [ 0 , P _ { m a x } ] , \forall n \in \mathbb { N } ,\tag{15c}
$$

$$
P _ { B } [ n ] \in [ 0 , P _ { m a x } ] , \forall n \in \mathbb { N } ,\tag{15d}
$$

$$
\begin{array} { r } { \sum _ { n = 1 } ^ { N } P _ { A } [ n ] < N P _ { m a x } , \forall n \in \mathbb { N } , } \end{array}\tag{15e}
$$

$$
\begin{array} { r } { \sum _ { n = 1 } ^ { N } P _ { B } [ n ] < N P _ { m a x } , \forall n \in \mathbb { N } . } \end{array}\tag{15f}
$$

The reduced-form SEMCMOP constitutes a nonlinear multidimensional 0-1 knapsack configuration problem, where binary decisions maximize item value while respecting capacity constraints [48]. In this mapping, discrete power variables correspond to item values, $f _ { 1 }$ represents cumulative item values, and power constraints establish the capacity limitations. Moreover, the 0-1 knapsack problem is explicitly categorized as NP-hard in complexity computation [49], and this complexity extends to the original SEMCMOP when the discrete constraints are generalized to continuous domains. Consequently, the SEMCMOP exhibits NP-hard complexity.

In summary, the SEMCMOP presents unique challenges that render conventional convex optimization methods and evolutionary algorithms inadequate [13]. In this case, the DRL algorithm offers a promising alternative, as it can autonomously learn optimal policies through environmental interactions while enabling real-time decision-making [50]. Therefore, we adopt the DRL algorithm to solve the formulated SEMCMOP.

## 5 ALGORITHM

In this section, we first formulate the SEMCMOP as a POMDP, followed by an introduction to the conventional SAC algorithm. Next, given the challenges of conventional SAC in POMDP, we propose an SAC-CVAE algorithm to address these challenges.

## 5.1 POMDP Formulation

For effective implementation of robust DRL algorithms, we transform the formulated SEMCMOP into a POMDP. A POMDP extends the standard Markov decision process (MDP) by incorporating perceptual limitations that restrict agents from directly observing the complete state, and the partial observability in POMDP stems from the condition that the positions of the eavesdropper become unknown when the time slot exceeds the threshold. Specifically, the POMDP is structured by $\langle s , \mathcal { A } , \mathcal { O } , \mathcal { P } , \mathcal { R } , \gamma \rangle$ [28], where S denotes the global state space and O denotes the observation space accessible to agents. At time slot $n ,$ the state of the environment is represented by $s [ n ] \in S ,$ , and the observations of the agent are denoted by $\mathbf { \boldsymbol { o } } [ n ] \in \mathcal { O }$ . Moreover, the action space is given by $\scriptstyle A ,$ including the independent action spaces of Alice and Bob. In addition, $\mathscr { P } ( s [ n \bar { + } 1 ] | s [ n ] , \mathbf { { \em a } } [ n ] )$ represents the probability of transitioning from state s[n] to the next state $s [ n + 1 ]$ after performing the action $\mathbf { a } [ n ] \in { \mathcal { A } } .$ Then, the reward function R evaluates optimization objectives, and the single-slot reward at time slot n is given as $r [ n ] ,$ , and $\gamma ~ \in ~ [ 0 , 1 )$ is the temporal discount factor balancing immediate versus future rewards. The action of an agent is determined by the policy $\pi ,$ where the probability of choosing an action in the state is expressed as $\pi ( { \boldsymbol { a } } | { \boldsymbol { s } } ) .$ and the goal of the POMDP is to determine a policy π that maximizes cumulative rewards. Next, we introduce the necessary elements of the POMDP in detail.

## 5.1.1 State

In the dynamic decision-making process, the agent needs to extract the real-time state to develop a corresponding policy. This agent is concerned with multi-dimensional information, including the parameters of Alice and Bob, and the spatial coordinates of the MU and Eve. However, Eve may strategically conceal its position to prevent the agent from obtaining accurate and complete position information. To improve the jamming effectiveness of Bob, we consider predicting the unobserved positions of Eve. Note that building an effective prediction model based solely on current position samples is challenging. To this end, we introduce the historical trajectory sequence of Eve as a component of the observation space, which is expressed by

$$
\begin{array} { r } { o [ n ] = \{ \mathcal { L } _ { E } [ n - Z + 1 ] , \mathcal { L } _ { E } [ n - Z + 2 ] , \ldots , \mathcal { L } _ { E } [ n ] ,  \quad } \\ {  \forall n \in \mathbb { N } \} , } \end{array}\tag{16}
$$

where $\mathcal { L } _ { E } [ n ] ~ = ~ \{ x _ { E } [ n ] , y _ { E } [ n ] , z _ { E } [ n ] \}$ represents the 3D location of Eve at time slot $n ,$ and Z is the maximum storage length of the historical trajectory sequence. When $n < { \bar { Z } } ,$ the length of the trajectory sequence is equal to $n ,$ reflecting that the observation space contains the trajectory sequence of Eve up to the current time slot.

Furthermore, the global state space contains the observation space, which can be expressed by

$$
\begin{array} { r } { S = \{ s [ n ] | s [ n ] = ( \Upsilon [ n ] , o [ n ] , ( x _ { A } [ n ] , y _ { A } [ n ] , z _ { A } [ n ] ) , } \\ { ( x _ { B } [ n ] , y _ { B } [ n ] , z _ { B } [ n ] ) ) , P _ { A } [ n ] , P _ { B } [ n ] , \forall n \} . } \end{array}\tag{17}
$$

## 5.1.2 Action

In our considered scenario, Alice and Bob need to dynamically optimize their flight trajectories and transmit powers to ensure reliable and secure maritime communications. Accordingly, the action space is denoted by

$$
\begin{array} { r } { \mathcal { A } = \{ \pmb { a } [ n ] | \pmb { a } [ n ] = ( A _ { A } [ n ] , P _ { A } [ n ] , \pmb { A } _ { B } [ n ] , P _ { B } [ n ] ) , \forall n \in \mathbb { N } \} , } \end{array}\tag{18}
$$

where $\boldsymbol { \mathcal { A } _ { A } [ n ] }$ and $A _ { B } [ n ]$ are the 3D action vectors of Alice and Bob, respectively. Note that our research considers an eavesdropping UAV (Eve) and a corresponding assisted UAV (Bob). Furthermore, our approach has good scalability, enabling adaptation to extended scenarios with multiple eavesdropping UAVs and jamming UAVs.

## 5.1.3 Reward

The reward function serves as a critical feedback mechanism that guides agent actions and determines the quality of the policy. Thus, we design a composite reward structure comprising reward components and penalty terms. This dual mechanism ensures efficient policy exploration while maintaining operational constraints. Note that the constraints C1-C4, C6, and C7 of the SEMCMOP are fulfilled by configuring the UAV parameters to operate within their specified allowable ranges. The remaining constraints C5 and C8 are satisfied by incorporating them into the reward function as penalty components. Specifically, we set a penalty item $W _ { 1 }$ according to the constraint C5 to guarantee the transmission requirement for legitimate users as follows:

$$
W _ { 1 } [ n ] = { \left\{ \begin{array} { l l } { R _ { M } [ n ] , } & { { \mathrm { i f ~ } } R _ { M } [ n ] \leq R _ { m i n } . } \\ { 0 , } & { { \mathrm { o t h e r w i s e } } . } \end{array} \right. }\tag{19}
$$

Then, we set a penalty item $W _ { 2 }$ based on the constraint C8 to prevent jamming signals from disrupting legitimate maritime communication as follows:

$$
\begin{array} { r l } & { W _ { 2 } [ n ] = } \\ & { \left\{ \begin{array} { l l } { P _ { B } [ n ] G _ { B } \left| \mathcal { C } _ { B , M } [ n ] \right| ^ { 2 } , } & { \mathrm { i f } \ P _ { B } [ n ] G _ { B } \left| \mathcal { C } _ { B , M } [ n ] \right| ^ { 2 } > I _ { 0 } . } \\ { 0 , } & { \mathrm { o t h e r w i s e } . } \end{array} \right. } \end{array}\tag{20}
$$

Therefore, the reward function is formulated as follows:

$$
\begin{array} { r l } & { \mathcal { R } = \{ r [ n ] | r [ n ] = \omega _ { 1 } \mu _ { 1 } C _ { s } [ n ] - \omega _ { 2 } \mu _ { 2 } ( E _ { A } [ n ] + E _ { B } [ n ] ) } \\ & { \qquad - \mu _ { 3 } W _ { 1 } [ n ] - \mu _ { 4 } W _ { 2 } [ n ] , \forall n \in \mathbb { N } \} , } \end{array}\tag{21}
$$

where $\mu _ { 1 } { - } \mu _ { 4 }$ are scaling factors to ensure that the different targets are on the same order of magnitude. Moreover, ω<sub>1</sub> and $\omega _ { 2 }$ are the weighting factors that control the trade-off between the two objectives.

## 5.2 Conventional SAC Algorithm

Next, we discuss the advantages of the SAC algorithm in dealing with MDP and describe the process in detail.

## 5.2.1 Selection of SAC Algorithm

Traditional DRL algorithms, such as discrete-action approaches $( e . g .$ , deep Q-network (DQN)) fail to support continuous control tasks [51]. Moreover, while trust region policy optimization (TRPO) provides improved policy stability through trust region optimization, it imposes prohibitively high computational complexity [52]. These algorithmic limitations face significant challenges when addressing the continuous and rapidly evolving POMDP.

To overcome these challenges, we adopt the SAC algorithm as our optimization framework. Specifically, its entropy maximization principle promotes systematic exploration across vast state-action spaces, avoiding premature convergence to suboptimal policies. Moreover, its twin Qvalue network architecture and policy smoothing reduce value overestimation, enhancing learning stability in uncertain environments. In addition, the automated temperature adjustment mechanism dynamically balances exploration and exploitation, avoiding manual hyperparameter tuning in complex and dynamic environments. Therefore, we select SAC as the foundational framework for the POMDP.

The SAC algorithm introduces maximum entropy to encourage exploration, and the redefined reward function is denoted by

$$
J ( \pi ) = \sum _ { n = 1 } ^ { N } \mathbb { E } \{ \gamma \left[ r [ n ] + \alpha \mathcal { H } ( \pi ( \cdot | s [ n ] ) ) \right] | \pi \} ,\tag{22}
$$

where $\mathbb { E } \{ \cdot \}$ is the expectation indicator, $\mathcal { H } ( \pi ( \cdot | s [ n ] ) ) =$ $- \log \pi ( { \pmb a } [ n ] | { \pmb s } [ n ] )$ is the entropy of the policy $\pi ,$ and α is the temperature parameter that controls the balance between the entropy term and reward, thereby regulating the stochasticity of the optimal policy. Furthermore, within the actor-critic architecture, the critic and actor are allocated to policy evaluation and policy optimization, respectively, as introduced below.

## 5.2.2 The Critic Part

The SAC algorithm effectively handles continuous action spaces by implementing an approximate form of soft policy iteration. By employing parametric approximators for both the Q-value and policy networks, this approach achieves optimization via stochastic gradient descent mechanisms. In the SAC framework, we consider three key components which consist of a state-value network $\dot { V _ { \psi } } ( s [ n ] )$ , a soft Q-value network $Q _ { \theta } ( \pmb { s } [ n ] , \pmb { a } [ n ] )$ , and a tractable policy network $\pi _ { \Phi } ( { \pmb a } [ n ] | { \pmb s } [ n ] )$ , where $\psi , \theta ,$ , and Φ represent their respective network parameters.

To enhance training stability, a separate function approximator is set for the state-value network [53]. The state-value network is trained to minimize the squared residual error as follows:

$$
\begin{array} { l } { { J _ { V } ( \psi ) = \mathbb { E } \{ \displaystyle \frac { 1 } { 2 } [ V _ { \psi } ( \pmb { s } [ { n } ] ) - } } \\ { { \phantom { \int } \mathbb { E } \{ Q _ { \theta } \left( \pmb { s } [ { n } ] , \pmb { a } [ { n } ] \right) - \alpha \log \pi _ { \Phi } \left( \pmb { a } [ { n } ] | \pmb { s } [ { n } ] \right) | \pi _ { \Phi } \} ] ^ { 2 } | \mathcal { D } \} , } } \end{array}\tag{23}
$$

where D denotes the replay buffer, and the parameter ψ undergoes iterative refinement with the stochastic gradient $\nabla _ { \psi } J _ { V } ( \psi )$ [54]. Moreover, the soft Q-value network parameter is trained by reducing the soft Bellman residual, which is expressed by

$$
J _ { Q } ( \theta ) = \mathbb { E } \{ \frac { 1 } { 2 } [ Q _ { \theta } \left( s [ n ] , \pmb { a } [ n ] \right) - \hat { Q } \left( s [ n ] , \pmb { a } [ n ] \right) ] ^ { 2 } | \mathcal { D } \} ,\tag{24}
$$

where $\hat { Q } \left( s [ n ] , \pmb { a } [ n ] \right) = r [ n ] + \gamma \mathbb { E } \{ V _ { \hat { \psi } } ( \pmb { s } [ n + 1 ] ) \}$ is the Q target value at time slot n. Correspondingly, the parameter θ is optimized through stochastic gradient descent $\nabla _ { \boldsymbol { \theta } } J _ { Q } ( \boldsymbol { \theta } )$

## 5.2.3 The Actor Part

The primary objective of the actor component is to search for policy improvements. Our approach utilizes the stateconditional stochastic policy network π to sample actions, and then uses the KL divergence to evaluate. Moreover, we use a neural network transformation to reparameterize the policy, resulting in a lower variance estimator. At this point, the policy network can be learned as follows:

$$
\begin{array} { r l r } & { } & { J _ { \pi } ( \Phi ) = { \mathbb E } \{ \alpha \log \pi _ { \Phi } \left( f _ { \Phi } ( \epsilon [ n ] ; s [ n ] ) | s [ n ] \right) - } \\ & { } & { Q _ { \theta } \left( s [ n ] , f _ { \Phi } ( \epsilon [ n ] ; s [ n ] ) \right) | { \mathcal D } , \mathcal N \} , } \end{array}\tag{25}
$$

where $f _ { \Phi } ( \epsilon [ n ] ; s [ n ] )$ is the reparameterization trick, and $\epsilon \sim$ $\mathcal { N } ( 0 , 1 )$ is an action noise signal sampled from a standard normal distribution [54]. Similarly, the parameter Φ can be optimized with stochastic gradient $\nabla _ { \Phi } \bar { J } _ { \pi } ( \Phi )$

## 5.3 The Proposed SAC-CVAE Algorithm

In this part, we present the motivation of proposing the SAC-CVAE algorithm and provide the implementation details of this algorithm.

## 5.3.1 Motivation of SAC-CVAE Algorithm

Algorithm 1: SAC-CVAE Algorithm   
Input: Number of iterations $\overline { { I , } }$ batch size, update   
rate $\tau ,$ and learning rates.   
$/ \star$ Initialization stage $\star /$   
1 Initialize: Replay buffer ${ \mathcal { D } } ,$ critic networks $Q _ { \theta }$ and   
$V _ { \psi } ,$ and actor network $\pi _ { \Phi } ;$   
2 for each iteration $i = 1 , 2 , \dots , I$ do   
3 Initialize the environmental information;   
4 for each step $n = 1 , 2 , \ldots , N$ do   
5 Store the observed location of Eve ${ \mathcal { L } } _ { E } [ n ] ;$   
$/ \star$ LSTM-assisted prediction stage   
$\star /$   
6 if $n \geq Z$ then   
$/ /$ Prediction mechanism   
7 LSTM processes historical trajectory   
sequence of Eve o[n] by Eqs. (31)-(33);   
8 Predicts the position of Eve;   
9 Obtain complete observation space o[n];   
$/ \star$ Update and learn stage $\star /$   
10 Obtain global state space $s [ n ]$ by Eq. (34);   
11 Select and execute action ${ \pmb a } [ n ]$   
${ \mathbf { } } \mathbf { a } [ n ] \sim \pi _ { \Phi } ( { \mathbf { } } \mathbf { a } [ n ] | s [ n ] ) ;$   
12 Update the environmental information,   
obtain $o [ n + 1 ] ;$   
13 Observe next state $s [ n + 1 ]$ and reward $r [ n ] ;$   
14 Store $( s [ n ] , \mathbf { } a [ n ] , r [ n ] , s [ n \mathop { \mathrm { ~ \tiny ~ + ~ } } 1 ] )$ to $\mathcal { D } ;$   
15 $/ /$ Experience replay mechanism   
16 Update the state-value network by Eq. (23);   
17 Update the soft Q-value network by Eq. (24);   
18 Obtain the optimized policy by Algorithm 2;   
19 Update the target network with   
ψˆ $ \tau \psi + ( 1 - \tau ) \hat { \psi } ;$   
Output: Trained model.

While the SAC algorithm can solve continuous-time problems, it faces the following challenges when dealing with the POMDP.

(i) Suboptimal Solutions in the Multi-modal Decision Space: In our considered dynamic scenario, a single state may correspond to multiple distinct yet optimal actions (i.e., a multi-modal decision space), where each action may lead to different future states and rewards. While the conventional

SAC algorithm encourages exploration through entropy regularization, it fails to explicitly distinguish or model different action modalities [53]. This limitation causes its learned policy to converge toward a broad peak distribution that inappropriately averages across potentially optimal actions, exhibiting suboptimal or unstable solutions. Note that this action-averaging issue becomes particularly detrimental in long-term trajectory optimization tasks, where decisively selecting one specific action modality rather than blending viable alternatives is crucial for achieving stable and optimal performance trajectories.

(ii) Computational inefficiency in the High-dimensional State Space: The optimization problems under consideration involve high-dimensional state spaces. In particular, the historical trajectory sequence of Eve is utilized to predict its unobserved position, forming the observation space and being stored in the global state space. However, this significantly expands the state space dimensions, thereby increasing the computational overhead for policy updates. Notably, this challenge becomes more severe in real-time deployment systems, as excessive state dimensions can lead to latency, instability, and convergence failure.

To address these challenges of the conventional SAC algorithm in POMDP, we propose a novel improved algorithm, SAC-CVAE. Note that the SAC-CVAE algorithm is trained on servers and deployed to UAVs for execution, thereby balancing computational demands with constrained UAV resources. Furthermore, Fig. 2 provides the visual architecture of the SAC-CVAE algorithm, and Algorithm 1 outlines its overall structure. The main advances in the $\mathrm { S A C - }$ CVAE algorithm are detailed in the following sections.

## 5.3.2 Conditional Variational Autoencoder (CVAE)-based Improved Framework

Variational autoencoder (VAE) provides a principled framework for learning latent representations of data [55]. By combining an encoder-decoder architecture with variational inference, VAE can generate diverse samples while maintaining a meaningful structure in the latent space. On this basis, we propose a CVAE-based improved framework, which disentangles policies and further optimizes the advantage-aware policies toward high advantage values, thereby avoiding the policy becoming overly biased toward a single mode. Algorithm 2 presents the comprehensive CVAE-based improved framework, with the implementation details elaborated below.

First, our framework models the advantage value as a conditional variable. Specifically, the encoder $q _ { \varphi } ( z | \mathbf { a } , \mathbf { c } )$ processes condition c and action a to generate a latent representation z, and the corresponding decoder $p _ { \delta } ( { \pmb a } | { \pmb z } , { \pmb c } )$ reconstructs a by preserving the correlation between c and z. Notably, unlike previous state-conditioned methods [56], our framework incorporates the state s and advantage values $\zeta ,$ forming a dual-conditioned input structure to enhance decision context. The state-advantage condition is given by [57]

$$
\begin{array} { r } { \pmb { c } [ n ] = \pmb { s } [ n ] | | \zeta [ n ] , } \end{array}\tag{26}
$$

where || denotes vector concatenation, and the advantage value ζ can be computed by

$$
\zeta [ n ] = \operatorname { t a n h } ( Q _ { \theta } ( s [ n ] , \pmb { a } [ n ] ) - V _ { \psi } ( \pmb { s } [ n ] ) ) ,\tag{27}
$$

![](images/aaf21fe6f3b64577904936b21500489bddaef1eb03a1108dba03b36d7d5bd7a2.jpg)  
Fig. 2. The architecture of the proposed SAC-CVAE algorithm for solving the SEMCMOP, which integrates a CVAE-based improved framework to disentangle and optimize policies as well as an LSTM-assisted prediction mechanism to enhance computational efficiency.

where tanh(·) function is used to normalize the advantage condition.

Furthermore, the CVAE is trained by maximizing the evidence lower bound (ELBO) for minibatches of the stateadvantage condition c and the corresponding action a. The training function is defined by [58]

$$
\begin{array} { r l } & { J _ { C } ( \varphi , \delta ) = - \mathbb { E } \{ \mathbb { E } \left[ \log \left( p _ { \delta } ( \pmb { a } [ n ] \ : | \ : z [ n ] , \pmb { c } [ n ] ) \right) | \boldsymbol { q } _ { \varphi } \right] + } \\ & { \phantom { J _ { C } ( \varphi , \delta ) } \phantom { x x x x x x x x x x x x x x x x x x x x x x x x x } } \\ & { \phantom { x x x x x x x x x x x x x x x x x x } \imath \cdot K L \left[ q _ { \varphi } ( \boldsymbol { z } [ n ] \ : | \ : \ : \pmb { a } [ n ] , \pmb { c } [ n ] ) \| | p ( \boldsymbol { z } [ n ] ) \right] \mathcal { D } \} , } \end{array}\tag{28}
$$

where ı is the coefficient for balancing the KL-divergence loss term, and $p ( z ) \sim \mathcal { N } ( 0 , 1 )$ is the latent prior. The first reconstruction term ensures accurate action generation, while the KL divergence term makes the latent representation distribution match the prior distribution.

During each training iteration, the critic networks $Q _ { \theta }$ and $V _ { \psi }$ evaluate state-action pairs to compute corresponding advantage values $\zeta$ via Eq. (27). Then, the advantageaware CVAE is trained according to Eq. (28). In this case, the latent representation z captures the underlying structure of action distributions, while the state-advantage condition c guides the model to generate actions that are positively correlated with ζ. Consequently, the trained CVAE can generate disentangled actions $\bar { \mathbf { a } _ { \mathbf { \theta } } } \sim p _ { \delta } ( \mathbf { a } | z , c )$ and capture the correlations between the action distribution and ζ. Subsequently, the trained CVAE is used for policy optimization, generating progressively higher-quality actions.

Then, during the policy optimization phase, we employ a hierarchical constraint to enable advantage-aware exploration. Specifically, the actor network $\pi _ { \Phi }$ generates a latent representation z˜ based on the condition c. Then, this representation z˜ is decoded into an action that aligns with its advantage values ζ. These processes are denoted by

$$
\tilde { z } [ n ] \sim \pi _ { \Phi } ( \cdot \mid c [ n ] ) ,\tag{29a}
$$

$$
{ \pmb a } _ { \zeta } [ n ] \sim p _ { \delta } ( { \cdot } \mid { \tilde { z } } [ n ] , c [ n ] ) .\tag{29b}
$$

Algorithm 2: CVAE-based Improved Framework   
Input: CVAE training step $\overline { { K } }$   
1 Initialize: CVAE encoder $q _ { \varphi }$ and decoder $p _ { \delta } \dot { } ;$   
/<sub>\*</sub> Policy disentangling \*/   
2 Calculate the advantage value $\zeta [ n ]$ by Eq. (27);   
3 Calculate the state-advantage condition $c [ n ]$ by $\operatorname { E q . }$   
(26);   
4 if $i \leq K$ then   
5 Sample the latent representation $z [ n ] ;$   
6 Optimize CVAE encoder $q _ { \varphi }$ and decoder $p _ { \delta }$   
according to Eq. (28);   
$/ \star$ Policy optimization $\star /$   
7 Optimize critic networks $Q _ { \theta }$ and $V _ { \psi }$ by optimal   
action $\mathbf { \Delta } \mathbf { a } _ { \zeta } ^ { * } \mathbf { ; }$   
8 Optimize the advantage-aware policy toward high   
advantage values by Eq. (30).   
Output: Trained policy.

In this case, π<sub>Φ</sub> generates actions of different qualities that are correlated with a specified $\zeta .$ Among them, the optimal action $\mathbf { \Delta } \mathbf { a } _ { \zeta } ^ { \ast }$ is obtained by processing the condition $\boldsymbol { c } ^ { * } = \boldsymbol { s } \| \zeta ^ { * }$ , where $\zeta ^ { * } = 1$ represents the maximum advantage value. This approach optimizes the advantage-aware policy toward high advantage values. The policy network can be updated by

$$
\begin{array} { r l } & { J _ { \pi } ( \Phi ) = \mathbb { E } \{ - \lambda Q _ { \theta } ( s [ n ] , \pmb { a } _ { \zeta } ^ { * } [ n ] ) + ( \pmb { a } [ n ] - \pmb { a } _ { \zeta } [ n ] ) ^ { 2 } + } \\ & { \qquad \alpha \log \pi _ { \Phi } \left( \pmb { a } _ { \zeta } ^ { * } [ n ] \enspace | \enspace \pmb { c } [ n ] \right) | \mathcal { D } , p _ { \delta } \} , } \end{array}\tag{30}
$$

where $\lambda$ is the normalization coefficient to maintain proper scaling between the Q-value maximization and policy regularization. Moreover, the first term drives optimal actions through the fixed high-advantage condition $c ^ { * }$ , the second term imposes constraints on the advantage-aware policy to ensure that selected actions follow the advantage condition, and the third term is the maximum entropy term based on $c ^ { * }$ . Thus, suboptimal samples with a low advantage value do not undermine the optimization of the optimal policy $\pi _ { \Phi } ( \cdot | c ^ { * } )$ . Instead, they impose effective constraints on the corresponding policy $\pi _ { \Phi } ( \cdot | c )$ . This hierarchical constraint enables stable and efficient learning, where lower-quality samples guide exploration, while higher-quality actions refine policies toward optimal performance.

In summary, the CVAE-based improved framework combines policy disentanglement with advantage-aware policy optimization. This framework captures multi-modal action distributions and further optimizes policies toward high advantage values, improving the robustness and efficiency of our algorithm.

## 5.3.3 LSTM-assisted Prediction Mechanism

The historical trajectory sequence of Eve used for prediction, as an observation space, is stored in the state space, which imposes a significant computational burden. To address this challenge, we propose an LSTM-assisted prediction mechanism that calculates predictions in advance and simplifies the stored observation space to the current position of Eve. Specifically, the LSTM network is a specialized variant of recurrent neural networks and can efficiently capture temporal dependencies through its gate mechanisms [59]. This architecture enables it to identify complex patterns in trajectory sequences, including acceleration patterns, directional tendencies, and recurring motion sequences. Moreover, the LSTM network can selectively retain important historical information and filter irrelevant noise, thereby making it suited for modeling trajectory sequences over time. As such, we utilize the LSTM network to extract patterns from the historical trajectory sequence of Eve and predict its unobserved positions. The LSTM network architecture, as illustrated in the lower left segment of Fig. 2, consists of three principal gates, each performing distinct functions as follows:

(i) Forget gate: The forget gate $( L S T M _ { f } [ n ] )$ determines the amount of previous information to be discarded, which is denoted by

$$
L S T M _ { f } [ n ] = \sigma ( W _ { f } \cdot [ h [ n - 1 ] , o [ n ] ] + b _ { f } ) ,\tag{31}
$$

where $\sigma ( \cdot )$ is the sigmoid function to control output values in $[ 0 , 1 ] ,$ , with 0 indicating complete discarding and 1 representing full preservation of the previous cell state $C [ n \bar { - } 1 ]$ Moreover, $\bar { W } _ { f }$ and $b _ { f }$ are the weight matrix and bias vector for the forget gate, respectively, and $h [ n - 1 ]$ is the hidden state of the previous time slot.

(ii) Input gate: The input gate $( L S T M _ { i } [ n ] )$ regulates updates to the cell state through the following two operations:

$$
\begin{array} { r } { L S T M _ { i } [ n ] = \sigma ( W _ { i } \cdot [ h [ n - 1 ] , o [ n ] ] + b _ { i } ) , } \end{array}\tag{32a}
$$

$$
\tilde { C } [ n ] = \operatorname { t a n h } ( W _ { C } \cdot [ h [ n - 1 ] , o [ n ] ] + b _ { C } ) ,\tag{32b}
$$

where ${ \tilde { C } } [ n ]$ denotes the new candidate values for state updates. Moreover, $W _ { i }$ and $W _ { C }$ are the weight matrices for input components, $b _ { i }$ and $b _ { C }$ are the corresponding bias vectors. Then, the cell state updates via $C [ n ] \stackrel { \textstyle \sim } { = } L S T M _ { f } [ n ]$ $C [ n - 1 ] + L S T M _ { i } [ n ] \cdot \tilde { C } [ n ]$

(iii) Output gate: The output gate $( L S T M _ { o } [ n ] )$ generates output information as follows:

$$
L S T M _ { o } [ n ] = \sigma ( W _ { o } \cdot [ h [ n - 1 ] , o [ n ] ] + b _ { o } ) ,\tag{33a}
$$

$$
h [ n ] = L S T M _ { o } [ n ] \cdot \operatorname { t a n h } ( C [ n ] ) ,\tag{33b}
$$

where $h [ n ]$ becomes the final hidden state containing distilled sequential information, which is then fed into a fully connected layer to generate the predicted position.

At this point, we can obtain the prediction results using the LSTM network, and the simplified global state space $( i . e . ,$ the observation space is the position of Eve at the current time) is denoted by

$$
\begin{array} { r l } & { S = \{ s [ n ] | s [ n ] = ( \mathbf { Y } [ n ] , \mathcal { L } _ { E } [ n ] , ( x _ { A } [ n ] , y _ { A } [ n ] , z _ { A } [ n ] ) , } \\ & { \qquad ( x _ { B } [ n ] , y _ { B } [ n ] , z _ { B } [ n ] ) ) , P _ { A } [ n ] , P _ { B } [ n ] , \forall n \in \mathbb { N } \} , } \end{array}\tag{34}
$$

where $\mathcal { L } _ { E }$ denotes either the observed location of Eve when available or the predicted location of Eve obtained by the LSTM network based on the historical trajectory sequence of Eve, and the simplified state output is input into the CVAE framework. Note that the LSTM network can be periodically fine-tuned with newly collected historical data to adapt to evolving movement patterns.

In summary, we employ the LSTM network that selectively filters information via its gating mechanisms while preserving relevant historical features in memory cells, to predict the unobserved position of Eve. Furthermore, we compress the global state space from the historical trajectory sequence of Eve to the current predicted (or observed) position of Eve, significantly reducing the state space dimension and improving the computational efficiency of our algorithm.

## 5.4 Complexity Analysis of SAC-CVAE Algorithm

In this part, we provide a comprehensive analysis of the resource requirements of the SAC-CVAE algorithm, including computational complexity and space complexity.

The computational complexity of the SAC-CVAE algorithm can be decomposed into the following four major components.

(i) Network Initialization: The network setup requires parameter initialization. The corresponding complexity is $\mathbf { \hat { \mathcal { O } } } ( 2 | \theta | + | \psi | + | \Phi | )$ , where |θ| and |ψ| represent the number of parameters in each of the twin Q-value networks and statevalue network, respectively, and |Φ| denotes the number of actor network parameters.

(ii) Policy Execution: Action selection through the policy network has the complexity of $\mathcal { O } ( I N ( | \Phi | + | \mathfrak { d } _ { h } | ^ { 2 } + | z | ) \bar { ) }$ where I is the total training iterations, N denotes the number of steps per iteration, $| \bar { d } _ { h } |$ is the dimension of the LSTM hidden state, and |z| denotes the dimension of the latent representation in CVAE.

(iii) Replay Buffer Collection: The complexity of collecting transitions in the replay buffer is $\mathcal { O } ( I \bar { N } B )$ , where B is the environmental interaction complexity.

(iv) Network Update: For critic and actor network updates, including the advantage-aware policy network optimization, the complexity is $\mathrm { \bar { \mathcal { O } } } ( 2 I G ( 2 \vert \mathrm { \bar { \theta } } \vert + \mathrm { \bar { \vert } } \psi \vert + \vert \Phi \vert ) )$ , where G denotes the gradient steps per update.

Combining these components, the aggregate computational complexity is $\mathcal { O } ( 2 | \hat { \theta } | + | \psi | + | \Phi | + \hat { I } \hat { N ( } | \Phi | + | \hat { d _ { h } } | ^ { 2 } +$ $\vert z \vert ) + I N \hat { B } + 2 \dot { I } G ( 2 \vert \theta \vert + \vert \psi \vert + \vert \Phi \vert ) )$

The space complexity of the SAC-CVAE algorithm primarily consists of network parameters and replay buffer storage. For network architecture, the complexity is $\dot { \mathcal { O } } ( 2 | \theta | +$ $| \psi | + \breve { | \Phi } | + | z | + | d _ { h } | ^ { 2 } )$ for critic and actor networks, latent representation, along with the LSTM hidden state. Moreover, the replay buffer stores current states, actions, rewards, and next states. Given a replay buffer capacity D, the complexity is $D ( 2 | \pmb { s } | + | \pmb { a } | + 1 )$ , where |s| and |a| denote the state dimension and action dimension, respectively. Thus, the aggregate space complexity is $O ( 2 | \theta | \ { \overset { \cdot } { + } } \ | \psi | + | \Phi | + | z | +$ $| \breve { d } _ { h } | ^ { 2 } + D ( 2 | \pmb { s } | + | \pmb { a } | \overset { . } { + } 1 ) )$ .

## 6 SIMULATION RESULTS AND ANALYSES

In this section, we evaluate the performance of the SAC-CVAE algorithm through simulation results.

## 6.1 Simulation Configurations

In this part, we detail the parameter configurations adopted for our simulations and present the baselines selected for comparative evaluation.

## 6.1.1 Parameter Configurations

We execute all simulations on a high-performance computing platform equipped with an AMD EPYC 7642 48-Core processor, NVIDIA GeForce RTX 3090 graphics card, and 128GB system memory.

In the simulations, the development environment is Python 3.8 and Visual Studio Code 1.91. The UAVs (Alice and Bob) are initialized within a 100 m × 100 m area, with randomized starting positions to simulate real conditions where UAVs might be transitioning from previous tasks. Meanwhile, for the SAC-CVAE algorithm, each actor and critic network has two hidden-layer architectures with the ReLU activation function, and the Adam optimizer for parameter updates. Moreover, the batch size is 128 from the replay buffer, and the remaining main parameters are shown in Table 3.

## 6.1.2 Baselines

To comprehensively assess the effectiveness of the SAC-CVAE algorithm, we provide a comparative approach and several comparison algorithms as follows:

(i) Non-jamming Approach: In this scenario, Alice sends signals to the MU without jamming. This approach highlights the necessity of UAV-assisted intelligent jamming against eavesdroppers in low-altitude maritime communications.

(ii) State-of-the-Art DRL Algorithms: To further evaluate the performance of SAC-CVAE, we choose conventional SAC and the following state-of-the-art algorithms as benchmarks. Specifically, the deep deterministic policy gradient (DDPG) combines policy gradient methods with deep learning, utilizing an actor-critic framework to enhance policy learning [60]. Twin delayed DDPG (TD3) is an enhanced variant of DDPG that improves stability via double Qlearning, delayed policy updates, and target policy smoothing [61]. Moreover, proximal policy optimization (PPO)

Main parameters in the simulation process
<table><tr><td>Notation</td><td>Definition</td><td>Value</td></tr><tr><td> $d _ { r }$ </td><td>Reference distance of the U2V link</td><td>2600 m</td></tr><tr><td> $P _ { T }$ </td><td>Maximum total power of the UAV</td><td>400 mW</td></tr><tr><td> $F _ { V }$ </td><td>Rician factor</td><td>31.3</td></tr><tr><td> $f _ { c }$ </td><td>Carrier frequency</td><td>2.4 GHz</td></tr><tr><td> $\gamma$ </td><td>Discount factor</td><td>0.9</td></tr><tr><td> $G _ { A }$ </td><td>Antenna gain of Alice</td><td>8 dBi</td></tr><tr><td> $G _ { B }$ </td><td>Antenna gain of Bob</td><td>8 dBi</td></tr><tr><td> $I _ { 0 }$ </td><td>Maximum interference power</td><td>-74 dBm</td></tr><tr><td> $I _ { r }$ </td><td>Path loss relevant index</td><td>1.5</td></tr><tr><td> $I _ { h }$ </td><td>MU horizontal inertial matrix element</td><td> $3 0 0 \mathrm { k g } { \cdot } m ^ { 2 }$ </td></tr><tr><td> $I _ { z }$ </td><td>MU vertical inertial matrix element</td><td> $1 5 0 \mathrm { k g } { \cdot } m ^ { 2 }$ </td></tr><tr><td> $m _ { M U }$ </td><td>Mass of the MU</td><td> $1 0 0 \mathrm { k g }$ </td></tr><tr><td> $m _ { U }$ </td><td>Mass of the UAV</td><td>2 kg</td></tr><tr><td> $P _ { d }$ </td><td>Path loss parameter of the U2V link</td><td>116.7</td></tr><tr><td> $R _ { m i n }$ </td><td>Threshold value of effective transmission</td><td>0.0014</td></tr><tr><td> $\sigma ^ { 2 }$ </td><td>Power of additive white Gaussian noise</td><td>-107 dBm</td></tr><tr><td> $v _ { l }$ </td><td>Linear velocity of the MU</td><td> $1 \mathrm { m } / \mathrm { s }$ </td></tr><tr><td> $v _ { r }$ </td><td>Rotational velocity of the MU</td><td> $0 . 5 ~ \mathrm { r a d / s }$ </td></tr><tr><td> $x _ { A } ^ { m i n }$ </td><td>Minimum x-coordinate of Alice</td><td>100 m</td></tr><tr><td> $x _ { \ A } ^ { \bar { m } a x }$ </td><td>Maximum x-coordinate of Alice</td><td>200 m</td></tr><tr><td> $x _ { B } ^ { \bar { m } i n }$ </td><td>Minimum x-coordinate of Bob</td><td>200 m</td></tr><tr><td> $x _ { B } ^ { \overline { { m } } a x }$ </td><td>Maximum x-coordinate of Bob</td><td>300 m</td></tr><tr><td> $y _ { A } ^ { m i n }$ </td><td>Minimum y-coordinate of Alice</td><td>100 m</td></tr><tr><td> $y _ { A } ^ { \overline { { { m } } } a x }$ </td><td>Maximum y-coordinate of Alice</td><td>200 m</td></tr><tr><td> $y _ { B } ^ { m i n }$ </td><td>Minimum y-coordinate of Bob</td><td>400 m</td></tr><tr><td> $y _ { R } ^ { m a x }$ </td><td>Maximum y-coordinate of Bob</td><td>500 m</td></tr><tr><td> $z ^ { m i n }$ </td><td>Minimum altitude of Alice and Bob</td><td>50 m</td></tr><tr><td> $z ^ { m a x }$ </td><td>Maximum altitude of Alice and Bob</td><td>70 m</td></tr><tr><td> $\zeta ^ { * }$ </td><td>Maximum advantage value</td><td>1</td></tr></table>

TABLE 3

optimizes policy updates with a clipping mechanism to ensure training stability and efficiency [62]. In addition, the greedy algorithm makes locally optimal decisions at each step by maximizing immediate rewards [63]. Additionally, all algorithms are trained for $4 \times 1 0 ^ { 5 }$ training iterations, with performance evaluations conducted every 80 iterations.

## 6.2 Simulation Results

In this part, we evaluate the performance of the SAC-CVAE algorithm. We consider two distinct eavesdropper movement patterns, including the case where Eve approaches the MU to enhance eavesdropping capabilities and the case where Eve moves away from the MU to escape detection for future eavesdropping. For each pattern, we provide detailed analyses of jamming effectiveness, optimized objective values, convergence performance, and trajectory results. Additionally, we present both the weight sensitivity analysis and the performance of the SAC-CVAE algorithm in an extended scenario.

## 6.2.1 Comparisons with Non-jamming Approach

We compare the security performance of UAV-assisted intelligent jamming and non-jamming approaches in lowaltitude maritime communications. Specifically, Fig. 3 presents the total secrecy rate obtained for both approaches as Eve approaches the MU and Eve moves away from the MU, where the secrecy rate at time slot n in the nonjamming approach is given by $C _ { s } [ n ] = R _ { M } [ n ] - R _ { E } [ n ]$ for comparative analysis. The results demonstrate that the intelligent jamming approach sustains high secrecy rates and ensures communication reliability, whereas the results of the non-jamming method are around 0. These comparative results validate the effectiveness of the UAV-assisted intelligent jamming approach in achieving secure low-altitude maritime communications.

![](images/9ec3e50822163b400c216325610c092e39df25d4213a2b94ef83c0536513ea61.jpg)  
Fig. 3. Total secrecy rates obtained by the intelligent jamming and nonjamming approaches as Eve approaches the MU and Eve moves away from the MU.

## 6.2.2 Comparisons with Other Algorithms

We evaluate the optimized objective values obtained by different algorithms. As shown in Fig. 4, when Eve approaches the MU, the SAC-CVAE algorithm achieves a maximum total secrecy rate and a near-optimal total energy consumption of the UAVs. While DDPG has a minimum total energy consumption, it fails to provide an effective secrecy rate. Thus, the proposed SAC-CVAE algorithm demonstrates superior performance. In addition, Fig. 5 provides the optimized objective values as Eve moves away from the MU. The SAC-CVAE consistently outperforms other algorithms both in secrecy rate and energy consumption. This balance makes SAC-CVAE particularly suitable for secure maritime communications under the energy constraints of UAVs. These results further demonstrate that the SAC-CVAE algorithm can effectively maintain communication security while addressing the deployment challenges of UAVs in maritime environments.

![](images/ca0c58e17149f9e2d6b7b5b6d0adffa055d44b9ff9ad379d0bd645df55c0e484.jpg)

![](images/75c6a1679517964dbbccfe691d28510ac848811a1cbf08b5fbbc7bc228d1a0ba.jpg)  
Fig. 4. The optimization objective values obtained by different algorithms as Eve approaches the MU.

## 6.2.3 Convergence Performance

Convergence performance is a key metric for assessing the stability and optimization capability of DRL algorithms.

![](images/657461fdec9ea203e6c6094d83560d67606f5d06e397f466f23fae692757e379.jpg)

![](images/3ee2d51326a12deb980c6a0d79b4b5ff56ea7a9d0be55aad14fbb755e46a1774.jpg)  
Fig. 5. The optimization objective values obtained by different algorithms as Eve moves away from the MU.

![](images/95b47184afcd2075a6a25d61fa8f1743d9ce1281fb83e729fb80771f3f90603d.jpg)  
Fig. 6. Convergence performance obtained by different algorithms as Eve approaches the MU.

![](images/9ac86248c614d27a1b00a366fc34186d3d975aa578d1d29c68de900f1ff76103.jpg)  
Fig. 7. Convergence performance obtained by different algorithms as Eve moves away from the MU.

Accordingly, we present convergence results of different algorithms to provide a comparative analysis. As illustrated in Fig. 6, when Eve approaches the MU, upon convergence, the SAC-CVAE algorithm achieves greater cumulative rewards compared to other comparison algorithms, demonstrating its superior learning efficiency. Moreover, when Eve moves away from the MU, as shown in Fig. 7, the converged SAC-CVAE algorithm maintains the optimal performance in terms of reward values. Therefore, the excellent convergence performance across various eavesdropper movement patterns confirms the robustness of the SAC-CVAE algorithm, further validating its ability to learn more effective policies.

## 6.2.4 Trajectory Results

Furthermore, Figs. 8 and 9 illustrate the 3D trajectory results obtained by the SAC-CVAE algorithm across various eavesdropper movement patterns. Specifically, when Eve approaches the MU (Fig. 8) or moves away from the MU (Fig. 9), Alice advances toward the MU to optimize data transmission, while Bob dynamically positions toward Eve to improve jamming effectiveness. These coordinated movements indicate that Alice and Bob can adaptively track their respective targets and execute autonomous path optimization. Note that the system incorporates a security constraint preventing Eve from getting too close to Alice. Thus, the trajectory results demonstrate that the proposed SAC-CVAE algorithm can achieve intelligent trajectory optimization to enable secure low-altitude maritime communications.

## 6.2.5 Weight Sensitivity Analysis

Furthermore, we analyze the weight sensitivity to evaluate the influence of weights $\omega _ { 1 }$ and ω<sub>2</sub> in the reward function (Eq. (21)) on system performance through a sensitivity analysis (where $\omega _ { 1 } + \omega _ { 2 } = 1 )$ , thereby determining the optimal weight configurations. Specifically, we systematically vary ω<sub>1</sub> from 0.4 to 0.8 to control the emphasis on secrecy rate maximization, with corresponding adjustments of ω<sub>2</sub> from 0.6 to 0.2 to determine the energy consumption of UAVs minimization. These weight values are evaluated through a sensitivity analysis, as shown in Fig. 10. When prioritizing security $( \omega _ { 1 } = 0 . 8 , \omega _ { 2 } = 0 . 2 )$ , the system achieves a superior secrecy rate, yet at the cost of substantially higher energy consumption, while emphasizing energy efficiency $( \omega _ { 1 } = 0 . 4 ,$ $\omega _ { 2 } = 0 . 6 )$ reduces energy consumption at the cost of secrecy rate. Through careful analysis of trade-offs, we identify an optimal intermediate weight configuration where $\omega _ { 1 } = 0 . 6$ and $\omega _ { 2 } = 0 . 4 ,$ , achieving security performance improvements while maintaining energy consumption within acceptable thresholds. This particular point represents a knee point in the multi-objective optimization problem [64], which offers a more favorable compromise between competing objectives.

![](images/5890efa0059cf8631454abaf4fdb5bf284a9ceeaad3fbf9c79082e53b2d1549e.jpg)  
Fig. 8. Trajectory results obtained by the SAC-CVAE algorithm as Eve approaches the MU.

![](images/3b8290aea354879119f4a83b9040418df2f91a5c4ea8999c2011d120130bae67.jpg)  
Fig. 9. Trajectory results obtained by the SAC-CVAE algorithm as Eve moves away from the MU.

![](images/2a01b09e8b65b85e610d378173017ce7a35bd40d8a0a587bf764db8309b86211.jpg)

![](images/e2dd2f37e06e56db6432698eb975290fcb8b4f53dec19029102f3c8e88c3e368.jpg)  
Fig. 10. Weight sensitivity analysis showing system performance across different weight configurations of ω and ω in the reward function.

## 6.2.6 Extended Scenario Performance

We further evaluate our approach in an extended scenario with multi-user and multi-eavesdropper. Specifically, we consider that two legitimate UAVs send data signals to two users, respectively, and two jamming UAVs send jamming signals to two eavesdropping UAVs, respectively. At this point, the first optimization objective becomes maximizing the minimum total secrecy rate of the system, and the POMDP needs to incorporate expanded state and action spaces to accommodate multiple users and multiple UAVs. Fig. 11 presents the minimum total secrecy rates of the system obtained by the intelligent jamming and non-jamming approaches in the extended scenario. As can be seen, our proposed intelligent jamming approach obtains a superior minimum total secrecy rate, thereby ensuring reliable and secure low-altitude maritime communications. In contrast, the result obtained by the non-jamming approach is a negative value, which indicates that the non-jamming approach cannot achieve secure maritime communications. Therefore, our approach can adapt to the extended scenario with multiuser and multi-eavesdropper.

## 7 DISCUSSION

In this section, we further discuss the effectiveness of the proposed approach through the following three critical aspects:

![](images/588e2bf732abba42c6182f8e0fff2eeabe8400961357b0d2163e6f6ee302e205.jpg)  
Fig. 11. Minimum total secrecy rates obtained by the intelligent jamming and non-jamming approaches in the extended scenario.

i) Ablation Simulation Results: We present comprehensive ablation simulation results that demonstrate the performance enhancements achieved through each individual improvement in the proposed SAC-CVAE algorithm. The detailed simulations are shown in Appendix A.

ii) Error Results of Prediction Mechanism: We evaluate the impact of errors generated by the LSTM-assisted prediction mechanism, and detailed results and discussions are provided in Appendix B.

## 8 CONCLUSION

This paper has implemented secure low-altitude maritime communications via UAV-assisted intelligent jamming. In the considered system, given the inherent trade-offs between conflicting objectives, we have formulated an SEMC-MOP to jointly maximize the total secrecy rate of the system and minimize the total energy consumption of UAVs. To address the dynamic and long-term optimization problem, we have reformulated it into a POMDP. Then, we have proposed a GenAI-improved DRL algorithm, SAC-CVAE, which integrates a CVAE-based framework for policy disentanglement and optimization, as well as an LSTM-assisted prediction mechanism to enhance computational efficiency. Simulation results have shown that the UAV-assisted intelligent jamming approach significantly outperforms the non-jamming approach. Moreover, comparison results have demonstrated that our proposed SAC-CVAE algorithm exhibits superior performance compared to other benchmark algorithms across various eavesdropper movement patterns, thereby maximizing the total secrecy rate while maintaining near-optimal total energy consumption of UAVs. In addition, performance in the extended scenario further demonstrates the effectiveness and robustness of the SAC-CVAE algorithm. Future research can explore extending this work to proactive monitoring scenarios, thereby expanding the coverage of secure maritime communications. Additionally, a comprehensive investigation of different eavesdropper types is a promising direction to further enhance the robustness of maritime communications.

## REFERENCES

[1] X. Cao, S. Wang, and Y. Zhang, “Intelligent reflecting surface enhanced maritime joint sensing and communication systems: Performance optimization,” IEEE Trans. Commun., vol. 73, no. 2, pp. 938–949, 2025.

[2] C. Xu, S. Song, X. Wu, G. Han, M. Pan, G. Xu, and J. Cui, “A high reliable routing protocol based on spatial-temporal graph model for multiple unmanned underwater vehicles network,” IEEE Trans. Mob. Comput., vol. 24, no. 5, pp. 4434–4450, 2025.

[3] X. Hu, B. Lin, X. Lu, P. Wang, N. Cheng, Z. Yin, and W. Zhuang, “Performance analysis of end-to-end LEO satellite-aided shoreto-ship communications: A stochastic geometry approach,” IEEE Trans. Wirel. Commun., vol. 23, no. 9, pp. 11 753–11 769, 2024.

[4] C. Zhang, G. Sun, J. Li, Q. Wu, J. Wang, D. Niyato, and Y. Liu, “Multi-objective aerial collaborative secure communication optimization via generative diffusion model-enabled deep reinforcement learning,” IEEE Trans. Mob. Comput., vol. 24, no. 4, pp. 3041– 3058, 2025.

[5] S. Zhou, H. Yang, L. Xiang, and K. Yang, “Temporal-assisted beamforming and trajectory prediction in sensing-enabled UAV communications,” IEEE Trans. Commun., vol. 73, no. 7, pp. 5408– 5419, 2025.

[6] H. Lei, D. Meng, H. Ran, K. Park, G. Pan, and M. Alouini, “Multi-UAV trajectory design for fair and secure communication,” IEEE Trans. Cogn. Commun. Netw., vol. 11, no. 3, pp. 1966–1980, 2025.

[7] S. Jeon, J. Kwak, and J. P. Choi, “An integration of cryptography and physical layer security for multibeam satellite systems,” IEEE Trans. Commun., vol. 73, no. 2, pp. 1087–1099, 2025.

[8] M. H. Khoshafa, G. A. Ahmed, T. M. N. Ngatched, and M. D. Renzo, “Aerial reconfigurable intelligent surfaces-enabled secured wireless communications: Performance analysis and optimization,” IEEE Trans. Commun., vol. 73, no. 7, pp. 4662–4677, 2025.

[9] M. Dai, T. Wang, S. Chang, Z. Su, and Y. Wu, “Energy minimization oriented hybrid semantic data transmission in air-ocean integrated networks: A resource allocation design,” IEEE Trans. Mob. Comput., vol. 24, no. 9, pp. 8329–8346, 2025.

[10] J. Li, G. Sun, Q. Wu, S. Liang, J. Wang, D. Niyato, and D. I. Kim, “Aerial secure collaborative communications under eavesdropper collusion in low-altitude economy: A generative swarm intelligent approach,” IEEE Trans. Mobile Comput., 2025.

[11] J. Huang, A. Wang, G. Sun, J. Li, J. Wang, H. Du, and D. Niyato, “Dual AAV cluster-assisted maritime physical-layer secure communications via collaborative beamforming,” IEEE Internet Things J., vol. 12, no. 9, pp. 12 589–12 607, 2025.

[12] L. Wu, W. Wang, Z. Ji, Y. Yang, K. Cumanan, G. Chen, Z. Ding, and O. A. Dobre, “UAV-assisted maritime legitimate surveillance: Joint trajectory design and power allocation,” IEEE Trans. Veh. Technol., vol. 72, no. 10, pp. 13 701–13 705, 2023.

[13] F. Wang, D. Jiang, Z. Wang, and S. Mumtaz, “Service continuity based data delivery optimization in satellite-terrestrial networks,” IEEE Trans. Veh. Technol., vol. 72, no. 10, pp. 13 604–13 617, 2023.

[14] X. Yuan, T. Yang, Y. Hu, J. Xu, and A. Schmeink, “Trajectory design for UAV-enabled multiuser wireless power transfer with nonlinear energy harvesting,” IEEE Trans. Wireless Commun., vol. 20, no. 2, pp. 1105–1121, 2020.

[15] D. Guo, L. Tang, X. Zhang, and Y.-C. Liang, “Joint optimization of trajectory and jamming power for multiple UAV-aided proactive eavesdropping,” IEEE Trans. Mobile Comput., vol. 23, no. 5, pp. 5770–5785, 2023.

[16] G. Zhang, X. Wei, X. Tan, Z. Han, and G. Zhang, “AoI minimization based on deep reinforcement learning and matching game for IoT information collection in SAGIN,” IEEE Trans. Commun., vol. 73, no. 8, pp. 5950–5964, 2025.

[17] Z. Ning, H. Ji, X. Wang, E. C. H. Ngai, L. Guo, and J. Liu, “Joint optimization of data acquisition and trajectory planning for UAVassisted wireless powered Internet of Things,” IEEE Trans. Mob. Comput., vol. 24, no. 2, pp. 1016–1030, 2025.

[18] R. Wu, Z. Li, Z. Xie, and X. Liang, “Intelligent spectrum sharing strategy for integrated satellite-maritime heterogeneous mobile networks,” IEEE Trans. Veh. Technol., vol. 73, no. 5, pp. 6780–6794, 2024.

[19] Z. Li and B. Shang, “Fundamentals of satellite-maritime communications: Downlink and uplink analysis,” IEEE Trans. Commun., vol. 73, no. 4, pp. 2191–2206, 2025.

[20] C. Zeng, J.-B. Wang, C. Ding, M. Lin, and J. Wang, “MIMO unmanned surface vessels enabled maritime wireless network coexisting with satellite network: Beamforming and trajectory design,” IEEE Trans. Commun., vol. 71, no. 1, pp. 83–100, 2022.

[21] Y. Liu, C.-X. Wang, H. Chang, Y. He, and J. Bian, “A novel nonstationary 6G UAV channel model for maritime communications,” IEEE J. Sel. Areas Commun., vol. 39, no. 10, pp. 2992–3005, 2021.

[22] J. Yu, Y. Cai, S. Yan, Y. Li, J. Wang, J. Liu, and J. An, “Joint 3D beamforming-and-trajectory design for UAV-satellite uplink covert communication,” IEEE Trans. Commun., vol. 73, no. 5, pp. 3469–3481, 2025.

[23] N. Nomikos, A. Giannopoulos, A. Kalafatelis, V. Ozduran,<sup>¨</sup> P. Trakadas, and G. K. Karagiannidis, “Improving connectivity in 6G maritime communication networks with UAV swarms,” IEEE Access, vol. 12, pp. 18 739–18 751, 2024.

[24] Y. Liu, J. Yan, and X. Zhao, “Deep reinforcement learning based latency minimization for mobile edge computing with virtualization in maritime UAV communication network,” IEEE Trans. Veh. Technol., vol. 71, no. 4, pp. 4225–4236, 2022.

[25] T. Yang, Z. Jiang, R. Sun, N. Cheng, and H. Feng, “Maritime search and rescue based on group mobile computing for unmanned aerial vehicles and unmanned surface vehicles,” IEEE Trans. Ind. Inform., vol. 16, no. 12, pp. 7700–7708, 2020.

[26] H. Luo, Y. Wu, G. Sun, H. Yu, and M. Guizani, “ESCM: an efficient and secure communication mechanism for UAV networks,” IEEE Trans. Netw. Serv. Manag., vol. 21, no. 3, pp. 3124–3139, 2024.

[27] W. Min, M. S. A. Muthanna, M. Ibrahim, R. Alkanhel, A. Muthanna, and A. Laouid, “Privacy-preserving federated UAV data collection framework for autonomous path optimization in maritime operations,” Applied Soft Computing, vol. 173, p. 112906, 2025.

[28] Q. Wang, S. Tang, W. Sun, Y. Zhang, G. Sun, H. Dai, and M. Guizani, “Smart shield: Prevent aerial eavesdropping via cooperative intelligent jamming based on multi-agent reinforcement learning,” IEEE Trans. Mob. Comput., vol. 24, no. 4, pp. 2995–3011, 2025.

[29] J. Huang, A. Wang, G. Sun, J. Li, and X. Zheng, “Physical layer encrypted maritime communications utilizing UAV-enabled virtual antenna array,” in ICC 2024 - IEEE International Conference on Communications, 2024, pp. 67–72.

[30] F. Lu, G. Liu, W. Lu, Y. Gao, J. Cao, N. Zhao, and A. Nallanathan, “Resource and trajectory optimization for UAV-relay-assisted secure maritime MEC,” IEEE Trans. Commun., vol. 72, no. 3, pp. 1641– 1652, 2024.

[31] H. Yang, K. Lin, L. Xiao, Y. Zhao, Z. Xiong, and Z. Han, “Energy harvesting UAV-RIS-assisted maritime communications based on deep reinforcement learning against jamming,” IEEE Trans. Wirel. Commun., vol. 23, no. 8, pp. 9854–9868, 2024.

[32] K. Lin, H. Yang, M. Zheng, L. Xiao, C. Huang, and D. Niyato, “Penalized reinforcement learning-based energy-efficient UAV-RIS assisted maritime uplink communications against jamming,” IEEE Trans. Veh. Technol., vol. 73, no. 10, pp. 15 768–15 773, 2024.

[33] C. Liu, Y. Zhang, G. Niu, L. Jia, L. Xiao, and J. Luan, “Towards reinforcement learning in UAV relay for anti-jamming maritime communications,” Digit. Commun. Networks, vol. 9, no. 6, pp. 1477– 1485, 2023.

[34] G. Sun, X. Zheng, Z. Sun, Q. Wu, J. Li, Y. Liu, and V. C. Leung, “UAV-enabled secure communications via collaborative beamforming with imperfect eavesdropper information,” IEEE Trans. Mob. Comput., vol. 23, no. 4, pp. 3291–3308, 2023.

[35] G. Sun, Y. Wang, Z. Sun, Q. Wu, J. Kang, D. Niyato, and V. C. M. Leung, “Multi-objective optimization for multi-UAV-assisted mobile edge computing,” IEEE Trans. Mob. Comput., vol. 23, no. 12, pp. 14 803–14 820, 2024.

[36] A. Vangala, S. Agrawal, A. K. Das, S. Pal, N. Kumar, P. Lorenz, and Y. Park, “Big data-enabled authentication framework for offshore maritime communication using drones,” IEEE Trans. Veh. Technol., vol. 73, no. 7, pp. 10 196–10 210, 2024.

[37] S. Lee, S. Lee, and H. Kim, “Differential security barriers for virtual emotion detection in maritime transportation stations with cooperative mobile robots and UAVs,” IEEE Trans. Intell. Transport. Syst., vol. 24, no. 2, pp. 2461–2471, 2023.

[38] H. Lei, D. Meng, K. Park, N. Saeed, and G. Pan, “DRL-based resource allocation for aerial IoT systems with no-fly-zones,” IEEE Trans. Aerosp. Electron. Syst., vol. 61, no. 6, pp. 17 892–17 905, 2025.

[39] F. Karami and A. Dariane, “A review and evaluation of multi and many-objective optimization: Methods and algorithms,” Global Journal of Ecology, vol. 7, no. 2, pp. 104–119, 2022.

[40] Z. Ren, X. Han, X. Yu, R. Skjetne, B. J. Leira, S. Sævik, and M. Zhu, “Data-driven simultaneous identification of the 6DOF dynamic model and wave load for a ship in waves,” Mech Syst Signal Pr, vol. 184, p. 109422, 2023.

[41] R. Skulstad, G. Li, T. I. Fossen, B. Vik, and H. Zhang, “A hybrid approach to motion prediction for ship docking-integration of a

neural network model into the ship dynamic model,” IEEE Trans. Instrum. Meas., vol. 70, pp. 1–11, 2020.

[42] G. Sun, J. Xiao, J. Li, J. Wang, J. Kang, D. Niyato, and S. Mao, “Aerial reliable collaborative communications for terrestrial mobile users via evolutionary multi-objective deep reinforcement learning,” IEEE Trans. Mobile Comput., vol. 24, no. 7, pp. 5731–5748, 2025.

[43] H. Tabassum, M. Salehi, and E. Hossain, “Fundamentals of mobility-aware performance characterization of cellular networks: A tutorial,” IEEE Commun. Surv. Tut., vol. 21, no. 3, pp. 2288–2308, 2019.

[44] F. Huang, X. Liao, and Y. Bai, “Multipath channel model for radio propagation over sea surface,” Wirel. Pers. Commun., vol. 90, no. 1, pp. 245–257, 2016.

[45] Y. Wang, W. Feng, J. Wang, and T. Q. S. Quek, “Hybrid satellite-UAV-terrestrial networks for 6G ubiquitous coverage: A maritime communications perspective,” IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3475–3490, 2021.

[46] Y. Zeng, X. Xu, and R. Zhang, “Trajectory design for completion time minimization in UAV-enabled multicasting,” IEEE Trans. Wireless Commun., vol. 17, no. 4, pp. 2233–2246, 2018.

[47] J. Li, G. Sun, Q. Wu, D. Niyato, J. Kang, A. Jamalipour, and V. C. M. Leung, “Collaborative ground-space communications via evolutionary multi-objective deep reinforcement learning,” IEEE J. Sel. Areas Commun., vol. 42, no. 12, pp. 3395–3411, 2024.

[48] S. Sahni, “Approximate algorithms for the 0/1 knapsack problem,” J. ACM, vol. 22, no. 1, pp. 115–124, 1975.

[49] P. Goos, U. Syafitri, B. Sartono, and A. R. Vazquez, “A nonlinear multidimensional knapsack problem in the optimal design of mixture experiments,” Eur. J. Oper. Res., vol. 281, no. 1, pp. 201– 221, 2020.

[50] M. Wu, K. Guo, X. Li, Z. Lin, Y. Wu, T. A. Tsiftsis, and H. Song, “Deep reinforcement learning-based energy efficiency optimization for RIS-aided integrated satellite-aerial-terrestrial relay networks,” IEEE Trans. Commun., vol. 72, no. 7, pp. 4163–4178, 2024.

[51] J. Fan, Z. Wang, Y. Xie, and Z. Yang, “A theoretical analysis of deep Q-learning,” in Learning for dynamics and control. PMLR, 2020, pp. 486–489.

[52] J. Schulman, S. Levine, P. Moritz, M. I. Jordan, and P. Abbeel, “Trust region policy optimization,” CoRR, vol. abs/1502.05477, 2015.

[53] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, “Soft actor-critic: Off-policy maximum entropy deep reinforcement learning with a stochastic actor,” in Proceedings of the 35th International Conference on Machine Learning, ICML, Stockholmsm¨assan, Stockholm, Sweden, July 10-15, 2018, vol. 80, 2018, pp. 1856–1865.

[54] B. Zhang, W. Hu, D. Cao, T. Li, Z. Zhang, Z. Chen, and F. Blaabjerg, “Soft actor-critic–based multi-objective optimized energy conversion and management strategy for integrated energy systems with renewable energy,” Energ Convers Manage, vol. 243, p. 114381, 2021.

[55] G. Sun, W. Xie, D. Niyato, F. Mei, J. Kang, H. Du, and S. Mao, “Generative AI for deep reinforcement learning: Framework, analysis, and use cases,” IEEE Wirel. Commun., vol. 32, no. 3, pp. 186– 195, 2025.

[56] X. Chen, A. Ghadirzadeh, T. Yu, J. Wang, A. Y. Gao, W. Li, L. Bin, C. Finn, and C. Zhang, “LAPO: Latent-variable advantageweighted policy optimization for offline reinforcement learning,” Advances in Neural Information Processing Systems, vol. 35, pp. 36 902–36 913, 2022.

[57] Y. Qing, S. Liu, J. Cong, K. Chen, Y. Zhou, and M. Song, “A2PO: Towards effective offline reinforcement learning from an advantageaware perspective,” Advances in Neural Information Processing Systems, vol. 37, pp. 29 064–29 090, 2024.

[58] K. Sohn, H. Lee, and X. Yan, “Learning structured output representation using deep conditional generative models,” in Annual Conference on Neural Information Processing Systems, 2015, pp. 3483– 3491.

[59] A. E. Sagheer and M. Kotb, “Time series forecasting of petroleum production using deep LSTM recurrent networks,” Neurocomputing, vol. 323, pp. 203–213, 2019.

[60] H. Lei, H. Ran, I. S. Ansari, K. Park, G. Pan, and M. Alouini, “DDPG-based aerial secure data collection,” IEEE Trans. Commun., vol. 72, no. 8, pp. 5179–5193, 2024.

[61] S. Fujimoto, H. Hoof, and D. Meger, “Addressing function approximation error in actor-critic methods,” in International conference on machine learning. PMLR, 2018, pp. 1587–1596.

[62] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy optimization algorithms,” CoRR, vol. abs/1707.06347, 2017.

[63] K. Shafique and M. Shah, “A noniterative greedy algorithm for multiframe point correspondence,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 27, no. 1, pp. 51–65, 2005.

[64] X. Zhang, Y. Tian, and Y. Jin, “A knee point-driven evolutionary algorithm for many-objective optimization,” IEEE Trans. Evol. Comput., vol. 19, no. 6, pp. 761–776, 2014.

![](images/69073542a1a85a0505c088391bb2ed3812c214eebd54728a9b523e52000c025e.jpg)  
Jiawei Huang received a BS degree in Software Engineering from Dalian Jiaotong University, and an MS degree in Software Engineering from Jilin University in 2019 and 2024, respectively. She is currently studying Computer Science at Jilin University to get a Ph.D. degree. Her current research interests are UAV networks and optimization.

![](images/a12cdeb39996bcfffaf512aaa9af344c73537eb6b5673d1be75e93be5ad7383f.jpg)

Aimin Wang received the Ph.D. degree in Communication and Information System from Jilin University, Changchun, China, in 2004. He is currently a professor at Jilin University. His research interests are wireless sensor networks and QoS for multimedia transmission.

![](images/8e3a9df706415d4864698bab70a28f03250c3008e8610d38e86efff868b79c4e.jpg)

![](images/ead7953ce254df02eebeb223e7ab713f8e4227f92641a3b5dd1f4b38c8273782.jpg)

Geng Sun (Senior Member, IEEE) received the B.S. degree in communication engineering from Dalian Polytechnic University, and the Ph.D. degree in computer science and technology from Jilin University, in 2011 and 2018, respectively. He was a Visiting Researcher with the School of Electrical and Computer Engineering, Georgia Institute of Technology, USA. He is a Professor in the College of Computer Science and Technology at Jilin University. His research interests include Low-altitude Wireless Networks,

UAV communications and Networking, Mobile Edge Computing (MEC), Intelligent Reflecting Surface (IRS), Generative AI and Agentic AI, and Deep Reinforcement Learning.

![](images/93d59d1d997d2d003630b0e72a587025d9b440dae40013b79aa996ae83162bd0.jpg)

Jiahui Li (Member, IEEE) received his B.S. in Software Engineering, and M.S. and Ph.D. in Computer Science and Technology from Jilin University, Changchun, China, in 2018, 2021, and 2024, respectively. He was a visiting Ph.D. student at the Singapore University of Technology and Design (SUTD). He currently serves as an assistant researcher in the College of Computer Science and Technology at Jilin University. His current research focuses on integrated airground networks, UAV networks, wireless en-

Jiacheng Wang received the Ph.D. degree from the School of Communication and Information Engineering, Chongqing University of Posts and Telecommunications, Chongqing, China. He is currently a Research Associate in computer science and engineering with Nanyang Technological University, Singapore. His research interests include wireless sensing, semantic communications, and metaverse.

ergy transfer, and optimization.  
![](images/b83d8145d8b751b917276617b16218d1c2ad2ed397b2930349521259e7d75276.jpg)

Weijie Yuan (Senior Member, IEEE) received the joint Ph.D. degree from the University of Technology Sydney, Ultimo, NSW, Australia, and Beijing Institute of Technology, Beijing, China, in 2019. In 2016, he was a Visiting Ph.D. Student with the Institute of Telecommunications, Vienna University of Technology, Austria. From 2017 to 2019, he was a Research Assistant with The University of Sydney, Visiting Associate Fellow with the University of Wollongong, and Visiting Fellow with the University of Southampton. From

2019 to 2021, he was a Research Associate with The University of New South Wales. He is currently the Series Lead Editor of IEEE Communications Magazine, and an Associate Editor for IEEE Transactions on Wireless Communications, IEEE Transactions on Green Communications and Networking, IEEE Communications Letters, IEEE Open Journal of Communications Society, and EURASIP Journal on Advances in Signal Processing. He is the Lead Editor of two feature topics in IEEE Communications Magazine.

![](images/c730876e96a34b9be074a333083dd483c4b7fc1c9f83956a84978107164df04b.jpg)

Xianbin Wang (Fellow, IEEE) received the Ph.D. degree in electrical and computer engineering from the National University of Singapore in 2001. He is a Professor and a Tier-1 Canada Research Chair of 5G and Wireless IoT Communications with Western University, Canada. He has over 600 highly cited journals and conference papers, in addition to over 30 granted and pending patents and several standard contributions. His current research interests include 5G/6G technologies, Internet of Things, machine learning, communications security, and intelligent communications. He is currently a member of the Senate, Senate Committee on Academic Policy, and Senate Committee on University Planning at Western University. He has been involved in many flagship conferences, including GLOBECOM, ICC, VTC, PIMRC, WCNC, CCECE, and ICNC, in different roles, such as General Chair, TPC Chair, Symposium Chair, Tutorial Instructor, Track Chair, Session Chair, and Keynote Speaker. He serves/has served as the Editor-in-Chief, an associate Editor-in-Chief, and an Editor/Associate Editor for over ten journals. He was the Chair of the IEEE ComSoc Signal Processing and Computing for Communications Technical Committee and is currently serving as the Central Area Chair of IEEE Canada. He is a Fellow of the Canadian Academy of Engineering and the Engineering Institute of Canada.