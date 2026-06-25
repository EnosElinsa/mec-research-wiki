# Revolutionizing Future Connectivity: A Contemporary Survey on AI-Empowered Satellite-Based Non-Terrestrial Networks in 6G

Shadab Mahboob , Graduate Student Member, IEEE, and Lingjia Liu , Senior Member, IEEE

Abstract—Non-Terrestrial Networks (NTN) are expected to be a critical component of 6th Generation (6G) networks, providing ubiquitous, continuous, and scalable services. Satellites emerge as the primary enabler for NTN, leveraging their extensive coverage, stable orbits, scalability, and adherence to international regulations. However, satellite-based NTN presents unique challenges, including long propagation delay, high Doppler shift, frequent handovers, spectrum sharing complexities, and intricate beam and resource allocation, among others. The integration of NTNs into existing terrestrial networks in 6G introduces a range of novel challenges, including task offloading, network routing, network slicing, and many more. To tackle all these obstacles, this paper proposes Artificial Intelligence (AI) as a promising solution, harnessing its ability to capture intricate correlations among diverse network parameters. We begin by providing a comprehensive background on NTN and AI, highlighting the potential of AI techniques in addressing various NTN challenges. Next, we present an overview of existing works, emphasizing AI as an enabling tool for satellite-based NTN, and explore potential research directions. Furthermore, we discuss ongoing research efforts that aim to enable AI in satellite-based NTN through software-defined implementations, while also discussing the associated challenges. Finally, we conclude by providing insights and recommendations for enabling AI-driven satellitebased NTN in future 6G networks.

Index Terms—Non-terrestrial networks (NTN), space-airground integrated networks (SAGIN), artificial intelligence (AI), machine learning (ML), deep learning (DL), 5G-advanced, 6G, satellite, beam-hopping, handover, spectrum sharing, doppler shift, resource allocation, computational offloading, network routing, network slicing, channel estimation, security, open radio access network (O-RAN), RAN intelligent controller (RIC).

# I. INTRODUCTION

HE THIRD Generation Partnership Project (3GPP) has already started the standardization towards the 5th Generation (5G)-Advanced in Release 17 and 18 to facilitate its worldwide deployment [1], [2]. 5G-Advanced provides much higher data rates, lower latency, increased capacity, and more efficient spectrum utilization than any of its predecessors. It supports a wide range of applications

Manuscript received 9 June 2023; revised 1 October 2023 and 12 November 2023; accepted 13 December 2023. Date of publication 19 January 2024; date of current version 23 May 2024. This work was supported by the U.S. National Science Foundation under Grant CNS-2148212. (Corresponding author: Lingjia Liu.)

The authors are with the Wireless@Virginia Tech, Bradley Department of Electrical and Computer Engineering, Virginia Tech, Blacksburg, VA 24060 USA (e-mail: ljliu@vt.edu).

Digital Object Identifier 10.1109/COMST.2023.3347145

encompassing all 5G use cases such as Ultra Reliable Low Latency Communications (URLLC), massive Machine Type Communication (mMTC), and enhanced Mobile Broadband (eMBB) communication with different Key Performance Indicator (KPI) requirements [3]. Nevertheless, future applications such as Augmented Reality (AR), Virtual Reality (VR), Tactile Internet, Holographic Type Communication (HTC), remote health and surgery, etc. require extremely high throughput, low latency, high reliability, and ubiquity at the same time which cannot be met with current technological standards [4]. Consequently, the next-generation global wireless standard, namely, 6th Generation (6G) has become the current research focus for the industry and research community [5].

6G is expected to provide an extremely high data rate (peak data rate up to 1 Tbps and user-experienced data rate up to 10 Gbps, around 100 times higher than 5G), very low latency (in the order of μs), high reliability (around 100 times better than 5G) and extreme coverage to support the diverse set of future applications [6], [7], [8]. Due to the limited coverage area and geographical constraints, it is not possible to guarantee ubiquitous connectivity with existing terrestrial-only network infrastructures. Non-Terrestrial Networks (NTNs), networks involving space and aerial platforms, can provide us with multicast opportunities over very large areas as well as can serve users even in remote areas or during times of natural calamities [4]. Furthermore, the launching and maintenance costs for satellites have significantly decreased as they are deployed at lower heights (typically around 600 km). These satellites can provide much higher throughput and lower latency compared to legacy satellites and potentially can support different use cases of 6G. So NTN is considered to become one of the major technological enablers of future 6G networks visioning connectivity anywhere and anytime [4], [9], [10], [11]. Tech giants such as SpaceX Starlink, Amazon Kuiper, and OneWeb have already begun to invest billions of dollars in this field, reflecting its massive potential for future growth [12].

Although NTN presents numerous potential benefits for the development of future 6G networks, it also entails several challenges that need to be addressed, primarily due to the unique characteristics of its mobility and propagation environments [13], [14]. Due to the long distances between the space-borne Base Stations (BS) and the ground User Equipment (UE), the propagation delay is usually higher in NTN environments. Additionally, high-speed air or space-borne platforms necessitate modifications to existing handover and paging protocols, as well as introduce a significant Doppler shift in carrier frequencies. The large path loss also increases the minimum power requirement for reliable transmission, initiating the need for novel beam and resource allocation strategies. Spectrum sharing in the same frequency band with existing terrestrial or other services also requires further study in order to avoid interference between terrestrial and non-terrestrial users. Even though currently there are some stand-alone satellite network deployments, the ultimate goal is the convergence of terrestrial and non-terrestrial environments for extreme network performance in 6G. [4]. This potential integrated environment requires efficient computing, routing, and slicing algorithms for meeting the expected KPI requirements of 6G.

Artificial intelligence (AI) is currently having a profound and revolutionary impact on a multitude of industries, including but not limited to healthcare, military, transportation, and e-Commerce [15]. AI encompasses a wide array of smart machines, while Machine Learning (ML) is a popular subset of AI that allows machines to learn from large amounts of data and make decisions without the need for explicit programming [16]. Deep Learning (DL) is a special subset of ML that studies Artificial Neural Networks (ANNs) which contain more than one hidden layer, often implemented to simulate the human brain [17]. DL is currently being leveraged in various applications, such as computer vision, speech recognition, and bioinformatics, outperforming human-level performance in these particular domains. The cellular domain is still in its infancy in terms of AI integration [18] compared to other fields due to the complex and dynamic nature of wireless networks. As an integral part of 6G networks, challenges associated with NTN deployment provides an enticing field for AI applications. However, while deploying algorithms in a real environment, practical implementation difficulties may arise to provide reliable vertical connectivity between the ground and space networks. To reach optimal performance, theoretical advancements in communication system design must be complemented by appropriate AI solutions for NTN integration into 6G.

# A. Contribution

Most of the existing articles either focus on a discussion of architecture and challenges associated with NTN or AI approaches for wireless communications from a broader point of view. Although some research articles also discuss the potential research scopes for AI-powered NTNs to some extent, those discussions are either generally not very comprehensive or do not capture the role of AI in NTN-integrated 6G networks in a complete manner. Also, the current research efforts and practical complications related to AI-empowered NTN-integrated 6G networks are not covered. This survey article aims to provide a comprehensive survey into different AI methods used to overcome the specific challenges of NTN. To help our readers understand better, we also provide a necessary relevant background discussion on NTN and its challenges in the context of 6G. We also discuss different AI approaches and how they can help solve NTN challenges. Additionally, we explore ongoing research efforts and the difficulties of using AI methods in real integrated TNTN setups in 6G. The main contributions of this article can be summarized as follows:

1) We present a systematic survey of existing and relevant research works in each research thrust to organize the current research progress in these fields. This helps us to get an insight into the current status and potential future research scopes of different relevant research fields in this domain.   
2) We summarize the current AI testbeds for satellite networks and potential integration efforts to current 5G software-defined testbeds for implementing integrated satellite-terrestrial networks.   
3) We explore various practical complications associated with applying AI approaches to NTN as future open issues. This helps us access the maximum potential of AI techniques while being mindful of the practical constraints of NTN integration into next-generation wireless networks.   
4) We provide insights and recommendations on various aspects of applying AI techniques to satellite-based NTNs for future 6G networks.

# B. Paper Organization

The rest of the paper is organized as follows. In Section II, we provide a compact overview discussion of NTN and its platforms, use cases, architecture, and characteristics; and discuss potential challenges associated with its deployment in 6G. In Section III, we introduce different types of AI approaches to provide a brief overview of relevant AI techniques to solve various challenges associated with NTNs. We then discuss the related surveys on AI-enabled satellite-based NTNs empowering future 6G networks in Section IV. We then summarize the existing AI approaches to address various NTN challenges categorizing them into different NTN research thrusts in Section V. Furthermore, We summarize the current research efforts from the industrial and research community to apply AI into satellite-based NTN in future 6G networks in Section VI. We also discuss the technical challenges associated with the integration of AI to NTNs in Section VII. Finally, we provide a discussion on insights and potential future studies for ensuring the proper AI-enabled satellite-based NTN in future 6G networks in Section VIII. We illustrate the structure of the paper showing the major components in Figure 1 for better understanding. We also provide the list of acronyms in Table I for the convenience of the readers.

# II. BACKGROUND ON NTN

To understand the role of AI in enabling NTNs in 6G, we provide a concise background discussion on NTNs and the challenges associated with NTNs to realize them in 6G in this section. First, we familiarize the readers with various space and air-borne NTN components along with the general architectures and use cases in 6G. We clarify that we focus on satellite-based NTN while discussing NTNs for the rest of the paper due to their critical role in enabling 6G with ubiquitous coverage, predictable trajectory, and scalability. Then we emphasize on unique characteristics of NTNs which pose new challenges for integrating them into existing terrestrial networks for 6G. Depending on the nature of these challenges, we present the current research trends in this domain in Section V by combining them with the AI techniques discussed in Section III.

![](images/29997074a858a62bfdcdfb8962b6dab239771a5d74eaa72c716bfe3a2ff643e5.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Introduction"] --> B["Background on NTN"]
    B --> C["AI and Its Relevance to NTN Challenges"]
    C --> D["Related Works"]
    D --> E["Current Research Thrusts"]
    E --> F["Current Status"]
    F --> G["Challenges"]
    G --> H["Insights and Potential Future Studies"]
    H --> I["Conclusions"]

    subgraph Inputs
        J["Frequency Band"] --> K["Definitions"]
        L["Propagation Delay"] --> M["Propagation Loss"]
        N["Moving Base Stations"] --> O["Large Cov. Area"]
        P["Propagation Loss"] --> Q["Moving Base Stations"]
        R["Large Cov. Area"] --> S["Large Cov. Area"]
    end

    subgraph Outputs
        T["Channel Estimation"] --> U["References of NTNs in 6G"]
        V["Mobility Management"] --> W["General Architecture"]
        X["Doppler Shift Estimation"] --> Y["Fundamental Characteristics"]
        Z["Resource Management"] --> AA["Spectrum Sharing"]
        AB["Network Procedures"] --> AC["Network Procedures"]
    end

    subgraph Results
        AD["Machine Learning"] & AE["Offline Learning vs Online Learning"] & AF["Deep Learning"] & AG["Major Learning Paradigms"] & AH["Distributed Learning Paradigms"] & AI["Synergy between AI and NTN"] & AJ["Federated Learning"] & AK["Decentralized Learning"] & AL["Split Learning"]
    end

    subgraph Outputs
        AM["Supervised Learning"] & AN["Unsupervised Learning"] & AO["Reinforcement Learning"] & AP["Complex Task Automation"] & AQ["Tractable Solutions"] & AR["Data-Driven Decisions"] & AS["Adaptability & Learning"] & AT["Reduced Computation Complexity"] & AU["Reduced Transmission Overhead"] & AV["Real-time Imp."] & AW["Leveraging CSI"]
    end

    subgraph Inputs
        AX["Channel Estimation"] --> AY["Doppler Shift Estimation"]
        AZ["Physical Layer Authentication"] --> BA["Intrusion Detection"]
        BB["Anti Jamming"] --> BC["Traffic Prediction"]
    end

    subgraph Outputs
        DA["ML Testbeds"] & EDA["OAI-SDR Testbeds"] & AFDA["Current Research Efforts"]
        AE["Onboard Limitations"] & AFD["Aging of Information"] & AG["Comm. Overheads"] & AH["Security Aspects"] & AI["Environmental Conditions"]
        AI["Scalability Issue"] & AJ["Lack of Convergence"] & AK["Scarcity of Quality Data"] & AL["Hyperparameter Settings"] & AM["Lack of Generalization"]
    end

    subgraph Outputs
        AN["Potential Future Studies"] --> AO["Interrelated Issues"] & AP["Recurrent Learning Architectures"] & AQ["Online Implementation"] & AR["Distributed Learning Architectures"]
        AR["Control Feedback Design"] & AH["Development in Miniaturization"] & AI["Energy Efficiency"] & AJ["Secured System Design"]
        AK --> AN
        AL --> AN
        AM --> AN
        AN --> AO
        AO --> AP
        AP --> AQ
        AQ --> AR
    end

    A --> D --> E --> F --> G --> H --> I --> J --> K --> L --> M --> N --> O --> P --> Q --> R --> S --> T --> U --> V --> W --> X --> Y --> Z --> AA --> AB --> AC --> AD --> AE --> AF --> AG --> AH
    end

    subgraph Outputs
        AH --> AA --> AB --> AC --> AD --> AE --> AF --> AG
    end

    style Inputs fill:#f9f,stroke:#333
    style Outputs fill:#bbf,stroke:#333
```
</details>

Fig. 1. Structure of the paper.

# A. Definition

Non-Terrestrial Network (NTN) refers to any network operating through the air or space-borne vehicle(s) for communication [19]. This definition implies that two distinct types of NTN platforms (space-borne and air-borne) can be utilized for NTN at different heights which is illustrated in Figure 2.

1) Space-Borne Platforms: Space-borne platforms, such as satellites, are deployed in space for communication [19]. They move around the Earth in specific orbits with varying angular velocities, relying on gravity to provide the necessary centripetal force to maintain their orbits. The orbital period of a satellite refers to the time required for the satellite to complete one full revolution around the Earth. Due to differences in orbital periods, some satellites may not be visible to ground observers all the time. To characterize this, another term is used to denote the duration of direct visibility for a satellite. This is known as the horizon time, which refers to the maximum duration during which the satellite is within the line of sight of a given ground station or receiver. Depending on their mobility with respect to the Earth, satellites can be classified into two broad categories: Geostationary (GEO/GSO) and Non-Geostationary (NGEO/NGSO) Earth Orbit satellites. We discuss these two types of satellites below and summarize their key features in Table II.

Geostationary Earth Orbit (GEO or GSO) Satellites: These satellites have an orbital period of 24 hours which is the same as the time required for the Earth to complete a full rotation on its axis. As a result, these satellites appear stationary from the ground and are named Geostationary Earth Orbit (GEO or GSO)

TABLE I   
LIST OF ACRONYMS 

<table><tr><td>Acronyms</td><td>Definitions</td><td>Acronyms</td><td>Definitions</td></tr><tr><td>3GPP</td><td>Third Generation Partnership Project</td><td>MADRL</td><td>Multi-Agent Deep Reinforcement Learning</td></tr><tr><td>5G</td><td>5th Generation</td><td>MAP</td><td>Maximum A Posteriori</td></tr><tr><td>6G</td><td>6th Generation</td><td>MARL</td><td>Multi-Agent Reinforcement Learning</td></tr><tr><td>AC</td><td>Actor-Critic</td><td>MC</td><td>Monte Carlo method</td></tr><tr><td>ACO</td><td>Ant-Colony based Optimization</td><td>MDP</td><td>Markov Decision Process</td></tr><tr><td>AI</td><td>Artificial Intelligence</td><td>MEMS</td><td>Micro-Electro-Mechanical Systems</td></tr><tr><td>ANN</td><td>Artificial Neural Networks</td><td>MEO</td><td>Medium Earth Orbit</td></tr><tr><td>AoA</td><td>Angle of Arrival</td><td>MiM</td><td>Man-in-the-Middle</td></tr><tr><td>AoD</td><td>Angle of Departure</td><td>ML</td><td>Machine Learning</td></tr><tr><td>AR</td><td>Augmented Reality</td><td>MLP</td><td>Multi-Layer Perceptron</td></tr><tr><td>ARIMA</td><td>Auto-Regressive Moving Average</td><td>MMSE</td><td>Minimum Mean Square Error</td></tr><tr><td>ARMA</td><td>Auto-Regressive Integrated Moving Average</td><td>mMTC</td><td>massive Machine Type Communication</td></tr><tr><td>ATM</td><td>Asynchronous Transfer Mode</td><td>MNL</td><td>Minimum Network Load</td></tr><tr><td>BS</td><td>Base Station</td><td>MSQ</td><td>Maximum Signal Quality</td></tr><tr><td>CCI</td><td>Co-Channel Interference</td><td>MST</td><td>Maximum Service Time</td></tr><tr><td>CDMA</td><td>Code Division Multiple Access</td><td>mULC</td><td>massive Ultra-reliable low-Latency Communication</td></tr><tr><td>CG</td><td>Coordinate Graph</td><td>NGEO/NGSO</td><td>Non-Geostationary Earth Orbit</td></tr><tr><td>CNN</td><td>Convolutional Neural Network</td><td>NN</td><td>Neural Network</td></tr><tr><td>CSD</td><td>Cyclo-Stationary Detection</td><td>NOMA</td><td>Non-Orthogonal Multiple Access</td></tr><tr><td>CSI</td><td>Channel State Information</td><td>NTN</td><td>Non-Terrestrial Networks</td></tr><tr><td>CU</td><td>Central Unit</td><td>OAI</td><td>OpenAirInterface</td></tr><tr><td>DBN</td><td>Deep Belief Network</td><td>OFDM</td><td>Orthogonal Frequency Division Multiplexing</td></tr><tr><td>DcL</td><td>Decentralized Learning</td><td>O-RAN</td><td>Open Radio Access Network</td></tr><tr><td>DDPG</td><td>Deep Deterministic Policy Gradient</td><td>OSI</td><td>Open Systems Interconnection</td></tr><tr><td>DDQN</td><td>Double Deep Q-Learning Network</td><td>OSPF</td><td>Open Shortest Path First</td></tr><tr><td>DL</td><td>Deep Learning</td><td>PCA</td><td>Principal Component Analysis</td></tr><tr><td>DN</td><td>Deconvolutional Network</td><td>PG</td><td>Policy Gradient</td></tr><tr><td>DoS</td><td>Denial-of-Service</td><td>PGM</td><td>Probabilistic Graph Model</td></tr><tr><td>DP</td><td>Dynamic Programming</td><td>PNN</td><td>Probabilistic Neural Network</td></tr><tr><td>DPG</td><td>Deterministic Policy Gradient</td><td>PSD</td><td>Power Spectral Density</td></tr><tr><td>DQN</td><td>Deep Q-Learning Network</td><td>PSO</td><td>Particle Swarm Optimization</td></tr><tr><td>DRL</td><td>Deep Reinforcement Learning</td><td>QoE</td><td>Quality of Experience</td></tr><tr><td>DRN</td><td>Deep Residual Network</td><td>QoS</td><td>Quality of Service</td></tr><tr><td>DRQN</td><td>Deep Recurrent Q-Learning Network</td><td>RC</td><td>Reservoir Computing</td></tr><tr><td>DU</td><td>Distributed Unit</td><td>RAN</td><td>Radio Access Network</td></tr><tr><td>ED</td><td>Energy Detection</td><td>RBM</td><td>Restricted Boltzmann Machine</td></tr><tr><td>eMBB</td><td>enhanced Mobile Broadband</td><td>RF</td><td>Random Forest</td></tr><tr><td>ELM</td><td>Extreme Learning Machine</td><td>RIC</td><td>RAN Intelligent Controller</td></tr><tr><td>ESA</td><td>European Space Agency</td><td>RIS</td><td>Reflective Intelligent Surface</td></tr><tr><td>ESN</td><td>Echo-State Network</td><td>RL</td><td>Reinforcement Learning</td></tr><tr><td>EVD</td><td>Eigen Value-based Detection</td><td>RMS</td><td>Root Mean Square</td></tr><tr><td>FCNN</td><td>Fully Connected Neural Network</td><td>RNN</td><td>Recurrent Neural Network</td></tr><tr><td>FDMA</td><td>Frequency Division Multiple Access</td><td>RSMA</td><td>Rate-Splitting Multiple Access</td></tr><tr><td>FL</td><td>Federated Learning</td><td>RSRP</td><td>Reference Signal Received Power</td></tr><tr><td>FlexRIC</td><td>Flexible RIC</td><td>RSRQ</td><td>Reference Signal Received Quality</td></tr><tr><td>GA</td><td>Genetic Algorithm</td><td>RU</td><td>Radio Unit</td></tr><tr><td>GDM</td><td>Generative Diffusion Model</td><td>SA</td><td>Simulated Annealing</td></tr><tr><td>GMM</td><td>Gaussian Mixture Model</td><td>SAGIN</td><td>Space-Air-Ground Integrated Networks</td></tr><tr><td>GAN</td><td>Generative Adversarial Network</td><td>SARSA</td><td>State-Action-Reward-State-Action</td></tr><tr><td>GNN</td><td>Graph Neural Network</td><td>SDMA</td><td>Space Division Multiple Access</td></tr><tr><td>GEO/GSO</td><td>Geostationary Earth Orbit</td><td>SDN</td><td>Software Defined Network</td></tr><tr><td>GNSS</td><td>Global Navigation Satellite System</td><td>SDR</td><td>Software Defined Radio</td></tr><tr><td>GPS</td><td>Global Positioning System</td><td>SINR</td><td>Signal to Interference and Noise Ratio</td></tr><tr><td>GRU</td><td>Gated Recurrent Unit</td><td>SL</td><td>Supervised Learning</td></tr><tr><td>HAPS</td><td>High Altitude Platform System</td><td>SNR</td><td>Signal to Noise Ratio</td></tr><tr><td>HARQ</td><td>Hybrid Automatic Repeat Request</td><td>SoC</td><td>System-on-Chip</td></tr><tr><td>HIBS</td><td>High-altitude International Mobile Base Station</td><td>SOM</td><td>Self-Organizing Map</td></tr><tr><td>HTC</td><td>Holographic Type Communication</td><td>SpL</td><td>Split Learning</td></tr><tr><td>IC</td><td>Integrated Circuit</td><td>SVM</td><td>Support Vector Machine</td></tr><tr><td>ICI</td><td>Inter-Carrier Interference</td><td>TDD</td><td>Time Division Duplexing</td></tr><tr><td>IoT</td><td>Internet of Things</td><td>TDMA</td><td>Time Division Multiple Access</td></tr><tr><td>IP</td><td>Internet Protocol</td><td>TNTN</td><td>integrated Terrestrial and Non-Terrestrial Network</td></tr><tr><td>ISL</td><td>Inter-Satellite Link</td><td>UE</td><td>User Equipment</td></tr><tr><td>ITU</td><td>International Telecommunication Union</td><td>UL</td><td>Unsupervised Learning</td></tr><tr><td>KKT</td><td>KarushKuhnTucker</td><td>ULBC</td><td>Ultra-reliable low Latency Broadband Communication</td></tr><tr><td>KNN</td><td>k-Nearest Neighbor</td><td>uMBB</td><td>ubiquitous Mobile BroadBand</td></tr><tr><td>KPI</td><td>Key Performance Indicator</td><td>URLLC</td><td>Ultra Reliable Low Latency Communication</td></tr><tr><td>LEO</td><td>Low Earth Orbit</td><td>V2X</td><td>Vehicle-to-Everything</td></tr><tr><td>LoS</td><td>Line of Sight</td><td>VR</td><td>Virtual Reality</td></tr><tr><td>LSM</td><td>Liquid State Machine</td><td>VSAT</td><td>Very Small Aperture Terminal</td></tr><tr><td>LSTM</td><td>Long-Term Short Memory</td><td>WMMSE</td><td>Weighted Minimum Mean Square Error</td></tr></table>

Satellites. These satellites orbit on the Earth’s equatorial plane at an altitude of about 35,786 km to maintain this orbital period. Due to this high altitude, it has an extremely large beam footprint (typically the diameter ranges from 200 to 1000 km) covering a pretty wide area. However, it also incurs an extremely long propagation delay (typically around 270 ms) [20] which makes it infeasible for low-latency communications. These satellites have been used in broadcasting services for a very long time, but are not very suitable for low-latency emerging applications.

![](images/416a748d071077cd47f200322431f5af18155574559302c289043295af33af67.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Spaceborne platforms"] --> B["GEO Satellite"]
    A --> C["MEO Satellite"]
    A --> D["LEO Satellite"]
    A --> E["Airborne platforms"]
    B --> F["HAPS Airships"]
    C --> F
    D --> F
    E --> F
    F --> G["Ground"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#ccf,stroke:#333
    style D fill:#ccf,stroke:#333
    style E fill:#ccf,stroke:#333
    style F fill:#cfc,stroke:#333
    style G fill:#fcc,stroke:#333
    subgraph Coverage Type
        H["Tran Terrestrial BS"]
        I["Rural"]
        J["Remote"]
        K["Isolated"]
    end
    H --> L["Ground"]
    I --> L
    J --> L
    K --> L
    L --> M["10 km Ground"]
    style H fill:#fff,stroke:#333
    style I fill:#fff,stroke:#333
    style J fill:#fff,stroke:#333
    style K fill:#fff,stroke:#333
    style L fill:#fff,stroke:#333
```
</details>

Fig. 2. An illustration of different NTN components in 6G.

TABLE II KEY FEATURES OF DIFFERENT TYPES OF SATELLITES 

<table><tr><td>Attribute</td><td>GEO</td><td>MEO</td><td>LEO</td></tr><tr><td>Orbital height (km)</td><td>35786</td><td>2000-25000</td><td>200-2000</td></tr><tr><td>Typical diameter of beam footprint (km)</td><td>1000</td><td>500</td><td>100</td></tr><tr><td>Propagation delay (ms)</td><td>270</td><td>94</td><td>12-25</td></tr><tr><td>Orbital period (hours)</td><td>24</td><td>12</td><td>1.5-2</td></tr><tr><td>Horizon time</td><td>24 hours</td><td>1-2 hours</td><td>5-10 minutes</td></tr></table>

Non-Geostationary Earth Orbit (NGEO or NGSO) Satellites: As the name suggests, these satellites orbit around the Earth at a period lower than 24 hours, so they are not stationary with respect to a ground observer. As the orbital period is smaller, their angular velocity is also higher but the altitude is lower compared to GEO satellites. Depending on the heights, they can be divided into two categories: Low Earth Orbit (LEO) and Medium Earth Orbit (MEO) satellites. Typically they are deployed at a height ranging from 200 to 2000 km for LEO and 2000 to 25000 km for MEO satellites. The horizon time is much smaller for NGEO satellites due to smaller orbital

periods, for example, the LEO satellites deployed at a height of around 500-600 km with an orbital period of 1.5-2 hours can have a horizon time of 5-10 minutes depending on channel conditions. Due to smaller heights, these satellites have a smaller beam footprint (diameter ranges from 5 to 500 km) with a much smaller propagation delay (typically around 20 ms for LEO satellites and 94 ms for MEO satellites) [20] compared to GEO satellites. With their proximity to Earth and lower cost of launch and maintenance, these satellites, especially the LEO satellites, have gained significant attention in recent years. Their reduced propagation delay and path loss make them an attractive choice for facilitating highspeed data transfer and real-time communication, so as to transform the future 6G connectivity.

2) Air-Borne Platforms: High Altitude Platform Systems (HAPS) refer to air-borne platforms that can be used for wireless communication. Airships, balloons, and airplanes are the most prominent types of air-borne platforms in NTN. They are viewed as air-borne counterparts of terrestrial base stations serving as High-altitude International Mobile Base Stations (HIBS) [21]. They usually operate at the stratosphere region with an altitude of around 20 km and a beam footprint size with a diameter of several km. Despite it having a lot smaller propagation delay compared to space-borne platforms, it has some additional challenges related to stabilization on air and refueling.

While both satellites and airborne platforms can be utilized in the development of NTNs, satellites are often considered more critical for discussions related to NTNs. This is due to their global coverage, stable and predictable orbits, high scalability, and the existence of international regulations that govern satellites. As such, satellite networks comprise a significant portion of future NTN-enabled communication networks. Therefore, for the purposes of this article, we will primarily focus on satellite-enabled NTNs in the context of 6G communication technology.

# B. Role of NTN in 6G

NTNs are anticipated to be a major component of 6G communication systems, providing a wide array of vertical services, such as transport, health, energy, automotive, public safety, and many more. The International Telecommunication Union (ITU) has identified three major categories of applications for 5G that are based on network performance and user Quality of Experience (QoE): (1) eMBB: extremely high bandwidth with moderate latency requirements, for example, multimedia applications; (2) mMTC: low power and bandwidth and no strict delay requirements, for example, IoT; and (3) URLLC: low latency and high-reliability requirements, for example, remote medical surgery. However, future applications such as AR, VR, Tactile Internet, HTC, intelligent transport and automation, multi-sense communication, global ubiquitous connectivity, etc. require extremely high throughput, low latency, high reliability, and ubiquity at the same time which cannot be met with current 5G standards [4]. Based on the characteristics, these new applications are classified into three more new groups,

1) Ubiquitous MBB (uMBB): High throughput and extreme coverage requirements, combining both eMBB and mMTC. Examples: Digital twins, pervasive intelligence, global ubiquitous connectivity, etc.   
2) Ultra-Reliable Low Latency Broadband Communication (ULBC): High throughput and low latency requirements, combining both eMBB and URLLC. Examples: HTC, AR, VR, Tactile Internet, multi-sense experiences, etc.   
3) Massive Ultra-Reliable Low-Latency Communication (mULC): Extreme coverage and low latency requirements, combining both mMTC and URLLC. Example: Vehicle-to-Everything (V2X), intelligent transport and automation, etc.

The principal strength of NTNs lies in their extreme coverage. As discussed in Hexa-X project [22], a flagship for B5G/6G vision and intelligent fabric of technology enablers connecting human, physical, and digital worlds, the vision of enabling 6G networks towards provisioning service everywhere and always through NTN is presented. Due to its extreme coverage, satellites can reach underserved or unserved areas such as islands, remote locations, ships, airplanes, etc. where terrestrial communication is either difficult or impossible to some extent. In times of natural disaster, terrestrial links can be unavailable, in which case users can benefit from the reliable backup of non-terrestrial links. This ensures resilient and robust communication with global connectivity which is considered to be one of the main features of future 6G networks. With the advancements in antenna techniques and miniaturization, high throughput satellites are also deployed in low earth orbits. Consequently, current 5G use cases such as mMTC and eMBB as well as future 6G use cases such as uMBB can be the most important use cases for NTNs. Furthermore, the considerably low latency for LEO satellite systems makes the satellite useful even for low-latency applications. However, 5G URLLC or 6G new use cases with extremely low latency may not be directly applicable for NTN use cases. Nevertheless, NTNs can still be beneficial for these use cases in conjunction with terrestrial networks to improve network efficiencies and reliability. Combining all these, satellites are expected to be one of the major driving forces toward revolutionizing the future 6G applications extensively.

# C. General Architecture

Satellites can employ a transparent payload configuration, acting as a relay that performs RF filtering, frequency conversion, and amplification to facilitate communication between UEs and ground stations. Alternatively, they can utilize a regenerative payload configuration, which involves payload processing after modulation and coding, and act as base stations with additional onboard processing capabilities. Besides, the satellites can provide backhaul support for the core networks of terrestrial networks. The general architecture for a satellite-based NTN for the above-mentioned different configurations as per release 16 and 17 is discussed below [20], [23]:

1) Satellite: Satellite is the key component of this architecture. It carries the payload between the UE and the ground station as shown in Figure 3. In the case of a transparent payload, it works as a simple relay that transmits the payload after RF filtering, frequency conversion, and amplification to the ground station (or UE). Conversely, in the case of a regenerative payload, it processes the payload after modulation and coding on top of these actions, so it works like a BS that needs onboard processing capabilities. Also as per [23], satellites can provide backhaul by providing a connection between ground BS and the core network as illustrated in Figure 3.   
2) Gateway: Gateway refers to the ground station that connects NTN to the public data network. In the case of a transparent payload, the ground terminal needs to be equipped with a terrestrial base station. In the case of a regenerative payload and satellite backhaul support, the ground terminal only relays the received information to the core networks.   
3) User Equipment (UE): User equipment is either handheld or Very Small Aperture Terminal (VSAT) within the coverage area of the satellite.   
4) Feeder Link: Feeder link connects a satellite to the gateway.   
5) Service Link: Service link connects UEs to the serving satellite.   
6) Inter-Satellite Links (ISLs): ISLs provide connectivity between multiple satellites deployed in NTN so that a payload can be delivered to other cells.

