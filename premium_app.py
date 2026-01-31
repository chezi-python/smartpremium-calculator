import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Page config
# --------------------------------------------------
st.set_page_config(
    page_title="Insurance Premium Prediction",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Insurance Premium Prediction App")

# --------------------------------------------------
# Load trained model (Pipeline)
# --------------------------------------------------
@st.cache_resource
def load_model():
    return joblib.load("best_insurance_model.pkl")

model = load_model()
st.success("✅ Model loaded successfully")

# --------------------------------------------------
# User Inputs
# --------------------------------------------------
st.header("Enter Customer Details")

age = st.number_input("Age", min_value=18, max_value=100, value=30)

annual_income = st.number_input(
    "Annual Income", min_value=0, value=500000, step=10000
)

marital_status = st.selectbox(
    "Marital Status", ["Single", "Married", "Divorced"]
)

num_dependents = st.number_input(
    "Number of Dependents", min_value=0, max_value=10, value=0
)

education_level = st.selectbox(
    "Education Level", ["High School", "Bachelor", "Master", "PhD"]
)

occupation = st.text_input("Occupation", "Private Employee")

health_score = st.number_input(
    "Health Score", min_value=0, max_value=100, value=70
)

location = st.selectbox(
    "Location", ["Urban", "Semi-Urban", "Rural"]
)

policy_type = st.selectbox(
    "Policy Type", ["Basic", "Standard", "Premium"]
)

previous_claims = st.number_input(
    "Previous Claims", min_value=0, max_value=20, value=0
)

vehicle_age = st.number_input(
    "Vehicle Age (years)", min_value=0, max_value=50, value=5
)

credit_score = st.number_input(
    "Credit Score", min_value=300, max_value=900, value=700
)

insurance_duration = st.number_input(
    "Insurance Duration (years)", min_value=1, max_value=50, value=5
)

smoking_status = st.selectbox(
    "Smoking Status", ["Yes", "No"]
)

exercise_frequency = st.selectbox(
    "Exercise Frequency", ["None", "Low", "Medium", "High"]
)

property_type = st.selectbox(
    "Property Type", ["Owned", "Rented"]
)

# --------------------------------------------------
# IMPORTANT: Create FULL input schema
# --------------------------------------------------
input_data = pd.DataFrame([{
    # ----- REQUIRED BUT NOT USER INPUT -----
    "id": 0,                                # dummy id
    "Gender": "Male",                       # default gender
    "Policy Start Date": "2023-01-01",      # dummy date

    # ----- USER INPUT FEATURES -----
    "Age": age,
    "Annual Income": annual_income,
    "Marital Status": marital_status,
    "Number of Dependents": num_dependents,
    "Education Level": education_level,
    "Occupation": occupation,
    "Health Score": health_score,
    "Location": location,
    "Policy Type": policy_type,
    "Previous Claims": previous_claims,
    "Vehicle Age": vehicle_age,
    "Credit Score": credit_score,
    "Insurance Duration": insurance_duration,
    "Smoking Status": smoking_status,
    "Exercise Frequency": exercise_frequency,
    "Property Type": property_type
}])

# --------------------------------------------------
# Prediction
# --------------------------------------------------
if st.button("🔮 Predict Insurance Premium"):
    try:
        prediction = model.predict(input_data)[0]

        st.subheader("📊 Prediction Result")
        st.success(f"Estimated Insurance Premium: ₹ {prediction:,.2f}")

    except Exception as e:
        st.error("❌ Prediction failed")
        st.write(e)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.caption("Insurance Premium Prediction | Streamlit Deployment")
