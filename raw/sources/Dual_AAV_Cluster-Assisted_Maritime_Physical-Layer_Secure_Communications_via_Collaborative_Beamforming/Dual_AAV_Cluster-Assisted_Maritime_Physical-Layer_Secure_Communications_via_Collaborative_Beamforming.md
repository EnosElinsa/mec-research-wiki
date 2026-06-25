# Dual AAV Cluster-Assisted Maritime Physical-Layer Secure Communications via Collaborative Beamforming

Jiawei Huang, Aimin Wang, Geng Sun , Senior Member, IEEE, Jiahui Li, Jiacheng Wang Hongyang Du , Member, IEEE, and Dusit Niyato , Fellow, IEEE

Abstract—Autonomous aerial vehicles (AAVs) can be utilized as relay platforms to assist maritime wireless communications. However, complex channels and multipath effects at sea can adversely affect the quality of AAV transmitted signals. Collaborative beamforming (CB) can enhance the signal strength and range to assist the AAV relay for remote maritime communications. However, due to the open nature of AAV channels, security issue requires special consideration. This article proposes a dual AAV cluster-assisted system via CB to achieve physicallayer security in maritime wireless communications. Specifically, one AAV cluster forms a maritime AAV-enabled virtual antenna array (MUVAA) relay to forward data signals to the remote legitimate vessel, and the other AAV cluster forms an MUVAA jammer to send jamming signals to the remote eavesdropper. In this system, we formulate a secure and energy-efficient maritime communication multiobjective optimization problem (SEMCMOP) to maximize the signal-to-interference-plus-noise ratio (SINR) of the legitimate vessel, minimize the SINR of the eavesdropping vessel and minimize the total flight energy consumption of AAVs. Since the SEMCMOP is an NP-hard and large-scale optimization problem, we propose an improved swarm intelligence optimization algorithm with chaotic solution initialization and hybrid solution update strategies to solve the problem. Simulation results indicate that the proposed algorithm outperforms other comparison algorithms, and it can achieve more efficient signal transmission by using the CB-based method.

Received 10 October 2024; revised 7 December 2024; accepted 19 December 2024. Date of publication 23 December 2024; date of current version 25 April 2025. This work was supported in part by the National Natural Science Foundation of China under Grant 62172186, Grant 62272194, and Grant 62471200; in part by the Science and Technology Development Plan Project of Jilin Province under Grant 20240302075GX; in part by the Research Project of Department of Education of Jilin Province under Grant JJKH20231178KJ; in part by the Postdoctoral Fellowship Program of China Postdoctoral Science Foundation under Grant GZC20240592; in part by the China Postdoctoral Science Foundation General Fund under Grant 2024M761123; in part by the Graduate Innovation Fund of Jilin University under Grant 2024CX318; in part by the National Research Foundation, Singapore, and Infocomm Media Development Authority under Its Future Communications Research and Development Programme, Defence Science Organisation (DSO) National Laboratories under the AI Singapore Programme under Grant FCP-NTU-RG-2022-010 and Grant FCP-ASTAR-TG-2022-003; in part by the Singapore Ministry of Education (MOE) Tier 1 under Grant RG87/22; in part by the NTU Centre for Computational Technologies in Finance (NTU-CCTF), Seitee Pte. Ltd.; and in part by the RIE2025 Industry Alignment Fund—Industry Collaboration Projects (IAF-ICP) under Award I2301E0026; administered by A\*STAR, as well as supported by Alibaba Group and NTU Singapore through Alibaba-NTU Global e-Sustainability CorpLab (ANGEL). This article was presented in part at IEEE CSCWD, Rio de Janeiro, Brazil, 2023 [1] [DOI: 10.1109/CSCWD57460.2023.10152552.]. (Corresponding authors: Geng Sun; Jiahui Li.)

Please see the Acknowledgment section of this article for the author affiliations.

Digital Object Identifier 10.1109/JIOT.2024.3521977

Index Terms—Autonomous aerial vehicles (AAVs)-assisted, collaborative beamforming, maritime communications, multiobjective optimization, physical-layer secure.

# I. INTRODUCTION

N RECENT years, owing to the continuous development I of the marine economy, marine services have a wide range of applications in military, civilian, and commercial fields, and it is urgent to establish an efficient and reliable maritime communication network [2], [3]. However, the challenge of installing communications equipment at sea results in lower maritime signal transmission rates than cellular networks at present [4]. Due to the advantages of wide coverage, simple deployment, and low cost, unmanned aerial vehicles (AAVs) can be regarded as effective relay platforms to assist maritime wireless communications [5], [6]. However, the higher flight altitude of AAV brings long-distance communications, which may render gradual signal attenuation during the propagation, further impacting the effectiveness and reliability of the communication link.

Collaborative beamforming (CB) is considered to be a promising method that can enhance the transmission performance of AAVs as a relay. Specifically, multiple array elements on a AAV cluster can form a virtual antenna array (VAA). Then, VAA transmits synchronously among the array elements so that constructive signals are available at the location of the receiving user [7]. Ideally, $N _ { U }$ array elements in the VAA can generate $N _ { U } ^ { 2 }$ times gain to the target via CB [8]. Therefore, CB can improve the communication performance of AAVs at high altitudes without changing the equipment. However, the open channel of the AAVs, as well as the increased transmission range, make the signals more susceptible to malicious eavesdropping [9], [10].

The conventional upper layer decryption and encryption methods require high-computing ability for frequent encoding and decoding, which is extremely challenging for resourcelimited AAVs and marine services [11]. Different from these methods, physical-layer security (PLS) is an effective way to accomplish secure wireless communication due to its strong adaptability [12], [13]. Moreover, the flexibility of AAVs has made them increasingly attractive for maritime PLS applications [14]. For example, Dang-Ngoc et al. [15] presented a AAV-aided friendly jamming architecture to strengthen safety performance by adjusting the positions of the AAVs. Liu et al. [16] designed a maritime anti-jamming transmission framework by using AAVs, and optimized the moving path and power allocation of the AAV to improve the performance. However, the abovementioned power allocation method can decrease the communication rates of legitimate users. Furthermore, these works need the AAVs to fly a long distance from original locations to target locations [17], which consumes much energy. Note that the energy consumption needs to be focused, since it is a critical factor in realistic maritime communications and determines the communication duration. In addition, due to the complexity of the maritime channels, AAVs are more likely to crash when they fly far away from the shore or vessel.

Similarly, based on the long-range transmission characteristic of CB, another set of AAVs can form a VAA as jammer to send jamming signals directly to the remote eavesdropping vessel, protecting data from decoding through noise jamming. In this case, AAVs can form two communication types for long-range and friendly jamming secure maritime wireless communications. Specifically, one AAV cluster forms a maritime AAV-enabled VAA (MUVAA) relay to forward data signals to the legitimate vessel by CB, and the other AAV cluster forms an MUVAA jammer to send jamming signals to the eavesdropper via CB. The CB-based system can be applied to realistic scenarios. For example, vessels are difficult to approach in a disaster situation at sea as the existence of obstacles and limitation of routes [18]. In this case, the VAA can use CB to send real-time data signals to the rescue vessel, and another distant VAA can protect against eavesdropping by sending jamming signals through the CB.

Note that the jamming signals may also be sent to the area of legitimate users, reducing the communication quality of data signals. Thus, we need to precisely design the VAA to reduce the undesirable impact of jamming signals. Since the performance of the VAA is determined by the 3-D positions and excitation current weights of AAVs, making CB implementation complex in such systems. Hence, we require jointly control the positions and excitation current weights of AAVs in the MUVAA relay and MUVAA jammer to optimize the performance of maritime communications. However, this process involves a large number of variables. Moreover, the process of position adjustment also incurs energy consumption, which means that maritime communication efficiency and AAV energy usage are conflicted. Consequently, achieving the tradeoff between the transmission efficiency of VAA and the total flight energy consumption of AAVs is a challenge. In this case, swarm intelligence algorithms have recently advanced, improving their global search capabilities and convergence rates [19]. In the multiobjective optimization problem (MOP), these algorithms excel by efficiently exploring solution spaces to identify Pareto optimal sets and balancing conflicting multiple objectives. Their parallel search and diversity maintenance make them effective for nonlinear MOP [20].

As far as we know, this is the first work to consider the dual AAV cluster-assisted maritime secure communications via CB, analyze conflicts between multiple objectives, and present a novel swarm intelligence algorithm to resolve them. A preliminary version of this work was presented in [1], and the primary contributions of this article are summarized as follows.

1) CB-Based Dual AAV Cluster-Assisted Maritime Secure Communication System: We propose using one AAV cluster to form an MUVAA relay, which can forward data signals to the remote legitimate vessel directly via CB. Then, the other AAV cluster forms an MUVAA jammer which can send jamming signals directly to the remote illegitimate user by CB to protect against eavesdropping. The system can facilitate maritime wireless communications and ensure security while reducing the flight distance of the AAVs, thus improving energy efficiency.

2) MOP Formulation: Considering that the implementation of maritime secure communications and the energy consumption of a AAV are in conflict with each other, we adopt a multiobjective optimization scheme to tradeoff the optimization objectives. Thus, we formulate a secure and energy-efficient maritime communication MOP (SEMCMOP) to enhance transmission efficiency, security, and minimize energy consumption. The SEMCMOP is an NP-hard and large-scale optimization problem, making it more complex to solve.

3) Improved Swarm Intelligence Optimization Algorithm: We utilize swarm intelligence optimization algorithms for dealing with the complex SEMCMOP. Specifically, we propose an improved multiobjective mayfly algorithm (IMOMA) with chaotic solution initialization and hybrid solution update strategies to optimize the AAVs. The IMOMA can enhance the diversity of initial solutions and update the solutions in different dimensions in a targeted manner.

4) Simulations and Findings: The simulation results demonstrate that the CB-based method can achieve more efficient and secure long-distance signal transmission compared to non-CB, single CB, and multihop approaches. Moreover, comparison results show that the proposed IMOMA outperforms other contrasting swarm intelligence algorithms. In addition, IMOMA is particularly significant in protecting against eavesdropping, improving the security-related objective by up to 43.20%, making it highly suitable for secure maritime communications.

The remainder of this work is organized as follows. Section II reviews the related work. Section III gives the models and preliminaries. Section IV formulates the SEMCMOP. Section V presents the algorithm. Section VI illustrates the simulation results. Section VII supplements the relevant discussion and Section VIII summarizes this article.

# II. RELATED WORK

In this section, we review the works associated with relay-assisted maritime wireless communications, maritime communication security strategies, and multiobjective optimization problems. Moreover, we summarize the differences between existing works and current work in Table I.

TABLE I COMPARISON BETWEEN RELATED WORKS AND THIS WORK 

<table><tr><td></td><td colspan="2">Considered scenarios</td><td colspan="2">Security</td><td colspan="3">Optimization objectives</td><td>Optimization methods</td></tr><tr><td>Reference</td><td>Maritime scenario</td><td>UAV-assisted relay</td><td>PLS</td><td>UAV-assisted jamming</td><td>Signal transmission</td><td>Security</td><td>Energy consumption</td><td>Swarm intelligence algorithm</td></tr><tr><td>[21]</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>[22]</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>[23]</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>[4]</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>[24]</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>[25]</td><td>✓</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>[6]</td><td>✓</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td></tr><tr><td>[26]</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[27]</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[28]</td><td>×</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[29]</td><td>✓</td><td>×</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>[30]</td><td>×</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[31]</td><td>✓</td><td>×</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[32]</td><td>✓</td><td>×</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>×</td></tr><tr><td>[33]</td><td>✓</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td></tr><tr><td>[34]</td><td>✓</td><td>×</td><td>✓</td><td>✓</td><td>×</td><td>✓</td><td>×</td><td>✓</td></tr><tr><td>[35]</td><td>×</td><td>✓</td><td>×</td><td>×</td><td>×</td><td>×</td><td>×</td><td>✓</td></tr><tr><td>This work</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr></table>

# A. Relay-Assisted Maritime Communications

Maritime communications are vital for vessel navigation and emergency response. Due to the difficulty of deploying equipment, relying on auxiliary tools to enhance network performance is necessary [21]. For example, Hu et al. [22] proposed a theoretical framework for a low-Earth orbit (LEO) satellite-aided shore-to-ship communication network to obtain the end-to-end transmission performance by considering signal transmissions through either a marine link or a space link. Wu et al. [23] introduced an intelligent spectrum-sharing strategy for satellite maritime networks, enabling satellites to evaluate channel allocation actions to optimize throughput and spectrum efficiency. However, satellite-assisted maritime communications face latency problems over long distances. Moreover, Wang et al. [4] utilized an unmanned surface vessel (USV) to assist maritime wireless communications and demonstrated the benefits of USV-assisted mobile relaying. Zeng et al. [24] considered a USV-enabled maritime wireless network, where a USV is employed to assist the communications between the terrestrial base station and ships. However, the off-shore propagation conditions are influenced by sea surface reflection and scattering, which lead to multipath effects and deteriorate the quality of the received signals [36], [37]. Moreover, the slow mobility of USVs limits their communication coverage and flexibility, and waves can pose safety risks to their operation.

In recent years, a AAV has been used as an effective and convenient tool to assist maritime communications due to its flexibility and ease of deployment. For example, Liu et al. [38] established a two-layer AAV-enabled maritime communication network, which is employed to solve the latency minimization problem for computation and communication. Qian et al. [6] considered a AAV-assisted maritime Internet of Things (M-IoT) network to improve the workload computation and energy efficiency of offloading transmission. However, AAVs operating at higher altitudes may encounter signal attenuation over long distances, thereby adversely impacting the overall communication performance. In this case, CB can adjust the amplitude and phase of signals through the cooperation of multiple transmitting antennas so that the signals can be superimposed at the receiving end, thus improving signal strength and coverage [39]. Therefore, based on CB, multiple AAVs form a VAA to enhance the synthetic gain of the signal to achieve long-distance maritime communications.

# B. Maritime Communication Security Strategies

Due to the open nature of the maritime channels, security issues need to be taken into account during communications. For instance, Aman et al. [26] systematically discussed the security needs and solutions of air–water wireless communication networks. Vangala et al. [27] proposed a new lightweight authentication protocol by utilizing drone technology in conjunction with the 5G mobile network communications, withstanding various security attacks and maintaining low communication and computation costs. Ren et al. [28] presented a novel physically unclonable function-based access authentication scheme to achieve mutual authentication and privacy protection in the AAV-aided satellite-terrestrial integration networks. However, the energy of the encryption and decryption methods in the abovementioned works depends on the amount of transmitted data. When the data is larger, computational energy is more immense, making the methods unsuitable for an energy-limited maritime environment. In addition, complex key distribution and management mechanisms increase the complexity of communications.

Since the PLS can dynamically adjust the security mechanism based on the channel states, and the dynamic deployment characteristics of AAVs, there have been many studies that considered AAVs for PLS maritime communications. For instance, Wang et al. [30] investigated a dual-AAV-enabled secure communication system, in which a AAV sends confidential messages to a mobile user while another cooperative AAV sends artificial noise signals to confuse malicious eavesdroppers, improving a worst case secrecy rate. Lu et al. [31] proposed an efficient secure communication scheme for AAVrelay-assisted maritime mobile edge computing (MEC) with a flying eavesdropper, to maximize the secure computing capacity of maritime devices. Liu et al. [25] proposed a reinforcement learning-based AAV relay policy for maritime communications to resist jamming attacks and decrease the bit-error-rate of the maritime signals. Note that the implementations of the abovementioned works require optimizing the 3-D trajectories or power allocation of AAVs. However, the power allocation approach can decrease the communication rates of the target receivers. In addition, the AAVs need to fly from original locations to target locations to improve communication performance, which inevitably increases their flight energy consumption and reduces the corresponding lifetime. Therefore, AAVs can form VAA to send jamming signals to the remote illegitimate eavesdropper via CB, which allows AAVs to achieve secure maritime communications without long-distance flight. Note that CB has limitations, such as increased communication overhead for data sharing and limited support for multiple users. However, it remains a promising solution for enhancing secure maritime communications, offering significant benefits in signal quality and energy efficiency.

# C. Multiobjective Optimizations

