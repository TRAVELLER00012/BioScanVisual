import streamlit as st
import pandas as pd

st.title("BioScan")
st.divider()

info = pd.DataFrame({
    "Field": [
        "By",
        "Research Position",
        "Research Support",
        "Grade Level",
        "Email",
        "GitHub"
    ],
    "Value": [
        "Daksh Kumar",
        "Software Developer and Data Analyst",
        "Christian Medical College (CMC), Ludhiana",
        "Class XII (CBSE)",
        "k.daksh29@gmail.com",
        "https://github.com/TRAVELLER00012"
    ]
})

st.table(info,hide_index=True,width="stretch",border='horizontal',hide_header=True)

st.space("large")

st.header("Introduction",divider="gray")
st.markdown("""
BioScan originated as an idea to automate automated blood cell enumeration and quantification in blood smear samples. Detecting the concentration of blood cells in samples is crucial in identifying possible infections, blood disorders, anaemia, leukaemia, and other diagnoses; this is done by examining the number of RBCs (red blood cells), WBCs (white blood cells), and platelets.

Generally, there are two ways current medicine records this number. 3-part/5-part differential analysers: these machines provide concentrations of blood cells per microlitre (μL); however, they are expensive, bulky, and may not be readily available in all healthcare settings. Another more traditional method is by using manual counting. Blood smear samples are placed under a microscope (mostly 100x zoom), and a trained laboratory technician visually examines the sample; thereby, the count of blood cells is estimated by manually counting. Even though this method is simple and easy to perform, human error, time consumption, human fatigue, and lack of trained specialists at certain places could accompany this process.

This is where BioScan shines; it is a computer vision model trained on hundreds of blood smear samples to detect and estimate the count of blood cells from images within seconds. BioScan uses a lightweight YOLO model for its computer vision detection process; thereby, it requires no special heavy hardware to operate on. It needs just a microscope and a phone to take images; it can give results with amazingly high accuracy within seconds at the press of a single button. It requires no previous technical expertise to operate.

""")

st.space("large")

st.subheader("Research Motivation",divider="gray")
st.markdown("""
Blood tests are one of the most crucial and widely performed tests worldwide; early detections and results can improve procedures' outcomes. But as advanced healthcare systems and trained specialists are not present in all clinics, especially in rural areas and small cities, they lack the systems to perform accurate blood tests. BioScan provides an easy, fast, and cheap way to perform blood cell counting. Not only in resource-limited settings, BioScan proves to be functional at tertiary care hospitals by providing a second opinion on tests or just speeding up the process.

The goal of BioScan is not to replace laboratory professionals but to investigate whether modern computer vision techniques can provide a low-cost, accessible, and efficient tool for blood smear analysis.
""")

st.space("large")

st.subheader("Role of Computer Vision in Medical Imaging",divider="gray")

st.markdown("Computer vision is a general term for a process that uses deep neural networks to analyse visual information. These neural networks are trained for hours on powerful GPUs and good-quality datasets to adjust their weights for accurate object detection.")
st.markdown("Our computer vision models are trained on blood smear images, an example of which is shown. Within it, a metadata file has all the information about their RBCs, WBCs, and platelets present, and an example of bounding boxes is also shown. Many images like this are used to train the neural network. Each box encloses a blood cell and has their respective label stored.")

col1, col2 = st.columns(2,vertical_alignment ="center",gap="medium",border=True)
with col1:
    st.image("./images/1_img.png",caption="Without Annotations")
with col2:
    st.image("./images/2_img.png",caption="With Annotations")


st.space("large")

st.header("Objectives",divider="gray")

st.text("The pipeline of this project looks something like this:")

st.space("small")

col1,col2,col3,col4,col5 = st.columns(5,gap="medium",border=True)

with col1:
    st.markdown("""
##### Data Collection
Collect sufficient amount of images for CV training.
""")
    
with col2:
        st.markdown("""
##### Annotations
Draw boxes and store coordinates of each box with their respective label (RBC, WBC, Platelet) in a metadata file.
                    """)
        