![](images/02200b4a9ab9c9593d0c96d3cd4812e9d583bbab41aaa8e0e58a7a67b29e8396.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph_BS["Satellite (BS)"]
        A["Regenerative Payload"] --> B["Service Link"]
        A --> C["Feeder Link"]
        A --> D["Ground Terminal"]
        E["Satellite (Backhaul)"] --> F["Feeder Link"]
        E --> G["Service Link"]
        H["Satellite (Backhaul)"] --> I["Ground Terminal"]
        H --> J["Ground BS"]
        K["Satellite (Backhaul)"] --> L["Service Link"]
        M["Satellite (Backhaul)"] --> N["Ground Terminal"]
        O["Satellite (Backhaul)"] --> P["Ground BS"]
        Q["Satellite (Backhaul)"] --> R["Service Link"]
        S["Satellite (Backhaul)"] --> T["Ground Terminal"]
        U["Satellite (Backhaul)"] --> V["Ground BS"]
        W["Satellite (Backhaul)"] --> X["Service Link"]
    end

    subgraph_Relay["Satellite (Relay)"]
        Y["Transparent Payload"] --> Z["Feeder Link"]
        Y --> AA["Service Link"]
        AB["Satellite (Relay)"] --> AC["Ground BS"]
        AD["Satellite (Relay)"] --> AE["Ground Terminal"]
        AF["Satellite (Relay)"] --> AG["Service Link"]
    end

    subgraph_Core["Next Generation Core"]
        AH["Data Network"] --> AI["Cloud Cloud"]
    end
```
</details>

Fig. 3. General communication architecture for satellite-based NTN.

# D. Fundamental Characteristics of NTN

NTN presents us with several potentially promising use cases for the next generation of wireless networks as discussed in Section II-B. However, as can be seen from Section II-A, it also has a number of unique characteristics due to the large distances between satellites and ground transceivers, the high mobility of NGEO satellites, and the proposed frequency range for operation. In this subsection, we will delve into these features of NTN and discuss their impact on network performances and procedures.

1) Target Frequency Band: The allowable frequency range of operation is 0.5-100 GHz [24]. Traditionally, six major frequency bands within this range are used in satellite communications, which are listed below:

1) L-Band (1-2 GHz): Global Positioning System (GPS) carriers and satellite mobile phones, e.g. Iridium, use this band.

2) S-Band (2-4 GHz): This frequency band is used for weather radar, marine radar, etc. satellite communications.

3) C-Band (4-8 GHz): Primarily used for satellite television broadcasting.

4) X-Band (4-8 GHz): Primarily used in military communications.

5) Ku-Band (12-18 GHz): Primarily used for satellite broadcasting services.

6) Ka-Band (26-40 GHz): This frequency band is used for high-speed data transmission, including broadband Internet access via communication satellites.

However, as per 3GPP, currently, two frequency bands (S and Ka-band) are targeted in particular for integrated TNTN environments considering performance and regulatory concerns [20]. The two target frequency bands are:

S-Band: The downlink frequency band is 2170- 2200 MHz and the uplink frequency band is 1980-2010 MHz.

Ka-band: The downlink frequency band is 19.7- 21.2 GHz and the uplink frequency band is 29.5-30 GHz.

2) Propagation Delay: Propagation delay is the time duration taken for a signal to reach its destination. For communication signals, we can calculate the propagation delay for a signal by using the equation: $\textstyle t = { \frac { d } { c } }$ where d is the distance between the source and destination and $c = 3 \times 1 0 ^ { 8 }$ m/s is the speed of light. Considering the speed of light as a constant, we observe the propagation delay for a signal is proportional to the propagation distances. Satellites are located very far from the surface of the earth as discussed in Section II-A. Consequently, the propagation delay is going to be extremely large for NTNs. The GEO, MEO, and LEO satellites can have a one-way propagation delay of about 270, 94, and 20 ms respectively as shown in Table II. These values are much larger, especially for GEO and MEO cases compared to conventional terrestrial networks, which generally have a very negligible propagation delay of around a few $\mu s$ [20]. This extended propagation delay has an effect on different network procedures and performances for communication systems.

3) Propagation Loss: The propagation loss, or path loss, refers to the reduction in power density that an electromagnetic signal experiences as it travels through space. The most significant component of this path loss is the free space path loss, which is proportional to the distance between the source and destination and the frequency of the signal [25]. For NTNs, this free space path loss is much higher (around 60-120 dB) than it is for terrestrial networks, due to the greater distances between satellites and the use of higher carrier frequencies. In fact, the Ka-band is not suitable for GEO satellites, as it does not meet the minimum link budget for them. The basic path loss component also includes shadow fading [26], as with traditional terrestrial networks.

In addition to that, there is attenuation due to atmospheric gases that depends on frequency, elevation angle, altitude above sea level, and water vapor density [27]. Another important component is attenuation due to rain and fog, which is typically significant for frequencies above 6 GHz [28]. Additionally, scintillation corresponds to rapid fluctuation in amplitude and phase of the propagating signal in the ionosphere (for Sub-6 GHz) and troposphere (for above 6 GHz) [29]. Depending on different scenarios, either flat fading based on ITU two-state model [30] or fast fading [20] can be considered. The average propagation loss for different types of satellites in different frequency bands is illustrated in Figure 4. This high path loss necessitates the need for efficient power allocation strategies in NTN.

![](images/680f43a4655adb39b6a725840a042c619a700020da97f2de1119d02bbd7f2c12.jpg)

<details>
<summary>line</summary>

| Elevation Angle (degree) | 2 GHz-GEO | 20 GHz-LEO-1400 km | 20 GHz-LEO-550 km | 2 GHz-LEO-1400 km | 2 GHz-LEO-550 km |
| ------------------------ | --------- | ------------------ | ----------------- | ----------------- | ---------------- |
| 10                       | 193       | 192                | 184               | 170               | 163              |
| 20                       | 193       | 189                | 181               | 168               | 160              |
| 30                       | 193       | 187                | 179               | 166               | 158              |
| 40                       | 193       | 185                | 177               | 164               | 156              |
| 50                       | 193       | 184                | 175               | 163               | 155              |
| 60                       | 193       | 183                | 174               | 162               | 154              |
| 70                       | 193       | 182                | 173               | 162               | 153              |
| 80                       | 193       | 182                | 173               | 162               | 153              |
| 90                       | 193       | 182                | 173               | 162               | 153              |
</details>

Fig. 4. Propagation loss for satellites at different heights and with different carrier frequencies.

4) Moving Base Stations: As discussed in Section II-C, for regenerative payloads, satellites can be used as base stations for improved network performances. The terrestrial base stations are located at fixed locations. As the GEO satellites do not change their relative positions with respect to the ground terminal, they appear static in nature with respect to the earth’s surface, so the scenario is similar to terrestrial ones. However, the scenario is very different for NGEO satellites where they need to maintain a lower height and higher angular velocity compared to GEO satellites as discussed in Section II-A, so they do not appear static from the earth’s surface. Due to the dynamic nature of NGEO satellites, they turn into moving base stations in case of regenerative payloads. Due to this highspeed movement of NGEO satellites, different mobility issues arise for NTN platforms.

5) Coverage Area: One of the most important features of the satellites is the large beam footprint associated with them due to their long distances from the earth’s surface. This enables the network coverage of very large areas compared to the coverage area of terrestrial counterparts. It provides us with ubiquitous network coverage including remote, even isolated areas. However, this also creates the necessity for modifications in existing timing and synchronization procedures for conventional terrestrial networks. The cell area is much larger, so the UEs situated at the farthest side of the cells experience a larger delay compared to the UEs situated closer

to the satellites [20]. So the timestamps for different network procedures need to be modified according to the distances of the users as we will see in the next subsection.

# E. Challenges Associated With NTN

NTN offers a range of unique features due to the large distances between the transceivers and the high mobility of NGEO satellites, as outlined in Section II-D. These features open up possibilities for new use cases, taking advantage of the extensive coverage offered by the satellites. The high mobility of the satellites also allows for the deployment of satellites across the globe to provide global network coverage. However, NTN also presents a number of new challenges that must be tackled due to these characteristics, which are discussed in detail below:

1) Channel Estimation: In wireless communications, Channel State Information (CSI) refers to the information which represents the state of a communication channel between the transmitter(s) and the receiver(s); the process of obtaining this information is known as channel estimation. By having access to CSI, it is possible to adjust transmissions to the current channel conditions, which is essential for achieving reliable communication with high data rates in multi-antenna systems with effective channel resources and interference management. There are numerous advanced approaches, such as Maximum Likelihood estimation and Minimum Mean Square Error (MMSE) estimation, for effective channel estimation in traditional terrestrial cellular networks. Nevertheless, these methods are not well-suited for NTN, particularly for LEO satellites due to the inherent time-variant nature of the satellite communication channels. LEO satellites usually move from horizon to horizon in approximately 5-10 minutes, so a UE remains within the coverage of a specific LEO satellite for a very short time period. Furthermore, the propagation delay for satellite networks, especially in the case of GEO satellites, is considerably larger (250 ms RTT) in comparison to general terrestrial networks. Therefore, the CSI estimated by the LEO satellites can be outdated [31]. Because of these reasons, the CSI estimation in NTN necessitates new efficient techniques in addition to the traditional terrestrial estimation methods.

2) Mobility Management: Since an NGEO satellite operates at a lower altitude, the coverage area of each NGEO satellite is smaller than that of a GEO satellite. Typically around 5-20, NGEO satellites form complex megaconstellations to sustain global coverage across the earth. The NGEO satellite needs to move at a much higher speed than the earth’s rotational speed (can be up to around 7.8 km/s) to get the necessary centripetal force to move around the earth at that low altitude. As a result, these satellites typically orbit around the earth pretty fast (usually within around 2-10 hours) as discussed in Section II-A. This quick orbital motion poses a great challenge for integrating NGEO satellites into traditional wireless communication systems. Due to the smaller orbital period, any specific terrestrial UE can be only visible to an NGEO satellite for a very short span of time, typically several minutes. So the UE needs to undergo multiple handovers within a short span of time interval regardless of its mobility [14]. If the satellite covers an area using multiple spot beams, the scenario is worse because the spot beam is much smaller compared to a total coverage area of an NGEO satellite. So the UEs need to through multiple (beam) handovers within a few minutes, even when they are stationary, for seamless continuation of data sessions. This frequent handover phenomenon in NGEO satellite networks creates a lot of overhead in communication channels, leading to an overall degradation in network performance.

3) High Doppler Shift: Doppler shift is the shift in the signal frequency due to the motion of the transceivers. In the case of NGEO satellites, satellites are moving at a very high speed under a specific constellation. Due to this relative motion between UEs and satellites, Doppler shift happens in the original signal frequency. Due to frequency offsets, UEs tune to different carrier frequencies than the original carrier frequencies. So the frequency synchronization is lost, and the UEs may interfere with the other users. This is known as Inter-Carrier Interference (ICI) between multiple UEs. Generally, even for the high mobility scenarios in terrestrial networks, the frequency shift is pretty negligible, and so is the Doppler shift. However, the frequency offset is pretty significant in NTN due to the much higher speed of the NGEO satellites. The Doppler shift value mainly depends on the carrier frequency and height of the satellites. For NGEO satellites operating at Ka-Band, the Doppler shift can go from 225 kHz to even 720 kHz [20] depending on the heights. This can cause significant ICI among NTN users which requires efficient strategies for compensation of the Doppler effect.

4) Resource Management: Spectrum and power are the two fundamental resources for any communication system. In NTN, the allocation of these two resources becomes an even more complex problem due to the high path loss and limited spectrum availability. As discussed in Section II-D, the path loss associated with Non-Terrestrial Networks is much higher compared to terrestrial networks. To correctly decode the transmitted symbols from the received signals, the received signal needs to meet the minimum RSRP requirement. That means the transmitted signal power needs to be much higher (typically at least 10 times the terrestrial transmitted signals) than terrestrial signals. This poses a great obstacle for traditional UEs as they have power limitations. Furthermore, the target frequency bands as discussed in Section II-D for NTN are limited. To support a large number of satellite UEs, this spectrum resource appears to be scarce in NTN systems. So efficient resource (spectrum and power) allocation strategies are needed for integrating NTN into terrestrial networks.

5) Spectrum Sharing: As discussed in Section II-D, the S-Band and Ka-Band are the target bands for NTN. On top of this limited spectrum allocation, we have interference from terrestrial users in these bands. In S-Band, we already have existing terrestrial communication from 4G LTE devices. With the advent of mm-wave technology, terrestrial communication is also using the Ka-band in 5G. So the satellite users will suffer from co-channel interference with the terrestrial users in both bands. To avoid this interference, we have to come up with efficient spectrum-sharing techniques to put

the interference below a certain threshold ensuring proper decoding of the received signals.

6) Effect on Network Procedures: Timing advances ensure synchronous uplink transmissions for all UEs. The UEs can be located at different distances from the gNB, so there is a differential propagation delay between different UEs. If the uplink reception is not synchronized, the gNB needs to make sure the allocation of resource blocks to a specific UE does not include the resource blocks already in use by other UEs, which is inefficient in terms of resource allocation. Due to the long propagation delay, the TA is much larger than the transmission time slots in NTN compared to NR. Also due to the mobility of LEO satellites, the delay is time-varying and TA needs dynamic updates for proper uplink alignments. The other processes affected by the long propagation delay are Random Access, Hybrid Automatic Repeat Requests (HARQ) procedures, etc [20]. These procedures need to be modified properly to compensate for the long propagation delay.

7) Network Aspects: On top of all these challenges, integration into existing terrestrial networks comes with several open research issues to be addressed. Computational offloading, which involves transferring the computational burden to satellite networks for supporting devices with low computing power, particularly in IoT applications, gets complicated due to extended propagation delay and highly mobile NGEO satellites. Network routing has been studied for a long time, and network slicing has been discussed since the implementation of 5G. However, with the emergence of NTN, the integration of terrestrial networks calls for research in this area with new effective strategies. The ever-changing network topology of mobile NTN platforms makes it challenging to solve these problems in a complex environment.

Key Takeaways: We note that satellite-based NTNs can be extremely useful to provide ubiquitous connectivity, service continuity, and extreme reliability for diverse future 6G applications. Nevertheless, the extreme nature of the satellite networks, e.g., long distance between transceivers, high mobility for NGEO satellites, spectrum sharing with existing services, and high propagation loss, etc. impose a highly challenging environment to address for the research community. These challenges also open a new door for AI applications to move toward the future 6G revolution. In the following section, we discuss how AI can be incorporated so that we can address the issues for potential TNTN integration for future 6G networks.

# III. AI AND ITS RELEVANCE TO NTN CHALLENGES

AI refers to the simulation of human intelligence processes (e.g. visual reception, speech recognition, computer vision, etc.) by machines, especially computer systems. This human-level cognitive ability is achieved through either some predefined algorithms or learning from data-based approaches [15]. Many practical systems are very diverse and complex. The rule-based approaches are not very feasible for these systems because of an enormous number of scenario possibilities. As a result, the learning-based approaches show a lot more promise compared to predefined approaches in these types of real systems. As our focus for this paper is mostly on NTN which has an extremely complex and time-variant topology, we focus on learning-based approaches when we consider AI. In this section, we give an overview of these approaches to get an intuition of how these approaches can be useful in solving NTN issues discussed in the next section.

![](images/88863fc46db9ebf9922bb47c9654f179b12949174266b48ca83b8b9585eeab62.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Choice of learning approach"] --> B["Preliminary ML model"]
    C["Selecting values for model parameters"] --> B
    D["Model initialization"] --> B
    E["Environment/Source"] --> F["Training Data"]
    F --> G["Preliminary ML model"]
    G --> H["Performance evaluation"]
    H --> I["Model Adaptation"]
    I --> G
    J["Testing Data"] --> K["Trained ML model"]
    K --> L["Performance evaluation"]
    M["Training Data"] --> N["Training Data"]
    O["Testing Data"] --> P["Training Data"]
    Q["After Training"] --> K
```
</details>

Fig. 5. Generic ML model.

# A. Machine Learning (ML)

Machine Learning (ML) is a special subset of AI approaches where machines learn algorithms to perform a task by generalizing from past experiences or historical data without being explicitly programmed for it [32]. The performance of human intelligence processes can be improved with each iteration evolving through new feature extractions in ML approaches. Generally speaking, each ML approach has three distinctive features, namely task, performance measure, and experience [33]. A machine is first assigned to learn to perform a specific task. It starts with a model with an initial set of random parameters. Then at every iteration, the model is recalculated based on some performance measures, essentially representing the learning process. Thus utilizing experiences, it can learn how to perform the task properly which is the main goal of ML approaches.

A generic ML model works in three phases utilizing various components [16] - Pre-Training Phase, Training Phase, and Testing Phase. We discuss the fundamental components of these three phases as shown in Figure 5 below:

1) Pre-Training Phase: The Pre-Training Phase includes the choice of learning approach along with the necessary model initialization. The selection and design of the learning approach greatly depend on the nature of the problem for the learning systems. We show in the next few subsections different learning strategies for different problems. Each ML model generally requires some initial set of parameters and initialization that need to be carefully tuned to achieve expected performances.   
2) Training Phase: After setting up the preliminary model with initialization, the most important phase – training begins. The training data is provided as input to the initial model. Typically the raw data collected for a specific problem may not be properly structured to be used for the model. Moreover,

these data may contain redundant and unnecessary information which is not beneficial for learning the model. Consequently, data needs to be preprocessed in a suitable manner to have good performance. The features also need to be chosen in such a way that they can capture the correlation for empowering the learning process. The output of the model is fetched for performance evaluation. Based on the feedback from the evaluators, the model is adapted to improve its performance. This whole learning process is known as ‘training’.

3) Testing Phase: After the training, we have a trained ML model based on our provided data. This model can be used to later evaluate in the real environment. Similarly, as training data, testing data can be generated and preprocessed for evaluation. The performance evaluator provides the accuracy of the model using the testing data as inputs. This whole process is known as ‘testing’. In the case of offline learning, the testing phase starts once the training is done. On the other hand, in the case of online training, the testing is generally executed in a parallel manner with training.

# B. Offline vs Online Learning

Depending on the training approach, learning can be either offline or online. In the case of offline training, training data is generated in the pre-training phase all at once and can be used to train the model. In this case, training continues until some predefined number of iterations or some constraints are met. In the case of online training, training data is generated in an incremental manner instead of being generated all at once. So the difference between the training and testing phases is blurred as discussed in Section III-A. This specifically suits the fast-changing environment like wireless networks and provides benefits in terms of scalability, adaptability, and realtime learning.

# C. Deep Learning (DL)

In complex real-world problems, feature extraction can turn out to be extremely challenging using generic ML models. There may be hundreds of parameters that need to be learned and the outputs may not be linearly correlated to the inputs. So general ML models may not provide satisfactory performance in learning these problems. To facilitate mapping outputs to inputs, Neural Networks (NNs) [34] are widely used in ML frameworks. With the availability of a large amount of data, NNs have emerged as a key technology to be used in ML in the recent past. The learning process can be largely benefited from the introduction of NNs to deal with complicated large-scale problems. This learning process involving NNs to estimate the models is known as Deep Learning (DL) [17] which is a special important subset of ML.

NNs are inspired by the biological neural networks in the brain, more specifically the nervous system. To mimic the operation of the brain, the NNs are composed of multiple layers where each layer consists of multiple neurons followed by an activation function. Generally, the neurons in one layer are connected to the neurons in the adjacent layers. The connecting edges have weights that represent the relationship between the neurons. Each layer output can be viewed as some intermediate decisions which eventually result in the final output values. The weights are generally trained through a number of iterations using backpropagation algorithms [35]. Generally, the cost function associated with the model to calculate the difference between the predicted and actual outputs is not very simple, so we use different numerical methods like Gradient Descent [36], Stochastic Gradient Descent [37], Mini-Batch Stochastic Gradient Descent [38], Newton’s method [39] etc. and so on to estimate the gradients of the cost function with respect to corresponding weights. At each iteration, the weights are updated by an amount based on these calculated gradients and a predefined learning rate. As we move towards the gradient descent direction, it helps us to reduce the cost at every iteration. In this manner, we can map the inputs to outputs through NNs.

![](images/300ccc0dc737398ea9f3a364da094b33e6c03ed63928de9621fefcdc8bee25d8.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Supervised Learning"] --> B["Machine Learning"]
    C["Reinforcement Learning"] --> B
    D["Unsupervised Learning"] --> B
    E["Naive Bayes"] --> A
    F["Linear Regression"] --> A
    G["Decision Tree"] --> A
    H["Support Vector Machine"] --> A
    I["Logistic Regression"] --> A
    J["Model Based Methods: Dynamic Programming Monte Carlo Method"] --> B
    K["Model Free Methods: Q Learning SARSA Policy Gradient"] --> B
    L["K-means clustering"] --> B
    M["K-nearest neighbors"] --> B
    N["Principal Component Analysis"] --> B
```
</details>

Fig. 6. Taxonomy of ML approaches.

![](images/feabfffb25c59533754e5b0e571766d231440380ae8399f1144158d8fa839d88.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph Input Layer R4
        A1["•"] --> B1["•"]
        A2["•"] --> B2["•"]
        A3["•"] --> B3["•"]
        A4["•"] --> B4["•"]
    end
    subgraph Hidden Layer R6
        B1 --> C1["•"]
        B2 --> C2["•"]
        B3 --> C3["•"]
        B4 --> C4["•"]
    end
    subgraph Hidden Layer R6
        C1 --> D1["•"]
        C2 --> D2["•"]
        C3 --> D3["•"]
        C4 --> D4["•"]
    end
    subgraph Output Layer R1
        D1 --> E1["•"]
        D2 --> E2["•"]
        D3 --> E3["•"]
    end
    A1 --> B1
    A1 --> B2
    A1 --> B3
    A1 --> B4
    A2 --> B1
    A2 --> B2
    A2 --> B3
    A2 --> B4
    A3 --> B1
    A3 --> B2
    A3 --> B3
    A3 --> B4
    A4 --> B1
    A4 --> B2
    A4 --> B3
    A4 --> B4
    A5 --> B1
    A5 --> B2
    A5 --> B3
    A5 --> B4
    A6 --> B1
    A6 --> B2
    A6 --> B3
    A6 --> B4
```
</details>

Fig. 7. Fully Connected Neural Network (FCNN).

# D. Major Learning Paradigms

Depending on how an algorithm is being trained and on the basis of the availability of the output for training, learning approaches can be classified mainly into three categories: Supervised Learning (SL), Unsupervised Learning (UL), and Reinforcement Learning (RL). A short overview of different types of learning approaches is shown in Figure 6. These approaches are discussed below:

1) Supervised Learning (SL): In an SL model, a training dataset containing a set of features as inputs and corresponding current outputs is provided to the model. The model with an initial set of parameters is trained through a number of iterations for mapping inputs to outputs. As the output label is clearly defined, the model can improve its performance by comparing its predicted outputs with the actual outputs [40]. SL problems can be broadly classified into two categories depending on the type of output labels: regression and classification problems. Regression [41] is a statistical method that investigates the relationship between a dependent (target) variable to one or more independent (given) variables. In this method, the functional mapping between inputs and outputs is estimated by minimizing the error between the predicted and actual outputs. Here the output label can be continuous. In classification, the output labels correspond to distinct classes arising in computer vision, image classification, etc. Generally, classification problems are solved by using probabilistic classifiers to map output classes from inputs. To train complex SL problems, NNs are used to learn complicated functional mapping between inputs and outputs. We discuss the major ML and DL approaches in the context of SL problems below:

ML Approaches: There are a number of SL algorithms to train the model. Linear regression [42] focuses on regression problems, whereas logistic regression [43] focuses on classification problems. Decision tree is used in classification problems by forming a tree-like structure to learn the best split at every node level based on a statistical measure like information gain [44]. The classification starts at the root node and traverses down along the branches based on intermediate decisions till the leaf nodes which represent the final classification decisions. Naive Bayes Model [45] is a form of a simple probabilistic classifier that uses the Bayesian Theorem to decide the classes under the strong assumption of feature independence. It is very useful, especially in highdimensional classification problems. Support Vector Machine (SVM) [46] is another important type of classifier that decides the splitting hyperplane between different classes by maximizing the distances between the nearest data point (in both classes) and the hyperplane.

DL Approaches: Different DL approaches are also proposed in the literature to tackle complicated SL problems effectively. Perceptron [47] is one of the first NN architectures that have been proposed. It is a single-layer NN that can do binary classification like logistic regression. The main difference is to introduction of a simple activation function (step function) as a first step to more complex and advanced architectures. The simplest multi-layer NN architecture is the Fully Connected Neural Networks (FCNN) (Figure 7). This is also known as Multi-Layer Perceptron (MLP). It has multiple hidden layers between the input and output layers without any back loops. As the name suggests, all the neurons between two adjacent layers are connected to each other. Extreme Learning Machine (ELM) [48] is a very special type of NNs where the neurons are randomly connected and the training is done one-shot using least square fits. Another different type of NN is the Deep Residual Network (DRN) [49] with extra connections passing input from one layer to a later layer as well as the next layer. There are also Probabilistic Neural Networks (PNN) [50] which can recognize the underlying pattern and generate the probability distribution function for different classes.

Convolutional Neural Networks (CNN) [51] is an important type of NN that can take multidimensional inputs like images and classify them with great accuracy by discovering spatial features (Figure 8). The CNNs are composed of convolutional layers and subsequent pooling layers. The convolutional layers divide the whole input into smaller blocks and scan through them to learn the different features. The idea is to exploit the high correlation among neighboring cells with reduced complexity. A pooling layer is used to simplify this extraction process by getting rid of redundant features. Often CNN is accompanied by an FCNN to take care of nonlinearity and generate final classification results. A counterpart of CNN is the Deconvolutional Network (DN) [52] which takes the classes as inputs and generates CNN input features by comparing them with actual CNN inputs.

![](images/e5d0293c99124c2d7e04e2fec46be790a95a785cad869c4312327280c31a6f05.jpg)

<details>
<summary>text_image</summary>

8@64x64
16@48x48
16@16x16
1x256
1x10
Convolution
Max-Pool
Dense
</details>

Fig. 8. Convolutional Neural Network (CNN).

