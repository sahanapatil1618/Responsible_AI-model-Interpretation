         ** Responsible AI - Loan Prediction System**

      Project Overview

This project is a Machine Learning-based Responsible AI system that predicts whether a loan application will be approved or rejected based on applicant details. The system also includes explainability using SHAP (SHapley Additive exPlanations) and is deployed using a Flask API for real-time predictions.

            Objective

The main objective of this project is to build an AI system that:
- Predicts loan approval status
- Ensures transparency using Responsible AI techniques
- Provides explainable AI outputs using SHAP
- Deploys the model as a real-time web AP

         Dataset Description

The dataset contains applicant financial and personal details such as:
- Age
- Gender
- Education
- Person Income
- Employment Experience
- Home Ownership
- Loan Amount
- Loan Intent
- Loan Interest Rate
- Credit History
- Credit Score
- Previous Loan Status

Target variable:
- Loan Status (0 = Rejected, 1 = Approved)



           Machine Learning Model

- Algorithm Used: Random Forest Classifier
- Data Preprocessing: Label Encoding, Train-Test Split
- Evaluation Metric: Accuracy Score



          
        Responsible AI (Explainability)

To ensure transparency in predictions, SHAP (SHapley Additive exPlanations) was used to:
- Identify important features affecting loan decisions
- Explain model predictions visually



            Deployment (Flask API)

The trained model is deployed using Flask to provide real-time predictions.

             API Endpoints:

- `/` → Home route
- `/predict` → Accepts JSON input and returns loan prediction

              Example Input:
```json
{
  "Age": 25,
  "Gender": 1,
  "Education": 0,
  "Person Income": 50000,
  "Employee Experience": 2,
  "Home Onwership": 1,
  "Loan Amount": 10000,
  "Loan Intent": 2,
  "Loan interest Rate": 12.5,
  "Loan percentage": 0.4,
  "Credit History": 3,
  "Credit Score": 650,
  "Previous Loan": 0
}
            
            output

{
  "Loan_Status": 1
}