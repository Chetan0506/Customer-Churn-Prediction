
# Customer Churn Prediction using Machine Learning

## Overview

Customer churn is a significant issue for many businesses, as it directly impacts revenue and profitability. This project aims to predict customer churn using a machine learning model. By accurately identifying customers who are likely to churn, businesses can take proactive measures to retain them, thereby improving customer retention and revenue stability.

## Features

- **Predict Customer Churn**: Use historical data to predict whether a customer will churn (leave) or not.
- **Data Preprocessing**: Handle missing values, encode categorical variables, and normalize features.
- **Model Training**: Train multiple machine learning models and evaluate their performance.
- **Feature Importance**: Identify which features contribute most to predicting churn.
- **Deployment**: Deploy the model using a simple web interface to make predictions on new data.

## Project Structure

- **data/**: Contains the dataset used for training and testing.
- **notebooks/**: Jupyter notebooks for exploratory data analysis (EDA) and model training.
- **src/**: Source code for data processing, feature engineering, and model building.
- **models/**: Saved models and scripts for model evaluation.
- **app/**: Code for the web application to interact with the churn prediction model.
- **README.md**: This file, providing an overview and instructions for the project.

## Dataset

The dataset used in this project is the [Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn). It includes customer demographics, account information, and service usage patterns. The target variable is `Churn`, which indicates whether the customer has left within the last month.

### Key Features

- **SeniorCitizen**: Whether the customer is a senior citizen.
- **Tenure**: Number of months the customer has been with the company.
- **PhoneService**: Whether the customer has phone service.
- **InternetService**: Type of internet service.
- **OnlineSecurity**: Whether the customer has online security.
- **OnlineBackup**: Whether the customer has online backup.
- **DeviceProtection**: Whether the customer has device protection.
- **TechSupport**: Whether the customer has tech support.
- **Contract**: Type of contract (month-to-month, one year, two year).
- **PaperlessBilling**: Whether the customer uses paperless billing.
- **PaymentMethod**: Payment method.
- **MonthlyCharges**: Monthly charges for the customer.
- **TotalCharges**: Total charges for the customer.
- **Churn**: Whether the customer churned.

## Models and Techniques

Several machine learning algorithms were explored for this project:

- **Logistic Regression**: Simple and interpretable model.
- **Decision Tree**: Non-linear model capturing complex interactions.
- **Random Forest**: Ensemble model reducing variance.
- **Gradient Boosting**: Boosting technique for higher accuracy.
- **Support Vector Machine (SVM)**: Classifies with high dimensional decision boundaries.

## Model Evaluation

Models were evaluated using several metrics:

- **Accuracy**: Overall correctness of the model.
- **Precision**: Proportion of positive identifications that were actually correct.
- **Recall**: Proportion of actual positives that were correctly identified.
- **F1 Score**: Harmonic mean of precision and recall.
- **ROC-AUC**: Area under the Receiver Operating Characteristic curve.

## Results

The Gradient Boosting model achieved the highest performance with an accuracy of 85% and an AUC-ROC score of 0.91. Feature importance analysis indicated that `Contract`, `TotalCharges`, and `MonthlyCharges` were significant predictors of churn.