![](images/06273f43bba13f0df301162a9b8246d4b3e05fe66684e480c786a7cfb60f853d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A1["Input Layer"] --> B1["Hidden Layer 1"]
    A1 --> B2["Hidden Layer 2"]
    A1 --> B3["Hidden Layer 3"]
    A1 --> B4["Hidden Layer 4"]
    A2["Input Layer"] --> B1
    A2 --> B2
    A2 --> B3
    A2 --> B4
    A3["Input Layer"] --> B1
    A3 --> B2
    A3 --> B3
    A3 --> B4
    A4["Input Layer"] --> B1
    A4 --> B2
    A4 --> B3
    A4 --> B4
    B1 --> C["Output Layer"]
    B2 --> C
    B3 --> C
    B4 --> C
```
</details>

Fig. 9. Recurrent Neural Network (RNN).

Another important type of NN is Recurrent Neural Networks (RNN) [53] with back loops. So the neurons in a layer are not only connected to previous layer neurons but also can be connected to the neurons from the subsequent layers. (Figure 9) This allows it to capture temporal correlation among different layers and can be useful where decisions from past iterations or samples can influence current ones. However, they suffer from vanishing gradient issues due to long-term temporal dependencies [54]. To tackle this issue more sophisticated architectures like Gated recurrent units (GRU) [55] and Long-Term Short Memory (LSTM) [56] with special memory cells and gates are introduced. Reservoir computing (RC) [57] is a low training complexity RNN framework for computation where the inputs are fed into a fixed and non-linear system, known as a reservoir, and then mapped into outputs from the reservoir neurons. Liquid State Machines (LSMs) are examples of RCs where the neurons are randomly connected receiving time-varying inputs. Echostate networks (ESNs) are also a type of RC that uses a sparsely connected hidden layer (reservoir) with typically 1% connectivity. The connectivity and weights of hidden neurons are fixed and randomly assigned.

Another significant advancement in deep learning architecture, known as transformers, holds immense promise in the development of intelligent systems, particularly in communication environments. The transformer is a sequence-to-sequence neural network model comprising both an encoder and a decoder module, each with an identical architecture [58]. To streamline the input and output sequences, embedding and positional encoding layers are employed. Both the encoder and decoder primarily consist of a self-attention sub-layer and a position-wise sub-layer, with an additional masked attention sub-layer in the decoder. Each sub-layer is complemented by a residual connection and normalization module, facilitating the capture of long-range dependencies within the input data through self-attention.

2) Unsupervised Learning (UL): In UL, a raw unlabeled dataset is provided to discover existing patterns and features [59] using some statistical learning approach. This is very useful when the data is not labeled. The algorithms find the underlying structure of the data and predict the outputs by adapting the model. Here the classes are not explicitly stated, so the classes need to be generated based on the distribution of input features in multi-dimensional spaces. It can be even used for generating labeled data to transform the original problem into an SL problem, which is usually easier to solve. Furthermore, clustering is another important UL problem where the model outputs different clusters based on the inherent pattern of data distribution. Dimensionality reduction can be also classified as a UL problem as it reduces the state space of the feature vectors in a general ML setup.

ML Approaches: There are a number of unsupervised learning algorithms in the literature. Principal Component Analysis (PCA) [60] is primarily used for dimensionality reduction of a high dimensional dataset. It reduces the number of correlated features converting them into a set of uncorrelated features, which are also termed principal components, using orthogonal transformation of basis vectors. Reducing the dimensions of inputs also reduces the number of features to be learned, which later can be leveraged in SL techniques. It is sometimes not considered an UL technique, but rather a preprocessing technique for data analysis with reduced dimensions. In Probabilistic Graph Models (PGMs), the probabilistic relationship between random variables is modeled through a graph [61].

K-means Clustering [62] divides all the data points into K clusters in which each data point belongs to the cluster having the nearest mean. The mean of the data points in a particular cluster defines the center of the cluster. Another variant of K-means Clustering is called K-medoids Clustering where the centralmost data point of a cluster is defined as the center of the cluster [63]. Various mixture models, such as the finite mixture model, Gaussian Mixture Model (GMM) [64], etc. are also used for clustering. Hierarchical clustering can cluster data into a hierarchy of groups without predefining the number of clusters. It also comes with increasing computational costs compared to other clustering approaches. k-Nearest Neighbours (KNN) [65] algorithm determines the k-nearest neighbors for all the data points of an unknown feature vector whose class is to be identified.

![](images/2946ea2bb593be01eb693f88678846c84d499983f7fcb3cee3fcbdbf227e8ac9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph Input Layer
        A1["•"] --> B1["•"]
        A2["•"] --> B2["•"]
        A3["•"] --> B3["•"]
        A4["•"] --> B4["•"]
        A5["•"] --> B5["•"]
        A6["•"] --> B6["•"]
    end
    subgraph Hidden Layer
        C1["•"] --> D1["•"]
        C2["•"] --> D2["•"]
        C3["•"] --> D3["•"]
        C4["•"] --> D4["•"]
        C5["•"] --> D5["•"]
        C6["•"] --> D6["•"]
    end
    subgraph Hidden Layer
        E1["•"] --> F1["•"]
        E2["•"] --> F2["•"]
        E3["•"] --> F3["•"]
        E4["•"] --> F4["•"]
        E5["•"] --> F5["•"]
        E6["•"] --> F6["•"]
    end
    subgraph Hidden Layer
        G1["•"] --> H1["•"]
        G2["•"] --> H2["•"]
        G3["•"] --> H3["•"]
        G4["•"] --> H4["•"]
        G5["•"] --> H5["•"]
        G6["•"] --> H6["•"]
    end
    subgraph Hidden Layer
        I1["•"] --> J1["•"]
        I2["•"] --> J2["•"]
        I3["•"] --> J3["•"]
        I4["•"] --> J4["•"]
        I5["•"] --> J5["•"]
        I6["•"] --> J6["•"]
    end
    subgraph Hidden Layer
        K1["•"] --> L1["•"]
        K2["•"] --> L2["•"]
        K3["•"] --> L3["•"]
        K4["•"] --> L4["•"]
        K5["•"] --> L5["•"]
        K6["•"] --> L6["•"]
    end
    subgraph Hidden Layer
        M1["•"] --> N1["•"]
        M2["•"] --> N2["•"]
        M3["•"] --> N3["•"]
        M4["•"] --> N4["•"]
        M5["•"] --> N5["•"]
        M6["•"] --> N6["•"]
    end
    subgraph Hidden Layer
        O1["•"] --> P1["•"]
        O2["•"] --> P2["•"]
        O3["•"] --> P3["•"]
        O4["•"] --> P4["•"]
        O5["•"] --> P5["•"]
        O6["•"] --> P6["•"]
    end
    subgraph Hidden Layer
        Q1["•"] --> R1["•"]
        Q2["•"] --> R2["•"]
        Q3["•"] --> R3["•"]
        Q4["•"] --> R4["•"]
        Q5["•"] --> R5["•"]
        Q6["•"] --> R6["•"]
    end
    subgraph Hidden Layer
        S1["•"] --> T1["•"]
        S2["•"] --> T2["•"]
        S3["•"] --> T3["•"]
        S4["•"] --> T4["•"]
        S5["•"] --> T5["•"]
        S6["•"] --> T6["•"]
    end
```
</details>

Fig. 10. Autoencoder.

![](images/9343b84005e8bf4cf87ef6b6947fb82f9fcc50da113b1f4cf3148b97c629bf3d.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Environment"] -->|Action| B["Agent"]
    B -->|Current State| A
    A -->|New State| A
    B -->|Current Reward| B
    A -->|New Reward| A
```
</details>

Fig. 11. MDP model.

DL Approaches: Generally speaking, autoencoders [66] are used to help reduce the noise in data. In an autoencoder, first, we encode a high dimensional input, then decode it to reconstruct the input at the output again (Figure 10). The intermediate hidden layer neurons represent a compressed representation of the inputs getting rid of irrelevant and noisy components. Some other variations of this architecture are variational [67], noisy [68], and sparse [69] autoencoders. In variational autoencoders, the compact representation of data is used to generate new data points sampling from the latent space. In sparse autoencoders, the loss function is also expanded by adding another term called sparsity penalty regularization term for encouraging sparsity in the learned representations. In denoising autoencoders, robust representations are learned from the noisy input data.

Deep Belief Networks (DBNs) [70] is a probabilistic generative graph model composed of hierarchical layers representing feature vectors. Here the top layers create undirected symmetric connections among them forming an associative memory. Greedy layer-wise training can be used for DBNs [71]. Two symmetric DBNs can be extended to the structure of deep autoencoders for efficiently decoding the feature vectors [72]. To use the feature extraction capability CNNs for UL, a combination of CNN and DBN is used in [73]. Hopfield NN [74] is a cyclic recurrent NN architecture where all the nodes are connected to each other. This provides an abstraction of circular shift register memory to form a global energy function and finding clusters without a supervisor. The Boltzmann Machine is another type of recurrent NN that has a stochastic symmetric recurrent architecture [75]. As the convergence rate is generally slow for these NNs, a variant of this, Restricted Boltzmann Machine (RBM) is designed to learn the probability distribution over input data but in a layered manner [76].

In UL, competitive learning approaches, such as Self-Organizing Maps (SOMs) [77], each neuron competes to represent an input subset. Here a single neuron from a group of output neurons is activated while the other neurons adjust their individual values in regard to input data distribution. Generative Adversarial Networks (GAN) [78] consist of any two networks, with one generating data (generative network) and the other judging the generated data (discriminating network). The prediction accuracy of the discriminating network is then used to evaluate the error for the generating network. This creates a form of competition between the discriminator and the generator to get better in their corresponding tasks. We can also use ensemble learning methods [79] comprising multiple learning methods for better performances.

Generative Diffusion Models (GDMs), as introduced in [80], represents a recent breakthrough in UL leveraging DL techniques, drawing inspiration from the principles of thermodynamic diffusion. GDMs have gained widespread recognition due to their remarkable ability to generate highquality data and simple implementation procedures. In contrast to GANs, GDMs employ a denoising network that iteratively converges to an estimate of the real sample. This model works in two distinct phases: the forward and reverse diffusion processes [81]. In the forward diffusion phase, Gaussian noise is gradually introduced through a series of steps to create the target input for the denoising network. Subsequently, the denoising network is trained to reverse the noise effect for generating the original content.

3) Reinforcement Learning (RL): In RL, an agent learns to behave in a particular environment by performing thousands of actions and getting rewards or penalties based on those actions [82]. This behavior (formally known as policy) is defined by the set of actions the agent learns from its experiences. The environment is defined by some mathematical models, the most common one is the Markov Decision Process (MDP) [83]. Here the feedback is neither provided using explicit labels like in SL nor the model is learned like in UL, but the behavior of an agent is learned through the rewards or penalties based on the set of actions taken by going from one state to another with a transition probability. The goal is to find out the optimum policy so that the total reward can be maximized (or the total penalty can be minimized) over a horizon of future time intervals given the current state of the agent. In Figure 11, we show a generic structure of an RL framework as an MDP model.

ML Approaches: Depending on whether an RL model is explicitly created or not, RL can be fundamentally divided into two major categories: model-based and model-free RL methods [84]. In the model-based methods, the transition probabilities between different states are assumed to be known, whereas, in model-free methods, these probabilities are learned through iterations. Dynamic Programming (DP) [85] is the most popular model-based method used in practice. However, model-free methods like the Monte Carlo (MC) method [86] are most commonly used due to their flexibility and practicality in real systems. Q-learning [87] is one of the most popular model-free methods where “Q” refers to the expected rewards for an action taken in a given state over the time horizon, known as the value function. Another important counterpart of Q-learning is the State-Action-Reward-State-Action (SARSA) learning method where the agent learns the optimal policy in an online fashion [88]. This Q-learning is extended to the context of stochastic games [89] involving multiple agents in [90], which is also known as the Multi-Agent Reinforcement Learning (MARL) method. Another approach for modelfree RL is to learn the policy directly instead of learning the value functions, which is known as the Policy Gradient (PG) method [91]. If the policy gradient is estimated in a deterministic fashion, it is called the Deterministic Policy Gradient (DPG) method [92]. To have the benefits of both approaches, the Actor-Critic (AC) method is proposed in [93] where the critic estimates the value function and the actor updates the policy gradient in the direction suggested by the critic.

DL Approaches: General RL approaches without NNs can work well for small-scale experiments. However, when the action or state space is really large, the computation complexity exponentially increases. This phenomenon is quite common in practical systems like communication networks. To estimate the value functions or policies with RL frameworks with large state or action spaces, DL approaches can be very useful. This learning approach is also known as Deep Reinforcement Learning (DRL). The most popular and simplest DRL approach is the Deep Q-Network (DQN) [94] method. In this approach, instead of an iterative approach for updating Q values in the Q-table, an NN is used to estimate the Q function value approximately. To prevent a large overestimation of action values, another DL framework is introduced on top of DQN for a fair evaluation of policies in Double Deep-Q-Network (DDQN) [95], [96]. In Dueling Deep-Q-Network [97] method, both state and action values are separately estimated. As the expected value function may be overestimated as the expected value does not capture the complete probability distribution of random variables, Distributional Deep-Q-Network [98] is considered to update the Q function value based on its distribution. In the case of continuous action spaces, DL aided DPG method, known as Deep Deterministic Policy Gradient (DDPG) Q-Learning [99] provides better results. To deal with partial observable environments, Deep Recurrent Q-Networks (DRQN) [100] by introducing an LSTM layer in the FCNN architecture of DQN. Similarly, as for RL, MARL approaches can be efficiently solved using DRL architecture for each agent, namely known as a Multi-Agent Deep Reinforcement Learning (MADRL) framework.

# E. Distributed Learning Paradigms

The learning paradigms discussed in Section III-D, can be executed in various distributed approaches which will be discussed in this section. Unlike other fields, future 6G communications systems including satellite-based NTNs may need to incorporate a huge amount of network data from different network operators which ask for distributed approaches more. However, there are some inherent challenges in terms of privacy and efficiency with distributed approaches as the network needs to deal with gathering data from different parties. Three major distributed learning paradigms: Federated Learning (FL), Decentralized Learning (DcL), and Split Learning (SpL) are discussed below:

1) Federated Learning (FL): FL is a distributed learning technique in which multiple network data owners collaboratively build and train a global DL model, all while ensuring data isolation and privacy, as outlined in [101]. In the FL paradigm, individual data owners are initially provided with a base model by a centralized server, which they then train using their own respective data. Subsequently, these locally trained models are shared back with the central server, allowing it to update and maintain a global model. This iterative process continues until the global model reaches convergence. Consequently, FL enables the development of a globally trained model through distributed efforts, all the while safeguarding the privacy of the data owners.

2) Decentralized Learning (DcL): DcL involves computing nodes conducting local training on their individual DL/ML models and then sharing these models with neighboring computing nodes at each iteration. Global convergence is achieved when all the local models have converged. Notably, this approach ensures that no actual data is exchanged between the computing nodes, but the local models are shared among neighboring nodes. One notable advantage of DcL is the absence of the need for a centralized server, which is a requirement in FL. An illustrative example of DcL can be found in the context of MARL, where agents collaboratively train their models in a distributed manner, as elaborated in [102].

3) Split Learning (SpL): In SpL, instead of sharing model parameters, training occurs across various computing nodes, as described in [103]. Each computing node has the responsibility for training multiple layers of NNs within a DL model. Gradients for backpropagation are exchanged among these nodes to enhance training efficiency. Consequently, it can yield superior privacy performance when compared to FL, as indicated in [104]. Recent endeavors have been made to combine these two approaches, aiming to harness the advantages of both methodologies, as explored in [105].

# F. Synergy Between AI and NTN

Like many other fields, NTN is expected to be a major advancement in the realm of AI applications [106]. More precise and pragmatic analytical models with reduced overhead consumption, and efficient algorithms with a lower computational complexity are the primary catalysts for the deployment of AI-enabled NTN in next-generation wireless networks. In the preceding sections, we give a concise overview of NTN and AI to introduce these two crucial aspects of this article. Now, we motivate our readers by outlining the primary motivating forces behind combining AI and NTN for future wireless networks.

1) Complex Task Automation: In NTNs, the complexity of tasks and procedures involved in communication networks is significantly heightened. These tasks encompass a wide range of operations, including resource allocation, channel estimation, modulation, coding, and the intricacies of satellite management control. Attempting to perform these tasks manually is not only challenging but often unfeasible. The complexity involved in optimizing network performance for satellites, in particular, renders manual operations insufficient. Moreover, these tasks require meticulous precision to ensure uninterrupted service and mitigate potential hazards. However, the advent of ML and DL approaches has By harnessing ML and DL, not only can accurate actions be executed, but complex chains of procedures can also be automated seamlessly without the need for human intervention following the general ML framework as discussed in Section III-A.

2) Tractable Solutions: The deployment of next-generation NTNs is more complex than any other previous-generation cellular network due to its multifaceted architecture. For instance, the integration of satellite networks introduces a significant number of additional parameters to consider for optimum network performance [107]. However, this can result in computationally intractable solutions for practical networks, even if the solutions are computationally tractable, they may be very inefficient. Resource management in TNTN networks is a prime example of this, as resource optimization in TNTN networks often turns into non-convex optimization problems, where only suboptimal or heuristic solutions can be obtained using numerical techniques [108], [109]. Fortunately, DL techniques can approximate complicated functions involving a large number of input variables with the help of NNs, as discussed in Section III-C. As a result, complicated network functionalities can be characterized with NNs and resource management issues can be solved in a tractable manner [110], [111].

3) Data-Driven Decision Making: Although probabilistic and deterministic models can be used to model NTN functionalities, these models are often derived using very strong assumptions to get the general closed-form expressions, resulting in significant deviations in performances in simulations compared to real networks. In contrast, ML models are obtained based on real data, which means different scenarios are taken into account during training, without the need for making any assumptions. For instance, resource scheduling for users or network slices in a cellular network is typically decided based on the channel condition of the corresponding users or user groups. However, the channel is highly timevariant, so the decision feedback needs to be in real-time to incorporate optimal scheduling decisions for all the users in the network. For NTNs, the scenario is worse due to the extremely time-variant nature due to the high mobility of NGSO satellites and dynamic propagation environments. Various AI models, on

the other hand, have shown great promise in dealing with this kind of challenging problem due to their potential to capture real scenarios with more precision than theoretical models with a reasonable amount of computation complexity.

4) Adaptability and Learning: AI algorithms can adapt to changing network conditions and learn from experience. Through ML techniques, AI can continually improve its performance, optimize network operations, and adapt to evolving user demands. By leveraging AI techniques such as RL and predictive modeling, NTNs can adaptively allocate resources, optimize network parameters, and proactively detect and mitigate faults through online learning as discussed in Section III-B. AI enables NTNs to dynamically respond to changing network conditions, enhance operational efficiency, and ensure uninterrupted service delivery. The ability to learn from data and make intelligent decisions without human intervention empowers NTNs to continually improve their performance, optimize resource utilization, and deliver reliable connectivity in complex and evolving environments.

5) Reduced Computation Complexity: Obtaining optimal algorithms for various challenges in NTNs can be a daunting task. Even if such algorithms are derived for complex systems, their computational complexity often renders them impractical for real-world implementation. This complexity arises from the vast number of variables that govern different network procedures in NTNs. However, data-driven AI techniques offer a promising solution by reducing the dimensions of high-dimensional data through feature learning. Particularly, DL approaches have demonstrated remarkable effectiveness in extracting implicit features from complex systems. As a result, these techniques prove highly valuable in addressing the diverse challenges encountered in NTN environments.

6) Reduced Transmission Overhead: In some cases, traditional methods heavily rely on the exchange of information between various network participants, such as satellites and users. This might lead to a large overhead in communication channels, resulting in a decrease in the overall throughput of the network. AI can be used to reduce the control overhead of NTNs significantly. For example, to calculate the Doppler shift, the UEs must be provided with the latest ephemeris information of the satellites [112]. However, this would cause an immense overhead and a decline in the achievable data rate for the UEs. Alternative DL techniques can be employed to estimate the Doppler shift without requiring any ephemeris information from the satellites [113]. This leads to a significant decrease in transmission overhead over communication channels, resulting in superior network throughput.

7) Real-Time Implementation: Network optimization and management decisions in NTNs usually require real-time implementation, usually in the order of milliseconds to tens of milliseconds. Consequently, complex algorithms cannot be used to obtain these real-time decisions. In most cases, the algorithms become either heuristic or offline. To have an online adaptable approach, AI techniques can be considered as a suitable option. For example, an online DRL-based approach as discussed in Section III-B can be used to obtain resource management decisions in real-time and ensure proper utilization of available resources in NTNs [114]. This is particularly valuable in latency-sensitive decision-making, such as scheduling, handover decisions, etc.

8) Leveraging CSI: In communication networks, CSI is fed back to the BS from the UE to assist in selecting different schemes - such as modulation, channel coding, etc. - for improved network performance. Leveraging this data, which contains the general state of the channel, different ML approaches can be benefited. For example, RL approaches can use this data to train models. This implies that we do not need to modify the information segments sent from the UE to the BS for deploying these RL schemes, but rather can rely on feedback already existing in the communication networks. This again illustrates the capability of AI to integrate into traditional communication networks without any additional overhead costs. For NTNs, this is more important as the spectrum is more scarce and expensive; utilizing traditional CSI feedback for learning becomes another motivating factor for AI approaches to NTNs.

Key Takeaways: The data-driven ML and DL approaches are the major AI technologies for empowering satellite-based NTNs for the next-generation 6G networks. Due to their inherent capability of capturing practical scenarios with realtime tractable solutions, different learning paradigms, such as SL, UL, and RL can be extremely beneficial in addressing various challenges associated with future NTN-empowered 6G networks. Consequently, there have been a lot of research activities to deal with these challenges in the literature. In the following section, we explore various current research thrusts for incorporating AI into NTN in greater detail to get insight into potential research scopes.

# IV. RELATED WORKS

The possibility of potential integration of NTNs into 5G-Advanced [14] and future 6G networks to support various future high-demanding use cases has attracted significant attention from the research community in recent times. This emerging area of research has spurred numerous investigations to address the unique challenges and opportunities posed by NTN integration. Reference [120] discusses the potential integration aspects for satellites, which is an integral part of NTNs, into future communication networks. Reference [19] presents a summary of 3GPP efforts towards supporting NTNs in the 5G-Advanced networks. Reference [119] presents the real system prototypes along with the general overview discussion on NTNs. Reference [115] presents the challenges from the aspects of different communication layers to provide better insights for addressing these issues. In [13], [14], a concise discussion on various NTN components, use cases, technological enablers, and challenges for realizing NTN in 6G is presented. In [133], a detailed survey on the evolution of satellite networks towards the convergence with terrestrial networks from 3G to 6G along with the proposed architectures, use cases, and challenges is presented. In [118], future architectural options, use cases along the challenges associated with NTN-integrated 6G networks are explored. In [134], the necessary architectural evolution for integrating NTNs into 6G networks along with the challenges is discussed. [135] specifically focuses on the integrated Space-Air-Ground Integrated Network (SAGIN) in 6G while discussing the above topics in the context of NTNs. Another short magazine paper, [117] on NTN architectures, motivational use cases in 6G, necessary 5G NR modifications and future research directions is also in the literature. In [116], a detailed discussion on architectural options for integrating NTN into future 6G and the challenges associated with it is presented.

Likewise, AI has been acting as a driving force for various applications in wireless environments, especially in the last couple of decades; many surveys have been published on these topics recently [136], [137], [138], [139]. To facilitate the potential of AI in the 5G-Advanced and 6G environments several research articles and surveys are in the literature [18], [140], [141], [142]. In [121], [123], [126], some short surveys on the role of AI enabling 6G networks focusing on the vision, research opportunities, and challenges are presented. Reference [122] discusses the explainability of AI to address various 6G challenges. In [124], [125], comprehensive surveys on vision, enabling technologies, and applications for AI on 6G are presented. Some relevant surveys are also published focusing on different aspects of AI-enabled 6G like pervasive network intelligence [143], green communications [144], privacy [145], [146], network access and routing [147]. As NTNs are expected to be integrated into the existing terrestrial environment for the development of 6G networks, it is clear that AI is expected to play a crucial role in this process. To unleash the full potential of AI to enable NTN in 6G, we need to have a clear understanding of the potential issues of NTN, we can gain insight into what AI tools can be useful down the road to resolve those issues.

There have been a few research articles capturing the key aspects of AI as an enabling technology for NTN in 6G in the recent past. In [115], [119], a short discussion on important applications of AI/ML in satellite-based NTN communication for 6G is provided along with the general discussion on NTN. In [107], several potential AI approaches for sustainable integrated Terrestrial and Non-Terrestrial Networks (TNTN) with a focus on maritime networking are discussed in a concise manner. In [127], a brief discussion of ML approaches to tackle different potential problems associated with integrated TNTNs is presented. In [106], it provides a short discussion on ML approaches for a limited number of issues related to next-generation mega-satellite networks. In [130], a compact discussion on different ML and DL techniques at various layers of the Open Systems Interconnection (OSI) model for NTN integration into existing 5G infrastructures is presented. Even though the above-mentioned works attempt to capture the role of AI in future 6G networks for enabling integrated TNTN environments, they are generally brief and do not provide a comprehensive overview of works in this particular domain. In [128], the potential role of AI techniques in the provision of NTN-based Intelligent Internet of Things (IoT) services is discussed; they do not focus on cellular environments for future integrated TNTN 6G networks. In [129], reviews of potential AI approaches for both broadcasting and communication satellites are provided. However, they do not focus on the issues related to NTN-integrated 6G networks, rather only focus on general satellite communication. In [131], a comprehensive review of the control approaches like coverage, spectrum, interference, and mobility management required by NTN platforms that are solved using RL formulations is presented, but they do not focus on other AI approaches related to prediction and estimation. A very recent comprehensive survey paper on ML and DL applications on satellite communications is published [132]. However, they do not discuss the current research efforts from the integrated 6G perspective and the potential challenges of applying ML and DL techniques in this domain.

Most existing articles either concentrate on analyzing the architecture and challenges within Non-Terrestrial Networks (NTNs) or take a broader perspective on AI applications in wireless communications. While a few research articles touch upon potential research directions for AI-driven NTNs, these discussions are often not exhaustive or do not fully grasp the role of AI in 6G networks integrated with NTNs. Additionally, the current state of research and the practical complexities tied to AI-empowered NTN-integrated 6G networks remain largely unexplored. This survey article attempts to offer a comprehensive overview of various AI techniques employed to address the distinct challenges encountered in NTN technology. The list of related articles along with the key features is provided in Table III.

# V. AI-NTN: CURRENT RESEARCH THRUSTS

AI is considered to be one of the major driving forces for empowering next-generation NTNs. To unleash the great potential of AI in this field, exploring potential research thrusts of AI-NTN integration is extremely important. The scarce network resources, high mobility, and complex and time-varying hierarchical network topology give rise to different unique challenges in realizing NTNs for future wireless networks. Conventional optimization and estimation approaches are not always feasible for practical deployment in real networks. Various data-driven AI techniques are being explored by researchers due to their inherent capability of learning the surrounding environment and providing superior performances in practical scenarios. In this section, we discuss the current research thrusts for AI applications into NTNs.

# A. Taxonomy of Research Thrusts

We categorize current research areas according to the distinct challenges encountered across various communication layers, facilitating a clearer understanding of the current AI-NTN research landscape. NTN, owing to its dynamic propagation environment and the high mobility of NGSO satellites, presents inherent challenges that span all the layers of communication systems. As the lower layers, namely, the physical and data link layers are highly affected by the new impairments, we discuss various challenges associated with these layers in the next two separate subsections. Following this, we group traditional network and higher-layer challenges in a subsequent subsection. Within each subsection, we provide insights into the problem description, existing conventional methods, and the application of AI-based approaches to tackle these issues. While discussing AI methods, we cover SL, UL, and RL approaches, encompassing perspectives from both ML and DL for each research focus within their respective subsections. For a visual representation of this classification scheme, please refer to Figure 12.

# B. Physical Layer Aspects

1) Channel Estimation: Channel estimation is an important aspect of NTNs, serving a dual role in encompassing comprehensive network planning and managing interference, similar to other wireless networks. This entails the technique of estimating the impacts of the channel through which a transmitted signal traverses in a wireless environment. Conventionally, the channel effect is encapsulated in an information block termed CSI in modern communication systems. While conventional methods like MMSE or Least Squares are employed for CSI estimation, they often entail high computational costs and may not always align with the demands of real networks. Furthermore, obtaining timely CSI information gets more challenging due to extended propagation delays and fastchanging propagation environments in NTN conditions.

Therefore, ML-based methods are increasingly being adopted by the research community and vendors, as a promising alternative for channel prediction. This channel estimation can potentially be turned into an SL problem by considering channel features such as distance, time delay, received power, azimuth Angle of Arrival (AoA) and Departure (AoD), elevation angle, Root Mean Square (RMS) Delay Spread, and frequency as inputs and CSI as output labels. In [148], the reciprocity property of the downlink and uplink channels in Time Division Duplexing (TDD) systems is considered. So the downlink channel is estimated from uplink CSI using an LSTM-based DL model. In [149], CSI is estimated from historical CSI data using a CNN-LSTM model. However, as channel estimation is a near-real-time process, low-complexity NNs such as ESNs need to be explored for realistic implementations. In [150], a denoising CNN is used to reduce the LS channel estimation error. In [151], a CSI prediction scheme is presented without utilizing any ephemeris information, rather only using past CSI feedback information leveraging GRUs with low prediction error. In [152], an auto-regressive integrated moving average of past CSIs is utilized to predict future CSIs where the order of the past ones is determined by an LSTM network. In [153], graph attention networks are used for cascaded channel estimation for Reflective Intelligent Surface (RIS) assisted satellite networks in IoT communications. In [154], future CSI information is predicted using k-Nearest Neighbour and MLP-based algorithms from past CSI and some correlated network metrics such as latency, terminal velocity, weather, and environment state, etc. which is later used to adapt the modulation and coding scheme for next timestamp. In [155], an RNN-based CSI compression technique is presented especially focusing on future SAGIN networks. An ANN is trained to estimate the fading at 40 GHz band exploiting the knowledge of its previous channel states in [156]. In [157], an LSTM-based CSI prediction framework is discussed to provide in future NTN-integrated 6G networks.

TABLE IIIRELATED PAPERS ON AI APPROACHES FOR SATELLITE-BASED NTNS IN 6G

<table><tr><td rowspan="2">Ref.</td><td rowspan="2">Pub. year</td><td colspan="2">Background</td><td colspan="4">Discussion on AI-Enabled NTN in 6G</td></tr><tr><td>NTN challenges</td><td>AI relevance</td><td>Research thrusts</td><td>6G perspective</td><td>Current efforts</td><td>Practical challenges</td></tr><tr><td>[115]</td><td>2021</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>[19]</td><td>2021</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>[116]</td><td>2021</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>[117]</td><td>2022</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>[118]</td><td>2022</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>[119]</td><td>2022</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>[120]</td><td>2023</td><td>√</td><td></td><td></td><td>√</td><td></td><td></td></tr><tr><td>[121]</td><td>2020</td><td></td><td>√</td><td></td><td>√</td><td></td><td></td></tr><tr><td>[122]</td><td>2020</td><td></td><td>√</td><td></td><td>√</td><td></td><td></td></tr><tr><td>[123]</td><td>2020</td><td></td><td>√</td><td></td><td>√</td><td></td><td></td></tr><tr><td>[124]</td><td>2021</td><td></td><td>√</td><td></td><td>√</td><td></td><td></td></tr><tr><td>[125]</td><td>2022</td><td></td><td>√</td><td></td><td>√</td><td></td><td></td></tr><tr><td>[126]</td><td>2023</td><td></td><td>√</td><td></td><td>√</td><td></td><td></td></tr><tr><td>[127]</td><td>2019</td><td>√</td><td>√</td><td>Short</td><td>√</td><td></td><td></td></tr><tr><td>[106]</td><td>2019</td><td>√</td><td>√</td><td>Short</td><td>√</td><td></td><td>Short</td></tr><tr><td>[128]</td><td>2020</td><td>√</td><td>√</td><td>Comprehensive, but only covers IoT applications</td><td>√</td><td></td><td>Short and only covers IoT applications</td></tr><tr><td>[119]</td><td>2021</td><td>√</td><td>√</td><td>Short</td><td>√</td><td>Complete</td><td></td></tr><tr><td>[115]</td><td>2021</td><td>√</td><td>√</td><td>Short uncategorized</td><td></td><td>Does not cover AI for NTN</td><td></td></tr><tr><td>[129]</td><td>2021</td><td>√</td><td>√</td><td>Comprehensive, but does not cover the 6G perspective</td><td></td><td></td><td></td></tr><tr><td>[107]</td><td>2022</td><td>√</td><td>√</td><td>Short</td><td>√</td><td></td><td>Short</td></tr><tr><td>[130]</td><td>2023</td><td>√</td><td>√</td><td>Short</td><td></td><td></td><td></td></tr><tr><td>[131]</td><td>2023</td><td>√</td><td>√</td><td>Comprehensive, but only covers RL</td><td>√</td><td>Only covers RL</td><td></td></tr><tr><td>[132]</td><td>2023</td><td>√</td><td>√</td><td>Comprehensive, but does not cover the 6G perspective</td><td></td><td></td><td></td></tr></table>

2) Doppler Shift Estimation: As the LEO satellites move around the Earth typically at a very high speed, both the satellite and ground user transceivers experience a large Doppler effect due to their relative velocity. If the transmitter moves towards (or away from) the receiver, the emitted signal from the transmitter may take less (or more) time to reach the receiver depending on the direction of the movement, hence the frequency of the signal increases (or decreases). This shift in signal frequency due to the motion of the transmitter, the receiver, or both refers to the Doppler shift. If the original frequency is $f _ { 0 } ,$ the Doppler shift due to the motion of transceivers towards some specific direction with some specific relative velocity can be given by:

$$
\delta f = f _ {0} \times \frac {v}{c} \times c o s (\theta)
$$

Here

v = The relative velocity of the transceiver

θ = The angle between the direction of the transceiver and the direction of the propagating signal

For LEO satellites, due to high mobility, This frequency offset is pretty significant (48 kHz with a center frequency of 2GHz [20]). Due to these frequency offsets, UEs tune to some different carrier frequencies from their originally assigned carrier frequencies. This may lead to ICI between multiple UEs as discussed in Section II-E.

![](images/745b59fd96b65c77710931735ca601c69ae4be1339727311b93914f80c57b3fa.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Physical"] --> B["Data Link"]
    B --> C["Channel Estimation"]
    B --> D["Doppler Shift Estimation"]
    B --> E["Authentication"]
    B --> F["Intrusion Detection"]
    B --> G["Anti jamming"]
    B --> H["Spectrum Sharing"]
    B --> I["Resource Allocation"]
    B --> J["Network"]
    B --> K["Handover Optimization"]
    B --> L["Multiple Access"]
    B --> M["Computational Offloading"]
    B --> N["Net..."]
    B --> O["Traffic Prediction"]
    style A fill:#f9f,stroke:#333
    style B fill:#ff9,stroke:#333
```
</details>

Fig. 12. Taxonomy of research thrusts.

There have been significant efforts to characterize the Doppler effect for LEO satellites since the launching of communication satellites. In [161], an equation for Doppler shift is derived for the simple case of LEO satellites with circular orbits in the equatorial plane and ground observing points on the equator. In [162], the Doppler shift is analytically derived assuming the trajectory of the satellite with respect to the earth by a great circle arc and the speed of the satellite as constant. In [112], the Doppler shift is characterized by considering a new orbit generator using different orbital parameters through a rigorous analysis. UEs with Global Navigation Satellite System (GNSS) can get the global positioning of satellites and estimate the amount of Doppler shift needed to be addressed for the next transmission slot [163]. However, this increases the cost and complexity which may not be feasible for ground UEs [31]. Additionally, The GNSS signals are weak, not ubiquitous, and susceptible to interference and spoofing. Recently, there have been also efforts to estimate the Doppler shift in LEO satellite systems using various other approaches, such as stochastic geometry [164], Maximum A Posteriori (MAP) [165], algebraic solutions [166], two-stage estimators consisting of time-varying Burg spectral analyzer and alphabeta filter [167] etc. In [168], the Doppler shift is estimated using reference signals in more than one frequency position in Orthogonal Frequency Division Multiplexing (OFDM) carrier in a 5G integrated NTN system.

These different theoretical approaches can estimate the Doppler shift with a certain accuracy in different scenarios. However, the methods are generally very cumbersome due to the complexity associated with the orbital mechanics of the satellites. Most of these methods come with simplifying assumptions to keep the approach feasible for practical systems, thereby affecting accuracy. Moreover, due to the constant high-speed movement of LEO satellites, the wireless environment associated with it becomes time-variant. The computation complexity increases more to model these temporal variations using traditional estimation approaches. Additionally, the UEs may need the ephemeris information of the satellites to compute the Doppler shift associated with its motion, which creates large additional overheads in the communication channels. To characterize this Doppler effect, ML-based algorithms seem to appear as potential practical alternatives to the research community.

In wireless communication systems, due to the mobility of the transceivers, the channel between the transceivers changes significantly resulting in received signal power variation and Doppler shift. So, intuitively, the CSI of this channel should contain information about the Doppler shift. This idea has been already explored in terrestrial networks to generate a model using ML [113], [158], [159]. The ground truth values or the labels are usually generated using the ephemeris information. Different channel characteristic variables like Rician K factor, azimuth AoA width, mean azimuth AoA and channel estimation errors are generated randomly, and averaged Power Spectral Density (PSD) is used as inputs with some preprocessing to a multi-layered FCNN to estimate the Doppler shift in [158]. In [113], RSRP values mapped from an ambiguity reducer are used to generate the weights for an MLP. In [159], different time and frequency domain signals with various modulation schemes, delay profiles, and Signal to Noise Ratio (SNR) have been used as inputs to a hybrid CNN-LSTM model to estimate the Doppler shifts. In NTN, the research in this domain is still at the early stage The estimated CSI is used as input to a CNN model to estimate the Doppler shift in [160]. In the future, other potentially efficient SL models can be also explored to generate the real-time accurate Doppler shift in an online manner. In Table IV, we summarize the AI approaches for Doppler shift estimation in NTN. Even though the DL techniques are found to be useful in estimating Doppler shift using channel parameters, Doppler shift can be also estimated by analyzing the predictable trajectory of the satellites. Complexity analysis is required to justify the applicability of these DL architectures replacing the state of art methods in real systems.

3) Security - Physical Layer Authentication: Due to the new interfaces introduced by satellite-integrated terrestrial architectures, various spoofing and replay attacks can be launched using these interfaces. Spoofing attacks involve an attacker satellite impersonating a legitimate one, while replay attacks involve the retransmission of previously intercepted messages to deceive users. Generally, in terrestrial networks, these kinds of attacks are detected and mitigated by using standard cryptographic techniques, a concept also investigated in satellite communications [169], [170]. However, when it comes to NTN-integrated future 6G networks, these conventional cryptographic methods face several challenges. Firstly, these techniques are computationally intensive and, thereby challenging to implement in satellites due to their limited onboarding capabilities. Secondly, the highly dynamic and massive scale network topology of NTNs, particularly for enabling IoT devices, necessitates significant modifications in network protocol design and introduces overheads that may not be practical to manage with existing architectures Also, these cryptographic techniques often assume that attackers lack the computational resources to break the encryption. However, with ongoing advances in quantum computing research, these assumptions may no longer hold in the future, presenting yet another challenge that needs to be addressed.

TABLE IVSUMMARY OF AI APPROACHES FOR DOPPLER SHIFT ESTIMATION IN SATELLITE-BASED NTN

<table><tr><td rowspan="2">Reference</td><td rowspan="2">Input to the ML model</td><td colspan="3">Learning Approach</td><td rowspan="2">DL Tool</td><td colspan="2">Comments on Models</td></tr><tr><td>SL</td><td>UL</td><td>RL</td><td>RL Model</td><td>DL Model</td></tr><tr><td>[158]</td><td>Averaged PSD</td><td>√</td><td></td><td></td><td>√</td><td></td><td>FCNN</td></tr><tr><td>[159]</td><td>Modulation scheme, delay profiles, SNR</td><td>√</td><td></td><td></td><td>√</td><td></td><td>CNN-LSTM</td></tr><tr><td>[113]</td><td>RSRP</td><td>√</td><td></td><td></td><td>√</td><td></td><td>FCNN</td></tr><tr><td>[160]</td><td>CSI</td><td>√</td><td></td><td></td><td>√</td><td></td><td>CNN</td></tr></table>

Physical layer authentication offers a promising alternative to these conventional techniques. In [171], Wyner introduced the concept of physical layer authentication where the message was encoded in such a way that the mutual information between the legitimate channel and wiretap channel is maximized. This encoding generally captures the unique characteristics of the channel between the user and the legitimate transmitter, serving as a means to verify the transmitter’s identity. This technique has been already explored in terrestrial networks using the CSI information as radio signatures for the transmitter devices [172], [173], [174]. However, the prevalence of Line of Sight (LoS) paths in satellite networks makes radio fingerprinting using channel fading information from CSI impractical. Furthermore, due to the high mobility of NGSO satellites, as discussed in Section II-E, the high Doppler Shift is introduced in received signals, which can be used to verify the identity of the legitimate satellites. In [175], a maximum likelihood estimation and uniform quantizer are used to obtain the secret key bits from the Doppler frequency shifts, which is used in the authentication of legitimate satellites [176] In [177], an orbital information – time difference of arrival-based authentication mechanism is introduced providing low false authentication rates.

In the recent past, various DL techniques have shown lofty promises in the field of extracting features from noisy data, which is also leveraged in this field using different ML models. In [178], CNNs and Autoencoders are used to extract the necessary channel features for physical layer authentication of legitimate satellites. In [179], [180], [181], both the received signal power and Doppler shift are used for radio fingerprinting using SVMs providing improved authentication rates.

4) Security - Intrusion Detection: In modern satelliteterrestrial integrated networks, the majority of satellite communication systems rely on elementary security threat detection mechanisms. Typically, these mechanisms operate by flagging an anomaly if the received signal frequency deviates from the baseline spectrum by a predetermined threshold. However, this simplistic approach frequently leads to a significant number of false positives. On top of that many

