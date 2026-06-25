# YOLO-Based Semantic Communication With Generative AI-Aided Resource Allocation for Digital Twins Construction

Baoxia Du , Graduate Student Member, IEEE, Hongyang Du , Graduate Student Member, IEEE, Haifeng Liu, Dusit Niyato , Fellow, IEEE, Peng Xin, Jun Yu, Mingyang Qi, and You Tang

Abstract—Digital Twins play a crucial role in bridging the physical and virtual worlds. Given the dynamic and evolving characteristics of the physical world, a huge volume of data transmission and exchange is necessary to attain synchronized updates in the virtual world. In this article, we propose a semantic communication framework based on you only look once (YOLO) to construct a virtual apple orchard with the aim of mitigating the costs associated with data transmission. Specifically, we first employ the YOLOv7-X object detector to extract semantic information from captured images of edge devices, thereby reducing the volume of transmitted data and saving transmission costs. Afterwards, we quantify the importance of each semantic information by the confidence generated through the object detector. Based on this, we propose two resource allocation schemes, i.e., the confidence-based scheme and the artificial intelligence-generated scheme, aimed at enhancing the transmission quality of important semantic information. The proposed diffusion model generates an optimal allocation scheme that outperforms both the average allocation scheme and the confidence-based allocation scheme. Moreover, to obtain semantic information more effectively, we enhance the detection capability of the YOLOv7-X object detector by introducing new efficient layer aggregation network-horNet (ELAN-H) and SimAM attention modules, while reducing the model parameters

Manuscript received 23 June 2023; revised 19 August 2023; accepted 10 September 2023. Date of publication 20 September 2023; date of current version 21 February 2024. This work was supported in part by the Jilin Scientific and Technological Development Program under Grant YDZJ202201ZYTS692; in part by the National Research Foundation, Singapore; in part by the Infocomm Media Development Authority under its Future Communications Research and Development Programme; in part by DSO National Laboratories under the AI Singapore Programme (AISG) under Award AISG2-RP-2020-019; in part by the Energy Research Test-Bed and Industry Partnership Funding Initiative, Energy Grid (EG) 2.0 Programme; in part by the DesCartes and the Campus for Research Excellence and Technological Enterprise (CREATE) Programme; and in part by MOE Tier 1 under Grant RG87/22. (Corresponding authors: Mingyang Qi; You Tang.)

Baoxia Du and You Tang are with the School of Electrical and Information Engineering, Jilin Agricultural Science and Technology University, Jilin City 132101, China, and also with the School of Information and Control Engineering, Jilin Institute of Chemical Technology, Jilin City 132022, China (e-mail: dubaoxia@jlict.edu.cn; tangyou9000@163.com).

Hongyang Du and Dusit Niyato are with the School of Computer Science and Engineering, Nanyang Technological University, Singapore (e-mail: hongyang001@e.ntu.edu.sg; dniyato@ntu.edu.sg).

Haifeng Liu is with the College of Agriculture, Yanbian University, Yanji 133002, China (e-mail: liufeng\_1989@163.com).

Peng Xin and Jun Yu are with the School of Information and Control Engineering, Jilin Institute of Chemical Technology, Jilin City 132022, China (e-mail: xinpeng4321@163.com; yujun@jlict.edu.cn).

Mingyang Qi is with the School of Electrical and Information Engineering, Jilin Agricultural Science and Technology University, Jilin City 132101, China (e-mail: qimingyang0912@126.com).

Digital Object Identifier 10.1109/JIOT.2023.3317629 and computational complexity, making it easier to run on edge devices with limited performance. The numerical results indicate that our proposed semantic communication framework and resource allocation schemes significantly reduce transmission costs while enhancing the transmission quality of important information in communication services.

Index Terms—Digital twins, object detection, resource allocation, semantic communication.

# I. INTRODUCTION

N RECENT years, the advances in technologies, such I as augmented/extended/virtual reality (AR/XR/VR), blockchain, sixth-generation (6G) network, artificial intelligence (AI), and edge computing have led to an increasing demand for virtual reality and digital worlds. The metaverse, as a virtual reality concept, is considered an integration of multiple virtual worlds that can provide people with a more immersive and realistic digital space [1], [2], allowing them to engage in various activities, such as virtual conferences, remote collaboration, online learning, digital exhibitions, etc. The emergence of these virtual reality activities has not only alleviated social isolation and transportation restrictions, but also saved time and costs, gradually becoming essential tools for people’s lives and work. Moreover, the popularity of these activities in various social domains has also accelerated the development of digital economy and digital transformation [3], [4].

In agriculture, novel paradigms, such as digital farms, smart agriculture, and agricultural metaverse, which are combined with metaverse technology, are emerging and flourishing [4], [5]. In terms of agricultural production, users, such as farmers, can establish virtual farms in a virtual environment, simulate the complete growth process of crops and livestock, and obtain real-time growth data to achieve intelligent and refined agriculture. For instance, the XR Laboratory of Alibaba DAMO Academy presented a case study of an autonomous agricultural picking robot. The proposed approach entails the development of a high-precision 3-D model of the entire orchard via 3-D modeling techniques of both the orchard and fruit trees. Subsequently, a motion planning scheme can be established in the virtual environment, which can facilitate the robot’s autonomous picking process in the real world. This innovative approach can potentially minimize the costs associated with orchard management [6]. Furthermore, virtual agriculture can be combined with other fields, such as agricultural leisure and agricultural education. For example, the Faculty of Agriculture has developed an agricultural metaverse teaching system for an egg chicken farm at the National University of Laos. Through the VR technology, the faculty members provide agricultural education to learners, including knowledge related to technology, farm location, and other relevant aspects. The system has been reported to have yielded positive results [7].

Digital twins (DTs), namely, digital replications of physical objects, have emerged as a pivotal technology for creating virtual environments [8], [9]. In agriculture, the physical realm is characterized by its intricate and constantly changing nature, necessitating DTs synchronizing with the physical world to ensure their accuracy in virtual operations. This process requires that edge devices persistently gather the most recent data from the physical world, enabling real-time DTs updates. The acquisition and transmission of the data from the physical world often rely on various advanced edge devices and wireless communication technologies [10], [11]. Various fixed or mobile devices (e.g., sensors and cameras) are deployed to collect status data of physical objects, which, in real time, update, and interact with the virtual world through wireless communication. However, continuous data transmission poses stringent requirements on wireless communication systems, especially when dealing with extensive data, such as high-definition images, which can be both expensive and challenging when the physical world is vast.

Fortunately, semantic communication has been introduced as a novel avenue for tackling the aforementioned challenge [12], [13]. In contrast to conventional communication technologies, semantic communication systems regard transmission effective if the meaning of the received information maintains the original meaning of the transmitted information [14]. For example, in the context of image transmission, a semantic-based communication system can reduce the amount of data that needs to be transmitted by only transmitting the semantic information behind the image, while achieving the same effect [15].

In this article, we present a case study focusing on the development of a virtual apple orchard using a real apple data set. In the virtual orchard, users, i.e., fruit growers, can easily access various information, such as the quantity and location of fruit on each apple tree, as well as growth status and view real images of individual apples. The virtual orchard can help users manage their orchard more efficiently. In this case, the implementation of DTs requires edge devices, such as unmanned aerial vehicle (UAV) to capture the status information of fruit trees by taking photographs, and then transmitting the collected data to users via the wireless communication technology. To reduce costs and enhance communication quality during this process, we propose a semantic communication and resource allocation framework based on you only look once (YOLO). Our main contributions are summarized as follows.

1) Unlike traditional communication methods that necessitate transmitting all acquired images, we propose a YOLO-based semantic communication framework. Specifically, the proposed framework discards irrelevant interference information after image data acquisition, retaining only the critical semantic information for transmission. This significantly reduces the data volume needed for transmission and lowers resource costs while achieving the same outcome.

2) We employ the YOLOv7-X object detector to extract semantic information from images and enhance its performance on a real-world apple data set. Considering the limitations of existing object detectors in detecting small objects, such as small apples, and the constraints of processing power and memory in edge devices, larger models necessitate increased computational resources and memory for operation, which may result in performance degradation or inoperability. Consequently, we improve the YOLOv7-X algorithm by introducing the efficient layer aggregation networkhorNet (ELAN-H) and the SimAM attention modules. These modifications elevate the detector’s performance and reduce the parameters and computational requirements, facilitating deployment on edge devices with greater ease.

3) In the pursuit of enhancing transmission quality during the wireless transmission of a huge volume of images, we propose a resource allocation scheme based on the significance of semantic information. The scheme allocates transmission power following the relative importance of the semantic information, with the aim of enhancing the overall communication quality of image transmission systems by minimizing important information loss and improving the reliability of transmitted information. This approach ensures that critical information is transmitted with high quality to users, even in challenging wireless communication environments.

4) Furthermore, we utilize the AI-generated resource allocation scheme algorithm as an alternative allocation scheme, which facilitates more efficient processing power distribution. Specifically, by using the denoising technique, the AI-generated algorithm generates a design for the allocation scheme and subsequently adds exploration noise to execute it, thereby gaining experience in exploration. The numerical results clearly demonstrate that this method achieves the highest score in terms of semantic information transmission quality.

The remainder of this article is organized as follows. In Section II, we initially summarize the related work about DTs, semantic communication, and apple detection. Section III introduces the overall system design, semantic communication approach, and the metric used for evaluating the system’s communication quality. In Section IV, the YOLOv7-X object detector and its enhancement methods are described in detail, followed by an explanation of two distinct resource allocation methods for data transmission. Subsequently, we analyze the numerical results in Section V. Finally, Section VI concludes this article.

# II. RELATED WORK

In this section, we briefly introduce three related techniques, i.e., DTs, semantic communication, and apple detection.

# A. Digital Twins

The physical system and physical world in agriculture are complex and dynamic environments that include basic information and characteristics of physical objects. DTs require continuous updating from the physical to the virtual space as the state of physical objects changes over time [16], [17]. Li et al. [18] proposed a deep learning-based single-view leaf reconstruction method for a plant growth DT system, improving leaf reconstruction’s accuracy and speed. Angin et al. [19] introduced a DT framework for agriculture called AgriLoRa, which detects plant diseases and weeds using computer vision algorithms after uploading data from UAV images and field sensor data to cloud servers. Awais et al. [20] used the multispectral UAV and DTs model to achieve intelligent irrigation in the field. However, these works have focused only on the use of collected data and have not considered the impact of data transmission. DTs require a significant amount of computing power to render 3-D objects, which is achieved through collecting large amounts of data from perception networks and ultralow latency communication to maintain a seamless user experience [1]. When physical objects are large enough, the massive data streams can burden communication systems and cause excessive latency, or even transmission failure. Therefore, in this article, we use a semantic-aware communication method to reduce the amount of data that needs to be transmitted.

# B. Semantic Communication

