# UAV-Enabled Integrated Sensing and Communication: Opportunities and Challenges

Kaitao Meng, Qingqing Wu, Jie Xu, Wen Chen, Zhiyong Feng, Robert Schober, and A. Lee Swindlehurst

# Abstra ct

Unmanned aerial vehicle (UAV)-enabled integrated sensing and communication (ISAC) has attracted growing research interests in the context of sixth-generation (6G) wireless networks, in which UAVs will be exploited as aerial wireless platforms to provide better coverage and enhanced sensing and communication (S&C) services. However, due to the size, weight, and power (SWAP) constraints of UAVs, their controllable mobility, and the line-ofsight (LoS) air-ground channels, UAV-enabled ISAC introduces new opportunities and challenges. This article provides an overview of UAV-enabled ISAC and proposes various solutions for optimizing the S&C performance. In particular, we first introduce UAV-enabled joint S&C and discuss UAV motion control, wireless resource allocation, and interference management for ISAC systems employing single and multiple UAVs. Then, we present two application scenarios for exploiting the synergy between S&C, namely sensing-assisted UAV communication and communication-assisted UAV sensing. Finally, we highlight several interesting research directions to guide and motivate future work.

# Introducti on

Integrated sensing and communication (ISAC) has recently emerged as a candidate technology for sixth-generation (6G) wireless networks, in which wireless infrastructure and spectrum resources are shared to provide both sensing and communication (S&C) services. By leveraging advanced multiple-input and multiple-output (MIMO) and millimeter-wave (mmWave)/ terahertz (THz) technology, ISAC is expected to provide high-throughput, ultra-reliable, and low-latency wireless communications, as well as ultra-accurate and high-resolution wireless sensing for 6G [1, 2]. This thus offers new opportunities for realizing environment- and location-aware applications for smart cities, smart manufacturing, autonomous driving, and so on. However, conventional terrestrial ISAC networks can only provide sensing services within a fixed and limited range, as surrounding obstacles may block the line-of-sight (LoS) links to long-range targets, which leads to a seriously degraded sensing performance [3, 4].

Motivated by the success of pilot projects on unmanned aerial vehicle (UAV)-enabled communications, such as AT&T’s flying COW and Nokia’s F-cell [5], there is a growing interest in employing UAVs as cost-effective aerial platforms to provide enhanced ISAC services supporting traffic accident rescue, non-authorized eavesdropper monitoring, and service enhancement in temporary hot spot areas, as illustrated in Fig. 1. By exploiting the high mobility of UAVs in three-dimensional (3D) space and their strong air-ground LoS channels, UAV-enabled ISAC is expected to provide better S&C coverage, more flexible surveillance, and enhanced S&C performance compared to terrestrial ISAC. However, such a new aerial ISAC paradigm also introduces new design challenges. First, both fixedwing and rotary-wing UAVs have to meet stringent constraints regarding their size, weight, and power, which limits their communication, sensing, and endurance capabilities. Second, strong air-ground LoS links inevitably incur severe interference in ISAC networks [6], which however can be exploited to extract rich target information such as location, velocity, and direction. Third, the flexible UAV placement/trajectory introduces new degrees-offreedom (DoFs) for optimization, which makes the system design more complicated. Last but not least, unlike conventional UAV-enabled communications focusing on rate maximization, UAV-enabled ISAC systems need to incorporate (radar) sensing performance metrics (e.g., detection probability and estimation/recognition accuracy), sensing signal processing (e.g., echo signal processing and clutter interference suppression) [7], and efficient cooperative mechanisms. As such, how to design UAV-enabled ISAC to achieve high S&C performance and effective coordination among the UAVs is a new and challenging problem to address.

Given the above considerations, there is an urgent need to investigate joint S&C design for UAV-enabled ISAC systems for improving spectrum efficiency, enabling hardware reuse, and reducing power consumption. Specifically, proper trajectory planning and resource allocation are needed to meet the distinct S&C performance requirements and balance the performance-cost trade-off. For example, communication services are usually continuously provided for a period of

Kaitao Meng is with the University of Macau, China; Qingqing Wu (corresponding author) and Wen Chen are with Shanghai Jiao Tong University, China; Jie Xu is with The Chinese University of Hong Kong (Shenzhen), China; Zhiyong Feng is with Beijing University of Posts and Telecommunications, China; Robert Schober is with Friedrich-Alexander University Erlangen-Nürnberg (FAU), Germany; A. Lee Swindlehurst is with the University of California, Irvine, USA.

Digital Object Identifier: 10.1109/MWC.131.2200442