anomalies represent unusual behavioral patterns, exhibiting temporal correlations that escape detection by these simple detectors. Consequently, these conventional methods often struggle to effectively identify and respond to sophisticated security threats.

To address these challenges, DL techniques are explored to efficiently detect security threats using various innovative approaches. In the study presented in [182], an ensemble model combining Random Forest (RF) and MLP is developed to improve the performance of security threat detection across diverse datasets for satellite communications. [183] leverages critical feature selection driven by RF to streamline complexity and enhance the relevance of features before the detection phase. These features are then forwarded to different NN architectures, including LSTM, GRU, RF, and ANN enabling robust security threat detection. These models are tested on different datasets where GRU-empowered threat detection models exhibit superior performances by capturing temporal behavioral patterns. In [184], a UL approach using LSTM networks is explored, which can not only detect unforeseen security threats but also does not need any labeled data. In another study as shown in [185], two SL and five UL approaches are considered for threat detection to show the effectiveness of ML techniques. In [186], a DDPG-based DRL framework is considered where the agents decide whether the aerial platform is malicious or not (actions) based on their behavior (states) and the system condition (rewards) for threat detection. Recognizing the computational constraints of satellites and Internet of Things (IoT) devices, federated learning approaches are also investigated as detailed in [187], [188], [189] for threat detection.

5) Security - Anti-Jamming: Satellites are vulnerable to jamming threats due to their predictable and periodic visibility in NTNs, so anti-jamming approaches are important to tackle this challenge. Conventional spread spectrum techniques are used in anti-jamming for satellite networks. However, they are not very useful in dealing with new smart jamming attacks which can adjust their actions based on the network feedback. Various RL techniques are adopted to tackle these problems in an efficient manner. In [190], [191], a hierarchical anti-jamming Stackelberg game is introduced for routing antijamming problems which is later solved by providing fast anti-jamming decisions using a DRL-based routing algorithm for satellites. in [192], a DL-based jamming detection algorithm is proposed for satellite navigation systems. In [193], an anti-jamming coalition game is formed to decrease energy consumption, and suboptimal jamming policies are obtained by RL approaches. In [194], ML-aided cognitive anti-jamming communication is designed, developed, and tested on real satellite-ground links.

![](images/0099cc622b147d2037e9eb6803e227eff82110a30924b16e81846bf0e6c1e293.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph Scenario 1
        A["Satellite"] --> B["Node 12"]
        A --> C["Node 13"]
        A --> D["Node 14"]
        A --> E["Node 15"]
        A --> F["Node 16"]
        A --> G["Node 17"]
        A --> H["Node 18"]
        I["Satellite"] --> J["Node 10"]
        K["Satellite"] --> L["Node 9"]
        M["Satellite"] --> N["Node 8"]
        O["Satellite"] --> P["Node 7"]
        Q["Satellite"] --> R["Node 6"]
        S["Satellite"] --> T["Node 5"]
        U["Satellite"] --> V["Node 4"]
        W["Satellite"] --> X["Node 3"]
        Y["Satellite"] --> Z["Node 2"]
    end

    subgraph Scenario 2
        AA["Satellite"] --> AB["Node 11"]
        AA --> AC["Satellite"]
        AA --> AD["Satellite"]
        AE["Satellite"] --> AF["Node 10"]
        AE --> AG["Satellite"]
        AE --> AH["Satellite"]
        AI["Satellite"] --> AJ["Node 9"]
        AK["Satellite"] --> AL["Satellite"]
        AK --> AM["Satellite"]
        AN["Satellite"] --> AO["Satellite"]
    end

    style Scenario 1 fill:#f9f,stroke:#333
    style Scenario 2 fill:#bbf,stroke:#333
```
</details>

Fig. 13. A simple beam hopping example in satellite-based NTN.

# C. Data Link Layer Aspects

1) Beam Hopping: Modern communication satellites form multiple beams to support a large number of users over a large area through spatial multiplexing into different NTN cells. Each satellite can effectively reuse the allocated spectrum with very low co-channel interference as well as provide strong signals at the ground user terminals with relatively low transmission power using beamforming techniques. However, due to the high cost and low availability of onboard processing computing resources in satellite systems, mostly simple fixed beam allocation policies are used in traditional satellite communication. These strategies lack the flexibility to adapt to the temporal and spatial variation of traffic demands in real satellite networks. Beam hopping is a technique for allocating beams in a flexible manner so that these changes can be addressed efficiently. It refers to a procedure for activating different beams according to the current demands of an NTN cell covered by those beams, so effectively hopping the set of active beams from one combination to another [195]. In Figure 13, a simple beam-hopping scenario is depicted, where we have different NTN cells with varying demands. We classify the cells into three different categories, e.g., high, medium, and low, based on their traffic demands. In the first scenario, the low-demand NTN cells, e.g. cell 9, have less number of active beams than high-demand NTN cells, e.g. cell 6, even lesser than moderate-demand NTN cells, e,g, cell 1, 2, 5 or cell 13. However, due to mobility or change in traffic patterns, the traffic demand in cell 13 reduces and in cell 5 increases. As a result, we can see the intensity of the beams also changes accordingly in these two cells at a later time, and a new beam-hopping pattern emerges.

The key question of beam hopping is to find out which beams need to be activated when and for how long while maximizing the network performances given the capacity constraints [202]. This can be effectively formulated as an optimization problem considering different network performance metrics such as system throughput, delay, fairness, etc. as the objective(s) along with power and spectrum constraints. In [203], a convex optimization framework with an objective to match the system capacity to traffic demand along with power allocation constraints is considered. This yields a close-form solution giving insights into resource allocation policies for maximizing network performances from different perspectives. However, from the perspective of real networks, the convex objective function is not very realistic, so the results are not applicable to real networks in a straightforward manner. Assuming the non-convexity of the problem, obtaining a globally optimal solution with efficient algorithms gets difficult. In [109], the steepest gradient descent algorithm is chosen to get the sub-optimal solution using the optimal set of precoding vectors. Some heuristic iterative approaches are also proposed in [108], [204], [205] to tackle these non-convex problems in a practical and feasible manner. Different meta-heuristic approaches like Genetic Algorithm (GA) [206], Simulated Annealing (SA) Algorithm [207], Particle Swarm Optimization (PSO) [208], and combined metaheuristic approaches like GA-SA [209] have been considered to generate suboptimal solutions with a reduced amount of computational complexity.

The main challenge in designing a beam-hopping pattern in an optimization framework lies in the large search space associated with an optimal solution. The size of the search space for finding out an optimal beam hopping pattern scales exponentially with the number of beams in the satellite networks. Modern satellites can have hundreds to thousands of beams depending on their coverage area, so the computational complexity becomes pretty high, and the computation time becomes pretty large to find out the exact solutions. The low-complexity suboptimal solutions using iterative and metaheuristic approaches achieving satisfactory performances in real networks are not very abundant. In this context, the DL approaches turn out to be a suitable alternative for this problem.

In [110], [111], an SL approach is considered by forming labeled datasets with beam hopping patterns as outputs and channel matrix, transmission power, and traffic demand as inputs. First, a mixed integer linear problem formulation for matching the offered capacity to traffic demands is reduced to a simple linear programming problem. A training dataset is generated using conventional optimization algorithms and a DL model is trained on this dataset by considering beam hopping patterns as labels. Furthermore, the optimization framework can be potentially transformed into an RL problem to capture the optimal beam-hopping pattern in a learning environment. In [196], [197] the transmission delay is minimized considering the power and beam allocation constraints using a DRL approach. The state space consists of the average transmission delay and the buffer length with beam hopping pattern as actions and the negative Hadamard product of the current states, the negative of total queuing delay as the reward function. In [198], a combined DRL-metaheuristic approach is considered to optimize both the throughput and delay fairness while at the same time designing different reward functions for the two cases. In [199], [200], a network consisting of real-time and non-real-time traffic is considered. A multi-objective problem minimizing the transmission delay for real-time traffics, maximizing the throughput for non-realtime traffics as well as overall delay fairness is considered. Individual reward functions are designed to capture each of the goals. In [201], a cooperative multi-agent framework is considered to dynamically allocate the power and bandwidth to illuminating beams optimizing throughput and delay fairness using a DDQN. In Table V, we summarize the AI approaches for beam-hopping in NTN. As traffic demand changes with time, recursive architectures such as RNN, ESN, etc. should be also explored to design the NN for DL architectures used to address beam-hopping issues. Also, distributed learning architectures can be useful to design efficient beam-hopping schemes.

TABLE VSUMMARY OF AI APPROACHES FOR BEAM-HOPPING IN SATELLITE-BASED NTN

<table><tr><td rowspan="2">Reference</td><td colspan="4">Target Optimization Objectives</td><td colspan="3">Learning Approach</td><td rowspan="2">DL Tool</td><td colspan="2">Comments on Models</td></tr><tr><td>Throughput</td><td>Tx Delay</td><td>Delay Fairness</td><td>Capacity-Demand Ratio</td><td>SL</td><td>UL</td><td>RL</td><td>RL Model</td><td>DL Model</td></tr><tr><td>[110]</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>FCNN</td></tr><tr><td>[111]</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>FCNN</td></tr><tr><td>[196]</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>DQN</td><td>FCNN</td></tr><tr><td>[197]</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>DQN</td><td>CNN</td></tr><tr><td>[198]</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>Proximal Policy Optimization</td><td>FCNN</td></tr><tr><td>[199]</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>DQN</td><td>CNN</td></tr><tr><td>[200]</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>DQN</td><td>CNN</td></tr><tr><td>[201]</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>DDQN</td><td>FCNN</td></tr></table>

2) Spectrum Sharing: In traditional communication systems, satellite, and terrestrial cellular networks generally occupy different frequency bands, so they do not interfere with each other. However, the satellites in the new integrated TNTN environment for 6G are expected to use the same S and Ka-Band as discussed in Section II-D. This improves the overall spectral efficiency of the integrated networks as well as provides a better QoE for the users. However, as both the satellite and the ground network use the same frequency band, the signals

produced by them interfere with each other, i.e. cause Co-Channel Interference (CCI) to each other. In Figure 14, a simple spectrum-sharing scenario in the downlink channel in an integrated TNTN network is shown. The satellite user is connected to a satellite and the downlink channel is indicated using the green link. There are three more terrestrial BSs using the same channel as the satellite provide CCI to the satellite user (indicated by red links).

In TNTN, the spectrum-sharing phenomenon needs more attention because we have a hierarchical network scenario consisting of non-terrestrial and terrestrial BSs as shown in Figure 3. To support this complex topology in a single framework, we need to come up with efficient spectrumsharing strategies causing low interference to the users [217]. In conventional spectrum sharing methods, we use efficient frequency reuse, leveraging directional antennas, adaptive

![](images/5444870fac5381df07616b8f062b91f22e2ab7290dde9739224fe811af303ce2.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Satellite"] -->|Desired Signal| B["Satellite UE"]
    B --> C["Interfering Signal"]
    C --> D["Terrestrial BS"]
    style A fill:#f9f,stroke:#333
    style B fill:#ccf,stroke:#333
    style C fill:#cfc,stroke:#333
    style D fill:#fcc,stroke:#333
```
</details>

Fig. 14. General spectrum sharing scenario in TNTN.

power control, etc. methods to mitigate the effect of CCI. However, traditional four-color frequency reuse can effectively reduce the level of interference at the expense of more spectrum. beamforming approach can reduce the interference greatly, but that too comes at the cost of increasing complexity.

To tackle this situation, a process called spectrum sensing is introduced in cognitive radio networks, where the unlicensed users can sense the occupancy status of the target band using some radio sensing method [218]. The popular spectrum sensing methods are Energy Detection (ED)[219], Cyclo-Stationary Detection (CSD) [220], Eigen Value-based Detection (EVD) [221] etc. However, these methods either are simple with poor performance in low SNR scenarios (ED) or provide good performance but with more computational complexity (CSD and EVD). For these reasons, ML has been adopted for spectrum sharing to capture the correlation with a reduced computational complexity which can be extended to integrated satellite-terrestrial network scenarios [217].

TABLE VI SUMMARY OF AI APPROACHES FOR SPECTRUM SHARING IN TNTN 

<table><tr><td rowspan="2">Reference</td><td colspan="3">Problem Insight</td><td colspan="3">Learning Approach</td><td rowspan="2">DL Tool</td><td colspan="2">Comments on Models</td></tr><tr><td>Spectrum Sensing</td><td>Spectrum Occupancy Prediction</td><td>Spectrum Access</td><td>SL</td><td>UL</td><td>RL</td><td>RL Model</td><td>DL Model</td></tr><tr><td>[210]</td><td></td><td>√</td><td></td><td>√</td><td></td><td></td><td>√</td><td></td><td>CNN-BiLSTM</td></tr><tr><td>[211]</td><td></td><td>√</td><td></td><td>√</td><td></td><td></td><td>√</td><td></td><td>CNN</td></tr><tr><td>[212]</td><td></td><td>√</td><td></td><td>√</td><td></td><td></td><td>√</td><td></td><td>CNN-LSTM</td></tr><tr><td>[213]</td><td>√</td><td>√</td><td></td><td>√</td><td></td><td></td><td>√</td><td></td><td>CNN-LSTM</td></tr><tr><td>[214]</td><td></td><td></td><td>√</td><td></td><td></td><td>√</td><td></td><td>Modified Q-Learning</td><td></td></tr><tr><td>[215]</td><td>√</td><td>√</td><td></td><td>√</td><td></td><td></td><td>√</td><td></td><td>SVM-CNN</td></tr><tr><td>[216]</td><td></td><td></td><td>√</td><td></td><td></td><td>√</td><td>√</td><td>MADDPG</td><td>FCNN</td></tr></table>

Different intelligent learning approaches are adopted to tackle the spectrum-sharing problem for next-generation TNTN networks [222]. In [210], a spectrum-sharing strategy is developed for LEO satellites from the GEO satellite spectrum historical occupancy data using a CNN-BiLSTM model. Here the LEO satellite users are considered as unlicensed secondary users and the GEO satellite users are considered as the licensed primary users. In [212], a CNN-LSTM-based spectrum sensing method is introduced for satellites to capture the spatial and temporal correlation effectively for spectrum occupancy of satellite systems. In [213], a CNN-LSTM model is introduced to predict the frequency assignment for satellites based on historical data. In [214], a modified Q-Learning algorithm is used in an RL setup for the adaptive selection of access and modulation schemes for NGSO satellites in an NGSO-GEO system. In [215], an SVM model is first used for low complexity spectrum sensing, then a CNNbased spectrum prediction model based on historical data is developed. In [216], a cooperative MADRL framework is considered for bandwidth management in a game-theoretic model minimizing inter-beam interference. In [211], a CNNbased spectrum reconstruction method from incomplete data is discussed for satellite networks. In Table VI, we summarize the AI approaches for spectrum sharing in TNTN. However, these spectrum sensing decisions need to be in real-time to increase the overall throughput of the secondary users; this means the conventional LSTM architectures need to be replaced by efficient low-complexity ESN architectures to tackle this in an online manner. Furthermore, spatial spectrum sharing scenarios need to be also considered along with the state of art temporal spectrum sharing scenarios leveraging the benefits of future 3D SAGIN networks.

3) Resource Allocation: Power and spectrum are the two fundamental resources for any type of wireless network, and NTN is also not an exception. The spectrum allocation is typically performed by the assignment of carriers with equal width from the allocated spectrum for that service. Hence, the number of assigned carriers and their positions are optimized to achieve good signal quality with the minimum resources. Often, the carrier assignment is achieved by the orthogonal splitting of the spectrum resources, which is also known as frequency reuse. However, the strict orthogonality of the frequency bands cannot be always achieved to achieve better spectral efficiency. In case of lack of orthogonality of spectrum resources used by different transceivers can also introduce CCI. The interfering signal can be effectively suppressed by increasing transmission power for the original signals. However, as power is also a scarce resource, we cannot increase the transmission power indefinitely and increasing transmission power will result in a decrease in energy efficiency. For better resource utilization, a more robust radio resource management needs to be designed by controlling both power and spectrum resources [231].

Generally, an optimization framework can be considered to optimize the system performance with bandwidth and power constraints. In most cases, such optimization problems are non-linear and non-convex due to objective function nonlinearity and complex constraints involving Signal to Interference and Noise Ratio (SINR) [232]. Furthermore, the carrier assignment indicator variables result in a mixed-integer programming problem [232]. Hence, no optimal solution can be determined using the known methods of convex optimization with low computation complexity. Instead, suboptimal and metaheuristic approaches are proposed, which tackle parts of the problem separately and then iteratively tune the parameters [232]. Different suboptimal approaches are adopted to optimize resource allocations [233], [234], [235], [236], [237] for satellite systems. However to reduce computation complexity several heuristic [238] and metaheuristic approaches like GA [206], PSO [208] are explored to reach the suboptimal solutions within a shorter computation time.

To tackle this resource allocation issue in real satellite networks in a practical manner, ML approaches are being started to be adopted by the research community. A DL framework is combined with conventional optimization algorithms to overcome the computation complexity issue of the conventional approach in [229], [230] by reducing the feature space. A model-free DRL framework is adopted for power allocation of high throughput satellites in [226]. A Q-learning-based long-term capacity allocation algorithm in an RL framework is introduced for a heterogeneous satellite network in [223]. In [114], an Actor-Critic and Critic Only based RL framework is considered for optimal resource allocation for LEO satellite networks. Different advanced RL frameworks like DRL [224], [225], [239], Multi-objective DRL [228] and MADRL [227] are also proposed to solve the resource allocation issue for satellites. In Table VII, we summarize the AI approaches for resource allocation in TNTN. As both power and spectrum are equally important and scarce resources for NTNs, new DL architectures need to be explored to jointly allocate these resources in an efficient manner for NTNs.

TABLE VIISUMMARY OF AI APPROACHES FOR RESOURCE ALLOCATION IN SATELLITE-BASED NTN

<table><tr><td rowspan="2">Reference</td><td colspan="2">Target Objective</td><td colspan="3">Learning Approach</td><td rowspan="2">DL Tool</td><td colspan="2">Comments on Models</td></tr><tr><td>Spectral Efficiency</td><td>Energy Efficiency</td><td>SL</td><td>UL</td><td>RL</td><td>RL Model</td><td>DL Model</td></tr><tr><td>[114]</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td><td>AC</td><td></td></tr><tr><td>[223]</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td><td>Q-learning</td><td></td></tr><tr><td>[224]</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td>DQN</td><td>FCNN</td></tr><tr><td>[225]</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>DQN</td><td>CNN</td></tr><tr><td>[226]</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>DQN</td><td>FCNN</td></tr><tr><td>[227]</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td><td>MARL</td><td></td></tr><tr><td>[228]</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td>DQN</td><td>Ensembles of FCNN</td></tr><tr><td>[229]</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>FCNN</td></tr><tr><td>[230]</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>FCNN</td></tr></table>

4) Network Slicing: Network slicing refers to the process of virtually partitioning the physical network into different network slices corresponding to different service requirements. The slices are allocated with radio resources as per the demand of the users belonging to the slices. Slicing is useful for wireless networks as each slice can share the same physical network infrastructures while receiving necessary radio resources for guaranteeing a minimum level of service to the users. Also, network slicing provides the flexibility to switch users between slices with different amounts of allocated resources responding to changes in traffic conditions. Integrated TNTN networks appear to be an excellent candidate for applying the concept of network slicing due to their diversified traffic patterns. In fact, different use cases like mMTC and eMBB applications can be extensively benefited through the network slicing in these networks. In Figure 15, a simple network slicing scenario is shown. Here the network consists of a satellite and a terrestrial BS which form 3 slices in a combined manner. Slice 1 is for high-priority users, they share network resources from the satellite and the terrestrial BS (depicted by green links). Slice 2 is for users with low latency requirements, the terrestrial BS provides resources to the users (shown by red links). Slice 3 is for the remote users who can only be served by the satellite (shown by blue links).

In a general network slicing framework, a composite utility function consisting of different network performance characteristics like average throughput and other costs like slice reconfiguration cost, resource reservation cost, etc. is formulated as an objective function that needs to be minimized. The constraints are generally the minimum service level To ensure real-time implementation, simple heuristic approaches are tested on real platforms [240], [241], [242]. requirements depending on the type of services for particular slices. In [240], an extensible 5G network slicing framework in conjunction with satellite networks is discussed to facilitate the integration of satellite services into 5G. In [243], a multi-objective optimization problem comprising latency,

![](images/b7dbf016d5d3ec6064a1b675d3a4ad3b834d698469c5bc63f83baee4caeea55b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    Satellite["Satellite"] -->|Wireless Signal| Slice1["Slice 1"]
    Satellite -->|Wireless Signal| Slice2["Slice 2"]
    Satellite -->|Wireless Signal| Slice3["Slice 3"]
    Slice1 -->|Terrestrial BS| Slice1
    Slice2 -->|Terrestrial BS| Slice2
    Slice3 -->|Terrestrial BS| Slice3
```
</details>

Fig. 15. Network slicing in satellite-terrestrial integrated networks.

computational, and power requirements in an edge-computing scenario is formulated to find suitable slice scheduling strategies based on numerical methods. However, these approaches do not guarantee optimal performance guarantee. To tackle this issue, different AI-based approaches are explored as it is done in the case of traditional 5G terrestrial networks.

In [244], RL-based network slicing frameworks for satelliteintegrated future 6G networks are discussed along with experimental results for simple networks. In [245], AI-based network slicing for space-air-ground integrated vehicular networks is discussed from the perspective of slice creation, user association, and resource scheduling. In [246], [247], satellite-terrestrial network slice resource allocation frameworks utilizing network function virtualization are presented which can be leveraged for applying advanced AI-based methods. In [248], FCNNs are used to train a suitable set of network parameters that can produce latency similar to a non-linear optimizer-based network slicer. In [249], a general Radio Access Network (RAN) slicing problem is considered where the objective function is a weighted function of bandwidth and spectrum consumption satisfying QoS and inter-slice isolation constraints. In a simple 2-slice satelliteterrestrial integrated network, different DL architectures are tested. In [250], an ML approach similar to the meta-heuristic ACO approach is considered to realize network slicing in a TNTN environment. An air-ground integrated network is considered in a DRL framework in [251], later solved by the DDPG algorithm. Here both the actor and critic networks are FCNNs consisting of four layers. Distributed learning architectures can be potentially explored in future works for real network implementations.

5) Handover Optimization: In order to maintain an orbital path around the Earth at a lower altitude, an LEO satellite needs to move at a much higher velocity (around 7.8 km/s) compared to a GEO satellite. So these satellites orbit around the Earth typically within 2 hours [20]. Due to the smaller orbital period, any LEO satellite remains visible to a ground UE for only several minutes which poses a great challenge for integrating these satellites into the traditional terrestrial networks. The UE needs to undergo multiple handovers within a short span of time interval regardless of its mobility status for seamless continuation of the data sessions [14]. This frequent handover phenomenon in LEO satellite networks creates a lot of overhead in communication channels and results in overall degradation in network performances. Moreover, due to lower altitudes, the coverage area of an LEO satellite is much smaller compared to a GEO satellite. Typically a large number of LEO satellites are needed to maintain global coverage across the Earth with complex constellations. In the case of an ultra-dense constellation of LEO satellites (like Starlink), each UE is generally covered by multiple satellites, so the UE can choose the best one from the list of suitable candidate LEO satellites. This problem can be potentially solved in an optimization framework jointly considering different handover decision criteria.

In traditional terrestrial communication networks, a UE chooses to attach to a BS based on periodic signal power and quality measurements, such as Reference Signal Received Power (RSRP), and Reference Signal Received Quality (RSRQ) for the link between the BS and the UE. Moreover, load balancing is also important to ensure no BS gets overloaded or underloaded as a result of initial attachment or handover procedures. However, for LEO satellite networks, choosing a satellite BS merely based on signal measurements and network load information is not enough due to the limited visibility time of these satellites. So the UE also needs to take the potential service time into account before attaching to a satellite. In Figure 16, a simple general handover scenario involving multiple LEO satellites and a single UE is shown. Here initially, the UE is connected to an LEO satellite, indicated as LEO 2, and it needs an immediate handover to some other neighboring satellite covering the UE, either to LEO 1 or LEO 3 as it will soon lose the coverage of LEO 2. As shown in Figure 16, LEO 2 has more network load and bad channel condition, but offers more service time; LEO 3 has less network load, moderate channel condition, but offers less service time. Furthermore, a new satellite, LEO 4 becomes available for providing coverage to the UE with excellent channel conditions, great service time with moderate network load. So even for a simple case involving 4 LEO satellites, the handover decision is not straightforward for a single UE. So finding a suitable handover strategy for a UE jointly considering all handover criteria becomes a complicated problem to be solved.

Different simple greedy strategies, like Maximum Service Time (MST), Maximum Signal Quality (MSQ), or Minimum Network Load (MNL) [260] are adopted to solve the problem in a simple heuristic manner but none of these approaches provide the optimal solution. The satellite handover scenario can be also modeled as a directed graph between different satellites for a single user where the weights can be set by different handover criteria like Quality of Service (QoS), service time, etc. [261], [262]. A bipartite graph matching problem between the satellites and the users [263] is also considered in the literature to provide the optimal handover decision for satellites. In addition, a network flow-based cost minimization approach is considered in [264] by weighting each edge as the QoS perceived by the user. A handover strategy based on a potential game in a bipartite graph is considered in [265]. Different heuristic algorithms are also proposed to solve the problem [266], [267], [268]. A dynamic optimization problem is considered to be solved based on forecasting in [269]. Channel reservation is also associated to design an efficient handover algorithm while balancing the load for satellites in [270].

An RL framework can be naturally adopted for solving this problem considering the handover criteria as states and UEs as agents who act by selecting a suitable LEO satellite and collecting a reward based on the network performances. In [252], only the overall signal quality of the network is maximized using the RL approach without considering any other criteria. In [253], [255], a multi-objective optimization problem considering satellite load and signal quality constraints is solved using the DRL approach. In real networks, we have a large number of UEs; the handover decision for one UE can affect another UE, so the handover problem needs to be solved in a cooperative manner. In [254], a MARL framework is considered where multiple UEs cooperatively optimize the number of handovers in the whole network considering different handover criteria. In [256], using graph matching, a database of optimum handover decisions in satellite networks is produced and later it is used to predict handover decisions using a CNN model. Advanced DL architectures like Auction based DL [257], DDQN [258], Successive DQN [259], etc. are also considered to provide optimal handover decisions. In Table VIII, we summarize the AI approaches for handover optimization in NTN involving LEO satellites. However, as all the system models consider the agents located at the UE side, it does not comply with the current standards where the handover decision is generally controlled by the BSs (satellites in this case). Furthermore, the distributed multiagent learning architectures give rise to stability issues in real implementations. The handover criteria also need to be carefully investigated to provide the agents with the necessary information to learn the mobility behavior of the environment.

![](images/841681e070fa38f708cb0c828356995a106a5a0bb2268e4c52a27912f11b9085.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    subgraph_LEO_1["LEO 1"]
        A["User with group icons"] --> B["UE that needs handover"]
        C["User with group icons"] --> D["UE that needs handover"]
        E["User with group icons"] --> F["UE that needs handover"]
        G["User with group icons"] --> H["UE that needs handover"]
        I["User with group icons"] --> J["UE that needs handover"]
    end

    subgraph_LEO_2["LEO 2"]
        K["User with group icons"] --> L["UE that needs handover"]
        M["User with group icons"] --> N["UE that needs handover"]
        O["User with group icons"] --> P["UE that needs handover"]
        Q["User with group icons"] --> R["UE that needs handover"]
        S["User with group icons"] --> T["UE that needs handover"]
        U["User with group icons"] --> V["UE that needs handover"]
        W["User with group icons"] --> X["UE that needs handover"]
    end

    subgraph_LEO_3["LEO 3"]
        Y["User with group icons"] --> Z["UE that needs handover"]
        AA["User with group icons"] --> AB["UE that needs handover"]
        AC["User with group icons"] --> AD["UE that needs handover"]
        AE["User with group icons"] --> AF["UE that needs handover"]
        AG["User with group icons"] --> AH["UE that needs handover"]
        AI["User with group icons"] --> AJ["UE that needs handover"]
    end

    LEO_4["LEO 4"]
    subgraph LEO_2
        AK["User with group icons"] --> AL["UE that needs handover"]
        AM["User with group icons"] --> AN["UE that needs handover"]
        AO["User with group icons"] --> AP["UE that needs handover"]
        AQ["User with group icons"] --> AR["UE that needs handover"]
        AS["User with group icons"] --> AT["UE that needs handover"]
    end
```
</details>

LEO 1: Moving out of coverage   
LEO 2: More network load, more service time,bad channel condition   
LEO 3: Less network load, lessservice time, moderate channel condition   
LEO 4: Currently not in the horizon, will provide excellent channel condition with moderate network load and best service time   
LEO 1: Moved out of coverage   
LEO 2: More network load, less service time, bad channel condition   
LEO 3: Moved out of coverage   
LEO 4: Great channel condition, best service time,moderate network load

Fig. 16. A Typical Handover Scenario in LEO Satellite-Based NTN   
TABLE VIIISUMMARY OF AI APPROACHES FOR HANDOVER OPTIMIZATION IN SATELLITE-BASED NTN

<table><tr><td rowspan="2">Reference</td><td colspan="4">Target Optimization Objectives</td><td colspan="3">Learning Approach</td><td rowspan="2">DL Tool</td><td colspan="2">Comments on Models</td></tr><tr><td>Signal Quality</td><td>Network Load</td><td>Service Time</td><td>Tx Delay</td><td>SL</td><td>UL</td><td>RL</td><td>RL Model</td><td>DL Model</td></tr><tr><td>[252]</td><td>√</td><td></td><td>√</td><td></td><td></td><td></td><td>√</td><td></td><td>Q-Learning</td><td></td></tr><tr><td>[253]</td><td>√</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td>√</td><td></td><td>Online Q-Learning</td><td></td></tr><tr><td>[254]</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td>√</td><td></td><td>Multi-Agent Q-Learning</td><td></td></tr><tr><td>[255]</td><td>√</td><td>√</td><td>√</td><td></td><td></td><td></td><td>√</td><td>√</td><td>DQN</td><td>CNN</td></tr><tr><td>[256]</td><td>√</td><td></td><td></td><td></td><td>√</td><td></td><td></td><td>√</td><td></td><td>CNN</td></tr><tr><td>[257]</td><td>√</td><td></td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td>Auction based approach (Game theory)</td><td>FCNN</td></tr><tr><td>[258]</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td>√</td><td>DDQN</td><td>FCNN</td></tr><tr><td>[259]</td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td>√</td><td>Successive DQN</td><td>FCNN</td></tr></table>

These issues need to be resolved in an efficient manner for future research work in this domain.

6) Multiple Access: Multiple access is a vital technique that enables multiple users to efficiently share network resources like spectrum and time. In traditional satellite networks, orthogonal multiple access schemes like Time Division Multiple Access (TDMA), Frequency Division Multiple Access (FDMA), Code Division Multiple Access (CDMA), and Space Division Multiple Access (SDMA) are employed. These schemes allocate distinct time slots, spectra, codes, or spatial divisions to us0ers, ensuring their orthogonality in resource utilization. However, the performance of these conventional methods is constrained by the inherent limitations of these network resources. To meet the extremely

