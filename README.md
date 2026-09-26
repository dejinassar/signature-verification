# CNN-Based Handwritten Signature Verification System for Forgery Detection

## Overview

This project implements an offline handwritten signature verification system using a standard Convolutional Neural Network (CNN). The system is designed to classify signature images as either **genuine** or **forged**, and includes a complete pipeline from data preprocessing and model training to a deployable Streamlit application for real-time inference.

The work is based on academic research into offline signature verification and demonstrates the application of deep learning to biometric forgery detection.

## Research Title

**"A Convolutional Neural Network Approach to Offline Handwritten Signature Verification and Forgery Detection"**
## Live Demo

 **Try the application:** https://signature-verification-cnn.streamlit.app/
## Features

- End-to-end offline signature verification pipeline (preprocessing → training → inference)
- Standard CNN architecture trained for binary classification (genuine vs. forged)
- Interactive Streamlit web application for uploading and verifying signature images
- Support for batch verification via multiple image uploads
- Visualized prediction outputs with associated confidence scores
- Downloadable CSV export of prediction results
- Clean, reproducible project structure

## Dataset

The model was trained and evaluated on the **CEDAR handwritten signature dataset**, a widely used benchmark dataset for offline signature verification research.

| Category | Count |
|---|---|
| Genuine signatures | 1,320 |
| Forged signatures | 1,320 |
| **Total images** | **2,640** |

> **Note:** The raw dataset is **not included** in this repository due to file size, privacy considerations, and general repository management best practices. Users wishing to reproduce training must obtain the CEDAR dataset independently and structure it according to `split_cedar_dataset.py`.

## Preprocessing

All images used in training and inference undergo the following preprocessing steps:

1. Conversion to grayscale
2. Resizing to **128 × 128** pixels
3. Pixel value normalization to the range **0–1**

During the original training process, the following data augmentation techniques were additionally applied to improve generalization:

- Rotation
- Width shift
- Height shift
- Zoom

## CNN Architecture

The model is a standard Convolutional Neural Network (not a Siamese network) built for binary image classification, structured as follows:

| Layer | Configuration |
|---|---|
| Conv2D | 32 filters, ReLU activation |
| MaxPooling2D | — |
| Conv2D | 64 filters, ReLU activation |
| MaxPooling2D | — |
| Conv2D | 128 filters, ReLU activation |
| MaxPooling2D | — |
| Flatten | — |
| Dense | 128 units, ReLU activation |
| Dropout | Rate = 0.5 |
| Dense | 1 unit, Sigmoid activation (output) |

## Training Configuration

| Parameter | Value |
|---|---|
| Optimizer | Adam |
| Loss Function | Binary Crossentropy |
| Epochs | 10 |
| Batch Size | 16 |
| Input Shape | 128 × 128 × 1 |

## Results

The following results are **reported from the original academic experiment** conducted during model development and evaluation. They are presented here for reference and are **not** results independently reproduced within this repository.

| Metric | Value |
|---|---|
| Training Accuracy | 91.98% |
| Validation Accuracy | 83.59% |
| Test Accuracy | 98.99% |
| Precision | 0.99 |
| Recall | 0.99 |
| F1-Score | 0.99 |
| False Acceptance Rate (FAR) | 0.00 |
| False Rejection Rate (FRR) | 0.0201 |
| AUC | 1.00 |

## Streamlit Application

An interactive Streamlit application (`app.py`) is provided to demonstrate the trained model's inference capabilities. The application allows users to:

- Upload signature images in **PNG, JPG, or JPEG** format
- Upload and process **multiple images** at once
- Automatically convert uploaded images to grayscale
- Automatically resize images to **128 × 128** pixels
- Automatically normalize pixel values before inference
- Run predictions using the trained CNN model (`cnn_model.keras`)
- View **Genuine** or **Forgery** classification results
- View associated **prediction probabilities**
- View **visualizations** of prediction outputs
- **Download** prediction results as a CSV file

## Project Structure

```text
signature-verification/
├── app.py                     # Streamlit application for signature verification
├── cnn_model.keras            # Trained CNN model
├── split_cedar_dataset.py     # Script for preparing/splitting the CEDAR dataset
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
├── .gitignore                 # Files/folders excluded from version control
└── Results/                   # Training results, plots, and evaluation outputs
```

> **Note:** Raw datasets and temporary archives (e.g., downloaded CEDAR dataset files, `.zip`/`.rar` archives, extracted image folders) are intentionally excluded from this repository via `.gitignore`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/signature-verification.git
   cd signature-verification
   ```

2. (Optional but recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Once dependencies are installed and the trained model (`cnn_model.keras`) is present in the project directory, launch the Streamlit application:

```bash
streamlit run app.py
```

This will start a local web server and open the application in your default browser, where you can upload signature images for verification.

## Technologies Used

- **Python**
- **TensorFlow / Keras**
- **Streamlit**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Plotly**
- **Pillow**
- **OpenCV**

## Important Note

This project is an academic and research-oriented implementation intended to demonstrate the application of CNNs to offline signature verification. The reported results reflect performance on the CEDAR dataset under the specific experimental conditions of the original study and should not be interpreted as guaranteed performance on other datasets, real-world signature samples, or production deployment scenarios. This system is **not** intended for use as a production-grade or legally binding forgery detection tool without further validation, testing, and domain-specific adaptation.