![](images/018ca93e150a02217c7a5e945062c30791f5ecfa60009a3d7b0897e709ab3513.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph_InterferenceManagement["Interference management"]
        A["Hot spot"] --> B["User"]
        B --> C["Target"]
        D["Error bar"] --> E["Error signal"]
        F["Error signal"] --> G["Error signal"]
        H["Error signal"] --> I["Error signal"]
        J["Error signal"] --> K["Error signal"]
        L["Error signal"] --> M["Error signal"]
        N["Error signal"] --> O["Error signal"]
        P["Error signal"] --> Q["Error signal"]
        R["Error signal"] --> S["Error signal"]
        T["Error signal"] --> U["Error signal"]
        V["Error signal"] --> W["Error signal"]
        X["Error signal"] --> Y["Error signal"]
        Z["Error signal"] --> AA["Error signal"]
        AB["Error signal"] --> AC["Error signal"]
        AD["Error signal"] --> AE["Error signal"]
        AF["Error signal"] --> AG["Error signal"]
        AH["Error signal"] --> AI["Error signal"]
        AJ["Error signal"] --> AK["Error signal"]
        AL["Error signal"] --> AM["Error signal"]
        AN["Error signal"] --> AO["Error signal"]
        AP["Error signal"] --> AQ["Error signal"]
        AR["Error signal"] --> AS["Error signal"]
        AT["Error signal"] --> AU["Error signal"]
        AV["Error signal"] --> AW["Error signal"]
        AX["Error signal"] --> AY["Error signal"]
        AZ["Error signal"] --> BA["Error signal"]
        BB["Error signal"] --> BC["Error signal"]
        BD["Error signal"] --> BE["Error signal"]
        BF["Error signal"] --> BG["Error signal"]
        BH["Error signal"] --> BI["Error signal"]
        BJ["Error signal"] --> BK["Error signal"]
        BL["Error signal"] --> BM["Error signal"]
        BN["Error signal"] --> BO["Error signal"]
        BP["Error signal"] --> BQ["Error signal"]
        BR["Error signal"] --> BS["Error signal"]
        BT["Error signal"] --> BU["Error signal"]
        BV["Error signal"] --> BW["Error signal"]
        BX["Error signal"] --> BY["Error signal"]
        BZ["Error signal"] --> CA["Error signal"]
        CB["Error signal"] --> DA["Error signal"]
        DB["Error signal"] --> DBQ["Error signal"]
        DC["Error signal"] --> DBX["Error signal"]
        DBT["Error signal"] --> DBU["X/A"]
        DBU["X/A"] --> DBV["X/A"]
        DBV["X/A"] --> DBW["X/A"]
        DBW["X/A"] --> DBX["X/A"]
        DBX["X/A"] --> DBY["X/A"]
    end

    subgraph_CooperativeISAC["Cooperative ISAC"]
        BZ
        BC
        BW
        BA
        BB
        BW
        BA
        BB
        BW
    end

    style InterferenceManagement fill:#f9f,stroke:#333
    style CooperativeISAC fill:#bbf,stroke:#333
    style User fill:#dfd,stroke:#333
    style Target fill:#dfd,stroke:#333
    style CooperativeISAC fill:#dfd,stroke:#333
    style User fill:#dfd,stroke:#333
    style Target fill:#dfd,stroke:#333
    style CooperativeISAC fill:#dfd,stroke:#333
    style User fill:#dfd,stroke:#333
    style Target fill:#dfd,stroke:#333
    style CooperativeISAC fill:#dfd,stroke:#333
    style User fill:#dfd,stroke:#386
    style Target fill:#dfd,stroke:#386
    style CooperativeISAC fill:#dfd,stroke:#386
    style User fill:#dfd,stroke:#386
    style Target fill:#dfd,stroke:#386
    style CooperativeISAC fill:#dfd,stroke:#386
    style User fill:#dfd,stroke:#386
    style Target fill:#dfd,stroke:#386
    style CooperativeISAC fill:#dfd,stroke:#386
    style User fill:#dfd,stroke:#386
    style Targetfill fill:#dfd,stroke:#386
```
</details>

FIGURE 1. Application scenarios for UAV-enabled ISAC.

time determined by the data volume, while sensing tasks tend to be performed with a certain sensing frequency depending on the targets’ position and velocity, and the task’s timeliness requirement. On the other hand, enforcing continuous sensing along with communication at all times may inevitably lead to higher energy consumption, a waste of spectrum resources, and stronger interference to communication users [8]. Moreover, the use of multiple UAVs to collaboratively provide ISAC services is an effi cient solution to further enhance the S&C coverage and increase the integration gain, but such systems demand more sophisticated interference management [6].

Besides the integration gain obtained by the joint design of S&C, mutual assistance of S&C off ers the potential to achieve a coordination gain in UAV-enabled ISAC, which enables sensing-assisted UAV communication and communication-assisted UAV sensing. For example, UAVs equipped with (radar) sensing capabilities can design their real-time trajectories and allocate communication resources based on their sensing results while incurring only a small signaling overhead. In turn, wireless communication provides an efficient means for UAVs to enhance their sensing data processing capabilities via, for example, sensory data off loading and over-the-air computation [9].

In view of the above discussion, this article aims to provide a state-of-the-art overview of UAV-enabled ISAC, by identifying the related key challenges, discussing potential solutions, and presenting interesting directions for future research. To this end, the following section proposes new ISAC protocols and discusses UAV-enabled joint S&C design for single- and multi-UAV systems, respectively. We then present novel concepts for sensing-assisted UAV communication and communication-assisted UAV sensing. Following that we provide promising research directions for the integration of ISAC and UAVs. Finally, we conclude the article.

# uAV-enAbled JoInt sensIng And communIcAtIon

This section discusses UAV-enabled joint S&C, where UAVs serve ground communication users while concurrently detecting or estimating ground targets in relevant sensing areas. We distinguish between single- and multi-UAV systems.

# sIngle-uAV-enAbled IsAc

While sensing and communication functionalities could be time multiplexed, improved performance is expected if both services can operate as needed, and possibly simultaneously. Therefore, in this subsection, we present new transmission protocols, novel resource allocation strategies, and UAV trajectory designs for UAV-Enabled joint S&C.

ISAC Frame Protocol Design: Suppose that unified ISAC waveforms or beams are employed to sense multiple targets, for which the received sensing signal-to-clutter-and-noise ratio (SCNR) [4] or the sensing beampattern [10] are adopted as performance metrics. Since communication is generally continuously required while sensing tasks are often performed periodically, specifi c ISAC frames should be designed to facilitate the resource allocation and trajectory optimization, as shown in the top subfigure of Fig. 2. During each ISAC frame, diff erent targets may be sensed simultaneously or separately at least once. Accordingly, the ISAC frame protocols can be classifi ed into the following three categories.

Co-ISAC: During each ISAC frame, all targets are sensed simultaneously at least once, and thus the ISAC beams need to be radiated divergently to cover all targets and users at the same time, as shown in the top subfigure of Fig. 2. Due to the potentially stringent sensing requirements for all targets, the UAV trajectory design in this case is less flexible since the transmit power has to be divided into multiple directions for both S&C.

TDM-ISAC: Multi-target sensing is performed in a time division multiplexing (TDM) manner along with communication functions, that is, in each time instant unified waveforms/beams only cover one intended target (instead of all targets in Co-ISAC) together with one communication user. In this case, echo signals from other targets become clutter/interference for the intended target sensing. On the other hand, a target and users with small angular separation tend to be jointly served to improve energy effi ciency, since the leakage power of the sensing beam toward a user can be utilized for information transmission [2, 10].

Hybrid-ISAC: This protocol is a combination of Co-ISAC and TDM-ISAC. In this design, multiple targets are grouped based on their locations. Accordingly, Co-ISAC is performed within each group to improve intra-group sensing efficiency while TDM-ISAC is implemented among different groups to avoid inter-group interference. By properly optimizing the target grouping, this hybrid protocol is expected to outperform the Co-ISAC and TDM-ISAC protocols in terms of effi ciency and cost.

The three above protocol designs have advantages and disadvantages, and their relative performance depends on various factors such as the S&C quality-of-service (QoS) requirements, the locations of users/targets, and their mobility [11]. How to optimize the protocol design to enhance the S&C performance needs further investigation.

Joint Resource Allocation, Waveform, and Deployment/Trajectory Design: Unlike conventional terrestrial ISAC systems, in UAV-enabled ISAC systems, optimal resource allocation and waveform design are deeply infl uenced by the UAV deployment/trajectory, since the angular separations between users/targets change with the UAV location. Therefore, to achieve high S&C performance, user association, transmit beamforming, and the UAV trajectory must be jointly designed to maximize communication performance while ensuring the required sensing power and sensing frequency [8]. Solutions to this problem can be generally divided into optimization-based and learning-based methods [5]. However, fi nding the optimal solution to the resulting joint optimization problem is challenging, since the beamforming design and UAV trajectory are closely coupled in multiple nested transcendental functions and integer optimization is required, for example, for user association and target allocation [8]. To tackle this issue, a two-layer penalty-based algorithm was proposed to decompose the involved coupled integer optimization variables for fi nding high-quality solutions [8].

To demonstrate the effectiveness of the algorithm outlined above, the middle subfi gure of Fig. 2 illustrates various UAV trajectory designs and the corresponding achievable communication rates under the TDM-ISAC protocol, for a scenario with four users and four targets. The parameters are set based on practical system requirements and related references [5]. In particular, the number of antennas at the UAV is 16, and the UAV’s maximum horizontal fl ight speed is 30 m/s with a fl ight altitude of 40 m and a flight duration of 40 s. In addition, the channel gain at a reference distance of 1 m and the noise power at each user are set to –30 dB and –70 dBm, respectively. The maximum transmit power is 0.1 W, and the length of the time slots is 0.25 s. In the middle subfi gure of Fig. 2, two benchmarks are considered:

• Straight fl ight (SF): The UAV fl ies from the initial location to the final location along a straight line at a constant speed of 6 m/s. Flight-hover-fl ight (FHF): The UAV fl ies directly at its maximum speed from the initial location to the optimal location, where the UAV can transmit with the maximum achievable rate, hovers at the optimal location for a certain period of time, and then fl ies straight to the fi nal location.

Our proposed scheme for a high (low) required sensing frequency is referred as to Proposed-L (Proposed-H), similar to the benchmark schemes. Here, the high (low) sensing frequency is 0.2 Hz (0.025 Hz). Specifically, the sensing frequency refers to the reciprocal of the interval between two sensing times. It is observed that as the sensing frequency increases, the UAV’s trajectory gradually shrinks from a longer arc toward the users to several turn-back sub-trajectories between the targets and the users. The bottom subfi gure of Fig. 2 unveils a fundamental trade-off between sensing frequency and communication rate in UAV-enabled ISAC systems.

The complexity of the above trajectory design methods may become intractable for long flying periods. In fact, how to design a low-complexity trajectory achieving satisfactory performance is an open problem of high practical interest. A possible solution for this challenge is to partition the whole period into a number of ISAC frames with limited duration. In this manner, for periodic sensing tasks, we can obtain the trajectory for one ISAC frame, based on which the trajectories for the other ISAC frames can be constructed, thereby reducing the algorithmic complexity [8].

![](images/52ffd5f80fe8817c549fb4e4c34d250773868ff4802d52df5b1055cd89f6256c.jpg)  
FIGURE 2. Illustration of ISAC protocols and comparisons of UAV trajectory and achievable rate.

# multI-uAV-enAbled IsAc

In single-UAV-enabled ISAC, the achievable S&C performance may be low for geographically distributed and time-critical tasks, due to the limited sensing range and communication rate of a single UAV. This thus motivates the development of eff ective multi-UAV collaboration schemes to further improve resource effi ciency. Compared to the single-UAV scenario, multi-UAV-enabled ISAC requires mitigation of the potentially severe inter-UAV interference caused by the strong LoS-dominant airground channels. To allow for different levels of cooperation among UAVs, we consider two cases, namely coordinated interference management and cooperative ISAC. Their respective advantages and weaknesses are compared in Table 1.

Coordinated Interference Management: In this case, each UAV serves the users and targets assigned to it, and different UAVs serve different users and targets. The UAVs may cause strong

In single-UAV-enabled ISAC, the achievable S&C performance may be low for geographically distributed and time-critical tasks, due to the limited sensing range and communication rate of a single UAV.

<table><tr><td colspan="2">Classification</td><td>Advantages</td><td>Weaknesses</td></tr><tr><td colspan="2">Single-UAV-enabled ISAC</td><td>Low-cost, less interference</td><td>Small coverage, high latency</td></tr><tr><td rowspan="2">Multi-UAV-enabled ISAC</td><td>Coordinated interference management</td><td>Large coverage, low complexity, less overhead</td><td>Under-utilized echo, strong interference in open space</td></tr><tr><td>Cooperative ISAC</td><td>Multi-directional observation, richer target information, deep coordination, more flexibility</td><td>Large overhead, high complexity, strict time synchronization</td></tr></table>

TABLE 1. Comparison between single-UAV-enabled ISAC and multi-UAV-enabled ISAC.

interference to adjacent unassociated users/targets, thus limiting the S&C range and performance [12]. It is therefore of paramount importance to develop advanced countermeasures for managing such interference. One viable solution is to exploit the mobility of the UAV together with beamforming design and power control for reducing inter-UAV interference. Intuitively, sufficiently separated users/targets (i.e., the users’/targets’ angular separations exceed the angular resolution of the antenna array installed on one UAV), are preferably served simultaneously by different UAVs, especially in poor scattering environments. The main reasons for this are that the interference among UAVs caused by the side lobes of communication beams is greatly reduced due to the low correlation of the user channels and that the received signals reflected from more separated targets are distinguishable by one UAV. Furthermore, obstacles in the surrounding environment can even be utilized for interference reduction through proper deployment/trajectory design. As illustrated in Fig. 1, each UAV tends to hover at an optimized location that has LoS links to its associated users/targets but blocked LoS links to unassociated users/targets, thus enhancing the S&C performance while minimizing the interference. This thus leads to a multi-UAV collaboration gain.

Cooperative ISAC: In cooperative ISAC, multiple UAVs perform distributed radar sensing and coordinated wireless communications with a higher degree of collaboration, thus enabling the combination of distributed MIMO radar and aerial coordinated multi-point (CoMP) transmission/reception compared to coordinated interference management. In this case, UAVs are also allowed to act as dedicated transmitters/receivers and send/receive correlated signals for collaborative S&C. From the sensing perspective, by sharing or fusing the sensing results of different UAVs, larger sensing coverage, more diverse observation angles, and more accurate target parameter estimates are obtained. In addition, the received signals of all UAVs can be collected and fused at a central UAV or at on-ground base stations (BSs), and then the sensing results can be fed back to the different UAVs. Note that, for cooperative ISAC, the overhead required for information exchange is larger than that for coordinated interference management described earlier. Furthermore, for cooperative ISAC, the geometric dilution of precision (GDOP), as an important factor of positional measurement precision [6], needs to be optimized to realize a large distributed MIMO gain. From the communication perspective, by exploiting the benefits of the adjustable distributed antenna array created by multi-UAV systems, high spectrum efficiency can be achieved with the help of CoMP.

It is worth noting that NLoS links are exploitable for communication with the served users, whereas typically only LoS links are exploited for sensing and NLoS links are treated as unfavorable interference. Accordingly, UAVs at higher altitudes and in more open environments are more likely to have strong LoS links to the targets sensed by neighboring UAVs, and thus more reflected signals can be utilized for collaborative sensing; on the contrary, multi-user communications may suffer from more potentially harmful interference and channels with fewer DoFs due to LoS-dominated links. Therefore, UAV deployments with strong LoS links to the intended targets as well as a sufficiently large number of NLoS links to communication users to create high-rank MIMO channels are preferable, leading to a fundamental trade-off between S&C performance. Furthermore, the ground BSs can assist in radar signal processing and interference cancellation for communication signals in multi-UAV-enabled ISAC networks, as shown in Fig. 1. Nonetheless, such distributed multi-static ISAC systems pose several new challenges that need to be addressed, including the high signaling overhead and strict time synchronization requirements. Therefore, more in-depth studies are needed to unveil the most suitable approach for realizing efficient and distributed multi-UAV-enabled ISAC.

# Sensi ng-Assi sted UAV Communi ca ti on

Sensing can provide the capability to see the physical world for future wireless networks, which in turn can potentially enhance their communication performance [13]. For instance, instead of relying on sending pilots to the receivers and feeding back channel estimates to the transmitter (or performing channel estimation at the BS based on the pilots sent by users), tVhe signals reflected by the served ISAC users with sensing and communication requirements can be directly utilized for localization and/or channel estimation. This thus helps to reduce the signaling overhead and yields a performance improvement, which gives rise to a new type of sensing gain. However, it remains an open problem how to quantitatively measure such sensing gain and how to fully exploit it for maximization of the communication performance by optimizing the UAV trajectory and/or beamforming. To find answers to these questions, we consider the UAVto-ground vehicle communication scenario shown in Fig. 3, where the communication performance improvement introduced by sensing is analyzed.

# Sensi ng Gai n

Instead of downlink pilots or uplink feedback, the served ground vehicle’s information, for example, location, velocity, and angle, can be extracted from the reflected ISAC signals for use in beam tracking and beam alignment. To shed some light on the communication performance improvement achieved via sensing, the rate gain realized by ISAC prediction over conventional beam training is analyzed as follows. First, for ISAC prediction, the estimated vehicle location error may lead to beam misalignment, and the corresponding impact on the received communication signal-to-noise ratio (SNR) decreases exponentially with respect to (w.r.t.) the ratio of the angle estimation error l (rad) and the equivalent beamwidth L (rad) [14]. For comparison, for conventional beam training (c.f. the top subfi gure in Fig. 3), the achievable rate of the served user is the product of two terms: the time ratio 1 – a, which accounts for the overhead introduced by the downlink pilots, and the communication rate, which accounts for the SNR loss bt caused by beam misalignment. The communication performance improvement gained with sensing, namely the sensing gain, can thus by characterized as the diff erence between the achievable rate of the proposed ISAC prediction scheme and that of the conventional beam training scheme.

Based on the above discussion, the more (less) accurate the target (channel) estimation, the larger the sensing gain that can be achieved. For LoS-dominated channels, the location estimation error l is generally a function of the fourth power of the link distance between the UAV and the ground vehicle due to the round-trip path loss of the reflected signals, while the SNR loss of conventional beam training schemes depends on the received signal power at the ground vehicle. Thus, the rate gain realized by sensing-assisted communication is expected to decrease as the link distance increases. This is illustrated in Fig. 4, where the end-to-end spectrum effi ciency of conventional beam training and ISAC prediction are plotted for a setup, where the ground vehicle moves along the x-axis and the UAV is hovering at x = 700 m with a fl ight altitude of 80 m and a constant beam width. Figure 4 reveals that a higher sensing gain is achieved when the ground vehicle is closer to the UAV, as the accuracy of ISAC prediction decreases and begins to fluctuate as the echo signal power becomes weaker. As a result, exploiting the UAV’s mobility to shorten the link distance not only reduces the large-scale path loss but also strengthens the performance improvement gained from sensing. We note that joint beamwidth and UAV trajectory design is a promising approach to further improve ISAC performance.

For general multi-UAV scenarios, collaborative sensing potentially leads to signifi cant communication performance improvement but requires sophisticated cooperation schemes. In particular, how to realize effi cient and reliable sensing data exchange and fusion among multiple UAVs for high-quality and seamless communication coverage is an open problem that requires further investigation.

# sensIng-AssIsted beAm trAckIng

How to achieve precise target tracking and a high beamforming gain for communication is also an open problem. Specifically, for long-distance users that can be modeled as point-like objects, the sensing/radar beam should be designed as narrow as possible to accurately point toward its receive antennas, thereby providing both high beamforming gain for communication and excellent angular resolution for sensing. On the other hand, nearby users are not points but rather angularly extended objects, and in this case, a wider beam is preferred to cover the extended object while a narrower beam toward the receiver antennas can realize potentially higher communication performance. One possible approach to achieve an effi cient balance between S&C is to employ a dynamic waveform to adjust the width and center of the ISAC beam in real time according to the relative position of the receive antennas w.r.t. the estimated contour of the object. For example, in the S&C stage, the beamwidth may be designed to cover the entire object to guarantee sensing accuracy with relatively low communication performance [13], while in the communication-only stage, a narrower beam can be adopted to align with the receive antennas based on the prior knowledge of the antennas’ locations. In addition, for users with high mobility, it is advantageous for UAVs to use wide beams to provide reliable and effective target tracking at a possibly large distance to the target, while the communication performance can be improved by adopting narrow beams close to the target. This leads to a fundamental trade-off between communication throughput and sensing reliability for joint beamwidth and UAV trajectory design. Therefore, how to provide reliable beam tracking and enhanced communication performance by exploiting the mobility of UAVs and beamwidth design is a new and practically important problem.

![](images/ee023a83da8a5ca36c2490280f535f2422b39f5c2fbcdaf6e0618fa7389c0acd.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Real location"] --> B["Estimated location"]
    B --> C["ISAC signal"]
    C --> D["Beam training"]
    D --> E["Uplink feedback"]
    E --> F["Beam prediction"]
    F --> G["Data blocks"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#ffc,stroke:#333
    style D fill:#cfc,stroke:#333
    style E fill:#fcc,stroke:#333
    style F fill:#ffc,stroke:#333
    style G fill:#fcc,stroke:#333
```
</details>

FIGURE 3. Sensing-assisted UAV communication.

# sensIng-AssIsted predIctIVe resource AllocAtIon

Although multi-UAV-enabled ISAC is promising for performance and coverage extension, it causes several practical challenges for resource allocation and user scheduling at the network level, such as dynamic load balancing and seamless coverage. For example, in multi-UAV networks, some UAVs may suffer from heavy S&C traffic loads while others may have only light loads, due to the uneven distribution and mobility of the users. This thus seriously degrades the service time and quality due to the limited energy and resources of each UAV. One possible solution is to allow the UAVs to actively/passively monitor the served users’ state (e.g., position and velocity) by analyzing their reflected signals, and then predict their trajectories based on the measured information. Then, these results can be further exploited to optimize the network resource

Although multi-UAVenabled ISAC is promising for performance and coverage extension, it causes several practical challenges for resource allocation and user scheduling at the network level, such as dynamic load balancing and seamless coverage.

One challenging issue related to UAV sensing arises from environmental obstacles, which could either block LoS sensing links or cause clutter interference.

![](images/864a4ff814161987fdcd9f9894db4b4802eae0925e0cc73cce6430c58cadb37f.jpg)

<details>
<summary>line</summary>

| Vehicle location at x-axis (m) | Ideal channel | ISAC prediction | Beam training |
| ------------------------------ | ------------- | --------------- | ------------- |
| 0                              | 4.0           | 2.0             | 3.0           |
| 200                            | 5.5           | 4.5             | 3.5           |
| 400                            | 7.0           | 6.0             | 4.5           |
| 600                            | 9.0           | 8.5             | 6.0           |
| 800                            | 10.5          | 10.0            | 8.0           |
| 1000                           | 9.0           | 8.5             | 6.5           |
| 1200                           | 7.0           | 6.5             | 5.0           |
| 1400                           | 5.0           | 4.0             | 3.0           |
</details>

FIGURE 4. Sensing gain achieved by ISAC prediction over conventional beam training.

![](images/2f4d46b8c84c2a713963b502980c294a738e6f13167cf4dfa772a2c02ff9247c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Auxiliary information"] --> B["Information sharing"]
    B --> C["Target information"]
    C --> D["Offloading"]
    D --> E["Clutter interference"]
    E --> F["3D map"]
    F --> G["Truck"]
    G --> H["Truck"]
    H --> I["Truck"]
    I --> J["Truck"]
    J --> K["Truck"]
    K --> L["Truck"]
    L --> M["Truck"]
    M --> N["Truck"]
    N --> O["Truck"]
    O --> P["Truck"]
    P --> Q["Truck"]
    Q --> R["Truck"]
    R --> S["Truck"]
    S --> T["Truck"]
    T --> U["Truck"]
    U --> V["Truck"]
    V --> W["Truck"]
    W --> X["Truck"]
    X --> Y["Truck"]
    Y --> Z["Truck"]
    Z --> AA["Truck"]
    AA --> AB["Truck"]
    AB --> AC["Truck"]
    AC --> AD["Truck"]
    AD --> AE["Truck"]
    AE --> AF["Truck"]
    AF --> AG["Truck"]
    AG --> AH["Truck"]
    AH --> AI["Truck"]
    AI --> AJ["Truck"]
    AJ --> AK["Truck"]
    AK --> AL["Truck"]
    AL --> AM["Truck"]
    AM --> AN["Truck"]
    AN --> AO["Truck"]
    AO --> AP["Truck"]
    AP --> AQ["Truck"]
    AQ --> AR["Truck"]
    AR --> AS["Truck"]
    AS --> AT["Truck"]
    AT --> AU["Truck"]
    AU --> AV["Truck"]
    AV --> AW["Truck"]
    AW --> AX["Truck"]
    AX --> AY["Truck"]
    AY --> AZ["Truck"]
    AZ --> BA["Truck"]
    BA --> BB["Truck"]
    BB --> BC["Truck"]
    BC --> BD["Truck"]
    BD --> BE["Truck"]
    BE --> BF["Truck"]
    BF --> BG["Truck"]
    BG --> BH["Truck"]
    BH --> BI["Truck"]
    BI --> BJ["Truck"]
    BJ --> BK["Truck"]
    BK --> BL["Truck"]
    BL --> BM["Truck"]
    BM --> BN["Truck"]
    BN --> BO["Truck"]
    BO --> BP["Truck"]
    BP --> BQ["Truck"]
    BQ --> BR["Truck"]
    BR --> BS["Truck"]
    BS --> BT["Truck"]
    BT --> BU["Truck"]
    BU --> BV["Truck"]
    BV --> BW["Truck"]
    BW --> BX["Truck"]
    BX --> BY["Truck"]
    BY --> BZ["Truck"]
    BZ --> CA["Truck"]
    CA --> CB["Truck"]
    CB --> CC["Truck"]
    CC --> CD["Truck"]
    CD --> CE["Truck"]
    CE --> CF["Truck"]
    CF --> CG["Truck"]
    CG --> CH["Truck"]
    CH --> CI["Truck"]
    CI --> CJ["Truck"]
    CJ --> CK["Truck"]
    CK --> CR["Truck"]
    CR --> CS["Truck"]
    CS --> CT["Truck"]
    CT --> CU["Truck"]
    CU --> CV["Truck"]
    CV --> CW["Truck"]
    CW --> CX["Truck"]
    CX --> CY["Truck"]
    CY --> CZ["Truck"]
    CZ --> DA["Truck"]
    DA --> DB["Truck"]
    DB --> DC["Truck"]
    DC --> DD["Truck"]
    DD --> DE["Truck"]
    DE --> DF["Truck"]
    DF --> DG["Truck"]
    DG --> DH["Truck"]
    DH --> DI["Truck"]
    DI --> DJ["Truck"]
    DJ --> DK["Truck"]
    DK --> DL["Truck"]
    DL --> DJ
```
</details>

FIGURE 5. Communication-assisted UAV sensing.

allocation and user scheduling, thus achieving high-quality service by reserving resources and communication data for the users in advance. There are still many open and challenging issues for seamless coverage and connectivity in multi-UAV networks, especially in urban environments with many potential obstructions. Specifically, how to jointly design the dynamic UAV deployment and resource allocation to provide seamless service is a crucial challenge.

# communIcAtIon-AssIsted uAV sensIng

Besides sensing-assisted UAV communication, the communication functionality can also assist sensing to enhance the sensing robustness, effi ciency, and accuracy.

# dAtA oFFloAdIng

As the sensing results are generally needed for subsequent processes, two challenges for UAVs performing sensing tasks in practice are their limited computational capabilities and the low latency requirements for data processing. For example, processing all the received echoes locally at the UAV may be too time-consuming to meet the latency requirements of delay-sensitive ISAC missions, such as target tracking. To tackle this problem, one viable solution is to offload some computationally-intensive sensing tasks (e.g., in form of raw data or processed data) to nearby edge servers (e.g., at ground BSs or a central UAV with powerful computing capabilities), as shown in Fig. 5. By judiciously selecting the computing nodes (e.g., those with strong LoS links to the UAV) and scheduling multi-dimensional resources (e.g., communication resource allocation and computation offloading optimization), ISAC services can be provided more efficiently ensuring better timeliness. However, how to balance the associated energy consumption and transmission/processing latency requires further study. Moreover, due to the potentially large amounts of sensory data and limited link capacity, advanced compression methods may be applied to pre-process the sensing results and reduce the transmission burden. Alternatively, multiple UAVs may form multi-hop links for collaboratively relaying and off loading sensing tasks.

# InFormAtIon shArIng And FusIon

Considering the limited sensing range and performance of a single UAV, another solution to improve the sensing performance is to allow multiple UAVs to share and integrate their information for joint processing. For example, individually estimated information regarding the users’ positions and velocities may be shared among UAVs, and thus the sensing mission assignment can be made more efficient in the next ISAC frame. By sharing the users’ direction of motion and changes in the surrounding environment, a multi-UAV system with maneuverability can collaboratively provide seamless coverage and tracking. In addition, through information sharing, the waste of resources caused by repetitive target detection and excessive target searching is avoided. Furthermore, a UAV or a ground BS can serve as a data center for the collection and fusion of sensing results, thus improving the sensing accuracy and obtaining richer target information. However, information sharing/ exchange also introduces transmission latency and consumes communication resources. Hence, how to design a low-cost and highly-effi cient data sharing/fusion strategy to improve the network sensing performance is an open and challenging issue. Since in practice the communication rates are often severely limited, it may be difficult to meet the stringent sensing latency requirements, especially for wireless data aggregation in swarm UAV scenarios. A promising approach for improving data fusion efficiency is to apply over-the-air computation [9], which exploits the waveform superposition property of wireless channels to realize over-the-air aggregation of data simultaneously transmitted by multiple UAVs, without the need for separate data demodulation and fusion processes.

# 3d mAp AssIstAnce

One challenging issue related to UAV sensing arises from environmental obstacles, which could either block LoS sensing links or cause clutter interference. For example, when a UAV flies to an unknown area to perform an ISAC mission, the UAV-ground channels may be occasionally blocked by high-rise buildings in urban areas, which degrades the S&C performance. To overcome this issue, one possible solution is to employ an environment map constructed based on historical measurements. For example, nearby BSs or edge servers may transmit a stored 3D map of the surrounding environment to the UAV, and based on this map, the states of the links between the UAV and the targets can be predicted. In turn, the map can be further updated based on the current sensing results. However, relying on map information only does not allow to address the dynamics of the environment. To tackle this problem, one viable method is to combine the offline LoS modeling and online sensing information (e.g., positions of the UAV and obstacles) to more accurately determine whether there exists an LoS link between the UAV and a given target location. This enables the UAV to design its real-time trajectory to ensure LoS links to the served users for providing enhanced and reliable ISAC services. Furthermore, it is also possible to extract auxiliary information for sensing based on a 3D environment map, such as the features of the explored/served areas and potential clutter. With such information, the UAV is able to create awareness of the environment around it and reduce/cancel clutter interference for facilitating target sensing, as illustrated in Fig. 5.

# Di recti ons For Future Resea rch

Some open issues and challenges related to the integration of ISAC and UAVs are discussed in the following sections.

# ISAC f or UAVs

ISAC networks can also be utilized to monitor and manage network-connected UAVs, especially UAVs at low altitudes. For network-connected UAVs, ISAC signals emitted by ground BSs can be used for tracking the UAVs and thus enhancing the communication performance through efficient beam prediction. By exploiting the UAVs’ reflected signals, a more reliable cellular connection can be realized by proper resource allocation and trajectory design. However, the strong UAVground LoS links inevitably increase the interference to terrestrial users/BSs [4]. This motivates the development of new techniques for cooperative interference management and cancellation for heterogeneous ISAC networks.

# IRS -Assi sted UAV-Ena bled ISAC

Intelligent reflecting surface (IRS) is a promising technology to reconfigure wireless channels by exploiting smart reflections by massive low-cost reflecting elements. By exploiting an IRS, a virtual LoS link between a UAV and blocked users can be established to enlarge the UAV’s coverage area. This in turn provides higher flexibility for UAV deployment/trajectory design to achieve better S&C performance. Thus, IRS and UAV can synergistically improve S&C performance by proactively jointly altering the wireless communication channel via phase shift and trajectory design, respectively. However, the signaling overhead required for channel estimation is expected to be significant and the joint system design may entail high complexity.

# Secure UAV ISAC

UAV-enabled ISAC systems increase the risk of eavesdropping and jamming attacks due to the LoS-dominated air-ground channels. In addition, unauthorized malicious UAVs pose a new security threat to ground ISAC networks. As such, how to effectively safeguard the legitimate S&C users (e.g., preventing the target location and user information from being eavesdropped) and how to efficiently protect the S&C services (e.g., accurate sensing and reliable communication) against malicious attacks are new and challenging problems to address. Combining information signals with artificial noise is a promising approach for target/ eavesdropper tracking [15], but providing secure ISAC services is still challenging due to the difficulty in determining the locations and channels of the eavesdroppers.

# UAV ISAC Meets Artifi cia l Intelli gence

Artificial intelligence (AI)-based designs are promising options for coping with such highly dynamic scenarios while avoiding the time-consuming iterations of traditional optimization algorithms [15]. By integrating sensing information, such as the states of the environment, into the AI algorithm, future network states can be predicted, which allows UAVs to adjust their actions in an online manner. In turn, ISAC can provide training data for new AI-enabled applications via wireless network sensing. To properly train AI models using ISAC data from distributed UAVs while preserving their privacy, federated learning (FL) can be an efficient solution, where each participating UAV updates its local AI model based on its own local ISAC data, and then sends the updated parameters to a central server for updating the global AI model. However, how to efficiently integrate the training algorithm and the ISAC process is an interesting open problem.

# Conclusi ons

In this article, we have discussed UAV-enabled ISAC to realize an integration gain and facilitate mutual support between S&C. New design considerations and key challenges have been highlighted for UAV-enabled ISAC networks. Coordinated interference management and cooperative ISAC have been proposed for performance improvement in multi-UAV-enabled ISAC networks. Two representative examples for ISAC coordination gains, that is, sensing-assisted UAV communication and communication-assisted UAV sensing, have been presented to demonstrate the complementary nature of S&C. Furthermore, the presented representative simulation results have verified the benefits of the proposed methods. As UAV-enabled ISAC remains largely unexplored, it is hoped that this article will provide a useful initial guide and motivation for future research.

# Acknowledgment

Jie Xu’s work was supported in part by the National Natural Science Foundation of China under grants No. U2001208, 92267202, the Shenzhen Fundamental Research Program under grant No. JCYJ20210324133405015. Wen Chen’s work was supported by National key project 2020YFB1807700. Robert Schober’s work was supported in part by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) GRK 2680 – Project-ID 437847244. A. Lee Swindlehurst’ work was supported by the U.S. National Science Foundation by grant CCF-2225575.

# Ref erences

[1] J. A. Zhang et al., “An Overview of Signal Processing Techniques for Joint Communication and Radar Sensing,” IEEE J. Sel. Top. Signal Process., vol. 15, no. 6, Nov. 2021, pp. 1295–1315.   
[2] F. Liu et al., “Joint Radar and Communication Design: Applications, State-of-the-Art, and the Road Ahead,” IEEE Trans. Commun., vol. 68, no. 6, June 2020, pp. 3834–62.   
[3] J. A. Zhang et al., “Enabling Joint Communication and Radar Sensing in Mobile Networks — A Survey,” IEEE Commun. Surveys Tuts., vol. 24, no. 1, 1st Quart. 2022, pp. 306–45.   
[4] F. Liu et al., “Integrated Sensing and Communications: Towards Dual-Functional Wireless Networks for 6G and Beyond,” IEEE JSAC, vol. 40, no. 6, June 2022, pp. 1728–67.

One challenging issue related to UAV sensing arises from environmental obstacles, which could either block LoS sensing links or cause clutter interference. For example, when a UAV flies to an unknown area to perform an ISAC mission, the UAV-ground channels may be occasionally blocked by high-rise buildings in urban areas, which degrades the S&C performance. To overcome this issue, one possible solution is to employ an environment map constructed based on historical measurements.

[5] Y. Zeng, Q. Wu, and R. Zhang, “Accessing from the Sky: A Tutorial on UAV Communications for 5G and Beyond,” Proc. IEEE, vol. 107, no. 12, Dec. 2019, pp. 2327–75.   
[6] X. Wang et al., “Constrained Utility Maximization in Dual-Functional Radar-Communication Multi-UAV Networks,” IEEE Trans. Commun., vol. 69, no. 4, Apr. 2020, pp. 2660–72.   
[7] A. Liu et al., “A Survey on Fundamental Limits of Integrated Sensing and Communication,” IEEE Commun. Surveys Tuts., vol. 24, no. 2, 2nd Qtr. 2022, pp. 994–1034.   
[8] K. Meng et al., “Throughput Maximization for UAV-Enabled Integrated Periodic Sensing and Communication,” IEEE Trans. Wireless Commun., vol. 22, no. 1, Jan. 2023, pp. 671–87.   
[9] G. Zhu et al., “Over-the-Air Computing for Wireless Data Aggregation in Massive IoT,” IEEE Wireless Commun., vol. 28, no. 4, Aug. 2021, pp. 57–65.   
[10] X. Liu et al., “Joint Transmit Beamforming for Multiuser MIMO Communications and MIMO Radar,” IEEE Trans. Signal Process., vol. 68, 2020, pp. 3929–44.   
[11] M. F. Keskin, H. Wymeersch, and V. Koivunen, “MIMO-OFDM Joint Radar-Communications: Is ICI Friend or Foe?” IEEE J. Sel. Top. Signal Process., vol. 15, no. 6, Nov. 2021, pp. 1393–1408.   
[12] X. Chen et al., “Performance of Joint Sensing-Communication Cooperative Sensing UAV Network,” IEEE Trans. Veh. Technol., vol. 69, no. 12, Dec. 2020, pp. 15,545–56.   
[13] F. Liu et al., “Radar-Assisted Predictive Beamforming for Vehicular Links: Communication Served by Sensing,” IEEE Trans. Wireless Commun., vol. 19, no. 11, Nov. 2020, pp. 7704–19.   
[14] B. Chang et al., “Integrated Scheduling of Sensing, Communication, and Control for mmWave/THz Communications in Cellular Connected UAV Networks,” IEEE JSAC, vol. 40, no. 7, July 2022, pp. 2103–13.   
[15] X. Lu et al., “UAV-Aided Cellular Communications With Deep Reinforcement Learning Against Jamming,” IEEE Wirel. Commun., vol. 27, no. 4, Aug. 2020, pp. 48–53.

# Bi ogra phi es

Kaitao Meng is currently a Post-Doctoral Researcher with the State Key Laboratory of Internet of Things for Smart City, University of Macau, Macau, China. His current research interests include integrated sensing and communication, multi-UAV collaboration, and intelligent reflecting surface.

Qingq ing Wu is currently an Associate Professor with the Department of Electronic Engineering, Shanghai Jiao Tong University, China. He was listed as the Clarivate ESI Highly Cited Researcher since 2021, the Most Influential Scholar Award in AI-2000 by Aminer since 2021, and World’s Top 2% Scientist by Stanford University since 2020.

Jie Xu is currently an Associate Professor with the School of Science and Engineering, The Chinese University of Hong Kong, Shenzhen, China. His research interests include wireless communications, wireless information and power transfer, UAV communications, edge computing and intelligence, and integrated sensing and communication (ISAC). He served or is serving as an Editor of IEEE Trans. Wireless Communications, IEEE Trans. Communications, and IEEE Wireless Commun. Letters.

Wen Chen is a tenured Professor with the Department of Electronic Engineering, Shanghai Jiao Tong University, China, where he is the director of Broadband Access Network Laboratory. He is a fellow of Chinese Institute of Electronics and the distinguished lecturers of IEEE Communications Society and IEEE Vehicular Technology Society. He is the Shanghai Chapter Chair of IEEE Vehicular Technology Society, Editors of IEEE Trans. Wireless Communications, IEEE Trans. Communications, IEEE Access, and IEEE Open J. Vehicular Technology.

Zhiyong Feng is a professor at Beijing University of Posts and Telecommunications (BUPT), and the director of the Key Laboratory of the Universal Wireless Communications, Ministry of Education, P.R.China. Currently, she is serving as Associate Editors-in-Chief for China Communications. Her main research interests include wireless network architecture design and radio resource management in mobile networks, spectrum sensing and dynamic spectrum management in cognitive wireless networks, and integrated sensing and communications.

Rober t Sc hober is an Alexander von Humboldt Professor and the Chair for Digital Communication at Friedrich-Alexander University of Erlangen-Nuremberg (FAU), Germany. His research interests fall into the broad areas of Communication Theory, Wireless and Molecular Communications, and Statistical Signal Processing.

A. Lee Sw indl ehurs t [F] received the B.S. and M.S. degrees in Electrical Engineering from BYU, and the Ph.D. degree in Electrical Engineering from Stanford. He was with the ECE Department at BYU from 1990-2007, then on leave from during 2006-07 working as VP of Research for ArrayComm LLC. Since 2007 he has been a Professor in the EECS Department at UC Irvine. During 2014-17 he was also a Hans Fischer Senior Fellow at the Technical University of Munich. He is an IEEE Fellow, and in 2016 he was elected as a Foreign Member of the Royal Swedish Academy of Engineering Sciences.