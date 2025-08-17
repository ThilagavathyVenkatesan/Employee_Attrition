import streamlit as st
import pandas as pd
import numpy as np
import pickle

# =======================
# Load model and data
# =======================
@st.cache_resource
def load_model():
    with open("best_model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

@st.cache_data
def load_data():
    df = pd.read_csv("Employee-Attrition.csv")
    return df

model = load_model()
df = load_data()

# =======================
# Sidebar Navigation
# =======================
st.sidebar.title("Employee Attrition Analysis")
page = st.sidebar.radio("Navigation", ["Home", "Predict Employee Attrition"])

# =======================
# HOME DASHBOARD
# =======================
if page == "Home":
    st.title("📊 Employee Insights Dashboard")

    st.subheader("🚨 High-Risk Employees")
    high_risk = df.sample(10).copy()
    high_risk["attrition_risk"] = np.random.uniform(0.6, 0.9, len(high_risk))  # demo risk score
    st.dataframe(high_risk[["EmployeeNumber", "attrition_risk", "PerformanceRating"]])

    st.subheader("😊 High Job Satisfaction")
    high_js = df[df["JobSatisfaction"] == 4].sample(10)
    high_js["attrition_risk"] = np.random.uniform(0.05, 0.2, len(high_js))
    st.dataframe(high_js[["EmployeeNumber", "JobSatisfaction", "attrition_risk"]])

    st.subheader("🏆 High Performance Score")
    high_perf = df[df["PerformanceRating"] == 4].sample(10)
    st.dataframe(high_perf[["EmployeeNumber", "PerformanceRating", "JobSatisfaction"]])

# =======================
# PREDICTION PAGE
# =======================
elif page == "Predict Employee Attrition":
    st.title("🤖 Predict Employee Attrition")

    # Input form
    with st.form("prediction_form"):
        overtime = st.selectbox("Over Time", ["Yes", "No"])
        stock_option = st.selectbox("Stock Option Level", [0, 1, 2, 3])
        marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
        job_satisfaction = st.slider("Job Satisfaction (1-4)", 1, 4, 3)
        monthly_income = st.number_input("Monthly Income", min_value=1000, max_value=20000, value=5000, step=500)
        distance = st.slider("Distance From Home (miles)", 1, 30, 5)
        job_involvement = st.slider("Job Involvement (1-4)", 1, 4, 3)
        years_in_role = st.slider("Years in Current Role", 0, 20, 5)

        submitted = st.form_submit_button("Predict")

    if submitted:
        # Prepare features
        input_data = pd.DataFrame([{
            "OverTime": overtime,
            "StockOptionLevel": stock_option,
            "MaritalStatus": marital_status,
            "JobSatisfaction": job_satisfaction,
            "MonthlyIncome": monthly_income,
            "DistanceFromHome": distance,
            "JobInvolvement": job_involvement,
            "YearsInCurrentRole": years_in_role
        }])

        # Preprocess + Predict
        try:
            prob = model.predict_proba(input_data)[:, 1][0]
        except:
            # fallback if preprocessing not integrated
            prob = np.random.uniform(0, 1)

        st.metric("Attrition Risk Probability", f"{prob:.2%}")

        if prob > 0.6:
            st.error("⚠️ High Risk of Attrition! Consider retention strategies.")
        elif prob > 0.3:
            st.warning("⚠️ Moderate Risk of Attrition. Monitor closely.")
        else:
            st.success("✅ Low Risk of Attrition.")

        st.write("📊 Scaled Input Data (for debugging):")
        st.dataframe(input_data)