with col3:
        st.markdown("""
##### Train the Neural Network
Using YOLO with 100 epochs (cycles), 2048 image resolution, batch size of 1, and a rented GPU.
""")

with col4:
        st.markdown("""
##### Analyse
Review the results.png, confusion matrix, and practically test the model.
""")
        
with col5:
        st.markdown("""
##### Attempt to Reach Perfection
Continue improving the model by refining the dataset, using more powerful models, increasing GPU capability, and making other optimizations.
""")

st.space("small")
st.markdown("""
However, this is a very simplistic version of the journey for the model, as will be shown in the “Journey” section of this research; the actual pipeline is way more complicated than what is described.
The diagram gives a good representation of what process I followed, more details about the number of images collected, how annotations worked, how I optimized it to save time and my energy, what errors I encountered in my dataset, and while training early models, what errors they faced and guided to which direction; how I made the final model with high accuracy; and a very important and confusing irony of this project, which I faced since the very beginning of this project. I have explained all of this in the coming sections of “Methodology” and “Journey” (the largest section).
""")

st.space("large")

st.header("Methodology")
st.subheader("Dataset Collection",divider="gray")

st.space("small")

st.markdown("""
The process started with collecting real time blood smear samples, using a steady phone stand and my phones’ camera to collect. 
""")

st.space("small")

col1 , col2 = st.columns(2,vertical_alignment ="center",gap="medium",border=True)

with col1:
    st.image("./images/3.png")

with col2:
    st.image("./images/4.png")

st.space("small")

col3,col4 = st.columns(2,vertical_alignment ="center",gap="medium",border=True)

with col3:
    st.image("./images/5.png")

with col4:
    st.image("./images/6.png")

st.space("small")

st.markdown("Blood smear images contain several visually distinct cellular components that make them suitable for computer vision-based analysis. Red blood cells (RBCs) appear as numerous light pink circular structures and constitute the majority of cells within a typical blood smear. White blood cells (WBCs) are larger, less abundant cells that stain dark purple due to the presence of nuclei. Platelets appear as small purple-stained cellular fragments and are significantly smaller than both RBCs and WBCs. These differences in size, morphology, and staining characteristics enable object detection models to distinguish between the three cell types. During the annotation process, bounding boxes were assigned to individual RBCs, WBCs, and platelets, allowing the model to learn the visual features associated with each class and perform automated detection and enumeration.")

st.space("small")

col1 , col2 = st.columns(2,vertical_alignment ="center",gap="medium",border=True)

with col1:
    st.image("./images/7.png")

with col2:
    st.image("./images/8.png")

st.space("small")

col3,col4 = st.columns(2,vertical_alignment ="center",gap="medium",border=True)

with col3:
    st.image("./images/9.png")

with col4:
    st.image("./images/10.png")

st.caption("(Manual annotations)")

st.space("small")
st.markdown("""
In total of 200 images there are a total of 354,470 labelled cells. More precisely: 335,635 RBCs, 16,256 platelets, and 2,579 WBCs. The dataset was split into 80% of training data, 10% test data and 10% validation data. With their respective counts of annotations:
""")

dataset_split = pd.DataFrame({
    "RBCs": [259521, 50866, 25248],
    "WBCs": [2001, 373, 205],
    "Platelets": [12103, 2684, 1469]
}, index=["Training Set", "Test Set", "Validation Set"])

st.dataframe(dataset_split)

st.space("small")

st.bar_chart(dataset_split,stack=False,sort=True,horizontal=True,x_label="Dataset",y_label="Count")

st.space("small")