In classical communication theory, the semantic content and meaning of the message are largely considered irrelevant to communication. However, in the age of rapidly increasing data volume, the limitations of classical communication theory have begun to be revealed [21]. Semantic communication constitutes an innovative paradigm wherein message transmission is not confined solely to the message content, but rather entails direct extraction of pertinent semantic information, thereby eliminating redundant data and mitigating associated costs. Xie et al. [22] proposed a text transfer framework called DeepSC based on the Transformer [23], which can recover the meaning of sentences through semantic information, thus minimizing semantic errors during transmission. Zhou et al. [24] proposed a cognitive semantic communication framework that utilizes knowledge graphs, which has good data compression rates and communication reliability. In addition to text-based semantic communication, some literature also proposes semantic communication methods applied to images. Lokumarambage et al. [25] obtained semantic information through semantic segmentation at the transmitter and used GAN networks to reconstruct the image at the receiver, greatly saving bandwidth resources, but the reconstructed image is slightly different from reality. Zhang et al. [26] proposed a neural network-based image transfer semantic communication system, where the transmitter can extract and transmit the required semantic information in a dynamic environment through a receiver-leading training process without knowing the task. Kang et al. [27] proposed a task-oriented semantic communication framework, where users can match the semantic information of images by querying text, and also consider the resource allocation problem when there are multiple users. Although the above literature reduces communication overhead through semantic communication, they have not considered the varying importance of semantic information itself, which may result in the loss of significant semantic information in the competition for channel resources. Therefore, we assign different levels of importance to the semantic information extracted from images to ensure the transmission quality of critical semantic information by rationally allocating transmission power.

# C. Object Detection

In the communication framework proposed in this article, the UAV needs to extract the semantic information of the acquired images, i.e., to achieve the separation of apples and backgrounds, and the core of achieving this is the object detection technique.

Apple Detection: In recent years, deep learning-based object detection techniques have achieved remarkable success. In contrast to traditional algorithms that rely on appearance features, such as shape and color [28], [29], deep learning-based techniques demonstrate strong adaptability to different scenarios and achieve higher accuracy. Chen et al. [30] utilized the DenseNet network structure to optimize the YOLOv4 model, proposing a Des-YOLOv4 algorithm for detecting apples. However, the performance of the algorithm significantly deteriorates under low-light conditions. Yan et al. [31] proposed an improved YOLOv5 [32] algorithm for real-time apple recognition by incorporating squeeze-and-excitation (SE) modules and modifying the fusion mode of feature maps. Despite the improved performance, the algorithm’s effectiveness in detecting small apples is suboptimal. Sun et al. [33] proposed a novel balanced feature pyramid network (BFP Net) that enhances the accuracy of small apple detection. Nevertheless, the BFP Net has a slower detection speed. The above work indicates that it is difficult to balance the detection speed and accuracy of the model, and detecting small apples in complex environments remains a challenge. With the continuous development of the YOLO series object detectors, the YOLOv7 model emerges as a highly advanced and efficient end-to-end object detector. It employs a state-of-the-art methodology for detecting objects in an image, with exceptional accuracy and real-time performance [34]. However, its performance on data set with a considerable number of small apples is slightly limited. Thus, we employed it as the baseline model for improving detection performance.

Data Augmentation: In addition to modifying the model structure to improve detection capability, data augmentation is another straightforward and effective approach. Data augmentation allows generating additional equally effective data based on limited data without altering the essential information of the images. This significantly enhances the diversity of the training data, thereby enhancing the model with stronger generalization capabilities. Changing the color and shape of images is the fundamental and common approach in data augmentation. In this study, we use fundamental data augmentation methods, such as randomly altering the hue, saturation, and brightness of images, as well as performing random scaling and translation. In addition to these basic data augmentation methods, some studies have proposed more efficient approaches, such as Mosaic [35] and Mixup [36]. Mosaic involves randomly cropping and scaling four images, then combining them into a single image for training data. Mixup randomly selects two samples from the training data and constructs new training samples and labels through linear interpolation. In this work, we use a combination of Mosaic, Mixup, and fundamental methods.

