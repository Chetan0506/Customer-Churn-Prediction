import numpy as np
import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Loading the model
model = pickle.load(open('churn.pkl', 'rb'))
# Assuming you also have a dataframe saved as pickle, uncomment the next line and replace with your actual data
# df = pickle.load(open('your_dataframe.pkl', 'rb'))

st.title("Churn Prediction")

# Sample options for categorical features (replace with your actual options)

contract_options = ['Month-to-month', 'One year', 'Two year']
senior_options = ['Yes', 'No']  # Options for SeniorCitizen
internet_options = ['DSL', 'Fiber optic', 'No']
online_security_options = ['Yes', 'No', 'No internet service']
online_backup_options = ['Yes', 'No', 'No internet service']
device_protection_options = ['Yes', 'No', 'No internet service']
tech_support_options = ['Yes', 'No', 'No internet service']
payment_options = ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']

col1, col2, col3 = st.columns(3)

with col1:
    SeniorCitizen = st.radio("Senior Citizen:", options=senior_options)
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=72)
    Contract = st.selectbox("Select Contract:", options=contract_options)
    PaymentMethod = st.selectbox("Payment Method:", options=payment_options)

with col2:
    PhoneService = st.radio("Phone Service:", options=['Yes', 'No'])
    InternetService = st.selectbox("Internet Service:", options=internet_options)
    OnlineSecurity = st.selectbox("Online Security:", options=online_security_options)
    OnlineBackup = st.selectbox("Online Backup:", options=online_backup_options)

with col3:
    DeviceProtection = st.selectbox("Device Protection:", options=device_protection_options)
    TechSupport = st.selectbox("Tech Support:", options=tech_support_options)
    PaperlessBilling = st.radio("Paperless Billing:", options=['Yes', 'No'])
    MonthlyCharges = st.number_input("Monthly Charges")
    TotalCharges = st.number_input("Total Charges")

# Example data preparation for prediction
# Encoding categorical variables

le_contract = LabelEncoder()
le_contract.fit(contract_options)
contract_encoded = le_contract.transform([Contract])[0]

le_internet = LabelEncoder()
le_internet.fit(internet_options)
internet_encoded = le_internet.transform([InternetService])[0]

le_online_security = LabelEncoder()
le_online_security.fit(online_security_options)
online_security_encoded = le_online_security.transform([OnlineSecurity])[0]

le_online_backup = LabelEncoder()
le_online_backup.fit(online_backup_options)
online_backup_encoded = le_online_backup.transform([OnlineBackup])[0]

le_device_protection = LabelEncoder()
le_device_protection.fit(device_protection_options)
device_protection_encoded = le_device_protection.transform([DeviceProtection])[0]

le_tech_support = LabelEncoder()
le_tech_support.fit(tech_support_options)
tech_support_encoded = le_tech_support.transform([TechSupport])[0]

le_payment = LabelEncoder()
le_payment.fit(payment_options)
payment_encoded = le_payment.transform([PaymentMethod])[0]

senior_encoded = 1 if SeniorCitizen == 'Yes' else 0
phone_service_encoded = 1 if PhoneService == 'Yes' else 0
paperless_billing_encoded = 1 if PaperlessBilling == 'Yes' else 0

# Creating the input list for prediction
L = [[senior_encoded, tenure,phone_service_encoded,internet_encoded,
      online_security_encoded, online_backup_encoded, device_protection_encoded,
      tech_support_encoded,contract_encoded, paperless_billing_encoded, payment_encoded, 
      MonthlyCharges, TotalCharges]]

# Example prediction logic
prediction = ""

if st.button("Predict"):
    churn = model.predict(L)
    prediction = churn[0]
    st.write(f"Predicted Churn: {'Yes' if prediction == 1 else 'No'}")