high data rate and low latency demands of future 6G networks, innovative and efficient multiple access techniques, such as Non-Orthogonal Multiple Access (NOMA) and Rate Splitting Multiple Access (RSMA), have emerged in satellite network research. These advanced techniques deliver superior performance, achieving higher spectral efficiency and reduced latency, thereby paving the way for the evolution of future 6G networks.

In contrast to other conventional approaches, NOMA allows multiple users to share the same time-frequency resource block by allocating different power levels to users based on their respective channel conditions. The users are assigned the transmit power levels in an inverse manner with respect to their channel conditions, i.e. users with poorer channel conditions are allotted more transmit power whereas users with better channel conditions are allotted lower transmit power. These signals are subsequently encoded, combined using superposition coding, and transmitted to the receiver. Then Successive Interference Cancellation (SIC) technique is employed to decode signals for different users. Starting with the user granted the highest transmission power, SIC successively extracts signals while treating others as interference. This process continues down to the user with the lowest transmission power, efficiently enabling multiple users to share the resource block and enhancing spectral efficiency. However, it’s important to note that SIC’s computational complexity increases with this approach.

The optimum power allocation problem in NOMA for NTNs can be formulated as a non-convex problem which is often difficult to solve using conventional approaches. In [271], a long-term power allocation scheme for NOMA in satellite-IoT networks is solved by deriving the optimal decoding order leveraging DL techniques. A DQN-based DRL approach is investigated in [272] for optimum power allocation in satellite-IoT networks under different channel conditions and delay-QoS requirements of NOMA users. In another study as discussed in [273], the non-convex problem involving integer variables is later reformulated as a mixedinteger convex problem which was later solved by two DL techniques instead of conventional iterative solutions. Some studies also focus on the non-convex user selection problem for given power allocations based on the CSI feedback. Such a study, [274] used DQN to find out the suitable user pairing for delay-limited NOMA-based satellite networks considering the channel conditions and delay constraints as states. k-means UL approach is also considered to find out the pair of terrestrial users to be simultaneously served by space and aerial BSs adopting NOMA in [275]. Q-learning is adopted in [276] to allocate the time slots and communications channels for IoTsatellite terrestrial relay networks.

Another significant multiple access method, RSMA, is also explored in the context of satellite networks to enhance spectral efficiency. In RSMA, user messages are partitioned into two segments: common and private. The common signals are collectively encoded and merged into a unified data stream intended for all users, while each user linearly precodes their private messages. On the receiver side, the common component is extracted while treating the private signals as noise, employing the SIC technique. Subsequently, each user extracts their respective private signals. This provides the users with another way to share the same resource blocks with an increase in spectral efficiency. Generally maximizing the sum rate for both parts is a complicated non-convex problem and can be solved by Weighted MMSE (WMMSE) problem which is difficult to implement in practical hardware. A successive convex approximation as well as KarushKuhnTucker (KKT) conditions are used to calculate the transmit power in RSMA power for different beams in satellite networks in [277]. However, DL techniques can be extremely useful in modeling the solution framework with low complexity as shown in [278], [279]. Here a deep unfolding technique is used to implement the WMMSE algorithm using a deep NN

![](images/b028dc8c7aff2c0e96a64a82d157c9dbcdf947552347c8361a8f21e30300ea8e.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Terrestrial Cloud"] -->|Offloading| B["LEO Satellites"]
    B <--> C["Offloading"]
    C --> D["Terrestrial UEs"]
    D --> E["Offloading"]
    E --> F["TERrestrial BSs"]
    F --> G["Offloading"]
    G --> H["TERrestrial UEs"]
    H --> I["Offloading"]
    I --> J["TERrestrial BSs"]
    J --> K["Offloading"]
    K --> L["TERrestrial UEs"]
    L --> M["Offloading"]
    M --> N["TERrestrial BSs"]
    N --> O["Offloading"]
    O --> P["TERrestrial UEs"]
    P --> Q["Offloading"]
    Q --> R["TERrestrial BSs"]
    R --> S["Offloading"]
    S --> T["TERrestrial UEs"]
    T --> U["Offloading"]
    U --> V["TERrestrial BSs"]
    V --> W["Offloading"]
    W --> X["TERrestrial UEs"]
    X --> Y["Offloading"]
    Y --> Z["TERrestrial BSs"]
    Z --> AA["Offloading"]
    AA --> AB["TERrestrial UEs"]
    AB --> AC["Offloading"]
    AC --> AD["TERrestrial BSs"]
    AD --> AE["Offloading"]
    AE --> AF["TERrestrial UEs"]
    AF --> AG["Offloading"]
    AG --> AH["TERrestrial BSs"]
    AH --> AI["Offloading"]
    AI --> AJ["TERrestrial UEs"]
    AJ --> AK["Offloading"]
    AK --> AL["TERrestrial BSs"]
    AL --> AM["Offloading"]
    AM --> AN["TERrestrial UEs"]
    AN --> AO["Offloading"]
    AO --> AP["TERrestrial BSs"]
    AP --> AQ["Offloading"]
    AQ --> AR["TERrestrial UEs"]
    AR --> AS["Offloading"]
    AS --> AT["TERrestrial BSs"]
    AT --> AU["Offloading"]
    AU --> AV["TERrestrial UEs"]
    AV --> AW["Offloading"]
    AW --> AX["TERrestrial BSs"]
    AX --> AY["Offloading"]
```
</details>

Fig. 17. Task offloading in satellite-terrestrial integrated networks.

and momentum-accelerated Projection Gradient Descent algorithm. A DRL framework using Proximal Policy Optimization is used to maximize the sum rate in [280]. Here each BS works as an agent, the channel state information i.e. SINR of the private and common messages is used as the states, the action is to find the suitable power allocation whereas the reward is the achieved sum rate.

# D. Upper Layer Aspects

1) Computation Offloading: One of the most important applications of satellite-terrestrial integrated networks is enhancing the computation capabilities of existing terrestrial network architectures leveraging satellites. With traditional terrestrial networks, supporting a diverse set of new applications like AR, VR, etc. with high data processing and extremely low latency requirement can get very challenging. Generally, terrestrial BSs are deployed sparsely due to high infrastructure and maintenance costs. Due to resource constraints, in case of the high demand for data processing for these types of applications, the BSs need to offload the computation tasks to the terrestrial cloud via the satellites [290]. However, due to longer propagation delay, the latency requirements set by the applications are difficult to be met [291]. Nevertheless, due to the emergence of LEO satellites with comparatively low propagation delay, the overall delay is considerably reduced. Also instead of acting as relays, the satellite can now also do the processing works acting as edge-servers. So we can consider a three-level hierarchical architecture comprising of ground UEs connected to terrestrial BSs, LEO satellites, and terrestrial cloud as shown in Figure 17 where the terrestrial BSs can offload the computational tasks to LEO satellites and to terrestrial clouds via the LEO satellites.

The main challenges in task offloading problems lie in meeting the delay constraints for low-latency applications while minimizing the energy consumption for the satellites. So this can be formulated as an optimization problem to come up with an efficient offloading approach for integrated TNTN architecture. Such an optimization problem is solved using different conventional approaches like 3D hypergraph matching [292], game theory [293], stochastic approach [294], efficient algorithms [295] in the existing literature. In [296], a joint optimization framework comprising task offloading and resource allocation is also considered in an integrated satelliteterrestrial environment. Although these algorithms work well in theory for particular scenarios, in real networks, the feasibility of these algorithms is compromised due to different issues. Some of these works do not consider the cooperation among terrestrial cloud and LEO satellite servers which result in suboptimal approaches [292], [293]. Also, these approaches are some predefined models highly dependent on different network states causing a large overhead in networks. Moreover, they usually converge to the solutions after a large number of iterations causing high computational complexity.

TABLE IX SUMMARY OF AI APPROACHES FOR TASK OFFLOADING IN TNTN 

<table><tr><td rowspan="2">Reference</td><td colspan="3">Problem Insight</td><td colspan="3">Learning Approach</td><td rowspan="2">DL Tool</td><td colspan="2">Comments on Models</td></tr><tr><td>Energy Consumption</td><td>Tx Delay</td><td>Computational Resources</td><td>SL</td><td>UL</td><td>RL</td><td>RL Model</td><td>DL Model</td></tr><tr><td>[281]</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>DDPG</td><td>FCNN</td></tr><tr><td>[282]</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>Model-Free</td><td>FCNN</td></tr><tr><td>[283]</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td>Value Iteration, DQN, DDQN</td><td>FCNN</td></tr><tr><td>[283]</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td>Dueling DDQN</td><td>FCNN</td></tr><tr><td>[284]</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>MARL</td><td></td></tr><tr><td>[285]</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td>DQN based MARL</td><td>FCNN</td></tr><tr><td>[286]</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>LSTM</td></tr><tr><td>[287]</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td>DQN</td><td>FCNN</td></tr><tr><td>[288]</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td>✓</td><td></td><td>Distributed FCNN (For solving Optimization)</td></tr><tr><td>[289]</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>Distributed FCNN (For solving Optimization)</td></tr></table>

To tackle these issues, different ML approaches are proposed in the literature to solve task offloading problems. In [282], a DRL-based task offloading framework dependent on channel state information is proposed. A similar DRLbased framework is also considered in [297] with additional consideration of the dynamic queue condition in satellites. In [283], both DQN and DDQN are explored to solve the task offloading problem in a decentralized manner. DDPG algorithm is considered to solve the optimization problem in a DQN framework in [281] while taking the potential security issues into account. An LSTM model is used to solve the task offloading problem while considering channel conditions and energy dynamics in [286]. A DL-based caching strategy is considered in satellite edge networks in [287]. As we have multiple satellites in the real networks, to improve the overall system performances, different multi-agent architectures are considered both in a distributed [288] and cooperative environment [284], [285]. Distributed architectures for generating discrete offloading decisions in a supervised manner are also considered in [289]. In Table IX, we summarize the AI approaches for task offloading in TNTN. As the delay constraints vary with network traffic types, the offloading decisions need to be derived taking network traffic types into account. Potential research works can show how computational offloading can be done for various network traffics and show superior network performances.

![](images/8b8ef7bef5b7ac0dcd02d0d3b0987ab21627b3bda50beb7f2b0e229dead26db7.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Satellites"] -->|Satellite-Ground Links| B["Ground Terminal"]
    A -->|Satellite-Ground Links| C["Terrestrial BS"]
    A -->|Satellite-Ground Links| D["Terrestrial LG"]
    B --> E["TEA"]
    C --> F["TEA"]
    D --> G["TEA"]
    E --> H["UEs"]
    F --> I["UEs"]
    G --> J["UEs"]
    H --> K["Satellite Gateway"]
    I --> L["Satellite Gateway"]
    J --> M["Satellite Gateway"]
    K --> N["Satellite Gateway"]
    L --> O["Satellite Gateway"]
    M --> P["Satellite Gateway"]
    N --> Q["Satellite Gateway"]
    O --> R["Satellite Gateway"]
    P --> S["Satellite Gateway"]
    Q --> T["Satellite Gateway"]
    R --> U["Satellite Gateway"]
    S --> V["Satellite Gateway"]
    T --> W["Satellite Gateway"]
    U --> X["Satellite Gateway"]
    V --> Y["Satellite Gateway"]
    W --> Z["Satellite Gateway"]
    X --> AA["Satellite Gateway"]
    Y --> AB["Satellite Gateway"]
    Z --> AC["Space-Air Segment"]
    AA --> AC
    AB --> AC
```
</details>

Fig. 18. Network routing in satellite-terrestrial integrated networks.

2) Network Routing: In wireless networks, depending on the traffic and channel conditions, the network traffics are routed to different paths among different network nodes so that the overall network performance can be improved. In any network with static channel and traffic conditions, this routing problem can be transformed into the well-known shortest path problem and solved by Dijkstra’s algorithm [306]. Here the network nodes can be considered as nodes in the graph and the edges can represent the links between different nodes. The weights of the edges can be defined based on the target network performance metrics like delay, jitter, throughput, packet loss, etc. However, the topology of the real satelliteterrestrial integrated networks (shown in Figure 18) are very complex and dynamic due to hierarchical network architecture and uncertain channel and traffic conditions, respectively. So simple Djikstra’s algorithm cannot be directly applied to meet the performance requirements in these networks.

TABLE XSUMMARY OF AI APPROACHES FOR NETWORK ROUTING IN TNTN

<table><tr><td rowspan="2">Reference</td><td colspan="3">Target Optimization Objective</td><td colspan="3">Learning Approach</td><td rowspan="2">DL Tool</td><td colspan="2">Comments on Models</td></tr><tr><td>Throughput</td><td>Tx Delay/jitter</td><td>Error Rate</td><td>SL</td><td>UL</td><td>RL</td><td>RL Model</td><td>DL Model</td></tr><tr><td>[298]</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>Q-Learning</td><td></td></tr><tr><td>[299]</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>Q-Learning</td><td></td></tr><tr><td>[300]</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td>✓</td><td></td><td>Distributed Q-Learning</td><td></td></tr><tr><td>[301]</td><td>✓</td><td>✓</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td>Fuzzy-CNN</td></tr><tr><td>[127]</td><td>✓</td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>CNN</td></tr><tr><td>[302]</td><td>✓</td><td>✓</td><td></td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>FCNN</td></tr><tr><td>[303]</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>ELM</td></tr><tr><td>[304]</td><td></td><td>✓</td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td></td><td>Graph Neural Network (GNN) + FCNN</td></tr><tr><td>[305]</td><td></td><td>✓</td><td>✓</td><td></td><td></td><td>✓</td><td>✓</td><td>DDPG</td><td>LSTM</td></tr></table>

In real satellite networks, Asynchronous Transfer Mode (ATM) routing is introduced in [307]. The well-known Open Shortest Path First (OSPF) [308] protocol-based Internet Protocol (IP) routing is also adapted to the dynamic satellite environment in [309]. However, the dynamics of satellite-terrestrial networks are very different from traditional terrestrial networks due to their highly dynamic network topology, link status, and traffic conditions. Depending on the instantaneous network topology, a static-dynamic combined routing scheme is considered in [310]. An ant-colonybased optimization (ACO) framework is considered in [311]. In [312], a Kalman filter-based Wolf Colony Optimization algorithm is used to solve the local optimal solution issue in [311]. An improved ACO framework is considered to find out the optimal set of links with multiple network constraints in [313]. A Coordinate Graph (CG) model-based network routing approach for three-dimensional TNTN is considered in [314]. In [315], minimum flow maximum residual pathbased network flow algorithm is used to find out the optimal network routing path for satellites. In [316], a 3-dimensional network mapping using hyperbolic geometry is considered for integrated satellite-terrestrial networks.

To cope with the dynamic environment in integrated satellite-terrestrial networks, different DL architectures are proposed in the literature. In [301], fuzzy logic is used to evaluate task requirements to improve the CNN output for optimal path allocation. The network routing optimization problem can be put into an RL framework. In [298], a speedup Q-learning algorithm is used to find out the optimal routing strategy for TNTN. A similar Q-learning-based RL framework is also considered to solve the routing problem for LEO satellites in [299]. To tackle the complexity issue, a DRL framework is used to generate optimal routing strategies in TNTN [305] and LEO satellite networks [299]. FCNN [302], CNN [127], etc. architectures are used to solve the routing problem in a supervised manner. Other ML frameworks like GNN [304] and ELM [303] are also considered to solve the routing problem in NTNs. In Table X, we summarize the AI approaches for network routing in TNTN. Recursive NN architectures need to be also explored for capturing the temporal behavior in network routing decisions. Furthermore, the channels are extremely dynamic and time-varying in the case of TNTNs; the channel conditions can be also considered in the learning criteria of RL frameworks.

3) Traffic Prediction: Traffic prediction is very critical in modern communication systems to ensure high-speed low latency communications. Particularly, in NTNs, accurate traffic prediction is extremely crucial due to the highly dynamic network topology as well as diverse user requirements. At its core, traffic prediction involves forecasting future network traffic based on past usage patterns. Conventional approaches such as Auto Regressive Moving Average (ARMA), Auto Regressive Integrated Moving Average (ARIMA) [317], [318], etc. are typically used for these predictions. However, the DL approaches have emerged as more effective alternatives by providing improved performances in recent times due to their inherent capability to capture spatial and temporal correlations.

In [319], Radial Basis Functions (RBF) neural networkbased short-term traffic flow forecasting is proposed. In [320], an LSTM-based architecture is utilized for traffic prediction due to its temporal characteristics handling capability where the attention mechanism is used to balance the effect of inputs on outputs properly. The RNN architectures suffer from gradient explosion issues. To overcome this issue, GRU architectures are explored for traffic prediction in [321], [322], and [323]. In [321], the transfer learning approach and particle filter online training algorithm are combined to address the lack of online training data and reduce the training time complexity. In [322], GNNs are used to extract the spatial features of the satellite network traffic from the input network topology, which is later used as an input to a GRU network for traffic prediction. In [323], on top of the attention mechanism and GRU models, PSO is used to obtain the best set of hyperparameters for the network.

Key Takeaways: As evidenced by the above discussion, various RL techniques are used to examine network optimization problems such as handover, beam, and resource allocation, task offloading, network routing, and network slicing, while SL techniques are employed to tackle estimation problems, such as Doppler shift, channel state, and spectrum sensing.

![](images/e38f6dc10161629624c5df24264d1420906b275cda2b33762b9187ae7120e881.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Channel Estimation"] --> B["NTN Challenges"]
    C["Doppler Shift Estimation"] --> B
    D["Spectrum Sharing"] --> B
    E["Traffic Prediction"] --> B
    F["Security Aspects"] --> B
    G["Supervised Learning"] --> H["ML"]
    I["Handover"] --> B
    J["Beam and Resource Allocation"] --> B
    K["Network Routing"] --> B
    L["Network Slicing"] --> B
    M["Task Offloading"] --> B
    N["Reinforcement Learning"] --> H
```
</details>

Fig. 19. Relationship diagram different AI techniques and NTN challenges.

UL techniques have not been extensively covered in the literature due to the ambiguity and difficulty of applying them in real networks. To further illustrate the interrelations between different NTN challenges and AI techniques, we present Figure 19.

# VI. AI-NTN INTEGRATION: CURRENT STATUS

In the previous section, we discuss how AI can be beneficial for us in resolving potential NTN issues for the next-generation 6G networks. In this section, how AI can be applied to real systems to resolve the challenges associated with NTNs. We begin our discussion by discussing the current ML testbeds for satellites. Then we discuss how AI can be potentially applied to future 6G networks by utilizing the RAN Intelligent Controller (RIC) embedded in the Open Radio Access Network (O-RAN) framework [324] to overcome the inflexibility of the monolithic cellular networks. Finally, we provide a discussion on current research efforts toward realizing the Software Defined Radio (SDR) based 5G-NTN platform development in the O-RAN framework.

# A. ML Testbeds for Satellite Networks

MultI-layer awaRe SDN-based testbed for SAtellite-Terrestrial networks (MIRSAT) testbed [325] provides a Software Defined Network (SDN) based experimentation platform for testing network slicing algorithms on NGSO constellations. The European Space Agency (ESA) has numerous completed projects focusing on the applicability of AI techniques in satellite networks such as MLSAT [326] and SATAI [327]. There are also several other ongoing projects of ESA focusing on AI-satellite issues like AI integrated 5G-Satellite testbed [328], AI-based interference detection [329], AI-based signal processing [330], etc. All these testbeds show promises for AI to be an integral part of future satelliteterrestrial integrated networks.

# B. AI-NTN Integration Through O-RAN-Based RIC

Traditional 5G networks with little or no reconfiguration capabilities suffer from a wide variety of challenges to satisfy the heterogeneity and variability of the networks and meet the strict application requirements [331]. Even though there has been a significant amount of research on addressing different issues in 5G cellular networks, an open interface for the deployment of AI algorithms is required. O-RAN offers a general framework for the deployment of AI algorithms in 5G-Advanced networks [332]. It achieves this by facilitating an open interface that enables the exchange of network KPIs and control information between the RAN and the AI controller. This integration allows for the implementation of a closedloop control framework for the RAN using different AI approaches [333], [334]. As a potential integral part of future 6G networks, NTNs are expected to be deployed in the O-RAN framework to leverage AI capabilities effectively.

In 5G, a base station, namely gNB has multiple functional splits, namely:

1) Central Unit (CU): responsible for higher layers such as non-real-time link and network layer functionalities.   
2) Distributed Unit (DU): responsible for lower layer such as near real-time link and upper PHY layer functionalities.   
3) Radio Unit (RU): responsible for low PHY layer functionalities.

A new central controller entity called RIC is introduced in the O-RAN architecture which can provide network monitoring and control functionalities in near real-time and non-real-time through external and internal applications, called xApps and rApps respectively, for the purpose of network optimization. Evidently, these xApps and rApps can provide us with an effective way of deploying AI algorithms extracting network KPIs, and sending control commands for optimizing network performance.

To realize the NTN architecture in the O-RAN framework, the satellites can be used for either transparent or regenerative payloads as discussed in Section II-C. In the case of regenerative payloads, where the NTN platforms work as BSs, there are multiple options for potential O-RAN-based NTN deployment. There can be three different architectural deployments for NTN gNBs in the regenerative architecture:

1) RU in the space/air, CU and DU on the ground,   
2) Both RU and DU in the space/air, CU on the ground,   
3) CU, DU, and RU in the space/air.

The non-real-time which does not need to consider latency requirements, is expected to be deployed on the ground considering power, onboard capability, and mobility constraints. However, the near real-time RIC needs to be close to DUs to provide near real-time control functionalities which provide two different options for its deployments with corresponding pros and cons. The near real-time RIC should be on the ground when only RU is in the air, whereas it should be also in the air in the other two cases. There is a clear tradeoff between the latency and power, mobility, and onboard capability constraints. If the near-real-time RIC is in the air, the latency for control commands will be low, whereas the cost will be high for hosting it in the air. In Figure 20, the potential framework for AI-Enabled NTN deployment in O-RAN framework as specified in [324] is illustrated. Depending on the deployment scenarios of the near-real-time

![](images/03a4f8dee41937c33a953ccd380e0236df259dc1935eef781130b3f9e66448b6.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Applying AI using xApps"] -->|Open API| B["Near real-time RIC"]
    B -->|A1| C["Non-real-time RIC"]
    C -->|R1| D["Applying AI using rApps"]
    B -->|E2| E["RU"]
    C -->|O1| F["DU"]
    E --> G["Uu"]
    F --> H["FH"]
    H --> I["F1"]
    I --> J["CU"]
    J --> K["NG"]
    K --> L["Next Generation Core"]
    M["Ground deployment"] --> N["On the air deployment"]
    O["Ground/ On the air deployment"] --> P["Ground deployment"]
```
</details>

Fig. 20. Various architectural deployments for NTN in the O-RAN framework for regenerative payload.

RIC, the xApps can be also deployed also in the air or on the ground, and so do the AI control algorithms.

# C. Current Research Efforts for AI-NTN Integration Through O-RAN-Based RIC

To facilitate the integration of NTN into 6G networks, there have been already some technical advancements and experimental research works towards developing real prototypes for testing and evaluation of proof-of-concept methods. OpenAirInterface (OAI) is an open-source 3GPP compliant SDR-based protocol stacks that are widely used across the research community for experimentation with 5G networks [335]. As specified in the O-RAN framework, OAI protocol stacks adopt the notion of RIC by enabling serviceoriented controllers using an efficient Software Development Kit, called Flexible RIC (FlexRIC) [336]. This RIC provides an interface for applying AI algorithms in order to optimize the network performances through xApps as discussed before. This enables us to perform experiments for testing diverse AI approaches for optimizing the performances of real 5G networks.

OAI has been adopted for developing experimental prototypes with 5G-NTN adaptations due to its efficient and flexible design and structure [337]. Currently, there are several research projects on 5G-NTN that are leveraging OAI protocol stacks to perform experiments with NTN adaptations for both in-lab validation and over-the-satellite testing. 5G AgiLe and flexible integration of SaTellite And cellulaR (5G-ALLSTAR) [338] and 5G New Radio EMUlation over SATellite (5G-EmuSat) [339] project developed a 5G-NTN platform with necessary PHY and MAC layer 5G-NR adaptations on top of OAI 5G protocol stacks and a satellitechannel emulator for in-lab validation. 5G-EmuSat even has also demonstrated its over-the-satellite capability by having direct access to a UE using a satellite channel. 5G Space Communications lab also has performed in-lab validation experiments extending OAI-4G protocol stacks for NTN along with ISL implementation using SDR [340]. Two current ongoing projects focusing on GEO and LEO satellites, named 5G-GOA [341] and 5G-LEO [342] respectively, are currently working on implementing necessary 3GPP NTN adaptations extending from 5G protocol stacks of OAI. Even though current implementations are mostly for demonstration purposes, integration of NTN into OAI 5G protocol stacks paves the way for deploying AI algorithms through xApps in the future.

Key Takeaways: Currently, there are some deployed ML testbeds specifically designed for satellite networks. Moreover, O-RAN is envisioned to unleash the great potential of AI in enabling the future 6G networks via satellite-based NTNs by addressing various challenges associated with it. Nevertheless, both O-RAN and NTN standardization aspects are still in the development process, and different SDR-based 5G protocol stacks, such as OAI, are being incorporated with NTN adaptations.

# VII. AI-NTN INTEGRATION: CHALLENGES

NTNs come with an intrinsic set of challenges when it comes to deploying AI models. Even though there is a significant decrease in the launching and maintenance cost of various NTN platforms, especially satellites, cost optimization is still one of the major limiting factors of realizing NTNs for 6G communication on a large scale. With that being the case, these platforms have limited power, spectrum, and computational resources which limits the performance of the AI models. The unavoidable long propagation delay along with the complex and time-varying nature of the NTN environment introduces additional challenges for AI models to be trained and deployed in real-time. In this section, we discuss these open research issues to get an insight into designing an efficient AI-based non-terrestrial system with robust and superior performance.

# A. Limited Onboard Capability

Advanced AI applications necessitate specialized AI-capable embedded chipsets developed by leading technology companies, including NVIDIA, AMD, Intel, and Qualcomm [343]. Typically, these chipsets feature on-chip accelerators like CUDA and Tensor, enabling highly efficient parallel processing of intricate data tasks, especially those involving extensive matrix operations as utilized in DL methodologies. The performance of these AI algorithms highly depends on the availability of the computational resources and data processing capabilities of the AI hardware blocks. More computational capability typically means more power consumption as well as more physical space which increases the overall maintenance cost for the non-terrestrial platforms. Most non-terrestrial platforms such as satellites have a very limited amount of computational resources due to cost optimization. The efficiency of computing devices, particularly those used for onboard purposes, is often quantified by evaluating the ratio of computational power to the product of power consumption, total mass, and associated cost. This metric, highlighted in [344], necessitates a notably high value for onboard computing devices in satellites. All these AI-capable chipsets must undergo meticulous design and rigorous testing procedures to ensure they satisfy the minimum computing efficiency standards mandated for space platforms. A lot more advancements in miniaturization and power efficiency are necessary to ensure the adaption of AI models and algorithms into non-terrestrial platforms with adequate onboard capabilities as well.

# B. Aging of Information

The long propagation delay is a great challenge in the way of AI-based NTN deployment. Online RL frameworks are very promising for solving different NTN challenges due to their inherent capability of adapting to fast time-varying environments as we show in the previous sections. However, the performance of these algorithms is highly dependent on the feedback received from the environment. As the network changes very rapidly, the feedback has to be real-time or near real-time to ensure the integrity of the information embedded in the feedback. For example, the resource allocation for different network slices and users needs to be near-real-time (in the order of 1-10 ms) and real-time (less than 1 ms), respectively. For NTNs, as we know from Section II-D, the propagation delay is extremely high due to the long distance between the transmitter and the receiver. Thus the feedback exchange time intervals are quite high compared to terrestrial environments which hampers the online training approach greatly. Furthermore, to adapt to the highly time-varying environment, AI models usually need to send an appropriate chain of control commands to the network components. Due to the rapid channel variations, the channel coherence time is significantly reduced, leading to potential issues where both received information and transmitted control commands may become outdated, resulting in reduced effectiveness for resource allocation decisions from AI algorithms.

# C. Additional Communication Overheads

On top of long propagation delay, non-terrestrial platforms also have limited bandwidth due to the scarcity of spectrum resources and ensure no additional interference to the licensed services. As the generic RL frameworks depend on the feedback received from the environment, the additional overhead introduced by the network parameters results in undesirable network resource consumption. Even though CSI feedback in 5G networks contains a set of network parameters, this may not be enough for all different network problems. For instance, when dealing with the handover optimization problem, many solution techniques operate under the assumption that mobility state information for satellites and users is readily available, which is not typically included in the CSI feedback. Consequently, this assumption introduces additional feedback overhead alongside the existing format. This additional communication overhead puts an additional burden on the limited spectrum of resources allocated for the non-terrestrial platforms.

# D. Security Aspects

Applying AI in NTNs introduces more vulnerability to various security attacks by introducing new attack surfaces and less transparency. Adversarial attacks, data poisoning, and model evasion involving the manipulation of input data to AI models can cause degradation in network performance and reliability [345]. Since this input data is gathered from the NTN environment, featuring various attack interfaces for potential attackers, there is a risk that the training data used for AI models could be compromised by these attackers. Denialof-Service (DoS) attacks can cause interruptions in crucial network operations by overwhelming the network with too much resource consumption [346]. As an illustrative example within the context of NTNs, an attacker could conceivably gain access to one of the network slices. They could then exploit this access to excessively consume network resources by setting up extreme requirements, potentially leading to network congestion and subsequently causing a decline in overall network performance. As discussed before, the AI controller and the network environment, especially in the online setup, needs to exchange control information during training of the models. While carrying the control information between the AI controller and the network, an attacker can intercept and possibly modify this information, which is known as a Man-in-the-Middle (MiM) attack [347]. This can often result in a degradation in network performances due to the compromised control information. Therefore, A securityconstrained framework for deploying AI models needs to be designed carefully in such a way that they can detect and mitigate these attacks while maintaining the overall network performance.

# E. Environmental Conditions

NTN platforms, especially satellites are generally deployed in pretty hostile environments with extreme radiation, extreme temperatures, and other extreme environmental conditions. The computational hardware for AI models is very susceptible to radiation as they are built on customized circuitry [344]. The satellites need to consider both single-event effects caused by ionizing particles [348] as well as the effects due to longterm radiation [349]. These effects may result in bit flips both in registers and memories introducing errors in the control logic of their hosting hardware platforms. Also, in space, these circuitry elements need to withstand extreme temperatures for a long period of time [350]. To ensure the proper performance of these models, the hosting hardware components are required to be more advanced and have rigorous testing to ensure extreme environmental tolerance, which increases the cost of the satellite operation.

# F. Scalability Issue

RL frameworks can be naturally applied to address a variety of NTN problems with control objectives as we discuss in the previous section. However, for large-scale 6G satellite-terrestrial integrated wireless networks, the complex network topology entails high dimensional state and action spaces that can lead to high computational complexity for RL models [351]. In the case of MARL frameworks, the state space grows exponentially with the increase in the number of agents [352], making this approach infeasible for largescale real networks. Although DRL approaches can be helpful in reducing the state space [353], more research is needed to effectively address this challenge in order to successfully deploy RL approaches in TNTNs.

# G. Lack of Convergence

An important challenge to be addressed when applying the distributed RL framework in real networks for solving various important NTN challenges like handover optimization is to deal with its uncertainty in convergence [90]. In this framework, multiple agents try to optimize their goals based on the rewards received from the environment. In a competitive environment, when all the agents are attempting to maximize their long-term returns, they may take conflicting actions, resulting in a non-stationary environment with no convergence to an optimum state [352]. As a result, no optimum policy can be obtained for the system as a whole. As highlighted in [254], this convergence issue has limited the number of UEs (agents) that can be considered in the simulation environment, thus hindering the potential of this approach.

# H. Scarcity of Quality Data

All ML approaches are data-driven, so the availability of suitable training data is of paramount importance for the improved performance of these methods. However, in satellite-terrestrial integrated networks, the generation of quality data can be sometimes very costly and inefficient, even impossible at times due to spectrum and intermittent connectivity constraints. Due to this inherent data generation issue, applying different ML approaches can get extremely challenging. Additionally, the data distribution and characteristics in non-terrestrial environments may differ significantly from terrestrial environments, requiring careful consideration during model training and adaptation. As a result, the training procedure can be greatly hampered resulting in performance degradation of these approaches in real networks.

# I. Complicated Hyperparameter Settings

The complexity of satellite-terrestrial networks, such as their topology and time-varying nature, can make traditional ML approaches less effective. As a result, DL methods have become increasingly popular due to their powerful feature extraction capabilities through NNs. The performance of any NN is reliant on the hyperparameter settings, such as the number of layers, activation functions, number of neurons in a layer, and learning rate. However, there is no way of deriving an optimal set of these parameters for any given problem to provide the best performance. In fact, tuning these parameters to provide satisfactory performance for a particular problem is not any straightforward process, but rather dependent on empirical speculations. This means the training process is not a one-time event, but rather a trial-and-error process that involves multiple attempts to determine the most suitable parameters. Moreover, depending on the nature of the problem, it can be challenging to determine possible candidates for the parameters to begin with. This results in a very uncertain and time-consuming training process. For NTNs, these issues are more severe due to their high network complexity resulting in a more complex set of hyperparameters.

# J. Lack of Generalization

As data-driven ML approaches are used to train ML algorithms, it can be difficult to generalize these algorithms to different scenarios. Trained models are able to capture the characteristics of the training data, but this does not always guarantee successful performance with test data due to the varying nature of NTNs. A model trained for a specific scenario may not be successful in another, and may not be able to adapt to different NTN scenarios. Even if the model has not encountered certain scenario features during training, it is desirable to have a model that is generalizable and performs well in any context. Developing such models is one of the biggest challenges of the NTN domain due to their high network complexity. As there are no theoretical performance bounds for these empirical ML models, unpredictable performance drops can occur while deploying in the real environment.

Key Takeaways: The cost-limited on-board computation, highly dynamic environmental conditions, and long propagation delay introduce a diverse set of challenges to realize the AI-enabled NTN environment for future 6G networks. These challenges need to be addressed with efficient solutions to ensure superior network performances in real NTN deployments.

# VIII. INSIGHTS AND POTENTIAL FUTURE STUDIES

In this comprehensive study, we delve into the realm of NTNs and their relationship with AI techniques, establishing a solid background for our exploration. We explore the synergy between NTNs and AI, highlighting how these two domains intersect and complement each other. Moving forward, we shift our focus to the current research thrusts in the field, examining ongoing efforts to bring these concepts to fruition in realworld networks. While highlighting these advancements, we also address the potential challenges that must be overcome to realize the full potential of NTNs in the context of future 6G networks. Within this section, we provide an in-depth discussion of valuable insights and potentianl future studies for leveraging various AI techniques in the context of satellitebased NTNs.

# A. Insights

In this section, we present a summary of the lessons learned and insights gained from our paper’s discussion. These insights are intended to serve as valuable guidance and information for the implementation and integration of AI in shaping the future landscape of 6G networks.

1) Existing Learning Approaches: Upon examining the contents presented in Section V, it becomes evident that SL and RL approaches take center stage in addressing the diverse array of challenges faced by satellite-based NTNs in future 6G networks, primarily due to the availability of real-world data and feedback mechanisms within existing networks. In the context of SL, having access to welllabeled data is of utmost importance, especially in scenarios involving estimation problems like channel estimation and Doppler Shift estimation. On the contrary, RL shines when dealing with problems lacking clear labels but featuring a notion of reward functions. Furthermore, RL techniques are extremely suitable and efficient for problems where supervision is lacking which is usually the case for many NTN problems such as resource allocation, beam hopping, and network routing as illustrated in Section V of the paper. Meanwhile, RL techniques can be effectively employed across a wide spectrum of problems using general network feedback, such as CSI, acknowledgments, and more. Consequently, a significant portion of research efforts tends to leverage RL frameworks to address their specific challenges.

