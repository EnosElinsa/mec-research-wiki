# EMPOWERING INTELLIGENT LOW-ALTITUDE ECONOMY WITH LARGE AI MODEL DEPLOYMENT

Zhonghao Lyu , Member, IEEE, Yulan Gao , Member, IEEE, Junting Chen , Member, IEEE, Hongyang Du , Member, IEEE, Jie Xu , Fellow, IEEE, Kaibin Huang , Fellow, IEEE, and Dong In Kim , Life Fellow, IEEE

## ABSTRACT

Low-altitude economy (LAE) represents an emerging economic paradigm that redefines commercial and social aerial activities. Large artificial intelligence models (LAIMs) offer transformative potential to further enhance the intelligence of LAE services. However, deploying LAIMs in LAE poses several challenges, including the significant gap between their computational/storage demands and the limited onboard resources of LAE entities, the mismatch between lab-trained LAIMs and dynamic physical environments, and the inefficiencies of traditional decoupled designs for sensing, communication, and computation. To address these issues, we first propose a hierarchical system architecture tailored for LAIM deployment and present representative LAE application scenarios. Next, we explore key enabling techniques that facilitate the mutual co-evolution of LAIMs and low-altitude systems, and introduce a taskoriented execution pipeline for scalable and adaptive service delivery. Then, the proposed framework is validated through real-world case studies. Finally, we outline open challenges to inspire future research.

## I. INTRODUCTION

The low-altitude economy (LAE) is rapidly emerging as a critical engine of global industrial innovation and economic growth. As a foundational element of nextgeneration digital infrastructure, LAE is enabling transformative services in logistics, transportation, and public safety. For instance, China’s LAE market is expected to exceed 1 trillion RMB by 2026 with a 33.8% annual growth rate. Germany has investigated over 13 billion USD to air mobility since 2019, while Amazon’s Prime Air MK30 drones have been designed for cross-country package delivery in 2024 [1]. These global developments highlight the urgent need for scalable, intelligent, and secure low-altitude systems.

In parallel, the rise of large artificial intelligence models (LAIMs) has redefined the capabilities of machine perception, reasoning, and decision-making beyond traditional AI systems, offering a powerful foundation for intelligent LAE services. Their strong generalization capabilities and cross-domain adaptability make them well-suited for tasks such as aerial monitoring [2], robust communication [3], [4], and multi-agent coordination [5].

Despite their promise, deploying LAIMs in LAE introduces several challenges:

1) Resource-aware deployment: Generally, the massive model size and high computation intensity far exceed the onboard battery, storage, and processing capabilities of intelligent aerial agents (IAAs) and ground nodes. This makes direct deployment of full-scale LAIMs infeasible. To tackle this issue, recent efforts have explored scalable LAIM deployment strategies, including efficient pretraining and fine-tuning [6], joint task-offloading and resource management [7], and light-weight model inference [8]. Moreover, full-scale LAIMs can be hosted on the edge/cloud servers with sufficient computing power, while IAAs interact with them for prediction and inference via prompt engineering [9].  
2) Environment-aware adaptation: Low-altitude system design must adapt to highly complex and dynamic real-world environments. This includes handling three-dimensional (3D) airspace geometry, operation constraints, electromagnetic interference, and seamless integration with terrestrial and satellite networks. Conventional offline designs built on idealized simulation environments fail to capture such dynamics, necessitating environment-aware IAA deployment and real-time resource management [10]. Furthermore, the performance of LAIMs pre-trained on general-purpose datasets may degrade, when faced with mission-specific tasks and evolving real-world scenarios. To ensure effectiveness, LAIMs must be continuously adapted through feedback-driven refinement informed by realworld interactions and task-specific data.  
3) Co-designing of sensing, communication, and computation (SCC): To meet heterogeneous quality-of-service (QoS) requirements in LAE, it is essential to co-design SCC in a task-oriented paradigm. Traditional decoupled designs often

This work was supported in part by Guangdong S&T Programme under Grant 2024B0101030002, in part by the Basic Research Project under Grant HZQB-KCZYZ-2021067 of Hetao Shenzhen-HK S&T Cooperation Zone, in part by the National Natural Science Foundation of China under Grant 62471424, Grant 92267202, and Grant 62171398, in part by Guangdong Provincial Key Laboratory of Future Networks of Intelligence under Grant 2022B1212010001, in part by the National Key R&D Program of China under Grant 2024YFB2907500, in part by Guangdong Basic and Applied Basic Research Foundation under Grant 2024A1515011206, in part by Shenzhen Science and Technology Program under Grant KJZD20230923115104009, in part by the VINNOVA (Swedish Innovation Agency) Project “Multi-RO-6GIoT-GAI”, in part by the Research Grants Council of the Hong Kong Special Administrative Region, China under a fellowship award under Grant HKU RFS2122- 7S04 and NSFC/RGC CRS under Grant CRS\_HKU702/24, in part by the Areas of Excellence Scheme under Grant AoE/E-601/22-R, in part by the Collaborative Research Fund (C1009-22G) under Grant 17212423 and Grant 17304925, in part by Shenzhen-Hong Kong-Macau Technology Research Programme under Grant SGDX20230821091559018, and in part by the MSIT (Ministry of Science and ICT), Korea, through the ICT Creative Consilience Program under Grant IITP-2020-0- 01821 supervised by the IITP (Institute for ICT Planning & Evaluation).

Digital Object Identifier: 10.1109/MWC.2025.3631765

Date of Current Version: 28 January 2026

Date of Publication: 30 December 2025

