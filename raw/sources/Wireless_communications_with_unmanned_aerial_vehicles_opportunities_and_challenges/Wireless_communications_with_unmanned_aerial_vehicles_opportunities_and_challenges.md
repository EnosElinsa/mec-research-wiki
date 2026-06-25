# Wireless Communications with Unmanned Aerial Vehicles: Opportunities and Challenges

Yong Zeng, Rui Zhang, and Teng Joon Lim

The authors provide an overview of UAV-aided wireless communications by introducing the basic networking architecture and main channel characteristics, highlighting the key design considerations as well as the new opportunities to be exploited.

# Abstra ct

Wireless communication systems that include unmanned aerial vehicles promise to provide cost-effective wireless connectivity for devices without infrastructure coverage. Compared to terrestrial communications or those based on high-altitude platforms, on-demand wireless systems with low-altitude UAVs are in general faster to deploy, more flexibly reconfigured, and likely to have better communication channels due to the presence of short-range line-of-sight links. However, the utilization of highly mobile and energy-constrained UAVs for wireless communications also introduces many new challenges. In this article, we provide an overview of UAV-aided wireless communications, by introducing the basic networking architecture and main channel characteristics, highlighting the key design considerations as well as the new opportunities to be exploited.

# Introducti on

With their high mobility and low cost, unmanned aerial vehicles (UAVs), also commonly known as drones or remotely piloted aircrafts, have found a wide range of applications during the past few decades [1]. Historically, UAVs have been primarily used in the military, mainly deployed in hostile territory to reduce pilot losses. With continuous cost reduction and device miniaturization, small UAVs (typically with weight not exceeding 25 kg) are now more easily accessible to the public; hence, numerous new applications in the civilian and commercial domains have emerged, with typical examples including weather monitoring, forest fire detection, traffic control, cargo transport, emergency search and rescue, communication relaying, and others [2]. UAVs can be broadly classified into two categories, fixed wing and rotary wing, each with their own strengths and weaknesses. For example, fixed-wing UAVs usually have high speed and heavy payload, but they must maintain continuous forward motion to remain aloft, and thus are not suitable for stationary applications like close inspection. In contrast, rotary-wing UAVs such as quadcopters, while having limited mobility and payload, are able to move in any direction as well as to stay stationary in the air. Thus, the choice of UAVs critically depends on the applications.

Among the various applications enabled by UAVs, the use of UAVs for achieving highspeed wireless communications is expected to play an important role in future communication systems. In fact, UAV-aided wireless communication offers one promising solution to provide wireless connectivity for devices without infrastructure coverage due to, say, severe shadowing by urban or mountainous terrain, or damage to the communication infrastructure caused by natural disasters [3]. Note that besides UAVs, one alternative solution for wireless connectivity is via high-altitude platforms (HAPs), such as balloons, which usually operate in the stratosphere that is tens of kilometers above the Earth’s surface. HAP-based communications have several advantages over UAV-based low-altitude platforms (LAPs), such as wider coverage and longer endurance. Thus, HAPs are in general preferred for providing reliable wireless coverage for very large geographic areas. On the other hand, compared to HAP-based communications, or those based on terrestrial or satellite systems, wireless communications with low-altitude UAVs (typically at an altitude not exceeding several kilometers) also have several important advantages.

First, on-demand UAV systems are more cost-effective and can be much more swiftly deployed, which makes them especially suitable for unexpected or limited-duration missions. Besides, with the aid of low-altitude UAVs, short-range line-of-sight (LoS) communication links can be established in most scenarios, which potentially leads to significant performance improvement over direct communication between source and destination (if possible) or HAP relaying over long-distance LoS links. In addition, the maneuverability of UAVs offers new opportunities for performance enhancement, through the dynamic adjustment of UAV state to best suit the communication environment. Furthermore, adaptive communications can be jointly designed with UAV mobility control to further improve the communication performance. For example, when a UAV experiences good channels with ground terminals, besides transmitting at higher rates, it can also lower its speed to sustain good wireless connectivity to transmit more data to the ground terminals. These evident benefits make UAV-aided wireless communication a promising integral component of future wireless systems, which need to support more diverse applications with orders-of-magnitude capacity improvement

The authors are with the National University of Singapore.

over current systems. Figure 1 illustrates three typical use cases of UAV-aided wireless communications, which are discussed in the following.