![](images/740431738b91fef52b25244701f7a565d9d85f76e234dad9b708f1a704952e94.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Apple Trees"] -->|Take Photos| B["UAV"]
    B --> C["Importance-Based Semantic Communication"]
    C --> D["Users"]
    C --> E["Applications"]
    D --> F["Receive Semantic Information"]
    E --> G["Semantic Information"]
    H["Apple Photos"] --> I["YOLOv7 Detector"]
    I --> J["Apple Detection Results"]
    J --> K["Allocate Transmission Power"]
    K --> L["Confidence"]
    K --> M["Apple Images"]
    K --> N["Positions"]
    L --> O["Obtain the Semantic Information"]
    M --> O
    N --> O
    O --> P["Semantic Information"]
```
</details>

Fig. 1. Illustration of the YOLO-based semantic communication system model.

In summary, we propose a YOLO-based semantic communication and resource allocation framework to address the above problems in this article. First, we select the advanced YOLOv7-X object detector as the core of the entire system and optimize its performance on real data set. Following that, the UAV extracts semantic information from collected images using the optimized YOLOv7-X object detector. Then, the UAV allocates transmission power based on the importance of semantic information before transmitting, ultimately achieving high-quality transmission of critical information.

# III. SYSTEM MODEL

In this section, we present the proposed data transmission framework and the semantic-based communication approach, followed by an explanation of the metric methodology for assessing image semantic information transmission quality.

# A. Design of Semantic Communication and Resource Allocation Framework

In data collection in DTs, a UAV takes images along a specified trajectory and transmit the data to users. However, in wireless communication environments with fading channels, the cost of transmitting all data to users at high quality is prohibitive. To address this issue, we propose a semantic communication framework based on YOLO, as shown in Fig. 1. We first simulate the images captured by the UAV using real apple data set. After the collection task is completed, the UAV uses the trained YOLOv7-X object detector to extract semantic information behind the image that people need and transmit them. At the same time, we quantify the importance of each semantic information based on the confidence generated by the object detector and allocate transmission power accordingly to ensure the transmission quality of important information. The problem of optimal power allocation schemes is introduced in Section IV. It is worth noting that the semantic extraction model is a flexible module. When faced with user interest in other single or multiple classes of objects in the captured image, this module can be replaced with other pretrained YOLO series models or alternative object detectors to assist users in extracting useful information. By employing other well-trained object detectors, our semantic communication framework can expand its applicability, enabling the extraction and transmission of useful information about different objects in images according to user demands.

# B. Semantic Communication Solution

In conventional communication paradigms, edge devices transmit the entirety of the acquired image data to facilitate continuous data synchronization for DTs, resulting in voluminous data traffic. This imposes substantial burdens on both edge devices and the communication infrastructure. To illustrate, in smart agriculture, users deploy UAVs for image capture [37]. However, oftentimes, only a portion of the captured content is relevant to users, e.g., ripening fruits. Utilizing such an inefficient communication approach for transmitting all images leads to the excessive consumption of communication resources and energy for UAVs, thereby exacerbating resource wastage.

The development of semantic communication provides a solution to the aforementioned problems. Upon completing the designated data acquisition task, the UAV transmits only the pertinent semantic features extracted from the captured images, rather than the entire data set. The transmission of these semantic features requires minimal channel resources and facilitates efficient data storage for users. In the virtual orchard, users, e.g., fruit growers, are primarily more concerned about the status of the fruits. As a result, we discard irrelevant background and interference factors before transmitting the images, ensuring that users only receive the semantic information they are interested in, which helps reduce transmission cost.

# C. Semantic Communication Quality Analysis

To evaluate the quality of semantic communication, we propose a metric for image semantic transmission (MIST) in this work, which involves combining the importance weights of each semantic information with their respective transmission quality to obtain the final evaluation result. Considering that a UAV needs to send an image to the user after capturing it, semantic information is first extracted by the object detector. Specifically, a total of U apple objects are detected, with i denoting the ith object and $c _ { i }$ denoting its corresponding confidence. The relationship between the importance score $W _ { i }$ and the confidence $c _ { i }$ of the object i can be represented as $W _ { i } = { c _ { i } } ^ { \sigma }$ , where $\sigma$ is a variable that adjusts the importances among different semantic information. The final semantic transmission quality score can be represented as follows:

$$
E (A, W _ {i}, Q (p _ {i})) = A \sum_ {i = 1} ^ {U} (W _ {i} \times Q (p _ {i})) \tag {1}
$$

where A represents the accuracy of semantic information extraction, i.e., the performance evaluation metric Average Precision at 0.5 Intersection over Union (AP@0.5) of the object detector, and Q(pi) represents the structure similarity index measure (SSIM) [38] value of object i before and after transmission, which is a function that is positively correlated with the transmission power $p _ { i }$ according to [27]. Therefore, considering the definition of the communication system in this article, our goal is to maximize the MIST while satisfying the transmission power constraint, which can be expressed as follows:

$$
\max _ {A, W _ {i}, p _ {i}} \sum_ {i = 1} ^ {U} E (A, W _ {i}, Q (p _ {i}))) \tag {2}
$$

$$
\sum_ {i = 1} ^ {U} p _ {i} \leq P \tag {2a}
$$

$$
c _ {i} \in [ c _ {\min}, 1 ] \tag {2b}
$$

where the constraint in (2a) is the total transmitted power, and $c _ { \mathrm { m i n } }$ in (2b) is the confidence threshold, the objects with confidence below this value are not detected by the detector. In this study, we set the variable $\sigma = 1$ and the confidence threshold $c _ { \operatorname* { m i n } } = 0 . 2 5$ by default. The proposed MIST considers not only the transmission quality of each semantic information but also their respective significance, which can provide a more comprehensive and accurate assessment of the performance of these methods.

# IV. YOLO-BASED SEMANTIC COMMUNICATION SYSTEM DESIGN

The YOLOv7-X object detector is a critical component of the overall communication system. It aids UAVs in extracting semantic information from images and subsequently quantifying the semantic information’s importance to facilitate optimal transmission power allocation. In this section, we present the motivation for choosing YOLO and provide a detailed exposition of YOLOv7-X, along with the improvements made. Subsequently, we discuss two distinct resource allocation schemes in data transmission.

# A. Overview of YOLOv7-X

The motivation for selecting YOLO as the semantic extraction model in our study stems from several key factors. First, YOLO has demonstrated exceptional performance in real-time object detection tasks, making it a suitable choice for various applications. Its ability to achieve high accuracy while maintaining impressive inference speed aligns with our goal of efficiently detecting and extracting semantic information from apple images in real-world scenarios. Moreover, YOLO’s end-to-end architecture contributes to its simplicity and ease of implementation. This feature not only simplifies the overall model structure but also reduces computational complexity, making it suitable for resource-constrained environments such as edge devices like UAVs. Furthermore, in the application scenario of our article, the confidence generated by the YOLO model effectively measures the importance of the object’s semantic information. This aids in efficient semantic communication by prioritizing and transmitting important features, thus ensuring optimal power allocation for the information.

YOLOv7 has seven different models of varying sizes, including YOLOv7-tiny, YOLOv7, YOLOv7-X, and YOLOv7-W6, among others, which are suitable for different application environments. Considering both model complexity and detection performance, we select YOLOv7-X as the base model for improvement. The YOLOv7-X model can be divided into three parts: 1) Input; 2) Backbone; and 3) Head. Specifically, the Input resizes the input image to the required training size. The Backbone component includes multiple CBS convolutions, max pooling convolution (MPConv), efficient layer aggregation network in YOLOv7-X (ELAN-X) modules, and an SPPCSPC module. The CBS convolution consists of a convolutional layer, a batch normalization layer (BN), and a sigmoid linear unit (SiLU) activation function. ELAN-X extends the efficient layer aggregation network (ELAN) module by increasing its depth and width, and enhances the learning capability of the network by guiding the computation blocks to learn more diverse features of different feature groups. The MPConv module adds a Maxpool layer on top of CBS and strengthens the feature extraction ability by merging features from the top and bottom branches. The SPPCSPC module is similar to the spatial pyramid pooling-fast (SPPF) used by YOLOv5 [32], which increases a network’s receptive field. The Head component employs the same path aggregation feature pyramid network (PAFPN) [39] architecture as YOLOv5 to efficiently fuse features from multiple levels. Finally, the fused and enhanced feature map is fed to three detection heads to generate predictions for confidence, object category, and anchor boxes.

# B. Model Enhancement Methods

ELAN-H: The ELAN-X module in YOLOv7-X is an efficient network structure that enables the network to learn more features and have stronger robustness by controlling the shortest and longest gradient paths. The structure of ELAN-X is shown in Fig. 4. The shortest branch passes through only one CBS convolution to change the number of channels, while the longest branch extracts features through seven CBS convolutions. The feature maps extracted by each branch are concatenated through the Concatenation (Concat) operation as the final result of feature-enhanced fusion. ELAN-X is repeatedly used in the Neck to improve the model’s learning capability. However, too many branches and convolution operations also increase model complexity and parameter size, leading to increased processing time and consumption of computing resources. Therefore, we reduce the depth and width of this module without breaking its original architecture, changing the number of CBS in the longest branch to three and correspondingly decreasing the number of output feature maps to four. In addition, to compensate for the decrease in detection performance caused by simplifying this module, we replace one CBS convolution in the long branch with Hornet Block [40] to enhance the module’s ability to learn important features. Finally, this module, named ELAN-H, has a structure shown in Fig. 2(a).

![](images/07ef273c747b68e2bbce7d5c90c2a694fbfed800781ae8033c4d83207385c124.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["CBS,4C,C"] --> B["Concat,4C"]
    C["CBS,2C,C"] --> B
    D["CBS,C,C"] --> E["HorNet"]
    F["CBS,2C,C"] --> E
    B --> E
    E --> G["2C"]
    H["CBS,4C,C"] --> I["Concat,4C"]
    J["CBS,C,C"] --> I
    K["CBS,2C,C"] --> I
```
</details>

(a)   
![](images/d633b459bfd973beb948a02ad8fd2f7e432de183c78b315461d8df06fc6a4172.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Multi-Layer Perceptron"] --> B["LayerNorm"]
    B --> C["g^nConv"]
    C --> D["LayerNorm"]
    D --> E["HorNet"]
    E --> F["+"]
    F --> G["+"]
    G --> H["LayerNorm"]
    H --> I["g^nConv"]
    I --> J["+"]
    J --> K["+"]
    K --> L["LayerNorm"]
    L --> M["+"]
    M --> N["+"]
    N --> O["+"]
    O --> P["+"]
    P --> Q["+"]
    Q --> R["+"]
    R --> S["+"]
    S --> T["+"]
    T --> U["+"]
    U --> V["+"]
    V --> W["+"]
    W --> X["+"]
    X --> Y["+"]
    Y --> Z["+"]
    Z --> AA["+"]
    AA --> AB["+"]
    AB --> AC["+"]
    AC --> AD["+"]
    AD --> AE["+"]
    AE --> AF["+"]
    AF --> AG["+"]
    AG --> AH["+"]
    AH --> AI["+"]
    AI --> AJ["+"]
    AJ --> AK["+"]
    AK --> AL["+"]
    AL --> AM["+"]
    AM --> AN["+"]
    AN --> AO["+"]
    AO --> AP["+"]
    AP --> AQ["+"]
    AQ --> AR["+"]
    AR --> AS["+"]
    AS --> AT["+"]
    AT --> AU["+"]
    AU --> AV["+"]
    AV --> AW["+"]
    AW --> AX["+"]
    AX --> AY["+"]
    AY --> AZ["+"]
    AZ --> BA["+"]
    BA --> BB["+"]
    BB --> BC["+"]
    BC --> BD["+"]
    BD --> BE["+"]
    BE --> BF["+"]
    BF --> BG["+"]
    BG --> BH["+"]
    BH --> BI["+"]
    BI --> BJ["+"]
    BJ --> BK["+"]
    BK --> BL["+"]
    BL --> BM["+"]
    BM --> BN["+"]
    BN --> BO["+"]
    BO --> BP["+"]
    BP --> BQ["+"]
    BQ --> BR["+"]
    BR --> BS["+"]
    BS --> BT["+"]
    BT --> BU["+"]
    BU --> BV["+"]
    BV --> BW["+"]
    BW --> BX["+"]
    BX --> BY["+"]
    BY --> BZ["+"]
    BZ --> CA["+"]
    CA --> CB["+"]
    CB --> CC["+"]
    CC --> CD["+"]
    CD --> CE["+"]
    CE --> CF["+"]
    CF --> CG["+"]
    CG --> CH["+"]
    CH --> CI["+"]
    CI --> CJ["+"]
    CJ --> CK["+"]
    CK --> CR["+"]
    CR --> CS["+"]
    CS --> CT["+"]
    CT --> CU["+"]
    CU --> CV["+"]
    CV --> CW["+"]
    CW --> CX["+"]
    CX --> CY["+"]
    CY --> CZ["+"]
    CZ --> DA["+"]
    DA --> DB["+"]
    DB --> DC["+"]
    DC --> DV["+"]
    DV --> DW["+"]
    DW --> DX["+"]
    DX --> DWB["+"]
    DWB --> DWC["-2C-C/4"] & DWC
```
</details>

(b)   
Fig. 2. ELAN-H model structure with HorNet. (a) ELAN-H model structure, which stacks feature maps from different levels by Concatenation (Concat) operation as the final output. (b) Overview of the basic building block in HorNet with Recursive Gated Convolution $( g ^ { n } \mathbf { C _ { 0 n v } } )$ .

Here, the Hornet block is a design based on Recursive Gated Convolution $( g ^ { n } \mathbf { C } \mathbf { o n v } )$ . The output of the gated convolution $\mathbf { y } = g \mathbf { C o n v } ( \mathbf { x } )$ can be represented as follows:

$$
\left[ \mathbf {p} _ {0} ^ {H W \times C}, \mathbf {q} _ {0} ^ {H W \times C} \right] = \phi_ {\text { in }} (\mathbf {x}) \in \mathbb {R} ^ {H W \times 2 C} \tag {3}
$$

$$
\mathbf {p} _ {1} = f \left(\mathbf {q} _ {0}\right) \odot \mathbf {p} _ {0} \in \mathbb {R} ^ {H W \times C}, y = \phi_ {\text {out}} \left(\mathbf {p} _ {1}\right) \in \mathbb {R} ^ {H W \times C} \tag {4}
$$

where $\mathbf { x } ~ \in ~ \mathbb { R } ^ { H W \times C }$ represents the input features which are linearly projected to obtain ${ \bf p } _ { 0 }$ and ${ \bf q } _ { 0 } .$ . Then, ${ \bf q } _ { 0 }$ is subjected to depth-wise convolution and multiplied with ${ \bf p } _ { 0 }$ to obtain $\mathbf { p } _ { 1 }$ . Finally, $\mathbf { p } _ { 1 }$ is projected linearly again to yield the output y.

High-order spatial interaction requires the implementation of gated convolutions with recursive designs. Initially, a higher-order linear projection is applied to x resulting in p0 and ${ \bf q } _ { k } ( k = 0 , 1 , \ldots , n - 1 )$ . Subsequently, recursive gated convolutions are executed to generate $\mathbf { p } _ { k + 1 }$ . The output of $\mathbf { y } = g ^ { n } \mathbf { C o n v } ( \mathbf { x } )$ can be mathematically expressed as follows:

$$
\left[ \mathbf {p} _ {0} ^ {H W \times C _ {0}}, \mathbf {q} _ {0} ^ {H W \times C _ {0}}, \dots , \mathbf {q} _ {n - 1} ^ {H W \times C _ {n - 1}} \right]
$$

$$
= \phi_ {\text { in }} (\mathbf {x}) \in \mathbb {R} ^ {H W \times \left(C _ {0} + \sum_ {0 \leq k \leq n - 1} C _ {k}\right)} \tag {5}
$$

$$
\mathbf {p} _ {k + 1} = f _ {k} \big (\mathbf {q} _ {k} \big) \odot g _ {k} \big (\mathbf {p} _ {k} \big) / \alpha , \quad k = 0, 1, \dots , n - 1 \tag {6}
$$

$$
g _ {k} = \left\{ \begin{array}{l l} \text { Identity }, & k = 0, \\ \text { Linear } (C _ {k - 1}, C _ {k}), & 1 \leq k \leq n - 1 \end{array} \right. \tag {7}
$$

$$
C _ {k} = \frac {C}{2 ^ {n - k - 1}}, \quad 0 \leq k \leq n - 1 \tag {8}
$$

where {gk} are utilized to match the dimension in various orders and {fk} are depth-wise convolution layers. As depicted in Fig. 2(b), the HorNet block employs a block-wise design inspired by Transformer [23] and replace the self-attention sublayer with $g ^ { n } \mathbf { C } \mathbf { o n v }$ that have high-order spatial modeling capability. We replace all ELAN-X modules in the Neck with ELAN-H modules, which can better fuse and enhance the image features extracted by the Backbone, leading to improved detection performance while reducing model complexity.

SimAM $I 4 I { \mathrm { . } }$ : The attention module can assign different weights to different channels or regions in space, thereby helping the model to focus on extracting more important information. Existing attention mechanisms typically generate corresponding 1-D or 2-D weights in the channel or spatial dimension, as shown in Fig. 3(a) and (b), such as BAM [42], which parallelly connects two kinds of attention, and CBAM [43], which serially connects them. However, they treat each neuron in every channel or spatial position equally during the generation process. This limitation restricts their ability to learn more discriminative cues, while in the human brain, these two types of attention often occur simultaneously [41].

As shown in Fig. 3(c), SimAM is a unified weight attention module that can derive 3-D attention weights for feature maps without requiring additional parameters. In visual neuroscience, the most informative neurons typically exhibit discharge patterns that differ from those of surrounding neurons, and active neurons tend to inhibit surrounding neurons [44]. Drawing inspiration from this, the SimAM module designs an energy function to measure the linear separability between neurons, thereby identifying important neurons. The energy function is defined as follows:

$$
\begin{array}{l} e _ {t} \left(w _ {t}, b _ {t}, y, x _ {i}\right) = \frac {1}{M - 1} \sum_ {i = 1} ^ {M - 1} \left(- 1 - \left(w _ {t} x _ {i} + b _ {t}\right)\right) ^ {2} \\ + (1 - (w _ {t} t + b _ {t})) ^ {2} + \lambda w _ {t} ^ {2} \tag {9} \\ \end{array}
$$

where t denotes the target neuron and xi denotes other neurons in a single channel of the input feature $\mathbf { x } \in \mathbb { R } ^ { H W \times C }$ , i is index over spatial dimension, and M is the number of neurons. wt and $b _ { t }$ are weight and bias the transform. Subsequently, by computing the closed-form solutions of variables wt and $b _ { t } .$ and substituting them into (9). The minimum energy can be obtained as follows:

![](images/e97205672fa908c27406f6dec89a764ebf7671659da275b104ee60c720a82501.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input Feature"] -->|Generation| B["Fusion"]
    B -->|Expansion| C["Refined Feature"]
    subgraph "1-D channel-wise weights"
        D["Green block: X, C, H, W"]
    end
```
</details>

(a)

![](images/38c3b1214dee7b34592335ec091eee1fa14c3709d8fc0248784c5cc594526f4a.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    A["Input Feature"] -->|Fusion| B["Refined Feature"]
    B -->|Expansion| C["Generation"]
    C -->|2-D spatial-wise weights| D["Output"]
```
</details>

(b)

![](images/a11e52d92421b6035d9d291c07b00b7aa1356ebbcd945459cc0c066a5eae8a8c.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["Input Feature X C H W"] -->|Generation| B["3-D weights"]
    B -->|Expansion| C["Refined Feature X C H W"]
    A -->|Fusion| C
```
</details>

(c)   
Fig. 3. Comparisons of different attention steps. (a) Channel-wise attention. (b) Spatial-wise attention. (c) Full 3-D weights for attention.

$$
e _ {t} ^ {*} = \frac {4 (\hat {\sigma} ^ {2} + \lambda)}{(t - \hat {\mu}) ^ {2} + 2 \hat {\mu} ^ {2} + 2 \lambda}. \tag {10}
$$

The expression in (10) indicates that a smaller energy value corresponds to a greater linear separability between neuron t and other neurons, which signifies higher importance. Following the definition of attention mechanisms, the SimAM module can be expressed as follows:

$$
\tilde {\mathbf {x}} = \operatorname{sigmoid} \left(\frac {1}{E}\right) \odot \mathbf {x} \tag {11}
$$

where E is a classification function for all energy functions $e _ { t } ^ { * }$ in both channel and spatial dimensions. The sigmoid function ensures that the larger values in E are constrained, thereby not affecting the relative importance of each neuron. We integrate SimAM modules into the Neck section of the YOLOv7- X model, which helps the model to better focus on targets without introducing additional parameters.

YOLOv7-HS: The improved architecture of the YOLOv7-X model is depicted in Fig. 4. We enhance the YOLOv7-X model using the above methods to make it more suitable for the Minneapple data set, and named it YOLOv7-HS.

# C. Resource Allocation in Semantic Communication

After the UAV obtains the semantic information of images, a straightforward approach is to transmit it equally to users. However, due to the limited bandwidth resources in wireless transmission, semantic information is susceptible to signal attenuation during transmission, consequently affecting communication quality. Simultaneously, as nearly every original image is cropped into numerous apple images, and considering the highly complex orchard environment and the inherent limitations of the detection model, the importance of each cropped image (e.g., apple completeness and cropping accuracy) varies. The average allocation method (named Avg-SemCom) faces intense competition for scarce wireless channel resources among multiple images, resulting in the discarding of crucial images. Therefore, we propose a Confidence-based Semantic Communication (Conf-SemCom) method, which allocates transmission power by quantifying the importance of semantic information to ensure the transmission quality of important data.

Algorithm 1 Resource Allocation in Conf-SemCom   
Input: Captured image X on a UAV
Output: Users receive semantic information x of the image X
1: procedure UAV-SEND(x)
2: YOLOv7-HS detects apple images $x_{1}, x_{2}, \ldots, x_{i}, \ldots, x_{U}$ and their confidence $c_{1}, c_{2}, \ldots, c_{i}, \ldots, c_{U}$ 3: Calculate the priority weight $w_{i}$ of $x_{i}$ by confidence $c_{i}$ using (12)
4: for i = 1 to U do
5: Allocate transmission power to $x_{i}$ according to their priority weight $w_{i}$ using PA [27]
6: end for
7: The UAV sends semantic information x to users
8: end procedure

The correlation between an object detector’s confidence and the object it identifies is significant. Generally, the confidence of a detected object is positively correlated with the amount of semantic features it contains. As illustrated in Fig. 5, apples f , g, and h exhibit relatively complete and rich characteristic information of apples, making them easily detectable with a high confidence. While apples a and c are heavily obscured by leaves, resulting in low confidence scores for all of them. The semantic information of these low-confidence objects, after being cropped, is far less important than the other objects, and they should not occupy too much power during wireless transmission. In summary, the Conf-SemCom method can ensure that more important information is successfully transmitted to users.

Specifically, we prioritize sorting based on the confidence $c _ { i }$ of each object i and allocate more transmission power with a higher priority weight $w _ { i } .$ The definition of $w _ { i }$ is as follows:

$$
\boldsymbol {w} _ {i} = c _ {i} ^ {\eta} \tag {12}
$$

we use the variable η to adjust the relative difference in power allocation between different semantic information. The proposed Conf-SemCom is summarized in Algorithm 1 with the corresponding pseudo code.

![](images/abaa093522518377caaf40175cb5f2374a38e27ae4cf1eb52c2b8f52a7457218.jpg)

<details>
<summary>flowchart</summary>

Deep learning architecture diagram showing backbone, head, and SPPCSPC components with data flow between MPConv, ELAN-X, and SimAM layers.
</details>

Fig. 4. Network architecture of YOLOv7-HS contains general modules: input, backbone, and head, and basic components: CBS, MPConv, UP, SPPCSPC, SimAM, and two ELAN NPSabbrpl with different structures, namely, ELAN-X and ELAN-H.

![](images/2d4bdd903a9d513c77f9ca455640cb0cc8c3fc4be242a8d43aebe12b02ee4a71.jpg)

<details>
<summary>text_image</summary>

0.38
0.44
0.45
a
b
c
...
0.75
0.76
d
e
...
0.88
0.88
0.91
f
g
h
</details>

Fig. 5. Results of apple detection comprise anchor boxes and corresponding confidence values for each object, apples a to f are sorted in ascending order of confidence scores. Furthermore, the cropped images are resized to the same height for ease of viewing.

# D. Diffusion-Based Resource Allocation

Diffusion Model: The diffusion model has emerged as a new state-of-the-art deep generative model [45]. The fundamental concept of the diffusion model entails systematically perturbing the distribution of data during the forward diffusion process by introducing the Gaussian noise. Subsequently, the data distribution is recovered through the reverse diffusion process, which can be viewed as a denoising procedure. Specifically, within the forward diffusion process, by iteratively adding Gaussian noise T times to any initial sample x0, we can obtain $\mathbf { x } _ { 1 } , \mathbf { x } _ { 2 } , \ldots , \mathbf { x } _ { T }$ . As T approaches infinity, the original features of sample x0 completely vanish and become pure Gaussian noise. This process can be represented as follows:

$$
q (\mathbf {x} _ {1}, \dots , \mathbf {x} _ {T} | \mathbf {x} _ {0}) = \prod_ {t = 1} ^ {T} q (\mathbf {x} _ {t} | \mathbf {x} _ {t - 1}) \tag {13}
$$

$$
q \left(\mathbf {x} _ {t} \mid \mathbf {x} _ {t - 1}\right) := \mathcal {N} \left(\mathbf {x} _ {t}; \sqrt {1 - \beta_ {t}} \mathbf {x} _ {t - 1}, \beta_ {t} \mathbf {I}\right) \tag {14}
$$

where $\beta _ { t }$ is a parameter that controls the progress of noise. From (14), it can be inferred that given the sample $\mathbf X _ { t - 1 }$ , the sample xt at time t follows a Gaussian distribution with a mean of $\sqrt { 1 - \beta _ { t } } \mathbf { x } _ { t - 1 }$ and a variance of $\beta _ { t } \mathbf { I }$ . The parameters under this condition only depend on the $\mathbf { X } _ { t - 1 }$ at the previous time step. Therefore, the diffusion process is a Markov process.

When $\beta _ { t }$ is sufficiently small, the reverse diffusion process $q ( \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } , \mathbf { x } _ { 0 } )$ is the posterior probability distribution of the forward diffusion process $q ( \mathbf { x } _ { t } | \mathbf { x } _ { t - 1 } )$ . In order to achieve incremental sampling from the Gaussian noise $\mathbf { X } _ { T }$ to obtain real samples, it is necessary for the generative model $p _ { \theta } ( \mathbf { x } _ { 0 : T } )$ to learn sufficiently good parameters θ from the training samples. This process can be represented as follows:

$$
p _ {\theta} (\mathbf {x} _ {0: T}) = p (\mathbf {x} _ {T}) \prod_ {t = 1} ^ {T} p _ {\theta} (\mathbf {x} _ {t - 1} | \mathbf {x} _ {t}) \tag {15}
$$

$$
p _ {\theta} (\mathbf {x} _ {t - 1} | \mathbf {x} _ {t}) = \mathcal {N} (\mathbf {x} _ {t - 1}; \mu_ {\theta} (\mathbf {x} _ {t}, t), \Sigma_ {\theta} (\mathbf {x} _ {t}, t)) \tag {16}
$$

where $p ( \mathbf { x } _ { T } ) = \mathcal { N } ( \mathbf { x } _ { T } ; 0 , \mathbf { I } )$ . Finally, the reverse diffusion process can be achieved by utilizing a well-trained $p _ { \theta } ( \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } )$ to approximate $q ( \mathbf { x } _ { t - 1 } | \mathbf { x } _ { t } , \mathbf { x } _ { 0 } )$ .

AI-Generated Power Allocation Scheme: Motivated by diffusion model-based AI-generated contract [46], we propose an AI-generated power allocation scheme. In deep reinforcement learning (DRL), the intelligent agent learns the optimal policy through interaction with the environment to maximize cumulative rewards. As shown in Fig. 6, the AI-generated algorithm is capable of addressing the challenges posed by high-dimensional state spaces and complex action spaces. Compared to the aforementioned two methods, i.e., Avg-SemCom and Conf-SemCom, this method exhibits superior performance in generating resource allocation schemes. Specifically, we represent the environment using the vector e, which encompasses various factors, such as the wireless channel model, the transmission power $P ,$ and the number of objects U involved in the semantic communication. In this given environment, our objective is to maximize the expected cumulative reward across a series of time steps, aiming to determine the transmission power weights $w _ { i }$ for each object.

![](images/c77b2d8a1d10517a37ddc3f4dde6aeb6430c0f2284d66c54ef08e02c9dc92637.jpg)  
Fig. 6. Design principles of diffusion model. The diffusion model performs multistep denoising on noise and generates an optimal allocation scheme.

We first construct a generative model $\pi _ { \boldsymbol { \theta } } ( \pmb { w } | \pmb { e } )$ that can map the environmental state e. The reverse process of the conditional diffusion model can be represented as follows:

$$
\begin{array}{l} \pi_ {\theta} (\boldsymbol {w} | \boldsymbol {e}) = p _ {\theta} \left(\boldsymbol {w} ^ {0: N} | \boldsymbol {e}\right) \\ = \mathcal {N} (\boldsymbol {w} ^ {N}; 0, \mathbf {I}) \prod_ {i = 1} ^ {N} p _ {\theta} \left(\boldsymbol {w} ^ {j - 1} | \boldsymbol {w} ^ {j}, \boldsymbol {e}\right) \tag {17} \\ \end{array}
$$

where $p _ { \theta } ( \pmb { w } ^ { j - 1 } | \pmb { w } ^ { j } , \pmb { e } )$ can be modeled as a Gaussian distribution $\mathcal { N } ( \boldsymbol { w } ^ { j - 1 } ; \mu _ { \boldsymbol { \theta } } ( \boldsymbol { w } ^ { j } , \boldsymbol { e } , j ) , \Sigma _ { \boldsymbol { \theta } } ( \boldsymbol { w } ^ { j } , \boldsymbol { e } , j ) )$ . According to denoising diffusion probabilistic models (DDPMs) [47], the covariance matrix $\Sigma _ { \theta } ( w ^ { j } , e , j )$ of this Gaussian distribution is $\beta _ { j } \mathbf { I } ,$ and the mean $\pmb { \mu } _ { \boldsymbol { \theta } } ( \pmb { w } ^ { j } , \pmb { e } , j )$ can be represented as $( 1 / \bar { \sqrt { \alpha _ { j } } } ) ( w ^ { j } - ( \beta _ { j } ) / \sqrt { 1 - \bar { \alpha } _ { j } } ) \varepsilon _ { \theta } ( w ^ { j } , e , j ) )$ . Initially, we sample $\pmb { w } ^ { N } \overset { \cdot } { \sim } \mathcal { N } ( 0 , \mathbf { I } )$ , and then from the reverse diffusion chain parameterized by $\theta$ as follows:

$$
\boldsymbol {w} ^ {j - 1} \mid \boldsymbol {w} ^ {j} = \frac {1}{\sqrt {\alpha_ {j}}} \left(\boldsymbol {w} ^ {j} - \frac {\beta_ {j}}{\sqrt {1 - \bar {\alpha} _ {j}}} \varepsilon_ {\theta} (\boldsymbol {w} ^ {j}, \boldsymbol {e}, j)\right) + \sqrt {\beta_ {j}} \varepsilon . \tag {18}
$$

From (18), as can be seen that the result is only related to $w ^ { j }$ and the added noise $\varepsilon .$ Therefore, the training of the denoising process $\pi _ { \theta }$ can be achieved by training $\varepsilon _ { \boldsymbol { \theta } } .$ . Subsequently, we use the quality network $Q _ { \nu }$ to train the $\varepsilon _ { \boldsymbol { \theta } } .$ , which represents the expected cumulative reward that an agent takes an allocation scheme in the current state and executes accordingly. The objective function that needs to be optimized becomes

$$
\pi = \underset {\pi_ {\theta}} {\arg \min} \mathcal {L} (\theta) = - \mathbb {E} _ {\boldsymbol {w} ^ {0} \sim \pi_ {\theta}} \left[ Q _ {v} \left(\boldsymbol {e}, \boldsymbol {w} ^ {0}\right) \right]. \tag {19}
$$