The previous approach, which combines multiple objectives into a single one [25], [40], can be effective while it lacks flexibility, making it difficult to quickly evaluate and select the most appropriate tradeoffs. In this case, multiobjective optimization methods can be used to address various tradeoffs in different scenarios, enabling optimal decision-making. Consequently, the following are multiobjective optimization methods for handling MOP. First, the weighted sum method transforms multiple objectives into a single objective by weighted summing, where different objectives are assigned different weights, and the total value of the objective function is the weighted sum [41], [42]. However, the method requires predefined weight coefficients and may reduce the solution space. Moreover, when the Pareto front (PF) is nonconvex, the weighted sum method may not get the complete set of Pareto optimal solutions. Second, deep reinforcement learning (DRL) is increasingly used to solve MOP by learning policies, which integrates PF approximation to balance multiple conflicting objectives. For instance, Yang et al. [32] explored a AAVassisted maritime communication scheme using reconfigurable intelligent surfaces to enhance energy efficiency while defending against jamming attacks, ensuring quality of service. Luo et al. [33] developed a DRL-optimized method that allows AAVs to predict buoy positions and optimize movement control to enhance beam pointing and maintain stable lineof-sight (LoS) communication for efficient maritime data transmission. However, DRL is more suitable for continuous time-slot problems in real-time decision-making scenarios. When applied to the transient MOP in this article, it may incur additional computational overhead in the training phase, wasting valuable maritime resources. In addition, DRL can further address the challenge of vessels in continuous motion, requiring AAVs to dynamically adjust their positions to maintain communications, which will be explored in subsequent work.

Furthermore, multiobjective swarm intelligence optimization algorithms introduce Pareto dominant to find a set of candidate solutions for MOP. For example, Hashim and Abido [34] proposed the multiobjective particle swarm optimization to tradeoff two objectives and defined a set of nondominated solutions on the PF that gave the optimal compromise solutions. Qiu and Duan [35] adapted a multiobjective pigeon-inspired optimization algorithm to coordinate AAVs, ensuring stable flight formations in complex environments. However, our problem contains a large number of variables with different boundary values, which is challenging for classical swarm intelligence algorithms. Therefore, we intend to propose a novel swarm intelligence algorithm to handle multiple decision variables in the considered scenario.

Different from previous works, this article utilizes AAVs to achieve remote maritime communications based on CB while noting the security issues of the process. Moreover, a corresponding improved algorithm is proposed for solving the MOP in this scenario. In summary, our approach uniquely extends transmission range, enhances security, and energy efficiency, making a significant contribution to secure maritime communications.

# III. MODELS AND PRELIMINARIES

In this section, we present the CB-based dual AAV clusterassisted maritime secure communication system. Then, we give the communication models and energy consumption model of the AAV.

# A. System Overview

Fig. 1 shows the CB-based dual AAV cluster-assisted maritime secure communication system model, which includes a land base station (LBS), a legitimate vessel denoted as Bob, an illegitimate vessel denoted as Willie, and two AAV clusters. Due to infrastructure limitations in the maritime environment and the large vessel Bob cannot move close to the coast, it is challenging for the LBS to communicate with the remote Bob directly. Therefore, a set of rotary-wing AAVs denoted as $\mathcal { U } _ { R } = \{ 1 , 2 , \dots , N _ { U R } \}$ are dispatched as a cluster to receive and forward data signals by the data link, whereas Willie aims to eavesdrop on the link. To restraint Willie, the other set of AAVs marked as $\mathcal { U } _ { J } = \{ 1 , 2 , \dots , N _ { U J } \}$ sends jamming signals to Willie. In this work, the specific shipping-lanes can be obtained to determine the directions and locations of vessels in advance. Moreover, the AAV is assumed to be fitted with a single omnidirectional antenna and global positioning system (GPS), and the information of illegitimate vessels can be detected by optical cameras or synthetic aperture radar installed on the AAV.

![](images/51dc3934f6bd0d7ed80291805e8df7cd3e217719c3cd1838cd1866998bbb76d1.jpg)

<details>
<summary>text_image</summary>

Z
MUVAA Jammer
y
x
Mainlobe
Interference
Willie
Bob
Eavesdropping
Mainlobe
LBS
Jamming Link
Data Link
MUVAA Relay
</details>

Fig. 1. CB-based dual AAV cluster-assisted maritime secure communication system.

The process begins with LBS sending data signals to the dispatched $\mathcal { U } _ { R } \mathrm { \ A A V s }$ by the ground-to-air (G2A) data link. Next, the AAV cluster forms the MUVAA relay and forwards data signals to Bob by the air-to-sea (A2S) data link. Then, $\mathcal { U } _ { J }$ AAVs can depart from their original hovering positions, and form an MUVAA jammer to send jamming signals to Willie by the A2S jamming link. We consider that the AAVs in the same VAA are synchronized in terms of the carrier frequency, initial phase, and time [43], and these AAVs can achieve data sharing by using the method in [44]. Note that we analyze the operations of AAVs in a specific scenario. Specifically, Bob and Willie are located at fixed positions when the AAVs send signals to them. This allows us to derive a clear understanding of the performance of the system under specific conditions and lays the foundation for future studies of dynamic factors.

In this process, the LBS as the central node of data signals can efficiently get the channel state information (CSI) of objects through centralized control, feedback mechanisms, and channel estimation techniques [45]. Moreover, we consider that the AAVs obtain the quantified version of the CSI through the approaches in [46]. The balance between the CSI code rates and the quantization errors needs to be optimized, as the lower code rate can reduce the description of the CSI accuracy and increase the errors. To demonstrate the general applicability of this work, we employ the 3-D Cartesian coordinate system, in which the positions of Bob, Willie, LBS, the mth AAV in the MUVAA relay, and nth AAV in the MUVAA jammer are denoted as $( { \bar { x } } ^ { B } , \ y _ { . . . } ^ { B } , \ z ^ { B } ) , \ ( { \underline { { x } } } ^ { W }$ , $y ^ { W } , \ z ^ { W } ) , \ ( x ^ { L } , \ y ^ { \ L } , \ z ^ { L } ) , \ ( x _ { m } ^ { U r } , \ y _ { m } ^ { U r } , \ z _ { m } ^ { U r } )$ , and $( x _ { n } ^ { U j } , ~ y _ { n } ^ { U j } , ~ z _ { n } ^ { U j } )$ respectively. Subsequently, we give the key model associated with communications.

# B. Communication Models

In our considered system, there are three types of communication links: 1) the G2A data link to send data signals from the LBS to MUVAA relay; 2) the A2S data link to forward data signals between the MUVAA relay and Bob, which might be eavesdropped by Willie; and 3) the A2S jamming link from the MUVAA jammer, that is, used to send jamming signals to Willie and might interfere with Bob. Next, we elaborate on the three links.

1) G2A Data Link From the LBS to MUVAA Relay: In the considered system, a CB-based AAV relay can forward data signals from an LBS to Bob, and the specific process is as follows. First, the LBS utilizes CB to send data signals to AAV in $\mathcal { U } _ { R } ,$ , which immediately caches or forwards the signals based on channel conditions or node ranges. Specifically, the LBS is usually configured with a large number of antennas and can perform channel estimation through massive multipleinput–multiple-output (MIMO) [47]. In addition, the LBS has powerful computation and processing capabilities to obtain accurate CSI of the AAVs. Therefore, the LBS can calculate the weights of beam patterns based on CSI to focus on the AAV direction, thus efficiently sending signals over longer distances. Then, the AAV broadcasts the received data signals to all AAVs in $\mathcal { U } _ { R }$ Due to the high altitude of the AAVs, the airborne transmission follows the LoS channel conditions [39]. Finally, the AAVs form the MUVAA relay based on the assigned weights for coordinated transmission.

We can accomplish the abovementioned process by satisfying the information dissemination constraint in the following ways. First, the airborne signal sharing process among AAVs in the MUVAA relay usually has a small transmission distance and good channel conditions, which achieve high-broadcast rates of airborne AAVs. Moreover, the signal sharing process can be implemented by using many low-cost and efficient methods [44]. Therefore, the transmission rates of the CBbased relay system are not constrained by the airborne signal sharing phase. Second, our proposed signal relaying method can be offline, i.e., the data has been uploaded to the AAV. At this point, the transmission rates from the LBS to the AAV in the MUVAA relay can be reasonably omitted. Moreover, the LBS can dynamically adjust the uplink transmission rates depending on the signal relay rates of the AAV. Therefore, the information transfer performed in the G2A data link is reliable. Finally, the AAVs usually have a storage device with some caching capability. Therefore, when the signal rates of the G2A data link are higher than that of the A2S data link, the AAVs can first cache some of the data and then send it to the legitimate vessel in unison [7]. In summary, in our considered system, the LBS can conduct spectrum and power allocation, and it has adequate transmission power [48], which means that the LBS can automatically adapt the G2A data link transmission rates by the A2S data link.

2) A2S Data Link From MUVAA Relay to Bob: Mathematically, we use the array factor to measure the strength of the data signals in different directions for MUVAA relay [49], which is represented as follows:

$$
\begin{array}{l} A F _ {r} (\theta , \phi) = \\ \sum_ {m = 1} ^ {N _ {U R}} I _ {m} ^ {U r} e ^ {\iota \left[ k _ {c} \left(x _ {m} ^ {U r} \sin \theta \cos \phi + y _ {m} ^ {U r} \sin \theta \sin \phi + z _ {m} ^ {U r} \cos \theta\right) \right]} \tag {1} \\ \end{array}
$$

where $I _ { m } ^ { U r }$ denotes the excitation current weight of the mth AAV in the MUVAA relay and $\theta \in [ 0 , \pi ]$ and $\phi \in [ - \pi , \pi ]$ denote the elevation and azimuth angles under the A2S data link, respectively. In addition, ι is imaginary units, $k _ { c } = 2 \pi / \lambda$ and λ denotes the wavelength.

TABLE II DEFINITION OF THE VARIABLES 

<table><tr><td>Variable expression</td><td>Variable elements</td><td>Variable Declarations</td></tr><tr><td> $\mathbb{P}_{r}$ </td><td> $\{\mathbb{P}_{r} = \mathbb{X}_{r}, \mathbb{Y}_{r}, \mathbb{Z}_{r}\},$  $\{\mathcal{P}_{m}^{Ur} = (x_{m}^{Ur}, y_{m}^{Ur}, z_{m}^{Ur}) | m \in \mathcal{U}_{R}\}$ </td><td> $\mathbb{P}_{r}$  represents the relay set including positions of all UAVs in the MUVAA relay, $\mathbb{X}_{r}$  and  $\mathbb{Y}_{r}$  are the horizontal positions of UAVs,  $\mathbb{Z}_{r}$  is the vertical positions of UAVs, $\mathcal{P}_{m}^{Ur}$  represents the position of the  $m$ th UAV in the MUVAA relay.</td></tr><tr><td> $\mathbb{P}_{j}$ </td><td> $\{\mathbb{P}_{j} = \mathbb{X}_{j}, \mathbb{Y}_{j}, \mathbb{Z}_{j}\},$  $\left\{ \mathcal{P}_{n}^{Uj} = (x_{n}^{Uj}, y_{n}^{Uj}, z_{n}^{Uj}) | n \in \mathcal{U}_{J} \right\}$ </td><td> $\mathbb{P}_{j}$  denotes the set of positions of all UAVs in the MUVAA jammer, $\mathbb{X}_{j}$  and  $\mathbb{Y}_{j}$  are the horizontal positions of UAVs,  $\mathbb{Z}_{j}$  is the vertical positions of UAVs, $\mathcal{P}_{n}^{Uj}$  represents the position of the  $n$ th UAV in the MUVAA jammer.</td></tr><tr><td> $\mathbb{I}_{r}$ </td><td> $\{I_{m}^{Ur}| m \in \mathcal{U}_{R}\}$ </td><td> $\mathbb{I}_{r}$  is the set of excitation current weights of all UAVs in the MUVAA relay, $I_{m}^{Ur}$  is the excitation current weight of the  $m$ th in the MUVAA relay.</td></tr><tr><td> $\mathbb{I}_{j}$ </td><td> $\left\{ I_{n}^{Uj} | n \in \mathcal{U}_{J} \right\}$ </td><td> $\mathbb{I}_{j}$  is the set of excitation current weights of all UAVs in the MUVAA jammer, $I_{n}^{Uj}$  is the excitation current weight of the  $n$ th in the MUVAA jammer.</td></tr></table>

Then, the antenna gain from the AAVs in the MUVAA relay to the vessel is denoted by

$$
G _ {v} \left(\mathbb {P} _ {r}\right) = \frac {4 \pi \left| A F _ {r} \left(\theta_ {v} , \phi_ {v}\right) \right| ^ {2} \omega \left(\theta_ {v} , \phi_ {v}\right) ^ {2}}{\int_ {0} ^ {2 \pi} \int_ {0} ^ {\pi} \left| A F _ {r} (\theta , \phi) \right| ^ {2} \omega (\theta , \phi) ^ {2} \sin \theta d \theta d \phi} \eta \tag {2}
$$

where $\mathbb { P } _ { r } = \{ \mathbb { X } _ { r } , \mathbb { Y } _ { r } , \mathbb { Z } _ { r } \}$ denotes the set of AAV positions in the MUVAA relay, which is one of the decision variables of the system. The definitions of this variable and other relevant variables in this article are detailed in Table II. Moreover, $( \theta _ { \nu } , \phi _ { \nu } )$ and $\omega ( \theta , \phi )$ denote the direction toward a vessel (either Bob or Willie) and magnitude of the far-field beam pattern of a AAV under the A2S data link, respectively, and $\eta \in [ 0 , 1 \bar { . }$ ] denotes the antenna array efficiency [7]. In addition, the main notations are summarized in Table III.

Then, during the A2S transmission, the antenna heights of AAVs are significantly greater than those of vessels. Thus, the path loss from MUVAA relay to the vessel can be expressed as follows [50]:

$$
\begin{array}{l} P L (\mathbb {P} _ {r}) [ d B ] = \frac {A _ {U}}{1 + \alpha_ {a} e ^ {- \alpha_ {b} (\theta - \alpha_ {a})}} + 2 0 \log_ {1 0} ^ {d} + C _ {r} \\ + 2 0 \log_ {1 0} ^ {(4 \pi f _ {c} / 3 0 0)} \tag {3} \\ \end{array}
$$

where $d = \sqrt { ( x _ { r } - x _ { \nu } ) ^ { 2 } + ( y _ { r } - y _ { \nu } ) ^ { 2 } + ( z _ { r } - z _ { \nu } ) ^ { 2 } }$ and $\theta \ =$ $( 1 8 0 / \pi ) \arcsin ( z _ { r } / d )$ , wherein $x _ { r } = \mathbb { E } ( \mathbb { X } _ { r } ) , y _ { r } = \mathbb { E } ( \mathbb { Y } _ { r } ) , z _ { r } =$ $\mathbb { E } ( \mathbb { Z } _ { r } )$ . E(·) is a mean operator, that is, used to calculate the average value of each row of a matrix, and $( x _ { \nu } , y _ { \nu } , z _ { \nu } )$ is the 3-D location at a vessel (either Bob or Willie). Moreover, $f _ { c }$ is the carrier frequency in MHz, and $A _ { U } , C _ { r } , \alpha _ { a }$ and $\alpha _ { b }$ are environment-related constant parameters in dB.

3) A2S Jamming Link From MUVAA Jammer to Willie: Similarly, the array factor is used to evaluate the strength of jamming signals of the MUVAA jammer, which is given by

$$
\begin{array}{l} A F _ {j} \left(\theta^ {\prime}, \phi^ {\prime}\right) = \\ \sum_ {n = 1} ^ {N _ {U J}} I _ {n} ^ {U j} e ^ {\iota \left[ k _ {c} \left(x _ {n} ^ {U j} \sin \theta^ {\prime} \cos \phi^ {\prime} + y _ {n} ^ {U j} \sin \theta^ {\prime} \sin \phi^ {\prime} + z _ {n} ^ {U j} \cos \theta^ {\prime}\right) \right]} \tag {4} \\ \end{array}
$$

where $I _ { n } ^ { U j }$ denotes the excitation current weight of the nth AAV in the MUVAA jammer, and $\theta ^ { \prime } \in [ 0 , \pi ]$ and $\phi ^ { \prime } \in [ - \pi , \pi ]$ denote the elevation and azimuth angles under the jamming link, respectively.

Correspondingly, the antenna gain from the AAVs in the MUVAA jammer to the vessel is as follows:

