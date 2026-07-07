# Communication and Control in Collaborative UAVs: Recent Advances and Future Trends

Shumaila Javaid, Nasir Saeed , Senior Member, IEEE, Zakria Qadir , Graduate Student Member, IEEE, Hamza Fahim , Bin He , Member, IEEE, Houbing Song , Fellow, IEEE, and Muhammad Bilal , Senior Member, IEEE

Abstract— The recent progress in unmanned aerial vehicles (UAV) technology has significantly advanced UAV-based applications for military, civil, and commercial domains. Nevertheless, the challenges of establishing high-speed communication links, flexible control strategies, and developing efficient collaborative decision-making algorithms for a swarm of UAVs limit their autonomy, robustness, and reliability. Thus, a growing focus has been witnessed on collaborative communication to allow a swarm of UAVs to coordinate and communicate autonomously for the cooperative completion of tasks in a short time with improved efficiency and reliability. This work presents a comprehensive review of collaborative communication in a multi-UAV system. We thoroughly discuss the characteristics of intelligent UAVs and their communication and control requirements for autonomous collaboration and coordination. Moreover, we review various UAV collaboration tasks, summarize the applications of UAV swarm networks for dense urban environments and present the use case scenarios to highlight the current developments of UAV-based applications in various domains. Finally, we identify several exciting future research direction that needs attention for advancing the research in collaborative UAVs.

Index Terms— Unmanned aerial vehicle (UAV), swarm, autonomous, communication, collaboration, control.

Manuscript received 28 August 2022; revised 5 January 2023; accepted 20 February 2023. Date of publication 20 March 2023; date of current version 31 May 2023. This work was supported in part by the National Key Research and Development Program of China under Grant 2020AAA0108905; in part by the National Natural Science Foundation of China under Grant 61825303 and Grant 62088101; in part by the Shanghai Municipal Commission of Science and Technology Project under Grant 19511132101; and in part by the Shanghai Municipal Science and Technology Major Project under Grant 2021SHZDZX0100. The Associate Editor for this article was L. Wang. (Corresponding authors: Nasir Saeed; Muhammad Bilal.)

Digital Object Identifier 10.1109/TITS.2023.3248841

## I. INTRODUCTION

controlled speed and height to carry out designated tasks gained significant recognition in military operations for longterm surveillance, decoys, and missile launches against fixed targets [1], [2], [3], [4]. Nevertheless, recently the tremendous potential of UAVs also surged their exploration for various civilian applications, including transportation, recuse, disaster relief, wireless recovery, and agriculture [5], [6], [7]. Most of these UAV-based applications require a swarm of UAVs rather than a single UAV to work together to perform independent operations to complete tasks. However, in a multi-UAV system, the lack of proper UAV-to-UAV communication architecture influences their performance in a distributed environment. The multi-UAV communication network architecture allows UAVs to perform different tasks collaboratively by sharing information and responsibilities. Furthermore, collaborative UAV communication enables fast operations with more reliability and robustness; for instance, if a specific UAV fails to perform some task due to failure, other UAVs can continue to complete the job [8], [9]. Therefore, inspired by the great prospective of collaborative UAV communication, scientific and research communities focused on investigating the possibilities and limitations of achieving collaborative UAV communication [10], [11], [12].

State-of-the-art literature has presented various collaborative communication schemes for UAV swarm networks in different domains to optimize service time, energy efficiency, coverage and communication performance. For example, in the context of UAV-based collaborative beamforming [13], UAVs can realize collaborative beamforming for establishing a virtual antenna array to generate a beam pattern with a sharp main lobe and low sidelobe levels to enhance the antenna gain, reduce interference and improve the signal-to-noise ratio of the received signal and focused transmitted signal [14]. Similarly, in collaborative multiple-target tracking [15], the natural characteristics of flexible mobility of UAVs can play a significant role in sensing and tracking mobile targets at a large scale, leading to advanced disaster monitoring, damage assessment, manufacturing safety, and border security [16], [17]. At the same time, collaborative UAV routing also offers efficient ways for tasks offloading in a distributed manner, such as localization, actuation-based task assignments and optimal path selection from source to destination for different product delivery and disaster relief applications [18], [19]. However, a few primary constraints include lack of physical infrastructure, high mobility, channel characterization, intermittent connectivity, bounded transmission range, and limited resources [10], [20] are hindering the development of collaborative UAV swarm architecture.

Accordingly, existing studies address the aforementioned issues by focusing on different solutions, including channel characterization, resource management, data communication, and emerging technologies integration (such as 5G and 6G) to enable fast and reliable collaborative UAV communications. For example, in [21], Li et al. highlighted the advancement of 5G-assisted UAV communication for achieving high reliability, fast speed, rapid recovery, flexibility, and cost-effective traffic offloading in highly crowded areas. In another work [22], authors identified the limitations of UAV communication (such as Line of Sight (LoS) dominant UAV-ground channel, high Quality of Service (QoS) requirements, and inadequate power, size and weight constraints) that can be addressed using 5G and beyond 5G technology. A few recent studies [1], [2], [23], [24], [25], investigated the 5G millimeter-wave communication and the scope of 5G aided UAV communication for channel characterization, standardization, collision avoidance, energy efficiency, and optimal trajectory design.

## A. Related Surveys

Due to emerging applications of UAVs, various surveys in the literature cover different aspects of UAVs. For instance, In [25], a detailed review of communication networks and routing protocols are presented that highlight their contribution to improve the reliability, data delivery, and resource optimization of UAV networks. Authors in [24] investigated the potential of UAVs for enhancing the performance of wireless networks in terms of coverage, energy efficiency, capacity, and reliability. In another survey [26], Khuwaja et al. reviewed the channel characterization models for UAV communication and discussed various methods that improve the shadowing and propagation effects. In [27] channel fading effects and measurements are thoroughly studied for link budget analysis and reduced link losses. Authors in [28] highlighted several communication issues such as network setup, link failure, and energy challenges to enable UAV communication. Fotouhi et al. in [29] focused on the integration of UAV systems with cellular networks for standardization and advancements of UAV systems.

Furthermore, various state-of-the-art surveys have summarized the primary contributions of existing solutions for achieving collaborative communication. For example, in [30], authors review wireless sensor network (WSN) and UAV collaboration for sensor nodes deployment, localization, and UAV’s path formation for data collection to enable efficient monitoring in different domains such as agriculture field, environment and disaster area management. The authors explicitly reviewed UAV-WSN architecture for efficient monitoring while lacking focus on UAV-to-UAV collaborative communication for task completion. In another work [10], chmaj et al. presented an overview of different distributed operations such as object tracking, path planning, navigation, monitoring and data manipulation that a swarm of UAVs can perform. However, the authors did not include a comprehensive discussion on collaborative communication architecture and mechanisms for performing distributed operations. Nawaz et al. in [31] discussed the characteristics of a UAV network compared to WSN and mobile ad-hoc networks and summarized the network issues (such as routing, power and quality of service) that need to be addressed for collaborative UAV networks. However, the presented review did not discuss the UAV’s collaborative tasks in detail. In another work [20], authors comprehensively studied the UAV communication links (such as UAV-to-UAV and UAV-to-infrastructure) to identify the requirements of UAV-based communication systems. However, the detailed review of the networking architectures and communication framework did not include the UAV collaboration for joint control and task completion. In [32], authors studied the UAV’s role in achieving green Internet of Things (IoT) to realize a sustainable smart world. The survey summarizes strategies to integrate UAVs with IoT as edge intelligence devices to collect and process data obtained from IoT devices. The review also explores the opportunities for connectivity and communication beyond 5G. However, it did not include UAV-to-UAV communication for collaborative control and task performance. In another work [33], Shi et al. in reviewed the existing UAV communication protocols for power line inspection industry and classified the UAV communication link type and summarized the wireless mesh networking protocols; however, it lacks focus on the existing schemes related to collaborative UAV communication.

In [34], the authors reviewed machine learning techniques for UAV communication and provided an overview for integrating machine learning techniques that can optimize the physical layer and improve resource and network management. Furthermore, Hayat et al. in [35] studied the civil applications of UAVs and discussed QoS and data communication requirements for multi-UAV communication. While Sharma et al. specifically discussed the cellular communication challenges of UAV-to-UAV and UAV-to-device communication. Table I further highlights the key features of existing related surveys.

Although the surveys mentioned above are quite comprehensive, they lack a comprehensive focus on collaborative communication in UAVs. Therefore, this review aims to fill the gap and provide a detailed study to help design collaborative multi-UAV systems in the future to advance the performance of multi-UAV systems. To this end, this paper discusses the current literature on collaborative UAV communication, including communication and control requirements, use cases for different applications, and opportunities for collaborative UAV communication. Moreover, the paper discusses the open challenges and future research directions that need significant attention to realize the scope of collaborative UAV communication.

## B. Contributions and Organization

We summarize the primary contributions of this review as follows:

![](images/9d5f690a3fa625721f61a2a9d07fb1a8cdcbf2a603bc870ca84af2b7ff6d50c8.jpg)  
Fig. 1. Illustration of a collaborative UAV network.

• First, we present the prospects of UAV collaboration and summarize their basic requirements and challenges, including communication, control, and cooperation.

• Then, we describe different collaborative tasking performed by a swarm of UAVs, such as joint task completion, trajectory formation, cooperative localization, data collection, and other cooperative decisions. In addition, we have also discussed the UAV swarm network applications in urban environments.

• After that, we present several use cases of collaborative UAVs to show their effectiveness. These use cases include agriculture and environment monitoring, remote sensing, surveillance, and disaster management.

• Finally, we highlight various exciting future research directions that can play a crucial role in advancing the potential of collaborative UAVs.

The rest of the paper is organized as follows: Section II thoroughly discusses the communication and control requirements and challenges of collaborative UAVs. Section III presents UAV swarm network applications in urban environments. Section IV describes the use cases of UAVs applications. Section V highlights the future research directions, and finally, Section VI summarizes the key findings of the paper.

## II. COLLABORATION IN UAVS: AN OVERVIEW

At first, single UAV systems were used for navigation, surveillance, and disaster recovery, where each UAV works as an isolated node directly connected to the central ground station. However, in a single UAV system, due to independent operations of UAV in a designated area, they are more prone to system and communication failure. In addition, independent working of UAVs in a network also requires a longer time and a higher bandwidth to complete a mission. In contrast, in a multi-UAV system, UAVs work together to achieve a common objective. For example, UAVs can work collaboratively to generate high-resolution images and 3D mapping to identify hotspot areas during disaster relief. At the same time, the UAVs equipped with sniffers can detect a high level of methane to locate broken gas lines. Accordingly, UAVs can also supply water and food without endangering the lives of rescue personnel. Therefore, coordination and collaboration are crucial for achieving desired performance in a multi-UAV environment. This section will provide a detailed discussion on the requirements and challenges of collaborative UAVs, such as intelligence, communication, control, and collaboration. Furthermore, we will present state-of-the-art collaborative communication methods to highlight the UAV network’s contributions and limitations.

## A. Intelligent UAVs

The main components of a conventional UAV include sensing, communication, control, and a computational unit [25]. The sensing unit comprises multiple sensors integrated into a UAV for different purposes, such as assessing high-resolution objects, temperature estimation, light detection, and antenna configuration [36]. At the same time, the communication unit enables UAVs to communicate with each other and with the central control station for exchanging information. A mandatory control unit generally controls the operations of conventional UAVs for collision avoidance, path planning, object tracking, and resource management. However, frequent communication with the central control unit and limited UAVto-UAV communication capabilities limit the autonomy and collaboration of UAVs for independent mission completion. For example, in disaster relief operations, multiple UAVs with autonomous features can perform collaborative functions, such as a group of UAVs can examine the hazardous area while the other UAVs can perform supply-drop runs with medical aid to help the victims. In addition, UAVs with high-resolution cameras and resource management algorithms can perform intelligent decision-making to minimize damage. At the same time, when UAVs have an improved understanding of wind patterns in the urban environment, they can use that knowledge to avoid turbulence and choose minimal energy routes without taking frequent instructions from the control unit.

TABLE I  
SUMMARY OF RELATED SURVEYS
<table><tr><td rowspan=1 colspan=1>Ref.</td><td rowspan=1 colspan=1>Primary focus</td><td rowspan=1 colspan=1>Key features</td></tr><tr><td rowspan=1 colspan=1>[10]</td><td rowspan=1 colspan=1>Distributed operationsof UAVs</td><td rowspan=1 colspan=1>1. Provides a comprehensivediscussion on UAVs swarmnetwork for various operationssuch as object tracking, pathplanning, navigation, monitoringand data manipulation</td></tr><tr><td rowspan=1 colspan=1>[20]</td><td rowspan=1 colspan=1>UAV communicationlinks</td><td rowspan=1 colspan=1>1. Discusses UAV communicationlinks (such as UAV-to-UAV andUAV-to-infrastructure)2. Study and identify the requirem-ents of UAV-based communicationsystems</td></tr><tr><td rowspan=1 colspan=1>[24]</td><td rowspan=1 colspan=1>Prospects of UAV-enabledwireless networks</td><td rowspan=1 colspan=1>1. Discusses the opportunities ofUAV-enabled wireless communicatio2. Investigates the challenges ofUAV networks including, 3Ddeployment, channel modeling, andenergy efficiency3. Review mathematical tools forUAV applications</td></tr><tr><td rowspan=1 colspan=1>[25]</td><td rowspan=1 colspan=1>UAV communicationprotocols</td><td rowspan=1 colspan=1>1. Discussion on UAV architectures2. Existing UAV communicationprotocols</td></tr><tr><td rowspan=1 colspan=1>[27]</td><td rowspan=1 colspan=1>Channel measurementsand modeling for UAVand aeronauticalcommunications</td><td rowspan=1 colspan=1>1. Provides design guidelines formanagingthe link budget of UAVcommunications2. Discussion on link losses andchannel fading effects</td></tr><tr><td rowspan=1 colspan=1>[28]</td><td rowspan=1 colspan=1>UAV communicationnetworks</td><td rowspan=1 colspan=1>1. Discuss characterization of aUAV network2. Explore network set issues,mobility, and resource constraintsof UAV network</td></tr><tr><td rowspan=1 colspan=1>[29]</td><td rowspan=1 colspan=1>Commercial applicationsof UAVs</td><td rowspan=1 colspan=1>1. Discussion on integration ofUAVs into cellular networks2. Interference issues and potentialsolutions addressed by standard-ization bodies for providingaerial services</td></tr><tr><td rowspan=1 colspan=1>[31]</td><td rowspan=1 colspan=1>Characteristics of aUAV network</td><td rowspan=1 colspan=1>1. Discusses the characteristicsof a UAV network compared toWSN and mobile ad-hoc networks2. Summarizes the networkissues (such as routing, powerand quality of service) forcollaborative UAV networks</td></tr><tr><td rowspan=1 colspan=1>[32]</td><td rowspan=1 colspan=1>UAV&#x27;s role in realizing asustainable smart world</td><td rowspan=1 colspan=1>1. Summarizes strategies to integrateUAVs with IoT as edge intelligencedevices to collect and process dataobtained from IoT devices2. Explores the opportunities forconnectivity and communicationbeyond 5G</td></tr><tr><td rowspan=1 colspan=1>[33]</td><td rowspan=1 colspan=1>UAV communicationprotocols for powerline inspection industry</td><td rowspan=1 colspan=1>1. Reviews the existing UAVcommunication protocols forpower line inspection industry2. Classifies UAV communicationlink type and summarizes wirelessmesh networking protocols</td></tr><tr><td rowspan=1 colspan=1>[35]</td><td rowspan=1 colspan=1>UAVs for civil applications</td><td rowspan=1 colspan=1>1. Discussion on the characteristicsand requirements of UAV networksfor civil applications2. Investigate the suitability ofexisting communication technologiesfor UAV networks</td></tr><tr><td rowspan=1 colspan=1>Ourpaper</td><td rowspan=1 colspan=1>Collaborative communicati-on and control mechanismsin UAVs</td><td rowspan=1 colspan=1>1. Presents collaborative communi-cation and control requirements formulti-UAV networks2. Reviews current collaborativecommunication mechanisms3. Presents UAVs applications forurban environments and smart cities</td></tr></table>