Utilizing the double Q-learning method [48], the network $Q _ { \nu }$ is learned by minimizing the Bellman operator. Consequently, we construct two networks, specifically $Q _ { \nu _ { 1 } }$ and $Q _ { \nu _ { 2 } }$ , along with corresponding target networks $Q _ { \nu _ { 1 } ^ { \prime } } , \ Q _ { \nu _ { 2 } ^ { \prime } } ,$ , and $\pi _ { \theta ^ { \prime } }$ . The optimization of $\nu _ { 1 }$ and $\nu _ { 2 }$ is achieved by minimizing the

Algorithm 2 Diffusion Model-Based AI-Generated Scheme   
Training:   
1: Initial:
2: Initialize replay buffer R and the weights of models, i.e., $\theta$ , $\theta'$ , v, $v'$ 3: for Episode = 1 to Max_episode do
4: Initialize a random process N
5: for Step = 1 to Max_step do
6: Observe the existing environment $e_{t}$ 7: According to (18), set $w_{t}^{N}$ as Gaussian noise and generate allocate scheme $w_{t}^{0}$ by denoising $w_{t}^{N}$ using $\varepsilon_{\theta}$ 8: Combine $w_{t}^{0}$ with the exploration noise $\epsilon$ 9: Execute scheme $w_{t}^{0}$ and observe reward score according to (1)
10: Save the record ( $e_{t}$ , $w_{t}^{0}$ , $\tau_{t}$ ) in R
11: Randomly sample $N_{b}$ records ( $e_{j}$ , $w_{j}$ , $\tau_{j}$ ) from R as a minibatch
12: Minimize the loss to update $Q_{v}$ according to (21)
13: Update $\varepsilon_{\theta}$ by taking gradient descent step on
14: $\nabla_{\theta}\varepsilon_{\theta} \approx \frac{1}{N_{b}}\sum_{j}\nabla_{w^{0}}Q_{v}(e,w^{0})|_{e=e_{j}}\nabla_{\theta}\varepsilon_{\theta}|e_{j}$ 15: $\theta' \leftarrow \tau\theta + (1 - \tau)\theta'$ 16: $v' \leftarrow \tau v + (1 - \tau)v'$ 17: end for
18: end for
19: return $\varepsilon_{\theta}$ Inference:
1: Input e
2: According to (18), denoise Gaussian noise using $\varepsilon_{\theta}$ to generate the optimal allocation scheme $w^{0}$ 3: return The optimal resource allocate scheme $w^{0}$

TABLE I OBJECT DETECTION MODELS TRAINING PARAMETERS 

<table><tr><td>Parameter</td><td>Value</td><td>Parameter</td><td>Value</td></tr><tr><td>Learning Rate</td><td>0.01</td><td>Epochs</td><td>300</td></tr><tr><td>Batch Size</td><td>16</td><td>Momentum</td><td>0.937</td></tr><tr><td>Image Size</td><td>640×640</td><td>Weight Decay</td><td>0.0005</td></tr></table>

![](images/3d14ce1ccb308ce60731d68bf80d9ad1360253af2dfb43ef81bc2d58bcec352b.jpg)

![](images/31df98d0dd201aac29f03f4fb7cbc3749b1b460de4ce6c78c20e0dbf39414be1.jpg)

![](images/4d96ed8fa8591446ec725ca93406170facf87526f5bb815b081e00fe62a1d23c.jpg)

![](images/1fc823666871da55ca184da8009740e8ddfaf615eebb136465207acf9428f8b9.jpg)  
Fig. 7. Partial overview of MinneApple data set.

TABLE II DIFFUSION MODEL-BASED AI-GENERATED ALGORITHM TRAINING PARAMETERS 

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Diffusion Step N = 5</td><td>50</td></tr><tr><td>Batch Size Nb</td><td>512</td></tr><tr><td>Discount Factor γ</td><td>0.95</td></tr><tr><td>Soft Target Update Parameter τ</td><td>0.005</td></tr><tr><td>Exploration Noise ε</td><td>0.05</td></tr><tr><td>The Learning Rate of Network εθ</td><td>10-5</td></tr><tr><td>The Learning Rate of Network Qv</td><td>10-4</td></tr></table>

objective

$$
\mathbb {E} _ {\boldsymbol {w} _ {t + 1} ^ {0} \sim \pi_ {\theta^ {\prime}}} \left[ \left\| \binom {r (\boldsymbol {e}, \boldsymbol {w} _ {t}) + \gamma \min _ {i = 1, 2} Q _ {v _ {i} ^ {\prime}} \left(\boldsymbol {e}, \boldsymbol {w} _ {t + 1} ^ {0}\right)} {- Q _ {v _ {i}} (\boldsymbol {e}, \boldsymbol {w} _ {t})} \right\| ^ {2} \right]. \tag {20}
$$

In DRL, we set the training parameters: batch size $N _ { b }$ , discount factor $\gamma .$ , diffusion step $N ,$ soft target update parameter τ , and exploration noise . The loss function can be represented as follows:

$$
\mathcal {L} = \frac {1}{N _ {b}} \sum_ {j} \left(r _ {j} + \gamma Q _ {v ^ {\prime}} ^ {\prime} \big (\boldsymbol {e} _ {j}, \boldsymbol {w} _ {t} ^ {\prime o} \big) - Q _ {v} \big (\boldsymbol {e} _ {j}, \boldsymbol {w} _ {j} \big)\right) ^ {2}. \tag {21}
$$

Then, we can obtain the optimal allocation scheme based on the wireless communication environment. The detail of the AIgenerated scheme is shown in Algorithm 2. Additionally, the trained diffusive model requires only five denoising process steps during inference to achieve optimized power allocation schemes. Its low computational complexity avoids excessive resource consumption.

# V. NUMERICAL RESULTS

This section primarily presents the experimental settings, materials, and results in this study. Initially, we evaluate the effectiveness of the improvements made to the object detector YOLOv7-X and compare its performance with other stateof-the-art models. Subsequently, we assess the performance of the proposed YOLO-based semantic communication

![](images/0be27dc8ade59b2afd3ed2f49345e3adeec3a14e62c7418b24b6cb4352d18d4d.jpg)

<details>
<summary>line</summary>

| Apple Tree Images | Traditional Communication (MB) | Semantic Communication (MB) |
| ----------------- | ------------------------------ | --------------------------- |
| 0                 | 1.8                            | 0.1                         |
| 50                | 1.9                            | 0.1                         |
| 100               | 1.7                            | 0.1                         |
| 150               | 2.0                            | 0.3                         |
| 200               | 1.8                            | 0.2                         |
| 250               | 1.7                            | 0.2                         |
| 300               | 1.9                            | 0.2                         |
| 350               | 1.9                            | 0.2                         |
</details>

