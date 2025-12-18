import joblib
import pandas as pd

def load_model():
    model = joblib.load('C:\\Users\\yahaf\\OneDrive\\Desktop\\New folder\\Telcom-Chern-Prediction\\model\\telco.joblib')
    return model

# Example new customer
example_customer = pd.DataFrame({
    "gender": ["Female"],
    "SeniorCitizen": ["No"],
    "Partner": ["Yes"],
    "Dependents": ["Yes"],
    "tenure": [10],
    "PhoneService": ["Yes"],
    "MultipleLines": ["Yes"],
    "InternetService": ["Fiber optic"],
    "OnlineSecurity": ["No"],
    "OnlineBackup": ["No"],
    "DeviceProtection": ["No"],
    "TechSupport": ["No"],
    "StreamingTV": ["Yes"],
    "StreamingMovies": ["Yes"],
    "Contract": ["Two year"],
    "PaperlessBilling": ["Yes"],
    "PaymentMethod": ["Electronic check"],
    "MonthlyCharges": [80.0],
    "TotalCharges": [800.0]
})

model = load_model()
pred =  model.predict(example_customer)[0]
if pred == 1:
  print('Churn')
else:
  print('Not Churn')