Zhonghao Lyu is with The Chinese University of Hong Kong (Shenzhen), China, and also with KTH Royal Institute of Technology, 100 44 Stockholm, Sweden; Yulan Gao (corresponding author) is with KTH Royal Institute of Technology, Sweden; Junting Chen and Jie Xu are with The Chinese University of Hong Kong (Shenzhen), Shenzhen 518172, China; Hongyang Du and Kaibin Huang are with The University of Hong Kong, Hong Kong SAR 518172, China; Dong In Kim is with Sungkyunkwan University, Suwon 16419, South Korea.

![](images/14746a489f4353c32f91dc16737392a9d0a5e15bddd0fb1946312cc72a363dd9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Precision agriculture"] --> B["Smart manufacturing in industry 4.0"]
  B --> C["Sensing"]
  C --> D["Communication"]
  D --> E["LAIM Computation"]
  E --> F["Intelligent vehicular networks"]
    
    subgraph Smart grid
        G["Continuous electricity infrastructure monitoring"]
        H["Selective transmission of sensed grid data"]
        I["Fast response to grid anomalies, load prediction and balancing"]
    end
    
    subgraph Smart logistics
        J(Item identification, package status tracking, sensing surrounding environment for aerial delivery]
        K["Synchronization between delivery platforms, warehouse, and control systems"]
        L["Real-time object recognition, route optimization, and demand prediction"]
    end
    
    subgraph Intelligent vehicular networks
        M["High-resolution multi-modal sensing (LiDAR, radar, and camera) for 3D traffic awareness"]
        N["Low-latency and high-reliable V2X communications among pedestrians, vehicles, and IAAs"]
        O["Real-time reactions for alerts (obstacle avoidance), traffic prediction, and path planning"]
    end
```
</details>

FIG. 1. Architecture and application scenarios of LAIM-empowered intelligent LAE services.

lead to resource inefficiencies, as the three functionalities are often closely coupled and may compete for constrained resources in low-altitude systems [11]. A task-oriented integrated SCC (ISCC) framework could ensure task-relevant sensing, semantic-aware transmission, and adaptive computation tailored to specific LAIM tasks.

These challenges call for unified system architectures, environment-aware system design methodologies, and real-world prototypes to enable efficient deployment of LAIMs to empower intelligent LAE services, which are still underexplored in existing literature. Motivated by this gap, this paper investigates the integration of LAIMs into low-altitude systems. The main contributions are summarized as follows,

First, we propose a hierarchical system architecture for deploying LAIMs in low-altitude systems, and classify representative LAE application scenarios. Also, open issues are outlined to motivate future research.  
Second, we explore the mutual benefits between LAIMs and LAE, including key enabling techniques for SCC co-design, and real-world interaction loops that continuously refine LAIM performance. Moreover, we propose a task-oriented execution pipeline for LAIM-empowered LAE.  
Finally, we present real-world case studies, i.e., LAIM-guided uncrewed aerial vehicle (UAV) placement and resource-aware LAIM deployment across air-ground platforms. These studies are grounded in real-world data and testbeds, demonstrating the feasibility of our framework under practical low-altitude environments.

## II. SYSTEM ARCHITECTURE AND APPLICATION SCENARIOS OF LAIM-EMPOWERED LAE

LAIM-empowered LAE requires a fundamental shift in architectural design for intelligent service delivery. Unlike traditional mobile edge computing (MEC) systems that rely on static terrestrial infrastructure, LAE necessitates an aerial-native and mission-adaptive system architecture capable of supporting distributed AI execution across dynamic 3D network topologies with fast-moving IAAs. To address these unique demands, we propose a three-tier hierarchical framework, as shown in Fig. 1, consisting of a ground layer, an aerial layer, and a cloud layer, which enables scalable and adaptive LAIM-empowered intelligence across LAE services.

## A. LOW-ALTITUDE SYSTEM ARCHITECTURE WITH LAIM INTEGRATION

The ground layer comprises heterogeneous terrestrial nodes, such as sensors, mobile user equipments, base stations (BSs), and edge servers, which are responsible for ubiquitous data collection and preliminary processing. While sensors and mobile user equipments are typically constrained by limited battery, memory, and processing resources, making them suitable only for lightweight LAIM components like ultra-compact encoders for early-stage feature extraction, BSs and edge servers offer stronger processing and communication capabilities. This hierarchical architecture enables the transmission of semantically compressed embeddings or taskrelevant raw data to higher-tier nodes, reducing bandwidth consumption while preserving task-critical information.

The aerial layer consists of IAAs, such as UAVs, which serve as multifunctional entities integrating sensing, computing, communication, and service execution. Unlike traditional ground infrastructures that are constrained by fixed deployment and twodimensional coverage, IAAs offer a unique aerial perspective with comprehensive 3D environmental awareness and situational perception that cannot be achieved from the ground. Their high mobility further enables rapid repositioning and agile adaptation, supporting flexible network topology reconfiguration, on-demand coverage extension, and dynamic load balancing in response to varying service demands or environmental changes. For instance, in logistics or disaster response scenarios, IAAs act as aerial users to simultaneously perceive the environment, process data in real time, and maintain reliable low-latency communications with centralized controllers. When deployed as aerial BSs, they extend network coverage in hotspots or emergency zones, improving connectivity and service continuity. Each IAA is embedded with segmented LAIM modules and edge computing capabilities to execute latency-sensitive tasks locally, while offloading compute-intensive tasks to the cloud for collaborative processing. Moreover, in cooperative tasks, IAAs form flying ad hoc networks through dynamic routing, adaptive beamforming, and mesh reconfiguration, offering robust interagent connectivity and resilience under high mobility, interference, or partial network failure, far beyond what static ground infrastructures can achieve.

The cloud layer consists of centralized infrastructure, including terrestrial BSs, cloud data centers, and low-orbit satellites. It acts as the global coordinator for LAIM-empowered LAE services, supporting distributed model training, inference, and cross-layer resource management. It typically hosts various fullscale LAIMs and partitions their execution across different layers based on environment-aware and taskspecific QoS requirements, such as task urgency, channel conditions, and resource availability. This hierarchical orchestration enables flexible LAIM deployment for large-scale LAE applications in real-world.

## B. TYPICAL APPLICATION SCENARIOS

Typical LAE applications can be broadly categorized into three classes based on their dominant functional demands, i.e., communication-centric, sensing-centric, and computation-centric scenarios.

1) Communication-centric Applications: The primary challenge is to achieve intelligent, reliable, and low-latency communication in dynamic and resourcelimited low-altitude environments. Unlike traditional UAV-assisted communication networks, LAIM-enabled IAAs not only serve as aerial BSs, extending wireless coverage in disaster zones, temporary hotspots, or infrastructure-limited rural regions, but also perform real-time scheduling and dynamic spectrum access. Moreover, IAAs can form self-organized mesh networks beyond static relaying, to support robust multihop communications, ensuring continuity between mobile agents and disconnected infrastructure segments. Additionally, IAAs leverage multi-sensor fusion for precise wireless channel measurement and modeling, enabling predictive channel estimation, 3D beamforming, and interference mitigation, thereby providing a resilient communication backbone for LAE networks.

2) Sensing-centric Applications: Sensing-centric scenarios focus on air-ground collaborative and highresolution environmental awareness, achieving by the enhanced perception capabilities of IAAs equipped with multi-modal sensors, such as LiDAR, cameras, and millimeter-wave radar. Unlike traditional UAVs, LAIMempowered IAAs are capable of dynamic sensing adaptation, which autonomously modify sensing modes and trajectories in response to real-time environmental feedback. Representative use cases include precision agriculture, urban pollution assessment, and disaster response, where periodic scanning, wide-area coverage, and multi-angle imaging are essential to detect crop stress, evaluate air quality, or rescue survivors in post-disaster areas. Another critical application is obstacle detection and avoidance during aerial navigation for transportation and delivery missions, particularly in low-visibility or rapidly changing environments, where IAAs continuously observe their surroundings to identify potential hazards such as trees, power lines, or other flying objects, enabling timely and safe trajectory adjustments.

3) Computation-centric Applications: Computationcentric applications position LAE entities (i.e., ground, aerial, and cloud nodes) as distributed computation infrastructures, supporting a wide range of AI-driven tasks. Specifically, for delay-sensitive tasks, such as anomaly detection in smart grids or real-time UAV path replanning, IAAs act as mobile edge computing nodes, by processing data close to the source for fast computation responses. Beyond real-time services, LAE also supports computation-intensive LAIM applications that require large-scale data analysis, predictive reasoning, and global optimization. Examples include low-altitude channel and environment map reconstruction, traffic forecasting, and airspace coordination through system-level optimization. Nevertheless, continuous LAIM fine-tuning via real-world interactions is necessary for narrowing the performance gap between lab training and field deployment.

To summarize, Fig. 1 presents representative use cases of LAIM-empowered LAE, including smart manufacturing, smart grid, intelligent vehicular networks, smart logistics, and precision agriculture, while highlighting the corresponding sensing, communication, and computation functionalities involved in each scenario.

## III. MUTUAL BENEFITS OF DEPLOYING LAIMS IN LAE

This section discusses the mutual benefits of integrating LAIMs into LAE, and presents a task-oriented execution pipeline to facilitate this integration.

A. KEY ENABLING TECHNIQUES FOR LAIM-EMPOWERED LAE Deploying LAIMs in dynamic and resource-constrained low-altitude environments requires tight integration of SCC functionalities to ensure real-time, mission-adaptive intelligence. We identify three core enabling techniques that jointly empower LAIM deployment: integrated sensing and communication (ISAC), integrated communication and computation (ICC), and ISCC.

1) ISAC for LAIM-empowered LAE: In low-altitude systems, multi-modal sensors are widely deployed on both IAAs and ground nodes. ISAC frameworks enable these entities to use shared spectrum and hardware resources for both environmental sensing and data transmission by leveraging dual-purpose waveform design [12]. This design paradigm is especially beneficial in low-altitude scenarios where spectrum availability and hardware capacity are constrained. Beyond resource reuse, ISAC enables environment-aware channel modeling and real-time channel state information (CSI) acquisition by jointly estimating the channel parameters and perceiving the physical environment [13]. Moreover, networklevel ISAC further enables adaptive 3D beamforming, allowing IAAs and edge nodes to sustain high-quality communication links and perform high-precision sensing collaboratively, even in highly dynamic or low-visibility environments.

2) ICC for LAIM-empowered LAE: ICC focuses on the co-design of communication and computation to ensure efficient transmission and processing of taskrelevant information with reduced latency. Two foundational enablers of ICC in LAIM-empowered LAE are semantic communications and over-the-air computation (AirComp). Semantic communications aim to transmit only compressed task-relevant features or intermediate inference results instead of raw data. For example, [14] proposed an interest-based image segment transmission method, which can help to extract only the relevant part of UAV-sensed images to reduce bandwidth consumption and latency. Air-Comp exploits the superposition property of wireless multiple-access channels to enable simultaneous communication and functional aggregation of distributed data. This is particularly advantageous for collaborative LAE tasks needing efficient information aggregation, such as UAV swarming, distributed sensing, and consensus building. Together, these techniques enable a compute-while-communicate paradigm, alleviating communication bottlenecks and enhancing the responsiveness of latencysensitive LAIM-empowered services in resourceconstrained low-altitude environments.

3) ISCC for LAIM-empowered LAE: ISCC represents an advanced convergence of ISAC and ICC, enabling the task-driven co-optimization of SCC resources. Traditionally designed in isolation, these functions are inherently coupled and exhibit complex relationships in LAIM-empowered low-altitude systems, from collaboration to competition over limited resources. The overall service quality depends on their joint effectiveness, but their contributions to task performance are uneven. Therefore, their individual optimization, e.g., maximizing sensing resolution or transmission rate, can lead to degraded task performance and inefficiencies.

To address it, a task-oriented ISCC design paradigm is essential, which co-optimizes SCC for mission-level goals such as LAIM training/inference accuracy, latency, energy efficiency, and reliable primary and secondary control. In this paradigm, sensing prioritizes acquiring task-relevant information, communication focuses on transmitting semantic features or intermediate results, and computation is adaptively offloaded across heterogeneous entities aligned with task-specific QoS demands [15]. Additionally, jointly optimizing IAA positioning with SCC resource allocation further enhances system flexibility and supports adaptation to the dynamic low-altitude environments.

ISCC for distributed LAIM training in LAE: ISCC provides the architectural backbone for LAIM-based services in LAE, supporting continual model refinement driven by real-world feedback. Emerging techniques, such as parameter-efficient fine-tuning (e.g., low-rank adaptation (LoRA) and prompt-tuning), mixture-of-experts (MoE), and distributed learning (e.g., federated and split learning) are particularly suitable for lifelong LAIM adaptation and naturally aligned with ISCC principles in low-altitude environments. To fine-tune a pre-trained LAIM for a specific LAE task, split learning can be used to distribute model segments and training tasks across ground devices, IAAs, and the cloud, leveraging heterogeneous computation resources. Under this setup, only gradient/model information needs to be exchanged, reducing communication overhead and enhancing privacy compared to transmitting raw training data. LoRA can accelerate this fine-tuning process, while federated learning enables semantic heads to generalize across multi-modal and multi-task settings via periodic model aggregation. Throughout this process, a task-aware ISCC framework coordinates model partitioning, node selection, resource allocation, and IAA positioning to accelerate the convergence speed.

ISCC for efficient LAIM inference in LAE: ISCC also supports efficient inference by enabling flexible partitioning and execution of LAIMs across ground, aerial, and cloud nodes based on real-time QoS requirements, which is commonly referred to as split or co-inference. Enhanced by expert-path routing, model components such as attention heads or decision layers, can be selectively executed depending on the capabilities of each node. Moreover, to enable lightweight deployment for fast inference, various model compression techniques, such as pruning, quantization, sparse activation, and knowledge distillation are applied. However, these must be guided by QoS-aware strategies and theoretical performance guarantees to ensure a balance among inference accuracy, latency, and energy consumption. For example, high-reasoning-demand tasks (e.g., multi-view 3D scene reconstruction) may require retaining more model capacity, even at higher energy and delay costs. ISCC coordinates model compression, task offloading, IAA placement, and resource allocation, enabling resource-efficient LAIM inference tailored to evolving service demands in dynamic low-altitude environments.

## B. LAE FOR CONTINUAL LAIM EVOLUTION

While LAIMs serve as powerful enablers of intelligent LAE services, the relationship between them is inherently bidirectional. LAE is not merely a consumer of LAIMs, it could also help to advance LAIMs. Unlike static datasets or simulation environments, lowaltitude systems continuously generate vast volumes of real-world, multi-modal, spatio-temporal data under diverse physical constraints, enabling taskoriented fine-tuning of pre-trained LAIMs.

1) Real-World Data for Robust Representation Learning: The multi-modal and spatially distributed sensing data produced in low-altitude environments often contain rich contextual correlations, varying noise patterns, and real-world outliers. These characteristics are critical for learning robust and generalizable representations. Continuous exposure to such diverse data fosters improved feature extraction, contextual adaptation, and multi-modal data fusion, allowing LAIMs to refine digital twin-based world models and semantic knowledge bases. To ensure trustworthiness, LAE systems should incorporate data quality and reliability checks, cross-node consistency validation, and privacy-preserving collection.

2) Reinforcement Learning (RL) in Real-world Loops: LAE offers unique training environments for RL-type LAIMs, where intelligent agents interact directly with the physical world, execute tasks, observe feedback, and iteratively improve policies. The complexity of LAE tasks introduces highdimensional state-action spaces and diverse reward mechanisms, which are ideal for training scalable RL architectures. These systems can be further enhanced using human-in-the-loop feedback, such as expert demonstrations, to guide policy optimization. Through continual interaction with real-world environments, LAIMs can develop reusable policies that generalize to unseen conditions.

3) Multi-Task LAIM Adaptation: The heterogeneity of LAE tasks necessitates the deployment of multi-task LAIMs for cross-domain reasoning. A single IAA may be expected to perform tasks from visual inspection to path planning, which pose significant challenges to traditional single-task models. To meet these demands, LAIMs are evolving toward rapid multi-task adaptation, adopting parameter-efficient designs, such as shared multi-head attention, cross-modal encoders, and task-specific output modules. Moreover, low-altitude systems inherently support continual LAIM learning, where task failures naturally trigger on-the-fly adjustment and retraining.

## C. EXECUTION PIPELINE

The execution of LAIM-empowered LAE services follows a task-oriented pipeline comprising both offline and online stages, which is summarized as follows.

1) Offline System Initialization: The pipeline begins with an offline initialization phase grounded in a digital twin or virtual world model. At this stage, IAA positioning, resource allocation, cooperation strategies, and task scheduling are jointly optimized under taskoriented objectives and QoS constraints. This optimization problem can be solved via a range of techniques, including convex/non-convex optimizations, RL, and generative AI. The outcome provides a coarse-grained initial system setups. However, due to inevitable mismatches between simulation and realworld conditions, this offline plan requires subsequent refinement through online adaptation.

2) Multi-modal Data Sensing: Once deployed, LAE nodes begin collecting environmental data using multi-modal sensors mounted on both ground terminals and IAAs. The sensing process is task-oriented, employing spatially selective and temporally adaptive strategies, such as continuous or event-triggered sampling, based on region-of-interest characteristics and mission requirements. The collected data, ranging from raw sensing data to semantic features, form the foundation for downstream LAIM inference and control tasks.

3) Information Transmission: To synchronize information and support cooperative intelligence, sensing and control signals are transmitted across the LAE networks. This involves both horizontal exchange within each layer (e.g., among IAAs or ground terminals) to build task and environment consensus, and vertical exchange across layers (e.g., IAA-to-cloud) for collaborative task execution. Depending on task urgency, node topology, and available resources, the system dynamically chooses between bit-level and semanticlevel transmission modes to improve communication efficiency.

4) Downstream Task Execution and Control: LAIM tasks are executed in a distributed and collaborative manner across LAE entities. Execution is partitioned based on task complexity and latency sensitivity. For example, lightweight semantic heads may run on ground nodes, transformer encoders on IAAs, and global decision modules on the cloud. This paradigm supports both real-time responsiveness for latencycritical operations and high-accuracy performance for computationally intensive tasks requiring centralized processing.

5) Closed-loop Control Adaptation: Following task execution, the system continuously monitors environmental feedback, such as task outcomes, signal quality variations, and unexpected disturbances. These feedback signals are used to update resource allocation, adjust IAA deployment strategies, and reconfigure task execution pipelines in real time. Through this closed-loop control mechanism, the system supports timely performance evaluation, strategy adjustment, and LAIM refinement under dynamic and uncertain low-altitude environments.

## IV. CASE STUDY

We present case studies to validate the proposed framework, focusing on LAIM-guided UAV deployment and resource-aware LAIM deployment across LAE platforms.

## A. REAL-WORLD IMPLEMENTATION DETAILS

We conduct signal mapping experiments using a low-altitude channel measurement prototype over the campus of the Chinese University of Hong Kong, Shenzhen. The BS is equipped with $\textrm { a 4 } \times \bar { 8 }$ dual-polarized antenna array and periodically transmits 7 synchronization signal block (SSB) beams. We built a USRP-based software-defined radio platform, mounted on a DJI M300 RTK UAV, to collect raw I/Q samples over a 10 MHz bandwidth at 2.6 GHz. The UAV flies at a fixed altitude of 112 meters above the BS, and maintains a speed of 10 m/s over an area of approximately 530 400 meters. The collected I/Q samples are processed following the 5G physical layer signal processing protocols, where SSBs are detected and their reference signal received power (RSRP) is estimated. RSRP values are sampled at 10 Hz from the PBCH-XSS RSRP metric, while RTK-based positioning ensured centimeterlevel localization accuracy. The collected data provides a fine-grained signal quality measurements under realistic low-altitude environments as shown in Fig. 3.

## B. LAIM-GUIDED UAV DEPLOYMENT

We evaluate the potential of LAIMs to guide UAV positioning in low-altitude environments based on real-world RSRP measurements. The task objective and system setups are specified in the prompts as shown in Fig. 4.

We adopt a prompt-driven workflow to interact with cloud-deployed LAIMs, which serve as high-level decision-making coordinators. The input includes the real-world RSRP values and a task description specifying the objective, system constraints, and relevant parameters. Then, the LAIM autonomously interprets the spatial distribution of signal strength and generates UAV coordinates along with

![](images/a99646ecc3391f2e67e60674ef67659955be1758e4eab7d85130d744a3599448.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["Step 1 Multi-modal data sensing"] --> B["Policy and system update"]
  B --> C["Step 2 Information transmission"]
  C --> D["Step 3 Downstream task execution and control"]
  D --> E["Step 4 Closed-loop control adaptation"]
  E --> F["Feedback"]
  F --> G["Step 0 Offline system initialization"]
    
    subgraph A
        A1["Drone icon with drone"]
        A2["Camera icon with sensor"]
        A3["User interface icons"]
    end
    
    subgraph B
        B1["Task-oriented sensing"]
        B2["Spatial-temporal sampling strategy design"]
        B3["Fusion of multi-modal raw data and semantic embeddings"]
    end
    
    subgraph C
        C1["Information transmission"]
        C2["Horizontal and vertical transmission for information synchronization and task coordination"]
        C3["Adaptive bit-/semantic-level modes switching"]
    end
    
    subgraph D
        D1["Model partitioning and task-offloading"]
        D2["QoS-aware collaborative task execution"]
    end
    
    subgraph E
        E1["Collecting feedback after task execution"]
        E2["Real-time system adjustment"]
        E3["Continuous LAIM fine-tuning"]
    end
    
    subgraph F
        F1["Digital twin or virtual world model construction"]
        F2["Joint optimization of IAA positioning and system resource scheduling"]
        F3["Optimization/RL/Generative AI-based solutions under QoS constraints"]
    end
```
</details>

FIG. 2. Execution pipeline for LAIM-empowered LAE services.

![](images/64c89e9ef47e6fcd373ee0b914548bf4b7e532710b7e8adac882fd1b1c2ba69d.jpg)

<details>
<summary>text_image</summary>

DJI M300 RTK UAV
E-port
Power Amplifier + Antenna
USRP B200mini + X86 mini PC + Antenna
Portable power supply
USRP B210
Ground system
UAV remote controller
Satellite map
22°41'35"N
22°41'30"N
22°41'25"N
22°41'20"N
114°12'20"E
114°12'30"E
114°12'40"E
Longitude
Channel measurement prototype in low-altitude scenarios
3D RSRP distribution
RSRP map at 112 m altitude
</details>

FIG. 3. Real-world implementation with the channel measurement prototype in low-altitude scenarios.

estimated communication rates. For comparison, we consider a conventional optimization-based benchmark scheme using a location-dependent line-of-sight (LoS) channel model. The corresponding non-convex sum-rate maximization problem is solved using successive convex approximation.

![](images/8ab75b25705569798369cc77c1dd620e8db0a2c6e0aecf9fa2fc969d317e13f3.jpg)

## Prompts forUAVdeploymentinLAEsystems

![](images/534f36d027b4e760744c4388ce32666a42a3fb7a05e429f2cbc5a6dc8659ba72.jpg)

First,Iwill providea.mat file containingthe variable RSRP,where each row representsa sample.In each row,the first column correspondsto the latitude,the second to the longitude,and thelast columntothe RSRP value.[Datauploading]

(Thinking...)I've loaded theRSRPvariable from yourMAT-file.Itcontains22671samplesacross3 columns(latide,logitude,P).Hre'saquik summary ofthe data...

You are an expert in wireless communications, particularly in UAVcommunications.Iaimtodeploy UAVsin an LAE system using real-world channel measurementstodesignaninitialoflinetopologyfor theUAV network.[General task description]

Weconsideran uplink communication scenario where multiple UAVs simultaneously transmit data toaBS overa shared frequency band.The objective is to determine the optimal UAV locationsto maximize the overall uplink sum-rate.Thechannel conditionsbetween potential UAVpositionsand theBSareprovided in the above.mat file.Toensure collisionavoidance,a minimumdistanceconstraintisimposedbetweenany two UAVs.[Systemand objectivedescription]

Pleasecomputetheoptimal UAV placementsunder the followingsystemsetups:

1)Thenumber ofUAVsis3.