$$
G _ {v} ^ {\prime} \left(\mathbb {P} _ {j}\right) = \frac {4 \pi \left| A F _ {j} \left(\theta_ {v} ^ {\prime} , \phi_ {v} ^ {\prime}\right) \right| ^ {2} \omega \left(\theta_ {v} ^ {\prime} , \phi_ {v} ^ {\prime}\right) ^ {2}}{\int_ {0} ^ {2 \pi} \int_ {0} ^ {\pi} \left| A F _ {j} \left(\theta^ {\prime} , \phi^ {\prime}\right) \right| ^ {2} \omega \left(\theta^ {\prime} , \phi^ {\prime}\right) ^ {2} \sin \theta^ {\prime} d \theta^ {\prime} d \phi^ {\prime}} \eta (5)
$$

where $\mathbb { P } _ { j } = \{ \mathbb { X } _ { j } , \mathbb { Y } _ { j } , \mathbb { Z } _ { j } \}$ denotes the set of AAV positions in the MUVAA jammer, which is shown in Table II. Moreover, $( \theta _ { \nu } ^ { \prime } , \phi _ { \nu } ^ { \prime } )$ is the direction to a vessel (either Bob or Willie) under the jamming link, and $\omega ( \theta ^ { \prime } , \phi ^ { \prime } )$ denotes the magnitude of the far-field beam pattern of a AAV under the jamming link.

Then, from the MUVAA jammer, the transmission path loss toward the vessel is calculated by

$$
\begin{array}{l} P L ^ {\prime} \left(\mathbb {P} _ {j}\right) [ d B ] = \frac {\eta_ {\mathrm{LOS}} - \eta_ {\mathrm{NLOS}}}{1 + \alpha_ {a} e ^ {- \alpha_ {b} \left(\theta^ {\prime} - \alpha_ {a}\right)}} + \eta_ {\mathrm{NLOS}} \\ + 2 0 \left(\log_ {1 0} ^ {(4 \pi f _ {c} / 3 0 0)} + \log_ {1 0} ^ {d ^ {\prime}}\right) \tag {6} \\ \end{array}
$$

where $d ^ { \prime } = \sqrt { ( x _ { j } - x _ { \nu } ) ^ { 2 } + ( y _ { j } - y _ { \nu } ) ^ { 2 } + ( z _ { j } - z _ { \nu } ) ^ { 2 } }$ is the distance between the center of MUVAA jammer and the vessel (either Bob or Willie), wherein $x _ { j } = \mathbb { E } ( \mathbb { X } _ { j } ) , y _ { j } = \mathbb { E } ( \mathbb { Y } _ { j } ) , z _ { j } =$ $\mathbb { E } ( \mathbb { Z } _ { j } )$ . Moreover, $\theta ^ { \prime } = ( 1 8 0 / \pi )$ arcsin(zj/d ), ηLOS and ηNLOS are the corresponding parameters shown in Table IV.

Signal-to-interference-plus-noise ratio (SINR) is a key metric to measure signal quality in wireless communications. Specifically, SINR reflects the channel condition by the ratio of the useful signal strength to the sum of interference and noise. Therefore, based on the A2S data link and A2S jamming link, the obtainable SINR of Bob is expressed as

$$
\gamma_ {\mathrm{Bob}} = \frac {P _ {U R} N _ {U R} G _ {B} P L _ {B}}{P _ {U J} N _ {U J} G _ {B} ^ {\prime} P L _ {B} ^ {\prime} + \sigma^ {2}} \tag {7}
$$

where $P _ { U R }$ and $P _ { U J }$ are the transmission powers of AAV in the MUVAA relay and MUVAA jammer, and $N _ { U R }$ and $N _ { U J }$ are the numbers of AAVs in the MUVAA relay and MUVAA jammer, respectively. Moreover, $G _ { B }$ and $G _ { B } ^ { \prime }$ can be obtained by replacing (2) and (5) with $( \theta _ { \nu } , \phi _ { \nu } ) = ( { \bar { \theta _ { B } } } , \phi _ { B } ) , ( \theta _ { \nu } ^ { \prime } , \phi _ { \nu } ^ { \prime } ) =$ $( \theta _ { B } ^ { \prime } , \phi _ { B } ^ { \prime } ) , P L _ { B }$ and $P L _ { B } ^ { \prime }$ are required according to (3) and (6) with $d = d _ { B }$ and $d ^ { \prime } = { d _ { B } ^ { \prime } } ,$ respectively. In addition, $\sigma ^ { 2 }$ is the additive white Gaussian noise.

TABLE III SUMMARY OF MAIN NOTATIONS 

<table><tr><td>Notation</td><td>Meaning</td></tr><tr><td colspan="2">Notation in system model</td></tr><tr><td> $\theta$ </td><td>Elevation angle between the MUVAA relay and vessel</td></tr><tr><td> $\phi$ </td><td>Azimuth angle between the MUVAA relay and vessel</td></tr><tr><td> $AF_r(\cdot)$ </td><td>Array factor of the MUVAA relay</td></tr><tr><td> $\lambda$ </td><td>Wavelength</td></tr><tr><td> $G_v(\cdot)$ </td><td>Antenna gain of the MUVAA relay</td></tr><tr><td> $PL(\cdot)$ </td><td>Path loss from the MUVAA relay</td></tr><tr><td> $d$ </td><td>Distance from the center of MUVAA relay to vessel</td></tr><tr><td> $\theta'$ </td><td>Elevation angle between the MUVAA jammer and vessel</td></tr><tr><td> $\phi'$ </td><td>Azimuth angle between the MUVAA jammer and vessel</td></tr><tr><td> $AF_j(\cdot)$ </td><td>Array factor of the MUVAA jammer</td></tr><tr><td> $G'_v(\cdot)$ </td><td>Antenna gain of the MUVAA jammer</td></tr><tr><td> $PL'(\cdot)$ </td><td>Path loss from the MUVAA jammer</td></tr><tr><td> $d'$ </td><td>Distance from the center of MUVAA jammer to vessel</td></tr><tr><td> $v_m$ </td><td>Mean rotor induced velocity in hovering</td></tr><tr><td> $v_t$ </td><td>Tip speed of the rotor blade</td></tr><tr><td> $d_f$ </td><td>Fuselage drag ratio</td></tr><tr><td> $s_r$ </td><td>Rotor solidity</td></tr><tr><td> $\rho_a$ </td><td>Air density</td></tr><tr><td> $a_r$ </td><td>Rotor disc area</td></tr><tr><td colspan="2">Notation in the IMOMA</td></tr><tr><td>N</td><td>Population size</td></tr><tr><td> $ub_r$ </td><td>Upper bound of relay set</td></tr><tr><td> $lb_r$ </td><td>Lower bound of relay set</td></tr><tr><td> $ub_j$ </td><td>Upper bound of jammer set</td></tr><tr><td> $lb_j$ </td><td>Lower bound of jammer set</td></tr><tr><td>M</td><td>Coefficients of the AOA</td></tr><tr><td> $M'$ </td><td>Coefficients of the AOA</td></tr><tr><td> $\zeta$ </td><td>Threshold</td></tr><tr><td>a</td><td>Parameter of Tent mapping</td></tr><tr><td> $\mu$ </td><td>Control parameter of the AOA</td></tr><tr><td>j</td><td>An elite solution of jammer set</td></tr><tr><td>r</td><td>An elite solution of relay set</td></tr><tr><td>Max</td><td>Maximum value of the accelerated function of the AOA</td></tr><tr><td>Min</td><td>Minimum value of the accelerated function of the AOA</td></tr></table>

Correspondingly, we set $( \theta _ { \nu } , \phi _ { \nu } ) \ = \ ( \theta _ { W } , \phi _ { W } ) , \ d \ = \ d _ { W }$ , $( \theta _ { \nu } ^ { \prime } , \phi _ { \nu } ^ { \prime } ) = ( \theta _ { W } ^ { \prime } , \phi _ { W } ^ { \prime } )$ , and $d ^ { \prime } = d _ { W } ^ { \prime }$ to replace (2), (3), (5), and (6), the obtainable SINR of Willie can be expressed as

$$
\gamma_ {\text {Willie}} = \frac {P _ {U R} N _ {U R} G _ {W} P L _ {W}}{P _ {U J} N _ {U J} G _ {W} ^ {\prime} P L _ {W} ^ {\prime} + \sigma^ {2}}. \tag {8}
$$

As aforementioned, the positions of the vessels are not adjustable, and the 3-D positions and excitation current weights of AAVs are the key decision variables to affect maritime communications effectiveness. Moreover, the process of regulating the 3-D positions of the AAVs consumes their energy. Next, we introduce the moving energy consumption model for the AAV.

# C. Energy Consumption Model of the AAV

In general, the communication and propulsion energy consumption compose the total flight energy consumption of AAVs. However, the value of communication energy consumption is minimal, and it is often neglected in the calculation [51]. Thus, when a rotary-wing AAV flies horizontally in 2-D, the propulsion power consumption can be calculated by

TABLE IV MAIN PARAMETERS IN THE SIMULATION PROCESS 

<table><tr><td>Notation</td><td>Meaning</td><td>Default value</td></tr><tr><td> $f_c$ </td><td>Carrier frequency</td><td>2.4 GHz</td></tr><tr><td> $P_{UR}$ </td><td>Transmission power of each UAV in the MUVAA relay</td><td>0.1 W</td></tr><tr><td> $P_{UJ}$ </td><td>Transmission power of each UAV in the MUVAA jammer</td><td>0.1 W</td></tr><tr><td> $\sigma^2$ </td><td>Power of additive white Gaussian noise</td><td>-150 dBm</td></tr><tr><td> $m_U$ </td><td>Aircraft mass</td><td>2 kg</td></tr><tr><td> $\eta_{LOS}$ </td><td>Attenuation factor for LoS links</td><td>2.3 dB</td></tr><tr><td> $\eta_{NLOS}$ </td><td>Attenuation factor for NLoS links</td><td>34 dB</td></tr><tr><td> $\alpha_a$ </td><td>Sigmoid function parameter</td><td>5.0188 dB</td></tr><tr><td> $\alpha_b$ </td><td>Sigmoid function parameter</td><td>0.3511 dB</td></tr><tr><td> $C_U$ </td><td>Constant parameter</td><td>1 dB</td></tr><tr><td> $C_r$ </td><td>Environment-related parameter</td><td>34 dB</td></tr><tr><td> $Lr_{min}$ </td><td>Minimum horizontal scope of  $\mathcal{U}_R$ </td><td>0 m</td></tr><tr><td> $Lr_{max}$ </td><td>Maximum horizontal scope of  $\mathcal{U}_R$ </td><td>100 m</td></tr><tr><td> $Lj_{xmin}$ </td><td>Minimum x-axis horizontal scope of  $\mathcal{U}_J$ </td><td>4400 m</td></tr><tr><td> $Lj_{xmax}$ </td><td>Maximum x-axis horizontal scope of  $\mathcal{U}_J$ </td><td>4500 m</td></tr><tr><td> $Lj_{ymin}$ </td><td>Minimum y-axis horizontal scope of  $\mathcal{U}_J$ </td><td>4300 m</td></tr><tr><td> $Lj_{ymax}$ </td><td>Maximum y-axis horizontal scope of  $\mathcal{U}_J$ </td><td>4400 m</td></tr><tr><td> $H_{min}$ </td><td>Minimum vertical scope of  $\mathcal{U}_R$  and  $\mathcal{U}_J$ </td><td>60 m</td></tr><tr><td> $H_{max}$ </td><td>Maximum vertical scope of  $\mathcal{U}_R$  and  $\mathcal{U}_J$ </td><td>120 m</td></tr><tr><td> $P_R$ </td><td>Transmission power of the UAV-R</td><td>0.1 W</td></tr><tr><td> $P_J$ </td><td>Transmission power of the UAV-J</td><td>0.1 W</td></tr></table>

$$
\begin{array}{l} P (v) = P _ {I} \left(\sqrt {1 + \frac {v ^ {4}}{4 v _ {m} ^ {4}}} - \frac {v ^ {2}}{2 v _ {m} ^ {2}}\right) ^ {\frac {1}{2}} + P _ {B} \left(1 + \frac {3 v ^ {2}}{v _ {t} ^ {2}}\right) \\ + \frac {1}{2} d _ {f} s _ {r} \rho_ {a} a _ {r} v ^ {3} \tag {9} \\ \end{array}
$$

where v is the velocity of the AAV, and $P _ { I }$ and $P _ { B }$ represent the induced power and blade profile power in the hovering conditions, respectively. $\nu _ { m }$ is the mean rotor induced velocity in hovering, $\nu _ { t }$ is the tip speed of the rotor blade, and $d _ { f } , s _ { r } ,$ $\rho _ { a }$ and $a _ { r }$ represent the fuselage drag ratio, rotor solidity, air density, and rotor disc area, respectively.

Note that the additional energy consumption of AAVs from acceleration and deceleration during horizontal flight is negligible, as it takes up only a small fraction of the entire running time of AAVs. Therefore, based on the propulsion energy consumption, movement and gravity energy consumption in the case of ascent and descent with time, the energy consumption of 3-D trajectory of AAV using the heuristic closed-form approximation is expressed by [52]

$$
\begin{array}{l} E (T) \approx \int_ {0} ^ {T} P (v (t)) d t + \frac {1}{2} m _ {U} \left(v (T) ^ {2} - v (0) ^ {2}\right) \\ + m _ {U} g (h (T) - h (0)) \tag {10} \\ \end{array}
$$

where v(t) is the instantaneous velocity of the AAV at time t and T is the time duration of the AAV flight. Moreover, mU and g are the aircraft mass of a AAV and gravitational acceleration, respectively.

According to the energy consumption model, we can summarize that the energy consumption of the AAVs is primarily related to their positions. Therefore, the positions of AAVs in the MUVAA relay and MUVAA jammer have a critical influence on communication effectiveness.

# IV. PROBLEM FORMULATION AND ANALYSIS

In this section, we specify the problem of the considered system. Then, we propose the optimization objectives and formulate the SEMCMOP. Next, the problem is analyzed.

# A. Problem Statement

The main objective of this article is to achieve remote maritime communications and ensure security while saving energy consumption of the AAV. On the one hand, since the LBS is far from Bob, making direct communication challenging, we utilize CB for the remote transmission. Specifically, in a maritime square monitoring area denoted as $A _ { s r } ,$ NUR AAVs form the MUVAA relay and forward data signals to Bob directly. As the vessel moves along its fixed trajectory, the transmission performance of the data signals mainly depends on the beam pattern of the MUVAA relay. To improve the transmission efficiency, the beam patterns can be optimized to point toward Bob to obtain more directional signals. On the other hand, to enhance the communication security, $N _ { U J }$ AAVs forming MUVAA jammer interfere with Willie receiving signals, which may have an impact on Bob. In this case, we optimize the beam patterns of the MUVAA jammer to emit stronger jamming signals toward Willie. As mentioned above, the 3-D positions and excitation current weights of AAVs in the VAA jointly determine the beam patterns.

According to the abovementioned description, the relevant decision variables to be jointly optimized are as follows: 1) $\mathbb { P } _ { r }$ denotes the 3-D position set of AAVs in the MUVAA relay; 2) $\mathbb { P } _ { j }$ denotes the 3-D position set of AAVs in the MUVAA jammer; 3) Ir is the excitation current weights set of AAVs in the MUVAA relay; and 4) $\mathbb { I } _ { j }$ is the excitation current weights set of AAVs in the MUVAA jammer. Note that the optimization variables are specified in Table II.

# B. Problem Formulation

In the CB-based dual AAV cluster-assisted maritime secure communication system, we simultaneously reflect on the optimization objectives as follows.

Optimization Objective 1: To enhance the reliability of legitimate maritime communications, our first optimization objective is to maximize the obtainable SINR value of Bob, and it can be achieved by jointly optimizing the 3-D positions and excitation current weights of the AAVs in the MUVAA relay and MUVAA jammer. Thus, the first optimization objective can be given as follows:

$$
f _ {1} \big (\mathbb {P} _ {r}, \mathbb {I} _ {r}, \mathbb {P} _ {j}, \mathbb {I} _ {j} \big) = \gamma_ {\mathrm{Bob}}. \tag {11}
$$

