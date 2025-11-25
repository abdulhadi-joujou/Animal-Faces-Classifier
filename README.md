# 🦁 Animal Faces Classification (Full-Stack AI App)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.10%2B-orange?style=for-the-badge&logo=tensorflow)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95%2B-green?style=for-the-badge&logo=fastapi)
![HTML5](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-yellow?style=for-the-badge&logo=html5)

A production-ready **AI Web Application** capable of classifying animal faces (**Cat**, **Dog**, **Wild Animal**) with **~99.6% accuracy**. 

This project demonstrates a complete Machine Learning pipeline: from training a **MobileNetV2** model using Transfer Learning, to deploying it via a **FastAPI** backend, and serving it through a modern, responsive **Frontend UI**.

---

## 🚀 Key Features

* **🧠 High Accuracy:** Achieved **99.67%** validation accuracy on the AFHQ dataset.
* **⚡ Optimized Inference:** Uses a manually reconstructed MobileNetV2 architecture for robust weight loading and fast CPU inference.
* **🎨 Interactive UI:** A clean, responsive web interface (HTML/CSS/JS) for easy image uploading and visualization.
* **🌐 REST API:** Fully documented API with Swagger UI support.
* **🛡️ Robust Engineering:** Implemented strict file validation, error handling, and modular code structure.

---

## 📂 Project Structure

```text
Animal-Faces-Classifier/
│
├── 📂 venv/                     # Virtual Environment (Local only).
├── 📂 dataset/                  # Training Dataset (Local only, ignored by Git).
│
├── 📓 model_training.ipynb      # Jupyter Notebook: Training pipeline & Visualization.
├── 📄 README.md                 # Project Documentation.
├── 📄 .gitignore                # Git ignore rules.
│
└── 📂 app/                      # Main Application Source Code
    ├── 📜 main.py               # FastAPI Server & Entry Point.
    ├── 📜 prediction_engine.py  # AI Logic (Model loading & Inference).
    ├── 📄 requirements.txt      # Python Dependencies.
    │
    ├── 📂 models/               # Model Artifacts
    │   ├── 📦 animal_faces_ultimate.keras
    │   └── 📄 class_names.txt
    │
    └── 📂 static/               # Frontend Assets (Web Interface)
        ├── 📄 index.html
        ├── 📄 style.css
        └── 📄 script.js
🛠️ Installation & Setup1. Clone the RepositoryBashgit clone [https://github.com/YourUsername/Animal-Faces-Classifier.git](https://github.com/YourUsername/Animal-Faces-Classifier.git)
cd Animal-Faces-Classifier
2. Set Up Virtual EnvironmentIt is highly recommended to use a virtual environment to manage dependencies.Windows:PowerShellpython -m venv venv
.\venv\Scripts\activate
Mac / Linux:Bashpython3 -m venv venv
source venv/bin/activate
3. Install DependenciesNavigate to the app directory and install the required packages:Bashcd app
pip install -r requirements.txt
🏃‍♂️ Running the AppStart the server using the Python command:Bashpython main.py
You should see a message indicating the server is running at http://0.0.0.0:8000🎮 How to UseOption 1: The Web Interface (User Friendly)Open your browser and go to: http://localhost:8000Click the upload area to select an image.Click "Analyze Image".The AI will display the prediction, confidence score, and probability breakdown.Option 2: API Documentation (For Developers)Go to: http://localhost:8000/docsUse the interactive Swagger UI to test the /predict endpoint directly.🧠 Model DetailsThe model was trained using Transfer Learning on the MobileNetV2 architecture.ParameterValueBase ModelMobileNetV2 (ImageNet Weights)Input Shape(224, 224, 3)Training StrategyFrozen Base (Feature Extraction)Epochs12Batch Size32Final Val Accuracy99.67%Training Graphs:(See model_training.ipynb for detailed Loss/Accuracy curves and Confusion Matrix)🤝 ContributingContributions, issues, and feature requests are welcome!Feel free to check the issues page.

Author: Abdulhadi Joujou