2)ThevarianceofAWGNis-110dBm.

3)TheminimumdistancebetweenUAVsis20meters.

4)SINR shouldbe calculated based on theprovided RSRPvaluesand AWGN variance.Thecommunication rateofeach UAViscomputedusingShannon'scapacity formula.[System setups]

Ifyourequireanyadditionalinformationorclarification, please let me know.

![](images/dbef0e7b8f12667ba1629ca6c1a07b3c75c67a277154e257b3ef464c4a279221.jpg)

![](images/c9aa4622876addafdc8df0f73c7b7a5033dec062e7c672c903da207fee97ad0f.jpg)

(Thinking..) The UAVs locations are (22.689688°, 114.206455°),(22.688900，114.207376),and (22.689292104893).eumateis13.257 bps/Hz.

Ifyou have any further requirements,such as modifying the systemsetups,please letme know!

![](images/860a324792f0bc42320f3b1d62342548ad7a94256218a174794c9e769c0206d2.jpg)

![](images/fb242544916c069fbf35cdfe2a0f7bccb6d684e6787f41323330ae897cd21aa1.jpg)

UAVdeployment in LAE systems  
![](images/74f32cb43abeede4830b0e5eff5c4b78285ef22e12c309a82af35ec6b630888c.jpg)

<details>
<summary>heatmap</summary>

