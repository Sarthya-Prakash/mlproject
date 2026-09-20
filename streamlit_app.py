import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Page configuration

st.set_page_config(
    page_title="Student Math Score Predictor",
    page_icon="🎓",
    layout="centered"
)

# Title

st.title("🎓 Student Exam Performance Indicator")
st.write("Predict a student's Mathematics score based on their academic information.")

st.divider()

# Input section

st.subheader("Enter Student Details")

gender = st.selectbox(
    "Gender",
    ["male", "female"]
)

race_ethnicity = st.selectbox(
    "Race or Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
    "associate's degree",
    "bachelor's degree",
    "high school",
    "master's degree",
    "some college",
    "some high school"
    ]
)

lunch = st.selectbox(
    "Lunch Type",
    ["free/reduced", "standard"]
)

test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

reading_score = st.number_input(
    "Reading Score (out of 100)",
    min_value=0,
    max_value=100,
    value=50
)

writing_score = st.number_input(
    "Writing Score (out of 100)",
    min_value=0,
    max_value=100,
    value=50
)

st.divider()

# Prediction

if st.button("Predict Math Score", type="primary"):
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )

        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        st.success("Prediction completed successfully!")
        st.metric(
            label="🎯 Predicted Mathematics Score",
            value=f"{results[0]:.2f}"
        )

    except Exception as e:
        st.error(f"Prediction failed: {e}")