Similarly, intelligent UAVs with collaborative communication abilities can perform various distributed operations and make independent decisions for smart city applications [32]. For instance, UAVs working in the urban environment need a high level of coordination and collaboration with other sensing devices, machines, robots, drones, and people to perform certain operations. Accordingly, improved cooperation and knowledge of the deployment environment assist in the seamless interaction of UAVs with the surrounding objects for processing monitored data and making real-time decisions to enhance safety and reliability in complex environments [37]. Likewise, UAVs can improve object recognition by the semantic understanding of the surrounding objects in an urban environment to better understand and devise methods to interact with the surroundings.

However, the lack of efficient intelligent autonomous UAVto-UAV communication mechanisms that enable independent UAV flight, trajectory formation, target localization and data manipulation decisions is hindering the scope of UAV-based applications. Thus, to benefit from the natural characteristics of UAVs (such as high mobility, flexible deployment, and different types of sensors integration), it is necessary to focus more on the autonomy and intelligent collaborative communication capabilities integration into UAVs to improve their performance as a team to understand the environment and share the knowledge and resources for intelligent decisions without a high dependency on the central control for systematic instructions [38].

## B. Communication Requirements

In a multi-UAV system, UAVs communicate with each other and with the central backbone infrastructure to complete various designated tasks successfully. Communication among UAVs and infrastructure networks generally follows two modes of communication, UAV-to-infrastructure, and UAV-to-UAV, to exchange data and ensure a high level of connectivity to achieve collaborative communication. This section discusses the communication requirements of both modes in detail.

1) UAV-to-Infrastructure: UAV-to-Infrastructure communication enables information transfer between the UAVs and infrastructure network using different platforms, including terrestrial, high-altitude platforms (HAP), and satellites, as shown in Fig. 2. UAVs can act as a communication relay, user or a base station to establish effective communication. UAVs, as a relay, provide wireless coverage between ground stations and remote infrastructures when direct contact is unavailable. UAVs as a relay bring many advantages, such as improved coverage, fast speed, clear communication channel, easy deployment, and reliable data forwarding mode [39], [40]. While UAVs can also work as a user to offload task to the edge server for enhanced coverage with low latency [41]. At the same time, when UAVs work as base stations, they offer more flexibles solution to provide communication services as they enable better LoS propagation, scalability, and higher operational altitude for heterogeneous networks [42]. This section highlights the primary communication requirements for enabling an efficient swarm of UAVs using each platform mentioned above.

![](images/1e758a5a43180b5ab18bee85053eb01587d3bda3c87babd67027070cfbbfe53e.jpg)  
Fig. 2. Overview of a communication links a collaborative UAV network.

• UAV-to-Terrestrial: It is the link between UAVs and on-ground Base Stations (BSs). These links can be established using LoS or Non-LoS communication links. Nevertheless, the high altitude and increased mobility of UAVs raise various critical issues for UAV-to-Terrestrial communication, such as substantial aerial-terrestrial network interference, QoS requirements for UAV control messages, and LoS communication [22], [43]. In addition, UAV-to-Terrestrial communication is also affected by natural disasters such as forest fires, tsunamis, and earthquakes that destroy the communication entities and cause complete damage to backhaul networks [44], [45]. To increase the data rate and reduce latency, recent works [21], [22] suggested integrating 5G and future cellular networks with the UAVs. In addition, satellite or direct communication links can overcome the terrestrial communication challenges in remote areas such as deserts, seas, and forests.

• UAV-to-Satellites: UAV-to-Satellite communication offers several benefits for connecting UAVs to the ground infrastructure compared to the UAV-to-Terrestrial communication, such as global coverage, improved navigation, and localization [22]. The advanced global coverage using low earth orbit satellites provides services in remote areas such as deserts and seas where terrestrial services are unavailable. Satellite links also provide beyond LoS communication, which is significantly beneficial for advancing global coverage and reliability of UAVs applications for tactical and commercial applications [46]. However, the high propagation loss and delays of UAV-to-Satellite communication links are significant challenges that need to be addressed for delay-sensitive applications [23], [47]. Moreover, the operational costs for UAV-to-Satellite communication are also high, and the communication equipment, such as large antennas, consumes high energy [22]. In addition, during navigations, when UAV’s altitude varies frequently, they must constantly direct the beam towards the satellite to maintain the communication link [48]. Furthermore, effective channel modeling and physical layer characterization are also required for improved UAV-to-satellite communication [49], [50].

• UAV-to-HAPs: HAPs such as balloons and helikites are positioned highly elevated (up-to-20 km) compared to the terrestrial systems and offer multiple benefits, including broader coverage, advanced endurance, high data rate, and better path-loss characteristics. HAPs have low deployment costs compared to terrestrial setup, and UAV-to-HAP communication links also have better LoS communication that improves the signal reliability for direct communication while reducing the probability of LoS communication obstruction by the tall buildings in the urban environment [51], [52]. In addition, the HAPs platform is best suited to provide broadband communication services by carrying 3G, 4G, or beyond 4G payload that can play an essential role in providing emergency communication services in disaster areas [53], [54]. HAPs have more advantages over terrestrial and satellite systems; however, spectrum regulation is the primary challenge for HAPs. HAPs need to address the global and regional spectrum challenges for frequency band allocation to enable flexible operation while protecting existing services within candidate frequency bands [55]. Moreover, HAPs also raise safety, privacy, and security issues that need to be focused on providing secure UAVto-HAP communication services [56].

2) UAV-to-UAV Communications: Besides UAV-to-Infrastructure communication, effective UAV-to-UAV links enable a swarm of UAVs to overcome various fundamental challenges such as autonomous flight, collision avoidance, distributed processing, and joint operations. The stateof-the-art literature has suggested multiple means to provide UAV-to-UAV communication, including satellite communication links, Wi-Fi links, Ultra-High Frequency (UHF) links, cellular communication links, Long-Range Wide-Area Network (LoRAWAN), and Free-Space Optical (FSO) links. This section discusses the requirements of these different approaches for enabling stable and reliable UAV-to-UAV communication.

• Wi-Fi and UHF radio links: UAV-to-UAV communication using Wi-Fi radio links support communication only at a short-range and suffer from high interference. Wi-Fi radio links can provide BLoS communication using a ground control station as a correlated communication relay system. However, it increases delay and degrades the effectiveness of UAV-to-UAV communication for mission-critical applications. In contrast, UHF radio links provide better communication over long distances without getting affected by obstacles and diffraction. Point-topoint wireless link in the UHF band (400 MHz) also provides reliable communication in near-line or non-line of sight conditions. However, the spectrum regulatory bodies have not specified the frequency band for UHF radio links that are required for licensed protection [57], [58].

• Cellular networks-based links: Civil and commercial applications prefer cellular communication technologies for UAV-to-UAV communication to alleviate various limitations such as range of communication, networking, and inadequate resources. Cellular-connected UAV also provides a cost-effective solution as they will reuse the millions of cellular BSs worldwide without the need to build new infrastructure dedicated to UAVs only [22]. However, cellular-connected UAVs have different communication and spectrum requirements that require new design considerations to avoid interference between the existing ground users and flying UAVs [59]. Moreover, BSs antennas conventionally provide 2D coverage; however, flying UAVs have high altitudes that require modifications in BS antenna design to provide 3D coverage [60].

• LoRaWAN-based links: Besides cellular networks, LoRAWAN provides long-distance LoS communication for UAVs in a swarm, establishing UAV-to-UAV communication with high bandwidth and increased connectivity for exchanging a high amount of data [61]. In addition, LoRAWAN extends the coverage area for different operational regions and enables low energy dissipation communication among UAVs [62]. However, LoRAWAN operates at the unlicensed 900 MHz ISM band that experiences severe co-channel interference and path loss [63]. Therefore, interference mitigation approaches are required to provide LoRWAN-based reliable UAV-to-UAV communication [64].

• FSO-based links: Another alternative to establishing UAV-to-UAV links is FSO which uses light in the free space to transmit data wirelessly among UAVs [65]. FSO communication links are generally point-to-point or longrange links with high bandwidth for increased data rate connectivity, making them suitable for UAV-to-UAV communication to transmit a large amount of data wirelessly. Due to the long-range, the occasional loss of one of the UAVs operating in swarm formation does not entirely stop the data transfer process [66]. Nevertheless, UAV’s high mobility is the primary constraint for establishing FSO-based links due to the misalignment between the transmitters and receivers. Moreover, atmospheric and turbulence effects also degrade the FSO-based UAVto-UAV links, requiring effective channel and mobility modeling [67].

• Satellite-based UAV-to-UAV communication links: They provide secure LoS and BLoS communication to support stable and reliable UAV-to-UAV communication. The satellite-based UAV-to-UAV communication links are commonly used for surveillance, security, and defense applications for long-term operations, better coverage, and reliability. However, as UAVs are constantly moving, thus the high relative velocity results in a significant Doppler shift. In addition, satellite-based UAV-to-UAV communication links also suffer from a high latency for time-critical applications [68]. Therefore, more in-depth analyses are required to overcome the challenges of delay, Doppler shift, and multi-user interference when multiple UAVs are communicating using satellite-based UAV-to-UAV communication links [46].

## C. Control Requirements

Due to UAVs’ small size and low-cost demand, they require a cost-effective control system that can enable flexible movement and trajectory tracking for takeoff, landing, hovering, maneuverability, altitude control, localization, and collision avoidance. The primary control requirements for UAVs are discussed below:

• Landing and Takeoff: The UAVs can be classified as fixed-wing and rotary-wing, where both have their specific requirements for landing and taking. The fixedwing UAVs require a runway for takeoff and landing, while rotary-wing UAVs can take off and land vertically, improving their suitability for diverse civilian applications [69], [70], [71]. In [72], the authors presented a hybrid Vertical Takeoff and Landing VTOL solution that integrates fixed-wing and rotary-wing UAV features in a single platform to achieve long flight endurance with high flight efficiency. The VTOL approach requires a fixed-wing position controller, rotary-wing position controller, transition controller, and VTOL mixer based on aerodynamic characteristics to realize transition and improved flight stability. In another work [73], different

PID controllers are used for VTOL without a runway and launch recovery equipment, performing a smooth operation with control commands. Furthermore, in existing literature [74], [75], [76], various solutions have also been presented that use visible light camera sensors, GPS, and IMU to land and take off using PID controllers.

• Controlled Movement and Hovering: UAV’s rotors use propellers that enable roll, thrust control, pitch, yaw, and six degrees of freedom for spinning, maneuvering, and hovering. UAV’s control algorithm adjusts the roll, pitch, and yaw for stable rotation on the X-axis, Y-axis, and Z-axis. Existing studies have presented various models to control the movement of UAVs; for example, Thu et al. in [77] modeled the well-known quadcopter control system for flexible movement and maneuver based on “+” and “C−” flying configurations. In another work [78], a dynamic model is designed to control the UAV’s motion on one rotation axis. Elkaim et al. in [79] presented a UAV control system that used position, velocity, and altitude estimation for UAV-controlled movement and trajectory formation. In another work in [80], an autonomous UAV flight control system is introduced that integrates a GPS to generate optimal flight paths. Furthermore, throttle movements, state information, and onboard sensing components have also been analyzed and modeled in existing literature for stable maneuver and hovering [81], [82], [83].

• In-flight Control: UAVs state information such as the position and velocity are used to guide and control the UAV for precision operations such as landing or object tracking. Remotely Operated Aerial Model Autopilot (RAMA) is thoroughly described in [84] that uses altitude, angular rates, and position information for designing the control system for small UAVs. Furthermore, PID controllers have also attracted significant attention from academia and industry for autonomous UAV operations [85]. Integrated PID autopilot enables a complete set of avionics for autonomous UAV navigation and realtime operations [86]. In addition, the PID controller also improves reliability and stabilizes the movement of flying UAVs on a predefined trajectory with minimal error and energy consumption.

• Collision avoidance It is the basic requirement of UAV design to ensure autonomous UAV flight. Current literature [80], [87] suggested various means such as GPS-guided navigation and different collision-avoidance sensors to avoid collisions. Furthermore, according to existing studies [88], [89], cheap commercially available sensors (such as infrared, pressure, and height sensors) can easily be integrated into UAV flight systems to estimate the distance from an obstacle to control its movement. In addition, accurate location estimation of UAVs and trajectory planning is also a fundamental requirement for collision avoidance [90].

## D. Collaborative Tasking

The existing developments regarding collaborative communication are focused comprehensively in this section.

UAVs’ collaborative tasking allows multiple UAVs to share information to perform various tasks cost and time effectively in a distributed manner with enhanced flexibility, robustness, and fault tolerance. In recent years, a few collaborative communication architectures have been presented, primarily focusing on integrating UAV networks with WSNs, Ad-hoc networks, and the IoT paradigm for effective monitoring and data collection [91]. In addition, a few swarm-based approaches have also been introduced for collaborative trajectory planning, routing, and target localization.

1) Swarm-Based Collaborative Communication: Several recent works use a swarm of UAVs to complete a mission collaboratively in a short time with better coverage, reliability, and efficiency. For example, Sathyan et al. in [92] presented a fuzzy genetic algorithm that is specific to polygon visiting multiple traveling salesman problems to solve the clustering and routing issues of UAVs swarms. The genetic fuzzy algorithm use distance for cluster formation and cost function optimization for efficient route selection to identify maximum targets with reduced computational complexity. In [93], the authors introduced a swarm of UAVs that are controlled and operated by a human operator at different levels to enable the self-organization of UAVs for monitoring and surveillance purposes. In another work [94], UAV’s collaborative movement and coordination are managed through mobile networks by integrating a smartphone into the UAVs. The UAVs fly in the region of interest either in a swarm or petrol mode to capture the images and transmit them to the ground station using the mobile network. Another work in [95] presented a joint task placement and routing algorithm for a UAV swarm network. In the UAV swarm network, each UAV is assigned a different task and path by the central algorithm to complete the collaborative operation with reduced latency, improving QoS demand. In [96], the particle swarm optimization algorithm is presented for optimal localization and clustering of the swarm of UAVs. Once targets are identified, the swarm intelligence-based algorithm forms the cluster for multi-hop communication and retrieves the emergency information with reduced energy consumption.

