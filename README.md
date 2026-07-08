# 🌱 OptiCrop: Smart Agricultural Production Optimization Engine

OptiCrop is a Machine Learning-based web application that recommends the most suitable crop based on soil nutrients and environmental conditions. The application analyzes Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall to predict the best crop using a trained Machine Learning model.

The project aims to assist farmers in selecting suitable crops, improving agricultural productivity, reducing crop failure, and promoting sustainable farming practices.

---

# 📖 Table of Contents

- Project Overview
- Business Problem
- Objectives
- Business Requirements
- Dataset Information
- Exploratory Data Analysis
- Data Preprocessing
- Machine Learning Models
- Model Performance
- Features
- Technologies Used
- Project Structure
- Installation
- Running the Application
- Application Screenshots
- Future Enhancements
- Team Members
- Acknowledgements
- License

---

# 📌 Project Overview

Agriculture plays an essential role in food production. However, selecting the right crop according to soil nutrients and climatic conditions is often challenging.

OptiCrop uses Machine Learning to recommend the most suitable crop by analyzing:

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

The application provides crop recommendations through a simple and user-friendly Flask web interface.

---

# 🎯 Business Problem

Farmers often face difficulties in choosing the appropriate crop due to changing environmental conditions and varying soil nutrient levels.

Incorrect crop selection can lead to:

- Reduced agricultural productivity
- Crop failure
- Financial loss
- Inefficient resource utilization

OptiCrop addresses these challenges by providing intelligent crop recommendations using Machine Learning.

---

# 🎯 Objectives

- Recommend suitable crops using Machine Learning.
- Improve agricultural productivity.
- Support sustainable farming practices.
- Provide an easy-to-use web application.
- Reduce crop selection errors.

---

# 📋 Business Requirements

The application should:

- Predict the most suitable crop accurately.
- Accept soil and environmental parameters from users.
- Display crop information and recommendations.
- Provide a responsive and user-friendly interface.
- Deploy the trained Machine Learning model using Flask.

---

# 📊 Dataset Information

**Dataset:** Crop Recommendation Dataset

### Input Features

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

### Target

- Crop Label

---

# 📈 Exploratory Data Analysis (EDA)

The following analyses were performed:

### ✔ Univariate Analysis

- Distribution of Soil Nutrients
- Temperature Distribution
- Humidity Distribution
- Rainfall Distribution

### ✔ Bivariate Analysis

- Relationship between crop labels and environmental features.

### ✔ Correlation Analysis

- Heatmap to understand feature relationships.

---

# ⚙ Data Preprocessing

The following preprocessing steps were performed:

- Dataset Loading
- Data Inspection
- Missing Value Check
- Exploratory Data Analysis
- Feature Selection
- Train-Test Split
- Model Training

---

# 🤖 Machine Learning Models

The following Machine Learning models were used during project development:

| Model | Purpose | Status |
|--------|---------|--------|
| Logistic Regression | Crop Classification | ✅ Implemented |
| K-Means Clustering | Crop Pattern Analysis | ✅ Implemented |
| Random Forest Classifier | Final Prediction Model | ⭐ Best Model |

Random Forest was selected as the deployment model because it achieved the best performance.

---

# 📊 Model Performance

| Model | Status |
|--------|--------|
| Logistic Regression | Implemented |
| K-Means Clustering | Implemented |
| Random Forest Classifier | ⭐ Selected Best Model |

**Final Model Accuracy:** **99.32%**

---

# 🚀 Features

- Crop Recommendation using Machine Learning
- Soil Nutrient Analysis
- Environmental Condition Analysis
- Prediction Confidence Score
- Crop Information and Growing Tips
- Responsive Flask Web Application
- User-Friendly Interface
- Random Sample Data Generator

---

# 🛠 Technologies Used

### Programming Languages

- Python
- HTML5
- CSS3
- JavaScript

### Framework

- Flask

### Machine Learning

- Scikit-Learn
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Pickle

### Development Tools

- Visual Studio Code
- Jupyter Notebook
- Git
- GitHub

---

# 📂 Project Structure

```text
OptiCrop
│
├── 1. Brainstorming & Ideation
├── 2. Requirement Analysis
├── 3. Project Design Phase
├── 4. Project Planning Phase
├── 5. Project Development Phase
│   ├── dataset
│   ├── model
│   ├── notebooks
│   ├── screenshots
│   ├── static
│   │   ├── css
│   │   ├── images
│   │   └── js
│   ├── templates
│   ├── app.py
│   ├── crop_data.py
│   ├── requirements.txt
│   └── .gitignore
│
├── 6. Project Testing
├── 7. Project Documentation
├── 8. Project Demonstration
│
└── README.md
```

---

# ▶ Installation

Clone the repository

```bash
git clone https://github.com/Mohammed-Sadia-Rahmatunnisa/OptiCrop.git
```

Move into the project directory

```bash
cd "5. Project Development Phase"
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Running the Application

Run the Flask application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

# 🔗 Repository

GitHub Repository:

https://github.com/Mohammed-Sadia-Rahmatunnisa/OptiCrop

---
# 🌐 Live Demo

Live Application:

https://opticrop-1-sh40.onrender.com

---

# 📷 Application Screenshots

## 🏠 Home Page

### Top Section

![Home Top](5.%20Project%20Development%20Phase/screenshots/home_top.png)

### Bottom Section

![Home Bottom](5.%20Project%20Development%20Phase/screenshots/home_bottom.png)

---

## ℹ️ About Page

![About Page](5.%20Project%20Development%20Phase/screenshots/about.png)

---

## 🌾 Prediction Page

![Prediction Page](5.%20Project%20Development%20Phase/screenshots/predict.png)

---

## 🌾 Prediction Result

![Prediction Result](5.%20Project%20Development%20Phase/screenshots/rice_prediction.png)

---

# 🚀 Future Enhancements

- Weather API Integration
- Fertilizer Recommendation System
- Disease Detection
- Mobile Application
- Multi-language Support
- GPS-Based Crop Recommendation

---

# 👥 Team Members

- **Mohammed Sadia Rahmatunnisa** – Team Lead
- **Akhil Varma**
- **Done Divya**
- **Ullingala Swathi**
- **Yamini Karumuri**

---

# 🙏 Acknowledgements

- SmartBridge
- AICTE
- IBM SkillsBuild
- Open Source Community
- Flask
- Scikit-Learn

---

# 📄 License

This project was developed for academic and educational purposes as part of the SmartBridge AI & Machine Learning Internship.

---

# 🌱 OptiCrop

**Smart Agricultural Production Optimization Engine**

Empowering farmers through Machine Learning-based crop recommendation for smarter and sustainable agriculture.
