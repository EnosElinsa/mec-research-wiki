# Generative AI Agent Empowered Power Allocation for HAP Propulsion and Communication Systems

Xiaoyu Xing , Graduate Student Member, IEEE, Dingyi Lu, Graduate Student Member, IEEE, Peng Yang , Member, IEEE, Zehui Xiong , Senior Member, IEEE, Xianbin Cao , Senior Member, IEEE, and Tony Q. S. Quek , Fellow, IEEE

Abstract—High altitude platforms (HAPs) are emerging as a key enabler for 6G coverage, yet limited energy must be split between propulsion and communications. Most prior HAP studies ignore propulsion power or rely on surrogates that miss hull–propeller interference, leading to misestimated communication power budgets and degraded beamforming. More importantly, HAP power allocation is intrinsically a multi-system, multidisciplinary problem in which aerodynamics, propulsion-system efficiency, and communication-system performance [quality of service (QoS) and energy efficiency (EE)] are tightly coupled. To address these challenges, this paper designs an interactive generative artificial intelligence (AI)-empowered HAP power allocation agent. By interacting with the AI agent, we develop an accurate propulsion power consumption model that takes into account the aerodynamic interference between the HAP’s hull and the propeller. Assisted by the AI agent, we further formulate a HAP beamforming problem to improve user QoS and enhance the EE of the HAP communication system. This paper also proposes a QoS-enhanced energy-efficient (Q3E) beamforming algorithm to solve the formulated problem. Simulation results demonstrate the accuracy of the propulsionpower model and the effectiveness of the Q3E algorithm.

Index Terms—High altitude platform (HAP), HAP power allocation, generative AI agent, beamforming, multidisciplinary research.

Received 20 March 2025; revised 17 October 2025 and 2 February 2026; accepted 6 April 2026. Date of publication 13 April 2026; date of current version 15 April 2026. This study was supported in part by the NSFC under Grant 62471018 and Grant 61827901, in part by the Fundamental Research Funds for the Central Universities, and in part by the National Research Foundation, Singapore and Infocomm Media Development Authority under its Communications and Connectivity Bridging Funding Initiative. An earlier version of this paper was presented in part at the 2025 IEEE/CIC International Conference on Communications in China [DOI: 10.1109/ICCC65529.2025.11148893]. The associate editor coordinating the review of this article and approving it for publication was K. Ota. (Corresponding authors: Peng Yang; Xianbin Cao; Tony Q. S. Quek.)

Xiaoyu Xing, Dingyi Lu, and Xianbin Cao are with the School of Electronic Information Engineering, Beihang University, Beijing 100191, China (e-mail: xiaoyuxing@buaa.edu.cn; ludingyi@buaa.edu.cn; xbcao@buaa.edu.cn).

Peng Yang is with the School of Electronic Information Engineering, Beihang University, Beijing 100191, China, also with the Pengcheng Laboratory, Shenzhen 518100, China, and also with the State Key Laboratory of CNS/ATM, Beijing 100083, China (e-mail: peng yang@buaa.edu.cn).

Zehui Xiong is with the School of Electronics, Electrical Engineering and Computer Science, Queen’s University Belfast, BT7 1NN Belfast, U.K. (e-mail: z.xiong@qub.ac.uk).

Tony Q. S. Quek is with Singapore University of Technology and Design, Singapore 487372, and also with the Department of Electronic Engineering, Kyung Hee University, Yongin 17104, South Korea (e-mail: tonyquek@sutd.edu.sg).

## I. INTRODUCTION

Digital Object Identifier 10.1109/TCCN.2026.3683194

high capacity, and wider wireless coverage has driven the evolution of wireless communication networks. Driven by innovations in manufacturing, materials, communications, electronics, and control technologies, high altitude platform (HAP) networks have emerged as essential components of sixth-generation (6G) mobile communication systems [1], [2], [3], [4], [5], [6].

Compared with terrestrial networks (TNs), HAPs can respond rapidly to flash-crowd traffic, provide cost-effective coverage for underserved areas, and enhance resilience to natural and man-made disruptions [7], [8]. A HAP, deployed at an altitude ranging from 17 km to 25 km, has the ability to extend communication coverage quickly and provide widearea communication services. Compared with satellites, the deployment altitude of a HAP is much lower, resulting in lower communication latency and higher data rates. Compared with autonomous aerial vehicles (AAVs), a HAP can cover a more expansive area due to its elevated altitude [9]. However, as emerging networks, many key issues, including channel model and power allocation, must be studied for the HAP networks. A HAP incorporates many crucial systems, e.g., propulsion system and communication system. This paper is concerned with the propulsion and communication power allocation issue of a HAP.

## A. State of the Art

1) HAP Communication Power Allocation: Much research effort [10], [11], [12], [13], [14] has been devoted to the power allocation of the HAP communication system. For example, the authors in [10] studied the robust beamforming design for intelligent reflecting surface (IRS)-enhanced multiuser downlink communications in a satellite and HAP integrated network, and formulated and solved an optimization problem of minimizing the transmit power of HAP terminals, subject to the constraints on signal-to-interference-plus-noise ratio (SINR) and the outage probabilities experienced at both satellite and HAP terminals. In [11], the authors proposed a joint user association and beamforming optimization framework for integrated satellite-HAP-ground networks, aiming to maximize the total network throughput while satisfying

HAP payload connectivity constraints, HAP and ground base station power constraints, and free-space optical (FSO) backhaul constraints. In [12], the authors proposed to deploy a HAP equipped with a uniform concentric ring array to serve multiple mobile terminals using a space division multiple access (SDMA) technique. A beamforming scheme aiming at maximizing the minimum average SINR was designed to implement the SDMA technique. In [13], the authors proposed a deep reinforcement learning (DRL)-based method to enhance the energy efficiency (EE) of HAP networks by optimizing beam vectors, power allocation ratios, and phase shifts, while taking into account the users’ quality of service (QoS) requirements and the power limitation of the transmitter. In [14], the authors investigated the power allocation problem of integrated satellite-HAP-terrestrial networks. Taking into account practical limitations like channel estimation errors and imperfect interference cancellation, they proposed an innovative nonorthogonal multiple access-based power allocation strategy to satisfy various QoS requirements of users.

Although the above work [10], [11], [12], [13], [14], [15], [16] investigated the optimization issue of communication power consumption of HAP networks, the modeling of propulsion power consumption of a HAP was not touched upon. Most of them assumed that a HAP did not consume propulsion power when remaining stationary in the stratosphere. However, the reality is that to maintain a stationary status in the face of stratospheric winds, the HAP must maintain continuous motion. Furthermore, the propulsion system of a HAP consumes a significant amount of power. In this case, the modeling of the propulsion power consumption cannot be ignored in the research. Since a HAP mainly relies on rechargeable batteries and solar panels for its energy supply, unlike TNs, power allocation becomes a critical system design objective. Accurate propulsion power models are essential for effective power allocation. Thus, it is essential to investigate the modeling of propulsion power consumption for HAP.

2) HAP Propulsion Power Consumption Modeling: The modeling of propulsion power consumption has also attracted extensive attention from the research community [17], [18], [19], [20], [21], [22]. For instance, in [17], a propulsion power consumption strategy based on the output power of a solar array and the ambient wind field conditions was proposed. However, the utilized propulsion power consumption model was not established based on the aerodynamic theory and was not accurate enough. To improve the accuracy of models, some researchers proposed to derive models of the propulsion power consumption of a HAP based on the aerodynamic theory [18], [19], [20], [21], [22]. For instance, the authors in [18] studied the effects of aerodynamic drag on the propulsion power consumption of a HAP. In [19], the authors established a proxy model for calculating a propeller’s power consumption and carried out a wind tunnel experiment to verify its correctness. In [20], the effects of different kinetic and structural design parameters of HAP’s propellers on a propeller’s efficiency of a HAP were discussed in detail. Besides, in [21], the authors studied the application of polynomial chaos expansion (PCE) method to quantify the uncertainty of the aerodynamic performance of high-altitude propellers.

## B. Motivations and Contributions

Although propeller aerodynamics have been extensively investigated in prior studies [18], [19], [20], [21], [22], the hull-induced turbulence effects on power consumption of the HAP remain largely unaddressed. This oversight leads to underestimated propulsion-power requirements, thereby compelling HAP controllers to allocate excessive reserve power to the propulsion system. These safeguards progressively reduce the power allocated to communication payloads, ultimately constraining the power available for beamforming refinement. More importantly, HAP power allocation is intrinsically a multi-system, multidisciplinary problem in which aerodynamics, propulsion-system efficiency, and communication-system performance (QoS and EE) are tightly coupled. In contrast to existing work, this paper focuses on HAP power allocation through the development of an accurate propulsionpower model and the optimization of communication power consumption. We use computational fluid dynamics (CFD)- validated models to compute the propulsion-power budget. We then pass the resulting feasible communication power to the beamforming optimizer.

The interdisciplinary nature of this research presents significant challenges in formulating mathematical optimization models that accurately represent complex real-world operational scenarios—a task requiring advanced comprehension of nonlinear equations and multi-domain system dynamics. To address these challenges, we propose a generative AI agent with advanced reasoning capabilities, leveraging techniques including chain-of-thought (CoT) processing and hierarchical problem decomposition [23]. Recent applications demonstrate the efficacy of such an AI agent in resolving complex scientific problems, including human genome sequence decoding [24], advanced network security [25], task coordination and scheduling [26], and intelligent system management [27], aerial access networks [15], AAV networks mobility-aware [16]. Our main contribution is a generative-AI framework for HAPs that support cross-disciplinary studies. The key innovations of our work can be summarized as follows:

• Generative AI agent framework design: This paper proposes a generative AI agent framework for power allocation of a HAP. The framework employs a retrievalaugmented generation (RAG) and large language model (LLM) collaboration mechanism. This mechanism utilizes a knowledge database constructed by processing academic documents through semantic analysis, text chunking, and embedding techniques. It enhances reasoning accuracy through semantic matching between researchers’ queries and knowledge database content.

Accurate propulsion power consumption modeling: Under the guidance of the generative AI agent, we derive an accurate model for the propulsion power consumption of HAP, utilizing aerodynamic principles and numerical analysis methods. More specifically, using CFD numerical analysis techniques for precise aerodynamic assessments, the impact of aerodynamic interference from the HAP’s hull on the propulsion system’s efficiency is thoroughly analyzed. Incorporating these detailed analyses and principles of aerodynamics, an accurate propulsion power consumption model is constructed, which leads to more reliable and accurate communication power constraints.

Optimization of HAP communication power consumption: By interacting with the generative AI agent, we propose a communication power consumption framework for the HAP. The framework comprises two key components: 1) A HAP beamforming optimization problem that aims to enhance the QoS of terrestrial users and improve the EE of the HAP communication system. 2) A QoS-enhanced energy-efficient (Q3E) beamforming algorithm based on a novel artificial neural network (ANN) architecture is designed to solve the formulated problem. By systematically integrating the crucial constraints into the training process, the designed ANN architecture enables unsupervised learning without reliance on labeled datasets.

• Finally, we conduct extensive simulations to verify the accuracy of the propulsion power consumption model and the effectiveness of the proposed beamforming algorithm. Simulation results demonstrate an average 84.3% reduction in propulsion power consumption deviation for the derived model compared to the existing model. The proposed beamforming algorithm demonstrates substantial improvements over the benchmarks, achieving a maximum 33.3% increase in QoS satisfaction ratio of users and 45% higher EE.

Notation: The upper and lower case boldface letters represent the matrices and column vectors, respectively. The definition of the imaginary unit is given by $j = \sqrt { - 1 }$ . The representation of unitary space with $M \times N$ -dimension is shown as $\mathbb { C } ^ { M \times N }$ . The right hand side $\operatorname { o f } \ { \overset { \Delta } { = } }$ denotes the definition of the left hand side. The operator of the Kronecker product of two matrices is represented by $\otimes .$ The symbols $\exp \{ \cdot \} , \log _ { 2 } \{ \cdot \} , \ln ( \cdot )$ and $\mathbb { E } \{ \cdot \}$ stand for the exponential, base-2 logarithm, natural logarithm and expectation operations, respectively. The representations of operating the inverse and Hermitian conjugate are presented as $( \cdot ) ^ { - 1 }$ and $( \cdot ) ^ { H }$ , respectively. The maximum value of a set is denoted by max{·}. The operator | · | denotes the absolute value for scalars and the cardinality for sets. The $l _ { 2 } { \mathrm { - n o r m } }$ is denoted by $\| \cdot \| _ { 2 }$