2) Deep Reinforcement Learning for UAV Swarm Networks: In the past few years, reinforcement learning techniques have been considerably adopted to improve the performance of UAV swarm networks for path planning, navigation, and control in complex environments [97], [98]. For example, in [99], a multiagent reinforcement learning technique is introduced for UAV Swarm-based target tracking. End-to-end cooperative multiagent reinforcement learning allows UAVs to make intelligent flight decisions based on the past and present states of the target for cooperative target tracking with reduced energy consumption. In another work [100], Hu et al. proposed an autonomous maneuver decision-making scheme based on deep reinforcement learning for cooperative air combat. UAVs perform the situation assessment to identify the target’s current situation and design the reward function for increasing the training convergence of UAVs for defeating the enemy. In [101], authors presented a deep reinforcement learning method that allows UAVs to execute navigation tasks in large-scale complex environments for remote surveillance and goods delivery application. Reinforcement learning-based navigation enables direct mapping of UAVs’ raw sensory measurements into control signals for autonomous navigation in large-scale, complex, and three-dimensional environments.

Furthermore, Zhang et al. in [102] presented a geometric reinforcement learning scheme for UAV’s path planning by exploiting a specific reward matrix to select the candidate points from the current position to the target position for effective navigation. In another work [103], authors designed an interference-aware path planning scheme for cellularconnected UAVs based on an echo state network deep reinforcement learning algorithm. The deep echo state network architecture enables each UAV to map each observation of the network state to action for reducing a sequence of timedependent utility functions and learn about its transmission path, optimal path, and cell association vector for minimizing the interference level and transmission delay. In [104], the authors introduced a deep reinforcement learning algorithm based on deep neural networks for UAV control. Deep neural network-based reinforcement learning algorithm leads to significantly enhanced energy efficiency, coverage, and connectivity of the UAV swarm network.

In another work [105], Hu et al. focused on improving the sensing and communication quality of cellular-connected UAVs by designing a reinforcement learning algorithm-based distributed sense-and-send protocol. The reinforcement learning algorithm-based distributed protocol enhanced UAV coordination and led to efficient collaborative trajectory control and resource management. Cui et al. in [106] also improve resource allocation in the UAV swarm network by introducing a multiagent reinforcement learning framework that allows each UAV to work as a learning agent. Each action of UAVs as a learning agent corresponds to a resource allocation solution and helps them to find the best solution for the resource allocation based on their local observations. In [107], the authors introduced deep reinforcement learning for backscattering data collection with multiple UAVs to reduce their total flight time. The deep reinforcement learning algorithm allows UAVs to fly within the deterministic boundary and enable cooperative learning to find the ambiguous backscatter sensor node for data collection. In addition, in [108], the deep reinforcement learning algorithm has also been used for three-dimensional complex flight environments by introducing a reinforcement learning-based grey wolf optimizer algorithm for UAV path planning. The grey wolf optimizer algorithms mimic the social hunting behavior of the grey wolf and perform exploration, exploitation, geometric adjustment, and optimal adjustment for smooth planning of the UAV’s flight route.

3) Trajectory Formation: Collaborative trajectory formation enables multiple UAVs to find the optimal path from the starting point to the target point. It is one of the emerging areas of research in UAV systems as collaborative path planning minimizes localization cost, improves maneuver decisions, and helps in collision avoidance [109], [110], [111]. In the existing literature, various collaborative trajectory formation techniques exist. For example, in [112], a dynamic trajectory planning method is introduced, in which the leader UAV uses the hp-adaptive pseudospectral method to find the optimal path and shares it with the follower UAV for operation execution. The hp-adaptive pseudospectral method begins with a global pseudospectral approximation for the state. Then, each iteration determines locations for the segment breaks and the polynomial degree for the next iteration to select the optimal path in a dynamic environment in a reduced time. In another work in [113], optimal path planning is performed by solving multiple traveling salesman problems using the genetic algorithm. Each UAV flies randomly to locate the target and share this information with the central BS. The central BS executes the information collected from the flying UAVs and estimates the target location for trajectory formation with reduced complexity and energy consumption. Wang et al. in [114] introduced the Sequential Convex Programming (SCP) method for cooperative trajectory formation that iteratively finds an optimal local solution with reduced computational complexity. Therefore, it has been extensively used for trajectory planning with highly nonlinear dynamics, such as proximity operations, spacecraft rendezvous, and fueloptimal powered landing [115], [116]. In [117], the optimized Artificial Potential Field (APF) method is proposed for UAVs collaborative path formation. UAVs use optimized APF (APF was originally introduced for moving robots from initial points to the targeted points [118]) to perform dynamic steps adjustment and climb strategy for safe and stable paths selection for their movement with reduced collision probability. In [119], Guo et al. introduced a cooperative relative localization scheme to enable infrastructure-free communication among UAVs for UAVs localization and flight formation using consensus-based fusion. Each UAV performs consensusbased fusion for direct and indirect estimation of a target location and uses this information to control flight trajectory. Recently, Qadir et al. [120] compared different metaheuristic algorithm for UAVs efficient path planning in complex envi ronments. The autonomous trajectory optimization for UAV shows promising results in naturally occurring catastrophic events as shown in Figure 3.

![](images/36048f0eb4ee637e42ad5ea883a080b96d13c0625296a2f3ce213166f0131c5d.jpg)  
Fig. 3. Trajectory optimization using collaborative UAVs.

4) Cooperative Target Localization: Accurate localization brings significant advantages for target indication, aerial filming, data sensing, and air-to-ground attacks [121]. Collaborative UAVs communication helps identify the target in reduced time with better position accuracy [122]. Therefore, various methods have been introduced in the literature to enable collaborative UAVs localization with reduced communication delay and packet loss. For instance, in [123], authors introduced a centralized and distributed mechanism for cooperative UAVs target localization with reduced communication delay and packet loss. Each follower UAV separately transmits the target information to the leader UAV during centralized localization without any prior processing. The leader UAV processes all obtained information for the final target location estimation. On the other hand, in disturbed target identification, multiple UAVs cooperatively process the location information and transfer the final positioning information to the leader UAV for further processing. In [124], Received Signal Strength (RSS) and Differential RSS (DRSS) are used to identify RF sources and plan UAVs’ movement toward the RF targets. Then, in [125]db@fu2019pollution , Fu et al. improved pollution source localization by enhancing the convergence and the searchability of particles by using APF and particle swarm optimization for cooperative UAV communication.

Furthermore, in [126], a cooperative maneuver scheme is introduced in which two UAVs are equipped with heterogeneous sensors (i.e., bearing-only and range-only sensors) for cooperative localization. The use of heterogeneous sensors for cooperative maneuver localization led to reduced complexity and enhanced data collection in a shorter time. Another work [127] simulates and demonstrates a cooperative search and rescue operation for a post-disaster situation using multiple UAVs. Multiple UAVs perform different tasks such as localization, inspection, path planning, and navigation to identify the houses and survivors in the targeted area for collaborative search and rescue operations.

5) Data Collection: In the past few years, numerous collaborative communication mechanisms have been introduced to improve the remote data collection experience [128]. Furthermore, various existing schemes have also integrated UAV networks with WSN and IoT to enhance their collaborative performance. For example, in [129], a WSN-UAV collaborative network is presented to optimize data collection from a resource constraint sensor network by introducing a UAV that follows a predefined trajectory for energyefficient and fast data acquisition. Similarly, in [130], multiple flying UAVs collaboratively collect data from the sensing devices in a short time with better efficiency and reduced energy consumption. In [131], UAV and fog computingbased data communication architecture (consisting of multiple UAVs, fog nodes, and ground station) is presented to collect data from natural disaster and hazard monitoring areas efficiently. During an emergency, when flying UAVs cannot transfer data to the ground station directly, then the flying UAVs transfer the collected data to the fog nodes for storage, processing, and transmission to the ground station for effective remote processing and rescue operations. Wang et al. in [132] also introduced multiple flying UAVs for data collection from IoT devices. The flying UAVs follow their predefined path to collect data from their designated areas with the aim of equal opportunity for all UAVs to participate in data aggregation with a reduced flight time to save energy.

![](images/b701ab1e6ca70b7135ed407f878954460a524817d777784f4b453432644e751d.jpg)  
Fig. 4. Collaborative UAV-WSN-IoT in an agricultural field.

In [133], a collaborative UAV-WSN-IoT communication architecture is presented comprising multiple UAVs, sensing, and IoT devices deployed in an agriculture field as shown in Figure 4. UAVs search for IoT devices to efficiently collect the monitored data energy for precision agriculture. In [134], UAV-WSN-IoT is introduced for collaborative data acquisition and processing for post-disaster management using cloud services. Multiple UAVs fly in their predefined clusters to localize sensing and IoT devices. The collected data is stored in the cloud for efficient data processing and management. Schmuck in [135] presented a new collaborative UAV communication architecture based on the Simultaneous Localization And Mapping (SLAM) algorithm where multiple flying UAVs run the SLAM algorithm to enable independent exploration of their environment. Each UAV communicates its experience with the ground station, and then the ground station uses the collected information for data fusion, advanced processing, task assignments, management, and optimization. In [136], the authors introduced UAVs for opportunistic data collection in cognitive WSN where the ground sensing device forms clusters using the coalition formation game model. Coalition game theory allows ground sensing devices to share resources and balance the load to upload the data to the flying UAVs with improved reliability and efficiency.

6) Cooperative Decisions: The autonomous operations of UAVs require making complex decisions to meet the application objectives, such as the elimination of threats or time-critical rescue operations. These complex decisions are affected by inadequate information, high uncertainty, delay, and task coupling [137]. Therefore, UAVs need cooperative decision algorithms to provide robustness and flexibility to ensure adequate performance in uncertain and adversarial environments. Zhao et al. in [138] introduced the max-consensus algorithm for estimating the Joint Multi-Target Probability Distribution (JMTPD) of UAVs for cooperative multitarget identification decisions. The max-consensus protocol employs a distributed information fusion strategy to improve the JMTPD estimation and lead to accurate observation and estimation of the moving targets. In [139], Partially Observable Markov Decision Processes (POMDPs) are adopted for cooperative surveillance decisions, which are modeled for different surveillance problems, and each UAV is assigned a different behavior to complete the surveillance policy cooperatively. Furthermore, various state-of-the-art schemes have focused on cooperative decisions for task assignments, control, and coordination. However, the joint decisions of UAVs need more attention for reducing delay and uncertainties in dynamic environments for stable operations of multiple UAV systems. The state-of-the-art developments regarding collaborative communication are also further summarized in Table II.

TABLE II  
STATE-OF-THE-ART WORKS ON COLLABORATIVE TASKS MECHANISMS
<table><tr><td>Ref.</td><td>Purpose</td><td>Advantages</td><td>Ref.</td><td>Purpose</td><td>Advantages</td></tr><tr><td>[112]</td><td>Optimal trajectory formation in a dynamic environment</td><td>1. A new trajectory can be formed at low cost when a new event occurs</td><td>[113]</td><td>Energy-efficient cooperative trajectory formation using genetic algorithm</td><td>1. Low computational complexity 2. Energy conservation</td></tr><tr><td>[114]</td><td>SCP-based cooperative trajectory formation for reduced computational complexity</td><td>1. Minimum time trajectory formation 2. Low computational complexity</td><td>[117]</td><td>Optimal path planning and collision avoidance for stable path formation</td><td>1. Stable trajectory formation 2. Collision avoidance</td></tr><tr><td>[127]</td><td>Cooperative search and rescue in a post-disaster situation for localization, inspection, path planning and navigation to identify the houses and survivors in the targeted area</td><td>1. Collaborative search and rescue operations simulation and demonstration</td><td>[119]</td><td>Consensus-based location estimation and formation control for target identification</td><td>1. UAVs formation without infrastructures, global positions, and pattern detection computation</td></tr><tr><td>[123]</td><td>Centralized and disturbed localization with precision and accuracy</td><td>1. Reduced communication delay and packet loss 2. Improved position estimation</td><td>[124]</td><td>RSS and DRSS are used for trajectory planning and location estimation</td><td>1. Minimized number of UAVs 2. Reduced mission time and path length</td></tr><tr><td>[125]</td><td>Cooperative location estimation for identifying pollution sources</td><td>1. APF helps in collision avoidance 2. Reduced cost and efficient target localization</td><td>[126]</td><td>Cooperative maneuver localization using two small UAVs that are equipped with heterogeneous sensors</td><td>1. Low complexity 2. Enhanced data collection in a limited time 3. Improved accuracy</td></tr><tr><td>[130]</td><td>Collaborative data collection in reduced time</td><td>1. Minimized data collection time 2. Reduced energy consumption</td><td>[131]</td><td>UAV-fog collaborative communication architecture for remote data collection</td><td>1. Improves the revenue of UAV-enabled remote data collection</td></tr><tr><td>[132]</td><td>predefined path to efficiently collect data in a reduced flight time Multiple UAVs fly in their predefined</td><td>1. Reduced flight time 2. Low energy consumption</td><td>[133]</td><td>UAVs search for sensing and IoT devices to efficiently collect data for precision agriculture Localization and data collection using</td><td>1. Energy efficiency 2. High precision</td></tr><tr><td>[134]</td><td>clusters to localize sensing and IoT devices for efficient data collection Coalition game theory is used that allows</td><td>1. Energy efficiency 2. Improved data management</td><td>[135]</td><td>SLAM algorithm for independent exploration of the environment</td><td>1. Energy efficiency 2. Optimized resource utilization</td></tr><tr><td>[136]</td><td>and balance the load for opportunistic data transmission</td><td>1. Improved reliability and efficiency</td><td>[138]</td><td>tracking</td><td>1. Improved observation and location estimation</td></tr><tr><td>[139]</td><td>The cooperative surveillance decision</td><td>1. Prove the POMDPs for cooperative surveillance decisions</td><td>[140]</td><td>Cooperative control and decision using Ad-hoc communication for tasks assignment and coordination</td><td>1. Effective bandwidth utilization 2. Accurate target localization</td></tr></table>

## III. UAV SWARM NETWORK APPLICATIONS IN URBAN ENVIRONMENTS

UAVs are an integral part of sustainable urban development due to their crucial roles in accelerating the development of various smart city applications such as transportation, surveillance, security, key infrastructure monitoring, networking and disaster relief [141], [142], [143]. Accordingly, the current literature substantially focuses on UAVs for the seamless integration of information and communication technology for realizing the concept of a smart city for urban development. This section summarizes the developmental challenges and state-of-the-art solutions of UAV swarm networks in different smart city applications.

## A. Intelligent Transportation System

An intelligent transportation system is one of the primary components of smart city applications. However, the high mobility of vehicles, the large number of obstacles, bridges, and tall buildings lead to substantial connectivity and communication issues for effective management of transportation systems in an urban environment. Therefore, UAV-aided transportation systems are considered one of the optimal solutions to ensure the essential requirement of high connectivity and automation of vehicles and other building blocks of the smart transportation system (such as traffic police, road surveys, and rescue teams) [144], [145], [146]. UAV-aided transportation systems offer increased mobility and fast response in an emergency. In addition, a UAV swarm network can also optimize vehicle route selection to avoid congestion and help better enforce traffic rules and regulations [142]. State-of-theart literature [147], [148] have introduced UAV-based vehicular networks to use a swarm of UAVs to work collaboratively to provide increased coverage, robustness and connectivity for urban vehicular networks. In [149], the authors introduced a hybrid model based on vehicular ad hoc networks and UAV swarm networks to enable communication between vehicles and UAVs. The hybrid framework focus on finding a reliable routing path and tracking the expiration of a routing path to ensure a high level of connectivity for a stable transportation system. The authors in [150] also introduced UAV-assisted routing to enable fast data delivery for urban vehicular networks. However, the collaborative operations of UAV swarm networks need more efforts to facilitate effective UAV-to-UAV, UAV-to-vehicle and UAV-to-infrastructure communication for the practical realization of an intelligent transportation system.