| Latitude   | Longitude | Value |
| ---------- | --------- | ----- |
| 22°41'35"N | 22°41'30"N | -30   |
| 22°41'25"N | 22°41'20"N | -45   |
</details>

114°12'20°E 11412'30°E

![](images/72873c9ce145102274033bcf049ba7d87b283686c8a41543d50a54a71161d93c.jpg)

<details>
<summary>heatmap</summary>

| RA (deg) | CS (dBm) |
| -------- | -------- |
| 22°41'20"N | -45 |
| 22°41'25"N | -35 |
| 22°41'30"N | -30 |
| 22°41'35"N | -25 |
</details>

114°12'20WE 114°12'30E

![](images/3634486d6b59437af6651ee410bf8fe70ee8330e9258bad424567f43cd41dbc7.jpg)

<details>
<summary>heatmap</summary>

| Latitude   | Longitude  | Value |
| ---------- | ---------- | ----- |
| 22°41'35"N | 14°00'00'E | -20   |
| 22°41'30"N | 14°00'00'E | -35   |
| 22°41'25"N | 14°00'00'E | -45   |
| 22°41'20"N | 14°00'00'E | -50   |
</details>

Longitude

![](images/449d64a46c4d6c897f718946bfb72f2be564c9beb13d2f93f6784e0c6a0228af.jpg)