## II. GENERATIVE AI AGENT FRAMEWORK AND HAP POWER CONSUMPTION MODEL

## A. Generative AI Agent Framework

Generative AI agents surpass traditional data interaction models by engaging human users in dynamic, bidirectional information exchange [28]. In this paper, the agent serves as a retrieval-augmented and validator-gated research assistant. It compiles and presents literature-based system models and parameter tables to support our HAP study. The optimization problem is solved by our dedicated solver.

The LLM-based AI agent exemplifies generative AI appli cations [29], Fig. 1 depicts a conceptual structure of an LLM-based generative AI agent, which comprises three components: 1) Perception: This module collects raw input data and converts the data into structured, machine-interpretable semantic representations. 2) Brain: Functioning as the cognitive architecture’s central module, it processes information, executes decision-making, and resolves novel tasks through reasoning and planning. 3) Action: Guided by brain-derived inferences, the action module interacts with external environments, analyzes interaction data, and generates contextually appropriate user feedback. Below we specify how each module is instantiated in our HAP study.

![](images/872ff20d7fbd845fed4292a8ca774ad896971bfa22d35c7c35bff9a6c5e92ed4.jpg)  
Fig. 1. The conceptual architecture of LLM-based generative AI Agent: perception, brain, and action.

1) Perception Module (Data Interpretation): Task-specific prompts are designed to align LLM with interdisciplinary research objectives. Raw inputs (e.g., academic documents on massive multiple input multiple output (MIMO), HAP systems, and aerodynamics) undergo semantic analysis, chunking, and embedding. This process converts heterogeneous data into structured representations for downstream processing. Specifically, PDF documents and notes are divided by a recursive text splitter (chunk size $L _ { c } { = } 8 0 0$ , overlap $L _ { o } { = } 1 5 0 \ \mathrm { \ t o k e n s } )$ embedded using a normalized sentence encoder, and stored in a Facebook AI Similarity Search (FAISS) index with cosine similarity. We perform maximal marginal relevance (MMR) selection of k=8 passages (with λ=0.5) to balance relevance and diversity. The retrieved context is then concatenated with schema-specific prompts in the brain module.

2) Brain Module (Knowledge-Augmented Reasoning): A knowledge database is constructed from preprocessed textual content, integrating domain theories and empirical constraints. The brain module leverages RAG to retrieve contextually relevant information, enabling adaptive reasoning for decisionmaking. This phase ensures academic rigor in deriving theoretical frameworks and methodologies. In this paper, the brain first extracts the overall HAP system model from the literature. It then compiles the parameters and models required by the study according to the research objectives and needs. We call the DeepSeek-R1 model through an API, sending the retrieved text chunks and research objectives to the LLM, and use its reasoning ability to support our study. The main components include:

CFD atmosphere/flow for setup: see Sec. III. International Standard Atmosphere (ISA-1976) [30] properties at the target altitude, steady incompressible RANS with shear-stress transport (SST) $k { \mathrm { - } } \omega ,$ propellers modeled by

Multiple Reference Frame (MRF), and wall resolution $y ^ { + } \in [ 1 , 5 ]$

Communication model and optimization directions: A model that links RF transmit power with static terms. The solver follows a lexicographic-style solver policy: first maximize the number of QoS-satisfied users |Q|, then maximize energy efficiency.

To ensure consistency with system tasks and physical laws, the brain performs validation checks: 1) Pre-processing check: review document provenance and metadata, task scope (HAP altitude envelope, ISA-1976 variants), and unit systems to prevent irrelevant or inconsistent content from entering the index. 2) LLM response admission check: verify consistency of units and dimensions with this paper, assess the feasibility of CFD settings under available computational resources, confirm the aerodynamic plausibility of $P _ { \mathrm { p r o p } } ( V _ { 0 } )$ , and ensure that the communication model and optimization objectives are consistent with the HAP network architecture. 3) End-toend post-study validation: validate the fitted $P _ { \mathrm { p r o p } } ( V _ { 0 } )$ using CFD data, check curve characteristics within $V _ { 0 } \in [ 1 , 2 5 ]$ m/s, confirm RF-budget feasibility with the capped-simplex projector, and cross-check the computation and optimization results against ground test data.

3) Action Module (Closed-Loop Execution): Guided by brain-derived insights, the action module formalizes solutions into mathematical optimization problems and executes them offline in simulation. The agent iteratively refines assumptions based on offline experimental feedback (CFD and communication simulations), ensuring alignment with constraints. In this paper, the LLM assists with problem scoping and model drafting, while numerical CFD and optimization are executed by dedicated solvers rather than the LLM.

4) Technical Limitations and Potential Challenges: 1) Onplatform constraints: HAP platforms operate under strict energy budgets and weight limits; on-board compute cannot host large LLMs, while small-footprint models typically do not meet the accuracy required for safety-critical decisions. Backhaul bandwidth and latency also preclude reliable cloud inference during flight. Consequently, our agent is used offline to assist research-stage modeling and parameter preparation; numerical CFD and communication optimization are executed by dedicated solvers, not by the LLM. 2) Engineer-in-the-loop: Because current LLMs may hallucinate, all AI-inferred components are researcher-reviewed and must pass the admission checks before they parameterize simulations or optimizers. 3) Bias and robustness: AI-inferred components can inherit biases from the literature corpus (e.g., publication bias, dominant-design bias, or outdated ISA-1976 variants) and from retrieval itself (MMR selection bias).

## B. Generative AI Agent-Based Modeling of HAP Power Consumption

We operationalize the perception–brain–action loop of Sec. II-A as shown in Fig. 2: the perception pipeline prepares the corpus and index, the brain performs RAG-augmented reasoning with validator checks, and the action stage formalizes optimization and runs simulations offline.

![](images/9eaedf718de0d26350608f52ae615b932df102aee171980b06249cc7480702c7.jpg)  
Fig. 2. Generative AI Agent-based framework for HAP power consumption modeling.

Firstly, we initiate the research by posing questions to a generative AI agent based on the target problems to be investigated. The generative AI agent utilizes existing LLM to analyze the existing questions and proposes a research framework. Specifically, we inquire of the generative AI agent about the HAP system architecture and components of HAP power consumption, and which academic disciplines are involved in studying HAP power consumption. Unlike freeform dialogue, we employ structured prompts so that the agent returns literature-cited, parameterized outputs consistent with HAP system characteristics and the propulsion/communication requirements.

The HAP power consumption model encompasses several key areas: communication system power consumption, propulsion system power consumption, payload system power consumption, and environmental and maintenance system power consumption. Mathematically, the power consumption model for HAP is as follows

$$
P _ { \mathrm { H A P } } = P _ { \mathrm { c o m } } + P _ { \mathrm { p r o p } } + P _ { \mathrm { p a y l o a d } } + P _ { \mathrm { s t a n d b y } } ,\tag{1}
$$

where $P _ { \mathrm { H A P } }$ is HAP power consumption, $P _ { \mathrm { c o m } }$ is HAP communication system power consumption, $P _ { \mathrm { p r o p } }$ is HAP propulsion system power consumption, $P _ { \mathrm { p a y l o a d } }$ is HAP payload power consumption, $P _ { \mathrm { s t a n d b y } }$ is the power consumption of environmental and maintenance systems of the HAP. Among these, payload power consumption includes devices such as cameras and environmental sensors; the power consumption for environmental and maintenance systems is primarily related to thermal control, and accurate values for these components can be obtained through ground testing.<sup>1</sup> This paper will focus on exploring the power consumption modeling of the communication system and the propulsion system of the HAP.

Secondly, we refine the prompt words based on the AI agent’s research framework and existing research findings, and provide the AI agent with relevant academic documents to enhance the AI agent’s understanding and the precision of its reasoning regarding the research content. Having clarified the research focuses on the power consumption of the communication system and the propulsion system of the HAP, we proceed to review relevant academic research literature, including studies on massive MIMO [31], [32], [33], [34], [35], [36], beamforming [1], [7], [10], [11], [37], [38], [39], [40], HAP energy management [41], [42], aerodynamics [22], [43], [44], [45], [46], and other pertinent areas. These scholarly documents are then input into the knowledge database of the LLM to enhance the learning and construction of an accurate AI agent. The final parameter tables are versioned only after passing the brain-level conformance checks and are then delivered to the LLM.

Finally, upon the completion of the knowledge database construction by the AI agent, researchers can interact with the AI agent based on more detailed research objectives and content. More specifically, in the research of HAP propulsion power consumption, a precise propulsion model can be constructed based on the methods of aerodynamics combined with CFD simulation.

With the assistance of the AI agent, we can establish the communication power model as follows

$$
P _ { \mathrm { c o m } } = \xi \sum _ { k = 1 } ^ { K } \|  { \mathbf { b } } _ { k } \| _ { 2 } ^ { 2 } + P _ { \mathrm { t } } ,\tag{2}
$$

where $P _ { \mathrm { t } } = N _ { t } P _ { \mathrm { R F C } } + P _ { \mathrm { L 0 } } + P _ { \mathrm { B B } }$ . We consider a fully-digital architecture, so $N _ { \mathrm { R F } } = N _ { t }$ . Here, ξ is the PA inefficiency factor, $\mathbf { b } _ { k }$ denotes the transmit beamforming vector for user $k ,$ and $P _ { \mathrm { R F C } } , P _ { \mathrm { L O } } ,$ , and $P _ { \mathrm { B B } }$ are, respectively, the per-chain RF front-end, local oscillator, and baseband circuit powers.

Next, we introduce the modeling of HAP propulsion power consumption and the optimization of HAP communication power consumption in detail in the following two Sections.

## III. MODELING OF HAP PROPULSION POWER CONSUMPTION

This study considers a finalized HAP configuration whose hull geometry, propeller size, and placement are fixed by prior system-level optimization. The learned propeller–efficiency map $\hat { \eta } _ { p } ( V _ { 0 } )$ is therefore design-specific and not intended for cross-geometry generalization. All analyses are performed within this design. Hull–propeller interference, which isolatedpropeller theory cannot capture, is quantified using CFD. However, the modeling techniques developed in this paper are applicable to the modeling of propulsion power consumption of other HAP configurations.

An accurate propulsion-power model for a four-propeller HAP is developed using aerodynamic principles and numerical analysis, with a generative-AI agent assisting literature synthesis and parameter selection.

## A. HAP Propulsion Power Consumption Model

For a HAP flying forward at a constant airspeed of $V _ { 0 } ,$ its propulsion power consumption can be modeled as follows [22], [45]

$$
P _ { \mathrm { p r o p } } = { \frac { T V _ { 0 } } { \eta } } = { \frac { T V _ { 0 } } { \eta _ { p } \eta _ { m } } } ,\tag{3}
$$

![](images/e9b4a60d5a805b31f34e3a20d1859ec8333841dcf062fb4304d0c36000491b3f.jpg)  
Fig. 3. Comparison of power consumption obtained by the model in [22] and numerical analysis.

where $T$ is the aerodynamic drag of a HAP, η is the efficiency of a propulsion system, $\eta _ { p }$ is the efficiency of propeller, and $\eta _ { m }$ is the efficiency of motor.

In order to verify the accuracy of the propulsion power consumption model, the CFD numerical analysis technique is utilized. Fig. 3 illustrates the comparison of propulsion power consumption for a HAP at airspeeds $V _ { 0 } \in [ 1 , 2 5 ]$ m/s, as obtained from CFD numerical analysis and the model proposed in [22]. From this figure, we observe a large deviation between the analytical propulsion model and CFD. Further, the deviation grows superlinearly with airspeed. For example, when the HAP flight airspeed is 25 m/s, the deviation reaches 8367.3 W. Therefore, the existing propulsion power consumption model is inaccurate.

The aerodynamic drag depends on environmental parameters, airspeed, and HAP shape. And the aerodynamic drag model has been extensively studied [22], [43], [44], [45], [46]. Particularly, the aerodynamic drag of a HAP at a constant airspeed of $V _ { 0 }$ can be calculated by