Optimization Objective 2: To maintain the security of legitimate maritime communications, and reduce the risk of eavesdropping on data signals, the second optimization objective is to minimize the available SINR of Willie, which can be expressed as follows:

$$
f _ {2} \left(\mathbb {P} _ {r}, \mathbb {I} _ {r}, \mathbb {P} _ {j}, \mathbb {I} _ {j}\right) = \gamma_ {\text { Willie }}. \tag {12}
$$

Optimization Objective 3: In our designed system, both the MUVAA relay and MUVAA jammer need to move continuously in order to achieve the aforementioned two optimization objectives. Therefore, the third optimization objective is to minimize the total flight energy consumption of AAVs, which is expressed as follows:

$$
f _ {3} \left(\mathbb {P} _ {r}, \mathbb {P} _ {j}\right) = \sum_ {m = 1} ^ {N _ {U r}} E _ {m} + \sum_ {n = 1} ^ {N _ {U j}} E _ {n} \tag {13}
$$

where $E _ { m }$ and $E _ { n }$ represent the flight energy consumption of the mth AAV in the MUVAA relay and the nth AAV in the MUVAA jammer, respectively.

Note that the three optimization objectives depend on the same decision variables, which means that optimizing one objective can affect others. Moreover, in the process of using AAVs to implement maritime secure communications, the AAVs in the MUVAA relay and MUVAA jammer need to adjust their positions to optimize data transmission rates and regulate the effect of jamming signals. However, the process of constant movements of the AAVs also causes additional energy consumption, which conflicts with our objective of minimizing the total flight energy consumption of AAVs. In addition, according to (9), higher AAV speeds increase energy consumption, while slower speeds result in longer hovering durations and increased energy consumption. Therefore, the considered optimization objectives are in conflict with each other and need to be balanced. As such, multiobjective optimization allows for specific tradeoffs based on different scenarios, providing flexibility in decision-making.

According to the aforementioned three optimization objectives, the SEMCMOP can be formulated as follows:

$$
\min _ {\left\{\mathbb {P} _ {r}, \mathbb {I} _ {r}, \mathbb {P} _ {j}, \mathbb {I} _ {j} \right\}} F = \{- f _ {1}, f _ {2}, f _ {3} \}, \tag {14a}
$$

$$
\text { s.t. } \quad 0 \leq I _ {m} ^ {U r} \leq 1, \forall m \in \mathcal {U} _ {R}, \tag {14b}
$$

$$
0 \leq I _ {n} ^ {U j} \leq 1, \forall n \in \mathcal {U} _ {J}, \tag {14c}
$$

$$
\mathcal {P} _ {m} ^ {U r} \in A _ {s r}, \forall m \in \mathcal {U} _ {R}, \tag {14d}
$$

$$
\mathcal {P} _ {n} ^ {U j} \in A _ {s j}, \forall n \in \mathcal {U} _ {J}, \tag {14e}
$$

$$
D R _ {m _ {1}, m _ {2}} \geq D _ {\min}, \forall m _ {1}, m _ {2} \in \mathcal {U} _ {R}, \tag {14f}
$$

$$
D J _ {n _ {1}, n _ {2}} \geq D _ {\min}, \forall n _ {1}, n _ {2} \in \mathcal {U} _ {J} \tag {14g}
$$

where $I _ { m } ^ { U r } , ~ I _ { n } ^ { U j } , ~ \mathcal { P } _ { m } ^ { U r }$ , and $\mathcal { P } _ { n } ^ { U j }$ are the variables associated with AAVs in the relay and jamming sets, respectively, which are displayed in Table II. Moreover, $A _ { s r }$ and $A _ { s j }$ are the 3- D coordinates of flight range areas of AAVs in the relay set and jammer set, respectively. In addition, $D R _ { m _ { 1 } , m _ { 2 } }$ denotes the distance between the $m _ { 1 }$ th AAV and m th AAV in the relay set, $D J _ { n _ { 1 } , n _ { 2 } }$ denotes the distance between the $n _ { 1 }$ th AAV and $n _ { 2 } 1$ h AAV in the jammer set, and $D _ { \mathrm { m i n } }$ is the minimum distance between two neighboring AAVs to avoid collision.

# C. Problem Analysis

Next, we analyze the formulated SEMCMOP.

1) The Formulated SEMCMOP is NP-Hard: The $f _ { 3 }$ is shown in (13), the minimization of $f _ { 3 }$ is a continuous optimization problem. For facilitating the analysis, we transform the continuous problem into a discrete problem, such as the solutions of the x-coordinate of AAVs in the MUVAA relay $( X _ { m } ^ { U r } )$ , are chosen from a set with finite factors. Next, we will verify that the transformed problem is a combinatorial optimization problem. The goal of a combinatorial optimization problem is to identify the optimal subset from a finite universal set that meets specific criteria to achieve the best solutions, and it can be described using three parameters $( F , G ,$ and $D )$ . During the minimization of $f _ { 3 } ,$ where F is the cost function (13), G represents the feasible solution region and is a set of constraint functions (14d)–(14g), D is the domain of solutions. The transformed version of $f _ { 3 }$ can be regarded as a combinatorial optimization problem which is NPhard [53]. Therefore, the transformed $f _ { 3 }$ is NP-hard, and the initial $f _ { 3 }$ is NP-hard. In addition, the optimization problems related to SINR model $( f _ { 1 }$ and $f _ { 2 } )$ are usually NP-hard [54]. Due to $f _ { 1 } , f _ { 2 } ,$ , and $f _ { 3 }$ are NP-hard, the originally formulated SEMCMOP is NP-hard. In this case, our current task is to develop an effective algorithm to solve this problem.

2) The SEMCMOP is a Large-Scale Optimization Problem: The solution space of the formulated SEMCMOP consists of the 3-D positions and excitation current weights of AAVs in the MUVAA relay $( \mathbb { X } _ { r } , \mathbb { Y } _ { r } , \mathbb { Z } _ { r } , \mathbb { I } _ { r } )$ and MUVAA jammer $( \mathbb { X } _ { r } , \mathbb { Y } _ { r } , \mathbb { Z } _ { r } , \mathbb { I } _ { r } )$ . Thus, the solution dimensions to be processed are $( 4 \times N _ { U R } + 4 \times N _ { U J } )$ . As the number of AAVs increases, the solution space of the SEMCMOP expands accordingly. Therefore, the formulated SEMCMOP is a large-scale optimization problem.

Since the formulated SEMCMOP is NP-hard and its complexity increases significantly as the network size increases, it is difficult to find a deterministic algorithm to solve it efficiently. Moreover, due to the SEMCMOP involving a large number of decision variables, and complex constraints and tradeoffs among the objectives, weighted sum methods have challenges in facing objective weight setting. In addition, DRL may face convergence difficulties and resource-wasting issues, and it is better suited to address the challenges posed by the dynamic movement of vessels in real-world scenarios [55]. In contrast, the multiobjective swarm intelligence optimization algorithms can utilize Pareto dominance to find a set of nearoptimal solutions in a short period and choose a suitable final solution from the set according to the requirements of the scenario. Therefore, considering the complexity of SEMCMOP and the limitations of AAV hardware conditions, we propose a novel swarm intelligence optimization algorithm to control the decision variables of SEMCMOP. Additionally, the proposed algorithm runs on Raspberry Pi, which is located on the AAV as an edge computing node, processes the data locally, and uploads the crucial results. It improves the efficiency of data processing and eases the burden on the AAV, thus optimizing the overall resources.

# V. PROPOSED ALGORITHM

In this section, we first introduce the outline of the conventional multiobjective mayfly algorithm (MOMA). Then, the IMOMA is proposed to handle the formulated SEMCMOP.

# A. Outline the Conventional MOMA

First, we describe the advantages of MOMA in dealing with formulated SEMCMOP. Then, we give the overall process of MOMA.

1) Advantages of MOMA: Swarm intelligence optimization algorithms have advantages, such as parallel search capability and flexible adjustment of solutions, which makes them show efficient performance in dealing with complex MOP [56]. The MOMA is a newly proposed swarm intelligence optimization algorithm and it can find the optimal solutions by simulating the evolution of mayflies and has been applied in practical engineering problems [57]. In detail, MOMA has the following advantages. First, male mayflies initially congregate and perform synchronized flights over water to attract females. In response, female mayflies approach the swarm for mating. This process is more effective in balancing exploration and exploitation [58]. Then, after mating, the female mayflies produce offspring, of which only the healthier ones can survive after hatching. If the offspring demonstrates superior fitness, it will displace the weaker parent in the population. This process maintains population diversity and avoids over convergence of the population to the local optimum. More importantly, MOMA is relatively simple and has low-computational complexity, and its core mechanisms (mating, displacement) can be executed with smaller computational resources, which is advantageous for large-scale optimization problems [59]. Therefore, the above features of MOMA make it an ideal choice for handling with the formulated SEMCMOP.

2) MOMA Process: The cycling mechanism of MOMA makes it pass on stronger traits to offspring and improve the overall fitness of the population [59]. In this case, the movement of the mayfly can be defined by

$$
X _ {i} ^ {t + 1} = X _ {i} ^ {t} + v _ {i} ^ {t + 1} \tag {15}
$$

where Xt and Xt+1 $X _ { i } ^ { t }$ $X _ { i } ^ { t + 1 }$ are the current ith position of mayfly in the search space at time step t and $t + 1 , \ \nu _ { i } ^ { t + 1 }$ is the velocity of mayfly for changing its position. Moreover, the increasing velocity of male mayfly, female mayfly and offspring is computed differently, which depends on the current different personal best position, global best position, attraction constants, and other corresponding parameters.

The position of each mayfly (Xi) in the search space denotes a prospective solution to the optimization problem. Fig. 2 shows the outline of MOMA, and the details are described as follows.

1) Population Initialization: Generate the initial population $( X _ { N } )$ of male and female mayflies at random containing potential solutions to the optimization problem, where N is the population size.