Fig. 8. Comparison of transferred bytes for each image in the two communication methods.

![](images/593b516192b33f9eb5bcfd67c01430495fc785a0fc24d3fdbee4837241d72f31.jpg)

<details>
<summary>line</summary>

| Weight Adjustment Variable η | The Value of Transmission Quality |
| ---------------------------- | ---------------------------------- |
| 0.25                         | 18.71                              |
| 0.5                          | 18.72                              |
| 0.75                         | 18.71                              |
| 1                            | 18.69                              |
| 1.25                         | 18.66                              |
| 1.5                          | 18.62                              |
</details>

(a)

![](images/a3c24e63ce00f32e869608db4e5c8f5026be85236cccaed8543d3ee4a6f380b7.jpg)

<details>
<summary>line</summary>

| Weight Adjustment Variable η | Conf-SemCom | Avg-SemCom |
| ---------------------------- | ----------- | ---------- |
| 0.25                         | 16.69       | 16.64      |
| 0.5                          | 16.72       | 16.64      |
| 0.75                         | 16.73       | 16.64      |
| 1                            | 16.71       | 16.64      |
| 1.25                         | 16.68       | 16.64      |
| 1.5                          | 16.64       | 16.64      |
</details>

(b)

![](images/bffd6288e6d5ac089b0ddbf8e090c536bffdba57d896cd365c8f5f64cdde33f3.jpg)

<details>
<summary>line</summary>

| Weight Adjustment Variable η | Conf-SemCom | Avg-SemCom |
| ---------------------------- | ----------- | ---------- |
| 0.25                         | 14.85       | 14.80      |
| 0.5                          | 14.88       | 14.80      |
| 0.75                         | 14.90       | 14.80      |
| 1.0                          | 14.91       | 14.80      |
| 1.25                         | 14.88       | 14.80      |
| 1.5                          | 14.87       | 14.80      |
</details>

Fig. 9. Curves of transmission quality scores with different weight adjustment variables η and transmission distance D. (a) Transmission Distance D = 10 m. (b) Transmission Distance $D = 2 0$ m. (c) Transmission Distance $D = 3 0$ m.

system, verify the cost savings of semantic communication, and examine the impact of two proposed power allocation schemes on the transmission quality for critical information.

TABLE III RESULTS OF ABLATION EXPERIMENT 

<table><tr><td>Model</td><td>Parameters</td><td>FLOPs</td><td>AP@0.5</td><td>AP@0.5:0.95</td></tr><tr><td>YOLOv7-X</td><td>70.7M</td><td>188.0G</td><td>87.8%</td><td>43.7%</td></tr><tr><td>YOLOv7-X+ELAN-H</td><td>53.5M</td><td>152.6G</td><td>89.1%</td><td>45.4%</td></tr><tr><td>YOLOv7-X+ELAN-H+SimAM</td><td>53.5M</td><td>152.6G</td><td>89.8%</td><td>45.4%</td></tr></table>

TABLE IV COMPARISON OF STATE-OF-THE-ART OBJECT DETECTORS 

<table><tr><td>Model</td><td>Parameters</td><td>FLOPs</td><td>AP@0.5</td><td>AP@0.5:0.95</td><td>FPS</td></tr><tr><td>Faster R-CNN [50]</td><td>41.7M</td><td>59.4G</td><td>74.1%</td><td>33.1%</td><td>34</td></tr><tr><td>RetinaNet [51]</td><td>56.9M</td><td>74.4G</td><td>62.4%</td><td>24.8%</td><td>32</td></tr><tr><td>FCOS [52]</td><td>51.2M</td><td>66.3G</td><td>66.6%</td><td>27.8%</td><td>25</td></tr><tr><td>Scaled-YOLOv4-p5 [53]</td><td>70.2M</td><td>165.1G</td><td>88.3%</td><td>45.9%</td><td>22</td></tr><tr><td>YOLOX-X [39]</td><td>104.5M</td><td>312.0G</td><td>88.4%</td><td>47.0%</td><td>27</td></tr><tr><td>YOLOv5-X</td><td>86.2M</td><td>203.8G</td><td>87.5%</td><td>44.7%</td><td>32</td></tr><tr><td>YOLOR-CSP-X [54]]</td><td>96.4M</td><td>225.5G</td><td>81.3%</td><td>42.0%</td><td>22</td></tr><tr><td>PPYOLOE-X [55]</td><td>95.3M</td><td>204.9G</td><td>88.6%</td><td>45.4%</td><td>19</td></tr><tr><td>Ours</td><td>53.5M</td><td>152.6G</td><td>89.8%</td><td>45.4%</td><td>34</td></tr></table>

# A. Environment Setup

The experimental platform is built on a generic Ubuntu 20.04 system with 2 Intel Xeon Silver 4110 CPUs and GeForce RTX 3090 GPU. The parameters of the object detection model training process used are shown in Table I. The MinneApple data set [49] is the apple image data set used in this experiment. It is a publicly available data set utilized for apple detection and segmentation, containing images of multiple apple varieties at different stages of growth, with a large number of densely packed small apples. The MinneApple data set contains a total of 670 labeled images and 331 unlabeled images. Fig. 7 shows example images from the MinneApple data set.

We use the Fisher-Snedecor  channel model [27] in wireless semantic communication to analyze the performance of our model. The small-scale fading between the UAV and users is represented by the Fisher–Snedecor $\mathcal { F }$ fading distribution, while small-scale variations follow the Nakagami-m distribution and shadowing follows the inverse Nakagami-m distribution [27]. We set the fading parameter $m _ { f } = 6$ , the shadowing parameter $m _ { s } = 6$ and the transmit power P = 3000 W by default. In addition, the parameters of the resource allocation scheme generated by the AI-generated algorithm during the training process are shown in Table II.

# B. Results and Analysis

Results of Ablation Experiment: To evaluate the effectiveness of the ELAN-H and SimAM attention modules, we utilize the amount of parameters and computational complexity, i.e., floating point operations (FLOPs), as well as AP@0.5 and AP@0.5:0.95 as indicators to measure the performance of the models, where AP@0.5 and AP@0.5:0.95 are commonly used evaluation standards in object detection, with higher values indicating better model performance. From the results in Table III, the utilization of the ELAN-H module leads to 1.3% and 1.7% increases in AP@0.5 and AP@0.5:0.95, respectively, while reducing the amount of parameters by 24% and FLOPs by 19%. The incorporation of the SimAM attention module enhances the value of AP@0.5 by 0.8%, with no changes to the amount of parameters and FLOPs.

![](images/4ecc9c4e8c7942d342815fded369300f55be72ebc497bf1edf137023cda5851b.jpg)

<details>
<summary>line</summary>

| Single Apple Images | [Conf-SemCom] Distance:10 m | [Conf-SemCom] Distance:20 m | [Conf-SemCom] Distance:30 m | [Avg-SemCom] Distance:10 m | [Avg-SemCom] Distance:20 m | [Avg-SemCom] Distance:30 m |
| ------------------- | --------------------------- | --------------------------- | --------------------------- | -------------------------- | -------------------------- | -------------------------- |
| 0                   | 0.03                        | 0.08                        | 0.12                        | 0.01                       | 0.03                       | 0.06                       |
| 5                   | 0.02                        | 0.06                        | 0.09                        | 0.01                       | 0.03                       | 0.06                       |
| 10                  | 0.01                        | 0.04                        | 0.06                        | 0.01                       | 0.03                       | 0.06                       |
| 15                  | 0.01                        | 0.03                        | 0.06                        | 0.01                       | 0.03                       | 0.06                       |
| 20                  | 0.01                        | 0.03                        | 0.05                        | 0.01                       | 0.03                       | 0.06                       |
| 25                  | 0.01                        | 0.02                        | 0.05                        | 0.01                       | 0.03                       | 0.06                       |
| 30                  | 0.01                        | 0.02                        | 0.04                        | 0.01                       | 0.03                       | 0.06                       |
</details>

Fig. 10. BER of images at different transmission distances under two transmission methods.

Comparison With Other State-of-the-Art Object Detectors: We conduct a performance comparison of our enhanced YOLOv7-X model with other advanced object detection models. In addition to the comparison items presented in Table III, we also compare the detection speed.

As shown in Table IV, our proposed model achieves the best performance in terms of AP@0.5 compared to other models. Although the performance difference between our proposed model and other advanced YOLO series models is not significant, our model greatly reduces the amount of parameters and FLOPs while achieving the fastest detection speed. However, Faster R-CNN, RetinaNet, and FCOS models, although having smaller parameter size, perform poorly on the MinneApple data set, which contains many small objects, and their detection performance fails to meet the requirements of our proposed scenarios.

![](images/c142ebf6e088af0a0d9a24f1f02c76900d191cd11debce47aaa6c75936b1ab74.jpg)

<details>
<summary>heatmap</summary>

| Apples: | a | b | c | ... | d | e | ... | f | g | h |
|---|---|---|---|---|---|---|---|---|---|---|
| D = 10 m | 0.912 | 0.805 | 0.930 | ... | 0.965 | 0.957 | ... | 0.948 | 0.967 | 0.971 |
| D = 10 m | 0.968 | 0.846 | 0.960 | ... | 0.962 | 0.949 | ... | 0.913 | 0.946 | 0.935 |
| D = 20 m | 0.769 | 0.536 | 0.797 | ... | 0.910 | 0.859 | ... | 0.795 | 0.877 | 0891 |
| D = 20 m | 0.885 | 0.736 | 0.920 | ... | 0.892 | 0.794 | ... | 0.737 | 0.839 | 0.813 |
| D = 30 m | 0.725 | 0.419 | 0.750 | ... | 0.814 | 0.746 | ... | 0.705 | 0.833 | 0.824 |
| D = 30 m | 0.790 | 0.578 | 0.815 | ... | 0.819 | 0.728 | ... | 0.633 | 0.735 | 0.747 |
</details>

Fig. 11. Transmission effects and corresponding SSIM values of partial images at different transmission distances. The odd-numbered rows are Conf-SemCom and the even-numbered rows are Avg-SemCom.

The Effects of Reducing Communication Overhead: We use 331 unannotated test images from the MinneApple data set as the images to be sent by the UAV. Fig. 8 illustrates a comparison between the data size of images transmitted through conventional communication methods and the data size resulting from semantic communication after the implementation of semantic feature extraction. The aggregate size of the original images amounts to 595.2 MB. However, following semantic feature extraction, the volume of data required for transmission by edge devices is considerably reduced to 55.4 MB, encompassing 54.8 MB of image format data and 0.6 MB of text format data. This reduction corresponds to a 91% decrease in communication costs, thereby substantially minimizing power consumption during transmission.