$$
T = 0 . 5 \rho { V _ { 0 } } ^ { 2 } C _ { D } \Omega ^ { \frac { 2 } { 3 } } = 0 . 5 \rho { V _ { 0 } } ^ { 2 } C _ { D V } \Omega ^ { \frac { 2 } { 3 } } K _ { F } ,\tag{4}
$$

where $\rho , C _ { D } , C _ { D V } , K _ { F }$ , and Ω denote air density, the HAP drag coefficient, the HAP hull drag coefficient, the tail drag correction factor, and the volume of the HAP. The HAP hull drag coefficient is given by [47], [48], and [49]

$$
C _ { D V } = { \frac { 0 . 1 8 \epsilon ^ { \frac { 3 } { 1 0 } } + 0 . 2 7 \epsilon ^ { - { \frac { 6 } { 5 } } } + 1 . 0 8 \epsilon ^ { - { \frac { 2 7 } { 1 0 } } } } { \mathrm { R e } ^ { \frac { 1 } { 6 } } } } ,\tag{5}
$$

where $\epsilon = l / d$ is the slenderness ratio of a HAP, l the length of HAP, and d the width of a HAP. $\mathrm { R e } = \rho V _ { 0 } l / \mu$ is the Reynolds number, $\mu$ the dynamic viscosity.

We conduct a CFD numerical analysis to verify the accuracy of the aerodynamic drag model. Fig. 4 depicts the deviation ratio of the model from the numerical analysis results. From this figure, we can observe that the achieved deviation ratio of the model is less than 6%. Further, the deviation ratio is within 1% when the airspeed of the HAP is greater than 5 m/s.

## B. Performance Modeling of Propellers

Similar to (3), the propeller efficiency of a propeller can be calculated by

$$
\eta _ { p } = { \frac { T _ { p } V _ { 0 } } { P _ { p } } } ,\tag{6}
$$

![](images/af9a1e9537a24ed3dbc5a178a3b6a0c535fd988c5a54fe2c82bd12cac25f148d.jpg)  
Fig. 4. Deviation ratio of the aerodynamic drag model in [43] versus CFD numerical analysis.

where $T _ { p }$ is thrust of propeller, $V _ { 0 }$ is airspeed of HAP, and $P _ { p }$ is power consumption of propeller. To analyze the efficiency of a propeller, we should first analyze the kinetic characteristics of its blade.

Consider an $N _ { b }$ -blade propeller operating at freestream speed $V _ { 0 }$ and rotational speed $n _ { s } .$ . Let $r \in [ r _ { 0 } , R ]$ denote the spanwise coordinate, $b ( r )$ the local chord, $\varphi = \varphi _ { 0 } + \alpha _ { i }$ the inflow angle, and $( c _ { l } , c _ { d } )$ the sectional lift/drag coefficients. Enforcing consistency between blade-element theory and momentum theory yields the axial induction factor [50], [51]

$$
a _ { a } = \left( \frac { 4 K _ { p } \sin ^ { 2 } \varphi } { \sigma \left[ c _ { l } \cos \varphi - c _ { d } \sin \varphi \right] } - 1 \right) ^ { - 1 } , \quad \sigma = \frac { N _ { b } b } { 2 \pi r } ,\tag{7}
$$

$$
K _ { p } = \frac { 2 } { \pi } \operatorname { a r c c o s } \Bigl ( \exp \Bigl \{ - \frac { N _ { b } ( R - r ) } { 2 r \sin \varphi _ { 0 } } \Bigr \} \Bigr ) .\tag{8}
$$

With local relative speed $V = V _ { 0 } ( 1 + a _ { a } ) / \sin \varphi .$ , the thrust and shaft power follow

$$
T _ { p } = { \textstyle \frac { 1 } { 2 } } \rho V _ { 0 } ^ { 2 } N _ { b } \int _ { r _ { 0 } } ^ { R } \bigl [ c _ { l } \cos \varphi - c _ { d } \sin \varphi \bigr ] b \frac { ( 1 + a _ { a } ) ^ { 2 } } { \sin ^ { 2 } \varphi } d r ,\tag{9}
$$

$$
P _ { p } = \pi n _ { s } \rho V _ { 0 } ^ { 2 } N _ { b } \int _ { r _ { 0 } } ^ { R } \left[ c _ { l } \sin \varphi + c _ { d } \cos \varphi \right] b \frac { ( 1 + a _ { a } ) ^ { 2 } } { \sin ^ { 2 } \varphi } r d r ,\tag{10}
$$

and the efficiency is given by (6), i.e., $\eta _ { p } = T _ { p } V _ { 0 } / P _ { p }$ . These compact expressions are consistent with [50], [51] and are used for the subsequent numerical comparison and regression calibration.

According to the above theoretical derivations, we can obtain the value of $\eta _ { p }$ . Next, we verify the accuracy of the derived propeller efficiency model through CFD numerical analysis. Fig. 5 illustrates the propeller efficiency obtained by the numerical analysis and the derived model. The comparison results in Fig. 5 show that the theoretical model deviates significantly from the numerical analysis. For instance, the maximum deviation of the model from the numerical analysis is as high as 12.7%. Moreover, the deviation exceeds 10% when the flight airspeed of a HAP is greater than 12 m/s. Because a reliable closed-form proximity correction is not available, we adopt a regression model for $\eta _ { p } ( V _ { 0 } )$ based on CFD analysis. Over 1-25 m/s, both CFD and the regression indicate a mild increase in $\eta _ { p } ( V _ { 0 } )$ . However, hull proximity lowers its absolute level relative to an isolated propeller. We conducted a CFD numerical analysis to explicitly reflect the impact of the HAP hull on its propellers, and the analysis results are shown in Fig. 6.

![](images/00b0b6b4f2fa3a762f2725188f827e374f8adcaf86e7b6022c485ea0977279e3.jpg)  
Fig. 5. Comparison of propeller efficiency obtained by the model in [22] and numerical analysis.

![](images/23942cc5f588c0a4f292c9c8fb0898152c72a3ca06156cf37631220c44e061a6.jpg)  
(a) Velocity contour of a propeller operating alone

![](images/873bbc2e4acb348541b2adb348b6c2cfe05c90ba6a8d0168b64777d097409be2.jpg)  
(b) Velocity contour of a propeller installed on a HAP

![](images/ce255e181bf244ea4e8ade04323c30f8887956a67d6d103f350d37af68321ab4.jpg)  
(c) Pressure contour of a propeller operating alone

![](images/85f265576c8541520b652040b7b6a9e0e831546fed27231e0b1d99c32656b019.jpg)  
(d) Pressure contour of a propeller installed on a HAP  
Fig. 6. Comparison of velocity and pressure contours under different propeller operating conditions at an airspeed of 20 m/s.

From this figure, we can observe that when the propeller operates alone, the wake flow is regular and the velocity is faster, as shown in Fig. 6(a). When a propeller is installed on a HAP, the wake flow is subjected to turbulence, and the wake flow velocity is decreased, as shown in Fig. 6(b). As can be seen from Figs. 6(c) and 6(d), the pressure is lower when the propeller is installed on a HAP. Besides, the closer the propeller is to the HAP hull, the lower the pressure field at the front of the propeller. From Fig. 6, we can conclude that the aerodynamic interference caused by the HAP hull is the direct reason affecting the propeller efficiency. Analyzing and quantifying the aerodynamic interference is essential to achieving the accurate modeling of HAP propulsion power consumption.

TABLE I  
KEY SYMBOLS
<table><tr><td>Symbol</td><td>Meaning</td><td>Symbol</td><td>Meaning</td></tr><tr><td> $P _ { \mathrm { H A P } }$ </td><td>Total HAP power Propulsion power</td><td>κk</td><td>Rician factor SINR of user k</td></tr><tr><td>P prop</td><td>Communication power</td><td> $\mathrm { S I N R } _ { k }$ </td><td></td></tr><tr><td> $\bar { P _ { \mathrm { c o m } } }$ </td><td></td><td> $R _ { k }$ </td><td>Rate of user k</td></tr><tr><td> $\mathrm { \underline { { { P _ { p a y l o a d } } } } }$ </td><td>Payload power</td><td> $E E$ </td><td>Energy efficiency</td></tr><tr><td> $\underline { { P } } _ { \mathrm { s t a n d b y } }$ </td><td>Thermal/env. &amp; housekeeping</td><td> $\kappa , \boldsymbol { \mathcal { Q } }$ </td><td>User set, QoS-satisfied subset</td></tr><tr><td> $P _ { \mathrm { { t } } }$ </td><td>Static Radio Frequency (RF)/baseband power</td><td> $p _ { \mathrm { { k } } } , p _ { k , \mathrm { { m i n } } }$ </td><td>Power coeff., minimal coeff.</td></tr><tr><td> $\xi$ </td><td>Power Amplifier (PA) inefficiency factor</td><td> $P _ { \mathrm { { t o t } } }$ </td><td>RF transmit-power budget</td></tr><tr><td> $\mathbf { b } _ { k }$ </td><td>Beamformer for user k</td><td> $_ { T } ^ { g _ { k } , \gamma _ { k } }$ </td><td>Small-scale gain, avg. power</td></tr><tr><td> $\mathbf { W }$ </td><td>zero-forcing (ZF) beamformer</td><td></td><td>Aerodynamiċ drag</td></tr><tr><td> $\mathbf { v } _ { k }$ </td><td>uniform planar array (UPA) response (user k)</td><td>1  $\eta , \eta _ { p } , \eta _ { m }$ </td><td>System/propeller/motor efficiency</td></tr><tr><td> $N _ { t }$ </td><td>Antennas</td><td> $C _ { D } , C _ { D V }$ </td><td>Total drag coeff., hull drag coeff.</td></tr><tr><td> $K$ </td><td>users</td><td> $K _ { F }$ </td><td>Tail drag correction</td></tr><tr><td> $N ^ { x } , N ^ { y }$ </td><td>UPA elements  $\left( \mathrm { x } / \mathrm { y } \right)$ </td><td> $\Omega$ </td><td>Hull volume</td></tr><tr><td> $r ^ { x } , r ^ { y }$ </td><td>Element spacings</td><td></td><td>Air density, viscosity</td></tr><tr><td> $f _ { c }$ </td><td>Carrier fréquency</td><td> $\rho , \mu$   $i , \dot { d } , \epsilon$ </td><td>Hull length, width, slenderness</td></tr><tr><td> $B _ { w }$ </td><td></td><td> $\dot { V _ { 0 } }$ </td><td></td></tr><tr><td></td><td>System bandwidth</td><td></td><td>Airspeed</td></tr><tr><td> $N _ { 0 }$ </td><td>Noise power</td><td> $\mathrm { R e }$ </td><td>Reynolds number</td></tr></table>

## C. Aerodynamic Interference Analysis of HAP Hull

As illustrated in Fig. 6, hull–propeller interference is strongly coupled to geometry and local flow, which makes reliable closed-form corrections difficult. To remain tractable and accurate for the finalized design, we therefore learn the efficiency map $\eta _ { p } ( V _ { 0 } )$ from CFD samples and use this surrogate directly in (3).

In this way, we may obtain a tractable expression of the propeller efficiency and the HAP airspeed. Note that $P _ { \mathrm { p r o p } } ( V _ { 0 } )$ grows superlinearly with airspeed due to the $V _ { 0 } ^ { 3 }$ -like scaling in $T V _ { 0 }$ and the airspeed-dependent efficiency term. Therefore, given 25 values of HAP airspeed ranging from 1.0 m/s to 25.0 m/s, we leverage CFD numerical analysis to generate 25 values of the efficiency of the HAP propeller. We adopt an inverse-power surrogate $\hat { \eta } _ { p } ( V _ { 0 } ) = c - \alpha V _ { 0 } ^ { - \beta } ;$ ; on 25 CFD samples it attains low fit errors (e.g., $\mathrm { R M S E } = 2 . 3 3 \times 1 0 ^ { - 3 } )$ Based on these results, we attempt to capture the non-linear relationship between the propeller efficiency and the airspeed using a non-linear regression technique. We fit an inversepower surrogate $\hat { \eta } _ { p } ( V _ { 0 } ) = c - \alpha V _ { 0 } ^ { - \beta }$ to $n = 2 5$ CFD samples over $V _ { 0 } \in [ 1 , 2 5 ]$ m/s, and obtain

