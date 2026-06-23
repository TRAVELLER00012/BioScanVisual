# BioScan Website

BioScan is an AI-powered blood smear analysis platform capable of detecting and classifying Red Blood Cells (RBCs), White Blood Cells (WBCs), and Platelets from microscope images using computer vision.

This repository contains the BioScan website and inference application used to showcase the final trained models and research outcomes. The research paper, dataset creation process, model benchmarking, and training experiments were conducted separately and are not fully contained within this repository.

---

## Features

* Blood smear image upload
* Automatic detection of RBCs, WBCs, and Platelets
* Annotated prediction visualization
* Detection statistics and cell counts
* Comparison between multiple YOLO architectures
* Research paper viewer and download support
* Interactive model benchmarking showcase

---

## Project Background

BioScan was developed as an independent research project focused on automated blood smear analysis through computer vision.

The project involved:

* Collection of real-world blood smear samples
* Manual annotation of over 350,000 blood cells
* Progressive dataset expansion from 2 images to 200 images
* Benchmarking of multiple YOLOv8, YOLO11, and YOLO26 architectures
* Cloud GPU experimentation using Google Colab and Vast AI
* Development of custom annotation automation tools

The final system was evaluated on a dataset containing approximately:

* 259,000+ RBC annotations
* 2,000+ WBC annotations
* 12,000+ Platelet annotations

---

## Repository Scope

This repository focuses on:

* User interface
* Model inference
* Visualization of predictions
* Research presentation

The original training environment, cloud configurations, dataset generation workflow, and large model checkpoints are maintained separately from this repository.

---

## Models Included

The website supports multiple architectures trained during the BioScan research project:

* YOLOv8m
* YOLOv8l
* YOLOv8x
* YOLO11m
* YOLO11l
* YOLO11x
* YOLO26m
* YOLO26l
* YOLO26x
* YOLO26x (2048 Resolution)

Among these, YOLO26x was selected as the final BioScan model due to its strong practical performance and consistency during real-world testing.

---

## Technology Stack

### Frontend

* Streamlit

### Machine Learning

* Ultralytics YOLO
* PyTorch
* OpenCV
* Pillow

### Data Processing

* NumPy
* Pandas

---

## Research Paper

The complete BioScan research paper is included within the website and can also be downloaded directly through the application interface.

The paper covers:

* Dataset creation
* Annotation workflow
* Model benchmarking
* Experimental findings
* Limitations
* Future work
* Development journey

---

## Disclaimer

BioScan is a research and educational project.

The platform is not intended for clinical diagnosis, medical decision-making, or healthcare deployment. Results should be interpreted only as outputs from an experimental computer vision system.

---

## Author

Daksh Kumar

Independent Student Researcher

BioScan was developed to explore the intersection of artificial intelligence, computer vision, and biomedical imaging while investigating how modern object detection models can assist blood smear analysis.