The Effect of η on Conf-SemCom: Given that the textual data required for transmission by the UAV is considerably smaller than image data, we focus solely on the impact of wireless transmission environments on the semantic information transfer of image formats. Taking Fig. 5 as an example, the UAV first detects that the image contains 30 objects and then allocates power for transmission according to the confidence of each object. We first show the effectiveness of the proposed Conf-SemCom method. Additionally, to investigate the impact of variable η on the transmission performance, we increase η from 0.25 to 1.5 and the transmission distance from 10 to 30 m. Each experiment is repeated 100 times, and the average results are shown. The curves of transmission quality values (i.e., MIST scores) are shown in Fig. 9. It can be observed that due to allocating more resources to important information, Conf-SmeCom outperforms the Avg-SemCom method in most cases, with its effectiveness becoming more evident as the transmission distance increases. Furthermore, the optimal value of variable η varies across different transmission distances. At transmission distances of 10, 20, and 30 m, the highest MIST scores are achieved when η equals 0.5, 0.75, and 1, respectively. This indicates that appropriately increasing the value of variable η as the transmission distance increases, while keeping the total power P unchanged, allows for a better enhancement of overall communication quality by increasing the transmission power pi for more significant objects i.

The Effects of Power Allocation: We investigate the impact of two power allocation methods, i.e., Avg-SemCom and Conf-SemCom, on the transmission quality of images with different levels of confidence, over different transmission distances (i.e., 10, 20, and 30 m). As shown in Fig. 10, the horizontal axis represents the 30 detected images, sorted in ascending order of confidence levels, and the vertical axis represents the bit error rate (BER) values derived from the channel model according to the allocated power. It is evident that, as the distance increases, the image transmission quality declines for both communication methods. However, Conf-SemCom opts to allocate more power to semantically important information, resulting in reduced error rates for crucial semantic information even under poor channel conditions.

![](images/9be8e6667ffbd4bca59e6a8922372ca878d1494a63705660bd80506519e47a7a.jpg)

<details>
<summary>line</summary>

| Iteration Number | AI-Generated Scheme | Conf-SemCom | Avg-SemCom |
| ---------------- | ------------------- | ----------- | ---------- |
| 0                | 17.15               | 17.20       | 17.05      |
| 1000             | 17.22               | 17.18       | 17.06      |
| 2000             | 17.24               | 17.19       | 17.07      |
| 3000             | 17.23               | 17.20       | 17.06      |
| 4000             | 17.25               | 17.21       | 17.07      |
| 5000             | 17.24               | 17.20       | 17.06      |
| 5500             | 17.23               | 17.19       | 17.05      |
</details>

Fig. 12. Comparison of the training process of the diffusion model-based AIgenerated algorithm and the results of two other methods (i.e., Avg-SemCom and Conf-SemCom), with transmission distance $D = 2 0$ m and transmission power $P = 4 ~ \mathrm { k W } .$

To facilitate a comprehensive comparison between the two power allocation methods, Fig. 11 illustrates the transmission performance of select images at various communication distances. We use SSIM to evaluate the transmission quality of each object. From Fig. 11, the transmitted image quality for both methods degrades significantly as the transmission distance increases. Moreover, due to the uniformed distribution of transmission power, the SSIM values transmitted by Avg-SemCom for each image exhibit a relatively uniform and irregular pattern, resulting in certain critical images possessing inferior transmission quality compared to original images. For instance, apples a and c are heavily occluded and contain very little usable information. The significance of semantic features for these images is less than that for other images. However, their transmission quality surpasses that of other images, which is unreasonable. In contrast, Conf-SemCom allocates increased power to salient images, enabling the highquality transmission of these images even in poor channel conditions.

The Effects of AI-Generated Scheme: We compare the diffusion model-based AI-generated scheme with two other transmission power allocation methods for transmitting semantic information at the transmission distance $D = 2 0$ m and the transmission power P = 4 kW. As illustrated in Fig. 12, the diffusion model-based AI-generated algorithm exhibits rapid training speed during the optimization of power allocation schemes, surpassing the confidence-based allocation scheme at approximately 500 iterations. The superiority of the AI-generated approach primarily stems from the exploration conducted through the diffusion method, which enhances the flexibility of strategies and prevents the model from getting trapped in suboptimal solutions. Furthermore, it is evident that the Avg-SemCom method significantly underperforms in terms of the MIST score compared to the other two schemes, indicating the necessity of considering the importance of semantic information during the communication process.

# VI. CONCLUSION

In this article, we have proposed a YOLO-based semantic communication framework for developing a virtual apple orchard case, focusing on optimizing semantic information transmission and resource allocation for images collected by edge devices. Initially, we have enhanced the performance of the object detector YOLOv7-X on a real apple data set and have employed the optimized object detector to extract semantic information from images captured by edge devices, aiming to reduce transmission costs. Furthermore, to ensure the high-quality transmission of essential semantic information, we have allocated resource based on the significance of their semantic content. Specifically, we have allocated the transmission power of semantic information based on the confidence generated by the object detection algorithm and the scheme generated by the diffusion model-based AI-generated algorithm, respectively. Numerical results have demonstrated that the proposed framework and strategy have considerably reduced communication costs and have markedly improved the transmission quality of important information during communication.

# REFERENCES

[1] N. H. Chu, D. T. Hoang, D. N. Nguyen, K. T. Phan, and E. Dutkiewicz, “MetaSlicing: A novel resource allocation framework for metaverse,” 2022, arXiv:2205.11087.   
[2] D. Wu, Z. Yang, P. Zhang, R. Wang, B. Yang, and X. Ma, “Virtual-reality interpromotion technology for metaverse: A survey,” IEEE Internet Things J., vol. 10, no. 18, pp. 15788–15809, Sep. 2023.   
[3] Y. Wu, K. Zhang, and Y. Zhang, “Digital twin networks: A survey,” IEEE Internet Things J., vol. 8, no. 18, pp. 13789–13804, Sep. 2021.   
[4] C. Feng, X. Bin, L. Na, L. Haishen, and S. Chuanheng, “The metaverse for agriculture,” Smart Agricult., vol. 4, pp. 126–137, Sep. 2022.   
[5] S. Neethirajan and B. Kemp, “Digital twins in livestock farming,” Animals (Basel), vol. 11, no. 4, p. 1008, 2021.   
[6] P. Tan. “Tech forum: Accelerating digitalization with new technology.” 2021. [Online]. Available: https://www.alibabacloud.com/zh/ apsara-conference-2021   
[7] C. Khansulivong, S. Wicha, and P. Temdee, “Adaptive of new technology for agriculture online learning by metaverse: A case study in faculty of agriculture, National University of Laos,” in Proc. Joint Int. Conf. Digital Arts, Media Technol. ECTI Northern Sect. Conf. Electr. Electron., Comput. Telecommun. Eng. (ECTI DAMT NCON), 2022, pp. 428–432.   
[8] Y. Han et al., “A dynamic hierarchical framework for IoT-assisted digital twin synchronization in the metaverse,” IEEE Internet Things J., vol. 10, no. 1, pp. 268–284, Jan. 2023.   
[9] L. U. Khan, W. Saad, D. T. Niyato, Z. Han, and C. S. Hong, “Digitaltwin-enabled 6G: Vision, architectural trends, and future directions,” IEEE Commun. Mag., vol. 60, no. 1, pp. 74–80, Jan. 2022.   
[10] M. S. Farooq, S. Riaz, A. Abid, K. Abid, and M. A. Naeem, “A survey on the role of IoT in agriculture for the implementation of smart farming,” IEEE Access, vol. 7, pp. 156237–156271, 2019.   
[11] D. S. Paraforos and H. W. Griepentrog, Digital Farming and Field Robotics: Internet of Things, Cloud Computing, and Big Data. Cham, Switzerland: Springer Int., 2021, pp. 365–385. [Online]. Available: https://doi.org/10.1007/978-3-030-704   
[12] E. C. Strinati and S. Barbarossa, “6G networks: Beyond Shannon towards semantic and goal-oriented communications,” Comput. Netw., vol. 190, May 2021, Art. no. 107930.   
[13] P. Zhang et al., “Toward wisdom-evolutionary and primitive-concise 6G: A new paradigm of semantic communication networks,” Engineering, vol. 8, pp. 60–73, Jan. 2022.   
[14] W. C. Ng, H. Du, W. Y. B. Lim, Z. Xiong, D. T. Niyato, and C. Miao, “Stochastic resource allocation for semantic communication-aided virtual transportation networks in the metaverse,” 2022, arXiv:2208.14661.   
[15] C. Dong, H. Liang, X. Xu, S. Han, B. Wang, and P. Zhang, “Semantic communication system based on semantic slice models propagation,” IEEE J. Sel. Areas Commun., vol. 41, no. 1, pp. 202–213, Jan. 2023.