$$
\hat { \eta } _ { p } = - 0 . 2 V _ { 0 } ^ { - \frac { 9 } { 2 0 } } + 0 . 7 3 .\tag{11}
$$

Finally, by substituting equations (4), (5), and (11) into (3), we can recalculate the propulsion power consumption of a HAP as

$$
\begin{array} { l } { { \displaystyle P _ { \mathrm { p r o p } } = \frac { T V _ { 0 } } { \hat { \eta } _ { p } \eta _ { m } } = 0 . 5 \rho ^ { \frac { 5 } { 6 } } V _ { 0 } ^ { \frac { 1 7 } { 6 } } \mu ^ { \frac { 1 } { 6 } } \Omega ^ { \frac { 2 } { 3 } } \eta _ { m } ^ { - 1 } K _ { F } } } \\ { { \displaystyle ~ \times \frac { 0 . 1 8 l ^ { \frac { 2 } { 1 5 } } d ^ { - \frac { 3 } { 1 0 } } + 0 . 2 7 l ^ { - \frac { 4 1 } { 3 0 } } d ^ { \frac { 6 } { 5 } } + 1 . 0 8 l ^ { - \frac { 4 3 } { 1 5 } } d ^ { \frac { 2 7 } { 1 0 } } } { - 0 . 2 V _ { 0 } ^ { - \frac { 9 } { 2 0 } } + 0 . 7 3 } . } } \end{array}\tag{12}
$$

which is used throughout as the core propulsion-power relation for the finalized HAP design.

Given the obtained propulsion power consumption model, we next investigate the EE of the HAP communication system

to achieve the optimization of the HAP communication power consumption.

## D. CFD Validation, Uncertainty, and Design-Transfer Workflow

At a fixed operating altitude (20 km), we adopt ISA-1976 constant properties $( \rho , \mu )$ . Because the maximum airspeed is $V _ { 0 } ~ \le ~ 2 5$ m/s (Mach <0.1), validation uses steady, incompressible RANS; turbulence closure and key CFD settings are audited for reproducibility, summarized in Table II.

Under identical meshes and boundary conditions in STAR-CCM+ 2502, the propulsion-power differences between SST k-ω and realizable k-ε closures are 1.83% (5 m/s), 0.90% (15 m/s), and 0.13% (25 m/s), i.e., turbulence-model variability $\leq 2 \%$ . Combining this with the validated drag correlation (overall $\leq 6 \%$ , and $\leq 1 \%$ for $V _ { 0 } > 5 \mathrm { m } / \mathrm { s } )$ and the surrogatefit error for $\hat { \eta } _ { p }$ $( \mathrm { R M S E } = 2 . 3 3 \times 1 0 ^ { - 3 } ,$ ; relative $\lesssim 0 . 4 \%$ in our range), we obtain the following conservative bound for $V _ { 0 } > 5 \mathrm { m } / \mathrm { s } ;$

$$
\frac { | \Delta P _ { \mathrm { p r o p } } | } { P _ { \mathrm { p r o p } } } \ \lesssim \ 1 . 0 \% + 0 . 4 \% + 2 . 0 \% \ \approx \ 3 . 4 \% .\tag{13}
$$

This lever (i.e., 3.4%) is the uncertainty inherited by the propulsion-informed RF budget in subsequent beamforming optimization.

For a different hull/propeller layout or operating altitude, the efficiency map $\hat { \eta } _ { p } ( V _ { 0 } )$ is re-identified before updating the propulsion-informed RF budget:

1) Fix the finalized geometry and propeller placement for the new platform.

2) Run steady, incompressible RANS CFD over a discrete airspeed grid $V _ { 0 } \in \{ 1 , . . . , 2 5 \}$ m/s spanning the admissible envelope at the target altitude (ISA-1976 properties).

3) Extract $\bar { \{ \eta _ { p } ^ { \mathrm { C F D } } ( V _ { 0 } ^ { ( i ) } ) \} } _ { i = 1 } ^ { n }$ with convergence checks (residuals $\leq 1 0 ^ { - 5 } ;$ flat thrust/torque/power traces).

4) Fit a smooth, monotone surrogate $\hat { \eta } _ { p } ( V _ { 0 } )$ (e.g., inversepower family) and validate on holdout speeds.

5) Update $\begin{array} { r l r } { P _ { \mathrm { p r o p } } } & { { } = } & { T V _ { 0 } / ( \hat { \eta } _ { p } \eta _ { m } ) } \end{array}$ and refresh the propulsion-informed RF budget prior to beamforming optimization.

TABLE II  
CFD SETUP SUMMARY
<table><tr><td>Solver/physics</td><td>Steady incompressible RANS; turbulence: SST k-ω; propeller region: MRF</td></tr><tr><td>Domain size</td><td>8×5×5 (streamwise × spanwise × vertical) relative to hull length; inlet 2L upstream, outlet 5L downstream</td></tr><tr><td>BCs</td><td>Velocity inlet  $( \mathrm { T I } = 1 \% ) ,$  pressure outlet; no-slip walls</td></tr><tr><td>Mesh</td><td>Multi-block + BL; total cells  $\leq 1 2 \mathbf { M } ;$  12 prism layers; growth  $\leq 1 . 2 ;$  target  $y ^ { + } \in [ 1 , 5 ]$ </td></tr><tr><td>Convergence</td><td>Residuals  $\leq 1 0 ^ { - 5 }$  &amp; flat thrust/torque/power (drift  $< 1 \% )$ </td></tr></table>

IV. BEAMFORMING DESIGN OF HAP COMMUNICATIONS

Guided by a retrieval-augmented LLM agent (Sec. II), we adopt a lexicographic-style solver policy [52] that prioritizes QoS satisfaction over EE: we first enlarge the QoS-satisfied subset under the instantaneous RF budget, and then maximize EE over the resulting feasible set. The diminishing returns of $\mathrm { l o g } _ { 2 } ( 1 + \mathrm { S I N R } )$ motivate prioritizing QoS satisfaction before EE. According to the results retrieved from the AI agent knowledge database, optimizing power consumption of MIMO systems is crucial for achieving high EE, particularly in scenarios where a large number of antennas and users are involved. EE is commonly defined as the ratio of the achievable data rate to the total power consumed [35]. A goal of this paper is then to maximize the EE of the HAP communication system and satisfy QoS requirements of users by optimizing the transmit beamforming vectors. In contrast to directly optimizing a single weighted-sum objective, we follow the same lexicographic-style solver policy motivated by the diminishing-return structure of $\log _ { 2 } ( 1 + \mathrm { S I N R } )$

## A. System Modeling of HAP Communications

We consider a HAP equipped with a UPA consisting of $N ^ { x }$ and $N ^ { y }$ elements along the x-axis and y-axis, respectively. Consequently, the total number of antennas is given by $N _ { t } { \overset { \Delta } { = } } N ^ { x } N ^ { y }$ . The response vector of the UPA, denoted as $\mathbf { v } _ { k } .$ can be expressed as

$$
\mathbf { v } _ { k } = \mathbf { v } _ { k } ^ { x } \otimes \mathbf { v } _ { k } ^ { y } \in \mathbb { C } ^ { N _ { t } \times 1 } .\tag{14}
$$

The array response vector $\mathbf { v } _ { k } ^ { d } \in \mathbb { C } ^ { N ^ { d } \times 1 }$ for $d \in \mathcal { D } \overset { \Delta } { = } \{ x , y \}$ is defined as [53]

$$
\begin{array} { l } { { { \displaystyle { \bf v } _ { k } ^ { d } } \triangleq \frac 1 { \sqrt { N ^ { d } } } \left[ 1 , \exp \left\{ - j 2 \pi f _ { c } \frac { r ^ { d } u _ { k } ^ { d } } { c } \right\} , \right. } } \\ { { \left. \dots \cdot , \exp \left\{ - j 2 \pi f _ { c } \frac { r ^ { d } u _ { k } ^ { d } } { c } ( N ^ { d } - 1 ) \right\} \right] ^ { T } , } } \end{array}\tag{15}
$$

where $f _ { c }$ represents the carrier frequency, and c is the speed of light, $r ^ { \bar { d } }$ denotes the antenna separation of the UPA, $( \theta _ { k } ^ { x } , \theta _ { k } ^ { y } )$ represents the angle-of-departure (AoD) of the k-th user, respectively. Then the spatial-angle pair of the k-th user $( u _ { k } ^ { x } , u _ { k } ^ { y } )$ can be represented as

$$
u _ { k } ^ { x } = \sin \theta _ { k } ^ { y } \cos \theta _ { k } ^ { x } , \quad u _ { k } ^ { y } = \cos \theta _ { k } ^ { y } .\tag{16}
$$

We assume that K single-antenna users request communication services from the HAP, and the set of users is defined as ${ \mathcal { K } } { \stackrel { \Delta } { = } } \{ 1 , 2 , \dots , K \}$ . Due to the high altitude of the HAP, the relative positions between the HAP and the k-th user remain nearly unchanged over a given time period. In this work, the channel gain $g _ { k } \in \mathbb { C }$ is modeled to follow the Rician fading distribution random variable with Rician factor $\kappa _ { k }$ and power $\gamma _ { k }$ . The downlink channel for k-th user can be expressed as

$$
\mathbf { h } _ { k } = \mathbf { v } _ { k } g _ { k } \in \mathbb { C } ^ { N _ { t } \times 1 } .\tag{17}
$$

It is worth noting that the channel model adopted in this work is similar to RF channel model described in [11]. In this paper, we utilize statistical channel state information (sCSI), which remains stable over an extended period, for the design of the beamforming scheme. The received signal for k-th user can be expressed as [38]

$$
y _ { k } = \mathbf { h } _ { k } ^ { H } \sum _ { \ell = 1 } ^ { K } \mathbf { b } _ { \ell } s _ { \ell } + n _ { k } = \mathbf { h } _ { k } ^ { H } \mathbf { b } _ { k } s _ { k } + \mathbf { h } _ { k } ^ { H } \sum _ { \ell \neq k } \mathbf { b } _ { \ell } s _ { \ell } + n _ { k } ,\tag{18}
$$

where $s _ { k }$ denotes the transmitted signal for k-th user, $n _ { k }$ represents the additive white Gaussian noise (AWGN) with an average energy of $N _ { 0 } .$ , and ${ \mathbf b } _ { k } \in \ \mathbb { C } ^ { N _ { t } \times 1 }$ denotes the beamforming vector for k-th user. Based on (18), the received SINR of the k-th user can be expressed as

$$
\mathrm { S I N R } _ { k } \triangleq \frac { \left. \mathbf b _ { k } ^ { H } \mathbf h _ { k } \right. ^ { 2 } } { \sum _ { \ell \neq k } \left. \mathbf b _ { \ell } ^ { H } \mathbf h _ { k } \right. ^ { 2 } + N _ { 0 } } .\tag{19}
$$

The beamforming vectors are constrained by the available RF transmit-power budget $P _ { \mathrm { t o t } } \ [ 3 4 ]$ , which can be expressed as

$$
\sum _ { k = 1 } ^ { K } \| \mathbf { b } _ { k } \| _ { 2 } ^ { 2 } \leq \frac { P _ { \mathrm { H A P } } - P _ { \mathrm { p r o p } } - P _ { \mathrm { p a y l o a d } } - P _ { \mathrm { s t a n d b y } } - P _ { \mathrm { t } } } { \xi } \ \triangleq \ P _ { \mathrm { t o t } } .\tag{20}
$$

## B. Problem Formulation

In this paper, a beamforming strategy is devised by jointly considering the system’s EE and QoS satisfaction ratio. The user set K is divided into two subsets: Q denoting users with satisfied QoS requirements, and K \ Q containing the remaining users. The QoS satisfaction ratio is mathematically defined as $\frac { | \mathcal { Q } | } { | \mathcal { K } | }$ . Moreover, the system EE is expressed as the ratio between the achievable sum-rate and the total power consumption, formulated as [35]

$$
E E = \frac { \sum _ { k = 1 } ^ { K } R _ { k } } { P _ { \mathrm { c o m } } } ,\tag{21}
$$

where $R _ { k }$ denotes the average data rate of the k-th user, expressed as