## B. Intelligent Environmental Monitoring Systems

The realization of the smart city require intelligent monitoring systems to manage its resources and infrastructure for better connectivity and services. UAVs with different types of integrated sensors and communication equipment present an excellent solution to monitor a large area independently. UAVs can perform remote sensing and provide high-resolution images, video footage, and multispectral, hyperspectral, and thermal imagery that helps them work as independent monitoring stations to execute various operations when required [151], [152]. However, due to the natural challenges of monitoring a complex and large area, environmental monitoring requires a UAV swarm network to work cooperatively with the ground sensing devices to monitor a large area and share the resources for efficient data manipulation and decision. In addition, the high-level collaboration among UAVs and ground sensing devices also needs to reduce latency and enable real-time communication to achieve high QoS requirements for intelligent monitoring applications.

Integrating UAV swarm networks with the IoT paradigm offers advanced monitoring opportunities by connecting ground sensing devices with flying UAVs to address the above-mentioned issues [32]. Various existing UAV-IoT frameworks [133], [134], [153] focus on connecting the UAV swarm network with IoT architecture to enable continuous monitoring. In [154], authors introduced UAV-fog to reduce latency and improve scalability and real-time communication for UAV-IoT-based applications. In another work [155], the authors presented a software architecture framework for autonomous operations of a UAV swarm network to carry out coordinated firefighting operations in dense urban or forest environments. The software architecture includes a set of complementary methods that allow UAVs to communicate autonomously for cooperative navigation and establish a scalable, robust, and secure communication system for firefighting in dense environments. Moreover, in [156], Sharma et al. also introduced the UAV-IoT framework to monitor the air quality for detecting toxic gases and finding the cause of air pollution to mitigate its effect on human health. However, the massive potential of UAV-based environmental monitoring requires more attention toward developing advanced UAV collaborative networks to ensure a high level of connectivity and networking to enable cost-effective long-term intelligent monitoring.

## C. Intelligent Surveillance

Security and safety have always been the foremost concerns for urbanization. Accordingly, realizing the concept of the smart city is impossible without an intelligent surveillance system that can provide safety and security to the residents with a well-established secure infrastructure. The deployment of UAVs with integrated high-definition cameras can be a security measure to track intruders and monitor unsafe activities such as violence and theft. In addition, a swarm of UAVs can also work together to provide scalable surveillance in a large area with advanced recognition and detection abilities to prevent crimes and to provide safety and security to the citizens around the clock. Various UAV-based surveillance applications for police forces, emergency responders, and industrial and border inspection and security personnel have already been successfully implemented.

Consequently, state-of-the-art literature [157], [158], [159] focuses on developing UAV-based intelligent surveillance systems for urban environments. For example, Liu et al. in [160] introduced a reinforcement learning-based control framework for a swarm of UAVs to perform persistent cooperative surveillance in an unknown urban area. UAV maneuver and target localization using an artificial neural network improve target identification and lead to quality surveillance in the complex urban environment. In another work [161], the authors introduced a UAV-based surveillance network that optimizes the performance of smart devices with integrated cameras to enable reliable and real-time large-scale video surveillance with reduced latency and improved throughput and QoS. Furthermore, current literature [162], [163] also emphasizes using artificial intelligence techniques to provide cost-effective optimal surveillance quality.

## D. Edge Computing Based Resource Management

UAV’s diverse operation for providing surveillance, internet coverage, rescue and relief demands long-term real-time monitoring leading to the extensive amount of video data generation that needs to be communicated and managed [164]. The UAV-based system needs to perform video analytics operations to digitally visualize the video inputs through advanced machine learning algorithms to transform video data into intelligent data for smart decision-making. However, real-time data monitoring and management require addressing several crucial challenges, such as QoS degradation, communication latency, and inadequate computational and storage capacity. Edge computing brings opportunities to solve these shortcomings by providing services at the network’s edge to avoid data transmission to remote servers for data manipulation and decisions. Accordingly, various edge-computing-based schemes have been introduced for resource management of smart city applications [165], [166], [167], [168], [169], [170]. For example, Chen et al. in [95] introduced a hybrid model called UAV-Edge-Cloud to improve the QoS and resource provision for resource-intensive applications for smart city applications. The UAV-Edge-Cloud framework consists of a UAV swarm layer that forms an edge layer near the UAV swarm to enable fast real-time interaction with the users with better quality and resource utilization. Another work [171] introduces energy-efficient rechargeable UAV deployment to optimize the energy efficiency of the UAVswarm network for improved seamless radio coverage in an urban environment.

In another work [172], the UAV-enabled mobile edge computing system is introduced to reduce energy consumption. UAVs fly near the IoT devices to complete different tasks with local computational capabilities for efficient resource management and minimization of energy resources of UAVs and IoT devices. In [173], the authors presented a joint computation and communication architecture for IoT and UAV-assisted mobile edge computing framework. UAVs with integrated edge computing server handles the local data of the IoT devices to reduce latency and save communication and computation energy of the network. Furthermore, Yang et al. in [174] also used a swarm of UAVs with integrated edge computing servers for offloading tasks of IoT devices to improve QoS and network performance. The above discussion shows that UAVenabled edge computing services significantly improve the QoS provisioning and resources management of various WSN and IoT architectures. However, more efforts are required to optimize the communication among IoT devices and UAVs for better task offloading and resource sharing.

## IV. USE CASES OF COLLABORATIVE UAVS

Collaborative UAVs have already become a crucial part of various real-world applications. This section presents some of the use cases of UAVs to highlight their role in advancing various industries.

## A. Agriculture and Environmental Monitoring

UAVs continue to be widespread in agricultural, forest, and environmental monitoring. In agriculture, UAV technology plays a significant role in improving crop production to manage the rising global population pressure on agriculture consumption. For example, UAV-based soil information sourcing is beneficial at the early stage of crop cycles for soil analysis, seed planting patterns scheduling, and irrigation planning to determine the precise quantity of fertilizer needed for improved yield quantity. Agricultural UAVs also assist farmers in crop spraying by covering a large area in a short amount of time with high precision. UAV-based efficient spraying can reach both the plants and the soil below and can protect the farmers against prolonged exposure to potentially dangerous chemicals that have previously been linked with manual spraying [175]. Furthermore, UAV technology can enable extensive forest monitoring to support policies and decisions to conserve, protect, and sustainably manage forests. UAV-based forest monitoring systems can consistently assess forest cover and carbon stock change, especially in the tropics where forests are rapidly vanishing [176]. Recently, drones, satellites, and mobile phone apps have already been used to protect the forest from deforestation in the

Peruvian Amazon [177]. Moreover, UAVs can also plant trees in the forest at a precise location by analyzing the soil and existing plants.

The swarm of UAVs has the potential to perform all the above-discussed tasks in a more cost and time-effective manner. For example, a swarm of UAVs can work with the ground IoT paradigm deployed in an agriculture field to aggregate crop condition monitoring data and cover a large field in a relatively more shorter time. In addition, UAVs equipped with different features such as high-definition cameras, sprays, and edge computing servers can collect detailed information, perform data processing operations with intelligent algorithms and make decisions such as spraying the water or fertilizers to improve crop conditions.

## B. Advanced Surveillance

Advanced surveillance applications require long-term monitoring of the interested area with high QoS demand [159]. However, single UAV systems cannot meet the requirements of advanced surveillance due to limited resources and computational power, as surveillance drones are required to stay in the air for hours or days, and their high-tech cameras need to scan the entire city and zoom in for advanced monitoring. Moreover, UAVs also require the integration of complex machinelearning algorithms for video analytical operations to extract useful information for independent decision-making [164]. Nevertheless, single UAV systems’ limited resources and computational power significantly hinder their potential for advanced surveillance.

At the same time, multiple UAVs equipped with different types of high-resolution cameras, live-feed cameras, infrared cameras, radar, and sensing components can be assigned diverse tasks to provide advanced collaborative surveillance for various commercial, civil and military applications. For example, military drones with integrated advanced live-feed cameras and sensors can enable continuous surveillance for longer hours. In contrast, UAVs with more storage and computational power can provide edge services to process the monitored information with high QoS and low resource consumption. In addition, multiple UAVs can work collaboratively as a high-level perimeter and a response system to prevent unauthorized access in industrial plants such as factories, solar parks, offshore platforms, quarries, and refineries. The images collected from multi-UAV systems are vital for reconnaissance or rapid situation awareness. Ground security can also use ariel surveillance to detect and monitor potential threats from a safe distance and reduce the requirement for foot patrols by security guards. Maritime defense can also significantly benefit from the multiple-UAVs system for counter-piracy operations to monitor, analyze and anticipate pirate vessel movements for identifying hazardous locations and evaluating piracy trends around the world. Moreover, UAVs can also work collaboratively to provide protection services for superyachts, such as helping crews stay safe and reducing delays and cost overruns, which minimizes insurance premiums while assuring stakeholders that company assets are secure.

## C. Cooperative Aerial Imaging for Remote Sensing

Numerous military, commercial and civilian applications require aerial imaging for various purposes such as homeland security, border patrol, monitoring forest fires, tracking wildlife, and nuclear power plants perimeter monitoring [178]. UAVs integrated with high-resolution cameras can perform cooperative aerial imaging by capturing individual images from different viewpoints. Later, the captured images can be analyzed separately or combined to create an overall image. In addition, pictures taken from multiple UAVs flying at a low altitude provide vital information compared to the pictures captured from helicopters or airplanes. UAVs with integrated multimodal sensors and improved photogrammetry and computer algorithms have also displayed great results for acquiring and processing terrain data. The digital surface models and digital elevation models generated from drones provide essential inputs for topography for the accurate modeling of flood plain hydrodynamics, and overland flow predictions [179]. Moreover, UAVs equipped with multispectral cameras also provide the most accurate metadata, leading to efficient and straightforward imagery data collection for vegetation mapping [180]. Accordingly, a swarm of UAVs can cooperatively cover a large area to provide a synoptic view efficiently and economically. UAVs can also provide data under clouds, which is particularly useful in tropical areas where cloud cover is frequent for long periods of the year. Thus, UAVs can improve satellite data’s spatial, temporal or spectral resolutions by providing a complementary dimension through fusion methods.

## D. Disaster Management

UAVs have shown significant strides and advances in disaster risk reduction, preparedness, response, recovery, relief, and rehabilitation. A swarm of UAVs can provide better help and support during a disaster by assigning different recuse and relief tasks to a group of UAVs. Accordingly, sufficient knowledge and resource sharing among UAVs can better facilitate the victims with medical aid and rescue operations. For example, drone-led surveillance can detect a potential or apparent disaster quickly by flying to a potential hazard to investigate a suspicious occurrence. Collaborative UAVbased reconnaissance gives a first-hand analysis of the disaster point and helps strategize on-ground action much faster than manual detection, investigation, and action. In addition to emergency response and disaster awareness, a group of drones can efficiently perform supply-drop runs with medical and essential packages during floods, cyclones, or earthquakes for the well-being of stranded survivors. For example, UAVs can be notified by the other surveillance providing UAVs to deliver medical equipment such as Automated External Defibrillators (AED) (i.e., AED help analyze the heart rhythm and deliver an electric shock to victims of ventricular fibrillation to restore the heart rhythm to normal) for first aid.

Furthermore, the collaborative working of UAVs also exhibits a tangible impact on disaster response by performing multiple search and rescue operations. Drones equipped with high-definition cameras and thermal sensors can conduct high-resolution visual and thermal imaging to clearly picture survivors, even under rubble or within inaccessible crevices. The information provided by the drones helps the on-ground team to understand all access points and paths toward the survivors, assisting in better understanding the current situation in terms of communication or transport disruption. Recently, Qadir et al. [181] compared four state-of-the-art metaheuristic algorithms for disaster management using UAV swarm in the context of smart cities. The algorithms are designed in such a way to provide obstacle-free efficient paths for UAVs in a complex environment. Figure 5 illustrates the best cost vs. iteration comparison between Particle Swarm Optimization (PSO), Flower Pollination Algorithm (FPA), Grasshopper Optimization (GHO), and Smart Flower Optimization Algorithm (SFOA). Figure 6 shows the trajectory optimization between these algorithms from start to endpoints having obstacles in the complex environment. For this complex case, Table III shows that the SFOA algorithm outperforms the other algorithms having a computation time of 109.42 s with the distance covered as 10.971 km.

![](images/2dd0486d8a94c0eadaf7f24cca3c10f1743ffdbee93d86e61e4a07071e975610.jpg)  
Fig. 5. Cost vs. number of iterations for UAVs-based disaster management.

TABLE III  
COMPARISON FOR THE COMPLEX CASE
<table><tr><td rowspan="2">Metaheuristic algorithm</td><td colspan="2">Complex Case</td></tr><tr><td>Path length (km)</td><td>Computational t (s)</td></tr><tr><td>PSO</td><td>14.547</td><td>126.210</td></tr><tr><td>FPA</td><td>13.892</td><td>119.191</td></tr><tr><td>GHO</td><td>13.2889</td><td>113.568</td></tr><tr><td>SFOA</td><td>10.9719</td><td>109.42</td></tr></table>

## E. Connecting the Unconnected

In the digital world, every individual should be able to live, learn, work, and participate. However, there is a gap between regions with access to communication services and those without restricted access. Hence, the digital divide must be bridged to make the world more resilient and inclusive. The situation is much worse in the least developed countries, where an average of two out of every ten people have connectivity. The question is how to reach people at risk of being left behind? Recent research in telecommunication recommends the development of aerial networks in rural areas to connect the unconnected since connectivity is no longer a luxury but a lifeline. In this context, the swarm of UAVs is a viable solution to provide coverage in unconnected regions, creating a flying ad hoc network (FANET) [182]. Bringing aerial networksbased connectivity, especially in rural and underserved areas, can enable various applications, such as online education, smart agriculture, e-health, and an efficient supply chain.

![](images/997070d15ec1b0777dfb605c7bd28c118ff1bc23eb9e2472df04ffb409eab2dc.jpg)  
Fig. 6. Comparison between metaheuristic algorithms (a)SFOA (b)GHO (c)FPA (d)PSO.

In addition to the wide range of opportunities in rural areas, FANET also brings significant benefits in realizing the smart city concept by enabling seamless connectivity. UAV-assisted applications for intelligent traffic monitoring, key infrastructures management and monitoring development work regularly can enhance the lives of its residents by providing efficient infrastructure and services at a reduced cost [142], [153], [154]. For example, UAVs can considerably influence the construction industry by incorporating new X-ray technology to help craft high-resolution 3D maps of objects through Wi-Fi. X-ray technology can also create models of areas hidden behind walls or other barriers to give workers more important information to monitor dangerous structures that could harm workers or the general public. Moreover, collaborative UAVs can help in the recovery of the network in case of disasters [183] and can also improve coverage for underserved regions, such as maritime networks [184].

## V. FUTURE RESEARCH DIRECTIONS

Collaborative UAVs are the new future and can play a significant role in serving different real-world applications. In this article, we reviewed various aspects of collaborative UAVs, including communication, control, and collaboration requirements. However, there are still many issues with establishing an efficient swarm of UAVs to perform coordinated tasking. Therefore, in this section, we highlight a few exciting future directions as summarized in Table IV.

## A. Trajectory Optimization and Scheduling