•UAV-aided ubiquitous coverage, where UAVs are deployed to assist the existing communication infrastructure, if any, in providing seamless wireless coverage within the serving area. Two example scenarios are rapid service recovery after partial or complete infrastructure damage due to natural disasters, and base station offloading in extremely crowded areas (e.g., a stadium during a sports event). Note that the latter case has been identified as one of the five key scenarios that need to be effectively addressed by fifth generation (5G) wireless systems [4].

•UAV-aided relaying, where UAVs are deployed to provide wireless connectivity between two or more distant users or user groups without reliable direct communication links. For example, this could be between the frontline and the command center for emergency responses.

•UAV-aided information dissemination and data collection, where UAVs are despatched to disseminate (or collect) delay-tolerant information to (from) a large number of distributed wireless devices. An example is wireless sensors in precision agriculture applications.

Despite the many promising benefits, wireless communications with UAVs are also faced with several new design challenges. First, besides the normal communication links as in terrestrial systems, additional control and non-payload communications (CNPC) links with much more stringent latency and security requirements are needed in UAV systems for supporting safety-critical functions, such as real-time control, and collision and crash avoidance. This calls for more effective resource management and security mechanisms specifically designed for UAV communication systems. Besides, the high mobility environment of UAV systems generally results in highly dynamic network topologies, which are usually sparsely and intermittently connected [5]. As a result, effective multi-UAV coordination, or UAV swarm operations, need to be designed for ensuring reliable network connectivity [6]. At the same time, new communication protocols need to be designed taking into account the possibility of sparse and intermittent network connectivity. Another main challenge stems from the size, weight, and power (SWAP) constraints of UAVs, which could limit their communication, computation, and endurance capabilities. To tackle such issues, energy-aware UAV deployment and operation mechanisms are needed for intelligent energy usage and replenishment. Last but not least, due to the mobility of UAVs as well as the lack of fixed backhual links and centralized control, interference coordination among the neighboring cells with UAV-enabled aerial base stations is more challenging than in terrestrial cellular systems. Thus, effective interference management techniques specifically designed for UAV-aided cellular coverage are needed.

The objective of this article is to give an overview of UAV-aided wireless communications. The basic networking architecture, main channel characteristics and design considerations, as well as the key performance enhancing techniques that exploit the UAV’s mobility, are presented.

![](images/d7f57a38497998dddd05a923bb628a05835b769e681a993f4d7673dc024f6f16.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Overloaded base station"] --> B["Ground gateway"]
    C["Malfunctioning base station"] --> B
    B --> D["Core network"]
    style A fill:#f9f,stroke:#333
    style C fill:#ccf,stroke:#333
    style D fill:#cfc,stroke:#333
```
</details>

![](images/4896084ca1ad0fc20a27cba8d7aeb80c98c42c5b6a6d4a3b54a833ea064ebcfc.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Military Vehicle"] --> B["Mountainous Area"]
    B --> C{Signal Transmission}
    C --> D["Ground Crew"]
    C --> E["Military Team"]
    D --> F["Mountainous Area"]
    E --> G["Mountainous Area"]
    F --> H["Arrow to Airplane"]
    G --> I["Arrow to Ground Team"]
```
</details>

![](images/3f0c959658df51d6eaf42ab57b3dd66e9edfa437c8fa2e4859395378dcda07c3.jpg)

<details>
<summary>text_image</summary>

Diagram illustrating aircraft flight over a field with airplane and ground stations, labeled with aircraft symbols and directional arrow.
</details>

(c)   
Figure 1. Three typical use cases of UAV-aided wireless communications: a) UAV-aided ubiquitous coverage; b) UAV-aided relaying; c) UAV-aided information dissemination and data collection.

# Ba si c Netw orki ng Archi tecture

Figure 2 shows the generic networking architecture of wireless communications with UAVs, which consists of two basic types of communication links: the CNPC link and the data link.

# Control a nd Non-Pa yloa d Communi ca ti ons Li nk

The CNPC links are essential to ensure the safe operation of all UAV systems. Highly reliable, low-latency, and secure two-way communications, usually with low data rate requirements, must be supported by these links for exchanging safety-critical information among UAVs, as well as between the UAV and ground control stations (GCS), such as dedicated mobile terminals mounted on ground vehicles. The main CNPC information flow can be broadly categorized into three types:

• Command and control from GCS to UAVs   
• Aircraft status report from UAVs to ground   
• Sense-and-avoid information among UAVs Even for autonomous UAVs, which are able to accomplish missions relying on onboard computers without real-time human control, CNPC links are also necessary in case emergency human intervention is needed. Not shown in Fig. 2 are the air traffic control (ATC) links, which are necessary only when the UAVs are within a controlled airspace (e.g., near an airport).