$$
\begin{array} { r l } & { R _ { k } \triangleq B _ { w } \mathbb { E } \{ \log _ { 2 } ( 1 + \mathrm { S I N R } _ { k } ) \} } \\ & { \quad \triangleq B _ { w } \mathbb { E } \left\{ \log _ { 2 } \left( 1 + \frac { \left| \mathbf { b } _ { k } ^ { H } \mathbf { h } _ { k } \right| ^ { 2 } } { \sum _ { \ell \neq k } \left| \mathbf { b } _ { \ell } ^ { H } \mathbf { h } _ { k } \right| ^ { 2 } + N _ { 0 } } \right) \right\} . } \end{array}\tag{22}
$$

This paper aims to jointly maximize both the QoS satisfaction ratio and the EE of the HAP communication system. The optimization problem is formulated as

$$
\mathcal { P } : \operatorname* { m a x i m i z e } _ { \left\{ \mathbf { b } _ { k } \right\} _ { k = 1 } ^ { K } , \mathcal { Q } } \quad \omega E E + ( 1 - \omega ) \frac { | \mathcal { Q } | } { | K | }\tag{23a}
$$

$$
\begin{array} { r } { \mathrm { s . t . } \quad R _ { k } \geq r _ { k } , \quad \forall k \in \mathcal { Q } , } \end{array}\tag{23b}
$$

$$
{ \begin{array} { r l } { \Omega } & { \subseteq K , } \end{array} }\tag{23c}
$$

$$
\sum _ { k = 1 } ^ { K } \left\| \mathbf { b } _ { k } \right\| _ { 2 } ^ { 2 } \leq P _ { \mathrm { t o t } } ,\tag{23d}
$$

where $r _ { k }$ (in bps) denotes the QoS requirement of user $k ,$ and ω is a weight coefficient. Since $B _ { w }$ is in Hz, $r _ { k } / B _ { w }$ is in bit/s/Hz, consistent with $\log _ { 2 } ( \cdot )$

## C. Beamforming Algorithm Design

To simplify the expected calculation, we utilize Jensen’s inequality to estimate the achievable data rate with an upper bound approximation $R _ { k }$ , as follows

$$
\begin{array} { r } { R _ { k } \leq \bar { R } _ { k } \triangleq B _ { w } \log _ { 2 } \left( 1 + \frac { {  { \mathbb E } } \left\{ \left| {  { \mathbf E } } _ { k } ^ { H } {  { \mathbf h } } _ { k } \right| ^ { 2 } \right\} } { {  { \mathbb E } } \left\{ \sum _ { \ell \neq k } \left| {  { \mathbf b } } _ { \ell } ^ { H } {  { \mathbf h } } _ { k } \right| ^ { 2 } \right\} + N _ { 0 } } \right) } \\ { = B _ { w } \log _ { 2 } \left( 1 + \frac { \gamma _ { k } \left| {  { \mathbf v } } _ { k } ^ { H } {  { \mathbf b } } _ { k } \right| ^ { 2 } } { \sum _ { \ell \neq k } \gamma _ { k } \left| {  { \mathbf v } } _ { k } ^ { H } {  { \mathbf b } } _ { \ell } \right| ^ { 2 } + N _ { 0 } } \right) . } \end{array}\tag{24}
$$

In the remainder of this section, we use $\bar { R } _ { k }$ as a tractable surrogate of the ergodic rate. For notational simplicity, we drop the bar and denote the surrogate rate by $R _ { k }$ hereafter.

By employing the ZF method, we effectively mitigate the cross-interference among different users [54], and we define a digital beamformer W, as follows

$$
\mathbf { W } = \mathbf { V } \left( \mathbf { V } ^ { H } \mathbf { V } \right) ^ { - 1 } \in \mathbb { C } ^ { N _ { t } \times K } ,\tag{25}
$$

where $\mathbf { V } = \left\{ \mathbf { v } _ { 1 } , \mathbf { v } _ { 2 } , \ldots , \mathbf { v } _ { K } \right\}$ . Then the beamforming vector $b _ { k }$ for user k can be calculated as follows

$$
\begin{array} { r } { \mathbf { b } _ { k } = p _ { k } \mathbf { w } _ { k } , } \end{array}\tag{26}
$$

where $\mathbf { w } _ { k }$ is the k-th column of the matrix W, and $p _ { k }$ is the k-th user power coefficient.

Thus, we can transform the optimization problem (23a) into the following

$$
\mathcal { P } : \operatorname* { m a x i m i z e } _ { \{ p _ { k } \} _ { k = 1 } ^ { K } , \mathcal { Q } } \quad \omega \frac { \sum _ { k = 1 } ^ { K } R _ { k } } { P _ { \mathrm { c o m } } } + ( 1 - \omega ) \frac { | \mathcal { Q } | } { | K | }\tag{27a}
$$

$$
\mathrm { s . t . } R _ { k } \triangleq B _ { w } \log _ { 2 } \left( 1 + \frac { \gamma _ { k } | p _ { k } | ^ { 2 } } { N _ { 0 } } \right) \geq r _ { k } , \quad \forall k \in \mathcal { Q } ,\tag{27b}
$$

$$
\mathcal { Q } \subseteq \mathcal { K } ,\tag{27c}
$$

$$
\sum _ { k = 1 } ^ { n } \left\| p _ { k } \mathbf { w } _ { k } \right\| _ { 2 } ^ { 2 } \leq P _ { \mathrm { t o t } } .\tag{27d}
$$

The logarithmic relationship between rate and SINR $( R _ { k }$ ∝ $\log _ { 2 } ( 1 + \mathrm { S I N R } _ { k } ) )$ leads to a strictly concave power-rate curve, implying diminishing marginal returns in power efficiency. Beyond certain SINR thresholds, achieving a unit rate improvement requires superlinear power growth. Consequently, we follow a lexicographic-style solver policy: (1) determine the largest QoS-satisfied subset Q via the feasibility test below; (2) with Q fixed, maximize EE over the corresponding feasible set under (27d). Under the ZF structure with sCSI, let $p _ { k , \mathrm { m i n } }$ be the minimal per-user powers defined in (28), and let $\begin{array} { r } { C ( S ) = \sum _ { k \in \cal S } \| p _ { k , \operatorname* { m i n } } \mathbf { w } _ { k } \| _ { 2 } ^ { 2 } } \end{array}$ be the minimum budget to make users in $s$ feasible. Then selecting users by the ascending order of $\| p _ { k , \operatorname* { m i n } } \mathbf { w } _ { k } \| _ { 2 } ^ { 2 }$ (greedy) maximizes |Q| subject to $C ( \mathcal { Q } ) \leq P _ { \mathrm { t o t } }$ . Since $C ( \cdot )$ is additive and nonnegative, the problem reduces to a cardinality maximization under a single knapsack with items of weights $\| p _ { k , \operatorname* { m i n } } \mathbf { w } _ { k } \| _ { 2 } ^ { 2 }$ and identical unit values. The greedy by nondecreasing weights attains an optimal solution. With |Q| fixed, maximizing EE over the feasible face yields the optimal solution of the second stage under the proposed decomposition.

The minimum required power coefficient $p _ { k , \mathrm { m i n } }$ to satisfy QoS requirements $r _ { k }$ for the k-th user can be calculated by

$$
p _ { k , \mathrm { m i n } } = \sqrt { \frac { N _ { 0 } \left( 2 ^ { r _ { k } / B _ { w } } - 1 \right) } { \gamma _ { k } } } .\tag{28}
$$

This follows from $R _ { k } = B _ { w } \log _ { 2 } ( 1 + \mathrm { S I N R } _ { k } )$ under the $\mathrm { Z F }$ structure.

Based on (28), the minimum transmit power required to satisfy the QoS requirements of all users is given by $P _ { e _ { m i n } } =$ $\begin{array} { r } { \sum _ { k = 1 } ^ { K } \left\| p _ { k , \operatorname* { m i n } } \mathbf { w } _ { k } \right\| _ { 2 } ^ { 2 } } \end{array}$ . Accordingly, the constraint in (27d) can be rewritten as

$$
P _ { e _ { m i n } } \leq P _ { \mathrm { t o t } } .\tag{29}
$$

This formulation leads to two distinct cases, as described below:

Case 1 (Full User QoS Satisfaction): If (29) holds, all users achieve or exceed their QoS requirements $( R _ { k } \ge$ $r _ { k } , \ \forall k \in \mathcal { K } )$ , resulting in $| \mathcal { Q } | = | \mathcal { K } |$ . Then problem $\mathcal { P }$ can be transformed into

$$
\mathcal { P } _ { 1 } : ~ \operatorname* { m a x i m i z e } _ { \{ p _ { k } \} _ { k = 1 } ^ { K } } ~ \frac { \sum _ { k = 1 } ^ { K } R _ { k } } { P _ { \mathrm { c o m } } }\tag{30a}
$$

$$
\mathrm { s . t . } p _ { k } \geq p _ { k _ { \mathrm { m i n } } } , \forall k \in \mathcal { K } ,\tag{30b}
$$

$$
\sum _ { k = 1 } ^ { K } \left\| p _ { k } \mathbf { w } _ { k } \right\| _ { 2 } ^ { 2 } \leq P _ { \mathrm { t o t } } .\tag{30c}
$$

Case 2 (Partial QoS Satisfaction): If (29) is violated, at least one user fails to meet its QoS requirement $( \mathcal { Q } \subset \mathcal { K } )$ To maximize the number of QoS-satisfied users |Q|, a prioritization strategy is adopted: The magnitude of the power allocated to all users is sorted in ascending order based on their minimum power demands. Let $k = g ( i )$ , where the function $g \ : \ i \  \ k , \ i \ \in \ K$ , and we sequentially allocate power to users $\{ g ( i ) \}$ . Mathematically, users are ordered according to the following expression

$$
\begin{array} { r l } & { \left\| p _ { g ( { 1 } ) } \mathbf { w } _ { g ( { 1 } ) } \right\| _ { 2 } ^ { 2 } \leq \ldots \leq \left\| p _ { g ( { i } ) } \mathbf { w } _ { g ( { i } ) } \right\| _ { 2 } ^ { 2 } } \\ & { \leq \ldots \leq \left\| p _ { g ( K ) } \mathbf { w } _ { g ( K ) } \right\| _ { 2 } ^ { 2 } . } \end{array}\tag{31}
$$

This ordering scheme ensures that users with lower power requirements are prioritized, thereby systematically expanding |Q|. The above ordering can be interpreted as a greedy solution to the cardinality-constrained feasibility problem over (27d); it is optimal for the ZF-based structure because each user’s minimal feasible power contributes additively to (27d). The maximum admissible set is then determined by

![](images/a8c616b224733c22ab8f8bbb30834ea2ac8fa334212aa2aa2a0613506e5b2899.jpg)  
Fig. 7. The ANN architecture that has been contemplated provides a resolution to Problem (27a).

$$
\mathcal { Q } = \{ g ( 1 ) , \ldots , g ( m ) \} ,\tag{32}
$$

where $m = \operatorname* { m a x } \bigg \{ n \bigg | \sum _ { i = 1 } ^ { n } \left\| p _ { g ( i ) } \mathbf { w } _ { g ( i ) } \right\| _ { 2 } ^ { 2 } \leq P _ { \mathrm { t o t } } \bigg \} .$

After allocating minimum required power $p _ { k _ { \mathrm { m i n } } }$ to users in $\mathcal { Q } ,$ the remaining power budget $\begin{array} { r l r } { P _ { \mathrm { t o t } } ^ { \prime } } & { { } = } & { P _ { \mathrm { t o t } } - } \end{array}$ $\begin{array} { r } { \sum _ { i = 1 } ^ { m } \left\| p _ { g ( i ) } \mathbf { w } _ { g ( i ) } \right\| _ { 2 } ^ { 2 } } \end{array}$ is utilized to enhance EE for users in $\kappa \backslash \mathcal { Q } .$ . Then problem $\mathcal { P }$ can be transformed into

$$
\mathcal { P } _ { 2 } : \begin{array} { l l } { \operatorname* { m a x i m i z e } } & { \frac { \sum _ { k \in \kappa \backslash \mathcal { Q } } R _ { k } } { \{ p _ { k } \} _ { k \in \kappa \backslash \mathcal { Q } } } } \end{array}\tag{33a}
$$

$$
\mathrm { s . t . } \sum _ { k \in \mathcal { K } \backslash \mathcal { Q } } \left\| p _ { k } \mathbf { w } _ { k } \right\| _ { 2 } ^ { 2 } \leq P _ { \mathrm { t o t } } ^ { \prime } .\tag{33b}
$$