<details>
<summary>heatmap</summary>

| RA(°) | B(°) | RSRP (dBm) |
|-------|------|------------|
| 22°4130'N | 25 | -25 |
| 22°4130'N | 30 | -30 |
| 22°4130'N | 35 | -35 |
| 22°4130'N | 40 | -40 |
| 22°4130'N | 45 | -45 |
| 22°4130'N | 50 | -50 |
The image displays a heatmap with color intensity representing the RSRP values. The chart includes a scale bar of 100 m and a legend indicating 'CA: HSP, Gema, RSD, NETRMA'. Red stars mark specific data points along the map. The right side is labeled 'longxian'.
</details>

Longitude

BS△UAV(Optimization-based)★UAV(LAIM-based)

<table><tr><td>The number of UAVs</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>LAIM-based rate (bps/Hz)</td><td>29.57</td><td>12.45</td><td>10.27</td><td>8.59</td></tr><tr><td>Optimization-based rate (bps/Hz)</td><td>26.50</td><td>2.11</td><td>1.78</td><td>1.69</td></tr></table>

FIG. 4. LAIM-guided UAV deployment in LAE.

Fig. 4 shows that LAIM-based solutions significantly outperform the traditional optimization-based schemes, with performance gaps increasing with the number of UAVs. This is due to the mismatch between the simplified LoS channel models assumed in the traditional optimization-based scheme and the complex real-world wireless environments. Optimizing UAV placement based on idealized LoS assumptions can lead to positions that suffer from strong interference. In contrast, LAIMs can directly interpret real-world channel measurements, enabling more interference-aware and environment-adaptive deployment decisions. These results highlight the practicality of LAIM-driven IAA deployment in complex lowaltitude environments.