Due to the critical functions to be supported, CNPC links should in general operate in protected spectrum. Currently two such bands have been allocated: the L-band (960–977 MHz) and the C-band (5030–5091 MHz) [7]. Furthermore, although the direct links between GCS and UAVs (primary CNPC links) are always preferred for delay reasons, secondary CNPC links via satellite could also be exploited as a backup to enhance reliability and robustness. Another key requirement for CNPC links is superior security. In particular, effective security mechanisms should be employed to avoid the so-called ghost control scenario, a potentially catastrophic situation in which the UAVs are controlled by unauthorized agents via spoofed control or navigation signals. Therefore, powerful authentication techniques, possibly complemented by the emerging physical layer security techniques, should be applied for CNPC links.

![](images/3c3249721cc00ced1222df45dec592ec3844b4ed8fb2f34295a2dfc0113d46a8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    Satellite -->|Primary CNPC Link| UAV1
    Satellite -->|Secondary CNPC Link| UAV2
    Satellite -->|Data Link| UAV3
    UAV1 <--> UAV2
    UAV1 <--> Ground control station
    UAV2 <--> Ground terminals
    UAV2 <--> UAV3
    UAV3 <--> Ground terminals
```
</details>

Figure 2. Basic networking architecture of UAV-aided wireless communications.

# Da ta Li nk

The data links, on the other hand, aim to support mission-related communications for the ground terminals, which, depending on the application scenarios, may include terrestrial base stations (BSs), mobile terminals, gateway nodes, wireless sensors, and so on. Taking the UAV-aided ubiquitous coverage shown in Fig. 1a as an example, the data links maintained by the UAVs need to support the following communication modes:

• Direct mobile-UAV communication as for BS offloading or during complete BS malfunction   
• UAV-BS and UAV-gateway wireless backhaul   
• UAV-UAV wireless backhaul

The capacity requirement for these data links critically depends on the applications, possibly ranging from several kilobits per second in UAV-sensor links to dozens of gigabits per second in UAV-gateway wireless backhaul. Compared to CNPC links, the data links usually have higher tolerance in terms of latency and security requirements. In terms of spectrum, the UAV data links could reuse the existing band that has been assigned for the particular applications to be supported, (e.g., the LTE band while assisting cellular coverage), or dedicated new spectrum could be allocated for enhanced performance (e.g., using millimeter-wave, mmWave, band for high capacity UAV-UAV wireless backhaul) [8].

# Cha nnel Cha ra cteri sti cs

Both CNPC and data links in UAV-aided communications consist of two types of channels, UAV-ground and UAV-UAV channels, which exhibit several unique characteristics as compared to the extensively studied terrestrial communication channels.

# UAV-Ground Cha nnel

While the air-ground channels for aeronautical applications with piloted aircrafts are well understood, systematic measurements and modeling of UAV-ground channels are still ongoing [7, 9]. Unlike piloted aircraft systems, where the ground sites are usually in open areas with tall antenna towers, the UAV-ground channels for UAV systems are more complicated due to the more complex operation environment. While LoS links are expected for such channels in most scenarios, they could also be occasionally blocked by obstacles such as terrain, buildings, or the airframe itself. In particular, recent measurements have shown that UAV-ground channels could suffer from severe airframe shadowing with a duration up to dozens of seconds during aircraft maneuvering [9], which needs to be taken into account for mission-critical operations. For low-altitude UAVs, the UAV-ground channels may also constitute a number of multi-path components due to reflection, scattering, and diffraction by mountains, ground surface, foliage, and so on. For UAVs operating over desert or sea, the two-ray model has mostly been used due to the dominance of the LoS and surface reflection components. Another widely used model is the stochastic Rician fading model, which consists of a deterministic LoS component, and a random scattered component with certain statistical distributions. Depending on the environment surrounding the ground terminals as well as the frequency used, the UAV-ground channels exhibit widely varying Rician factors (i.e., the power ratio between the LoS and the scattered components), with typical values around 15 dB for L-band and 28 dB for C-band in hilly terrain [7].

# UAV-UAV Cha nnel

The UAV-UAV channels are mainly dominated by the LoS component. Although there may be limited multipath fading due to ground reflections, its impact is minimal compared to that experienced in UAV-ground or ground-ground channels. In addition, the UAV-UAV channels may have even higher Doppler frequencies than the UAV-ground counterparts, due to the potentially large relative velocity between UAVs. Such channel characteristics have direct implications on spectrum allocation for UAV-UAV links. On one hand, the dominance of LoS links may suggest that the emerging mmWave communications could be employed to achieve high-capacity UAV-UAV wireless backhaul. On the other hand, the high relative velocity between UAVs coupled with the higher frequency in the mmWave band could lead to excessive Doppler shift. More in-depth studies are needed to find out the most suitable technology to use in UAV-UAV links, given their unique channel characteristics.

# mAIn desIgn consIderAtIons

This section presents the main design considerations specifically for wireless communications with UAVs. The following three aspects are discussed: UAV path planning, energy-aware deployment and operation, and multiple-input multiple-output (MIMO) communications in UAV systems.

# uAV dePloyment And PAth PlAnnIng

One important design aspect of UAV systems is path planning [10, 11]. For UAV-aided communications in particular, appropriate path planning may signifi cantly shorten the communication distance and thus is crucial for high-capacity performance. Unfortunately, fi nding the optimal fl ying path for UAV is a challenging task in general. On one hand, UAV path optimization problems essentially involve an infinite number of variables due to the continuous UAV trajectory to be determined. On the other hand, the problems are also usually subject to a variety of practical constraints (e.g., connectivity, fuel limitation, collision, and terrain avoidance), many of which are time-varying in nature and are diffi cult to model accurately. One useful method for UAV path planning is to approximate the UAV dynamics by a discrete-time state space, with the state vector typically consisting of the position and velocity in a three-dimensional (3D) coordinate system. The UAV trajectory is then given by the sequence of states, which are subject to finite transition constraints to reflect the practical UAV mobility limitations. Many of the resulting problems with such an approximation belong to the class of mixed integer linear programming (MILP) [11], which can be solved with well developed software packages.

Intuitively, the optimal UAV fl ight path critically depends on the application scenarios. For instance, for UAV-aided cellular coverage in Fig. 1a, it is evident that more than one UAVs should be jointly deployed above the serving areas to cooperatively achieve real-time communications with ground users; whereas for UAV-aided information dissemination or collection for delay-tolerant data, as shown in Fig. 1c, it could be sufficient to dispatch one single UAV to fly over the area to communicate with the ground nodes sequentially. Furthermore, for the cellular coverage application, one option is to employ rotary-wing UAVs that hover above the coverage area, serving as static aerial base stations. In this case, no dedicated path planning is needed. Instead, the main design problems for UAV deployment usually involve finding the optimal UAV separations as well as their hovering altitude to achieve maximum coverage. Note that for a typical urban environment, in general there is an optimal UAV altitude in terms of coverage maximization, which is due to the following nontrivial trade-off: While increasing UAV altitude will lead to higher free space path loss, it also increases the possibility of having LoS links with the ground terminals. Such a trade-off has been characterized in [12, 13], based on which the optimal UAV altitude has been obtained.

# energy-AWAre dePloyment And oPerAtIon

The performance and operational duration of a UAV system is fundamentally constrained by the limited onboard energy. Although power plant and energy storage technologies have advanced dramatically over the past few decades, limited energy availability still severely hampers UAV endurance. From the operational perspective, this problem can be addressed through two approaches. First, effective energy-aware deployment mechanisms are needed for timely onboard energy replenishment, but without noticeable interruption of the communication services supported. Second, energy-effi cient operation through smart energy management is required, that is, accomplishing missions with minimum energy consumption.

In terms of energy-aware deployment, one effective approach is to exploit inter-UAV cooperation to enable sequential energy replenishment. For instance, at any one time, only one UAV is scheduled to leave the serving area for energy replenishment, during which the service gap is temporarily filled by neighboring UAVs, for example, via increasing the transmission power and/or adjusting the aircraft positions. This energy replenishment scheduling can be matched to the dynamic load patterns that need to be supported by the UAVs. For instance, it might be preferred to schedule energy replenishment only when low data traffi c is expected (e.g., at night) for the cellular coverage application. Note that apart from commonly used energy sources such as electric batteries or liquid fuels, there has been increasing interest in powering UAVs by solar energy or dedicated wireless energy transfer technology (e.g., via laser beams).1

Energy-effi cient operation, on the other hand, aims to reduce unnecessary energy consumption by the UAVs. As the main energy usage of UAVs in wireless applications is to support either aircraft propulsion or wireless communications, energy-efficient operation schemes can be broadly classified into two categories. The first one is energy-efficient mobility, for which the movement of the UAVs should be carefully controlled by taking into account the energy consumption associated with every maneuver. For instance, unnecessary aircraft maneuvering or ascending should be avoided since they are generally quite energy-intensive. Energy-effi cient mobility schemes can usually be designed with path planning optimization, by using appropriate energy consumption models as a function of UAV speed, acceleration, altitude, and so on. The other category of energy-effi cient operation is energy-effi cient communication, which aims to satisfy the communication requirement with the minimum energy expenditure on communication-related functions, such as communication circuits, signal transmission, etc. To this end, one common approach is to optimize the communication strategies to maximize the energy efficiency (EE) in bits per Joule (i.e., the number of successfully communicated data bits per unit of energy consumption). Note that while energy-ef-

The performance and operational duration of a UAV system is fundamentally constrained by the limited onboard energy. Although power plant and energy storage technologies have advanced dramatically over the past few decades, limited energy availability still severely hampers UAV endurance.

ficient communication has been extensively studied for terrestrial communications, its systematic investigation for UAV communication systems is still underdeveloped.

# MIMO for UAV-Ai ded Communi ca ti ons

Although MIMO technology has been extensively implemented in terrestrial communication systems due to its high spectral efficiency and superior diversity performance, its application in UAV systems is still hindered by several factors. First, the lack of rich scattering in the UAV environment considerably limits the spatial multiplexing gain of MIMO, which usually leads to only marginal rate improvement over single-antenna systems. Besides, the high signal processing complexity as well as the hardware and power consumption costs make it quite costly to employ multiple antennas in UAVs due to the SWAP limitations. Furthermore, MIMO systems rely on accurate channel state information (CSI) for best performance. However, this is practically difficult to achieve in a highly dynamic environment, and therefore further limits the practical MIMO gain in UAV systems.

Despite the above challenges, some recent results still show great potential for MIMO technology in UAV systems. In particular, in contrast to the common conception that spatial multiplexing gain is fundamentally limited by the number of signal paths, it has been found that high spatial multiplexing gain may also be attainable even in LoS channels, by carefully designing the antenna separation with respect to carrier wavelength and link distance [14], although this usually requires large antenna separation, high carrier frequency, and short communication range. Alternatively, a more practical way to reap the multiplexing gain in poor scattering environment is to leverage multi-user MIMO, by simultaneously serving a number of sufficiently separated ground terminals with angular separations exceeding the angular resolution of the antenna array installed on the UAVs. In this case, the signals for different terminals are distinguishable by the UAV array, and thus restores the MIMO spatial multiplexing gain. Another way of utilizing MIMO in UAV systems is through mmWave communications, for which the MIMO array gain, instead of the spatial multiplexing gain, is more critical due to the large available bandwidth as well as the high signal attenuation. However, due to the high mobility of UAVs, it would be quite challenging to achieve transmitter/receiver beam alignment for directional mmWave communications, an issue that needs to be properly addressed before mmWave MIMO could be practically employed in UAV systems.

![](images/8a765f7c83ee0d7fdb725585e64f8c870a5e2cdf06b6311ab7012b023877cc78.jpg)

<details>
<summary>line</summary>

| Time (s) | Static | Mobile, v=40 m/s | Mobile, v=70 m/s | Mobile, v=100 m/s |
|----------|--------|------------------|------------------|-------------------|
| 0        | 100    | 100              | 100              | 100               |
| 5        | 100    | 96               | 92               | 86                |
| 10       | 100    | 90               | 88               | 86                |
| 15       | 100    | 96               | 92               | 86                |
| 20       | 100    | 101              | 101              | 101               |
| 25       | 100    | 96               | 92               | 86                |
| 30       | 100    | 90               | 88               | 86                |
| 35       | 100    | 96               | 92               | 86                |
| 40       | 100    | 101              | 101              | 101               |
</details>

Figure 3. UAV-enabled mobile relaying and the corresponding path loss of the communication links: a) a schematic of the UAV-enabled mobile relaying; b) path loss with static vs. mobile relaying.

# Communi ca ti ons wi th UAV Controlled Mobi li ty

The high mobility of UAVs offers unique opportunities for performance improvement in UAV-aided communications. In this section, we discuss two key techniques for wireless communications with UAV controlled mobility, which are UAV-enabled mobile relaying and deviceto-device (D2D)-enhanced UAV information dissemination.

# UAV-Ena bled Mobi le Rela yi ng

Relaying is an extensively studied technique in terrestrial communication systems for throughput/reliability improvement as well as range extension. Due to the practical constraints such as limited mobility and wired backhauls, most relays in terrestrial systems are deployed in fixed locations, which we refer to as static relaying. To further exploit UAV controlled mobility, we present in this subsection a UAV-enabled mobile relaying strategy, which works particularly well for delay-tolerant applications.

With mobile relaying, the UAV flies continuously between the source and destination aiming to reduce the link distances during both UAV information reception and relaying phases. For example, with half-duplex decodeand-forward (DF) mobile relaying, each relaying cycle consists of two phases each with duration δ s, where δ is determined by the maximum tolerable delay. As illustrated in Fig. 3a, the first phase corresponds to UAV information reception, where it keeps receiving and decoding the information sent from the source and stores in its data buffer. Concurrently, starting from the initial position at the middle point between the source and destination, the UAV first flies toward the source at maximum possible speed v, and then flies back promptly so that it returns to the initial position at the end of the first phase (t = δ). Note that if v and/or δ is sufficiently large, the UAV will have time to hover above the source before returning so as to enjoy the best channel for data reception. In the second phase starting from $t = \delta .$ the UAV sends the data in its buffer to the destination. This is accompanied by symmetric UAV movement, where it first flies toward the destination, hovers above the nearest location to the destination if time allows, and then returns to the initial position at the end of the cycle $\left( t = 2 8 \right)$ ). It is evident that compared to static relaying with the fixed UAV location at the same initial position, the proposed mobile relaying strategy always enjoys a shorter link distance (or better average channel) in each of the two phases of information reception and relaying. This is illustrated in Fig. 3b with δ = 20 s under different UAV velocity and a constant flying altitude $H = 1 0 0 \textrm { m }$ . The carrier frequency is 5 GHz, and the source and destination are assumed to be separated by R = 1 km. It is observed from Fig. 3b that with higher UAV speed, mobile relaying enjoys larger link gains (or less path loss) than static relaying. In particular, for sufficiently large UAV speed (e.g., v = 100 m/s), the UAV would be able to stay stationary above the source and destination each for about 10 s, during which the path loss remains at a constant value that is about 14 dB lower than that of the static relaying.

By employing adaptive rate transmission, the proposed mobile relaying strategy can achieve significant throughput improvement over conventional static relaying. This is illustrated in Fig. 4, where the end-to-end spectrum efficiency in bits per second per Hertz is plotted against the maximum tolerable delay δ for different UAV velocity. Both the source and the UAV are assumed to transmit with a constant power P, with P setting to a value so that the average received signal-to-noise ratio (SNR) at the UAV for the static relaying is 10 dB. Note that the direct link between source and destination is assumed to be blocked and thus ignored. For simplicity, we assume that the Doppler effect due to the UAV’s mobility has been well compensated at the receivers. It is observed that for sufficiently high delay tolerance δ, the mobile relaying strategy achieves a throughput more than twice that by static relaying. Furthermore, for any fixed δ, larger throughput is achieved for higher UAV velocity, which is as expected.

Note that an alternative strategy of mobile relaying is known as data ferrying or load-carry-and-delivery [5]. With this strategy, the UAV “loads” the data from the source as it reaches the nearest possible location from the source, flies toward the destination with the loaded data until it reaches the nearest possible location to the destination, and then delivers the data to the destination. As data ferrying has less communication time than the proposed mobile relaying, its achievable throughput is expected to be smaller, especially for cases with low UAV speed and/ or stringent delay requirement. Furthermore, in the above discussions, a data buffer with sufficiently large buffer size is assumed at the UAV. In general, there is a trade-off between onboard buffer size and achievable throughput in the mobile relaying design.

![](images/eb0c0f740e403f76a79a01f7a2a63d0acc5cd182dc0304ee44bbbffc986fe188.jpg)

<details>
<summary>line</summary>

| Maximum tolerable delay δ (s) | Static | Mobile, ν = 40 m/s | Mobile, ν = 70 m/s | Mobile, ν = 100 m/s |
| ----------------------------- | ------ | ------------------ | ------------------ | ------------------- |
| 0                             | 1.7    | 1.7                | 1.7                | 1.7                 |
| 20                            | 1.7    | 2.5                | 3.0                | 3.5                 |
| 40                            | 1.7    | 3.0                | 3.5                | 3.7                 |
| 60                            | 1.7    | 3.5                | 3.7                | 3.8                 |
| 80                            | 1.7    | 3.6                | 3.8                | 3.85                |
| 100                           | 1.7    | 3.7                | 3.85               | 3.9                 |
</details>

Figure 4. Spectrum efficiency vs. maximum tolerable delay with mobile vs. static relaying.

# D2D-Enha nced UAV Informa ti on Di ssemi na ti on

D2D communication is an effective technique for capacity improvement in terrestrial communication systems [15]. The main idea is to offload the BS by enabling direct communications between nearby mobile terminals. For UAV-aided communication systems, D2D communication is expected to play an important role by providing additional benefits such as UAV energy saving and lower capacity requirement for UAV wireless backhaul. Many existing D2D techniques for terrestrial communication systems, such as those on interference mitigation and spectrum sharing, can be directly applied in UAV-aided communications, especially in the scenario to support ubiquitous cellular coverage as shown in Fig. 1a. On the other hand, new D2D communication techniques could be devised by exploiting the unique characteristics of UAV-aided communications. In the following, we present one such technique, D2D-enhanced UAV information dissemination, which aims to achieve efficient information dissemination to a large number of ground nodes by exploiting both D2D communications and the UAV mobility.

As illustrated in Fig. 1c, we consider the scenario where one UAV flies over a certain area to distribute a common file to a large number of ground nodes. One simple approach to achieve this is by letting the UAV repeatedly transmit the same file as it flies over different ground nodes until all of them successfully receive the file. It is not difficult to see that such a scheme requires substantial UAV retransmissions, and its performance is essentially limited by the ground terminals that experience the weakest channel conditions with the UAV. The D2D-enhanced information dissemination scheme can effectively solve this problem with a two-phase protocol, as illustrated in Fig. 5. In the first phase, the UAV broadcasts the appropriately coded file to the ground nodes as it flies over them. Since each node has only limited wireless connectivity with the UAV, it is very likely that it can only successfully receive a fraction of the file, where different portions of the file are received by different nodes. In the second phase, the ground nodes exchange their respectively received data via D2D communications, until all the nodes receive a sufficient number of packets to successfully decode the file. This scheme significantly reduces the number of UAV retransmissions, and as a result the total flying time of the UAV, which saves its energy and is particularly useful for small UAVs with limited onboard energy. Notice that if the ground nodes are distributed over a wide geographical area, efficient node clustering algorithms can be applied to improve the file sharing performance by enabling short-range D2D communications only within each cluster. The joint optimization of the UAV path planning, coding, node clustering, as well as D2D file sharing for this scenario is an important problem for future research.

![](images/f15f0d2b765cdd87aa0c2b7f86c315d9ca52ed66cf55b9d500571620791a2a67.jpg)

<details>
<summary>text_image</summary>

Phase I: UAV information broadcasting
Phase II: D2D file sharing
</details>

Figure 5. The two-phase protocol of D2D-enhanced UAV information dissemination.

# Conclusi ons

In this article, we have provided an overview on UAV-aided wireless communications with the help of three use cases: UAV-aided ubiquitous coverage, UAV-aided relaying, and UAV-aided information dissemination. The basic networking architecture and main channel characteristics have been introduced. Furthermore, the key design considerations for UAV communications have also been discussed. Lastly, we have highlighted two key performance enhancing techniques by utilizing UAV controlled mobility, including UAV-enabled mobile relaying and D2D-enhanced UAV information dissemination. It is hoped that the challenges and opportunities described in this article will help pave the way for researchers to design and build UAV-enhanced wireless communication systems in the future.

# References

[1] K. P. Valavanis and G. J. Vachtsevanos, Handbook of Unmanned Aerial Vehicles, Springer Netherlands, 2015.

[2] US Department of Transportation, “Unmanned Aircraft System (UAS) Service Demand 2015–2035: Literature Review & Projections of Future Usage,” tech. rep., v.0.1, DOT-VNTSC-DoD-13-01, Sept. 2013.   
[3] A. Merwaday and I. Guvenc, “UAV Assisted Heterogeneous Networks for Public Safety Communications,” Proc. IEEE Wireless Commun. Net. Conf., 9–12 Mar. 2015, pp. 329–34.   
[4] A. Osseiran et al., “Scenarios for 5G Mobile and Wireless Communications: the Vision of the METIS Project,” IEEE Commun. Mag., vol. 52, no. 5, May 2014, pp. 26–35.   
[5] E. W. Frew and T. X. Brown, “Airborne Communication Networks for Small Unmanned Aircraft Systems,” Proc. IEEE, vol. 96, no. 12, Dec. 2008, pp. 2008–27.   
[6] N. Goddemeier, K. Daniel, and C. Wietfeld, “Role-Based Connectivity Management with Realistic Air-to-Ground Channels for Cooperative UAVs,” IEEE JSAC, vol. 30, no. 5, June 2012, pp. 951–63.   
[7] D. W. Matolak and R. Sun, “Unmanned Aircraft Systems: Air-Ground Channel Characterization for Future Applications,” IEEE Vehic. Tech. Mag., vol. 10, no. 2, June 2015, pp. 79–85.   
[8] T. S. Rappaport et al., Millimeter Wave Wireless Communications, Prentice Hall, 2014.   
[9] R. Sun and D. W. Matolak, “Initial Results for Airframe Shadowing in L- and C-Band Air-Ground Channels,” Proc. Integrated Commun., Navigation, and Surveillance Conf., Apr. 2015, pp. 1–8.   
[10] Z. Han, A. L. Swindlehurst, and K. J. R. Liu, “Optimization of MANET Connectivity via Smart Deployment/Movement of Unmanned Air Vehicles,” IEEE Trans. Vehic. Tech., vol. 58, no. 7, Sept. 2009, pp. 3533–46   
[11] T. Schouwenaars et al., “Mixed Integer Programming for Multi-Vehicle Path Planning,” Proc. Euro. Control Conf., 2001., pp. 2603–08.   
[12] A. Al-Hourani, S. Kandeepan, and S. Lardner, “Optimal LAP Altitude for Maximum Coverage,” IEEE Wireless Commun. Lett., vol. 3, no. 6, Dec. 2014, pp. 569–72.   
[13] M. Mozaffari et al., “Drone Small Cells in the Clouds: Design, Deployment and Performance Analysis,” Proc. IEEE GLOBECOM, San Diego, CA, Dec. 2015.   
[14] F. Bohagen, P. Orten, and G. E. Oien, “Design of Optimal High-Rank Line-of-Sight MIMO Channels,” IEEE Trans. Wireless Commun., vol. 6, no. 4, Apr. 2007, pp. 1420–25.   
[15] A. Asadi, Q. Wang, and V. Mancuso, “A Survey on Device-to-Device Communication in Cellular Networks,” IEEE Commun. Surveys & Tutorials, vol. 16, no. 4, Apr. 2014, pp. 1801–19.

# Bi ograp hi es

Yong Zeng [S’12, M’14] (elezeng@nus.edu.sg) received his B.Eng. (First-Class Hons.) and Ph.D. degrees in electrical and electronic engineering from Nanyang Technological University, Singapore, in 2009 and 2014, respectively. Since September 2013, he has been working as a research fellow at the Department of Electrical and Computer Engineering, National University of Singapore. His research interests include MIMO transceiver optimization for interfering systems, wireless power transfer, massive MIMO, millimeter-wave, and other 5G related topics.

Rui Zhang [S’00, M’07, SM’15] (elezhang@nus.edu.sg) received his Ph.D. degree from Stanford University in 2007. He is now an associate professor with the Electrical and Communications Engineering Department of the National University of Singapore. His current research interests include energy-efficient and energy-harvesting-enabled wireless communications, wireless information and power transfer, and 5G wireless systems. He was the recipient of the 6th IEEE ComSoc Asia-Pacific Region Best Young Researcher Award in 2011, and co-recipient of the IEEE Marconi Prize Paper Award in Wireless Communications in 2015. He is now an Editor for IEEE Transactions on Wireless Communications, IEEE Transactions on Signal Processing, and IEEE Journal on Selected Areas in Communications. He was selected as a Thomson Reuters Highly Cited Researcher in 2015.

Teng Joon Lim [S’92, M’95, SM’02] (eleltj@nus.edu.sg) obtained his B.Eng. from the National University of Singapore in 1992 and his Ph.D. from the University of Cambridge in 1995. He was with the Centre for Wireless Communications in Singapore from 1995 to 2000 and the University of Toronto from 2000 to 2011, and has been with the National University of Singapore since June 2011, where he is a professor and Vice Dean of Graduate Programmes in the Faculty of Engineering. He is an Area Editor of IEEE Transactions on Wireless Communications and an Editor of IEEE Wireless Communications Letters.