Both problems $\mathcal { P } _ { 1 }$ and $\mathcal { P } _ { 2 }$ are non-convex optimization problems. The AI agent generates multiple candidate approaches for their solutions, including the sequential least squares quadratic programming (SLSQP) and ANN methods. This paper employs the SLSQP method and develops an ANN method to solve the optimization problem, and compares the performance of these methods.

The proposed ANN method integrates inequality constraints into neural network training, enabling direct optimization from problem formulation equations without requiring labeled data, the framework of the ANN method is depicted in Fig. 7. The network minimizes the barrier-augmented EE objectives in (34)–(35); feasibility is enforced by the in-loop projection operator described in Algorithm 1. For the ANN method, we design dedicated loss functions corresponding to optimization problems $\mathcal { P } _ { 1 }$ and $\mathcal { P } _ { 2 }$ as

$$
\begin{array} { r l } & { \ell _ { s , \mathrm { o u t } } ^ { \perp } = \operatorname* { m i n i m i t i p } _ { x \in - 1 } \frac { B _ { w } \sum _ { k = 1 } ^ { K } \log _ { 2 } ( 1 + \frac { \gamma _ { s } \lfloor n \rfloor ^ { 2 } } { N _ { 0 } } ) } { P _ { \mathrm { c o u t } } } } \\ & { \phantom { \frac { 1 } { 1 } } - \lambda ( \displaystyle \sum _ { k = 1 } ^ { K } \ln ( p _ { k } - p _ { k , \mathrm { a n } } + \varepsilon )  } \\ & { \phantom { \frac { 1 } { 1 } } + \ln ( P _ { 0 \mathrm { c o } } - \displaystyle \sum _ { k = 1 } ^ { K } \lVert p _ { k } w _ { k } \rVert _ { 2 } ^ { 2 } + \varepsilon ) ) , } \\ & { \ell _ { s , \mathrm { o u t } } ^ { \perp } = \operatorname* { m i n i m i t i p } _ { x \in - 1 } \frac { B _ { w } \sum _ { k \in \mathcal { K } \backslash \mathcal { C } } \log _ { 2 } ( 1 + \frac { \gamma _ { s } \lfloor n \rfloor ^ { 2 } } { N _ { 0 } } ) } { P _ { \mathrm { c o m } } } } \\ & { \phantom { \frac { 1 } { 1 } } - \lambda \ln ( \displaystyle P _ { \mathrm { m a } } ^ { \varepsilon } - \displaystyle \sum _ { k \in \mathcal { K } \backslash \mathcal { C } } \lVert p _ { k } w _ { k } \rVert _ { 2 } ^ { 2 } + \varepsilon ) , } \end{array}\tag{34}
$$

(35)

where $\lambda > 0$ is the barrier weight, and $\varepsilon > 0$ is a small constant (set to $1 0 ^ { - 6 } )$ to keep the log arguments strictly positive. In implementation, each slack term is evaluated as ln $\left( \operatorname* { m a x } \{ x , \varepsilon \} \right)$ to avoid numerical issues when the slack approaches zero. We adopt direct constrained learning with an in-loop feasibility projector (Algorithm 1). At every forward pass we enforce $p _ { k } \ge p _ { k , \mathrm { m i n } }$ and $\lVert \mathbf { W p } \rVert _ { 2 } ^ { 2 } \leq P _ { \mathrm { t o t } } .$ , thereby satisfying (27d) and all per-user lower bounds. The network then minimizes the barrier-augmented EE objectives with penalty parameter λ. Training uses Adam with early stopping (patience $P { = } 5 0 .$ , max epochs = 2000). The methodological novelty is twofold: 1) a lexicographic-style solver policy with a provably optimal greedy feasibility stage under ZF beamforming with statistical CSI (ZF+sCSI). 2) an in-the-loop capped-simplex feasibility projector that enforces all power and QoS constraints at every forward pass.

```latex
Algorithm 1 Training Loop for the ANN Solver
INPUT: sCSI $\{ \gamma _ { k } , \mathbf { V } \}$ , QoS $\overline { { \left\{ { r _ { k } } \right\} } }$ , budget $P _ { \mathrm { { t o t } } }$ , Adam,
max epochs= 2000, patience P=50.
1: Precompute: $\begin{array} { r l r } { { \bf W } } & { { } \ = \ } & { { \bf V } ( { \bf V } ^ { H } { \bf V } ) ^ { - 1 } } \end{array}$ , p<sub>k,min</sub>
$\sqrt { \frac { N _ { 0 } ( 2 ^ { r _ { k } / B _ { w } } - 1 ) } { \gamma _ { k } } }$
2: function NET(V, {γ<sub>k</sub>}, {r<sub>k</sub>}, P<sub>tot</sub>)
3: return raw $\tilde { \textbf { p } } \in \ \mathbb { R } ^ { K }$ from the feed-forward MLP
(Sec. IV-B).
4: end function
5: function PROJECT(p˜, Q)
6: $m _ { k } = p _ { k , \mathrm { m i n } }$ if k ∈ Q else 0.
7: $\hat { p } _ { k } = \operatorname* { m a x } ( \tilde { p } _ { k } , m _ { k } )$ for all k.
8: $\begin{array} { r } { c _ { k } = \| \mathbf { w } _ { k } \| _ { 2 } ^ { 2 } , P _ { m } = \sum _ { k } c _ { k } m _ { k } ^ { 2 } , P _ { 0 } = \sum _ { k } c _ { k } \hat { p } _ { k } ^ { 2 } . } \end{array}$
9: if $P _ { 0 } \leq P _ { \mathrm { t o t } }$ then
10: return pˆ.
11: else
12: $\begin{array} { r } { \alpha = \frac { P _ { \mathrm { t o t } } - P _ { m } } { P _ { 0 } - P _ { m } } ; \alpha \gets \operatorname* { m i n } \{ 1 , \operatorname* { m a x } \{ 0 , \alpha \} \} . } \end{array}$
13: $p _ { k } = { \sqrt { m _ { k } ^ { 2 } + \alpha ( { \hat { p } } _ { k } ^ { 2 } - m _ { k } ^ { 2 } ) } }$ for all k.
14: return p.
15: end if
16: end function
17: for epoch = 1 to max epochs do
18: for each minibatch do
19: $\tilde { \mathbf { p } } = \mathrm { N E T V } , \{ \gamma _ { k } \} , \{ r _ { k } \} , P _ { \mathrm { t o t } } ; \mathbf { p } = \mathrm { P R O J E C T } \tilde { \mathbf { p } } , \mathcal { Q } .$
20: $\ell = \ell _ { \mathrm { s o f t } } ^ { 1 }$ if Q=K else $\ell _ { \mathrm { s o f t } } ^ { 2 } ;$ Adam update.
21: end for
22: Validate EE; early stop if no improvement for P
epochs.
23: end for
24: Output: trained weights $\Theta ^ { \star } .$
```

The input of neural network comprises the UPA response vector V, HAP’s power budget $P _ { \mathrm { t o t } } ,$ and QoS requirement $r _ { k } ,$ while the output of the neural network is the optimized power coefficients $\left\{ p _ { k } \right\}$ . The parameters of the system utilized within the optimization procedure are delineated in Section V. In the ANN method, a five-tier feedforward fully-connected neural network architecture is employed, characterized by sequential layer dimensions of K, 64, 64, 32, and 32 neurons. We ran a lightweight ablation over hidden-layer depth {2, 3, 4, 5} and width {32, 64, 128}. After fine-tuning, a 4-hidden-layer architecture with widths [64, 64, 32, 32] provides the best EE–stability trade-off and is adopted throughout. Each layer is followed by a rectified linear unit (ReLU) activation function except for the fifth layer.

Algorithm 2 QoS-Enhanced Energy-Efficient (Q3E) Beam  
forming Algorithm   
INPUT: UPA response vector $\left\{ { \bf v } _ { k } \right\}$ ; HAP’s power budget $P _ { \mathrm { t o t } } ;$   
QoS requirement set $\{ r _ { k } \}$   
1: Compute the beamforming vectors $\left\{ { \bf w } _ { k } \right\}$ based on the   
UPA response vector $\left\{ { \bf v } _ { k } \right\}$   
2: Calculate (28) to obtain $p _ { k , \mathrm { m i n } } .$   
3: if Condition (29) is satisfied then   
4: Update $\mathcal { Q } = \kappa$ and solve problem $\mathcal { P } _ { 1 }$ using either the   
ANN method or the SLSQP method to obtain $\left\{ p _ { k } \right\}$   
5: else   
6: Calculate (32) to obtain Q and update $\begin{array} { r l } { p _ { k } } & { { } = } \end{array}$   
$p _ { k , \operatorname* { m i n } } , \forall k \in \mathcal { Q } .$   
7: Solve problem $\mathcal { P } _ { 2 }$ using either the ANN method or the   
SLSQP method to obtain $\{ p _ { k } \}$   
8: end if   
OUTPUT: The satisfied-user set $\mathcal { Q }$ and the optimized power   
coefficients $\{ p _ { k } \}$

The following Q3E algorithm presents the core procedures for solving the optimization problem P. Note that ω is only used in the weighted-sum baselines for comparison; Q3E follows a lexicographic-style solver policy rather than directly optimizing the weighted-sum objective.

Then, we evaluate the computational complexity of the algorithm. This complexity is primarily determined by whether all users meet their QoS requirements. We assume that the probability of all users meeting their QoS requirements is $p .$ If all users achieve their QoS requirements, the complexity of solving problem $\mathcal { P } _ { 1 }$ is related to the use of the ANN method and the ${ \mathrm { S L S Q P } }$ method. The computational complexity of training neural network is $O \left( T _ { 1 } \sum _ { l = 1 } ^ { L } n _ { l } ^ { 2 } \right)$ , where $T _ { 1 }$ represents the number of training epochs, $L$ represents the number of network layers, and $n _ { l }$ represents the number of neurons in the l-th layer. The complexity of the SLSQP method is $O ( T _ { 2 } | \mathcal { K } | ^ { 3 } )$ , where $T _ { 2 }$ is the number of SLSQP iterations. If some users cannot achieve their QoS constraints, the complexity of solving problem $\mathcal { P } _ { 2 }$ is related to the ANN method and the SLSQP method, as well as the number of users not meeting QoS requirements. The SLSQP method is similar to the situation where all users achieve their QoS requirements, but it only optimizes for some users, so its complexity is $O ( T _ { 2 } ( | K | -$ $| \mathcal { Q } | ) ^ { 3 } )$ . In addition, the neural network training is the same as the situation where all users achieve their QoS requirements. Besides, a quick sort approach is utilized to obtain (31), the computational complexity is then $O ( | K | \log | K | )$ . Overall, the computational complexity of Algorithm 1 is $O ( N _ { t } ^ { 3 } +$ |K|+p min $\{ ( T _ { 1 } \sum _ { l = 1 } ^ { L } n _ { l } ^ { 2 } , T _ { 2 } | { \cal K } | ^ { 3 } \} + ( 1 - p ) | { \cal K } |$ log |K| min $\left\{ \begin{array} { l l }  T _ { 1 } \sum _ { l = 1 } ^ { L } \dot { n _ { l } ^ { 2 } } , T _ { 2 } \bigl ( \left| \mathcal { K } \right| - \left| \boldsymbol { \mathcal { Q } } \right| \bigr ) ^ { 3 } \biggr ) \right\} \end{array}$

## V. NUMERICAL SIMULATION RESULTS

In this section, we assess the accuracy of the proposed propulsion power-consumption model and evaluate the performance of the proposed beamforming algorithms for the HAP communication system.

## A. Comparison Algorithms and Parameter Setting

To verify the accuracy of the proposed model, we compare it with the model in [22] and with CFD numerical analysis results obtained using STAR-CCM+ software. All CFD validations use incompressible steady RANS with SST k–ω at ISA-1976 properties for $h = 2 0 \mathrm { { k m } }$ (Mach <0.1). As previously stated, the proposed algorithm prioritizes user QoS satisfaction ratio and EE. To validate its performance, we evaluate four benchmark algorithms: 1) a QoS-satisfaction beamforming algorithm that maximizes the number of users meeting their QoS targets under a power constraint [38]. 2) a max- $\mathcal { R } _ { k }$ algorithm that maximizes the sum rate under the same constraint [38]. 3) a Proximal Policy Optimization (PPO) benchmark that learns to optimize the composite objective under the power constraint [55]. 4) an Ant Colony Optimization for Continuous Domains (ACOR) benchmark that searches the continuous power-allocation space to optimize the same objective [56]. The comparison algorithms are implemented on PyTorch 2.5, SciPy 1.9 and Python 3.9, and a PC configured with Core i7, 16G RAM, and Windows 10 OS is used.