UAV trajectory optimization in a complex environment depends on the cost associated with the flight and the time it takes to reach the destination. In the dense urban environment, UAV trajectory planning needs to consider several important issues (e.g., signal multipath interference, obstruction, or attenuation) as UAVs fly at relatively lower altitude in the presence of many natural and man-made obstacles [190]. Moreover, trajectory planning in complex environments also faces various challenges from the navigation point of view that compromises mission autonomy, control and planning functionalities that degrade UAV performance for smart city applications such as environmental inspection and monitoring, mobility of people and goods and traffic management. Therefore, the challenges associated with trajectory optimization and scheduling (such as accurate prediction of UAV trajectory, modeling the safety of UAV flight, and the ordering and timing decisions for UAV) need to be mathematically modeled to minimize the traveling time and battery consumption. In this regard, metaheuristic algorithms can be investigated for UAV trajectory optimization and time scheduling for future insights.

## B. Integration of Federated Learning

Machine learning (ML) is an emerging field contributing to several applications in collaborative UAV tasks. ML, a sub-field of Artificial Intelligence (AI), uses state-of-theart techniques to design algorithms that work closely with human nature and are more efficient. Owing to the diversified applications of ML, the designed algorithms are timeconsuming and computationally complex as well. To address these constraints, there is a need to develop resource-aware Federated Learning (FL) architecture that can address computational complexity, limited onboard memory, and high latency limitations for collaborative UAVs. Moreover, collaborative UAVs will provide seamless and reliable communication while distributing the tasks, requiring an energy-efficient approach. In this context, trajectory optimization and the role of FL need to be further researched in helping to create a practical framework where UAVs can collaborate without any energy constraint, which is still a big challenge open for further investigation.

TABLE IV  
SUMMARY OF FUTURE RESEARCH DIRECTIONS
<table><tr><td>Author Year</td><td colspan="2">Contribution</td><td>Challenges</td><td>Possible Future Direction</td></tr><tr><td>Qadir et al., 2022 [181]</td><td>Trajectory Scheduling</td><td>Optimization and</td><td>Computation time and complexity</td><td>Proposing different metaheuristic algorithms for UAV trajectory op- timization</td></tr><tr><td>Nguyen et al., 2021 [185]</td><td>Integration of Federated learning</td><td></td><td>Performance accuracy and com- putational complexity for machine learning algorithms</td><td>Incorporating resource aware Fed- erated Learning architecture for minimizing computational com- plexity</td></tr><tr><td>Wang et al., 2022 [186]</td><td>Cellular Integration</td><td></td><td>Deployment of UAV and associa- tion schemes</td><td>Enhancing the battery life by min- imizing the transmission power consumption of UAVs</td></tr><tr><td>Tedeschi et al., 2022 [187]</td><td>Self-organization</td><td></td><td>Collisions with obstacles, neigh- bouring UAVs and data privacy</td><td>Privacy preserving scheme along with collision avoidance algorithms for secure and reliable information</td></tr><tr><td>Sahni et al., 2021 [188]</td><td>edge computing)</td><td>Collaborative task completion (Collaborative Task Offloading for</td><td>Network congestion and perfor- mance delay</td><td>sharing Implementing the collaborative edge computing (CEC) for computational resource optimization between different</td></tr><tr><td>Yang et al., 2021 [189]</td><td>Energy-efficiency</td><td></td><td>Wireless transmission and local computation</td><td>edge devices and sharing data securely Developing Hybrid iterative algo- rithm along with the proactive ap- proach for power optimization aid- ing wireless transmission</td></tr></table>

## C. Cellular Integration

UAV deployment and alternative association schemes are the real backbones for providing UAV-integrated cellular coverage. In the dense urban environment where network connectivity is affected by tall buildings, bridges and tunnels, UAV-integrated cellular coverage can enhance the network connectivity for Vehicular ad hoc networks (VANETs) and optimize the selection of the fastest route. While during a natural disaster, when the communication architecture is destroyed, or no other modes of communication are available, UAV-integrated cellular coverage can provide a self-sustaining infrastructure to provide surveillance or relief services. However, for large-scale cellular integration, it is necessary to understand the bandwidth, range, speed, cost, and power requirements of the communication technology to enable UAV-integrated cellular networks [3]. Existing studies also emphasized investigating low latency and high data rate ultrareliable communication requirements for collaborative UAV communication.

## D. Self-Organization

Self-organization and automation in collaborative UAVs can perform data aggregation, management, privacy preservation, and path optimization. In complex urban environments, the use of UAV-based applications is exponentially growing for every domain of life as UAVs with self-organizing capabilities can develop a self-sustainable network to complete complex operations in reduced time with better efficiency. For example, a swarm of UAVs can self-organize to work independently to monitor a large agricultural field without taking frequent instructions from the central base station. Similarly, UAVs with self-organizing capabilities can provide cellular coverage or disaster relief services to help the victims during a natural disaster. However, achieving self-organization in a swarm of UAVs using distributed, hybrid and centralized methods is quite challenging. For instance, in a confined environment where UAVs have to hover and collect data for processing and analyzing to make collaborative decisions is a demanding task and needs further investigation. Furthermore, collision avoidance among neighboring UAVs, obstacle avoidance, and data are also daunting challenges that must be addressed. Towards this end, state-of-the-art collision avoidance algorithms integrated with privacy preservation schemes must be adopted for self-organization in the swarm of UAVs.

## E. Collaborative Task Offloading

Task offloading is a serious concern for many applications dealing with different activities in a dedicated space or a complex environment. Nevertheless, it results in performance delays and network congestion. However, collaborative edge computing (CEC) can reduce computational costs and securely transfer data between edge devices [164]. For example, in the digital healthcare environment, edge-computing services help in analyzing the patient’s data at the local server with low latency and security concerns. Accordingly, UAV-based task offloading allows UAVs to provide edge computing services for improved computational efficiency, QoS and reduced latency. Task offloading using UAVs, especially in complex environments, suffers from signal coverage problems that can be solved by optimizing the UAVs’ mobility and improved collaboration strategies. Also, the UAVs can collaborate for task offloading using edge computing or transmitting it to the ground station to further improve the model efficiency.

## F. Energy-Efficiency

Energy scarcity is one of the major concerns for nextgeneration wireless communication systems. In a collaborative

UAV network, the UAVs transmit data and retrieve information at the energy cost consumed by batteries. For example, UAVbased long-term surveillance requires UAVs placement for longer hours, leading to a massive amount of video data generation that needs to be transmitted, consuming considerable power resources. Thanks to the emerging concept of Tethered UAVs, the battery problem is now solved at the expense of limited mobility and coverage. However, in various UAVbased applications for emergencies, energy is still a primary issue; for instance, during disaster management, UAVs are required to monitor, scan, and collect videos/images to notify the authorities for relief operations. Thus, they need enough power resources to enable efficient management and rescue operations. Moreover, developing optimization algorithms that optimize the hovering, sensing time, and power for UAVs is needed to further improve the network’s energy efficiency.

## VI. CONCLUSION

The importance of collaborative UAVs has proliferated to advance their autonomy and coordination for a wide range of applications. At the same time, developing collaborative UAVs faces various challenges concerning communication, control, and collective decision-making. Therefore, this review thoroughly studies the potential and challenges of collaborative UAVs to highlight the state-of-the-art developments. We comprehensively discuss the existing literature to summarize collaborative tasks such as trajectory formation, target localization, data collection, and cooperative decisions that advance the multi-UAV system’s performance. Moreover, we also explore the real-world application of UAV systems and highlight their role in advanced monitoring, surveillance, and management. Towards the end, we provide possible future directions that need attention for realizing the broader concept of collaborative UAVs. In a nutshell, this review offers an indepth discussion for researchers and engineers to understand the collaborative aspect of a swarm of UAVs for designing an efficient network architecture.

## REFERENCES

[1] L. Zhang et al., “A survey on 5G millimeter wave communications for UAV-assisted wireless networks,” IEEE Access, vol. 7, pp. 117460–117504, 2019.

[2] Z. Ullah, F. Al-Turjman, and L. Mostarda, “Cognition in UAV-aided 5G and beyond communications: A survey,” IEEE Trans. Cognit. Commun. Netw., vol. 6, no. 3, pp. 872–891, Sep. 2020.

[3] A. Sharma et al., “Communication and networking technologies for UAVs: A survey,” J. Netw. Comput. Appl., vol. 168, Oct. 2020, Art. no. 102739.

[4] Z. Haider et al., “A novel cooperative relaying-based vertical handover technique for unmanned aerial vehicles,” Secur. Commun. Netw., vol. 2022, pp. 1–16, Sep. 2022.

[5] C. Torresan et al., “Forestry applications of UAVs in Europe: A review,” Int. J. Remote Sens., vol. 38, nos. 8–10, pp. 2427–2447, 2017.

[6] H. Shakhatreh et al., “Unmanned aerial vehicles (UAVs): A survey on civil applications and key research challenges,” IEEE Access, vol. 7, pp. 48572–48634, 2019.

[7] G. Pajares, “Overview and current status of remote sensing applications based on unmanned aerial vehicles (UAVs),” Photogramm. Eng. Remote Sens., vol. 81, no. 4, pp. 281–330, 2015.

[8] M. Erdelj, M. Król, and E. Natalizio, “Wireless sensor networks and multi-UAV systems for natural disaster management,” Comput. Netw., vol. 124, pp. 72–86, Sep. 2017.

[9] R. Shakeri et al., “Design challenges of multi-UAV systems in cyber-physical applications: A comprehensive survey and future directions,” IEEE Commun. Surveys Tuts., vol. 21, no. 4, pp. 3340–3385, 4th Quart. 2019.

[10] G. Chmaj and H. Selvaraj, “Distributed processing applications for UAV/drones: A survey,” in Progress in Systems Engineering. Switzerland: Springer, 2015, pp. 449–454.

[11] J. Sun, J. Tang, and S. Lao, “Collision avoidance for cooperative UAVs with optimized artificial potential field algorithm,” IEEE Access, vol. 5, pp. 18382–18390, 2017.

[12] P. Dinh, T. M. Nguyen, S. Sharafeddine, and C. Assi, “Joint location and beamforming design for cooperative UAVs with limited storage capacity,” IEEE Trans. Commun., vol. 67, no. 11, pp. 8112–8123, Nov. 2019.

[13] G. Sun et al., “Collaborative beamforming for UAV networks exploiting swarm intelligence,” IEEE Wireless Commun., vol. 29, no. 4, pp. 10–17, Aug. 2022.

[14] G. Sun, J. Li, Y. Liu, S. Liang, and H. Kang, “Time and energy minimization communications based on collaborative beamforming for UAV networks: A multi-objective optimization method,” IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3555–3572, Nov. 2021.

[15] L. Zhou, S. Leng, Q. Liu, and Q. Wang, “Intelligent UAV swarm cooperation for multiple targets tracking,” IEEE Internet Things J., vol. 9, no. 1, pp. 743–754, Jan. 2022.

[16] S. Xiao, T. Li, C. Tang, and Y. Cao, “Coverage adaptive optimization algorithm of static-sensor networks for target discovery,” Chin. J. Electron., vol. 28, no. 2, pp. 398–403, Mar. 2019.

[17] Q. Zhang, M. Jiang, Z. Feng, W. Li, W. Zhang, and M. Pan, “IoT enabled UAV: Network architecture and routing algorithm,” IEEE Internet Things J., vol. 6, no. 2, pp. 3727–3742, Apr. 2019.

[18] A. Mukherjee, S. Misra, V. S. P. Chandra, and N. S. Raghuwanshi, “ECoR: Energy-aware collaborative routing for task offload in sustainable UAV swarms,” IEEE Trans. Sustain. Comput., vol. 5, no. 4, pp. 514–525, Oct. 2020.

[19] M. F. Khan, K.-L.-A. Yau, R. M. Noor, and M. A. Imran, “Routing schemes in FANETs: A survey,” Sensors, vol. 20, no. 1, p. 38, Dec. 2019.

[20] I. Jawhar, N. Mohamed, J. Al-Jaroodi, D. P. Agrawal, and S. Zhang, “Communication and networking of UAV-based systems: Classification and associated architectures,” J. Netw. Comput. Appl., vol. 84, pp. 93–108, Apr. 2017.

[21] B. Li, Z. Fei, and Y. Zhang, “UAV communications for 5G and beyond: Recent advances and future trends,” IEEE Internet Things J., vol. 6, no. 2, pp. 2241–2263, Apr. 2019.

[22] Y. Zeng, Q. Wu, and R. Zhang, “Accessing from the sky: A tutorial on UAV communications for 5G and beyond,” Proc. IEEE, vol. 107, no. 12, pp. 2327–2375, Mar. 2019.

[23] M. Marchese, A. Moheddine, and F. Patrone, “IoT and UAV integration in 5G hybrid terrestrial-satellite networks,” Sensors, vol. 19, no. 17, p. 3704, Aug. 2019.

[24] M. Mozaffari, W. Saad, M. Bennis, Y.-H. Nam, and M. Debbah, “A tutorial on UAVs for wireless networks: Applications, challenges, and open problems,” IEEE Commun. Surveys Tuts., vol. 21, no. 3, pp. 2334–2360, 3rd Quart., 2019.

[25] A. I. Hentati and L. C. Fourati, “Comprehensive survey of UAVs communication networks,” Comput. Standards Interfaces, vol. 72, Oct. 2020, Art. no. 103451.

[26] A. A. Khuwaja, Y. Chen, N. Zhao, M.-S. Alouini, and P. Dobbins, “A survey of channel modeling for UAV communications,” IEEE Commun. Surveys Tuts., vol. 20, no. 4, pp. 2804–2821, 4th Quart., 2018.

[27] C. Yan, L. Fu, J. Zhang, and J. Wang, “A comprehensive survey on UAV communication channel modeling,” IEEE Access, vol. 7, pp. 107769–107792, 2019.

[28] L. Gupta, R. Jain, and G. Vaszkun, “Survey of important issues in UAV communication networks,” IEEE Commun. Surveys Tuts., vol. 18, no. 2, pp. 1123–1152, 2nd Quart., 2016.

[29] A. Fotouhi et al., “Survey on UAV cellular communications: Practical aspects, standardization advancements, regulation, and security challenges,” IEEE Commun. Surveys Tuts., vol. 21, no. 4, pp. 3417–3442, 4th Quart., 2019.

[30] D. Popescu, F. Stoican, G. Stamatescu, O. Chenaru, and L. Ichim, “A survey of collaborative UAV–WSN systems for efficient monitoring,” Sensors, vol. 19, no. 21, p. 4690, Oct. 2019.

[31] H. Nawaz, H. M. Ali, and A. A. Laghari, “UAV communication networks issues: A review,” Arch. Comput. Methods Eng., vol. 28, no. 3, pp. 1349–1369, May 2021.

[32] S. H. Alsamhi et al., “Green Internet of Things using UAVs in B5G networks: A review of applications and strategies,” Ad Hoc Netw., vol. 117, Jun. 2021, Art. no. 102505.

[33] L. Shi, N. J. H. Marcano, and R. H. Jacobsen, “A review on communication protocols for autonomous unmanned aerial vehicles for inspection application,” Microprocessors Microsyst., vol. 86, Oct. 2021, Art. no. 104340.

[34] P. S. Bithas, E. T. Michailidis, N. Nomikos, D. Vouyioukas, and A. G. Kanatas, “A survey on machine-learning techniques for UAVbased communications,” Sensors, vol. 19, no. 23, p. 5170, 2019.

[35] S. Hayat, E. Yanmaz, and R. Muzaffar, “Survey on unmanned aerial vehicle networks for civil applications: A communications viewpoint,” IEEE Commun. Surveys Tuts., vol. 18, no. 4, pp. 2624–2661, 4th Quart., 2016.

[36] T. Adão et al., “Hyperspectral imaging: A review on UAV-based sensors, data processing and applications for agriculture and forestry,” Remote Sens., vol. 9, no. 11, p. 1110, 2017.

[37] L. Geng, Y. F. Zhang, J. J. Wang, J. Y. H. Fuh, and S. H. Teo, “Mission planning of autonomous UAVs for urban surveillance with evolutionary algorithms,” in Proc. 10th IEEE Int. Conf. Control Autom. (ICCA), Jun. 2013, pp. 828–833.

[38] P. Chamoso, A. González-Briones, A. Rivas, F. Bueno De Mata, and J. Corchado, “The use of drones in Spain: Towards a platform for controlling UAVs in urban environments,” Sensors, vol. 18, no. 5, p. 1416, May 2018.

[39] H. Baek and J. Lim, “Design of future UAV-relay tactical data link for reliable UAV control and situational awareness,” IEEE Commun. Mag., vol. 56, no. 10, pp. 144–150, Oct. 2018.

[40] M. S. Mahmoud, M. O. Oyedeji, and Y. Xia, “Path planning in autonomous aerial vehicles,” in Advanced Distributed Consensus for Multiagent Systems, M. S. Mahmoud, M. O. Oyedeji, and Y. Xia, Eds. New York, NY, USA: Academic, 2021, ch. 10, pp. 331–362. [Online]. Available: https://www.sciencedirect.com/ science/article/pii/B9780128211861000180

[41] P. McEnroe, S. Wang, and M. Liyanage, “A survey on the convergence of edge computing and AI for UAVs: Opportunities and challenges,” IEEE Internet Things J., vol. 9, no. 17, pp. 15435–15459, Sep. 2022.

[42] C. T. Cicek, H. Gultekin, B. Tavli, and H. Yanikomeroglu, “UAV base station location optimization for next generation wireless networks: Overview and future research directions,” in Proc. 1st Int. Conf. Unmanned Vehicle Syst.-Oman (UVS), Feb. 2019, pp. 1–6.

[43] Y. Wang, W. Feng, J. Wang, and T. Q. S. Quek, “Hybrid satellite-UAV-terrestrial networks for 6G ubiquitous coverage: A maritime communications perspective,” IEEE J. Sel. Areas Commun., vol. 39, no. 11, pp. 3475–3490, Nov. 2021.

[44] C. A. Grazia et al., “Integration between terrestrial and satellite networks: The PPDR-TC vision,” in Proc. IEEE 10th Int. Conf. Wireless Mobile Comput., Netw. Commun. (WiMob), Oct. 2014, pp. 77–84.

[45] J. Zhang, B. Evans, M. A. Imran, X. Zhang, and W. Wang, “Green hybrid satellite terrestrial networks: Fundamental trade-off analysis,” in Proc. IEEE 83rd Veh. Technol. Conf. (VTC Spring), May 2016, pp. 1–5.

[46] N. Hosseini, H. Jamal, J. Haque, T. Magesacher, and D. W. Matolak, “UAV command and control, navigation and surveillance: A review of potential 5G and satellite systems,” in Proc. IEEE Aerosp. Conf., Mar. 2019, pp. 1–10.

[47] N. Saeed, T. Y. Al-Naffouri, and M.-S. Alouini, “Around the world of IoT/climate monitoring using Internet of X-Things,” IEEE Internet Things Mag., vol. 3, no. 2, pp. 82–83, Jun. 2020.

[48] J. Zhao, F. Gao, G. Ding, T. Zhang, W. Jia, and A. Nallanathan, “Integrating communications and control for UAV systems: Opportunities and challenges,” IEEE Access, vol. 6, pp. 67519–67527, 2018.

[49] E. Haas, “Aeronautical channel modeling,” IEEE Trans. Veh. Technol., vol. 51, no. 2, pp. 254–264, Mar. 2002.

[50] D. W. Matolak and R. Sun, “Air–ground channel characterization for unmanned aircraft systems—Part I: Methods, measurements, and models for over-water settings,” IEEE Trans. Veh. Technol., vol. 66, no. 1, pp. 26–44, Jan. 2017.

[51] Y. Zeng, R. Zhang, and T. J. Lim, “Wireless communications with unmanned aerial vehicles: Opportunities and challenges,” IEEE Commun. Mag., vol. 54, no. 5, pp. 36–42, May 2016.

[52] F. A. D’Oliveira, F. C. L. D. Melo, and T. C. Devezas, “High-altitude platforms–present situation and technology trends,” J. Aerosp. Technol. Manage., vol. 8, no. 3, pp. 249–262, Aug. 2016.

[53] S. Morosi, S. Jayousi, E. Falletti, and G. Araniti, “Cooperative strategies in satellite assisted emergency services,” Int. J. Satell. Commun Netw., vol. 31, no. 3, pp. 141–156, May 2013.

[54] F. Dong, H. Li, X. Gong, Q. Liu, and J. Wang, “Energy-efficient transmissions for remote wireless sensor networks: An integrated HAP/satellite architecture for emergency scenarios,” Sensors, vol. 15, no. 9, pp. 22266–22290, Sep. 2015.

[55] D. Yuniarti, “Regulatory challenges of broadband communication services from high altitude platforms (HAPs),” in Proc. Int. Conf. Inf. Commun. Technol. (ICOIACT), Mar. 2018, pp. 919–922.

[56] D. He, S. Chan, and M. Guizani, “Communication security of unmanned aerial vehicles,” IEEE Wireless Commun., vol. 24, no. 4, pp. 134–139, Aug. 2017.

[57] Z. Becvar, M. Vondra, P. Mach, J. Plachy, and D. Gesbert, “Performance of mobile networks with UAVs: Can flying base stations substitute ultra-dense small cells?” in Proc. Eur. Wireless, 23th Eur. Wireless Conf. Dresden, Germany: VDE, 2017, pp. 1–7.

[58] G. Militaru, D. Popescu, and L. Ichim, “UAV-to-UAV communication options for civilian applications,” in Proc. 26th Telecommun. Forum (TELFOR), Nov. 2018, pp. 1–4.

[59] M. M. Azari, G. Geraci, A. Garcia-Rodriguez, and S. Pollin, “UAVto-UAV communications in cellular networks,” IEEE Trans. Wireless Commun., vol. 19, no. 9, pp. 6130–6144, Sep. 2020.

[60] Y. Zeng, J. Lyu, and R. Zhang, “Cellular-connected UAV: Potential, challenges, and promising technologies,” IEEE Wireless Commun., vol. 26, no. 1, pp. 120–127, Feb. 2019.

[61] N. Xia, H.-H. Chen, and C.-S. Yang, “Emerging technologies for machine-type communication networks,” IEEE Netw., vol. 34, no. 1, pp. 214–222, Jan. 2020.

[62] S. Khan, M. Zeeshan, and Y. Ayaz, “Implementation and analysis of MultiCode MultiCarrier code division multiple access (MC–MC CDMA) in IEEE 802.11 ah for UAV swarm communication,” Phys. Commun., vol. 42, Oct. 2020, Art. no. 101159.

[63] M. Jouhari, E. Mehdi Amhoud, N. Saeed, and M.-S. Alouini, “A survey on scalable LoRaWAN for massive IoT: Recent advances, potentials, and challenges,” 2022, arXiv:2202.11082.

[64] M. Behjati, A. B. M. Noh, H. A. H. Alobaidy, M. A. Zulkifley, R. Nordin, and N. F. Abdullah, “LoRa communications as an enabler for Internet of Drones towards large-scale livestock monitoring in rural farms,” Sensors, vol. 21, no. 15, p. 5044, Jul. 2021.

[65] W. Fawaz, C. Abou-Rjeily, and C. Assi, “UAV-aided cooperation for FSO communication systems,” IEEE Commun. Mag., vol. 56, no. 1, pp. 70–75, Aug. 2018.

[66] V. R. Nallagonda and P. Krishnan, “Performance analysis of FSO based inter-UAV communication systems,” Opt. Quantum Electron., vol. 53, no. 4, pp. 1–20, Apr. 2021.

[67] A. K. Majumdar, Advanced Free Space Optics (FSO): A Systems Approach, vol. 186. New York, NY, USA: Springer, 2014.

[68] N. Saeed, A. Elzanaty, H. Almorad, H. Dahrouj, T. Y. Al-Naffouri, and M.-S. Alouini, “CubeSat communications: Recent advances and future challenges,” IEEE Commun. Surveys Tuts., vol. 22, no. 3, pp. 1839–1862, 3rd Quart., 2020.

[69] M. F. S. Rabelo, A. S. Brandao, and M. Sarcinelli-Filho, “Landing a UAV on static or moving platforms using a formation controller,” IEEE Syst. J., vol. 15, no. 1, pp. 37–45, Mar. 2021.

[70] J. Ghommam and M. Saad, “Autonomous landing of a quadrotor on a moving platform,” IEEE Trans. Aerosp. Electron. Syst., vol. 53, no. 3, pp. 1504–1519, Jun. 2017.

[71] N. Saeed, T. Y. Al-Naffouri, and M.-S. Alouini, “Wireless communication for flying cars,” Frontiers Commun. Netw., vol. 2, p. 16, Jun. 2021.

[72] H. Gu, X. Lyu, Z. Li, S. Shen, and F. Zhang, “Development and experimental verification of a hybrid vertical take-off and landing (VTOL) unmanned aerial vehicle(UAV),” in Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS), Jun. 2017, pp. 160–169.