![](images/83e28fed4b94fdbd3477cbdecc527fa32dc001082f7b461ad8f504fe8cd9a423.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Step 1: Population Initialization"] --> B["Step 2: Objective Calculation"]
    B --> C["Step 3: Comparison and Evaluation"]
    C --> D["Step 4: Solution Update"]
    D --> E["Step 5: Termination?"]
    E --> F{No}
    F -->|Yes| G["The values in the Archive is final solutions. Archive"]
    G --> H["Final Solutions"]
    
    subgraph Step 1
        I["Generate the initial mayfly population. X₁, Xₙ"] --> J["A solution of the problem"]
        J --> K["Initial Population"]
    end
    
    subgraph Step 2
        L["Calculate the optimization values by population. f₁, f₂, f₃, f₄"] --> M["Objective Values"]
    end
    
    subgraph Step 3
        N["Comparison to get the Pareto optimal solutions. Storage in the archive. X₁, X₂, X₃, ..., Xₙ"] --> O["Current Population"]
        P["Pareto Solutions"] --> Q["Storage"]
        Q --> R["Archive"]
    end
    
    subgraph Step 4
        S["Update mayfly and female mayfly. Post-mating superior offspring replaces the parent. Replacement"] --> T["Replacement"]
        U["Current Population"] --> V["New Population"]
    end
    
    subgraph Step 5
        W["End"]
    end
```
</details>

Fig. 2. Evolutionary outline based on the MOMA.

2) Objective Calculation: Calculate the values of the optimization objectives by using the candidate solutions according to (11)–(13).   
3) Comparison and Evaluation: Compare solutions with optimization objective values by Pareto sorting, and obtain the nondominated Pareto solutions. Then, store them to the archive.   
4) Solution Update: Update the mayfly by (15) according to the corresponding principle. The male and female mayflies move and mate, and the post-mating superior offspring replaces the poor parent. In turn, the new population replaces the current population.   
5) Termination or Loop: Determine if the termination condition is reached. If it is reached, the solutions in the archive are the final solutions; if not, return to 2) for a loop.

# B. IMOMA

Since the formulated SEMCMOP has been proven to be an NP-hard and large-scale optimization problem, with optimization objectives need to be balanced, the conventional MOMA may encounter the following challenges in dealing with the problem.

1) Poor Initial Solutions: The conventional MOMA generates random initial solutions, which can reduce the diversity of solutions and restrict the search directions. In addition, due to the solution space of the SEMCMOP shown in (14) is more extensive, poorquality initial solutions are more prone to falling into local optima [60]. Therefore, enhancing the quality of initial solutions is critical.   
2) Nonuniform Search Space: The solutions can be continuously updated by the conventional MOMA. However,

the values of the optimization objectives are jointly determined by two solution sets Xr and Xj, which have different sizes. Moreover, the upper and lower boundaries of each set of solutions are different, which indicates that different dimensions of the algorithm are assigned distinct values. Note that the elements can impact optimal performance, and search strategy may be biased toward certain dimensions, resulting in other dimensions being ignored, which in turn produces the nonuniform solution space and affects overall optimization performance [61]. Therefore, different solution spaces (Xr and Xj) and different dimensions of the solutions need to be cautiously considered about developing corresponding update strategies.

Therefore, we propose the IMOMA which is the improved version of the conventional MOMA.structure of IMOMA is illustrated in Algorithm 1, and corresponding improvement points are as follows.

1) Chaotic Solution Initialization: The chaotic search is a random movement method, which transforms the parameters from the solution space to the chaotic domain to achieve an optimal distribution of initial solutions. The Tent map is utilized to optimize the initial solutions and it is expressed by [62]

$$
z _ {i + 1} = \left\{ \begin{array}{l l} z _ {i} / a, & 0 \leq z _ {i} \leq a, \\ (1 - z _ {i}) / (1 - a), & a <   z _ {i} \leq 1 \end{array} \right. \tag {16}
$$

where zi denotes the ith value of the Tent chaotic map and a ∈ [0, 1] denotes the parameter of mapping. Thus, according to the Tent map, the initial solution is calculated by

$$
X r _ {i} = l b _ {r} + z _ {i} \times (u b _ {r} - l b _ {r}) \tag {17}
$$

$$
X j _ {i} = l b _ {j} + z _ {i} \times (u b _ {j} - l b _ {j}) \tag {18}
$$

where $X r _ { i }$ and $X j _ { i }$ are the ith initial solutions of the relay set and jammer set, which are combined to represent the ith

Algorithm 1: IMOMA   
Input: Population size N, maximum iteration $t_{max}$ , archive set Ar; #Ar for storing the Pareto solutions.

1 Set the corresponding parameters;

2 for i = 1 to N do

3 Initialize the ith solution of the relay set ( $Xr_i$ ) by Eq. (17);

4 Initialize the ith solution of the jammer set ( $Xj_i$ ) by Eq. (18);

5 end

6 for t = 1 to $t_{max}$ do

7 Compute the optimization objective values and update Ar based on non-dominated solutions;

8 for i = 1 to N do

9 Calculate the $Xr_i$ and $Xj_i$ of the ith mayfly relay set and jammer set (Note that $Xr_i$ and $Xj_i$ are integrated as $X_i$ ) by Eq. (15);

10 Compute $\zeta$ by Eq. (28); #Threshold $\zeta$ for updating the relay and jamming sets.

11 Generate some random numbers ( $r_1$ , $r_3$ and $r_4$ ) between 0 and 1;

12 Update the $Xj_i$ by using Algorithm 2;

13 Update the $Xr_i$ by using Algorithm 3;

14 end

15 end

Output: Updated Ar.

solution (Xi) of the optimization objectives. In addition, $u b _ { r }$ and $l b _ { r }$ are the upper and lower bounds of the relay set, respectively, and ubj and $l b _ { j }$ are the upper and lower bounds of the jammer set, respectively.

2) Hybrid Solution Update Strategies: In this work, inspired by the whale optimization algorithm (WOA), which offers the benefits of simplicity in implementation and high flexibility [63], we introduce a WOA-based solution update strategy to update the positions of AAVs in the jammer set (Xj). Then, the arithmetic optimization algorithm (AOA) has the characteristics of fast running speed, low-computational complexity and fewer parameters [64], which makes it more suitable for optimizing a larger number of AAVs in the relay set. Therefore, we present an AOA-based solution update strategy to update the positions of AAVs in the MUVAA relay (Xr). Note that the WOA-based solution update strategy and AOA-based solution update strategy are integrated as the hybrid solution update strategies, which can further balance the exploration and exploitation abilities of the IMOMA. Moreover, for different boundary values in different dimensions, we adopt corresponding update strategies and footsteps. The decision variables in this article can be updated as follows.

First, an antenna array can obtain higher gain and avoid mutual coupling when the elements are at appropriate distances in terms of the theories of electromagnetism and CB. Moreover, the AAVs in the MUVAA consume less energy when they are closely distributed in the process of communication [7]. Therefore, a better enhancement to the algorithm is to centralize the horizontal positions of AAVs. In this work, we update the horizontal positions of AAVs in the MUVAA jammer $( \mathbb { X } _ { j } , \ \mathbb { Y } _ { j } )$ by using the proposed WOA-based solution update strategy, where whales move either through a shrinking encircling mechanism or a spiral path, with 50% probability of choosing each [63]. The update process is expressed by

$$
\begin{array}{l} X j _ {i} ^ {\left(\mathbb {X} _ {j}, \mathbb {Y} _ {j}\right)} = \\ \left\{ \begin{array}{l} X j _ {i} ^ {\left(\mathbb {X} _ {j}, \mathbb {Y} _ {j}\right)} + C j _ {i} - l \mid 2 r _ {2} \cdot C j _ {i} - X j _ {i} ^ {\left(\mathbb {X} _ {j}, \mathbb {Y} _ {j}\right)} |, p <   0. 5, \\ X j _ {i} ^ {\left(\mathbb {X} _ {j}, \mathbb {Y} _ {j}\right)} + \mid C j _ {i} - X j _ {i} ^ {\left(\mathbb {X} _ {j}, \mathbb {Y} _ {j}\right)} \mid H + C j _ {i}, \quad p \geq 0. 5 \end{array} \right. \end{array} \tag {19}
$$

where $X j _ { i } ^ { ( \mathbb { X } _ { j } , \mathbb { Y } _ { j } ) }$ denotes the ith solution of the jammer set in the horizontal direction and $C j _ { i } = ( \mathbb { E } ( \mathbb { X } _ { j } ) , \mathbb { E } ( \mathbb { Y } _ { j } ) )$ . Moreover, l and H are the related parameters [63], and $r _ { 2 }$ and p are random numbers between 0 and 1. Likewise, inspired by AOA, we utilize a stochastic scaling coefficient to explore diverse regions of the search space and generate more diversification results for the case of more elements. The horizontal positions of AAVs in the MUVAA relay $( \mathbb { X } _ { r } , \ \mathbb { Y } _ { r } )$ can be updated by using the AOA-based solution update strategy, which is as follows:

$$
\begin{array}{l} X r _ {i} ^ {\left(\mathbb {X} _ {r}, \mathbb {Y} _ {r}\right)} = \\ \left\{ \begin{array}{l} C r _ {i} / \left(M ^ {\prime} \times \left(\left(u b _ {r} - l b _ {r}\right) \times \mu + l b _ {r}\right)\right), r _ {3} <   0. 5 \\ C r _ {i} \times M \times \left(\left(u b _ {r} - l b _ {r}\right) \times \mu + l b _ {r}\right), r _ {3} \geq 0. 5 \end{array} \right. \end{array} \tag {20}
$$

where $X r _ { i } ^ { ( \mathbb { X } _ { r } , \mathbb { Y } _ { r } ) }$ denotes the ith solution of the relay set in the horizontal direction, and $C r _ { i } = ( \mathbb { E } ( \mathbb { X } _ { r } ) , \mathbb { E } ( \mathbb { Y } _ { r } ) )$ . Moreover, M and $M ^ { \prime }$ denote the coefficients of the $\mathrm { \ A O A } , \mu$ denotes the control parameter to tune the search procedure, and $r _ { 3 }$ is the random number between 0 and 1. In the AOA, the subtraction and addition as exploitation operators explore the search area deeply on several dense regions to find a better solution. The updating process for the exploitation phase by the AOA-based solution update strategy can be expressed as follows:

$$
\begin{array}{l} X r _ {i} ^ {\left(\mathbb {X} _ {r}, \mathbb {Y} _ {r}\right)} = \\ \left\{ \begin{array}{l} C r _ {i} - M \times \left(\left(u b _ {r} - l b _ {r}\right) \times \mu + l b _ {r}\right), r _ {4} <   0. 5 \\ C r _ {i} + M \times \left(\left(u b _ {r} - l b _ {r}\right) \times \mu + l b _ {r}\right), r _ {4} \geq 0. 5 \end{array} \right. \end{array} \tag {21}
$$

where $r _ { 4 }$ is the random number between 0 and 1.

Second, as vertical flight costs more energy than horizontal flight, the crucial elements in the third optimization objective are the vertical positions of AAVs in the MUVAA relay $( \mathbb { Z } _ { r } )$ and MUVAA jammer $( \mathbb { Z } _ { j } )$ , which means that the vertical positions of AAVs require being updated more cautiously. Thus, an elite solution of the jammer set $( j )$ is chosen from the archive by the roulette wheel selection, and it indicates the fittest AAV in the current optimization to guide the updates of all AAVs. We select $j ^ { ( \mathbb { Z } _ { j } ) }$ to update the solutions of the $z -$ axis in the MUVAA jammer by using the WOA-based method, which is as follows:

$$
\begin{array}{l} X j _ {i} ^ {\left(\mathbb {Z} _ {j}\right)} = \\ \left\{ \begin{array}{l l} X j _ {i} ^ {\left(\mathbb {Z} _ {j}\right)} + j ^ {\left(\mathbb {Z} _ {j}\right)} - l \left| 2 r _ {2} \cdot j ^ {\left(\mathbb {Z} _ {j}\right)} - X j _ {i} ^ {\left(\mathbb {Z} _ {j}\right)} \right|, & p <   0. 5, \\ X j _ {i} ^ {\left(\mathbb {Z} _ {j}\right)} + \left| j ^ {\left(\mathbb {Z} _ {j}\right)} - X j _ {i} ^ {\left(\mathbb {Z} _ {j}\right)} \right| H + j ^ {\left(\mathbb {Z} _ {j}\right)}, & p \geq 0. 5 \end{array} \right. \end{array} \tag {22}
$$

where Xj(i $X j _ { i } ^ { ( \mathbb { Z } _ { j } ) }$ denotes the ith solution of the jammer set in the vertical direction. Likewise, an elite solution of the relay set (r) can be chosen from the archive, where $r ^ { ( \mathbb { Z } _ { r } ) }$ is used to update the z-axis values in the MUVAA relay by the AOAbased solution update method, which is as follows:

$$
X r _ {i} ^ {(\mathbb {Z} _ {r})} =
$$

$$
\left\{ \begin{array}{l} r ^ {(\mathbb {Z} _ {r})} / \left(M ^ {\prime} \times ((u b _ {r} - l b _ {r}) \times \mu + l b _ {r})\right), r _ {3} <   0. 5 \\ r ^ {(\mathbb {Z} _ {r})} \times M \times ((u b _ {r} - l b _ {r}) \times \mu + l b _ {r}), r _ {3} \geq 0. 5 \end{array} \right. \tag {23}
$$

$$
X r _ {i} ^ {(\mathbb {Z} _ {r})} =
$$

$$
\left\{ \begin{array}{l} r ^ {(\mathbb {Z} _ {r})} - M \times ((u b _ {r} - l b _ {r}) \times \mu + l b _ {r}), r _ {4} <   0. 5 \\ r ^ {(\mathbb {Z} _ {r})} + M \times ((u b _ {r} - l b _ {r}) \times \mu + l b _ {r}), r _ {4} \geq 0. 5 \end{array} \right. \tag {24}
$$

where Xr(Zr)i $X r _ { i } ^ { ( \mathbb { Z } _ { r } ) }$ Yi denotes the ith solution of the relay set in the vertical direction after the update.

Finally, proper excitation current weights in the MUVAA relay $( \mathbb { I } _ { r } )$ can efficiently adjust the beam pattern when the AAVs in the MUVAA relay communicate with the legitimate vessel. Moreover, proper excitation current weights in the MUVAA jammer $( \mathbb { I } _ { j } )$ can assist AAVs in delivering stronger jamming signals to the eavesdropper, thus enhancing communication rates and improving security performance. Therefore, we choose the elite solution of the jammer set $j ^ { ( \mathbb { X } _ { j } , \mathbb { Y } _ { j } , \mathbb { Z } _ { j } ) }$ to substitute the previous corresponding solutions $X j _ { i } ^ { ( \mathbb { X } _ { j } , \mathbb { Y } _ { j } , \mathbb { Z } _ { j } ) }$ , and use $j ^ { ( \mathbb { I } _ { j } ) }$ to iterate over $X j _ { i } ^ { ( \mathbb { I } _ { j } ) }$ . The ith solution in the MUVAA jammer $X j _ { i } ^ { ( \mathbb { I } _ { j } ) }$ by using the WOA-based method can be updated as follows:

$$
X j _ {i} ^ {(\mathbb {I} _ {j})} =
$$

$$
\left\{ \begin{array}{l} X j _ {i} ^ {\left(\mathbb {I} _ {j}\right)} + j ^ {\left(\mathbb {I} _ {j}\right)} - l \left| 2 r _ {2} \cdot j ^ {\left(\mathbb {I} _ {j}\right)} - j ^ {\left(\mathbb {I} _ {j}\right)} \right|, p <   0. 5 \\ X j _ {i} ^ {\left(\mathbb {I} _ {j}\right)} + \left| j ^ {\left(\mathbb {I} _ {j}\right)} - X j _ {i} ^ {\left(\mathbb {I} _ {j}\right)} \right| H + j ^ {\left(\mathbb {I} _ {j}\right)}, \quad p \geq 0. 5. \end{array} \right. \tag {25}
$$

Moreover, the elite solution of the relay set $r ^ { ( \mathbb { X } _ { r } , \mathbb { Y } _ { r } , \mathbb { Z } _ { r } ) }$ can be $X r _ { i } ^ { ( \mathbb { X } _ { r } , \mathbb { Y } _ { r } , \mathbb { Z } _ { r } ) }$ o substitute the previous corresponding. The ith solution in the MUVAA relay $X r _ { i } ^ { ( \mathbb { I } _ { r } ) }$ tionscan be iterated with $r ^ { ( \mathbb { I } _ { r } ) }$ by using the AOA-based method as follows:

$$
X r _ {i} ^ {(\mathbb {I} _ {r})} =
$$

$$
\left\{ \begin{array}{l} r ^ {(\mathbb {I} _ {r})} / \left(M ^ {\prime} \times ((u b _ {r} - l b _ {r}) \times \mu + l b _ {r})\right), r _ {3} <   0. 5 \\ r ^ {(\mathbb {I} _ {r})} \times M \times ((u b _ {r} - l b _ {r}) \times \mu + l b _ {r}), r _ {3} \geq 0. 5 \end{array} \right. \tag {26}
$$

$$
X r _ {i} ^ {(\mathbb {I} _ {r})} =
$$

$$
\left\{ \begin{array}{l} r ^ {(\mathbb {I} _ {r})} - M \times ((u b _ {r} - l b _ {r}) \times \mu + l b _ {r}), r _ {4} <   0. 5 \\ r ^ {(\mathbb {I} _ {r})} + M \times ((u b _ {r} - l b _ {r}) \times \mu + l b _ {r}), r _ {4} \geq 0. 5. \end{array} \right. \tag {27}
$$

Accordingly, the IMOMA is shown in Algorithm 1, in which the marker ζ is a threshold used for regulating and it is calculated by [61]

$$
\zeta = \left\{ \begin{array}{l} 0. 5 - \frac {t}{t _ {\max}}, t <   \frac {t _ {\max}}{2} \\ \frac {t}{t _ {\max}} - 0. 5, \text { otherwise. } \end{array} \right. \tag {28}
$$

Moreover, the AOA-based solution update algorithm of the relay set is shown in Algorithm 3. The math optimizer accelerated (MOA) function can be used to select the search phase (i.e., exploration or exploitation), which is calculated by [59]

$$
\mathrm{MOA} (t) = \mathrm{Min} + t \times \left(\frac {\mathrm{Max} - \mathrm{Min}}{t _ {\max}}\right) \tag {29}
$$

Algorithm 2: WOA-Based Solution Update Algorithm of the Jammer Set   
Input: Current jammer set $Xj_{i}$ , current elite solution of jammer set j; # Elite solution is the current most appropriate solution.

1 Update the value of $Xj_{i}^{(\mathbb{Z}_{j})}$ by Eq. (22);

2 if $t < t_{max}/2$ then

3 if $r_{1} < \zeta$ then

4 Update the value of $Xj_{i}^{(\mathbb{X}_{j},\mathbb{Y}_{j})}$ by Eq. (19);

5 end

6 else

7 if $r_{1} < \zeta$ then

8 Substitute $Xj_{i}^{(\mathbb{X}_{j},\mathbb{Y}_{j},\mathbb{Z}_{j})}$ with the value of $j^{(\mathbb{X}_{j},\mathbb{Y}_{j},\mathbb{Z}_{j})}$ ;

9 Update the value of $Xj_{i}^{(\mathbb{I}_{j})}$ by Eq. (25);

10 end

11 end

Output: Updated jammer set $X j _ { i } ^ { ( \mathbb { X } _ { j } , \mathbb { Y } _ { j } , \mathbb { Z } _ { j } , \mathbb { I } _ { j } ) } ;$

where MOA(t) denotes the function value at the tth iteration. Moreover, t is the current iteration, ranging from 1 to $t _ { \mathrm { m a x } }$ . In addition, Min and Max denote the minimum and maximum values of the accelerated function, respectively.

# C. Complexity of the IMOMA

The computational complexity of the proposed algorithm mainly depends on the computations of the optimization objectives and sorting the solutions in each optimization objective. We denote the number of optimization objectives, population size, and archive size as $N _ { o b j }$ , N, and $N _ { a } ,$ , respectively. Specifically, the optimization objective computation has $\mathcal { O } ( N _ { o b j } \cdot N )$ computational complexity. Moreover, for sorting the solutions in each objective, the computational complexity of classifying the $N _ { a }$ solutions in the Pareto archive is $\mathcal { O } ( N _ { o b j } .$ $N _ { a }$ ·log $N _ { a } )$ . In this article, we set $N _ { a }$ to the same size as N, then the computational complexity for the nondominated sorting is $\mathcal { O } ( N _ { o b j } \cdot N ^ { 2 } )$ , and the overall complexity of the proposed IMOMA is $\mathcal { O } ( N _ { o b j } \cdot N ^ { 2 } )$ .

# VI. SIMULATION RESULTS AND ANALYSIS

In this section, the performance of the proposed improved algorithm is evaluated by the simulations.

# A. Simulation Setups

1) Parameter Settings: The simulation experiments are conducted using MATLAB 9.2. The 3-D positions (in meters) of Bob and Willie, which are set to (2400, 2300, 5) and (2000, 2000, 5), respectively, and the sea level is set as 5 m. The distribution area of the AAV relay set $( A _ { s r } )$ and AAV jammer set $( A _ { s j } )$ are located within a 100 m × 100 m area to form the MUVAA relay and MUVAA jammer. We randomly initialize the hovering positions of the AAVs from their feasible flight area since they may have been working on other tasks before. Moreover, we consider a larger scale network, including 16 and 8 AAVs in the relay set and jammer set, and a smaller scale network with 8 and 4 AAVs in the relay set and jammer set. In addition, the remaining key parameters used in the simulations are shown in Table IV [50], [65].

Algorithm 3: AOA-Based Solution Update Algorithm of the Relay Set   
1 Compute the value of MOA by Eq. (29);
Input: Current relay set $Xr_{i}$ , current elite solution of relay set r;
2 if $r_{1} > MOA$ then
3 Exploration phase: Determine applying multiplication or division operator, update $Xr_{i}^{(\mathbb{Z}_{r})}$ by Eq. (23);
4 else
5 Exploitation phase: Determine applying addition or subtraction operator, update $Xr_{i}^{(\mathbb{Z}_{r})}$ by Eq. (24);
6 end
7 if $t < t_{max}/2$ then
8 if $r_{1} < \zeta$ then
9 if $r_{1} > MOA$ then
10 Update $Xr_{i}^{(\mathbb{X}_{r},\mathbb{Y}_{r})}$ by Eq. (20); #Exploration phase.
11 else
12 Update $Xr_{i}^{(\mathbb{X}_{r},\mathbb{Y}_{r})}$ by Eq. (21); #Exploration phase.
13 end
14 end
15 else
16 if $r_{1} < \zeta$ then
17 Substitute $Xr_{i}^{(\mathbb{X}_{r},\mathbb{Y}_{r},\mathbb{Z}_{r})}$ with $r^{(\mathbb{X}_{r},\mathbb{Y}_{r},\mathbb{Z}_{r})}$ ;
18 if $r_{1} > MOA$ then
19 Update $Xr_{i}^{(\mathbb{I}_{r})}$ by Eq. (26); #Exploration phase.
20 else
21 Update $Xr_{i}^{(\mathbb{I}_{r})}$ by Eq. (27); #Exploration phase.
22 end
23 end
24 end
Output: Updated relay set $Xr_{i}^{(\mathbb{X}_{r},\mathbb{Y}_{r},\mathbb{Z}_{r},\mathbb{I}_{r})}$ ;

2) Baselines: To demonstrate the effectiveness of the proposed IMOMA, three comparison approaches and various comparison algorithms are introduced as follows.   
1) Non-CB Approach: This approach does not use CB to achieve signal transmission. Specifically, a AAV, denoted as AAV-R, acts as a relay to forward data signals from the LBS to Bob by the data link, the other AAV, denoted as AAV-J, moves from its hovering position toward Willie and sends jamming signals by the jamming link at a suitable location. As such, the comparison approach can highlight the effect of CB in long-distance signal transmission.   
2) Single CB Approach: This approach only utilizes CB to send data signals from the MUVAA relay to Bob, and AAV-J sends jamming signals to Willie. In this case, the comparison between this approach and the proposed

![](images/d7e7412dec9221c76ad18c1fd9d2a4258f518cba65073b92e9af8605ac22f862.jpg)

<details>
<summary>line</summary>

| φ    | Gain |
| ---- | ---- |
| -200 | 15   |
</details>

(a)

![](images/f221c79dcae6e3fd32c61eef9d429c9050b829a2534d26c97c43ee6476d776da.jpg)

<details>
<summary>line</summary>

| φ    | Gain |
| ---- | ---- |
| -200 | 10   |
</details>

(b)   
Fig. 3. Gain distributions optimized by the IMOMA in larger scale network. (a) Gain distributions of the MUVAA relay. (b) Gain distributions of the MUVAA jammer.

method can illustrate the effectiveness of CB in longdistance data signal transmission and the necessity of establishing an MUVAA jammer.

3) Multihop Approach: The approach employs AAV multihop to achieve data and jamming signal transmission, which is used to extend communication range. As such, the comparison between this approach and the proposed method further highlights the effectiveness of CB in long-distance transmission and its capability for efficient energy savings.   
4) State-of-the-Art Swarm Intelligence Algorithms: We select conventional MOMA, multiobjective dragonfly algorithm (MODA) [66], multiobjective multiverse optimization (MOMVO) [67], and multiobjective ant lion optimizer (MALO) [68] as benchmark swarm intelligence algorithms for comparison. These algorithms are known for their excellent diversity and exploration capabilities in solving MOP, and their efficiency has been well-validated by existing studies [39], [61]. Specifically, MODA simulates the social behavior of dragonflies to preserve diversity, MOMVO extends the search space based on the parallel universe theory, and MALO strikes a balance between exploration and exploitation by mimicking the predatory behavior of ant lions. The rich variety of mechanisms provides a robust set of benchmarks that highlights the effectiveness of the proposed algorithm in addressing the formulated problem. The maximum number of iterations and population size in these aforementioned algorithms are set as 500 and 30, respectively.

Furthermore, we provide the comparison results of different baselines and the CB-based approach.

# B. Simulation Results

1) Visualization Results: This part presents the visualization results of the larger scale network.

Fig. 3 shows the distribution of antenna gains optimized by the proposed IMOMA. Specifically, Fig. 3(a) shows the antenna gains from the MUVAA relay in all directions. As can be seen, the gain toward Bob is the highest among all directions, which makes Bob receives the maximum strength of data signals. Fig. 3(b) shows the antenna gain from the MUVAA jammer in all directions. It can be seen that Willie receives the maximum strength of jamming signals. Thus, the legitimate vessel Bob can achieve more secure and reliable maritime communication performance. Moreover, Fig. 4 illustrates the movement paths of AAVs in the MUVAA relay and MUVAA jammer from the initial hovering positions to the optimized positions, which are obtained by the proposed IMOMA. As can be seen, in the MUVAA relay and jammer, the optimized AAV positions are more centralized and compact than the original positions, which results in stronger transmitted signals and optimal SINR values compared to less centralized positions of AAVs. This more focused placement facilitates better implementation of CB, thus achieving more energy-efficient maritime wireless communications.

![](images/1ccc6b4751f37e98878f258309b4eaddb7a428e31235b6de782591cfb9025b0b.jpg)

<details>
<summary>scatter</summary>

| x     | y     | z-axis (m) |
|-------|-------|------------|
| 2000  | 2000  | 4400       |
| 2500  | 2500  | 4350       |
| 3000  | 3000  | 4300       |
| 3500  | 3500  | 4250       |
| 4000  | 4000  | 4200       |
| 4500  | 4500  | 4150       |
</details>

(a)

![](images/68f79384483b51a220d5e357f463f72029f1e4379a089218eda25318045d31c1.jpg)  
(b)

Fig. 4. Movement paths optimized by the IMOMA in larger scale network. (a) Movement paths of AAVs in the MUVAA relay. (b) Movement paths of AAVs in the MUVAA jammer.   
![](images/20042b11115d24534fb80b9c864e5b4a1a35f0f3a2689e73d7eaf4243084cc18.jpg)

<details>
<summary>bar</summary>

| Category | SINR of Bob | SINR of Willie |
| :--- | :--- | :--- |
| CB-based | 20.75 | -39.9 |
| Non-CB | -2.26 | -4.17 |
| Single CB | 10.18 | 8.31 |
</details>

Fig. 5. Values of SINR of Bob and Willie obtained by the approaches of CB-based, non-CB, and single CB.

2) Comparison With the Different Approaches: Fig. 5 shows the optimization objective values in terms of f1 and f2, which are obtained by the CB-based, non-CB, and single CB approaches. First, the satisfactory values SINR of Bob and Willie under the CB-based approach in larger scale network indicate that CB can achieve remote maritime transmission and effectively protect against eavesdropping. Second, the SINR of Bob of the non-CB approach is negative, which suggests that Bob cannot effectively receive information by the data link, and the non-CB approach can not achieve long-distance communications. Moreover, data signals are unlikely to be received by Willie next to Bob. Finally, according to the single CB approach, Bob and Willie both can receive data signals, which demonstrates that data signals can be sent by CB, and the jamming signals of non-CB can not affect Willie and can not guarantee the safe transmission of data signals.

![](images/ffd1dc3a11bdcb458b054da3bd30d07a7ec57116c884978d5ea84c79ec63b674.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["UAV₁"] --> B["..."]
    C["UAV₂"] --> B
    D["UAV_UJ"] --> E["..."]
    F["Willie"] --> G["..."]
    H["Bob"] --> I["..."]
    J["LBS"] --> K["..."]
    L["Jamming Link"] -.-> M["..."]
    N["Data Link"] -.-> O["..."]
    P["UAV_UR"] -.-> Q["..."]
    R["UAV₂"] -.-> S["..."]
    T["UAV₁"] -.-> U["..."]
    V["Cloud Icon"] --> W["Waveform"]
    X["Cloud Icon"] --> Y["Waveform"]
    Z["Cloud Icon"] --> AA["Waveform"]
```
</details>

Fig. 6. AAV multihop maritime communication system.

TABLE V PERFORMANCE COMPARISON BETWEEN CB-BASED AND MULTIHOP METHODS 

<table><tr><td rowspan="2">Methods</td><td colspan="3">Smaller scale network</td><td colspan="3">Larger scale network</td></tr><tr><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$  (J)</td><td> $f_1$ </td><td> $f_2$ </td><td> $f_3$  (J)</td></tr><tr><td>Multi-hop</td><td>0</td><td>0</td><td> $4.1\times 10^5$ </td><td>0</td><td>0</td><td> $5.2\times 10^6$ </td></tr><tr><td>CB-based</td><td>15.5</td><td>-27.9</td><td> $6.6\times 10^4$ </td><td>20.8</td><td>-39.9</td><td> $1.4\times 10^5$ </td></tr></table>

Furthermore, we use the AAV multihop method to compare with the CB-based approach. Fig. 6 shows the sketch of the AAV multihop communication system. Specifically, multiple AAVs are uniformly deployed between the initial area and the target location at the same altitude [69]. The free-space channel model is applied to represent airborne communications, and the results are shown in Table V. As can be seen, the SINR values of Bob and Willie obtained by the multihop method are 0, which is attributed to the longdistance transmission preventing the target user from receiving the signals. These comparison results further demonstrate the effectiveness of the CB approach. In summary, the results mentioned above indicate that the CB-based approach outperforms other approaches, achieving more efficient maritime secure communications. In addition, as shown in Fig. 3, the CB-based approach can maximize the antenna gain in the target direction, which further illustrates its reliability and efficiency.

![](images/4d146005e054542a5407424dc81950faff4a29b9f8f086dd67e49cbe69068ec3.jpg)  
(a)

![](images/19d51d02e860665ee7cae8b44b3fc787f10ebf3fd6c7bec1669f05092fa5c12a.jpg)  
Fig. 7. Solution distributions obtained by different algorithms in (a) larger and (b) smaller scale networks of CB-based approach.

In this article, the implementation of the key CB approach requires increasing the number of AAVs. In this case, the VAA formed by multiple AAVs is used to improve signal coverage and transmission reliability, whereas the process inevitably leads to more energy consumption. Note that this tradeoff is necessary to achieve more efficient maritime secure communications. In real-time communication requirements, communication effectiveness is the main concern, and the CB method can substantially improve the long-distance signal transmission quality and ensure security. Therefore, despite the rise in energy consumption, the CB approach is reasonable and in line with the realistic needs.

3) Comparison With Other Algorithms: Fig. 7 shows the Pareto solution distributions obtained by the different algorithms in larger and smaller scale networks of the CB-based approach. The coordinates of the points in the 3-D space represent the values derived from the three optimization objectives. It is obvious that the solutions obtained by the proposed IMOMA are more concentrated and they are closer to the PF both in larger and smaller scale networks. Therefore, the proposed IMOMA is more suitable for forming VAA and has greater superiority in solving the corresponding optimization problems.

