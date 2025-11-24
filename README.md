# 🦁 Animal Faces Classification API

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10%2B-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A high-performance Deep Learning project designed to classify animal faces into three categories: **Cat**, **Dog**, and **Wild Animal**. The model achieves an impressive accuracy of **~99.67%** using Transfer Learning with **MobileNetV2** and is deployed via a fast, asynchronous REST API using **FastAPI**.

---

## 🚀 Key Features

* **State-of-the-Art Accuracy:** Achieved **99.67%** validation accuracy on the AFHQ dataset.
* **Robust Model:** Trained using **Label Smoothing**, **L2 Regularization**, and extensive **Data Augmentation** to prevent overfitting.
* **Fast Inference:** Powered by **MobileNetV2** (lightweight architecture) suitable for real-time applications.
* **Modern API:** Built with **FastAPI** for high performance and automatic interactive documentation (Swagger UI).
* **Clean Architecture:** Modular code structure separating the prediction engine from the API logic.

---

## 📂 Project Structure

```text
Animal-Faces-Classifier/
│
├── 📂 venv/                     # Virtual Environment (Contains libraries, scripts, etc.)
├── 📂 dataset/                  # Data Directory (Not uploaded to Git)
│   ├── train/                   # Training images
│   └── val/                     # Validation images
│
├── 📓 model_training.ipynb      # Jupyter Notebook for training & visualization.
├── 📄 README.md                 # Project documentation.
├── 📄 .gitignore                # Git ignore rules.
│
└── 📂 app/                      # Main Application Directory
    ├── 📜 main.py               # FastAPI entry point.
    ├── 📜 prediction_engine.py  # Model loading and inference logic.
    ├── 📄 requirements.txt      # Python dependencies.
    │
    └── 📂 models/               # Model artifacts
        ├── 📦 animal_faces_ultimate.keras    # The trained model file.
        └── 📄 class_names.txt           # List of class labels.
🛠️ Installation & Setup
Follow these steps to run the project locally:

1. Clone the Repository
Bash

git clone https://github.com/abdulhadi-joujou/Animal-Faces-Classifier.git
cd Animal-Faces-Classifier
2. Set Up Virtual Environment (Recommended)
Bash

# Create virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate
3. Install Dependencies
Navigate to the app directory and install the required packages:

Bash

cd app
pip install -r requirements.txt
🏃‍♂️ Running the Server
Start the API server using Uvicorn:

Bash

python main.py
Alternatively, you can run: uvicorn main:app --reload

The server will start at: http://localhost:8000

📖 API Usage
Once the server is running, you can test the API using the built-in Swagger UI:

Open your browser and go to: http://localhost:8000/docs

Click on the POST /predict endpoint.

Click "Try it out".

Upload an image (JPG/PNG).

Click "Execute".

Sample JSON Response:
JSON

{
  "prediction": "Dog",
  "confidence": 99.85,
  "details": {
    "Cat": 0.05,
    "Dog": 99.85,
    "Wild": 0.10
  },
  "filename": "my_puppy.jpg"
}
🧠 Model Training Details
The model was trained using the AFHQ (Animal Faces HQ) dataset.

Base Model: MobileNetV2 (Pre-trained on ImageNet).

Input Size: 224x224 pixels.

Optimizer: Adam.

Loss Function: Categorical Crossentropy (with Label Smoothing=0.1).

Techniques Used:

Frozen Base Training (Phase 1).

Global Average Pooling.

Dropout (0.3) for regularization.

Performance Metrics: | Metric | Score | | :--- | :--- | | Validation Accuracy | 99.67% | | Validation Loss | 0.3100 |

💻 Technologies Used
Deep Learning: TensorFlow, Keras.

Backend Framework: FastAPI, Uvicorn.

Image Processing: Pillow (PIL), NumPy.

Environment: Python 3.x.

🤝 Contributing 
Contributions are welcome! Please feel free to submit a Pull Request.

Author: Abdulhadi Joujou