## C. RESOURCE-AWARE LAIM DEPLOYMENT

To enable the deployment of LAIMs on resourcelimited LAE platforms, we propose a pruning-aware co-inference scheme [8]. A pre-trained LAIM is first pruned and then partitioned into on-IAA and on-server sub-models for collaborative execution. To balance trade-offs among inference quality, delay, and energy consumption, we jointly optimize the pruning ratio, transmit power, and computation frequency. We consider three objectives, i.e., maximizing inference quality, minimizing delay, and minimizing energy consumption, the remaining two QoS metrics are treated as constraints. Furthermore, we compare co-inference with two inference paradigms: 1) On-server inference, where the full LAIM is executed on the cloud server; 2) On-IAA inference, where the full inference task is performed locally on IAAs.

We experiment with the Video Masked Autoencoder (VideoMAE) model on the Kinetics-400 dataset for video analysis via magnitude-based pruning.

Specifically, we adopt independent and identically distributed (i.i.d.) Rayleigh fading with an average path loss of 10−5, and perform 300 independent experiments to obtain the averaged results. Moreover, we set the power of the additive white Gaussian noise (AWGN) as −120 dBm. Fig. 5 shows that the co-inference paradigm consistently achieves the best performance. The result validates that the proposed design could well balance the trade-offs between LAIM inference quality, delay, and energy consumption. Jointly optimizing the model structure and resource allocation allows for efficient LAIM deployment, tailored to low-altitude system resource availability and real-world task demands.