[73] F. Çakici and M. K. Leblebicioglu, “Control system design of a vertical˘ take-off and landing fixed-wing UAV,” IFAC-PapersOnLine, vol. 49, no. 3, pp. 267–272, 2016.

[74] S. Kyristsis et al., “Towards autonomous modular UAV missions: The detection, geo-location and landing paradigm,” Sensors, vol. 16, no. 11, p. 1844, Nov. 2016.

[75] O. Araar, N. Aouf, and I. Vitanov, “Vision based autonomous landing of multirotor UAV on moving platform,” J. Intell. Robot. Syst., vol. 85, no. 2, pp. 369–384, 2017.

[76] T. Yang et al., “A ground-based near infrared camera array system for UAV auto-landing in GPS-denied environment,” Sensors, vol. 16, no. 9, p. 1393, 2016.

[77] K. M. Thu and A. I. Gavrilov, “Designing and modeling of quadcopter control system using L1 adaptive control,” Proc. Comput. Sci., vol. 103, pp. 528–535, Oct. 2017.

[78] D. Gheorghita, I. Vintu, L. Mirea, and C. Braescu, “Quadcopter control system,” in Proc. 19th Int. Conf. Syst. Theory, Control Comput. (ICSTCC), Oct. 2015, pp. 421–426.

[79] G. H. Elkaim, F. A. P. Lie, and D. Gebre-Egziabher, “Principles of guidance, navigation, and control of UAVs,” in Handbook Unmanned Aerial Vehicles. Dordrecht, The Netherlands: Springer, 2015, pp. 347–380.

[80] J. Kwak and Y. Sung, “Autonomous UAV flight control for GPS-based navigation,” IEEE Access, vol. 6, pp. 37947–37955, 2018.

[81] J. D. Barton, “Fundamentals of small unmanned aircraft flight,” Johns Hopkins APL Tech. Dig., vol. 31, no. 2, pp. 132–149, 2012.

[82] A. Frank, J. McGrew, M. Valenti, D. Levine, and J. How, “Hover, transition, and level flight control design for a single-propeller indoor airplane,” in Proc. AIAA Guid., Navigat. Control Conf. Exhib., Aug. 2007, p. 6318.

[83] J. R. Azinheira and A. Moutinho, “Hover control of an UAV with backstepping design including input saturations,” IEEE Trans. Control Syst. Technol., vol. 16, no. 3, pp. 517–526, May 2008.

[84] O. Spinka, S. Kroupa, and Z. Hanzálek, “Control system for unmanned aerial vehicles,” in Proc. 5th IEEE Int. Conf. Ind. Informat., vol. 1, Jun. 2007, pp. 455–460.

[85] B. Kada and Y. Ghazzawi, “Robust PID controller design for an UAV flight control system,” in Proc. World Congr. Eng. Comput. Sci., vol. 2, 2011, pp. 1–6.

[86] H. Noshahri and H. Kharrati, “PID controller design for unmanned aerial vehicle using genetic algorithm,” in Proc. IEEE 23rd Int. Symp. Ind. Electron. (ISIE), Jun. 2014, pp. 213–217.

[87] K. Y. Chee and Z. W. Zhong, “Control, navigation and collision avoidance for an unmanned aerial vehicle,” Sens. Actuators A, Phys., vol. 190, pp. 66–76, Feb. 2013.

[88] J. N. Yasin, S. A. S. Mohamed, M.-H. Haghbayan, J. Heikkonen, H. Tenhunen, and J. Plosila, “Unmanned aerial vehicles (UAVs): Collision avoidance systems and approaches,” IEEE Access, vol. 8, pp. 105139–105155, 2020.

[89] N. Gageik, P. Benz, and S. Montenegro, “Obstacle detection and collision avoidance for a UAV with complementary low-cost sensors,” IEEE Access, vol. 3, pp. 599–609, 2015.

[90] Y. Lin and S. Saripalli, “Sampling-based path planning for UAV collision avoidance,” IEEE Trans. Intell. Transp. Syst., vol. 18, no. 11, pp. 3179–3192, Nov. 2017.

[91] N. Lin, L. Fu, L. Zhao, G. Min, A. Al-Dubai, and H. Gacanin, “A novel multimodal collaborative drone-assisted VANET networking model,” IEEE Trans. Wireless Commun., vol. 19, no. 7, pp. 4919–4933, Jul. 2020.

[92] A. Sathyan, N. D. Ernest, and K. Cohen, “An efficient genetic fuzzy approach to UAV swarm routing,” Unmanned Syst., vol. 4, no. 2, pp. 117–127, Apr. 2016.

[93] G. P. Sadrollah, J. C. Barca, A. I. Khan, J. Eliasson, and I. Senthooran, “A distributed framework for supporting 3D swarming applications,” in Proc. Int. Conf. Comput. Inf. Sci. (ICCOINS), Jun. 2014, pp. 1–5.

[94] B. J. O. de Souza and M. Endler, “Coordinating movement within swarms of UAVs through mobile networks,” in Proc. IEEE Int. Conf. Pervasive Comput. Commun. Workshops (PerCom Workshops), Mar. 2015, pp. 154–159.

[95] W. Chen, B. Liu, H. Huang, S. Guo, and Z. Zheng, “When UAV swarm meets edge-cloud computing: The QoS perspective,” IEEE Netw., vol. 33, no. 2, pp. 36–43, Mar./Apr. 2019.

[96] M. Y. Arafat and S. Moh, “Localization and clustering based on swarm intelligence in UAV networks for emergency communications,” IEEE Internet Things J., vol. 6, no. 5, pp. 8958–8976, Oct. 2019.

[97] W. Koch, R. Mancuso, R. West, and A. Bestavros, “Reinforcement learning for UAV attitude control,” ACM Trans. Cyber-Phys. Syst., vol. 3, no. 2, pp. 1–21, Feb. 2019.

