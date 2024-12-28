# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 15:49:46 2024

@author: Dell
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import GradientBoostingRegressor

# Load the pre-trained model
model = joblib.load('zor.pkl')

# Title of the application
st.title("Health Insurance Premium Prediction")

# Define the prediction function
def predict(age, gender, region, marital_status, bmi_category, smoking_status, 
            employment_status, income_lakhs, medical_history, insurance_plan, genetical_risk):
    # Encoding categorical variables to numeric values
    gender = 1 if gender == 'Male' else 0
    region_map = {'Northwest': 0, 'Southeast': 1, 'Northeast': 2, 'Southwest': 3}
    marital_status_map = {'Unmarried': 0, 'Married': 1}
    bmi_category_map = {'Normal': 0, 'Obesity': 1, 'Overweight': 2, 'Underweight': -1}
    smoking_status_map = {'No Smoking': 0, 'Regular': 1, 'Occasional': 2}
    employment_status_map = {'Salaried': 0, 'Self-Employed': 1, 'Freelancer': 2}
    medical_history_map = {
        'No Disease': 0, 
        'Diabetes': 1, 
        'High blood pressure': 2, 
        'Heart disease': 3, 
        'Thyroid': 4,
        'Diabetes & High blood pressure': 5, 
        'Diabetes & Thyroid': 6, 
        'Diabetes & Heart disease': 7, 
        'High blood pressure & Heart disease': 8
    }
    insurance_plan_map = {'Bronze': 0, 'Silver': 1, 'Gold': 2}

    # Map inputs
    region = region_map[region]
    marital_status = marital_status_map[marital_status]
    bmi_category = bmi_category_map[bmi_category]
    smoking_status = smoking_status_map[smoking_status]
    employment_status = employment_status_map[employment_status]
    medical_history = medical_history_map[medical_history]
    insurance_plan = insurance_plan_map[insurance_plan]

    # Make the prediction
    prediction = model.predict([[age, gender, region, marital_status, bmi_category, smoking_status, 
                                 employment_status, income_lakhs, medical_history, insurance_plan, genetical_risk]])
    return prediction[0]

# Main function to run the Streamlit app
def main():
    st.markdown('### Prediction Application')

    # Input fields
    age = st.selectbox('Enter Age', list(range(18, 101)))
    gender = st.selectbox('Enter Gender', ('Male', 'Female'))
    region = st.selectbox('Enter Your Region', ('Northwest', 'Southeast', 'Northeast', 'Southwest'))
    marital_status = st.selectbox('Enter Marital Status', ('Unmarried', 'Married'))
    bmi_category = st.selectbox('Enter BMI Category', ('Normal', 'Obesity', 'Overweight', 'Underweight'))
    smoking_status = st.selectbox("Enter Smoking Status", ('No Smoking', 'Regular', 'Occasional'))
    employment_status = st.selectbox("Enter Employment Status", ('Salaried', 'Self-Employed', 'Freelancer'))
    income_lakhs = st.slider("Enter Your Income in Lakhs", min_value=1, max_value=100, step=1)
    medical_history = st.selectbox(
        "Enter Medical History", 
        ('No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure', 
         'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 
         'Diabetes & Thyroid', 'Diabetes & Heart disease')
    )
    insurance_plan = st.selectbox("Choose Your Insurance Plan", ('Bronze', 'Silver', 'Gold'))
    genetical_risk = st.slider('Enter Genetical Risk Level (1 to 5)', min_value=1, max_value=5, step=1)

    # Button to trigger prediction
    if st.button('Predict Premium'):
        try:
            # Call the predict function
            prediction = predict(age, gender, region, marital_status, bmi_category, smoking_status, 
                                 employment_status, income_lakhs, medical_history, insurance_plan, genetical_risk)
            st.success(f"Estimated Health Insurance Premium: ₹{prediction:,.0f}")
        except Exception as e:
            st.error(f"Error in prediction: {e}")

# Run the application
if __name__ == '__main__':
    main()
