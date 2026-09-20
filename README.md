# 📊 Student Math Score Prediction

An **End-to-End Machine Learning project** that predicts a student's **Mathematics Score** based on demographic, academic, and test-related information.

The project demonstrates a complete machine learning workflow — from **data ingestion and preprocessing to model training, evaluation, prediction, and deployment using Streamlit**.

---

## 🚀 Live Demo

🌐 **Streamlit Application:**

https://mlproject-wzazra5ptovxzarqeymf79.streamlit.app/

The application is deployed using **Streamlit Community Cloud**.

---

## 🎯 Project Overview

The goal of this project is to predict a student's mathematics score using the following features:

* Gender
* Race/Ethnicity
* Parental Level of Education
* Lunch Type
* Test Preparation Course
* Reading Score
* Writing Score

Instead of training a model only inside a notebook, this project implements a complete **end-to-end machine learning pipeline**.

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
Prediction Pipeline
   ↓
Streamlit Web Application
   ↓
Predicted Math Score
```

---

## 🛠️ Tech Stack

| Technology                | Purpose                |
| ------------------------- | ---------------------- |
| Python                    | Programming Language   |
| Pandas                    | Data Processing        |
| NumPy                     | Numerical Computing    |
| Scikit-learn              | Machine Learning       |
| Matplotlib                | Data Visualization     |
| Seaborn                   | Data Visualization     |
| CatBoost                  | Machine Learning Model |
| XGBoost                   | Machine Learning Model |
| Streamlit                 | Web Application & UI   |
| Git & GitHub              | Version Control        |
| Streamlit Community Cloud | Deployment             |

---

## 📁 Project Structure

```text
mlproject/
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── train.csv
│   └── test.csv
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
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── streamlit_app.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sarthya-Prakash/mlproject.git
```

### 2. Navigate to the Project Directory

```bash
cd mlproject
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application Locally

Start the Streamlit application:

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

Usually, the local application will be available at:

```text
http://localhost:8501
```

---

## 🔮 How Prediction Works

The user enters the required student information through the Streamlit interface.

The application then:

1. Collects the student's input.
2. Converts the input into a Pandas DataFrame.
3. Loads the saved preprocessing pipeline.
4. Transforms the input features.
5. Loads the trained machine learning model.
6. Generates the predicted mathematics score.
7. Displays the prediction in the Streamlit interface.

---

## 📦 Model Artifacts

The trained model and preprocessing pipeline are stored in the `artifacts/` directory:

```text
artifacts/
├── model.pkl
└── preprocessor.pkl
```

These serialized files allow the application to make predictions without retraining the model every time.

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

### Deployment Configuration

```text
Repository: Sarthya-Prakash/mlproject
Branch: main
Main File: streamlit_app.py
```

### Live Application

https://mlproject-wzazra5ptovxzarqeymf79.streamlit.app/

---

## 📚 Dataset

The project uses a student performance dataset containing demographic information and academic scores.

The target variable is:

```text
math score
```

The model uses the student's **reading score** and **writing score**, along with demographic and test-preparation information, to predict the mathematics score.

---

## 💡 Key Concepts Demonstrated

* End-to-End Machine Learning
* Data Ingestion
* Data Cleaning
* Data Transformation
* Feature Engineering
* Model Training
* Model Evaluation
* Hyperparameter Tuning
* Model Serialization
* ML Prediction Pipeline
* Streamlit Application Development
* Cloud Deployment
* Git & GitHub

---

## 🎓 Project Highlights

* Built a complete **end-to-end ML pipeline**.
* Implemented separate components for **data ingestion, transformation, and model training**.
* Compared multiple machine learning algorithms.
* Used preprocessing pipelines for handling numerical and categorical features.
* Serialized the trained model and preprocessing object using Pickle.
* Created an interactive prediction interface using **Streamlit**.
* Deployed the application on **Streamlit Community Cloud**.

---

## 👨‍💻 Author

**Sarthya Prakash**

GitHub:

https://github.com/Sarthya-Prakash

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!