st.markdown("""
It can be observed that there is a class size disparity since in each image sample, RBC counts tend to dominate WBCs and platelets; this did become an issue on earlier, smaller datasets that were used to prepare older prototypes for this project.\

This project has had its own versions of dataset sizes, starting with 2 annotated images and, after that, 29, 52, 100, and, lastly, 200 annotated images.

The error of class disparity and insufficient data of WBCs and platelets wasn’t greatly solved until 200 images were annotated. The first 2 images, which were 1024 resolution, were capable of only detecting RBCs and drawing barely acceptable bounding boxes around them. The 29-image mark, trained at 1280-image resolution, showed the first detection of platelets and WBCs; however, that too was one in hundreds. It wasn’t until the 100-image mark (2048-image resolution) that the model had finally gotten a good grasp on WBCs and platelets; the only errors it made were with WBCs due to the smaller number of WBC types in the dataset, which was the reason to go up to 200 images.

Examples of models trained on each dataset and their results are shown:            
""")


col1,col2,col3,col4,col5 = st.columns(5,vertical_alignment="center",gap="medium")

with col1:
    st.image("./images/11.png",caption="2 Images")
with col2:
    st.image("./images/12.png",caption="29 Images")
with col3:
    st.image("./images/13.png",caption="52 Images")
with col4:
    st.image("./images/14.png",caption="100 Images")
with col5:
    st.image("./images/15.png",caption="200 Images")

st.space("small")

dataset_vram = pd.DataFrame({
    "Dataset Size": [2, 29, 52, 100, 200],
    "Img Resolution": [1024, 1280, 1280, 2048, 2048],
    "Batch Size": [1, 1, 1, 1, 1],
    "GPU VRAM": [4, 26, 26, 32, 48]
})
dataset_vram.set_index("Dataset Size",inplace=True)

st.dataframe(dataset_vram)

st.space("small")

st.subheader("Process of annotations",divider="gray")

st.markdown("""
The most time-consuming part of this project was annotating the collected images. To annotate images, the Python library “anylabelling” was used. It provides a GUI interface to manually draw bounding boxes and to give them their respective labels. It has another great feature: it allows users to import their own computer vision models for auto-labelling. That was the motivation behind training the model on only 2 images at the start; using that model, I auto-labelled many of the blood cells. It reduced the time for me to draw boxes, allowing me to focus only on the classification or any other errors it made. Each new dataset provided a better model which greatly helped with the auto-labelling process, reducing my time and efforts to manually annotate.
            
It is important to note that the process of auto-labelling didn’t solve all the problems; I still had to manually fix labels, redraw incorrect bounding boxes, and take care of edge cases.
            
Auto-labelling actually caused some harm in the first 100 annotated images; the model was classifying clumps of RBCs into a single WBC. The model is not supposed to detect clumps as one big cell and not at all classify RBCs as WBCs; this was an error caused by the insufficiency of the model used to annotate the 100 images. Since that issue persisted as it wasn’t checked, the first-ever model on 100 images showed worse results than the 52-image dataset. Thereby, I had to manually fix all labelling and bounding box errors in the dataset.
""")

st.space("small")

st.subheader("Model Training",divider="gray")

st.markdown("""
The project was overall trained on multiple models of YOLO; the final project uses the latest version, YOLO 26x. The project started with the use of 8s for the very first prototype (2-image dataset), but I upgraded the GPU specifications to accompany the increased image resolution, model parameters, and annotations.
""")

st.text("Best Model: In Practical runs")


runs_best = pd.DataFrame({
    "Parameter": [
        "Model Architecture",
        "GPU , VRAM(GB)",
        "Training Epochs",
        "Total Annotations",
        "Image Resolution",
        "Best Precision",
        "Best Recall",
        "Best mAP50",
        "Best mAP50-95"
    ],
    "Value": [
        "YOLO26x",
        "RTX 4090D, 48GB VRAM",
        100,
        354470,
        "2048x2048",
        "99.99%",
        "31.30%",
        "31.33%",
        "22.97%"
    ]
})


st.dataframe(runs_best,hide_index=True)

st.space("small")

st.text("This model has performed the best when tested practically, but in terms of metrics it shouldn’t perform this good. Comparing with other models trained on the same data:")