Furthermore, Fig. 8 illustrates the optimization objective values, which are obtained by different algorithms in larger and smaller scale networks of the CB-based approach. As can be seen, the IMOMA achieves the optimal results on the first and second optimization objective values, which indicates that IMOMA can implement the effective communications of the legitimate vessel, and ensures security in the communication process. Notably, the enhancement of optimizing the SINR of Willie is more significant. Moreover, it is clear that the proposed IMOMA is optimal in minimizing the total flight energy consumption of AAVs compared to other algorithms. The abovementioned results further show that IMOMA has strong applicability and robustness during the VAA maritime secure communications. The reason may be that we use the chaotic approach to generate the initial values, which increases the probability that the initial solutions are located around the optimal positions. In addition, the considered hybrid solution update strategies utilize heuristic methods to guide the solution update directions, and it adopts different strategies to update the solutions in different dimensions, thus improving the performance of the proposed IMOMA.

![](images/e83f304d9a967f20855bc46343e8c5ef6259fb7fad1b783e713cc30c1b543d01.jpg)

<details>
<summary>bar</summary>

| Model | SINR of Bob | SINR of Willie | Energy consumption of UAVs (J) |
| :--- | :--- | :--- | :--- |
| MODA | 17.49 | -17.63 | 1.40200 |
| MALO | 18.63 | -15.17 | 1.43200 |
| MOMVO | 16.31 | -15.88 | 1.39600 |
| MOMA | 19.97 | -27.87 | 1.39700 |
| IMOMA | 20.75 | -39.91 | 1.38500 |
</details>

(a)

![](images/80a238557f4d1955c0255bef59adb8c0eccd9ce201d71f4174a0261faa788143.jpg)

<details>
<summary>bar</summary>

| Method | SINR of Bob | SINR of Willie | Energy consumption of UAVs (J) |
| :--- | :--- | :--- | :--- |
| MODA | 14.26 | -4.58 | 69230 |
| MALO | 14.52 | -3.63 | 70610 |
| MOMVO | 12.08 | -9.59 | 67020 |
| MOMA | 14.82 | -20.91 | 67730 |
| IMOMA | 15.46 | -27.91 | 66300 |
</details>

(b)   
Fig. 8. Optimization objective values obtained by different algorithms in (a) larger and (b) smaller scale networks of the CB-based approach.

In addition, Fig. 9 presents the optimization objective values obtained by different algorithms of non-CB and single CB approaches. In Fig. 9(a), IMOMA performs well in the three optimization objectives compared to other comparison algorithms, which further confirms the efficiency of IMOMA. In Fig. 9(b), IMOMA displays remarkable improvements in the SINR of Bob and energy consumption of AAVs, whereas its greater sensitivity to CB may cause Willie to receive more data signals, resulting in poor results about the SINR of Willie. In general, IMOMA demonstrates strong performance, achieving efficient and secure maritime communications.

4) Convergence of the IMOMA: Note that proving convergence is challenging due to the stochastic nature of the algorithm. Moreover, it is difficult to give a direct convergence curve for multiobjective optimization algorithms [70]. Thus, we use the solution distributions, inverted generational distance (IGD), and alternative average convergence rate (ACR) methods to assess the convergence of the IMOMA as follows.

1) Solution Distributions Method: We analyze the solution distributions with different iterations, as shown in Fig. 10(a). Specifically, as the number of iterations increases, the solutions gradually approach the PF. When the iterations reach around 300, the distributions begin to overlap, indicating the stabilization of the solution, thereby suggesting convergence of the proposed algorithm.

![](images/9075bee7ba11262526e498576be4885634ff9f1c0190486f0476b5ee4b1f63d4.jpg)

<details>
<summary>bar</summary>

| Model | SINR of Bob | SINR of Willie | Energy consumption of UAVs (J) |
| :--- | :--- | :--- | :--- |
| MODA | -2.27 | -4.17 | 5597 |
| MALO | -2.26 | -4.13 | 5095 |
| MOMVO | -2.36 | -4.07 | 6412 |
| MOMA | -2.35 | -4.07 | 5084 |
| IMOMA | -2.26 | -4.17 | 5458 |
</details>

(a)

![](images/0393ae7bbd6acef2334806a36663ebbe44a66e35ad894feca93773d69f7bd7d3.jpg)

<details>
<summary>bar</summary>

| Model | SINR of Bob | SINR of Willie | Energy consumption of UAVs (J) |
| :--- | :--- | :--- | :--- |
| MODA | 9.93 | 8.01 | 69240 |
| MALO | 9.75 | 8.03 | 79740 |
| MOMVO | 9.73 | 8.01 | 80430 |
| MOMA | 9.86 | 7.89 | 78540 |
| IMOMA | 10.18 | 8.31 | 64370 |
</details>

(b)   
Fig. 9. Optimization objective values obtained by different algorithms of (a) non-CB and (b) single CB approaches.

2) IGD Method: The IGD measures the average distance between the obtained solution set and the true PF. Since the true PF is often unattainable, we use the nondominated solutions from multiple experiments to form an approximate PF. Fig. 10(b) presents the IGD curve obtained by IMOMA. As can be seen, the IGD value decreases over iterations, indicating that the solutions are aligning with the PF. After 200 iterations, the IGD stabilizes, indicating that the IMOMA has converged effectively.   
3) ACR Method: We utilize the ACR, which has been shown to effectively reflect convergence performance [71], [72]. For each of the three optimization objectives in IMOMA, we calculate the ACR at each iteration, selecting the best objective value within the Pareto set. Trend plots of the ACR for the three objectives are shown in Fig. 10(c), where we observe that the ACR converges toward 0, indicating convergence.

In summary, the results from the solution distribution, IGD, and ACR methods confirm that the proposed IMOMA has effectively converged.

# VII. DISCUSSION

In this section, the synchronized transmission process of AAVs in the same VAA is further discussed.