## V. CONCLUSION AND FUTURE DIRECTIONS

By presenting a hierarchical system architecture, a task-oriented execution pipeline, and real-world case studies, this work investigated efficient LAIM deployment in dynamic and resource-constrained low-altitude environments. It enables a new air-ground intelligence paradigm for LAE, where real-time perception, high-quality communication, adaptive decisionmaking, and continual LAIM refinement converge. This transformation unlocks broad opportunities, from smart manufacturing to disaster response, driving future digital innovation and inspiring further research, as outlined below.

1) Fusion of Airspace Knowledge Graphs and LAIMs: Enhancing airspace intelligence in LAE requires reconciling strict regulatory constraints with the operational flexibility needed by LAIM-driven IAAs. Traditional knowledge graph (KG)-based systems offer structured representations of airspace rules. However, they struggle to adapt to rapid environment dynamics, limiting their responsiveness in tasks like obstacle avoidance. Meanwhile, current LAIMs lack the domain-specific reasoning necessary to accurately interpret complex airspace regulations. This gap leads to unreliable or non-compliant behaviors in high-risk scenarios. Bridging this gap demands new frameworks that fuse real-time sensing with KG-grounded LAIM reasoning, empowering UAVs to understand and act on complex regulations.

2) Multi-agent Collaboration and Open Ecosystem: Collaborative decision-making in multi-agent LAE systems remains highly challenging due to conflicting commercial interests, data confidentiality, and regulatory constraints. In competitive airspace, IAAs from different stakeholders must operate under partial observability and strategic uncertainty, where limited data sharing and the opacity of LAIM-driven decisions hinder coordination and regulatory trust. These challenges not only highlight the need for game-theoretic mechanisms to balance competition and cooperation, but also call for an open ecosystem that ensures technical interoperability and collective progress. However, current proprietary technologies, incompatible protocols, and mismatches between rapid AI model evolution and hardware lifecycles create barriers, while data silos further restrict collaboration. Future LAE development should therefore embrace open standards, interoperable architectures, and shared governance frameworks, enabling scalable multi-agent collaboration that is both ecosystem-wide and policy-compliant.  
3) Sustainable LAIM Deployment in LAE: The growing computational needs of LAIMs significantly exceed the limited and unstable energy resources available to aerial platforms. Wireless power transfer (WPT) from terrestrial nodes may not work because of its much lower end-to-end efficiency for long-range scenarios. Instead, the satellite-based long-range WPT would be feasible, given that a large-scale array antenna can deliver the solar power harvested at the low earth orbit (LEO)/geostationary equatorial orbit (GEO) stations. Furthermore, the mismatch between intermittent renewable energy availability and the continuous power demands of AI workloads calls for energy-aware model design, task-adaptive execution, and robust power management strategies.  
4) Security Issues: IAAs with limited operational power are more likely exposed to intentional jamming attacks, because of low-power transmissions for uploading data from sensors, and the backhaul links to terrestrial BSs. Consequently, it is important to ensure secure and reliable operation against jamming attacks, where the primary and secondary control links should be designed in a layered and integrated manner under the proposed hierarchical network infrastructure and task-oriented ISCC design paradigm.  
5) Airspace Computing Network Infrastructure: Building an efficient airspace computing network for LAE is crucial for real-time, AI-driven applications. It requires seamless coordination of computing tasks across heterogeneous platforms under stringent latency and energy constraints. However, large-scale deployment is hindered by high infrastructure costs, fragmented investment responsibilities, lack of unified standards, and difficulties in coordinating resources across diverse systems and administrative domains. Furthermore, node mobility introduces dynamic resource availability, complicating task scheduling and system stability.

