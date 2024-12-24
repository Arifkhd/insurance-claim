import streamlit as st
import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

model = joblib.load('Insurance.pkl')

st.title("Health Insurance Premium")

def predict(Age, Gender, Region, Marital_status, Dependants, BMI_Category, Smoking_Status, Employment_Status, Income_Lakhs, Medical_History, Insurance_Plan, Genetical_Risk):
    prediction = model.predict([[Age, Gender, Region, Marital_status, Dependants, BMI_Category, Smoking_Status, Employment_Status, Income_Lakhs, Medical_History, Insurance_Plan, Genetical_Risk]])
    return prediction[0]

def main():
    st.markdown('Prediction Application')
    
    # Age Validation
    Age = st.selectbox('Enter Age', list(range(18, 100)))
    if Age < 18 or Age > 100:
        st.warning("Please select an age between 18 and 100.")
    
    # Gender Validation
    Gender = st.selectbox('Enter Gender', ('None', 'Male', 'Female'))
    if Gender == 'None':
        st.warning("Please select a valid Gender.")
    else:
        st.success(f"You selected: {Gender}")
        
    # Region Validation
    Region = st.selectbox('Enter Region', ('None', 'Northeast', 'Northwest', 'Southeast', 'Southwest'))
    if Region == 'None':
        st.warning("Please select a valid Region.")
    else:
        st.success(f"You selected: {Region}")
        
    # Marital Status Validation
    Marital_status = st.selectbox('Enter marital status', ('None', 'Married', 'Unmarried'))
    if Marital_status == 'None':
        st.warning("Please select a valid Marital Status.")
    else:
        st.success(f"You selected: {Marital_status}")
        
    # Dependants Validation
    Dependants = st.selectbox('Enter Number of Dependants', list(range(0, 50)))
    
    # BMI Category Validation
    BMI_Category = st.selectbox('Enter BMI Category', ('None', 'Overweight', 'underweight', 'Normal', 'Obesity'))
    if BMI_Category == 'None':
        st.warning("Please select valid BMI Category")
    else:
        st.success(f"you have selected: {BMI_Category}")
    
    # Smoking Status Validation
    Smoking_Status = st.selectbox('Smoking Status', ('Regular', 'Occasional', 'No Smoking'))
    
    # Employment Status Validation
    Employment_Status = st.selectbox('Employment Status', ('Self-Employed', 'Freelancer', 'Salaried'))
    
    # Income Validation
    Income_Lakhs = st.selectbox('Income (in Lakhs)', list(range(1, 100)))
    if Income_Lakhs <= 0:
        st.warning("Income must be greater than 0.")
    
    # Medical History Validation
    Medical_History = st.selectbox('Medical History', ('None', 'No Disease', 'High blood pressure', 'Heart disease', 'Diabetes & Heart disease', 'Diabetes & Thyroid', 'Thyroid', 'Diabetes & High blood pressure'))
    if Medical_History == 'None':
        st.warning("Please select a valid Medical History.")
    else:
        st.success(f"You selected: {Medical_History}")

    # Genetical Risk Validation
    Genetical_Risk = st.selectbox('Genetical Risk', list(range(1, 5)))
    
    # Insurance Plan Validation
    Insurance_Plan = st.selectbox('Insurance Plan', ('Silver', 'Bronze', 'Gold'))
    
    if st.button('Predict'):
        # Check if all selections are valid before making the prediction
        if Gender != 'None' and Region != 'None' and Marital_status != 'None' and BMI_Category != 'None' and Medical_History != 'None' and Income_Lakhs > 0:
            # Call the predict function and display the result
            result = predict(Age, Gender, Region, Marital_status, Dependants, BMI_Category, Smoking_Status, Employment_Status, Income_Lakhs, Medical_History, Insurance_Plan, Genetical_Risk)
            st.success(f'Predicted Premium: ₹{result:,.0f}')  # Format for better readability
        else:
            st.error("Please fill in all fields.")
    
if __name__ == '__main__':
    main()