In each round of G2A communications, with S sensing nodes at the LBS and N AAVs, if each sensing node broadcasts its data individually, S transmissions and $\textit { S } \times \textit { N }$ packet receptions are required. To improve energy efficiency, a master node can be selected to collect data from the sensing nodes and multicast the summarized packets to all AAVs. This aggregation reduces $( S \times N )$ receptions to $( S + N )$ receptions and one data transmission, with an additional N control packets used for the master node selection. The data-sharing process in each round involves the following steps [73].

1) Master Node Selection: AAVs multicast their IDs and residual energy levels to select the AAV with the highest energy as the master node, minimizing communication and ensuring adequate energy for data aggregation and forwarding.   
2) Master Node ID Sharing: The selected master node broadcasts its ID to the sensing nodes, so they know where to send their data. This single control packet saves energy compared to multiple transmissions.   
3) Data Collection by Master Node: Sensing nodes transmit their data to the master node, which aggregates the information for efficient distribution.   
4) Data Multicast to AAVs: The master node then multicasts the aggregated data to all AAVs, enabling them to perform synchronized beamforming for the final transmission.

To further reduce communication overhead, master node selections do not need to occur every round. AAVs can exchange energy status information and estimate the number of rounds a master node can sustain, reducing the frequency of selections and enhancing energy efficiency.

Furthermore, the overhead of this process is relatively low, approximately 10–20 s, which is minimal compared to the time savings in communication and motion achieved by the CB method. Compared to multihop approaches, our method saves 50% to 90% of the time, with minimal energy consumption, as confirmed by [73]. This combination of time and energy efficiency makes the method highly applicable to real-world scenarios, where quick decisions and sustainable energy use are essential.

# VIII. CONCLUSION

In this article, the dual AAV cluster-assisted maritime physical-layer secure communications via CB were investigated. Specifically, we considered the CB-based dual AAV cluster-assisted maritime secure communication system, which involves maritime long-distance communications and takes into account the security. In the system, one AAV cluster formed an MUVAA relay to forward data signals to the legitimate vessel, and the other AAV cluster formed an MUVAA jammer to send jamming signals to the eavesdropper. Moreover, taking into account the conflicting objectives, we formulated the SEMCMOP. Then, to resolve the complex NP-hard and large-scale problem, we proposed the IMOMA with chaotic solution initialization and hybrid solution update strategies. Simulation results showed that the CB-based method is significantly better than that of the non-CB, single

![](images/b3dd7bb6742c8d817c2090b0af59758a91c345d68b0c38930e51b52605f2a47f.jpg)

<details>
<summary>scatter</summary>

| SINR of Willie | SINR of Bob | Energy consumption of UAVs (J) | Iteration |
| -------------- | ----------- | ------------------------------- | --------- |
| -40            | -20         | 1.38 × 10⁵                      | 100       |
| -40            | -20         | 1.38 × 10⁵                      | 200       |
| -40            | -20         | 1.38 × 10⁵                      | 300       |
| -40            | -20         | 1.38 × 10⁵                      | 400       |
| -40            | -20         | 1.38 × 10⁵                      | 500       |
| -60            | -20         | 1.38 × 10⁵                      | 100       |
| -60            | -20         | 1.38 × 10⁵                      | 200       |
| -60            | -20         | 1.38 × 10⁵                      | 300       |
| -60            | -20         | 1.38 × 10⁵                      | 400       |
| -60            | -20         | 1.38 × 10⁵                      | 500       |
| -25            | -20         | 1.38 × 10⁵                      | 100       |
| -25            | -20         | 1.38 × 10⁵                      | 200       |
| -25            | -20         | 1.38 × 10⁵                      | 300       |
| -25            | -20         | 1.38 × 10⁵                      | 400       |
| -25            | -20         | 1.38 × 10⁵                      | 500       |
| 25             | -20         | 1.38 × 10⁵                      | 100       |
| 25             | -20         | 1.38 × 10⁵                      | 200       |
| 25             | -20         | 1.38 × 10⁵                      | 300       |
| 25             | -20         | 1.38 × 10⁵                      | 400       |
| 25             | -20         | 1.38 × 10⁵                      | 500       |
| 5              | -20         | 1.38 × 10⁵                      | 100       |
| 5              | -20         | 1.38 × 10⁵                      | 200       |
| 5              | -20         | 1.38 × 10⁵                      | 300       |
| 5              | -20         | 1.38 × 10⁵                      | 400       |
| 5              | -20         | 1.38 × 10⁵                      | 500       |
| -45            | -65         | 1.38 × 10⁵                      | 100       |
| -45            | -65         | 1.38 × 10⁵                      | 200       |
| -45            | -65         | 1.38 × 10⁵                      | 300       |
| -45            | -65         | 1.38 × 10⁵                      | 400       |
| -45            | -65         | 1.38 × 10⁵                      | 500       |
| -65            | -65         | 1.38 × 10⁵                      | 100       |
| -65            | -65         | 1.38 × 10⁵                      | 200       |
| -65            | -65         | 1.38 × 10⁵                      | 300       |
| -65            | -65         | 1.38 × 10⁵                      | 400       |
| -65            | -65         | 1.38 × 10⁵                      | 500       |
| -25            | -65         | 1.38 × 10⁵                      | 100       |
| -25            | -65         | 1.38 × 10⁵                      | 200       |
| -25            | -65         | 1.38 × 10⁵                      | 300       |
| -25            | -65         | 1.38 × 10⁵                      | 400       |
| -25            | -65         | 1.38 × 10⁵                      | 500       |
| -65            | -65         | 1.38 × 10⁵                      | 100       |
| -65            | -65         | 1.38 × 10⁵                      | 200       |
| -65            | -65         | 977                             | 397     |
| -65            | -65         | 977                             | 497     |
| -65            | -65         | 977                             | 597     |
| -25            | -65         | —                               | —        |
| -25            | -65         | —                               | —        |
| -25            | -65         | —                               | —        |
| -25            | -65         | —                               | —        |
| -25            | -65         | —                               | —        |
| -25            | -65         | —                               | —        |
| -25            | -65         | —                               (with label "Direction of PF")   | —        |
| -25            | -65         | —                               (with label "Direction of PF")   | —        |
| -25            | -65         | —                               (with label "Direction of PF")   | —        |
| -25            | -65         | —                               (with label "Direction of PF")   | —        |
| -25            | -65         | —                               (with label "PF")           | —        |
| -25            | -65         | —                               (with label "PF")           | —        |
| -25            | -65         | —                               (with label "PF")           | —        |
| -25            | -65         | —                               (with label "PF")           | —        |
| -25            | -65         | —                               (with label "PF")           | —        |

Note: The y-axis values are estimated based on the formula y = sin(φ) / sin(φ₀). The x-axis values are sin(φ) and the y-axis values are sin(φ₀). The labels represent different numbers of iterations.
</details>

(a)

![](images/a9126dc53381269c09baab58c931fad5d9a06b2adc80b3f2cb6a5ffe691f7f23.jpg)

<details>
<summary>line</summary>

| Iterations | IGD Value |
| ---------- | --------- |
| 0          | 1.2       |
| 50         | 0.8       |
| 100        | 0.75      |
| 150        | 0.7       |
| 200        | 0.65      |
| 250        | 0.6       |
| 300        | 0.6       |
| 350        | 0.6       |
| 400        | 0.6       |
</details>

![](images/76c3b9c039f711c27c6a435ccd21a2526a2ce89793305b9845db31b6df20797c.jpg)

<details>
<summary>line</summary>

| Iterations | Optimization objective 1 | Optimization objective 2 | Optimization objective 3 |
| ---------- | ------------------------ | ------------------------ | ------------------------ |
| 100        | 0.02                     | 0.00                     | 0.02                     |
| 150        | 0.01                     | 0.00                     | 0.03                     |
| 200        | 0.04                     | 0.00                     | 0.05                     |
| 250        | 0.05                     | 0.00                     | 0.04                     |
| 300        | 0.00                     | 0.00                     | 0.00                     |
| 350        | 0.01                     | 0.00                     | 0.01                     |
| 400        | 0.00                     | 0.00                     | 0.00                     |
</details>

（c）  
Fig. 10. Convergence analysis of the IMOMA. (a) Solution distribution with different iterations. (b) IGD curve. (c) ACRs of optimization objectives.

CB, and multihop approaches, which means that CB is suitable for long-distance maritime secure communications. Moreover, comparison results indicated the proposed IMOMA outperforms several comparison algorithms and is more suitable for CB-based maritime long-distance secure communication scenarios. Future work can extend the results of this study by incorporating real-time variations in vessel positions and adopting more adaptive DRL algorithms, enhancing the ability of system dynamics to autonomously adjust to real-world scenarios. Additionally, exploring high-altitude communication platforms, such as HAPs, could further enhance system diversity.

# ACKNOWLEDGMENT

Jiawei Huang, Aimin Wang, and Jiahui Li are with the College of Computer Science and Technology, and the Key Laboratory of Symbolic Computation and Knowledge Engineering of Ministry of Education, Jilin University, Changchun 130012, China (e-mail: huangjiawei97@foxmail.com; wangam@jlu.edu.cn; lijiahui@jlu.edu.cn).

Geng Sun is with the College of Computer Science and Technology, and the Key Laboratory of Symbolic Computation and Knowledge Engineering of Ministry of Education, Jilin University, Changchun 130012, China, and also with the College of Computing and Data Science, Nanyang Technological University, Singapore 639798 (e-mail: sungeng@jlu.edu.cn).

Jiacheng Wang and Dusit Niyato are with the College of Computing and Data Science, Nanyang Technological University, Singapore 639798 (e-mail: jiacheng.wang@ntu.edu.sg; dniyato@ntu.edu.sg).

Hongyang Du is with the Department of Electrical and Electronic Engineering, The University of Hong Kong, Hong Kong (e-mail: duhy@eee.hku.hk).

# REFERENCES

[1] J. Huang, A. Wang, G. Sun, and J. Li, “Jamming-aided maritime physical layer encrypted dual-UAVs communications exploiting collaborative beamforming,” in Proc. IEEE CSCWD, 2023, pp. 1142–1147.   
[2] H. Zhang, T. Zhou, T. Xu, M. Cheng, and H. Hu, “Field measurement and channel modeling around Wailingding Island for maritime wireless communication,” IEEE Antennas Wireless Propag. Lett., vol. 23, no. 6, pp. 1934–1938, Jun. 2024.   
[3] X. Fang et al., “NOMA-based hybrid satellite-UAV-terrestrial networks for 6G maritime coverage,” IEEE Trans. Wireless Commun., vol. 22, no. 1, pp. 138–152, Jan. 2023.   
[4] J.-B. Wang, C. Zeng, C. Ding, H. Zhang, M. Lin, and J. Wang, “Unmanned surface vessel assisted maritime wireless communication toward 6G: Opportunities and challenges,” IEEE Wireless Commun., vol. 29, no. 6, pp. 72–79, Dec. 2022.   
[5] N. Nomikos, A. Giannopoulos, A. Kalafatelis, V. Özduran, P. Trakadas, and G. K. Karagiannidis, “Improving connectivity in 6G maritime communication networks with UAV swarms,” IEEE Access, vol. 12, pp. 18739–18751, 2024.   
[6] L. P. Qian, H. Zhang, Q. Wang, Y. Wu, and B. Lin, “Joint multi-domain resource allocation and trajectory optimization in UAV-assisted maritime IoT networks,” IEEE Internet Things J., vol. 10, no. 1, pp. 539–552, Jan. 2023.

[7] G. Sun, J. Li, A. Wang, Q. Wu, Z. Sun, and Y. Liu, “Secure and energy-efficient UAV relay communications exploiting collaborative beamforming,” IEEE Trans. Commun., vol. 70, no. 8, pp. 5401–5416, Aug. 2022.   
[8] S. Jayaprakasam, S. K. A. Rahim, and C. Y. Leow, “Distributed and collaborative beamforming in wireless sensor networks: Classifications, trends, and research directions,” IEEE Commun. Surveys Tuts., vol. 19, no. 4, pp. 2092–2116, 4th Quart., 2017.   
[9] L. Zhu, J. Zhang, Z. Xiao, X. Cao, X. Xia, and R. Schober, “Millimeterwave full-duplex UAV relay: Joint positioning, beamforming, and power control,” IEEE J. Sel. Areas Commun., vol. 38, no. 9, pp. 2057–2073, Sep. 2020.   
[10] H. Bastami, M. Letafati, M. Moradikia, A. Abdelhadi, H. Behroozi, and L. Hanzo, “On the physical layer security of the cooperative ratesplitting-aided downlink in UAV networks,” IEEE Trans. Inf. Forensics Security., vol. 16, pp. 5018–5033, 2021.   
[11] K. Mahmood, S. Shamshad, M. F. Ayub, Z. Ghaffar, M. K. Khan, and A. K. Das, “Design of provably secure authentication protocol for edge-centric maritime transportation system,” IEEE Trans. Intell. Transp. Syst., vol. 24, no. 12, pp. 14536–14545, Dec. 2023.   
[12] Y. Wu, A. Khisti, C. Xiao, G. Caire, K. Wong, and X. Gao, “A survey of physical layer security techniques for 5G wireless networks and challenges ahead,” IEEE J. Sel. Areas Commun., vol. 36, no. 4, pp. 679–695, Apr. 2018.   
[13] D. Wang, B. Bai, W. Zhao, and Z. Han, “A survey of optimization approaches for wireless physical layer security,” IEEE Commun. Surveys Tuts., vol. 21, no. 2, pp. 1878–1911, 2nd Quart., 2019.   
[14] Y. Zhou et al., “Improving physical layer security via a UAV friendly jammer for unknown eavesdropper location,” IEEE Trans. Veh. Technol., vol. 67, no. 11, pp. 11280–11284, Nov. 2018.   
[15] H. Dang-Ngoc et al., “Secure swarm UAV-assisted communications with cooperative friendly jamming,” IEEE Internet Things J., vol. 9, no. 24, pp. 25596–25611, Dec. 2022.   
[16] K. Liu, P. Li, C. Liu, L. Xiao, and L. Jia, “UAV-aided anti-jamming maritime communications: A deep reinforcement learning approach,” in Proc. IEEE WCSP, 2022, pp. 1–6.   
[17] Y. Wu, W. Yang, X. Guan, and Q. Wu, “UAV-enabled relay communication under malicious jamming: Joint trajectory and transmit power optimization,” IEEE Trans. Veh. Technol., vol. 70, no. 8, pp. 8275–8279, Aug. 2021.   
[18] S. Rani, H. Babbar, P. Kaur, M. D. Alshehri, and S. H. Ahmed, “An optimized approach of dynamic target nodes in wireless sensor network using bio inspired algorithms for maritime rescue,” IEEE Trans. Intell. Transp. Syst., vol. 24, no. 2, pp. 2548–2555, Feb. 2023.   
[19] J. Tang, H. Duan, and S. Lao, “Swarm intelligence algorithms for multiple unmanned aerial vehicles collaboration: A comprehensive review,” Artif. Intell. Rev., vol. 56, no. 5, pp. 4295–4327, 2023.   
[20] R. J. Kuo, M. F. Luthfiansyah, N. A. Masruroh, and F. E. Zulvia, “Application of improved multi-objective particle swarm optimization algorithm to solve disruption for the two-stage vehicle routing problem with time windows,” Expert Syst. Appl., vol. 225, Sep. 2023, Art. no. 120009.   
[21] C. Zeng, J. Wang, C. Ding, M. Lin, and J. Wang, “MIMO unmanned surface vessels enabled maritime wireless network coexisting with satellite network: Beamforming and trajectory design,” IEEE Trans. Commun., vol. 71, no. 1, pp. 83–100, Jan. 2023.   
[22] X. Hu et al., “Performance analysis of end-to-end LEO satellite-aided shore-to-ship communications: A stochastic geometry approach,” IEEE Trans. Wireless Commun., vol. 23, no. 9, pp. 11753–11769, Sep. 2024.