[98] A. T. Azar et al., “Drone deep reinforcement learning: A review,” Electronics, vol. 10, no. 9, p. 999, 2021.

[99] Z. Xia et al., “Multi-agent reinforcement learning aided intelligent UAV swarm for target tracking,” IEEE Trans. Veh. Technol., vol. 71, no. 1, pp. 931–945, Jan. 2022.

[100] J. Hu, L. Wang, T. Hu, C. Guo, and Y. Wang, “Autonomous maneuver decision making of dual-UAV cooperative air combat based on deep reinforcement learning,” Electronics, vol. 11, no. 3, p. 467, Feb. 2022.

[101] C. Wang, J. Wang, Y. Shen, and X. Zhang, “Autonomous navigation of UAVs in large-scale complex environments: A deep reinforcement learning approach,” IEEE Trans. Veh. Technol., vol. 68, no. 3, pp. 2124–2136, Mar. 2019.

[102] B. Zhang, Z. Mao, W. Liu, and J. Liu, “Geometric reinforcement learning for path planning of UAVs,” J. Intell. Robotic Syst., vol. 77, no. 2, pp. 391–409, Feb. 2015.

[103] U. Challita, W. Saad, and C. Bettstetter, “Interference management for cellular-connected UAVs: A deep reinforcement learning approach,” IEEE Trans. Wireless Commun., vol. 18, no. 4, pp. 2125–2140, Apr. 2019.

[104] C. H. Liu, Z. Chen, J. Tang, J. Xu, and C. Piao, “Energy-efficient UAV control for effective and fair communication coverage: A deep reinforcement learning approach,” IEEE J. Sel. Areas Commun., vol. 36, no. 9, pp. 2059–2070, Sep. 2018.

[105] J. Hu, H. Zhang, L. Song, Z. Han, and H. V. Poor, “Reinforcement learning for a cellular Internet of UAVs: Protocol design, trajectory control, and resource management,” IEEE Wireless Commun., vol. 27, no. 1, pp. 116–123, Feb. 2020.

[106] J. Cui, Y. Liu, and A. Nallanathan, “Multi-agent reinforcement learning-based resource allocation for UAV networks,” IEEE Trans. Wireless Commun., vol. 19, no. 2, pp. 729–743, Feb. 2020.

[107] Y. Zhang, Z. Mou, F. Gao, L. Xing, J. Jiang, and Z. Han, “Hierarchical deep reinforcement learning for backscattering data collection with multiple UAVs,” IEEE Internet Things J., vol. 8, no. 5, pp. 3786–3800, Mar. 2021.

[108] C. Qu, W. Gai, M. Zhong, and J. Zhang, “A novel reinforcement learning based grey wolf optimizer algorithm for unmanned aerial vehicles (UAVs) path planning,” Appl. Soft Comput., vol. 89, Apr. 2020, Art. no. 106099.

[109] I. Mir et al., “A survey of trajectory planning techniques for autonomous systems,” Electronics, vol. 11, no. 18, p. 2801, Sep. 2022.

[110] T. Schouwenaars, J. How, and E. Feron, “Decentralized cooperative trajectory planning of multiple aircraft with hard safety guarantees,” in Proc. AIAA Guid., Navigat., Control Conf. Exhibit, Aug. 2004, p. 5141.

[111] S. Fatima et al., “Data driven model estimation for aerial vehicles: A perspective analysis,” Processes, vol. 10, no. 7, p. 1236, Jun. 2022.

[112] Z. Wei, C. Huang, D. Ding, H. Huang, and H. Zhou, “UCAV formation online collaborative trajectory planning using hp adaptive pseudospectral method,” Math. Problems Eng., vol. 2018, pp. 1–25, Oct. 2018.

[113] Y. Ji, C. Dong, X. Zhu, and Q. Wu, “Fair-energy trajectory planning for multi-target positioning based on cooperative unmanned aerial vehicles,” IEEE Access, vol. 8, pp. 9782–9795, 2020.

[114] Z. Wang, L. Liu, and T. Long, “Minimum-time trajectory planning for multi-unmanned-aerial-vehicle cooperation using sequential convex programming,” J. Guid., Control, Dyn., vol. 40, no. 11, pp. 2976–2982, Nov. 2017.

[115] X. Liu, Z. Shen, and P. Lu, “Entry trajectory optimization by secondorder cone programming,” J. Guid. Control Dyn., vol. 39, no. 2, pp. 227–241, Aug. 2015.

[116] M. Szmuk, B. Acikmese, and A. W. Berning, “Successive convexification for fuel-optimal powered landing with aerodynamic drag and non-convex constraints,” in Proc. AIAA Guid., Navigat., Control Conf., Jan. 2016, p. 0378.

[117] J. Tang, J. Sun, C. Lu, and S. Lao, “Optimized artificial potential field algorithm to multi-unmanned aerial vehicle coordinated trajectory planning and collision avoidance in three-dimensional environment,” Proc. Inst. Mech. Eng., G, J. Aerosp. Eng., vol. 233, no. 16, pp. 6032–6043, 2019.

[118] O. Khatib, “Real-time obstacle avoidance for manipulators and mobile robots,” in Autonomous Robot Vehicles. San Francisco, CA, USA: Springer, 1986, pp. 396–404.

[119] K. Guo, X. Li, and L. Xie, “Ultra-wideband and odometry-based cooperative relative localization with application to multi-UAV formation control,” IEEE Trans. Cybern., vol. 50, no. 6, pp. 2590–2603, Jun. 2020.

[120] Z. Qadir, M. H. Zafar, S. K. R. Moosavi, K. N. Le, and M. A. P. Mahmud, “Autonomous UAV path-planning optimization using metaheuristic approach for predisaster assessment,” IEEE Internet Things J., vol. 9, no. 14, pp. 12505–12514, Jul. 2022.

[121] H. Sarieddeen, N. Saeed, T. Y. Al-Naffouri, and M.-S. Alouini, “Next generation terahertz communications: A rendezvous of sensing, imaging, and localization,” IEEE Commun. Mag., vol. 58, no. 5, pp. 69–75, May 2020.

[122] R. A. Khalil, N. Saeed, and M. Almutiry, “UAVs-assisted passive source localization using robust TDOA ranging for search and rescue,” ICT Exp., early access, May 2022, doi: 10.1016/j.icte.2022.04.011.

[123] X. Fu, H. Bi, and X. Gao, “Multi-UAVs cooperative localization algorithms with communication constraints,” Math. Problems Eng., vol. 2017, pp. 1–8, Jul. 2017.

[124] S. A. A. Shahidian and H. Soltanizadeh, “Optimal trajectories for two UAVs in localization of multiple RF sources,” Trans. Inst. Meas. Control, vol. 38, no. 8, pp. 908–916, Jul. 2016.

[125] Z. Fu, Y. Chen, Y. Ding, and D. He, “Pollution source localization based on multi-UAV cooperative communication,” IEEE Access, vol. 7, pp. 29304–29312, 2019.

[126] W. Lee, H. Bang, and H. Leeghim, “Cooperative localization between small UAVs using a combination of heterogeneous sensors,” Aerosp. Sci. Technol., vol. 27, pp. 105–111, Jun. 2013.

[127] J. Q. Cui et al., “Drones for cooperative search and rescue in postdisaster situation,” in Proc. IEEE 7th Int. Conf. Cybern. Intell. Syst. (CIS) IEEE Conf. Robot., Autom. Mechatronics (RAM), Jul. 2015, pp. 167–174.

[128] S. Mahmoud and N. Mohamed, “Collaborative UAVs cloud,” in Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS), May 2014, pp. 365–373.

[129] D. Popescu, C. Dragana, F. Stoican, L. Ichim, and G. Stamatescu, “A collaborative UAV-WSN network for monitoring large areas,” Sensors, vol. 18, no. 12, p. 4202, Nov. 2018.

[130] Y. Wang, Z. Hu, X. Wen, Z. Lu, and J. Miao, “Minimizing data collection time with collaborative UAVs in wireless sensor networks,” IEEE Access, vol. 8, pp. 98659–98669, 2020.

[131] Y. Luo, Q. Hu, Y. Wang, J. Wang, O. Alfarraj, and A. Tolba, “Revenue optimization of a UAV-fog collaborative framework for remote data collection services,” IEEE Access, vol. 8, pp. 150599–150610, 2020.

[132] Y. Wang et al., “Multi-UAV collaborative data collection for IoT devices powered by battery,” in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), May 2020, pp. 1–6.

[133] D. Popescu, F. Stoican, G. Stamatescu, L. Ichim, and C. Dragana, “Advanced UAV–WSN system for intelligent monitoring in precision agriculture,” Sensors, vol. 20, no. 3, p. 817, 2020.

[134] J. S. Kumar, S. Kumar, M. Choksi, and M. A. Zaveri, “Collaborative data acquisition and processing for post disaster management and surveillance related tasks using UAV-based IoT cloud,” Int. J. Ad Hoc Ubiquitous Comput., vol. 34, no. 4, pp. 216–232, 2020.

[135] P. Schmuck and M. Chli, “Multi-UAV collaborative monocular SLAM,” in Proc. IEEE Int. Conf. Robot. Autom. (ICRA), May 2017, pp. 3863–3870.

[136] D. Liu et al., “Opportunistic data collection in cognitive wireless sensor networks: Air–ground collaborative online planning,” IEEE Internet Things J., vol. 7, no. 9, pp. 8837–8851, Sep. 2020.

[137] T. Shima and S. Rasmussen, UAV Cooperative Decision and Control: Challenges and Practical Approaches. Philadelphia, PA, USA: SIAM, 2009.

[138] Y. Zhao, X. Wang, C. Wang, Y. Cong, and L. Shen, “Systemic design of distributed multi-UAV cooperative decision-making for multitarget tracking,” Auto. Agents Multi-Agent Syst., vol. 33, nos. 1–2, pp. 132–158, Mar. 2019.

[139] J. Capitan, L. Merino, and A. Ollero, “Cooperative decision-making under uncertainties for multi-target surveillance with multiples UAVs,” J. Intell. Robotic Syst., vol. 84, nos. 1–4, pp. 371–386, Dec. 2016.

[140] Y. Ben-Asher, S. Feldman, P. Gurfil, and M. Feldman, “Distributed decision and control for cooperative UAVs using ad hoc communication,” IEEE Trans. Control Syst. Technol., vol. 16, no. 3, pp. 511–516, May 2008.

[141] Z. Qadir, F. Ullah, H. S. Munawar, and F. Al-Turjman, “Addressing disasters in smart cities through UAVs path planning and 5G communications: A systematic review,” Comput. Commun., vol. 168, pp. 114–135, Feb. 2021.

[142] H. Menouar, I. Guvenc, K. Akkaya, A. S. Uluagac, A. Kadri, and A. Tuncer, “UAV-enabled intelligent transportation systems for the smart city: Applications and challenges,” IEEE Commun. Mag., vol. 55, no. 3, pp. 22–28, Mar. 2017.

[143] K. Kuru, “Planning the future of smart cities with swarms of fully autonomous unmanned aerial vehicles using a novel framework,” IEEE Access, vol. 9, pp. 6571–6595, 2021.

[144] Z. Xiong, H. Sheng, W. G. Rong, and D. E. Cooper, “Intelligent transportation systems for smart cities: A progress review,” Science China, vol. 55, no. 12, pp. 2908–2914, 2012.

[145] M. B. Brahim, W. Drira, and F. Filali, “Roadside units placement within city-scaled area in vehicular ad-hoc networks,” in Proc. Int. Conf. Connected Vehicles Expo (ICCVE), 2014, pp. 1010–1016.

[146] C. Zhang, “An UAV-based photogrammetric mapping system for road condition assessment,” Int. Arch. Photogramm. Remote Sens. Spatial Inf. Sci., vol. 37, pp. 627–632, Jul. 2008.

[147] W. Fawaz, “Effect of non-cooperative vehicles on path connectivity in vehicular networks: A theoretical analysis and UAV-based remedy,” Veh. Commun., vol. 11, pp. 12–19, Jan. 2018.

[148] M. A. Khan, W. Ectors, T. Bellemans, D. Janssens, and G. Wets, “UAV-based traffic analysis: A universal guiding framework based on literature survey,” Transp. Res. Proc., vol. 22, pp. 541–550, Jan. 2017.

[149] O. S. Oubbati, N. Chaib, A. Lakas, P. Lorenz, and A. Rachedi, “UAVassisted supporting services connectivity in urban VANETs,” IEEE Trans. Veh. Technol., vol. 68, no. 4, pp. 3944–3951, Apr. 2019.

[150] O. S. Oubbati, A. Lakas, F. Zhou, M. Güne¸s, N. Lagraa, and M. B. Yagoubi, “Intelligent UAV-assisted routing protocol for urban VANETs,” Comput. Commun., vol. 107, pp. 93–111, Jul. 2017.

[151] D. R. Green, J. J. Hagon, C. Gómez, and B. J. Gregory, “Using lowcost UAVs for environmental monitoring, mapping, and modelling: Examples from the coastal zone,” in Coastal Management. Amsterdam, The Netherlands: Elsevier, 2019, pp. 465–501.

[152] H. J. Jumaah, B. Kalantar, A. A. Halin, S. Mansor, N. Ueda, and S. J. Jumaah, “Development of UAV-based PM<sub>2.5</sub> monitoring system,” Drones, vol. 5, no. 3, p. 60, 2021.

[153] J.-I. Hernández-Vega, E. R. Varela, N. H. Romero, C. Hernández-Santos, J. L. S. Cuevas, and D. G. P. Gorham, “Internet of Things (IoT) for monitoring air pollutants with an unmanned aerial vehicle (UAV) in a smart city,” in Smart Technology. Monterrey, Mexico: Springer, 2018, pp. 108–120.

[154] N. Mohamed, J. Al-Jaroodi, I. Jawhar, H. Noura, and S. Mahmoud, “UAVFog: A UAV-based fog computing for Internet of Things,” in Proc. IEEE SmartWorld, Ubiquitous Intell. Comput., Adv. Trusted Comput., Scalable Comput. Commun., Cloud Big Data Comput., Internet People Smart City Innov. (SmartWorld/SCALCOM/UIC/ATC/CBDCom/IOP/SCI), Aug. 2017, pp. 1–8.

[155] Á. Madridano, A. Al-Kaff, P. Flores, D. Martín, and A. De La Escalera, “Software architecture for autonomous and coordinated navigation of UAV swarms in forest and urban firefighting,” Appl. Sci., vol. 11, no. 3, p. 1258, Jan. 2021.

[156] R. Sharma and R. Arya, “UAV based long range environment monitoring system with industry 5.0 perspectives for smart city infrastructure,” Comput. Ind. Eng., vol. 168, Jun. 2022, Art. no. 108066.

[157] A. Giyenko and Y. I. Cho, “Intelligent UAV in smart cities using IoT,” in Proc. 16th Int. Conf. Control, Autom. Syst. (ICCAS), Oct. 2016, pp. 207–210.

[158] R. Cooley, S. Wolf, and M. Borowczak, “Secure and decentralized swarm behavior with autonomous agents for smart cities,” in Proc. IEEE Int. Smart Cities Conf. (ISC2), Sep. 2018, pp. 1–8.

[159] R. Jain, P. Nagrath, N. Thakur, D. Saini, N. Sharma, and D. J. Hemanth, “Towards a smarter surveillance solution: The convergence of smart city and energy efficient unmanned aerial vehicle technologies,” in Development and Future of Internet of Drones (IoD): Insights, Trends and Road Ahead. Switzerland: Springer, 2021, pp. 109–140.