[16] Y. Han et al., “A dynamic hierarchical framework for IoT-assisted metaverse synchronization,” 2022, arXiv:2203.03969.   
[17] K. Li et al., “When Internet of Things meets metaverse: Convergence of physical and cyber worlds,” IEEE Internet Things J., vol. 10, no. 5, pp. 4148–4173, Mar. 2023.   
[18] W. Li, D. Zhu, and Q. Wang, “A single view leaf reconstruction method based on the fusion of ResNet and differentiable render in plant growth digital twin system,” Comput. Electron. Agric., vol. 193, Feb. 2022, Art. no. 106712.   
[19] P. Angin, M. H. Anisi, F. Göksel, C. Gürsoy, and A. Büyükgülcü, “AgriLoRa: A digital twin framework for smart agriculture,” J. Wireless Mob. Netw. Ubiquitous Comput. Dependable Appl., vol. 11, no. 4, pp. 77–96, 2020.   
[20] M. Awais, W. Li, H. Li, M. J. M. Cheema, S. Hussain, and C. Liu, “Optimization of intelligent irrigation systems for smart multi-spectral unmanned aerial vehicle and digital twins modeling,” Environ. Sci. Proc., vol. 23, no. 1, p. 13, Dec. 2022.   
[21] Q. Lan et al., “What is semantic communication? A view on conveying meaning in the era of machine intelligence,” JCIN, vol. 6, no. 4, pp. 336–371, Dec. 2021.   
[22] H. Xie, Z. Qin, G. Y. Li, and B.-H. Juang, “Deep learning enabled semantic communication systems,” IEEE Trans. Signal Process., vol. 69, pp. 2663–2675, Apr. 2021.   
[23] A. Vaswani et al., “Attention is all you need,” 2017, arXiv:1706.03762.   
[24] F. Zhou, Y. Li, X. Zhang, Q. Wu, X. Lei, and R. Q. Hu, “Cognitive semantic communication systems driven by knowledge graph,” in Proc. ICC 2022–IEEE Int. Conf. Commun., 2022, pp. 4860–4865.   
[25] M. Lokumarambage, V. S. S. Gowrisetty, H. Rezaei, T. Sivalingam, R. M. A. P. Rajatheva, and W. Fernando, “Wireless end-to-end image transmission system using semantic communications,” 2023, arXiv:2302.13721.   
[26] H. Zhang, S. Shao, M. Tao, X. L. Bi, and K. B. Letaief, “Deep learning-enabled semantic communication systems with task-unaware transmitter and dynamic data,” IEEE J. Sel. Areas Commun., vol. 41, no. 1, pp. 170–185, Jan. 2023.   
[27] J. Kang et al., “Personalized saliency in task-oriented semantic communications: Image transmission and performance analysis,” IEEE J. Sel. Areas Commun., vol. 41, no. 1, pp. 186–201, Jan. 2023.   
[28] J. Lv, “Recognition of overlapping and occluded fruits in natural environment,” J. Comput. Theoret. Nanosci., vol. 13, no. 4, pp. 2475–2484, 2016.   
[29] X. Liu, D. Zhao, W. Jia, W. Ji, and Y. Sun, “A detection method for apple fruits based on color and shape features,” IEEE Access, vol. 7, pp. 67923–67933, 2019.   
[30] W. Chen, J. Zhang, B. Guo, Q. T. Wei, and Z. Zhu, “An apple detection method based on des-YOLO v4 algorithm for harvesting robots in complex environment,” Math. Probl. Eng., vol. 2021, Oct. 2021, Art. no. 7351470.   
[31] B. Yan, P. Fan, X. Lei, Z. Liu, and F. Yang, “A real-time apple targets detection method for picking robot based on improved YOLOv5,” Remote. Sens., vol. 13, no. 9, p. 1619, 2021.   
[32] Ultralytics. “YOLOv5.” Accessed: Sep. 10, 2022. [Online]. Available: https://github.com/ultralytics/yolov5   
[33] M. Sun, L. Xu, X. Chen, Z. Ji, Y. Zheng, and W. Jia, “BFP net: Balanced feature pyramid network for small apple detection in complex orchard environment,” Plant Phenom., vol. 2022, Sep. 2022, Art. no. 9892464.   
[34] C.-Y. Wang, A. Bochkovskiy, and H.-Y. M. Liao, “YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors,” 2022, arXiv:2207.02696.   
[35] A. Bochkovskiy, C.-Y. Wang, and H.-Y. M. Liao, “YOLOv4: Optimal speed and accuracy of object detection,” 2020, arXiv:2004.10934.   
[36] H. Zhang, M. Cissé, Y. Dauphin, and D. Lopez-Paz, “mixup: Beyond empirical risk minimization,” 2017, arXiv:1710.09412.   
[37] F. K. Shaikh, S. Karim, S. Zeadally, and J. Nebhen, “Recent trends in Internet-of-Things-enabled sensor technologies for smart agriculture,” IEEE Internet Things J., vol. 9, no. 23, pp. 23583–23598, Dec. 2022.   
[38] Z. Wang, A. C. Bovik, H. R. Sheikh, and E. P. Simoncelli, “Image quality assessment: From error visibility to structural similarity,” IEEE Trans. Image Process., vol. 13, no. 4, pp. 600–612, Apr. 2004.   
[39] Z. Ge, S. Liu, F. Wang, Z. Li, and J. Sun, “YOLOX: Exceeding YOLO series in 2021,” 2021, arXiv:2107.08430.   
[40] Y. Rao, W. Zhao, Y. Tang, J. Zhou, S. N. Lim, and J. Lu, “HorNet: Efficient high-order spatial interactions with recursive gated convolutions,” 2022, arXiv:2207.14284.   
[41] L. Yang, R.-Y. Zhang, L. Li, and X. Xie, “SimAM: A simple, parameterfree attention module for convolutional neural networks,” in Proc. Int. Conf. Mach. Learn., vol. 139, Jul. 2021, pp. 11863–11874.

[42] J. Park, S. Woo, J.-Y. Lee, and I.-S. Kweon, “Bam: Bottleneck attention module,” in Proc. Brit. Mach. Vis. Conf., 2018.   
[43] S. Woo, J. Park, J.-Y. Lee, and I.-S. Kweon, “CBAM: Convolutional block attention module,” in Proc. Eur. Conf. Comput. Vis. (ECCV), 2018, pp. 3–19.   
[44] B. S. Webb, N. T. Dhruv, S. G. Solomon, C. Tailby, and P. Lennie, “Early and late mechanisms of surround suppression in striate cortex of macaque,” J. Neurosci., vol. 25, pp. 11666–11675, Dec. 2005.   
[45] L. Yang et al., “Diffusion models: A comprehensive survey of methods and applications,” 2022, arXiv:2209.00796.   
[46] H. Du, J. Wang, D. Niyato, J. Kang, Z. Xiong, and D. In Kim, “AI-generated incentive mechanism and full-duplex semantic communications for information sharing,” 2023, arXiv:2303.01896.   
[47] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,” 2020, arXiv:2006.11239.   
[48] H. V. Hasselt, “Double Q-learning,” in Proc. NIPS, 2010, pp. 1–9.   
[49] N. Häni, P. Roy, and V. Isler, “MinneApple: A benchmark dataset for apple detection and segmentation,” IEEE Robot. Autom. Lett., vol. 5, no. 2, pp. 852–858, Apr. 2020.   
[50] S. Ren, K. He, R. B. Girshick, and J. Sun, “Faster R-CNN: Towards real-time object detection with region proposal networks,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 39, no. 6, pp. 1137–1149, Jun. 2017.   
[51] T.-Y. Lin, P. Goyal, R. B. Girshick, K. He, and P. Dollár, “Focal loss for dense object detection,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 42, no. 2, pp. 318–327, Feb. 2020.   
[52] Z. Tian, C. Shen, H. Chen, and T. He, “FCOS: Fully convolutional onestage object detection,” in Proc. IEEE Int. Conf. Comput. Vis., 2019, pp. 9626–9635.   
[53] C.-Y. Wang, A. Bochkovskiy, and H.-Y. M. Liao, “Scaled-YOLOv4: Scaling cross stage partial network,” in Proc. IEEE Conf. Comput. Vis. Pattern Recog., 2020, pp. 13024–13033.   
[54] C.-Y. Wang, I.-H. Yeh, and H. Liao, “You only learn one representation: Unified network for multiple tasks,” J. Inf. Sci. Eng., vol. 39, pp. 691–709, May 2021.   
[55] S. Xu et al., “PP-YOLOE: An evolved version of YOLO,” 2022, arXiv:2203.16250.

![](images/db71b1a5bdef3aa5df55b64734a604e5917ff8c1cc07a62c601c83546bd66122.jpg)

<details>
<summary>natural_image</summary>

Portrait of a young man in a sports jersey (no text or symbols visible)
</details>

Baoxia Du (Graduate Student Member, IEEE) received the B.S. degree from Shandong University of Science and Technology, Qingdao, China, in 2020. He is currently pursuing the M.S. degree with the School of Information and Control Engineering, Jilin Institute of Chemical Technology, Jilin City, China.

His current research interests include deep learning, computer vision, and semantic communication.

![](images/e63e814371cd2dd85af2f302b177d828925e98ec24341efbb704b0d63d16efba.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man in formal attire (no text or symbols visible)
</details>

Hongyang Du (Graduate Student Member, IEEE) received the B.S. degree from Beijing Jiaotong University, Beijing, China, in 2021. He is currently pursuing the Ph.D. degree with the School of Computer Science and Engineering, Energy Research Institute, Nanyang Technological University, Singapore, under the Interdisciplinary Graduate Program.

His research interests include semantic communications, resource allocation, and communication theory.

Mr. Du was the recipient of the IEEE Daniel E. Noble Fellowship Award in 2022. He was recognized as an Exemplary Reviewer of the IEEE TRANSACTIONS ON COMMUNICATIONS in 2021.

![](images/9661872febd812403824af6e4f03dd19350ecaf4718573895f2421ae48862065.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man in uniform (no visible text or symbols)
</details>

Haifeng Liu received the Ph.D. degree from Northeast Forestry University, Harbin, China, in 2010.

He is currently an Associate Professor with the Agricultural College, Yanbian University, Yanji, China. His research interests include crops and plant protection.

![](images/76423a31a0083c203d52b24a056158a0eac362a54c1121d60d423b00ddfb1643.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man (no text or symbols visible)
</details>

Jun Yu received the M.S. degree from Changchun University of Science and Technology, Changchun, China, in 2002.

He is currently a Professor with the School of Information and Control Engineering, Jilin Institute of Chemical Technology, Jilin City, China. His research interests include intelligent information processing and intelligent control.

![](images/b90601fa645817f8ec1cf982f977cfe5761dece46350c1daea6bc87cd9e27a03.jpg)

<details>
<summary>natural_image</summary>

Black-and-white portrait of a person wearing glasses and a dark jacket (no visible text or symbols)
</details>

Dusit Niyato (Fellow, IEEE) received the B.Eng. degree from the King Mongkut’s Institute of Technology Ladkrabang, Bangkok, Thailand, in 1999, and the Ph.D. degree in electrical and computer engineering from the University of Manitoba, Winnipeg, MB, Canada, in 2008.

He is currently a Professor with the School of Computer Science and Engineering, Nanyang Technological University, Singapore. His research interests are in the areas of the Internet of Things, machine learning, and incentive mechanism design.

![](images/dff3511e9fa24cf69293680123b4dbd970d7f4596f2afb64e53d2943a2a0158d.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a man in formal attire (no text or symbols visible)
</details>

Mingyang Qi received the M.S. degree from Changchun University of Technology, Changchun, China, in 2015.

He is currently a Lecturer with the Electrical and Information Engineering College, Jilin Agricultural Science and Technology University, Jilin City, China. His current research interests include deep learning and computer vision.

![](images/aa8b7abe1c112a31ddfe7f1c6a14d3b577b2657967a5669438918a2f02e32f95.jpg)

<details>
<summary>natural_image</summary>

Portrait photo of a young man in a polo shirt (no text or symbols visible)
</details>

Peng Xin received the Ph.D. degree from Harbin University of Science and Technology, Harbin, China, in 2018.

He is currently an Associate Professor with the School of Information and Control Engineering, Jilin Institute of Chemical Technology, Jilin City, China. His research interests include the application of artificial intelligence technology and equipment internal fault diagnosis.

![](images/39a72769486bf0405eee68152bc76b7372e1aa4bc66c55856d52020d0a396450.jpg)

<details>
<summary>natural_image</summary>

Portrait of a man in formal suit and tie (no text or symbols visible)
</details>

You Tang received the Ph.D. degree from Northeast Agricultural University, Harbin, China, in 2017.

He is currently a Professor with the Electrical and Information Engineering College, Jilin Agricultural Science and Technology University, Jilin City, China. His research interests include bioinformatics and software engineering.