[23] R. Wu, Z. Li, Z. Xie, and X. Liang, “Intelligent spectrum sharing strategy for integrated satellite-maritime heterogeneous mobile networks,” IEEE Trans. Veh. Technol., vol. 73, no. 5, pp. 6780–6794, May 2024.   
[24] C. Zeng, J.-B. Wang, C. Ding, H. Zhang, M. Lin, and J. Cheng, “Joint optimization of trajectory and communication resource allocation for unmanned surface vehicle enabled maritime wireless networks,” IEEE Trans. Commun., vol. 69, no. 12, pp. 8100–8115, Dec. 2021.   
[25] C. Liu, Y. Zhang, G. Niu, L. Jia, L. Xiao, and J. Luan, “Towards reinforcement learning in UAV relay for anti-jamming maritime communications,” Digit. Commun. Netw., vol. 9, no. 6, pp. 1477–1485, Dec. 2023.   
[26] W. Aman, S. Al-Kuwari, M. Muzzammil, M. M. U. Rahman, and A. Kumar, “Security of underwater and air–water wireless communication: State-of-the-art, challenges and outlook,” Ad Hoc Netw, vol. 142, Apr. 2023, Art. no. 103114.   
[27] A. Vangala et al., “Big data-enabled authentication framework for offshore maritime communication using drones,” IEEE Trans. Veh. Technol., vol. 73, no. 7, pp. 10196–10210, Jul. 2024.   
[28] X. Ren et al., “A novel access and handover authentication scheme in UAV-aided satellite-terrestrial integration networks enabling 5G,” IEEE Trans. Netw. Service Manage., vol. 20, no. 3, pp. 3880–3899, Sep. 2023.   
[29] N. Zhao et al., “Caching UAV assisted secure transmission in hyper-dense networks based on interference alignment,” IEEE Trans. Commun., vol. 66, no. 5, pp. 2281–2294, May 2018.   
[30] W. Wang et al., “Robust 3D-trajectory and time switching optimization for dual-UAV-enabled secure communications,” IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3334–3347, Nov. 2021.   
[31] F. Lu et al., “Resource and trajectory optimization for UAV-relayassisted secure maritime MEC,” IEEE Trans. Commun., vol. 72, no. 3, pp. 1641–1652, Mar. 2024.   
[32] H. Yang, K. Lin, L. Xiao, Y. Zhao, Z. Xiong, and Z. Han, “Energy harvesting UAV-RIS-assisted maritime communications based on deep reinforcement learning against jamming,” IEEE Trans. Wireless Commun., vol. 23, no. 8, pp. 9854–9868, Aug. 2024.   
[33] H. Luo, S. Ma, H. Tao, R. Ruby, J. Zhou, and K. Wu, “DRL-Optimized optical communication for a reliable UAV-based maritime data transmission,” IEEE Internet Things J., vol. 11, no. 10, pp. 18768–18781, May 2024.   
[34] H. A. Hashim and M. A. Abido, “Location management in LTE networks using multi-objective particle swarm optimization,” Comput. Netw., vol. 157, pp. 78–88, Jul. 2019.   
[35] H. Qiu and H. Duan, “A multi-objective pigeon-inspired optimization approach to UAV distributed flocking among obstacles,” Inf. Sci., vol. 509, pp. 515–529, Jan. 2020.   
[36] Y. Liu, C.-X. Wang, H. Chang, Y. He, and J. Bian, “A novel nonstationary 6G UAV channel model for maritime communications,” IEEE J. Select. Areas Commun., vol. 39, no. 10, pp. 2992–3005, Oct. 2021.   
[37] A. G. Stove, M. Gashinova, S. Hristov, and M. Cherniakov, “Passive maritime surveillance using satellite communication signals,” IEEE Trans. Aerosp. Electron. Syst., vol. 53, no. 6, pp. 2987–2997, Dec. 2017.   
[38] Y. Liu, J. Yan, and X. Zhao, “Deep reinforcement learning based latency minimization for mobile edge computing with virtualization in maritime UAV communication network,” IEEE Trans. Veh. Technol., vol. 71, no. 4, pp. 4225–4236, Apr. 2022.   
[39] J. Li, G. Sun, L. Duan, and Q. Wu, “Multi-objective optimization for UAV swarm-assisted IoT with virtual antenna arrays,” IEEE Trans. Mobile Comput., vol. 23, no. 5, pp. 4890–4907, May 2024.   
[40] X. Wang, W. Feng, Y. Chen, and N. Ge, “UAV swarm-enabled aerial coMP: A physical layer security perspective,” IEEE Access, vol. 7, pp. 120901–120916, 2019.   
[41] W. U. Khan, F. Jameel, X. Li, M. Bilal, and T. A. Tsiftsis, “Joint spectrum and energy optimization of NOMA-enabled small-cell networks with QoS guarantee,” IEEE Trans. Veh. Technol., vol. 70, no. 8, pp. 8337–8342, Aug. 2021.   
[42] X. Lin, X. Zhang, Z. Yang, F. Liu, Z. Wang, and Q. Zhang, “Smooth Tchebycheff Scalarization for multi-objective optimization,” 2024, arXiv:2402.19078.   
[43] S. Mohanti, C. Bocanegra, S. G. Sanchez, K. Alemdar, and K. R. Chowdhury, “SABRE: Swarm-based aerial beamforming radios: Experimentation and emulation,” IEEE Trans. Wireless Commun., vol. 21, no. 9, pp. 7460–7475, Sep. 2022.   
[44] J. Feng, Y. Lu, B. Jung, D. Peroulis, and Y. C. Hu, “Energy-efficient data dissemination using beamforming in wireless sensor networks,” ACM Trans. Sens. Netw., vol. 9, no. 3, p. 31, 2013.   
[45] J. Guo, L. Wang, F. Li, and J. Xue, “CSI feedback with model-driven deep learning of massive MIMO systems,” IEEE Commun. Lett., vol. 26, no. 3, pp. 547–551, Mar. 2022.

[46] I. Ahmad, C. Sung, D. Kramarev, G. Lechner, H. Suzuki, and I. Grivell, “Outage probability and ergodic capacity of distributed transmit beamforming with imperfect CSI,” IEEE Trans. Veh. Technol., vol. 71, no. 3, pp. 3008–3019, Mar. 2022.   
[47] Z. Wang et al., “A tutorial on extremely large-scale MIMO for 6G: Fundamentals, signal processing, and applications,” IEEE Commun. Surveys Tuts., vol. 26, no. 3, pp. 1560–1605, 3rd Quart., 2024.   
[48] J. Gong, J. S. Thompson, S. Zhou, and Z. Niu, “Base station sleeping and resource allocation in renewable energy powered cellular networks,” IEEE Trans. Commun., vol. 62, no. 11, pp. 3801–3813, Nov. 2014.   
[49] M. Mozaffari, W. Saad, M. Bennis, and M. Debbah, “Communications and control for wireless drone-based antenna array,” IEEE Trans. Commun., vol. 67, no. 1, pp. 820–834, Jan. 2019.   
[50] Y. Wang, W. Feng, J. Wang, and T. Q. S. Quek, “Hybrid satellite-UAV-terrestrial networks for 6G ubiquitous coverage: A maritime communications perspective,” IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3475–3490, Nov. 2021.   
[51] J. Li, H. Kang, G. Sun, S. Liang, Y. Liu, and Y. Zhang, “Physical layer secure communications based on collaborative beamforming for UAV networks: A multi-objective optimization approach,” in Proc. IEEE INFOCOM, 2021, pp. 1–10.   
[52] Y. Zeng, Q. Wu, and R. Zhang, “Accessing from the sky: A tutorial on UAV communications for 5G and beyond,” Proc. IEEE, vol. 107, no. 12, pp. 2327–2375, Dec. 2019.   
[53] C. Blum, J. Puchinger, G. R. Raidl, and A. Roli, “Hybrid metaheuristics in combinatorial optimization: A survey,” Appl. Soft Comput., vol. 11, no. 6, pp. 4135–4151, Sep. 2011.   
[54] M. Andrews and M. Dinitz, “Maximizing capacity in arbitrary wireless networks in the SINR model: Complexity and game theory,” in proc. IEEE INFOCOM, 2009, pp. 1332–1340.   
[55] G. Sun et al., “UAV-enabled secure communications via collaborative beamforming with imperfect eavesdropper information,” IEEE Trans. Mobile Comput., vol. 23, no. 4, pp. 3291–3308, Apr. 2024.   
[56] S. A. Yasear and K. R. Ku-Mahamud, “Review of the multi-objective swarm intelligence optimization algorithms,” J. Inf. Commun. Technol., vol. 20, no. 2, pp. 171–211, 2021.   
[57] G. Lei, X. Chang, Y. Tianhang, and W. Tuerxun, “An improved mayfly optimization algorithm based on median position and its application in the optimization of PID parameters of hydro-turbine governor,” IEEE Access, vol. 10, pp. 36335–36349, 2022.   
[58] D. Zhou, Z. Kang, X. Su, and C. Yang, “An enhanced mayfly optimization algorithm based on orthogonal learning and chaotic exploitation strategy,” Int. J. Mach. Learn. Cybern., vol. 13, no. 11, pp. 3625–3643, 2022.   
[59] K. Zervoudakis and S. Tsafarakis, “A mayfly optimization algorithm,” Comput. Ind. Eng., vol. 145, Jul. 2020, Art. no. 106559.   
[60] B. Kazimipour, X. Li, and A. K. Qin, “A review of population initialization techniques for evolutionary algorithms,” in Proc. IEEE Congr. Evol. Comput., 2014, pp. 2585–2592.   
[61] G. Sun, J. Li, Y. Liu, S. Liang, and H. Kang, “Time and energy minimization communications based on collaborative beamforming for UAV networks: A multi-objective optimization method,” IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3555–3572, Nov. 2021.   
[62] Y. Li, M. Han, and Q. Guo, “Modified whale optimization algorithm based on tent chaotic mapping and its application in structural optimization,” KSCE J. Civ. Eng., vol. 24, no. 12, pp. 3703–3713, 2020.   
[63] S. Mirjalili and A. Lewis, “The whale optimization algorithm,” Adv. Eng. Softw., vol. 95, pp. 51–67, May 2016.   
[64] L. Abualigah, A. Diabat, S. Mirjalili, M. Abd Elaziz, and A. H. Gandomi, “The arithmetic optimization algorithm,” Comput. Methods Appl. Mech. Eng., vol. 376, Apr. 2021, Art. no. 113609.   
[65] J. Huang, A. Wang, G. Sun, J. Li, and X. Zheng, “Physical layer encrypted maritime communications Utilizing UAV-enabled virtual antenna array,” in Proc. IEEE ICC, 2024, pp. 67–72.   
[66] S. Mirjalili, “Dragonfly algorithm: A new meta-heuristic optimization technique for solving single-objective, discrete, and multi-objective problems,” Neural Comput. Appl., vol. 27, no. 4, pp. 1053–1073, 2016.   
[67] S. Mirjalili, P. Jangir, S. Z. Mirjalili, S. Saremi, and I. N. Trivedi, “Optimization of problems with multiple objectives using the multi-verse optimization algorithm,” Knowl. Based Syst., vol. 134, pp. 50–71, Oct. 2017.   
[68] S. Mirjalili, P. Jangir, and S. Saremi, “Multi-objective ant lion optimizer: A multi-objective optimization algorithm for solving engineering problems,” Appl. Intell., vol. 46, no. 1, pp. 79–95, 2017.   
[69] Y. Chen, N. Zhao, Z. Ding, and M. Alouini, “Multiple UAVs as relays: Multi-hop single link versus multiple dual-hop links,” IEEE Trans. Wireless Commun., vol. 17, no. 9, pp. 6348–6359, Sep. 2018.

[70] K. Deb and H. Jain, “An evolutionary many-objective optimization algorithm using reference-point-based nondominated sorting approach, part I: Solving problems with box constraints,” IEEE Trans. Evol. Comput., vol. 18, no. 4, pp. 577–601, Aug. 2014.   
[71] Y. Chen and J. He, “Average convergence rate of evolutionary algorithms in continuous optimization,” Inf. Sci., vol. 562, pp. 200–219, Jul. 2021.   
[72] J. He and G. Lin, “Average convergence rate of evolutionary algorithms,” IEEE Trans. Evol. Comput., vol. 20, no. 2, pp. 316–321, Apr. 2016.   
[73] J. Feng, Y. Nimmagadda, Y. Lu, B. Jung, D. Peroulis, and Y. C. Hu, “Analysis of energy consumption on data sharing in beamforming for wireless sensor networks,” in Proc. IEEE ICCCN, 2010, pp. 1–6.

![](images/08fbbe6b088811b87ac77ea13a05a4f04301f120763e2c979c06717c9efc2b8b.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a young man in a collared shirt (no text or symbols visible)
</details>

Jiahui Li received the B.S. degree in software engineering and the Ph.D. degree in computer science and technology from Jilin University, Changchun, China, in 2018 and 2024, respectively.

He is currently a Postdoctoral Researcher with the College of Computer Science and Technology, Jilin University. His current research focuses on UAV networks, antenna arrays, and optimization.

![](images/0d02386249e17730811da4483e375cc3068d19354b04e15ee1bb410f71e58089.jpg)

<details>
<summary>natural_image</summary>

Portrait of a young woman with dark hair and short dark hair, wearing a black top (no visible text or symbols)
</details>

Jiawei Huang received the B.S. degree in software engineering from Dalian Jiaotong University, Dalian, China, in 2019, and the M.S. degree in software engineering from Jilin University, Changchun, China, in 2024, where she is currently pursuing the Ph.D. degree in computer science.

Her current research interests are UAV networks and optimization.

![](images/ed94472d3d88ae6b3a1784b887bd0a91c8ab6b2070a832202d1811fb9cd9bee2.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a young man with short dark hair (no text or symbols visible)
</details>

Jiacheng Wang received the bachelor’s degree from the Department of Science, Kunming University of Science and Technology, Kunming, China, in 2015, and the M.E. and Ph.D. degrees from the Department of Communication and Information Technology, Chongqing University of Posts and Telecommunications, Chongqing, China, in 2018 and 2022, respectively.

He is currently a Research Associate of Computer Science and Engineering with Nanyang Technological University, Singapore. His research

interests include wireless sensing, semantic communications, and metaverse.

![](images/79c8f375e7944fd0c8e86646af2a26771b2ea5a5f2dd6e3e32dda2465cc5b445.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man wearing a dark turtleneck sweater (no text or symbols visible)
</details>

Aimin Wang received the Ph.D. degree in communication and information system from Jilin University, Changchun, China, in 2004.

He is currently a Professor with Jilin University. His research interests are wireless sensor networks and QoS for multimedia transmission.

![](images/f266597d9c147bf17936952c3c560538507233fc379f29bc025e198728fb869f.jpg)

<details>
<summary>natural_image</summary>

Portrait of a young man wearing glasses and a dark shirt, with blurred architectural background (no text or symbols visible)
</details>

Hongyang Du (Member, IEEE) received the B.Sc. degree from Beijing Jiaotong University, Beijing, China, in 2021, and the Ph.D. degree from Nanyang Technological University, Singapore, in 2024.

He is currently an Assistant Professor with the Department of Electrical and Electronic Engineering, The University of Hong Kong, Hong Kong, and the Principal Investigator of the Network Intelligence and Computing Ecosystem Lab. His research interests include semantic communications, generative AI, and resource allocation.

![](images/fbe377b97de5b4a4b462b715aa016dce6056526428540cf84e8c48d95bd6e34b.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in formal attire against a blue background (no text or symbols visible)
</details>

Geng Sun (Senior Member, IEEE) received the B.S. degree in communication engineering from Dalian Polytechnic University, Dalian, China, in 2007, and the Ph.D. degree in computer science and technology from Jilin University, Changchun, China, in 2018.

He was a Visiting Researcher with the School of Electrical and Computer Engineering, Georgia Institute of Technology, Atlanta, GA, USA. He is a Professor with the College of Computer Science and Technology, Jilin University, and also a Senior

Research Scholar with the College of Computing and Data Science, Nanyang Technological University. His research interests include wireless networks, UAV communications, and collaborative beamforming and optimizations.

![](images/7f70de96f36c1a716f68e6ccb0da50d3ca153979c084582ef4660691e83f5fe2.jpg)

<details>
<summary>natural_image</summary>

Portrait of a person wearing glasses and a dark jacket (no visible text or symbols)
</details>

Dusit Niyato (Fellow, IEEE) received the bachelor’s degree in computer engineering from King Mongkut’s Institute of Technology Ladkrabang, Bangkok, Thailand, in 1999, the master’s and Ph.D. degrees from the University of Manitoba, Winnipeg, MB, Canada, in 2005 and 2008, respectively.

He is currently a Professor with the College of Computing and Data Science, Nanyang Technological University, Singapore. His research interests are in the areas of sustainability, edge intelligence, decentralized machine learning, and

incentive mechanism design.