![](images/b4a565310e3ec3595dcf9de0a591debe161b31acc3118a71609059f679428dba.jpg)

<details>
<summary>radar chart</summary>

| Scenario | Co-inference Accuracy | On-Server Inference Accuracy | On-IAA Inference Accuracy | On-Server Inference Accuracy | On-IAA Inference Energy (J) | Best performance |
|---|---|---|---|---|---|---|
| LAIM inference quality maximization | 0.6 | 0.4 | 0.4 | 0.4 | 0.45 | 0.6 |
| LAIM inference minimization | 0.2 | 0.15 | 0.15 | 0.15 | 0.15 | 0.2 |
| Energy consumption minimization | 0.4 | 0.2 | 0.2 | 0.2 | 0.25 | 0.4 |
</details>

FIG. 5. Resource-aware LAIM deployment across LAE platforms.

6) Standardization Alignment: As the LAE increasingly relies on IAAs and non-terrestrial networks (NTNs), alignment with ongoing 3GPP standardization efforts becomes critical. Future sixth-generation (6G) of wireless systems are expected to natively support integrated terrestrial, aerial, and satellite communication. This requires unified architecture designs, interoperability protocols, and standardized interfaces for heterogeneous LAE-NTN deployments. Key challenges include delay-tolerant protocols for high-altitude relays, dynamic spectrum access, and service continuity across multi-layered infrastructures.

## REFERENCES

[1] Y. Yang, Y. Chen, J. Wang, G. Sun, and D. Niyato, “Embodied AI-empowered low altitude economy: Integrated sensing, communications, computation, and control (ISC3),” 2024. [Online]. Available: https://arxiv.org/pdf/2412.19996  
[2] J. Wang et al., “Generative AI based secure wireless sensing for ISAC networks,” IEEE Trans. Inf. Forensics Secur., vol. 20, pp. 5195–5210, 2025.  
[3] S. Javaid, R. Khalil, N. Saeed, B. He, and M. Alouini, “Leveraging large language models for integrated satelliteaerial-terrestrial networks: Recent advances and future directions,” IEEE Open J. Commun. Soc., vol. 6, pp. 399–432, 2024.  
[4] C. Zhao et al., “Generative AI-enabled wireless communications for robust low-altitude economy networking,” 2025. [Online]. Available: https://arxiv.org/pdf/2502.18118  
[5] L. Zhou et al., “Cooperative generative AI for UAV-based scenarios: An intelligent cooperative framework,” IEEE Veh. Technol. Mag., vol. 20, no. 2, pp. 44–52, Jun. 2025.  
[6] Z. Lyu, Y. Li, G. Zhu, J. Xu, H. Vincent Poor, and S. Cui, “Rethinking resource management in edge learning: A joint pre-training and fine-tuning design paradigm,” IEEE Trans. Wireless Commun., vol. 24, no. 2, pp. 1584–1601, Feb. 2025.  
[7] Y. Gao, Z. Ye, and H. Yu, “Cost-efficient computation offloading in SAGIN: A deep reinforcement learning and

perception-aided approach,” IEEE J. Sel. Areas Commun., vol. 42, no. 12, pp. 3462–3476, Dec. 2024.

[8] Z. Lyu, M. Xiao, J. Xu, M. Skoglund, and M. Renzo, “The larger the merrier? Efficient large AI model inference in wireless edge networks,” 2025. [Online]. Available: https:// arxiv.org/pdf/2505.09214

[9] H. Li, M. Xiao, K. Wang, D. I. Kim, and M. Debbah, “Large language model based multi-objective optimization for integrated sensing and communications in UAV networks,” IEEE Wireless Commun. Lett., vol. 14, pp. 979–983, Apr. 2025.

[10] Y. Zeng et al., “A tutorial on environment-aware communications via channel knowledge map for 6G,” IEEE Commun. Surv. Tuts., vol. 26, no. 3, pp. 1478–1519, 3rd Quart. 2024.

[11] D. Wen, Y. Zhou, X. Li, Y. Shi, K. Huang, and K. B. Letaief, “A survey on integrated sensing, communication, and

computation,” IEEE Commun. Surv. Tuts., vol. 27, no. 5, pp. 3058–3098, Oct. 2025.

[12] Z. Lyu, G. Zhu, and J. Xu, “Joint maneuver and beamforming design for UAV-enabled integrated sensing and communication,” IEEE Trans. Wireless Commun., vol. 22, no. 4, pp. 2424–2440, Apr. 2023.

[13] W. Liu and J. Chen, “UAV-aided radio map construction exploiting environment semantics,” IEEE Trans. Wireless Commun., vol. 22, no. 9, pp. 6341–6355, Sep. 2023.

[14] Y. Cheng, D. Niyato, H. Du, C. Miao, and D. I. Kim, “Goaloriented semantic communication with message-sharing NOMA for metaverse,” IEEE Wireless Commun., vol. 31, no. 3, pp. 309–315, Jun. 2024.

[15] G. Zhu et al., “Pushing AI to wireless network edge: An overview on integrated sensing, communication, and computation towards 6G,” Sci. China Inf. Sci., vol. 66, Feb. 2023, Art. no. 130301.