We consider a HAP operating at 20 km altitude [1], stationed at a predefined location to provide communication services for ground users with three distinct QoS levels [57]: high, medium, and low. The QoS thresholds for these levels are defined as: High QoS: 60 Mbps < Data rate $\leq \mathrm { 9 0 M b p s } ,$ Medium QoS: 30 Mbps < Data rate $\leq 6 0 \mathrm { M b p s } ,$ Low QoS: Data rate $\leq 3 0 \mathrm { M b p s } .$ . The parameters related to the HAP are set as follows: the length $l = 1 4 0 \mathrm { m } .$ , the width $d = 3 4 \mathrm { m }$ the total volume $\Omega \ = \ 8 5 0 0 0 \ \mathrm { m } ^ { 3 } .$ , the tail drag correction factor $K _ { F } = 1 . 1 2$ , the efficiency of motor $\eta _ { m } = 0 . 8 5$ , and the maximum flight airspeed is 25 m/s. The environmental parameters follow ISA-1976 [45] and are set as follows: the air density $\rho ~ = ~ 0 . 0 8 8 0 3 \mathrm { k g } / \mathrm { m } ^ { 3 }$ , and the dynamic viscosity $\mu = 1 . 4 2 1 6 \times 1 0 ^ { - 5 } \mathrm { P a } { \cdot } \mathrm { s }$ . In addition, each propeller has three blades(3 m radius for each blade), and the distance between a propeller and the HAP hull is 0.72 m. The parameters related to HAP communications are set as follows [1], [36]: system bandwidth $B _ { w } = 1 0  { \mathrm { M H z } }$ , Rician factor $\kappa _ { k } = 1 2 { \mathrm { d B } }$ , number of antennas $N ^ { x } \times N ^ { y } = 1 2 \times 1 2$ , number of users $K = 9 ,$ antenna spacing $r ^ { x } = r ^ { y } = \lambda / 2$ with $\lambda = c / f _ { c } ,$ , inefficiency of power amplifier ξ = 2, static power consumption of baseband beamformer $\begin{array} { r } { P _ { \mathrm { B B } } ~ = ~ 2 0 0 \mathrm { { m W } } , } \end{array}$ , static power consumption of local oscillator $P _ { \mathrm { L O } } = 5 \mathrm { m W } ,$ , per-RF chain power consumption $P _ { \mathrm { R F C } } = 3 3 8$ mW. Besides, the channel power is defined as $\begin{array} { r } { \gamma _ { k } \ = \ G _ { \mathrm { H A P } } G _ { \mathrm { u s e r } } N _ { t } \left( \frac { c } { 4 \pi f _ { c } h } \right) ^ { \frac { } { } } } \end{array}$ 2 with the antenna gains of the transmitter and the receiver $G _ { \mathrm { H A P } } = G _ { \mathrm { u s e r } } = 3 \mathrm { d B }$ , carrier frequency $f _ { c } = 2 1 0 0 \mathbf { M } \mathrm { H z } .$ , and the speed of light $c = 3 { \times } 1 0 ^ { 8 }$ m/s.

## B. Performance Evaluation

1) Propulsion Power Consumption Model Simulation: We simulate the task scenario of a HAP performing wind-resistant flight for station-keeping above a designated location. We plot the tendency of the propulsion power consumption over the HAP flight airspeed and the deviation ratios of different propulsion power consumption models in Fig. 8. From this figure, we can observe: 1) Propulsion power consumption increases significantly with flight airspeed, exhibiting a superlinear growth pattern. 2) The analytical results obtained from the derived model show close agreement with numerical simulations, demonstrating better accuracy than existing models. 3) The maximum deviation ratio of the derived model remains below 6%, with deviations constrained within 5% when airspeed exceeds 3 m/s. This represents a substantial improvement over the model in [22] which shows deviations exceeding 20%. 4) Fig. 3 reveals an additional energy penalty caused by aerodynamic interference between the HAP hull and propulsion system, particularly noticeable at higher airspeeds.

![](images/11b0d58c1fe59069673b0e5726a6a304b8f5c4032f7ead2b0c60fa3ba35e8f31.jpg)  
Fig. 8. Propulsion power and deviation ratios for the derived model.

TABLE III  
ABLATION ON SOFT-LOSS AND SCALING
<table><tr><td>Variant</td><td>Feasibility (%)</td><td>Mean-Overshoot (W)</td><td>Mean EE (Mbps/W)</td></tr><tr><td>Q3E (ANN)</td><td>100.0</td><td>0.00</td><td>2.976</td></tr><tr><td>Ablation-1 (no soft loss)</td><td>100.0</td><td>0.00</td><td>2.822</td></tr><tr><td>Ablation-2 (no scale)</td><td>64.7</td><td>37.9</td><td></td></tr></table>

To further evaluate the model accuracy, a comparative analysis was conducted between the derived model, the benchmark model in [22], and the CFD numerical analysis results. The derived model shows the closest agreement with the CFD results. In particular, it achieves an average 84.3% reduction in propulsion power deviation compared with the benchmark model.

2) Beamforming Design Algorithms Simulation: With an accurate propulsion power consumption model, we can obtain an accurate communication power constraint. Next, a realistic scenario is simulated, where a HAP provides communication services to ground users with three distinct QoS requirement levels, each corresponding to three user terminals. As shown in Figs. 9 and 10, the Q3E algorithm is evaluated against four benchmarks: QoS-satisfaction, max- $R _ { k } ,$ , PPO, and ACOR. The ablation in Table III shows that removing the scaling module yields frequent infeasibility under tight budgets (hence EE is not reported), while removing the soft-loss module preserves feasibility but slightly reduces EE relative to full Q3E(ANN).

Fig. 9 shows that Q3E, QoS-satisfaction, and PPO exhibit similar monotonic gains with increasing power and reach full satisfaction around 250 W, while ACOR rises more gradually and catches up as the budget relaxes. By contrast, max- $R _ { k }$ plateaus near 66% over 70–400 W since it optimizes sum-rate rather than the count of QoS-satisfied users.

![](images/874d0c8cf7fb7ae98e73263ff7ead2e8e334c2d3e1fb3bc0910571db1b5db6cd.jpg)  
Fig. 9. The QoS satisfaction ratio versus communication power constraints for five beamforming methods.

![](images/9fed30a8b708ed7573738b926d4c75bf79e82813b89c06a6caa84466ce057d61.jpg)  
Fig. 10. The EE performance versus communication power constraints for five beamforming methods.

Fig. 10 compares EE from 70 to 600 W. Key findings: 1) Q3E versus QoS-satisfaction: Q3E is about 35–45% higher at 90–150 W and about 8–10% higher at 300 W or above because it optimizes EE rather than only the satisfied user count. 2) Q3E versus PPO: Both show steps near 140, 200, and 250 W as more QoS users activate. Q3E is higher by about 5–15% under tight to mid constraints and about 10–25% when the budget is 300 W or above. 3) Q3E versus ACOR: Around 150 W, Q3E is about 15% lower. For budgets of 300 W or above, they converge, with Q3E higher on average by 1–4%. 4) Q3E versus max- $R _ { k } \colon$ Q3E is 8–12% lower at 70–110 W and up to about 15% lower at 140–300 W. For budgets of 300 W or above, Q3E is 10–25% higher, consistent with max- $\mathbf { \mathcal { R } } _ { k }$ continuing to chase throughput when it is no longer EE-optimal. 5) Q3E(ANN) versus Q3E(SLSQP): Both variants show the same stepwise trend as additional QoS users become active. Q3E(SLSQP) is slightly better only at 70, 250, and 260 W. At all other budgets it falls below Q3E(ANN).

Overall, the interactive generative AI scheme facilitates solving interdisciplinary problems by seamlessly integrating domain-specific knowledge. The neural network has a built-in feasibility projector. It also uses a barrier loss. These features make sure the solution always meets the constraints during training and deployment.

## VI. CONCLUSION

This paper studied power allocation for HAP communications by jointly modeling propulsion power and optimizing communication power. Guided by a generative AI agent, we developed an accurate propulsion power model that captures hull-propeller aerodynamic interference via aerodynamic principles and numerical analysis. Compared with the benchmark, it reduces the average deviation by 84.3%; at $V _ { 0 } { = } 2 5$ m/s, the error drops from 8367.3 W to 85.32 W (98:1), enabling substantially tighter system power budgeting and more reliable communication power allocation. Building on this model, we formulated a beamforming optimization problem and proposed an ANN-based constrained training approach that requires no supervised datasets. Under the same communicationpower constraints, Q3E achieves the highest QoS satisfaction ratio among the evaluated baselines, and typically attains higher energy efficiency (EE) at the same QoS satisfaction ratio. Overall, simulations validate both the propulsion-power modeling accuracy and the effectiveness of the proposed beamforming optimization.

This study targets a single finalized HAP and a static sCSI model; multi-HAP cooperation and heterogeneous use cases are out of scope. Next, we will extend to mobile/heterogeneous scenarios with cooperative multi-HAP beamforming and co-optimize power and trajectory for joint aero–propulsion–communication design.

## ACKNOWLEDGMENT

Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not reflect the views of the National Research Foundation, Singapore.

## REFERENCES

[1] A. A. Shamsabadi, A. Yadav, and H. Yanikomeroglu, “Enhancing nextgeneration urban connectivity: Is the integrated HAPS-terrestrial network a solution?,” IEEE Commun. Lett., vol. 28, no. 5, pp. 1112–1116, May 2024.

[2] Y. Xiao et al., “Space-air-ground integrated wireless networks for 6G: Basics, key technologies, and future trends,” IEEE J. Sel. Areas Commun., vol. 42, no. 12, pp. 3327–3354, Dec. 2024.

[3] X. Cao, X. Su, P. Yang, Y. Gao, D. Oliver Wu, and T. Q. S. Quek, “Survey on near-space information networks: Channel modeling, transmission, and networking perspectives,” IEEE Commun. Surveys Tuts., vol. 28, pp. 672–715, Mar. 10, 2026, doi: 10.1109/ COMST.2025.3549523.

[4] P. Ramezani, B. Lyu, and A. Jamalipour, “Toward RIS-enhanced integrated terrestrial/non-terrestrial connectivity in 6G,” IEEE Netw., vol. 37, no. 3, pp. 178–185, May 2023.

[5] H. Liu et al., “Near-space communications: The last piece of 6G space–air–ground–sea integrated network puzzle,” Space: Sci. Technol., vol. 4, p. 0176, Aug. 2024.

[6] A. Puguang, S. Yang, S. Jiazheng, L. Jinlong, P. Yang, and C. Xianbin, “Survey on HA2G and A2A channel measurement and modeling for airborne maneuvering networks,” Chin. J. Aeronaut., vol. 39, no. 5, May 24, 2026, Art. no. 104036, doi: 10.1016/j.cja.2025.104036.

[7] M. Wu, Z. Gao, Z. Wang, D. Niyato, G. K. Karagiannidis, and S. Chen, “Deep joint semantic coding and beamforming for near-space airshipborne massive MIMO network,” IEEE J. Sel. Areas Commun., vol. 43, no. 1, pp. 260–278, Jan. 2025.

[8] F. Salehi, M. Ozger, and C. Cavdar, “Reliability and delay analysis of 3-dimensional networks with multi-connectivity: Satellite, HAPs, and cellular communications,” IEEE Trans. Netw. Service Manage., vol. 21, no. 1, pp. 437–450, Feb. 2024.

[9] H. Sun, Y. Zhou, H. Zhang, L. Ale, H. Dai, and N. Zhang, “Joint optimization of caching, computing, and trajectory planning in aerial mobile edge computing networks: An MADDPG approach,” IEEE Internet Things J., vol. 11, no. 24, pp. 40996–41007, Dec. 2024.

