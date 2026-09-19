# 📊 Student Math Score Prediction

An **End-to-End Machine Learning project** that predicts a student's **Math Score** based on demographic, academic, and test-related information.

The project demonstrates a complete ML workflow — from **data ingestion and preprocessing to model training, prediction, and deployment using Flask**.

---

## 🚀 Live Demo

🌐 **Application:**
https://students-maths-score-prediction.onrender.com

> The application is deployed using Render.

---

## 🎯 Project Overview

The goal of this project is to predict a student's mathematics score using features such as:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

The project follows an **end-to-end machine learning pipeline** rather than training a model only inside a notebook.

---

## 🧠 Machine Learning Workflow

```text
Dataset
   ↓
Data Ingestion
   ↓
Data Transformation
   ↓
Feature Engineering
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model & Preprocessor Saved
   ↓
Flask Web Application
   ↓
Prediction
```

---

## 🛠️ Tech Stack

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming Language |
| Pandas       | Data Processing      |
| NumPy        | Numerical Computing  |
| Scikit-learn | Machine Learning     |
| Matplotlib   | Data Visualization   |
| Seaborn      | Data Visualization   |
| CatBoost     | ML Model             |
| XGBoost      | ML Model             |
| Flask        | Web Application      |
| Gunicorn     | Production Server    |
| Render       | Deployment           |

---

## 📁 Project Structure

```text
mlproject/
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── data/
│   └── raw.csv
│
├── notebook/
│   └── experimentation notebooks
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   └── predict_pipeline.py
│   │
│   └── exception.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── app.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sarthya-Prakash/mlproject.git
```

### 2. Navigate to the project

```bash
cd mlproject
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

For prediction:

```text
http://127.0.0.1:5000/predictdata
```

---

## 🔮 How Prediction Works

The user enters the required student information through the web interface.

The application then:

1. Collects the input data.
2. Converts it into a Pandas DataFrame.
3. Applies the saved preprocessing pipeline.
4. Loads the trained ML model.
5. Generates the predicted mathematics score.
6. Displays the prediction on the web page.

---

## 📦 Model Artifacts

The trained model and preprocessing object are stored in the `artifacts/` directory:

```text
artifacts/
├── model.pkl
└── preprocessor.pkl
```

These files allow the Flask application to make predictions without retraining the model every time.

---

## 🌐 Deployment

The application is deployed on **Render** using Gunicorn.

### Start Command

```bash
gunicorn app:app
```

The project uses a pinned Python/scikit-learn environment to maintain compatibility with the saved ML model.

---

## 📚 Dataset

The project uses a student performance dataset containing demographic information and academic scores.

The target variable is:

```text
math score
```

---

## 💡 Key Concepts Demonstrated

* End-to-End Machine Learning
* Data Ingestion
* Data Cleaning
* Data Transformation
* Feature Engineering
* Model Training
* Model Evaluation
* Pickle Model Serialization
* ML Prediction Pipeline
* Flask Web Development
* Production Deployment
* Git & GitHub

---

## 👨‍💻 Author

**Sarthya Prakash**

GitHub:
https://github.com/Sarthya-Prakash

---

## ⭐ If you found this project useful

Consider giving the repository a ⭐ on GitHub!