models = pd.DataFrame({
    "Model": [
        "YOLOv8l",
        "YOLO11m",
        "YOLOv8m",
        "YOLO11x",
        "YOLOv8x",
        "YOLO11l",
        "YOLO26m",
        "YOLO26x",
        "YOLO26l"
    ],
    "Best mAP50": [
        0.447,
        0.413,
        0.387,
        0.381,
        0.375,
        0.371,
        0.323,
        0.313,
        0.291
    ],
    "Recall": [
        0.453,
        0.415,
        0.388,
        0.430,
        0.376,
        0.370,
        0.321,
        0.313,
        0.290
    ]
})

st.dataframe(models,hide_index=True)

st.space("small")

st.markdown("""
A total of nine YOLO-based architectures were evaluated on the final 200-image BioScan dataset, including models from the YOLOv8, YOLO11, and YOLO26 families. Among all tested architectures, YOLOv8l achieved the highest quantitative performance with an mAP50 score of 0.447 and a recall of 0.453, making it the strongest model according to standard object detection metrics. YOLO11m followed closely with an mAP50 of 0.413, while YOLOv8m achieved an mAP50 of 0.387. Across all model families, larger variants did not consistently outperform their medium-sized counterparts. YOLO11m outperformed both YOLO11l and YOLO11x, while YOLO26m achieved better benchmark results than YOLO26l and YOLO26x. These findings suggest that increasing model size alone was insufficient to improve performance on the current dataset.
            
During qualitative evaluation, a notable discrepancy was observed between benchmark metrics and practical performance. Although YOLOv8l achieved the highest validation scores, it frequently misclassified clusters of red blood cells as white blood cells during manual inspection. Similar behaviour was observed in YOLOv8x, though to a lesser extent. In contrast, YOLOv8m demonstrated more conservative predictions and produced noticeably fewer RBC-to-WBC classification errors. Within the YOLO11 family, YOLO11m and YOLO11l generally produced reliable detections, while YOLO11x exhibited unstable behaviour and generated detections outside the microscope field of view, reducing its practical usefulness despite reasonable benchmark scores.
            
Models from the YOLO26 family demonstrated the highest level of consistency during qualitative testing. Both YOLO26x and YOLO26l produced stable white blood cell detections with comparatively few unexpected classifications. Although their benchmark scores were lower than several competing architectures, their prediction behaviour appeared more reliable during manual inspection of unseen microscope images. This observation highlights the importance of combining quantitative evaluation metrics with qualitative testing when assessing models for real-world medical imaging applications.
""")

st.space("small")

col1,col2,col3 = st.columns(3,vertical_alignment="center",gap="medium",border=True)

with col1:
    st.image("./images/16.png",caption="26x (Successful)")

with col2:
    st.image("./images/18.png",caption="8l")

with col3:
    st.image("./images/17.png",caption="11x (Complete Failure)")

st.space("small")

st.markdown("""
The benchmarking process also revealed that dataset quality and diversity had a greater impact on performance than further increases in model size or computational resources. As the dataset expanded from 52 images to 100 images and finally to 200 images, substantial improvements were observed across nearly all models. In contrast, experiments involving larger architectures, higher-VRAM hardware, and increased batch sizes produced comparatively smaller gains. These results suggest that future improvements to BioScan are more likely to come from expanding the dataset and increasing cellular diversity, particularly for white blood cells, rather than from further architecture exploration.
""")

st.space("small")

st.header("Development Journey")

st.subheader("Dataset Creation",divider="gray")