2) Leveraging Deep Neural Networks: The emergence of Deep NNs and their effectiveness in addressing intricate challenges in fields like computer vision and natural language processing has piqued the interest of the research community in applying these architectures to network-related issues. Satellite-based NTNs introduce a unique set of challenges, characterized by highly dynamic network conditions and a multitude of variables influencing network performance. Traditional ML) approaches often fall short in comprehensively addressing these complex problems, frequently limited to small-scale issues. As a result, DL techniques have gained significant popularity within the research community, proving to be a more adept choice for tackling the multifaceted challenges encountered in satellite-based NTNs, as elaborated in Section V.

3) Potential Learning Approaches: The nature of UL approaches presents a unique set of challenges in the context of highly dynamic and time-varying NTNs. Understanding and capturing the intrinsic behavioral patterns within such networks prove to be particularly hard. However, it is important to note that UL approaches still hold the potential to derive the distribution of crucial network parameters that may not be readily accessible in real networks. These derived

parameters can play a pivotal role in addressing various NTN challenges. The distributed learning approaches such as FL can be also beneficial for future satellite-based NTNs as the computing capabilities requirements can be reduced to a minimum enhancing practical feasibility.

4) Enabling O-RAN-Based RIC: Currently, there are some ongoing research efforts focused on developing SDR-based prototypes for NTNs with adaptations to OAI 4G and 5G protocol stacks, as discussed in Section VI-C. However, to fully unlock the potential of AI in NTN for future 6G networks, the integration of the RIC into these implementations is crucial. This integration is particularly important given that the immense benefits of AI in addressing NTN deployment challenges for future 6G networks are demonstrated in Section V but current 5G networks lack a dedicated interface for applying AI algorithms. By enabling the O-RAN framework with RIC, the deployment of AI algorithms in real NTN networks can be efficiently performed, paving the way for advanced capabilities and improved performance.

5) Practical Implications: The cost limitations on onboard computation, the extreme environmental conditions, and the extensive propagation delays form a multifaceted array of challenges when endeavoring to bring AI-driven NTNs to fruition in anticipation of the forthcoming 6G network era, as elaborated in Section VII. These formidable challenges necessitate the development of innovative, resourceful solutions to ensure superior network performance in practical NTN deployments. Notably, three key factors come to the fore when considering the limitations imposed on AI capabilities for satellites and other NTN platforms: power, bandwidth, security, and physical space. Advancements in miniaturization, secured system design, energy-efficient design principles, and the judicious utilization of available bandwidth resources serve as the driving forces enabling AI technologies within satellitebased NTNs.

# B. Potential Future Studies

In the preceding sections, we have observed how a multitude of ML and DL approaches has played an important role in shaping the trajectory of future NTN-enabled 6G networks. Nonetheless, we have also encountered certain limitations that enforce the requirement for exploring alternative, more efficient methodologies. Furthermore, the integration of AI into NTNs introduces a set of inherent challenges to be addressed carefully. In this section, our attention shifts to these prospective areas of future research, aiming to establish a resilient framework for the forthcoming era of 6G networks powered by AI techniques.

1) Interrelated Issues: Section V sheds light on the interconnected nature of the various issues encountered in NTNs. It is crucial to recognize that addressing a singular problem can serve as an initial step toward resolving larger, more complex challenges inherent in TNTNs. However, when transitioning these solutions into real-world networks, it becomes imperative to acknowledge and account for the intricate interdependencies among various aspects. An illustrative example of such interrelations lies in the dynamic nature of network load status following a user’s attachment to a satellite. In this scenario, integrating resource allocation strategies into the handover decisions can yield enhanced network performance. MIMO systems can be also beneficial for the single-user and multi-user cases for NTNs as in LTE-Advanced [354]. By considering the broader context and understanding how different aspects influence one another, we can develop more holistic and effective approaches for realworld NTN implementations.

2) Recurrent Learning Architectures: Presently, the majority of DL algorithms deployed to tackle the time-varying nature of NTNs in beam-hopping, resource allocation, network slicing, etc. rely on feed-forward NNs. While these architectures have proven successful in computer vision applications such as image detection and classification, they may not effectively capture the temporal behavior inherent in these NTN problems. Unlike feed-forward networks, recurrent architectures possess the ability to capture and process temporal dependencies within the problem domain. By leveraging RNNs or other similar architectures, we can effectively model and solve the corresponding NTN challenges in a more comprehensive and accurate manner. In particular, for dynamic spectrum access and sharing approaches low complexity NN architectures such as ESNs can be very useful for NTNs as illustrated in [355], [356].

3) Online Implementation: One major limitation of the current works in the domain is the limited consideration given to online implementation and the associated computational complexity when designing algorithms for various control operations in NTNs. This oversight poses a significant hurdle to the practical application of these algorithms in real NTNs as many control decisions in NTN systems must be made in realtime, and the use of complex deep feed-forward NNs becomes impractical. To address this challenge, exploring alternative options becomes imperative. One such option involves investigating low-complexity architectures such as ESNs and ELMs or combining them with traditional feedforward-NNs. These low-complexity architectures offer a more viable solution for online implementation, enabling the deployment of DL algorithms in real NTN networks in a timely and efficient manner.

4) Distributed Learning Models: In the context of integrated satellite-terrestrial networks, the adoption of distributed learning models can significantly enhance scalability. These models involve distributing the training and inference processes of machine learning algorithms across multiple computing nodes, resulting in accelerated computation and improved efficiency. Various distributed approaches, such as data parallelism, model parallelism, ensemble learning, and federated learning, offer promising solutions to address the diverse challenges faced by NTNs in extended network environments [357]. By leveraging these distributed approaches, NTN systems can effectively harness the power of parallel computing and collaborative learning to overcome constraints and achieve optimal performance.

5) Control Feedback Design: One of the major motivating factors for implementing feedback-based learning, such as RL methods, in NTNs, is the inherent feedback system of the

current cellular networks. CSI information is readily available for the BSs which can be helpful in network optimization approaches. However, with the emergence of NTNs, new challenges arise, necessitating the efficient design of feedback mechanisms to minimize the overall overhead while improving network performance. This consideration is crucial, as AI approaches for addressing various issues may require similar types of feedback. The utilization of combined feedback can prove highly beneficial in optimizing network performance and achieving efficient resource allocation, thus enhancing the overall effectiveness of AI algorithms in NTNs.

6) Development in Miniaturization: The limited availability of computational resources currently poses a challenge to the onboard capability of satellites, especially when deploying AI algorithms. However, the miniaturization of satellite components and equipment has emerged as a solution to this issue. By reducing the weight and size of equipment, miniaturization enables the integration of more powerful processors and larger memory devices within the limited space available on satellites. This advancement in computational resources greatly facilitates the deployment of AI algorithms, unlocking new possibilities for satellite applications. Achieving miniaturization in satellite technology requires innovations in material science, efficient Integrated Circuit (IC) design, advancements in IC fabrication technologies, System-on-Chip (SoC) integration, and Micro-Electro-Mechanical Systems (MEMS) design, among others. The development of miniaturization is particularly crucial for NTNs, as it enhances the onboard capability of satellites and enables the realization of advanced technologies and functionalities in space-based systems.

7) Energy Efficiency: The launching and maintenance of satellites require substantial power consumption, which imposes limitations on the onboard capability of satellites. Consequently, efficient energy system design becomes a critical criterion for NTNs. To address this, various aspects need to be considered, including lightweight component design, advanced power management techniques, efficient power conversion, optimized propulsion system design, effective energy storage systems, etc. By focusing on these factors, satellite systems can achieve higher energy efficiency, which is essential for the successful deployment of advanced AI algorithms. The performance of these algorithms relies on the availability of computational resources, making energy efficiency a crucial aspect to maximize the satellite’s capabilities within the given power constraints.

8) Secured System Design: As highlighted in Section VII, security concerns in NTNs can be highly significant, introducing new attack vectors and vulnerabilities. NTNs are susceptible to a range of security attacks, including adversarial attacks, data poisoning, DoS attacks, Fuzzy attacks, MiM attacks, and more. These attacks have the potential to severely impact network performance and compromise the integrity and confidentiality of data. To address these challenges, it is essential to design efficient intrusion detection and prevention systems specifically tailored for secure NTNs. By continuously monitoring a set of relevant network parameters and detecting anomalies in the network’s behavioral patterns, mitigation techniques can be promptly deployed to ensure optimal network performance and safeguard against potential degradation caused by security breaches.

# IX. CONCLUSION

NTN is considered the driver of ubiquitous, reliable, and scalable 6G wireless networks. It adds new dimensions to the existing traditional terrestrial communication systems by providing connections to remote and isolated areas subject to geographical constraints and offloading the primary links during traffic peaks. However, diverse unique challenges are accompanied by the deployment of NTN in existing communication systems. The long propagation delay, high Doppler effect, spectrum sharing, complicated resource allocation, and fast and frequent handover are the major problems associated with NTN deployment. Integration to existing terrestrial networks presents a set of new problems such as task offloading, network routing, network slicing, etc. to be addressed in an efficient manner. The convergence of AI and NTN allows for the building of sustainable AI-based Non-Terrestrial Networks addressing many of these challenges. Depending on the characteristics of the problem at hand, various learning approaches can be employed. When dealing with prediction and estimation problems, SL techniques appear to be a more suitable choice. On the other hand, for tasks involving closed-loop control, RL techniques show greater promise. By tailoring the learning approach to the specific problem, we can effectively leverage the strengths of each technique and achieve optimal results.

However, the integration of AI into NTNs presents certain challenges that need to be addressed. Both the industry and research community are collaborating to ensure the successful implementation of AI-based NTNs in next-generation wireless networks. This includes the establishment of ML testbeds specifically designed for satellite networks and the adaptation of SDR-based OAI 4G/5G protocol stacks for NTN applications. In order to realize satellite-based NTNs in future 6G networks, several practical challenges must be overcome. These challenges include addressing the constraints of cost-limited onboard capabilities, managing the highly time-varying nature of satellite networks, and mitigating the effects of long propagation delays. It is important to consider these interconnected issues and develop joint solutions to enhance overall network performance. Furthermore, exploring low-complexity and distributed learning architectures that incorporate efficient control feedback mechanisms is essential for enabling real-time, online implementation. Additionally, ensuring the secure, compact, and energy-efficient design of NTN platforms is integral to the successful deployment of satellite-based NTNs in the 6G era.

# REFERENCES

[1] I. Rahman et al., “5G evolution toward 5G advanced: An overview of 3GPP releases 17 and 18,” Ericsson Technol. Rev., vol. 2021, no. 14, pp. 2–12, 2021.   
[2] X. Lin, “An overview of 5G advanced evolution in 3GPP release 18,” IEEE Commun. Stand. Mag., vol. 6, no. 3, pp. 77–83, Sep. 2022.   
[3] J. Pang et al., “A new 5G radio evolution towards 5G-advanced,” Sci. China Inf. Sci., vol. 65, no. 9, 2022, Art. no. 191301.

[4] W. Jiang, B. Han, M. A. Habibi, and H. D. Schotten, “The road towards 6G: A comprehensive survey,” IEEE Open J. Commun. Soc., vol. 2, pp. 334–366, 2021.   
[5] W. Chen et al., “5G-advanced towards 6G: Past, present, and future,” IEEE J. Sel. Areas Commun., vol. 41, no. 6, pp. 1592–1619, Jun. 2023.   
[6] “6G: The next horizon.” Accessed: Nov. 2021. [Online]. Available: https://www.huawei.com/en/huaweitech/future-technologies/6g-thenext-horizon   
[7] “6G—Connecting a cyber-physical world.” Accessed: Feb. 2022. [Online]. Available: https://www.ericsson.com/en/reports-and-papers/ white-papers/a-research-outlook-towards-6g   
[8] “Samsung 6G white paper: The next hyper-connected experience for all.” 2020. [Online]. Available: https://research.samsung.com/nextgeneration-communications   
[9] M. Z. Chowdhury, M. Shahjalal, S. Ahmed, and Y. M. Jang, “6G wireless communication systems: Applications, requirements, technologies, challenges, and research directions,” IEEE Open J. Commun. Soc., vol. 1, pp. 957–975, 2020.   
[10] P. Yang, Y. Xiao, M. Xiao, and S. Li, “6G wireless communications: Vision and potential techniques,” IEEE Netw., vol. 33, no. 4, pp. 70–75, Jul./Aug. 2019.   
[11] Z. Zhang et al., “6G wireless networks: Vision, requirements, architecture, and key technologies,” IEEE Veh. Technol. Mag., vol. 14, no. 3, pp. 28–41, Sep. 2019.   
[12] X. Lin, S. Cioni, G. Charbit, N. Chuberre, S. Hellsten, and J.-F. Boutillon, “On the path to 6G: Embracing the next wave of low earth orbit satellite access,” IEEE Commun. Mag., vol. 59, no. 12, pp. 36–42, Dec. 2021.   
[13] M. Giordani and M. Zorzi. “Non-terrestrial communication in the 6G era: Challenges and opportunities.” 2019. [Online]. Available: http://arxiv.org/abs/1912.10226   
[14] M. Bacco et al., “Networking challenges for non-terrestrial networks exploitation in 5G,” in Proc. IEEE 2nd 5G World Forum (5GWF), 2019, pp. 623–628.   
[15] Y. Lu, “Artificial intelligence: A survey on evolution, models, applications and future trends,” J. Manag. Anal., vol. 6, no. 1, pp. 1–29, 2019. [Online]. Available: https://doi.org/10.1080/23270012.2019.1570365   
[16] J. G. Carbonell, R. S. Michalski, and T. M. Mitchell, “1—An overview of machine learning,” in Machine Learning, R. S. Michalski, J. G. Carbonell, and T. M. Mitchell, Eds. San Francisco, CA, USA: Morgan Kaufmann, 1983, pp. 3–23. [Online]. Available: https://www. sciencedirect.com/science/article/pii/B9780080510545500054   
[17] S. Dong, P. Wang, and K. Abbas, “A survey on deep learning and its applications,” Comput. Sci. Rev., vol. 40, May 2021, Art. no. 100379. [Online]. Available: https://www.sciencedirect.com/science/article/pii/ S1574013721000198   
[18] C.-X. Wang, M. D. Renzo, S. Stanczak, S. Wang, and E. G. Larsson, “Artificial intelligence enabled wireless networking for 5G and beyond: Recent advances and future challenges,” IEEE Wireless Commun. Mag., vol. 27, no. 1, pp. 16–23, Feb. 2020.   
[19] X. Lin, S. Rommer, S. Euler, E. A. Yavuz, and R. S. Karlsson, “5G from space: An overview of 3GPP non-terrestrial networks,” IEEE Commun. Stand. Mag., vol. 5, no. 4, pp. 147–153, 2021.   
[20] “Study on new radio (NR) to support non-terrestrial networks,” 3GPP, Sophia Antipolis, France, Rep. TR 38.811, Sep. 2020. [Online]. Available: https://www.3gpp.org/ftp//Specs/archive/38\_series/38.811/   
[21] L. C. Alexandre, A. Linhares, G. Neto, and A. C. Sodre, “Highaltitude platform stations as IMT base stations: Connectivity from the stratosphere,” Commun. Mag., vol. 59, no. 12, pp. 30–35, Dec. 2021. [Online]. Available: https://doi.org/10.1109/MCOM.001.2100477   
[22] Hexa-X. “Final 6G architectural enablers and technological solutions.” Apr. 2023. [Online]. Available: https://hexa-x.eu/wp-content/uploads/ 2023/08/Hexa-X\_D5.3\_v1.1.pdf   
[23] “Summary of rel-17 work items,” 3GPP, Sophia Antipolis, France, Rep. TR 21.917, Jan. 2023. [Online]. Available: https://www.3gpp.org/ftp/ Specs/archive/23\_series/23.917/   
[24] N. Cassiau et al., “Satellite and terrestrial multi-connectivity for 5G: Making spectrum sharing possible,” in Proc. IEEE Wireless Commun. Netw. Conf. Workshops (WCNCW), 2020, pp. 1–6.   
[25] H. Friis, “A note on a simple transmission formula,” Proc. IRE, vol. 34, no. 5, pp. 254–256, 1946.   
[26] J. Salo, L. Vuokko, H. El-Sallabi, and P. Vainikainen, “Shadow fading revisited,” in Proc. IEEE 63rd Veh. Techn. Conf., vol. 6, 2006, pp. 2843–2847.