[10] S. Xu, J. Liu, T. K. Rodrigues, and N. Kato, “Robust multiuser beamforming for IRS-enhanced near-space downlink communications coexisting with satellite system,” IEEE Internet Things J., vol. 9, no. 16, pp. 14900–14912, Aug. 2022.

[11] S. Liu, H. Dahrouj, and M.-S. Alouini, “Joint user association and beamforming in integrated satellite-HAPS-ground networks,” IEEE Trans Veh. Technol., vol. 73, no. 4, pp. 5162–5178, Apr. 2024.

[12] H. Kong, M. Lin, L. Han, W.-P. Zhu, Z. Ding, and M.-S. Alouini, “Uplink multiple access with semi-grant-free transmission in integrated satellite-aerial-terrestrial networks,” IEEE J. Sel. Areas Commun., vol. 41, no. 6, pp. 1723–1736, Jun. 2023.

[13] R. Zhang, K. Xiong, Y. Lu, P. Fan, D. W. K. Ng, and K. B. Letaief, “Energy efficiency maximization in RIS-assisted SWIPT networks with RSMA: A PPO-based approach,” IEEE J. Sel. Areas Commun., vol. 41, no. 5, pp. 1413–1430, May 2023.

[14] K. Guo et al., “Power allocation and performance evaluation for NOMAaided integrated satellite-HAP-terrestrial networks under practical limitations,” IEEE Internet Things J., vol. 11, no. 7, pp. 13002–13017, Apr. 2024.

[15] T.-H. Nguyen, T. K. Nguyen, V. N. Quoc Bao, H. Park, and L. Park, “Generative AI-powered aerial access networks: Recent studies and future outlook,” in Proc. 15th Int. Conf. Inf. Commun. Technol. Converg. (ICTC), Oct. 2024, pp. 529–533.

[16] M. Pourghasemian, M. R. Abedi, S. S. Hosseini, N. Mokari, M. R. Javan, and E. A. Jorswieck, “AI-based mobility-aware energy efficient resource allocation and trajectory design for NFV enabled aerial networks,” IEEE Trans. Green Commun. Netw., vol. 7, no. 1, pp. 281–297, Mar. 2023.

[17] W. Zhu, B. Zhang, L. Zhang, Y. Xu, and K. Yang, “Spatial path analysis for high-altitude solar-powered airship with maximum net energy,” Aerosp. Sci. Technol., vol. 117, Oct. 2021, Art. no. 106922.

[18] L. Zhang, W. Zhu, H. Du, and M. Lv, “Multidisciplinary design of high altitude airship based on solar energy optimization,” Aerosp. Sci. Technol., vol. 110, Mar. 2021, Art. no. 106440.

[19] W. Dongchen, S. Bifeng, J. Jun, and W. Haifeng, “High-altitude airship propulsion system optimal design and experiment based on energy balance,” Proc. Inst. Mech. Eng., G, J. Aerosp. Eng., vol. 237, no. 1, pp. 3–16, Jan. 2023.

[20] N. Mourousias, B. G. Marinus, and M. C. Runacres, “A novel multifidelity optimization framework for high-altitude propellers,” Aerosp. Sci. Technol., vol. 153, Oct. 2024, Art. no. 109407.

[21] N. Mourousias, A. Garc´ıa-Gutierrez, A. Malim, D. Dom´ ´ınguez Fernandez, B. G. Marinus, and M. C. Runacres, “Uncertainty quantifica-´ tion study of the aerodynamic performance of high-altitude propellers,” Aerosp. Sci. Technol., vol. 133, Feb. 2023, Art. no. 108108.

[22] K. Song, Z. Li, Y. Zhang, X. Wang, G. Xu, and H. Zhang, “A rule-based online energy management strategy for long-endurance stratospheric airships,” Aerosp. Sci. Technol., vol. 151, Aug. 2024, Art. no. 109266.

[23] D. Zhou et al., “Least-to-most prompting enables complex reasoning in large language models,” 2022, arXiv:2205.10625.

[24] S. Gao et al., “Empowering biomedical discovery with AI agents,” Cell, vol. 187, no. 22, pp. 6125–6151, Oct. 2024.

[25] C. Wang, M. Scazzariello, A. Farshin, D. Kostic, and M. Chiesa, “Making network configuration human friendly,” 2023, arXiv:2309.06342.

[26] T. Yang et al., “AutoHMA-LLM: Efficient task coordination and execution in heterogeneous multi-agent systems using hybrid large language models,” IEEE Trans. Cognit. Commun. Netw., vol. 11, no. 2, pp. 987–998, Apr. 2025.

[27] C. Cao, F. Wang, L. Lindley, and Z. Wang, “Managing Linux servers with LLM-based AI agents: An empirical evaluation with GPT4,” Mach. Learn. Appl., vol. 17, Sep. 2024, Art. no. 100570.

[28] R. Zhang et al., “Interactive AI with retrieval-augmented generation for next generation networking,” IEEE Netw., vol. 38, no. 6, pp. 414–424, Nov. 2024.

[29] Z. Xi et al., “The rise and potential of large language model based agents: A survey,” 2023, arXiv:2309.07864.

[30] M. H. Noor, A. Sarosh, U. Riaz, M. Adnan, and O. A. A. Awan, “A figure of merit based computational heat transfer method for aerothermal analysis of airborne electronics system LRU,” in Proc. 19th Int. Bhurban Conf. Appl. Sci. Technol. (IBCAST), Aug. 2022, pp. 70–75.

[31] Z. Lian, Y. Su, Y. Wang, and L. Jiang, “A non-stationary 3-D wideband channel model for intelligent reflecting surface-assisted HAP-MIMO communication systems,” IEEE Trans. Veh. Technol., vol. 71, no. 2, pp. 1109–1123, Feb. 2022.

[32] R. Shafie, M. J. Omidi, O. Abbasi, and H. Yanikomeroglu, “MIMO-NOMA enabled sectorized cylindrical massive antenna array for HAPS with spatially correlated channels,” IEEE Trans. Wireless Commun., vol. 23, no. 10, pp. 15155–15168, Oct. 2024.

[33] S. H. Hariq and R. Iyer Seshadri, “Integration of LoS MIMO RF and optical links via HAPS for high-capacity satellite feeder links,” in Proc. IEEE 100th Veh. Technol. Conf. (VTC-Fall), Oct. 2024, pp. 1–5.

[34] Z. Gao et al., “Data-driven deep learning based hybrid beamforming for aerial massive MIMO-OFDM systems with implicit CSI,” IEEE J. Sel. Areas Commun., vol. 40, no. 10, pp. 2894–2913, Oct. 2022.

[35] Y. Huang, L. You, C. G. Tsinos, W. Wang, and X. Gao, “QoS-aware precoding in downlink massive MIMO LEO satellite communications,” IEEE Commun. Lett., vol. 27, no. 6, pp. 1560–1564, Jun. 2023.

[36] L. You et al., “Beam squint-aware integrated sensing and communications for hybrid massive MIMO LEO satellite systems,” IEEE J. Sel. Areas Commun., vol. 40, no. 10, pp. 2994–3009, Oct. 2022.

[37] O. Abbasi and H. Yanikomeroglu, “UxNB-enabled cell-free massive MIMO with HAPS-assisted sub-THz backhauling,” IEEE Trans. Veh. Technol., vol. 73, no. 5, pp. 6937–6953, May 2024.

[38] Y.-F. Liu et al., “A survey of recent advances in optimization methods for wireless communications,” IEEE J. Sel. Areas Commun., vol. 42, no. 11, pp. 2992–3031, Nov. 2024.

[39] Z. Li, S. Yang, Y. Yin, M. Bouazizi, and T. Ohtsuki, “Beamforming design using UE positions and 3D terrain-building in HAPS system,” in Proc. IEEE 100th Veh. Technol. Conf. (VTC-Fall), Oct. 2024, pp. 1–7.

[40] O. Abbasi, H. Yanikomeroglu, and G. Kaddoum, “Hemispherical massive MIMO architecture for high-altitude platform station (HAPS),” in Proc. IEEE Wireless Commun. Netw. Conf. (WCNC), Apr. 2024, pp. 1–6.

[41] M. Salamatmoghadasi, A. Mehrabian, and H. Yanikomeroglus, “Energy sustainability in dense radio access networks via high altitude platform stations,” IEEE Netw. Lett., vol. 6, no. 1, pp. 21–25, Mar. 2024.

[42] Y. Liu, K. Sun, and M. Lv, “Stratospheric wind field feature extraction and energy management for hybrid electric solar airship with deep reinforcement learning,” Sustain. Energy Technol. Assessments, vol. 71, Nov. 2024, Art. no. 103993.

[43] W. Dongchen, S. Bifeng, J. Jun, and X. Dong, “High-altitude airship variable-pitch propeller performance analysis at multiple altitudes,” Proc. Inst. Mech. Eng., G, J. Aerosp. Eng., vol. 237, no. 13, pp. 2961–2973, Apr. 2023.

[44] A. Delgado, D. Dom´ınguez, J. Gonzalo, and A. Escapa, “Station-keeping HAPS mission through optimal sprint and drift trajectories,” Aerosp. Sci. Technol., vol. 152, Sep. 2024, Art. no. 109365.

[45] L. Qi, X. Yang, F. Bai, X. Deng, and Y. Pan, “Stratospheric airship trajectory planning in wind field using deep reinforcement learning,” Adv. Space Res., vol. 75, no. 1, pp. 620–634, Jan. 2025.

[46] A. Gangadhar, M. Manikandan, D. Rajaram, and D. N. Mavris, “Conceptual design and feasibility study of winged hybrid airship,” Aerosp., vol. 9, no. 1, p. 8, Dec. 2021.

[47] S. F. Hoerner, Fluid-Dynamic Drag: Practical Inf. Aerodynamic Drag Hydrodynamic Resistance. Brick Town, New Jersey: Hoerner Fluid Dynamics, 1965.

[48] M. I. Alam and R. S. Pant, “Estimation of volumetric drag coefficient of two-dimensional body of revolution,” J. Aircr., vol. 56, no. 5, pp. 2080–2082, Sep. 2019.

[49] M. Manikandan and R. S. Pant, “A comparative study of conventional and tri-lobed stratospheric airships,” Aeronaut. J., vol. 125, no. 1290, pp. 1434–1466, Aug. 2021.

[50] L. S. Diehl and J. G. Coelho, “Assessment of the effectiveness of stall delay and tip loss corrections for the simulation of small propeller performance with virtual blade model,” Eur. J. Mech.-B/Fluids, vol. 105, pp. 34–43, May 2024.

[51] W. Zhong, T. Wang, W. Z. Shen, and W. J. Zhu, “A function improving tip loss correction of blade-element momentum theory for wind turbines,” Int. J. Sustain. Energy, vol. 43, no. 1, Dec. 2024, Art. no. 2352794.

[52] D. He, H. Li, and H. Du, “Lexicographic multi-objective MPC for constrained nonlinear systems with changing objective prioritization,” Automatica, vol. 125, Mar. 2021, Art. no. 109433.

[53] S. Yang, P. An, P. Yang, X. Cao, D. Oliver Wu, and T. Q. S. Quek, “Adaptive subarray segmentation: A new paradigm of spatial nonstationary near-field channel estimation for XL-MIMO systems,” IEEE Trans. Commun., vol. 74, pp. 2220–2234, Dec. 15, 2026, doi: 10.1109/ TCOMM.2025.3644475.

[54] Y. Kawamoto et al., “HAPS-based interference suppression through null broadening with directivity control in space-air-ground integrated networks,” IEEE Trans. Veh. Technol., vol. 72, no. 12, pp. 16098–16107, Dec. 2023.

[55] J. Dai, Y. Liu, J. Zheng, R. Zhang, J. Zhang, and B. Ai, “Movable cell-free massive MIMO for high-speed train communications: A PPObased antenna position optimization,” in Proc. IEEE Int. Conf. Commun. Workshops (ICC Workshops), Jun. 2025, pp. 38–43.

[56] V. That, S. Muy, and J.-R. Lee, “Multi-UAV-aided power-up and data collection: Multi-agent DQL with genetic algorithm approach,” Expert Syst. Appl., vol. 297, Feb. 2026, Art. no. 129401.

[57] B. E. Y. Belmekki et al., “Cellular network from the sky: Toward peoplecentered smart communities,” IEEE Open J. Commun. Soc., vol. 5, pp. 1916–1936, 2024.