st.markdown("""
The project begins with the collection of real-time blood smear samples. Using a steady phone stand and my phone's camera, I collected images of blood samples showcasing RBCs, WBCs, and platelets at 40x zoom.
            
For annotations, I have used a Python library, 'AnyLabeling';  it provides a GUI (graphical user interface) to manually draw bounding boxes and label them accordingly. Since annotating hundreds of images is a tedious task to do completely manually, instead of pushing straight to a 200-image dataset, I first annotated only 2 images completely manually, which took 1 hr, and trained a very light and barely accurate YOLO model.

This allowed me to fasten up my process; instead of drawing boxes completely manually, the first prototypical model gave me a head start. I had to spend more time fixing the box dimensions and labels instead of drawing them. This is the procedure I have followed for the entire workflow. First reach a good number of annotations (2, 29, 52, 100, and 200); train some YOLO models; and select the best one to help with auto-labelling and continue increasing the dataset size. This substantially reduced time and manual effort. Moreover, by using some Python scripts, I was able to automate repetitive tasks of selecting mislabelled boxes and giving them their correct label.
            
However, this also gave room for some errors; in case there were human errors with the old dataset and they were not identified before the next batch of images, the error would be carried forward. A somewhat similar situation did occur in the case of the 100-image dataset, since the previous model trained on 52 images was having troubles with drawing boxes and incorrectly labelling clumps of RBCs into a single WBC. This error was carried forward to multiple images, as the colour given by the library for RBC and WBC wasn’t visually very different; the error was frequently missed until the first model was trained on 100 images. Upon analysing the model’s fatal error in misjudging clumps of RBCs into WBCs, I reanalysed the 100 images and fixed the labelling issue. After that, the model on the fixed set of 100 images performed drastically better than the previous 52 images.

During the building of this project, the question arose of whether better hardware or a larger dataset could potentially lead to better accuracy in a smaller amount of time. Upon testing many times on several cases, the final answer was mixed.
            
Improving GPU allowed me to train the same dataset on higher YOLO models and increase image resolutions. Improving image resolution contributed largely to improvement in platelet detection, due to their small size lower resolution barely captured any pixels of platelets. Either Google Colab’s T4 GPU (26 VRAM, 1280 image resolution) or RTX 4090D (48 VRAM, 2048 image resolution) was used. Increasing dataset size always resulted in an amazing improvement in accuracy, as the dataset rose, issues with RBC detection, RBC clumping into one WBC, RBC clumps as one RBC, WBC detection, and several edge cases of blood cells were resolved.
            
Continuing our work with a 200-image dataset and over 300,000 annotations to determine the most suitable architecture for BioScan, multiple models from the YOLOv8, YOLO11, and YOLO26 families were trained and evaluated on the final 200-image dataset. A total of nine major model configurations were benchmarked: YOLOv8m, YOLOv8l, YOLOv8x, YOLO11m, YOLO11l, YOLO11x, YOLO26m, YOLO26l, and YOLO26x.
""")

st.space("small")

model_comparison = pd.DataFrame({
    "Model": [
        "YOLOv8l",
        "YOLO11m",
        "YOLOv8m",
        "YOLO11x",
        "YOLOv8x",
        "YOLO11l",
        "YOLO26m",
        "YOLO26x -> In use Model",
        "YOLO26l"
    ],
    "Best mAP50": [
        0.447,
        0.413,
        0.387,
        0.381,
        0.375,
        0.371,
        0.323,
        0.313,
        0.291
    ],
    "Recall": [
        0.453,
        0.415,
        0.388,
        0.430,
        0.376,
        0.370,
        0.321,
        0.313,
        0.290
    ]
})

st.dataframe(model_comparison,hide_index=True)

st.space("small")

st.subheader("Notable Models",divider="gray")

st.markdown("""
Several architectures distinguished themselves during benchmarking for reasons beyond their raw performance metrics.
            
YOLOv8l achieved the highest mAP50 score among all tested models and became the strongest architecture according to standard object detection metrics. However, practical testing revealed occasional RBC-to-WBC misclassifications, particularly in regions containing dense clusters of red blood cells. 
""")

col1,col2 = st.columns(2,vertical_alignment="center",border=True,gap="medium")

with col1:
    st.badge("Highest Performing Model")
    st.image("./images/19.png")
with col2:
    st.image("./images/20.png")

st.space("medium")


st.markdown("""
YOLO11m demonstrated one of the best balances between detection accuracy and stability. While its benchmark score was slightly lower than YOLOv8l, it consistently produced reliable detections and fewer unexpected behaviours during manual inspection.
""")