[160] Y. Liu, H. Liu, Y. Tian, and C. Sun, “Reinforcement learning based two-level control framework of UAV swarm for cooperative persistent surveillance in an unknown urban area,” Aerosp. Sci. Technol., vol. 98, Mar. 2020, Art. no. 105671.

[161] Y. Jin, Z. Qian, and W. Yang, “UAV cluster-based video surveillance system optimization in heterogeneous communication of smart cities,” IEEE Access, vol. 8, pp. 55654–55664, 2020.

[162] Z. Ullah, F. Al-Turjman, L. Mostarda, and R. Gagliardi, “Applications of artificial intelligence and machine learning in smart cities,” Comput. Commun., vol. 154, pp. 313–323, Mar. 2020.

[163] N. Thakur, P. Nagrath, R. Jain, D. Saini, N. Sharma, and D. J. Hemanth, “Artificial intelligence techniques in smart cities surveillance using UAVs: A survey,” in Machine Intelligence and Data Analytics for Sustainable Future Smart Cities. Switzerland: Springer, 2021, pp. 329–353.

[164] M. Ishtiaq, N. Saeed, and M. Asif Khan, “Edge computing in IoT: A 6G perspective,” 2021, arXiv:2111.08943.

[165] J. Zheng, T. Yang, H. Liu, T. Su, and L. Wan, “Accurate detection and localization of unmanned aerial vehicle swarms-enabled mobile edge computing system,” IEEE Trans. Ind. Informat., vol. 17, no. 7, pp. 5059–5067, Jul. 2021.

[166] Z. Yang, C. Pan, K. Wang, and M. Shikh-Bahaei, “Energy efficient resource allocation in UAV-enabled mobile edge computing networks,” IEEE Trans. Wireless Commun., vol. 18, no. 9, pp. 4576–4589, Sep. 2019.

[167] S. Jeong, O. Simeone, and J. Kang, “Mobile edge computing via a UAV-mounted cloudlet: Optimization of bit allocation and path planning,” IEEE Trans. Veh. Technol., vol. 67, no. 3, pp. 2049–2063, May 2018.

[168] F. Zhou, Y. Wu, H. Sun, and Z. Chu, “UAV-enabled mobile edge computing: Offloading optimization and trajectory design,” in Proc. IEEE Int. Conf. Commun. (ICC), May 2018, pp. 1–6.

[169] S. Javaid, H. Fahim, Z. Hamid, and F. B. Hussain, “Traffic-aware congestion control (TACC) for wireless multimedia sensor networks,” Multimedia Tools Appl., vol. 77, no. 4, pp. 4433–4452, Feb. 2018.

[170] S. Javaid, S. Zeadally, H. Fahim, and B. He, “Medical sensors and their integration in wireless body area networks for pervasive healthcare delivery: A review,” IEEE Sensors J., vol. 22, no. 5, pp. 3860–3877, Mar. 2022.

[171] X. Li, H. Yao, J. Wang, X. Xu, C. Jiang, and L. Hanzo, “A near-optimal UAV-aided radio coverage strategy for dense urban areas,” IEEE Trans. Veh. Technol., vol. 68, no. 9, pp. 9098–9109, Sep. 2019.

[172] C. Zhan et al., “Completion time and energy optimization in the UAV-enabled mobile-edge computing system,” IEEE Internet Things J., vol. 7, no. 8, pp. 7808–7822, Aug. 2020.

[173] T. Zhang, Y. Xu, J. Loo, D. Yang, and L. Xiao, “Joint computation and communication design for UAV-assisted mobile edge computing in IoT,” IEEE Trans. Wireless Commun., vol. 16, no. 8, pp. 5505–5516, Oct. 2019.

[174] L. Yang, H. Yao, J. Wang, C. Jiang, A. Benslimane, and Y. Liu, “Multi-UAV-enabled load-balance mobile-edge computing for IoT networks,” IEEE Internet Things J., vol. 7, no. 8, pp. 6898–6908, Aug. 2020.

[175] C. Yinka-Banjo and O. Ajayi, “Sky-farmers: Applications of unmanned aerial vehicles (UAV) in agriculture,” in Autonomous Vehicles. London, U.K.: IntechOpen, 2019, pp. 107–128.

[176] R. Dainelli, P. Toscano, S. F. Di Gennaro, and A. Matese, “Recent advances in unmanned aerial vehicle forest remote sensing—A systematic review. Part I: A general framework,” Forests, vol. 12, no. 3, p. 327, Mar. 2021.

[177] Environmental Monitoring and Surveillance Drones Applications. Accessed: Feb. 15, 2022. [Online]. Available: https://resoilfoundation.org/en/innovation-technology/indigenousdrones-deforestation/

[178] R. W. Beard, T. W. McLain, D. B. Nelson, D. Keingston, and D. Johnson, “Decentralized cooperative aerial surveillance using fixedwing miniature UAVs,” Proc. IEEE, vol. 94, no. 7, pp. 1306–1324, Aug. 2006.

[179] J. Grau et al., “Improved accuracy of riparian zone mapping using near ground unmanned aerial vehicle and photogrammetry method,” Remote Sens., vol. 13, no. 10, p. 1997, May 2021.

[180] C. A. F. Ezequiel et al., “UAV aerial imaging applications for postdisaster assessment, environmental management and infrastructure development,” in Proc. Int. Conf. Unmanned Aircr. Syst. (ICUAS), May 2014, pp. 274–283.

[181] Z. Qadir, M. H. Zafar, S. K. R. Moosavi, K. N. Le, and V. W. Tam, “Optimizing UAV path for disaster management in smart cities using metaheuristic algorithms,” in Computational Intelligence for Unmanned Aerial Vehicles Communication Networks, vol. 1033. Switzerland: Springer, 2022, p. 225.

[182] D. F. Cabrera-Castellanos, A. Aragón-Zavala, and G. Castañón-Ávila, “Closing connectivity gap: An overview of mobile coverage solutions for not-spots in rural zones,” Sensors, vol. 21, no. 23, p. 8037, Dec. 2021.

[183] M. Matracia, N. Saeed, M. A. Kishk, and M.-S. Alouini, “Postdisaster communications: Enabling technologies, architectures, and open challenges,” IEEE Open J. Commun. Soc., vol. 3, pp. 1177–1205, 2022.

[184] F. S. Alqurashi, A. Trichili, N. Saeed, B. S. Ooi, and M.-S. Alouini, “Maritime communications: A survey on enabling technologies, opportunities, and challenges,” IEEE Internet Things J., vol. 10, no. 4, pp. 3525–3547, Feb. 2023.

[185] D. C. Nguyen, M. Ding, P. N. Pathirana, A. Seneviratne, J. Li, and H. V. Poor, “Federated learning for Internet of Things: A comprehensive survey,” IEEE Commun. Surveys Tuts., vol. 23, no. 3, pp. 1622–1658, 3rd Quart., 2021.

[186] L. Wang, H. Zhang, S. Guo, and D. Yuan, “Deployment and association of multiple UAVs in UAV-assisted cellular networks with the knowledge of statistical user position,” IEEE Trans. Wireless Commun., vol. 21, no. 8, pp. 6553–6567, Aug. 2022.

[187] P. Tedeschi, S. Sciancalepore, and R. Di Pietro, “PPCA—Privacypreserving collision avoidance for autonomous unmanned aerial vehicles,” IEEE Trans. Dependable Secure Comput., early access, Mar. 16, 2022, doi: 10.1109/TDSC.2022.3159837.

[188] Y. Sahni, J. Cao, L. Yang, and Y. Ji, “Multihop offloading of multiple DAG tasks in collaborative edge computing,” IEEE Internet Things J., vol. 8, no. 6, pp. 4893–4905, Mar. 2021.

[189] Z. Yang, M. Chen, W. Saad, C. S. Hong, and M. Shikh-Bahaei, “Energy efficient federated learning over wireless communication networks,” IEEE Trans. Wireless Commun., vol. 20, no. 3, pp. 1935–1949, Mar. 2020.

[190] F. Causa and G. Fasano, “Multiple UAVs trajectory generation and waypoint assignment in urban environment based on DOP maps,” Aerosp. Sci. Technol., vol. 110, Mar. 2021, Art. no. 106507.

![](images/ed399d4d5aa260e3d6400bfb9f5c849ff949d8f3dc0fd7955c5cf09ae8c6532b.jpg)

Shumaila Javaid received the B.S. degree from COMSATS University, Islamabad, Pakistan, in 2012, the M.S. degree in telecommunication and networking from Bahria University, Islamabad, in 2015, and the Ph.D. degree in computer science from Shaanxi Normal University, China, in 2020. She is currently working as a Post-Doctoral Researcher with Tongji University, Shanghai, China. Her research interests include wireless sensor networks, unmanned aerial vehicles (UAVs), intrabody nanonetworks, robotic communication, neural net-

works, information-centric networks, and wireless networking in general.

![](images/4721260aad4d7b37be42ad10a237d32a200413488ef72f61f390869200070041.jpg)

Nasir Saeed (Senior Member, IEEE) received the B.Sc. degree in telecommunication from the University of Engineering and Technology, Peshawar, Pakistan, in 2009, the M.Sc. degree in satellite navigation from the Politecnico di Torino, Italy, in 2012, and the Ph.D. degree in electronics and communication engineering from Hanyang University, Seoul, South Korea, in 2015. He was an Assistant Professor with the Department of Electrical Engineering, IQRA National University, Peshawar, from 2015 to 2017. From July 2017 to December

2020, he was a Post-Doctoral Research Fellow with the Communication Theory Laboratory, King Abdullah University of Science and Technology (KAUST), Saudi Arabia. He is currently an Associate Professor with the Department of Electrical and Communication Engineering, United Arab Emirates University (UAEU), Al Ain, United Arab Emirates. He has published more than 80 international journals and conference papers. His current research interests include non-conventional communication networks, heterogenous vertical networks, multi-dimensional signal processing, and localization. He is an Associate Editor of the IEEE WIRELESS COMMUNICATIONS LETTERS.

![](images/5d4e93881c74325063311d2b331ef04c93dafb979b98b1863e5c303444936468.jpg)

Zakria Qadir (Graduate Student Member, IEEE) received the M.Sc. degree in sustainable environment and energy systems from Middle East Technical University, Turkey, in 2019. He is currently pursuing the Ph.D. degree in electrical and computer engineering with Western Sydney University, Australia. He is the author/coauthor of more than 35 articles published in renowned journals and conferences. His research interests include trajectory optimization, the Internet of Things, artificial intelligence, machine learning, wireless communication, cybersecurity, and cloud computing.

![](images/e7b630b23d4e592bbd235d613a2654dc69d607605154530936e535323a0d7248.jpg)  
Hamza Fahim received the B.S. and M.S. degrees from the Department of Computer Science, COM-SATS University (CU), Pakistan, in 2012 and 2015, respectively, and the Ph.D. degree in computer science and networks from Xi’an Jiaotong University, China. He is currently associated with Tongji University, Shanghai, China, as a Post-Doctoral Researcher. He is also associated with Ilma University Karachi, Pakistan, as an Assistant Professor. His current research interests include intrabody nanonetworks, software-defined networks, and wireless sensor networks.

![](images/063749fd43e5a47f3afd5e9ae94fdbac8957404f593b4c5634c87536b5feff87.jpg)

Bin He (Member, IEEE) received the B.S. degree in engineering machinery from Jilin University, Changchun, China, in 1996, and the Ph.D. degree in mechanical and electronic control engineering from Zhejiang University, Hangzhou, China, in 2001. From 2001 to 2003, he held post-doctoral research appointments with the State Key Laboratory of Fluid Power Transmission and Control, Zhejiang University. He is currently a Professor with the Department of Control Science and Engineering, Tongji University, Shanghai, China, and the Shanghai Research

Institute for Intelligent Autonomous Systems, Shanghai. His current research interests include intelligent robot control, neural networks, biomimetic microrobots, image processing and fusion, wireless communications, and wireless networks.

![](images/2796709f6052efc25e0ec892a1612c3139ace585cd1293322ac0054dd8df1823.jpg)

Houbing Song (Fellow, IEEE) received the Ph.D. degree in electrical engineering from the University of Virginia, Charlottesville, VA, USA, in August 2012. He is currently a tenured Associate Professor and the Director of the Security and Optimization for Networked Globe Laboratory (SONG Lab, www.SONGLab.us), University of Maryland, Baltimore County (UMBC), Baltimore, MD, USA. Prior to joining UMBC, he was a tenured Associate Professor of electrical engineering and computer science with Embry-Riddle Aeronautical University,

Daytona Beach, FL, USA. His research has been sponsored by federal agencies (including the National Science Foundation, the U.S. Department of Transportation, and the Federal Aviation Administration, among others) and industry. His research has been featured by popular news media outlets, including the IEEE GlobalSpec’s Engineering360, the Association for Uncrewed Vehicle Systems International (AUVSI), Security Magazine, CXOTech Magazine, Fox News, U.S. News and World Report, The Washington Times, and New Atlas. He is the editor of eight books, the author of more than 100 articles, and the inventor of two patents. His research interests include cyber-physical systems/the Internet of Things, cybersecurity and privacy, and AI/machine learning/big data analytics. He is a Senior Member of ACM and an ACM Distinguished Speaker. He was a recipient of more than ten best paper awards from major international conferences, including IEEE CPSCom-2019, IEEE ICII 2019, IEEE/AIAA ICNS 2019, IEEE CBDCom 2020, WASA 2020, AIAA/ IEEE DASC 2021, IEEE GLOBECOM 2021, and IEEE INFOCOM 2022. He has served as an Associate Technical Editor for the IEEE Communications Magazine from 2017 to 2020, an Associate Editor for the IEEE INTERNET OF THINGS JOURNAL since 2020, the IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS since 2021, and the IEEE JOURNAL ON MINIATURIZATION FOR AIR AND SPACE SYSTEMS since 2020. He is a Highly Cited Researcher identified by Clarivate, in 2021 and 2022, and a Top 1000 Computer Scientist identified by Research.com.

![](images/89e3bd29703d084d64e4ecd66a0573c0b3d96803bb52344d749756449112dead.jpg)

Muhammad Bilal (Senior Member, IEEE) received the Ph.D. degree in information and communication network engineering from the School of Electronics and Telecommunications Research Institute (ETRI), Korea University of Science and Technology, in 2017. From 2017 to 2018, he was with Korea University, where he was a Post-Doctoral Research Fellow with the Smart Quantum Communication Center. In 2018, he joined the Hankuk University of Foreign Studies, South Korea, where he is currently an Associate Professor with the Division of

Computer and Electronic Systems Engineering. He is the author/coauthor of more than 100 articles published in renowned journals, one book editorship, three issued U.S. patents, and six Korean patents. His research interests include network optimization, cyber security, the Internet of Things, vehicular networks, information-centric networking, digital twin, artificial intelligence, and cloud/fog computing. He is an Editorial Board Member of the IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYSTEMS, IEEE Future Directions in Technology, Policy, and Ethics Newsletter, Alexandria Engineering Journal (Elsevier), Physical Communication (Elsevier), Computer Systems Science and Engineering, Intelligent Automation and Soft Computing, Frontiers in Communications and Networks, and Frontiers in the Internet of Things, and the Co-Editor-in-Chief of the International Journal of Smart Vehicles and Smart Transportation.