[27] “Attenuation by atmospheric gases and related effects,” Int. Telecommun. Union, Geneva, Switzerland, ITU Recommendation ITU-R P.676-13, Aug. 2022. [Online]. Available: https://www.itu.int/rec/R-REC-P.676-13-202208-I/en   
[28] “Attenuation due to clouds and fog,” Int. Telecommun. Union, Geneva, Switzerland, ITU Recommendation ITU-R P.840-8, Aug. 2019. [Online]. Available: https://www.itu.int/rec/R-REC-P.840-8-201908-I/ en   
[29] “Ionospheric propagation data and prediction methods required for the design of satellite networks and systems,” Int. Telecommun. Union, Geneva, Switzerland, ITU Recommendation ITU-R P.531-14, Aug. 2019. [Online]. Available: https://www.itu.int/rec/R-REC-P.531- 14-201908-I/en   
[30] “Propagation data required for the design systems in the land mobilesatellite service,” Int. Telecommun. Union, Geneva, Switzerland, ITU Recommendation ITU-R P.681-11, Aug. 2019. [Online]. Available: https://www.itu.int/rec/R-REC-P.681-11-201908-I/en   
[31] “Solutions for NR to support non-terrestrial networks (NTN),” 3GPP, Sophia Antipolis, France, Rep. TR 38.821, Jan. 2020. [Online]. Available: https://www.3gpp.org/ftp//Specs/archive/38\_series/38.821/   
[32] A. L. Samuel, “Some studies in machine learning using the game of checkers,” IBM J. Res. Dev., vol. 3, no. 3, pp. 210–229, 1959.   
[33] T. Mitchell, Machine Learning, 1st ed. New York, NY, USA: McGraw-Hill, 1997. [Online]. Available: https://www.cs.cmu.edu/\~tom/mlbook. html   
[34] C. M. Bishop, “Neural networks application,” Rev. Sci. Instrum., vol. 65, no. 6, pp. 1803–1832, 1994.   
[35] R. Rojas, “The backpropagation algorithm,” in Neural Networks. Heidelberg, Germany: Springer, 1996, pp. 149–182.   
[36] S. Boyd, S. P. Boyd, and L. Vandenberghe, Convex Optimization. Cambridge, U.K.: Cambridge Univ. Press, 2004.   
[37] S.-I. Amari, “Backpropagation and stochastic gradient descent method,” Neurocomputing, vol. 5, nos. 4–5, pp. 185–196, 1993.   
[38] J. Konecnˇ y, J. Liu, P. Richtárik, and M. Taká \` c, “Mini-batch semi- ˇ stochastic gradient descent in the proximal setting,” IEEE J. Sel. Topics Signal Process., vol. 10, no. 2, pp. 242–255, Mar. 2016.   
[39] J. J. Moré and D. C. Sorensen, Newton’s Method, Argonne Nat. Lab., Lemont, IL, USA, 1982.   
[40] I. Muhammad and Z. Yan, “Supervised machine learning approaches: A survey,” ICTACT J. Soft Comput., vol. 5, no. 3, p. 125, 2015.   
[41] R. J. Freund, Regression Analysis: Statistical Modeling of a Response Variable, 2nd ed. Hoboken, NJ, USA: Wiley, 2006.   
[42] J. Groß, Linear Regression, vol. 175, Berlin, Germany: Springer, 2003.   
[43] R. E. Wright, Logistic Regression. Washington, DC, USA: Amer. Psychol. Assoc., 1995.   
[44] C. Kingsford and S. L. Salzberg, “What are decision trees?” Nat. Biotechnol., vol. 26, no. 9, pp. 1011–1013, 2008.   
[45] K. M. Leung, “Naive Bayesian classifier,” Finance Risk Eng., vol. 2007, pp. 123–156, May 2007.   
[46] M. A. Hearst, S. T. Dumais, E. Osuna, J. Platt, and B. Scholkopf, “Support vector machines,” IEEE Intell. Syst. Appl., vol. 13, no. 4, pp. 18–28, Jul./Aug. 1998.   
[47] F. Rosenblatt, “The perceptron: A probabilistic model for information storage and organization in the brain,” Psychol. Rev., vol. 65, no. 6, p. 386, 1958.   
[48] G.-B. Huang, Q.-Y. Zhu, and C.-K. Siew, “Extreme learning machine: Theory and applications,” Neurocomputing, vol. 70, nos. 1–3, pp. 489–501, 2006.   
[49] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit., 2016, pp. 770–778.   
[50] D. F. Specht, “Probabilistic neural networks,” Neural Netw., vol. 3, no. 1, pp. 109–118, 1990.   
[51] Y. LeCun et al., “Convolutional networks for images, speech, and time series,” Handbook Brain Theory Neural Netw., vol. 3361, no. 10, p. 1995, 1995.   
[52] M. D. Zeiler, D. Krishnan, G. W. Taylor, and R. Fergus, “Deconvolutional networks,” in Proc. IEEE Comput. Soc. Conf. Comput. Vis. Pattern Recognit, 2010, pp. 2528–2535.   
[53] L. R. Medsker and L. Jain, “Recurrent neural networks,” Des. Appl., vol. 5, no. 1, pp. 64–67, 2001.   
[54] R. Pascanu, T. Mikolov, and Y. Bengio, “On the difficulty of training recurrent neural networks,” in Proc. Int. Conf. Mach. Learn, 2013, pp. 1310–1318.   
[55] K. Cho, B. Van Merriënboer, D. Bahdanau, and Y. Bengio, “On the properties of neural machine translation: Encoder–decoder approaches,” 2014, arXiv:1409.1259.

[56] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural Comput., vol. 9, no. 8, pp. 1735–1780, 1997.   
[57] B. Schrauwen, D. Verstraeten, and J. Van Campenhout, “An overview of reservoir computing: Theory, applications and implementations,” in Proc. 15th Eur. Symp. Artif. Neural Netw., 2007, pp. 471–482.   
[58] A. Vaswani et al., “Attention is all you need,” in Proc. Adv. Neural Inf. Process. Syst., vol. 30, 2017, pp. 1–8. [Online]. Available: https: //proceedings.neurips.cc/   
[59] T. Hastie, R. Tibshirani, and J. Friedman, “Unsupervised learning,” in The Elements of Statistical Learning. Springer Series in Statistics. New York, NY, USA: Springer, 2009, pp. 485–585.   
[60] H. Abdi and L. J. Williams, “Principal component analysis,” Wiley Interdiscipl. Rev. Comput. Stat., vol. 2, no. 4, pp. 433–459, 2010.   
[61] J. M. Kleinberg, R. Kumar, P. Raghavan, S. Rajagopalan, and A. S. Tomkins, “The Web as a graph: Measurements, models, and methods,” in Proc. 5th Annu. Int. Conf. Comput. Comb. (COCOON), Jul. 1999, pp. 1–17.   
[62] D. Steinley, “K-means clustering: A half-century synthesis,” Brit. J. Math. Stat. Psychol., vol. 59, no. 1, pp. 1–34, 2006.   
[63] H.-S. Park and C.-H. Jun, “A simple and fast algorithm for K-medoids clustering,” Exp. Syst. Appl., vol. 36, no. 2, pp. 3336–3341, 2009.   
[64] D. A. Reynolds et al., “Gaussian mixture models,” Encyclopedia of Biometrics, vol. 741. Boston, MA, USA: Springer, 2009.   
[65] T. Cover and P. Hart, “Nearest neighbor pattern classification,” IEEE Trans. Inf. Theory, vol. IT-13, no. 1, pp. 21–27, Jan. 1967.   
[66] P. Baldi, “Autoencoders, unsupervised learning and deep architectures,” in Proc. Int. Conf. Unsupervised Transfer Learn. Workshop, vol. 27, 2011, pp. 37–50.   
[67] D. P. Kingma and M. Welling, “Auto-encoding variational Bayes,” 2013, arXiv:1312.6114.   
[68] P. Vincent, H. Larochelle, Y. Bengio, and P.-A. Manzagol, “Extracting and composing robust features with denoising autoencoders,” in Proc. 25th Int. Conf. Mach. Learn., 2008, pp. 1096–1103.   
[69] M. Ranzato, C. Poultney, S. Chopra, and Y. Cun, “Efficient learning of sparse representations with an energy-based model,” in Proc. Adv. Neural Inf. Process. Syst., vol. 19, 2006, pp. 1137–1144.   
[70] G. E. Hinton, S. Osindero, and Y.-W. Teh, “A fast learning algorithm for deep belief nets,” Neural Comput., vol. 18, no. 7, pp. 1527–1554, 2006.   
[71] Y. Bengio, P. Lamblin, D. Popovici, and H. Larochelle, “Greedy layerwise training of deep networks,” in Proc. Adv. Neural Inf. Process. Syst., vol. 19, 2006, pp. 153–160.   
[72] G. E. Hinton and R. R. Salakhutdinov, “Reducing the dimensionality of data with neural networks,” Science, vol. 313, no. 5786, pp. 504–507, 2006.   
[73] H. Lee, R. Grosse, R. Ranganath, and A. Y. Ng, “Convolutional deep belief networks for scalable unsupervised learning of hierarchical representations,” in Proc. 26th Annu. Int. Conf. Mach. Learn., 2009, pp. 609–616. [Online]. Available: https://doi.org/10. 1145/1553374.1553453   
[74] J. J. Hopfield, “Neural networks and physical systems with emergent collective computational abilities,” Proc. Nat. Acad. Sci. USA, vol. 79, no. 8, pp. 2554–2558, 1982.   
[75] G. E. Hinton, T. J. Sejnowski, and D. H. Ackley, Boltzmann Machines: Constraint Satisfaction Networks That Learn. Dep. Comput. Sci., Carnegie-Mellon Univ., Pittsburgh, PA, USA, 1984.   
[76] R. Salakhutdinov and G. Hinton, “Deep Boltzmann machines,” in Proc. Artif. Intell. Stat., 2009, pp. 448–455.   
[77] T. Kohonen, “The self-organizing map,” Proc. IEEE, vol. 78, no. 9, pp. 1464–1480, Sep. 1990.   
[78] A. Creswell, T. White, V. Dumoulin, K. Arulkumaran, B. Sengupta, and A. A. Bharath, “Generative adversarial networks: An overview,” IEEE Signal Process. Mag., vol. 35, no. 1, pp. 53–65, Jan. 2018.   
[79] X. Dong, Z. Yu, W. Cao, Y. Shi, and Q. Ma, “A survey on ensemble learning,” Front. Comput. Sci., vol. 14, no. 2, pp. 241–258, 2020.   
[80] J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli, “Deep unsupervised learning using nonequilibrium thermodynamics,” in Proc. Int. Conf. Mach. Learn., 2015, pp. 2256–2265.   
[81] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” in Proc. Adv. Neural Inf. Process. Syst., vol. 33, 2020, pp. 6840–6851.   
[82] L. P. Kaelbling, M. L. Littman, and A. W. Moore, “Reinforcement learning: A survey,” J. Artif. Intell. Res., vol. 4, pp. 237–285, May 1996.   
[83] M. L. Puterman, “Markov decision processes,” in Handbooks in Operations Research and Management Science, vol. 2. Hoboken, NJ, USA: Wiley, 1990, pp. 331–434.

[84] R. Sutton and A. Barto, “Reinforcement learning: An introduction,” IEEE Trans. Neural Netw., vol. 9, no. 5, pp. 1054–1054, Sep. 1998.   
[85] R. Bellman, “Dynamic programming,” Science, vol. 153, no. 3731, pp. 34–37, 1966.   
[86] N. Metropolis and S. Ulam, “The Monte Carlo method,” J. Amer. Stat. Assoc., vol. 44, no. 247, pp. 335–341, 1949.   
[87] C. J. Watkins and P. Dayan, “Q-learning,” Mach. Learn., vol. 8, no. 3, pp. 279–292, 1992.   
[88] G. A. Rummery and M. Niranjan, On-Line Q-Learning Using Connectionist Systems, vol. 37. Cambridge, U.K.: Univ. Cambridge, 1994.   
[89] L. S. Shapley, “Stochastic games,” Proc. Nat. Acad. Sci. USA, vol. 39, no. 10, pp. 1095–1100, 1953.   
[90] J. Hu and M. P. Wellman, “Nash Q-learning for general-sum stochastic games,” J. Mach. Learn. Res., vol. 4, pp. 1039–1069, Nov. 2003.   
[91] R. S. Sutton, D. McAllester, S. Singh, and Y. Mansour, “Policy gradient methods for reinforcement learning with function approximation,” in Proc. Adv. Neural Inf. Process. Syst., vol. 12, 1999, pp. 1057–1063.   
[92] D. Silver, G. Lever, N. Heess, T. Degris, D. Wierstra, and M. Riedmiller, “Deterministic policy gradient algorithms,” in Proc. Int. Conf. Mach. Learn, 2014, pp. 387–395.   
[93] V. Konda and J. Tsitsiklis, “Actor–critic algorithms,” in Proc. Adv. Neural Inf. Process. Syst., vol. 12, 1999, pp. 1–8.   
[94] V. Mnih et al., “Human-level control through deep reinforcement learning,” Nature, vol. 518, no. 7540, pp. 529–533, 2015.   
[95] H. Hasselt, “Double Q-learning,” in Proc. Adv. Neural Inf. Process. Syst., vol. 23, 2010, pp. 1–9.   
[96] H. Van Hasselt, A. Guez, and D. Silver, “Deep reinforcement learning with double Q-learning,” in Proc. AAAI Conf. Artif. Intell., vol. 30, 2016, pp. 2094–2100.   
[97] Z. Wang, T. Schaul, M. Hessel, H. Hasselt, M. Lanctot, and N. Freitas, “Dueling network architectures for deep reinforcement learning,” in Proc. Int. Conf. Mach. Learn, 2016, pp. 1995–2003.   
[98] M. G. Bellemare, W. Dabney, and R. Munos, “A distributional perspective on reinforcement learning,” in Proc. Int. Conf. Mach. Learn., 2017, pp. 449–458.   
[99] T. P. Lillicrap et al., “Continuous control with deep reinforcement learning,” 2015, arXiv:1509.02971.   
[100] M. Hausknecht and P. Stone, “Deep recurrent Q-learning for partially observable MDPs,” in Proc. AAAI Fall Symp., 2015, pp. 29–37.   
[101] J. Konecnˇ y, H. B. McMahan, F. X. Yu, P. Richtárik, A. T. Suresh, and \` D. Bacon, “Federated learning: Strategies for improving communication efficiency,” 2016, arXiv:1610.05492.   
[102] O. Gupta and R. Raskar, “Distributed learning of deep neural network over multiple agents,” J. Netw. Comput. Appl., vol. 116, pp. 1–8, Aug. 2018.   
[103] P. Vepakomma, O. Gupta, T. Swedish, and R. Raskar, “Split learning for health: Distributed deep learning without sharing raw patient data,” 2018, arXiv:1812.00564.   
[104] A. Singh, P. Vepakomma, O. Gupta, and R. Raskar, “Detailed comparison of communication efficiency of split learning and federated learning,” 2019, arXiv:1909.09145.   
[105] C. Thapa, P. C. M. Arachchige, S. Camtepe, and L. Sun, “SplitFed: When federated learning meets split learning,” in Proc. AAAI Conf. Artif. Intell., vol. 36, 2022, pp. 8485–8493.   
[106] B. A. Homssi et al., “Artificial intelligence techniques for nextgeneration mega satellite networks,” 2022, arXiv:2207.00414.   
[107] S. Saafi, O. Vikhrova, G. Fodor, J. Hosek, and S. Andreev, “AI-aided integrated terrestrial and non-terrestrial 6G solutions for sustainable maritime networking,” IEEE Netw., vol. 36, no. 3, pp. 183–190, May/Jun. 2022.   
[108] R. Alegre, N. S. Alagha, and M. A. Vázquez-Castro, “Heuristic algorithms for flexible resource allocation in beam hopping multi-beam satellite systems,” in Proc. 29th AIAA Int. Commun. Satellite Syst. Conf. (ICSSC), 2011, pp. 1–8.   
[109] G. Zheng, S. Chatzinotas, and B. Ottersten, “Generic optimization of linear precoding in multibeam satellite systems,” IEEE Trans. Wireless Commun., vol. 11, no. 6, pp. 2308–2320, Jun. 2012.   
[110] L. Lei, E. Lagunas, Y. Yuan, M. G. Kibria, S. Chatzinotas, and B. Ottersten, “Deep learning for beam hopping in multibeam satellite systems,” in Proc. IEEE 91st Veh. Tech. Conf. (VTC-Spring), 2020, pp. 1–5.   
[111] L. Lei, E. Lagunas, Y. Yuan, M. G. Kibria, S. Chatzinotas, and B. Ottersten, “Beam illumination pattern design in satellite networks: Learning and optimization for efficient beam hopping,” IEEE Access, vol. 8, pp. 136655–136667, 2020.

[112] S. Amiri and M. Mehdipour, “Accurate doppler frequency shift estimation for any satellite orbit,” in Proc. 3rd Int. Conf. Recent Adv. Space Technol., 2007, pp. 602–607.   
[113] T. Kim, K. Ko, I. Hwang, D. Hong, S. Choi, and H. Wang, “RSRPbased doppler shift estimator using machine learning in high-speed train systems,” IEEE Trans. Veh. Technol., vol. 70, no. 1, pp. 371–380, Jan. 2021.   
[114] W. Usaha and J. A. Barria, “Reinforcement learning for resource allocation in LEO satellite networks,” IEEE Trans. Syst. Man, Cybern. B, Cybern., vol. 37, no. 3, pp. 515–527, Jun. 2007.   
[115] O. Kodheli et al., “Satellite communications in the new space era: A survey and future challenges,” IEEE Commun. Surveys Tuts., vol. 23, no. 1, pp. 70–109, 1st Quart., 2021.   
[116] X. Zhu and C. Jiang, “Integrated satellite-terrestrial networks toward 6G: Architectures, applications, and challenges,” IEEE Internet Things J., vol. 9, no. 1, pp. 437–461, Jan. 2021.   
[117] G. Araniti, A. Iera, S. Pizzi, and F. Rinaldi, “Toward 6G non-terrestrial networks,” IEEE Netw., vol. 36, no. 1, pp. 113–120, Jan./Feb. 2022.   
[118] G. Geraci, D. Lopez-Perez, M. Benzaghta, and S. Chatzinotas, “Integrating terrestrial and non-terrestrial networks: 3D opportunities and challenges,” IEEE Commun. Mag., vol. 61, no. 4, pp. 42–48, Apr. 2023.   
[119] M. M. Azari et al., “Evolution of non-terrestrial networks from 5G to 6G: A survey,” IEEE Commun. Surveys Tuts., vol. 24, no. 4, pp. 2633–2672, 4th Quart., 2022.   
[120] H. Al-Hraishawi, H. Chougrani, S. Kisseleff, E. Lagunas, and S. Chatzinotas, “A survey on nongeostationary satellite systems: The communication perspective,” IEEE Commun. Surveys Tuts., vol. 25, no. 1, pp. 101–132, 1st Quart., 2023.   
[121] S. Zhang and D. Zhu, “Towards artificial intelligence enabled 6G: State of the art, challenges, and opportunities,” Comput. Netw., vol. 183, Dec. 2020, Art. no. 107556.   
[122] W. Guo, “Explainable artificial intelligence for 6G: Improving trust between human and machine,” IEEE Commun. Mag., vol. 58, no. 6, pp. 39–45, Jun. 2020.   
[123] H. Yang, A. Alphones, Z. Xiong, D. Niyato, J. Zhao, and K. Wu, “Artificial-intelligence-enabled intelligent 6G networks,” IEEE Netw., vol. 34, no. 6, pp. 272–280, Nov./Dec. 2020.   
[124] K. B. Letaief, Y. Shi, J. Lu, and J. Lu, “Edge artificial intelligence for 6G: Vision, enabling technologies, and applications,” IEEE J. Sel. Areas Commun., vol. 40, no. 1, pp. 5–36, Jan. 2022.   
[125] M. R. Mahmood, M. A. Matin, P. Sarigiannidis, and S. K. Goudos, “A comprehensive review on artificial intelligence/machine learning algorithms for empowering the future IoT toward 6G era,” IEEE Access, vol. 10, pp. 87535–87562, 2022.   
[126] T. B. Ahammed, R. Patgiri, and S. Nayak, “A vision on the artificial intelligence for 6G communication,” ICT Exp., vol. 9, no. 2, pp. 197–210, 2023.   
[127] N. Kato et al., “Optimizing space-air-ground integrated networks by artificial intelligence,” IEEE Wireless Commun. Mag., vol. 26, no. 4, pp. 140–147, Aug. 2019.   
[128] E. T. Michailidis, S. M. Potirakis, and A. G. Kanatas, “AI-inspired non-terrestrial networks for IIoT: Review on enabling technologies and applications,” Internet Things, vol. 1, no. 1, p. 3, 2020.   
[129] F. Fourati and M.-S. Alouini, “Artificial intelligence for satellite communication: A review,” Intell. Converg. Netw., vol. 2, no. 3, pp. 213–243, 2021.   
[130] R. Giuliano and E. Innocenti, “Machine learning techniques for nonterrestrial networks,” Electronics, vol. 12, no. 3, p. 652, 2023.   
[131] T. Naous, M. Itani, M. Awad, and S. Sharafeddine, “Reinforcement learning in the sky: A survey on enabling intelligence in NTNbased communications,” IEEE Access, vol. 11, pp. 19941–19968, 2023.   
[132] A. Bhattacharyya, S. M. Nambiar, R. Ojha, A. Gyaneshwar, U. Chadha, and K. Srinivasan, “Machine learning and deep learning powered satellite communications: Enabling technologies, applications, open challenges, and future research directions,” Int. J. Satellite Commun. Netw., vol. 41, no. 6, pp. 539–588, 2023. [Online]. Available: https: //onlinelibrary.wiley.com/doi/abs/10.1002/sat.1482   
[133] F. Rinaldi et al., “Non-terrestrial networks in 5G & beyond: A survey,” IEEE Access, vol. 8, pp. 165178–165200, 2020.   
[134] A. Vanelli-Coralli, A. Guidotti, T. Foggi, G. Colavolpe, and G. Montorsi, “5G and beyond 5G non-terrestrial networks: Trends and research challenges,” in Proc. IEEE 3rd 5G World Forum (5GWF), 2020, pp. 163–169.

[135] S. Zhang, D. Zhu, and Y. Wang, “A survey on space-aerialterrestrial integrated 5G networks,” Comput. Netw., vol. 174, Jun. 2020, Art. no. 107212. [Online]. Available: https://www.sciencedirect.com/ science/article/pii/S1389128619314045   
[136] A. Feriani and E. Hossain, “Single and multi-agent deep reinforcement learning for AI-enabled wireless networks: A tutorial,” IEEE Commun. Surveys Tuts., vol. 23, no. 2, pp. 1226–1252, 2nd Quart., 2021.   
[137] M. Elsayed and M. Erol-Kantarci, “AI-enabled future wireless networks: Challenges, opportunities, and open issues,” IEEE Veh. Technol. Mag., vol. 14, no. 3, pp. 70–77, Sep. 2019.   
[138] D. C. Nguyen et al., “Enabling AI in future wireless networks: A data life cycle perspective,” IEEE Commun. Surveys Tuts., vol. 23, no. 1, pp. 553–595, 1st Quart., 2021.   
[139] C. Li, Z. Cao, and Y. Liu, “Deep AI enabled ubiquitous wireless sensing: A survey,” ACM Comput. Surveys, vol. 54, no. 2, pp. 1–35, 2021.   
[140] K. B. Letaief, W. Chen, Y. Shi, J. Zhang, and Y.-J. A. Zhang, “The roadmap to 6G: AI empowered wireless networks,” IEEE Commun. Mag., vol. 57, no. 8, pp. 84–90, Aug. 2019.   
[141] R. Shafin, L. Liu, V. Chandrasekhar, H. Chen, J. Reed, and J. C. Zhang, “Artificial intelligence-enabled cellular networks: A critical path to beyond-5G and 6G,” IEEE Wireless Commun. Mag., vol. 27, no. 2, pp. 212–217, Apr. 2020.   
[142] S. Jere, Y. Song, Y. Yi, and L. Liu, “Distributed learning meets 6G: A communication and computing perspective,” IEEE Wireless Commun., vol. 30, no. 1, pp. 112–117, Feb. 2023.   
[143] X. Shen, J. Gao, W. Wu, M. Li, C. Zhou, and W. Zhuang, “Holistic network Virtualization and pervasive network intelligence for 6G,” IEEE Commun. Surveys Tuts., vol. 24, no. 1, pp. 1–30, 1st Quart., 2022.   
[144] B. Mao, F. Tang, Y. Kawamoto, and N. Kato, “AI models for green communications towards 6G,” IEEE Commun. Surveys Tuts., vol. 24, no. 1, pp. 210–247, 1st Quart., 2022.   
[145] Y. Sun, J. Liu, J. Wang, Y. Cao, and N. Kato, “When machine learning meets privacy in 6G: A survey,” IEEE Commun. Surveys Tuts., vol. 22, no. 4, pp. 2694–2724, 4th Quart., 2020.   
[146] Z. M. Fadlullah, B. Mao, and N. Kato, “Balancing QoS and security in the edge: Existing practices, challenges, and 6G opportunities with machine learning,” IEEE Commun. Surveys Tuts., vol. 24, no. 4, pp. 2419–2448, 4th Quart., 2022.   
[147] F. Tang, B. Mao, Y. Kawamoto, and N. Kato, “Survey on machine learning for intelligent end-to-end communication toward 6G: From network access, routing to traffic control and streaming adaption,” IEEE Commun. Surveys Tuts., vol. 23, no. 3, pp. 1578–1598, 3rd Quart., 2021.   
[148] Y. Zhang, A. Liu, P. Li, and S. Jiang, “Deep learning (DL)- based channel prediction and hybrid beamforming for LEO satellite massive MIMO system,” IEEE Internet Things J., vol. 9, no. 23, pp. 23705–23715, Dec. 2022.   
[149] Y. Zhang, Y. Wu, A. Liu, X. Xia, T. Pan, and X. Liu, “Deep learning-based channel prediction for LEO satellite massive MIMO communication system,” IEEE Wireless Commun. Lett., vol. 10, no. 8, pp. 1835–1839, Aug. 2021.   
[150] M. J. Kang, J. H. Lee, and S. H. Chae, “Channel estimation with DnCNN in massive MISO LEO satellite systems,” in Proc. 14th Int. Conf. Ubiquitous Future Netw. (ICUFN), 2023, pp. 825–827.   
[151] G.-Y. Chang, C.-K. Hung, and C.-H. Chen, “A CSI prediction scheme for satellite-terrestrial networks,” IEEE Internet Things J., vol. 10, no. 9, pp. 7774–7785, May 2023.   
[152] R. Guo, K. Wang, Z. Deng, W. Lin, and R. Song, “A prediction model for channel state information in satellite communication system,” in Proc. IEEE 31st Annu. Int. Symp. Pers. Indoor Mobile Radio Commun., 2020, pp. 1–6.   
[153] K. Tekbıyık, G. K. Kurt, A. R. Ekti, and H. Yanikomeroglu. “Graph attention networks for channel estimation in RIS-assisted satellite IoT communications.” 2022. [Online]. Available: https://arxiv.org/abs/2104. 00735   
[154] X. Wang, H. Li, and Q. Wu, “Optimizing adaptive coding and modulation for satellite network with ML-based CSI prediction,” in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), 2019, pp. 1–6.   
[155] M. K. Shehzad, L. Rose, and M. Assaad, “RNN-based twin channel predictors for CSI acquisition in UAV-assisted 5G+ networks,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), 2021, pp. 1–6.   
[156] L. Bai, C.-X. Wang, Q. Xu, S. Ventouras, and G. Goussetis, “Prediction of channel excess attenuation for satellite communication systems at Q-band using artificial neural network,” IEEE Antennas Wireless Propag. Lett., vol. 18, no. 11, pp. 2235–2239, Nov. 2019.

[157] F. Ortiz et al., “Onboard processing in satellite communications using AI accelerators,” Aerospace, vol. 10, no. 2, p. 101, 2023.   
[158] E. Yoon, S. Kwon, U. Yun, and S.-Y. Kim, “Doppler spread estimation based on machine learning for an OFDM system,” Wireless Commun. Mobile Comput., vol. 2021, Sep. 2021, Art. no. 5586029.   
[159] T. Ngo, B. T. Kelley, and P. Rad, “Deep learning based prediction of doppler shift for mobile communications,” in Proc. Telecoms Conf. (ConfTELE), 2021, pp. 1–6.   
[160] S. Kim, J. Park, and C. Lee, “CNN-based doppler shift estimation for low earth orbit satellites,” in Proc. 37th Int. Tech. Conf. Circuits Syst. Comput. Commun. (ITC-CSCC), 2022, pp. 1–3.   
[161] M. Katayama, A. Ogawa, and N. Morinaga, “Carrier synchronization under doppler shift of the nongeostationary satellite communication systems,” in Proc. ICCS/ISITA, 1992, pp. 466–470.   
[162] I. Ali, N. Al-Dhahir, and J. Hershey, “Doppler characterization for LEO satellites,” IEEE Trans. Commun., vol. 46, no. 3, pp. 309–313, Mar. 1998.   
[163] Z. Chenggong, C. Xi, and H. Zhen, “A comprehensive analysis on doppler frequency and doppler frequency rate characterization for GNSS receivers,” in Proc. 2nd IEEE Int. Conf. Comput. Commun. (ICCC), 2016, pp. 2606–2610.   
[164] T. A. Khan and M. Afshang, “A stochastic geometry approach to doppler characterization in a LEO satellite network,” in Proc. IEEE Int. Conf. Commun. (ICC), 2020, pp. 1–6.   
[165] J. Lin, Z. Hou, Y. Zhou, L. Tian, and J. Shi, “Map estimation based on doppler Characterization in broadband and mobile LEO satellite communications,” in Proc. IEEE 83rd Veh. Tech. Conf. (VTC Spring), 2016, pp. 1–5.   
[166] N. H. Nguyen and K. Dogançay, “Algebraic solution for stationary ˘ emitter geolocation by a LEO satellite using doppler frequency measurements,” in Proc. IEEE Int. Conf. Acoust. Speech Signal Process. (ICASSP), 2016, pp. 3341–3345.   
[167] M. Pan, J. Hu, J. Yuan, J. Liu, and Y. Su, “An efficient blind doppler shift estimation and compensation method for LEO satellite communications,” in Proc. IEEE 20th Int. Conf. Commun. Technol. (ICCT), 2020, pp. 643–648.   
[168] X. Lin, Z. Lin, S. E. Löwenmark, J. Rune, and R. S. Karlsson. “Doppler shift estimation in 5G new radio non-terrestrial networks.” 2021. [Online]. Available: https://arxiv.org/abs/2108.07757   
[169] M.-S. Hwang, C.-C. Yang, and C.-Y. Shiu, “An authentication scheme for mobile satellite communication systems,” ACM SIGOPS Oper. Syst. Rev., vol. 37, no. 4, pp. 42–47, 2003.   
[170] R. J. Hughes et al., “Quantum cryptography for secure satellite communications,” in Proc. IEEE Aerosp. Conf. Process., vol. 1, 2000, pp. 191–200.   
[171] A. D. Wyner, “The wire-tap channel,” Bell Syst. Tech. J., vol. 54, no. 8, pp. 1355–1387, 1975.   
[172] P. Baracca, N. Laurenti, and S. Tomasin, “Physical layer authentication over MIMO fading wiretap channels,” IEEE Trans. Wireless Commun., vol. 11, no. 7, pp. 2564–2573, Jul. 2012.   
[173] L. Senigagliesi, M. Baldi, and E. Gambi, “Comparison of statistical and machine learning techniques for physical layer authentication,” IEEE Trans. Inf. Forensics Security, vol. 16, pp. 1506–1521, 2020.   
[174] M. Abdrabou and T. A. Gulliver, “Adaptive physical layer authentication using machine learning with antenna diversity,” IEEE Trans. Commun., vol. 70, no. 10, pp. 6604–6614, Oct. 2022.   
[175] O. A. Topal, G. K. Kurt, and H. Yanikomeroglu, “Securing the interspacecraft links: Physical layer key generation from doppler frequency shift,” IEEE J. Radio Freq. Identification, vol. 5, no. 3, pp. 232–243, Sep. 2021.   
[176] O. A. Topal and G. K. Kurt, “Physical layer authentication for LEO satellite constellations,” in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), 2022, pp. 1952–1957.   
[177] E. Jedermann, M. Strohmeier, M. Schäfer, J. Schmitt, and V. Lenders, “Orbit-based authentication using TDOA signatures in satellite networks,” in Proc. 14th ACM Conf. Security Privacy Wireless Mobile Netw., 2021, pp. 175–180.   
[178] G. Oligeri, S. Sciancalepore, S. Raponi, and R. Di Pietro, “Past-AI: Physical-layer authentication of satellite transmitters via deep learning,” IEEE Trans. Inf. Forensics Security, vol. 18, pp. 274–289, 2022.   
[179] M. Abdrabou and T. A. Gulliver, “Physical layer authentication for satellite communication systems using machine learning,” IEEE Open J. Commun. Soc., vol. 3, pp. 2380–2389, 2022.   
[180] M. Abdrabou and T. A. Gulliver, “LEO satellite authentication using physical layer features with support vector machine,” in Proc. IEEE Int. Conf. Commun. Netw. Satellite (COMNETSAT), 2022, pp. 277–282.

[181] M. Abdrabou and T. A. Gulliver, “Authentication for satellite communication systems using physical characteristics,” IEEE Open J. Veh. Technol., vol. 4, pp. 48–60, 2022.   
[182] I. Ashraf et al., “A deep learning-based smart framework for cyberphysical and satellite system security threats detection,” Electronics, vol. 11, no. 4, p. 667, 2022.   
[183] A. T. Azar, E. Shehab, A. M. Mattar, I. A. Hameed, and S. A. Elsaid, “Deep learning based hybrid intrusion detection systems to protect satellite networks,” J. Netw. Sys. Manag., vol. 31, no. 4, p. 82, 2023.   
[184] L. Gunn, P. Smet, E. Arbon, and M. D. McDonnell, “Anomaly detection in satellite communications systems using LSTM networks,” in Proc. IEEE Mil. Commun. Inf. Syst. Conf. (MilCIS), 2018, pp. 1–6.   
[185] N. Koroniotis, N. Moustafa, and J. Slay, “A new intelligent satellite deep learning network forensic framework for smart satellite networks,” Comput. Elect. Eng., vol. 99, Jun. 2022, Art. no. 107745.   
[186] J. Tao, T. Han, and R. Li, “Deep-reinforcement-learning-based intrusion detection in aerial computing networks,” IEEE Netw., vol. 35, no. 4, pp. 66–72, Jul./Aug. 2021.   
[187] N. Moustafa et al., “DFSat: Deep federated learning for identifying cyber threats in IoT-based satellite networks,” IEEE Trans. Ind. Informat., early access, Oct. 20, 2022, doi: 10.1109/TII.2022.3214652.   
[188] K. Li, H. Zhou, Z. Tu, W. Wang, and H. Zhang, “Distributed network intrusion detection system in satellite-terrestrial integrated networks using federated learning,” IEEE Access, vol. 8, pp. 214852–214865, 2020.   
[189] R. Uddin and S. Kumar, “Federated learning based intrusion detection system for satellite communication,” in Proc. IEEE Cogn. Commun. Aerosp. Appl. Workshop (CCAAW), 2023, pp. 1–6.   
[190] C. Han, L. Huo, X. Tong, H. Wang, and X. Liu, “Spatial anti-jamming scheme for Internet of Satellites based on the deep reinforcement learning and Stackelberg game,” IEEE Trans. Veh. Technol., vol. 69, no. 5, pp. 5331–5342, May 2020.   
[191] C. Han, A. Liu, L. Huo, H. Wang, and X. Liang, “Anti-jamming routing for Internet of Satellites: A reinforcement learning approach,” in Proc. IEEE Int. Conf. Acoust. Speech Signal Process. (ICASSP), 2020, pp. 2877–2881.   
[192] H. Xu, Y. Cheng, J. Liang, and P. Wang, “A jamming recognition algorithm based on deep neural network in satellite navigation system,” in Proc. China Satellite Navig. Conf., 2020, pp. 701–711.   
[193] C. Han, A. Liu, H. Wang, L. Huo, and X. Liang, “Dynamic antijamming coalition for satellite-enabled army IoT: A distributed game approach,” IEEE Internet Things J., vol. 7, no. 11, pp. 10932–10944, Nov. 2020.   
[194] S. K. Jayaweera et al. “Cognitive anti-jamming satellite-to-ground communications on NASA’s SCaN testbed.” 2018. Accessed: Sep. 13, 2023. [Online]. Available: https://ntrs.nasa.gov/citations/20190001548   
[195] Y. Li, Y. Fan, S. Liu, L. Liu, and W. Yang, “Overview of beam hopping algorithms in large scale LEO satellite constellation,” in Proc. IEEE 20th Int. Conf. Trust Security Privacy Comput. Commun. (TrustCom), 2021, pp. 1345–1351.   
[196] Y. Han, C. Zhang, and G. Zhang, “Dynamic beam hopping resource allocation algorithm based on deep reinforcement learning in multibeam satellite systems,” in Proc. 3rd Int. Acad. Exchange Conf. Sci. Technol. Innov. (IAECST), 2021, pp. 68–73.   
[197] X. Hu et al., “Deep reinforcement learning-based beam hopping algorithm in multibeam satellite systems,” IET Commun., vol. 13, no. 16, pp. 2485–2491, 2019. [Online]. Available: https://ietresearch. onlinelibrary.wiley.com/doi/abs/10.1049/iet-com.2018.5774   
[198] X. Hu, L. Wang, Y. Wang, S. Xu, Z. Liu, and W. Wang, “Dynamic beam hopping for DVB-S2X GEO satellite: A DRL-powered GA approach,” IEEE Commun. Lett., vol. 26, no. 4, pp. 808–812, Apr. 2022.   
[199] Y. Zhang, X. Hu, R. Chen, Z. Zhang, L. Wang, and W. Wang, “Dynamic beam hopping for DVB-S2X satellite: A multi-objective deep reinforcement learning approach,” in Proc. IEEE Int. Conf. Ubiquitous Comput. Commun. (IUCC) Data Sci. Comput. Intell. (DSCI) Smart Comput. Netw. Services (SmartCNS), 2019, pp. 164–169.   
[200] X. Hu, Y. Zhang, X. Liao, Z. Liu, W. Wang, and F. M. Ghannouchi, “Dynamic beam hopping method based on multi-objective deep reinforcement learning for next generation satellite broadband systems,” IEEE Trans. Broadcast., vol. 66, no. 3, pp. 630–646, Sep. 2020.   
[201] Z. Lin, Z. Ni, L. Kuang, C. Jiang, and Z. Huang, “Dynamic beam pattern and bandwidth allocation based on multi-agent deep reinforcement learning for beam hopping satellite systems,” IEEE Trans. Veh. Technol., vol. 71, no. 4, pp. 3917–3930, Apr. 2022.   
[202] Q. Zhao, Y. Hu, Z. Pang, and D. Ren, “Beam hopping for LEO satellite: Challenges and opportunities,” in Proc. Int. Conf. Culture Oriented Sci. Technol. (CoST), 2022, pp. 319–324.

[203] J. Choi and V. Chan, “Optimum power and beam allocation based on traffic demands and channel conditions over satellite downlinks,” IEEE Trans. Wireless Commun., vol. 4, no. 6, pp. 2983–2993, Nov. 2005.   
[204] X. Alberti et al., “System capacity optimization in time and frequency for multibeam multi-media satellite systems,” in Proc. 5th Adv. Satellite Multimedia Syst. Conf. 11th Signal Process. Space Commun. Workshop, 2010, pp. 226–233.   
[205] R. Alegre-Godoy, N. Alagha, and M. A. Vázquez-Castro, “Offered capacity optimization mechanisms for multi-beam satellite systems,” in Proc. IEEE Int. Conf. Commun. (ICC), 2012, pp. 3180–3184.   
[206] A. Paris, I. Del Portillo, B. Cameron, and E. Crawley, “A genetic algorithm for joint power and bandwidth allocation in multibeam satellite systems,” in Proc. IEEE Aerosp. Conf., 2019, pp. 1–15.   
[207] G. Cocco, T. de Cola, M. Angelone, Z. Katona, and S. Erl, “Radio resource management optimization of flexible satellite payloads for DVB-S2 systems,” IEEE Trans. Broadcast., vol. 64, no. 2, pp. 266–280, Jun. 2018.   
[208] N. Pachler, J. J. G. Luis, M. Guerster, E. Crawley, and B. Cameron, “Allocating power and bandwidth in multibeam satellite systems using particle swarm optimization,” in Proc. IEEE Aerosp. Conf., 2020, pp. 1–11.   
[209] A. I. Aravanis, B. Shankar, P.-D. Arapoglou, G. Danoy, P. G. Cottis, and B. Ottersten, “Power allocation in multibeam satellite systems: A twostage multi-objective optimization,” IEEE Trans. Wireless Commun., vol. 14, no. 6, pp. 3171–3182, Jun. 2015.   
[210] X. Ding, L. Feng, Y. Zou, and G. Zhang, “Deep learning aided spectrum prediction for satellite communication systems,” IEEE Trans. Veh. Technol., vol. 69, no. 12, pp. 16314–16319, Dec. 2020.   
[211] X. Ding, L. Feng, J. Cheng, and G. Zhang, “Spectrum reconstruction via deep convolutional neural networks for satellite communication systems,” IEEE Trans. Commun., vol. 70, no. 9, pp. 5989–6001, Sep. 2022.   
[212] X. Ding, T. Ni, Y. Zou, and G. Zhang, “Deep learning for satellites based spectrum sensing systems: A low computational complexity perspective,” IEEE Trans. Veh. Technol., vol. 72, no. 1, pp. 1366–1371, Jan. 2023.   
[213] Z. Ren, J. Jin, W. Li, R. Wen, and Y. Zhan, “Frequency prediction and assignment among SatComs networks: A CNN- LSTM approach,” in Proc. IEEE/CIC Int. Conf. Commun. China (ICCC Workshops), 2022, pp. 106–111.   
[214] Z. Ren, J. Jin, W. Li, and Y. Zhan, “Intelligent action selection for NGSO networks with interference constraints: A modified Q-learning approach,” IEEE Trans. Aerosp. Electron. Syst., vol. 58, no. 3, pp. 2231–2242, Jun. 2022.   
[215] M. Jia, X. Zhang, J. Sun, X. Gu, and Q. Guo, “Intelligent resource management for satellite and terrestrial spectrum shared networking toward B5G,” IEEE Wireless Commun. Mag., vol. 27, no. 1, pp. 54–61, Feb. 2020.   
[216] X. Hu et al., “Multi-agent deep reinforcement learning-based flexible satellite payload for mobile terminals,” IEEE Trans. Veh. Technol., vol. 69, no. 9, pp. 9849–9865, Sep. 2020.   
[217] C. Zhang, C. Jiang, J. Jin, S. Wu, L. Kuang, and S. Guo, “Spectrum sensing and recognition in satellite systems,” IEEE Trans. Veh. Technol., vol. 68, no. 3, pp. 2502–2516, Mar. 2019.   
[218] J. Mitola and G. Maguire, “Cognitive radio: Making software radios more personal,” IEEE Pers. Commun., vol. 6, no. 4, pp. 13–18, Aug. 1999.   
[219] A.-A. A. Boulogeorgos, N. D. Chatzidiamantis, and G. K. Karagiannidis, “Energy detection spectrum sensing under RF imperfections,” IEEE Trans. Commun., vol. 64, no. 7, pp. 2754–2766, Jul. 2016.   
[220] P. Semba Yawada and A. J. Wei, “Cyclostationary detection based on non-cooperative spectrum sensing in cognitive radio network,” in Proc. IEEE Int. Conf. Cyber Technol. Autom. Control Intell. Syst. (CYBER), 2016, pp. 184–187.   
[221] Y. Zeng and Y.-C. Liang, “Eigenvalue-based spectrum sensing algorithms for cognitive radio,” IEEE Trans. Commun., vol. 57, no. 6, pp. 1784–1793, Jun. 2009.   
[222] E. Biglieri, “An overview of cognitive radio for satellite communications,” in Proc. IEEE 1st AESS Eur. Conf. Satellite Telecommun. (ESTEL), 2012, pp. 1–3.   
[223] C. Jiang and X. Zhu, “Reinforcement learning based capacity management in multi-layer satellite networks,” IEEE Trans. Wireless Commun., vol. 19, no. 7, pp. 4685–4699, Jul. 2020.   
[224] B. Zhao, J. Liu, Z. Wei, and I. You, “A deep reinforcement learning based approach for energy-efficient channel allocation in satellite Internet of Things,” IEEE Access, vol. 8, pp. 62197–62206, 2020.

[225] X. Hu, S. Liu, R. Chen, W. Wang, and C. Wang, “A deep reinforcement learning-based framework for dynamic resource allocation in multibeam satellite systems,” IEEE Commun. Lett., vol. 22, no. 8, pp. 1612–1615, Aug. 2018.   
[226] N. Dai, D. Zhou, M. Sheng, and J. Li, “Deep reinforcement learning based power allocation for high throughput satellites,” in Proc. IEEE 94th Veh. Tech. Conf. (VTC-Fall), 2021, pp. 1–5.   
[227] X. Li, H. Zhang, W. Li, and K. Long, “Multi-agent DRL for user association and power control in terrestrial-satellite network,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), 2021, pp. 1–5.   
[228] P. V. R. Ferreira et al., “Multiobjective reinforcement learning for cognitive satellite communications using deep neural network ensembles,” IEEE J. Sel. Areas Commun., vol. 36, no. 5, pp. 1030–1041, May 2018.   
[229] S. Nie, J. M. Jornet, and I. F. Akyildiz, “Deep-learning-based resource allocation for multi-band communications in CubeSat networks,” in Proc. IEEE Int. Conf. Commun. Workshops (ICC Workshops), 2019, pp. 1–6.   
[230] T. S. Abdu, S. Kisseleff, L. Lei, E. Lagunas, J. Grotz, and S. Chatzinotas, “A deep learning based acceleration of complex satellite resource management problem,” in Proc. 30th Eur. Signal Process. Conf. (EUSIPCO), 2022, pp. 1092–1096.   
[231] S. Kisseleff, E. Lagunas, T. S. Abdu, S. Chatzinotas, and B. Ottersten, “Radio resource management techniques for multibeam satellite systems,” IEEE Commun. Lett., vol. 25, no. 8, pp. 2448–2452, Aug. 2021.   
[232] L. Kuang, X. Chen, C. Jiang, H. Zhang, and S. Wu, “Radio resource management in future terrestrial-satellite communication networks,” IEEE Wireless Commun. Mag., vol. 24, no. 5, pp. 81–87, Oct. 2017.   
[233] T. S. Abdu, S. Kisseleff, E. Lagunas, and S. Chatzinotas, “Power and bandwidth minimization for demand-aware GEO satellite systems,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), 2021, pp. 1–6.   
[234] T. S. Abdu, E. Lagunas, S. Kisseleff, and S. Chatzinotas, “Carrier and power assignment for flexible broadband GEO satellite communications system,” in Proc. IEEE 31st Annu. Int. Symp. Pers., Indoor Mobile Radio Commun., 2020, pp. 1–7.   
[235] T. S. Abdu, S. Kisseleff, E. Lagunas, and S. Chatzinotas, “Limits of smart radio resource assignment in GEO satellite communications,” in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), 2021, pp. 1–7.   
[236] P. Gu, R. Li, C. Hua, and R. Tafazolli, “Dynamic cooperative spectrum sharing in a multi-beam LEO- GEO co-existing satellite system,” IEEE Trans. Wireless Commun., vol. 21, no. 2, pp. 1170–1182, Feb. 2022.   
[237] T. Salih Abdu, L. Lei, S. Kisseleff, E. Lagunas, S. Chatzinotas, and B. Ottersten, “Precoding-aided bandwidth optimization for high throughput satellite systems,” in Proc. IEEE 4th 5G World Forum (5GWF), 2021, pp. 13–17.   
[238] P. Angeletti and R. De Gaudenzi, “Heuristic radio resource management for massive MIMO in satellite broadband communication networks,” IEEE Access, vol. 9, pp. 147164–147190, 2021.   
[239] B. Deng, C. Jiang, H. Yao, S. Guo, and S. Zhao, “The next generation heterogeneous satellite communication networks: Integration of resource management and deep reinforcement learning,” IEEE Wireless Commun. Mag., vol. 27, no. 2, pp. 105–111, Apr. 2020.   
[240] Y. Drif et al., “An extensible network slicing framework for satellite integration into 5G,” Int. J. Satellite Commun. Netw., vol. 39, no. 4, pp. 339–357, 2021. [Online]. Available: https://onlinelibrary. wiley.com/doi/abs/10.1002/sat.1387   
[241] T. Ahmed, A. Alleg, R. Ferrus, and R. Riggio, “On-demand network slicing using SDN/NFV-enabled satellite ground segment systems,” in Proc. 4th IEEE Conf. Netw. Softw. Workshops (NetSoft), 2018, pp. 242–246.   
[242] C. Suzhi et al., “Space edge cloud enabling network slicing for 5G satellite network,” in Proc. 15th Int. Wireless Commun. Mobile Comput. Conf. (IWCMC), 2019, pp. 787–792.   
[243] T. Kim, J. Kwak, and J. P. Choi, “Satellite edge computing architecture and network slice scheduling for IoT support,” IEEE Internet Things J., vol. 9, no. 16, pp. 14938–14951, Aug. 2022.   
[244] J. Wang, J. Liu, J. Li, and N. Kato, “Artificial intelligence-assisted network slicing: Network assurance and service provisioning in 6G,” IEEE Veh. Technol. Mag., vol. 18, no. 1, pp. 49–58, Mar. 2023.   
[245] H. Wu et al., “Resource management in space-air-ground integrated vehicular networks: SDN control and AI algorithm design,” IEEE Wireless Commun., vol. 27, no. 6, pp. 52–60, Dec. 2020.   
[246] T. Kim, J. Kwak, and J. P. Choi, “Satellite network slice planning: Architecture, performance analysis, and open issues,” IEEE Veh. Technol. Mag., vol. 18, no. 2, pp. 29–38, Jun. 2023.

[247] H. H. Esmat, B. Lorenzo, and W. Shi, “Toward resilient network slicing for satellite–terrestrial edge computing IoT,” IEEE Internet Things J., vol. 10, no. 16, pp. 14621–14645, Aug. 2023.   
[248] I. Bisio, F. Lavagetto, G. Verardo, and T. de Cola, “Network slicing optimization for integrated 5G-satellite networks,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), 2019, pp. 1–6.   
[249] L. Lei, Y. Yuan, T. X. Vu, S. Chatzinotas, M. Minardi, and J. F. M. Montoya, “Dynamic-adaptive AI solutions for network slicing management in satellite-integrated B5G systems,” IEEE Netw., vol. 35, no. 6, pp. 91–97, Nov./Dec. 2021.   
[250] W. Wu et al., “AI-native network slicing for 6G networks,” IEEE Wireless Commun. Mag., vol. 29, no. 1, pp. 96–103, Feb. 2022.   
[251] T. K. Rodrigues and N. Kato, “Network slicing with centralized and distributed reinforcement learning for combined satellite/ground networks in a 6G environment,” IEEE Wireless Commun. Mag., vol. 29, no. 1, pp. 104–110, Feb. 2022.   
[252] M. Chen, Y. Zhang, Y. Teng, B. Liu, and L. Zhang, “Reinforcement learning based signal quality aware handover scheme for LEO satellite communication networks,” in Proc. 5th Int. Conf. Human Centered Comput. (HCC), 2019, pp. 44–55.   
[253] H. Xu, D. Li, M. Liu, G. Han, W. Huang, and C. Xu, “QoE-driven intelligent handover for user-centric mobile satellite networks,” IEEE Trans. Veh. Technol., vol. 69, no. 9, pp. 10127–10139, Sep. 2020.   
[254] S. He, T. Wang, and S. Wang, “Load-aware satellite handover strategy based on multi-agent reinforcement learning,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), 2020, pp. 1–6.   
[255] J. Wang, W. Mu, Y. Liu, L. Guo, S. Zhang, and G. Gui, “Deep reinforcement learning-based satellite handover scheme for satellite communications,” in Proc. 13th Int. Conf. Wireless Commun. Signal Process. (WCSP), 2021, pp. 1–6.   
[256] C. Zhang, N. Zhang, W. Cao, K. Tian, and Z. Yang, “An AI-based optimization of handover strategy in non-terrestrial networks,” in Proc. ITU Kaleidoscope Ind. Driven Digit. Transf. (ITU K), 2020, pp. 1–6.   
[257] S. Jung, M.-S. Lee, J. Kim, M.-Y. Yun, J. Kim, and J.-H. Kim, “Trustworthy handover in LEO satellite mobile networks,” ICT Exp., vol. 8, no. 3, pp. 432–437, 2022.   
[258] D.-F. Wu et al., “LB-DDQN for handover decision in satellite-terrestrial integrated networks,” Wireless Commun. Mobile Comput., vol. 2021, pp. 1–11, Dec. 2021.   
[259] H. Liu, Y. Wang, and Y. Wang, “A successive deep Q-learning based distributed handover scheme for large-scale LEO satellite networks,” in Proc. IEEE 95th Veh. Tech. Conf. (VTC-Spring), 2022, pp. 1–6.   
[260] E. Papapetrou, S. Karapantazis, G. Dimitriadis, and F.-N. Pavlidou, “Satellite handover techniques for LEO networks,” Int. J. Satellite Commun. Netw., vol. 22, no. 2, pp. 231–245, 2004. [Online]. Available: https://onlinelibrary.wiley.com/doi/abs/10.1002/sat.783   
[261] Z. Wu, F. Jin, J. Luo, Y. Fu, J. Shan, and G. Hu, “A graph-based satellite handover framework for LEO satellite communication networks,” IEEE Commun. Lett., vol. 20, no. 8, pp. 1547–1550, Aug. 2016.   
[262] X. Lv, S. Wu, A. Li, J. Jiao, N. Zhang, and Q. Zhang, “A weighted graph-based handover strategy for aeronautical traffic in LEO SatCom networks,” IEEE Netw. Lett., vol. 4, no. 3, pp. 132–136, Sep. 2022.   
[263] S. Zhang, A. Liu, and X. Liang, “A multi-objective satellite handover strategy based on entropy in LEO satellite communications,” in Proc. IEEE 6th Int. Conf. Comput. Commun. (ICCC), 2020, pp. 723–728.   
[264] S. Zhang, A. Liu, C. Han, X. Ding, and X. Liang, “A network-flowsbased satellite handover strategy for LEO satellite networks,” IEEE Wireless Commun. Lett., vol. 10, no. 12, pp. 2669–2673, Dec. 2021.   
[265] Y. Wu, G. Hu, F. Jin, and J. Zu, “A satellite handover strategy based on the potential game in LEO satellite networks,” IEEE Access, vol. 7, pp. 133641–133652, 2019.   
[266] J. Miao, P. Wang, H. Yin, N. Chen, and X. Wang, “A multi-attribute decision handover scheme for LEO mobile satellite networks,” in Proc. IEEE 5th Int. Conf. Comput. Commun. (ICCC), 2019, pp. 938–942.   
[267] M. Rahman, T. Walingo, and F. Takawira, “Adaptive handover scheme for LEO satellite communication system,” in Proc. AFRICON, 2015, pp. 1–5.   
[268] W. Zhaofeng, H. Guyu, Y. Seyedi, and J. Fenglin, “A simple realtime handover management in the mobile satellite communication networks,” in Proc. 17th Asia–Pac. Netw. Oper. Manag. Symp. (APNOMS), 2015, pp. 175–179.   
[269] Y. Li, W. Zhou, and S. Zhou, “Forecast based handover in an extensible multi-layer LEO mobile satellite system,” IEEE Access, vol. 8, pp. 42768–42783, 2020.   
[270] Y. Liu, X. Tang, Y. Zhou, J. Shi, M. Qian, and S. Li, “Channel reservation based load aware handover for LEO satellite communications,” in Proc. IEEE 95th Veh. Tech. Conf. (VTC-Spring), 2022, pp. 1–5.

[271] Y. Sun, Y. Wang, J. Jiao, S. Wu, and Q. Zhang, “Deep learning-based long-term power allocation scheme for NOMA downlink system in S-IoT,” IEEE Access, vol. 7, pp. 86288–86296, 2019.   
[272] X. Yan, K. An, Q. Zhang, G. Zheng, S. Chatzinotas, and J. Han, “Delay constrained resource allocation for NOMA enabled satellite Internet of Things with deep reinforcement learning,” IEEE Internet Things J., vol. 11, no. 1, pp. 6541–6550, Jan. 2023   
[273] A. Wang, L. Lei, E. Lagunas, S. Chatzinotas, and B. Ottersten, “Dual-DNN assisted optimization for efficient resource scheduling in NOMA-enabled satellite systems,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), 2021, pp. 1–6.   
[274] Q. Zhang, K. An, X. Yan, H. Xi, and Y. Wang, “User pairing for delay-limited NOMA-based satellite networks with deep reinforcement learning,” Sensors, vol. 23, no. 16, p. 7062, 2023.   
[275] M. Karavolos, L. Tsipi, P. S. Bithas, D. Vouyioukas, and P. T. Mathiopoulos, “Satellite aerial terrestrial hybrid NOMA scheme in 6G networks: An unsupervised learning approach,” in Proc. 1st Int. Conf. 6G Netw. (6GNet), 2022, pp. 1–5.   
[276] D. A. Tubiana, J. Farhat, G. Brante, and R. D. Souza, “Q-learning NOMA random access for IoT-satellite terrestrial relay networks,” IEEE Wireless Commun. Lett., vol. 11, no. 8, pp. 1619–1623, Aug. 2022.   
[277] W. U. Khan et al., “Rate splitting multiple access for next generation cognitive radio enabled LEO satellite networks,” IEEE Trans. Wireless Commun., vol. 22, no. 11, pp. 8423–8435, Nov. 2023.   
[278] Q. Zhang, L. Zhu, S. Jiang, and X. Tang, “Deep unfolding for cooperative rate splitting multiple access in hybrid satellite terrestrial networks,” China Commun., vol. 19, no. 7, pp. 100–109, 2022.   
[279] Q. Zhang and L. Zhu, “A deep learning approach for downlink sum rate maximization in satellite-terrestrial integrated network,” in Proc. Int. Symp. Netw. Comput. Commun. (ISNCC), 2022, pp. 1–5.   
[280] J. Huang, Y. Yang, L. Yin, D. He, and Q. Yan, “Deep reinforcement learning-based power allocation for rate-splitting multiple access in 6G LEO satellite communication system,” IEEE Wireless Commun. Lett., vol. 11, no. 10, pp. 2185–2189, Oct. 2022.   
[281] S. Sthapit, S. Lakshminarayana, L. He, G. Epiphaniou, and C. Maple, “Reinforcement learning for security-aware computation offloading in satellite networks,” IEEE Internet Things J., vol. 9, no. 14, pp. 12351–12363, Jul. 2022.   
[282] D. Zhu et al., “Deep reinforcement learning-based task offloading in satellite-terrestrial edge computing networks,” in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), 2021, pp. 1–7.   
[283] N. Waqar, S. A. Hassan, A. Mahmood, K. Dev, D.-T. Do, and M. Gidlund, “Computation offloading and resource allocation in MEC-enabled integrated aerial-terrestrial vehicular networks: A reinforcement learning approach,” IEEE Trans. Intell. Transp. Syst., vol. 23, no. 11, pp. 21478–21491, Nov. 2022.   
[284] Z. Qin, H. Yao, T. Mai, D. Wu, N. Zhang, and S. Guo, “Multiagent reinforcement learning aided computation offloading in aerial computing for the Internet-of-Things,” IEEE Trans. Services Comput., vol. 16, no. 3, pp. 1976–1986, May/Jun. 2023.   
[285] Y. Lyu, Z. Liu, R. Fan, C. Zhan, H. Hu, and J. An, “Optimal computation offloading in collaborative LEO-IoT enabled MEC: A multi-agent deep reinforcement learning approach,” IEEE Trans. Green Commun. Netw., vol. 7, no. 2, pp. 996–1011, Jun. 2023.   
[286] B. Mao, F. Tang, Y. Kawamoto, and N. Kato, “Optimizing computation offloading in satellite- UAV-served 6G IoT: A deep learning approach,” IEEE Netw., vol. 35, no. 4, pp. 102–108, Jul./Aug. 2021.   
[287] J. Zhang, X. Zhang, P. Wang, L. Liu, and Y. Wang, “Double-edge intelligent integrated satellite terrestrial networks,” China Commun., vol. 17, no. 9, pp. 128–146, 2020.   
[288] H. Li, C. Chen, C. Li, L. Liu, and G. Gui, “Aerial computing offloading by distributed deep learning in collaborative satellite-terrestrial networks,” in Proc. 13th Int. Conf. Wireless Commun. Signal Process. (WCSP), 2021, pp. 1–6.   
[289] Q. Tang, Z. Fei, and B. Li, “Distributed deep learning for cooperative computation offloading in low earth orbit satellite networks,” China Commun., vol. 19, no. 4, pp. 230–243, 2022.   
[290] T. Lv, W. Liu, H. Huang, and X. Jia, “Optimal data downloading by using inter-satellite offloading in LEO satellite networks,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), 2016, pp. 1–6.   
[291] R. Xie, Q. Tang, Q. Wang, X. Liu, F. R. Yu, and T. Huang, “Satellite-terrestrial integrated edge computing networks: Architecture, challenges, and open issues,” IEEE Netw., vol. 34, no. 3, pp. 224–231, May/Jun. 2020.

[292] L. Zhang, H. Zhang, C. Guo, H. Xu, L. Song, and Z. Han, “Satelliteaerial integrated computing in disasters: User association and offloading decision,” in Proc. IEEE Int. Conf. Commun. (ICC), 2020, pp. 554–559.   
[293] Y. Wang, J. Yang, X. Guo, and Z. Qu, “A game-theoretic approach to computation offloading in satellite edge computing,” IEEE Access, vol. 8, pp. 12510–12520, 2019.   
[294] S. Huang, G. Li, E. Ben-Awuah, B. O. Afum, and N. Hu, “A stochastic mixed integer programming framework for underground mining production scheduling optimization considering grade uncertainty,” IEEE Access, vol. 8, pp. 24495–24505, 2020.   
[295] J. Gao, L. Zhao, and X. Shen, “Service offloading in terrestrial-satellite systems: User preference and network utility,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), 2019, pp. 1–6.   
[296] J. Kim, T. Kim, M. Hashemi, C. G. Brinton, and D. J. Love, “Joint optimization of signal design and resource allocation in wireless D2D edge computing,” in Proc. IEEE INFOCOM Conf. Comput. Commun., 2020, pp. 2086–2095.   
[297] T. Chen et al., “Learning-based computation offloading for IoRT through Ka/Q-band satellite–terrestrial integrated networks,” IEEE Internet Things J., vol. 9, no. 14, pp. 12056–12070, Jul. 2022.   
[298] Y. Yin, C. Huang, D.-F. Wu, S. Huang, M. Ashraf, and Q. Guo, “Reinforcement learning-based routing algorithm in satellite-terrestrial integrated networks,” Wireless Commun. Mobile Comput., vol. 2021, Oct. 2021, Art. no. 3759631.   
[299] X. Wang, Z. Dai, and Z. Xu, “LEO satellite network routing algorithm based on reinforcement learning,” in Proc. IEEE 4th Int. Conf. Electron. Technol. (ICET), 2021, pp. 1105–1109.   
[300] Y. Huang et al., “Reinforcement learning based dynamic distributed routing scheme for mega LEO satellite networks,” Chin. J. Aeronaut., vol. 36, no. 2, pp. 284–291, Feb. 2023.   
[301] F. Wang, D. Jiang, Z. Wang, Z. Lv, and S. Mumtaz, “Fuzzy- CNN based multi-task routing for integrated satellite-terrestrial networks,” IEEE Trans. Veh. Technol., vol. 71, no. 2, pp. 1913–1926, Feb. 2022.   
[302] D. Liu, J. Zhang, J. Cui, S.-X. Ng, R. G. Maunder, and L. Hanzo, “Deep learning aided routing for space-air-ground integrated networks relying on real satellite, flight, and shipping data,” IEEE Wireless Commun. Mag., vol. 29, no. 2, pp. 177–184, Apr. 2022.   
[303] Z. Na, Z. Pan, X. Liu, Z. Deng, Z. Gao, and Q. Guo, “Distributed routing strategy based on machine learning for LEO satellite network,” Wireless Commun. Mobile Comput., vol. 2018, Jun. 2018, Art. no. 3026405.   
[304] M. Liu, J. Li, and H. Lu, “Routing in small satellite networks: A GNNbased learning approach,” 2021, arXiv:2108.08523.   
[305] Z. Tu, H. Zhou, K. Li, G. Li, and Q. Shen, “A routing optimization method for software-defined SGIN based on deep reinforcement learning,” in Proc. IEEE Globecom Workshops (GC Wkshps), 2019, pp. 1–6.   
[306] E. W. Dijkstra, “A note on two problems in connexion with graphs,” in Edsger Wybe Dijkstra: His Life, Work, and Legacy. Singapore: Springer, 2022, pp. 287–290.   
[307] M. Werner, “A dynamic routing concept for ATM-based satellite personal communication networks,” IEEE J. Sel. Areas Commun., vol. 15, no. 8, pp. 1636–1648, Oct. 1997.   
[308] J. T. Moy, OSPF: Anatomy of an Internet Routing Protocol. Boston, MA, USA: Addison-Wesley Prof., 1998.   
[309] L. Wood, A. Clerget, I. Andrikopoulos, G. Pavlou, and W. Dabbous, “IP routing issues in satellite constellation networks,” Int. J. Satellite Commun., vol. 19, no. 1, pp. 69–92, 2001.   
[310] Y. Lv, C. Xing, N. Xu, X. Han, and F. Wang, “Research of adaptive routing scheme for LEO network,” in Proc. IEEE 5th Int. Conf. Comput. Commun. (ICCC), 2019, pp. 987–992.   
[311] E. Sigel, B. Denby, and S. Le Hégarat-Mascle, “Application of ant colony optimization to adaptive routing in a LEO telecommunications satellite network,” Annales des Télécommun., vol. 57, nos. 5–6, pp. 520–539, 2002.   
[312] S. Liu, D. Wu, and L. Zhang, “A routing model based on multipleuser requirements and the optimal solution,” IEEE Access, vol. 8, pp. 156470–156483, 2020.   
[313] N. Zhao, X. Long, and J. Wang, “A multi-constraint optimal routing algorithm in LEO satellite networks,” Wireless Netw., to be published.   
[314] J. Tao, Z. Na, and N. Zhang, “Time-varying graph model for LEO satellite network routing,” in Proc. IEEE 9th Int. Conf. Depend. Syst. Appl. (DSA), 2022, pp. 486–491.   
[315] R. Kucukates and C. Ersoy, “High performance routing in a LEO satellite network,” in Proc. 8th IEEE Symp. Comput. Commun. (ISCC), 2003, pp. 1403–1408.

[316] S. Lv et al., “Routing strategy of integrated satellite-terrestrial network based on hyperbolic geometry,” IEEE Access, vol. 8, pp. 113003–113010, 2020.   
[317] J. Zhou, Q. Yang, X. Zhang, C. Han, and L. Sun, “Traffic prediction method for GEO satellites combining ARIMA model and grey model,” J. Shanghai Jiaotong Univ., vol. 25, pp. 65–69, Feb. 2020.   
[318] C. Chen, J. Hu, Q. Meng, and Y. Zhang, “Short-time traffic flow prediction with ARIMA-GARCH model,” in Proc. IEEE Intell. Veh. Symp. (IV), 2011, pp. 607–612.   
[319] Y. Zhang, S. Qu, and K. Wen, “A short-term traffic flow forecasting method based on chaos and RBF neural network,” Syst. Eng., vol. 25, no. 11, pp. 26–30, Jan. 2007.   
[320] F. Zhu, L. Liu, and T. Lin, “An LSTM-based traffic prediction algorithm with attention mechanism for satellite network,” in Proc. 3rd Int. Conf. Artif. Intell. Pattern Recognit., 2020, pp. 205–209.   
[321] N. Li, L. Hu, Z.-L. Deng, T. Su, and J.-W. Liu, “Research on GRU neural network satellite traffic prediction based on transfer learning,” Wireless Pers. Commun., vol. 118, no. 1, pp. 815–827, 2021.   
[322] L. Yang, X. Gu, and H. Shi, “A noval satellite network traffic prediction method based on GCN-GRU,” in Proc. Int. Conf. Wireless Commun. Signal Process. (WCSP), 2020, pp. 718–723.   
[323] Z. Liu, W. Li, J. Feng, and J. Zhang, “Research on satellite network traffic prediction based on improved GRU neural network,” Sensors, vol. 22, no. 22, p. 8678, 2022.   
[324] “O-RAN: Towards an open and smart RAN.” Oct. 2018. [Online]. Available: https://www.o-ran.org/resources   
[325] M. Minardi, T. X. Vu, L. Lei, C. Politis, and S. Chatzinotas, “Virtual network embedding for NGSO systems: Algorithmic solution and SDN-Testbed validation,” IEEE Trans. Netw. Service Manag., vol. 20, no. 3, pp. 3523–3535, Sep. 2023.   
[326] “MLSAT—Machine learning and artificial intelligence for satellite communication.” 2020. Accessed: May 31, 2023. [Online]. Available: https://artes.esa.int/projects/mlsat   
[327] “SATAI—Machine learning and artificial intelligence for satellite communication.” 2020. Accessed: May 31, 2023. [Online]. Available: https://artes.esa.int/projects/satai   
[328] “ANChOR—Data-driven network controller and orchestrator for realtime network management.” 2021. Accessed: May 31, 2023. [Online]. Available: https://artes.esa.int/projects/anchor   
[329] “SkyMon PIA—SkyMon predictive interference analysis.” 2021. Accessed: May 31, 2023. [Online]. Available: https://artes.esa.int/ projects/skymon-pia   
[330] “SPAICE—Satellite signal processing techniques using a commercial off-the-shelf AI Chipset.” 2022. Accessed: May 31, 2023. [Online]. Available: https://artes.esa.int/projects/spaice   
[331] L. Bonati, M. Polese, S. D’Oro, S. Basagni, and T. Melodia, “Open, programmable, and virtualized 5G networks: State-of-the-art and the road ahead,” Comput. Netw., vol. 182, Dec. 2020, Art. no. 107516.   
[332] M. Polese, L. Bonati, S. D’Oro, S. Basagni, and T. Melodia, “Understanding O-RAN: Architecture, interfaces, algorithms, security, and research challenges,” IEEE Commun. Surveys Tuts., vol. 25, no. 2, pp. 1376–1411, 2nd Quart., 2023.   
[333] H. Lee, Y. Jang, J. Song, and H. Yeon, “O-RAN AI/ML Workflow implementation of personalized network optimization via reinforcement learning,” in Proc. IEEE Globecom Workshops (GC Wkshps), 2021, pp. 1–6.   
[334] N. Salhab, R. Rahim, R. Langar, and R. Boutaba, “Machine learning based resource orchestration for 5G network slices,” in Proc. IEEE Global Commun. Conf. (GLOBECOM), 2019, pp. 1–6.   
[335] F. Kaltenberger, G. d. Souza, R. Knopp, and H. Wang, “The OpenAirInterface 5G new radio implementation: Current status and roadmap,” in Proc. 23rd Int. ITG Workshop Smart Antennas (WSA), 2019, pp. 1–5.   
[336] R. Schmidt, M. Irazabal, and N. Nikaein, “FlexRIC: An SDK for nextgeneration SD-RANs,” in Proc. 17th Int. Conf. Emerg. Netw. Exp. Technol. (CoNEXT), 2021, pp. 411–425. [Online]. Available: https:// doi.org/10.1145/3485983.3494870

[337] S. Kumar et al., “OpenAirInterface as a platform for 5G-NTN research and experimentation,” in Proc. IEEE Future Netw. World Forum (FNWF), 2022, pp. 500–506.   
[338] J. Kim et al., “5G-ALLSTAR: An integrated satellite-cellular system for 5G and beyond,” in Proc. IEEE Wireless Commun. Netw. Conf. Workshops (WCNCW), 2020, pp. 1–6.   
[339] “5G-EMUSAT:5G new radio emulation over satellite.” 2022. Accessed: May 23, 2023. [Online]. Available: https://5gmeteors.eurescom.eu/ open-calls/1st-open-call-summary/5g-emusat/   
[340] O. Kodheli et al., “Random access procedure over non-terrestrial networks: From theory to practice,” IEEE Access, vol. 9, pp. 109130–109143, 2021.   
[341] S. Kumar et al., “5G-NTN GEO-based in-lab demonstrator using OpenAirInterface5G,” in Proc. 11th Adv. Satellite Multimedia Syst. Conf. 17th Signal Process. Space Commun. Workshop (ASMS/SPSC), Sep. 2022, pp. 1–8.   
[342] “5G-LEO—OpenAirInterface extension for 5G satellite links.” 2022. Accessed: May 23, 2023. [Online]. Available: https://artes.esa.int/ projects/5gleo   
[343] G. Pang, “The AI chip race,” IEEE Intell. Syst., vol. 37, no. 2, pp. 111–112, Mar./Apr. 2022.   
[344] G. Furano et al., “Towards the use of artificial intelligence on the edge in space systems: Challenges and opportunities,” IEEE Aerosp. Electron. Syst. Mag., vol. 35, no. 12, pp. 44–56, Dec. 2020.   
[345] Z. Kong, J. Xue, Y. Wang, L. Huang, Z. Niu, and F. Li, “A survey on adversarial attack in the age of artificial intelligence,” Wireless Commun. Mobile Comput., vol. 2021, pp. 1–22, Jun. 2021.   
[346] T. Mahjabin, Y. Xiao, G. Sun, and W. Jiang, “A survey of distributed denial-of-service attack, prevention, and mitigation techniques,” Int. J. Distrib. Sensor Netw., vol. 13, no. 12, p. 15, 2017.   
[347] M. Conti, N. Dragoni, and V. Lesyk, “A survey of man in the middle attacks,” IEEE Commun. Surveys Tuts., vol. 18, no. 3, pp. 2027–2051, 3rd Quart., 2016.   
[348] P. Manzano et al., “Heavy ion latch-up test on dsPIC microcontroller to be used in ExoMars 2020 mission,” in Proc. IEEE Radiat. Effects Data Workshop (REDW), 2017, pp. 1–4.   
[349] G. Furano and A. Menicucci, “Roadmap for on-board processing and data handling systems in space,” in Dependable Multicore Architectures at Nanoscale. Cham, Switzerland: Springer, 2018, pp. 253–281.   
[350] G. Lentaris et al., “High-performance embedded computing in space: Evaluation of platforms for vision-based navigation,” J. Aerosp. Inf. Syst., vol. 15, no. 4, pp. 178–192, 2018.   
[351] G. Dulac-Arnold et al., “Challenges of real-world reinforcement learning: Definitions, benchmarks and analysis,” Mach. Learn., vol. 110, no. 9, pp. 2419–2468, 2021.   
[352] L. Canese et al., “Multi-agent reinforcement learning: A review of challenges and applications,” Appl. Sci., vol. 11, no. 11, p. 4948, 2021.   
[353] Y. Li, “Deep reinforcement learning: An overview,” 2017, arXiv:1701.07274.   
[354] L. Liu, R. Chen, S. Geirhofer, K. Sayana, Z. Shi, and Y. Zhou, “Downlink MIMO in LTE-advanced: SU-MIMO vs. MU-MIMO,” IEEE Commun. Mag., vol. 50, no. 2, pp. 140–147, Feb. 2012.   
[355] H.-H. Chang, H. Song, Y. Yi, J. Zhang, H. He, and L. Liu, “DistribuIve dynamic spectrum access through deep reinforcement learning: A reservoir computing-based approach,” IEEE Internet Things J., vol. 6, no. 2, pp. 1938–1948, Apr. 2019.   
[356] H.-H. Chang, L. Liu, and Y. Yi, “Deep echo state Q-network (DEQN) and its application in dynamic spectrum sharing for 5G and beyond,” IEEE Trans. Neural Netw. Learn. Syst., vol. 33, no. 3, pp. 929–939, Mar. 2022.   
[357] J. Verbraeken, M. Wolting, J. Katzy, J. Kloppenburg, T. Verbelen, and J. S. Rellermeyer, “A survey on distributed machine learning,” ACM Comput. Surveys, vol. 53, no. 2, pp. 1–33, Mar. 2020. [Online]. Available: https://doi.org/10.1145/\penalty-\@M3377454