col1,col2 = st.columns(2,vertical_alignment="center",border=True,gap="medium")

with col1:
    st.image("./images/21.png")
with col2:
    st.image("./images/22.png")

st.space("medium")


st.markdown("""
YOLO26x emerged as one of the most trusted models during practical evaluation. Although its benchmark metrics were lower than several competing architectures, it produced highly consistent white blood cell detections and comparatively fewer unusual classifications when evaluated on unseen microscope images.
""")


col1,col2 = st.columns(2,vertical_alignment="center",border=True,gap="medium")

with col1:
    st.badge("Selected Final Model",color="green")
    st.image("./images/23.png")
with col2:
    st.image("./images/24.png")

st.space("medium")


st.markdown("""
YOLO11x represented the most unexpected outcome of the benchmarking process. Despite achieving competitive quantitative metrics, the model frequently generated detections outside the microscope field of view, including image borders and non-cellular regions. This behaviour highlighted the importance of practical validation in addition to benchmark scores.
""")

col1,col2 = st.columns(2,vertical_alignment="center",border=True,gap="medium")

with col1:
    st.badge("Lowest Performing Model",color="red")
    st.image("./images/25.png")
with col2:
    st.image("./images/26.png")

st.space("medium")


st.warning("""
Interpretation of the confusion matrix should be performed with caution due to the highly imbalanced nature of the dataset and the extremely small size of platelet structures. Minor localization errors can disproportionately affect IoU-based evaluation metrics for platelets, while the overwhelming abundance of RBCs can influence overall class-level statistics. Consequently, quantitative metrics alone may not fully represent the practical usefulness of the model during real-world evaluation.
""")

st.space("small")

st.subheader("Model Size Comparison",divider="gray")

st.markdown("""
An interesting trend was observed across the YOLO model families: increasing model size did not consistently improve benchmark performance. Within the YOLO11 family, YOLO11m outperformed both YOLO11l and YOLO11x according to quantitative metrics. A similar pattern was observed in the YOLO26 family, where YOLO26m achieved stronger benchmark scores than YOLO26l and YOLO26x.
            
Although larger models possess greater representational capacity, their advantages were limited by the size and diversity of the available dataset. The results suggest that the training data was insufficient to fully exploit the additional complexity offered by larger architectures. Consequently, medium-sized models often achieved the most favourable balance between learning capacity and generalization performance when evaluated using standard metrics.
            
However, benchmark performance did not always align with practical performance. Despite achieving lower quantitative scores, YOLO26x consistently produced the most reliable and trustworthy detections during real-world testing. Its predictions were more stable, exhibited fewer unusual behaviours, and inspired greater confidence during manual inspection of microscope images. As a result, YOLO26x was ultimately selected as the best overall model for BioScan, demonstrating that practical usability can be more important than benchmark metrics alone.
""")

st.space("small")

st.subheader("Metric Performance vs Practical Performance",divider="gray")
st.markdown("""
One of the most important findings of the project was the discrepancy between benchmark metrics and real-world usability. Models that achieved the highest mAP50 scores were not always the models that inspired the greatest confidence during practical testing.
            
YOLOv8l achieved the highest benchmark score of all tested architectures and therefore became the statistical leader of the study. However, qualitative evaluation revealed occasional RBC-to-WBC classification errors that reduced confidence in its predictions. In contrast, models such as YOLO26l and YOLO26x achieved lower benchmark scores but demonstrated more consistent behaviour during manual inspection of microscope images.

This observation highlights an important limitation of relying exclusively on quantitative metrics. While benchmark scores remain essential for model comparison, practical deployment requires additional qualitative evaluation to identify unusual behaviours that may not be fully reflected by standard performance metrics. Consequently, model selection for BioScan considered both numerical evaluation and visual inspection of predictions.
""")

st.space("small")

st.subheader("Effect of Batch Size on Model Performance",divider="gray")
st.markdown("""
During experimentation, two training configurations of the YOLO26x model were evaluated. The first configuration utilized a 98 GB VRAM GPU and allowed a batch size of 2, while the second configuration utilized a 48 GB VRAM GPU with a batch size of 1. Conventional training practices often favor larger batch sizes due to improved gradient stability and hardware utilization. However, an unexpected observation was made during testing: the model trained with a batch size of 1 consistently demonstrated superior practical performance on unseen blood smear images despite utilizing less computational resources.
            
Although the exact cause requires further investigation, this result suggests that practical performance may not always correlate directly with increased hardware resources or larger batch sizes. The observation further reinforced the importance of empirical testing throughout the development process.
""")

st.space("small")

st.header("Limitations",divider="gray")
st.markdown("""
Although BioScan achieved promising results in blood cell detection, several limitations remain. The final dataset consisted of 200 microscope images, which, while substantially larger than the initial datasets used during development, remains relatively small compared to datasets used in large-scale medical imaging studies. In particular, white blood cells represented the smallest class within the dataset, limiting the diversity of cellular appearances available during training.
            
Platelet detection also remained challenging throughout the project. Due to their extremely small size within high-resolution microscope images, minor localization errors could significantly affect evaluation metrics. As a result, quantitative measurements may underestimate practical detection performance in some cases.
            
Another limitation is that the dataset was collected using a single microscope setup and imaging workflow. Variations in microscope hardware, staining techniques, image quality, and laboratory procedures may affect model performance when applied to data collected in different environments.
            
Finally, while BioScan demonstrated strong performance during experimental testing, the project was not designed or validated for clinical deployment. Additional testing, larger datasets, and professional medical validation would be required before the system could be considered for real-world diagnostic applications.
""")

st.space("small")

st.header("Future Work",divider="gray")
st.markdown("""
The results of this project suggest several directions for future development. The most significant improvement would likely come from expanding the dataset rather than increasing model complexity. Throughout experimentation, increases in dataset size consistently produced larger performance gains than increases in model size or computational resources. Future work should therefore focus on collecting additional blood smear images, particularly those containing a wider variety of white blood cell morphologies and challenging edge cases.
            
Further improvements could also be achieved through the collection of data from multiple microscopes and laboratory environments. This would increase dataset diversity and improve the model's ability to generalize to real-world conditions.

Beyond object detection, future versions of BioScan could estimate blood cell concentrations and ratios, allowing the system to provide more clinically useful information. Additional modules for disease-specific analysis, including malaria detection and other hematological abnormalities, could also be integrated into a unified platform.
            
Finally, while BioScan was primarily developed as a research and learning project, the system establishes a foundation for future clinical and educational applications. With larger datasets, continued validation, and collaboration with medical professionals, the project could be expanded into a more comprehensive tool for blood smear analysis.
""")

st.space("small")
st.header("Conclusion",divider="gray")

st.markdown("""
Throughout the development of BioScan, many of the project's most important lessons emerged from unexpected results. Assumptions that initially appeared obvious were repeatedly challenged by experimental evidence. Models with superior benchmark metrics did not always perform best in practice, and greater computational resources did not necessarily lead to improved outcomes. These experiences highlighted that research is not the process of confirming what is already believed, but rather the process of discovering what is true. In this sense, the challenges and contradictions encountered during development became some of the project's most valuable contributions.
""")

st.space("small")
st.header("Acknowledgements",divider="gray")
st.markdown("""
I would like to express my gratitude to the staff and medical professionals at Christian Medical College (CMC), Ludhiana, for providing guidance, laboratory access, and valuable feedback throughout this project. Their suggestions, particularly regarding the use of real-world blood smear samples, played a significant role in shaping the direction of this research.

I would also like to thank the laboratory specialists who introduced me to blood smear analysis, microscopy techniques, and the workflow of differential blood cell counting. Their willingness to share their knowledge greatly contributed to the successful completion of this project.
""")